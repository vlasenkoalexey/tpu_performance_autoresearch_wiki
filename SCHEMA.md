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
    models/                            ← one page per (architecture, lane); variant matrix + SOTA target
    hypotheses/                        ← ranked candidate optimizations, not yet run
    experiments/                       ← <model>_autoresearch_optimization/<lane>/experiments/<date>-<slug>.md
                                          (+ per-model and per-lane program.md overrides)
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

### Procedural complement — `program.md` hierarchy

This file defines the **structural** spec (page types, wiki layout, links, file naming). The **procedural** spec — how to actually execute the loop step-by-step (fork, branch, build, launch, poll, file, decide) — lives in a hierarchy of `program.md` files:

```
wiki/experiments/program.md                                       ← generic loop methodology
wiki/experiments/<model>_autoresearch_optimization/program.md     ← model-family overrides
wiki/experiments/<model>_autoresearch_optimization/<lane>/program.md  ← lane-specific overrides
```

**Resolution**: read root → model → lane. For each H2 section, the most-specific file that defines it wins outright (replace-per-section, not merge). Child files omit sections they don't specialize.

Read all three layers together with this SCHEMA.md before starting an experiment. Skills under `.claude/skills/` are the canonical shared workflow definitions, exposed to Gemini/Antigravity and Codex through the `.agents/skills` compatibility symlink. These skills orchestrate the lifecycle:

- **`/create-experiment`** — bootstrap a new model family: ask for slug, lanes, sizes, hardware, target seq; create `wiki/experiments/<slug>_autoresearch_optimization/` folder structure; scaffold model-level `program.md` and model page stubs.
- **`/start-experiment`** — loads the program.md layers in order, prints the effective resolved program, runs hardware selection + cluster discovery + occupancy check, then starts `/loop` with parallel-tracks (default `--parallelism 1`).
- **`/stop-experiment`** — performs cleanup: cancels background subagents, reaps orphan workloads, files missing pages, runs LINT, appends clean-shutdown marker.

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

### codebase  (`wiki/codebases/<slug>/` — the grounded wiki; optional thin `<slug>.md` perf note)
Ingested repository. The **grounded layer** — `wiki/codebases/<slug>/{overview,concepts,catalog,doc-concepts}` — is generated by the **`wikify-ingest-repo`** skill (SCIP-grounded, cited, lint-gated), *not* hand-authored.
- **`overview.md`** is the front door (read first). With the `synthesis_focus` lens it **leads with a *Performance-relevant surfaces* section** — the knobs, kernels, layouts, and code paths optimization hypotheses will touch, each linked to its concept/catalog page.
- **`catalog/`** is the per-symbol structural index (where-is-X / signature / who-calls-it); **`concepts/`** are the deep mechanism pages. The commit is pinned via the submodule gitlink + `commit:` in the generated pages.
- **Optional thin `wiki/codebases/<slug>.md`** — created **on demand** when the repo enters the optimization loop, only for what the regenerable overview can't hold: cross-ecosystem verdicts ("AQT deprecated → use qwix", "SOTA config is X") + loop status. It cross-links to `<slug>/overview.md`; a pure reference ingest never needs one. (Legacy hand pages from earlier ingests are being slimmed to this form.)

### concept  (`wiki/concepts/<slug>.md`)
An optimization technique, hardware feature, compiler pass, flag, kernel, or abstraction.
- H2: Definition, Why it matters for TPU perf, Mechanism, When it applies / when it doesn't, Known results, Connections.
- If the concept has measured impact, include a results table with model × baseline × delta × source/experiment.
- **These pages are also the connect vocabulary + hubs.** `wikify connect` reads `wiki/concepts/*.md`
  filenames as the shared concept keys; a **connected** page carries an `## In this wiki's repos`
  block (a `connect:auto` block) linking each ingested repo's grounded implementation, and each of
  those silo pages links back up. A concept worth cross-repo depth gains *how-they-differ* hub prose
  above that block — authored by the `wikify-connect-repo` skill. No `_connect/` side-table.

