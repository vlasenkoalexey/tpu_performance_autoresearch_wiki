---
name: scan-gke-clusters
description: Refresh the GKE TPU cluster inventory for one or more GCP projects. Runs `.claude/scripts/scan-gke-clusters.sh` to enumerate clusters with TPUs in each project (status, XPK presence, ready-node count, XPK type, topology, machine type), writes a per-project Markdown summary at `.env/<project>-gke-tpu-cluster-scan.md`, and merges the project's rows into the combined `.env/gke-tpu-cluster-scan.md` (preserving the existing TPU-gen breakdown + sort rules + prose between tables). Invoke when a new cluster has been added to a project, when an existing cluster's XPK status or pool composition has changed, or for periodic batch refresh across multiple projects. NOT for occupancy checks ("which clusters have free capacity right now?") — that's `/start-experiment`'s Step 6 job and uses live `xpk workload list`.
---

# /scan-gke-clusters — refresh GKE TPU cluster inventory

Updates the inventory under `.env/` that `/start-experiment` Step 5 consults when picking a cluster. Reads it by running gcloud + kubectl probes against each project's clusters; writes both a per-project file (deep dive) and updates the combined inventory (cross-project overview).

## When to invoke

- **New cluster reported** — colleague spun up a cluster, your inventory is missing it.
- **Cluster changed** — node-pool added/removed, XPK setup completed, pool composition changed.
- **Periodic batch refresh** — once every few weeks, pass every project the user maintains access to as separate `--project` args, to catch all drift.
- **NOT for occupancy** — "which cluster has free capacity right now" is a live query, not inventory. `/start-experiment` handles occupancy via its Step 6 (xpk workload list + name-based attribution).

## Cardinal rules

- **Outputs go in `.env/`**, scripts live in `.claude/scripts/`. Same convention as the rest of the autoresearch infra.
- **Per-project file is the source of truth for that project's clusters.** The combined file is a cross-project view; its rows are owned by per-project files.
- **The combined file's structure is preserved verbatim** — TPU-gen H2 sections, sort within each section (largest single-slice topology first, then cluster name), prose intro/outro. Only the rows for the scanned project change.
- **gcsfuse + Spot columns**: NOT in the bash probe TSV. New rows get `?`. Existing rows from OTHER projects are preserved verbatim. Detecting gcsfuse + spot would require additional kubectl + gcloud calls — deferred to v2.
- **Do NOT auto-commit.** The skill produces artifacts; the user reviews + commits per existing convention. `.env/` is gitignored on this repo so committing is opt-in if desired.

## Arguments

Required (at least one):
- `<project-name>` — bare positional. Skill treats any argument NOT starting with `--` as shorthand for `--project <arg>`. Most common form: `/scan-gke-clusters <project>`.
- `--project <p>` — repeatable; for multi-project refresh, pass once per project: `/scan-gke-clusters --project <project> --project <project>`.

Optional:
- `--skip-combined` — write per-project files only; don't update the combined file.
- `--combined-path <path>` — override default `.env/gke-tpu-cluster-scan.md`.

## Step 1 — Resolve projects

Parse arguments into a project list:
- Any arg starting with `--` is a flag (handle `--project`, `--skip-combined`, `--combined-path`).
- Any arg NOT starting with `--` is treated as a project name (bare-positional shorthand for `--project <arg>`).
- Default `combined_path` is `.env/gke-tpu-cluster-scan.md`; override via `--combined-path`.

Verify at least one project resolved — if zero, refuse with "specify at least one project".

For each project, do a fast existence check before doing real work:

```bash
gcloud projects describe "<project>" --format="value(name)" 2>&1
```

If the project doesn't exist or you lack access, surface and skip — don't fail the whole batch on one bad project.

## Step 2 — Run the probe (one project at a time, captured to file)

