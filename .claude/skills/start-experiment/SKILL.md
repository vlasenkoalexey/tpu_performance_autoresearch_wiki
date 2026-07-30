---
name: start-experiment
description: Start the autoresearch optimization loop for a specific model + lane. Resolves the hierarchical program.md (root → model → lane), asks the user for hardware (local TPU VM or GKE cluster of a specified TPU type + topology), discovers available clusters from .env/, checks occupancy with USER_PREFIX-aware attribution, arms the launch-time process watcher (Step 9·0), and starts the prose loop — the session itself drives the iteration protocol. Invoke at the beginning of an autoresearch session.
---

You are starting one autoresearch session. Follow this sequence precisely. Do not skip steps.

## Step 1 — Determine context (model, lane, parallelism)

**KERNEL FAST-PATH — check this FIRST.** If the invocation names a kernel (a kernel/benchmark path, a `wiki/kernels/` family slug, or "tpu chip N"), this is a KERNEL session. Steps 2–8 are model-lane machinery — skip them ALL (no cluster discovery, no xprof probe, no hardware question; the chip is in the prompt). Do exactly:

1. Read `wiki/kernel_experiments/program.md` end-to-end; derive the family slug per its Quick-start rule 1.
2. **Step 9·0** — arm the watcher (kernel mode: `family` + `home_repo` from the family binding; bootstrap the binding first if new, per Quick-start rule 2).
3. **Step 9b** — start marker, into the FAMILY's log: `wiki/kernel_experiments/<slug>/pallas/log.md`.
4. Hand off: run the kernel Quick start (load `/author-kernel`, then K0–K9 on the pinned chip).

Everything below this line is the MODEL-lane path.

**Model + lane**, try in order:
1. **Infer from CWD**: if the current working directory contains `wiki/experiments/<model>_autoresearch_optimization/<lane>/`, use `<model>` and `<lane>`.
2. **Read user invocation**: the user may have typed `/start-experiment <model> <lane>` (e.g. `/start-experiment <model> tpu`). Parse if present.
3. **Ask**: if neither resolves both, use `AskUserQuestion` to ask. Offer the model folders under `wiki/experiments/` (currently: `<model>_autoresearch_optimization`, `qwen3_autoresearch_optimization`, `gemma4_autoresearch_optimization`, `llama3_8B_autoresearch_optimization`); then ask for lane (typically `tpu`, `jax`, `torchax` — list whatever subdirectories of the chosen model folder actually contain a `program.md`).

**Parallelism** (how many clusters to run in parallel as independent tracks):
1. Parse `--parallelism N` (or `--parallelism all`) from the invocation if present.
2. If not given, **default to 1** (single-cluster, current behavior — safest for new sessions).
3. If user asked for `all`, treat as "up to the number of free clusters matching the requested TPU type + topology" (resolved in step 6).
4. If user asked for `N > free clusters available`, use however many ARE free, surface to user: "requested N, only K free, proceeding with K".

Hold the parallelism value through step 6 (cluster selection) and step 9 (loop start).

## Step 2 — Resolve hierarchical program.md

Read in order, gracefully skipping any that don't exist:

```
wiki/experiments/program.md
wiki/experiments/<model>_autoresearch_optimization/program.md
wiki/experiments/<model>_autoresearch_optimization/<lane>/program.md
```

(Kernel families never reach this step — the Step 1 fast-path handled them. Their spec is self-contained: `wiki/kernel_experiments/program.md` → `<family>/pallas/program.md`. Both lanes share one supervision pattern: the Step 9·0 watcher, armed once at launch, plus the prose loop the runner drives at Step 9c. `/loop` and the Stop-hook/marker machinery are retired — see SCHEMA "Launch-armed process watcher"; rationale in the 2026-07-21 enforcement design record.)

**Apply replace-per-section resolution** (per the inheritance rule in root `program.md`): later files completely replace earlier files' definitions of the same H2 section; new sections in later files are taken as-is.

