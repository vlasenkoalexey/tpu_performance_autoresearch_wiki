# sample-program.md — autoresearch program template

A starting point for a per-program operating contract. Copy this file to `wiki/experiments/<program-slug>/program.md`, fill in every `<PLACEHOLDER>`, and the autoresearch loop has everything it needs to run. The two worked examples in this repo ([Llama 3 8B](wiki/experiments/llama3_8B_autoresearch_optimization/program.md) and [Gemma 4 E4B](wiki/experiments/gemma4_autoresearch_optimization/program.md)) are concrete instantiations of this template — both filed before the template was extracted, so they read as real `program.md`s rather than as the template-with-blanks-filled-in. Use them as cross-reference if a placeholder below is ambiguous.

> **How to use this template**
>
> 1. **Copy** to `wiki/experiments/<program-slug>/program.md` (one program per (model, hardware) pair).
> 2. **Replace `<ANGLE_BRACKET_PLACEHOLDERS>`** — model identity, architecture, hardware, conda env, branch prefix. Leave the methodology, loop, and heuristics sections as-is unless your stack genuinely differs.
> 3. **Fill in (or stub out) the two model-specific Pallas tables** — *kernels to TRY* and *kernels to BUILD*. The structure carries over; the rows depend on your model's ops.
> 4. **Read SCHEMA.md** — `program.md` is the operating contract for *this* program; SCHEMA.md is the contract for the wiki overall. Both must be honored. In particular, the experiment template's `## Next hypotheses` requirement is what feeds your queue between runs.
> 5. **Pair with a [bottleneck reverse-index](wiki/analyses/2026-04-30-bottleneck-reverse-index.md) lookup** before formulating each hypothesis — saves rediscovering refutations.
>
> Sections marked `<!-- GENERIC -->` are stack-agnostic; sections marked `<!-- MODEL-SPECIFIC -->` need real values.

---

# performance-autoresearch — `<MODEL_NAME>` on `<HARDWARE>` via `<FRAMEWORK>`

Variant of Karpathy's [autoresearch](https://github.com/karpathy/autoresearch) adapted for **performance optimization** on a specific stack: `<ORG/MODEL_HF_ID>` running under `<FRAMEWORK>` on a `<HARDWARE>` host, fine-tuning on `<DATASET>` packed at a fixed `seq_len`. An AI agent modifies the trainer + sharding + compiler / runtime flags to maximize throughput.

**The model's output distribution is invariant.** The agent optimizes *how* the same computation runs — sharding, attention kernel, remat policy, XLA flags, layer implementation, training config — never the model architecture itself.

## Fixed bindings <!-- MODEL-SPECIFIC: every row's value -->

Single-environment program. These are the facts the loop must respect.

| Binding | Value |
|---|---|
| Hardware | `<TPU_GENERATION>`, **`<N_CHIPS>` chips**, `<HBM_PER_CHIP_GIB>` GiB HBM per chip, peak bf16 FLOP rate `<PEAK_BF16_TFLOPS>` TFLOP/s per chip (read from xprof_mcp `device_information`), peak HBM BW `<PEAK_HBM_BW_GBS>` GB/s per chip. HBM ridge point `<RIDGE_POINT>` FLOPs/byte. Mesh options: 1D (`fsdp=<N_CHIPS>`) or 2D (`dp=<X>,fsdp=<Y>`) etc. |
| Conda env | `<ENV_NAME>`; Python `<PYTHON_VERSION>`. Python binary: `/home/$USER/miniconda3/envs/<ENV_NAME>/bin/python`. |
| Trainer | `wiki/experiments/<program-slug>/<stack>/train.py`. `python -m train` from that folder. |
| Baseline command | `python -m train --steps 20 --batch_size 1 --seq_len <SEQ_LEN_BASELINE> --strategy fsdp --profile_dir $PROFILE_DIR --profile_steps 10 11 12`. `$PROFILE_DIR` = repo-root-anchored `raw/profiles/<YYYY-MM-DD>-<slug>/`. |
| Compiler / runtime env | `LIBTPU_INIT_ARGS`: per experiment. `XLA_FLAGS`: `--xla_dump_to=$HLO_DIR --xla_dump_hlo_as_text` recommended, other flags per experiment. **`--xla_tpu_*` flags go in `LIBTPU_INIT_ARGS`, not `XLA_FLAGS`** — XLA_FLAGS errors with `Unknown flags` otherwise. |
| libtpu version | `<LIBTPU_VERSION>` (confirmed `<DATE>`). When a flag is rejected as unknown, `strings $CONDA_PREFIX/lib/python<PY>/site-packages/libtpu/libtpu.so \| grep xla_tpu_<token>` is the source of truth. |
| Profile directory | `raw/profiles/<YYYY-MM-DD>-<slug>/` under the wiki repo root. **Gitignored.** |
| HLO dump directory | `raw/profiles/<YYYY-MM-DD>-<slug>/hlo/` (colocated). |
| xprof_mcp server | `xprof --logdir=<GCS_OR_LOCAL_LOGDIR> --port=<PORT>`. To make a captured profile queryable: upload the session dir to `<LOGDIR>/<run-name>/` (with the `plugins/profile/...` subtree inside), then `mcp__xprof__list_runs` reports it and it appears in the dropdown at `http://localhost:<PORT>/`. |
| xprof browser URL | **Per-run direct URL**: `http://localhost:<PORT>/?run=<run-name>` (TensorBoard-style — opens the interactive trace viewer for that run). Every experiment page **must** include this URL under `## Profile` alongside the on-disk path. Convention for `<run-name>`: the last path component of the profile directory. |
| Stack dimension | If multiple parallel execution stacks exist (e.g. **torchax** = HF-via-torchax and **jax** = from-scratch port), file writeups under `<stack>/experiments/`. Experiment numbers continue globally across stacks; the folder path + slug disambiguates. Include the stack word in the slug when ambiguous (e.g. `exp35-jax-splash-attention`). |
| Experiment page slug | `<YYYY-MM-DD>-exp<NN>-<short-slug>-<verdict-suffix>.md` in `<stack>/experiments/`. `<verdict-suffix>` ∈ { `accepted`, `rejected`, `potential` } per the rule below. The original baseline has no verdict suffix (it is the reference, not a hypothesis test). |
| Experiment **branch** | Each experiment is a git branch named `<BRANCH_PREFIX>-<YYYYMMDD>-exp<NN>-<short-slug>` (or `…-baseline`). The branch holds the exact `train.py` + `model/` + `data.py` state used for the run — the workload pulls a Docker image whose contents mirror that branch tip. Even env-only experiments get their own branch. Convention: branch from the most recent `-accepted` ancestor; document the parent as `branched_from:` in the experiment page frontmatter. |
| Experiment verdict suffix | **Rule**: once an experiment's verdict is final, the page filename MUST end with one of three suffixes before `.md`. `-accepted` for `keep` / `supported`. `-rejected` for `discard` / `refuted` / `crash` / `invalid`. `-potential` for `parked` / `inconclusive`. Suffix is part of the filename at file-creation time; rename on status change. Makes directory listings of `wiki/experiments/<program>/` self-summarizing. |
| Timeout per experiment | **15 minutes** wall-clock. Kill and mark `crash` otherwise. |

