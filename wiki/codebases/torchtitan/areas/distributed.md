---
title: 'Area: torchtitan/distributed'
type: area
area: 'torchtitan/distributed'
description: 'Distributed layer of torchtitan: ParallelDims and the device mesh, FSDP/TP/PP/CP/EP application, activation checkpointing, FlexShard, and the async/DeepEP expert-parallel paths.'
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Area: `torchtitan/distributed`

## Purpose
`torchtitan/distributed/` turns parallelism degrees into a device mesh and applies each axis to the model. [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md) covers `ParallelDims`, mesh construction (including the TPU topology-aware mesh), and how FSDP, TP, PP, CP, EP and activation checkpointing are composed. [flex-shard](../concepts/flex-shard.md) is the bucketed storage-sharding runtime (with DistMuon) that generalizes FSDP2; today it is GPU-only.

The small units `minimal_async_ep` and `deepep` are alternative expert-parallel dispatch paths; they are catalog-only and CUDA-oriented. On TPU, MoE dispatch is replaced by the TPU lane ([tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md)) and context parallelism by [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md).

## How the units connect
- [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md) is called from each model's `parallelize_fn` (see [model-spec-protocols](../concepts/model-spec-protocols.md)); per-model specifics are on the model pages (e.g. [llama3-model](../concepts/llama3-model.md), [qwen3-model](../concepts/qwen3-model.md)).
- [flex-shard](../concepts/flex-shard.md) plugs in as an alternative to `fully_shard` and owns its optimizer reshard schedule.
- `minimal_async_ep` and `deepep` sit under the MoE token dispatcher of [model-building-blocks](../concepts/model-building-blocks.md).

<!-- area:auto:begin -->
## Units
4 planned unit(s) in `torchtitan/distributed`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `torchtitan/distributed/flex_shard` | 5 | 301 | 5 | [`ComputeLayout`](../catalog/torchtitan/distributed/flex_shard/optimizer_reshard.md#ComputeLayout "torchtitan/distributed/flex_shard/optimizer_reshard.py:L111"), [`shardings_by_mesh_axis`](../catalog/torchtitan/distributed/flex_shard/optimizer_reshard.md#ComputeLayout.shardings_by_mesh_axis "torchtitan/distributed/flex_shard/optimizer_reshard.py:L165"), [`BlockShard`](../catalog/torchtitan/distributed/flex_shard/optimizer_reshard.md#BlockShard "torchtitan/distributed/flex_shard/optimizer_reshard.py:L35") | [flex-shard](../concepts/flex-shard.md) |
| `torchtitan/distributed` | 11 | 243 | 215 | [`ParallelDims`](../catalog/torchtitan/distributed/parallel_dims.md#ParallelDims "torchtitan/distributed/parallel_dims.py:L112"), [`MeshAxisName`](../catalog/torchtitan/distributed/parallel_dims.md#MeshAxisName "torchtitan/distributed/parallel_dims.py:L72"), [`get_spmd_backend`](../catalog/torchtitan/distributed/utils.md#get_spmd_backend "torchtitan/distributed/utils.py:L45") | [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md) |
| `torchtitan/distributed/minimal_async_ep` | 3 | 73 | 4 | [`MinimalAsyncEPDispatchMetadata`](../catalog/torchtitan/distributed/minimal_async_ep/api.md#MinimalAsyncEPDispatchMetadata "torchtitan/distributed/minimal_async_ep/api.py:L145"), [`E_row_to_T_row`](../catalog/torchtitan/distributed/minimal_async_ep/api.md#MinimalAsyncEPDispatchMetadata.E_row_to_T_row "torchtitan/distributed/minimal_async_ep/api.py:L165"), [`T_row_to_E_row`](../catalog/torchtitan/distributed/minimal_async_ep/api.md#MinimalAsyncEPDispatchMetadata.T_row_to_E_row "torchtitan/distributed/minimal_async_ep/api.py:L166") | [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md) |
| `torchtitan/distributed/deepep` | 2 | 59 | 6 | [`dispatch_tokens`](../catalog/torchtitan/distributed/deepep/deepep.md#dispatch_tokens "torchtitan/distributed/deepep/deepep.py:L454"), [`combine_tokens`](../catalog/torchtitan/distributed/deepep/deepep.md#combine_tokens "torchtitan/distributed/deepep/deepep.py:L560"), [`dispatch_tokens`](../catalog/torchtitan/distributed/deepep/hybridep.md#dispatch_tokens "torchtitan/distributed/deepep/hybridep.py:L455") | [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md) |

<!-- area:auto:end -->
