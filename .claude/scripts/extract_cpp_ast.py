#!/usr/bin/env python3
"""Extract AST snapshot from C/C++ source using tree-sitter.

Sibling to extract_ast.py (which handles Python via griffe). Outputs to
the same wiki/codebases/<slug>/_ast/ tree, but with filename `cpp.md`
per directory to avoid collision with Python's `README.md`.

Output:
  <output>/<rel_path>/cpp.md                ← per-dir C++ AST (own definitions only)
  <output>/_cpp_skeleton.md                 ← repo-wide C++ skeleton (no docstrings)

Usage:
  python .claude/scripts/extract_cpp_ast.py \\
    --source raw/code/cpp_project \\
    --output wiki/codebases/cpp_project/_ast/

Tolerant of missing #includes — tree-sitter is purely syntactic, doesn't
resolve dependencies. Works on any C/C++ source tree without setup.
"""
from __future__ import annotations

import argparse
import datetime
import os
import re
import subprocess
import sys
from pathlib import Path

import tree_sitter
import tree_sitter_cpp


# ----------------------------------------------------------------------------
# Tree-sitter setup
# ----------------------------------------------------------------------------

CPP_LANG = tree_sitter.Language(tree_sitter_cpp.language())
PARSER = tree_sitter.Parser(CPP_LANG)

# Macro patterns that are perf-relevant for torch-style codebases.
MACRO_INTEREST = re.compile(
    r"^(TORCH_|AT_DISPATCH|XLA_|TPU_|PJRT_|REGISTER_)|_REGISTER$|_REGISTER_OP$"
)

# Pattern for names that LOOK like macro invocations (mis-parsed by
# tree-sitter when they appear as the first statement in a function body —
# e.g. `TT_KERNEL(...)` or `ABSL_GUARDED_BY(mutex)` get reported as if
# they were the function definition with the rest of the body eaten into
# the signature). All-caps + underscores, 2+ chars.
LOOKS_LIKE_MACRO = re.compile(r"^[A-Z][A-Z0-9_]+$")

# Whitelist for legitimate all-caps function names we want to keep.
MACRO_NAME_WHITELIST = {"TEST_F", "TEST_P", "TYPED_TEST", "TEST"}

# Hard cap on signature length. Anything longer is almost certainly a
# macro-eaten function body. We truncate rather than skip so the entry's
# presence is still visible.
SIG_MAX = 200

# Hard cap on name length — a real function name is never this long. A
# longer "name" usually means the declarator parse went off the rails.
NAME_MAX = 80

# File extensions we parse.
CPP_EXTS = {".h", ".hpp", ".hh", ".cpp", ".cc", ".cxx", ".c"}

# Directory names to skip entirely.
SKIP_DIRS = {
    "__pycache__", ".git", "build", "bazel-bin", "bazel-out", "bazel-testlogs",
    "bazel-bin", "bazel-workspace", "third_party", "_skbuild", "dist",
    ".pytest_cache", "node_modules",
}


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


def text_of(node) -> str:
    if node is None:
        return ""
    try:
        return node.text.decode("utf-8", errors="ignore")
    except Exception:
        return ""


def line_of(node) -> int:
    return node.start_point[0] + 1 if node else 0


def collapse_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def is_macro_misparse(name: str, sig: str) -> bool:
    """True if (name, sig) look like a macro invocation tree-sitter mis-parsed
    as a function definition (with the rest of the function body absorbed
    into the signature)."""
    if not name:
        return True
    if "\n" in name or "{" in name or len(name) > NAME_MAX:
        return True
    # All-caps macro pattern, unless whitelisted
    base = name.split("::")[-1]
    if LOOKS_LIKE_MACRO.match(base) and base not in MACRO_NAME_WHITELIST:
        return True
    return False


def truncate_sig(sig: str) -> str:
    if len(sig) > SIG_MAX:
        return sig[: SIG_MAX - 4] + " ...)"
    return sig


# ----------------------------------------------------------------------------
# AST walking — extract entities per file
# ----------------------------------------------------------------------------


def walk_namespace_path(node) -> list[str]:
    """Walk parents to compute the enclosing namespace path for `node`."""
    path = []
    cur = node.parent
    while cur is not None:
        if cur.type == "namespace_definition":
            name_node = cur.child_by_field_name("name")
            nm = text_of(name_node) if name_node else "(anonymous)"
            path.append(nm)
        elif cur.type in ("class_specifier", "struct_specifier"):
            # Don't include classes in namespace path — handled separately
            pass
        cur = cur.parent
    return list(reversed(path))