### model  (`wiki/models/<architecture>-<lane>.md`)
A model under optimization. This is a **live page** — it tracks every (size × hardware) variant of one model architecture on one execution lane.

**One page per `(architecture, lane)` pair**, not per individual `(size, hardware)` deployment:
- The **lane axis** is fundamental: different framework, different code path, different debugging context, different launch command. Separating lanes is the whole point of multi-stack optimization (e.g. torchax vs JAX vs MaxText reference).
- The **size axis** (e.g. 3B / 8B) and **hardware axis** (v6e-4 / v6e-8 / …) are combinatorial accidents over the same code; most techniques transfer across the matrix with at most some retuning. The *iteration order* (small → big) is itself part of what the page tracks.

Required frontmatter additions:
```yaml
type: model
architecture: <slug>                          # e.g. gemma4-e4b, llama3-8b
lane: tpu | torchax | jax | maxtext | ...     # execution lane
sizes: [<size1>, ...]                         # e.g. ["8B"]
hardwares: [<hw1>, ...]                        # e.g. ["v6e-4", "v6e-8"]
```

Required H2 sections:
- **Target metrics** — what we're optimizing (step time, MFU, tokens/sec, peak HBM) and how each is measured.
- **How to run** — verbatim launch command template parameterized by size and hardware; one canonical form, not one per variant.
- **Variant matrix** — single source of truth for per-variant status:
  | Size | Hardware | Status | Baseline (step / TPS / MFU) | Current best (step / TPS / MFU) | Open hyps | Frontier exp |
  |------|----------|--------|------------------------------|----------------------------------|-----------|--------------|

  Status values: `live` (actively iterating), `open` (not yet measured), `blocked` (OOM / hang / infra), `parked` (deferred but reachable). Each row is keyed by the `Size/Hardware` join string (e.g. `"8B/v6e-8"`) — that string is what experiments cite in their `variant:` frontmatter.
- **Cross-variant open hypotheses** — apply to most or all variants. **Variant-specific open hypotheses** — bound to a single row. **Retired hypotheses** — note the variant they were retired against (a hypothesis may be retired for one variant, still open for another).
- **Knobs translation matrix** — which optimization techniques transfer cleanly across the matrix and which need re-tuning per variant; updated after every cross-variant validation. Lean on it before proposing a new hypothesis — if a technique is already proven universal, the next experiment only verifies the transfer.
- **Iteration ladder** — the ordered roadmap (typically smallest size on smallest hardware first, then scale, ending at the production target).

Only this page and `hypotheses/*` track "open questions" — keep them consistent. Cross-lane comparison is first-class: an `analysis` page can cite *Current best* rows from multiple lane pages of the same architecture to compute the per-lane gap (e.g. JAX vs torchax).

### hypothesis  (`wiki/hypotheses/<slug>.md`)
A candidate optimization, pre-experiment. Frontmatter adds:
```yaml
model: <architecture-lane>                    # the model lane page, e.g. llama3-8b-jax
variants: ["<size>/<hw>", ...]                # OPTIONAL — restrict to specific rows of the
                                              # model page's Variant matrix; omit ⇒ all variants on the lane
status: open | in_progress | supported | refuted | inconclusive | retired
expected_gain: "<e.g. 5-15% step time>"
confidence: low | medium | high
effort: S | M | L
origin: <source-slug or observation-slug or human>
```
- H2: Statement (one sentence, falsifiable), Rationale (why you believe this; cite sources/observations), Proposed experiment (what to change, what to measure, expected delta), Risks (semantic changes, regressions), Dependencies.
- The **ranked hypothesis list** for a model lives in that model's page (split into *Cross-variant* and *Variant-specific* sections per the model template), derived from these — keep them in sync.
- A hypothesis stays valid across the variant matrix unless explicitly retired for a row. If a small-scale-supported finding needs verification at larger scale, that's a new experiment on a different `variant:` of the same hypothesis — not a new hypothesis.

