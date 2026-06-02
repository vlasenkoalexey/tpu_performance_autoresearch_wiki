---
name: create-retrospective
description: Generate a comprehensive retrospective for a `(model, lane)` pair that maps the explored search space, identifies coverage gaps from the topic taxonomy (`model-optimization-index.md`) and Pallas kernel catalog, surfaces premature-exhaustion signals (single-axis-probe vs kernel-port imbalance, frontier-stuck duration), and proposes ranked next directions. **Reads ALL experiment pages in the lane** — not a sample — because the retrospective's value depends on comprehensive coverage of what's been tried. Includes a lightweight cross-lane brief by default. Manually callable; intended to be invoked when the agent reports "out of ideas" or hits the stuck-frontier signature, BEFORE concluding the lane is exhausted. Output is a dated analysis page at `wiki/analyses/<YYYY-MM-DD>-<model>-<lane>-retrospective.md`; the skill does NOT act on its own recommendations — it produces analysis, the loop / `/formulate-hypothesis` acts.
---

# /create-retrospective — comprehensive lane retrospective

Maps the search space already explored on a `(model, lane)` pair, identifies where coverage is incomplete, and ranks unexplored directions. Run this **before** declaring a lane exhausted — the 2026-05-21 case (gemma4-jax declared exhausted; tokamax-CE kernel +4.18 pp landed a week later) is exactly the failure this skill exists to prevent.

## When to invoke

- **The agent says "I'm out of ideas" / "all options exhausted" / "recommend pausing"** — call this skill FIRST. The retrospective often surfaces a direction the agent forgot or hasn't tried.
- **The frontier hasn't moved in 10+ experiments** — search strategy may need to change, not just the next probe.
- **N single-axis probes refuted on the same row** with no kernel-level work tried — the imbalance pattern.
- **Manual invocation for human review** — `/create-retrospective gemma4 jax` produces the file; user reads + decides.
- **NOT for routine iteration** — full-read of every experiment page is expensive (~250K–500K tokens for a large lane). Call this when stuck, not on every cycle.

## Cardinal rules

- **Reads ALL experiments** in the lane, not a sample. Coverage is the whole point.
- **Single-lane primary, cross-lane brief default ON** — the brief is a 5–10 line summary of sibling lanes' frontiers + Knobs-matrix universal levers untransferred to this lane. Full cross-lane experiment-by-experiment read requires explicit `--cross-lane-deep`.
- **Does NOT act on its recommendations.** The skill produces an analysis page; the loop / `/formulate-hypothesis` decides what to dispatch.
- **Does NOT update the model page or hypothesis list** beyond linking to itself.
- **Does NOT auto-invoke `/formulate-hypothesis`** — the agent reads the retrospective and decides.
- **Idempotent + dated** — each invocation writes a NEW dated file; old retrospectives stay as historical record.

## Arguments

Required:
- `<model>` `<lane>` — positional. Example: `/create-retrospective gemma4 jax`.

Optional:
- `--include-sibling-lanes` (DEFAULT ON) — adds cross-lane brief at the bottom.
- `--no-cross-lane` — disables the cross-lane brief if the lane is genuinely isolated.
- `--cross-lane-deep` — adds full cross-lane experiment reads (expensive; rare).
- `--cross-model` — adds cross-model patterns (very rare; for newly-bootstrapped model architectures only).
- `--variant <size>/<hardware>` — restrict the retrospective to one variant row of the model page's matrix. Default: aggregate across all variants of the `(model, lane)`.
- `--since <YYYY-MM-DD>` — restrict to experiments dated on/after the given date. Default: all-time on the lane.
- `--full-redo` — force FULL mode (re-read every experiment) even when a prior retrospective exists. Use when you suspect a prior categorization was wrong, when the taxonomy in `model-optimization-index.md` shifted in non-trivial ways, or after a SCHEMA update. Default: INCREMENTAL when a prior exists (see Step 1a).

## Step 1 — Resolve scope + read priors

Resolve `<model>` and `<lane>`. If either is missing, infer from CWD (per `/start-experiment` Step 1 conventions) or ask via `AskUserQuestion`.

Then read in this order (cheapest first; deep reads come in Step 2):

