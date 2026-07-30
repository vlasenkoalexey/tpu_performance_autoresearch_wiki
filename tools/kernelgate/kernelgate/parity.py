"""Floor-normalized oracle parity gate (fp32 oracle, fp64 escalation).

Oracle construction: the SAME canonical (bf16) inputs are cast to float32
(floating-point leaves only; integer index/length inputs pass through) and
run through the BASELINE workload. jax x64 stays disabled — the oracle is a
float32 recompute of the exact baseline semantics on the exact input values,
not a regenerated fp32 sample (jax.random.normal in fp32 draws different
values than the bf16 draw, so re-generation would change the problem).

Floor: baseline(bf16 inputs) vs oracle — the reference's own quantization
error. Gate: candidate error <= multiplier x floor on BOTH max_abs and
mean_abs, and candidate output 100% finite. (Published precedent: the
FlashAttention test suite's `2x (out_pt - out_ref)` rule.) Guarded relative
error is reported for diagnosis but never gates — bf16 attention tails make
max_rel meaningless.

fp64 escalation (the 21k false-FAIL fix): when the baseline computes in exact
fp32 — Precision.HIGHEST matmuls, or fp32 inputs with fp32 accumulation — the
fp32 recompute oracle IS the baseline, the floor collapses to zero, and the
gate degenerates to a ~1e-6 ABSOLUTE tolerance that any correct kernel-scale
output trips (the 2026-07-16 21k incident: a verified-correct 10.7x candidate
false-FAILed kgate parity). Fix: when the fp32 floor is ~0 (below
--floor-eps), or the baseline source mentions Precision.HIGHEST, the oracle
is escalated to a float64 recompute (x64 enabled locally, run on the CPU
backend — TPUs have no f64) so the floor measures the baseline's true
rounding error and stays non-zero. The report records which oracle graded
each point (`oracle_used`).

Optional input-scale probes rescale one designated input by given factors to
sharpen conditioning (e.g. K x10 / x50 turns a flat softmax into a spiky one,
exposing streaming-softmax bugs invisible at the default operating point).
The rescaled input index comes from --scale-input or the family spec module's
SCALE_INPUT constant (default 1, i.e. K in attention families).

Any exception anywhere is a FAIL with the traceback recorded — never
swallowed into a pass.
"""
from __future__ import annotations

import re

from . import protocol

DEFAULT_MULTIPLIER = 2.0
FLOOR_EPS_FALLBACK = 1e-6  # gate atol when the floor is exactly zero
FLOOR_ZERO_EPS = 1e-9      # fp32 floor below this => escalate to the fp64 oracle
ORACLE_MODES = ("auto", "fp32", "fp64")

_HIGHEST_RE = re.compile(
    r"Precision\.HIGHEST|precision\s*=\s*['\"]highest['\"]")


def detect_highest_precision(mod) -> bool:
    """Static sniff: does the baseline source mention Precision.HIGHEST?

    Advisory trigger only — the authoritative trigger is the measured fp32
    floor collapsing below FLOOR_ZERO_EPS (a HIGHEST baseline is fp32-exact,
    so its fp32-recompute floor is identically zero).
    """
    path = getattr(mod, "__kgate_path__", None)
    if not path:
        return False
    try:
        with open(path) as f:
            return bool(_HIGHEST_RE.search(f.read()))
    except OSError:
        return False


def _cast_fp32(inputs):
    import jax.numpy as jnp
    out = []
    for x in inputs:
        if hasattr(x, "dtype") and jnp.issubdtype(x.dtype, jnp.floating):
            out.append(x.astype(jnp.float32))
        else:
            out.append(x)
    return tuple(out)


def _cast_fp64(inputs):
    """Host-side cast to float64 — must run INSIDE an enable_x64 scope
    (outside one, jnp silently truncates f64 back to f32)."""
    import numpy as np
    import jax.numpy as jnp
    out = []
    for x in inputs:
        if hasattr(x, "dtype") and jnp.issubdtype(x.dtype, jnp.floating):
            out.append(jnp.asarray(np.asarray(x).astype(np.float64)))
        else:
            out.append(x)
    return tuple(out)


def parse_chunk_spec(spec: str | None):
    """"0:0,1:0,2:0" -> {input_index: axis} for size-1-slice oracle chunking."""
    if not spec:
        return None
    out = {}
    for part in spec.split(","):
        idx, axis = part.split(":")
        out[int(idx)] = int(axis)
    return out


def _run_entry_chunked(entry, inputs, chunk: dict | None, out_axis: int):
    import jax
    import jax.numpy as jnp
    if not chunk:
        out = entry(*inputs)
        jax.block_until_ready(out)
        return out
    n = inputs[list(chunk)[0]].shape[chunk[list(chunk)[0]]]
    outs = []
    for i in range(n):
        sl = []
        for j, x in enumerate(inputs):
            if j in chunk:
                ax = chunk[j]
                sl.append(jax.lax.slice_in_dim(x, i, i + 1, axis=ax))
            else:
                sl.append(x)
        outs.append(entry(*sl))
    out = jnp.concatenate(outs, axis=out_axis)
    jax.block_until_ready(out)
    return out


