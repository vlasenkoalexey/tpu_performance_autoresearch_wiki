"""Human tables + machine JSON emission."""
from __future__ import annotations

import json
import sys


def emit(report: dict, output: str | None = None, quiet_json: bool = False):
    """Print human summary, then the full JSON (marker-delimited); optionally
    also write JSON to a file."""
    for line in human_lines(report):
        print(line)
    if output:
        with open(output, "w") as f:
            json.dump(report, f, indent=2, default=str)
        print("[kgate] json written to %s" % output)
    if not quiet_json:
        print("--- KGATE-JSON ---")
        print(json.dumps(report, default=str))
    sys.stdout.flush()


def _fmt_leg(name: str, s: dict) -> str:
    return "  %-10s p50=%8.3f ms  mean=%8.3f  std=%7.3f  min=%8.3f  n=%d" % (
        name, s["p50_ms"], s["mean_ms"], s["std_ms"], s["min_ms"], s["n"])


def _parity_point_lines(label: str, rec: dict) -> list[str]:
    fl = rec["floor_baseline_vs_oracle"]
    cd = rec["candidate_vs_oracle"]
    g = rec["gate"]
    return [
        "%s:" % label,
        "  floor (baseline vs %s oracle)%s  max_abs=%.6g  mean_abs=%.6g" % (
            rec.get("oracle_used", "fp32"),
            "  [escalated: %s]" % rec["oracle_reason"] if rec.get("oracle_reason") else "",
            fl["max_abs"], fl["mean_abs"]),
        "  candidate vs oracle                   max_abs=%.6g  mean_abs=%.6g  "
        "max_rel(guarded, non-gating)=%.3g  finite=%.4f" % (
            cd["max_abs"], cd["mean_abs"], cd["max_rel_guarded"], cd["finite_fraction"]),
        "  gate: max_abs %.2fx floor, mean_abs %.2fx floor (limit %.1fx)  ->  %s" % (
            g["max_abs_ratio_vs_floor"], g["mean_abs_ratio_vs_floor"],
            g["multiplier"], "PASS" if g["ok"] else "FAIL"),
    ]


