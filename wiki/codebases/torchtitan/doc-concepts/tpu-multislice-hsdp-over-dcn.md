---
title: Multi-slice TPU training (HSDP over DCN, MegaScale)
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Multi-slice TPU training (HSDP over DCN, MegaScale)

## Definition
A multi-slice job spans several TPU slices. Each slice is its own ICI fabric; libtpu's MegaScale
PJRT client joins them over DCN, which is much slower than ICI. The layout that pays off is HSDP:
shard inside a slice, replicate across slices, so only the replicated gradient reduction crosses
DCN. TorchTitan sets up the MegaScale environment, validates the mesh so FSDP groups do not straddle
slices, and offers a min-cost DTensor redistribution planner that shrinks the DCN payload.

## In torchtitan (grounded)
- **Environment.** libtpu builds the MegaScale client from three variables:
  `MEGASCALE_NUM_SLICES`, `MEGASCALE_COORDINATOR_ADDRESS` (slice 0's first worker; without it every
  slice numbers devices from zero and the mesh cannot be built), and `MEGASCALE_SLICE_ID`.
  [`get_num_slices`](../catalog/torchtitan/experiments/tpu/cloud_distributed_utils.md#get_num_slices)
  reads the count; [`get_slice_id`](../catalog/torchtitan/experiments/tpu/cloud_distributed_utils.md#get_slice_id) /
  [`get_slice_id_from_worker_hostnames`](../catalog/torchtitan/experiments/tpu/cloud_distributed_utils.md#get_slice_id_from_worker_hostnames)
  recover the slice index from `TPU_WORKER_HOSTNAMES`; the GKE init path
  [`_maybe_init_distributed_on_gke`](../catalog/torchtitan/experiments/tpu/cloud_distributed_utils.md#_maybe_init_distributed_on_gke)
  exports `MEGASCALE_SLICE_ID` if absent (log line `Exporting MEGASCALE_SLICE_ID=...`), cross-checks
  an explicit value, and raises if `MEGASCALE_COORDINATOR_ADDRESS` is missing.
- **Mesh guard.** [`maybe_validate_multislice_parallelism`](../catalog/torchtitan/experiments/tpu/cloud_distributed_utils.md#maybe_validate_multislice_parallelism)
  is called from [`start_trainer`](../catalog/torchtitan/experiments/tpu/train.md#start_trainer) before
  `ParallelDims` is built. torch_tpu's topology-aware mesh puts the slice split on the outermost mesh
  axis with extent > 1 of `(pp, dp_replicate, dp_shard, cp, tp)`; with PP=1 and replicate=1 that is
  `dp_shard`, so every weight all-gather and gradient reduce-scatter would cross DCN. The guard
  raises instead of silently fixing it.
- **Required flag:** `--parallelism.data_parallel_replicate_degree=$MEGASCALE_NUM_SLICES`
  ([`ParallelismConfig.data_parallel_replicate_degree`](../catalog/torchtitan/config/configs.md#ParallelismConfig.data_parallel_replicate_degree)).
  A degree the slice count does not divide is rejected by torch_tpu; any multiple works.
- **Recommended flag:** `--parallelism.enable_min_cost_redistribute`
  ([`ParallelismConfig.enable_min_cost_redistribute`](../catalog/torchtitan/config/configs.md#ParallelismConfig.enable_min_cost_redistribute)),
  entered by [`_maybe_enable_min_cost_redistribute`](../catalog/torchtitan/train.md#_maybe_enable_min_cost_redistribute)
  before the model is built (the plan is baked in at trace time). The greedy planner all-reduces the
  **full** gradient on the replicate (DCN) axis before reduce-scattering; min-cost reduce-scatters
  first, shrinking the DCN payload by the shard degree.
- Multi-slice also calls `workarounds.disable_pinned_host_memory()`
  ([`disable_pinned_host_memory`](../catalog/torchtitan/experiments/tpu/workarounds.md#disable_pinned_host_memory))
  because the MegaScale PJRT client cannot serve pinned host memory.

### Launch recipe (README example, 2 slices, v7x)

```
--num-slices 2
--env MEGASCALE_NUM_SLICES=2
--env MEGASCALE_COORDINATOR_ADDRESS="$WORKLOAD_NAME-main-job-0-0.$WORKLOAD_NAME:8080"
--env LIBTPU_INIT_ARGS="--xla_tpu_scoped_vmem_limit_kib=65536 \
   --megascale_grpc_premap_memory_bytes=4294967296 \
   --megascale_use_numa_aware_block_allocator=false"
torchrun --nnodes=$((MEGASCALE_NUM_SLICES * VMS)) --nproc_per_node=8 \
   --node_rank=$((SLICE * VMS + TPU_WORKER_ID)) -m torchtitan.experiments.tpu.train \
   --module=torchtitan.experiments.tpu.muse_glimmer --config=muse_glimmer_30b_full_logits \
   --parallelism.data_parallel_replicate_degree=$MEGASCALE_NUM_SLICES \
   --parallelism.enable_min_cost_redistribute
```

The recipe used is [`muse_glimmer_30b_full_logits`](../catalog/torchtitan/experiments/tpu/muse_glimmer/config_registry.md#muse_glimmer_30b_full_logits).

### v7x host-memory pool
MegaScale pins a DCN-transfer pool of 16 GiB per NUMA node **per process**. torch_tpu runs one
process per TensorCore (8 per v7x VM, hence `--nproc_per_node=8`), so the default is
16 GiB x 2 NUMA x 8 = 256 GiB per VM. Both flags above are needed to cut it to 4 GiB/process
(32 GiB/VM): `--megascale_grpc_premap_memory_bytes=4294967296` and
`--megascale_use_numa_aware_block_allocator=false`. This matters whenever host RAM is also wanted
for activation offload (see [tpu-scan-graph-splitter-cpu-offload](tpu-scan-graph-splitter-cpu-offload.md)).

## Why it matters / when it applies
- A wrong layout still trains correctly, only at a fraction of throughput, and torch_tpu notes it
  at INFO only - the guard exists because a slow job is harder to notice than a failed one.
- Kueue + JobSet (installed by the Cluster Toolkit blueprint) admit a multi-slice workload
  all-or-nothing, so one slice cannot hold chips while the other never starts.
- Single-slice / multi-host jobs do **not** need HSDP: the optimization guide notes every shipped
  multi-host v7x recipe is plain FSDP with `data_parallel_replicate_degree=1`; full sharding spans
  hosts fine over ICI ([tpu-simplefsdp-and-mixed-precision](tpu-simplefsdp-and-mixed-precision.md)).

**Doc vs code nuance:** the README says TorchTitan refuses to start whenever the replicate degree is
left at 1 on multi-slice. The guard actually also accepts `pipeline_parallel_degree > 1` (the slice
split then lands on the PP axis); it only raises when **both** PP and replicate are 1.

## Connections
- Code concepts: [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md),
  [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md),
  [flex-shard](../concepts/flex-shard.md), [muse-glimmer-model](../concepts/muse-glimmer-model.md)
- Module catalogs: [cloud_distributed_utils](../catalog/torchtitan/experiments/tpu/cloud_distributed_utils.md),
  [train (tpu)](../catalog/torchtitan/experiments/tpu/train.md), [train (core)](../catalog/torchtitan/train.md),
  [config/configs](../catalog/torchtitan/config/configs.md)
- Related doc-concepts: [tpu-launch-and-profiling-workflow](tpu-launch-and-profiling-workflow.md),
  [tpu-libtpu-xla-flag-layering](tpu-libtpu-xla-flag-layering.md),
  [tpu-simplefsdp-and-mixed-precision](tpu-simplefsdp-and-mixed-precision.md),
  [tpu-recipe-simplefsdp-schedules](tpu-recipe-simplefsdp-schedules.md)

## Source
Extracted from `torchtitan/experiments/tpu/README.md` (section "Multi-slice model training on GKE"),
cross-checked against `torchtitan/experiments/tpu/cloud_distributed_utils.py` (kept in place).
