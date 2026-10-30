---
title: SimpleFSDP (compiler-friendly FSDP)
type: doc-concept
provenance: doc
source: torchtitan/experiments/graph_trainer/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# SimpleFSDP (compiler-friendly FSDP)

## Definition
SimpleFSDP is GraphTrainer's replacement for eager FSDP2. Instead of hiding all-gather / reduce-scatter behind module hooks, it represents parameter sharding as **parameterized collectives inside the computation graph**: each parameter is a sharded DTensor that is redistributed to a replicated compute placement when used, so the all-gather (forward) and reduce-scatter (backward) appear as traceable graph nodes. The README and Manifesto claim memory and throughput improvements over eager FSDP2 because those nodes can then be bucketed, reordered and overlapped by passes (paper: arXiv 2411.00284).

## In torchtitan (grounded)
- [`data_parallel`](../catalog/torchtitan/experiments/graph_trainer/simple_fsdp.md#data_parallel) applies SimpleFSDP to a model; [`apply_simple_fsdp`](../catalog/torchtitan/experiments/graph_trainer/common_utils.md#apply_simple_fsdp) is the GraphTrainer-side helper used by the per-model parallelize functions.
- [`ReplicateComputation`](../catalog/torchtitan/experiments/graph_trainer/simple_fsdp.md#ReplicateComputation) is the parametrization: [`ReplicateComputation.replicate_compute`](../catalog/torchtitan/experiments/graph_trainer/simple_fsdp.md#ReplicateComputation.replicate_compute) redistributes from `param_sharding` to `compute_placements` (with `grad_placements` controlling the backward reduction).
- Mixed precision: SimpleFSDP's own [`MixedPrecisionPolicy`](../catalog/torchtitan/experiments/graph_trainer/simple_fsdp.md#MixedPrecisionPolicy) (`param_dtype`, `reduce_dtype`).
- The collectives it emits are what the bucketing/overlap passes act on: [`joint_transformer_block_bucketing_reordering_pass`](../catalog/torchtitan/experiments/graph_trainer/fsdp_passes.md#joint_transformer_block_bucketing_reordering_pass), [`FSDPParamOrderBucketer`](../catalog/torchtitan/experiments/graph_trainer/fsdp_passes.md#FSDPParamOrderBucketer), [`schedule_fsdp_comms_to_dense_regions_pass`](../catalog/torchtitan/experiments/graph_trainer/fsdp_passes.md#schedule_fsdp_comms_to_dense_regions_pass).

## Why it matters / when it applies
- It is the precondition for compiler-driven comm/compute overlap: with eager FSDP2 the Manifesto notes that compile graph-breaks on FSDP2 and AC recomputes FSDP2 all-gathers in backward; with SimpleFSDP the all-gathers are ordinary nodes that a memory policy can choose to save or recompute (the default SAC policy saves FSDP all-gathers, see [graph-trainer-memory-policy](graph-trainer-memory-policy.md)).
- Composes with TP and EP in the graph (FSDP + TP + EP), and with GraphPP's split UNSHARD / REDUCE_GRAD graphs ([graph-pp-pipeline-parallelism](graph-pp-pipeline-parallelism.md)).
- **TPU relevance.** The TPU lane takes the same "collectives as graph nodes" idea further: XLA/GSPMD sees the whole step and schedules collectives itself. When comparing FSDP strategies across lanes, SimpleFSDP is the GPU graph-lane analogue of the TPU lane's FSDP-on-mesh path described in [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md) and [flex-shard](../concepts/flex-shard.md).

## Connections
- Code concepts: [graph-trainer](../concepts/graph-trainer.md), [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md), [flex-shard](../concepts/flex-shard.md), [tpu-graph-trainer](../concepts/tpu-graph-trainer.md)
- Module catalogs: [graph_trainer/simple_fsdp](../catalog/torchtitan/experiments/graph_trainer/simple_fsdp.md), [graph_trainer/fsdp_passes](../catalog/torchtitan/experiments/graph_trainer/fsdp_passes.md), [graph_trainer/common_utils](../catalog/torchtitan/experiments/graph_trainer/common_utils.md)
- Related doc-concepts: [graph-trainer-full-step-graph-capture](graph-trainer-full-step-graph-capture.md), [graph-trainer-pass-pipeline](graph-trainer-pass-pipeline.md), [fsdp-cast-forward-inputs-fp32-rope](fsdp-cast-forward-inputs-fp32-rope.md), [tpu-simplefsdp-and-mixed-precision](tpu-simplefsdp-and-mixed-precision.md) (SimpleFSDP on TPU), [tpu-recipe-simplefsdp-schedules](tpu-recipe-simplefsdp-schedules.md)

## Source
Extracted from `torchtitan/experiments/graph_trainer/README.md` and `torchtitan/experiments/graph_trainer/MANIFESTO.md` (kept in place).
