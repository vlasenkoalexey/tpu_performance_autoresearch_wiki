"""kgate verify — one-command independent verification (screen | full).

Collapses the K6 verification pipeline into a single invocation so the
verifier agent runs ONE command and reads ONE receipt (the ~20 LLM round
trips of hand-driven verification were the measured long pole: 20-40 min for
a compliant agent, 50-80 min for a thorough one).

Pipeline (parent stays jax-free; every device step is a fresh child process,
mirroring `kgate flags`):

  1. DUMP legs (cold-first)  — one forward call per module with
     --xla_dump_to; the same compile that emits the HLO dump WARMS the
     verifier-owned persistent compilation cache, so every later leg
     cache-hits (a persistent-cache HIT emits NO dump — the pinned gotcha —
     hence dumps run first).
  2. HLO firing audit        — declarative assertions on the candidate ENTRY
     (hlo.run_assertions) + custom-call counts on both legs.
  3. MEASURE                 — child `kgate measure` (co-measured, both
     orderings) under the warm cache.
  4. PARITY                  — child `kgate parity` at the family spec
     (multi-seed, floor-normalized, fp64 escalation).
  5. full mode: COVERAGE     — child `kgate coverage` when --spec is given.
  6. full mode: CAPTURE      — one instrumented run of the candidate under
     trace flags (timing discarded); artifacts land in --artifact-dir.
  7. full mode: DIGEST       — optional xprof-cli reads over the capture,
     invoked as subprocesses (soft dependency: absent/failing xprof-cli
     degrades to `digest: unavailable`, NEVER blocks the verdict path).
  8. Reproduction check      — candidate p50 vs --author-claim-p50
     (>2x gap = the timing-helper-bypass class).
  9. One combined report + tamper-evident receipt.

Independence properties: verifier-OWNED cache dir (never the author's — a
cache serves pre-built executables, so sharing the author's cache would mean
executing author-writable artifacts), fresh child processes, and the naive
leg stays cached across v-levels of a family (it never changes).

The trace/LLO READ side stays xprof-cli's (kgate embeds its output as an
opaque blob and compares only numbers it understands); the separation rule
lives in wiki/kernel_experiments/program.md `Profiling`.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback

from . import hlo

DEFAULT_CACHE_ROOT = os.environ.get("KGATE_VERIFY_CACHE_ROOT",
                                    "/tmp/kgate-verify-cache")
# Without these, small/fast-compiling kernels are silently NOT cached (the
# pinned 3-env-var pattern) and every leg re-pays the compile.
CACHE_ENV_KNOBS = {
    "JAX_PERSISTENT_CACHE_MIN_COMPILE_TIME_SECS": "0",
    "JAX_PERSISTENT_CACHE_MIN_ENTRY_SIZE_BYTES": "0",
}
TRACE_LIBTPU_FLAGS = ("--xla_enable_custom_call_region_trace=true "
                      "--xla_xprof_register_llo_debug_info=true")
XPROF_DIGEST_TOOLS = ("check_kernel_profiling", "get_top_hlo_ops",
                      "get_device_wall_report")


def _family_cache_dir(family: str | None, baseline_path: str) -> str:
    tag = family or hashlib.sha256(
        os.path.abspath(baseline_path).encode()).hexdigest()[:12]
    return os.path.join(DEFAULT_CACHE_ROOT, tag)


def _child_env(cache_dir: str, extra: dict | None = None) -> dict:
    env = dict(os.environ)
    env["JAX_COMPILATION_CACHE_DIR"] = cache_dir
    env.update(CACHE_ENV_KNOBS)
    env.update(extra or {})
    return env


def _run_child(argv: list[str], env: dict, tag: str, timeout: int = 1800) -> dict:
    """Run a kgate subcommand child; return its JSON report (via a temp -o)."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tf:
        out_path = tf.name
    cmd = [sys.executable, "-m", "kernelgate"] + argv + ["-o", out_path]
    proc = subprocess.run(cmd, env=env, capture_output=True, text=True,
                          timeout=timeout)
    try:
        with open(out_path) as f:
            rep = json.load(f)
    except Exception:
        rep = {"status": "FAIL",
               "error": "child %s produced no report (exit %d): %s"
                        % (tag, proc.returncode, (proc.stderr or proc.stdout)[-2000:])}
    finally:
        try:
            os.unlink(out_path)
        except OSError:
            pass
    rep["_child"] = {"tag": tag, "exit": proc.returncode}
    time.sleep(1.0)
    return rep


