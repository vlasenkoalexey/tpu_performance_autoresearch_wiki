---
name: formulate-hypothesis
description: Generate a structured optimization hypothesis for the autoresearch loop. Walks three layers — (1) the generic wiki/model-optimization-index.md for TPU envelope data + topic pointers + cross-model refuted-pattern principles, (2) the generic wiki/model-optimization-blueprint.md for ladder-keyed phase ordering + compounding rules + trap awareness, and (3) the per-model refuted-patterns layer + model page + recent experiments for variant-specific prior refutations. The index and blueprint are intentionally complementary: the index answers "for topic X, what's the mechanism and what's refuted?"; the blueprint answers "in what order do I apply optimizations, what compounds, what trap will bite me?". Reads both index and blueprint in FULL (each ~lean; full-read is the safety guarantee against TLDR-tunneling). Then reads the catalog-chosen depth pages (concept + observation + source pages cited under the 1-3 implicated topics' Mechanism subsections) directly via Read — the catalog has done the filtering; no subagent middleman. Returns a structured proposal with mandatory fields (hypothesis, topic, blueprint phase, wiki precedents reviewed, generic-principle checks, per-model refuted-patterns check, profile signal, falsification criterion, expected gain). Invoke from the autoresearch loop before constructing the workload name and dispatching the gke-cluster-runner. NEVER skip this skill before proposing a hypothesis — failures like 200× regressions on chunked-XLA backward (the v391y class) came from skipping the precedent check.
---

You are formulating one optimization hypothesis for the autoresearch loop. The output of this skill MUST be a structured proposal that the master agent reviews before dispatching. Do not skip steps.

## Step 1 — Gather inputs from caller / session context

The caller (typically the loop in `/start-experiment` Step 9, step 2(c)(i)) provides:
- **`<model>`** + **`<lane>`** — e.g. `gemma4` + `jax`
- **`<variant>`** — current variant being optimized (e.g. `3B/v5p-16`, `24B/v5p-32`)
- **`<mode>`** (optional, default `frontier`) — one of:
  - `frontier` (default): variant has a measured-best baseline and regression would be costly. Full ceremony. Pick this when the model page's variant matrix shows a non-trivial Current best for the variant.
  - `exploration`: variant is early-stage, stuck, or being probed. Lighter ceremony, hunches allowed. Pick for stalled variants where the ladder has saturated, or when probing a hypothesis category the wiki doesn't yet cover.
  - `bootstrap`: brand-new model with thin/no per-model state (no per-model refuted-patterns.md, no retrospectives, variant matrix has < 3 rows or no Current best). Even lighter ceremony — Steps 4, 5 degrade gracefully; first-principles reasoning from index + blueprint is the primary input. See the "Bootstrap mode" section below for the auto-detection rule and the full mode-specific override behavior.
  - `user-override`: the caller has specified an exact candidate (passed in `<user_specified_candidate>`). Skill skips hypothesis generation and just validates the candidate (refuted-pattern check + topic fit + semantics-preservation check), then emits the proposal.
- **`<user_specified_candidate>`** (optional, REQUIRED if `<mode>` is `user-override`) — the exact hypothesis the caller wants validated (one sentence, falsifiable form).
- **`<topic_hint>`** (optional) — caller's best guess at the topic. If not provided, infer from recent profile / frontier-shift conversation.
- **`<recent_profile_summary>`** (optional but strongly preferred) — bucket attribution from the most recent xprof. If absent, the proposal should recommend capturing a profile first rather than committing to a candidate.
- **`<current_frontier>`** — MFU + experiment ID of the variant's current frontier
- **`<last_2_3_experiments>`** — what was just tried, with verdicts
- **`<in_flight_v_ids>`** — workload v-IDs other tracks are running, so the proposal steers clear of duplicates

If any input is missing AND not derivable from session context, ask the caller for it before proceeding. Do not invent.

### Step 1.5 — Describe the profile signal in your own words BEFORE consulting the TLDR

Before you open the index, write a 2-3 sentence description of what `<recent_profile_summary>` actually shows: which buckets dominate, by what percentage, what changed vs the prior experiment, whether the dominant bucket has a clear name (`convolution fusion`, `custom-call`, `data formatting`, etc.) or is unusual.

This is the **profile-first anchor**. The TLDR table maps known signatures to topics; without grounding in your own reading of the profile first, you'll be tempted to round the actual signal into the nearest TLDR row even when it doesn't quite fit. Reading the profile first lets you spot mismatches and novel signatures.

If no recent profile is available, state that explicitly and recommend the caller capture a profile before this skill commits to a hypothesis — except in **exploration mode**, where a profile-less hunch is allowed (see Step 7's exploration template).

## Cost visibility — what this skill consumes per invocation

Full-ceremony invocations (frontier mode, no short-circuit) read:
- Index: ~25k tokens
- Blueprint: ~18k tokens
- Catalog-cited depth pages for 1-3 implicated topics: ~30-150k
- Model page + last 3 experiments + 1 retrospective: ~25-50k
- Per-model refuted-patterns.md: <5k

Total: **~100-260k tokens per invocation** = ~$0.50-2.00 at current Opus 4.7 input pricing.

This is the right cost when frontier-hardening, exploring a non-trivial candidate, or when a regression would be expensive. It is NOT the right cost for:
- One-off interactive questions ("what's the current frontier?") — just read the model page directly
- Quick triage during a chat ("what should we try next?") — caller can name a candidate and use `user-override` mode for a ~5k validation
- Loop iterations where the previous hypothesis just refuted and the next-best from the open-hypothesis list is obvious — caller can specify it via `user-override`

If you're invoking this skill repeatedly within a 5-minute window, the prompt cache will absorb most of the cost. Across multi-hour loop iterations, expect re-reads on cache eviction.

## Bootstrap mode — handling new models with thin state

If `<mode>` is `bootstrap` (or autodetected: model page has < 3 variant matrix rows AND no per-model refuted-patterns.md AND no retrospective in `wiki/analyses/` matching the model):

- **Steps 4 + 5 degrade gracefully**: per-model refuted-patterns.md likely doesn't exist; retrospectives don't exist; model page is thin. Note these absences explicitly in the proposal.
- **Step 3 (depth pages from index) becomes the primary precedent source** — substitute for per-model history.
- **First-principles reasoning from the index's hardware envelope + the blueprint's Phase 0 (substrate sanity) and Phase 1 (cheap memory + precision)** is what shapes the early proposals. Bootstrap candidates often live at Phase 0 or Phase 1, but novel-phase candidates are also allowed.
- **Refuted-pattern check (Step 6) uses Layer A (generic principles) only** — Layer B (per-model refutations) is empty by definition.
- **Proposal flagged as `Mode: bootstrap`** so the master/reviewer knows the precedent grounding is generic-only.

Use bootstrap mode when:
- A new model just entered the autoresearch loop and is being shaken down
- The variant has just been added to the matrix and there's no measured baseline yet
- All earlier ladder rungs (Phase 0, Phase 1) are unvalidated for this variant

## User-override mode — caller-specified candidate

If `<mode>` is `user-override`, the caller has already decided what to try and passed `<user_specified_candidate>`. The skill's job is **validation, not formulation**:

1. Read index + blueprint (Step 2, 2b) — but only to determine which topic the candidate lives in (or to confirm it's novel).
2. Skip Step 3 (depth-page reads) unless the candidate is in a topic with a documented refuted pattern adjacent to the candidate — then read the specific refutation observation page.
3. Check the candidate against:
   - Generic refuted-pattern principles for its topic (Layer A)
   - Per-model refuted patterns IF the per-model refuted-patterns.md exists (Layer B)
   - Semantics-preservation (program.md "What you CANNOT do" — math changes, dropping below bf16, etc.)
   - Phase ordering (is the candidate's phase reachable given saturation of earlier phases?)
4. Emit proposal as **Variant E: user-override** (see Step 7).

If the candidate violates a hard constraint (semantics change, structurally refuted pattern verbatim), surface the violation in the proposal — but the caller's override stands. Recommend an alternative for the caller's consideration; don't auto-abandon.

Total tokens: ~5-15k (vs ~100-260k for full ceremony). Latency: ~1-2 turns of master context.

## Exploration mode — lighter ceremony for hunches + stalled variants + novel directions

If `<mode>` was set to `exploration` in Step 1, the following apply throughout the skill:

- **Steps 3 + 4 are optional**, not mandatory. The catalog-cited depth-page reads and per-model refuted-patterns check can be skipped if the candidate is genuinely exploratory (you're trying X because you have a hunch from a recent profile observation, not because the catalog points at it).
- **Step 6 refuted-pattern check is advisory, not blocking**. If the candidate matches a refuted pattern, surface the match in the proposal — don't auto-abandon. Exploration mode tolerates retrying refuted patterns when the op-point has materially shifted.
- **Profile-less hunches allowed**. If no recent profile exists, exploration mode lets you propose anyway with the proposal explicitly flagged as `Profile-less: yes`.
- **Novel directions are first-class**. Phase and topic fields can be `novel` without justification ceiling — exploration mode exists precisely to probe ideas the catalog doesn't yet cover.
- **Proposal template is 5-line minimum** (see Step 7's exploration variant): hypothesis, what triggered the hunch, what's being explored, falsification criterion, recommended dispatch.
- **Flag the proposal as `Mode: exploration`** so the master/reviewer can weight differently (e.g., accept higher refutation rate in exchange for surface-area coverage).

Use exploration mode when:
- The variant has no measured-best baseline yet (early-stage)
- The variant has stalled at a plateau and the standard ladder has saturated
- You're probing a hypothesis category the wiki doesn't yet cover
- You have a novel direction that doesn't fit any cataloged topic or blueprint phase

Do NOT use exploration mode when:
- The variant has a non-trivial Current best and a regression would be costly (frontier mode is the default for a reason)
- A clear profile-driven candidate exists from the catalog (use the standard path)

---

## Step 2 — Read wiki/model-optimization-index.md in full

Read the **entire** `wiki/model-optimization-index.md`. Don't skim — read it.

Rationale: the file's [cardinal rule](../../wiki/model-optimization-index-regenerate-prompt.md) enforces that every line is hypothesis-generation material — TPU envelope constants, topic mechanism citations, generic principles, refuted-pattern principles, Pallas kernel catalog, reference stacks. There is nothing in it to skip. The downside of selective reads (missing cross-references the TLDR didn't telegraph, tunnel-visioning on TLDR-implied topics) is exactly the v391y-class failure mode this skill exists to prevent.

Reading the full file once at hypothesis time costs ~25k tokens; the master context is 200k+. Cheap relative to the safety it buys.

After reading, identify the **1–3 topic sections** the candidate hypothesis most directly touches, and **note any unexpected cross-references** to other topics (these are exactly the connections the TLDR table won't surface). Capture the topic anchor IDs (e.g. `#ce--softmax-loss`, `#moe-expert-dispatch`) for the proposal.

### Handling novel profile signatures

If no TLDR row matches the profile signal you described in Step 1.5: **do not punt to the caller**. Instead:
1. Describe the signal precisely (which bucket, what %, what's unusual about it).
2. Reason from first principles using the index's hardware envelope (HBM BW, VMEM cap, MXU shape, bytes/flop) + the most-relevant existing topic sections.
3. Propose a hypothesis grounded in that reasoning.
4. Flag the proposal as `Novel-signature: yes` so the master/reviewer knows the precedent path didn't apply, and **file a new TLDR row recommendation in the proposal** — one-line "profile-signature → topic → first-line hypothesis class" — for the next regeneration of the index to incorporate.

The catalog isn't a ceiling; it's a starting set. Novel signatures are where new optimizations come from. Reasoning from first principles + filing the row back is how the catalog grows.

## Step 2b — Read wiki/model-optimization-blueprint.md in full

Read the **entire** `wiki/model-optimization-blueprint.md`. Same rationale as Step 2 — it's lean, every line is operational, and you need full context to apply the phase-ordering rules.

The index and the blueprint are intentionally complementary:
- **Index** answers _"for topic X (CE / sharding / VMEM / flags / …), what's the mechanism and what's been refuted?"_ — topic-keyed lookup.
- **Blueprint** answers _"in what order do I apply optimizations, what compounds, what trap will bite me?"_ — ladder-keyed procedure.

Use the blueprint's ladder (Phase 0 → 6) to identify:
- **The phase the candidate sits at** — one of:
  - Phase 0 (substrate sanity)
  - Phase 1 (cheap memory + precision)
  - Phase 2 (known-good high-yield flag bundle)
  - Phase 3 (kernel / structural code work — biggest wins, 2-30×)
  - Phase 4 (batch + sequence amortization)
  - Phase 5 (cross-variant + cross-generation transfer)
  - Phase 6 (exploratory flag sweep — last resort)
- **Phase saturation**: have all earlier phases been applied for this variant? If Phase 0-1 substrate-sanity / cheap-memory levers haven't been verified, those should usually come BEFORE a Phase 3 kernel rewrite — even when the profile signal points at the kernel. Surface this to the caller.
- **Compounding awareness**: the blueprint documents which earlier phases unlock or remove blocking constraints for later ones (e.g., `xla_tpu_scoped_vmem_limit_kib` unlocks larger Pallas block sizes). If the candidate depends on a not-yet-applied earlier phase, sequence accordingly.
- **Trap awareness**: the blueprint flags specific traps per phase (e.g. "flag sweep last" rule, "silent no-op audit" requirement, "verify the change took effect before drawing perf conclusions"). The candidate must not violate the phase's traps.

If the candidate is genuinely Phase 6 (exploratory flag sweep) but Phase 1–5 are not yet saturated on this variant: the blueprint's "flag sweep last" rule is **advisory** — it reflects the empirical observation that Phase 6 has typically < 1 pp yield. The agent can still propose Phase 6 with a one-sentence justification (e.g., "new libtpu version unlocks this flag, want to validate before committing to Phase 3 kernel work"). The proposal must explicitly note the saturation gap.

**Phase doesn't fit any of 0-6?** Use `Blueprint phase: novel` in the proposal with a one-sentence mechanism description. The ladder is curated from past lessons; novel mechanisms are how it grows.

## Step 3 — Read the depth pages cited under the implicated topics

### Trivial-case short-circuit (skip Step 3 + 4 reads when this fires)

If ALL of the following are true:
- The candidate is a **single flag flip** that already appears verbatim in the index's "Universal multi-host stack" or a named MaxText preset (e.g., `CF_FOR_ALL_GATHER`, `DISABLE_COLLECTIVE_MATMUL`, `HOST_OFFLOAD_FLAGS`), AND
- The profile signal directly implicates the flag (e.g., dominant `all-reduce` bucket + you're proposing the AllReduce-related CF flag), AND
- You're in `frontier` mode (exploration mode also short-circuits — see "Exploration mode" below)

Then you can skip the depth-page reads in Step 3 and the per-model layer in Step 4, and produce a **3-line proposal** instead of the full template. The 3 lines must include: hypothesis (the flag + value), profile signal (1 line), falsification criterion (1 line). Flag the proposal as `Short-circuit: yes`.

Rationale: known-good flag bundles are documented precisely because they're low-risk + low-novelty. Walking the full ceremony for "set the flag the index says to set" is pure overhead.

### Otherwise — read the cited depth pages

For each of the 1–3 implicated topics identified in Step 2, the topic's **Mechanism** subsection in the index lists specific cited concept + observation + source pages. **Read those pages directly** — they are the depth content for the topic.

Use the Read tool for each cited path. The catalog already did the filtering work: by listing them under the topic's Mechanism, the index is telling you these are the relevant pages for this topic. No further filtering is needed; no subagent indirection is needed.

Selectivity guidance within a topic's citation list (so context doesn't balloon unnecessarily):
- **Always read** any observation page in the citation list — observations document failure modes specific to this project where exact wording matters most (e.g., the precise canonical pattern, the exact deadlock condition).
- **Always read** any concept page named as canonical (e.g., the index will mark "canonical" pages explicitly, or they'll be the only concept page for a load-bearing primitive like `shard_map`, `segment-matmul-pallas-kernel`, etc.).
- **Read by default** concept pages that the index's one-line description marks as load-bearing for the candidate's mechanism. If the description tells you the page isn't load-bearing for your specific candidate (e.g., a v6e-only nuance when you're on v5p), skip it.
- **Do not cascade** — when a depth page references further depth pages, do NOT follow those references. The catalog's curation stops at one level.

Source pages (papers, docs) — read these for foundational understanding when the candidate involves a kernel/architecture variant the wiki has ingested as a source (NSA, FA3, TyphoonMLA, etc.). The catalog will tell you when.

For each cited page read, note: principles, refuted patterns, cross-references to other topics, specific code patterns. Carry forward into the proposal in Step 7.

**Context-cost honest expectation**: a typical topic's Mechanism cites 5-10 pages; 1-3 topics × ~5-10 pages × ~5k tokens each = ~30-150k tokens read into master context per hypothesis. This is the right cost — the agent needs source material to formulate a quality hypothesis; the catalog already filtered to the most relevant material; adding a summarizer middleman would only reduce fidelity without reducing real cost.

## Step 4 — Read the per-model refuted-patterns layer (if it exists)

Read `wiki/experiments/<model>_autoresearch_optimization/refuted-patterns.md` if the file exists.

This is the per-model layer — it lists specific experiment IDs (e.g. `v391y on 3B/v5p-16`) that refuted a pattern with the variant + measured regression. If the file doesn't exist for this model, that's fine — note this and continue.

If the file exists but doesn't have an entry for the topic in scope: that's also fine — the topic may genuinely have no prior refutations on this model.

## Step 5 — Read the lane log + most recent retrospective FIRST + model page + last 3 experiments

Read in this order. The retrospective is the highest-density single input — read it FIRST when fresh.

### Step 5a — Most recent retrospective for THIS `(model, lane)` (read FIRST when fresh)

Search `wiki/analyses/` for `*<model>*<lane>*retrospective*.md`, take the newest. If it exists AND its `updated:` (or filename) date is within the last 6 hours, it is **fresh**; in that case:

- Read it in full
- Extract the `## Recommended next directions` table. The top 3 entries are **candidate proposals** for THIS hypothesis-formulation invocation. Add them to your candidate set with `source: retrospective:<filename>` tagging.
- Extract the `## Experiment ledger` table. Use it to skip redundant per-experiment reads (the retrospective already categorized + verdict-tagged everything).
- Note the retrospective's **Search-strategy assessment** (premature-exhaustion signals): if the retrospective flagged "single-axis-heavy: ratio > 5:1" or "frontier stuck for N+ experiments", **bias the candidate ranking toward kernel/structural work over more single-axis probing**. The retrospective's diagnosis IS evidence.

If the retrospective is **stale** (>6 hours OR not present), proceed normally — read it for context but don't treat it as primary input.

**Step 3 shortcut**: if the retrospective is fresh AND covered the topics your candidate touches, you may SKIP Step 3's depth-page reads for those topics — the retrospective is the synthesized view of that topic-space. Skip only when the retrospective explicitly cites the same depth pages you'd otherwise read (which it typically does in its Sources section).

### Step 5b — Lane log + model page + recent experiments

After the retrospective (or skipping to here if no retrospective), read:

1. **Last 50 lines of the lane's log**: `wiki/experiments/<model>_autoresearch_optimization/<lane>/log.md`. Per SCHEMA's two-tier log convention, the lane's log carries every recent `loop-iteration` + `start` / `stop` markers + manual ops on this lane. If the file doesn't exist, this is a new lane — skip and proceed.
2. `wiki/models/<model>-<lane>.md` — focus on the variant matrix row for `<variant>`, the "Cross-variant open hypotheses", and "Retired hypotheses" sections.
3. The last 3 experiment pages under `wiki/experiments/<model>_autoresearch_optimization/<lane>/` — what was just tried with verdicts. **If a fresh retrospective ALREADY covered these in its ledger, you may skip the deep read and use the retrospective's summary** (cite which retrospective row).
4. **Fallback for "most recent retrospective" search** — if Step 5a didn't find one for THIS lane, search wider:
   ```
   ls wiki/analyses/ | grep -E "<model>.*<lane>.*(retrospective|synthesis|day-summary|session-summary)" | sort -r | head -1
   ```
   If that returns nothing, also try the cross-lane retrospectives matching the model only (these capture lessons that span lanes — e.g. `*<model>*cross-lane*retrospective.md`).
   Read just the **single most recent** retrospective found. The newest retrospective is the freshest synthesis and typically references earlier ones if relevant — no need to load multiple. If none exist for this model+lane, note that and continue.
   
   Why this matters: retrospectives are the highest-density distillation of hard-won lessons across a multi-day or multi-experiment chunk of optimization work. They surface compounding patterns, near-miss refutations, and cross-cutting traps that the model page's variant matrix + per-experiment pages don't capture in one place. The blueprint's ladder is partly derived from retrospectives; reading the latest one catches model-specific nuances the blueprint generalized away.

These are the **per-model state** (vs the index/blueprint generic state). Together with Step 4's per-model refuted-patterns.md, they give the master the model-specific picture.

Optional: if the topic-keyword search of `wiki/observations/` surfaces an observation page the index didn't cite (the index isn't exhaustive), read that page too. Don't go beyond 1-2 such uncited observations.

## Step 6 — Check candidate against the two-layer refuted set

Compare the candidate hypothesis against:

**Layer A — Generic refuted-pattern principles** from the topic section(s) in Step 3:
- These are model-agnostic traps (e.g. "Reasoning about kernel cost from FLOPs alone"; "Auto-partitioning a Mosaic kernel"; "Same-axis nested collectives").
- If the candidate violates any of these principles → **abandon the candidate**. Pick a different angle.

**Layer B — Per-model refuted experiments** from Step 4 (refuted-patterns.md) + the model page's "Retired hypotheses" section + the last-3-experiments' verdicts read in Step 5:
- If the candidate matches a per-model refuted experiment verbatim → **abandon the candidate**.
- If the candidate is a *variant* of a refuted pattern (different op-point, different scale, different hardware row) → either explicitly cite why the prior refutation should not apply at the current op-point, OR pick a different candidate.
- If the candidate is genuinely orthogonal → proceed.

This step is the single biggest safeguard against repeat-failure-mode regressions. Do not skip.

## Step 7 — Produce the structured proposal

Five template variants — pick by mode + short-circuit status. Listed default-first:

### Variant A: Frontier (full)

The default. Used when `<mode>` is `frontier` and the trivial-case short-circuit (Step 3) didn't fire.

```
HYPOTHESIS PROPOSAL
===================
Model:     <model>
Lane:      <lane>
Variant:   <variant from Step 1>
Mode:      frontier
Novel-signature: <yes/no — yes if Step 2's novel-signature handler fired>
Topic:     <model-optimization-index section anchor(s) — OR 'first-principles'
            if no cataloged topic fits cleanly; OR 'novel-mechanism' if the
            candidate is a genuinely new optimization direction>

Hypothesis: <one sentence, falsifiable>

Blueprint phase: <0-6 OR 'novel'>
  If a numbered phase 0-6:
    Phase name: <e.g. "Kernel + structural code work">
    Earlier phases saturated for this variant? <yes / partially / no — list gaps>
    If unsaturated earlier phases exist AND they would unlock or block this
    candidate, recommend running that first — OR override with one-sentence reason
    (e.g., "Phase 1 not saturated but candidate is independent of memory pressure").
    Trap-awareness check (from blueprint's per-phase guidance):
      <e.g. "verify change took effect via silent-noop audit before drawing perf
      conclusions">
  If novel (doesn't fit existing 0-6 ladder):
    Mechanism (one sentence): <e.g. "exploits v7x SparseCore offload via new flag X">
    Why no existing phase fits: <one sentence>
    Self-consistency check: does this respect program.md invariants
    (no semantics change, no quality regression)? <yes/no — explain>

Index sections consulted:
  - wiki/model-optimization-index.md#<topic-anchor-1>
  - wiki/model-optimization-index.md#<topic-anchor-2>   (if multiple)
  - wiki/model-optimization-index.md#tpu-hardware-envelope (for <hw-gen>)

Blueprint sections consulted:
  - wiki/model-optimization-blueprint.md#tldr--the-ladder
  - wiki/model-optimization-blueprint.md#phase-<N>-<name>

Depth pages read directly (catalog-chosen from implicated topics):
  - wiki/<concept-page-1>
  - wiki/<observation-page-1>
  - wiki/<source-page-1>
  - ...

Per-model state consulted:
  - wiki/models/<model>-<lane>.md (variant matrix row + retired hyps)
  - last 3 experiment pages: <list>
  - most recent retrospective/synthesis: <path>
    ( OR: "no retrospectives found for this model+lane yet" )
  - per-model refuted-patterns.md (if exists)

Generic-principle checks (from index topic):
  - <principle 1> — pass / fail / not-applicable
  - <principle 2> — pass / fail / not-applicable
  - ...

Per-model refuted-patterns checked:
  Layer file: wiki/experiments/<model>_autoresearch_optimization/refuted-patterns.md
  ( OR: "no file yet for this model — using variant matrix retired-hypotheses + last 3 experiments" )
  - <refuted v-id 1> — <why this candidate is not that experiment>
  - <refuted v-id 2> — ...
  - <or: "no prior refutations in this topic on this model">

Profile signal (the bucket this targets):
  <bucket name>: <% of step from most recent profile, citing experiment ID>
  <if no profile available> "no profile yet for this variant — recommend
  capturing one BEFORE committing to this hypothesis"

Falsification criterion:
  <metric + threshold that would refute>
  Example: "step MFU does not exceed <current_frontier> + 0.3 pp over
  median of steps 10-50"

Expected gain:
  <pp MFU or % step time>
  <one-sentence reasoning grounded in either a generic principle or a
  measured precedent>

Effort estimate:
  S (flag/recipe), M (per-file model edit), L (multi-day, kernel work)

Risk of refutation:
  <low/medium/high> — <one sentence>

Duplicate-track check:
  In-flight v-IDs: <in_flight_v_ids>
  This candidate vs in-flight: <orthogonal / same-direction-as-Vx>
  ( if same-direction-as-Vx, pick a different candidate )

Recommended dispatch:
  Image: <base image + overlay summary>
  Cluster: <cluster_name>
  Workload slug: <≤10 chars per program.md naming budget>
```

### Variant B: Frontier (short-circuit, 3-line)

Used when the trivial-case short-circuit fired in Step 3.

```
HYPOTHESIS PROPOSAL (short-circuit)
===================================
Model: <model>, Lane: <lane>, Variant: <variant>
Mode: frontier
Short-circuit: yes

Hypothesis: <flag name>=<value> from <named bundle or index recipe>
Profile signal: <bucket>: <%> from <exp id>
Falsification criterion: <metric + threshold>

Recommended dispatch:
  Image: <base + overlay>
  Cluster: <cluster_name>
  Workload slug: <≤10 chars>
```

### Variant C: Exploration (5-line minimum)

Used when `<mode>` is `exploration`. Phase + topic fields are advisory only; novel directions are first-class here.

```
HYPOTHESIS PROPOSAL (exploration)
=================================
Model: <model>, Lane: <lane>, Variant: <variant>
Mode: exploration
Profile-less: <yes/no>

Hypothesis: <one sentence>
Hunch trigger: <e.g. "noticed N% growth in data formatting last exp"
                 OR "novel direction — wanted to probe X regardless of catalog">
What this explores: <open question this answers — can be outside any
                     cataloged topic>
Blueprint phase: <0-6 OR 'novel' OR 'n/a — exploration'>
Falsification criterion: <metric + threshold>
Refuted-pattern proximity: <none / matches X (advisory only)>

Recommended dispatch:
  Image: <base + overlay>
  Cluster: <cluster_name>
  Workload slug: <≤10 chars>
```

### Variant D: Bootstrap (new model, thin state)

Used when `<mode>` is `bootstrap`.

```
HYPOTHESIS PROPOSAL (bootstrap)
==============================
Model: <model>, Lane: <lane>, Variant: <variant>
Mode: bootstrap
Per-model state available:
  Variant matrix rows: <N>
  Per-model refuted-patterns.md: <yes / NO>
  Retrospectives: <count, or NONE>
  Last 3 experiments: <count, or fewer>

Blueprint phase: <0 / 1 typical for bootstrap; OR novel>
  Earlier-phase saturation: <typically N/A — first run on this variant>

Hypothesis: <one sentence, grounded in index hardware envelope +
              blueprint Phase 0/1 guidance, or first-principles if novel>

Generic-principle checks (Layer A only — Layer B not yet populated):
  - <principle 1>: pass / fail / N/A
  - ...

Profile signal: <bucket: % from first capture, or "no profile yet — recommend
                  capturing one as the first bootstrap experiment">
Falsification criterion: <metric + threshold>

Recommended dispatch:
  Image: <base + overlay>
  Cluster: <cluster_name>
  Workload slug: <≤10 chars>
```

### Variant E: User-override (validation-only)

Used when `<mode>` is `user-override`.

```
HYPOTHESIS PROPOSAL (user-override / validation)
================================================
Model: <model>, Lane: <lane>, Variant: <variant>
Mode: user-override
Candidate (caller-specified): <one sentence>
Topic (inferred): <model-optimization-index section anchor OR 'novel'>

Validation checks:
  Generic refuted-patterns (Layer A): pass / fail — <which principle>
  Per-model refuted-patterns (Layer B): pass / fail / no file yet
  Semantics-preservation: pass / fail — <which invariant violated>
  Phase ordering: <phase>; earlier-phase saturation: <yes/no — what's missing>

Profile signal: <bucket: % if available — or "no profile, caller asserted">
Falsification criterion: <metric + threshold>

Recommended dispatch:
  Image: <base + overlay>
  Cluster: <cluster_name>
  Workload slug: <≤10 chars>

If a check failed, also emit:
  Note: <surface the failure but caller's override stands; recommend
         alternative for caller's consideration>
```

## Step 8 — Return to caller

Hand the structured proposal back to the loop. The loop then:
- Validates the workload-name length per program.md
- Constructs the gke-cluster-runner dispatch prompt
- Calls Agent(subagent_type="gke-cluster-runner", run_in_background=true, ...)

If the proposal is incomplete (e.g. profile-signal field says "no profile yet"), the loop should redirect — capture a profile first, then re-invoke this skill.

## Failure modes to handle

- **model-optimization-index.md doesn't have a TLDR row matching the profile signal**: do NOT punt to the caller — use Step 2's novel-signature handler (reason from first principles, flag `Novel-signature: yes`, file a new TLDR row recommendation in the proposal).
- **model-optimization-blueprint.md doesn't have a phase that fits the candidate**: use `Blueprint phase: novel` in the proposal with a one-sentence mechanism description + justification. The ladder is a curated starting set, not an exhaustive enumeration; genuinely new mechanisms are how it grows.
- **Phase 6 (exploratory flag sweep) proposed while earlier phases not saturated**: advisory only. The blueprint's "flag sweep last" rule reflects empirical low-yield, but the agent can override with one-sentence justification (e.g., "new libtpu version unlocks this flag, want to validate first"). The proposal must explicitly note the saturation gap so reviewer can decide.
- **Candidate depends on an earlier phase that's not applied yet** (e.g. Phase 3 kernel depends on Phase 2's `xla_tpu_scoped_vmem_limit_kib`): surface the dependency; recommend the prerequisite first.
- **Per-model layer (Step 4 + Step 5's model-page Retired hypotheses) returns no relevant refutations**: that's fine for young topics on a model. Record this fact in the proposal ("Per-model refuted-patterns checked: none documented yet for this topic on this model") and proceed.
- **Multiple candidates all match either layer's refuted set**: surface to caller. Recommend either (a) jumping to a different topic (use the loop's priority order: profile-driven > follow-up > cross-lane gap > Pallas opportunity), or (b) re-examining whether one of the per-model refutations is no longer applicable at the current op-point (different hardware row, different lbs, different libtpu version).
- **Caller asks for an idea but session context is thin**: ask the caller for the current frontier + most recent experiment verdicts + recent profile before proceeding.
- **Per-model refuted-patterns.md doesn't exist for this model yet**: that's expected for new models. Use the model page's variant matrix "Retired hypotheses" + last 3 experiment pages as the Layer B source instead. Optionally surface to the caller that creating the file would help future iterations.

## Anti-patterns

- ❌ **Selectively reading** model-optimization-index.md or model-optimization-blueprint.md by topic — both files are kept lean by design (the index's cardinal rule + the blueprint's procedural focus). Reading them in full is the safety guarantee against TLDR-tunneling. The cost is ~40k tokens once per hypothesis; the cost of missing a cross-reference is a v391y-class regression. Always read both in full.
- ❌ **Skipping the blueprint** and proposing only from the index — you lose phase ordering, compounding awareness, and the "flag sweep last" rule. The index and blueprint are complementary and BOTH are required.
- ❌ **Proposing a Phase 6 exploratory flag sweep while Phase 1–5 are not saturated** — the blueprint's empirical rule says this is the lowest-yield activity (most sweeps flat or refuted). Recommend the highest unsaturated phase instead.
- ❌ **Cascading reads beyond catalog filter** — when a depth page references further depth pages, do NOT follow those references. The index's Mechanism subsection is the curated, one-level set. Going further explodes context for diminishing fidelity.
- ❌ **Dispatching a subagent to summarize the catalog's already-filtered citation list** — the index is the filter. The cited pages ARE the depth content master needs. Adding a summarizer middleman reduces fidelity without reducing real cost.
- ❌ Skipping Step 6 (refuted-pattern check) on either layer — the canonical failure mode.
- ❌ Inventing a hypothesis without reading the TLDR first — you'll often pick a topic that the profile doesn't actually implicate.
- ❌ Returning the proposal without filling the "Blueprint phase", "Generic-principle checks" or "Per-model refuted-patterns checked" fields — these are mandatory; an incomplete proposal must be rejected by the caller.
- ❌ Treating Layer A (generic principles) as exhaustive — they're necessary but not sufficient. Always also check Layer B (per-model refuted experiments).
- ❌ Asking the user to do research the skill should be doing (e.g. "what do we know about X?" — the answer is in the index + blueprint + depth pages; read them).
