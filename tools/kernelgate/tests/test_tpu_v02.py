"""v0.2 gates on a real TPU chip — tiny shapes, fast.

Run on a TPU host with:  KGATE_TPU=1 python -m pytest tests/test_tpu_v02.py -v
(single-chip env + flock per the repo's chip discipline).

Covers the TPU-specific seams of the v0.2 features:
  - fp64-oracle escalation from inside a TPU process (the fp64 recompute must
    hop to the host CPU backend — TPUs have no f64);
  - `kgate fit` parsing a REAL XLA RESOURCE_EXHAUSTED out of an oversized
    allocation (not a synthetic message);
  - the declarative head-skip battery on-device (the v042 incident class).
"""
import textwrap

import pytest

from kernelgate import coverage, fit, parity, protocol

pytestmark = pytest.mark.tpu

HIGHEST_BASELINE = '''
import jax
import jax.numpy as jnp

CONFIG = {"name": "highest_colsum_tpu", "rows": 2048, "cols": 128}

def create_inputs(dtype=jnp.float32):
    key = jax.random.key(42)
    return (jax.random.normal(key, (CONFIG["rows"], CONFIG["cols"]), dtype),)

def workload(x):
    # exact-fp32 sequential column sum; fp32-recompute oracle == baseline
    def step(carry, row):
        return carry + row, None
    out, _ = jax.lax.scan(step, jnp.zeros((x.shape[1],), x.dtype), x)
    return out
'''

CORRECT_CAND = '''
import jax.numpy as jnp

def workload_cand(x):
    return jnp.sum(x, axis=0)
'''

# ~64 GiB f32 OUTPUT -> guaranteed RESOURCE_EXHAUSTED on any v5e/v6e chip.
# (The buffer must be the output — a zeros+reduce intermediate gets fused
# away by XLA and never materializes.)
OOM_CAND = '''
import jax
import jax.numpy as jnp

CONFIG = {"name": "oom_probe"}

def create_inputs(dtype=jnp.float32):
    key = jax.random.key(42)
    return (jax.random.normal(key, (128,), dtype),)

def workload_cand(x, n=128):
    return jnp.zeros((n, n), jnp.float32) + x[:1]
'''

PERHEAD_BASELINE = '''
import jax
import jax.numpy as jnp

CONFIG = {"name": "tiny_perhead_tpu", "heads": 4}

def create_inputs(dtype=jnp.float32):
    key = jax.random.key(42)
    k1, k2 = jax.random.split(key)
    return (jax.random.normal(k1, (4, 16, 8), dtype),
            jax.random.normal(k2, (4, 8, 8), dtype))

def workload(x, w):
    return jnp.einsum("hsd,hde->hse", x, w)
'''

HEAD_SKIP_CAND = '''
import jax.numpy as jnp

def workload_cand(x, w):
    out = jnp.zeros((x.shape[0], x.shape[1], w.shape[2]), x.dtype)
    return out.at[0].set(x[0] @ w[0])
'''

PERHEAD_SPEC = {"axes": [{"name": "head", "input": 0, "size": 4,
                          "input_slice": "[i]", "output_slice": "[i]"}]}


def _mod(tmp_path, name, src):
    p = tmp_path / name
    p.write_text(textwrap.dedent(src))
    return protocol.load_module(str(p))


def test_fp64_escalation_from_tpu_process(tmp_path):
    """21k class on-device: fp32 floor collapses to 0 on the TPU leg, the
    oracle escalates to fp64 (executed on the host CPU backend), and the
    correct candidate PASSes instead of false-FAILing."""
    base = _mod(tmp_path, "baseline.py", HIGHEST_BASELINE)
    cand = _mod(tmp_path, "cand_correct.py", CORRECT_CAND)
    rep = parity.run_parity(base, cand, seeds=(42,))
    assert rep["status"] == "PASS", rep.get("exception")
    rec = rep["seeds"]["42"]
    assert rec["oracle_used"] == "fp64", rec
    assert rec["floor_baseline_vs_oracle"]["max_abs"] > 0


def test_fit_parses_real_hbm_oom(tmp_path):
    """A config sized past HBM yields a parsed row (real XLA error text);
    a small config fits; the sweep survives both."""
    cand = _mod(tmp_path, "cand_oom.py", OOM_CAND)
    rep = fit.run_fit(cand, [{"n": 256}, {"n": 131072}], run_once=True)
    assert rep["status"] == "PASS", rep.get("exception")   # sweep never crashes
    rows = {r["config"]["n"]: r for r in rep["rows"]}
    assert rows[256]["fits"]
    oom = rows[131072]                                     # 64 GiB > any HBM
    assert not oom["fits"]
    assert oom["error_class"] in ("xla_hbm", "resource_exhausted"), oom
    assert oom["raw_line"], oom
    if oom["limit_bytes"] is not None:                     # parsed numbers when present
        assert oom["requested_bytes"] > oom["limit_bytes"]


def test_declarative_head_skip_on_device(tmp_path):
    """v042 class on-device: 1-of-4-heads kernel FAILs with heads named."""
    base = _mod(tmp_path, "baseline.py", PERHEAD_BASELINE)
    cand = _mod(tmp_path, "cand_skip.py", HEAD_SKIP_CAND)
    rep = coverage.run_coverage(base, cand, PERHEAD_SPEC)
    assert rep["status"] == "FAIL", rep.get("exception")
    assert rep["axes"][0]["failing_slots"] == [1, 2, 3]
    assert any("all-zero" in v for v in rep["violations"]), rep["violations"]
