---
name: stop-experiment
description: Stop the autoresearch optimization loop cleanly. Cancels pending ScheduleWakeup, reaps orphan workloads on the project's cluster pool, files any missing experiment pages, runs lint, and appends a clean-shutdown marker to wiki/log.md. Invoke at the end of an autoresearch session.
---

You are stopping the autoresearch loop cleanly. Follow this sequence — do not abbreviate.

## Step 1 — Stop the loop

Cancel any pending `ScheduleWakeup` so no further iterations fire. If `/loop` is running, the way to stop it depends on the harness:
- If self-paced: omit the next `ScheduleWakeup` call. The loop naturally ends after this iteration.
- If interval-based: tell the user they need to use the harness's loop-stop mechanism (typically `/loop --stop` or interrupting the session).

Report to the user: "Loop stop requested — no more iterations will be scheduled."

## Step 2 — Determine context

Same as `/start-experiment` step 1:
1. Infer model + lane from CWD if possible.
2. Read user invocation (e.g. `/stop-experiment gemma4 tpu`).
3. Ask via `AskUserQuestion` if unresolved.

Resolve the hierarchical `program.md` and derive constants using the same chain as `/start-experiment` step 2b:

- **USER_PREFIX**: model-level override → `$USER` segment before first underscore (lowercased) → git first-name lowercased → refuse.
- **MODEL_NAME**: auto-derived from the model folder name (strip `_autoresearch_optimization`, lowercase, `_` → `-`).
- **Cluster pool**: scan `.env/` for cluster files matching the project's lane needs (typically inferred from recent experiments or asked).

The `USER_PREFIX` is required for the orphan-workload attribution in step 3.

## Step 2b — Cancel in-flight background subagents

Before reaping workloads on clusters, cancel any cluster-runner subagents the master dispatched in background mode (`run_in_background=true`) that are still polling.

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

## Step 4 — Cross-reference: every cluster-runner dispatch has a wiki page

Walk back through the recent session's transcript (or the most recent `wiki/log.md` entries) for `cluster-runner` subagent invocations. For each one, verify a corresponding experiment page exists at:

```
wiki/experiments/<model>_autoresearch_optimization/<lane>/<YYYY-MM-DD>-v<NNN>-<slug>.md
```

For any subagent run that returned a structured report but **does not** have a wiki page:
- File the missing page using the subagent's report as source data.
- Surface this to the user as "found N missing pages; filed them now."

This catches the failure mode where the main agent crashed between receiving a subagent report and writing the page.

## Step 5 — Run LINT

Execute the LINT operation per `SCHEMA.md`. Check and report (don't auto-fix judgment calls):

- Unresolved `[!warning]` contradictions.
- Hypotheses `open` with no activity > 14 days.
- Experiments without profile artifacts in `raw/profiles/`.
- Experiments missing a `variant:` field, or whose `variant:` doesn't appear in the parent model page's matrix.
- Model pages where any variant row's `Current best` doesn't match the latest `supported` experiment.
- Hypothesis `variants:` lists referencing rows not in the model page's matrix.
- Experiment commit messages on the model-code-repo side missing the `exp:` footer.
- Experiment artifacts accidentally duplicated into the model code repo.
- Orphan pages (no inbound links).
- Broken markdown links.
- Stale codebase pages whose `commit:` is far behind the current checkout.

Surface findings as a punch list. Fix mechanical issues automatically; flag judgment calls for the user.

## Step 6 — Append clean-shutdown marker

Append to `wiki/log.md`:

```markdown
## [YYYY-MM-DD] manual | /stop-experiment

**Op**: manual
**Pages created**: <list of any missing-page files filed in step 4>
**Pages updated**: log.md
**Notes**: Clean shutdown via /stop-experiment. Reaped orphan workloads: <list>.
Outstanding lint items: <count> (see report above).
```

This lets a subsequent `/start-experiment` distinguish "loop ended cleanly" from "session crashed mid-iteration."

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
