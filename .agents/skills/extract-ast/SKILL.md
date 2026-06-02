---
name: extract-ast
description: Extract an AST snapshot from an ingested codebase under raw/code/<slug>/. Open-ended language detection — counts file extensions, dispatches to the right extractor per language present. Python uses griffe (statically parses without import); C/C++ uses tree-sitter (purely syntactic, tolerant of missing #includes). Writes per-package nested README.md (Python) + per-dir cpp.md (C++) + repo-wide skeleton files to wiki/codebases/<slug>/_ast/. For unsupported languages (Rust, Go, Java, etc.) the skill reports presence and skips, with guidance for adding the extractor. Invoke when ingesting a new codebase (INGEST-CODEBASE step 4.5), when an existing codebase's commit has drifted materially, or ad-hoc when an agent needs structural lookup beyond what the human-curated wiki/codebases/<slug>.md page provides.
---

# /extract-ast — codebase AST snapshot extractor

Snapshots a codebase's structural skeleton (classes, functions, methods, namespaces, perf-relevant macros) into Markdown reference catalog at `wiki/codebases/<slug>/_ast/`. Derived from source like a `wiki/sources/<paper>.md` is derived from `raw/sources/<paper>.pdf` — same pattern: raw/ holds source material, wiki/ holds derived narrative.

The output is the **structural complement** to the human-curated `wiki/codebases/<slug>.md` parent page. Curated page tells you *which knobs matter for performance*; AST snapshot lets you grep for *where a thing is defined and what its signature looks like*.

## When to invoke

- **At INGEST-CODEBASE** (after the human-curated parent page + subpages, before LINT) — file the structural reference alongside the narrative.
- **When a codebase's `commit:` drifts** — re-run to refresh the snapshot. Stale `_ast/` is worse than missing because it lies.
- **Ad-hoc by an agent** — when /formulate-hypothesis or profile-analyzer or another consumer wants to grep "is there a `RMSNorm` class in this repo?" without reading every file.

## Cardinal rules

- **wiki/ is the destination, NOT raw/.** Snapshot is derived narrative; same category as `wiki/sources/<paper>.md`.
- **`_`-prefixed files/dirs in wiki/ are auto-generated.** LINT skips orphan-page checks for them. Human-curated pages don't use `_` prefix.
- **One file per directory.** Python: `README.md` per package (mirroring source layout). C/C++: `cpp.md` per source dir. Both can coexist in the same dir.
- **Frontmatter pins `commit:`.** Consumers can detect stale snapshots by comparing to the live source commit.
- **Don't commit the output unless the user asks.** Skill produces artifacts; commit decision is the user's.

## Arguments

Required:
- `<slug>` — the codebase identifier (e.g., `torchtitan`, `jax`). Resolves to `raw/code/<slug>/`.

Optional (asked or auto-detected if missing):
- `--source-path <path>` — override if the source isn't at `raw/code/<slug>/`.
- `--python-package <name>` — top-level Python package name for griffe. Defaults to detection (see Step 3).
- `--languages <list>` — limit to specific languages (e.g., `python,cpp`). Default: all detected.
- `--commit-from <path>` — git repo for the SHA. Defaults to the source path.

## Step 1 — Resolve the codebase

Normalize the input to a slug + source path:

```bash
SLUG=<user-provided>
SOURCE=raw/code/${SLUG}                          # default
OUTPUT=wiki/codebases/${SLUG}/_ast/

# Verify source exists
[ -d "${SOURCE}" ] || { echo "Source ${SOURCE} not found"; exit 1; }

# Resolve symlinks (raw/code/<slug> is often a symlink to the actual checkout)
SOURCE_REAL=$(readlink -f "${SOURCE}")

# Get commit SHA (optional — the extractor reads this too)
SHA=$(git -C "${SOURCE_REAL}" rev-parse HEAD 2>/dev/null || echo unknown)
```

If `raw/code/<slug>/` doesn't exist, surface "no ingested codebase at <path>; ingest first (see SCHEMA INGEST-CODEBASE)" and stop.

## Step 2 — Inventory languages

Count files by extension to determine which extractors to run:

```bash
# Skip dirs that shouldn't be scanned (build artifacts, caches, vendored deps)
EXCLUDE='-not -path "*/build/*" -not -path "*/bazel-*/*" -not -path "*/__pycache__/*" \
         -not -path "*/.git/*" -not -path "*/node_modules/*" \
         -not -path "*/third_party/*"'

# Per-language counts
PY_COUNT=$(find "${SOURCE_REAL}" -name "*.py" ${EXCLUDE} | wc -l)
CPP_COUNT=$(find "${SOURCE_REAL}" \( -name "*.h" -o -name "*.hpp" -o -name "*.cpp" \
            -o -name "*.cc" -o -name "*.cxx" -o -name "*.c" \) ${EXCLUDE} | wc -l)
RS_COUNT=$(find "${SOURCE_REAL}" -name "*.rs" ${EXCLUDE} | wc -l)
GO_COUNT=$(find "${SOURCE_REAL}" -name "*.go" ${EXCLUDE} | wc -l)
TS_COUNT=$(find "${SOURCE_REAL}" \( -name "*.ts" -o -name "*.tsx" -o -name "*.js" \) ${EXCLUDE} | wc -l)
JAVA_COUNT=$(find "${SOURCE_REAL}" -name "*.java" ${EXCLUDE} | wc -l)
```

Report the inventory before dispatching:

```
Inventory for <slug> @ <sha>:
  Python: <N> files
  C/C++:  <N> files
  Rust:   <N> files (unsupported — will skip)
  Go:     <N> files (unsupported — will skip)
  ...
```

## Step 3 — Detect Python package root (if Python present)

griffe requires a top-level Python package name (e.g., `torchtitan`, `jax`). Default heuristic:

1. **Match the slug**: if `${SOURCE_REAL}/${SLUG}/__init__.py` exists, use `${SLUG}`. This handles the common case where the repo dir name matches the Python package name.
2. **Single top-level package**: if only one dir directly under `${SOURCE_REAL}` contains `__init__.py`, use that.
3. **Ambiguous**: if multiple top-level packages exist (rare — e.g., a monorepo), use `AskUserQuestion` to pick:

   ```
   Question: "Multiple Python packages found. Which is the top-level for AST extraction?"
   Options: list each dir under ${SOURCE_REAL} that has __init__.py
   ```

4. **None found**: skip the Python pass. The codebase is C/C++-only or has Python only in non-package layout (scripts, namespace packages).

If `--python-package <name>` was passed, use it verbatim — skip detection.

## Step 4 — Run extractors per language

Always print the command before executing so the user sees what's happening.

### Python (if `PY_COUNT > 0` and package detected)

```bash
python3 .claude/scripts/extract_ast.py \
  --source "${SOURCE_REAL}" \
  --package "${PYTHON_PACKAGE}" \
  --output "${OUTPUT}" \
  --commit-from "${SOURCE_REAL}"
```

Writes:
- `${OUTPUT}/${PYTHON_PACKAGE}/<rel_path>/README.md` per package (nested package-mirror)
- `${OUTPUT}/_skeleton.md` — repo-wide Python skeleton (no docstrings)

### C/C++ (if `CPP_COUNT > 0`)

```bash
python3 .claude/scripts/extract_cpp_ast.py \
  --source "${SOURCE_REAL}" \
  --output "${OUTPUT}" \
  --commit-from "${SOURCE_REAL}" \
  --package-name "${SLUG}"
```

Writes:
- `${OUTPUT}/<rel_path>/cpp.md` per directory containing C/C++ files
- `${OUTPUT}/_cpp_skeleton.md` — repo-wide C/C++ skeleton

### Other languages (Rust, Go, Java, TypeScript, Bash, BUILD files)

Currently **report-and-skip**:

```
WARNING: <slug> contains <N> .rs files but no Rust extractor is registered.
Skipping. To add Rust support, see "Adding new languages" in
.claude/skills/extract-ast/SKILL.md.
```

Same pattern for `.go`, `.java`, `.ts/.tsx/.js`, `.sh`, BUILD/BUILD.bazel. Don't fail the skill — produce what we can, document what we can't.

## Step 5 — Verify outputs

Sanity check that something was actually produced:

```bash
# Python verification
if [ "${PY_COUNT}" -gt 0 ]; then
  README_COUNT=$(find "${OUTPUT}" -name "README.md" | wc -l)
  [ "${README_COUNT}" -gt 0 ] || echo "WARNING: Python extractor produced no READMEs"
fi

# C/C++ verification
if [ "${CPP_COUNT}" -gt 0 ]; then
  CPP_COUNT_OUT=$(find "${OUTPUT}" -name "cpp.md" | wc -l)
  [ "${CPP_COUNT_OUT}" -gt 0 ] || echo "WARNING: C++ extractor produced no cpp.md files"
fi
```

Spot-check by reading 2-3 generated files chosen randomly to verify format quality. Look for:
- Frontmatter present with `commit:` matching the source SHA
- At least one class or function with line number
- No garbage entries (multi-line "signatures", names with `{` or `\n`, etc.)

If spot-check fails (garbage entries visible), surface the issue and stop. Don't pretend the output is good when it isn't.

## Step 6 — Summarize to user

Report what was produced:

```
Extraction complete for <slug> @ <sha>:

  Python:  <N_packages> packages, <N_modules> single-file modules
           → wiki/codebases/<slug>/_ast/<package>/...
           → wiki/codebases/<slug>/_ast/_skeleton.md (<N_lines> lines)

  C/C++:   <N_classes> classes/structs, <N_functions> functions, <N_macros> macros
           → wiki/codebases/<slug>/_ast/<rel_path>/cpp.md (in <N_dirs> dirs)
           → wiki/codebases/<slug>/_ast/_cpp_skeleton.md (<N_lines> lines)

  Skipped: <list of unsupported languages with file counts>

  Total disk: <size>
  Total files: <count>

Inspect with:
  - Per-package detail: ls wiki/codebases/<slug>/_ast/
  - Repo-wide grep:     grep -rn '<query>' wiki/codebases/<slug>/_ast/
  - Single-file overview: head -50 wiki/codebases/<slug>/_ast/_skeleton.md

Commit with:
  git add wiki/codebases/<slug>/_ast/
  git commit -m "ast-snapshot: <slug> @ <short-sha>"
```

Surface any WARNINGs from Step 5 here too — the summary should not hide problems.

## Adding new languages

This skill is intentionally extensible. To add support for a new language (e.g., Rust):

1. **Pick a parser**. Two paths:
   - **Semantic** (e.g., rust-analyzer): handles types, traits, generics correctly. Requires resolved dependencies — fails on codebases with unresolved `Cargo.toml` paths.
   - **Syntactic** (tree-sitter + per-language grammar): purely structural. Tolerant of missing dependencies. **Strongly preferred** for our use case — we want structural snapshots of arbitrary codebases without setup ceremony.

   For tree-sitter, install: `pip install tree-sitter tree-sitter-<lang>` (e.g., `tree-sitter-rust`, `tree-sitter-go`, `tree-sitter-java`).

2. **Write `.claude/scripts/extract_<lang>_ast.py`**. Use `extract_cpp_ast.py` as the template — same structure (per-dir walker, per-file extractor, repo-wide skeleton, frontmatter). Adapt the node-type matching to the language's grammar:
   - Rust: `struct_item`, `enum_item`, `impl_item`, `function_item`, `trait_item`, `macro_definition`
   - Go: `type_declaration`, `function_declaration`, `method_declaration`, `interface_type`
   - Java: `class_declaration`, `interface_declaration`, `method_declaration`, `enum_declaration`
   - TypeScript: `class_declaration`, `function_declaration`, `interface_declaration`, `type_alias_declaration`

3. **Beware macro-misparse equivalents.** Tree-sitter often gets confused when expression-level constructs appear where statements are expected. C/C++ had `TT_KERNEL(...)` body-eating; expect similar issues in any language with macros (Rust `macro_rules!`, OCaml ppx, etc.). The filters in `extract_cpp_ast.py` (`is_macro_misparse`, `truncate_sig`, name-length cap) are a template — port them.

4. **Filter re-exports at the package-walk level**, not just at the entity level. Most languages with module systems have some equivalent of Python's `from .x import Y` re-export pattern (Rust `pub use`, Java `import` aliases, TypeScript barrel exports). Without an alias filter at the package-walk level, the extractor will walk into re-exported subpackages and create duplicated subtrees, possibly with cyclic alias chains that crash the parser. The Python extractor's `submodules_packages` and `submodules_files` helpers filter `is_alias` — port the same pattern. Symptom of missing this filter: output dir is 10×+ larger than expected and the parser hangs or crashes during a deep walk.

4. **Use a distinct output filename per language**: `cpp.md` for C/C++, `rust.md` for Rust, `go.md` for Go, etc. They coexist in the same directory next to `README.md` (Python). This is the convention; don't deviate without reason.

5. **Update this skill's Step 4** to dispatch to the new extractor when files of that type are detected. Update Step 2's inventory to count the new extension.

6. **Update the language-presence report** (Step 6's summary) so the new language shows up.

7. **Validate on a small codebase first**, then on a large one. Issues that don't show at small scale (alias cycles, deep recursion, parser pathologies) often surface at large scale. The Python extractor's alias-skip + RecursionError-tolerance came from jax exposing what torchtitan didn't. Expect every language to have its own "large scale gotcha"; budget time to diagnose + fix before declaring the language supported.

## Failure modes to handle

- **`raw/code/<slug>/` not found** — refuse with "no ingested codebase at <path>"; suggest INGEST-CODEBASE.
- **Source is a stale symlink** — readlink fails; surface and stop.
- **Source has no recognized files** — report inventory (all zeros), produce no output, exit gracefully.
- **Python package detection ambiguous** — `AskUserQuestion` per Step 3.
- **Extractor script missing** (e.g., `extract_ast.py` deleted) — fail with the missing path; suggest restoring from git.
- **Extractor crashes mid-run** — surface stderr; don't commit partial output. Output dir may be in inconsistent state — recommend `rm -rf wiki/codebases/<slug>/_ast/` and re-run.
- **Spot-check reveals garbage** — DON'T mark the run successful. Report the specific garbage pattern; suggest filter additions to the extractor script.
- **Output is wildly out of proportion to source size** (e.g., 100+ MB for <1000 modules) — alias-bloat signature. Caused by the extractor walking into re-exported subpackages and creating duplicated subtrees alongside their canonical locations. The Python extractor (`extract_ast.py`) now filters aliases in `submodules_packages` / `submodules_files`. If you see this for a future language extractor, port the same filter. Validated rough scale: a Python codebase produces roughly 1 README per package + 3-4 KB per source entity. torchtitan (50 packages, 750 entities) = 932 KB; jax (84 packages, 8000+ entities) = 3.6 MB. Anything dramatically off these ratios deserves investigation before commit.
- **`RecursionError` in griffe** (Python only) — happens on codebases with deep alias chains where `canonical_path` cycles. `extract_ast.py` raises `sys.recursionlimit` to 10000 and catches RecursionError in `is_owned_here()` (defaults to including the entry); the alias-skip filter at the package-walk level avoids most of these cycles. If you ever see RecursionError leak through to the user, the cycle has reached a path the filters don't cover — add a try/except at that site.

## Cost expectations

Per-codebase wall time on the project's typical hardware (measurements
from the three pilot runs):

| Codebase | Python files | C/C++ files | Python time | C/C++ time | Disk |
|----------|-------------:|------------:|------------:|-----------:|-----:|
| torchtitan | ~600 | 0   | ~10 s      | n/a        | 932 KB |
| cpp_project | 321  | 624 | ~3 s       | ~10 s      | 2.3 MB |
| jax        | 995  | 233 | 5.16 s     | <1 s       | 3.6 MB |

Rules of thumb:
- **Python (griffe)**: ~5-15s per 1000 modules. Mostly griffe's load
  + alias resolution; the walk + write is fast.
- **C/C++ (tree-sitter)**: ~1s per 100 files. Pure syntactic parse,
  no dependency resolution.
- **Disk**: ~3-4 KB per source entity (class / function / method).
  Output scales sub-linearly with source size because we drop bodies
  — only signatures + docstrings (Python) or signatures (C/C++) survive.

If a Python pass takes minutes (not seconds) for a codebase under
1000 modules, suspect an alias-chain cycle. The extractor catches
RecursionError defensively, but a pathological cycle can still slow
the walk dramatically. The first jax run (before the alias-skip fix)
took 27 minutes before crashing; with the fix it's 5 seconds. If you
see anything like that, the cycle has reached a path the filters
don't cover — diagnose (see Failure modes) before re-running.

## What this skill does NOT do

- **Does not regenerate the human-curated `wiki/codebases/<slug>.md` parent page.** That's manual narrative.
- **Does not update wiki/index.md.** Add a featured-reference subsection by hand if desired.
- **Does not commit the output.** Producing artifacts ≠ deciding what enters version control.
- **Does not modify raw/.** Source is immutable.
- **Does not do cross-codebase analysis.** Each invocation is one codebase.
- **Does not preserve comments.** Per design discussion: high-value comments (TODO/FIXME/HACK) live inside function bodies, which we skip; adjacent comments are mostly noise; docstrings are already preserved.
- **Does not show re-exports.** Aliased classes / functions / submodules appear at their *canonical* definition site only, not at every place they're re-exported via `from .X import Y`. For Python this means `jax.numpy.foo` may be reachable in the source via `import jax.numpy` but the AST snapshot only documents it under `jax/_src/numpy/...` (the actual definition). Consumers querying "where is X?" should grep across the whole `_ast/` tree, not assume re-export paths.

## Validated on (chronological)

| Codebase | Run date | Result | Notes |
|----------|----------|--------|-------|
| torchtitan | 2026-05-31 | clean first run | Python-only; surfaced the inheritance-leakage + re-export-duplication filters now in `is_owned_here` |
| cpp_project | 2026-05-31 | clean after one filter pass | Mixed Python + C/C++; surfaced the C++ macro-misparse filters (`is_macro_misparse`, `truncate_sig`) now in `extract_cpp_ast.py` |
| jax        | 2026-06-01 | clean after two fixes | Python-heavy with deep alias chains; surfaced RecursionError tolerance + package-walk-level alias filter — both now in `extract_ast.py` |

Pattern: each new codebase has surfaced one or two real robustness
bugs in the extractors. Before declaring the skill validated on a
language, expect at least one round of diagnose-and-fix per codebase
beyond the first.

## See also

- `.claude/scripts/extract_ast.py` — Python extractor (griffe) with
  alias-filter at package-walk level + RecursionError tolerance
- `.claude/scripts/extract_cpp_ast.py` — C/C++ extractor (tree-sitter)
  with macro-misparse filters + signature truncation
- `SCHEMA.md` — wiki structure + INGEST-CODEBASE operation
- `wiki/codebases/torchtitan/_ast/` — Python-only pilot output
- `wiki/codebases/cpp_project/_ast/` — mixed Python + C++ pilot output
- `wiki/codebases/jax/_ast/` — large Python codebase pilot output
