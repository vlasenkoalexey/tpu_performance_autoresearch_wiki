---
title: 'Module: src/vllm_torchtpu/executors/ray_distributed_executor.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/executors/ray_distributed_executor.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.executors.ray_distributed_executor`/
symbols:
  logger: logger.
  RayDistributedExecutor._init_workers_ray: RayDistributedExecutor#_init_workers_ray().
  RayDistributedExecutor.pp_tp_workers: RayDistributedExecutor#pp_tp_workers.
  RayDistributedExecutor.use_ray_spmd_worker: RayDistributedExecutor#use_ray_spmd_worker.
  AsyncResultFuture.result: AsyncResultFuture#result().
  RayDistributedExecutor.workers: RayDistributedExecutor#workers.
  RayDistributedExecutor._env_vars_for_all_workers: RayDistributedExecutor#_env_vars_for_all_workers.
  RayDistributedExecutor._execute_dag: RayDistributedExecutor#_execute_dag().
  RayWorkerWrapper.execute_model_ray: RayWorkerWrapper#execute_model_ray().
  RayWorkerWrapper.get_execute_model_output: RayWorkerWrapper#get_execute_model_output().
  RayDistributedExecutor.has_connector: RayDistributedExecutor#has_connector.
  RayDistributedExecutor._initialize_ray_cluster: RayDistributedExecutor#_initialize_ray_cluster().
  RayWorkerWrapper.setup_device_if_necessary: RayWorkerWrapper#setup_device_if_necessary().
  RayDistributedExecutor.forward_dag: RayDistributedExecutor#forward_dag.
  RayWorkerWrapper.result_id: RayWorkerWrapper#result_id.
  RayWorkerWrapper: RayWorkerWrapper#
  AsyncResultFuture.aggregator: AsyncResultFuture#aggregator.
  RayDistributedExecutor: RayDistributedExecutor#
  RayWorkerWrapper._execute_model_outputs: RayWorkerWrapper#_execute_model_outputs.
  AsyncResultFuture: AsyncResultFuture#
  AsyncResultFuture.result_ids_ref: AsyncResultFuture#result_ids_ref.
  AsyncResultFuture.workers: AsyncResultFuture#workers.
  RayDistributedExecutor.sort_by_driver_then_worker_ip: RayDistributedExecutor#sort_by_driver_then_worker_ip().
  RayWorkerWrapper.compiled_dag_cuda_device_set: RayWorkerWrapper#compiled_dag_cuda_device_set.
  AsyncResultFuture.__init__: AsyncResultFuture#__init__().
  RayDistributedExecutor.supports_async_scheduling: RayDistributedExecutor#supports_async_scheduling().
  RayDistributedExecutor._init_executor: RayDistributedExecutor#_init_executor().
  RayDistributedExecutor.use_ray_compiled_dag: RayDistributedExecutor#use_ray_compiled_dag.
  RayDistributedExecutor.pp_locks: RayDistributedExecutor#pp_locks.
  RayDistributedExecutor.scheduler_output: RayDistributedExecutor#scheduler_output.
  RayDistributedExecutor.uses_sampler: RayDistributedExecutor#uses_sampler.
  RayDistributedExecutor.get_kv_connector_handshake_metadata: RayDistributedExecutor#get_kv_connector_handshake_metadata().
  RayWorkerWrapper.__init__: RayWorkerWrapper#__init__().
---
# Module: [`src/vllm_torchtpu/executors/ray_distributed_executor.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py)

## Classes
### <a id="AsyncResultFuture"></a>`AsyncResultFuture`  ·  implements/extends Future
- def: [`src/vllm_torchtpu/executors/ray_distributed_executor.py:52`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L52)
- signature: `class AsyncResultFuture(Future):`
- members:
  - <a id="AsyncResultFuture.result"></a>`result(self, timeout=None)` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L59)
  - <a id="AsyncResultFuture.aggregator"></a>`aggregator` — [`L57`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L57)
  - <a id="AsyncResultFuture.result_ids_ref"></a>`result_ids_ref` — [`L55`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L55)
  - <a id="AsyncResultFuture.workers"></a>`workers` — [`L56`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L56)
