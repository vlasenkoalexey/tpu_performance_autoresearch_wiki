"""Tamper-evident receipts + verify-receipt — pure CPU.

A receipt binds a verdict to version/SHA, input/output hashes, floor and
thresholds. Editing the verdict or the floor must be detected (self-hash +
gate-arithmetic checks); a receipt whose inputs field doesn't regenerate
from the recorded module+seed must MISMATCH.
"""
import json
import textwrap

import pytest

from kernelgate import parity, protocol, receipt, timing
from tests.test_gates_cpu import BASELINE, GOOD_CAND


def _mod(tmp_path, name, src):
    p = tmp_path / name
    p.write_text(textwrap.dedent(src))
    return protocol.load_module(str(p))


@pytest.fixture
def parity_receipt(tmp_path):
    base = _mod(tmp_path, "baseline.py", BASELINE)
    cand = _mod(tmp_path, "cand_good.py", GOOD_CAND)
    rep = parity.run_parity(base, cand, seeds=(42,))
    assert rep["status"] == "PASS", rep.get("exception")
    path = str(tmp_path / "receipt.json")
    receipt.write(rep, path, argv=["parity", "--baseline", "baseline.py"])
    return path


def test_receipt_fields(parity_receipt):
    with open(parity_receipt) as f:
        r = json.load(f)
    assert r["kgate_version"]
    assert r["cmd"] == "parity"
    assert r["verdict"] == "PASS"
    assert r["oracle_type"] == "fp32"
    assert r["input_shapes"] and r["inputs_sha256"]
    assert r["outputs_sha256"]["baseline"] and r["outputs_sha256"]["candidate"]
    assert r["floor"]["max_abs"] > 0
    assert r["thresholds"]["multiplier"] == 2.0
    assert r["argv"] == ["parity", "--baseline", "baseline.py"]
    assert r["self_sha256"] == receipt.self_hash(r)


def test_verify_clean_receipt_ok(parity_receipt):
    rep = receipt.verify(parity_receipt)
    assert rep["status"] == "OK", rep["checks"]
    assert all(c["ok"] for c in rep["checks"])


def test_tampered_verdict_detected(parity_receipt):
    with open(parity_receipt) as f:
        r = json.load(f)
    r["verdict"] = "PASS" if r["verdict"] != "PASS" else "FAIL"
    with open(parity_receipt, "w") as f:
        json.dump(r, f)
    rep = receipt.verify(parity_receipt, recompute_inputs=False)
    assert rep["status"] == "TAMPERED"
    assert not [c for c in rep["checks"] if c["name"] == "self-hash"][0]["ok"]


def test_tampered_floor_detected_even_with_rehashed_receipt(parity_receipt):
    """Editing the floor AND recomputing the self-hash still trips the
    gate-arithmetic cross-check (verdict no longer follows from the numbers)."""
    with open(parity_receipt) as f:
        r = json.load(f)
    for pt in r["gate_points"].values():
        pt["floor_max_abs"] = 1e-12   # forged floor: cand error now >> 2x floor
        pt["floor_mean_abs"] = 1e-12
    r["self_sha256"] = receipt.self_hash(r)   # adversary re-hashes
    with open(parity_receipt, "w") as f:
        json.dump(r, f)
    rep = receipt.verify(parity_receipt, recompute_inputs=False)
    assert rep["status"] == "TAMPERED"
    bad = [c for c in rep["checks"] if c["name"].startswith("gate arithmetic")]
    assert bad and not all(c["ok"] for c in bad)


def test_tampered_floor_without_rehash_detected(parity_receipt):
    with open(parity_receipt) as f:
        r = json.load(f)
    r["floor"]["max_abs"] = 0.0
    with open(parity_receipt, "w") as f:
        json.dump(r, f)
    rep = receipt.verify(parity_receipt, recompute_inputs=False)
    assert rep["status"] == "TAMPERED"


def test_input_regeneration_mismatch(parity_receipt):
    """A receipt pointing at inputs it never measured must MISMATCH."""
    with open(parity_receipt) as f:
        r = json.load(f)
    r["seeds"] = ["43"]                      # claim a different seed...
    r["self_sha256"] = receipt.self_hash(r)  # ...with a consistent self-hash
    with open(parity_receipt, "w") as f:
        json.dump(r, f)
    rep = receipt.verify(parity_receipt)
    assert rep["status"] == "MISMATCH", rep["checks"]
    bad = [c for c in rep["checks"] if c["name"] == "input regeneration"][0]
    assert not bad["ok"]


