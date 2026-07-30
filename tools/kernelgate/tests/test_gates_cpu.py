"""End-to-end gate plumbing on tiny synthetic problems — CPU backend.

These exercise the full parity / coverage / sweep / measure pipelines with
small shapes so the machinery is verified anywhere; the real kernels are
covered by the TPU suite (test_tpu_gates.py).
"""
import textwrap

import pytest

from kernelgate import coverage, parity, protocol, sweep, timing

BASELINE = '''
import jax
import jax.numpy as jnp

CONFIG = {"name": "tiny_causal_mha", "batch": 1, "seq_len": 64,
          "num_heads": 2, "head_dim": 16}

def create_inputs(dtype=jnp.bfloat16):
    key = jax.random.key(42)
    k1, k2, k3 = jax.random.split(key, 3)
    B, H = CONFIG["batch"], CONFIG["num_heads"]
    S, D = CONFIG["seq_len"], CONFIG["head_dim"]
    q = jax.random.normal(k1, (B, H, S, D), dtype)
    k = jax.random.normal(k2, (B, H, S, D), dtype) * 0.5
    v = jax.random.normal(k3, (B, H, S, D), dtype) * 0.5
    return q, k, v

def workload(q, k, v):
    S = q.shape[-2]
    attn = jnp.einsum("bhqd,bhkd->bhqk", q, k) * (q.shape[-1] ** -0.5)
    mask = jnp.tril(jnp.ones((S, S)))
    attn = jnp.where(mask, attn, -1e30)
    attn = jax.nn.softmax(attn, axis=-1)
    return jnp.einsum("bhqk,bhkd->bhqd", attn, v)
'''

GOOD_CAND = BASELINE.replace("def workload(", "def workload_cand(")

# skips the second half of the keys — the 50%-coverage class
HALF_COVERAGE_CAND = '''
import jax
import jax.numpy as jnp

def workload_cand(q, k, v):
    S = q.shape[-2]
    half = S // 2
    k = k[..., :half, :]
    v = v[..., :half, :]
    attn = jnp.einsum("bhqd,bhkd->bhqk", q, k) * (q.shape[-1] ** -0.5)
    mask = jnp.tril(jnp.ones((S, S)))[:, :half]
    attn = jnp.where(mask, attn, -1e30)
    attn = jax.nn.softmax(attn, axis=-1)
    return jnp.einsum("bhqk,bhkd->bhqd", attn, v)
'''

# double softmax scale — semantics bug, parity must fail
DOUBLE_SCALE_CAND = BASELINE.replace(
    'attn = jnp.einsum("bhqd,bhkd->bhqk", q, k) * (q.shape[-1] ** -0.5)',
    'attn = jnp.einsum("bhqd,bhkd->bhqk", q, k) * (q.shape[-1] ** -1.0)').replace(
    "def workload(", "def workload_cand(")

CRASHING_CAND = '''
def workload_cand(q, k, v):
    raise RuntimeError("kaboom: does not lower")
'''

# accepts block-size params for sweep; bad param value crashes
SWEEPABLE_CAND = '''
import jax
import jax.numpy as jnp

def workload_cand(q, k, v, bq=32, bk=32):
    assert bq in (16, 32), "unsupported bq"
    S = q.shape[-2]
    attn = jnp.einsum("bhqd,bhkd->bhqk", q, k) * (q.shape[-1] ** -0.5)
    mask = jnp.tril(jnp.ones((S, S)))
    attn = jnp.where(mask, attn, -1e30)
    attn = jax.nn.softmax(attn, axis=-1)
    return jnp.einsum("bhqk,bhkd->bhqd", attn, v)
'''


def _mod(tmp_path, name, src):
    p = tmp_path / name
    p.write_text(textwrap.dedent(src))
    return protocol.load_module(str(p))


@pytest.fixture
def baseline_mod(tmp_path):
    return _mod(tmp_path, "baseline.py", BASELINE)


def test_parity_good_passes(tmp_path, baseline_mod):
    cand = _mod(tmp_path, "cand_good.py", GOOD_CAND)
    rep = parity.run_parity(baseline_mod, cand, seeds=(42, 43))
    assert rep["status"] == "PASS", rep.get("exception")
    # identical implementation -> ratio ~1x floor
    for rec in rep["seeds"].values():
        assert rec["gate"]["max_abs_ratio_vs_floor"] <= 1.001


