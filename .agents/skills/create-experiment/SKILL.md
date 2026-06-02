---
name: create-experiment
description: Bootstrap a new model family for the autoresearch loop. Creates the folder structure under wiki/experiments/, scaffolds the model-level program.md from a template (asking the user about lanes, sizes, hardware targets, sequence length, and architecture invariants), optionally creates lane-level program.md stubs, and creates model page stubs under wiki/models/. Invoke once per new model family before /start-experiment can run on it.
---

You are bootstrapping a new model family for the autoresearch optimization loop. Follow this sequence — ask questions, then create files. Do NOT silently write files without confirming with the user.

## Step 1 — Gather model details via AskUserQuestion

Ask these questions in order (some may be combined into a single AskUserQuestion call with multiple questions):

**Question 1**: "Model folder slug?" (free-text input expected)
- This becomes the folder name under `wiki/experiments/`. Convention: lowercase, underscores, no spaces.
- Examples: `gemma4`, `gemma5`, `qwen3_8B`, `llama4_70B`.
- The full folder will be `wiki/experiments/<slug>_autoresearch_optimization/`.

**Question 2**: "Model display name?" (free-text)
- Human-readable name for documentation. Used in the model-level program.md title.
- Examples: "Gemma 4", "Gemma 5", "Qwen3 8B", "Llama 4 70B".

**Question 3**: "Which lanes?" (multi-select)
- Options: `tpu (PyTorch eager on TPU)`, `jax (JAX + Flax NNX)`, `torchax (torchax bridge)`, `maxtext (MaxText)`. User can also type a custom lane name.
- The lane folders will be created under `wiki/experiments/<slug>_autoresearch_optimization/`.

**Question 4**: "Model sizes?" (free-text, comma-separated)
- Examples: `"3B, 24B"`, `"1B, 8B, 70B"`, `"125M, 1.3B"`.
- These populate the `sizes:` field in model page frontmatter and the architecture description.

**Question 5**: "Target hardware variants?" (free-text, comma-separated)
- Examples: `"v5p-8, v5p-32, v6e-16"`, `"v6e-8, v6e-32"`.
- These populate the `hardwares:` field. Used to build the variant matrix on the model page.

**Question 6**: "Target sequence length for MFU optimization?" (number input)
- Default: 8192.
- Examples: 8192 (most modern LLMs), 4096, 16384.

**Question 7** (optional): "Architecture invariants?" (free-text, multiline)
- Things that must NOT change without approval. Examples: "8 parallel tracks, 4 experts top-2 routing", "GLU activation, fused attention", etc.
- Skip if user has nothing specific yet — they can fill in later.

**Question 8** (optional): "Trainer entry-point pattern?" (free-text)
- Default: `torchtitan.experiments.<lane>.<slug>.train_minimal` (matches the existing convention).
- User can override if their model uses a different entry pattern.

## Step 2 — Confirm the plan

Before writing any files, summarize what will be created and ask the user to confirm via AskUserQuestion:

```
About to create:
  wiki/experiments/<slug>_autoresearch_optimization/
    program.md                          (model-level with consolidated Per-lane operational details, has TODO markers)
    <lane1>/.gitkeep                    (keeps empty experiment-page folder tracked)
    <lane1>/README.md                   (stub, ~20 lines)
    <lane2>/...                         (one per selected lane)
  wiki/models/
    <slug>-<lane1>.md                   (model page stub for variant matrix)
    <slug>-<lane2>.md
    ...

Proceed?
```

Options: `Yes, create`, `Modify` (let user edit answers), `Cancel`.

## Step 3 — Create the folder structure

```bash
SLUG="<from question 1>"
EXP_DIR="wiki/experiments/${SLUG}_autoresearch_optimization"
mkdir -p "${EXP_DIR}"

for LANE in <selected lanes>; do
  mkdir -p "${EXP_DIR}/${LANE}"
  # .gitkeep so the empty experiment-page folder is tracked until first experiment lands
  touch "${EXP_DIR}/${LANE}/.gitkeep"
done
```

