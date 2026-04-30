# TPU Model Performance Auto-optimization — Schema & Operating Rules

*(Autoresearch methodology; see [README](README.md) for the project intro.)*

You maintain a knowledge base in service of an **automated optimization loop** for TPU model performance. The loop is: ingest knowledge (papers, docs, codebases, profiles) → formulate ranked hypotheses → run experiments → record observations → update priors → formulate next hypotheses. Your job is to write and maintain every file. The human curates sources, sets optimization targets, approves experiments, and arbitrates contradictions.

**Scope:** step time, MFU, tokens/sec, memory, and everything that affects them on TPU — compiler flags, parallelism, rematerialization, attention kernels, layout, fusion, scheduling, precision. Out of scope: model quality/convergence. An optimization that changes model semantics is **invalid** — note the invalidation, do not report the speedup.

**Independence:** this wiki is self-contained. Do **not** read from or link into any sibling wiki. All state lives under the paths below.

---

## Directory layout

```
tpu_performance_autoresearch_wiki/     ← project root (agent CWD)
  SCHEMA.md                            ← this file — single source of truth
  CLAUDE.md                            ← @SCHEMA.md pointer
  notes.md                             ← human scratchpad (do not modify)
  wiki/
    index.md                           ← catalog — update on every write
    log.md                             ← append-only event log — newest on top
    sources/                           ← one page per ingested paper/article/doc/talk
    codebases/                         ← one page per ingested repo (plus subpages)
    concepts/                          ← techniques, abstractions, flags, kernels
    models/                            ← each model under optimization (inputs + SOTA target)
    hypotheses/                        ← ranked candidate optimizations, not yet run
    experiments/                       ← runs: config, profile link, metrics, verdict
    observations/                      ← reusable findings pulled from profiles/runs
    analyses/                          ← syntheses, comparisons, reports you're asked to write
  raw/
    sources/                           ← immutable source files (PDFs, HTML, etc.)
    code/                              ← checked-out or symlinked repos
    profiles/                          ← xprof traces, HLO dumps (immutable)
    assets/                            ← images, figures, plots
```

**Never modify anything under `raw/`.** It is the source of truth.

All wiki paths below are relative to `wiki/`.

---

## The autoresearch loop

The loop is the reason this wiki exists. Everything else supports it.

```
┌─────────────────────────────────────────────────────────┐
│  SOURCES + CODEBASES + PROFILES                         │
│            ↓ (inform)                                   │
│  CONCEPTS + MODELS                                      │
│            ↓ (suggest)                                  │
│  HYPOTHESES (ranked: expected gain × confidence / cost) │
│            ↓ (selected)                                 │
│  EXPERIMENTS (config + run + profile)                   │
│            ↓ (produce)                                  │
│  OBSERVATIONS (what the profile shows)                  │
│            ↓ (update)                                   │
│  CONCEPTS + HYPOTHESES (priors revised, new candidates) │
└─────────────────────────────────────────────────────────┘
```

Every experiment either **supports**, **refutes**, or is **inconclusive** about the hypothesis it tests. A "supports" verdict requires: (a) measurable improvement on the target metric beyond noise, (b) no regression on other tracked metrics, (c) no semantic change to the model.

A hypothesis stays on the ranked list until it is either tested or explicitly retired (with a reason).

---

## Page format

Every wiki page starts with YAML frontmatter. Minimum fields (extend per page type):

```yaml
---
title: "<page title>"
type: source | codebase | concept | model | hypothesis | experiment | observation | analysis
tags: [...]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Then:
- **Lead paragraph** (1–3 sentences) defining the page for any reader.
- H2 sections per the page-type template below.
- `## See also` — markdown links to related pages.
- `## Sources` — raw files that informed this page (raw paths).

**Links:** standard markdown, relative paths, `.md` extensions, spaces as `%20`. Example from `wiki/concepts/flash-attention.md` to `wiki/sources/2022-flash-attention.md`: `[FlashAttention](../sources/2022-flash-attention.md)`. **Do not use `[[wikilink]]` syntax.**

