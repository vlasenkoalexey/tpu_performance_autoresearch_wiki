---
title: SimpleFSDP schedules in the TPU recipes (Zero-2 vs Zero-3, prefetch vs interleave, all-reduce+slice)
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/recipes/ironwood/qwen3-32b/tpu7x-4x8x8/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# SimpleFSDP schedules in the TPU recipes (Zero-2 vs Zero-3, prefetch vs interleave, all-reduce+slice)

## Definition
Every transformer recipe in the TPU lane is pure SimpleFSDP over all devices (no TP / PP / CP; EP=1 even for
the MoE), usually on the topology-aware device mesh. What the recipes tune instead is the *FSDP schedule*:
whether gathered parameters are kept after forward (Zero-2) or resharded and re-gathered in backward (Zero-3),
how the re-gather all-gathers are ordered against gradient reduce-scatters (`prefetch` vs `interleave`
barriers), whether the optimizer runs inside the compiled graph, and, at 512 devices, rewriting specific
reduce-scatters as all-reduce plus a local slice so they stay on SparseCore.

## In torchtitan (grounded)
- SimpleFSDP and the topology mesh are switched on by
  [`ParallelismConfig.use_simple_fsdp`](../catalog/torchtitan/config/configs.md#ParallelismConfig.use_simple_fsdp) and
  [`ParallelismConfig.enable_tpu_topo_mesh`](../catalog/torchtitan/config/configs.md#ParallelismConfig.enable_tpu_topo_mesh)
  (Conformer uses its own [`TPUConfig.use_simple_fsdp`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TPUConfig.use_simple_fsdp)).
  Zero-2 vs Zero-3 is [`ParallelismConfig.fsdp_reshard_after_forward`](../catalog/torchtitan/config/configs.md#ParallelismConfig.fsdp_reshard_after_forward)
  (`"never"` = Zero-2, `"always"` = Zero-3).
- GraphTrainer schedule knobs live on [`TpuGraphTrainerCompileConfig`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig):
  [`fsdp_barrier_policy`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig.fsdp_barrier_policy)
  (`none` / `prefetch` / `interleave`; requires
  [`enable_remat_barriers`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig.enable_remat_barriers)
  and cannot be combined with the graph splitter),
  [`fsdp_allreduce_slice_parameter_patterns`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig.fsdp_allreduce_slice_parameter_patterns)
  with its size cap [`fsdp_allreduce_slice_max_input_bytes`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig.fsdp_allreduce_slice_max_input_bytes)
  (validated by [`_validate_fsdp_allreduce_slice`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#_validate_fsdp_allreduce_slice)),
  and [`optimizer_compile`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig.optimizer_compile)
  (`eager` / `separate_graph` / `in_graph`).
- Reduction precision is [`TrainingConfig.mixed_precision_reduce`](../catalog/torchtitan/config/configs.md#TrainingConfig.mixed_precision_reduce).

### Schedule per recipe

| Recipe (config) | Zero level | Barrier policy | Other schedule choices |
|---|---|---|---|
| qwen3-8b tpu7x ([`qwen3_8b`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_8b)) | Zero-2 (`never`) | none | optimizer `in_graph`, FP32 reductions, dual-SC or hierarchical reduce-scatter |
| alt: [`qwen3_8b_zero3`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_8b_zero3) | Zero-3 (`always`) | `interleave` | full remat, remat barriers, Splash `use_vmap_bwd` ("memory-oriented") |
| qwen3-32b tpu7x-4x4x4 ([`qwen3_32b`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_32b)) | Zero-3 | `prefetch` | built on `qwen3_8b_zero3`; packed QKV |
| qwen3-32b tpu7x-4x8x8 ([`qwen3_32b_4x8x8`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_32b_4x8x8)) | Zero-3 | `interleave` | all-reduce+slice for `feed_forward.w1/w3` gradients |
| muse-glimmer-30b ([`muse_glimmer_30b_full_logits`](../catalog/torchtitan/experiments/tpu/muse_glimmer/config_registry.md#muse_glimmer_30b_full_logits)) | Zero-3 | `prefetch` | optimizer `in_graph`, fused optimizer |
| qwen3-30b-a3b ([`_qwen3_moe_30b_fsdp_only_full_ac`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac)) | Zero-2 | none | FSDP over 128 with EP=1; remat barriers; all-reduce+slice for packed QKV and `wo` gradients (cap 40 MiB) |
| Llama3, FLUX, Trillium Qwen3 (regular TPUTrainer) | SimpleFSDP defaults | n/a | regular trainer; `reg_trainer_qwen3_8b` adds `materialize_forward_before_backward` and a compiled grad norm |

### Measured trade-offs stated in the READMEs (and matching code comments)
- **Zero-2 vs Zero-3 at 32B.** `qwen3_32b` uses Zero-3 because Zero-2 "would keep all ~61 GiB of gathered BF16
  weights resident".
- **prefetch vs interleave.** At 4x4x4, prefetch beats interleave by 0.3-0.6% for ~4 GiB more peak HBM (code
  comment in `qwen3_32b`). At 4x8x8, *before* the w1/w3 change, interleave beat prefetch by 2.3% step time and
  56 GiB peak HBM, so the 512-device recipe switches back to interleave.
- **All-reduce + slice at world 512.** Each w1/w3 gradient shard is 25600 / 512 = 50 rows, not a multiple of 8,
  so those reduce-scatters fall back to the TensorCore (~2.5 s per step). Reducing them with an all-reduce plus a
  local slice keeps them on SparseCore; the config docstring records 14.33 -> 12.34 s per step for +49 GiB peak
  HBM. The rewrite requires FP32 reductions, so there is no MaxText-parity (BF16 reduction) variant at 512 yet.
  The Qwen3-30B-A3B config applies the same rewrite to the 40 MiB packed-QKV and 32 MiB output-projection
  gradients and caps it there, noting that all-reduce sends roughly twice the ring traffic of a reduce-scatter.
- **In-graph optimizer.** Recipes with `optimizer_compile="in_graph"` log `grad_norm` as 0.0 because the
  optimizer runs inside the compiled graph; clipping is still applied there (Muse Glimmer, Qwen3-32B READMEs).

## Why it matters / when it applies
- On TPU the FSDP schedule, not the parallelism mix, is the main scale-out lever in these recipes: it decides
  peak HBM (resident gathered weights, prefetched next-layer weights) and how much collective time is exposed.
- The choice interacts with the SparseCore flags: dual-SparseCore reduce-scatter is tuned for Zero-2 and the
  Zero-3 interleave, where all-gather and reduce-scatter are not concurrent
  ([tpu-recipe-libtpu-flag-sets](tpu-recipe-libtpu-flag-sets.md)).
- Shard shapes matter at large world sizes: a dimension that stops dividing into multiples of 8 per device can
  push a collective off SparseCore; check shard sizes when scaling a recipe to a new slice.

## Connections
- Code concepts: [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md),
  [tpu-graph-trainer](../concepts/tpu-graph-trainer.md), [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md),
  [graph-trainer](../concepts/graph-trainer.md), [qwen3-model](../concepts/qwen3-model.md),
  [optimizers-and-lr-schedulers](../concepts/optimizers-and-lr-schedulers.md)
- Module catalogs: [graph_trainer/config](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md),
  [qwen3/config_registry](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md),
  [muse_glimmer/config_registry](../catalog/torchtitan/experiments/tpu/muse_glimmer/config_registry.md),
  [config/configs](../catalog/torchtitan/config/configs.md)
- Related doc-concepts: [tpu-recipe-matrix](tpu-recipe-matrix.md),
  [tpu-recipe-memory-policy-and-save-regions](tpu-recipe-memory-policy-and-save-regions.md),
  [tpu-recipe-libtpu-flag-sets](tpu-recipe-libtpu-flag-sets.md),
  [tpu-recipe-precision-and-throughput-accounting](tpu-recipe-precision-and-throughput-accounting.md),
  [simple-fsdp](simple-fsdp.md),
  [tpu-simplefsdp-and-mixed-precision](tpu-simplefsdp-and-mixed-precision.md),
  [tpu-graph-trainer-memory-policies](tpu-graph-trainer-memory-policies.md),
  [graph-trainer-full-step-graph-capture](graph-trainer-full-step-graph-capture.md)

## Source
Extracted from (kept in place):
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-32b/tpu7x-4x8x8/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-32b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-8b/tpu7x-2x2x2/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-8b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/muse-glimmer-30b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-30b-a3b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/qwen3-8b/v6e-8/README.md`

Cross-checked against `torchtitan/experiments/tpu/qwen3/config_registry.py`,
`torchtitan/experiments/tpu/muse_glimmer/config_registry.py` and
`torchtitan/experiments/tpu/graph_trainer/config.py` at commit 2ad96c939.