## Model constraints (architecture — off-limits) <!-- MODEL-SPECIFIC -->

These are fixed by the model identity and cannot be changed — changing them means you're training a different model.

| Field | Value |
|---|---|
| n_layers | `<N>` |
| n_heads | `<N>` |
| n_kv_heads | `<N>` (GQA `<RATIO>`:1) |
| head_dim | `<D>` |
| hidden_dim | `<D>` |
| intermediate (FFN) | `<D>` |
| vocab_size | `<V>` |
| max_position | `<L>` |
| `<MODEL_SPECIFIC_FIELD_1>` | `<value>` |
| `<MODEL_SPECIFIC_FIELD_2>` | `<value>` |
| tie_word_embeddings | `<true/false>` |

## The contract <!-- GENERIC -->

The final trained model must be equivalent to a baseline-trained model of the same architecture — same output distribution (bitwise up to floating-point rounding for a fixed seed/config). Everything about *how* that computation is expressed, scheduled, sharded, stored, or compiled is tunable.

## What you CAN do <!-- GENERIC -->

Anything preserving the output-distribution contract:

- Modify any file in `wiki/experiments/<program-slug>/<stack>/` (`train.py`, `model/sharding.py`, `data.py`). Also any text-only-forward monkey-patch in `train.py` if it preserves model semantics.
- **Training config**: `global_batch_size`, per-chip batch, `seq_len`, grad accumulation, `--strategy` (`fsdp` / `tp`), `--fsdp` / `--dp` / `--tp` mesh shape, `--dtype`, `--profile_*`, `--learning_rate`, `--warmup_steps`.
- **Environment / compiler**: any XLA flag or `LIBTPU_INIT_ARGS` value. Persistent compile cache (`JAX_COMPILATION_CACHE_DIR`).
- **Sharding**: mesh shape, axis names, `PartitionSpec` choices, FSDP/TP mix.
- **Attention kernel**: default (XLA through HF) → `tokamax.dot_product_attention` (splash) / `jax.experimental.pallas.ops.tpu.splash_attention` / custom Pallas — as long as numerically equivalent. GQA is native in splash — don't `jnp.repeat` K/V.
- **Remat policy**: `full` / selective / none, `jax.checkpoint_policies.save_and_offload_only_these_names`.
- **Optimizer implementation**: custom `scale_by_adam` with bf16 mu+nu, host-offload of opt state, AdamW variants.
- **Precision mix**: bf16 compute with fp32 master optional; fp8 acceptable if loss sanity passes.
- **Module structure**: fused QKV vs separate projections, different RoPE, scan-over-layers (`torchax.train.ScannedModule`), different residual fusion — provided math is preserved.
- **JIT boundaries**: where `jit` is placed, `donate_argnums`, `out_shardings`, `in_shardings`, `static_argnums`.
- **Data pipeline**: prefetch, packing, async host→device.
- **Pallas kernels** for any op with numerical equivalence.

## What you CANNOT do <!-- MOSTLY GENERIC; review the model-specific lines -->

