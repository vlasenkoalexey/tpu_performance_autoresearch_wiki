---
name: wikify-connect-repo
description: >
  Connect ingested code silos on the concept axis — cross-link the same concept
  (a Pallas kernel, an optimization technique) across repos, inline like a normal
  wiki: the host wiki's concept page links down to each repo's implementation, and
  each implementation links back up. Selective by design — you choose WHICH concepts
  to connect (connecting everything drowns the pages). Trigger at the tail of an
  ingest (from the 2nd repo on) or when the user asks to connect / cross-link the
  ingested repos. No new page types; idempotent and re-runnable.
---

# wikify-connect-repo

A single ingest produces a **silo** (`wiki/<subdir>/<slug>/` with `overview.md` + `concepts/` +
`catalog/`). This skill wires silos together on the **concept axis**, **inline, as a normal wiki**
— through the concept pages the host already curates (`wiki/concepts/*.md`). The concept page links
**down** to each repo's implementation page; each implementation links **up** to the concept. No
side-table, no new page type, no `_connect/` artifact — just links on existing pages.

**Selective by design.** Connecting every concept to every repo drowns the pages. So the human
picks *which* concepts to connect at this phase — that is the whole point of the interactive step.

**The Python/LLM split is hard here too.** Candidate proposal + the link insertion are pure Python
(`wikify connect`). The only judgment is *which* concepts to connect (and, optionally, pruning a
stray name-match) — done at the ask below.

## Preconditions
- The wiki has **≥2 ingested silos** (the first repo has nothing to connect to) and a concept
  vocabulary directory (`wiki/concepts/*.md`). If either is missing, STOP — nothing to do.
- Run from the wiki root (where `wiki/` and `config/` live). Non-interactive/batch: do only
  `--refresh` (regenerate already-connected concepts); never auto-connect new ones.

## Procedure

1. **Propose (deterministic; no model, writes nothing).** Run:
   ```
   wikify connect
   ```
   It prints each vocabulary concept that has candidate implementations across the silos
   (most-implemented first), the repos involved, and which concepts are **already connected** (`✓`).
   A candidate is `tag` (an explicit `concepts:` frontmatter match — authoritative) or a name/token
   match. Nothing is written yet.

2. **Ask what to connect (interactive — the selective step).** Show the human the proposed concepts
   and ask **which to connect**. Recommend the highest-value ones for the wiki's lens (e.g. the
   Pallas kernels + optimization techniques), not all of them — the goal is a useful spine, not a
   fully-connected graph. If a chosen concept's candidate list has an obvious name-collision (open
   the silo page to check when unsure), note the `repo/rel-path` to drop via `--exclude`.

3. **Apply (deterministic).** Wire the chosen concepts:
   ```
   wikify connect --apply <key1,key2,...>   [--exclude <repo/rel-path,...>]
   ```
   This writes, inside regenerable `connect:auto` blocks (hand prose untouched):
   - on each `wiki/concepts/<key>.md` — a `## In this wiki's repos` list linking **down** to every
     implementation page, grouped by repo;
   - on each linked silo concept page — a one-line **up-link** back to the concept(s) it's part of.

   **When this run follows a new ingest** (the usual trigger), also refresh the concepts that
   were connected before, so they pick up the new repo's implementations:
   ```
   wikify connect --refresh
   ```
   This skill owns `--refresh` — the ingest skill only hands off here and never runs
   `wikify connect` itself.

4. **Deepen a hub (optional; LLM, only where asked).** For a concept worth a real cross-repo
   narrative, edit its `wiki/concepts/<key>.md` prose *outside* the `connect:auto` block: a tight
   lens-framed definition, a short *how the implementations differ* synthesis grounded in the linked
   silo pages, and inbound backlinks (experiments/observations that used it). The auto block stays
   the machine-maintained link list; your prose sits above it. **Never rewrite the linted silo
   pages** — only their one-line up-link block is machine-managed.

5. **Record.** Append one line to the host `log.md` per its convention
   (e.g. `## [YYYY-MM-DD] connect | <n> concepts wired across <m> repos`).

## Notes
- **Idempotent / re-runnable.** Connection state *is* the wiki pages (a concept page with a
  `connect:auto` block is connected — no side-file). After a new ingest, `wikify connect --refresh`
  regenerates every already-connected concept's links (picking up the new repo's matches); re-running
  `--apply` on the same keys produces no churn.
- **Vocabulary is the host's.** The concept keys are `wiki/concepts/` filenames (or `--vocab <dir>`),
  never wikify's — a non-code or non-TPU wiki brings its own. To add a concept to the spine, add a
  `wiki/concepts/<key>.md` and connect it.
- **Dependency links (repos that import each other) are a separate, future op** (design.md Stage 7
  "(a) dependency links"): re-resolving an external citation against another silo's SCIP index. Not
  yet automated here; this skill covers the concept-correspondence half.