def test_input_regeneration_ok_end_to_end(parity_receipt):
    rep = receipt.verify(parity_receipt, recompute_inputs=True)
    assert rep["status"] == "OK", rep["checks"]


def test_measure_receipt_roundtrip(tmp_path):
    base = _mod(tmp_path, "baseline.py", BASELINE)
    cand = _mod(tmp_path, "cand_good.py", GOOD_CAND)
    rep = timing.run_measure(base, cand, warmup=1, n_min=3, n_max=4, se_target=1e-9)
    path = str(tmp_path / "receipt.json")
    receipt.write(rep, path)
    ver = receipt.verify(path)
    assert ver["status"] == "OK", ver["checks"]
    with open(path) as f:
        r = json.load(f)
    assert r["cmd"] == "measure"
    assert r["speedup_p50"] > 0
    assert r["outputs_sha256"]["baseline"]


def test_flags_receipt_ratio_arithmetic(tmp_path):
    """A flags receipt with a forged ratio (re-hashed) trips the arithmetic
    cross-check."""
    fake_report = {
        "cmd": "flags", "status": "PASS", "seed": None,
        "baseline": {"path": "b.py", "entry": "workload"},
        "candidate": {"path": "b.py", "entry": "workload"},
        "flag": {"key": "X", "value": "1", "parent_env_value": None},
        "same_graph": True,
        "timing": {"warmup": 1, "n": 3},
        "inputs": {"shapes": ["float32[4]"], "sha256": ["a"], "combined": "a"},
        "legs": {name: {"stats": {"p50_ms": p}, "output_sha256": "x"}
                 for name, p in (("naive_default", 1.5), ("naive_flagged", 1.0),
                                 ("cand_default", 1.5), ("cand_flagged", 1.0))},
        "ratios": {"flag_only_ratio": 1.5, "kernel_cell_ratio": 1.0,
                   "end_to_end_ratio": 1.5},
    }
    path = str(tmp_path / "receipt.json")
    receipt.write(fake_report, path)
    assert receipt.verify(path, recompute_inputs=False)["status"] == "OK"
    with open(path) as f:
        r = json.load(f)
    r["ratios"]["flag_only_ratio"] = 3.0      # forged headline
    r["self_sha256"] = receipt.self_hash(r)
    with open(path, "w") as f:
        json.dump(r, f)
    rep = receipt.verify(path, recompute_inputs=False)
    assert rep["status"] == "TAMPERED"


def test_no_receipt_schema_for_other_cmds():
    with pytest.raises(ValueError):
        receipt.build({"cmd": "lint", "status": "CLEAN"})


# --- regression: absence of evidence must not become a positive finding ------
# Before the fix, `verify` receipts carried no inputs_sha256 (the digests live
# in the parity leg and were never propagated), so _verify_inputs bailed out
# with ok=False and the overall status became MISMATCH — the tool's word for
# "the recorded inputs do not correspond to the baseline". 1731 of 1732 verify
# receipts in the campaign hit this, training readers to ignore verify-receipt
# entirely and masking the self-hash check that does work.

def _verify_receipt_missing_digests(tmp_path):
    fake = {
        "cmd": "verify", "status": "PASS", "mode": "screen",
        "baseline": {"path": str(tmp_path / "baseline.py"), "entry": "workload"},
        "candidate": {"path": str(tmp_path / "cand.py"), "entry": "workload"},
        "gates": {"measure": {"ok": True}, "parity": {"ok": True}},
        "speedup": 2.0, "legs": {}, "warnings": [], "anomalies": [],
    }
    path = str(tmp_path / "receipt.json")
    receipt.write(fake, path)
    return path


def test_missing_input_digests_skip_rather_than_mismatch(tmp_path):
    """No inputs_sha256 => the check is SKIPPED, not FAILED, and the receipt
    is not branded MISMATCH."""
    rep = receipt.verify(_verify_receipt_missing_digests(tmp_path))
    assert rep["status"] == "OK"
    assert rep["incomplete"] is True
    assert "input regeneration" in rep["unverified"]
    chk = [c for c in rep["checks"] if c["name"] == "input regeneration"][0]
    assert chk["skipped"] is True and chk["ok"] is None


