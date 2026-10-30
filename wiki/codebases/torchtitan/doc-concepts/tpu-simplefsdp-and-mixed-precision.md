---
title: SimpleFSDP on TPU (fully_shard vs hybrid_shard) with bf16/fp32 mixed precision
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/torch-tpu-optimization-guide.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# SimpleFSDP on TPU (fully_shard vs hybrid_shard) with bf16/fp32 mixed precision

## Definition
SimpleFSDP is TorchTitan's DTensor-based FSDP: sharding is expressed purely as **DTensor
parametrizations riding DTensor autograd** - the all-gather is a `redistribute` in forward and the
reduce-scatter is implicit in backward, with no module hooks and no explicit collective calls. That
makes it **compiler-native**: collectives live inside the traced graph, so `torch.compile` (and
GraphTrainer) can schedule and overlap them with compute. The guide pairs it with the standard mixed
precision policy `param_dtype=bfloat16, reduce_dtype=float32`.

## In torchtitan (grounded)
- Implementation: [`data_parallel`](../catalog/torchtitan/experiments/graph_trainer/simple_fsdp.md#data_parallel)
  with `mode="fully_shard"` (ZeRO-3-like: params + optimizer state sharded) or `mode="hybrid_shard"`
  (HSDP 2-D mesh: replicate across groups, shard within), and
  [`MixedPrecisionPolicy`](../catalog/torchtitan/experiments/graph_trainer/simple_fsdp.md#MixedPrecisionPolicy)
  ([`param_dtype`](../catalog/torchtitan/experiments/graph_trainer/simple_fsdp.md#MixedPrecisionPolicy.param_dtype),
  [`reduce_dtype`](../catalog/torchtitan/experiments/graph_trainer/simple_fsdp.md#MixedPrecisionPolicy.reduce_dtype)).
  The parametrization itself is [`ReplicateComputation`](../catalog/torchtitan/experiments/graph_trainer/simple_fsdp.md#ReplicateComputation);
  GraphTrainer's TPU variant is [`TpuReplicateComputation`](../catalog/torchtitan/experiments/tpu/graph_trainer/simple_fsdp.md#TpuReplicateComputation).
- Switch: [`ParallelismConfig.use_simple_fsdp`](../catalog/torchtitan/config/configs.md#ParallelismConfig.use_simple_fsdp)
  (TPU recipes also set [`enable_tpu_topo_mesh`](../catalog/torchtitan/config/configs.md#ParallelismConfig.enable_tpu_topo_mesh)).
  The Llama3 TPU parallelizer ([`parallelize_llama`](../catalog/torchtitan/experiments/tpu/llama3/infra/parallelize.md#parallelize_llama))
  applies every other parallelism with DP skipped, then wraps the model in SimpleFSDP over the
  `fsdp` (or `dp_replicate` x `fsdp`) mesh - `hybrid_shard` exactly when
  `data_parallel_replicate_degree > 1`.
- Precision comes from [`TrainingConfig.mixed_precision_param`](../catalog/torchtitan/config/configs.md#TrainingConfig.mixed_precision_param)
  (default `bfloat16`) and [`TrainingConfig.mixed_precision_reduce`](../catalog/torchtitan/config/configs.md#TrainingConfig.mixed_precision_reduce)
  (default `float32`), i.e. the guide's recommended policy is the default.
- ZeRO-2 vs ZeRO-3 is [`ParallelismConfig.fsdp_reshard_after_forward`](../catalog/torchtitan/config/configs.md#ParallelismConfig.fsdp_reshard_after_forward)
  (`"never"` vs `"always"`); it matters for GraphTrainer memory policies and the dual-SparseCore RS
  flag bundle.

## Why it matters / when it applies
- **Why not FSDP2 here:** FSDP2's `fully_shard` drives collectives from pre/post-forward hooks,
  which trace poorly, cause graph breaks and overlap worse. SimpleFSDP + per-block compile is
  "meaningfully faster than FSDP alone" because the compiler can overlap DTensor collectives.
- **Default to `fully_shard`, across hosts too.** HSDP is not a multi-host requirement: every shipped
  multi-host v7x recipe (`qwen3-8b`, `qwen3-32b`, `qwen3-30b-a3b`, `muse-glimmer-30b`, `flux1` at
  4x4x4 and 4x8x8) is plain FSDP with `data_parallel_replicate_degree=1`. HSDP buys cheaper gradient
  reduction within a group at the cost of replicating params + optimizer state (per-chip memory x
  replicate degree). Pick it when the FSDP group would be wider than collectives need (very large chip
  counts) or when the replicate axis maps onto a slow link - multi-slice over DCN
  ([tpu-multislice-hsdp-over-dcn](tpu-multislice-hsdp-over-dcn.md)). Choose the mesh from
  interconnect, collective cost and memory budget, not host count.
- **Mixed precision:** bf16 params are what is all-gathered and used for matmuls (the MFU denominator
  assumes bf16); fp32 reduce avoids bf16 cross-shard accumulation error. Dropping `reduce_dtype` to
  bf16 to save bandwidth is a **model-quality regression, not a perf lever**.
- Without FSDP use `torch.autocast` (TPU lane: [`TPUConfig.enable_amp`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TPUConfig.enable_amp)).
- Collective-overlap libtpu bundles (SparseCore LHS, collective offload, AG/RS pipelining) tune how
  these FSDP collectives are scheduled - see [tpu-libtpu-xla-flag-layering](tpu-libtpu-xla-flag-layering.md).

## Connections
- Code concepts: [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md),
  [flex-shard](../concepts/flex-shard.md), [graph-trainer](../concepts/graph-trainer.md),
  [tpu-graph-trainer](../concepts/tpu-graph-trainer.md), [llama3-model](../concepts/llama3-model.md)
- Module catalogs: [graph_trainer/simple_fsdp](../catalog/torchtitan/experiments/graph_trainer/simple_fsdp.md),
  [tpu/graph_trainer/simple_fsdp](../catalog/torchtitan/experiments/tpu/graph_trainer/simple_fsdp.md),
  [llama3/infra/parallelize (tpu)](../catalog/torchtitan/experiments/tpu/llama3/infra/parallelize.md),
  [config/configs](../catalog/torchtitan/config/configs.md)
- Related doc-concepts: [tpu-multislice-hsdp-over-dcn](tpu-multislice-hsdp-over-dcn.md),
  [tpu-per-block-torch-compile](tpu-per-block-torch-compile.md),
  [tpu-graph-trainer-memory-policies](tpu-graph-trainer-memory-policies.md),
  [simple-fsdp](simple-fsdp.md), [tpu-recipe-simplefsdp-schedules](tpu-recipe-simplefsdp-schedules.md)

## Source
Extracted from `torchtitan/experiments/tpu/torch-tpu-optimization-guide.md` (section 5 and the
mixed-precision bullet of section 6; kept in place).
