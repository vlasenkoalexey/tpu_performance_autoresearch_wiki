---
name: formulate-kernel-hypothesis
description: Generate ONE structured kernel-optimization hypothesis — step K2 of wiki/kernel_experiments/program.md. Self-contained for the kernel lane (any harness, bare-prompt solo or dispatched): reads the K1 bound diagnosis + the kernel index's signal→lever map + the family's refuted layers, and returns a proposal with the mandatory kernel fields (intervention class w/ HLO evidence, op-point provenance or capability-eval, kernel-vocabulary predicted signals, parity-gated falsification bar vs the FRONTIER, and the enumerated candidate plan that becomes K3's checkbox list). NOT for model lanes — those use /formulate-hypothesis (index+blueprint machinery, phase ladder, variant matrices).
---

You are formulating ONE kernel-optimization hypothesis (K2). The output is a structured proposal
the master reviews and files as the K3 stub. Do not skip steps; do not formulate inline without
this skill.

## Step 1 — Gather inputs (most were just produced at K0/K1)

- **The K1 bound diagnosis** — the primary signal: the confirmed bound (memory / compute /
  dispatch), the HLO-confirmed sink structure (never the analytic guess — BRIEFS §1.5), the
  reference-envelope classification (inside / at / outside), and the naive's LLO digest
  (`get_llo_fit_summary`: spills/bundle, per-unit %util, top stalls).
- **The previous experiment's `## Headroom leads`** (verifier-authored) and the family page's
  *Variant-specific open hypotheses* — in the steady state, the hypothesis IS usually the top
  un-pulled lead. Pursuing a retrospective's recommendation (exploration mode) overrides.
- **The family frontier**: best verified p50 + its mechanism (family page Current best row).
- [`retrospectives-digest.md`](../../../wiki/kernel_experiments/retrospectives-digest.md) TLDRs +
  the family's `refuted-patterns.md` if it exists.

### Step 1.5 — describe the signal in your own words BEFORE reading the index

Two sentences: what is slow, and what the LLO/HLO evidence says binds it. Written *before* the
index read, so the index informs rather than anchors (anti-TLDR-tunneling).

## Step 2 — Read `wiki/kernel-optimization-index.md` IN FULL

The kernel lane's single catalog: the **signal→lever map** (the phase-ordering analog — there is no
blueprint in this lane), the **intervention-class table** + escalation ladder, the **"When NOT to
Pallas"** principles, category strategy, and the Load mandate (what K4's author must have read).
Full read, no TLDR-skimming — the map's cross-references are the point.

## Step 3 — Check the candidate against the refuted layers

- **Layer A** — the index's refuted principles (dispatch floor, op-point mismatch, XLA-already-fused).
- **Layer B** — the family's own `refuted-patterns.md` + the digest's refuted TLDRs: name the
  nearest refuted neighbor and say why this proposal is different, or drop it.
- **Frontier-bar rule (v002+):** the falsification bar is the family FRONTIER (best verified p50),
  never the naive — matching the frontier within noise is `inconclusive` even if it beats naive.

## Step 4 — Produce the structured proposal (all fields mandatory)

1. **Hypothesis** — one falsifiable sentence.
2. **Mechanism** — what changes structurally and why that attacks the K1-diagnosed bound. Pins
   structure (grid, blocking axes, memory strategy); tuning values stay free.
3. **Predicted signal** — kernel vocabulary, unit-level (`spills/bundle → <X`, `MXU util +N pp`,
   `wait_ratio < X`, `kernel µs −N%`, `roofline util +N pp`). "Kernel time drops" alone is
   under-specified.
4. **Falsification criterion** — beats the bar (frontier at v002+; naive at v001) by >N% at 3σ,
   **AND parity PASS at the family spec** (parity failure ⇒ `inconclusive`/`invalid`, never `refute`).
   **Calibrate `N` from the K1 bound diagnosis — never aspirational.** The bar is the improvement the
   roofline/dispatch analysis says is *reachable*, not a round number you'd like. On a dispatch-bound
   or near-roofline shape where K1 implies only ~1.2–1.3× is physically available, setting a 2× bar
   guarantees a `refuted` verdict AND discards the real correct+firing win the kernel does achieve
   (a 1.225× kernel filed `refuted` against an unreachable 2× bar — 2026-07-21 paged-attention). Set
   the bar at the reachable ceiling so a genuine win registers as `supported`; if K1 says the naive
   is already at its floor, the honest hypothesis is a `refute`, not an aspirational speedup target.
5. **Intervention class** — `refute | flag | xla-rewrite | kernel-authored`, justified by the HLO/
   roofline evidence (what the naive materializes; whether XLA is fusion-complete; dispatch-floor
   proximity). The author attacks this class first; escalation is recorded; class-death → pivot.
