---
title: 'Area: src/vllm_torchtpu/executors'
type: area
area: 'src/vllm_torchtpu/executors'
description: 'vLLM executor subclasses the TPU platform selects to spawn and drive one TPU worker per device: a multiprocess executor for single-host and non-Ray multi-host runs, and Ray V1/V2 executors for Ray multi-host slices.'
updated: 2026-11-03
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Area: `src/vllm_torchtpu/executors`

## Purpose
An executor is the vLLM component that spawns the worker processes and broadcasts engine calls to them. This area holds the TPU subclasses. None of them is chosen by the user directly. The [TPU platform](../concepts/tpu-platform.md) picks one inside `check_and_update_config`: `UniProcExecutor` for a single device with no parallelism, `TpuMultiprocExecutor` for a single host with TP/PP/PCP (and for multi-host runs without Ray, where each host spawns its local workers), and `RayDistributedExecutorV2` (or the older `RayDistributedExecutor`) when `TPU_MULTIHOST_BACKEND=ray`. Multi-host data parallelism requires the V2 Ray executor.

What enters the area is the engine core's calls (`collective_rpc`, KV-cache spec queries, `initialize_from_config`). What leaves is the same call fanned out to each [TPU worker](worker.md), always with one TPU device per worker. The TPU-specific work is small but affects startup. When hybrid (compact-mamba) KV sizing is in use, the multiprocess executor reconciles the block counts that workers measured separately, so every rank allocates the same number of blocks. It also splits KV-offload kernel prewarm into one RPC per shape, so the prewarm does not overrun vLLM's broadcast timeout.

This area has no mechanism page of its own. It sits between the platform, which chooses it, and the worker, which does the device work.

## How the units connect
- `tpu_multiproc_executor.py` subclasses vLLM's `MultiprocExecutor`. It patches the per-worker global-rank env before spawning, copies an agreed `num_gpu_blocks_override` back to the engine-side config in `get_kv_cache_specs`, and after `initialize_from_config` runs the [host-offload](../concepts/host-offload.md) H2D prewarm one shape per `collective_rpc` call.
- `kv_block_override.py` is the agreement rule it calls: under compact-mamba sizing, workers size the KV pool from their own measured free HBM, so their block counts differ slightly. `reconcile_num_gpu_blocks_override` accepts a spread within a relative tolerance and pins the minimum, so no worker is asked for more blocks than it measured (see [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md)).
- `ray_distributed_executor_v2.py` builds on vLLM V1's `RayExecutorV2` (message-queue control plane). It derives the DP geometry and slice-wide host order from the Ray cluster, because TorchTPU bootstraps the whole DP x TP grid at once, and it requests exactly one TPU resource per worker actor.
- `ray_distributed_executor.py` is the older Ray executor with its own worker wrapper, kept for Ray multi-host runs without the V2 backend.

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `src/vllm_torchtpu/executors`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `src/vllm_torchtpu/executors` | 4 | 65 | 1 | [`TpuMultiprocExecutor`](../catalog/src/vllm_torchtpu/executors/tpu_multiproc_executor.md#TpuMultiprocExecutor "src/vllm_torchtpu/executors/tpu_multiproc_executor.py:L27"), [`RayDistributedExecutorV2`](../catalog/src/vllm_torchtpu/executors/ray_distributed_executor_v2.md#RayDistributedExecutorV2 "src/vllm_torchtpu/executors/ray_distributed_executor_v2.py:L72"), [`RayDistributedExecutor`](../catalog/src/vllm_torchtpu/executors/ray_distributed_executor.md#RayDistributedExecutor "src/vllm_torchtpu/executors/ray_distributed_executor.py:L73") | section below |

## Small units
### `src/vllm_torchtpu/executors`
- modules: `src/vllm_torchtpu/executors/kv_block_override.py`, `src/vllm_torchtpu/executors/ray_distributed_executor.py`, `src/vllm_torchtpu/executors/ray_distributed_executor_v2.py`, `src/vllm_torchtpu/executors/tpu_multiproc_executor.py`
- entry points: [`TpuMultiprocExecutor`](../catalog/src/vllm_torchtpu/executors/tpu_multiproc_executor.md#TpuMultiprocExecutor "src/vllm_torchtpu/executors/tpu_multiproc_executor.py:L27"), [`RayDistributedExecutorV2`](../catalog/src/vllm_torchtpu/executors/ray_distributed_executor_v2.md#RayDistributedExecutorV2 "src/vllm_torchtpu/executors/ray_distributed_executor_v2.py:L72"), [`RayDistributedExecutor`](../catalog/src/vllm_torchtpu/executors/ray_distributed_executor.md#RayDistributedExecutor "src/vllm_torchtpu/executors/ray_distributed_executor.py:L73")
- hubs: [`reconcile_num_gpu_blocks_override`](../catalog/src/vllm_torchtpu/executors/kv_block_override.md#reconcile_num_gpu_blocks_override "src/vllm_torchtpu/executors/kv_block_override.py:L39"), [`_init_workers_ray`](../catalog/src/vllm_torchtpu/executors/ray_distributed_executor.md#RayDistributedExecutor._init_workers_ray "src/vllm_torchtpu/executors/ray_distributed_executor.py:L245"), [`_initialize_ray_cluster`](../catalog/src/vllm_torchtpu/executors/ray_distributed_executor_v2.md#RayDistributedExecutorV2._initialize_ray_cluster "src/vllm_torchtpu/executors/ray_distributed_executor_v2.py:L612")

<!-- area:auto:end -->