def declarator_name(decl_node) -> str:
    """Recursively pull the identifier out of a (possibly-nested) declarator."""
    if decl_node is None:
        return ""
    # Common simple cases first
    if decl_node.type == "identifier":
        return text_of(decl_node)
    if decl_node.type in ("field_identifier", "type_identifier",
                          "qualified_identifier", "operator_name",
                          "destructor_name"):
        return text_of(decl_node)
    # Pointer / reference / function declarators wrap an inner declarator
    inner = decl_node.child_by_field_name("declarator")
    if inner:
        return declarator_name(inner)
    # Fallback — find first identifier descendant
    for child in decl_node.children:
        if child.type in ("identifier", "field_identifier", "qualified_identifier"):
            return text_of(child)
    return text_of(decl_node).split("(")[0].strip()


def function_signature(decl_node) -> str:
    """Return '(params)' for a function/method declarator."""
    if decl_node is None:
        return "(...)"
    # Find function_declarator descendant
    fd = decl_node
    while fd and fd.type != "function_declarator":
        inner = fd.child_by_field_name("declarator")
        if inner is None:
            # search children
            found = None
            for c in fd.children:
                if c.type == "function_declarator":
                    found = c
                    break
            fd = found
        else:
            fd = inner
    if fd is None or fd.type != "function_declarator":
        return "(...)"
    params = fd.child_by_field_name("parameters")
    if params is None:
        return "(...)"
    return collapse_ws(text_of(params))


def base_classes(class_node) -> list[str]:
    """Pull '[name, ...]' from a class_specifier's base_class_clause."""
    bcc = class_node.child_by_field_name("base_class_clause")
    if bcc is None:
        return []
    bases = []
    for child in bcc.children:
        if child.type in ("type_identifier", "qualified_identifier"):
            bases.append(text_of(child))
    return bases


def is_function_decl(decl_node) -> bool:
    """True if a `declaration` node is for a function (has function_declarator)."""
    def find_func(n):
        if n is None:
            return False
        if n.type == "function_declarator":
            return True
        for c in n.children:
            if find_func(c):
                return True
        return False
    return find_func(decl_node)


def extract_file(file_path: Path) -> dict:
    """Parse one C/C++ file and return structured entity lists."""
    try:
        src = file_path.read_bytes()
    except Exception:
        return None
    tree = PARSER.parse(src)
    root = tree.root_node

    out = {
        "file": file_path.name,
        "namespaces": [],   # list of (fqn, line)
        "classes": [],      # list of dict: {ns, name, bases, line, methods: [{name, sig, line}]}
        "functions": [],    # list of dict: {ns, name, sig, line}
        "macros": [],       # list of (name, line)
    }
    seen_namespaces = set()

    def walk(node):
        if node.type == "namespace_definition":
            name_node = node.child_by_field_name("name")
            nm = text_of(name_node) if name_node else "(anonymous)"
            parent_path = walk_namespace_path(node)
            fqn = "::".join(parent_path + [nm])
            if fqn not in seen_namespaces:
                seen_namespaces.add(fqn)
                out["namespaces"].append((fqn, line_of(node)))
        elif node.type in ("class_specifier", "struct_specifier"):
            name_node = node.child_by_field_name("name")
            if name_node:  # skip anonymous (e.g., struct {...})
                # Only include DEFINITIONS (have a body), not forward declarations
                body = node.child_by_field_name("body")
                if body is not None:
                    ns_path = walk_namespace_path(node)
                    name = text_of(name_node)
                    bases = base_classes(node)
                    cls = {
                        "ns": "::".join(ns_path),
                        "name": name,
                        "kind": "class" if node.type == "class_specifier" else "struct",
                        "bases": bases,
                        "line": line_of(node),
                        "methods": [],
                    }
                    # Extract methods inside class body
                    for child in body.children:
                        if child.type == "function_definition":
                            mname = declarator_name(child.child_by_field_name("declarator"))
                            msig = function_signature(child.child_by_field_name("declarator"))
                            if is_macro_misparse(mname, msig):
                                continue
                            cls["methods"].append({
                                "name": mname, "sig": truncate_sig(msig), "line": line_of(child),
                            })
                        elif child.type == "declaration":
                            decl = child.child_by_field_name("declarator")
                            if is_function_decl(decl):
                                mname = declarator_name(decl)
                                msig = function_signature(decl)
                                if is_macro_misparse(mname, msig):
                                    continue
                                cls["methods"].append({
                                    "name": mname, "sig": truncate_sig(msig), "line": line_of(child),
                                })
                    out["classes"].append(cls)
        elif node.type == "function_definition":
            # Only top-level (not nested in a class — those are caught above)
            parent_kind = node.parent.type if node.parent else ""
            in_class = False
            cur = node.parent
            while cur is not None:
                if cur.type in ("class_specifier", "struct_specifier"):
                    in_class = True
                    break
                cur = cur.parent
            if not in_class:
                decl = node.child_by_field_name("declarator")
                name = declarator_name(decl)
                sig = function_signature(decl)
                if not is_macro_misparse(name, sig):
                    ns_path = walk_namespace_path(node)
                    out["functions"].append({
                        "ns": "::".join(ns_path), "name": name, "sig": truncate_sig(sig),
                        "line": line_of(node),
                    })
        elif node.type == "declaration":
            # Function declaration (no body) — only top-level
            in_class = False
            cur = node.parent
            while cur is not None:
                if cur.type in ("class_specifier", "struct_specifier"):
                    in_class = True
                    break
                cur = cur.parent
            if not in_class:
                decl = node.child_by_field_name("declarator")
                if is_function_decl(decl):
                    name = declarator_name(decl)
                    sig = function_signature(decl)
                    if name and not name.startswith("operator") and not is_macro_misparse(name, sig):
                        ns_path = walk_namespace_path(node)
                        out["functions"].append({
                            "ns": "::".join(ns_path), "name": name, "sig": truncate_sig(sig),
                            "line": line_of(node),
                        })
        elif node.type in ("preproc_def", "preproc_function_def"):
            name_node = node.child_by_field_name("name")
            nm = text_of(name_node) if name_node else ""
            if nm and MACRO_INTEREST.search(nm):
                out["macros"].append((nm, line_of(node)))

        for child in node.children:
            walk(child)

    walk(root)
    return out


