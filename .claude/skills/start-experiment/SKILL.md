---
name: start-experiment
description: Start the autoresearch optimization loop for a specific model + lane. Resolves the hierarchical program.md (root → model → lane), asks the user for hardware (local TPU VM or GKE cluster of a specified TPU type + topology), discovers available clusters from .env/, checks occupancy with USER_PREFIX-aware attribution, and starts /loop with the bounded-iteration prompt. Invoke at the beginning of an autoresearch session.
---

You are starting one autoresearch session. Follow this sequence precisely. Do not skip steps.

## Step 1 — Determine context (model, lane, parallelism)

**Model + lane**, try in order:
1. **Infer from CWD**: if the current working directory contains `wiki/experiments/<model>_autoresearch_optimization/<lane>/`, use `<model>` and `<lane>`.
2. **Read user invocation**: the user may have typed `/start-experiment <model> <lane>` (e.g. `/start-experiment gemma4 tpu`). Parse if present.
3. **Ask**: if neither resolves both, use `AskUserQuestion` to ask. Offer the model folders under `wiki/experiments/` (e.g. `gemma4_autoresearch_optimization`, `llama3_8B_autoresearch_optimization`); then ask for lane (typically `tpu`, `jax`, `torchax` — list whatever subdirectories of the chosen model folder actually contain a `program.md`).

**Parallelism** (how many clusters to run in parallel as independent tracks):
1. Parse `--parallelism N` (or `--parallelism all`) from the invocation if present.
2. If not given, **default to 1** (single-cluster, current behavior — safest for new sessions).
3. If user asked for `all`, treat as "up to the number of free clusters matching the requested TPU type + topology" (resolved in step 6).
4. If user asked for `N > free clusters available`, use however many ARE free, surface to user: "requested N, only K free, proceeding with K".

Hold the parallelism value through step 6 (cluster selection) and step 9 (/loop dispatch).

## Step 2 — Resolve hierarchical program.md

Read in order, gracefully skipping any that don't exist:

```
wiki/experiments/program.md
wiki/experiments/<model>_autoresearch_optimization/program.md
wiki/experiments/<model>_autoresearch_optimization/<lane>/program.md
```

**Apply replace-per-section resolution** (per the inheritance rule in root `program.md`): later files completely replace earlier files' definitions of the same H2 section; new sections in later files are taken as-is.

Print a one-line audit summary to the user showing which level each section came from. Example:

```
Effective program for gemma4 / tpu:
  Inheritance model        ← root
  Concurrency model        ← root
  Setup                    ← lane (overrides model + root)
  Workload naming          ← root (no model/lane override)
  Branching model          ← model
  Operational env vars     ← lane
  Kernels available        ← lane
  The goal                 ← model
  The experiment loop      ← root
  ... etc.
```

## Step 2b — Derive USER_PREFIX and MODEL_NAME

**USER_PREFIX resolution chain** (first hit wins):

1. If model-level `program.md` has an explicit `USER_PREFIX = <value>` line, use it.
2. `$USER` before first underscore, lowercased: `echo "${USER%%_*}" | tr '[:upper:]' '[:lower:]'`. Example: `jane_google_com` → `<USER_PREFIX>`.
3. Git first-name fallback: `git config user.name | awk '{print tolower($1)}'`. Example: `Jane Doe` → `jane`.
4. If still empty, refuse and ask the user to set it explicitly.

**MODEL_NAME** is auto-derived from the model folder name:

```
echo "<model>_autoresearch_optimization" | sed 's/_autoresearch_optimization$//' | tr '_' '-' | tr '[:upper:]' '[:lower:]'
```

Examples: `gemma4` → `gemma4`, `llama3_8B` → `llama3-8b`.

Print both to the user before continuing:

```
USER_PREFIX = <USER_PREFIX>  (from $USER segment)
MODEL_NAME  = gemma4  (auto-derived from folder)
LANE        = tpu  (from context)
```

## Step 3 — Determine hardware target

Ask the user via `AskUserQuestion`:

**Question**: "Where should experiments run?"
**Options**:
- `Local (this TPU VM)` — runs in the master session, no XPK. Use when the local machine itself is a TPU VM with enough chips for the requested experiment.
- `GKE (XPK)` — submits workloads to a GKE cluster. Will require TPU type + topology selection in the next step.

