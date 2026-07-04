---
name: wikify-ingest-repo
description: >
  Ingest a code repo into a grounded, lint-clean markdown wiki an agent can
  answer internals questions from. Idempotent reconcile — first build, version
  bump (--ref), or an added concept are all the same operation. Trigger when the
  user asks to wikify/ingest a repo, build an internals wiki, or update one.
  Accepts a repo URL or local path as the argument and bootstraps `config/<slug>.md`
  itself — the user never hand-writes config.
---

# wikify-ingest-repo

Drive the deterministic `wikify` CLI around one LLM-in-the-loop step: **concept
synthesis**. The CLI does everything else (acquire, SCIP index, graph, diff,
packets, lint, assemble). You write one mechanism page per packet. Never put
synthesis in Python; never push linting into your prose.

## Preconditions
- `wikify` is on PATH and `scip-python` is installed (see the repo's README install steps).

## Input — invoke with the repo to ingest
You are called with a repo **URL or local path** (e.g. `wikify-ingest-repo
https://github.com/owner/myrepo`), or with an existing `<slug>` to update.

**Step 0 — bootstrap the config yourself (never ask the user to write it).** Derive `<slug>`
from the repo (basename, minus `.git`). If `config/<slug>.md` does not already exist, create it:
```
---
slug: <slug>
repo: <the URL or local path>
---
```
No `## Concepts` list is needed — discovery auto-seeds the agenda from code centrality; add seed
concepts later only to go deeper into a subsystem. If a config for that slug already exists,
reuse it (re-ingest is idempotent). Then run the Procedure below with `<slug>`.

> **Docs mode (prose sources).** If the repo is documentation, not code — or you set
> `source_type: docs` in the config — the pipeline is the same shape but prose-grounded:
> `wikify prepare <slug>` emits one **doc packet** per document (no SCIP); you synthesize
> `topics/` + `sources/` pages following **`prompts/synthesis-docs.md`**, citing sections with
> `src:` tokens; `wikify finalize <slug>` gates those citations and runs the coverage floor. The
> grounding anchor is a *source document + section* instead of a symbol; everything below about
> catalogs/concepts is the code path. See design.md "Docs mode".

## Procedure

1. **Prepare (deterministic, no model).** Run:
   ```
   wikify prepare <slug> [--ref <commit>]
   ```
   This acquires + pins the repo, runs scip-python, builds the symbol graph,
   prints the reconcile **plan** (will build / rebuild / leave), and writes one
   packet per to-build concept at `.cache/packets/<slug>/<concept>.md`. If the
   plan is a no-op, STOP — the wiki is already converged.

2. **Synthesize (this is your job — heavy processing, not annotation).** For EACH
   packet the plan built, read the packet and follow
   `prompts/synthesis.md` exactly to write ONE file: the
   mechanism page `wiki/code/<slug>/concepts/<concept>.md`. The packet is your grounding
   index; **READ THE ACTUAL SOURCE** at the `file:line` it gives you (the snippets
   are truncated) so the page explains *how it really works and why*, not a cited
   trace. Lead with Overview + a Mermaid **Diagram** + Design rationale; weave
   citations (a few per paragraph, no `[extracted →]` tags). You do **not** create
   symbol stubs — paste each symbol's `cite:` link from the Subgraph verbatim (it
   resolves to the catalog anchor). Cite ONLY Subgraph symbols; ungrounded → a
   `> [!inferred]` block.

3. **Overview (after all concepts exist).** Follow
   `prompts/overview.md` to write `wiki/code/<slug>/overview.md` —
   the highest-level page: the main concepts, core system-level Mermaid diagrams,
   and a map of which concept answers which question. It is synthesis over the
   concept pages (no new grounding).

4. **Doc concepts (LAST synthesis step).** `prepare` wrote a doc worklist at
   `.cache/docs/<slug>.txt` (the project's own README / `docs/`, globbed from
   `config.docs`). For each doc, follow `prompts/ingest-docs.md`:
   read the doc, extract its concepts, and write **one grounded page per concept**
   into `wiki/code/<slug>/doc-concepts/<concept>.md` — each linking the symbols the doc
   names to their **catalog** entries and cross-linking sibling doc-concepts + code
   concepts. The doc stays in place (never moved). Skip if the worklist is empty.

5. **Finalize (deterministic gate).** Run:
   ```
   wikify finalize <slug>
   ```
   The citation linter is a hard gate over `concepts/`: every catalog citation must
   resolve to a real SCIP symbol, every Entry-points/Mechanism item must be cited,
   and no symbol outside the packet subgraph may appear. `doc-concepts/` get a
   lighter gate (citations must resolve — rule 1 — no subgraph/uncited gates). On
   success it also runs **Stage 6b coverage**: it emits a `catalog/<module>.md` page
   for every module (deterministic, no model) so the *whole repo* is represented,
   prints a coverage report, assembles `wiki/code/<slug>/index.md` (concepts + areas +
   **doc-derived concepts**), and updates reconcile state.

6. **Repair loop.** If `finalize` exits non-zero, it lists each failing
   `page:line [rule N]`. Fix those pages (add the missing citation or move the
   claim into an `[!inferred]` block) and run `wikify finalize <slug>` again.
   Repeat until it exits 0.

## Notes
- **Where pages go**: `wiki/<wiki_subdir>/<slug>/` — `wiki_subdir` defaults to `code`
  (so `wiki/code/<slug>/`, leaving `wiki/` for a curated index + prose). Set
  `wiki_subdir: ""` in `config/<slug>.md` for the classic flat `wiki/<slug>/` layout.
- **Adding a concept later**: add it to `config/<slug>.md` and re-run from step 1;
  `prepare` builds only the new packet (same commit, nothing else marked stale).
- **Version bump**: `wikify prepare <slug> --ref <newcommit>` — only changed
  symbols' pages rebuild.
- `wikify plan <slug>` previews the delta without emitting anything.
