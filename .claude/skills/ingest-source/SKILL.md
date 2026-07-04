---
name: ingest-source
description: Ingest a paper, article, blog post, talk, or documentation page into the wiki. Encodes SCHEMA's INGEST-SOURCE operation as a callable skill. Reads the raw source (PDF/HTML under raw/sources/ or fetched from URL), confirms emphasis with the human before writing, files wiki/sources/<year>-<slug>.md, updates connections (concepts/codebases/models that touched the source), generates hypothesis candidates if applicable, and updates wiki/index.md + wiki/log.md per the operations contract. Invoke when ingesting any new perf-relevant source — the discussion step prevents misemphasis and the connection updates keep the wiki graph coherent. NOT for codebases (use INGEST-CODEBASE / a future /ingest-codebase skill) or per-experiment notes (those live in wiki/experiments/).
---

# /ingest-source — ingest a paper/article/talk/docs into the wiki

Encodes SCHEMA's INGEST-SOURCE operation. The discipline matters: ingest is the front door for the wiki's hypothesis-generation pipeline, and getting emphasis wrong (or skipping connection updates) propagates downstream into bad hypothesis proposals.

## When to invoke

- User says "ingest this paper / blog post / talk / docs page" and provides a URL or `raw/sources/` path.
- A paper or talk just landed that touches TPU perf-relevant topics (Pallas kernels, sharding partitioners, FP8 training, attention kernels, scheduler/compiler passes, etc.).
- An existing source needs re-ingestion because a meaningful update was published.
- **NOT for codebases** — those go through INGEST-CODEBASE (separate skill, TBD).
- **NOT for per-experiment narrative** — that's `wiki/experiments/` and a different operations contract.

## Cardinal rules

- **Discuss before writing.** The human owns emphasis decisions. Do NOT write the source page until you've surfaced the key claims and confirmed which ones matter.
- **Update connections.** Every concept, model, or codebase that the source touches gets its `## Sources` updated and (where appropriate) prose extended. Skipping this step is the canonical failure — orphan source pages with no incoming links.
- **Generate hypothesis candidates.** If the source suggests optimizations applicable to an active model, file them as `wiki/hypotheses/<slug>.md` with `origin: <source-slug>`. Add to the model page's ranked list.
- **Update `index.md` and `log.md`.** Mandatory per SCHEMA's operations contract.
- **Never modify `raw/`.** The source file is immutable. If the URL was given, save to `raw/sources/<year>-<slug>.<ext>` first.

## Step 1 — Acquire the source

The user supplies one of:
- A `raw/sources/<year>-<slug>.<ext>` path (already ingested locally)
- A URL (fetch + save)
- A direct file paste

If URL: fetch and save to `raw/sources/<year>-<slug>.<ext>`. Choose `<slug>` to be short, lowercase, hyphen-separated, descriptive. Choose `<year>` from the source's publication date.

If the source has figures the wiki page will reference, save figures to `raw/assets/<year>-<slug>-<figure>.<ext>`.

## Step 2 — Read fully + draft key claims

Read the source end-to-end (PDF, HTML, transcript, slides). Do NOT skim. The whole point of ingestion is to extract durable knowledge; skimming produces shallow source pages that propagate misunderstanding downstream.

