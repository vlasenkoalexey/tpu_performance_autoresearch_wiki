"""kgate verify — pure-CPU coverage: HLO assertions, receipt schema, and the
end-to-end pipeline on the CPU backend (fresh children inherit JAX_PLATFORMS
from conftest, so measure/parity legs run on CPU).
"""
import json
import os
import textwrap

import pytest

from kernelgate import hlo, receipt

HLO_SAMPLE = """\
HloModule jit_workload, entry_computation_layout={(bf16[4,64,4096,128]{...})}

ENTRY %main.42 (p0: bf16[4,64,4096,128]) -> bf16[4,64,4096,128] {
  %p0 = bf16[4,64,4096,128] parameter(0)
  %cc = bf16[4,64,4096,128] custom-call(%p0), custom_call_target="tpu_custom_call"
  %fused = bf16[4,64,4096,4096] fusion(%p0), kind=kOutput
  ROOT %out = bf16[4,64,4096,128] add(%cc, %cc)
}
"""


# ---------------------------------------------------------------- hlo module
def test_hlo_assertions_pass_and_fail():
    a = hlo.run_assertions(HLO_SAMPLE,
                           expect_patterns=["tpu_custom_call"],
                           forbid_patterns=["sort\\("])
    assert a["status"] == "PASS"
    assert a["custom_call_count"] == 1  # 'custom-call(' + target string is 1 site line

    a = hlo.run_assertions(HLO_SAMPLE, expect_patterns=["segment_sum"])
    assert a["status"] == "FAIL"
    assert not a["checks"][0]["ok"]


def test_hlo_forbid_shape_matches_adjacent_dims_only():
    # [4096,4096] IS present (the fusion output)
    a = hlo.run_assertions(HLO_SAMPLE, forbid_shapes=["4096,4096"])
    assert a["status"] == "FAIL"
    # boundary safety: 14096 must not satisfy 4096-anchored specs
    text = "ROOT %x = f32[1,14096] parameter(0)"
    a = hlo.run_assertions(text, forbid_shapes=["4096"])
    assert a["status"] == "PASS"
    a = hlo.run_assertions(text, forbid_shapes=["14096"])
    assert a["status"] == "FAIL"


def test_hlo_expect_custom_calls_exact():
    a = hlo.run_assertions(HLO_SAMPLE, expect_custom_calls=1)
    assert a["status"] == "PASS"
    a = hlo.run_assertions(HLO_SAMPLE, expect_custom_calls=2)
    assert a["status"] == "FAIL"
    assert "found 1" in a["checks"][0]["detail"]


def test_hlo_newest_module_empty_dir(tmp_path):
    assert hlo.newest_module(str(tmp_path)) is None
    f = tmp_path / "module_0001.jit_x.after_optimizations.txt"
    f.write_text("ENTRY {}")
    assert hlo.newest_module(str(tmp_path)) == str(f)


# ------------------------------------------------------------ receipt schema
def test_verify_receipt_schema_and_self_hash(tmp_path):
    rep = {
        "cmd": "verify", "mode": "screen", "status": "PASS",
        "baseline": {"path": "/b.py", "entry": "workload"},
        "candidate": {"path": "/c.py", "entry": None},
        "gates": {"measure": {"ok": True, "detail": ""},
                  "parity": {"ok": True, "detail": ""}},
        "speedup": 1.5, "p50_ms": {"baseline": 3.0, "candidate": 2.0},
        "legs": {"measure": {"status": "PASS"}, "parity": {"status": "PASS"}},
        "hlo_audit": {"status": "PASS", "custom_call_count": 1,
                      "checks": [{"name": "expect-pattern:x", "ok": True,
                                  "detail": ""}]},
        "artifact_dir": "/tmp/a", "compilation_cache_dir": "/tmp/c",
        "anomalies": [],
    }
    path = str(tmp_path / "receipt.json")
    receipt.write(rep, path, argv=["verify"])
    with open(path) as f:
        r = json.load(f)
    assert r["cmd"] == "verify" and r["verdict"] == "PASS"
    assert r["speedup"] == 1.5
    assert r["gates"] == {"measure": True, "parity": True}
    assert r["hlo_audit"]["custom_call_count"] == 1
    # self-hash must detect tampering
    assert receipt.self_hash({k: v for k, v in r.items()
                              if k != receipt.SELF_HASH_FIELD}) == \
        r[receipt.SELF_HASH_FIELD]
    r["speedup"] = 9.9
    assert receipt.self_hash({k: v for k, v in r.items()
                              if k != receipt.SELF_HASH_FIELD}) != \
        r[receipt.SELF_HASH_FIELD]