def test_parity_double_scale_fails(tmp_path, baseline_mod):
    cand = _mod(tmp_path, "cand_scale.py", DOUBLE_SCALE_CAND)
    rep = parity.run_parity(baseline_mod, cand, seeds=(42,))
    assert rep["status"] == "FAIL"


def test_parity_crash_is_fail_with_traceback(tmp_path, baseline_mod):
    cand = _mod(tmp_path, "cand_crash.py", CRASHING_CAND)
    rep = parity.run_parity(baseline_mod, cand, seeds=(42,))
    assert rep["status"] == "FAIL"
    assert "kaboom" in rep.get("exception", "")


def test_parity_chunked_oracle_matches_unchunked(tmp_path, baseline_mod):
    cand = _mod(tmp_path, "cand_good2.py", GOOD_CAND)
    rep_full = parity.run_parity(baseline_mod, cand, seeds=(42,))
    rep_chunk = parity.run_parity(baseline_mod, cand, seeds=(42,),
                                  chunk={0: 0, 1: 0, 2: 0})
    a = rep_full["seeds"]["42"]["floor_baseline_vs_oracle"]["max_abs"]
    b = rep_chunk["seeds"]["42"]["floor_baseline_vs_oracle"]["max_abs"]
    assert a == pytest.approx(b, rel=1e-6)


def test_parity_scale_probes_run(tmp_path, baseline_mod):
    cand = _mod(tmp_path, "cand_good3.py", GOOD_CAND)
    rep = parity.run_parity(baseline_mod, cand, seeds=(42,), scale_probes=(4.0,),
                            scale_input=1)
    assert rep["status"] == "PASS", rep.get("exception")
    assert "x4" in rep["scale_probes"]


def test_coverage_good_passes(tmp_path, baseline_mod):
    from kernelgate.specs import causal_blocks
    cand = _mod(tmp_path, "cand_good4.py", GOOD_CAND)
    rep = coverage.run_coverage(baseline_mod, cand, causal_blocks)
    assert rep["status"] == "PASS", rep
    assert rep["n_fail"] == 0


def test_coverage_half_kernel_fails(tmp_path, baseline_mod):
    from kernelgate.specs import causal_blocks
    cand = _mod(tmp_path, "cand_half.py", HALF_COVERAGE_CAND)
    rep = coverage.run_coverage(baseline_mod, cand, causal_blocks)
    assert rep["status"] == "FAIL"
    # the second-half k-blocks must be the failing probes
    failing = [p["name"] for p in rep["probes"] if p["status"] == "FAIL"]
    assert any("vblock[32:" in n or "vblock[40:" in n or "vblock[48:" in n
               or "vblock[56:" in n for n in failing), failing


def test_measure_runs_and_checks(tmp_path, baseline_mod):
    cand = _mod(tmp_path, "cand_good5.py", GOOD_CAND)
    rep = timing.run_measure(baseline_mod, cand, warmup=2, n_min=5, n_max=8,
                             se_target=1e-9)  # force n_max path
    assert rep["timing"]["pooled"]["candidate"]["n"] == 16  # 8 per ordering
    assert rep["checks"]["input_mutation"]["ok"]
    assert rep["checks"]["candidate_ran_first"]
    assert rep["checks"]["output_finite"]


def test_sweep_gates_and_argmin(tmp_path, baseline_mod):
    cand = _mod(tmp_path, "cand_sweep.py", SWEEPABLE_CAND)
    rep = sweep.run_sweep(baseline_mod, cand, "bq=16,32,64", n_min=3, n_max=5,
                          warmup=1)
    by_status = {}
    for g in rep["grid"]:
        by_status.setdefault(g["status"], []).append(g["params"]["bq"])
    assert 64 in by_status.get("ERROR", []), rep["grid"]  # assert fires -> ERROR row
    assert set(by_status.get("OK", [])) == {16, 32}
    assert rep["argmin"]["params"]["bq"] in (16, 32)


def test_sweep_param_parsing():
    grid = sweep.parse_params("bq=512,1024,2048;bk=128,256,512")
    assert len(grid) == 9
    assert grid[0] == {"bq": 512, "bk": 128}
    assert all(isinstance(v, int) for g in grid for v in g.values())
    assert sweep.parse_params("x=1.5") == [{"x": 1.5}]
    assert sweep.parse_params("mode=fast,slow") == [{"mode": "fast"}, {"mode": "slow"}]