Draft (in your head or scratch space, NOT yet in a file):
- 1-paragraph summary
- 3–7 key claims with the exact mechanism + estimated impact when stated
- Key data points (extract tables when present)
- Techniques referenced (link to existing concept pages where they exist; flag missing concept pages)
- Gaps + caveats (what the source DOESN'T cover; what limits its conclusions)
- Connections to existing wiki pages (concepts / models / codebases / observations / other sources)

## Step 3 — Discuss with the human (MANDATORY)

Surface the draft to the user. Concretely:

```
Read [<year>-<slug>]. Key claims I extracted:

  1. <claim 1> — impact: <if stated>
  2. <claim 2> — impact: <if stated>
  3. ...

Connections I see:
  - Concept: <existing page or "STUB needed"> — extends with <one-liner>
  - Model: <active model> — applicable hypothesis: <one-liner>
  - Codebase: <existing page> — references <subsystem>
  - Sources: <other sources this should cross-link to>

Hypothesis candidates this could generate (for which models):
  - <model>: <hypothesis statement> (estimated <gain>, effort <S/M/L>)
  - ...

Anything to emphasize or de-emphasize before I file the wiki page?
```

WAIT for the human's response. The human typically:
- Reorders or adds emphasis to specific claims
- Says "skip this; not relevant to our optimization focus"
- Notes contradictions with existing wiki content (handle per the `[!warning]` rule)
- Names additional models/concepts to connect

Don't proceed to Step 4 until you have explicit confirmation or instructions.

## Step 4 — Write the source page

Path: `wiki/sources/<year>-<slug>.md`. Format per SCHEMA's source page template:

```markdown
---
title: "<full title>"
type: source
tags: [#<type>, ...]  # one of #paper, #article, #blog, #talk, #docs
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

<lead paragraph — 1-3 sentences defining the page for any reader>

## Overview

<2-4 paragraphs summarizing the source>

## Key claims

<numbered list of the agreed-upon-with-human claims, each with mechanism + impact>

## Key data points

<tables / numbers where the source provides them>

## Techniques referenced

<list with links to existing concept pages, or stubs for missing ones>

## Gaps & caveats

<what the source doesn't cover; limits of its conclusions>

## Connections

<list of wiki pages this source updates or should update>

## Sources

- raw/sources/<year>-<slug>.<ext>
- (URL if applicable)
```

Tags must include one of: `#paper`, `#article`, `#blog`, `#talk`, `#docs`.

## Step 5 — Update connections

For each connection identified in Step 3:

- **Concept page touched**: add the new claim to the page's prose, append the source to its `## Sources` list, bump `updated:` field. If the concept page doesn't exist, create a STUB per SCHEMA (`tags: [stub]` + `*Stub — expand when more sources are available.*` body).
- **Model page touched**: if the source suggests an optimization applicable to an active model, surface in the Cross-variant or Variant-specific open hypotheses section.
- **Codebase page touched**: extend the relevant H2 section (typically Performance-relevant surfaces) with the new mechanism + source citation.
- **Other source pages cross-linked**: add reciprocal links in the `## See also` sections.

## Step 6 — Generate hypothesis candidates

For each (model, hypothesis) pair from Step 3 the human approved:

- File `wiki/hypotheses/<slug>.md` per SCHEMA's hypothesis page template, with frontmatter `origin: <source-slug>` linking back to this source.
- Add to the model page's ranked list (Cross-variant open hypotheses or Variant-specific open hypotheses depending on scope).

If no hypotheses came out (the source was useful for concept-page enrichment but didn't suggest a directly-testable mechanism), skip this step.

## Step 7 — Update `wiki/index.md` and `wiki/log.md`

`wiki/index.md`:
- Bump the Sources count (`## Sources (N+1)`).
- Add a one-line entry: `- [<title>](sources/<year>-<slug>.md) — <one-line takeaway>`.
- If concept stubs were created, also bump Concepts count.
- If hypothesis pages were filed, bump Hypotheses count + add ranked rows.

`wiki/log.md` (global; ingest is cross-cutting per SCHEMA's two-tier log convention):

```markdown
## [YYYY-MM-DD] ingest-source | <title>

**Op**: ingest-source
**Pages created**: wiki/sources/<year>-<slug>.md, <any concept stubs>, <any hypothesis pages>
**Pages updated**: <list of concept/model/codebase pages touched>, wiki/index.md
**Key result**: <one-paragraph summary of what the source contributes — claims, applicability to active models>
**Notes**: <human guidance applied; contradictions resolved; specific de-emphasis decisions>
```

## Step 8 — Return to user

Brief summary:

```
Ingested <year>-<slug>:
  - Created: wiki/sources/<year>-<slug>.md
             <N concept stubs / N hypothesis pages>
  - Updated: <N concept/model/codebase pages>
             wiki/index.md (+1 source)
             wiki/log.md (+1 entry)
  - Key claims: <count>
  - Hypothesis candidates: <count> filed (model: <which>)
```

## Failure modes to handle

- **URL fetch fails** — surface the error; ask user to download manually and provide the `raw/sources/` path.
- **Source is in a format we can't read** (proprietary, password-protected) — refuse with a hint; ask user to extract relevant text.
- **Discussion step (Step 3) reveals the source isn't relevant** — abandon ingestion; do NOT file the source page or update connections. Note in summary: "Discussion concluded source not applicable to current optimization scope; not ingested."
- **Existing source page** for this `<year>-<slug>`** — never silently overwrite. If a re-ingest is intended (source updated), prompt user: "Existing page at <path>; overwrite (re-ingest) or version-suffix?" Default: prompt for which.
- **Contradicts existing wiki claim** — use the `[!warning]` contradiction block per SCHEMA's "Contradictions" rule. Surface to user; they adjudicate.
- **Connection ambiguity** (multiple concept pages plausible) — Ask via `AskUserQuestion`; don't guess.

## Cost expectations

- Per source: ~10–30 minutes wall time depending on source length. Most of the time is in Step 2 (reading) and Step 3 (discussion).
- Source-page write: ~5 minutes after discussion converges.
- Connection updates: ~10 minutes (varies by how many pages need touching).
- Tokens: ~30–100K depending on source length + connection breadth.

## What this skill does NOT do

- **Does not ingest codebases.** Different operation with different concerns (Architecture / Performance-relevant surfaces / SHA-pinning). Use the future `/ingest-codebase` skill or follow SCHEMA's INGEST-CODEBASE operation manually for now.
- **Does not silently overwrite existing source pages.** Prompts on conflict.
- **Does not file hypotheses without human approval.** Step 3's discussion gates hypothesis generation.
- **Does not commit.** Wiki changes are staged; user reviews and commits per existing convention.
- **Does not modify `raw/`.** Source file is immutable once saved.
- **Does not update `model-optimization-index.md` automatically.** If the source suggests a new topic mechanism citation, that's a separate manual edit (or a future regen of the index).

## See also

- `SCHEMA.md` — the INGEST-SOURCE operation contract this skill implements
- `wiki/model-optimization-index-regenerate-prompt.md` — how the index uses ingested sources at next regen
- `.claude/skills/formulate-hypothesis/SKILL.md` — downstream consumer (cites sources in proposals)
- `.claude/skills/wikify-ingest-repo/SKILL.md` — sibling skill for ingested codebases (SCIP-grounded catalogs)