# ------------------------------------------------------- end-to-end (CPU jax)
BASELINE_SRC = """
import jax.numpy as jnp
import jax

def create_inputs(seed=0, dtype=jnp.float32):
    k = jax.random.PRNGKey(seed)
    x = jax.random.normal(k, (64, 64), dtype)
    return (x,)

def workload(x):
    return jnp.tanh(x) @ x.T
"""

GOOD_CAND_SRC = """
import jax.numpy as jnp

def optimized(x):
    return jnp.tanh(x) @ x.T
"""

BAD_CAND_SRC = """
import jax.numpy as jnp

def optimized(x):
    return jnp.tanh(x) @ x.T * 1.5   # wrong result
"""


def _write(tmp_path, name, src):
    p = tmp_path / name
    p.write_text(textwrap.dedent(src))
    return str(p)


def test_verify_screen_end_to_end_cpu(tmp_path):
    from kernelgate import verify
    base = _write(tmp_path, "baseline.py", BASELINE_SRC)
    cand = _write(tmp_path, "cand.py", GOOD_CAND_SRC)
    rep = verify.run_verify(
        base, cand, mode="screen", dtype="float32",
        artifact_dir=str(tmp_path / "art"),
        family="testfam-cpu", fresh_cache=True,
        warmup=1, n_min=3, n_max=5, child_timeout=600)
    assert rep["status"] in ("PASS", "ANOMALY"), json.dumps(rep, indent=1,
                                                            default=str)[:4000]
    assert rep["gates"]["measure"]["ok"] and rep["gates"]["parity"]["ok"]
    assert rep["speedup"] is not None
    # dump legs ran; on CPU an XLA text dump is still emitted
    assert "dump_cand" in rep["legs"]


def test_verify_catches_parity_break_cpu(tmp_path):
    from kernelgate import verify
    base = _write(tmp_path, "baseline.py", BASELINE_SRC)
    cand = _write(tmp_path, "cand_bad.py", BAD_CAND_SRC)
    rep = verify.run_verify(
        base, cand, mode="screen", dtype="float32",
        artifact_dir=str(tmp_path / "art"),
        family="testfam-cpu-bad", fresh_cache=True,
        warmup=1, n_min=3, n_max=5, child_timeout=600)
    assert rep["status"] == "FAIL"
    assert not rep["gates"]["parity"]["ok"]


def test_verify_bar_gate_and_reproduction(tmp_path):
    from kernelgate import verify
    base = _write(tmp_path, "baseline.py", BASELINE_SRC)
    cand = _write(tmp_path, "cand.py", GOOD_CAND_SRC)
    rep = verify.run_verify(
        base, cand, mode="screen", dtype="float32",
        artifact_dir=str(tmp_path / "art"),
        family="testfam-cpu2", fresh_cache=True,
        bar_speedup=50.0,          # same graph — cannot be 50x faster
        author_claim_p50=1e-6,     # absurd claim -> >2x divergence
        warmup=1, n_min=3, n_max=5, child_timeout=600)
    assert not rep["gates"]["falsification_bar"]["ok"]
    assert "DIVERGES" in rep["reproduction"]["verdict"]

def test_speedup_role_labels_the_denominator(tmp_path):
    """`speedup` is relative to whatever --baseline pointed at. An unlabeled
    number has been misread as vs-naive when it was vs-frontier, so the role
    must be recorded at the source."""
    from kernelgate import verify
    base = _write(tmp_path, "baseline.py", BASELINE_SRC)
    cand = _write(tmp_path, "cand.py", GOOD_CAND_SRC)
    rep = verify.run_verify(
        base, cand, mode="screen", dtype="float32",
        artifact_dir=str(tmp_path / "art"),
        family="testfam-role", fresh_cache=True,
        warmup=1, n_min=3, n_max=5, child_timeout=600)
    assert rep["speedup_role"]["role"] == "vs_naive"
    assert rep["speedup_role"]["baseline_basename"] == "baseline.py"

    # the same candidate measured against a frontier file is NOT vs_naive
    front = _write(tmp_path, "frontier_v007.py", BASELINE_SRC)
    rep2 = verify.run_verify(
        front, cand, mode="screen", dtype="float32",
        artifact_dir=str(tmp_path / "art2"),
        family="testfam-role2", fresh_cache=True,
        warmup=1, n_min=3, n_max=5, child_timeout=600)
    assert rep2["speedup_role"]["role"] == "vs_frontier"


