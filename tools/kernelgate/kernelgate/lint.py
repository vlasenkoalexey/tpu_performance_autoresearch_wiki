"""Static AST prefilter for known reward-hacking / fallback patterns.

Cheap, evadable, still first (Kevin-style zero-reward static checks). Checks:

  L1  try/except wrapping calls inside a compute-path function — the
      classic silent-fallback-to-reference pattern;
  L2  candidate imports the baseline module AND calls baseline's workload
      from a compute-path function (importing baseline only for CONFIG /
      create_inputs is normal and reported as INFO);
  L3  trivial passthrough — an entry-like function that returns one of its
      parameters (optionally via a copy/astype/reshape) without compute;
  L4  no compute primitives anywhere in the module (dot/einsum/matmul/
      pallas_call/...) — the module cannot be doing the work itself.

Advisory: findings set exit code 1, never 2 — pipelines decide whether to
block on it. A clean lint proves nothing (survey item 10).
"""
from __future__ import annotations

import ast

COMPUTE_CALL_NAMES = {
    "dot", "dot_general", "einsum", "matmul", "pallas_call", "softmax",
    "conv", "conv_general_dilated", "scan", "fori_loop", "while_loop",
    "custom_call", "emit_pipeline",
}

PASSTHROUGH_WRAPPERS = {"copy", "astype", "reshape", "asarray", "array", "transpose"}

HELPER_PREFIXES = ("bench", "benchmark", "main", "test", "check", "get_",
                   "run_", "make_", "build_", "verify", "debug", "print_",
                   "create_inputs", "sweep", "plot_")


def _call_name(node: ast.Call) -> str:
    f = node.func
    while isinstance(f, ast.Attribute):
        if isinstance(f.value, ast.Name) or isinstance(f.value, ast.Attribute):
            name = f.attr
            return name
        f = f.value
    if isinstance(f, ast.Name):
        return f.id
    return ""


def _full_call_dotted(node: ast.Call) -> str:
    parts = []
    f = node.func
    while isinstance(f, ast.Attribute):
        parts.append(f.attr)
        f = f.value
    if isinstance(f, ast.Name):
        parts.append(f.id)
    return ".".join(reversed(parts))


def _is_compute_fn(fn: ast.FunctionDef) -> bool:
    return not fn.name.startswith("_") and not any(
        fn.name.startswith(p) for p in HELPER_PREFIXES)


def lint_source(source: str, path: str = "<candidate>") -> dict:
    findings = []
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        return {"cmd": "lint", "path": path, "status": "ERROR",
                "findings": [{"code": "L0", "level": "WARN",
                              "message": "syntax error: %s" % e}]}

    baseline_import_names = set()   # local names bound to the baseline module
    baseline_workload_aliases = set()  # local names bound to baseline's workload
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                if a.name == "baseline":
                    baseline_import_names.add(a.asname or a.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module == "baseline":
                for a in node.names:
                    if "workload" in a.name:
                        baseline_workload_aliases.add(a.asname or a.name)

    if baseline_import_names or baseline_workload_aliases:
        findings.append({
            "code": "L2-info", "level": "INFO",
            "message": "candidate imports the baseline module (%s) — fine for "
                       "CONFIG/create_inputs, checked below for workload calls"
                       % ", ".join(sorted(baseline_import_names | baseline_workload_aliases))})

    functions = [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef,
                                                             ast.AsyncFunctionDef))]
    module_has_compute = False

    for fn in functions:
        compute_path = _is_compute_fn(fn)
        for node in ast.walk(fn):
            if isinstance(node, ast.Call):
                name = _call_name(node)
                if name in COMPUTE_CALL_NAMES:
                    module_has_compute = True

        if not compute_path:
            continue

        # L1: try/except wrapping calls inside a compute-path function
        for node in ast.walk(fn):
            if isinstance(node, ast.Try):
                wraps_call = any(isinstance(n, ast.Call)
                                 for stmt in node.body for n in ast.walk(stmt))
                if wraps_call and node.handlers:
                    findings.append({
                        "code": "L1", "level": "WARN", "function": fn.name,
                        "line": node.lineno,
                        "message": "try/except around calls inside compute-path "
                                   "function %r — possible silent fallback" % fn.name})

        # L2: calling baseline.workload (or an alias) inside a compute path
        for node in ast.walk(fn):
            if isinstance(node, ast.Call):
                dotted = _full_call_dotted(node)
                head = dotted.split(".")[0] if dotted else ""
                if (head in baseline_import_names and "workload" in dotted) or \
                        (dotted in baseline_workload_aliases):
                    findings.append({
                        "code": "L2", "level": "WARN", "function": fn.name,
                        "line": node.lineno,
                        "message": "compute-path function %r calls the baseline "
                                   "workload (%s) — candidate may be relabeling "
                                   "reference output" % (fn.name, dotted)})

        # L3: trivial passthrough
        params = {a.arg for a in fn.args.args + fn.args.posonlyargs + fn.args.kwonlyargs}
        for node in ast.walk(fn):
            if isinstance(node, ast.Return) and node.value is not None:
                v = node.value
                returned = None
                if isinstance(v, ast.Name):
                    returned = v.id
                elif isinstance(v, ast.Call):
                    nm = _call_name(v)
                    if nm in PASSTHROUGH_WRAPPERS and v.args and isinstance(v.args[0], ast.Name):
                        returned = v.args[0].id
                    elif isinstance(v.func, ast.Attribute) and nm in PASSTHROUGH_WRAPPERS \
                            and isinstance(v.func.value, ast.Name):
                        returned = v.func.value.id
                if returned in params:
                    has_compute_in_fn = any(
                        isinstance(n, ast.Call) and _call_name(n) in COMPUTE_CALL_NAMES
                        for n in ast.walk(fn))
                    if not has_compute_in_fn:
                        findings.append({
                            "code": "L3", "level": "WARN", "function": fn.name,
                            "line": node.lineno,
                            "message": "function %r returns input %r without compute "
                                       "— trivial passthrough" % (fn.name, returned)})

    if not module_has_compute:
        findings.append({
            "code": "L4", "level": "WARN",
            "message": "no compute primitives (%s, ...) found anywhere in the module"
                       % ", ".join(sorted(list(COMPUTE_CALL_NAMES))[:4])})

    warn = any(f["level"] == "WARN" for f in findings)
    return {"cmd": "lint", "path": path,
            "findings": findings,
            "status": "FINDINGS" if warn else "CLEAN"}


def run_lint(path: str) -> dict:
    with open(path) as f:
        return lint_source(f.read(), path)
