"""fp64-oracle escalation — the 21k HIGHEST-baseline false-FAIL regression.

2026-07-16 incident: the 21k baseline computes in exact fp32 (Precision.
HIGHEST), so kgate's fp32-recompute oracle was bit-identical to the baseline,
the floor collapsed to zero, and the 2.0x floor-normalized gate degenerated
to a ~1e-6 ABSOLUTE tolerance — false-FAILing a candidate the independent
verifier confirmed correct (more accurate than the naive vs fp64). These
tests pin the fix: floor ~0 (or a Precision.HIGHEST sniff) escalates the
oracle to a float64 recompute so the floor is non-zero.

CPU backend; tiny colsum shapes (the 21k family shape class).
"""
import textwrap

import pytest

from kernelgate import parity, protocol

# HIGHEST-class baseline: fp32 inputs + sequential fp32 accumulation. The
# fp32-cast oracle re-runs the identical graph on identical values -> floor
# is exactly 0 (the 21k signature). The sequential scan gives the baseline a
# real (non-trivial) fp32 rounding error vs the fp64 truth.
HIGHEST_BASELINE = '''
import jax
import jax.numpy as jnp

CONFIG = {"name": "highest_colsum", "rows": 4096, "cols": 128}

def create_inputs(dtype=jnp.float32):
    key = jax.random.key(42)
    return (jax.random.normal(key, (CONFIG["rows"], CONFIG["cols"]), dtype),)

def workload(x):
    # exact-fp32 sequential column sum (dtype-polymorphic: f64 in -> f64 out)
    def step(carry, row):
        return carry + row, None
    out, _ = jax.lax.scan(step, jnp.zeros((x.shape[1],), x.dtype), x)
    return out
'''

# Correct kernel-scale rewrite (tree-reduction colsum): differs from the
# baseline by fp32 accumulation-order error only — MORE accurate vs fp64,
# exactly the verified-correct 21k candidate class.
CORRECT_CAND = '''
import jax.numpy as jnp

def workload_cand(x):
    return jnp.sum(x, axis=0)
'''

# Genuinely wrong: drops half the rows (coverage-class semantics bug).
WRONG_CAND = '''
import jax.numpy as jnp

def workload_cand(x):
    return jnp.sum(x[: x.shape[0] // 2], axis=0)
'''

HIGHEST_SNIFF_SRC = '''
import jax
import jax.numpy as jnp

CONFIG = {}

def create_inputs(dtype=jnp.bfloat16):
    key = jax.random.key(42)
    k1, k2 = jax.random.split(key)
    a = jax.random.normal(k1, (64, 64), dtype)
    b = jax.random.normal(k2, (64, 64), dtype)
    return a, b

def workload(a, b):
    return jnp.dot(a, b, precision=jax.lax.Precision.HIGHEST,
                   preferred_element_type=jnp.float32)
'''


def _mod(tmp_path, name, src):
    p = tmp_path / name
    p.write_text(textwrap.dedent(src))
    return protocol.load_module(str(p))


@pytest.fixture
def highest_mod(tmp_path):
    return _mod(tmp_path, "baseline.py", HIGHEST_BASELINE)


def test_highest_baseline_correct_candidate_passes(tmp_path, highest_mod):
    """The 21k regression: correct candidate + HIGHEST baseline must PASS."""
    cand = _mod(tmp_path, "cand_correct.py", CORRECT_CAND)
    rep = parity.run_parity(highest_mod, cand, seeds=(42, 43))
    assert rep["status"] == "PASS", rep.get("exception")
    for rec in rep["seeds"].values():
        assert rec["oracle_used"] == "fp64", rec
        assert rec["floor_baseline_vs_oracle"]["max_abs"] > 0  # non-zero floor
        assert "fp32 floor" in rec["oracle_reason"]
    assert rep["oracle"]["used"] == ["fp64"]