# ----------------------------------------------------------------------------
# Markdown formatters
# ----------------------------------------------------------------------------


def fqn(entry) -> str:
    """Return ns::name if ns is non-empty, else just name."""
    if entry["ns"]:
        return f"{entry['ns']}::{entry['name']}"
    return entry["name"]


def format_file_section(data: dict, with_macros: bool = True) -> str:
    """Render one C/C++ file as an H2 section."""
    out = [f"## {data['file']}"]
    if data["namespaces"]:
        nsstr = ", ".join(f"`{n}`" for n, _ in sorted(set(data["namespaces"]))[:6])
        out.append(f"> namespaces: {nsstr}")
    out.append("")

    if data["classes"]:
        # Classes first (most useful for navigation)
        out.append("### Classes / Structs")
        for cls in sorted(data["classes"], key=lambda c: (c["ns"], c["name"])):
            full = fqn(cls)
            bases_str = f" : {', '.join(cls['bases'])}" if cls["bases"] else ""
            kind_mark = "(struct)" if cls["kind"] == "struct" else ""
            line = f"- **{full}{bases_str}** {kind_mark}(line {cls['line']})"
            out.append(line.replace("  ", " ").rstrip())
            for m in cls["methods"]:
                out.append(f"  - `{m['name']}{m['sig']}` (line {m['line']})")
        out.append("")

    if data["functions"]:
        out.append("### Functions")
        for fn in sorted(data["functions"], key=lambda f: (f["ns"], f["name"], f["line"])):
            full = fqn(fn)
            out.append(f"- **{full}{fn['sig']}** (line {fn['line']})")
        out.append("")

    if with_macros and data["macros"]:
        out.append("### Macros (perf-relevant)")
        for nm, ln in sorted(data["macros"]):
            out.append(f"- **{nm}** (line {ln})")
        out.append("")

    if not (data["classes"] or data["functions"] or data["macros"]):
        out.append("*(no top-level entities)*")
        out.append("")
    return "\n".join(out)


# ----------------------------------------------------------------------------
# Filesystem walk
# ----------------------------------------------------------------------------


def find_cpp_dirs(source: Path) -> dict:
    """Return {rel_dir: [Path, ...]} of dirs containing C/C++ files."""
    dirs = {}
    for root, sub, files in os.walk(source):
        # Filter dirs in-place
        sub[:] = [d for d in sub if d not in SKIP_DIRS]
        cpp_files = sorted(
            Path(root) / f for f in files
            if Path(f).suffix in CPP_EXTS
        )
        if cpp_files:
            rel = Path(root).relative_to(source.parent)
            dirs[rel] = cpp_files
    return dirs


