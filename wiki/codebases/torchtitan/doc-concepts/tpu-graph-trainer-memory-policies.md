---
title: Whole-step capture with TPU GraphTrainer and its memory policies
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/torch-tpu-optimization-guide.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Whole-step capture with TPU GraphTrainer and its memory policies

## Definition
Per-block `torch.compile` leaves the glue between blocks eager and the loss and optimizer as separate
programs. **GraphTrainer** removes that surface: it traces the whole training step (forward, loss,
backward, optionally the optimizer step) ahead of time with `make_fx` into one FX graph, runs graph
passes over it, and compiles the result for TPU so forward+loss+backward run as **one XLA program**.
Activation memory is then governed by a graph-level **memory policy** (save / recompute / offload per
tensor) instead of eager `checkpoint()`.

## In torchtitan (grounded)
- Trainer: [`TpuGraphTrainer`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer);
  a recipe opts in by returning a [`TpuGraphTrainer.Config`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer.Config),
  typically built with [`from_tpu_trainer_config`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer.Config.from_tpu_trainer_config)
  from a regular TPU recipe; [`start_trainer`](../catalog/torchtitan/experiments/tpu/train.md#start_trainer)
  dispatches on the config type. The step trace is [`_make_fx_forward_backward_step`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer._make_fx_forward_backward_step).
- Compile policy: [`TpuGraphTrainerCompileConfig`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig)
  (on top of upstream [`GraphTrainerCompileConfig`](../catalog/torchtitan/experiments/graph_trainer/configs.md#GraphTrainerCompileConfig),
  whose `mode` defaults to `"aot_fx_trace"`). Key fields:
  [`memory_policy`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig.memory_policy),
  [`save_regions`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig.save_regions),
  [`save_last_n_layers`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig.save_last_n_layers),
  [`optimizer_compile`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig.optimizer_compile)
  (`eager` | `separate_graph` | `in_graph`),
  [`compile_grad_norm`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig.compile_grad_norm),
  [`enable_remat_barriers`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig.enable_remat_barriers),
  [`fsdp_barrier_policy`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig.fsdp_barrier_policy).
  Validation lives in [`apply_tpu_graph_trainer_model_transforms`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#apply_tpu_graph_trainer_model_transforms).
- TPU policies: [`full_remat_with_saves`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.md#full_remat_with_saves)
  and save-region selectors [`select_splash_attention`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.md#select_splash_attention),
  [`select_routing`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.md#select_routing),
  resolved by [`resolve_save_regions`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.md#resolve_save_regions);
  region names from [`remat_regions`](../catalog/torchtitan/experiments/tpu/remat_regions.md#annotate_region).

### Memory policies (`compile.memory_policy`)

| Policy | Saves | Notes |
|---|---|---|
| `default` | outputs of ops on the save list: `aten.linear` (torch_tpu traces `F.linear` as one op), SDPA, `topk`, RS / all-to-all | Splash and grouped-expert matmuls are Pallas custom ops -> **recomputed** |
| `full` | layer boundaries only | full recompute |
| `tpu_selective` | `full` + named regions: `attention.inner_attention` (Splash out + LSE) and/or `moe.routing` (top-k ids, expert-sort permutation), via `save_regions` (every layer) or `save_last_n_layers` | "full recompute but keep X"; **not with scan** |
| `tpu_selective_and_offload` | `tpu_selective`, layer boundaries offloaded to host; region values stay in HBM | Qwen3-235B graph-splitter recipe keeps Splash output of its last 36 layers on device |
| `eager` | alternates matmuls save/recompute | matches eager selective AC |
| `sac_and_offload`, `full_and_offload`, `full_and_scan_offload` | `default`/`full` + host offload | see [tpu-scan-graph-splitter-cpu-offload](tpu-scan-graph-splitter-cpu-offload.md) |

Exceptions that move the memory budget: FSDP all-gather outputs are force-saved only under ZeRO-2
(`fsdp_reshard_after_forward="never"`); RNG ops (dropout) are saved by `full` and policies built on it,
but inside a recompute region under `default`/`eager`/`sac_and_offload` they are a runtime error; under
scan the MoE expert-count all-reduces are saved ([`count_collectives`](../catalog/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.md#count_collectives)).

### Enable recipe
```python
config = TpuGraphTrainer.Config.from_tpu_trainer_config(base_config, graph_trainer_model_registry)
config.compile = TpuGraphTrainerCompileConfig(
    enable=True, components=["model"],
    memory_policy="default",       # replaces the eager activation_checkpoint config
    optimizer_compile="in_graph",  # optional: fold AdamW into the step graph
)
```
References: [`qwen3_8b`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_8b)
(in-graph optimizer) and the `llama3_*_scan()` recipes.

## Why it matters / when it applies
- Largest win where the step is dispatch-bound (small model / small batch); on a well-sized model
  where per-block compile already leaves little idle it can roughly tie; at the largest sizes, with
  scan or the graph splitter, it is the path that compiles at all.
- **Limits:** the whole step must trace (no graph breaks, no data-dependent Python control flow).
  Keep `compile.mode="aot_fx_trace"` - scan, graph splitter, remat barriers, FSDP barriers and the
  in-graph optimizer are rejected in other modes. One unrolled graph stops compiling/fitting at large
  sizes; ZeRO-3 on one unrolled graph is rejected unless scan, graph split or
  `fsdp_barrier_policy="prefetch"|"interleave"` (+ `enable_remat_barriers`) is used.
- **`optimizer_compile="in_graph"` costs HBM**: step inputs are not donated, so the graph holds input
  and updated copies of params and optimizer state; `compile_grad_norm` cannot combine with it.
- **libtpu 0.0.48+:** set `xla_enable_hlo_sharding_v3=false` (Shardy HLO sharding v3 segfaults on
  GraphTrainer); recipes do this in `xla_flags`
  (e.g. [`_on_scan_lane`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#_on_scan_lane)).
- GraphTrainer ignores the eager `activation_checkpoint` config; `components` still controls ordinary
  component-level `torch.compile`, so TPU recipes omit `"loss"` (the joint trace already covers it).

## Connections
- Code concepts: [tpu-graph-trainer](../concepts/tpu-graph-trainer.md),
  [graph-trainer](../concepts/graph-trainer.md),
  [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md),
  [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md),
  [qwen3-model](../concepts/qwen3-model.md)
- Module catalogs: [graph_trainer/tpu_graph_trainer](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_graph_trainer.md),
  [graph_trainer/config (tpu)](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md),
  [graph_trainer/tpu_memory_policy](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.md),
  [graph_trainer/configs (upstream)](../catalog/torchtitan/experiments/graph_trainer/configs.md),
  [remat_regions](../catalog/torchtitan/experiments/tpu/remat_regions.md)
- Related doc-concepts: [tpu-scan-graph-splitter-cpu-offload](tpu-scan-graph-splitter-cpu-offload.md),
  [tpu-per-block-torch-compile](tpu-per-block-torch-compile.md),
  [tpu-dispatch-bound-mental-model](tpu-dispatch-bound-mental-model.md),
  [tpu-moe-kernel-switches](tpu-moe-kernel-switches.md),
  [graph-trainer-full-step-graph-capture](graph-trainer-full-step-graph-capture.md), [graph-trainer-memory-policy](graph-trainer-memory-policy.md), [tpu-recipe-memory-policy-and-save-regions](tpu-recipe-memory-policy-and-save-regions.md)

## Source
Extracted from `torchtitan/experiments/tpu/torch-tpu-optimization-guide.md` (section 8; kept in
place).
