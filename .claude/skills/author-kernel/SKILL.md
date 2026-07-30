---
name: author-kernel
description: Authoring discipline for kernel-family candidates (the author role of kernel_experiments/program.md step K4). Load BEFORE writing any kernel candidate — whether you are a solo agent running the whole K0–K9 loop (production: Gemini / Claude / Codex from a bare prompt) or a dispatched author process in the trial topology. Covers the pre-authoring checklist, the BLOCKING early-kill gate (interpret parity + firing check on cand1's skeleton before any plan item), escalation ladder + class-pivot, interpret-first parity tiers, gotcha-first compile debugging, canonical timing, chip discipline, commit-each-candidate grammar, the declared-candidate-plan stop rule (flat, pre-registered — no open-ended inner loop), and the candidate-ledger output contract. NOT for model-lane code edits (use /edit-model-code), NOT for verification (K6 is independent of the author), NOT for wiki-page writes.
---

You are about to author kernel candidates for one kernel-family experiment. Read this end-to-end and keep it in scope while authoring.

**The role boundary (from the Roles invariant, kernel_experiments/program.md):** while authoring, you write candidates; you NEVER produce the evidence a verdict cites. Your own timing/parity numbers exist to steer iteration — label them **author-side**. The verdict evidence (independent re-measure, parity re-check, firing audit, capture) comes from the K6 verification step, which is independent of the author by construction: a `kernel-verifier` dispatch when the harness supports it, otherwise the fresh-process full-mode re-verification the process defines. This holds in solo mode too — the same agent later runs K6/K7, but authoring-phase numbers never graduate into verdict numbers. The falsification bar is public and pre-registered: you know exactly what you must beat; you just don't grade yourself.

## Before authoring — the checklist (assemble it yourself in solo mode; it arrives as a brief in dispatched mode)

All of these must exist before the first candidate. Solo mode: you produced them at K1–K3. Dispatched mode: they are pasted in your brief — if one is missing (including required reading), refuse and name it; do not improvise paths.

| Item | What it is |
|---|---|
| reference module | the family binding's parity oracle (`create_inputs` + `workload` contract = op-point definition + reference semantics) — an existing reference impl in the home repo, the pinned pre-optimization version of the target, or the suite's `baseline.py` for benchmark families. **Never edit it.** |
| target path | the kernel file(s) at their **real ship path** in the home repo (from the family binding) — existing kernels edited in place, new kernels born at their ship path; NOT a scratch `optimized.py` |
| work dir | the family worktree `wiki/kernel_experiments/<slug>/pallas/.repo/` on branch `kernel/<slug>-vNNN` (K4 creates it if missing). Everything you write goes here, nothing outside. The shared `raw/code/<home_repo>` checkout is the worktree PARENT only — no branch operations in it, ever; never sit on another family's branch (program.md Setup isolation invariants). |
| diagnosis | the K1 bound diagnosis: what the naive materializes, the bound, the **predicted intervention class** (`refute|flag|xla-rewrite|kernel-authored`) + HLO evidence |
| falsification bar | pre-registered in the K3 stub (e.g. "p50 beats naive by >2% AND 3σ") |
| `parity_spec` | atol/rtol or bit-exact, from the family `program.md` |
| chip + lock | `TPU_VISIBLE_DEVICES=<n>`; wrap every device execution in `flock /tmp/tpu-chip-<n>.lock` (held around the run only, never around editing/compiling) |
| required reading | the kernel index's category strategy + class table/ladder, `concepts/pallas-kernel.md` mechanics (memory spaces, the (8,128) rule, gotcha table), `BRIEFS.md` earned rules, the canonical timing helper. Solo: read the pages. Dispatched: pasted content. |
| `activity` | `optimization` or `capability-eval` + any constraints (e.g. a no-peek list) |
| candidate plan | the enumerated plan from the K3 stub — the concrete candidate list you will execute (mechanism implementation + named tile-sweep points + named structural alternative, or a pure TUNE sweep). The falsification bar is the verdict bar; **the plan is the stop rule** |

**Required-reading attestation:** your FIRST candidate-ledger line is `loaded: [<sections read>]`. A ledger without it caps the experiment's verdict at `inconclusive` (LINT-enforced). The reading exists to prevent the compile-fix churn that eats authoring budgets — the 2026-07-11 benchmark lost 6/8 problems to authors who skipped it.

## Procedure

0. **EARLY-KILL GATE — BLOCKING, before ANY plan item (~5 min).** First authoring action: a
   minimal cand1 skeleton that (a) passes `interpret=True` parity on the tiny shape (free, no TPU)
   AND (b) provably FIRES — custom_call present in the lowered HLO (`kgate verify --mode screen`
   firing audit, or one compile + HLO grep). Until both pass: no sweeps, no timing, no plan items.
   Can't pass within the budget ⇒ dead-on-arrival: class-pivot / refute path (rule 1; solo mode: a
   new K2), never iteration on a broken base — the gate kills a broken-from-the-start kernel in
   minutes instead of hours.
