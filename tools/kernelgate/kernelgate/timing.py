"""Co-measured interleaved timing with adaptive trial count and both orderings.

Discipline (from the campaign verifier batteries, plus published hardening):
- baseline and candidate are timed INTERLEAVED within each iteration, in the
  same process, on the same input buffers (co-measured);
- BOTH orderings are run: ordering A times the candidate FIRST inside each
  iteration (candidate-before-reference — the Kevin rule), ordering B times
  the baseline first;
- adaptive trial count per ordering: start at n_min/leg, stop when BOTH legs
  reach SE/mean < se_target, hard cap n_max (GPU MODE KernelBot rule);
- every call is fenced with jax.block_until_ready;
- the allocator is poisoned with NaN output-shaped buffers before the
  candidate's first execution, and the candidate runs before the baseline
  ever runs in the process;
- input arrays are hashed before and after — any mutation is an anomaly.
"""
from __future__ import annotations

import math
import time

from . import protocol

DEFAULT_N_MIN = 30
DEFAULT_N_MAX = 120
DEFAULT_SE_TARGET = 0.001
DEFAULT_WARMUP = 10
DISPATCH_WINDOW_MS = 1.0   # KernelBench-v0.1-style minimum-runtime sizing flag
ORDERING_TOLERANCE = 0.15  # relative disagreement between ordering speedups


def check_converged(times_ms, se_target: float = DEFAULT_SE_TARGET) -> bool:
    """Standard-error-of-the-mean over mean below target (KernelBot stop rule).

    Pure function so the stopping logic is unit-testable off-TPU.
    """
    n = len(times_ms)
    if n < 2:
        return False
    mean = sum(times_ms) / n
    if mean <= 0:
        return False
    var = sum((t - mean) ** 2 for t in times_ms) / (n - 1)
    se = math.sqrt(var / n)
    return (se / mean) < se_target


def adaptive_interleaved(time_first, time_second,
                         n_min: int = DEFAULT_N_MIN,
                         n_max: int = DEFAULT_N_MAX,
                         se_target: float = DEFAULT_SE_TARGET):
    """Run interleaved timing pairs until both legs converge or n_max.

    time_first / time_second are zero-arg callables returning one timed
    iteration in ms (injectable for unit tests).
    Returns (times_first, times_second, converged).
    """
    tf, ts = [], []
    while True:
        tf.append(time_first())
        ts.append(time_second())
        n = len(tf)
        if n >= n_max:
            return tf, ts, check_converged(tf, se_target) and check_converged(ts, se_target)
        if n >= n_min and check_converged(tf, se_target) and check_converged(ts, se_target):
            return tf, ts, True


def leg_stats(times_ms) -> dict:
    import numpy as np
    a = np.asarray(times_ms, dtype=float)
    return {
        "p50_ms": float(np.percentile(a, 50)),
        "mean_ms": float(a.mean()),
        "std_ms": float(a.std()),
        "min_ms": float(a.min()),
        "n": int(a.size),
    }


def _timer(fn, args):
    import jax

    def one() -> float:
        t0 = time.perf_counter()
        jax.block_until_ready(fn(*args))
        return (time.perf_counter() - t0) * 1e3
    return one


