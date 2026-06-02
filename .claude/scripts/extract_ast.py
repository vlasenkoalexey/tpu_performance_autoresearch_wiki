#!/usr/bin/env python3
"""Extract AST snapshot from a Python codebase using griffe.

Produces a nested package-mirror tree of Markdown skeletons:

  <output>/<package>/README.md                  ← per-package AST (with docstrings)
  <output>/<package>/<subpackage>/README.md     ← nested, mirrors source layout
  <output>/_skeleton.md                         ← single repo-wide skeleton (no docstrings)

Designed for the tpu_performance_autoresearch_wiki — see
wiki/codebases/<slug>/_ast/ convention.

Usage:
  python .claude/scripts/extract_ast.py \\
    --source raw/code/torchtitan \\
    --package torchtitan \\
    --output wiki/codebases/torchtitan/_ast/
"""
from __future__ import annotations

import argparse
import datetime
import subprocess
import sys
from pathlib import Path

# Large codebases (jax has 995 .py files with deep alias chains) can hit
# Python's default 1000-frame limit during griffe's canonical_path
# resolution. Lift it; we catch any remaining RecursionError below.
sys.setrecursionlimit(10000)

import griffe


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------


def get_commit_sha(repo_path: str) -> str:
    try:
        r = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_path, capture_output=True, text=True, check=True,
        )
        return r.stdout.strip()
    except Exception:
        return "unknown"


def is_package(module) -> bool:
    """True if module corresponds to a Python package (__init__.py)."""
    fp = getattr(module, "filepath", None)
    if fp is None:
        return False
    try:
        return Path(str(fp)).name == "__init__.py"
    except Exception:
        return False


def safe_str(x) -> str:
    try:
        return str(x)
    except Exception:
        return "<?>"


def first_line_of_docstring(obj) -> str:
    ds = getattr(obj, "docstring", None)
    if not ds or not getattr(ds, "value", None):
        return ""
    first = ds.value.strip().split("\n")[0].strip()
    # Strip trailing punctuation that's awkward in our markdown italic form
    return first


def format_signature(func) -> str:
    """Render (param, param=default, ...) — best effort, never raise."""
    parts = []
    try:
        for p in func.parameters:
            piece = p.name
            ann = getattr(p, "annotation", None)
            if ann:
                piece = f"{piece}: {safe_str(ann)}"
            default = getattr(p, "default", None)
            if default is not None:
                piece = f"{piece}={safe_str(default)}"
            parts.append(piece)
    except Exception:
        return "(...)"
    return f"({', '.join(parts)})"


def format_class_bases(cls) -> str:
    bases = getattr(cls, "bases", None)
    if not bases:
        return ""
    try:
        return f"({', '.join(safe_str(b) for b in bases)})"
    except Exception:
        return ""


def lineno(obj) -> int:
    return getattr(obj, "lineno", 0) or 0


def is_owned_here(obj, owner_path: str) -> bool:
    """True if obj is *canonically* defined at owner_path.<obj.name>.

    Filters out:
      - Inherited members (griffe sets `inherited=True` on subclass-resolved
        method lookups).
      - Re-exported aliases (canonical_path points elsewhere — e.g. an
        __init__.py that does `from .model import Foo` would otherwise
        produce a duplicate Foo entry in the __init__.py section).

    Tolerates RecursionError — griffe has alias-chain cycles in some large
    packages (jax) that cause canonical_path to recurse infinitely. When
    that happens we default to including the entry (the alias-skip in
    walk_packages catches most of these at the package-walk level anyway).
    """
    try:
        if getattr(obj, "inherited", False):
            return False
        canonical = getattr(obj, "canonical_path", None)
        if canonical is None:
            return True
        name = getattr(obj, "name", None)
        if name is None:
            return True
        return canonical == f"{owner_path}.{name}"
    except RecursionError:
        return True


def owned_members(container, kind: str, owner_path: str | None = None) -> list:
    """Sorted list of (name, obj) pairs for `container.<kind>` that are owned here.

    `kind` is one of: 'classes', 'functions', 'modules'.
    `owner_path` defaults to container.canonical_path (or .path) — needed for
    classes because a method's canonical_path is `<class.canonical_path>.<method>`.
    """
    if owner_path is None:
        owner_path = getattr(container, "canonical_path", None) or container.path
    items = getattr(container, kind, None) or {}
    out = []
    for name, m in items.items():
        if is_owned_here(m, owner_path):
            out.append((name, m))
    return sorted(out)


def rel_filepath(obj, source_root: Path) -> Path:
    fp = getattr(obj, "filepath", None)
    if fp is None:
        return Path("?")
    try:
        return Path(str(fp)).relative_to(source_root)
    except Exception:
        return Path(str(fp)).name