For each surviving project, invoke the bash probe with output redirected to a TSV file (DO NOT let the gcloud chatter into master context — that's the whole point of having the probe in a separate script):

```bash
TSV=/tmp/scan-gke-clusters-$$-<project>.tsv
SCANLOG=/tmp/scan-gke-clusters-$$-<project>.log
bash .claude/scripts/scan-gke-clusters.sh --project "<project>" > "${TSV}" 2> "${SCANLOG}"
EXIT=$?
```

Wall-clock expectation: ~30s-5min per project depending on number of clusters. Show the user a progress line: `Scanning <project>... (~N clusters, expect <T> sec)` based on the project's existing row count in the combined file.

If exit code is non-zero, read the last 20 lines of `${SCANLOG}` and surface to user. Common issues:
- `permission denied` → user needs `gcloud auth login` + the right roles for that project
- `quota exceeded` → kubectl request-throttling against the apiserver; rare with the probe's 5s timeouts
- `command not found: kubectl` → harness lacks kubectl; install via `gcloud components install kubectl`

## Step 3 — Write per-project file

For each successful TSV, write `.env/<project>-gke-tpu-cluster-scan.md` with the TSV inline. The per-project file is primarily a write-target for the merger and a human-readable "what was the last scan of project X" record; full Markdown table rendering can land in a future version. Inline TSV in a fenced code block + summary header is sufficient for v1.

```bash
OUT=".env/<project>-gke-tpu-cluster-scan.md"
N_ROWS=$(tail -n +2 "${TSV}" | wc -l)
N_TPU=$(tail -n +2 "${TSV}" | awk -F'\t' '$10 != "-" && $10 != ""' | wc -l)
N_READY=$(tail -n +2 "${TSV}" | awk -F'\t' '$5 == "Y" && $6 != "0" && $6 != "-"' | wc -l)
TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M UTC")

cat > "${OUT}" <<EOF
# \`<project>\` — GKE TPU cluster inventory

**Last scan**: ${TIMESTAMP}
**Clusters scanned**: ${N_ROWS}, **with TPUs**: ${N_TPU}, **RUNNING + TPU Ready**: ${N_READY}

## Source

Generated by \`/scan-gke-clusters <project>\` via \`.claude/scripts/scan-gke-clusters.sh --project <project>\`. The combined cross-project view is at \`.env/gke-tpu-cluster-scan.md\` (merged by \`.claude/scripts/merge_cluster_scan.py\`).

Re-run anytime — clusters' XPK + node-pool state changes between scans.

## Raw TSV (11 columns: project, cluster, location, status, xpk, tpu_ready, tpu_total, our_uses, xpk_type, topology, machine_type)

\`\`\`tsv
$(cat "${TSV}")
\`\`\`
EOF

echo "Wrote ${OUT}"
```

Skip this step if `--skip-combined` was passed (since per-project files are inputs to the combined merge; they're cheap to skip when the user only wants the side effect of running the probe).

## Step 4 — Merge into combined file

Skip this step entirely if `--skip-combined` was passed.

**Bootstrap if missing.** If `${combined_path}` doesn't exist (fresh checkout — `.env/` is gitignored — or accidental deletion — or intentional fresh start), seed a minimal scaffold before the merger runs:

```bash
combined_path="${combined_path:-.env/gke-tpu-cluster-scan.md}"

if [ ! -f "${combined_path}" ]; then
  mkdir -p "$(dirname "${combined_path}")"
  cat > "${combined_path}" <<'EOF'
# GKE TPU cluster inventory — source of truth

**Consult this file first when picking a cluster for a new XPK workload.** Refreshed via the `/scan-gke-clusters` skill (which wraps [`scan-gke-clusters.sh`](../.claude/scripts/scan-gke-clusters.sh) + [`merge_cluster_scan.py`](../.claude/scripts/merge_cluster_scan.py)).

**Last audit**: (none yet — first scan pending)

## Inventory by TPU type

## How to refresh this inventory

See `.claude/skills/scan-gke-clusters/SKILL.md`. Run `/scan-gke-clusters <project>` to refresh one project's rows.
EOF
  echo "Bootstrapped empty combined file at ${combined_path}"
fi
```

The merger's parser handles an empty `## Inventory by TPU type` block — no existing rows to delete; the project's new rows get inserted into newly-created TPU-gen sections.

**Run the merger** for each successful TSV:

```bash
python3 .claude/scripts/merge_cluster_scan.py \
  --tsv "${TSV}" \
  --combined "${combined_path}" \
  --project "<project>"
```

This rewrites `${combined_path}` in-place:
1. Deletes existing rows where `Project == <project>` (across all TPU-gen tables)
2. Inserts new rows for that project
3. Re-sorts each affected table per the existing rule (largest single-slice topology first, then cluster name)
4. Updates the `**Last audit**:` line with `+ <project> refreshed @ <timestamp>`

## Step 5 — Summarize to user

Report:

```
Scanned N projects (M succeeded, K skipped/failed):

  <project_A>: <Yes> — 12 clusters scanned, 8 with TPUs, 6 RUNNING + Ready
              → .env/<project_A>-gke-tpu-cluster-scan.md
              → combined file: replaced 8 rows, added 8 rows
  <project_B>: <No>  — gcloud auth failed; skipped
  ...

Combined file: .env/gke-tpu-cluster-scan.md (updated)
Inspect: head -40 .env/gke-tpu-cluster-scan.md
        grep "<project_A>" .env/gke-tpu-cluster-scan.md | wc -l

Commit with:
  (Note: .env/ is gitignored on this repo — outputs are local only.
   If you want to track this inventory in git, move outputs to a
   tracked path first.)
```

Surface any warnings from the merger (e.g., "couldn't determine TPU family for <cluster>") in this summary too.

## Failure modes to handle

- **No projects specified** — refuse, suggest `<project-name>` or `--project <p>` (repeatable)
- **Project doesn't exist / no access** — skip that project, surface in summary, continue with others
- **Probe script crashes mid-run** — `${TSV}` may be partial. Inspect the last few lines; if it ends with a complete row (no half-row), proceed; otherwise discard and surface "probe didn't complete cleanly for <project>"
- **Combined file missing** — bootstrap automatically per Step 4 (not an error; just a "first time on this checkout" signal)
- **TSV row count is dramatically different from existing combined row count for this project** (e.g., from 30 → 2) — surface to user as advisory: "project X went from 30 rows → 2 rows; significant drop. Sanity-check before merging." User decides whether to proceed or abort.
- **Merger fails** (parse error, etc.) — surface stderr; per-project file is still written; combined file is unchanged.
- **kubectl / gcloud not in PATH** — refuse with install hint: `gcloud components install kubectl`
- **Master timeout during a slow project scan** (>5 min) — the bash script's internal timeouts cap each cluster's probe at 30s; total wall-clock is bounded but can be long for large projects. Stream the log file's tail to surface progress (not just on completion).

## Cost expectations

- **Per project**: ~30s-5min wall-clock depending on cluster count (the existing batch script took 30-60 min for 5 projects = ~6-12 min/project on average). Most time is in gcloud + kubectl roundtrips, not local compute.
- **Per cluster**: ~5-10s (gcloud get-credentials + 4 kubectl calls + node-pools list)
- **Master context**: ~0 chatter — all gcloud/kubectl output is redirected to log file. Master only sees the summary line per project.

## What this skill does NOT do

- **Does not commit the output.** `.env/` is gitignored; user decides what to track.
- **Does not check occupancy.** That's a live query, not inventory. `/start-experiment` Step 6 handles it.
- **Does not detect gcsfuse or Spot.** New rows get `?` for these columns. Future versions could add this.
- **Does not update wiki/** or any other location — outputs live in `.env/` only.
- **Does not auto-discover projects.** User specifies projects explicitly.
- **Does not modify the existing per-cluster files** (e.g., `.env/gke-v5p-256-shared.md` — those are hand-curated detail files; this skill is for inventory, not per-cluster deep dives).

## See also

- `.claude/scripts/scan-gke-clusters.sh` — bash probe (multi-project; TSV output)
- `.claude/scripts/merge_cluster_scan.py` — Python merger (rewrites combined file in-place)
- `.env/gke-tpu-cluster-scan.md` — combined inventory (mutated by merger)
- `.env/<project>-gke-tpu-cluster-scan.md` — per-project files
- `/start-experiment` Step 5/6 — the downstream consumer of the inventory + occupancy check
- `SCHEMA.md` — wiki structure (the .env/ tier is operational config, gitignored, not part of the wiki itself)
