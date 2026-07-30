"""Spec-driven sensitivity coverage battery.

A family spec module defines:

    def perturb_regions(baseline_module, inputs) -> list of probe dicts:
        {
          "name":            str,
          "inputs":          perturbed input tuple,
          "affected_mask":   numpy bool array over the OUTPUT shape — True
                             where the perturbation is expected to change the
                             output, False where the output must be
                             bit-identical,
          "base_inputs":     optional — reference inputs the probe perturbs
                             (defaults to the canonical clean inputs; used by
                             probes that need a non-canonical base, e.g.
                             shortened kv_lens for invalid-page no-leak),
        }
    POWER_THRESHOLD = float   (optional, default 1e-3) — minimum baseline
                              response on the affected set for the probe to
                              count as having power
    SCALE_INPUT = int         (optional) — input index for parity scale probes

For each probe kgate runs baseline and candidate on (base, perturbed) inputs
and asserts the candidate reproduces the baseline's sensitivity structure
EXACTLY:
  - spec sanity: baseline itself must be bit-identical on the unaffected set
    (else the mask is wrong -> SPEC_ERROR, probe not charged to candidate);
  - probe power:  baseline must respond above threshold on the affected set;
  - candidate unaffected set: bit-identical between base and perturbed runs
    (any change = leak: wrong-side reads, aliasing, causal violation);
  - candidate affected set: must respond above threshold (silence = skipped
    work: 50%%-coverage class).

This is the gate class that catches kernels which pass loose atol parity while
skipping half the k-blocks or aliasing GQA groups.

Alternatively the spec can be DECLARATIVE (see declspec.py): a dict / module
with `axes` (or a .json/.yaml file via the CLI) naming the problem's semantic
axes and their input->output slot mapping. kgate then generates the per-slot
probes itself and additionally screens the clean candidate output for dead
slots (all-NaN / all-zero regions — the v042 head-skip signature). Failures
are reported per axis with the offending slots NAMED, in `violations`.
"""
from __future__ import annotations

from . import declspec, protocol

DEFAULT_POWER_THRESHOLD = 1e-3


def _spec_path(spec):
    if isinstance(spec, dict):
        return spec.get("__kgate_path__") or "<dict>"
    return getattr(spec, "__kgate_path__", getattr(spec, "__file__", "?"))


def _spec_threshold(spec) -> float:
    if isinstance(spec, dict):
        return float(spec.get("power_threshold", DEFAULT_POWER_THRESHOLD))
    return float(getattr(spec, "POWER_THRESHOLD", DEFAULT_POWER_THRESHOLD))


def bit_identical(a, b, region) -> bool:
    """Exact equality on the region (NaN == NaN counts as equal)."""
    import numpy as np
    if not region.any():
        return True
    av = np.asarray(a)[region]
    bv = np.asarray(b)[region]
    # ml_dtypes bfloat16 supports ==; equal_nan path via isnan
    eq = av == bv
    both_nan = None
    try:
        both_nan = np.isnan(av.astype(np.float32)) & np.isnan(bv.astype(np.float32))
    except (TypeError, ValueError):
        pass
    if both_nan is not None:
        eq = eq | both_nan
    return bool(np.all(eq))


def max_abs_delta(a, b, region) -> float:
    import numpy as np
    if not region.any():
        return 0.0
    av = np.asarray(a).astype(np.float32)[region]
    bv = np.asarray(b).astype(np.float32)[region]
    return float(np.max(np.abs(av - bv)))