If the user picks **Local**:
- Confirm the local TPU is appropriate for the model size: `python -c "import jax; print(jax.devices())"` to see what's available locally.
- Skip the cluster discovery (steps 4–6) and proceed to step 7.

If the user picks **GKE**:
- Continue to step 4.

## Step 4 — Ask for TPU type + topology (GKE only)

Ask the user via `AskUserQuestion`:

**Question 1**: "Which TPU generation?"
**Options**: `v5p`, `v6e` (list from what `.env/` actually contains — scan filenames for `v5p`, `v6e`, etc.)

**Question 2**: "Which topology / chip count?"
**Options**: scan `.env/*.md` for the chosen generation, extract topology from the "Topology" section of each cluster file (look for lines like `**TPU**: v5p, 2x2x2 topology = 8 chips per slice` or `**TPU**: v6e, 2x4 = 8 chips`). Group cluster files by topology and present each topology as an option. Example for v5p: `2x2x1 (4 chips)`, `2x2x2 (8 chips)`, `4x2x2 (16 chips)`, etc.

## Step 5 — Discover candidate clusters (GKE only)

From `.env/`, list every cluster file matching the chosen `(TPU generation, topology)`. Parse each cluster file to extract:
- `cluster_name` (from filename pattern `gke-<tpu>-<topo>-<owner>.md` or from the "Cluster" line in the Topology section)
- `region`, `zone`, `project` (from the Connection or Topology section)
- `context_name` (kubectl context — typically printed as a comment after `gcloud get-credentials`)
- `tpu_type` (the xpk-style `--tpu-type` value — note the v5p TC-vs-chip distinction: xpk's `v5p-16` = 16 TC = 8 chips; `v5p-8` = 8 TC = 4 chips)
- `chip_count`

Build a candidate list. Example:

```
v5p, 2x2x2 (8 chips per slice) candidates from .env/:
  - examplecluster-v5p-16    (<zone>, <project>)
  - tsbao-v5p-16     (<zone>, <project>)
  - othercluster-pw-v5p-16-2 (<zone>, <project>)
  - niting-v5p-16    (<zone>, <project>)
```

## Step 6 — Occupancy check + cluster selection (GKE only)

For each candidate cluster in turn, run the occupancy check:

```bash
# Fetch credentials (skip if already in kubeconfig)
gcloud container clusters get-credentials <cluster_name> --location=<region> --project=<project> 2>/dev/null

# List active workloads
xpk workload list --project=<project> --zone=<zone> --cluster=<cluster_name> 2>&1
# Or:
kubectl --context=<context_name> get jobset -A --no-headers 2>&1
```

Classify each active workload **from the name alone** (the format `<USER_PREFIX>-<MODEL_NAME>-<LANE>-v<NNN>-<SLUG>[-<retry>]` makes this one-step):

| Workload name pattern | Classification |
|---|---|
| Starts with `<USER_PREFIX>-<MODEL_NAME>-<LANE>-` (requested lane) | **mine, same model+lane** → cluster busy, skip |
| Starts with `<USER_PREFIX>-<MODEL_NAME>-<other-lane>-` | **mine, same model other lane** → conflict, skip |
| Starts with `<USER_PREFIX>-<other-model>-` | **mine, other model** → conflict, skip |
| Starts with `<other-prefix>-` | **foreign** → cluster occupied by another user, skip |

Image-tag inspection is the backstop only — use it if a workload name doesn't follow the convention (legacy workloads or manually-submitted ones), to verify lane/model. Pattern:

```bash
kubectl --context=<ctx> get jobset <workload> -o jsonpath='{.spec.replicatedJobs[0].template.spec.template.spec.containers[0].image}'
# Returns: <base>:<branch> where branch encodes <model>-<lane>-<date>-v<NNN>-<slug>
```

**Selection rule** (parallelism-aware):
- Walk candidates, classify each as `free` or `occupied` per the attribution table above.
- Select up to **N free clusters** (where N = parallelism from step 1; `all` = every free candidate).
- If parallelism = 1: pick the first free cluster (current single-cluster behavior).
- If parallelism > 1: pick the first N free clusters. Pool will operate as N independent tracks.
- If fewer than N are free, use however many are free and surface: "requested N, only K free, proceeding with K".
- If **zero** are free, report each candidate's occupancy with attribution and STOP. Do NOT pick an occupied cluster. Do NOT start the loop without targets.

Example output for parallelism=3:

```
v5p (2x2x2) cluster pool (4 candidates, 3 selected):
  ✓ examplecluster-v5p-16              → selected (track 0)
  ✓ tsbao-v5p-16               → selected (track 1)
  ✗ othercluster-pw-v5p-16-2     → occupied by my own jax-lane workload `<USER_PREFIX>-<MODEL_NAME>-jax-v204-...`
  ✓ niting-v5p-16              → selected (track 2)
Proceeding with 3 parallel tracks.
```

## Step 7 — Re-ground from the wiki

Before launching the loop, read the current state of the project:
- Last 50 lines of `wiki/log.md`
- The active model page: `wiki/models/<model>-<lane>.md` (variant matrix, Current best, Open hyps, Frontier exp)
- The last 2–3 experiment pages in `wiki/experiments/<model>_autoresearch_optimization/<lane>/`
- Any open hypotheses in `wiki/hypotheses/` tagged for this model + lane

Summarize to the user in 5–10 lines: which variant is the frontier, what was just learned, what's open, what hypothesis you'd run first.

## Step 8 — Confirm with user

Use `AskUserQuestion` to confirm the launch plan:

**Question**: "Start the loop with this plan?"
**Options**:
- `Yes, start loop` — proceed to step 9.
- `Different first hypothesis` — let user redirect.
- `Cancel` — exit without starting.

If the user has set a "no-prompt" mode (e.g. `--yes` flag in the invocation), skip this question.

## Step 9 — Start the loop

Invoke `/loop` (self-paced; let the model pick the next-iteration delay via `ScheduleWakeup`) with the bounded-iteration prompt template below. Substitute `<model>`, `<MODEL_NAME>`, `<lane>`, `<USER_PREFIX>`, and `<CLUSTER_POOL>` (a list of `{name, context}` for the N selected clusters from step 6).

```
/loop You are running one iteration of the <model> / <lane> autoresearch loop.

Session constants (derived once by /start-experiment, do not re-derive):
  USER_PREFIX  = <USER_PREFIX>
  MODEL_NAME   = <MODEL_NAME>
  LANE         = <lane>
  CLUSTER_POOL = [
    {name: "<cluster_1>", context: "<context_1>"},
    {name: "<cluster_2>", context: "<context_2>"},
    ...
  ]  # N independent tracks, one per cluster

ARCHITECTURE: parallel-tracks-via-background-subagents.
  - Each cluster is an INDEPENDENT TRACK with its own experiment lifecycle.
  - Cluster-runner subagents are dispatched with run_in_background=true.
  - Master does NOT block on subagents — it walks the pool, dispatches idle clusters,
    processes completed background notifications, and exits the iteration.
  - When a background subagent completes, the master is auto-notified — process on
    next iteration's step 2(a).

Iteration steps:

1. RE-GROUND from disk (ORDER MATTERS):
   (a) PROGRAM (methodology — the drift-prevention anchor; do NOT skip):
       Read wiki/experiments/program.md (root).
       Read wiki/experiments/<model>_autoresearch_optimization/program.md (model-level).
       Read wiki/experiments/<model>_autoresearch_optimization/<lane>/program.md
         (lane-level, if exists; gracefully skip if not).
       Apply replace-per-section resolution. Use additive-section convention for
       sections like "<MODEL>-specific CAN additions".
   (b) STATE (what's happened):
       Read last 50 lines of wiki/log.md.
       Read the active model page variant matrix (wiki/models/<model>-<lane>.md):
         current best, open hyps, frontier exp.
       Read the last 2-3 experiment pages in your lane.
   (c) LIVE (what's running):
       For each cluster in CLUSTER_POOL, xpk workload list to enumerate in-flight
       workloads matching <USER_PREFIX>-<MODEL_NAME>-<LANE>-* (yours).

2. WALK CLUSTER_POOL — for each cluster independently:
   (a) If a background cluster-runner notification arrived for this cluster
       (subagent completed since last iteration):
         → PROCESS the structured report:
           - file the experiment page per SCHEMA.md
           - update the model page variant matrix if Current best moved
           - append a one-line summary to wiki/log.md
       → Cluster is now idle; fall through to (c).
   (b) Else if cluster has an in-flight workload (matching <USER_PREFIX>-<MODEL_NAME>-<LANE>-*
       per step 1c):
         → SKIP. Background notification will trigger when the subagent finishes.
       → Continue to next cluster.
   (c) Else (cluster idle, ready for next dispatch):
       (i) PICK the next hypothesis for this cluster. Coordinate across tracks
           to avoid duplicates — if another cluster is currently running v541,
           do NOT also pick v541. Highest-ranked open from wiki/hypotheses/ or
           model page open list. Formulate new from recent observations if none.
       (ii) CONSTRUCT workload_name per convention:
            workload_name = "<USER_PREFIX>-<MODEL_NAME>-<LANE>-v<NNN>-<slug>"
            Retry: append "-b", "-c", … if resubmitting the same v-id.
       (iii) VALIDATE length:
             HARD: len(workload_name) ≤ 50 chars. If exceeded, shorten <slug>
             (e.g. "fusion"→"fus", drop articles). Do NOT strip required
             segments (USER_PREFIX, MODEL_NAME, LANE, v<NNN>).
             Recommended: ≤ 40 chars.
       (iv) DISPATCH in BACKGROUND mode:
            Agent(
              subagent_type="cluster-runner",
              run_in_background=true,        # ← critical: do NOT block
              description="<NNN>-<slug> on <cluster_name>",
              prompt="""
                Submit and run experiment <slug> on cluster <cluster_name>.
                Fields:
                  exp_slug:        <MODEL_NAME>-<LANE>-v<NNN>-<slug>
                  gcs_root:        gs://<bucket>/autoresearch/<MODEL_NAME>-<LANE>-v<NNN>-<slug>
                  launch_cmd:      <constructed from lane-level program.md>
                  image:           <torchtitan-container:branch-name>
                  cluster_name:    <cluster_name>
                  cluster_context: <cluster_context>
                  workload_name:   <workload_name from (ii)>
                  user_prefix:     <USER_PREFIX>
                  model_name:      <MODEL_NAME>
                  lane:            <LANE>
              """
            )
            Master continues immediately. Subagent runs independently and reports
            via background notification when done.

3. SCHEDULE next iteration (safety net):
   Call ScheduleWakeup(delaySeconds=600, prompt=<this loop prompt>,
                       reason="10-min cap; background subagent notifications will wake sooner")
   
   Notes:
   - Background subagent completions arrive as automatic notifications — these
     trigger iteration sooner than 600s. The ScheduleWakeup is a safety net for
     the case where no subagents complete within the window (idle pool, all tracks
     in long compile).
   - Minimum floor: 120s (2 min). NEVER pick delaySeconds below 120.
   - User interrupts naturally: a user message during the wait runs as a normal
     turn. At the end of EVERY response while the loop is active, call
     ScheduleWakeup(600) to reset the timer.
   - On user "stop" or /stop-experiment: do NOT call ScheduleWakeup; exit. Loop ends.

4. EXIT cleanly. Do NOT continue past step 4 in this iteration.

DO NOT:
- Ask the user clarifying questions (the loop is autonomous).
- Skip the RE-GROUND step — especially the PROGRAM sub-step (drift prevention).
- Run XPK launches directly from this session — always via cluster-runner subagent in BACKGROUND mode.
- Block on a cluster-runner subagent (e.g. running it foreground). Tracks must be independent.
- File summary pages covering multiple experiments — one page per experiment.
- Pick the same hypothesis on multiple tracks in the same iteration.

If you genuinely have no open hypotheses for any idle cluster, formulate new ones
based on recent observations and file them as wiki/hypotheses/<slug>.md before
dispatching. Different tracks should get different ideas.

The loop continues until the user invokes /stop-experiment or interrupts.
```

After invoking `/loop`, surface to the user:
- The chosen cluster, lane, and workload prefix.
- A reminder of how to stop the loop: `/stop-experiment` or interrupt.
- The expected first-iteration completion time.

## Failure modes to handle gracefully

- **No `program.md` at root** — refuse, point user to write it (this skill assumes the hierarchy exists).
- **No clusters in `.env/` match the requested TPU type + topology** — tell the user, offer to refine the criteria (e.g. "no v6e-2x2x2 clusters; you have v6e-2x2 (8 chips) and v6e-4x2 (16 chips) — pick one?").
- **All matching clusters are occupied** — report each cluster's occupancy attribution and stop. Do NOT silently pick a cluster that's busy.
- **User picks Local mode but the local TPU is too small** — warn, ask whether to proceed anyway.