- Change the **model architecture** per the table above. These define the parameter count and trained-model identity.
- Change `--model_id` away from `<MODEL_HF_ID>`. (Variant suffixes like `-it` are different models.)
- Quantize trained weights below bf16 (int8/int4 weight quantization is off-limits for this loop unless the program's metric explicitly admits it).
- Disable or approximate attention (linear attention, sliding-window on a full-attention layer are off). Swapping to a numerically-equivalent kernel is fine. **If your model has hybrid local/global attention, those layers must keep their local-mask semantics.** <!-- MODEL-SPECIFIC -->
- Skip / approximate the optimizer step, norm layers, or residual connections. Skip `<MODEL_SPECIFIC_INVARIANT, e.g. final_logit_softcapping>`.
- Modify anything outside `wiki/experiments/<program-slug>/<stack>/`. Wiki source pages, framework submodules (torchax, tokamax, HF transformers, etc.) are read-only from this program's perspective.
- Cheat the metric: skip or warp step-timing, fake the profile, log crashes as `discard`.

**If a framework / kernel-library / transformers source change seems necessary**: stop the loop and ask the human. Explain what you'd change, why, and what experiment it unblocks. Do not proceed until authorized.

## Hardware / parallelism constraints <!-- MOSTLY GENERIC; first two bullets need real numbers -->

- **Mesh divisibility**: every per-chip-shard axis must divide evenly into the mesh axis size. On `fsdp=<N>`, `global_batch_size ≥ <N>` and must be a multiple of `<N>`. Pre-check before proposing shape changes.
- **`num_kv_heads=<X>` does not divide `tp>=<Y>`**. K/V projections under TP with tp ≥ Y must be replicated. Known memory-leaving-on-the-table corner.
- **HBM budget**: track baseline peak HBM. **Memory-ceiling rule: win memory before throughput.** Structural order is *memory win → throughput win*, not the reverse.
- **Attention N² materialization**: the default (XLA-through-HF) path materializes the `[B, n_heads, S, S]` score tensor and OOMs at large (batch, seq). Splash attention avoids this.

## Pallas kernel landscape <!-- GENERIC: decision rules; tables MODEL-SPECIFIC -->

Two questions to ask on every profile before proposing an experiment:

1. **Which existing Pallas / Mosaic-TPU kernel could replace this op?** Default on this stack is `<framework> → JAX primitives → XLA → TPU MXU/VPU`. Pallas kernels substitute a **custom-call** path that keeps tiled intermediates in VMEM and typically wins on memory-bound ops.
2. **Which ops would benefit from a Pallas kernel that doesn't yet exist?** Build-candidates surface when (a) the op shows up in `loop fusion` with high HBM bytes_accessed and low flops_tf, (b) no upstream Pallas kernel covers it, and (c) XLA's existing fusion can't eliminate the HBM round-trip.

### Decision rule for "Pallas vs. XLA"

- **Compute-bound above the HBM ridge point** (OI > `<RIDGE_POINT>` FLOPs/byte): Pallas rarely wins. XLA's MXU lowering is hard to beat for dense GEMM.
- **Memory-bound below the ridge point**: Pallas candidate. Keep tiles in VMEM, fuse consecutive HBM round-trips.
- **Fusion of matmuls sharing an input**: helps **iff output shapes are similar**. `gate_proj` + `up_proj` are symmetric — good fuse. QKV under GQA are asymmetric (Q is N× K/V) — bad fuse.
- **Always profile first.** Proposing a Pallas kernel without a matched profile signal is speculation.
- **HLO pre-filter (MANDATORY for kernel-replacement hypotheses)**: before authoring any Pallas-replacement kernel, AOT-compile the baseline via `jax.jit(fn).lower(*args).compile()` or dump the post-optimization HLO (`XLA_FLAGS="--xla_dump_to=… --xla_dump_hlo_as_text"`) and grep for whether XLA already fuses your target pattern into an adjacent matmul (`kind=kOutput` Mosaic kernels). If it does, retire the hypothesis with reason `xla-already-fuses`. This is **required by [SCHEMA.md](SCHEMA.md) FORMULATE-HYPOTHESIS step 2b** — kernel-replacement hypotheses that skip this step fail LINT. See [AOT Compilation](wiki/concepts/aot-compilation.md) for the full workflow. This refuted the Pallas RMSNorm+matmul and SwiGLU+down_proj hypotheses in this wiki, saving weeks of kernel-authoring effort.

### Existing Pallas / Mosaic-TPU kernels to TRY <!-- MODEL-SPECIFIC: enumerate per-model -->

| Op in `<MODEL_NAME>` | Existing kernel | Current path | Expected win | Wiring |
|---|---|---|---|---|
| `<MODEL_NAME>Attention.forward` | `jax.experimental.pallas.ops.tpu.splash_attention` or `tokamax.dot_product_attention` | HF SDPA → framework lowering → XLA. Materializes full `[B, n_heads, S, S]` score tensor. | 15–40 % on attention. Native GQA; supports hybrid local-SW + global. Unlocks longer seq at bigger batch. | Monkey-patch `<MODEL_NAME>Attention.forward`; bridge via `torchax.interop.call_jax(splash_fn, q, k, v, mask)`. |
| Cross-entropy + LM head output | `tokamax.linear_softmax_cross_entropy_loss` (TPU Mosaic, `chunked_xla` impl preferred — see [bottleneck reverse-index](wiki/analyses/2026-04-30-bottleneck-reverse-index.md)) | Hand-rolled `log_softmax` + `gather`, materializes `[B, S, V]` fp32 logits. | Several GiB of HBM freed; can collapse CE bwd to ~0 % of step. | Replace hand-rolled CE with `tokamax.linear_softmax_cross_entropy_loss(hidden, lm_head.T, labels)`. |
| `<other op>` | `<kernel>` | `<current path>` | `<expected>` | `<wiring>` |

### Pallas kernels to BUILD (gaps in the ecosystem) <!-- MODEL-SPECIFIC: filter to ops profile says are dominant -->

Build only when profile justifies it. Each row below is a sketch — promote to a hypothesis page only when a profile points at it.

| Op | Why it's a build-target | Where in profile | Sketch | Expected |
|---|---|---|---|---|
| `<op>` | `<count of calls per fwd; HBM-bound; XLA-fallback only>` | `<profile bucket>` | `<kernel sketch>` | `<expected delta>` |

### When to propose vs. defer a new kernel <!-- GENERIC -->

- If the build cost is > 2 experiment cycles (~30 min) **and** the expected win < 5 %, **defer** and file it as a follow-up hypothesis.
- If a profile clearly points at a specific memory-bound hotspot > 10 % of step time with no existing Pallas coverage, **build**.
- Always check the [tokamax codebase page](wiki/codebases/tokamax.md) and the [Pallas kernel directory](wiki/analyses/2026-04-23-pallas-kernel-directory.md) before writing from scratch — many kernels exist but are not exposed via the public API.

## Known correctness bugs <!-- MODEL-SPECIFIC: usually short, sometimes empty -->

`<List any model-specific numerical or compile gotchas the loop must respect, e.g. "NaN loss at seq ≥ 2048", "checkpoint loads as multimodal-only", or remove this section if none apply.>`

**Loss sanity check** (GENERIC, mandatory) — required after changes that can affect numerics (attention kernel swap, precision change, custom Pallas, optimizer internals, init/seed change). Rerun for ≥ 20 steps and verify loss trajectory matches baseline within bf16-reorder noise at the same steps. If it diverges, mark `invalid` and revert.

**Simplicity criterion** (GENERIC):

- TPS win from **deleting** code → clear keep.
- ~1 % TPS win with 200 lines of fragile new code → probably discard; log the idea as a follow-up.
- No-op-or-faster plus simpler → always keep.

## Metric <!-- GENERIC structure; numbers MODEL-SPECIFIC -->

**Primary: TPS (tokens per second)** = `global_batch_size × seq_len / median_step_time_s`. Higher is better. Invariant under batch/seq tuning.

**Secondary: MFU** — sanity check. Use detailed matmul-FLOP accounting (not the `6PT` rule of thumb, which over-counts when the model has non-matmul params like PLE tables, embeddings under TP, or tied-weight setups; the right `P` is the matmul-only param count). If TPS rises but MFU falls, flag it in observations.

**Diagnostic: step_time** — human-readable signal. Not a decision metric.

**Measurement protocol**: median step_time over **steps 6–15** with `--steps 20`. Steps 0 and 1 are typically compiles (~150 s each on big LLMs). Short runs (< 10 steady-state steps) undercount slow outliers. Compile time is recorded separately; does not enter the metric.

## Output format — per run <!-- GENERIC -->

Extracted from the trainer's summary block + xprof_mcp `get_overview` + `get_memory_profile`:

```
tps:             <global_batch × seq_len / median step_time>
mfu_percent:     <detailed matmul FLOPs / (peak × wall time × n_chips)>
step_time_ms:    <median over steps 6-15; fall back to 2-<N-1> for short runs>
peak_hbm_gib:    <from get_memory_profile>
compile_seconds: <step 0 wall time — diagnostic only>
config:          <key flags / code change vs baseline, one-line>
```

## Ledger — `<stack>/experiments/RESULTS.tsv` <!-- GENERIC -->

One ledger per stack. Append one row per run (tab-separated, gitignored):

```
exp_id	date	tps	mfu_percent	step_time_ms	peak_hbm_gib	config	status	description
```

- `exp_id` — `exp<NN>` (or `baseline`). Numbering continues globally across stacks — folder path disambiguates.
- `status` ∈ `{keep, discard, crash, parked, inconclusive}`; the experiment-page filename's verdict suffix (`-accepted` / `-rejected` / `-potential`) must match.

## Observations log — `<stack>/experiments/OBSERVATIONS.md` <!-- GENERIC -->

One section per experiment. **The experiment page** (`<YYYY-MM-DD>-exp<NN>-<slug>-<verdict-suffix>.md` per [SCHEMA.md](SCHEMA.md)) remains the canonical per-experiment file; `OBSERVATIONS.md` is a **skim-and-reason** aggregation log for the human reviewer to thread through the session's arc.

Template per block (append-only, commit alongside code):

```markdown
### exp<NN> — <commit>  <one-line summary>

**Config**:
- Command diff from prior keep: <flag diffs + code change summary>
- Profile path: `raw/profiles/<YYYY-MM-DD>-<slug>/`
- **Profile browser URL**: `http://localhost:<PORT>/?run=<YYYY-MM-DD>-<slug>`
- HLO dump path: `raw/profiles/<YYYY-MM-DD>-<slug>/hlo/`
- Experiment page: `<YYYY-MM-DD>-exp<NN>-<slug>-<verdict-suffix>.md`

**Hypothesis**:
<2–4 sentences; what you expect and why. Cite profile signal / wiki page / prior follow-up.>

**Changes made**:
- <file:function — what was swapped — equivalence argument>
- <config flag change — old → new — why>

**Expected outcome**:
<TPS / MFU / HBM prediction + mechanism>

**Actual outcome**:
- TPS: X → Y (Δ Z%)
- MFU: A → B
- Step time: P → Q ms
- Peak HBM: M → N GiB
- Compile time: C → D s

**Profile signals**:
- Bottleneck (from `get_overview`): compute | memory | host | collective
- Top ops change (from `get_top_hlo_ops`): which ops moved, how bytes_accessed / FLOPs shifted
- HLO patterns: fusion formed/broke, collective placement, custom-call presence
- HLO-pass diff (if relevant, from `diff_hlo_stages`): what the compiler did differently

**Analysis**:
<If matched expected — why the mechanism worked. If not — what really happened, confounds, what it reveals about the system. If crash — root cause, and whether it invalidates the hypothesis or just the implementation. If numerics-affecting — report sanity loss vs baseline at a common step.>

**Decision**: keep | discard | crash | invalid

**Follow-ups** (ideas this surfaced — these become the experiment's `## Next hypotheses` per [SCHEMA.md](SCHEMA.md)):
- <idea 1 — what, why plausible>
- <idea 2 — ...>
```

## The experiment loop <!-- GENERIC -->

**Branch model (MANDATORY)**: each experiment lives on **its own branch**, forked from the current session-trunk tip (or another kept branch — see "hierarchical forking" below).

### Why branches matter

Each experiment branch is a **persistent rollback point**. At any future moment you can `git checkout <BRANCH_PREFIX>-<date>-exp<NN>-<slug>` to recover the exact code state that experiment ran on, read its `OBSERVATIONS.md` block, and start a new experiment from that state to explore an alternative direction. In-place editing on a single branch destroys that.

The branch structure is therefore a **tree of hypotheses**, not a linear history:
- The **trunk** (`<BRANCH_PREFIX>-<date>`) is the main line of compounding wins.
- **Side branches** are experiments run but not (yet) merged — discarded, crashed, or under evaluation.
- **Hierarchical forking**: a new experiment can fork from **any** kept branch in the tree, not only the current trunk tip. Use this when an earlier kept state is a cleaner ancestor for the new idea than the current trunk is.

### Naming and commit rules

- **Session trunk**: `<BRANCH_PREFIX>-<YYYYMMDD>`. Created once per session, branched from `main`. Holds only **kept** experiments.
- **Per-experiment branch**: `<BRANCH_PREFIX>-<YYYYMMDD>-exp<NN>-<short-slug>`. Forked from the session-trunk tip (or a chosen prior kept branch). Every code edit + experiment page + `OBSERVATIONS.md` block + `RESULTS.tsv` row commits **to this branch**, not to trunk.
- **Keep**: `git checkout <session-trunk>` + `git merge --no-ff <exp-branch>`. The `--no-ff` preserves a merge commit so the trunk history shows kept changes as discrete units.
- **Discard / crash**: `git checkout <session-trunk>`. Leave the experiment branch alone — unmerged but present, fully recoverable. If `OBSERVATIONS.md` on the discarded branch has useful follow-ups, cherry-pick just that file onto the trunk.

No `git reset --hard` in the happy path. Failed attempts are parked as unmerged branches for later review; the trunk's git log is a clean record of only the *kept* changes.

### LOOP FOREVER

**NEVER STOP**: Once the experiment loop has begun (after the initial setup), do NOT pause to ask the human if you should continue. Do NOT ask "should I keep going?" or "is this a good stopping point?". The human might be asleep, or gone from a computer and expects you to continue working *indefinitely* until you are manually stopped. You are autonomous. If you run out of ideas, think harder — read papers referenced in the code, re-read the in-scope files for new angles, try combining previous near-misses, try more radical architectural changes. The loop runs until the human interrupts you, period.

1. **State check.** Read the tail of `OBSERVATIONS.md` for recent context and the last `status: keep` row of `RESULTS.tsv`. The trainer source on the session trunk is at that kept state.
2. **Generate a hypothesis**, priority order:
   a. **Profile-driven** — highest-signal gap in the most recent profile: top slow op, low HBM BW utilization on bandwidth-bound op, collective wait, `async-collective-done` stall, missing fusion. Query `get_overview`, `get_top_hlo_ops`, `get_op_profile`, `get_memory_profile`. Cross-reference the [bottleneck reverse-index](wiki/analyses/2026-04-30-bottleneck-reverse-index.md) — *Tried & refuted* first, then *Standing levers*.
   b. **Follow-up** — an unexplored idea from a previous experiment's `## Next hypotheses` (the experiment template in [SCHEMA.md](SCHEMA.md) requires this section be populated).
   c. **Wiki-driven** — consult [scaling-book](wiki/codebases/scaling-book.md), [xprof-mcp TPU optimization guide](wiki/sources/2026-xprof-mcp-tpu-optimization.md), the relevant [concept page](wiki/concepts/) for the bottlenecked op.
   d. **Heuristics table below** — accumulated rules of thumb.

   **Within these, prefer structural changes (shape, sharding, code) over flag-only changes.** On already-decent configs, XLA/LIBTPU flag-only experiments tend to be null or noise unless they follow a structural change that unlocks them.

   **Memory-ceiling rule**: when the baseline is at 90 %+ HBM, memory-saving changes must come before any state-growing change.

3. **Implement** the hypothesis. One experiment = one `<YYYY-MM-DD>-exp<NN>-<slug>-<verdict-suffix>.md` page + code changes + `RESULTS.tsv` row + `OBSERVATIONS.md` block.
4. **Run** the baseline command with the hypothesis-adjusted config / env:
   ```bash
   cd wiki/experiments/<program-slug>/<stack>
   LIBTPU_INIT_ARGS="..." XLA_FLAGS="..." \
     python -m train --profile_dir $PROFILE_DIR --profile_steps 10 11 12 \
       --steps 20 --batch_size <B> --seq_len <S> [other flags] \
       2>&1 | tee /tmp/<program>_<exp>.log
   ```
5. **Classify the outcome**. A `CompileTimeHbmOom` or `RESOURCE_EXHAUSTED` log line by itself is not necessarily fatal — XLA may retry silently. Wait for a step-log line (success) OR a `RuntimeProgramAllocationFailure` followed by no further progress (crash). After timeout with no step summary → crash.
6. **Make the profile queryable**: upload the session dir to the xprof logdir under a descriptive name (`<program>_exp<NN>_<slug>_<YYYYMMDD>`) so xprof_mcp can access it later. Record the run name in the experiment page and the observation block.
7. **Extract metrics** via xprof_mcp:
   - `list_runs` → confirm the run is visible
   - `get_overview` → step time, device duty cycle, MFU when computed
   - `get_top_hlo_ops(limit=15)` → op time / FLOPs / bytes_accessed
   - `get_op_profile` → nested breakdown, HBM BW utilization per op
   - `get_memory_profile` → peak HBM, stack vs heap, fragmentation
   - For HLO-level changes: `list_hlo_modules`, `get_hlo_module_content`, `diff_hlo_stages` (needs HLO dumps enabled).
8. **Write up** the experiment page (full `experiment` template per [SCHEMA.md](SCHEMA.md), including the now-required `## Next hypotheses` section with at least one bullet per surfaced follow-up) + append to `OBSERVATIONS.md` + append to `RESULTS.tsv`. The **HLO-op diff table** (baseline vs this run, top ops, time / bytes deltas) is the single most diagnostic piece of evidence.
9. **Decision**:
   - **keep** — TPS improved beyond noise, no tracked-metric regression, loss trajectory within bf16-reorder noise. Merge the experiment branch into the session trunk.
   - **discard** — regression, no change, or correctness preserved but not worth the code complexity. Leave the experiment branch unmerged.
   - **crash** — OOM, compiler bug, infra failure. File the experiment page with `verdict: invalid` (or status `crash` in the ledger) and the root-cause analysis.
   - **invalid** — the change modified model semantics (loss sanity fails) or otherwise violated the contract. Mark the page `verdict: invalid`; do NOT report the measured number as a win.
10. **Loop.**

## Improving the approach itself <!-- GENERIC -->

If during experimentation a generalizable improvement surfaces (a better measurement protocol, a richer profile-reading heuristic, a new anti-cheat case, a new reference page to consult), commit the improvement **to this `program.md`** directly on the session trunk (methodology updates aren't experiments) and add a `## approach evolution` entry to `OBSERVATIONS.md`:

```markdown
### approach update — <date>
<what changed in program.md, why, and the experiment that revealed it>
```

## Heuristics accumulated <!-- MOSTLY GENERIC; prune to your stack as evidence builds -->

Rules of thumb, not invariants. Most of these surfaced from the worked Llama 3 / Gemma 4 programs and generalize; remove or qualify any that don't apply to your stack.

- **Flag-only experiments on a small workload often regress.** The stock XLA scheduler has usually found a good-enough schedule; giving it more freedom to fuse/reorder can break compute-side memory locality. Flag experiments become useful right after a structural change; prefer structural first.
- **`--xla_tpu_*` flags go in `LIBTPU_INIT_ARGS`, not `XLA_FLAGS`.** XLA_FLAGS errors with `Unknown flags` otherwise.
- **Flag-catalog drift vs installed runtime**: a named flag in a doc may not be in the installed libtpu. `strings libtpu.so | grep xla_tpu_<token>` is the source of truth.
- **HLO pre-filter for kernel-replacement hypotheses.** Before writing a Pallas kernel that fuses two ops, dump the post-optimization HLO and check whether XLA already fuses them in a `kind=kOutput` Mosaic kernel. This refuted multiple hypotheses cheaply in this wiki.
- **Tied-weight dedup in torchax `JittableModule` complicates `out_shardings`.** Building a sharding pytree from `weights.items()` for tied weights yields a collapsed single-device sharding for the duplicate; `jit` rejects the mismatch. Skip the explicit pin, or route around the dedup.
- **Measurement**: median step-time over steps 6–15 with `--steps 20`. Steps 0 and 1 are both compiles. Short runs (< 10 steady-state steps) undercount slow outliers.
- **Bytes-accessed is the diagnostic metric** for reorder-driven regressions. Wall-clock alone is ambiguous; HLO-op bytes_accessed shifts decide the mechanism.
- **Splash attention supports GQA natively.** Don't pre-split K/V with `jnp.repeat` — it wastes K/V memory and HBM bandwidth.
- **HBM ratchet**: once at 90 %+ HBM, every memory-saving change unlocks a potential throughput change (bigger batch, longer seq, less remat). Track peak HBM per experiment; when it drops, immediately queue the now-tryable state-growing change as a follow-up.
- **Compile time dominates short runs.** Step 0 + step 1 recompile can total ~300 s. `scan-over-layers` collapses N-layer unroll to one scan-body compile; consider it for any program with > 16 layers.
- **SparseCore offload of FSDP collectives** (`xla_tpu_enable_sparse_core_collective_offload_{all_reduce,reduce_scatter,all_gather}`): all three together is the win; each individually is small.

## AOT screening protocol <!-- GENERIC -->

Two AOT (ahead-of-time) analysis workflows supplement the main experiment loop. Both use JAX's `jit → lower → compile` pipeline to inspect what XLA will do **before** burning TPU time. See [AOT Compilation](wiki/concepts/aot-compilation.md) for the concept page and [HLO Dumping and Diffing](wiki/concepts/hlo-dumping-and-diffing.md) for the dump-file workflow.

### Use case 1: HLO pre-filter for kernel-replacement hypotheses

**When**: before ranking any hypothesis that proposes replacing XLA-generated code with a Pallas/Mosaic kernel (fusing ops, custom matmul prologue, custom norm+matmul, etc.).

**Status**: **MANDATORY** per [SCHEMA.md](SCHEMA.md) FORMULATE-HYPOTHESIS step 2b. Kernel-replacement hypotheses that skip this step fail LINT.

**Steps**:

1. **AOT-compile the baseline** (no code changes needed):
   ```python
   lowered = jax.jit(train_step, donate_argnums=(0, 2),
                     out_shardings=out_shardings).lower(*args)
   compiled = lowered.compile()
   ```
   Or capture via dump files:
   ```bash
   XLA_FLAGS="--xla_dump_to=/tmp/hlo --xla_dump_hlo_as_text" \
     python -m train --steps 1
   ```

2. **Inspect the post-optimization HLO** for the target fusion pattern:
   ```bash
   # Grep for Mosaic fused kernels containing your target op
   grep -A 20 'kind=kOutput' /tmp/hlo/*.after_optimizations.hlo \
     | grep -i 'rmsnorm\|rsqrt\|silu\|multiply'
   ```
   Or via xprof-mcp (works on CPU, no xprof server needed):
   ```
   list_hlo_dump_modules(dump_dir="/tmp/hlo")
   get_hlo_dump(dump_dir="/tmp/hlo", module_id="module_0262",
                stage="after_optimizations")
   ```

3. **Decision**:
   - If XLA already fuses the target pattern → **retire** the hypothesis with `status: retired`, `hlo_prefilter: refuted`, reason `xla-already-fuses`. Record the `fused_computation` name as evidence.
   - If XLA does **not** fuse it → hypothesis passes. Set `hlo_prefilter: passed` and proceed to ranking.

**Evidence from this wiki**: the Llama 3 Pallas RMSNorm+matmul and SwiGLU+down_proj hypotheses were both refuted this way in 30 minutes (2026-04-27 log entry), saving weeks of kernel-authoring effort.

### Use case 2: Pre-experiment AOT screening

**When**: before a full 20-step TPU run, for any hypothesis where you want an early sanity check.

**Status**: Optional but recommended, especially for sharding/config/flag changes. Specified in [SCHEMA.md](SCHEMA.md) RUN-EXPERIMENT step 1b.

**Steps**:

1. **AOT-compile both baseline and modified versions**:
   ```python
   # Baseline
   baseline_compiled = jax.jit(baseline_step).lower(*args).compile()
   baseline_cost = baseline_compiled.cost_analysis()

   # Modified
   modified_compiled = jax.jit(modified_step).lower(*args).compile()
   modified_cost = modified_compiled.cost_analysis()
   ```

2. **Compare cost analyses**:
   ```python
   for b, m in zip(baseline_cost, modified_cost):
       print(f"FLOPs:  {b['flops']:.2e} → {m['flops']:.2e}")
       print(f"Bytes:  {b['bytes accessed']/1e9:.2f} → {m['bytes accessed']/1e9:.2f} GB")
   ```

3. **Decision**:
   - Compilation failure (OOM, shape mismatch) → fix or abandon before TPU launch.
   - Cost model shows regression → reconsider hypothesis.
   - Cost model shows improvement or is neutral → proceed to full TPU run. Note that `cost_analysis()` uses the [XLA cost model](wiki/concepts/xla-cost-model.md) (static estimates, not wall-clock) — it is directional, not precise.

### Use case 3: Offline HLO analysis (customer dumps)

**When**: a customer provides HLO dump files but no TPU access. The agent diagnoses sharding, fusion, and collective patterns from the files alone.

**Steps**:

1. Point xprof-mcp dump tools at the customer's dump directory.
2. Use `list_hlo_dump_modules` to catalog available modules.
3. Use `get_hlo_dump` with `stage="after_optimizations"` to read the final HLO.
4. Use `diff_hlo_stages` to compare pre- vs post-optimization.
5. Use `get_hlo_dump_neighborhood` to trace specific ops' producer/consumer chains.
6. File findings as an [analysis page](SCHEMA.md) or respond directly.

No TPU, no xprof server, no training run required — the dump tools work entirely on CPU.

## Reference material at a glance <!-- GENERIC -->

- Bottleneck diagnosis: [xprof — overview page](wiki/sources/2026-xprof-overview-page.md), [xprof — roofline model](wiki/sources/2026-xprof-roofline-model.md), [xprof — HLO op stats](wiki/sources/2026-xprof-hlo-op-stats.md), [xprof — HLO op profile](wiki/sources/2026-xprof-hlo-op-profile.md), [xprof — memory profile](wiki/sources/2026-xprof-memory-profile.md), [xprof — trace viewer](wiki/sources/2026-xprof-trace-viewer.md).
- Crown jewel: [xprof-mcp — TPU optimization guide](wiki/sources/2026-xprof-mcp-tpu-optimization.md) — roofline, dimension alignment, dtype, fusion, remat, KV cache, decision trees, XLA flag catalog.
- **Bottleneck reverse-index**: [analyses/2026-04-30-bottleneck-reverse-index.md](wiki/analyses/2026-04-30-bottleneck-reverse-index.md) — read before formulating each hypothesis; saves rediscovering refutations.
- **Pallas kernel directory**: [analyses/2026-04-23-pallas-kernel-directory.md](wiki/analyses/2026-04-23-pallas-kernel-directory.md) — ~200 kernels across ~30 repos.
- Attention: [flash-attention](wiki/concepts/flash-attention.md), [splash-attention](wiki/concepts/splash-attention.md), [attention-block-sizes](wiki/concepts/attention-block-sizes.md), [tokamax — splash attention](wiki/sources/2026-tokamax-splash-attention.md), [tokamax — autotuning](wiki/sources/2026-tokamax-autotuning.md).
- Sharding / parallelism: [fsdp](wiki/concepts/fsdp.md), [tensor-parallelism](wiki/concepts/tensor-parallelism.md), [sharding](wiki/concepts/sharding.md), [collective-communication](wiki/concepts/collective-communication.md), [reduce-scatter](wiki/concepts/reduce-scatter.md), [all-gather](wiki/concepts/all-gather.md), [ici](wiki/concepts/ici.md).
- Remat / compile: [rematerialization](wiki/concepts/rematerialization.md), [scan-over-layers](wiki/concepts/scan-over-layers.md), [xla-fusion](wiki/concepts/xla-fusion.md), [hlo-dumping-and-diffing](wiki/concepts/hlo-dumping-and-diffing.md), [aot-compilation](wiki/concepts/aot-compilation.md), [xla-flags](wiki/concepts/xla-flags.md), [async-collectives](wiki/concepts/async-collectives.md), [latency-hiding-scheduler](wiki/concepts/latency-hiding-scheduler.md), [custom-call](wiki/concepts/custom-call.md), [pallas-kernel](wiki/concepts/pallas-kernel.md).
- Kernels library: [tokamax codebase](wiki/codebases/tokamax.md), [tokamax — supported ops](wiki/sources/2026-tokamax-supported-ops.md), [tokamax — basic usage](wiki/sources/2026-tokamax-basic-usage.md).
- Runtime: [torchax codebase](wiki/codebases/torchax.md) — `JittableModule`, `interop.jax_view`, `jax_shard_map`, `ScannedModule`.
- Prior art: [jax-huggingface codebase](wiki/codebases/jax-huggingface.md) + the four `2026-jax-huggingface-part-{1,2,3,4}.md` source pages.
- MCP tools: [xprof-mcp codebase](wiki/codebases/xprof-mcp.md) — 18 tools.
- Methodology root: [autoresearch codebase](wiki/codebases/autoresearch.md).
- Operating contract: [SCHEMA.md](SCHEMA.md) (wiki-wide rules).
- Worked examples: [Llama 3 8B program.md](wiki/experiments/llama3_8B_autoresearch_optimization/program.md), [Gemma 4 E4B program.md](wiki/experiments/gemma4_autoresearch_optimization/program.md).
