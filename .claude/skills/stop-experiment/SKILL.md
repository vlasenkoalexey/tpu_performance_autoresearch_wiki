---
name: stop-experiment
description: Stop the autoresearch optimization loop cleanly. Disarms the launch-armed process watcher, cancels pending wakeups, reaps orphan workloads on the project's cluster pool, files any missing experiment pages, runs lint, and appends a clean-shutdown marker to wiki/log.md. Invoke at the end of an autoresearch session.
---

You are stopping the autoresearch loop cleanly. Follow this sequence — do not abbreviate.

## Step 1 — Stop the loop

### Step 1·0 — Final audit gate (BLOCKING — before the watcher is disarmed)

You are the agent the watcher supervises; you may not end your own supervision unaudited. Dispatch the [`process-auditor`](../../agents/process-auditor.md) SYNC over the closing delta (the stop/at-ceiling claim, retrospective, and evidence table included). Then:

- **`stop blocked` / FABRICATION finding** → **ABORT `/stop-experiment`.** The watcher stays armed; apply the corrections and return to the loop (kernel family: the failing gate is the next K2 input). Exception: a user-ordered infrastructure stop making NO at-ceiling claim converts to a **PAUSE** (Stop rule's PAUSE ≠ STOP) instead of aborting — record the resume state and continue shutdown. A PAUSE claims no close, so the `.stop-authorized` requirement does NOT apply to it: disarm is permitted (the pause marker records the family OPEN; LINT's unauthorized-stop check keys on clean-close/at-ceiling markers only — without this carve-out a paused session could never disarm and the revive service would fight the operator's pause).
- **ALL-CLEAR (or only non-blocking findings, applied)** → the auditor **writes `<family>/pallas/.stop-authorized`** (its ALL-CLEAR line + cursor SHAs). **VERIFY THE FILE EXISTS before proceeding** — `test -e <family>/pallas/.stop-authorized`. No file = the audit did not complete clean = you may NOT proceed (wait for it or apply its findings; dispatching the audit is not the gate — its written authorization is). You may NEVER create this file yourself — that is fabrication-class and voids the close. Also record the auditor's report line verbatim; Step 6's marker cites it. A marker without a matching `.stop-authorized` is an unauthorized stop (LINT voids + reopens). Proceed to the disarm.

### Step 1·1 — Disarm the watcher

**Only after Step 1·0 passes AND `<family>/pallas/.stop-authorized` exists on disk (or Step 1·0 resolved to a PAUSE — no close claimed)**, disarm the Step 9·0 process watcher — the persistent, self-rescheduling `process-auditor` task that `/start-experiment` armed at launch. Cancelling the watcher task at ANY other moment — including as "teardown hygiene" while an audit is still running — is a process violation that voids the close (the 2026-07-21 cohort's signature failure: three sessions cancelled their auditor mid-final-audit and closed unaudited). Its revive service would otherwise wake the session back up after this clean shutdown:

- **claude**: stop the background watcher Agent/Task (`TaskStop` or the harness's task-cancellation mechanism).
- **agy**: cancel the self-rescheduling `Schedule`/`ManageTask` entry so it stops perpetuating itself.
- **codex**: nothing to disarm (its auditor is dispatched per-experiment, not scheduled).

If no programmatic cancellation is available, note that the watcher will fire once more, see the clean-shutdown marker (Step 6), and find nothing to audit — the marker is what tells a firing watcher the session ended deliberately.

Then cancel any pending timer wakeups (safety-net wakes armed at the end of loop iterations) so no further iterations fire.

(Legacy cleanup: if a `.claude/.loop_active.json` marker exists from a pre-retirement session, `rm -f` it — the Stop-hook/marker machinery was retired 2026-07-21; the watcher owns braking now.)

Report to the user: "Loop stop requested — watcher disarmed, no more iterations will be scheduled."

## Step 2 — Determine context

**Kernel families**: context = the family slug (from the invocation or the session's family dir). Kernel runs are local — **skip Steps 2b and 3 entirely** (no clusters, nothing to reap). Steps 4.5 (stuck stubs — in the family dir), 4.7, 4.8 (family page), 5 (LINT), and 6 (stop marker → the FAMILY's log, `wiki/kernel_experiments/<slug>/pallas/log.md`) all apply. Everything else in this step is model-lane machinery.

Model lanes — same as `/start-experiment` step 1:
1. Infer model + lane from CWD if possible.
2. Read user invocation (e.g. `/stop-experiment <model> tpu`).
3. Ask via `AskUserQuestion` if unresolved.

Resolve the hierarchical `program.md` and derive constants using the same chain as `/start-experiment` step 2b:

- **USER_PREFIX**: model-level override → `$USER` segment before first underscore (lowercased) → git first-name lowercased → refuse.
- **MODEL_NAME**: auto-derived from the model folder name (strip `_autoresearch_optimization`, lowercase, `_` → `-`).
- **Cluster pool**: scan `.env/` for cluster files matching the project's lane needs (typically inferred from recent experiments or asked).

The `USER_PREFIX` is required for the orphan-workload attribution in step 3.

## Step 2b — Cancel in-flight background subagents

Before reaping workloads on clusters, cancel any gke-cluster-runner subagents the master dispatched in background mode (`run_in_background=true`) that are still polling.

Background subagents own their own polling loop and would keep going past the loop's intended end. Stopping the loop without cancelling them means they continue consuming tokens and could re-trigger notifications after the user thinks the loop has stopped.

For each cluster in CLUSTER_POOL whose in-flight workload corresponds to a background subagent we dispatched this session: signal the subagent to stop (via `TaskStop` if available, or via the harness-specific cancellation mechanism). If no programmatic cancellation is available, note that the subagents will run to completion on their own and accept that as the cleanup baseline.

This is independent of the workload itself — even if the subagent stops, the GKE workload keeps running; step 3 handles workload-side cleanup.

## Step 3 — Reap orphan workloads on all clusters

For each cluster in the project's pool (matching the lane's relevant TPU type + topology), list active workloads:

```bash
xpk workload list --project=<project> --zone=<zone> --cluster=<cluster_name> 2>&1
```

Filter for `<USER_PREFIX>-<MODEL_NAME>-*` (yours, this model). The naming convention is `<USER_PREFIX>-<MODEL_NAME>-<LANE>-v<NNN>-<SLUG>[-<retry>]`, so:

- Workloads starting with `<USER_PREFIX>-<MODEL_NAME>-` are this model's orphans (attributable directly from the name).
- Workloads starting with `<USER_PREFIX>-` but different model belong to another model's loop — leave them alone (the other model's `/stop-experiment` invocation will handle them).
- Workloads not starting with `<USER_PREFIX>-` are foreign — never touch.

For each orphan attributable to this model:

1. Read the most recent worker-0 log (`kubectl --context=<ctx> logs <pod> --tail=50`).
2. Inspect state: actively making progress, hung, completed (uncollected), crashed?
3. **For each found workload, ask the user via `AskUserQuestion`**:

   **Question**: "Workload `<name>` on `<cluster>` is `<state>`. What do you want to do?"
   **Options**:
   - `Let it finish` — leave alone (the operator will deal with it manually later).
   - `Kill it (file as inconclusive)` — `xpk workload delete` AND file an experiment page with `verdict: inconclusive` noting "killed at /stop-experiment".
   - `Kill it (file as killed_by_master)` — same, but verdict reflects intentional termination, not failure.

   If the user has set a "yes" flag, default to `Let it finish` (safer default for unattended cleanup).

For each killed workload, the experiment page filing follows SCHEMA.md `experiment` page template — frontmatter, hypothesis (recover from prior subagent dispatch context if available), Setup (recover from the launch command), Results (whatever was captured), Profile section (whatever made it to GCS), Verdict + reasoning.

## Step 4 — Cross-reference: every gke-cluster-runner dispatch has a wiki page

Walk back through the recent session's transcript (or the most recent `wiki/log.md` entries) for `gke-cluster-runner` subagent invocations. For each one, verify a corresponding experiment page exists at:

```
wiki/experiments/<model>_autoresearch_optimization/<lane>/<YYYY-MM-DD>-v<NNN>-<slug>.md
```

For any subagent run that returned a structured report but **does not** have a wiki page:
- File the missing page using the subagent's report as source data.
- Surface this to the user as "found N missing pages; filed them now."

This catches the failure mode where the main agent crashed between receiving a subagent report and writing the page.

## Step 4.5 — Resolve stuck `status: in_progress` stubs

LINT (Step 5) reports stuck stubs (`status: in_progress` > 24h per SCHEMA), but reporting is not resolution. Leaving stuck stubs after a clean shutdown is unsatisfying — at minimum, every stub the session left behind should be either re-resolved or explicitly closed.

Walk the lane's experiment directory:

```bash
grep -l "^status: in_progress" wiki/experiments/<model>_autoresearch_optimization/<lane>/*.md
```

For each stub returned:

1. **Determine the workload's actual state** (from step 3's reaping):
   - Workload completed → results are on GCS; the analyzer just never ran.
   - Workload still running → either killed in step 3, or marked "let it finish".
   - Workload crashed → results unavailable.