1. **Attack the predicted intervention class first.** Escalate one rung up the cost ladder (`flag → xla-rewrite → kernel-authored`) only when the current class's best candidate fails the bar; record every escalation in the ledger with the reason. **Class-pivot rule:** if the predicted class is *dead* (compiler wall after the retry guard, dispatch-floor confirmation), do NOT silently swap classes — record a `class-pivot` (evidence + recommended class) and restart authoring under the new class with a fresh hypothesis (solo mode: that is a new K2). A silently-swapped class produces a mechanism-absent no-op the verification will refute anyway.
2. **Authoring against the diagnosis** (e.g. a Pallas kernel where the dispatch-floor prior says it loses) is allowed only within the knowledge-purchase budget (15 min unless the family program.md says otherwise) — the deliverable is then the measured refutation, not the kernel.
3. **Correctness before speed:** parity on a tiny shape first, **in `interpret=True` mode before any TPU compile** (hard gate — a candidate that never ran interpret-mode cannot be submitted; it is free and catches indexing/masking/grouping bugs that hide until a boundary case; rule 0 already enforced this on cand1's skeleton — this rule extends it to EVERY candidate), then on-TPU tiny shape, then the full op-point. Structure before tiling before flags; sweep block sizes only on a structurally-settled kernel. `pl.BlockSpec` index_maps return the BLOCK INDEX, not the element offset.
3.5 **Tool failure has an honorable exit — never a paper substitute.** A failed kgate/tool
   invocation is retried with corrected args (≥2 attempts, the error pasted into the page). If it
   still fails, file the experiment `BLOCKED — tooling` with the error transcript — a legal,
   respectable outcome. Filing `verified`/`supported` without an existing receipt is fabrication
   and is voided on audit.
4. **Gotcha-first on compile errors.** When a compile error matches a row of the gotcha table in your required reading (dynamic_slice, `pl.VMEM` vs `pltpu.VMEM`, `_check_block_mappings`, scoped-VMEM OOM, `pl.ANY` indexing, sub-tile matmul operands, …), apply that row's fix — no trial-and-error. Record which row fired in the ledger's why-column; an error matching no row is worth reporting (it becomes a new row).
5. **Time candidates with the canonical helper (kgate / the BRIEFS timing helper), verbatim** — cite numbers only from a saved receipt. Never hand-roll timing (unblocked async dispatch produced a 40× phantom speedup in the 2026-07-11 benchmark). Measure in the **graded dtype (bf16)**. All such numbers are "author-side". **Mode: verify intermediate/sweep candidates with `--mode screen` (fast — parity + firing audit + measure, no cold both-orderings capture); reserve `--mode full` for the one candidate you are about to bank as the frontier and the family-closing result.** Running full-mode on candidates you are still iterating is wasted wall-clock; screen still catches parity failures and silent no-ops (both gates run in both modes).
6. **Chip discipline:** every device execution under `flock` on your chip lock; at most 2 concurrent XLA compiles; one retry of a 137-killed compile before declaring a wall (which triggers rule 1's pivot path). Run synchronously — no background/poll patterns.
7. **COMMIT EACH CANDIDATE — mandatory, before the next one overwrites the kernel file.** One commit per ran-on-TPU candidate, grammar `cand<N>(<fam> vNNN): <what changed> — <p50/speedup/parity>` — self-check against the regex `^cand[0-9]+\([a-z0-9-]+ v[0-9]{3}\): .+ — .+` before committing — losers and rejected attempts included. Never overwrite an un-committed candidate and never replace your best kernel with a refute comment — a lost candidate is an unverifiable claim; K7 caps a multi-row ledger sitting on a fewer-commit branch at `inconclusive`. Keep the worktree ON its branch, never detached. `exp:` footer on the final commit.
8. **Respect `activity` constraints absolutely.** Under a `capability-eval` no-peek list: never open/grep/import any listed reference implementation; confirm compliance explicitly in your report.
9. **Stop rule = the declared candidate plan, executed in full — not first-win, not a clock, not your judgment.** Run every plan item, one commit each; done = plan exhausted. The plan already contains the anti-first-win substance (tile sweep + structural alternative), so a first-win stop leaves plan items visibly un-run — which caps the verdict. **Extensions** beyond the plan are allowed only with a recorded reason in the ledger (e.g. "cand4 OOM'd → added 1536"; "post-win refinement of the sweep optimum"). **Any idea you notice but don't pursue MUST appear as a named lead in your final report** — it seeds the next experiment; never leave it in your head.

## Output contract — the authoring phase ends with exactly this

(Solo mode: this is what flows into the experiment page's `## Candidate ledger` and the K6 verification input. Dispatched mode: this is your return message.)

1. **Candidate ledger** — a fixed-column table, one row per attempt INCLUDING failures and abandoned kernels, first line the `loaded:` attestation:
   `| candidate | class | committed SHA | parity (max abs / max rel) | p50 ms (author-side) | vs naive | receipt | why kept/rejected |`
   The `candidate` id matches the stub's `## Candidate plan` item (`candN`); the `receipt` column is the **saved kgate receipt path** (`-o` file) the row's numbers come from — **a row without a receipt path is unverifiable and caps the experiment at `inconclusive`**.
2. **Final candidate:** path under the work dir + its commit SHA + a one-paragraph mechanism description (what it does differently and why that attacks the diagnosed bound — name only mechanisms you actually implemented).
3. **Escalations + knowledge purchases:** what, why, minutes spent.
4. **Honest blockers:** what you couldn't reach before the stop rule fired, and any discrepancy between your results and the diagnosis's prediction.
5. **Compliance line** (when `activity` carried constraints): confirm each was obeyed.

## What authoring does NOT include

- No `## Profile` / `## HLO Dump` / firing-audit content, and no trace/LLO capture — K6's verification owns all of it.
- **Never `git add` (or force-add) anything under `raw/profiles/` — it is gitignored by design (multi-GB traces/HLO dumps).** The durable, citeable evidence is the small **`receipt.json`** (self-hashed, carries the digest); cite its path. Traces/HLO dumps stay on disk, out of git. Force-adding a trace once put a 149 MB blob in history and blocked all pushes (2026-07-21).
- No verdict language — candidates are reported against the bar; `supported`/`refuted` is assigned at K7 on the verification's evidence.
- No edits outside the family work dir; no edits to the reference module or any reference implementation; no wiki-page writes during authoring.
- Author-side timings never presented as final results.

## See also

- [`wiki/kernel_experiments/program.md`](../../../wiki/kernel_experiments/program.md) — the K0–K9 loop this skill's step (K4) belongs to.
- [`wiki/kernel-optimization-index.md`](../../../wiki/kernel-optimization-index.md) — intervention classes, category strategy, Load mandate.
- [`wiki/concepts/pallas-kernel.md`](../../../wiki/concepts/pallas-kernel.md) — authoring mechanics + gotcha table. [`wiki/kernel_experiments/BRIEFS.md`](../../../wiki/kernel_experiments/BRIEFS.md) — earned rules + the canonical timing helper.
