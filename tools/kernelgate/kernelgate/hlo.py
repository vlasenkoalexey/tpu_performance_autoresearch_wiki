"""HLO dump + declarative mechanism assertions (the kgate-verify firing audit).

The stub's Mechanism is prose; an agent extracts 2-3 CHECKABLE assertions and
this module executes them against the compiled HLO text — mechanizing the
firing audit that caught the 10p fabricated-mechanism claim (commits said
"sort/segment bucketing"; no such op existed in the compiled module).

Assertion grammar (all repeatable, all case-insensitive substring/regex on the
ENTRY after-optimizations module of the leg they target):

    expect-pattern PAT    PAT must appear   (regex)
    forbid-pattern PAT    PAT must NOT appear
    expect-custom-calls N exactly N custom-call sites in the candidate ENTRY
    forbid-shape DIMS     no tensor literal with these dims, e.g. "4096,4096"
                          (catches [S,S] materialization)

A dump is only emitted on actual compilation — a persistent-cache HIT skips
compile and leaves the dump dir EMPTY (the pinned gotcha). verify orders dump
legs first/cold so one compile both emits the dump and warms the cache;
`newest_module` returning None signals the cache-hit case to the caller.
"""
from __future__ import annotations

import glob
import os
import re

# after_optimizations text dumps, either .txt or .hlo flavor
_MODULE_GLOBS = (
    "*after_optimizations*.txt",
    "*after_optimizations*.hlo",
)

CUSTOM_CALL_RE = re.compile(r"\bcustom-call\b|\bcustom_call\b", re.IGNORECASE)


def dump_env(dump_dir: str) -> dict:
    """XLA_FLAGS addition for a dump leg (caller merges with its child env)."""
    prev = os.environ.get("XLA_FLAGS", "")
    flag = "--xla_dump_to=%s" % dump_dir
    return {"XLA_FLAGS": (prev + " " + flag).strip()}


def newest_module(dump_dir: str) -> str | None:
    """Path of the newest after-optimizations module text, or None (cache hit /
    no compile happened)."""
    hits: list[str] = []
    for pat in _MODULE_GLOBS:
        hits += glob.glob(os.path.join(dump_dir, pat))
        hits += glob.glob(os.path.join(dump_dir, "**", pat), recursive=True)
    if not hits:
        return None
    filtered = [h for h in hits if not h.endswith(("-memory-usage-report.txt", "-buffer-assignment.txt", "-buffer-assignment-values.txt", "-live-range.txt"))]
    hits = filtered or hits
    entry_hits = [h for h in hits if "workload" in os.path.basename(h) or "entry" in os.path.basename(h)]
    if entry_hits:
        return max(set(entry_hits), key=os.path.getmtime)
    return max(set(hits), key=os.path.getmtime)


def entry_text(module_path: str) -> str:
    with open(module_path, errors="replace") as f:
        return f.read()


def count_custom_calls(text: str) -> int:
    return len(CUSTOM_CALL_RE.findall(text))


def _shape_re(dims: str) -> re.Pattern:
    # "4096,4096" -> matches shape literals carrying these dims ADJACENT, e.g.
    # f32[4,64,4096,4096]. Boundary-anchored on [ or , both sides so "14096"
    # can never satisfy "4096".
    #
    # Rank can be pinned by writing the brackets explicitly:
    #   "[4096,4096]"  exact rank-2 shape only (NOT f32[4,64,4096,4096])
    #   "[4096,4096"   shape must START with these dims
    #   "4096,4096]"   shape must END with these dims
    # Without brackets the historical unanchored behaviour is preserved.
    spec = dims.strip()
    lead = spec.startswith("[")
    trail = spec.endswith("]")
    body = spec[1:] if lead else spec
    body = body[:-1] if trail else body
    parts = [d.strip() for d in body.split(",") if d.strip()]
    if not parts:
        raise ValueError("empty --forbid-shape spec")
    left = r"\[" if lead else r"[\[,]"
    right = r"\]" if trail else r"[\],]"
    return re.compile(left + ",".join(re.escape(p) for p in parts) + right)


def run_assertions(text: str,
                   expect_patterns: list[str] = (),
                   forbid_patterns: list[str] = (),
                   expect_custom_calls: int | None = None,
                   forbid_shapes: list[str] = ()) -> dict:
    """Execute the declarative assertions on one module's HLO text.

    Returns {"checks": [...], "status": "PASS"|"FAIL", "custom_call_count": n}.
    Every check records name/ok/detail so the receipt carries the evidence.
    """
    checks = []

    def _check(name: str, ok: bool, detail: str = ""):
        checks.append({"name": name, "ok": bool(ok), "detail": detail})

    n_cc = count_custom_calls(text)
    for pat in expect_patterns or ():
        found = re.search(pat, text, re.IGNORECASE) is not None
        _check("expect-pattern:%s" % pat, found,
               "" if found else "pattern not found in ENTRY HLO")
    for pat in forbid_patterns or ():
        m = re.search(pat, text, re.IGNORECASE)
        _check("forbid-pattern:%s" % pat, m is None,
               "" if m is None else "forbidden pattern present: %r" % m.group(0))
    if expect_custom_calls is not None:
        ok = n_cc == expect_custom_calls
        _check("expect-custom-calls:%d" % expect_custom_calls, ok,
               "found %d custom-call site(s)" % n_cc)
    for dims in forbid_shapes or ():
        m = _shape_re(dims).search(text)
        _check("forbid-shape:%s" % dims, m is None,
               "" if m is None else "forbidden shape present: %r" % m.group(0))

    status = "PASS" if all(c["ok"] for c in checks) else "FAIL"
    return {"status": status, "custom_call_count": n_cc, "checks": checks}