def filename_only(obj) -> str:
    fp = getattr(obj, "filepath", None)
    if fp is None:
        return "?"
    return Path(str(fp)).name


# ----------------------------------------------------------------------------
# Selectors
# ----------------------------------------------------------------------------


def submodules_files(pkg):
    """Yield (name, mod) for single-file modules OWNED by this package, sorted.

    Excludes aliases (re-exported modules whose canonical location is
    elsewhere). The canonical location handles them when we reach it.
    Without this filter, the same module would appear in multiple
    package READMEs and inflate the snapshot.
    """
    items = []
    for name, m in pkg.modules.items():
        if is_package(m):
            continue
        if getattr(m, "is_alias", False):
            continue
        items.append((name, m))
    return sorted(items)


def submodules_packages(pkg):
    """Yield (name, sub) for subpackages OWNED by this package, sorted.

    Excludes aliases (e.g. `jax.jaxlib` may be re-exported into jax.modules
    even though jaxlib is a sibling package on disk — walking it would
    create a duplicated subtree under jax/ AND traverse cyclic alias
    chains that crash griffe's canonical_path resolver). The canonical
    location handles them.
    """
    items = []
    for name, m in pkg.modules.items():
        if not is_package(m):
            continue
        if getattr(m, "is_alias", False):
            continue
        items.append((name, m))
    return sorted(items)


# ----------------------------------------------------------------------------
# Section formatters (per-package README.md, WITH docstrings)
# ----------------------------------------------------------------------------


def format_module_section(module, with_docstring: bool = True) -> str:
    """Render one Python module as an H2 section (own definitions only)."""
    fname = filename_only(module)
    out = [f"## {fname}"]
    if with_docstring:
        ds = first_line_of_docstring(module)
        if ds:
            out.append(f"> {ds}")
    out.append("")

    classes = owned_members(module, "classes")
    functions = owned_members(module, "functions")

    if classes:
        out.append("### Classes")
        for cname, cls in classes:
            bases = format_class_bases(cls)
            line = f"- **{cls.name}{bases}** (line {lineno(cls)})"
            if with_docstring:
                ds = first_line_of_docstring(cls)
                if ds:
                    line += f" — *{ds}*"
            out.append(line)
            # Methods — filter to own only via cls.canonical_path
            owner_path = getattr(cls, "canonical_path", None) or cls.path
            for mname, method in owned_members(cls, "functions", owner_path=owner_path):
                sig = format_signature(method)
                mline = f"  - `{method.name}{sig}` (line {lineno(method)})"
                if with_docstring:
                    mds = first_line_of_docstring(method)
                    if mds:
                        mline += f" — *{mds}*"
                out.append(mline)
        out.append("")

    if functions:
        out.append("### Functions")
        for fname2, fn in functions:
            sig = format_signature(fn)
            line = f"- **{fn.name}{sig}** (line {lineno(fn)})"
            if with_docstring:
                ds = first_line_of_docstring(fn)
                if ds:
                    line += f" — *{ds}*"
            out.append(line)
        out.append("")

    if not classes and not functions and not first_line_of_docstring(module):
        out.append("*(no top-level classes or functions defined here)*")
        out.append("")

    return "\n".join(out)


def write_package_readme(
    pkg, output_dir: Path, source_root: Path, commit: str, package_root_name: str
) -> None:
    """Write one package's README.md (covers __init__.py + all single-file modules)."""
    output_dir.mkdir(parents=True, exist_ok=True)

    rel_dir = rel_filepath(pkg, source_root.parent).parent  # path to dir containing __init__.py
    dotted = pkg.path  # griffe's dotted name

    files = submodules_files(pkg)
    subs = submodules_packages(pkg)

    # Frontmatter
    lines = [
        "---",
        f'title: "AST — {dotted}"',
        "type: ast-snapshot",
        "auto_generated: true",
        f"package: {dotted}",
        f"source: {rel_dir}/",
        f"commit: {commit}",
        f"extracted: {datetime.date.today().isoformat()}",
        f"module_count: {1 + len(files)}",  # +1 for __init__
        "---",
        "",
        f"# {rel_dir}/",
        "",
    ]

    # __init__.py section (only if it has own definitions or a docstring)
    has_init_content = bool(
        owned_members(pkg, "classes") or owned_members(pkg, "functions")
        or first_line_of_docstring(pkg)
    )
    if has_init_content:
        init_section = format_module_section(pkg, with_docstring=True)
        init_section = init_section.replace(
            f"## {filename_only(pkg)}", "## __init__.py", 1
        )
        lines.append(init_section)

    # Single-file modules
    for name, mod in files:
        lines.append(format_module_section(mod, with_docstring=True))

    # Subpackages index
    if subs:
        lines.append("## Subpackages")
        for name, sub in subs:
            n = 1 + len(submodules_files(sub))
            lines.append(f"- [{name}/]({name}/README.md) — {n} module{'s' if n != 1 else ''}")
        lines.append("")

    (output_dir / "README.md").write_text("\n".join(lines))


