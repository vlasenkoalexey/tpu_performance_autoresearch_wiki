"""Compile-only config-fit sweep (kgate fit) — the 2p/4p OOM-grind killer.

The 2p/4p VMEM bar-miss lanes burned author budget re-running full timed
sweeps just to learn which block configs fit the chip's scoped-VMEM / HBM
envelope. `kgate fit` answers that question directly: for each config it
attempts a jit lower+compile of the candidate entry (optionally one tiny
execution with --run-once for allocation-time failures), catches
RESOURCE_EXHAUSTED / Mosaic VMEM errors, and PARSES the requested-vs-limit
numbers out of the error text instead of crashing the sweep. No timing.

Handled OOM grammars (the raw matched line is always kept in the row):
  - Mosaic scoped-vmem:  "... 44.05M > 32M"  /  "Ran out of memory in memory
    space vmem. Used 44.05M of 32.00M."
  - XLA HBM:  "RESOURCE_EXHAUSTED: ... Ran out of memory in memory space hbm.
    Used 34.00G of 30.75G."  /  "the total memory required for HLO
    temporaries (64.00G) exceeds available HBM (31.25G)"  /  "Attempting to
    allocate 64.00G ... There are 10.51G free"
  - byte-count style:  "Scoped allocation with size 45108224 ... exceeds the
    scoped vmem limit of 33554432" / "requested 45108224 bytes, limit 33554432"

Output: one TSV row per config — config | fits | requested | limit |
error_class — plus the machine JSON.
"""
from __future__ import annotations

import functools
import json
import re

from . import protocol

_UNIT = {"": 1, "B": 1,
         "K": 2 ** 10, "KB": 2 ** 10, "KIB": 2 ** 10,
         "M": 2 ** 20, "MB": 2 ** 20, "MIB": 2 ** 20,
         "G": 2 ** 30, "GB": 2 ** 30, "GIB": 2 ** 30,
         "T": 2 ** 40, "TB": 2 ** 40, "TIB": 2 ** 40}

_NUM = r"([\d]+(?:\.[\d]+)?)\s*([KMGT]i?B?|B)?"
# ordered: first match wins
_REQ_LIMIT_PATTERNS = (
    re.compile(r"[Uu]sed\s+%s\s+of\s+%s" % (_NUM, _NUM)),          # XLA "Used X of Y"
    # XLA "temporaries (64.00G) exceeds available HBM (31.25G)"
    re.compile(r"\(%s\).{0,60}?exceeds.{0,60}?\(%s\)" % (_NUM, _NUM)),
    # runtime "Attempting to allocate 64.00G ... There are 10.51G free"
    re.compile(r"[Aa]ttempting to allocate\s+%s.{0,120}?[Tt]here (?:are|is)\s+%s\s+free"
               % (_NUM, _NUM)),
    re.compile(r"%s\s*>\s*%s" % (_NUM, _NUM)),                     # Mosaic "X > Y"
    re.compile(r"size\s+(\d+)()\D.{0,80}?limit\s+(?:of\s+)?(\d+)()"),  # "size N ... limit of M"
    re.compile(r"requested\s+(\d+)()\s*bytes.{0,80}?limit\s+(?:of\s+)?(\d+)()"),
)


def _to_bytes(num: str, unit: str | None) -> int:
    return int(float(num) * _UNIT[(unit or "").upper()])


# Positive evidence that a message is about running out of memory. Membership
# of the word "mosaic" is NOT such evidence: any Mosaic lowering failure (a
# plain TypeError in a Pallas kernel, a bad block shape) mentions it, and such
# tracebacks routinely mention `memory_space=vmem` too.
# Word-bounded: a bare "oom" substring also matches file paths and identifiers
# (a traceback line naming a pytest tmpdir `test_fit_non_oom_error_is_other`
# classified a TypeError as an OOM). `\b` does not fire inside `non_oom`
# because `_` is a word character.
_OOM_RE = re.compile(
    r"resource_exhausted|ran out of memory|out of memory|\boom\b"
    r"|not enough|insufficient|exceeds|exceeded"
    r"|does not fit|doesn't fit|no space left",
    re.IGNORECASE)


def classify_oom(text: str) -> str | None:
    """Error class from the message text; None = not an OOM-shaped error."""
    low = text.lower()
    if not _OOM_RE.search(text):
        return None
    if "vmem" in low:
        return "mosaic_vmem"
    if "hbm" in low:
        return "xla_hbm"
    return "resource_exhausted"