**Contradictions:** never silently overwrite. Mark the old claim:
```
> [!warning] Contradicted by [<source or experiment>](relative/path.md) on YYYY-MM-DD
<old claim>
```
then add the new claim below it. The human adjudicates.

**Stubs:** if a concept/entity is referenced but not yet worth a full page, create a minimal stub with `tags: [stub]` and a `*Stub — expand when more sources are available.*` body.

---

## Page types and templates

### source  (`wiki/sources/<year>-<slug>.md`)
Ingested paper, article, blog post, talk, or documentation page.
- H2: Overview, Key claims, Key data points (tables where possible), Techniques referenced, Gaps & caveats, Connections.
- `Connections` lists wiki pages this source updates or should update.
- `tags` includes one of: `#paper`, `#article`, `#blog`, `#talk`, `#docs`.

### codebase  (`wiki/codebases/<slug>.md`, optional subpages `wiki/codebases/<slug>/<subpage>.md`)
Ingested repository. Large repos get one parent page + focused subpages.
- H2: Overview, Architecture (layers/boundaries), Key abstractions, Entry points, Dependencies, Notable files, Performance-relevant surfaces, Connections.
- **Performance-relevant surfaces** is mandatory — list the knobs, flags, kernels, layouts, or code paths that optimization hypotheses will touch, with file/line references.
- When a repo evolves materially (major refactor, new abstraction), file a new dated codebase page (`<slug>-YYYY-MM-DD.md`) rather than overwriting — preserve history.
- Record the exact commit SHA ingested in frontmatter: `commit: <sha>`.

### concept  (`wiki/concepts/<slug>.md`)
An optimization technique, hardware feature, compiler pass, flag, kernel, or abstraction.
- H2: Definition, Why it matters for TPU perf, Mechanism, When it applies / when it doesn't, Known results, Connections.
- If the concept has measured impact, include a results table with model × baseline × delta × source/experiment.

### model  (`wiki/models/<slug>.md`)
A model under optimization. This is a **live page** — it tracks the current best configuration and open questions.
- H2: Target metrics, Hardware, How to run (verbatim command), Baseline, Current best, Known bottlenecks, Open hypotheses, Retired hypotheses, History.
- `Baseline` and `Current best` are tables: step time, MFU, tokens/sec, peak HBM, config hash, date, link to experiment page.
- Only this page and `hypotheses/*` track "open questions" — keep them consistent.

### hypothesis  (`wiki/hypotheses/<slug>.md`)
A candidate optimization, pre-experiment. Frontmatter adds:
```yaml
model: <model-slug>
status: open | in_progress | supported | refuted | inconclusive | retired
expected_gain: "<e.g. 5-15% step time>"
confidence: low | medium | high
effort: S | M | L
origin: <source-slug or observation-slug or human>
```
- H2: Statement (one sentence, falsifiable), Rationale (why you believe this; cite sources/observations), Proposed experiment (what to change, what to measure, expected delta), Risks (semantic changes, regressions), Dependencies.
- The **ranked hypothesis list** for a model lives in that model's page, derived from these — keep them in sync.

### experiment  (`wiki/experiments/<YYYY-MM-DD>-<slug>.md`)
A single run (or minimal set of comparable runs) testing a hypothesis. Frontmatter adds:
```yaml
hypothesis: <hypothesis-slug>
model: <model-slug>
commit: <model-repo-sha>
verdict: supported | refuted | inconclusive | invalid
```
- H2: Hypothesis under test, Setup (hardware, env, conda env, exact command — copy from model page and diff the changed flags), Baseline comparison, Results (table: metric × baseline × this run × delta × noise band), **Profile** (see below), Observations (links to observation pages produced), Verdict + reasoning, **Next hypotheses** (see below).
- **Next hypotheses section is mandatory.** Every experiment ends with `## Next hypotheses` enumerating the follow-up candidates this run motivates. This is what keeps the queue refilling — the experiment that just landed is the cheapest moment to capture the next move while the context is fresh. Format:
  - One bullet per candidate. Each bullet is a markdown link to a `../hypotheses/<slug>.md` page followed by ` — ` and a one-line description focused on *what differs from the run that just landed*.
  - Every linked hypothesis page must exist — file stubs in the same change as the experiment, with `origin: <experiment-slug>` in their frontmatter and `status: open`. A link to a non-existent file fails LINT.
  - If there are genuinely no follow-ups, write the single literal line `None — <reason>` (e.g. `None — frontier closed; ridge point reached`, `None — hypothesis refuted, no derivative`, `None — blocked on hardware scale-up`). An absent or empty section fails LINT.
  - Three or more bullets is normal and good. The discipline favors *breadth at capture time*; ranking happens later in the model/program page.
