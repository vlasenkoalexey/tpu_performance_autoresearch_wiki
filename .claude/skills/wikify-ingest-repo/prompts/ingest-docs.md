# Doc-concept extraction — the last synthesis step (per project doc)

Adapts the autoresearch **INGEST-SOURCE** procedure to a code silo: a project's own
docs (README, `docs/**`) carry the maintainers' mental models and the "why" that
source + docstrings don't. For each doc, extract its concepts and write **one
grounded, cross-linked concept page per concept** into `wiki/code/<slug>/doc-concepts/`.

The doc itself is **never moved or copied** — it stays in the repo. You only
extract from it.

**Lens.** If `config/<slug>.md` sets `synthesis_focus`, extract through it — prioritize the
concepts the lens cares about and frame each around it (e.g. a "TPU performance" lens → pull the
perf-relevant guidance, flags, and recipes the doc names). With no lens, extract neutrally.

## Inputs
- The doc worklist: `.cache/docs/<slug>.txt` (repo-relative doc paths), produced by
  `wikify prepare`.
- The repo root (read the actual doc files there).
- The silo's catalog (`wiki/code/<slug>/catalog/`) — the grounding target. Every code
  symbol/API a doc-concept names should link to its catalog entry.
- The silo's existing code concepts (`wiki/code/<slug>/concepts/`) — cross-link to them.

## Method (per doc)
1. **Read the doc fully** — don't skim. Identify its **3–8 load-bearing concepts**
   (a technique, abstraction, subsystem, flag, kernel, workflow it documents). Skip
   pure install/usage boilerplate; keep concepts that explain how the system works.
2. For each concept, **ground it**: find the code symbols it refers to and look them
   up in the catalog (`wiki/code/<slug>/catalog/<module>.md`) to get their `cite:`
   anchors. A doc-concept is valuable precisely because it links the doc's prose to
   the real code.
3. **Survey what's already in the silo BEFORE writing** — `ls wiki/code/<slug>/concepts/`
   and skim titles. A doc-concept almost always overlaps a code concept (e.g. a
   "compilation cache" doc-concept ↔ the `…cache_key` concept page). You must wire
   those links.
4. **Write one page** `wiki/code/<slug>/doc-concepts/<concept-slug>.md` (slug: short,
   lowercase, hyphenated). De-dup: if a concept already has a doc-concept page,
   *update* it (add this doc as a source) rather than duplicate.
5. **Cross-link (REQUIRED where it makes sense — this is the point of the step).**
   Each page connects three ways:
   - **to code concept pages** (`../concepts/<concept>.md`) — the deep page(s) on the
     same subsystem. Look for them in step 3; link every one that's genuinely
     related. (This is what was being missed.)
   - **to catalog files** — both the symbol anchors inline (grounding) AND a link to
     the owning **module catalog page** (`../catalog/<module>.md`) so a reader can
     jump to the full per-module index.
   - **to sibling doc-concepts** (`other-concept.md`).
   Don't force links that don't fit — but if a related code concept exists, linking
   it is mandatory, not optional.

## Page format
```
---
title: <Concept name>
type: doc-concept
provenance: doc
source: <repo-relative doc path, e.g. docs/gpu_to_tpu.md>   # the doc stays there
updated: <date>
status: fresh
---
# <Concept name>

## Definition
2–4 sentences: what it is, in the project's own framing (from the doc).

## In <slug> (grounded)
How it maps to the code — link the symbols the doc names to their catalog entries:
[`Symbol`](../catalog/<module>.md#Qualified.Name). Name the owning module(s).

## Why it matters / when it applies
The doc's rationale and the conditions it calls out.

## Connections
- Code concepts: [<concept>](../concepts/<concept>.md) — the deep page(s) on this
  subsystem (link every related one).
- Module catalogs: [<module>](../catalog/<module>.md) — the full per-module index.
- Related doc-concepts: [other](other-concept.md)

## Source
Extracted from `<repo-relative doc path>` (kept in place).
```

## Hard rules
- **Only cite catalog symbols that exist** — paste the `cite:` link from the catalog
  (`../catalog/<module>.md#anchor`). The finalizer lints doc-concept citations:
  every catalog link must resolve (rule 1). You need NOT confine prose to a subgraph
  (these come from a doc, not a packet) — but never link a symbol that isn't real.
- **Never edit the doc or `raw/`.** Extract only.
- **Ground generously but honestly.** If the doc names a subsystem with no clear
  catalog symbol, describe it in prose and say so — don't invent a link.
- Lead with the mental model; a doc-concept that just restates install steps is noise.

When done, reply one line per doc: doc path → N concept pages written (slugs).