def test_reproduction_records_why_it_was_skipped(tmp_path):
    """Without --author-claim-p50 the field was a bare null, indistinguishable
    from 'ran and found nothing'."""
    from kernelgate import verify
    base = _write(tmp_path, "baseline.py", BASELINE_SRC)
    cand = _write(tmp_path, "cand.py", GOOD_CAND_SRC)
    rep = verify.run_verify(
        base, cand, mode="screen", dtype="float32",
        artifact_dir=str(tmp_path / "art"),
        family="testfam-norepro", fresh_cache=True,
        warmup=1, n_min=3, n_max=5, child_timeout=600)
    assert rep["reproduction"]["verdict"] == "NOT_CHECKED"
    assert "author-claim-p50" in rep["reproduction"]["reason"]


def test_forbid_shape_can_pin_rank_with_explicit_brackets():
    """Unanchored specs match adjacent dims at any rank (historical); explicit
    brackets pin the rank so a hypothesis can forbid materializing exactly the
    full [S,S] score matrix without also firing on [B,H,S,S]."""
    big = "ROOT %f = f32[4,64,4096,4096] fusion(...)"
    exact = "ROOT %f = f32[4096,4096] fusion(...)"

    # historical behaviour preserved: unanchored fires on both
    assert hlo.run_assertions(big, forbid_shapes=["4096,4096"])["status"] == "FAIL"
    assert hlo.run_assertions(exact, forbid_shapes=["4096,4096"])["status"] == "FAIL"

    # bracket-anchored: rank-2 only
    assert hlo.run_assertions(big, forbid_shapes=["[4096,4096]"])["status"] == "PASS"
    assert hlo.run_assertions(exact, forbid_shapes=["[4096,4096]"])["status"] == "FAIL"

    # one-sided anchoring
    assert hlo.run_assertions(big, forbid_shapes=["[4,64"])["status"] == "FAIL"
    assert hlo.run_assertions(big, forbid_shapes=["[64,4096"])["status"] == "PASS"
    assert hlo.run_assertions(big, forbid_shapes=["4096,4096]"])["status"] == "FAIL"

    # boundary safety still holds under anchoring
    assert hlo.run_assertions("f32[14096,4096]",
                              forbid_shapes=["[4096,4096]"])["status"] == "PASS"


def test_requested_assertions_cannot_silently_evaporate(tmp_path, monkeypatch):
    """If assertions were requested but no candidate HLO dump was captured, the
    firing audit must FAIL, not be skipped into a PASS verdict."""
    from kernelgate import hlo, verify
    monkeypatch.setattr(hlo, "newest_module", lambda *a, **k: None)
    base = _write(tmp_path, "baseline.py", BASELINE_SRC)
    cand = _write(tmp_path, "cand.py", GOOD_CAND_SRC)
    rep = verify.run_verify(
        base, cand, mode="screen", dtype="float32",
        artifact_dir=str(tmp_path / "art"),
        family="testfam-noaudit", fresh_cache=True,
        expect_patterns=["tpu_custom_call_THAT_CANNOT_EXIST"],
        expect_custom_calls=7,
        warmup=1, n_min=3, n_max=5, child_timeout=600)
    assert rep["status"] != "PASS"
    assert rep["gates"]["hlo_firing_audit"]["ok"] is False


def test_requested_bar_cannot_silently_evaporate(tmp_path, monkeypatch):
    """A --bar the operator passed must be answered even when speedup
    extraction fails."""
    from kernelgate import verify
    base = _write(tmp_path, "baseline.py", BASELINE_SRC)
    cand = _write(tmp_path, "cand.py", GOOD_CAND_SRC)
    real = verify.measure.run_measure if hasattr(verify, "measure") else None
    rep = verify.run_verify(
        base, cand, mode="screen", dtype="float32",
        artifact_dir=str(tmp_path / "art"),
        family="testfam-bar", fresh_cache=True,
        bar_speedup=50.0,
        warmup=1, n_min=3, n_max=5, child_timeout=600)
    # same graph cannot be 50x faster -> the bar must be recorded and failed
    assert "falsification_bar" in rep["gates"]
    assert rep["gates"]["falsification_bar"]["ok"] is False
