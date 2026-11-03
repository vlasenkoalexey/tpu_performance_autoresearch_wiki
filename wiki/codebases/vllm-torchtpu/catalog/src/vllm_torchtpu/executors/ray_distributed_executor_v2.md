---
title: 'Module: src/vllm_torchtpu/executors/ray_distributed_executor_v2.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/executors/ray_distributed_executor_v2.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.executors.ray_distributed_executor_v2`/
symbols:
  RayDistributedExecutorV2.driver_env_vars: RayDistributedExecutorV2#driver_env_vars.
  logger: logger.
  RayDistributedExecutorV2.shutdown_lock: RayDistributedExecutorV2#shutdown_lock.
  RayDistributedExecutorV2.response_mqs: RayDistributedExecutorV2#response_mqs.
  RayDistributedExecutorV2._initialize_ray_cluster: RayDistributedExecutorV2#_initialize_ray_cluster().
  RayDistributedExecutorV2.ray_worker_handles: RayDistributedExecutorV2#ray_worker_handles.
  RayDistributedExecutorV2.has_connector: RayDistributedExecutorV2#has_connector.
  RayDistributedExecutorV2._get_dp_geometry: RayDistributedExecutorV2#_get_dp_geometry().
  RayDistributedExecutorV2._slice_host_layout: RayDistributedExecutorV2#_slice_host_layout().
  RayDistributedExecutorV2.rpc_broadcast_mq: RayDistributedExecutorV2#rpc_broadcast_mq.
  RayDistributedExecutorV2.get_kv_cache_specs: RayDistributedExecutorV2#get_kv_cache_specs().
  RayDistributedExecutorV2: RayDistributedExecutorV2#
  get_tpu_bundles_for_indices: get_tpu_bundles_for_indices().
  RayDistributedExecutorV2._get_actor_resource_kwargs: RayDistributedExecutorV2#_get_actor_resource_kwargs().
  RayDistributedExecutorV2._get_bundle_assignments: RayDistributedExecutorV2#_get_bundle_assignments().
  RayDistributedExecutorV2._init_executor: RayDistributedExecutorV2#_init_executor().
  RayDistributedExecutorV2._finalizer: RayDistributedExecutorV2#_finalizer.
  RayDistributedExecutorV2.is_failed: RayDistributedExecutorV2#is_failed.
  RayDistributedExecutorV2.failure_callback: RayDistributedExecutorV2#failure_callback.
  RayDistributedExecutorV2.shutting_down: RayDistributedExecutorV2#shutting_down.
  RayDistributedExecutorV2.futures_queue: RayDistributedExecutorV2#futures_queue.
  RayDistributedExecutorV2.output_rank: RayDistributedExecutorV2#output_rank.
  RayDistributedExecutorV2.initialize_from_config: RayDistributedExecutorV2#initialize_from_config().
  RayDistributedExecutorV2.bundle_assignments: RayDistributedExecutorV2#bundle_assignments.
---
# Module: [`src/vllm_torchtpu/executors/ray_distributed_executor_v2.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py)

## Classes
### <a id="RayDistributedExecutorV2"></a>`RayDistributedExecutorV2`
- def: [`src/vllm_torchtpu/executors/ray_distributed_executor_v2.py:72`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L72)
- doc: Ray-based distributed executor V2 for TPU.
- signature: `class RayDistributedExecutorV2(RayExecutorV2):`
- members:
  - <a id="RayDistributedExecutorV2._get_actor_resource_kwargs"></a>`_get_actor_resource_kwargs(self)` — [`L184`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L184) — Return Ray actor resource kwargs for the TPU platform.
  - <a id="RayDistributedExecutorV2._get_dp_geometry"></a>`_get_dp_geometry(self)` — [`L80`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L80) — Return (dp_size, dp_rank, slice_world_size) for this engine.
  - <a id="RayDistributedExecutorV2._init_executor"></a>`_init_executor(self)` — [`L193`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L193) — Initialize the RayDistributedExecutorV2 executor.
  - <a id="RayDistributedExecutorV2._initialize_ray_cluster"></a>`_initialize_ray_cluster(self)` — [`L612`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L612) — Initialize Ray and select this engine's placement group.
  - <a id="RayDistributedExecutorV2._slice_host_layout"></a>`_slice_host_layout(self, device_str: str)` — [`L107`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L107) — Return the slice's hosts in rank order and their device counts.
  - <a id="RayDistributedExecutorV2.get_kv_cache_specs"></a>`get_kv_cache_specs(self)` — [`L737`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L737)
  - <a id="RayDistributedExecutorV2.initialize_from_config"></a>`initialize_from_config(self, kv_cache_configs: list[KVCacheConfig])` — [`L757`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L757)
  - <a id="RayDistributedExecutorV2.bundle_assignments"></a>`bundle_assignments` — [`L792`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L792)
  - <a id="RayDistributedExecutorV2.driver_env_vars"></a>`driver_env_vars` — [`L284`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L284) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="RayDistributedExecutorV2.failure_callback"></a>`failure_callback` — [`L211`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L211)
  - <a id="RayDistributedExecutorV2.futures_queue"></a>`futures_queue` — [`L599`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L599)
  - <a id="RayDistributedExecutorV2.has_connector"></a>`has_connector` — [`L606`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L606)
  - <a id="RayDistributedExecutorV2.is_failed"></a>`is_failed` — [`L210`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L210)
  - <a id="RayDistributedExecutorV2.output_rank"></a>`output_rank` — [`L603`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L603)
  - <a id="RayDistributedExecutorV2.ray_worker_handles"></a>`ray_worker_handles` — [`L280`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L280)
  - <a id="RayDistributedExecutorV2.response_mqs"></a>`response_mqs` — [`L582`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L582)
  - <a id="RayDistributedExecutorV2.rpc_broadcast_mq"></a>`rpc_broadcast_mq` — [`L267`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L267)
  - <a id="RayDistributedExecutorV2.shutdown_lock"></a>`shutdown_lock` — [`L213`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L213)
  - <a id="RayDistributedExecutorV2.shutting_down"></a>`shutting_down` — [`L212`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L212)
- protocol/private: <a id="RayDistributedExecutorV2._finalizer"></a>`_finalizer`[`L209`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L209), <a id="RayDistributedExecutorV2._get_bundle_assignments"></a>`_get_bundle_assignments`[`L768`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L768)
- uses (calls/refs, reference-scoped): [`get_tpu_multihost_topology`](../platforms/tpu_platform.md#get_tpu_multihost_topology), [`reconcile_num_gpu_blocks_override`](kv_block_override.md#reconcile_num_gpu_blocks_override), [`logger`](ray_distributed_executor_v2.md#logger), [`slice_binding_env`](../worker/tpu_rank_binding.md#slice_binding_env), [`get_dp_size`](../utils.md#get_dp_size), [`set_node_kv_ip_port`](../distributed/utils.md#set_node_kv_ip_port), [`TORCH_TPU_BASE_PORT`](../envs.md#TORCH_TPU_BASE_PORT), [`get_tpu_bundles_for_indices`](ray_distributed_executor_v2.md#get_tpu_bundles_for_indices)
- used by: [`check_and_update_config`](../platforms/tpu_platform.md#TpuPlatform.check_and_update_config)

## Functions
- <a id="get_tpu_bundles_for_indices"></a>`get_tpu_bundles_for_indices(placement_group, bundle_indices: list[int], bundle_to_node_id: list[tuple[int, str, str]] | None = None)` — [`L49`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L49) — Return bundle metadata for the specified bundle indices.

## Module values
- <a id="logger"></a>`logger` — [`L69`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor_v2.py#L69)

