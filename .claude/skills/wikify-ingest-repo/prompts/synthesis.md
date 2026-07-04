# Synthesis instruction — one DEEPLY-PROCESSED mechanism page from one packet

You are writing a page of an internals wiki that a senior engineer will read to
*understand* a subsystem — not a citation-annotated restatement of signatures. The
bar: a reader should come away with a **mental model** they could not get by
skimming the code, including the *why*, the non-obvious, and the gotchas.

A grounded page that merely traces the code ("X calls Y, then Z", every clause
cited) is a FAILURE even if it passes the linter. Comprehension first; citations
support it.

**Lens.** If the packet has a `## Synthesis focus (lens)` block, that is the reader's
angle — foreground it: organize the page around it, lead with the symbols/mechanisms
that matter *for that lens*, and call out the knobs/tradeoffs it cares about. (E.g. a
"TPU performance" lens → surface kernels, sharding, autotune knobs, precision, memory,
and *why they matter for perf* — not a neutral tour.) With no lens, synthesize neutrally.

**Concept tags.** If the packet has a `## Concept vocabulary` block, decide whether this
page's mechanism *is an instance of* one or more of those shared concepts (e.g. a splash
kernel page → `splash-attention`, `pallas-kernel`). If so, add a `concepts: [<keys>]` list
to the frontmatter using ONLY the keys that genuinely apply — this is what lets Stage 7
`connect` link your page to the same concept in other repos as an authoritative match
(vs. a name-guess). Omit the field entirely if none apply; never invent a key not listed.

## Method (this is different from a shallow pass — follow it)
1. The packet is your **grounding index + citation target list**, not your only
   source. Its Subgraph lists the symbols you may cite (with `cite:` links) and
   their def `file:line`.
2. **READ THE ACTUAL SOURCE.** Open the real source files at the `file:line`
   locations for the symbols you document. The packet's snippets are truncated;
   do not write "source truncated / I infer…" when you can just read the file.
   Read enough to explain *how it actually works*, not how it probably works.
3. Build the mental model: what is this subsystem *for*, what is the key idea, why
   is it built this way, what would surprise a competent reader.
4. Write the page (structure below). Lead with understanding; attach citations to
   the load-bearing claims.
5. **Deepen pass:** re-read your draft. Delete or rewrite every sentence that only
   restates a signature or name. Every paragraph should teach something.

## Hard rules (grounding floor — necessary, not sufficient)
- Cite only symbols in the packet Subgraph (paste their `cite:` link). Never name a
  symbol not there; if you need one, raise it in Open questions.
- In "## Entry points" and "## Mechanism", every item must carry ≥1 citation — so
  write **fewer, richer items**, each a real paragraph anchored by its key
  symbol(s). Do NOT put a citation on every clause, and do NOT append `[extracted →
  …]` tags — a plain linked symbol name IS the citation. **Rule 2 is
  non-negotiable**: every numbered Mechanism step and every Entry-points bullet
  MUST contain at least one catalog link to an IN-SUBGRAPH symbol. If a step's
  central symbol is NOT in the Subgraph (e.g. the loop method itself), cite a
  related in-subgraph symbol the step touches, or move that claim into a
  `> [!inferred]` block — never leave a Mechanism step with zero citations.
- Claims you cannot ground in source/a cited symbol/an Evidence item go in a
  `> [!inferred]` block. But first try to ground them by reading the source.
- Quote the author's docstring (the `doc (author intent, L2)` lines) where it
  captures intent. Dynamics/rationale come from source + tests + docstrings only;
  never claim runtime behavior you cannot see statically.

## Page structure
---
title: <concept title>
type: concept
provenance: mixed
concept: <concept-slug>
concepts: [<shared-key>, ...]   # OPTIONAL — see "Concept tags" below; omit if none apply
updated: <date>
status: fresh
---
# <concept title>

## Overview
2–5 sentences of plain prose: what this subsystem is, the single key design idea,
and how the pieces relate. This is the mental model. Light citations only.

## Diagram
At least ONE Mermaid diagram that captures the mechanism visually — pick the kind
that fits: a `flowchart` for a data/control path, a `sequenceDiagram` for an
ordered interaction, a `classDiagram` for a type/containment structure. Label
nodes with the real symbol names you cite (so the diagram is grounded, not
decorative). Keep it to the load-bearing ~5–12 nodes; the diagram should make the
mechanism *clickable in the head*, not reproduce every edge. Add a second diagram
only if a distinct view genuinely adds understanding. Fence as ```mermaid.

## Design rationale (why it's built this way)
The non-obvious decisions and their reasons — grounded in docstrings/comments/tests
where possible, marked `> [!inferred]` where it's your reading. This section is
what separates a wiki from a code dump. Do not skip it.

## Entry points
- [`Sym`](../catalog/<module>.md#Sym) — what it is and *when control reaches it*.

## Mechanism (step-by-step)
Readable prose in execution order. Each numbered step is a substantive paragraph
that explains what happens AND why it matters, with the load-bearing symbol(s)
linked. Not a list of "calls X" lines.

## Key data structures
The state that matters and what it represents (not every field).

## Dynamics (design intent)
Concurrency/scheduling/ordering/parallelism behavior, grounded in tests + source.

## Edge cases
The conditions a reader would trip on.

## Open questions
Honest gaps where even the source didn't settle it.

## See also
Sibling concept pages.

## Citations resolve into the catalog (no stubs)
You write ONE file: the concept page. Every symbol already lives in its module
catalog (`wiki/code/<slug>/catalog/<module>.md`), whose frontmatter holds an
anchor→moniker map. Paste the packet's `cite:` link for a symbol verbatim; the
linter resolves the anchor there and checks it is in the SCIP index and this
packet's subgraph.