def test_highest_baseline_false_fails_without_escalation(tmp_path, highest_mod):
    """Pin the v0.1 bug: forcing the fp32 oracle reproduces the false FAIL."""
    cand = _mod(tmp_path, "cand_correct2.py", CORRECT_CAND)
    rep = parity.run_parity(highest_mod, cand, seeds=(42,), oracle="fp32")
    assert rep["status"] == "FAIL"  # the 21k incident behavior
    rec = rep["seeds"]["42"]
    assert rec["oracle_used"] == "fp32"
    assert rec["gate"]["floor_was_zero"]


def test_highest_baseline_wrong_candidate_still_fails(tmp_path, highest_mod):
    cand = _mod(tmp_path, "cand_wrong.py", WRONG_CAND)
    rep = parity.run_parity(highest_mod, cand, seeds=(42,))
    assert rep["status"] == "FAIL"
    rec = rep["seeds"]["42"]
    assert rec["oracle_used"] == "fp64"          # graded on the fixed oracle
    assert not rec["gate"]["ok"]


def test_healthy_bf16_baseline_keeps_fp32_oracle(tmp_path):
    """Normal bf16 workloads have a real fp32 floor — no escalation."""
    from tests.test_gates_cpu import BASELINE, GOOD_CAND
    base = _mod(tmp_path, "baseline.py", BASELINE)
    cand = _mod(tmp_path, "cand_good.py", GOOD_CAND)
    rep = parity.run_parity(base, cand, seeds=(42,))
    assert rep["status"] == "PASS", rep.get("exception")
    assert rep["seeds"]["42"]["oracle_used"] == "fp32"
    assert rep["oracle"]["used"] == ["fp32"]


def test_forced_fp64_oracle_mode(tmp_path):
    from tests.test_gates_cpu import BASELINE, GOOD_CAND
    base = _mod(tmp_path, "baseline.py", BASELINE)
    cand = _mod(tmp_path, "cand_good.py", GOOD_CAND)
    rep = parity.run_parity(base, cand, seeds=(42,), oracle="fp64")
    assert rep["status"] == "PASS", rep.get("exception")
    assert rep["seeds"]["42"]["oracle_used"] == "fp64"


def test_detect_highest_precision_sniff(tmp_path):
    mod = _mod(tmp_path, "highest_dot.py", HIGHEST_SNIFF_SRC)
    assert parity.detect_highest_precision(mod)
    from tests.test_gates_cpu import BASELINE
    plain = _mod(tmp_path, "plain.py", BASELINE)
    assert not parity.detect_highest_precision(plain)


def test_sniffed_highest_escalates_even_with_nonzero_floor(tmp_path):
    """Precision.HIGHEST in the source forces fp64 regardless of the floor."""
    mod = _mod(tmp_path, "baseline.py", HIGHEST_SNIFF_SRC)
    cand_src = HIGHEST_SNIFF_SRC.replace("def workload(", "def workload_cand(")
    cand = _mod(tmp_path, "cand_same.py", cand_src)
    rep = parity.run_parity(mod, cand, seeds=(42,))
    assert rep["status"] == "PASS", rep.get("exception")
    rec = rep["seeds"]["42"]
    assert rec["oracle_used"] == "fp64"
    assert "Precision.HIGHEST" in rec["oracle_reason"]


def test_sweep_inherits_fp64_escalation(tmp_path, highest_mod):
    from kernelgate import sweep
    cand = _mod(tmp_path, "cand_sweepable.py", '''
import jax.numpy as jnp

def workload_cand(x, chunks=2):
    parts = jnp.split(x, chunks, axis=0)
    out = jnp.sum(parts[0], axis=0)
    for p in parts[1:]:
        out = out + jnp.sum(p, axis=0)
    return out
''')
    rep = sweep.run_sweep(highest_mod, cand, "chunks=2,4", n_min=3, n_max=5, warmup=1)
    assert rep["status"] == "PASS", rep.get("exception")
    assert rep["oracle_used"] == "fp64"
    assert all(g["status"] == "OK" for g in rep["grid"]), rep["grid"]