def parse_oom(text: str) -> dict | None:
    """Extract {error_class, requested_bytes, limit_bytes, raw_line} from an
    OOM error text, or None if the text is not an OOM."""
    error_class = classify_oom(text)
    if error_class is None:
        return None
    out = {"error_class": error_class, "requested_bytes": None,
           "limit_bytes": None, "raw_line": None}
    for line in text.splitlines():
        # Only mine numbers from lines that are themselves OOM-shaped. Applying
        # the patterns to every line let the bare "X > Y" rule harvest e.g.
        # "block shape 512 > 256 for the last dim" into requested/limit BYTE
        # counts, so an author retuned block sizes against a VMEM wall that
        # was never reported.
        if classify_oom(line) is None:
            continue
        for pat in _REQ_LIMIT_PATTERNS:
            m = pat.search(line)
            if m:
                req_n, req_u, lim_n, lim_u = m.groups()
                out["requested_bytes"] = _to_bytes(req_n, req_u)
                out["limit_bytes"] = _to_bytes(lim_n, lim_u)
                out["raw_line"] = line.strip()
                return out
    # OOM without parsable numbers: keep the most informative line
    for line in text.splitlines():
        if classify_oom(line):
            out["raw_line"] = line.strip()
            break
    return out


def parse_configs(spec: str) -> list[dict]:
    """--configs value: a JSON list literal, or a path to a JSON file."""
    text = spec
    if not spec.lstrip().startswith(("[", "{")):
        with open(spec) as f:
            text = f.read()
    configs = json.loads(text)
    if not isinstance(configs, list) or not all(isinstance(c, dict) for c in configs):
        raise ValueError("--configs must be a JSON list of config dicts")
    return configs


def _fmt_bytes(n) -> str:
    if n is None:
        return "-"
    for unit, div in (("G", 2 ** 30), ("M", 2 ** 20), ("K", 2 ** 10)):
        if n >= div:
            return "%.2f%s" % (n / div, unit)
    return "%dB" % n


def run_fit(candidate_mod, configs: list[dict],
            baseline_mod=None,
            candidate_entry: str | None = None,
            run_once: bool = False) -> dict:
    """Per-config compile-fit table. Never raises on an OOM — every config
    yields a row and the sweep continues."""
    import traceback
    import jax
    from . import envinfo

    inputs_mod = baseline_mod if baseline_mod is not None else candidate_mod
    report = {
        "cmd": "fit",
        "candidate": {"path": candidate_mod.__kgate_path__},
        "baseline": {"path": inputs_mod.__kgate_path__},
        "config": protocol.get_config(inputs_mod),
        "run_once": run_once,
        "env": envinfo.capture(),
        "rows": [],
        "status": "PASS",
    }
    try:
        inputs = protocol.make_inputs(inputs_mod)
        n_inputs = len(inputs)
        c_name, c_fn = protocol.resolve_entry(candidate_mod, candidate_entry, n_inputs)
        report["candidate"]["entry"] = c_name

        n_fit = 0
        for cfg in configs:
            row = {"config": cfg, "fits": False, "requested_bytes": None,
                   "limit_bytes": None, "error_class": None, "raw_line": None}
            try:
                jitted = jax.jit(functools.partial(c_fn, **cfg))
                compiled = jitted.lower(*inputs).compile()
                del compiled
                if run_once:
                    out = jitted(*inputs)
                    jax.block_until_ready(out)
                    del out
                row["fits"] = True
                n_fit += 1
            except Exception as e:
                text = "%s\n%s" % (e, traceback.format_exc(limit=8))
                parsed = parse_oom(text)
                if parsed is not None:
                    row.update(parsed)
                else:
                    row["error_class"] = "other"
                    lines = str(e).strip().splitlines()
                    row["raw_line"] = lines[0][:300] if lines else repr(e)
            report["rows"].append(row)
        report["n_configs"] = len(report["rows"])
        report["n_fit"] = n_fit
    except Exception:
        report["status"] = "FAIL"
        report["exception"] = traceback.format_exc()
    return report


def tsv_lines(report: dict) -> list[str]:
    out = ["config\tfits\trequested\tlimit\terror_class"]
    for row in report.get("rows", []):
        cfg = json.dumps(row["config"], sort_keys=True)
        out.append("%s\t%s\t%s\t%s\t%s" % (
            cfg, str(row["fits"]).lower(),
            _fmt_bytes(row["requested_bytes"]), _fmt_bytes(row["limit_bytes"]),
            row["error_class"] or "-"))
    return out