### experiment  (`wiki/experiments/<model>_autoresearch_optimization/<lane>/experiments/<YYYY-MM-DD>-<slug>.md`)
A single run (or minimal set of comparable runs) testing a hypothesis on **one variant** of one model. Experiments nest under their model family and execution lane:
- `<model>_autoresearch_optimization/` parent collects every run of one architecture.
- `<lane>/experiments/` partitions by execution stack (`jax`, `tpu`, `torchax`, `maxtext`, …).
- The filename keeps the `<YYYY-MM-DD>-<slug>` form. The lane and the outcome are commonly encoded in the slug (e.g. `2026-04-27-jax-exp20-splash-accepted.md`), and the slug may carry a per-lane attempt counter (`exp<NN>`); these are conventions of the slug, not separate path segments.

Frontmatter adds:
```yaml
hypothesis: <hypothesis-slug>
model: <architecture-lane>                   # the model lane page, e.g. llama3-8b-jax
variant: "<size>/<hardware>"                 # the matrix row this run targets, e.g. "8B/v6e-8"
commit: <model-repo-sha>
verdict: supported | refuted | inconclusive | invalid
```
- H2: Hypothesis under test, Setup (hardware, env, conda env, exact command — copy from the model page's "How to run" template and diff the changed flags), Baseline comparison (against the same variant row's baseline), Results (table: metric × baseline × this run × delta × noise band), **Profile** (see below), Observations (links to observation pages produced), Verdict + reasoning, **Next hypotheses** (see below).
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

Trigger: human points at a repo path under `raw/code/` (usually a submodule) and says "ingest".
This is a **thin orchestrator** — it drives the `wikify-ingest-repo` skill and delegates; it does
*not* re-implement structure or hypotheses.

1. **Orient + scope.** Read README / top-level layout; record the commit SHA. Agree with the human
   on the **lens** and which packages to index (`index_shards`) for a big repo (e.g. JAX → just the
   pallas / sharding / kernel packages) — this wiki is deliberately selective.