def run_oracle(entry, inputs, chunk: dict | None, out_axis: int = 0,
               oracle: str = "fp32"):
    """Run the higher-precision oracle, optionally chunked into size-1 slices.

    oracle="fp32": float leaves cast to float32, baseline re-run in-process
    (x64 stays disabled). oracle="fp64": float leaves cast to float64 under a
    scoped enable_x64, executed on the CPU backend (TPUs do not support f64)
    — the HIGHEST-baseline escape hatch.

    Chunking slices the listed inputs along their given axes one element at a
    time and concatenates outputs along out_axis — used when the full-shape
    high-precision intermediate would not fit memory (e.g. batched full-S^2
    attention). Only valid when the chunk axis is batch-like (no cross-slice
    interaction); the caller asserts that by passing --chunk.
    """
    import jax
    if oracle == "fp64":
        with jax.enable_x64():
            with jax.default_device(jax.devices("cpu")[0]):
                return _run_entry_chunked(entry, _cast_fp64(inputs), chunk, out_axis)
    return _run_entry_chunked(entry, _cast_fp32(inputs), chunk, out_axis)


def oracle_with_floor(entry, naive_host, inputs, chunk: dict | None,
                      out_axis: int = 0, oracle_mode: str = "auto",
                      floor_eps: float = FLOOR_ZERO_EPS,
                      highest_hint: bool = False):
    """Pick the oracle, compute it, and return (oracle_host, floor, used, why).

    auto: fp32 first; escalate to fp64 when the baseline source sniffs as
    Precision.HIGHEST or the fp32 floor max_abs falls below floor_eps (both
    mean the fp32 recompute IS the baseline and the floor is meaningless).
    """
    import numpy as np
    if oracle_mode not in ORACLE_MODES:
        raise ValueError("oracle_mode %r not in %s" % (oracle_mode, ORACLE_MODES))
    if oracle_mode == "fp64" or (oracle_mode == "auto" and highest_hint):
        why = ("forced by --oracle fp64" if oracle_mode == "fp64"
               else "baseline source uses Precision.HIGHEST")
        o = np.asarray(run_oracle(entry, inputs, chunk, out_axis, oracle="fp64"))
        return o, diff_stats(naive_host, o), "fp64", why
    o32 = np.asarray(run_oracle(entry, inputs, chunk, out_axis))
    floor32 = diff_stats(naive_host, o32)
    if oracle_mode == "auto" and floor32["max_abs"] < floor_eps:
        why = ("fp32 floor max_abs %.3g < %.3g — fp32 oracle is the baseline "
               "(HIGHEST-class), escalating to fp64" % (floor32["max_abs"], floor_eps))
        o64 = np.asarray(run_oracle(entry, inputs, chunk, out_axis, oracle="fp64"))
        return o64, diff_stats(naive_host, o64), "fp64", why
    return o32, floor32, "fp32", None


def diff_stats(a, ref) -> dict:
    """Error metrics of a vs ref, computed in float64 on host."""
    import numpy as np
    a = np.asarray(a).astype(np.float64)
    ref = np.asarray(ref).astype(np.float64)
    d = np.abs(a - ref)
    finite = float(np.mean(np.isfinite(np.asarray(a))))
    return {
        "max_abs": float(np.max(d)),
        "mean_abs": float(np.mean(d)),
        "max_rel_guarded": float(np.max(d / np.maximum(np.abs(ref), 1e-5))),
        "finite_fraction": finite,
    }


def gate(cand: dict, floor: dict, multiplier: float) -> dict:
    fm = floor["max_abs"] if floor["max_abs"] > 0 else FLOOR_EPS_FALLBACK
    fmean = floor["mean_abs"] if floor["mean_abs"] > 0 else FLOOR_EPS_FALLBACK
    ok_max = cand["max_abs"] <= multiplier * fm
    ok_mean = cand["mean_abs"] <= multiplier * fmean
    ok_fin = cand["finite_fraction"] == 1.0
    return {
        "multiplier": multiplier,
        "max_abs_ratio_vs_floor": cand["max_abs"] / fm,
        "mean_abs_ratio_vs_floor": cand["mean_abs"] / fmean,
        "max_abs_ok": ok_max,
        "mean_abs_ok": ok_mean,
        "finite_ok": ok_fin,
        "floor_was_zero": floor["max_abs"] == 0.0,
        "ok": ok_max and ok_mean and ok_fin,
    }