def run_coverage(baseline_mod, candidate_mod, spec_mod,
                 baseline_entry: str = "workload",
                 candidate_entry: str | None = None,
                 seed: int | None = None) -> dict:
    import traceback
    import numpy as np
    import jax
    from . import envinfo

    declarative = declspec.is_declarative(spec_mod)
    report = {
        "cmd": "coverage",
        "baseline": {"path": baseline_mod.__kgate_path__},
        "candidate": {"path": candidate_mod.__kgate_path__},
        "spec": {"path": _spec_path(spec_mod), "declarative": declarative},
        "config": protocol.get_config(baseline_mod),
        "env": envinfo.capture(),
        "probes": [],
        "violations": [],
        "status": "PASS",
    }
    try:
        threshold = _spec_threshold(spec_mod)
        report["power_threshold"] = threshold
        inputs = protocol.make_inputs(baseline_mod, seed=seed)
        n_inputs = len(inputs)
        b_name, b_fn = protocol.resolve_entry(baseline_mod, baseline_entry, n_inputs)
        c_name, c_fn = protocol.resolve_entry(candidate_mod, candidate_entry, n_inputs)
        report["baseline"]["entry"] = b_name
        report["candidate"]["entry"] = c_name
        fb = protocol.as_jitted(b_fn)
        fc = protocol.as_jitted(c_fn)

        # cache clean-run outputs keyed by identity of base inputs
        cache = {}

        def outputs_for(inp):
            key = tuple(id(x) for x in inp)
            if key not in cache:
                ob = np.asarray(jax.block_until_ready(fb(*inp)))
                oc = np.asarray(jax.block_until_ready(fc(*inp)))
                cache[key] = (ob, oc)
            return cache[key]

        if declarative:
            spec = declspec.normalize(spec_mod)
            b_clean, c_clean = outputs_for(tuple(inputs))
            probes = declspec.build_probes(spec, inputs, b_clean.shape)
            # dead-slot screening of the CLEAN candidate output (v042 class)
            slot_checks = declspec.dead_slot_checks(spec, b_clean, c_clean)
            report["slot_checks"] = slot_checks
        else:
            probes = spec_mod.perturb_regions(baseline_mod, inputs)
            slot_checks = []

        n_fail = 0
        for probe in probes:
            name = probe["name"]
            base_inputs = probe.get("base_inputs") or inputs
            mask = np.asarray(probe["affected_mask"], dtype=bool)
            b0, c0 = outputs_for(tuple(base_inputs))
            b1 = np.asarray(jax.block_until_ready(fb(*probe["inputs"])))
            c1 = np.asarray(jax.block_until_ready(fc(*probe["inputs"])))
            unaffected = ~mask

            rec = {"name": name,
                   "affected_elems": int(mask.sum()),
                   "unaffected_elems": int(unaffected.sum())}
            if "axis" in probe:
                rec["axis"], rec["slot"] = probe["axis"], probe["slot"]

            # spec sanity — baseline must be silent on the unaffected set
            base_silent = bit_identical(b0, b1, unaffected)
            rec["baseline_unaffected_bit_identical"] = base_silent
            if not base_silent:
                rec["status"] = "SPEC_ERROR"
                rec["detail"] = ("baseline moved on the declared-unaffected set — "
                                 "the spec's mask is wrong for this workload")
                report["probes"].append(rec)
                report["status"] = "SPEC_ERROR" if report["status"] == "PASS" else report["status"]
                continue

            power = max_abs_delta(b0, b1, mask)
            rec["baseline_power_max_abs"] = power
            if mask.any() and power <= threshold:
                rec["status"] = "SPEC_ERROR"
                rec["detail"] = "probe has no power: baseline response %.3g <= %.3g" % (
                    power, threshold)
                report["probes"].append(rec)
                report["status"] = "SPEC_ERROR" if report["status"] == "PASS" else report["status"]
                continue

            cand_silent_ok = bit_identical(c0, c1, unaffected)
            cand_leak = 0.0 if cand_silent_ok else max_abs_delta(c0, c1, unaffected)
            cand_resp = max_abs_delta(c0, c1, mask)
            cand_resp_ok = (not mask.any()) or cand_resp > threshold

            rec["candidate_unaffected_bit_identical"] = cand_silent_ok
            rec["candidate_unaffected_leak_max_abs"] = cand_leak
            rec["candidate_affected_response_max_abs"] = cand_resp
            rec["candidate_responds"] = cand_resp_ok
            ok = cand_silent_ok and cand_resp_ok
            rec["status"] = "OK" if ok else "FAIL"
            if not ok:
                n_fail += 1
                detail = []
                if not cand_silent_ok:
                    detail.append("leak into unaffected set (max_abs %.3g)" % cand_leak)
                if not cand_resp_ok:
                    detail.append("no response on affected set (max_abs %.3g <= %.3g)"
                                  % (cand_resp, threshold))
                rec["detail"] = "; ".join(detail)
                report["violations"].append("probe %s: %s" % (name, rec["detail"]))
            report["probes"].append(rec)

        # dead-slot screening results (declarative specs only)
        for chk in slot_checks:
            if chk["status"] == "FAIL":
                n_fail += 1
                report["violations"].append(
                    "dead slot %s: %s" % (chk["name"], chk["detail"]))
            elif chk["status"] == "SPEC_ERROR" and report["status"] == "PASS":
                report["status"] = "SPEC_ERROR"

        if declarative:
            report["axes"] = _axes_table(spec, report["probes"], slot_checks)

        if n_fail:
            report["status"] = "FAIL"
        report["n_probes"] = len(report["probes"])
        report["n_slot_checks"] = len(slot_checks)
        report["n_fail"] = n_fail
    except Exception:
        report["status"] = "FAIL"
        report["exception"] = traceback.format_exc()
    return report


def _axes_table(spec: dict, probes: list, slot_checks: list) -> list[dict]:
    """Per-axis pass/fail rollup with the failing slots named."""
    table = []
    for ax in spec["axes"]:
        name = ax["name"]
        failing = sorted(
            {r["slot"] for r in probes if r.get("axis") == name and r["status"] == "FAIL"}
            | {c["slot"] for c in slot_checks if c["axis"] == name and c["status"] == "FAIL"})
        spec_errors = sorted(
            {r.get("slot") for r in probes
             if r.get("axis") == name and r["status"] == "SPEC_ERROR"}
            | {c["slot"] for c in slot_checks
               if c["axis"] == name and c["status"] == "SPEC_ERROR"})
        table.append({"axis": name, "size": int(ax["size"]),
                      "status": ("FAIL" if failing else
                                 "SPEC_ERROR" if spec_errors else "OK"),
                      "failing_slots": failing,
                      "spec_error_slots": [s for s in spec_errors if s is not None]})
    return table