## Step 4 — Write model-level program.md

Use this template, substituting the answers from step 1:

```markdown
---
title: "autoresearch — <DISPLAY_NAME> (model-family overrides)"
type: program
model: <SLUG>
created: <today's date>
updated: <today's date>
---

# autoresearch — <DISPLAY_NAME> (model-family overrides)

Model-family specialization for the **<DISPLAY_NAME>** family. Inherits from `../program.md`; overrides the sections below.

See `../program.md` for the inheritance rules. Sections defined here fully replace the parent's; sections not defined here inherit unchanged.

## Setup

The repo contains <N> execution lane(s) for the same model architecture:

| Lane | Stack | Trainer entry point |
|------|-------|---------------------|
<one row per selected lane, using Q9's trainer pattern>

Model code lives in `raw/code/torchtitan/torchtitan/experiments/<lane>/<SLUG>/` (typical — adjust if your code lives elsewhere).

**Model sizes**: <from Q4> (architecture-specific layer/track counts: TODO fill in).

**Architecture invariants** (do NOT change without approval):
<from Q8, or "TODO: list invariants once architecture is documented">

Before starting:
- Read this file (model-level) and the root `../program.md`.
- Read the lane `<lane>/README.md` (hardware/cluster operational notes).
- Read the model page: `wiki/models/<SLUG>-<lane>.md`.
- Read the last 2–3 experiment pages in your lane.

## <MODEL>-specific CAN additions

(Additive on top of root `program.md`'s "What you CAN do". Root section still applies.)

- **Preferred edit target**: `torchtitan/experiments/<lane>/<SLUG>/` — model code, configs, lane-specific wrappers.
- TODO: list any other model-specific edit targets (monkey-patches, etc.)
- TODO: lane-specific operational flags — see Per-lane operational details below.

## <DISPLAY_NAME>-specific CANNOT additions

(Additive on top of root `program.md`'s "What you CANNOT do".)

- TODO: list model-specific prohibitions (e.g. "do not change attention pattern", "do not skip MoE routing")
- TODO: any specific dtype/precision rules

## The goal

Maximize MFU at each model size on each hardware target. **Target sequence length: <Q6>.**

TODO: any model-specific framing (e.g. "JAX lane is the reference ceiling" for cross-lane comparisons).

## Branching model — branch naming

Inherits the parent's fork-per-experiment pattern. Project-level branch naming:

```
<SLUG-as-kebab>-${LANE}-$(date +%Y%m%d)-v${EXP_ID}-${SLUG}
```

Example: `<slug-kebab>-tpu-20260520-v001-baseline`.

**Trunk branch**: TODO (e.g. `<USER>_<SLUG>` at `raw/code/torchtitan/`).

**Docker image base name**: TODO (e.g. `torchtitan-container`). Full image tag = `<base>:<branch-name>`.

**Per-experiment fork path**: `wiki/experiments/<SLUG>_autoresearch_optimization/<lane>/.repo/<EXP_NAME>/torchtitan/`.

## Profile + HLO storage

Both profile and HLO dump for an experiment live under the same GCS slug folder. Path includes the model name to avoid collisions with other model families sharing the bucket:

```
gs://<your-bucket>/autoresearch/<MODEL_NAME>-<lane>-v<NNN>-<slug>/
├── plugins/profile/...
└── hlo/module_NNNN.*.{txt,pb}
```

Where `<MODEL_NAME>` = `<SLUG-as-kebab>` (auto-derived from the model folder name).

TODO: confirm the bucket name and write permissions before first run.

## Per-lane operational details

All selected lanes are covered in this file (consolidated, not split into per-lane `program.md` files — the lane-level layer in the inheritance hierarchy is optional and unused by default).

### <lane1> — <stack from Q3>

**Trainer entry**: <from Q9, substituted>

**Mandatory env vars on every launch**:
```
TODO: lane-specific env vars (e.g. LIBTPU_INIT_ARGS, JAX_COMPILATION_CACHE_DIR)
```

**Quirks**: TODO

**Known hang surfaces**: TODO

**Kernels available**: TODO

**Lane-specific CAN/CANNOT additions**: TODO

<repeat per selected lane>

## Sources

- Model pages: <one path per lane: wiki/models/<SLUG>-<lane>.md>
- Lane READMEs: <one path per lane>
- Cluster docs: `.env/` directory at repo root.
- Wiki schema: `SCHEMA.md`.
- Parent program: `../program.md`.
```

