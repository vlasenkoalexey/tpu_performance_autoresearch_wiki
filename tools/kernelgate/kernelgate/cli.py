"""kgate command-line interface (the KernelGate CLI).

Exit codes: 0 = PASS/CLEAN, 1 = advisory lint findings, 2 = gate FAIL /
anomaly / INVALID / error.

--chip-env KEY=VAL (repeatable, on the TPU-executing commands) re-execs the
command in a child process with those variables set BEFORE jax is imported —
the only way env like LIBTPU_INIT_ARGS or TPU_VISIBLE_DEVICES can take
effect. The re-exec is recorded via KGATE_REEXEC=1.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys

from . import EXIT_ADVISORY, EXIT_FAIL, EXIT_PASS, report as report_mod


def _maybe_reexec(args) -> int | None:
    """If --chip-env was given and we're not already the child, re-exec."""
    chip_env = getattr(args, "chip_env", None)
    if not chip_env or os.environ.get("KGATE_REEXEC") == "1":
        return None
    env = dict(os.environ)
    for kv in chip_env:
        if "=" not in kv:
            print("bad --chip-env %r (want KEY=VAL)" % kv, file=sys.stderr)
            return EXIT_FAIL
        k, v = kv.split("=", 1)
        env[k] = v
    env["KGATE_REEXEC"] = "1"
    proc = subprocess.run([sys.executable, "-m", "kernelgate"] + sys.argv[1:], env=env)
    return proc.returncode


def _status_exit(rep: dict) -> int:
    s = rep.get("status")
    if s in ("PASS", "CLEAN", "OK"):
        return EXIT_PASS
    if s == "FINDINGS":
        return EXIT_ADVISORY
    return EXIT_FAIL


def _add_common(p, tpu: bool = True):
    p.add_argument("--dtype", default="bfloat16",
                   choices=["bfloat16", "float32", "module"],
                   help="graded input dtype passed to create_inputs when it accepts one "
                        "(default bfloat16 = JAXBench grading basis; 'module' = module default)")
    p.add_argument("--baseline", required=True, help="baseline problem module (.py)")
    p.add_argument("--candidate", required=True, help="candidate module (.py)")
    p.add_argument("--entry", default=None,
                   help="candidate entry function name (default: auto-resolve)")
    p.add_argument("--baseline-entry", default="workload")
    p.add_argument("-o", "--output", default=None, help="also write JSON here")
    if tpu:
        p.add_argument("--chip-env", action="append", default=None, metavar="KEY=VAL",
                       help="env var to set before jax import (re-execs; repeatable)")


def _add_receipt(p):
    p.add_argument("--receipt", default="receipt.json", metavar="PATH",
                   help="write the tamper-evident receipt here (default: receipt.json)")
    p.add_argument("--no-receipt", action="store_true",
                   help="skip writing the receipt")