def test_skipped_input_check_still_detects_tampering(tmp_path):
    """The weaker input check must not weaken the self-hash check."""
    path = _verify_receipt_missing_digests(tmp_path)
    with open(path) as f:
        r = json.load(f)
    r["speedup"] = 99.0                        # forged headline, hash NOT resealed
    with open(path, "w") as f:
        json.dump(r, f)
    assert receipt.verify(path)["status"] == "TAMPERED"


def test_present_but_wrong_input_digest_still_mismatches(tmp_path):
    """A digest that IS present and does not regenerate must still MISMATCH —
    the fix must not swallow real inconsistencies."""
    base = tmp_path / "baseline.py"
    base.write_text(textwrap.dedent(BASELINE))
    fake = {
        "cmd": "measure", "status": "PASS", "seed": 0,
        "baseline": {"path": str(base), "entry": "workload"},
        "candidate": {"path": str(base), "entry": "workload"},
        "inputs": {"shapes": ["f32[4]"], "sha256": ["0" * 64], "combined": "0" * 64},
        "outputs_sha256": {"baseline": "x", "candidate": "x"},
        "timing": {"warmup": 1, "n_min": 1, "n_max": 2, "se_target": 0.1,
                   "pooled": {"baseline": {"p50_ms": 2.0},
                              "candidate": {"p50_ms": 1.0}, "speedup_p50": 2.0}},
    }
    path = str(tmp_path / "m.json")
    receipt.write(fake, path)
    rep = receipt.verify(path, recompute_inputs=True)
    assert rep["status"] == "MISMATCH"


def test_verify_receipt_propagates_parity_leg_digests(tmp_path):
    """New verify receipts must carry the parity leg's digests so the input
    check can actually run."""
    fake = {
        "cmd": "verify", "status": "PASS", "mode": "full",
        "baseline": {"path": "b.py", "entry": "workload"},
        "candidate": {"path": "c.py", "entry": "workload"},
        "gates": {}, "speedup": 2.0, "warnings": [], "anomalies": [],
        "legs": {"parity": {
            "status": "PASS",
            "inputs": {"shapes": ["f32[4]"], "sha256": ["abc"], "combined": "abc"},
            "seeds": {"0": {}, "1": {}}}},
    }
    path = str(tmp_path / "v.json")
    receipt.write(fake, path)
    with open(path) as f:
        r = json.load(f)
    assert r["inputs_sha256"] == ["abc"]
    assert r["seeds"] == ["0", "1"]


def test_verify_receipt_catches_pass_verdict_with_false_gate(tmp_path):
    """A `verify` receipt had NO consistency check at all — verdict PASS
    alongside a false gate validated clean."""
    fake = {"cmd": "verify", "status": "PASS",
            "baseline": {"path": "b.py"}, "candidate": {"path": "c.py"},
            "gates": {"parity": {"ok": False}, "measure": {"ok": True}},
            "speedup": 2.0, "legs": {}, "warnings": [], "anomalies": []}
    path = str(tmp_path / "v.json")
    receipt.write(fake, path)
    assert receipt.verify(path, recompute_inputs=False)["status"] == "TAMPERED"


def test_verify_receipt_catches_forged_measure_speedup(tmp_path):
    fake = {"cmd": "measure", "status": "PASS", "seed": 0,
            "baseline": {"path": "b.py"}, "candidate": {"path": "c.py"},
            "outputs_sha256": {},
            "timing": {"warmup": 1, "n_min": 1, "n_max": 2, "se_target": 0.1,
                       "pooled": {"baseline": {"p50_ms": 3.0},
                                  "candidate": {"p50_ms": 2.9},
                                  "speedup_p50": 10.0}}}
    path = str(tmp_path / "m.json")
    receipt.write(fake, path)
    assert receipt.verify(path, recompute_inputs=False)["status"] == "TAMPERED"


def test_honest_verify_receipt_still_validates(tmp_path):
    fake = {"cmd": "verify", "status": "PASS",
            "baseline": {"path": "b.py"}, "candidate": {"path": "c.py"},
            "gates": {"parity": {"ok": True}, "measure": {"ok": True}},
            "speedup": 2.0, "p50_ms": {"baseline": 4.0, "candidate": 2.0},
            "legs": {}, "warnings": [], "anomalies": []}
    path = str(tmp_path / "v.json")
    receipt.write(fake, path)
    assert receipt.verify(path, recompute_inputs=False)["status"] == "OK"