2. **Ingest (the `wikify-ingest-repo` skill).** Bootstrap `config/<slug>.md` — `slug`,
   `repo: raw/code/<slug>` (the submodule; wikify uses it in place), `acquire: submodule`,
   `wiki_subdir: codebases`, `source_type: code` (or `docs` for a doc-only repo),
   `synthesis_focus: TPU performance — kernels, sharding, attention, autotune knobs, precision, memory`
   (the **lens** — makes the overview lead with a *Performance-relevant surfaces* section),
   `index_shards` / `coverage_collapse` (collapse model-zoo `**/modules/*`, `**/models/*`) to keep
   it lean. Then run the skill (`wikify prepare <slug>` → agent synthesis → `wikify finalize <slug>`).
   It writes the SCIP-grounded `wiki/codebases/<slug>/{overview,concepts,catalog,doc-concepts}` **and
   registers** the repo's `overview.md` into `index.md` + appends `log.md` (skill step 7). Requires
   the `wikify` CLI ([wikify-repo](https://github.com/vlasenkoalexey/wikify-repo): `pip install -e` +
   `setup-vendor.sh`; TS/Go/Rust indexers install on demand). Skip for languages wikify doesn't cover.

3. **Connect (from the 2nd repo on).** The ingest skill then hands off to `wikify-connect-repo`,
   which cross-links this silo to the others on the concept axis **inline, as a normal wiki** (no
   side-table). `wikify connect` proposes which `concepts/` keys have implementations across the
   silos; you pick **which to connect** (selective — not everything); `wikify connect --apply <keys>`
   writes, in regenerable `connect:auto` blocks, a `## In this wiki's repos` list on the concept page
   linking each repo's implementation, plus a one-line up-link on each silo page. Run `wikify connect
   --refresh` after any new ingest so already-connected concepts pick up its implementations. Deepen a
   concept into a real hub by adding *how-they-differ* prose above the auto block.

**That's the ingest.** The two research artifacts are created **when the repo enters the optimization
loop, not at ingest** — never eagerly:
- **Hypotheses** → run `/formulate-hypothesis` when you start optimizing the repo (it owns
  falsifiability + the HLO pre-filter). *Not* an ingest step.
- **Perf verdicts the overview can't hold** — cross-ecosystem judgment ("AQT is deprecated → use
  qwix", "SOTA config is X") → a **thin** `wiki/codebases/<slug>.md`, created on demand, cross-linked
  to the overview. A pure reference ingest never needs one.

### ANSWER-CODEBASE-INTERNALS  (extraction — retrieve, don't re-read source)

For a *where / how / who-calls* question about an ingested repo, **retrieve from the wikify catalog**
instead of re-reading the source tree:
1. Read `wiki/codebases/<slug>/overview.md` first — it maps concepts to pages.
2. `grep`/`rg` the `wiki/codebases/<slug>/` tree to the relevant `concepts/` (mechanism) or
   `catalog/<module>.md` (per-symbol) page; read only that section.
3. Cite the catalog anchor (`catalog/<module>.md#<Symbol>`); follow its source link into
   `raw/code/<slug>/…` only when you need the exact line.

Division of labor: `wiki/codebases/<slug>.md` (hand-curated) answers *which knobs matter for perf*;
the wikify catalog answers *where it is, what its signature is, and who calls it* — grounded and
cited. This works identically in **Claude Code, Codex, and Antigravity**: the skill lives in
`.claude/skills/` (exposed to Codex + AG via the `.agents/skills` symlink) and this SCHEMA — read by
all three via `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` — is the shared protocol.

### FORMULATE-HYPOTHESIS

Trigger: human asks you to propose optimizations, or an observation suggests a new one.

1. Read the relevant model page, existing hypotheses (open and retired), and recent observations.
2. Draft hypothesis page(s). Each one must be **falsifiable** (state the expected metric delta and how you'd measure it).
   - **2b. HLO pre-filter (mandatory for kernel-replacement hypotheses).** Before ranking a hypothesis that proposes replacing XLA-generated code with a Pallas/Mosaic kernel (fusing ops, custom matmul prologue, custom norm+matmul, etc.), AOT-compile the baseline via `jax.jit(fn).lower(*args).compile()` and inspect the post-optimization HLO (or use the xprof-mcp dump tools on an existing dump). If XLA already fuses the target pattern into a single `kind=kOutput` Mosaic kernel, **retire the hypothesis immediately** with `status: retired` and reason `xla-already-fuses`. Record the specific `fused_computation` name as evidence. See [AOT Compilation](wiki/concepts/aot-compilation.md) for the full workflow.
   - Kernel-replacement hypothesis pages must include an `hlo_prefilter:` frontmatter field with value `passed`, `refuted`, or `pending`. A hypothesis with `hlo_prefilter: pending` may be filed as a stub but must not be ranked above hypotheses that have passed the pre-filter.
3. Rank against existing open hypotheses by `expected_gain × confidence / effort`. Place in the model page's ranked list.
4. Update `log.md`.

### RUN-EXPERIMENT

Trigger: human approves a hypothesis for testing (or asks "run the top hypothesis").

1. Read the hypothesis and the model page. Resolve any ambiguity **before running**. Confirm the target **variant** (size + hardware) — if unspecified, default to the next `live` row on the Iteration ladder, but ask if there's any doubt.
   - **1b. (Optional) AOT screening.** Before committing to a full 20-step TPU run, AOT-compile the modified function via `jax.jit(fn).lower(*args).compile()` and call `.cost_analysis()`. This catches compilation errors (OOM, shape mismatches) on CPU and provides a first-order prediction of whether the change will move the metric. Compare `flops`, `bytes accessed`, and `optimal_seconds` against the baseline's cost analysis. If the cost model shows no improvement or a regression, reconsider the hypothesis before burning TPU time. See [AOT Compilation](wiki/concepts/aot-compilation.md).
2. Prepare the run: take the model page's "How to run" template, fill in the variant's size + hardware, then diff only the flags/code paths the hypothesis changes. Record the full launch command in the experiment page.
3. Execute. Capture profile to `raw/profiles/<YYYY-MM-DD>-<exp-slug>/`.
4. **Validate the model still computes the same thing** — check loss trajectory vs baseline over the profiled steps. If it diverges, verdict is `invalid`.
5. Write `wiki/experiments/<model>_autoresearch_optimization/<lane>/experiments/<YYYY-MM-DD>-<slug>.md` (per-model + per-lane folder) with full results table, the `variant:` field pinned, and `commit:` set to the model-repo SHA used.
6. Extract `observation` pages for any finding that may recur.
7. Update the hypothesis (`status:`, link to experiment). Update the model page: the **target variant's matrix row** (`Current best` cell if this wins; `Open hyps` count; `Frontier exp` link). If the finding has cross-variant implications, also update the **Knobs translation matrix** row for the technique.
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
- Model pages where a variant row's `Current best` does not match the latest `supported` experiment for that variant.
- Experiments whose `variant:` field (when present) doesn't appear in the parent model page's Variant matrix; hypotheses whose `variants:` list rows that aren't in the matrix.
- Orphan pages (no inbound links).
- Broken markdown links (target `.md` does not exist).
- Concept/entity names mentioned in prose but not linked to an existing page.
- Stale codebase pages whose `commit:` is far behind the current checkout.
- Kernel-replacement hypothesis pages with `status: open` that lack an `hlo_prefilter:` frontmatter field (must be `passed`, `refuted`, or `pending`).
- **Hook health** — the never-stop loop's Stop hook (`.claude/stop_hook.sh`) must be wired and executable, no command hook may reference a missing script, and no hook may base a decision on a non-durable `/tmp` path or a rogue global-scope Stop hook. Run `.claude/scripts/check-hook-health.py` (ERROR ⇒ lint fails). This is the loop's control plane — if it breaks, the discipline fails silently.

Fix mechanical issues automatically; flag judgment calls for the human.

---

## index.md conventions

```markdown
# TPU Model Performance Auto-optimization — Index
*Last updated: YYYY-MM-DD — N pages*

## Models (N)
*One row per `(architecture, lane)` page. Summarize across the page's variants in the one-line status.*
- [<architecture> — <lane>](models/<architecture>-<lane>.md) — variants: 8B/v6e-8 live (best 96 ms/step, 3 open hyps), 8B/v6e-32 blocked (OOM at seq=8192)

## Hypotheses — ranked, open only (N)
| # | Hypothesis | Model | Expected | Confidence | Effort |
|---|---|---|---|---|---|
| 1 | [<slug>](hypotheses/<slug>.md) | ... | 10-20% | high | M |

## Experiments (N)
- [YYYY-MM-DD <slug>](experiments/<model>_autoresearch_optimization/<lane>/experiments/YYYY-MM-DD-<slug>.md) — variant — verdict — one-line delta

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
| Model pages | `<architecture>-<lane>.md` | `llama3-8b-jax.md`, `gemma4-e4b-torchax.md` |
| Variant identifiers (experiment/hypothesis frontmatter) | `<size>/<hardware>` | `"8B/v6e-8"`, `"3B/v6e-32"` |
| Hypothesis pages | `<slug>.md` | `flash-attention-block-2048.md` |
| Experiment pages | `<model>_autoresearch_optimization/<lane>/experiments/<YYYY-MM-DD>-<slug>.md` | `llama3_8B_autoresearch_optimization/jax/experiments/2026-04-27-jax-exp20-splash-accepted.md` |
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
15. **One model page per `(architecture, lane)`** — do not split by size or hardware. Track per-variant state in the model page's Variant matrix. The lane axis is fundamental (different framework, different code path); the size/hardware axes are combinatorial accidents over the same code. Experiments pin exactly one `variant:` row.