def _emit_receipt(args, rep) -> None:
    if getattr(args, "no_receipt", False):
        return
    from . import receipt
    try:
        receipt.write(rep, args.receipt, argv=sys.argv[1:])
        print("[kgate] receipt written to %s" % args.receipt)
    except Exception as e:  # a receipt failure must not mask the run's verdict
        print("[kgate] WARNING: receipt not written: %r" % (e,), file=sys.stderr)


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="kgate", description="verification gates for TPU kernel benchmarking")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("measure", help="co-measured interleaved timing, both orderings")
    _add_common(p)
    _add_receipt(p)
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--warmup", type=int, default=10)
    p.add_argument("--n-min", type=int, default=30)
    p.add_argument("--n-max", type=int, default=120)
    p.add_argument("--se-target", type=float, default=0.001)

    p = sub.add_parser("parity", help="floor-normalized oracle parity gate "
                                      "(fp32, fp64 escalation)")
    _add_common(p)
    _add_receipt(p)
    p.add_argument("--seeds", default="42,43", help="comma-separated seeds")
    p.add_argument("--multiplier", type=float, default=2.0,
                   help="gate = candidate error <= multiplier x floor")
    p.add_argument("--oracle", default="auto", choices=("auto", "fp32", "fp64"),
                   help="auto (default) escalates to a fp64-on-CPU oracle when "
                        "the fp32 floor is ~0 (Precision.HIGHEST baselines)")
    p.add_argument("--floor-eps", type=float, default=None,
                   help="fp32 floor max_abs below this escalates to fp64 "
                        "(default %g)" % 1e-9)
    p.add_argument("--scale-probes", default=None,
                   help="comma-separated rescale factors for the designated input")
    p.add_argument("--scale-input", type=int, default=None,
                   help="input index to rescale (default: spec SCALE_INPUT or 1)")
    p.add_argument("--spec", default=None, help="family spec module (.py)")
    p.add_argument("--chunk", default=None,
                   help="oracle chunking, e.g. '0:0,1:0,2:0' = size-1 slices of "
                        "inputs 0,1,2 along axis 0 (batch-like axes only)")
    p.add_argument("--chunk-out-axis", type=int, default=0)

    p = sub.add_parser("coverage", help="spec-driven sensitivity battery "
                                        "(family module or declarative axes spec)")
    _add_common(p)
    p.add_argument("--spec", required=True,
                   help="family spec module (.py with perturb_regions), a "
                        "declarative .py (SPEC/AXES), or a .json/.yaml axes spec")
    p.add_argument("--seed", type=int, default=None)

    p = sub.add_parser("flags", help="4-leg flag-fairness harness (fresh process "
                                     "per leg; both framing ratios)")
    _add_common(p)
    _add_receipt(p)
    p.add_argument("--flag", required=True, metavar="KEY=VALUE",
                   help="the flag under test, e.g. "
                        "LIBTPU_INIT_ARGS=--xla_tpu_scoped_vmem_limit_kib=131072")
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--warmup", type=int, default=5)
    p.add_argument("-n", "--n", type=int, default=20, help="timed iterations per leg")

    p = sub.add_parser("verify", help="one-command independent verification "
                                      "(screen|full): HLO dump + firing audit "
                                      "+ measure + parity [+ coverage/capture/"
                                      "digest], one receipt")
    _add_common(p)
    _add_receipt(p)
    p.add_argument("--mode", default="screen", choices=("screen", "full"))
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--seeds", default="42,43", help="parity seeds")
    p.add_argument("--multiplier", type=float, default=2.0)
    p.add_argument("--oracle", default="auto", choices=("auto", "fp32", "fp64"))
    p.add_argument("--spec", default=None,
                   help="family spec module (parity calibration; full-mode "
                        "coverage battery)")
    p.add_argument("--chunk", default=None,
                   help="oracle chunking, e.g. '0:0,1:0,2:0' = size-1 slices of "
                        "inputs 0,1,2 along axis 0 (batch-like axes only)")
    p.add_argument("--chunk-out-axis", type=int, default=0)
    p.add_argument("--bar", type=float, default=None, dest="bar_speedup",
                   help="falsification bar as min speedup, e.g. 1.02")
    p.add_argument("--author-claim-p50", type=float, default=None,
                   help="author-side candidate p50 ms (reproduction check)")
    p.add_argument("--expect-pattern", action="append", default=None,
                   help="regex that MUST appear in the candidate ENTRY HLO "
                        "(repeatable)")
    p.add_argument("--forbid-pattern", action="append", default=None,
                   help="regex that must NOT appear (repeatable)")
    p.add_argument("--expect-custom-calls", type=int, default=None,
                   help="exact custom-call count in the candidate ENTRY HLO")
    p.add_argument("--forbid-shape", action="append", default=None,
                   help="adjacent dims that must not appear in any shape "
                        "literal, e.g. 4096,4096 (repeatable)")
    p.add_argument("--artifact-dir", default=None,
                   help="where dumps/trace land (default: a temp dir)")
    p.add_argument("--family", default=None,
                   help="family slug — keys the persistent verifier-owned "
                        "compilation cache (naive stays warm across v-levels)")
    p.add_argument("--fresh-cache", action="store_true",
                   help="wipe the verifier cache first")
    p.add_argument("--capture", action="store_true", default=None,
                   help="force the instrumented trace capture leg "
                        "(default: on in full mode)")
    p.add_argument("--no-capture", action="store_false", dest="capture")
    p.add_argument("--digest", action="store_true", default=None,
                   help="run xprof-cli reads over the capture (soft dep; "
                        "default: follows --capture)")
    p.add_argument("--no-digest", action="store_false", dest="digest")
    p.add_argument("--warmup", type=int, default=10)
    p.add_argument("--n-min", type=int, default=30)
    p.add_argument("--n-max", type=int, default=120)
    p.add_argument("--child-timeout", type=int, default=1800,
                   help="per-leg timeout, seconds")

    p = sub.add_parser("fit", help="compile-only config-fit sweep (parses "
                                   "RESOURCE_EXHAUSTED / Mosaic VMEM errors)")
    p.add_argument("--candidate", required=True, help="candidate module (.py)")
    p.add_argument("--configs", required=True,
                   help="JSON list of config dicts, inline or a file path")
    p.add_argument("--baseline", default=None,
                   help="module providing create_inputs (default: the candidate)")
    p.add_argument("--entry", default=None)
    p.add_argument("--run-once", action="store_true",
                   help="also execute each fitting config once (catches "
                        "allocation-time OOM the compile misses)")
    p.add_argument("-o", "--output", default=None)
    p.add_argument("--chip-env", action="append", default=None, metavar="KEY=VAL")

    p = sub.add_parser("verify-receipt", help="validate a receipt.json "
                                              "(self-hash, arithmetic, input regen)")
    p.add_argument("receipt", help="path to a receipt.json")
    p.add_argument("--skip-inputs", action="store_true",
                   help="skip regenerating the inputs (no jax / module needed)")
    p.add_argument("-o", "--output", default=None)

    p = sub.add_parser("sweep", help="parity-gated grid sweep over static params")
    _add_common(p)
    p.add_argument("--params", required=True,
                   help="grid, e.g. 'bq=512,1024,2048;bk=128,256,512'")
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--multiplier", type=float, default=2.0)
    p.add_argument("--chunk", default=None)
    p.add_argument("--chunk-out-axis", type=int, default=0)
    p.add_argument("--n-min", type=int, default=10)
    p.add_argument("--n-max", type=int, default=50)
    p.add_argument("--warmup", type=int, default=5)

    p = sub.add_parser("roofline", help="speed-of-light hard gate on a measure JSON")
    p.add_argument("--candidate-json", required=True,
                   help="JSON produced by `kgate measure`")
    p.add_argument("--flops", type=float, required=True)
    p.add_argument("--bytes", type=float, required=True, dest="bytes_moved")
    p.add_argument("--peak-tflops", type=float, default=None)
    p.add_argument("--peak-gbps", type=float, default=None)
    p.add_argument("--leg", default="candidate", choices=("candidate", "baseline"))
    p.add_argument("-o", "--output", default=None)

    p = sub.add_parser("lint", help="static AST prefilter (advisory)")
    p.add_argument("--candidate", required=True)
    p.add_argument("-o", "--output", default=None)
    return ap