1. **Per-lane log** — `wiki/experiments/<model>_autoresearch_optimization/<lane>/log.md` (one-line summaries; gives a chronological bird's-eye view of every iteration).
2. **Per-model refuted-patterns.md** — `wiki/experiments/<model>_autoresearch_optimization/refuted-patterns.md` (the cross-variant refuted-pattern record; cheap, dense).
3. **Model page** — `wiki/models/<model>-<lane>.md`. Extract: Variant matrix (Current best per variant + Open hyps + Retired hyps), Knobs translation matrix, Iteration ladder.
4. **Topic taxonomy** — `wiki/model-optimization-index.md`. Need the 16-ish topic buckets (Sharding, CE/softmax loss, MoE dispatch, Splash attention, Tensor parallelism, FSDP, VMEM, AC, Batch/seq, Pallas kernels, torch.compile/scan, HBM/IO, Hardware envelope, libtpu/XLA flags, etc.) and what each topic's catalog options are.
5. **Pallas catalog** — `wiki/analyses/2026-04-23-pallas-kernel-directory.md`. The list of every Pallas kernel + the function each implements. Will be cross-referenced against this lane's kernel ports.
6. **Most recent existing retrospective for this `(model, lane)`** — search `wiki/analyses/` for `*<model>*<lane>*retrospective*.md` and read just the newest. Extract:
   - The retrospective's `updated:` date (or filename date)
   - The `## Experiment ledger` table at the bottom (machine-readable; see Step 8)
   - The frontier MFU + variant + experiment v-ID recorded at the top
   - The recommendations the prior surfaced (so the new retrospective can note which were acted on, which remain open)

## Step 1a — Decide FULL vs INCREMENTAL mode

The retrospective produces the same superseding output regardless of mode; only the read cost differs.

- **No prior retrospective** → FULL mode (read every experiment in Step 2a).
- **Prior retrospective exists** → default to INCREMENTAL (Step 2b: deep-read only NEW + UPDATED experiments; inherit categorizations for the rest from the prior's ledger).

Force FULL mode (even with a prior) if ANY of the following hold:

- **Topic taxonomy shifted** — `wiki/model-optimization-index.md` mtime is later than the prior retrospective's date. New topics may exist or old ones may have been renamed; categorizations need recomputing across all experiments.
- **Pallas catalog updated** — `wiki/analyses/2026-04-23-pallas-kernel-directory.md` mtime is later than the prior date. The 🔵 unexplored-kernel marks need recomputing across all experiments' kernel topic.
- **Model page variant matrix changed** — variant rows in `wiki/models/<model>-<lane>.md`'s Variant matrix differ from the rows the prior retrospective covered (e.g., a new hardware row was added). Per-variant sections need expansion against fresh categorization.
- **`--full-redo` flag passed** — user explicit override.

Report the chosen mode in your status update before doing real work:

```
Mode: FULL (no prior retrospective)
Mode: INCREMENTAL (prior: 2026-05-25-gemma4-jax-retrospective.md; +N new experiments since)
Mode: FULL (force-redo: taxonomy shifted — model-optimization-index.md updated 2026-06-01)
Mode: FULL (force-redo: --full-redo flag)
```

This lets the caller know what cost regime to expect (FULL ≈ 5-8 min on a 400-experiment lane; INCREMENTAL ≈ <2 min).

## Step 2 — Read experiment pages

### Step 2a — FULL mode

Walk `wiki/experiments/<model>_autoresearch_optimization/<lane>/*.md`. For each experiment page:

- Frontmatter: `variant`, `hypothesis`, `commit`, `status`, `verdict`, `backfilled` (if any).
- `## Hypothesis under test` section: extract Mechanism + Predicted signal (if present, per the stub-first lifecycle).
- `## Results` section: extract headline metric delta vs frontier.
- `## Verdict` section: reasoning + Phase 3 hypothesis-firing audit result (CONFIRMED / SILENT NO-OP / PARTIAL).

This is the expensive step. For a lane with N experiments at ~5 KB/page, the read cost is N × 5 KB. Budget: 100 KB to 2 MB total depending on lane size. The skill explicitly accepts this — coverage is non-negotiable.

If `--variant <size>/<hardware>` was passed, filter to experiments whose frontmatter `variant:` field matches.
If `--since <YYYY-MM-DD>` was passed, filter to experiments dated on/after.

The output of Step 2a is a fresh ledger: one row per experiment with `(v-ID, date, variant, topic, verdict, frontier-shift)`. This ledger feeds Steps 3-7.

### Step 2b — INCREMENTAL mode

Parse the prior retrospective's `## Experiment ledger` table into rows (v-ID + date + variant + topic + verdict + frontier-shift). This is the inherited ledger.

List the current experiment dir. For each experiment page:

- **NEW** — v-ID is absent from the prior ledger. **Must** be deep-read.
- **UPDATED** — v-ID is present in the prior ledger BUT the experiment page's `updated:` frontmatter date is later than the prior retrospective's date. **Must** be deep-read. This catches verdict-assignment-after-the-fact (stub was filed before prior retrospective; verdict assigned after; or `status: in_progress → filed` flip happened post-prior).
- **STABLE** — present in the prior ledger, not updated since. INHERIT the prior row verbatim (no read).

Deep-read NEW + UPDATED using the per-page extraction logic from Step 2a (frontmatter + `## Hypothesis under test` + `## Results` + `## Verdict`). Merge into the prior ledger:

- NEW rows append (any position; Step 7 sorts).
- UPDATED rows REPLACE the corresponding prior row by v-ID.
- STABLE rows unchanged.

If `--variant` / `--since` filters were passed, apply them to the MERGED ledger (so the filter is consistent regardless of mode).

The output of Step 2b is the same shape as Step 2a — a complete ledger, just produced with N_new + N_updated deep reads instead of N_total. Steps 3-7 are identical from here.

## Step 3 — Categorize each experiment

Map each experiment to ONE primary topic from the model-optimization-index taxonomy. Method runs in waves; first match wins. Each wave is more expensive than the last; later waves only fire when earlier ones don't catch the experiment.

### Wave 1 — Tag match (cheap)

If the experiment page's frontmatter `tags:` list contains a topic anchor (e.g., `pallas-kernel`, `splash`, `fsdp`, `tokamax`, `scan`, `ac`, `vmem`, `bf16`, `gate-up-fusion`, `data-formatting`, `topology`, etc.), use it.

### Wave 2 — Slug keyword match (cheap)

Match slug substrings against a topic dictionary. **This dictionary is intentionally broad and additive — if you encounter slugs that don't match an entry, ADD the entry to your in-memory dictionary as you go and surface it for the user (see Wave 5 + dictionary-growth note below).** The starting set covers ~16 topics; expect to grow it 2–5 entries per retrospective on a mature lane.

Topic dictionary (extend freely):

- **Pallas kernels** — `pallas|kernel|tokamax|mosaic|tpu-recipes|fused-rope|fused-rmsnorm|fused-qkv|splash-kernel|custom-call|hand-rolled`
- **Splash attention** — `splash|sa-block|sa_use|bkv|bq|sliding-window` (attention kernel knobs)
- **Op fusion / kernel fusion** (general — NOT MoE-specific) — `fusion|fuse-|coalesc|kernel-merge|epilogue|prologue|loop-fusion|input-fusion|output-fusion|convolution-fusion|elementwise-fusion`
- **Data transformation overhead** — `moveaxis|transpose|layout|reshape|spmd-copy|data-format|data_formatting|bitcast|copy-elimination|layout-canonicaliz|permute|view`
- **Sharding strategy** — `shard|sharding|gspmd|shardy|partir|mesh|named-sharding|partial-replication|p-spec`
- **FSDP / collective optimization** — `fsdp|all-gather|reduce-scatter|all-reduce|overlap|bucketing|async-collective|collective-matmul|host-offload|sparsecore-offload`
- **Tensor parallelism** — `tp|tensor-parallel|tensor-paralle|sequence-parallel`
- **MoE expert dispatch** — `moe|expert|dispatch|combine|gate|router|top-k|ragged-dot|segment-matmul`
- **Gate+up fusion** (MoE-specific subtype) — `gate-up|gate_up|up-gate|fused-gate|weight-fused|fused-weight` (often together with MoE)
- **torch.compile + scan** — `scan|compile|torch-compile|torch.compile|graph-trainer|aot|graph-break|dynamo|fullgraph`
- **Activation checkpointing** — `ac|checkpoint|remat|rematerialization|selective|ptd-checkpoint|memory-budget`
- **VMEM / scratch memory** — `vmem|scoped-vmem|scratch|smem|tile-size|block-size|vmem-budget`
- **Dimension alignment + dtype** — `bf16|fp8|fp16|dtype|precision|mxu-align|mixed-precision|reduce-dtype|param-dtype`
- **Batch-size + sequence amortization** — `lbs|batch|seq-len|seq_len|seq8k|seq4k|amortization|gradient-accumulation|microbatch|lbs8|lbs16`
- **HBM transient memory + I/O** — `hbm|oom|memory-pressure|defrag|peak-memory|cpu-offload|host-offload|spill|persistent-cache`
- **libtpu / XLA flags** — `libtpu|xla-flag|libtpu_init|enhanced-launch|barrier|collective-matmul|spmd-threshold|vmem-limit|tpu_use_|tpu_enable_`
- **Topology / hardware envelope** — `topology|v5p|v6e|v7x|multi-slice|single-slice|num-slices|cross-gen|cross-arch|chip-count`
- **Profile-driven attribution** — `xprof|profile-drilldown|op-profile|bucket-attribution|roofline|measurement` (rare; usually adjunct to another topic)
- **Checkpointing / persistence** — `orbax|checkpoint-save|checkpoint-load|async-save|persistence`

### Wave 3 — Hypothesis statement + Mechanism keyword match (medium cost)

If Waves 1–2 didn't catch it, scan the experiment page's `## Hypothesis under test` section (the Hypothesis + Mechanism + Predicted signal labels) with the same dictionary. The hypothesis statement often names the mechanism even when the slug abbreviates it ("v294 splash-1024" slug + "tile sizing reduces kernel-boundary count" mechanism would both hit Splash attention, but slugs like "v167" or "v282" might only describe the change in the body, not the slug).

### Wave 4 — Topic-inference from Predicted signal (medium cost)

If still uncategorized, look at the Predicted signal field. Many topics have signature predicted signals:

- "`<topic>` bucket drops from X to Y" → Profile-driven attribution + the named topic (categorize as the named topic if specific; fallback Profile-driven)
- "custom_call(target=<X>) appears in HLO" → Pallas kernels
- "HLO module count drops" → torch.compile + scan
- "all-gather time drops" → FSDP / collective optimization
- "peak HBM drops" → HBM transient memory + I/O (or Activation checkpointing if AC-driven)
- "MXU utilization rises" → Dimension alignment + dtype (alignment) or Pallas kernels (custom compute)

### Wave 5 — LLM inference + propose new topic (the expensive fallback)

If all keyword waves miss, the experiment is genuinely outside the current dictionary. Read the experiment page's Hypothesis + Mechanism + Predicted signal + Verdict reasoning, and **infer a topic** from the model-optimization-index's 16-topic taxonomy. If NONE of the 16 topics fits even loosely, propose a NEW topic name and flag in the retrospective:

```markdown
### Uncategorized experiments + proposed topic additions

The following experiments don't map cleanly to any existing topic in model-optimization-index.md:

- v418 (gemma4-tpu): tested an autograd-integrated structural rewrite (autograd-level hooks below the compiler). Proposed new topic: **"Autograd-integrated structural rewrites"** — distinct from torch.compile + scan because the lever operates BELOW Dynamo (autograd-level hooks rather than compile-time graph capture).

- v391y (gemma4-jax): tested chunked-XLA backward kernel. Proposed new topic: **"Compiler-side loss kernel rewriting"** — adjacent to Pallas kernels but the lever is XLA-pass-level rather than custom kernel.

→ Recommend updating wiki/model-optimization-index.md to include these topics with their own Mechanism subsections + Generic refuted-pattern principles.
```

These flagged experiments still get categorized into the closest existing topic for the tree (don't leave them dangling), but the retrospective surfaces the gap so the human curator can extend the index.

### Wave 6 — Last-resort Uncategorized

Reserved for experiments where even Wave 5 inference can't find a topic (genuinely unintelligible hypothesis, or the page is too sparse). Categorize as `Uncategorized`; flag the v-IDs in the retrospective with a "data-quality" note.

### Dictionary-growth discipline

Every retrospective run that hits Wave 2 misses (Waves 3–5 firing) should:
1. **Note the misses** — list which slugs/hypothesis-statements didn't catch on Wave 2
2. **Propose dictionary additions** — for each repeated miss (e.g., 3+ experiments using the same vocabulary), add the keyword to Wave 2's dictionary in your in-memory copy and mention the addition in the retrospective's "Methodology" subsection
3. **Don't auto-edit this SKILL.md** — surface the proposed additions; the human curator decides when to update the dictionary persistently

Per-experiment outcome: track per topic `[supported_v_ids, refuted_v_ids, inconclusive_v_ids, invalid_v_ids, total_count, categorization_method ∈ {tag, slug, hypothesis, predicted-signal, llm-inference, uncategorized}]`. The `categorization_method` field lets you report the dictionary coverage rate at the bottom of the retrospective ("78% of experiments caught at Wave 1-2; 18% at Wave 3-4; 4% required LLM inference"). Falling Wave 1-2 coverage is a signal the dictionary needs maintenance.

## Step 4 — Build the mechanism tree

Render a markdown nested-list tree, one top-level bullet per topic (sorted by total_count desc), one nested bullet per concrete attempt or sub-topic. Use status icons:

- 🏆 frontier-shifting supported experiment
- ✅ supported (non-frontier)
- ❌ refuted
- ⚠️ inconclusive
- 💥 invalid
- 🔵 unexplored catalog option (cross-ref against model-optimization-index's catalog + Pallas catalog)

For each catalog option that has zero experiments in this lane, add a 🔵 bullet citing the catalog source. This is how "what's NOT been explored" surfaces inline in the tree.

Example shape:

```
- **Pallas kernels** (12 experiments)
  - tokamax CE — 🏆 v391f +4.18pp; 🏆 v391m +1.61pp cross-variant
  - tokamax segment_matmul — ❌ v391y -200× regression (silent-noop refuted)
  - 🔵 fused RMSNorm+RoPE+QKV — UNEXPLORED (catalog: tpu-recipes/maxtext-deepseek)
  - 🔵 NSA (Native Sparse Attention) — UNEXPLORED (catalog: paper 2025-02)
  - 🔵 ring-attention — UNEXPLORED (catalog: jax-ring-attention)
- **FSDP / sharding** (17 experiments)
  - ...
```

## Step 5 — Detect premature-exhaustion signals

Compute and surface these signals prominently at the top of the retrospective (before the tree):

1. **Single-axis-probe vs kernel-port ratio.** Count topic-buckets:
   - "Single-axis probes" = libtpu/XLA flags + Dimension alignment + dtype + Batch/seq + VMEM (low-risk, single-knob)
   - "Kernel work" = Pallas kernels + torch.compile/scan (structural code changes)
   - Compute ratio. If single-axis : kernel ≥ 5:1 AND frontier-stuck-for-N ≥ 10 → flag.

2. **Frontier-stuck duration.** Sort supported experiments by date. Find the most recent verdict that moved the lane's `Current best` (per the model page's variant matrix). Count experiments since: if ≥ 10 → flag. The signal: search strategy needs to change, not the next probe.

3. **Topic refutation density.** For each topic, count refuted experiments. If any topic has ≥ 5 refuted AND no supported on the same variant → "the lane has comprehensively closed topic X; further experiments in this topic are anti-recommendations".

4. **Coverage incompleteness.** For each topic, compute `(tried catalog options / total catalog options)`. Topics with < 40% coverage AND no supported result → "under-explored; not yet enough evidence to call closed".

These signals get a dedicated section at the top of the retrospective:

```markdown
## Search-strategy assessment

⚠️ Single-axis-heavy: 17 flag/precision probes vs 2 kernel ports. Ratio 8.5:1 well above the 5:1 imbalance threshold.
⚠️ Frontier stuck for 14 experiments since v294 (2026-05-21 splash 1024 win).
✅ Sharding topic: well-explored (9 attempts, 1 supported, 8 refuted with diverse mechanisms) — calling this closed is justified.
🔵 Pallas kernels: under-explored (2 of 12 catalog options tried; 1 supported); coverage 17%.

**Inference**: lane likely has +3-5 pp upside in kernel work that single-axis probing won't surface.
```

## Step 6 — Generate cross-lane brief (default ON)

If `--no-cross-lane` was NOT passed, add a brief that scans sibling lanes for transferable wins. Two-tier read (cheap first, opportunistic second):

### Step 6a — Sibling model-page scan (always done if brief enabled)

For each other lane of the same model (e.g., if current is jax, scan tpu / torchax / maxtext):

1. Read `wiki/models/<model>-<sibling>.md`.
2. Extract:
   - Current best MFU per variant (one line summary)
   - Knobs translation matrix rows marked universal (`win` in every column)
3. Diff against current lane's Knobs matrix: which universal levers haven't been tried on this lane?

### Step 6b — Sibling retrospective scan (opportunistic — only when sibling has one)

For each sibling lane, also search for an existing retrospective:

```bash
wiki/analyses/*<model>*<sibling-lane>*retrospective*.md
```

If found, read just the most recent. Extract three things:

1. **Their top 5 recommended directions** — for each, check if it's transferable to OUR lane:
   - If the recommendation is a topic-agnostic mechanism (e.g., "kernel-port fused RMSNorm+RoPE+QKV") → likely transferable; surface as candidate
   - If lane-specific (e.g., "SimpleFSDP refactor" only applies to tpu's torch.compile path) → cite + mark non-transferable
   - If something we've already refuted on THIS lane → flag as conflict ("sibling lane recommends X; we refuted X on Y/Z; topology or stack difference may explain")

2. **Their experiment ledger's recent supported wins** — diff against our ledger by topic + mechanism. Any topic where sibling has a supported result and we have only refuted (or empty)? Those are immediate cross-port candidates.

3. **Their anti-recommendations / closed topics** — does the same trap apply here? If sibling closed "single-axis flag probes on 3B" and we're heavy in the same direction, that's corroborating evidence to close the same topic on our lane.

Mark each pulled-in item with **source**: which sibling retrospective + which section it came from. This lets `/formulate-hypothesis` cite the right precedent when proposing.

**Sibling retrospective staleness** — if the sibling retrospective is older than 14 days, lower confidence weight in Step 7's ranking. Surface the date in the brief so the reader can judge.

**Conflict signal** — if the sibling retrospective recommends something we have refuted (or closed), DO NOT silently drop it; surface explicitly in a `Conflicts with our prior work` subsection. Examples:
- Sibling jax says "Pallas RMSNorm refuted (compile-time blocker)"; we say "Pallas RMSNorm UNEXPLORED" → resolve: this is "unexplored due to sibling's evidence" not "uncalibrated unknown"
- Sibling jax says "scan-over-layers supported +18%"; we have it refuted → flag stack difference; sibling's mechanism may not port without modification

Output combines 6a + 6b:

```markdown
## Cross-lane brief

### Sibling lane summaries (model pages)

- **gemma4-tpu**: 3B/v5p-16 frontier 14.50% MFU @ v885; lbs=8 SimpleFSDP is the recent shift.
  - Universal levers transferable: SimpleFSDP (jax doesn't use it; needs shard_map equivalent), bf16-compute (jax has it; OK), gate+up MoE fusion (jax has it; OK)
- **gemma4-torchax**: 3B/v5p-16 frontier 0.17% MFU (structural floor); no immediate transfer candidates.
- **gemma4-maxtext**: not yet ingested for this model.

### Sibling retrospective candidates (from sibling lanes' own analysis)

- **gemma4-tpu** retrospective (2026-05-28, recent):
  - Top recommendation: "Pallas RoPE kernel avoiding reshape" — TRANSFERABLE: this lane also has the same view→reshape friction in apply_rope; cite tpu's v675b precedent
  - Ledger reveals: tpu has 3 supported tokamax kernels; we have only 1 (v391f CE); 2 more candidates surfaceable
  - Their anti-recommendation: "single-axis flag probes on 3B" — CORROBORATES our own closure of this topic
- **gemma4-torchax** retrospective (2026-04-10, STALE — 50+ days old; low confidence):
  - Recommendations age-discounted

### Conflicts with our prior work

- **scan-over-layers**: tpu's retrospective says "refuted (compile + numeric divergence)"; our ledger has v330 refuted but tpu's mechanism is different (FX-pass-vs-source-level) — port may require different code path; not auto-importable as a recommendation
```

The brief is intentionally short (10-25 lines for a model with 2-3 sibling lanes; 30+ lines if multiple have rich retrospectives). For the deeper "what specific experiment from sibling lane should we port?" question, that's the next iteration's `/formulate-hypothesis` job using this retrospective's Recommendations section as the candidate list.

The cross-lane brief's pulled-in candidates feed into Step 7's ranking with `source: sibling-retrospective:<lane>` annotation, so the final Recommended directions table shows whether each candidate was surfaced locally (gap-analysis) or imported from a sibling.

## Step 7 — Rank recommended next directions

For each 🔵 unexplored option from the tree + each transferable cross-lane lever + each transferable candidate pulled from sibling retrospectives in Step 6b, compute:

- **Expected gain** — from model-optimization-index estimates if cited, sibling-lane evidence if applicable, "speculative" if no source
- **Confidence** — high if cataloged + sibling-lane evidence; medium if cataloged only; low if speculative
- **Effort** — S (flag/recipe), M (per-file model edit), L (multi-day kernel work, multi-stack port)
- **Score** = (expected_gain × confidence_multiplier) / effort_multiplier

  where `confidence_multiplier ∈ {high: 1.0, medium: 0.7, low: 0.4}`, `effort_multiplier ∈ {S: 1, M: 3, L: 9}`

Surface top 5–10 in a ranked table. The `Source` column distinguishes provenance so the reader (and `/formulate-hypothesis`) can cite the right precedent:

```markdown
## Recommended next directions

| # | Direction | Topic | Gain | Conf | Effort | Score | Source |
|---|---|---|---|---|---|---|---|
| 1 | Fused RMSNorm+RoPE+QKV Pallas kernel | Pallas | +3-5pp | medium | L | 0.78 | local-gap: index Pallas catalog |
| 2 | Cross-port splash bkv=1024 from jax-frontier | Splash | +0.5pp | high | S | 0.50 | sibling-knobs: tpu lane v294 win |
| 3 | Pallas RoPE avoiding reshape (per tpu retrospective) | Pallas | +0.85pp | medium | M | 0.20 | sibling-retrospective: tpu 2026-05-28 |
| ... | ... | ... | ... | ... | ... | ... | ... |
```

Source taxonomy (use exactly one per row):
- `local-gap: <citation>` — surfaced by THIS retrospective's tree/coverage analysis
- `sibling-knobs: <lane> <citation>` — pulled from sibling model page's Knobs matrix (Step 6a)
- `sibling-retrospective: <lane> <date>` — pulled from sibling lane's prior retrospective recommendations (Step 6b)
- `cross-lane-conflict: <lane>` — sibling recommends X; we have evidence against; surface but lower confidence

The Source column lets the next `/formulate-hypothesis` invocation cite the right precedent + stack-difference caveats when filing the hypothesis page.

Plus an anti-recommendations section listing topics that are closed:

```markdown
## Anti-recommendations (don't pursue these)

- **Single-axis flag probes on 3B/v5p-16** — 17 refuted; coverage > 80% of catalog options; structurally closed. Spending more cycles here is the failure mode this retrospective exists to prevent.
- **Sharding axis re-exploration** — 9 attempts with diverse mechanisms; the one supported (v228) is already the frontier baseline. Wait for v6e topology before reopening.
```

## Step 8 — Write the retrospective file

Path: `wiki/analyses/<YYYY-MM-DD>-<model>-<lane>-retrospective.md`. If a retrospective with the same date already exists, suffix `-2`, `-3`, etc. (multiple per day OK; rare).

Page structure (in order):

```markdown
---
title: "Retrospective — <model> / <lane> as of <YYYY-MM-DD>"
type: analysis
tags: [retrospective, <model>, <lane>]
model: <model>
lane: <lane>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

# <model> / <lane> retrospective — <YYYY-MM-DD>

**Scope**: <variant matrix rows covered>
**Period**: <first experiment date> → <last experiment date>
**Experiments**: <N total>, <S supported>, <R refuted>, <I inconclusive>, <V invalid>, <B backfilled>
**Frontier**: <current best MFU per variant from model page>

## Search-strategy assessment

<premature-exhaustion signals from Step 5>

## Mechanism tree

<topic-by-topic tree from Step 4>

## Coverage gaps — what's NOT been explored

<table: Topic / Catalog options / Tried / Unexplored>

## Recommended next directions

<ranked table from Step 7>

## Anti-recommendations

<closed-topic list>

## Cross-lane brief

<from Step 6 if enabled>

## Experiment ledger (machine-readable — used by future incremental retrospectives)

This table is the persistent "state" that subsequent retrospectives parse in Step 2b's INCREMENTAL mode. **Keep it complete** (every experiment on the lane that fell within `--variant`/`--since` filters; or every experiment if no filters) and **structured** (parseable by standard markdown table readers).

| v-ID | Date | Variant | Topic | Verdict | Frontier-shift |
|---|---|---|---|---|---|
| v001 | 2026-04-10 | 3B/v5p-8 | dimension-alignment-dtype | supported | yes (+5.7×) |
| v002 | 2026-04-11 | 3B/v5p-8 | splash-attention | refuted | no |
| ... | ... | ... | ... | ... | ... |
| v412 | 2026-06-01 | 3B/v5p-16 | pallas-kernels | refuted | no |

**Schema**:
- `v-ID`: zero-padded 3-digit ID per `<lane>/` naming convention (e.g., `v412`).
- `Date`: `YYYY-MM-DD` from the experiment page's `updated:` frontmatter (falls back to `created:` if `updated:` absent).
- `Variant`: `<size>/<hardware>` per the variant matrix (e.g., `3B/v5p-16`).
- `Topic`: one of the model-optimization-index topic anchors (e.g., `pallas-kernels`, `splash-attention`); or `Uncategorized` (flagged in the tree as a hint that frontmatter `tags:` is missing).
- `Verdict`: `supported | refuted | inconclusive | invalid | backfilled-inconclusive | backfilled-invalid`.
- `Frontier-shift`: `yes (<delta>)` if this experiment moved the lane's `Current best` in the model page's variant matrix; `no` otherwise.

If `--full-redo` was passed AND the prior retrospective had a ledger, NOTE in this section any rows that materially changed (topic re-categorization, verdict revision) — that's the audit trail for why the redo was warranted.

## Sources

- Per-lane log: `wiki/experiments/<model>_autoresearch_optimization/<lane>/log.md`
- Per-model refuted-patterns: `wiki/experiments/<model>_autoresearch_optimization/refuted-patterns.md`
- Model page: `wiki/models/<model>-<lane>.md`
- Topic taxonomy: `wiki/model-optimization-index.md`
- Pallas catalog: `wiki/analyses/2026-04-23-pallas-kernel-directory.md`
- Prior retrospective (if any): `wiki/analyses/<prior>`
- All N experiment pages in `wiki/experiments/<model>_autoresearch_optimization/<lane>/`

## See also

- `wiki/models/<model>-<lane>.md`
- Prior retrospective (if any)
- `.claude/skills/formulate-hypothesis/SKILL.md` — the downstream consumer
```

Update `wiki/index.md` to bump the Analyses count + add a one-line entry.

Append to global `wiki/log.md` (cross-cutting op per SCHEMA's two-tier convention; analyses go in global if cross-lane, this one is single-lane but adds a global-log entry under op type `analyze`).

## Step 9 — Return to caller

One-line summary + path to file. Surface the top 3 recommended directions inline so the caller can act immediately without re-reading the file:

```
Retrospective written: wiki/analyses/2026-06-02-gemma4-jax-retrospective.md
Experiments analyzed: 412 (across 3B/v5p-16, 24B/v5p-32, 150B/v5p-64)
Frontier stuck for 14 experiments; single-axis-probe ratio 8.5:1 (imbalance signal)

Top 3 recommended next directions:
  1. Fused RMSNorm+RoPE+QKV Pallas kernel (gain +3-5pp, conf medium, effort L, score 0.78)
  2. Cross-port splash bkv=1024 from sibling lane (gain +0.5pp, conf high, effort S, score 0.50)
  3. ...
```

The caller (whether the agent itself or the user) reads this and decides what's next.

## Failure modes to handle

- **Model + lane doesn't resolve** — `AskUserQuestion` to disambiguate (cf. `/start-experiment` Step 1).
- **No experiments in lane (new lane)** — produce a "bootstrap mode" retrospective: cite the model-optimization-index recommendations for first-iteration probes; no mechanism tree (nothing tried yet); cross-lane brief becomes the primary input.
- **Model page missing** — refuse with hint: "model page `wiki/models/<model>-<lane>.md` doesn't exist; run `/create-experiment` first".
- **Pallas catalog missing** — proceed without it; flag in the output ("Pallas catalog not found; kernel coverage analysis skipped").
- **All experiments share one topic (skewed lane)** — that's actually informative; the retrospective surfaces it as "extreme single-topic focus" and is itself the premature-exhaustion signal.
- **Frontier unchanged for entire history** — flag immediately as "stuck-from-start"; recommend topology change or substrate validation before deeper iteration.
- **Read budget exceeds 1 MB / 250K tokens** — proceed anyway; warn user that this is an expensive call. The skill is designed for rare invocation (when stuck), so the cost is justified.

## Cost expectations

### FULL mode (no prior retrospective, or force-redo)

| Lane size | Total reads | Approx tokens | Wall-time |
|---|---|---|---|
| 50 experiments | ~250 KB | ~60K | <1 min |
| 200 experiments | ~1 MB | ~250K | 2-3 min |
| 400 experiments | ~2 MB | ~500K | 5-8 min |
| 1000+ experiments | ~5 MB | ~1.2 M | 15+ min, may hit context limits |

### INCREMENTAL mode (prior retrospective exists, foundation unchanged)

| New + updated since prior | Approx tokens | Wall-time |
|---|---|---|
| 5 | ~30K | <1 min |
| 30 | ~80K | <2 min |
| 100 | ~200K | 2-4 min |
| 300+ | (consider `--full-redo` for safety; this is borderline) | |

For lanes with > 500 experiments, consider using `--variant <size>/<hardware>` to restrict scope, OR `--since <date>` to read only recent history. The default is comprehensive; the flags exist for runaway-scale lanes.

The INCREMENTAL path is typically **5-10× cheaper** than FULL for routine refreshes. Use FULL when the foundation has materially shifted (taxonomy, catalog, variant matrix) or when you suspect a prior categorization was wrong.

### Cross-lane brief overhead

| Sibling lanes present | Approx extra reads | Approx extra tokens |
|---|---|---|
| 1 lane, no retrospective | model page only | ~30K |
| 1 lane, with retrospective | model page + retrospective | ~80K |
| 3 lanes, 1 with retrospective | 3 model pages + 1 retrospective | ~150K |
| 3 lanes, all with retrospectives | 3 model pages + 3 retrospectives | ~250K |

The sibling retrospective scan (Step 6b) is **opportunistic** — only fires when the file exists. New models with no sibling retrospectives just get the cheaper model-page-only brief. No flag needed to disable per-sibling; Step 6 just gracefully skips when nothing is there.

## What this skill does NOT do

- **Does NOT act on its recommendations.** Output is analysis. The loop / `/formulate-hypothesis` decides what to dispatch next.
- **Does NOT update the model page** beyond the new analysis-page link.
- **Does NOT auto-invoke `/formulate-hypothesis`** — the agent reads + decides.
- **Does NOT file hypothesis pages** — it surfaces directions; `/formulate-hypothesis` is the canonical hypothesis-filer.
- **Does NOT commit** — the user reviews + commits per existing convention.
- **Does NOT modify experiments** — read-only operation over the experiment ledger.
- **Does NOT cross-pollinate findings into model-optimization-index or blueprint** — that's a separate `analyze` or `manual` operation; this skill produces a single dated analysis page.

## See also

- `wiki/model-optimization-index.md` — topic taxonomy used in Step 3 categorization
- `wiki/model-optimization-blueprint.md` — effort estimates + phase ordering for Step 7 ranking
- `wiki/analyses/2026-04-23-pallas-kernel-directory.md` — Pallas kernel catalog used in Step 4 coverage detection
- `.claude/skills/formulate-hypothesis/SKILL.md` — the downstream consumer (reads the most recent retrospective at Step 5)
- `SCHEMA.md` — analysis page format + log routing rules (this op type is `analyze`; goes in global `wiki/log.md` if cross-lane, per-lane log if single-lane)