2. **Decide the resolution** (in priority order):

   - **If the workload completed AND the GCS profile + HLO paths exist**: re-dispatch `profile-analyzer` SYNC with the same fields the loop would have passed. Once it returns, paste the `## Profile` + `## HLO Dump` sections in, assign verdict from metrics + hypothesis-firing audit, flip `status: in_progress → filed`. The stub is now a normal completed experiment.
   - **If the workload completed BUT GCS paths are gone** (cleanup ran, retention expired): mark `verdict: inconclusive` with reason "stuck stub at /stop-experiment — workload completed but profile + HLO artifacts unavailable for re-analysis". Flip `status: in_progress → filed`. Add `backfilled: true` frontmatter so LINT's missing-Profile-section check skips it.
   - **If the workload was killed in step 3**: the user already picked the verdict in step 3's `AskUserQuestion` (`inconclusive` or `killed_by_master`); just verify the stub has that verdict and flip status.
   - **If the workload crashed**: `verdict: invalid` with reason from crash logs.
   - **If the workload is still running** (user chose "let it finish" in step 3): leave stub `in_progress`. Note in the shutdown marker that N stubs are intentionally left for in-flight workloads. The next `/start-experiment` invocation will process these on its first iteration's step 2(a) — but only if the new session uses the same model+lane and the workload's notification reaches it. If the user starts a different model, these stubs orphan until manually resolved.