def write_dir_cpp(rel_dir: Path, files: list[Path], output: Path,
                  source_parent: Path, commit: str) -> dict:
    """Write cpp.md for one source directory; return the parsed data per file."""
    target_dir = output / rel_dir
    target_dir.mkdir(parents=True, exist_ok=True)

    parsed = []
    for fp in files:
        data = extract_file(fp)
        if data is None:
            continue
        parsed.append(data)

    # Frontmatter
    lines = [
        "---",
        f'title: "C/C++ AST — {rel_dir}"',
        "type: ast-snapshot-cpp",
        "auto_generated: true",
        f"source: {rel_dir}/",
        f"commit: {commit}",
        f"extracted: {datetime.date.today().isoformat()}",
        f"file_count: {len(parsed)}",
        "---",
        "",
        f"# {rel_dir}/ — C/C++ AST",
        "",
        "*Headers (`*.h`/`*.hpp`) and implementation (`*.cpp`/`*.cc`) declarations.*",
        "*Bodies omitted; signatures only. Tree-sitter syntactic parse — tolerant of*",
        "*missing #includes.*",
        "",
    ]
    for data in parsed:
        lines.append(format_file_section(data))

    (target_dir / "cpp.md").write_text("\n".join(lines))
    return parsed


def write_cpp_skeleton(all_data: list[tuple[Path, list[dict]]],
                       output: Path, commit: str, package_name: str) -> None:
    """Single repo-wide _cpp_skeleton.md (no namespaces broken out — flat per dir)."""
    lines = [
        "---",
        f'title: "C/C++ repo skeleton — {package_name}"',
        "type: ast-snapshot-cpp-skeleton",
        "auto_generated: true",
        f"package: {package_name}",
        f"commit: {commit}",
        f"extracted: {datetime.date.today().isoformat()}",
        "---",
        "",
        f"# {package_name} — C/C++ repo skeleton",
        "",
        "*Structure only; no per-namespace grouping. Per-directory detail",
        "(with namespaces, full signatures) is in `cpp.md` at each level.*",
        "",
    ]
    for rel_dir, parsed in sorted(all_data, key=lambda x: str(x[0])):
        if not parsed:
            continue
        # Only emit if dir has at least one class / function / macro
        has_content = any(p["classes"] or p["functions"] or p["macros"] for p in parsed)
        if not has_content:
            continue
        lines.append(f"## {rel_dir}/")
        lines.append("")
        for data in parsed:
            entries = []
            for cls in data["classes"]:
                full = fqn(cls)
                kind = cls["kind"]
                entries.append(f"- **{full}** ({kind}) — {data['file']}:{cls['line']}")
                for m in cls["methods"]:
                    entries.append(f"  - `{m['name']}{m['sig']}` (line {m['line']})")
            for fn in data["functions"]:
                full = fqn(fn)
                entries.append(f"- **{full}{fn['sig']}** (function) — {data['file']}:{fn['line']}")
            for nm, ln in data["macros"]:
                entries.append(f"- **{nm}** (macro) — {data['file']}:{ln}")
            if entries:
                lines.extend(entries)
        lines.append("")
    (output / "_cpp_skeleton.md").write_text("\n".join(lines))


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", required=True, help="Source root dir (e.g., raw/code/cpp_project)")
    p.add_argument("--output", required=True, help="Output dir (will be created)")
    p.add_argument("--commit-from", default=None, help="Path to git repo for SHA")
    p.add_argument("--package-name", default=None, help="Display name for skeleton (defaults to source basename)")
    args = p.parse_args()

    source = Path(args.source).resolve()
    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    commit = get_commit_sha(args.commit_from or str(source))
    pkg_name = args.package_name or source.name

    print(f"[extract_cpp_ast] scanning {source} for C/C++ files...", file=sys.stderr)
    dirs = find_cpp_dirs(source)
    print(f"[extract_cpp_ast] found {len(dirs)} dirs with C/C++ files", file=sys.stderr)

    total_files = sum(len(files) for files in dirs.values())
    print(f"[extract_cpp_ast] parsing {total_files} files...", file=sys.stderr)

    all_data = []
    for i, (rel_dir, files) in enumerate(sorted(dirs.items()), 1):
        if i % 25 == 0 or i == len(dirs):
            print(f"[extract_cpp_ast]   {i}/{len(dirs)} dirs processed", file=sys.stderr)
        parsed = write_dir_cpp(rel_dir, files, output, source.parent, commit)
        all_data.append((rel_dir, parsed))

    print(f"[extract_cpp_ast] writing _cpp_skeleton.md...", file=sys.stderr)
    write_cpp_skeleton(all_data, output, commit, pkg_name)

    n_classes = sum(len(p["classes"]) for _, ps in all_data for p in ps)
    n_funcs = sum(len(p["functions"]) for _, ps in all_data for p in ps)
    n_macros = sum(len(p["macros"]) for _, ps in all_data for p in ps)
    print(f"[extract_cpp_ast] done: {n_classes} classes/structs, {n_funcs} functions, {n_macros} macros", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