def run_measure(baseline_mod, candidate_mod,
                baseline_entry: str = "workload",
                candidate_entry: str | None = None,
                seed: int | None = None,
                warmup: int = DEFAULT_WARMUP,
                n_min: int = DEFAULT_N_MIN,
                n_max: int = DEFAULT_N_MAX,
                se_target: float = DEFAULT_SE_TARGET) -> dict:
    """Full measure pipeline. Returns the report dict (status PASS/ANOMALY)."""
    import jax
    import jax.numpy as jnp
    import numpy as np
    from . import envinfo

    anomalies, warnings = [], []

    inputs = protocol.make_inputs(baseline_mod, seed=seed)
    n_inputs = len(inputs)
    b_name, b_fn = protocol.resolve_entry(baseline_mod, baseline_entry, n_inputs)
    c_name, c_fn = protocol.resolve_entry(candidate_mod, candidate_entry, n_inputs)
    fb = protocol.as_jitted(b_fn)
    fc = protocol.as_jitted(c_fn)

    hashes_before = protocol.hash_arrays(inputs)

    # Poison allocator, then candidate executes FIRST in this process.
    poison = protocol.poison_buffers(fb, inputs)
    out_c = fc(*inputs)
    jax.block_until_ready(out_c)
    finite = all(bool(jnp.all(jnp.isfinite(x))) for x in jax.tree_util.tree_leaves(out_c)
                 if jnp.issubdtype(x.dtype, jnp.floating))
    if not finite:
        anomalies.append("candidate output contains non-finite values")
    out_b = fb(*inputs)
    jax.block_until_ready(out_b)
    shapes_match = jax.tree_util.tree_structure(out_b) == jax.tree_util.tree_structure(out_c) \
        and all(a.shape == b.shape for a, b in zip(jax.tree_util.tree_leaves(out_b),
                                                   jax.tree_util.tree_leaves(out_c)))
    if not shapes_match:
        anomalies.append("output shape/structure mismatch between baseline and candidate")
    outputs_sha256 = {"baseline": protocol.sha256_output(out_b),
                      "candidate": protocol.sha256_output(out_c)}
    del out_b, out_c

    for _ in range(warmup):
        jax.block_until_ready(fc(*inputs))
        jax.block_until_ready(fb(*inputs))

    tb = _timer(fb, inputs)
    tc = _timer(fc, inputs)

    # Ordering A: candidate first inside each iteration (Kevin rule).
    ta_c, ta_b, conv_a = adaptive_interleaved(tc, tb, n_min, n_max, se_target)
    # Ordering B: baseline first inside each iteration.
    tb_b, tb_c, conv_b = adaptive_interleaved(tb, tc, n_min, n_max, se_target)

    hashes_after = protocol.hash_arrays(inputs)
    mutated = [h["index"] for h, g in zip(hashes_before, hashes_after) if h["md5"] != g["md5"]]
    if mutated:
        anomalies.append("input arrays mutated during measurement: indices %s" % mutated)

    sa_c, sa_b = leg_stats(ta_c), leg_stats(ta_b)
    sb_c, sb_b = leg_stats(tb_c), leg_stats(tb_b)
    speedup_a = sa_b["p50_ms"] / sa_c["p50_ms"]
    speedup_b = sb_b["p50_ms"] / sb_c["p50_ms"]

    pooled_b = leg_stats(ta_b + tb_b)
    pooled_c = leg_stats(ta_c + tb_c)
    pooled_speedup = pooled_b["p50_ms"] / pooled_c["p50_ms"]

    rel = abs(speedup_a - speedup_b) / ((speedup_a + speedup_b) / 2)
    if rel > ORDERING_TOLERANCE:
        anomalies.append(
            "ordering-dependent timing: speedup A=%.3fx vs B=%.3fx (rel diff %.1f%% > %.0f%%)"
            % (speedup_a, speedup_b, rel * 100, ORDERING_TOLERANCE * 100))
    if not (conv_a and conv_b):
        warnings.append("SE/mean did not reach %g before n_max=%d" % (se_target, n_max))
    if pooled_c["p50_ms"] < DISPATCH_WINDOW_MS:
        warnings.append(
            "candidate p50 %.3f ms below %.1f ms dispatch window — result may be "
            "dispatch-dominated; consider a larger op-point"
            % (pooled_c["p50_ms"], DISPATCH_WINDOW_MS))
    if min(pooled_b["min_ms"], pooled_c["min_ms"]) <= 0:
        anomalies.append("non-positive iteration time observed")

    report = {
        "cmd": "measure",
        "baseline": {"path": baseline_mod.__kgate_path__, "entry": b_name},
        "candidate": {"path": candidate_mod.__kgate_path__, "entry": c_name},
        "config": protocol.get_config(baseline_mod),
        "seed": seed,
        "inputs": protocol.sha256_arrays(inputs),
        "outputs_sha256": outputs_sha256,
        "env": envinfo.capture(),
        "timing": {
            "warmup": warmup, "n_min": n_min, "n_max": n_max, "se_target": se_target,
            "ordering_A_candidate_first": {
                "candidate": sa_c, "baseline": sa_b, "converged": conv_a,
                "speedup_p50": speedup_a},
            "ordering_B_baseline_first": {
                "candidate": sb_c, "baseline": sb_b, "converged": conv_b,
                "speedup_p50": speedup_b},
            "pooled": {"baseline": pooled_b, "candidate": pooled_c,
                       "speedup_p50": pooled_speedup},
        },
        "checks": {
            "candidate_ran_first": True,
            "allocator_poison": poison,
            "output_finite": finite,
            "output_shapes_match": shapes_match,
            "input_mutation": {"mutated_indices": mutated, "ok": not mutated},
            "ordering_consistency": {"rel_diff": rel, "ok": rel <= ORDERING_TOLERANCE},
        },
        "anomalies": anomalies,
        "warnings": warnings,
        "status": "PASS" if not anomalies else "ANOMALY",
    }
    return report
