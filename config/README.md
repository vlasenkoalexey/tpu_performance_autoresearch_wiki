# wikify ingest configs

One `config/<slug>.md` per code repo ingested with the **`wikify-ingest-repo`** skill (see
`SCHEMA.md` → INGEST-CODEBASE step 5). The skill reads these; the grounded catalog lands in
`wiki/codebases/<slug>/`. `.cache/` (SCIP indexes, packets) is gitignored; `wiki/` is committed.

Template — the frontmatter conventions for *this* wiki:

```markdown
---
slug: <slug>                 # matches raw/code/<slug> and wiki/codebases/<slug>/
repo: raw/code/<slug>        # the pinned submodule; wikify indexes it in place
acquire: submodule           # the checkout IS the pin
wiki_subdir: codebases       # → wiki/codebases/<slug>/ (this wiki's layout)
source_type: code            # or `docs` for a documentation-only repo
# languages: [python]        # optional; else auto-detected
# index_shards:              # scope a huge repo (e.g. JAX) to perf-relevant packages only
#   - jax/experimental/pallas/**
#   - jax/_src/pallas/**
---

## Concepts
```

Notes:
- **Scope large repos** with `index_shards` — this wiki is deliberately selective (index only the
  surfaces it uses), whereas wikify defaults to full coverage. Shards reconcile the two.
- **Requires the `wikify` CLI** — `pip install -e` + `setup-vendor.sh` from
  [wikify-repo](https://github.com/vlasenkoalexey/wikify-repo). TS/Go/Rust indexers install on demand.
- Works from **Claude Code, Codex, and Antigravity** — the skill is under `.claude/skills/`, exposed
  to Codex + AG via the `.agents/skills` symlink.