def walk_packages(
    pkg, output_dir: Path, source_root: Path, commit: str, package_root_name: str
) -> None:
    """Recursively walk packages, writing one README.md per directory."""
    write_package_readme(pkg, output_dir, source_root, commit, package_root_name)
    for name, sub in submodules_packages(pkg):
        walk_packages(sub, output_dir / name, source_root, commit, package_root_name)


# ----------------------------------------------------------------------------
# Repo-wide skeleton (NO docstrings, NO imports — pure structure)
# ----------------------------------------------------------------------------


def emit_skeleton_for_module(mod, lines: list[str]) -> None:
    """Append flat skeleton entries for one module's contents (own definitions only)."""
    fname = filename_only(mod)
    for cname, cls in owned_members(mod, "classes"):
        bases = format_class_bases(cls)
        lines.append(f"- **{cls.name}{bases}** (class) — {fname}:{lineno(cls)}")
        owner_path = getattr(cls, "canonical_path", None) or cls.path
        for mname, method in owned_members(cls, "functions", owner_path=owner_path):
            sig = format_signature(method)
            lines.append(f"  - `{method.name}{sig}` (line {lineno(method)})")
    for fname2, fn in owned_members(mod, "functions"):
        sig = format_signature(fn)
        lines.append(f"- **{fn.name}{sig}** (function) — {fname}:{lineno(fn)}")


def write_skeleton(
    root_pkg, output_root: Path, source_root: Path, commit: str, package_root_name: str
) -> None:
    """Single repo-wide _skeleton.md — package tree as nested H2..Hn sections."""
    lines = [
        "---",
        f'title: "Repo skeleton — {package_root_name}"',
        "type: ast-snapshot-skeleton",
        "auto_generated: true",
        f"package: {package_root_name}",
        f"commit: {commit}",
        f"extracted: {datetime.date.today().isoformat()}",
        "---",
        "",
        f"# {package_root_name} — repo skeleton",
        "",
        "*Structure only; no docstrings, no imports. Per-package detail (with",
        "docstrings) is in the adjacent README.md files at each level.*",
        "",
    ]

    def walk(pkg, level: int = 2):
        rel_dir = rel_filepath(pkg, source_root.parent).parent
        header = "#" * level
        lines.append(f"{header} {rel_dir}/")
        lines.append("")
        # __init__.py contents (own definitions only)
        had_any = False
        if owned_members(pkg, "classes") or owned_members(pkg, "functions"):
            emit_skeleton_for_module(pkg, lines)
            had_any = True
        # Single-file modules — only if they have own definitions
        for name, mod in submodules_files(pkg):
            if not (owned_members(mod, "classes") or owned_members(mod, "functions")):
                continue
            emit_skeleton_for_module(mod, lines)
            had_any = True
        if not had_any:
            lines.append("*(no own definitions in this package)*")
        lines.append("")
        # Recurse
        for name, sub in submodules_packages(pkg):
            walk(sub, level + 1)

    walk(root_pkg)
    (output_root / "_skeleton.md").write_text("\n".join(lines))


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", required=True, help="Dir containing the package (e.g., raw/code/torchtitan)")
    p.add_argument("--package", required=True, help="Top-level package name (e.g., torchtitan)")
    p.add_argument("--output", required=True, help="Output dir (will be created)")
    p.add_argument("--commit-from", default=None, help="Path to git repo for commit SHA (defaults to --source)")
    args = p.parse_args()

    source = Path(args.source).resolve()
    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=True)

    commit_from = args.commit_from or str(source)
    commit = get_commit_sha(commit_from)

    print(f"[extract_ast] loading {args.package} from {source}", file=sys.stderr)
    root = griffe.load(args.package, search_paths=[str(source)])
    print(f"[extract_ast] loaded: {root.path}", file=sys.stderr)

    print(f"[extract_ast] walking packages → {output / args.package}/", file=sys.stderr)
    walk_packages(root, output / args.package, source, commit, args.package)

    print(f"[extract_ast] writing _skeleton.md", file=sys.stderr)
    write_skeleton(root, output, source, commit, args.package)

    # Brief stats
    def count(pkg):
        n_pkgs = 1
        n_files = len(submodules_files(pkg))
        for _, sub in submodules_packages(pkg):
            sub_p, sub_f = count(sub)
            n_pkgs += sub_p
            n_files += sub_f
        return n_pkgs, n_files

    n_pkgs, n_files = count(root)
    print(f"[extract_ast] done: {n_pkgs} packages, {n_files} single-file modules", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