- **Profile section is mandatory whenever the run actually executed.** It must carry:
  - (a) a **direct clickable browser URL into the xprof UI** for the run (e.g., `http://localhost:8791/?run=<run-name>` when a local xprof server is configured; use the project's documented base URL otherwise). This lets the reviewer jump straight to the interactive trace viewer.
  - (b) the **run name** as it appears in the xprof server (typically the GCS/logdir subdirectory name).
  - (c) the exact on-disk directory path under `raw/profiles/<YYYY-MM-DD>-<exp-slug>/`, **as a relative markdown link** from the experiment page so editors can click through to the trace folder.
  - (d) which steps were captured (the `profile_steps` value or equivalent).
  - (e) a one-line description of what's inside (xprof trace, HLO dump, memory profile, etc.).
  - (f) the same `raw/profiles/...` path repeated in `## Sources`.
  
  Profiles are **gitignored** (multi-GB binary artifacts — see `.gitignore`), so this page is the sole persistent link between the trace on disk and the experiment that produced it. If the run was not executed (e.g., an infrastructure-only dry check, or a crash before step 0), omit the section and note the reason in `## Verdict`.
- `invalid` is the verdict when the experiment changed model semantics or was otherwise unsound; in that case the measured speedup is **not reported** as a win.
- Experiments are immutable once filed — if you rerun, file a new experiment and link them.

### observation  (`wiki/observations/<slug>.md`)
A reusable finding extracted from a profile or run — something that may inform multiple future hypotheses.
- H2: What was observed, How to see it (profile path + xprof query / HLO section), Implications, Seen in (list of experiments/profiles).
- Examples: "all-gather in FSDP overlaps < 40% with compute at batch=4", "flash attention block size 2048 has 2x the spill of 1024 on v6e".

### analysis  (`wiki/analyses/<YYYY-MM-DD>-<slug>.md`)
A synthesis the human asked for: a comparison, a report, a deep-dive.
- Free-form H2 sections appropriate to the question, but always include `## Sources` and `## See also`.

---

## Operations

### INGEST-SOURCE

Trigger: human adds a file to `raw/sources/` or provides a URL and says "ingest".

1. **Read** the source fully. If URL, fetch and save to `raw/sources/<year>-<slug>.<ext>`. If it has figures you need, save to `raw/assets/`.
2. **Discuss** with the human: "Here are the key claims relevant to TPU perf — anything to emphasize or de-emphasize?" Wait.
3. **Write source page** at `wiki/sources/<year>-<slug>.md`.
4. **Update connections**: for each concept/model/codebase touched, integrate the new claim, add source to `## Sources`, bump `updated:`.
5. **Generate hypothesis candidates** if the source suggests optimizations applicable to any current `model`. File them as `wiki/hypotheses/*.md` with `origin: <source-slug>` and add to the model's ranked list.
6. **Update `index.md` and `log.md`**.

### INGEST-CODEBASE

Trigger: human points at a repo path under `raw/code/` (usually a symlink) and says "ingest".

1. **Orient**: read README, top-level layout, entry points. Record commit SHA.
2. **Discuss** with the human: "This looks like it has X, Y, Z as perf-relevant surfaces — is that what matters, or should I focus elsewhere?" Wait.
3. **Write parent codebase page** at `wiki/codebases/<slug>.md`. Fill all H2 sections; **Performance-relevant surfaces** is the critical one — name files and line ranges.
4. **Create subpages** for any perf-relevant subsystem that warrants depth (e.g., `wiki/codebases/<slug>/attention.md`, `wiki/codebases/<slug>/fsdp.md`).
5. **Create concept stubs** for any technique named that lacks a page.
6. **Generate hypothesis candidates** from the code (e.g., flags not yet tried, kernels not yet used).
7. **Update `index.md` and `log.md`**.

### FORMULATE-HYPOTHESIS

Trigger: human asks you to propose optimizations, or an observation suggests a new one.

1. Read the relevant model page, existing hypotheses (open and retired), and recent observations.
2. Draft hypothesis page(s). Each one must be **falsifiable** (state the expected metric delta and how you'd measure it).
3. Rank against existing open hypotheses by `expected_gain × confidence / effort`. Place in the model page's ranked list.
4. Update `log.md`.

### RUN-EXPERIMENT

Trigger: human approves a hypothesis for testing (or asks "run the top hypothesis").

1. Read the hypothesis and the model page. Resolve any ambiguity **before running**.
2. Prepare the run: copy the model's baseline command, diff only the flags/code paths the hypothesis changes. Record the diff in the experiment page.
3. Execute. Capture profile to `raw/profiles/<YYYY-MM-DD>-<exp-slug>/`.
4. **Validate the model still computes the same thing** — check loss trajectory vs baseline over the profiled steps. If it diverges, verdict is `invalid`.
5. Write `wiki/experiments/<YYYY-MM-DD>-<slug>.md` with full results table.
6. Extract `observation` pages for any finding that may recur.
7. Update the hypothesis (`status:`, link to experiment), update the model page (`Current best` if this wins, ranked list if new hypotheses were generated).
8. **File next-hypothesis stubs.** Every bullet in the experiment's `## Next hypotheses` section must resolve to an existing `wiki/hypotheses/<slug>.md` page. File the stubs concurrently with the experiment, with `status: open`, `origin: <experiment-slug>`, and at minimum a one-sentence falsifiable Statement and a Rationale citing this experiment. They can be lightweight — ranking and full Proposed-experiment detail can come later under FORMULATE-HYPOTHESIS — but they must exist so the queue is real, not aspirational.
9. Update `index.md` and `log.md`.

### RECORD-OBSERVATION

Trigger: you notice something in a profile or run that doesn't belong to a single experiment's narrative.

1. Write `wiki/observations/<slug>.md`.
2. Link from every experiment/concept page where it applies.
3. If it suggests new hypotheses, file them and update rankings.

### ANALYZE

Trigger: human asks a question.

1. Read `index.md` first. Find relevant pages; read them.
2. Synthesize with citations (markdown links to wiki pages and raw sources).
3. Offer to file as `wiki/analyses/<YYYY-MM-DD>-<slug>.md`.
4. If filed, update `index.md` and `log.md`.

### LINT

Trigger: human says "lint".

Check and report:
- Unresolved `[!warning]` contradictions.
- Hypotheses `open` with no activity for > 14 days on an actively-optimized model.
- Experiments without profile artifacts in `raw/profiles/`.
- Experiments missing a `## Next hypotheses` section, with an empty body, or with a hypothesis link that targets a non-existent file. (`None — <reason>` is acceptable; bare absence is not.)
- Hypothesis pages whose `origin:` references an experiment slug that has no corresponding experiment page.
- Model pages where `Current best` does not match the latest `supported` experiment.
- Orphan pages (no inbound links).
- Broken markdown links (target `.md` does not exist).
- Concept/entity names mentioned in prose but not linked to an existing page.
- Stale codebase pages whose `commit:` is far behind the current checkout.

Fix mechanical issues automatically; flag judgment calls for the human.

---

## index.md conventions

```markdown
# TPU Model Performance Auto-optimization — Index
*Last updated: YYYY-MM-DD — N pages*

## Models (N)
- [<model>](models/<slug>.md) — one-line status: "baseline 420ms/step, current best 310ms/step, 3 open hypotheses"

## Hypotheses — ranked, open only (N)
| # | Hypothesis | Model | Expected | Confidence | Effort |
|---|---|---|---|---|---|
| 1 | [<slug>](hypotheses/<slug>.md) | ... | 10-20% | high | M |

## Experiments (N)
- [YYYY-MM-DD <slug>](experiments/YYYY-MM-DD-<slug>.md) — verdict — one-line delta

## Sources (N)
- [<title>](sources/<slug>.md) — one-line takeaway

## Codebases (N)
- [<slug>](codebases/<slug>.md) — commit `<short-sha>` — one-line role

## Concepts (N)
- [<slug>](concepts/<slug>.md) — one-line definition

## Observations (N)
- [<slug>](observations/<slug>.md) — one-line finding

## Analyses (N)
- [YYYY-MM-DD <slug>](analyses/YYYY-MM-DD-<slug>.md) — one-line question answered
```

---

## log.md conventions

Append-only, **newest first**. One entry per operation:

```markdown
## [YYYY-MM-DD] <op> | <subject>

**Op**: ingest-source | ingest-codebase | formulate | run-experiment | record-observation | analyze | lint | manual
**Pages created**: ...
**Pages updated**: ...
**Key result**: (for run-experiment: verdict + headline metric delta)
**Notes**: decisions, human guidance, contradictions found
```

Grepping the log: `grep "^## \[" wiki/log.md | head -20` → last 20 events.

---

## Naming conventions

| Item | Convention | Example |
|---|---|---|
| Source pages | `<year>-<slug>.md` | `2022-flash-attention.md` |
| Codebase pages | `<slug>.md` (+ `<slug>/<subpage>.md`) | `torchtitan.md`, `torchtitan/fsdp.md` |
| Concept pages | `<slug>.md` | `rematerialization.md` |
| Model pages | `<slug>.md` | `llama3-8b-torchtitan-jax.md` |
| Hypothesis pages | `<slug>.md` | `flash-attention-block-2048.md` |
| Experiment pages | `<YYYY-MM-DD>-<slug>.md` | `2026-04-22-remat-offload-query.md` |
| Observation pages | `<slug>.md` | `fsdp-allgather-overlap-gap.md` |
| Analysis pages | `<YYYY-MM-DD>-<slug>.md` | `2026-04-22-v6e-vs-v5p-llama.md` |
| Raw sources | `raw/sources/<year>-<slug>.<ext>` | `raw/sources/2022-flash-attention.pdf` |
| Raw profiles | `raw/profiles/<YYYY-MM-DD>-<exp-slug>/` | directory per experiment |
| Slugs | lowercase, hyphens only | |

---

## Behavioral rules

1. **Never modify `raw/`.**
2. **Update `index.md` and `log.md` after every operation that creates or materially changes pages.**
3. **Never silently overwrite** a claim — use `[!warning]` contradiction blocks.
4. **Every hypothesis is falsifiable** — state the metric, the delta, and how you'd measure. If you can't, it isn't a hypothesis yet.
5. **Every experiment records the full command** and the diff from baseline, not just prose.
6. **Every "supported" verdict requires** measured improvement beyond noise **and** a semantics check (loss or output parity) **and** no tracked-metric regression. Otherwise it is `inconclusive` or `invalid`.
7. **Profiles are mandatory** for experiments — missing profile ⇒ verdict is `inconclusive` at best. Every experiment page with a verdict other than `invalid` **must** carry the profile directory path under `## Profile` and cite it again in `## Sources`. Because profiles are gitignored (see `.gitignore` — `raw/profiles/*` except `.gitkeep`), the experiment page is the only persistent lineage link from trace-on-disk back to the run that produced it.
8. **No model-quality optimizations.** If a proposed change trades accuracy for speed, reject it or mark `invalid`.
9. **Discuss before writing** on ingest — confirm emphasis with the human.
10. **Prefer tables** for metrics, flags, and comparisons.
11. **ISO dates everywhere** (YYYY-MM-DD).
12. **Read `index.md` first** on any query — do not guess which pages exist.
13. **One entity/concept/model per page.** Split when a page exceeds ~500 lines.
14. **No cross-wiki links.** This wiki does not reference `tpu_wiki` or any sibling.
