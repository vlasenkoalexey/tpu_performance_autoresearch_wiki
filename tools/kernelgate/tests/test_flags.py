"""4-leg flag-fairness harness — the 37k both-flagged false-1.00x regression.

2026-07-17 incident: the 37k worker exported the flag in its shell, then
"co-measured naive vs flagged" — both legs ran under the flag, the ratio was
1.00x by construction, and a real 1.49x flag win was self-reported as nothing.
These tests pin: (a) the pure ratio/trap analysis, (b) one end-to-end 4-leg
run on the CPU backend (real subprocesses, fresh compilation-cache dirs) that
must emit the trap warning for a same-graph invocation.
"""
import json
import os
import textwrap

import pytest

from kernelgate import flags

TINY = '''
import jax
import jax.numpy as jnp

CONFIG = {"name": "tiny_matmul", "n": 64}

def create_inputs(dtype=jnp.float32):
    key = jax.random.key(42)
    k1, k2 = jax.random.split(key)
    n = CONFIG["n"]
    return jax.random.normal(k1, (n, n), dtype), jax.random.normal(k2, (n, n), dtype)

def workload(a, b):
    return a @ b
'''

CAND = TINY.replace("def workload(", "def workload_cand(")


def _legs(nd, nf, cd, cf):
    return {"naive_default": {"p50_ms": nd}, "naive_flagged": {"p50_ms": nf},
            "cand_default": {"p50_ms": cd}, "cand_flagged": {"p50_ms": cf}}


# ------------------------------------------------------------- pure analysis

def test_ratios_both_framings():
    ratios, warnings, anomalies = flags.analyze_legs(
        _legs(nd=1.5, nf=1.0, cd=1.5, cf=0.5), same_graph=False,
        flag_key="LIBTPU_INIT_ARGS", parent_value=None, flag_value="--x=1")
    assert ratios["flag_only_ratio"] == pytest.approx(1.5)
    assert ratios["kernel_cell_ratio"] == pytest.approx(2.0)
    assert ratios["end_to_end_ratio"] == pytest.approx(3.0)
    assert not warnings and not anomalies


def test_same_graph_emits_trap_warning():
    """The 37k invocation: same graph, both flagged -> the cell ratio is
    1.00x by construction; the warning must say so and name the honest ratio."""
    ratios, warnings, _ = flags.analyze_legs(
        _legs(nd=1.49, nf=1.0, cd=1.49, cf=1.0), same_graph=True,
        flag_key="LIBTPU_INIT_ARGS", parent_value=None, flag_value="--x=1")
    assert ratios["kernel_cell_ratio"] == pytest.approx(1.0)
    assert ratios["flag_only_ratio"] == pytest.approx(1.49)
    assert any("SAME-GRAPH TRAP" in w and "flag_only_ratio = 1.490x" in w
               for w in warnings), warnings


def test_flag_already_exported_is_anomaly():
    """The 37k shell state: flag exported in the parent env -> the '-default'
    legs are not default -> anomaly, not a silent 1.00x."""
    _, _, anomalies = flags.analyze_legs(
        _legs(1.0, 1.0, 1.0, 1.0), same_graph=False,
        flag_key="LIBTPU_INIT_ARGS", parent_value="--x=1", flag_value="--x=1")
    assert any("NOT default" in a for a in anomalies), anomalies


def test_flag_key_set_to_other_value_warns():
    _, warnings, anomalies = flags.analyze_legs(
        _legs(1.0, 1.0, 1.0, 1.0), same_graph=False,
        flag_key="XLA_FLAGS", parent_value="--y=2", flag_value="--x=1")
    assert not anomalies
    assert any("already set in the parent environment" in w for w in warnings)


def test_parse_flag():
    assert flags.parse_flag(
        "LIBTPU_INIT_ARGS=--xla_tpu_scoped_vmem_limit_kib=131072"
    ) == ("LIBTPU_INIT_ARGS", "--xla_tpu_scoped_vmem_limit_kib=131072")
    with pytest.raises(ValueError):
        flags.parse_flag("no_equals_sign")


# ---------------------------------------------------------------- end-to-end
# The e2e tests exercise the subprocess plumbing, which is backend-agnostic —
# pin the legs to the CPU backend so a KGATE_TPU=1 session's legs don't fight
# the pytest process for its chip (one process per chip).

@pytest.fixture
def cpu_legs(monkeypatch):
    monkeypatch.setenv("JAX_PLATFORMS", "cpu")


def test_flags_e2e_same_graph_trap(tmp_path, cpu_legs):
    """37k-style invocation end-to-end: baseline == candidate module. Four
    fresh-process legs, per-flag-value cache dirs, trap warning, ratio ~1x."""
    p = tmp_path / "baseline.py"
    p.write_text(textwrap.dedent(TINY))
    rep = flags.run_flags(str(p), str(p), "KGATE_TEST_DUMMY_FLAG=1",
                          warmup=1, n=3)
    assert rep["status"] == "PASS", rep.get("exception")
    assert rep["same_graph"]
    assert any("SAME-GRAPH TRAP" in w for w in rep["warnings"]), rep["warnings"]
    assert set(rep["legs"]) == set(flags.LEG_NAMES)
    # all four legs timed identical inputs
    assert len({leg["inputs"]["combined"] for leg in rep["legs"].values()}) == 1
    # fresh compilation cache dir per flag value
    dirs = rep["compilation_cache_dirs"]
    assert dirs["default"] != dirs["flagged"]
    for name, leg in rep["legs"].items():
        expected = dirs["flagged"] if name.endswith("_flagged") else dirs["default"]
        assert leg["env"]["env"]["JAX_COMPILATION_CACHE_DIR"] == expected, name
    # a no-op env flag: both framing ratios ~1x, reported explicitly
    assert 0.5 < rep["ratios"]["flag_only_ratio"] < 2.0
    assert 0.5 < rep["ratios"]["kernel_cell_ratio"] < 2.0


def test_flags_e2e_distinct_candidate_no_trap(tmp_path, cpu_legs):
    b = tmp_path / "baseline.py"
    b.write_text(textwrap.dedent(TINY))
    c = tmp_path / "cand.py"
    c.write_text(textwrap.dedent(CAND))
    rep = flags.run_flags(str(b), str(c), "KGATE_TEST_DUMMY_FLAG=1",
                          warmup=1, n=3)
    assert rep["status"] == "PASS", rep.get("exception")
    assert not rep["same_graph"]
    assert not any("SAME-GRAPH TRAP" in w for w in rep["warnings"])
    assert rep["candidate"]["entry"] == "workload_cand"


def test_flags_leg_failure_is_fail_with_detail(tmp_path, cpu_legs):
    b = tmp_path / "baseline.py"
    b.write_text("def create_inputs():\n    raise RuntimeError('boom-inputs')\n")
    rep = flags.run_flags(str(b), str(b), "KGATE_TEST_DUMMY_FLAG=1", warmup=1, n=2)
    assert rep["status"] == "FAIL"
    assert "boom-inputs" in rep.get("exception", "")