def human_lines(r: dict) -> list[str]:
    cmd = r.get("cmd")
    out = ["", "== kgate %s ==" % cmd]
    if cmd == "measure":
        t = r["timing"]
        a, b = t["ordering_A_candidate_first"], t["ordering_B_baseline_first"]
        out += ["ORDERING A (candidate first each iter)%s:"
                % ("" if a["converged"] else "  [NOT CONVERGED]"),
                _fmt_leg("candidate", a["candidate"]), _fmt_leg("baseline", a["baseline"]),
                "  speedup(p50) = %.3fx" % a["speedup_p50"],
                "ORDERING B (baseline first each iter)%s:"
                % ("" if b["converged"] else "  [NOT CONVERGED]"),
                _fmt_leg("candidate", b["candidate"]), _fmt_leg("baseline", b["baseline"]),
                "  speedup(p50) = %.3fx" % b["speedup_p50"],
                "POOLED: baseline p50=%.3f ms  candidate p50=%.3f ms  speedup=%.3fx" % (
                    t["pooled"]["baseline"]["p50_ms"], t["pooled"]["candidate"]["p50_ms"],
                    t["pooled"]["speedup_p50"])]
    elif cmd == "parity":
        out.append("oracle: %s" % r["oracle"]["strategy"])
        for seed, rec in r.get("seeds", {}).items():
            out += _parity_point_lines("seed %s" % seed, rec)
        for probe, rec in r.get("scale_probes", {}).items():
            out += _parity_point_lines("scale probe %s (input %s)" % (
                probe, r["oracle"].get("scale_input_index")), rec)
    elif cmd == "coverage":
        out.append("power threshold: %g" % r.get("power_threshold", float("nan")))
        for p in r.get("probes", []):
            out.append("  %-34s %-10s power=%9.4g  leak=%9.4g  resp=%9.4g  %s" % (
                p["name"], p.get("status", "?"),
                p.get("baseline_power_max_abs", float("nan")),
                p.get("candidate_unaffected_leak_max_abs", float("nan")),
                p.get("candidate_affected_response_max_abs", float("nan")),
                p.get("detail", "")))
        for c in r.get("slot_checks", []):
            if c["status"] != "OK":
                out.append("  dead-slot %-24s %-10s %s" % (
                    c["name"], c["status"], c.get("detail", "")))
        if r.get("axes"):
            out.append("per-axis:")
            for ax in r["axes"]:
                out.append("  %-16s %-10s %d slots%s" % (
                    ax["axis"], ax["status"], ax["size"],
                    "  failing: %s" % ax["failing_slots"] if ax["failing_slots"] else ""))
        for v in r.get("violations", []):
            out.append("VIOLATION: %s" % v)
        if r.get("n_slot_checks"):
            out.append("checks: %s probes + %s dead-slot screens, %s failed" % (
                r.get("n_probes"), r.get("n_slot_checks"), r.get("n_fail")))
        else:
            out.append("probes: %s total, %s failed" % (r.get("n_probes"), r.get("n_fail")))
    elif cmd == "sweep":
        if "baseline_timing" in r:
            out.append("baseline p50 = %.3f ms" % r["baseline_timing"]["p50_ms"])
        for g in r.get("grid", []):
            params = " ".join("%s=%s" % kv for kv in g["params"].items())
            if g["status"] == "OK":
                out.append("  %-32s p50=%8.3f ms  speedup=%.3fx  n=%d" % (
                    params, g["timing"]["p50_ms"], g["speedup_p50_vs_baseline"],
                    g["timing"]["n"]))
            elif g["status"] == "PARITY_FAIL":
                gt = g["parity"]["gate"]
                out.append("  %-32s PARITY_FAIL (max_abs %.1fx floor, mean_abs %.1fx floor)"
                           % (params, gt["max_abs_ratio_vs_floor"],
                              gt["mean_abs_ratio_vs_floor"]))
            else:
                exc = g.get("exception", "").strip().splitlines()
                out.append("  %-32s ERROR: %s" % (params, exc[-1] if exc else "?"))
        if r.get("argmin"):
            out.append("ARGMIN: %s  p50=%.3f ms  speedup=%.3fx" % (
                r["argmin"]["params"], r["argmin"]["p50_ms"],
                r["argmin"]["speedup_p50_vs_baseline"]))
        else:
            out.append("ARGMIN: none (no config passed parity + timing)")
    elif cmd == "roofline":
        if r["status"] == "ERROR":
            out.append("ERROR: %s" % r.get("error"))
        else:
            out += ["device=%s  peaks: %.0f TFLOP/s, %.0f GB/s" % (
                        r["device_kind"], r["peak_tflops"], r["peak_gbps"]),
                    "speed-of-light: compute=%.4f ms  memory=%.4f ms  bound=%.4f ms (%s)" % (
                        r["compute_bound_ms"], r["memory_bound_ms"],
                        r["speed_of_light_ms"], r["binding_resource"]),
                    "measured p50 = %.4f ms  ->  %.2f TFLOP/s, %.2f GB/s, %.1f%% of light" % (
                        r["measured_p50_ms"], r["achieved_tflops"], r["achieved_gbps"],
                        r["utilization_pct"])]
            if r.get("detail"):
                out.append("INVALID: %s" % r["detail"])
    elif cmd == "lint":
        for f in r.get("findings", []):
            loc = ":%s" % f["line"] if "line" in f else ""
            out.append("  [%s] %s%s %s" % (f["level"], f["code"], loc, f["message"]))
        if not r.get("findings"):
            out.append("  no findings (a clean lint proves nothing)")
    elif cmd == "flags":
        fl = r.get("flag") or {}
        out.append("flag: %s=%s" % (fl.get("key"), fl.get("value")))
        for name in ("naive_default", "naive_flagged", "cand_default", "cand_flagged"):
            leg = r.get("legs", {}).get(name)
            if leg:
                out.append(_fmt_leg(name, leg["stats"]))
        ratios = r.get("ratios", {})
        defs = r.get("ratio_definitions", {})
        for name in ("flag_only_ratio", "kernel_cell_ratio", "end_to_end_ratio"):
            if name in ratios:
                out.append("%-18s = %.3fx   (%s)" % (
                    name, ratios[name], defs.get(name, "")))
        if r.get("same_graph"):
            out.append("same-graph cell: baseline == candidate (flag-only comparison)")
    elif cmd == "fit":
        from . import fit as fit_mod
        out += ["  " + ln for ln in fit_mod.tsv_lines(r)]
        out.append("configs: %s total, %s fit" % (r.get("n_configs"), r.get("n_fit")))
    elif cmd == "verify-receipt":
        out.append("receipt: %s (cmd=%s, verdict=%s)" % (
            r.get("path"), r.get("receipt_cmd"), r.get("verdict")))
        for c in r.get("checks", []):
            mark = ("SKIPPED" if c.get("skipped") else
                    "ok" if c["ok"] else "FAILED")
            out.append("  %-32s %s  %s" % (
                c["name"], mark, c.get("detail", "")))
        if r.get("unverified"):
            out.append("  NOTE: status OK covers only the checks that ran; "
                       "not verified: %s" % ", ".join(r["unverified"]))

    for w in r.get("warnings", []):
        out.append("WARNING: %s" % w)
    for a in r.get("anomalies", []):
        out.append("ANOMALY: %s" % a)
    if r.get("exception"):
        out.append("EXCEPTION:")
        out += ["  " + ln for ln in r["exception"].rstrip().splitlines()]
    out.append("STATUS: %s" % r.get("status"))
    return out
