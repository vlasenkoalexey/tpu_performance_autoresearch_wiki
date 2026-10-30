---
title: GraphTrainer tensor-granularity memory policy (SAC, full recompute, CPU offload)
type: doc-concept
provenance: doc
source: torchtitan/experiments/graph_trainer/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# GraphTrainer tensor-granularity memory policy (SAC, full recompute, CPU offload)

## Definition
Because the whole step is one graph, GraphTrainer decides activation handling **per tensor**, not per module: each activation can independently be saved, recomputed, or offloaded to CPU, and different strategies can mix inside one layer. This is the graph-trainer counterpart of eager module-level selective activation checkpointing (SAC), selected with `--compile.memory_policy`.

## In torchtitan (grounded)
- Selector: [`GraphTrainerCompileConfig.memory_policy`](../catalog/torchtitan/experiments/graph_trainer/configs.md#GraphTrainerCompileConfig.memory_policy), typed by [`GraphTrainerMemoryPolicy`](../catalog/torchtitan/experiments/graph_trainer/configs.md#GraphTrainerMemoryPolicy). Policies register through [`register_memory_policy`](../catalog/torchtitan/experiments/graph_trainer/registry.md#register_memory_policy) and are applied by [`tag_with_memory_policy_pass`](../catalog/torchtitan/experiments/graph_trainer/memory_policy.md#tag_with_memory_policy_pass) (validated by [`validate_memory_policy_config`](../catalog/torchtitan/experiments/graph_trainer/memory_policy.md#validate_memory_policy_config)).
  - `default`: SAC saving all compute-intensive ops and FSDP all-gathers ([`tag_sac_policy`](../catalog/torchtitan/experiments/graph_trainer/memory_policy.md#tag_sac_policy)).
  - `full`: full recompute saving layer outputs plus ops named by [`full_recompute_save_ops`](../catalog/torchtitan/experiments/graph_trainer/configs.md#GraphTrainerCompileConfig.full_recompute_save_ops) (selectors `MODULE_FQN_PATTERN::OP`, `|`-separated, e.g. `layers.*.moe.router.gate::aten.mm.dtype`); with no selectors it mirrors eager full AC.
  - `eager`: alternate mm ops between save/recompute, matching core [`SelectiveAC`](../catalog/torchtitan/distributed/activation_checkpoint.md#SelectiveAC).
  - `min_cut`: min-cut partitioner chooses saved values ([`tag_min_cut_saved_values`](../catalog/torchtitan/experiments/graph_trainer/memory_policy.md#tag_min_cut_saved_values)).
  - `sac_and_offload`: default SAC, then offload surviving must-save activations to CPU within [`cpu_offload_budget_gb`](../catalog/torchtitan/experiments/graph_trainer/configs.md#GraphTrainerCompileConfig.cpu_offload_budget_gb) (largest first), via [`apply_cpu_offload_pass`](../catalog/torchtitan/experiments/graph_trainer/cpu_offload.md#apply_cpu_offload_pass); overlap knobs [`cpu_offload_prefetch_n_layers`](../catalog/torchtitan/experiments/graph_trainer/configs.md#GraphTrainerCompileConfig.cpu_offload_prefetch_n_layers) / [`cpu_offload_defer_n_layers`](../catalog/torchtitan/experiments/graph_trainer/configs.md#GraphTrainerCompileConfig.cpu_offload_defer_n_layers).
- The remat itself is materialized by [`selective_activation_remat_pass`](../catalog/torchtitan/experiments/graph_trainer/selective_activation_remat.md#selective_activation_remat_pass).
- FSDP interaction: with `reshard_after_forward=False` (ZeRO-2) the policy is overridden to must-save each FSDP all-gather output; with resharding (ZeRO-3) all-gathers may be recomputed in backward.

## Why it matters / when it applies
- It removes two eager pain points the Manifesto names: AC recomputing FSDP all-gathers in backward, and compile graph-breaks invalidating AC (causing OOM). Tests check that graph SAC matches eager selective-AC peak memory and full-AC numerics.
- The `full` + `full_recompute_save_ops` combination is the README's recipe for very large MoE (DeepSeek-V3 671B): recompute everything except a few expensive matmuls (router gate, MLA `wkv_a`).
- **TPU relevance.** The decision space (save vs recompute vs host offload, per tensor, with a memory budget) is the same one the TPU lane exposes through XLA remat policies and host offload; see [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md). The JAX lane maps `full`/`selective` AC onto `jax.checkpoint_policies` instead (see [jax-scan-over-layers](jax-scan-over-layers.md)).

**Doc vs code at this commit:** the README's CPU-offload example uses `--compile.memory_policy cpu_offload_all`; that value does not exist. The offload policy is `sac_and_offload`. Separately, the `GraphTrainerMemoryPolicy` Literal lists only `default | full | eager | sac_and_offload`, while `min_cut` is documented in the docstring and registered in `memory_policy.py` but missing from the type.

## Connections
- Code concepts: [graph-trainer](../concepts/graph-trainer.md), [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md), [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md), [tpu-graph-trainer](../concepts/tpu-graph-trainer.md)
- Module catalogs: [graph_trainer/memory_policy](../catalog/torchtitan/experiments/graph_trainer/memory_policy.md), [graph_trainer/cpu_offload](../catalog/torchtitan/experiments/graph_trainer/cpu_offload.md), [graph_trainer/selective_activation_remat](../catalog/torchtitan/experiments/graph_trainer/selective_activation_remat.md), [distributed/activation_checkpoint](../catalog/torchtitan/distributed/activation_checkpoint.md)
- Related doc-concepts: [graph-trainer-pass-pipeline](graph-trainer-pass-pipeline.md), [simple-fsdp](simple-fsdp.md), [graph-trainer-full-step-graph-capture](graph-trainer-full-step-graph-capture.md), [tpu-graph-trainer-memory-policies](tpu-graph-trainer-memory-policies.md) (TPU counterpart), [tpu-scan-graph-splitter-cpu-offload](tpu-scan-graph-splitter-cpu-offload.md), [tpu-recipe-memory-policy-and-save-regions](tpu-recipe-memory-policy-and-save-regions.md)

## Source
Extracted from `torchtitan/experiments/graph_trainer/README.md` (kept in place).