6. **Op-point provenance** — decided by where the op-point CAME FROM, not preference:
   name the model-lane experiment that produced this operating point ⇒ `activity: optimization`;
   a benchmark-suite op-point (JAXBench, tokamax bench) or demo has no model profile ⇒
   `activity: capability-eval` (barred from frontiers). A JAXBench sweep is `capability-eval`;
   only claim `optimization` when you can cite the model profile the op-point was attributed from.
7. **Candidate plan** — the enumerated checkbox list that becomes K3's `## Candidate plan` verbatim:
   the mechanism implementation, the named tile-sweep points (toward the VMEM wall), and ≥1
   structural alternative — or the value list for a pure TUNE sweep. A proposal without a concrete
   plan is under-specified (decision record: 2026-07-21-flat-candidate-plan-decision).
8. **Expected gain × confidence / effort** — gain grounded in the envelope (never below the
   compute floor), confidence from the evidence tier, effort in candidates.
9. **Refuted-check line** — layers consulted + nearest refuted neighbor + the distinguishing factor.
10. **Class-lever coverage table** — MANDATORY, and keyed to the *enumerated entries* of your routed
   class page's `## Levers (verified)` list. One row per lever entry, verbatim entry name, marked:
   - `tried@vNNN` — an experiment or candidate cites it (give the v-number),
   - `ruled-out` — plus a one-line argument against the lever's **MECHANISM at this op-point**
     ("no serial compute chain exists", "H_q == H_kv so nothing is shared"). Per K9's standard, one
     failed implementation route rules out **that route, not the lever** — a lowering error or a
     compile failure is NOT a rule-out,
   - `untried` — plus the reason it is being deferred this experiment.

   **Two hard constraints on this table:**
   - **Consecutive-lever limit.** If the previous **two** experiments both attacked the *same class-page
     lever entry* as the one you are about to propose, you may not propose it a third time. The next
     hypothesis must cite an `untried` entry, or rule one out on mechanism. Note this is keyed to the
     **lever entry**, never to a self-described "axis" — free-text axis labels are self-classified and
     three consecutive tunes of one lever can always be relabelled as three distinct axes
     (2026-07-27 flex-attention v001–v003: register liveness / tile shape / emission form, all one
     lever, +8.9% then +0.1% then 0).
   - **Bounded deferral.** An `untried` entry may be deferred at most **twice**. On its third
     appearance it must be run as this experiment's mechanism or ruled out on mechanism in writing.

   This is the K9 stop-gate coverage check moved to *selection* time. It was previously computed only
   when a family attempted to close, so a family that never attempted to close was never checked —
   flex ran three experiments without anything asking whether it had covered its class levers, while
   `attention.md`'s **Compact causal grid (live-pair enumeration)** sat untried and its own verifier
   flagged it as untouched.

   **Priming disclosure.** Consulting the class page more aggressively moves a `capability-eval`
   family away from cold authorship — the class page is accumulated priors from earlier campaigns
   (compact-causal-grid was harvested from a codex flash run). Any result produced under this rule is
   **class-page-primed, not cold**, and must be tagged as such wherever it is compared against cold
   arms (see the cold/primed legend in the combined kernel scoreboard).

## Modes

- **Frontier (default):** full fields, pursuing the top headroom lead.
- **Exploration** (post-retrospective, or leads look dry): pursue the retrospective's ranked
  recommendation; same fields, confidence may be `low`, class may be speculative — say so.
- **User-override:** the caller has decided what to try. Validate, don't veto: run Steps 2–3 on it,
  produce the full proposal (incl. plan) around the user's candidate, and surface any refuted-layer
  hit or envelope violation as a flagged risk, not a refusal.

## Return

The proposal only — the master (or the solo agent wearing the master hat) files it as the K3 stub
and commits. No wiki writes from this skill.

## Anti-patterns

- Proposing model-lane machinery: blueprint phases, knobs-matrix transfers, MFU targets — wrong
  lane; if the situation genuinely needs a model-lane experiment (K8 upward validation), say so.
- A bar vs naive on a v002+ experiment (verdict inflation — measured 2026-07-12).
- A plan without the tile sweep + structural alternative (re-opens stop-at-first-win).
- A predicted signal with no unit-level signature (unauditable by the firing audit).
- Skipping Step 1.5 and letting the index TLDRs pick the topic (the v391y-class failure).

## Sources

- [`wiki/kernel_experiments/program.md`](../../../wiki/kernel_experiments/program.md) — K1/K2/K3 (the caller).
- [`wiki/kernel-optimization-index.md`](../../../wiki/kernel-optimization-index.md) — the catalog + Load mandate.
- [`wiki/kernel_experiments/BRIEFS.md`](../../../wiki/kernel_experiments/BRIEFS.md) — §1.5 K1 diagnosis rules, §2 author discipline.
- `/formulate-hypothesis` — the MODEL-lane counterpart (index + blueprint + variant machinery).