def main(argv=None) -> int:
    ap = build_parser()
    args = ap.parse_args(argv)

    # Pin the graded measurement basis (JAXBench grades at bfloat16). Applied to
    # every create_inputs call that accepts a dtype; --dtype module opts out.
    _dt = getattr(args, "dtype", "bfloat16")
    if _dt and _dt != "module":
        import jax.numpy as _jnp
        from . import protocol as _proto
        _proto.GRADED_DTYPE = getattr(_jnp, _dt)

    code = _maybe_reexec(args)
    if code is not None:
        return code

    if args.cmd == "lint":
        from . import lint
        rep = lint.run_lint(args.candidate)
        report_mod.emit(rep, args.output)
        return _status_exit(rep)

    if args.cmd == "roofline":
        from . import roofline
        with open(args.candidate_json) as f:
            measure_rep = json.load(f)
        rep = roofline.run_roofline(measure_rep, args.flops, args.bytes_moved,
                                    args.peak_tflops, args.peak_gbps, args.leg)
        report_mod.emit(rep, args.output)
        return _status_exit(rep)

    if args.cmd == "verify-receipt":
        from . import receipt
        rep = receipt.verify(args.receipt, recompute_inputs=not args.skip_inputs)
        report_mod.emit(rep, args.output)
        return _status_exit(rep)

    if args.cmd == "verify":
        # parent stays jax-free — every device step is a fresh child process
        from . import verify
        rep = verify.run_verify(
            args.baseline, args.candidate,
            mode=args.mode,
            baseline_entry=args.baseline_entry, candidate_entry=args.entry,
            dtype=getattr(args, "dtype", "bfloat16"),
            seed=args.seed, seeds=args.seeds,
            multiplier=args.multiplier, oracle=args.oracle,
            spec=args.spec, bar_speedup=args.bar_speedup,
            chunk=args.chunk, chunk_out_axis=args.chunk_out_axis,
            author_claim_p50=args.author_claim_p50,
            expect_patterns=args.expect_pattern,
            forbid_patterns=args.forbid_pattern,
            expect_custom_calls=args.expect_custom_calls,
            forbid_shapes=args.forbid_shape,
            artifact_dir=args.artifact_dir, family=args.family,
            fresh_cache=args.fresh_cache,
            capture=args.capture, digest=args.digest,
            warmup=args.warmup, n_min=args.n_min, n_max=args.n_max,
            child_timeout=args.child_timeout)
        report_mod.emit(rep, args.output)
        _emit_receipt(args, rep)
        return _status_exit(rep)

    if args.cmd == "flags":
        # the parent stays jax-free — all device work happens in the leg
        # subprocesses, so the flag env can take effect there
        from . import flags
        rep = flags.run_flags(
            args.baseline, args.candidate, args.flag,
            baseline_entry=args.baseline_entry, candidate_entry=args.entry,
            seed=args.seed, warmup=args.warmup, n=args.n,
            dtype=getattr(args, "dtype", "bfloat16"))
        report_mod.emit(rep, args.output)
        _emit_receipt(args, rep)
        return _status_exit(rep)

    # TPU-executing commands: load modules lazily (imports jax)
    from . import protocol
    candidate_mod = protocol.load_module(args.candidate)
    baseline_mod = protocol.load_module(args.baseline) if args.baseline else None

    if args.cmd == "measure":
        from . import timing
        rep = timing.run_measure(
            baseline_mod, candidate_mod,
            baseline_entry=args.baseline_entry, candidate_entry=args.entry,
            seed=args.seed, warmup=args.warmup,
            n_min=args.n_min, n_max=args.n_max, se_target=args.se_target)
        report_mod.emit(rep, args.output)
        _emit_receipt(args, rep)
        return _status_exit(rep)

    if args.cmd == "parity":
        from . import parity
        spec_mod = protocol.load_module(args.spec) if args.spec else None
        seeds = tuple(int(s) for s in args.seeds.split(","))
        probes = tuple(float(s) for s in args.scale_probes.split(",")) \
            if args.scale_probes else ()
        rep = parity.run_parity(
            baseline_mod, candidate_mod,
            baseline_entry=args.baseline_entry, candidate_entry=args.entry,
            seeds=seeds, multiplier=args.multiplier,
            chunk=parity.parse_chunk_spec(args.chunk),
            chunk_out_axis=args.chunk_out_axis,
            scale_probes=probes, scale_input=args.scale_input, spec_mod=spec_mod,
            oracle=args.oracle,
            floor_eps=args.floor_eps if args.floor_eps is not None
            else parity.FLOOR_ZERO_EPS)
        report_mod.emit(rep, args.output)
        _emit_receipt(args, rep)
        return _status_exit(rep)

    if args.cmd == "coverage":
        from . import coverage, declspec
        if args.spec.lower().endswith((".json", ".yaml", ".yml")):
            spec_mod = declspec.load_spec_file(args.spec)
        else:
            spec_mod = protocol.load_module(args.spec)
        rep = coverage.run_coverage(
            baseline_mod, candidate_mod, spec_mod,
            baseline_entry=args.baseline_entry, candidate_entry=args.entry,
            seed=args.seed)
        report_mod.emit(rep, args.output)
        return _status_exit(rep)

    if args.cmd == "fit":
        from . import fit
        rep = fit.run_fit(candidate_mod, fit.parse_configs(args.configs),
                          baseline_mod=baseline_mod, candidate_entry=args.entry,
                          run_once=args.run_once)
        report_mod.emit(rep, args.output)
        return _status_exit(rep)

    if args.cmd == "sweep":
        from . import parity, sweep
        rep = sweep.run_sweep(
            baseline_mod, candidate_mod, args.params,
            baseline_entry=args.baseline_entry, candidate_entry=args.entry,
            seed=args.seed, multiplier=args.multiplier,
            chunk=parity.parse_chunk_spec(args.chunk),
            chunk_out_axis=args.chunk_out_axis,
            n_min=args.n_min, n_max=args.n_max, warmup=args.warmup)
        report_mod.emit(rep, args.output)
        return _status_exit(rep)

    ap.error("unknown command")
    return EXIT_FAIL


if __name__ == "__main__":
    sys.exit(main())
