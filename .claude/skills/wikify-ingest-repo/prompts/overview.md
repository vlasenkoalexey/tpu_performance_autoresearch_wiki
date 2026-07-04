# Overview synthesis — the highest-level page of a repo's wiki

After the concept pages exist, produce ONE top-level page, `wiki/code/<slug>/overview.md`,
that a newcomer reads FIRST to get the whole system in their head. It is the
"god-node" view: main concepts, how the subsystems compose, and the core diagrams.
It is synthesized from the concept pages (and their cited grounding) — you are
stitching the per-subsystem mental models into a single system mental model.

**Lens.** Read `synthesis_focus` from `config/<slug>.md`. If set, it is the reader's angle:
organize the overview around it and **add a dedicated section leading with the focus-relevant
surfaces** — e.g. a "TPU performance" lens → a `## Performance-relevant surfaces` section naming
the kernels / sharding / autotune knobs / precision / memory paths that matter, each linked to its
concept or catalog page. This is what makes the overview the perf entry point (it replaces a
hand-written perf page). With no lens, keep the overview neutral.

## Method
1. Read every page in `wiki/code/<slug>/concepts/` (their Overview + Design rationale
   sections are the raw material — that's where each subsystem's essence lives).
2. Identify the 5–10 **main concepts** of the whole repo and how they relate.
3. Write the page below. Link concepts to their concept pages; do not re-explain
   mechanism depth — point to the concept page for that.

## Page structure
---
title: <repo> — overview
type: overview
updated: <date>
---
# <repo> — what it is and how it fits together

## In one paragraph
The system in 4–6 sentences: what it does and the central design idea(s).

## Core architecture
At least one **system-level Mermaid diagram** showing the major subsystems and
their relationships (e.g. config → trainer → {model, dataloader, optimizer,
checkpoint, metrics} over a parallelism substrate). Nodes link-labeled with the
concept they map to. Add a second diagram for a cross-cutting flow (e.g. one
training step end-to-end, or the model-registration/dispatch path) when it earns
its place. Fence as ```mermaid.

## Main concepts
A short subsection per concept (5–10 total): one tight paragraph each, each ending
with a link to the concept page(s) that own it. These are the load-bearing ideas
a reader must hold (e.g. "model-agnosticism via the TrainSpec registry", "derived
device mesh", "global-token loss normalization", "two-tier coverage").

## How a request flows (optional)
If there's a single spine (e.g. config → construct → train loop → step), trace it
in a few sentences linking the concepts in order.

## Map of the wiki
A short guide: which concept to read for which question; pointer to `catalog/` for
the exhaustive per-module index; pointer to `index.md` for the concept table.

## Rules
- This page is **synthesis over the concept pages**, not new grounding. It may
  state a concept in plain prose; depth and citations live in the concept pages it
  links. Keep any claim that needs grounding on its concept page, not here.
- Diagrams must reflect real subsystems/relationships (grounded), not aspiration.
- Keep it tight: a newcomer should read the whole page in a few minutes and know
  where to go next.
