"""Tamper-evident receipts for parity / measure / flags runs.

Every parity, measure, and flags run also writes `receipt.json`: a compact,
self-hashed record binding the verdict to the kgate version + git SHA that
produced it, the exact input arrays (sha256, regenerable from the recorded
baseline module + seed), the output arrays both legs produced, the floor and
thresholds the verdict was graded against, and the argv. The receipt is what
a supervisor audits when a worker claims a PASS — a claim without a receipt
(or with a receipt that fails verification) is not evidence.

`kgate verify-receipt <receipt.json>` checks three layers:
  1. self-hash: sha256 over the canonical JSON (minus the hash field) —
     casual edits to any field (verdict, floor, p50s, ...) are detected;
  2. internal arithmetic: the verdict must follow from the recorded numbers
     (parity: candidate error <= multiplier x floor per point; flags: the
     ratios must equal the recorded p50 quotients);
  3. input regeneration: create_inputs(seed) from the recorded baseline
     module is re-run and its sha256 compared (skippable with --skip-inputs
     on a machine without the module).

The self-hash is integrity, not authentication — it detects editing, not a
determined forger who recomputes it; pair with trusted storage for the latter.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import time

from . import __version__, parity as parity_mod

SELF_HASH_FIELD = "self_sha256"
RECEIPT_CMDS = ("parity", "measure", "flags", "verify")


def _git_sha() -> str | None:
    pkg_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        out = subprocess.run(["git", "-C", pkg_dir, "rev-parse", "HEAD"],
                             capture_output=True, text=True, timeout=10)
        return out.stdout.strip() or None if out.returncode == 0 else None
    except Exception:
        return None


def canonical_json(obj: dict) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str)


def self_hash(receipt: dict) -> str:
    body = {k: v for k, v in receipt.items() if k != SELF_HASH_FIELD}
    return hashlib.sha256(canonical_json(body).encode()).hexdigest()


def _gate_points(report: dict):
    """Parity report -> {point_name: gate-relevant numbers} for the receipt."""
    points = {}
    for group in ("seeds", "scale_probes"):
        for key, rec in report.get(group, {}).items():
            points["%s:%s" % (group, key)] = {
                "oracle_used": rec.get("oracle_used"),
                "floor_max_abs": rec["floor_baseline_vs_oracle"]["max_abs"],
                "floor_mean_abs": rec["floor_baseline_vs_oracle"]["mean_abs"],
                "cand_max_abs": rec["candidate_vs_oracle"]["max_abs"],
                "cand_mean_abs": rec["candidate_vs_oracle"]["mean_abs"],
                "finite_fraction": rec["candidate_vs_oracle"]["finite_fraction"],
                "ok": rec["gate"]["ok"],
                "outputs_sha256": rec.get("outputs_sha256"),
            }
    return points


def build(report: dict, argv=None) -> dict:
    """Extract the receipt from a finished parity / measure / flags report."""
    cmd = report.get("cmd")
    if cmd not in RECEIPT_CMDS:
        raise ValueError("no receipt schema for cmd %r" % cmd)
    receipt = {
        "receipt_version": 1,
        "kgate_version": __version__,
        "git_sha": _git_sha(),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "cmd": cmd,
        "argv": list(argv) if argv is not None else None,
        "baseline": report.get("baseline"),
        "candidate": report.get("candidate"),
        "verdict": report.get("status"),
        "oracle_type": None,
        "input_shapes": (report.get("inputs") or {}).get("shapes"),
        "inputs_sha256": (report.get("inputs") or {}).get("sha256"),
        "inputs_sha256_combined": (report.get("inputs") or {}).get("combined"),
        "outputs_sha256": None,
        "floor": None,
        "thresholds": None,
    }
    if cmd == "parity":
        seeds = list(report.get("seeds", {}))  # run order; [0] is the canonical seed
        first = report["seeds"][seeds[0]] if seeds else None
        receipt.update({
            "oracle_type": ",".join(report.get("oracle", {}).get("used", [])) or None,
            "seeds": seeds,
            "outputs_sha256": (first or {}).get("outputs_sha256"),
            "floor": (first or {}).get("floor_baseline_vs_oracle"),
            "thresholds": {"multiplier": report.get("multiplier"),
                           "floor_eps": report.get("oracle", {}).get("floor_eps")},
            "gate_points": _gate_points(report),
        })
    elif cmd == "measure":
        receipt.update({
            "seed": report.get("seed"),
            "outputs_sha256": report.get("outputs_sha256"),
            "thresholds": {k: report["timing"][k]
                           for k in ("warmup", "n_min", "n_max", "se_target")},
            "pooled_p50_ms": {
                "baseline": report["timing"]["pooled"]["baseline"]["p50_ms"],
                "candidate": report["timing"]["pooled"]["candidate"]["p50_ms"]},
            "speedup_p50": report["timing"]["pooled"]["speedup_p50"],
            "anomalies": report.get("anomalies"),
        })
    elif cmd == "verify":
        m = report.get("legs", {}).get("measure", {}) or {}
        p = report.get("legs", {}).get("parity", {}) or {}
        audit = report.get("hlo_audit") or {}
        digest = report.get("xprof_digest") or {}
        # A verify report has no top-level "inputs" — the digests live in the
        # parity leg, which built them from the same baseline module. Propagate
        # them so `verify-receipt` can actually re-derive the inputs instead of
        # skipping the check (and, before the fix, reporting MISMATCH).
        p_inputs = (p.get("inputs") or {})
        if p_inputs:
            receipt.update({
                "input_shapes": p_inputs.get("shapes"),
                "inputs_sha256": p_inputs.get("sha256"),
                "inputs_sha256_combined": p_inputs.get("combined"),
            })
        p_seeds = list(p.get("seeds") or {})
        if p_seeds:
            receipt["seeds"] = p_seeds
        receipt.update({
            "mode": report.get("mode"),
            "gates": {name: g.get("ok")
                      for name, g in (report.get("gates") or {}).items()},
            "speedup": report.get("speedup"),
            "speedup_role": report.get("speedup_role"),
            "p50_ms": report.get("p50_ms"),
            "parity_verdict": p.get("status"),
            "measure_verdict": m.get("status"),
            "hlo_audit": {"status": audit.get("status"),
                          "custom_call_count": audit.get("custom_call_count"),
                          "checks": [{"name": c["name"], "ok": c["ok"]}
                                     for c in audit.get("checks", [])]},
            "reproduction": report.get("reproduction"),
            "digest_available": digest.get("available"),
            "artifact_dir": report.get("artifact_dir"),
            "compilation_cache_dir": report.get("compilation_cache_dir"),
            "anomalies": report.get("anomalies"),
        })
    elif cmd == "flags":
        receipt.update({
            "seed": report.get("seed"),
            "flag": report.get("flag"),
            "same_graph": report.get("same_graph"),
            "outputs_sha256": {name: leg.get("output_sha256")
                               for name, leg in report.get("legs", {}).items()},
            "leg_p50_ms": {name: leg["stats"]["p50_ms"]
                           for name, leg in report.get("legs", {}).items()},
            "ratios": report.get("ratios"),
            "thresholds": {k: report["timing"][k] for k in ("warmup", "n")},
        })
    receipt[SELF_HASH_FIELD] = self_hash(receipt)
    return receipt


def write(report: dict, path: str, argv=None) -> dict:
    receipt = build(report, argv=argv)
    with open(path, "w") as f:
        json.dump(receipt, f, indent=2, default=str)
    return receipt


def _check(checks: list, name: str, ok: bool, detail: str = ""):
    checks.append({"name": name, "ok": bool(ok), "detail": detail})
    return ok


# Sentinel for a check that could not be performed. Distinct from False:
# False means "checked and inconsistent", SKIPPED means "no evidence to check
# against". Rendering SKIPPED as False turns absence of evidence into a
# positive finding of tampering — see the verify-mode MISMATCH bug.
SKIPPED = "skipped"


def _skip(checks: list, name: str, detail: str = ""):
    checks.append({"name": name, "ok": None, "skipped": True, "detail": detail})
    return SKIPPED


def _verify_parity_arithmetic(receipt: dict, checks: list) -> bool:
    mult = receipt["thresholds"]["multiplier"]
    fallback = parity_mod.FLOOR_EPS_FALLBACK
    all_ok = True
    for name, pt in receipt.get("gate_points", {}).items():
        fm = pt["floor_max_abs"] or fallback
        fmean = pt["floor_mean_abs"] or fallback
        recomputed = (pt["cand_max_abs"] <= mult * fm
                      and pt["cand_mean_abs"] <= mult * fmean
                      and pt["finite_fraction"] == 1.0)
        ok = recomputed == pt["ok"]
        all_ok &= _check(checks, "gate arithmetic %s" % name, ok,
                         "" if ok else "recorded ok=%s but numbers imply %s"
                         % (pt["ok"], recomputed))
    points_ok = all(pt["ok"] for pt in receipt.get("gate_points", {}).values())
    verdict_ok = (receipt["verdict"] == "PASS") == points_ok
    all_ok &= _check(checks, "verdict consistency", verdict_ok,
                     "" if verdict_ok else "verdict %r inconsistent with gate points"
                     % receipt["verdict"])
    return all_ok


def _verify_flags_arithmetic(receipt: dict, checks: list) -> bool:
    p = receipt.get("leg_p50_ms", {})
    r = receipt.get("ratios", {})
    expected = {
        "flag_only_ratio": p.get("naive_default", 0) / p["naive_flagged"]
        if p.get("naive_flagged") else None,
        "kernel_cell_ratio": p.get("naive_flagged", 0) / p["cand_flagged"]
        if p.get("cand_flagged") else None,
        "end_to_end_ratio": p.get("naive_default", 0) / p["cand_flagged"]
        if p.get("cand_flagged") else None,
    }
    all_ok = True
    for name, exp in expected.items():
        got = r.get(name)
        ok = (exp is not None and got is not None
              and abs(got - exp) <= 1e-9 * max(abs(exp), 1.0))
        all_ok &= _check(checks, "ratio arithmetic %s" % name, ok,
                         "" if ok else "recorded %s, p50s imply %s" % (got, exp))
    return all_ok


def _verify_verify_consistency(receipt: dict, checks: list) -> bool:
    """Cross-check a `verify` receipt's headline against its own evidence.

    `verify` is the receipt type the campaign actually grades on, and it had no
    consistency check at all: a receipt could read `verdict: PASS` while
    carrying a false gate, and verify-receipt returned OK.
    """
    all_ok = True
    gates = receipt.get("gates") or {}
    verdict = receipt.get("verdict")
    if gates:
        failed = sorted(k for k, v in gates.items() if v is False)
        # PASS requires every recorded gate to be true. ANOMALY/FAIL may carry
        # failed gates legitimately — only PASS is contradicted by one.
        if verdict == "PASS":
            all_ok &= _check(
                checks, "verdict vs gates", not failed,
                "" if not failed else
                "verdict is PASS but these gates are false: %s" % ", ".join(failed))
        else:
            _check(checks, "verdict vs gates", True,
                   "verdict %s with failed gates %s" % (verdict, failed or "none"))
    else:
        _skip(checks, "verdict vs gates", "receipt records no gates to re-check")

    # speedup must equal baseline_p50 / candidate_p50 when both are recorded.
    p = receipt.get("p50_ms") or {}
    sp = receipt.get("speedup")
    b, c = p.get("baseline"), p.get("candidate")
    if sp is not None and b and c:
        exp = b / c
        ok = abs(sp - exp) <= 1e-6 * max(abs(exp), 1.0)
        all_ok &= _check(checks, "speedup arithmetic", ok,
                         "" if ok else "recorded %s, p50s imply %s" % (sp, exp))
    else:
        _skip(checks, "speedup arithmetic",
              "receipt lacks speedup or the p50 pair needed to re-derive it")
    return all_ok


def _verify_measure_arithmetic(receipt: dict, checks: list) -> bool:
    """`speedup_p50` must equal the recorded pooled p50 quotient."""
    p = receipt.get("pooled_p50_ms") or {}
    sp = receipt.get("speedup_p50")
    b, c = p.get("baseline"), p.get("candidate")
    if sp is None or not b or not c:
        _skip(checks, "speedup arithmetic",
              "receipt lacks speedup_p50 or the pooled p50 pair")
        return True
    exp = b / c
    ok = abs(sp - exp) <= 1e-6 * max(abs(exp), 1.0)
    return _check(checks, "speedup arithmetic", ok,
                  "" if ok else "recorded %s, pooled p50s imply %s" % (sp, exp))


def verify(path: str, recompute_inputs: bool = True) -> dict:
    """Verify a receipt file. Returns a report dict (status OK / TAMPERED /
    MISMATCH / ERROR)."""
    report = {"cmd": "verify-receipt", "path": os.path.abspath(path),
              "checks": [], "status": "OK"}
    checks = report["checks"]
    try:
        with open(path) as f:
            receipt = json.load(f)
        report["receipt_cmd"] = receipt.get("cmd")
        report["verdict"] = receipt.get("verdict")

        recorded = receipt.get(SELF_HASH_FIELD)
        recomputed = self_hash(receipt)
        hash_ok = _check(checks, "self-hash", recorded == recomputed,
                         "" if recorded == recomputed else
                         "recorded %s != recomputed %s — receipt was edited"
                         % (recorded, recomputed))

        arith_ok = True
        _cmd = receipt.get("cmd")
        if _cmd == "parity":
            if receipt.get("gate_points"):
                arith_ok = _verify_parity_arithmetic(receipt, checks)
            else:
                _skip(checks, "gate arithmetic",
                      "receipt records no gate points to re-check")
        elif _cmd == "flags":
            if receipt.get("ratios"):
                arith_ok = _verify_flags_arithmetic(receipt, checks)
            else:
                _skip(checks, "ratio arithmetic",
                      "receipt records no ratios to re-check")
        elif _cmd == "verify":
            arith_ok = _verify_verify_consistency(receipt, checks)
        elif _cmd == "measure":
            arith_ok = _verify_measure_arithmetic(receipt, checks)

        inputs_ok = True
        if recompute_inputs:
            inputs_ok = _verify_inputs(receipt, checks)

        if not hash_ok or not arith_ok:
            report["status"] = "TAMPERED"
        elif inputs_ok is SKIPPED:
            # Every check that could run, passed; the input-regeneration check
            # had no evidence to run against. That is OK-with-a-caveat, not a
            # mismatch.
            report["status"] = "OK"
            report["incomplete"] = True
            report["unverified"] = ["input regeneration"]
        elif not inputs_ok:
            report["status"] = "MISMATCH"
    except Exception:
        import traceback
        report["status"] = "ERROR"
        report["exception"] = traceback.format_exc()
    return report


def _verify_inputs(receipt: dict, checks: list) -> bool:
    """Regenerate the inputs from the recorded baseline module + seed and
    compare the sha256 digests."""
    from . import protocol
    base = (receipt.get("baseline") or {}).get("path")
    if not base:
        return _skip(checks, "input regeneration",
                     "receipt records no baseline path — nothing to regenerate "
                     "from (not evidence of a mismatch)")
    if not receipt.get("inputs_sha256"):
        return _skip(checks, "input regeneration",
                     "receipt carries no inputs_sha256, so the inputs cannot be "
                     "re-derived and compared. Receipts written by `kgate verify` "
                     "before the digests were propagated from the parity leg are "
                     "expected to hit this. NOT evidence of a mismatch — the "
                     "self-hash check above still covers tampering.")
    seed = receipt.get("seed")
    if seed is None:
        seeds = receipt.get("seeds") or []
        seed = int(seeds[0]) if seeds else None
    try:
        mod = protocol.load_module(base)
        inputs = protocol.make_inputs(mod, seed=seed)
        digest = protocol.sha256_arrays(inputs)
    except Exception as e:
        return _check(checks, "input regeneration", False,
                      "could not regenerate inputs: %r (pass --skip-inputs to "
                      "verify hash+arithmetic only)" % (e,))
    ok = digest["sha256"] == receipt["inputs_sha256"]
    return _check(checks, "input regeneration", ok,
                  "" if ok else "regenerated input sha256 differs — inputs field "
                  "does not correspond to %s seed %s" % (base, seed))
