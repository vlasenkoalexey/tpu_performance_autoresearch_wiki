"""Speed-of-light roofline gate.

A measured p50 FASTER than the physical bound (compute roofline or memory
roofline, whichever binds) is impossible — it means the kernel did not do the
work (skipped blocks, cached result, timing evasion). GPU MODE KernelBot uses
this as a prize gate; here it is a hard INVALID.

FLOP/byte counts are supplied by the caller (see the README's family formula
table, which follows the JAXBench harness accounting). Peaks default from the
device kind recorded in the measure JSON; override with --peak-tflops /
--peak-gbps.
"""
from __future__ import annotations

# Per-chip peaks: (bf16 dense TFLOP/s, HBM GB/s). Public spec numbers.
DEVICE_PEAKS = {
    "v6e": (918.0, 1640.0),   # Trillium
    "v6":  (918.0, 1640.0),
    "v5p": (459.0, 2765.0),
    "v5e": (197.0, 819.0),
    "v4":  (275.0, 1228.0),
}


def peaks_for_device(kind: str | None):
    if not kind:
        return None
    k = kind.lower().replace(" ", "")
    # match longest key first so "v5p" wins over "v5"
    for key in sorted(DEVICE_PEAKS, key=len, reverse=True):
        if key in k:
            return DEVICE_PEAKS[key]
    return None


def run_roofline(measure_report: dict, flops: float, bytes_moved: float,
                 peak_tflops: float | None = None,
                 peak_gbps: float | None = None,
                 leg: str = "candidate") -> dict:
    kind = (measure_report.get("env", {}).get("devices", {}) or {}).get("kind")
    if peak_tflops is None or peak_gbps is None:
        found = peaks_for_device(kind)
        if found is None:
            return {"cmd": "roofline", "status": "ERROR",
                    "error": "unknown device kind %r — pass --peak-tflops and --peak-gbps" % kind}
        peak_tflops = peak_tflops if peak_tflops is not None else found[0]
        peak_gbps = peak_gbps if peak_gbps is not None else found[1]

    p50_ms = measure_report["timing"]["pooled"][leg]["p50_ms"]
    compute_bound_ms = flops / (peak_tflops * 1e12) * 1e3
    memory_bound_ms = bytes_moved / (peak_gbps * 1e9) * 1e3
    bound_ms = max(compute_bound_ms, memory_bound_ms)
    invalid = p50_ms < bound_ms

    achieved_tflops = flops / (p50_ms / 1e3) / 1e12
    achieved_gbps = bytes_moved / (p50_ms / 1e3) / 1e9
    return {
        "cmd": "roofline",
        "leg": leg,
        "device_kind": kind,
        "flops": flops,
        "bytes": bytes_moved,
        "peak_tflops": peak_tflops,
        "peak_gbps": peak_gbps,
        "measured_p50_ms": p50_ms,
        "compute_bound_ms": compute_bound_ms,
        "memory_bound_ms": memory_bound_ms,
        "speed_of_light_ms": bound_ms,
        "binding_resource": "compute" if compute_bound_ms >= memory_bound_ms else "memory",
        "achieved_tflops": achieved_tflops,
        "achieved_gbps": achieved_gbps,
        "utilization_pct": 100.0 * bound_ms / p50_ms,
        "status": "INVALID" if invalid else "PASS",
        "detail": ("measured p50 %.4f ms is FASTER than the speed-of-light bound %.4f ms — "
                   "the kernel cannot have done the declared work" % (p50_ms, bound_ms))
                  if invalid else None,
    }