Print a one-line audit summary to the user showing which level each section came from. Example:

```
Effective program for <model> / tpu:
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
2. `$USER` before first underscore, lowercased: `echo "${USER%%_*}" | tr '[:upper:]' '[:lower:]'`. Example: `alekseyv_google_com` → `alekseyv`.
3. Git first-name fallback: `git config user.name | awk '{print tolower($1)}'`. Example: `Aleksey Vlasenko` → `aleksey`.
4. If still empty, refuse and ask the user to set it explicitly.

**MODEL_NAME** is auto-derived from the model folder name:

```
echo "<model>_autoresearch_optimization" | sed 's/_autoresearch_optimization$//' | tr '_' '-' | tr '[:upper:]' '[:lower:]'
```

Examples: `<model>` → `<model>`, `gemma4` → `gemma4`, `llama3_8B` → `llama3-8b`.

Print both to the user before continuing:

```
USER_PREFIX = alekseyv  (from $USER segment)
MODEL_NAME  = <model>  (auto-derived from folder)
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
  - atwigg-v5p-16    (europe-west4-b, cloud-tpu-multipod-dev)
  - tsbao-v5p-16     (europe-west4-b, cloud-tpu-multipod-dev)
  - wenxindong-pw-v5p-16-2 (europe-west4-b, cloud-tpu-multipod-dev)
  - niting-v5p-16    (europe-west4-b, cloud-tpu-multipod-dev)
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
- If **zero** are free, report each candidate's occupancy with attribution and STOP. Do NOT pick an occupied cluster. Do NOT start the run without targets.

Example output for parallelism=3:

```
v5p (2x2x2) cluster pool (4 candidates, 3 selected):
  ✓ atwigg-v5p-16              → selected (track 0)
  ✓ tsbao-v5p-16               → selected (track 1)
  ✗ wenxindong-pw-v5p-16-2     → occupied by my own jax-lane workload `alekseyv-<model>-jax-v204-...`
  ✓ niting-v5p-16              → selected (track 2)
Proceeding with 3 parallel tracks.
```

## Step 7 — Re-ground from the wiki

Before launching the loop, read the current state of the project:
- Last 50 lines of the **lane's** log: `wiki/experiments/<model>_autoresearch_optimization/<lane>/log.md` (this is the per-lane log per SCHEMA's two-tier convention; if it doesn't exist yet, this is the first session on this lane — create it empty at Step 9's loop-start marker)
- Last 30 lines of the **global** `wiki/log.md` (cross-cutting events — schema changes, ingests, lane scaffolding — that may affect this lane)
- The active model page: `wiki/models/<model>-<lane>.md` (variant matrix, Current best, Open hyps, Frontier exp)
- The last 2–3 experiment pages in `wiki/experiments/<model>_autoresearch_optimization/<lane>/`
- Any open hypotheses in `wiki/hypotheses/` tagged for this model + lane

Summarize to the user in 5–10 lines: which variant is the frontier, what was just learned, what's open, what hypothesis you'd run first.

## Step 7.5 — Probe xprof-cli (serverless — no MCP server, no `:8791`)

The `profile-analyzer` agent (dispatched per experiment) runs all xprof/HLO/LLO reads through the **`xprof-cli`** CLI in serverless local mode (`XPROF_MODE=local`, in-process; `--logdir` takes GCS paths and local dirs identically). There is no server to start. If the CLI is missing, every dispatch fails Phase 1 → no `## Profile` / `## HLO Dump` sections → LINT failures.

Probe once:

```bash
XPROF_MODE=local xprof-cli list_runs --logdir=<shared-profiles-tree>
```

- **Returns a (possibly empty) run list** → proceed.
- **Command not found / import error** → surface to the user: install with `pip install -e raw/code/xprof-cli` (the xprof-cli checkout; see `.claude/agents/profile-analyzer.md` for the tool inventory). Re-probe before continuing.