def _dump_leg(module_path: str, inputs_from: str, entry: str | None,
              dump_dir: str, cache_dir: str, seed: int | None,
              dtype: str, extra_env: dict | None = None,
              trace_dir: str | None = None,
              timeout: int = 1800) -> dict:
    """One forward call in a fresh child with --xla_dump_to (leg timing is
    irrelevant; this leg exists to emit the HLO dump and warm the cache —
    or, with trace_dir, to emit an instrumented xplane trace)."""
    os.makedirs(dump_dir, exist_ok=True)
    env = _child_env(cache_dir, hlo.dump_env(dump_dir))
    env.update(extra_env or {})
    cmd = [sys.executable, "-m", "kernelgate.flags", "--legrun",
           "--module", module_path, "--inputs-from", inputs_from,
           "--warmup", "0", "--n", "1", "--dtype", dtype]
    if trace_dir:
        cmd += ["--trace-dir", trace_dir]
    if entry:
        cmd += ["--entry", entry]
    if seed is not None:
        cmd += ["--seed", str(seed)]
    proc = subprocess.run(cmd, env=env, capture_output=True, text=True,
                          timeout=timeout)
    module_txt = hlo.newest_module(dump_dir)
    res = {"exit": proc.returncode,
           "dump_dir": dump_dir,
           "module_file": module_txt,
           "cache_hit_no_dump": proc.returncode == 0 and module_txt is None,
           "error": None if proc.returncode == 0
           else (proc.stderr or proc.stdout)[-2000:]}
    time.sleep(1.0)
    return res


def _xprof_digest(logdir: str) -> dict:
    """Soft-dependency xprof-cli reads (subprocess; graceful degradation)."""
    exe = shutil.which("xprof-cli")
    if exe is None:
        return {"available": False, "reason": "xprof-cli not on PATH"}
    out: dict = {"available": True, "tools": {}}
    env = dict(os.environ, XPROF_MODE="local", XPROF_LOGDIR=logdir)
    run_arg = None
    try:
        lr_proc = subprocess.run([exe, "list_runs", "--bypass_cache=True"], env=env, capture_output=True, text=True, timeout=60)
        lr_data = json.loads(lr_proc.stdout.strip())
        runs = lr_data.get("runs", [])
        if runs:
            run_arg = str(runs[-1])
    except Exception:
        pass

    for tool in XPROF_DIGEST_TOOLS:
        try:
            cmd = [exe, tool]
            if run_arg:
                cmd.append(run_arg)
            cmd.extend(["--logdir", logdir, "--bypass_cache=True"])
            proc = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=600)
            raw = proc.stdout.strip()
            try:
                payload = json.loads(raw)
            except (json.JSONDecodeError, ValueError):
                payload = {"raw_text": raw[-8000:]}
            out["tools"][tool] = {"exit": proc.returncode, "output": payload,
                                  "stderr": proc.stderr[-1000:] if proc.returncode else ""}
        except Exception as e:  # never block the verdict path
            out["tools"][tool] = {"exit": -1, "error": repr(e)}
    return out