Surface to user: "Resolved N stuck stubs: K via re-analysis, M as inconclusive (artifacts gone), P as invalid (crashed). Q stubs left in_progress for in-flight workloads."

## Step 4.7 — Sweep un-snapshotted subagent transcripts

Backstop for the per-consumption snapshots (root `program.md` step 8; `wiki/kernel_experiments/program.md` K4 + K6): for each experiment this session dispatched subagents for (`kernel-author`, `kernel-verifier`, `profile-analyzer`), check `raw/profiles/<exp-slug>/transcripts/`. If a dispatched agent's transcript is missing there and its file is still accessible in the session's task output, copy it in and reference it from the page's `## Sources`.

Best-effort and NON-BLOCKING: no accessible transcript → note the gap and continue; never fail or delay shutdown over this. `gke-cluster-runner` transcripts are optional (mostly polling output; the job logs persist on GCS independently). No dispatches this session → this step is a no-op.

## Step 4.8 — Update the live model / kernel family page with the latest status

The live page is the frontier source of truth and must reflect the session's final state before shutdown — a reader (or the next `/start-experiment`) should never have to reconstruct the frontier from the experiment ledger.

For the lane(s) this session touched, open the live page — a **model** lane's [`wiki/models/<architecture>-<lane>.md`](../../../wiki/models/) or a **kernel** family's [`wiki/kernels/<kernel>.md`](../../../wiki/kernels/) (`type: model`, `lane: pallas`) — and update **in place**:

- **Variant matrix row(s)** — `Status` (`live` / `blocked` / `parked` / `at-ceiling`), `Current best` (points at the latest `supported` experiment for that variant), `Open hyps` count, `Frontier exp` link. This is the same in-place update the loop does at model step 11 / kernel step K8; Step 4.8 is the backstop that guarantees it happened for the session's last experiment (the one most likely to have been interrupted).
- **Kernel families specifically**: if a family reached its physical ceiling this session (ALL FOUR Stop-rule conditions per `kernel_experiments/program.md` — and the closing retrospective carries the 4-row EVIDENCE TABLE (one artifact path per condition; unfillable without the 2nd retrospective + full-verify receipt) — leads dry at source, retrospective-confirmed bound, no progress across two consecutive retrospectives, AND the frontier's full verification: `kgate verify --mode full` receipt all-gates-PASS + the adversarial agentic check, receipt path + `verified_by` on the frontier page), set its row `Status: at-ceiling` and note the ceiling (roofline / dispatch floor) so it is not re-opened blindly — it is revisited only when accrued knowledge gives a fresh angle.
- Bump the page's `updated:` frontmatter.

This mirrors the loop's own in-place update rule; do NOT create a new page or a summary page. NON-BLOCKING for a crashed session with no clean final verdict — record what is known and let LINT (Step 5) flag any `Current best` that doesn't match the latest `supported` experiment.

## Step 5 — Run LINT

Execute the LINT operation per `SCHEMA.md`. Check and report (don't auto-fix judgment calls). The canonical list is in SCHEMA's LINT section — use that as the source of truth. Step 4.5 already resolved most stuck-stub cases, so this step's stuck-stub check should typically report 0 or only the intentionally-left-in_progress stubs.

Surface findings as a punch list. Fix mechanical issues automatically; flag judgment calls for the user.

## Step 6 — Append clean-shutdown marker

Append a `stop` marker to the **lane's** log (per SCHEMA's two-tier convention — the clean-shutdown marker is a lane-lifecycle event, not a cross-cutting one):

```markdown
## [YYYY-MM-DD] stop | /stop-experiment session end

**Op**: stop
**Final audit**: <the process-auditor's Step 1·0 report line, verbatim — e.g. "AUDIT <family> @wiki=<sha> code=<sha>: ALL CLEAR (delta: N wiki / M code commits)". MANDATORY — this is the stop authorization; a stop marker without it is unauthorized (LINT flags + reopens).>
**Pages created**: <list of any missing-page files filed in step 4>
**Pages updated**: <lane log path>
**Notes**: Clean shutdown via /stop-experiment. Reaped orphan workloads: <list>.
Outstanding lint items: <count> (see report above).
Session metrics: <N experiments run, verdict counts, frontier shifts>.
```

Path: `wiki/experiments/<model>_autoresearch_optimization/<lane>/log.md`. Insert at the top (newest-first).

This lets a subsequent `/start-experiment` distinguish "loop ended cleanly" from "session crashed mid-iteration" by reading the most recent marker in the lane's log (Step 7 of /start-experiment).

If `/stop-experiment` is being run for a session that touched MULTIPLE lanes (rare — typically each loop session is single-lane), append the `stop` marker to each lane's log. The global `wiki/log.md` does NOT get a `stop` marker — that file is for cross-cutting ops only.

## Step 7 — Summary to user

Report:

- Loop stop status: confirmed.
- Orphan workloads handled: list each with action taken.
- Missing pages filed: list each.
- Lint findings: count of clean items, count of items needing user judgment.
- Session metrics if available: total experiments run this session, verdict counts (supported / refuted / inconclusive / invalid), any frontier shifts on the model page.

End the skill — do NOT continue any further loop iterations after this.

## Failure modes to handle

- **Unable to reach a cluster** — credentials expired, network issue. Skip that cluster; surface the failure but don't block the rest of cleanup.
- **A workload's wiki page can't be filed** (missing info, etc.) — note in the summary, leave the workload's data on disk under `raw/profiles/` for manual followup.
- **User cancels mid-cleanup** — accept; record what was completed; surface what's pending.