Do NOT proceed past this step if `xprof-cli` is not functional. (The legacy `mcp__xprof__*` server transport is retired from this flow — never ask the user to start `xprof --port=8791`.)

## Step 8 — Confirm with user

Use `AskUserQuestion`:

**Question**: "Start the experiment run with this plan?"
**Options**:
- `Yes, start` — proceed to step 9. (Description shown to the user: "Runs autonomously in this session; a background audit subagent supervises and revives it. Stop anytime with /stop-experiment.")
- `Different first hypothesis` — let user redirect.
- `Cancel` — exit without starting.

(Do not mention internal step numbers like "Step 9·0" in the question or option text — the user hasn't read this skill; describe mechanics in plain terms only.)

CLI flag override: `--yes` — skip the question (assume "Yes, start"; safe default for unattended scripted invocation).

(There is no never-stop question anymore. The former opt-in Stop-hook/marker mechanism is retired — premature-stop protection is now unconditional, provided by the Step 9·0 watcher's braking + reviving services and by reader-side validation: a stop without the required retrospective/evidence is flagged by the watcher and voided+reopened by LINT.)

## Step 9 — Start the run (arm watcher, mark log, drive the prose loop)

### Step 9·0 — Arm the process watcher (ONE-TIME, both lanes)

**ARM IT NOW, EXACTLY ONCE.** The [`process-auditor`](../../agents/process-auditor.md) runs as a persistent, self-rescheduling watcher — your harness's scheduler drives the repetition, never your per-iteration memory. Never re-arm per iteration. Inputs: kernel mode `family` + `home_repo`; model mode `model` + `lane` (the auditor picks its battery from the mode).

How to arm — **native scheduler only, no scripts or scaffolding**:

| harness | arming action (do this now) |
|---|---|
| claude | launch a background `Agent` (Task) that re-runs every ~5 min or on new commits under the lane/family dir; findings arrive as task notifications |
| agy | `define_subagent` the auditor + arm a **self-rescheduling** `Schedule`/`ManageTask` loop (timer or new-commit wake) that invokes it as a background subagent and returns findings to your context; the reschedule is part of this one arming |
| codex | no scheduled watcher: dispatch the `process-auditor` subagent ([`.codex/agents/process-auditor.toml`](../../../.codex/agents/process-auditor.toml)) **after filing each experiment**; its result auto-returns to your context |

What the watcher does (it replaces the retired `/loop` + Stop hook):
1. **Check** — delta audit since `.audit-cursor`; findings + paste-ready corrections land in your context. **Your rule: apply them before your next K3 (kernel) / next iteration (model).**
2. **Brake** — a stop/at-ceiling claim without its artifacts ⇒ "stop blocked"; LINT voids+reopens unearned closes.
3. **Revive** — its scheduled firing wakes an idle session (proven on agy, 2026-07-21), restarting a runner that stopped early.

**Kernel families — clear any stale stop authorization as part of this arming:** `rm -f wiki/kernel_experiments/<family>/pallas/.stop-authorized`. That file is the auditor-written close authorization (`/stop-experiment` Step 1·0); one left over from a PREVIOUS close must never satisfy a new run's `test -e` gate — a fresh run voids all prior authorization.

(Why launch-time arming: the per-iteration dispatch buried in program.md fired for 1 of 6 agy families — see the 2026-07-21 enforcement design record, "Reversal".)

### Step 9b — Write start marker to the lane's log

Write a `start` marker to the lane's log so the lane's log starts with the session boundary. Path: `wiki/experiments/<model>_autoresearch_optimization/<lane>/log.md` (kernel fast-path: the FAMILY's log, `wiki/kernel_experiments/<slug>/pallas/log.md`, with Cluster pool = `chip <N>` and Parallelism = 1). Create the file if it doesn't exist; insert at the top (newest-first):

```markdown
## [YYYY-MM-DD] start | /start-experiment session begin

**Op**: start
**Cluster pool**: <comma-separated cluster names>
**Parallelism**: <N>
**First-pick hypothesis**: <one-line from Step 7's summary>
**Notes**: session opened via /start-experiment.
```

### Step 9c — Run the prose loop (the runner is the driver)

There is no `/loop` skill invocation and no external loop machinery: **this session IS the loop driver.** Adopt the iteration protocol below as your standing operating instructions and execute it repeatedly — kernel lanes run K0→K9 synchronously per `wiki/kernel_experiments/program.md`; model lanes run the iteration protocol below. The Step 9·0 watcher supervises (checks, brakes, revives); you drive. Substitute `<model>`, `<MODEL_NAME>`, `<lane>`, `<USER_PREFIX>`, and `<CLUSTER_POOL>` (a list of `{name, context}` for the N selected clusters from step 6).

```
You are running the <model> / <lane> autoresearch loop, one iteration at a time.

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

0. BACKFILL missing wiki pages (catches subagent silent-fail / iteration-race /
   direct-kubectl-bypass failure modes):
   For each cluster in CLUSTER_POOL, list Completed workloads matching
   `<USER_PREFIX>-<MODEL_NAME>-<LANE>-v<NNN>-*` via `kubectl get jobset` (or
   `xpk workload list`). For each Completed workload:
     - Extract `v<NNN>` from the workload name.
     - Check if `wiki/experiments/<model>_autoresearch_optimization/<lane>/`
       contains a `*-v<NNN>-*.md` page.
     - If NO page exists: this is a dispatch that completed without filing.
       File a page from `kubectl logs <pod> --tail=200` (extract MFU, loss,
       exit code, headline metrics).
       
       VERDICT POLICY for backfilled pages (NEVER assigns supported/refuted —
       those require profile-analyzer's hypothesis-firing audit, which did
       not run):
         - If logs indicate crash / non-zero exit → `verdict: invalid`,
           reason: "crashed; logs: <one-line summary>"
         - If logs show clean completion but no analyzer ran →
           `verdict: inconclusive`, reason: "backfilled — profile-analyzer
           not dispatched"
       
       FRONTMATTER add: `backfilled: true` — this is the LINT exception
       marker. SCHEMA's LINT check for missing `## Profile` / `## HLO Dump`
       skips pages with `backfilled: true`. The frontmatter persists; the
       page documents the gap rather than failing LINT.
       
       Page body: `## Hypothesis under test` is unknown (no stub was filed),
       so leave it as: "**Hypothesis not recovered** — page filed by
       BACKFILL after the run completed without a stub. The original
       dispatch context was lost; treat this experiment as
       observation-only."
   Surface to user: "Backfilled N missing pages (all marked invalid or
   inconclusive — no supported/refuted verdicts assigned without analyzer)."
   If N=0, no mention.
   This step is cheap (1 kubectl call + 1 dir listing) and prevents the
   wiki from drifting out of sync with cluster reality.

1. RE-GROUND from disk (ORDER MATTERS):
   (a) PROGRAM (methodology — the drift-prevention anchor; do NOT skip):
       Read wiki/experiments/program.md (root).
       Read wiki/experiments/<model>_autoresearch_optimization/program.md (model-level).
       Read wiki/experiments/<model>_autoresearch_optimization/<lane>/program.md
         (lane-level, if exists; gracefully skip if not).
       Apply replace-per-section resolution. Use additive-section convention for
       sections like "<Model>-specific CAN additions".
   (b) STATE (what's happened):
       Read last 50 lines of the LANE'S log:
         wiki/experiments/<model>_autoresearch_optimization/<lane>/log.md
         (per SCHEMA's two-tier log convention — loop-iteration entries
         live here, not in the global wiki/log.md). If the file doesn't
         exist, this is the lane's first iteration — proceed; the loop
         creates it at first append.
       Read last 30 lines of global wiki/log.md (cross-cutting events
         that may affect this lane — schema changes, ingests, etc.).
       Read the active model page variant matrix (wiki/models/<model>-<lane>.md):
         current best, open hyps, frontier exp.
       Read the last 2-3 experiment pages in your lane.
   (c) LIVE (what's running):
       For each cluster in CLUSTER_POOL, xpk workload list to enumerate in-flight
       workloads matching <USER_PREFIX>-<MODEL_NAME>-<LANE>-* (yours).

2. WALK CLUSTER_POOL — for each cluster independently:
   (a) If a background gke-cluster-runner notification arrived for this cluster
       (subagent completed since last iteration):
         → PROCESS the structured report. The experiment page stub
           already exists from step 2(c)(i.5); update it in place:
           - READ the existing stub at the path filed in step 2(c)(i.5).
             (Hypothesis under test is already there.)
           - FILL ## Setup with the actual launch_cmd + actual config
             (from gke-cluster-runner's report — replaces the planned setup).
           - FILL ## Results with metrics from gke-cluster-runner's report
             (step time, MFU, loss trajectory, peak HBM, exit code).
           - RE-READ the active model page (wiki/models/<MODEL>-<LANE>.md)
             for current_frontier_mfu — the value cached at step 2(c)(vi)
             may be stale if other tracks landed verdicts since.
           - DISPATCH profile-analyzer (SYNC — master waits for return).
             Program.md step 8 is MANDATORY — NON-NEGOTIABLE; this is
             how it gets enforced. ALL paths are passed explicitly
             (don't let the agent guess paths — silent breakage):
               Agent(
                 subagent_type="profile-analyzer",
                 description="profile + HLO analysis for v<NNN>-<slug>",
                 prompt="""
                   Analyze the profile and HLO dump for this completed
                   experiment.
                   Fields:
                     exp_slug:             <MODEL_NAME>-<LANE>-v<NNN>-<slug>
                     index_path:           <absolute path to wiki/profile-analyzer-index.md>
                     experiment_page_path: <absolute path to stub from step 2(c)(i.5)>
                     xprof_path:           <stored xprof_path from step 2(c)(vi)>
                     hlo_path:             <stored hlo_path from step 2(c)(vi)>
                     variant:              <variant>
                     current_frontier_mfu: <fresh % from model page re-read above>
                 """
               )
             Pass ABSOLUTE paths for index_path + experiment_page_path —
             relative paths break when the agent's cwd differs from
             master's. Pass xprof_path + hlo_path EXPLICITLY (not just
             gcs_root) so the agent doesn't derive a wrong subpath.
             Note: no prior_exp_slug. Cross-experiment comparison is
             master's responsibility at verdict time + via explicit
             Mode B drilldown when warranted.
           - PASTE the analyzer's `## Profile` and `## HLO Dump` sections
             verbatim into the experiment page (replaces the empty
             placeholders). The analyzer's output is already formatted;
             do not rewrite or summarize.
           - ASSIGN verdict (## Verdict section): supported / refuted /
             inconclusive / invalid. Use the profile-analyzer's
             hypothesis-firing audit + metrics-vs-baseline comparison
             as inputs. Change frontmatter status: in_progress →
             <verdict>. The page is now immutable per SCHEMA.
           - Update the model page variant matrix if Current best moved
             (use the profile-analyzer's MFU as the authoritative number).
           - AUTO-MERGE on supported + frontier shift (closes class C of
             the original audit). If BOTH of the following are true:
               * verdict == "supported"
               * the variant matrix's Current best row was updated to point
                 at this experiment
             THEN merge the experiment fork into the model-repo trunk:
               cd <MODEL_REPO_PATH>
               git checkout <trunk-branch>     # typically `main`
               git merge --no-ff <experiment-fork-branch> \
                 -m "Merge frontier-shifting experiment v<NNN>-<slug>

                 exp: wiki/experiments/<...>/v<NNN>-<slug>.md
                 verdict: supported
                 frontier shift: <prev-MFU> → <new-MFU> on <variant>"
             Then rebuild + push the stable production image so the next
             experiment's BUILD step starts from the new trunk:
               <build-cmd from program.md step 5, tagged as the lane's
                stable image>
             If the merge has conflicts (other tracks' supported merges
             touched the same files), abort the merge and surface to user
             — do NOT force-resolve. The user resolves the conflict and
             re-runs the merge step manually. Loop continues with the
             non-frontier verdict path.
             If verdict is NOT supported OR Current best did NOT shift,
             skip auto-merge — the fork stays as a per-experiment branch
             for potential future reference / observation extraction.
           - Append a SCHEMA-compliant log entry to the LANE'S log:
             wiki/experiments/<model>_autoresearch_optimization/<lane>/log.md
             (op type: `loop-iteration` — see SCHEMA log conventions for
             the one-line format this op allows). NOT global wiki/log.md
             — that file is reserved for cross-cutting ops per the
             two-tier convention. Writing loop-iteration to global is a
             LINT violation.
             Newest-first; insert at the top of the file. If the file
             doesn't exist (lane's first iteration), create it with the
             entry as its only content; no header line needed.
               ## [YYYY-MM-DD] loop-iteration | v<NNN>-<slug> on <variant>: <verdict> (<delta vs frontier>)
       → Cluster is now idle; fall through to (c).
   (b) Else if cluster has an in-flight workload (matching <USER_PREFIX>-<MODEL_NAME>-<LANE>-*
       per step 1c):
         → SKIP. Background notification will trigger when the subagent finishes.
       → Continue to next cluster.
   (c) Else (cluster idle, ready for next dispatch). Walk program.md
       steps 2-6 for this cluster (the loop orchestrates; skills/agents
       do the work):

       (i) PICK the next hypothesis (program.md step 2). Invoke
           /formulate-hypothesis with: current variant, recent profile
           summary (from the most recently filed experiment page on this
           variant), last 2-3 experiment verdicts, in-flight v-ids for
           duplicate avoidance. Skill returns a structured proposal —
           see the skill's own docs for output format + modes. DO NOT
           formulate inline; the skill enforces precedent checks that
           prevent v391y-class regressions.

           Coordinate across tracks: pass the in-flight v-ids list so
           /formulate-hypothesis can steer away from duplicates. If
           another cluster is currently running v541, this track must
           not also pick v541.

       (i.5) FILE experiment page STUB to disk BEFORE running. This
             gives durable hypothesis context that profile-analyzer
             reads later, and survives session crashes.
             Path: wiki/experiments/<MODEL>_autoresearch_optimization/<LANE>/<YYYY-MM-DD>-v<NNN>-<slug>.md
             Sections to populate from the /formulate-hypothesis proposal:
               - Frontmatter: variant, hypothesis (one-line), status: in_progress, created date
               - ## Hypothesis under test — MUST contain four labeled
                 paragraphs extracted from the proposal (profile-analyzer
                 Step 0 reads these — under-specification here defeats
                 the silent-noop audit):

                 **Hypothesis** (one falsifiable sentence): from the
                 proposal's `Hypothesis:` field.

                 **Mechanism** (what code / flag / kernel / sharding change
                 the hypothesis introduces, in 1-3 sentences): from the
                 proposal's hypothesis statement detail + the Blueprint
                 phase block's `Mechanism (one sentence):` field if the
                 phase is `novel`. For known phases, derive from the
                 proposal's hypothesis + the cited topic's mechanism in
                 model-optimization-index. The agent will use this to
                 know WHAT structural signal to grep the HLO for.

                 **Predicted signal** (what the profile should show if
                 the hypothesis fired correctly — bucket attribution
                 change, custom_call presence, module count shift, etc.):
                 from the proposal's `Profile signal:` field (current
                 bucket) + the expected delta (what bucket / op should
                 change and by how much). Phrase as: "expect <bucket>
                 to drop from <current %> to <expected %>" or "expect
                 custom_call(target=X) to appear in train_step module".
                 This is what Phase 3 verifies CONFIRMED / SILENT NO-OP /
                 PARTIAL against.

                 **Falsification criterion** (metric + threshold that
                 would refute): from the proposal's
                 `Falsification criterion:` field, verbatim.

               - ## Setup (planned setup — actual launch_cmd populated in step (vi))
               - ## Results (empty placeholder)
               - ## Profile (empty placeholder)
               - ## HLO Dump (empty placeholder)
               - ## Verdict (empty placeholder)
             SCHEMA tension: SCHEMA.md says experiments are immutable
             once filed. The compromise: `status: in_progress` means
             the page is a stub, not yet "filed" in the verdict-assigned
             sense. Mutability is bounded to the run's lifetime; verdict
             assignment closes immutability.

       (ii) FORK + IMPLEMENT (program.md steps 3-4):
            - Create the per-experiment fork of the model code repo per
              the Branching model snippet in program.md.
            - Invoke /edit-model-code BEFORE opening any file in the fork
              — it loads the surgical-edit discipline. Then apply the
              change from the proposal.
            - Commit with the `exp: wiki/experiments/<...>.md` footer.

       (iii) BUILD + PUSH (program.md step 5):
             - Build docker image from the fork; tag with branch name.
             - Smoke-test: `docker run --rm <new_tag> python -m <entry-module> --help`
               (per-stack guidance in program.md step 5).
             - If smoke-test fails, fix the rebase before pushing — never
               dispatch a broken image.
             - Push to artifact registry.

       (iv) CONSTRUCT workload_name per convention:
            workload_name = "<USER_PREFIX>-<MODEL_NAME>-<LANE>-v<NNN>-<slug>"
            Retry: append "-b", "-c", … if resubmitting the same v-id.

       (v) VALIDATE length (XPK rejects ≥40 at parse time):
             HARD: len(workload_name) < 40 chars (XPK enforces this — error is
             "Name must be less than 40 characters and match the pattern
             '[a-z]([-a-z0-9]*[a-z0-9])?'"). If at/over the limit, shorten
             <slug> before dispatching. Standard abbreviations: deepseek→ds,
             sparsecore→sc, attention→attn, fusion→fus, tensor-parallel→tp,
             expert-parallel→ep, track-parallel→pt, host-offload→ho,
             megablox→mblx, selective→sel. Do NOT strip required segments
             (USER_PREFIX, MODEL_NAME, LANE, v<NNN>).
             Recommended: ≤ 30 chars total (leaves room for retry suffix).
             Budget for <Model> JAX (alekseyv-<model>-jax-v<NNN>- = 29
             chars): slug must fit in 10 chars.

       (vi) DISPATCH gke-cluster-runner in BACKGROUND mode (program.md step 6):
            
            Compute the GCS paths EXPLICITLY (don't rely on convention —
            profile-analyzer needs the exact paths and convention drift
            silently breaks things):
              gcs_root  = gs://<bucket>/autoresearch/<MODEL_NAME>-<LANE>-v<NNN>-<slug>
              xprof_path = ${gcs_root}/xprof
              hlo_path   = ${gcs_root}/hlo
            
            The launch_cmd (from lane-level program.md) MUST write profiles
            to xprof_path and HLO dumps to hlo_path. If the lane's launch_cmd
            doesn't follow this convention, the lane's program.md is broken —
            fix that before running. Both paths are passed to profile-analyzer
            at notification time so it doesn't have to guess.

            Agent(
              subagent_type="gke-cluster-runner",
              run_in_background=true,        # ← critical: do NOT block
              description="<NNN>-<slug> on <cluster_name>",
              prompt="""
                Submit and run experiment <slug> on cluster <cluster_name>.
                Fields:
                  exp_slug:        <MODEL_NAME>-<LANE>-v<NNN>-<slug>
                  gcs_root:        <gcs_root from above>
                  xprof_path:      <xprof_path from above>   # explicit, not derived
                  hlo_path:        <hlo_path from above>     # explicit, not derived
                  launch_cmd:      <constructed from lane-level program.md;
                                    MUST write profiles to xprof_path and HLO
                                    dumps to hlo_path>
                  image:           <MODEL_REPO>-container:<branch-name>
                  cluster_name:    <cluster_name>
                  cluster_context: <cluster_context>
                  workload_name:   <workload_name from (iv)>
                  user_prefix:     <USER_PREFIX>
                  model_name:      <MODEL_NAME>
                  lane:            <LANE>
              """
            )
            
            STORE xprof_path + hlo_path + experiment_page_path (from i.5)
            keyed by exp_slug — master needs them at notification time to
            dispatch profile-analyzer in step 2(a).
            
            Master continues immediately. Subagent runs independently and reports
            via background notification when done.

3. END THE ITERATION — idle/wake discipline (no busy-polling, no sleep loops):
   - If any track has work in flight, you may end the iteration (and the turn):
     background subagent completion notifications re-invoke you, and the
     Step 9·0 watcher's periodic firing revives the session if nothing else
     does (empirically verified — the revive service).
   - Safety net: if your harness exposes a native timer wake (agy Schedule,
     claude scheduled wakeup), arm one at <=600 s (10 min) before ending the
     iteration — hung workloads burn TPU quota and must never wait longer
     than 10 min for a fresh look. Floor 120 s. If no native timer exists,
     the watcher's cadence is the fallback.
   - User interrupts naturally: a user message during the wait runs as a
     normal turn; resume the loop protocol at its end.
   - On user "stop" or /stop-experiment: do not schedule anything further;
     exit. Loop ends.

4. EXIT the iteration cleanly. Do NOT continue past step 4 in this iteration —
   the next wake (notification, timer, or watcher firing) starts the next one.

DO NOT:
- Ask the user clarifying questions (the loop is autonomous).
- Skip the RE-GROUND step — especially the PROGRAM sub-step (drift prevention).
- Run XPK launches directly from this session — always via gke-cluster-runner subagent in BACKGROUND mode.
- Block on a gke-cluster-runner subagent (e.g. running it foreground). Tracks must be independent.
- File summary pages covering multiple experiments — one page per experiment.
- Pick the same hypothesis on multiple tracks in the same iteration.

If you genuinely have no open hypotheses for any idle cluster, formulate new ones
based on recent observations and file them as wiki/hypotheses/<slug>.md before
dispatching. Different tracks should get different ideas.

The loop continues until the user invokes /stop-experiment or interrupts.
```

After starting the loop, surface to the user:
- The chosen cluster, lane, and workload prefix.
- A reminder of how to stop the run: `/stop-experiment` (disarms the watcher). An interrupt alone leaves the watcher armed — it will revive the session by design; only `/stop-experiment` ends the run cleanly.
- The expected first-iteration completion time.

## Failure modes to handle gracefully

- **No `program.md` at root** — refuse, point user to write it (this skill assumes the hierarchy exists).
- **No clusters in `.env/` match the requested TPU type + topology** — tell the user, offer to refine the criteria (e.g. "no v6e-2x2x2 clusters; you have v6e-2x2 (8 chips) and v6e-4x2 (16 chips) — pick one?").
- **All matching clusters are occupied** — report each cluster's occupancy attribution and stop. Do NOT silently pick a cluster that's busy.
- **User picks Local mode but the local TPU is too small** — warn, ask whether to proceed anyway.