## Step 5 — Write lane-level README stubs (per selected lane)

For each lane, write `<lane>/README.md` stub. (No lane-level `program.md` — all lane-specific operational content is consolidated into the model-level `program.md`'s "Per-lane operational details" section per step 4.)

```markdown
# <DISPLAY_NAME> — <lane> lane

TODO: hardware notes specific to this lane (cluster names, special LIBTPU flags, kernels available, known bugs).

## How to run (smoke test)

```bash
TODO: launch command template (xpk workload create ... or local python ...)
```

## Recent issues / debugging notes

(append as encountered)
```

## Step 6 — Write model page stubs (one per lane)

For each lane, write `wiki/models/<SLUG>-<lane>.md`:

```markdown
---
title: "<DISPLAY_NAME> — <lane>"
type: model
architecture: <SLUG-as-kebab>
lane: <lane>
sizes: [<from Q4 as YAML list>]
hardwares: [<from Q5 as YAML list>]
tags: [<SLUG-as-kebab>, <lane>]
created: <today's date>
updated: <today's date>
---

# <DISPLAY_NAME> — <lane>

TODO: 1–3 sentence overview of this model on this lane.

## Target metrics

- Primary: MFU at seq_len=<Q6>
- Secondary: tokens/sec, step time, peak HBM

## How to run

```
TODO: launch command template, parameterized by size and hardware
```

## Variant matrix

| Size | Hardware | Status | Baseline (step / TPS / MFU) | Current best (step / TPS / MFU) | Open hyps | Frontier exp |
|------|----------|--------|-----------------------------|---------------------------------|-----------|--------------|
<one row per (size, hardware) combination from Q4 × Q5, status="open">

## Cross-variant open hypotheses

(none yet — file under wiki/hypotheses/ and link here)

## Variant-specific open hypotheses

(none yet)

## Retired hypotheses

(none yet)

## Knobs translation matrix

| Technique | <variant 1> | <variant 2> | ... | Notes |
|-----------|-------------|-------------|-----|-------|
(populated after first cross-variant validation experiments)

## Iteration ladder

TODO: ordered roadmap, typically smallest size on smallest hardware first
```

## Step 7 — Report and next steps

Surface to the user:

- Files created (full list of paths).
- TODOs that remain in the templates (model-level program.md has ~5 TODOs the user should fill in).
- Next steps:
  1. Fill in the TODO markers in the model-level program.md (architecture invariants, branching trunk name, docker image base, etc.)
  2. Set up the model code fork in `raw/code/torchtitan/` (or wherever the model code lives) and create the trunk branch
  3. Write a baseline experiment manually (or via `/start-experiment` once you've established hardware availability)
  4. Run `/start-experiment <SLUG> <lane> --parallelism 1` for the first experiment

## What this skill does NOT do

- **Does NOT create the model code repo** — the model's code lives under `raw/code/<repo>/` and should be set up separately (clone, fork, initial commit).
- **Does NOT create cluster config** — `.env/` cluster files are shared infra. Add new clusters there, not per-model.
- **Does NOT auto-populate operational env vars** — those depend on the lane and runtime; user fills in the TODOs after initial bootstrap.
- **Does NOT start the loop** — that's `/start-experiment`'s job. This skill just creates the scaffolding so `/start-experiment` has something to resolve.

## Failure modes to handle

- **Slug collides with existing folder**: refuse and ask user to pick a different slug or confirm overwrite.
- **No lanes selected**: refuse — at least one lane is required.
- **Invalid characters in slug** (spaces, uppercase except where conventional, etc.): suggest a cleaned-up version, ask user to confirm.
