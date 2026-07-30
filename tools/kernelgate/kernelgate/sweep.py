"""Parity-gated grid sweep over candidate kernel static parameters.

Each grid point is (1) quick-parity-gated on one seed against the parity
oracle (fp32, with the same fp64 escalation as `kgate parity` for
HIGHEST-class baselines; computed ONCE and reused — it depends only on the
inputs),
then (2) timed. A config that fails parity is never timed and never eligible
for argmin — the table records it as PARITY_FAIL. A config that crashes
(e.g. a block shape Mosaic rejects) is recorded as ERROR with the message,
and the sweep continues.
"""
from __future__ import annotations

import functools
import itertools
import time

from . import parity, protocol, timing


def parse_params(spec: str) -> list[dict]:
    """"bq=512,1024;bk=128,256" -> [{'bq':512,'bk':128}, ...] (full grid)."""
    axes = []
    for part in spec.split(";"):
        part = part.strip()
        if not part:
            continue
        key, vals = part.split("=", 1)
        parsed = []
        for v in vals.split(","):
            v = v.strip()
            try:
                parsed.append(int(v))
            except ValueError:
                try:
                    parsed.append(float(v))
                except ValueError:
                    parsed.append(v)
        axes.append((key.strip(), parsed))
    grid = []
    for combo in itertools.product(*[v for _, v in axes]):
        grid.append({k: c for (k, _), c in zip(axes, combo)})
    return grid


def run_sweep(baseline_mod, candidate_mod, params_spec: str,
              baseline_entry: str = "workload",
              candidate_entry: str | None = None,
              seed: int | None = None,
              multiplier: float = parity.DEFAULT_MULTIPLIER,
              chunk: dict | None = None,
              chunk_out_axis: int = 0,
              n_min: int = 10, n_max: int = 50,
              warmup: int = 5,
              se_target: float = timing.DEFAULT_SE_TARGET) -> dict:
    import traceback
    import numpy as np
    import jax
    from . import envinfo

    grid = parse_params(params_spec)
    report = {
        "cmd": "sweep",
        "baseline": {"path": baseline_mod.__kgate_path__},
        "candidate": {"path": candidate_mod.__kgate_path__},
        "config": protocol.get_config(baseline_mod),
        "params": params_spec,
        "multiplier": multiplier,
        "env": envinfo.capture(),
        "grid": [],
        "status": "PASS",
    }
    try:
        inputs = protocol.make_inputs(baseline_mod, seed=seed)
        n_inputs = len(inputs)
        b_name, b_fn = protocol.resolve_entry(baseline_mod, baseline_entry, n_inputs)
        c_name, c_fn = protocol.resolve_entry(candidate_mod, candidate_entry, n_inputs)
        report["baseline"]["entry"] = b_name
        report["candidate"]["entry"] = c_name
        fb = protocol.as_jitted(b_fn)

        # Oracle + floor once for the whole sweep (fp64 escalation applies —
        # a HIGHEST-class baseline would otherwise PARITY_FAIL every config).
        naive = np.asarray(jax.block_until_ready(fb(*inputs)))
        oracle, floor, oracle_used, oracle_why = parity.oracle_with_floor(
            fb, naive, inputs, chunk, chunk_out_axis,
            highest_hint=parity.detect_highest_precision(baseline_mod))
        report["floor_baseline_vs_oracle"] = floor
        report["oracle_used"] = oracle_used
        if oracle_why:
            report["oracle_reason"] = oracle_why

        # Baseline timing once (candidate legs are timed per config).
        tb = timing._timer(fb, inputs)
        for _ in range(warmup):
            tb()
        base_times = [tb() for _ in range(max(n_min, 20))]
        report["baseline_timing"] = timing.leg_stats(base_times)
        base_p50 = report["baseline_timing"]["p50_ms"]

        best = None
        for combo in grid:
            rec = {"params": combo}
            try:
                fn = protocol.as_jitted(functools.partial(c_fn, **combo))
                out = jax.block_until_ready(fn(*inputs))
                cand_host = np.asarray(out)
                del out
                stats = parity.diff_stats(cand_host, oracle)
                g = parity.gate(stats, floor, multiplier)
                rec["parity"] = {"candidate_vs_oracle": stats, "gate": g}
                if not g["ok"]:
                    rec["status"] = "PARITY_FAIL"
                    report["grid"].append(rec)
                    continue
                tc = timing._timer(fn, inputs)
                for _ in range(warmup):
                    tc()
                times = []
                while True:
                    times.append(tc())
                    if len(times) >= n_max:
                        break
                    if len(times) >= n_min and timing.check_converged(times, se_target):
                        break
                rec["timing"] = timing.leg_stats(times)
                rec["speedup_p50_vs_baseline"] = base_p50 / rec["timing"]["p50_ms"]
                rec["status"] = "OK"
                if best is None or rec["timing"]["p50_ms"] < best["timing"]["p50_ms"]:
                    best = rec
            except Exception:
                rec["status"] = "ERROR"
                rec["exception"] = traceback.format_exc(limit=8)
            report["grid"].append(rec)

        if best is not None:
            report["argmin"] = {"params": best["params"],
                                "p50_ms": best["timing"]["p50_ms"],
                                "speedup_p50_vs_baseline": best["speedup_p50_vs_baseline"]}
        else:
            report["argmin"] = None
            report["status"] = "FAIL"  # nothing passed parity and timed
    except Exception:
        report["status"] = "FAIL"
        report["exception"] = traceback.format_exc()
    return report