- protocol/private: <a id="AsyncResultFuture.__init__"></a>`__init__`[`L53`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L53)
- used by: [`_execute_dag`](ray_distributed_executor.md#RayDistributedExecutor._execute_dag)

### <a id="RayDistributedExecutor"></a>`RayDistributedExecutor`
- def: [`src/vllm_torchtpu/executors/ray_distributed_executor.py:73`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L73)
- doc: Ray-based distributed executor for TPU.
- signature: `class RayDistributedExecutor(RayDistributedExecutorV1):`
- members:
  - <a id="RayDistributedExecutor._initialize_ray_cluster"></a>`_initialize_ray_cluster(self)` — [`L140`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L140) — Initialize the distributed cluster with Ray.
  - <a id="RayDistributedExecutor.get_kv_connector_handshake_metadata"></a>`get_kv_connector_handshake_metadata(self)` — [`L545`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L545)
  - <a id="RayDistributedExecutor.sort_by_driver_then_worker_ip"></a>`sort_by_driver_then_worker_ip(item: RayWorkerMetaData)` — [`L328`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L328) — Sort the workers based on 3 properties:
  - <a id="RayDistributedExecutor.supports_async_scheduling"></a>`supports_async_scheduling(cls)` — [`L92`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L92) — Whether the executor supports async scheduling.
  - <a id="RayDistributedExecutor.forward_dag"></a>`forward_dag` — [`L99`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L99)
  - <a id="RayDistributedExecutor.has_connector"></a>`has_connector` — [`L130`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L130)
  - <a id="RayDistributedExecutor.pp_locks"></a>`pp_locks` — [`L125`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L125)
  - <a id="RayDistributedExecutor.pp_tp_workers"></a>`pp_tp_workers` — [`L252`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L252)
  - <a id="RayDistributedExecutor.scheduler_output"></a>`scheduler_output` — [`L127`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L127)
  - <a id="RayDistributedExecutor.use_ray_compiled_dag"></a>`use_ray_compiled_dag` — [`L104`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L104)
  - <a id="RayDistributedExecutor.use_ray_spmd_worker"></a>`use_ray_spmd_worker` — [`L109`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L109)
  - <a id="RayDistributedExecutor.uses_sampler"></a>`uses_sampler` — [`L135`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L135)
  - <a id="RayDistributedExecutor.workers"></a>`workers` — [`L247`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L247)
- protocol/private: <a id="RayDistributedExecutor._env_vars_for_all_workers"></a>`_env_vars_for_all_workers`[`L467`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L467), <a id="RayDistributedExecutor._execute_dag"></a>`_execute_dag`[`L551`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L551), <a id="RayDistributedExecutor._init_executor"></a>`_init_executor`[`L98`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L98), <a id="RayDistributedExecutor._init_workers_ray"></a>`_init_workers_ray`[`L245`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L245)
- uses (calls/refs, reference-scoped): [`get_tpu_multihost_topology`](../platforms/tpu_platform.md#get_tpu_multihost_topology), [`logger`](ray_distributed_executor.md#logger), [`set_node_kv_ip_port`](../distributed/utils.md#set_node_kv_ip_port), [`TORCH_TPU_BASE_PORT`](../envs.md#TORCH_TPU_BASE_PORT), [`RayWorkerWrapper`](ray_distributed_executor.md#RayWorkerWrapper), [`AsyncResultFuture`](ray_distributed_executor.md#AsyncResultFuture), [`RAY_USAGE_STATS_ENABLED`](../envs.md#RAY_USAGE_STATS_ENABLED)
- used by: [`check_and_update_config`](../platforms/tpu_platform.md#TpuPlatform.check_and_update_config)

### <a id="RayWorkerWrapper"></a>`RayWorkerWrapper`
- def: [`src/vllm_torchtpu/executors/ray_distributed_executor.py:569`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L569)
- members:
  - <a id="RayWorkerWrapper.execute_model_ray"></a>`execute_model_ray(self, execute_model_input: tuple[SchedulerOutput, GrammarOutput] | tuple[SchedulerOutput, GrammarOutput, IntermediateTensors])` — [`L595`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L595)
  - <a id="RayWorkerWrapper.get_execute_model_output"></a>`get_execute_model_output(self, result_id)` — [`L629`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L629)
  - <a id="RayWorkerWrapper.setup_device_if_necessary"></a>`setup_device_if_necessary(self)` — [`L583`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L583)
  - <a id="RayWorkerWrapper.compiled_dag_cuda_device_set"></a>`compiled_dag_cuda_device_set` — [`L590`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L590)
  - <a id="RayWorkerWrapper.result_id"></a>`result_id` — [`L581`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L581)
- protocol/private: <a id="RayWorkerWrapper.__init__"></a>`__init__`[`L576`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L576), <a id="RayWorkerWrapper._execute_model_outputs"></a>`_execute_model_outputs`[`L580`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L580)
- uses (calls/refs, reference-scoped): [`get_output`](../runner/tpu_runner_async_output.md#AsyncTPUModelRunnerOutput.get_output), [`AsyncTPUModelRunnerOutput`](../runner/tpu_runner_async_output.md#AsyncTPUModelRunnerOutput)
- used by: [`pp_tp_workers`](ray_distributed_executor.md#RayDistributedExecutor.pp_tp_workers), [`workers`](ray_distributed_executor.md#RayDistributedExecutor.workers)

## Module values
- <a id="logger"></a>`logger` — [`L49`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/ray_distributed_executor.py#L49)