def run_verify(baseline_path: str, candidate_path: str, *,
               mode: str = "screen",
               baseline_entry: str = "workload",
               candidate_entry: str | None = None,
               dtype: str = "bfloat16",
               seed: int | None = None,
               seeds: str = "42,43",
               multiplier: float = 2.0,
               oracle: str = "auto",
               spec: str | None = None,
               bar_speedup: float | None = None,
               chunk: str | None = None,
               chunk_out_axis: int = 0,
               author_claim_p50: float | None = None,
               expect_patterns: list[str] | None = None,
               forbid_patterns: list[str] | None = None,
               expect_custom_calls: int | None = None,
               forbid_shapes: list[str] | None = None,
               artifact_dir: str | None = None,
               family: str | None = None,
               fresh_cache: bool = False,
               capture: bool | None = None,
               digest: bool | None = None,
               warmup: int = 10, n_min: int = 30, n_max: int = 120,
               child_timeout: int = 1800) -> dict:
    """Full verify pipeline. Returns the combined report dict."""
    from . import envinfo

    mode = mode.lower()
    if mode not in ("screen", "full"):
        raise ValueError("mode must be screen|full, got %r" % mode)
    capture = (mode == "full") if capture is None else capture
    digest = capture if digest is None else digest

    artifact_dir = os.path.abspath(artifact_dir or
                                   tempfile.mkdtemp(prefix="kgate-verify-"))
    os.makedirs(artifact_dir, exist_ok=True)
    cache_dir = _family_cache_dir(family, baseline_path)
    if fresh_cache and os.path.isdir(cache_dir):
        shutil.rmtree(cache_dir, ignore_errors=True)
    os.makedirs(cache_dir, exist_ok=True)

    report: dict = {
        "cmd": "verify",
        "mode": mode,
        "baseline": {"path": os.path.abspath(baseline_path),
                     "entry": baseline_entry},
        "candidate": {"path": os.path.abspath(candidate_path),
                      "entry": candidate_entry},
        "dtype": dtype,
        "artifact_dir": artifact_dir,
        "compilation_cache_dir": cache_dir,
        "env": envinfo.capture(include_devices=False),
        "legs": {}, "gates": {}, "warnings": [], "anomalies": [],
        "status": "PASS",
    }

    def _gate(name: str, ok: bool, detail: str = ""):
        report["gates"][name] = {"ok": bool(ok), "detail": detail}
        if not ok:
            report["status"] = "FAIL"

    try:
        # ---- 1. dump legs, cold-first (emit HLO + warm the cache) ----------
        for leg, mod_path, entry in (
                ("cand", candidate_path, candidate_entry),
                ("naive", baseline_path, baseline_entry)):
            ddir = os.path.join(artifact_dir, "hlo_%s" % leg)
            d = _dump_leg(mod_path, baseline_path, entry, ddir, cache_dir,
                          seed, dtype, timeout=child_timeout)
            if d["cache_hit_no_dump"]:
                # warm cache swallowed the compile: retry against an empty
                # throwaway cache purely to obtain the dump text
                tmp_cache = tempfile.mkdtemp(prefix="kgate-verify-dumponly-")
                d = _dump_leg(mod_path, baseline_path, entry, ddir, tmp_cache,
                              seed, dtype, timeout=child_timeout)
                d["dump_retry_fresh_cache"] = True
            report["legs"]["dump_%s" % leg] = d
            if d["error"]:
                _gate("dump_%s" % leg, False, d["error"])
        cand_dump = report["legs"].get("dump_cand", {})

        # ---- 2. HLO firing audit -------------------------------------------
        # Computed BEFORE the branch: if the operator asked for assertions they
        # must be answered either way. Deciding this inside the `if` meant a run
        # that captured no dump fell through with status PASS and the assertions
        # never evaluated — a fabricated PASS that the wiki's fake-win LINT
        # cannot even see, because it looks for hlo_firing_audit:false /
        # custom_call_count:0 and this leaves both null.
        had_assertions = bool(expect_patterns or forbid_patterns or
                              forbid_shapes) or expect_custom_calls is not None
        if cand_dump.get("module_file"):
            text = hlo.entry_text(cand_dump["module_file"])
            audit = hlo.run_assertions(
                text,
                expect_patterns=expect_patterns or [],
                forbid_patterns=forbid_patterns or [],
                expect_custom_calls=expect_custom_calls,
                forbid_shapes=forbid_shapes or [])
            naive_file = report["legs"].get("dump_naive", {}).get("module_file")
            if naive_file:
                audit["naive_custom_call_count"] = hlo.count_custom_calls(
                    hlo.entry_text(naive_file))
            report["hlo_audit"] = audit
            if had_assertions:
                _gate("hlo_firing_audit", audit["status"] == "PASS",
                      "; ".join("%s: %s" % (c["name"], c["detail"] or "ok")
                                for c in audit["checks"] if not c["ok"]))
        else:
            report["warnings"].append(
                "no candidate HLO dump captured — firing audit skipped")
            if had_assertions:
                # Assertions were requested and could not be evaluated. That is
                # a failure of the audit, not an absence of one: passing here
                # would certify a firing claim on zero evidence.
                _gate("hlo_firing_audit", False,
                      "no candidate HLO dump captured — the requested "
                      "assertions were never evaluated, so firing is "
                      "UNVERIFIED (not confirmed)")

        # ---- 3. measure (warm cache; co-measured both orderings) -----------
        m_argv = ["measure", "--baseline", baseline_path,
                  "--candidate", candidate_path,
                  "--baseline-entry", baseline_entry,
                  "--dtype", dtype, "--no-receipt",
                  "--warmup", str(warmup),
                  "--n-min", str(n_min), "--n-max", str(n_max)]
        if candidate_entry:
            m_argv += ["--entry", candidate_entry]
        if seed is not None:
            m_argv += ["--seed", str(seed)]
        m = _run_child(m_argv, _child_env(cache_dir), "measure", child_timeout)
        report["legs"]["measure"] = m
        _gate("measure", m.get("status") == "PASS",
              m.get("error", "") or m.get("status", ""))

        speedup = None
        cand_p50 = None
        try:
            pooled = m["timing"]["pooled"]
            speedup = pooled["speedup_p50"]
            cand_p50 = pooled["candidate"]["p50_ms"]
            report["p50_ms"] = {"baseline": pooled["baseline"]["p50_ms"],
                                "candidate": cand_p50}
        except (KeyError, TypeError):
            report["warnings"].append("measure report shape unexpected — "
                                      "speedup not extracted")
        report["speedup"] = speedup
        # `speedup` is always relative to whatever --baseline pointed at, which
        # may be the JAXBench naive baseline OR a previous frontier kernel. The
        # bare number is therefore ambiguous and has been misread as vs-naive
        # when it was vs-frontier. Label it at the source.
        _bn = os.path.basename(baseline_path or "")
        if _bn == "baseline.py":
            _role, _detail = "vs_naive", "JAXBench baseline.py"
        elif "frontier" in _bn or re.search(r"v\d{3}", _bn):
            _role, _detail = "vs_frontier", _bn
        else:
            _role, _detail = "vs_other", _bn
        report["speedup_role"] = {
            "role": _role,
            "baseline_basename": _bn,
            "baseline_path": baseline_path,
            "note": "speedup = baseline_p50 / candidate_p50, baseline = %s. "
                    "Only role=vs_naive is comparable to a scoreboard number."
                    % _detail,
        }
        if bar_speedup is not None:
            # The operator asked for a bar, so the bar must be answered. Gating
            # this on `speedup is not None` silently dropped the bar whenever
            # speedup extraction failed — the run then reported PASS having
            # never compared anything against the bar it was given.
            if speedup is None:
                _gate("falsification_bar", False,
                      "bar %.4fx requested but no speedup could be extracted "
                      "from the measure leg — bar UNEVALUATED" % bar_speedup)
            else:
                _gate("falsification_bar", speedup >= bar_speedup,
                      "speedup %.4fx vs bar %.4fx" % (speedup, bar_speedup))

        # ---- 4. parity ------------------------------------------------------
        p_argv = ["parity", "--baseline", baseline_path,
                  "--candidate", candidate_path,
                  "--baseline-entry", baseline_entry,
                  "--dtype", dtype, "--no-receipt",
                  "--seeds", seeds, "--multiplier", str(multiplier),
                  "--oracle", oracle]
        if candidate_entry:
            p_argv += ["--entry", candidate_entry]
        if spec:
            p_argv += ["--spec", spec]
        if chunk:
            p_argv += ["--chunk", chunk, "--chunk-out-axis", str(chunk_out_axis)]
        p = _run_child(p_argv, _child_env(cache_dir), "parity", child_timeout)
        report["legs"]["parity"] = p
        _gate("parity", p.get("status") == "PASS",
              p.get("error", "") or p.get("status", ""))

        # ---- 5. full: coverage battery -------------------------------------
        if mode == "full" and spec:
            c_argv = ["coverage", "--baseline", baseline_path,
                      "--candidate", candidate_path,
                      "--baseline-entry", baseline_entry,
                      "--dtype", dtype, "--spec", spec]
            if candidate_entry:
                c_argv += ["--entry", candidate_entry]
            if seed is not None:
                c_argv += ["--seed", str(seed)]
            c = _run_child(c_argv, _child_env(cache_dir), "coverage",
                           child_timeout)
            report["legs"]["coverage"] = c
            _gate("coverage", c.get("status") in ("PASS", "CLEAN", "OK"),
                  c.get("error", "") or c.get("status", ""))

        # ---- 6/7. full: capture + digest (timing discarded; soft xprof dep) -
        if capture:
            trace_dir = os.path.join(artifact_dir, "trace")
            os.makedirs(trace_dir, exist_ok=True)
            prev = os.environ.get("LIBTPU_INIT_ARGS", "")
            cap_env = {"LIBTPU_INIT_ARGS": (prev + " " + TRACE_LIBTPU_FLAGS).strip()}
            cap = _dump_leg(candidate_path, baseline_path, candidate_entry,
                            os.path.join(artifact_dir, "hlo_capture_scratch"),
                            cache_dir, seed, dtype, extra_env=cap_env,
                            trace_dir=trace_dir, timeout=child_timeout)
            report["legs"]["capture"] = {**cap, "trace_dir": trace_dir,
                                         "note": "instrumented run; timing discarded"}
            if digest:
                report["xprof_digest"] = _xprof_digest(trace_dir)
                if not report["xprof_digest"].get("available"):
                    report["warnings"].append(
                        "xprof digest unavailable: %s"
                        % report["xprof_digest"].get("reason"))

        # ---- 8. reproduction check ------------------------------------------
        if author_claim_p50 is not None and cand_p50 is not None:
            try:
                ratio = max(cand_p50, author_claim_p50) / max(
                    1e-9, min(cand_p50, author_claim_p50))
                verdict = ("MATCHES" if ratio <= 1.10 else
                           "DIVERGES" if ratio <= 2.0 else
                           "DIVERGES>2x — timing-helper bypass suspected")
                report["reproduction"] = {
                    "author_claim_p50_ms": author_claim_p50,
                    "verifier_p50_ms": cand_p50, "ratio": ratio,
                    "verdict": verdict}
                if ratio > 2.0:
                    report["anomalies"].append(
                        "author/verifier p50 gap %.2fx (>2x)" % ratio)
            except (KeyError, TypeError):
                pass
        else:
            # Record WHY the check did not run. A bare null is indistinguishable
            # from "ran and found nothing", which has let un-reproduced author
            # claims reach a K9 close unchallenged.
            if author_claim_p50 is None:
                _why = ("--author-claim-p50 not supplied, so the author's own "
                        "timing was never compared against the verifier's")
            else:
                _why = "verifier produced no candidate p50 to compare against"
            report["reproduction"] = {"verdict": "NOT_CHECKED", "reason": _why,
                                      "author_claim_p50_ms": author_claim_p50,
                                      "verifier_p50_ms": cand_p50}

        if report["anomalies"] and report["status"] == "PASS":
            report["status"] = "ANOMALY"
    except Exception:
        report["status"] = "FAIL"
        report["exception"] = traceback.format_exc()
    return report
