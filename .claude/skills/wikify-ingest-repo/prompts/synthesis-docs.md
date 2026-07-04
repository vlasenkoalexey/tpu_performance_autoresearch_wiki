# Synthesis — docs mode (prose ingestion)

You are ingesting **documentation**, not code. There is no SCIP catalog; the grounding anchor
is a **source document + section**. This is Karpathy's ingest operation — read a doc, integrate
it into the wiki, cite the source, cross-link — wrapped in wikify's guarantees: every citation
must resolve to a real section (the linter fails the build otherwise), and every doc must end up
represented (coverage floor).

`prepare` wrote one **doc packet** per document at `.cache/packets/<slug>/doc__<name>.md`. Each
packet gives you: the source file path, the doc text (truncated — **read the real file** at the
`raw/code/<slug>/…` path for anything long), the exact **`src:` citation tokens** you may use, and
the sibling docs it links to.

**Lens.** Read `synthesis_focus` from `config/<slug>.md` (same as code mode). If set, it is the
reader's angle: weight which topics get pages and what each summary leads with toward the focus.
The lens moves emphasis, never grounding — every claim still cites a real `src:` section. With no
lens, stay neutral.

## For each doc packet

Write into `wiki/<wiki_subdir>/<slug>/` (default `wiki/code/<slug>/`; here it's docs-mode, so
usually `wiki/<slug>/` or the configured subdir):

1. **A source summary** — `sources/<page_slug>.md` (use the packet's doc name): a tight summary of
   *that one doc* — what it covers, its key claims, and links to the topics it feeds. This is the
   doc's landing page; it is what makes the doc "represented" for coverage.

2. **Topic pages (the point)** — `topics/<concept>.md`: synthesized, **cross-source** pages for the
   concepts the doc discusses (an entity, technique, API area, decision). **Do not write one topic
   per doc.** A topic accumulates across docs: if `topics/<concept>.md` already exists, **update
   it** — integrate the new claims, reconcile or flag contradictions, add the new source. A single
   doc typically touches several existing topic pages. *That integration is the whole value* — a
   pile of isolated per-doc summaries is not a knowledge base.

## Grounding — cite with `src:` tokens (hard-gated)

Every non-obvious claim cites its source section. **Paste a `src:` token from the packet verbatim**:

```
Flags are set in the config block ([configuration](src:docs/guide.md#configuration)).
```

- The linter (`wikify finalize`) rejects any `src:` citation whose doc or `#section` isn't real —
  you may **only** cite tokens the packet lists. Whole-file formats (`.txt`, anchorless) use the
  bare `src:<doc>` token.
- Prose you can't tie to a source goes in a `> [!inferred]` block (your synthesis, flagged as such).

## Cross-linking (required — this is the compounding)

- **To sibling docs' topics/sources** — link the topics a related doc feeds (the packet lists
  siblings).
- **Between topics** — link related concepts so the graph connects.

## After all docs

Write `overview.md` — the highest-level page: the main topics, how the docs relate, and a map of
which topic answers which question. Then run `wikify finalize <slug>`: it gates every `src:`
citation, runs the coverage floor (flags any doc with no `sources/` page and no inbound citation —
go back and represent it), and assembles `index.md`.