def _one_point(fb, fc, inputs, chunk, out_axis, multiplier,
               oracle_mode: str = "auto", floor_eps: float = FLOOR_ZERO_EPS,
               highest_hint: bool = False):
    """candidate-first evaluation of one input point. Returns record dict."""
    import jax
    protocol.poison_buffers(fb, inputs)
    out_c = fc(*inputs)
    jax.block_until_ready(out_c)
    import numpy as np
    cand_host = np.asarray(out_c)
    del out_c
    out_b = fb(*inputs)
    jax.block_until_ready(out_b)
    naive_host = np.asarray(out_b)
    del out_b
    oracle, floor, used, why = oracle_with_floor(
        fb, naive_host, inputs, chunk, out_axis,
        oracle_mode=oracle_mode, floor_eps=floor_eps, highest_hint=highest_hint)
    cand = diff_stats(cand_host, oracle)
    vs_naive = diff_stats(cand_host, naive_host)
    g = gate(cand, floor, multiplier)
    rec = {
        "oracle_used": used,
        "floor_baseline_vs_oracle": floor,
        "candidate_vs_oracle": cand,
        "candidate_vs_baseline": vs_naive,
        "outputs_sha256": {"baseline": protocol.sha256_output(naive_host),
                           "candidate": protocol.sha256_output(cand_host)},
        "gate": g,
    }
    if why:
        rec["oracle_reason"] = why
    return rec


def run_parity(baseline_mod, candidate_mod,
               baseline_entry: str = "workload",
               candidate_entry: str | None = None,
               seeds=(42, 43),
               multiplier: float = DEFAULT_MULTIPLIER,
               chunk: dict | None = None,
               chunk_out_axis: int = 0,
               scale_probes=(),
               scale_input: int | None = None,
               spec_mod=None,
               oracle: str = "auto",
               floor_eps: float = FLOOR_ZERO_EPS) -> dict:
    """Full parity pipeline; raises nothing — exceptions become FAIL records."""
    import traceback
    from . import envinfo

    highest_hint = detect_highest_precision(baseline_mod)
    report = {
        "cmd": "parity",
        "baseline": {"path": baseline_mod.__kgate_path__, "entry": baseline_entry},
        "candidate": {"path": candidate_mod.__kgate_path__},
        "config": protocol.get_config(baseline_mod),
        "multiplier": multiplier,
        "oracle": {
            "strategy": "baseline workload re-run on higher-precision-cast canonical "
                        "inputs (float leaves cast, integer leaves passed through); "
                        "fp32 in-process, escalated to fp64-on-CPU when the fp32 "
                        "floor is ~0 (HIGHEST-class baseline)",
            "mode": oracle,
            "floor_eps": floor_eps,
            "baseline_highest_detected": highest_hint,
            "chunk": {str(k): v for k, v in (chunk or {}).items()} or None,
        },
        "env": envinfo.capture(),
        "seeds": {}, "scale_probes": {},
        "status": "PASS",
    }
    try:
        inputs0 = protocol.make_inputs(baseline_mod)
        n_inputs = len(inputs0)
        b_name, b_fn = protocol.resolve_entry(baseline_mod, baseline_entry, n_inputs)
        c_name, c_fn = protocol.resolve_entry(candidate_mod, candidate_entry, n_inputs)
        report["baseline"]["entry"] = b_name
        report["candidate"]["entry"] = c_name
        fb = protocol.as_jitted(b_fn)
        fc = protocol.as_jitted(c_fn)

        for seed in seeds:
            inputs = protocol.make_inputs(baseline_mod, seed=seed)
            if str(seed) == str(seeds[0]):
                report["inputs"] = protocol.sha256_arrays(inputs)
            rec = _one_point(fb, fc, inputs, chunk, chunk_out_axis, multiplier,
                             oracle_mode=oracle, floor_eps=floor_eps,
                             highest_hint=highest_hint)
            report["seeds"][str(seed)] = rec
            if not rec["gate"]["ok"]:
                report["status"] = "FAIL"
            del inputs

        if scale_probes:
            idx = scale_input
            if idx is None:
                idx = getattr(spec_mod, "SCALE_INPUT", 1) if spec_mod is not None else 1
            report["oracle"]["scale_input_index"] = idx
            base_inputs = protocol.make_inputs(baseline_mod, seed=seeds[0])
            for factor in scale_probes:
                probed = list(base_inputs)
                probed[idx] = probed[idx] * factor
                rec = _one_point(fb, fc, tuple(probed), chunk, chunk_out_axis,
                                 multiplier, oracle_mode=oracle,
                                 floor_eps=floor_eps, highest_hint=highest_hint)
                report["scale_probes"]["x%g" % factor] = rec
                if not rec["gate"]["ok"]:
                    report["status"] = "FAIL"
        report["oracle"]["used"] = sorted({
            rec["oracle_used"]
            for group in (report["seeds"], report["scale_probes"])
            for rec in group.values()})
    except Exception:
        report["status"] = "FAIL"
        report["exception"] = traceback.format_exc()
    return report
