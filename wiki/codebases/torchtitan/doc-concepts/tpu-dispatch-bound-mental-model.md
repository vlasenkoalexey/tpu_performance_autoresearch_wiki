---
title: TorchTPU performance mental model - compile, or be dispatch-bound
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/torch-tpu-optimization-guide.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# TorchTPU performance mental model - compile, or be dispatch-bound

## Definition
Every XLA program TorchTPU runs is dispatched by the host, and the TPU idles between launches.
Uncompiled, each op is its own program, so a naive model spends much of each step **idle between
tiny programs** (dispatch-bound) rather than compute-bound. The guide reduces all optimization to
two moves: (1) **raise work per launched program** (bigger matmuls, bigger batch) and
(2) **reduce the number of host dispatches** (compile blocks, fused kernels, compile the glue,
or capture the whole step). The single most useful number is the **idle percentage** in an xprof
op-profile.

## In torchtitan (grounded)
The guide maps each lever onto a TPU-lane knob; the deep pages are linked per row.

| Lever | Knob / symbol | Page |
|---|---|---|
| Compile each transformer block | `compile.enable`, `compile.mode="layer"` ([`TpuTrainerCompileConfig.mode`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TpuTrainerCompileConfig.mode)); core [`apply_compile`](../catalog/torchtitan/distributed/compile.md#apply_compile) | [tpu-per-block-torch-compile](tpu-per-block-torch-compile.md) |
| Defer and fuse the eager remainder | [`TPUConfig.eager_mode`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TPUConfig.eager_mode) | [tpu-defer-and-fuse-eager-mode](tpu-defer-and-fuse-eager-mode.md) |
| Fused loss (one `custom_call`, no logits) | [`PallasCrossEntropyLoss`](../catalog/torchtitan/experiments/tpu/loss.md#PallasCrossEntropyLoss) | [tpu-fused-linear-cross-entropy](tpu-fused-linear-cross-entropy.md) |
| Fused attention | [`SplashAttentionKernelConfig`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#SplashAttentionKernelConfig) | [tpu-splash-attention-tiles-and-vmem](tpu-splash-attention-tiles-and-vmem.md) |
| Compile optimizer / grad-norm glue | [`TpuTrainerCompileConfig.optimizer_compile`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TpuTrainerCompileConfig.optimizer_compile), [`TpuTrainerCompileConfig.compile_grad_norm`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TpuTrainerCompileConfig.compile_grad_norm) | [tpu-per-block-torch-compile](tpu-per-block-torch-compile.md) |
| Whole step as one program | [`TpuGraphTrainer`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer) | [tpu-graph-trainer-memory-policies](tpu-graph-trainer-memory-policies.md) |
| Memory to afford bigger batch | SimpleFSDP + MP policy | [tpu-simplefsdp-and-mixed-precision](tpu-simplefsdp-and-mixed-precision.md) |

MFU accounting: the lane exposes [`TPUConfig.enable_mfu_benchmark`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TPUConfig.enable_mfu_benchmark)
(one aggregate MFU over steps from `mfu_benchmark_start_step` to the end) and a MaxText-style FLOP
formula [`get_maxtext_decoder_nparams_and_flops`](../catalog/torchtitan/experiments/tpu/mfu_flops.md#get_maxtext_decoder_nparams_and_flops);
for MoE the guide insists on **active** params in `num_flops_per_token`.

## Why it matters / when it applies
**Classify the bottleneck first (profile a few steady-state steps):**
- High idle -> dispatch-bound (common for small model / small batch): apply compile + fused kernels.
- Matmuls near peak -> compute-bound: gains need bigger problems; residual glue is the ceiling.
- High HBM traffic / OOM -> memory-bound: fused CE kernel, FSDP, recompute/offload.

**Arithmetic intensity (dense-specific).**
- Per-device batch is often the single largest MFU lever at small scale - push it to the HBM limit
  (the fused CE kernel frees room).
- MXUs are 128x128 or 256x256 by generation; FLOPs per matmul scale with `dim^2` while dispatch cost
  is ~constant. Use hidden dims that are **multiples of 256**; moving a debug dim 1024 -> 2048 can
  roughly double MFU from MXU utilization alone.

**Small stuff (general).**
- Keep norms in fp32 when casting manually (autocast already does); see
  [`TPUConfig.enable_amp`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TPUConfig.enable_amp).
- Avoid host syncs in the step loop (`.item()`, `.cpu()`, printing tensors, Python branches on
  tensors, per-step loss logging) - each stalls dispatch.
- Disable per-op Python validators (shape checks) in benchmark runs.
- The lane also defaults [`TPUConfig.bld_block_layout`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TPUConfig.bld_block_layout)
  to True: dense Llama3/Qwen3 blocks compute on `[B, L, ...]` views because folded `[T, ...]` tensors
  make XLA pick slow layouts (not in the guide; see [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md)).

**The dispatch ceiling.** Even with per-block compile and fused kernels, optimizer step, loss,
embedding and layout ops remain separate programs; collapsing the transformer into one graph does
**not** lower the idle fraction, because the idle is *around* the transformer. A well-sized dense
model with per-block compile + fused CE typically lands in the "low-to-mid tens of percent" MFU;
going further means shrinking the eager surface or capturing the whole step with GraphTrainer.

**Quick-start checklist (dense):** profile -> compile blocks (`backend="tpu"`, static shapes) ->
size dim/batch -> fused CE + splash, tune tiles -> SimpleFSDP `fully_shard` with
bf16-param/fp32-reduce -> norms fp32, dims % 256, checks off -> re-profile -> GraphTrainer when only
glue idle remains -> scan / graph splitter + offload when one unrolled graph no longer fits.

## Connections
- Code concepts: [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md),
  [trainer-and-train-loop](../concepts/trainer-and-train-loop.md),
  [tpu-graph-trainer](../concepts/tpu-graph-trainer.md),
  [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md),
  [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md),
  [debug-and-profiling-tools](../concepts/debug-and-profiling-tools.md),
  [llama3-model](../concepts/llama3-model.md)
- Module catalogs: [tpu_job_config](../catalog/torchtitan/experiments/tpu/tpu_job_config.md),
  [mfu_flops](../catalog/torchtitan/experiments/tpu/mfu_flops.md),
  [llama3/config_registry (tpu)](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md)
- Related doc-concepts: all pages above, plus
  [tpu-scan-graph-splitter-cpu-offload](tpu-scan-graph-splitter-cpu-offload.md),
  [tpu-moe-kernel-switches](tpu-moe-kernel-switches.md),
  [tpu-launch-and-profiling-workflow](tpu-launch-and-profiling-workflow.md),
  [tpu-recipe-matrix](tpu-recipe-matrix.md), [tpu-recipe-precision-and-throughput-accounting](tpu-recipe-precision-and-throughput-accounting.md)

## Source
Extracted from `torchtitan/experiments/tpu/torch-tpu-optimization-guide.md` (sections 1-3, 6, 7 and
the quick-start checklist; kept in place). The guide self-describes as work in progress.
