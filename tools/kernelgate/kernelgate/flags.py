"""4-leg flag-fairness harness (kgate flags) — the 37k both-flagged trap killer.

A TPU flag (LIBTPU_INIT_ARGS, XLA_FLAGS, ...) is PROCESS-GLOBAL: it only
takes effect when the environment is set before jax/libtpu initializes.
Exporting the flag once in the surrounding shell and then "comparing baseline
vs candidate" applies it to BOTH legs — the 2026-07-17 37k incident measured
naive-under-flag vs cand-under-flag and self-reported 1.00x for what was
really a 1.49x flag win.

kgate flags runs FOUR legs, each in its own fresh child process (fresh jax,
fresh libtpu, fresh JAX_COMPILATION_CACHE_DIR per flag value so a persistent
cache can't serve the default-compiled executable to the flagged process):

    naive-default    baseline module, default env
    naive-flagged    baseline module, flag applied
    cand-default     candidate module, default env
    cand-flagged     candidate module, flag applied

and reports BOTH framing ratios explicitly labeled:

    flag_only_ratio   = naive_default / naive_flagged   (the deployable flag win)
    kernel_cell_ratio = naive_flagged / cand_flagged    (kernel win at fixed flag)
    end_to_end_ratio  = naive_default / cand_flagged    (combined cell win)

When baseline and candidate resolve to the same module + entry (a flag-only
cell), kernel_cell_ratio compares the same graph under the same flag and is
1.00x BY CONSTRUCTION — the harness emits the trap warning and points at
flag_only_ratio. It also warns when the flag key is already set in the parent
environment (the "-default" legs would not be default — the exact 37k shell
state).

The parent process never imports jax — all device work happens in the legs —
so `kgate flags` is safe to drive from a supervisor that must not grab a chip.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile

from . import protocol  # jax-free at import time (loads lazily inside calls)

LEG_JSON_MARKER = "--- KGATE-LEG-JSON ---"
LEG_NAMES = ("naive_default", "naive_flagged", "cand_default", "cand_flagged")
DEFAULT_WARMUP = 5
DEFAULT_N = 20

RATIO_DEFINITIONS = {
    "flag_only_ratio": "naive_default_p50 / naive_flagged_p50 — the flag's own "
                       "effect on the unmodified graph (the deployable flag win)",
    "kernel_cell_ratio": "naive_flagged_p50 / cand_flagged_p50 — the candidate's "
                         "effect with the flag held fixed on both legs",
    "end_to_end_ratio": "naive_default_p50 / cand_flagged_p50 — combined "
                        "flag+kernel cell vs the true default baseline",
}


def parse_flag(flag: str) -> tuple[str, str]:
    if "=" not in flag:
        raise ValueError("bad --flag %r (want KEY=VALUE, e.g. "
                         "LIBTPU_INIT_ARGS=--xla_tpu_scoped_vmem_limit_kib=131072)" % flag)
    key, val = flag.split("=", 1)
    if not key:
        raise ValueError("bad --flag %r (empty KEY)" % flag)
    return key, val


def analyze_legs(legs: dict, same_graph: bool, flag_key: str,
                 parent_value: str | None, flag_value: str) -> tuple[dict, list, list]:
    """Pure ratio + trap analysis over the four legs' p50s.

    Returns (ratios, warnings, anomalies). Separated from the subprocess
    plumbing so the trap logic is unit-testable off-TPU.
    """
    p = {name: legs[name]["p50_ms"] for name in LEG_NAMES}
    ratios = {
        "flag_only_ratio": p["naive_default"] / p["naive_flagged"],
        "kernel_cell_ratio": p["naive_flagged"] / p["cand_flagged"],
        "end_to_end_ratio": p["naive_default"] / p["cand_flagged"],
    }
    warnings, anomalies = [], []
    if same_graph:
        warnings.append(
            "SAME-GRAPH TRAP (the 37k false-1.00x): candidate resolves to the same "
            "module+entry as the baseline, so kernel_cell_ratio (%.3fx) compares the "
            "SAME graph under the SAME flag and is 1.00x by construction. The flag's "
            "real effect is flag_only_ratio = %.3fx."
            % (ratios["kernel_cell_ratio"], ratios["flag_only_ratio"]))
    if parent_value is not None:
        if parent_value == flag_value:
            anomalies.append(
                "flag %s is already set to the flagged value in the parent "
                "environment — the '-default' legs are NOT default (the 37k "
                "shell-export state); unset it and re-run" % flag_key)
        else:
            warnings.append(
                "flag %s is already set in the parent environment (value %r) — "
                "the '-default' legs inherit it; 'default' here means "
                "parent-env, not unset" % (flag_key, parent_value))
    return ratios, warnings, anomalies


def _run_leg(name: str, module_path: str, inputs_from: str, entry: str | None,
             env: dict, seed: int | None, warmup: int, n: int,
             dtype: str | None = None) -> dict:
    cmd = [sys.executable, "-m", "kernelgate.flags", "--legrun",
           "--module", module_path, "--inputs-from", inputs_from,
           "--warmup", str(warmup), "--n", str(n)]
    if dtype:
        cmd += ["--dtype", dtype]
    if entry:
        cmd += ["--entry", entry]
    if seed is not None:
        cmd += ["--seed", str(seed)]
    proc = subprocess.run(cmd, env=env, capture_output=True, text=True)
    payload = None
    for line in reversed(proc.stdout.splitlines()):
        line = line.strip()
        if line.startswith("{"):
            try:
                payload = json.loads(line)
                break
            except json.JSONDecodeError:
                continue
    if proc.returncode != 0 or payload is None or "error" in (payload or {}):
        detail = (payload or {}).get("error") or proc.stderr[-2000:] or proc.stdout[-2000:]
        raise RuntimeError("leg %s failed (exit %d): %s" % (name, proc.returncode, detail))
    return payload


def run_flags(baseline_path: str, candidate_path: str, flag: str,
              baseline_entry: str = "workload",
              candidate_entry: str | None = None,
              seed: int | None = None,
              warmup: int = DEFAULT_WARMUP,
              n: int = DEFAULT_N,
              dtype: str | None = None) -> dict:
    """Full 4-leg pipeline. Parent stays jax-free; each leg is a fresh process."""
    import traceback
    from . import envinfo

    report = {
        "cmd": "flags",
        "baseline": {"path": os.path.abspath(baseline_path), "entry": baseline_entry},
        "candidate": {"path": os.path.abspath(candidate_path)},
        "flag": None,
        "seed": seed,
        "timing": {"warmup": warmup, "n": n},
        "legs": {},
        "ratios": {},
        "ratio_definitions": RATIO_DEFINITIONS,
        "env": envinfo.capture(include_devices=False),
        "warnings": [], "anomalies": [],
        "status": "PASS",
    }
    try:
        key, val = parse_flag(flag)
        parent_value = os.environ.get(key)
        report["flag"] = {"key": key, "value": val,
                          "parent_env_value": parent_value}

        cache_default = tempfile.mkdtemp(prefix="kgate-flags-cache-default-")
        cache_flagged = tempfile.mkdtemp(prefix="kgate-flags-cache-flagged-")
        report["compilation_cache_dirs"] = {"default": cache_default,
                                            "flagged": cache_flagged}
        env_default = dict(os.environ, JAX_COMPILATION_CACHE_DIR=cache_default)
        env_flagged = dict(os.environ, JAX_COMPILATION_CACHE_DIR=cache_flagged)
        env_flagged[key] = val

        legs_spec = (
            ("naive_default", report["baseline"]["path"], baseline_entry, env_default),
            ("naive_flagged", report["baseline"]["path"], baseline_entry, env_flagged),
            ("cand_default", report["candidate"]["path"], candidate_entry, env_default),
            ("cand_flagged", report["candidate"]["path"], candidate_entry, env_flagged),
        )
        for name, module_path, entry, env in legs_spec:
            leg = _run_leg(name, module_path, report["baseline"]["path"],
                           entry, env, seed, warmup, n, dtype)
            leg["flag_applied"] = name.endswith("_flagged")
            report["legs"][name] = leg
        report["candidate"]["entry"] = report["legs"]["cand_default"]["entry"]

        # All four legs must have timed the same inputs.
        input_hashes = {name: report["legs"][name]["inputs"]["combined"]
                        for name in LEG_NAMES}
        if len(set(input_hashes.values())) != 1:
            report["anomalies"].append(
                "legs saw different inputs: %s" % input_hashes)
        report["inputs"] = report["legs"]["naive_default"]["inputs"]

        same_graph = (
            os.path.realpath(report["baseline"]["path"])
            == os.path.realpath(report["candidate"]["path"])
            and report["legs"]["naive_default"]["entry"]
            == report["legs"]["cand_default"]["entry"])
        report["same_graph"] = same_graph

        p50s = {name: {"p50_ms": report["legs"][name]["stats"]["p50_ms"]}
                for name in LEG_NAMES}
        for name in LEG_NAMES:
            report["legs"][name]["p50_ms"] = p50s[name]["p50_ms"]
        ratios, warnings, anomalies = analyze_legs(
            p50s, same_graph, key, parent_value, val)
        report["ratios"] = ratios
        report["warnings"] += warnings
        report["anomalies"] += anomalies
        if report["anomalies"]:
            report["status"] = "ANOMALY"
    except Exception:
        report["status"] = "FAIL"
        report["exception"] = traceback.format_exc()
    return report


# --------------------------------------------------------------------- legrun
# One timed leg, executed in a fresh child process so the flag env and the
# compilation cache dir take effect before jax initializes.

def _legrun_main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(prog="kernelgate.flags --legrun")
    ap.add_argument("--legrun", action="store_true", required=True)
    ap.add_argument("--module", required=True)
    ap.add_argument("--inputs-from", required=True)
    ap.add_argument("--entry", default=None)
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--warmup", type=int, default=DEFAULT_WARMUP)
    ap.add_argument("--n", type=int, default=DEFAULT_N)
    ap.add_argument("--dtype", default=None)
    ap.add_argument("--trace-dir", default=None,
                    help="wrap execution in jax.profiler.trace(DIR) — used by "
                         "kgate verify's capture leg (timing discarded there)")
    args = ap.parse_args(argv)
    try:
        import contextlib
        import jax
        from . import envinfo, timing
        if args.dtype and args.dtype != "module":
            import jax.numpy as _jnp
            protocol.GRADED_DTYPE = getattr(_jnp, args.dtype)
        src = protocol.load_module(args.inputs_from)
        mod = src if os.path.realpath(args.module) == os.path.realpath(
            args.inputs_from) else protocol.load_module(args.module)
        inputs = protocol.make_inputs(src, seed=args.seed)
        name, fn = protocol.resolve_entry(mod, args.entry, len(inputs))
        f = protocol.as_jitted(fn)
        tracer = (jax.profiler.trace(args.trace_dir) if args.trace_dir
                  else contextlib.nullcontext())
        with tracer:
            out = f(*inputs)
            jax.block_until_ready(out)
            out_sha = protocol.sha256_output(out)
            del out
            timer = timing._timer(f, inputs)
            for _ in range(args.warmup):
                timer()
            times = [timer() for _ in range(args.n)]
        payload = {
            "module": os.path.abspath(args.module),
            "entry": name,
            "stats": timing.leg_stats(times),
            "inputs": protocol.sha256_arrays(inputs),
            "output_sha256": out_sha,
            "env": envinfo.capture(),
        }
    except Exception:
        import traceback
        print(LEG_JSON_MARKER)
        print(json.dumps({"error": traceback.format_exc()}))
        return 1
    print(LEG_JSON_MARKER)
    print(json.dumps(payload, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(_legrun_main())
