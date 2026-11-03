---
title: 'Module: src/vllm_torchtpu/executors/tpu_multiproc_executor.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/executors/tpu_multiproc_executor.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.executors.tpu_multiproc_executor`/TpuMultiprocExecutor#
symbols:
  TpuMultiprocExecutor: ''
  TpuMultiprocExecutor._init_executor: _init_executor().
  TpuMultiprocExecutor.get_kv_cache_specs: get_kv_cache_specs().
  TpuMultiprocExecutor.initialize_from_config: initialize_from_config().
---
# Module: [`src/vllm_torchtpu/executors/tpu_multiproc_executor.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/tpu_multiproc_executor.py)

## Classes
### <a id="TpuMultiprocExecutor"></a>`TpuMultiprocExecutor`
- def: [`src/vllm_torchtpu/executors/tpu_multiproc_executor.py:27`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/tpu_multiproc_executor.py#L27)
- signature: `class TpuMultiprocExecutor(MultiprocExecutor):`
- members:
  - <a id="TpuMultiprocExecutor.get_kv_cache_specs"></a>`get_kv_cache_specs(self)` — [`L35`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/tpu_multiproc_executor.py#L35)
  - <a id="TpuMultiprocExecutor.initialize_from_config"></a>`initialize_from_config(self, kv_cache_configs: list[KVCacheConfig])` — [`L52`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/tpu_multiproc_executor.py#L52)
- protocol/private: <a id="TpuMultiprocExecutor._init_executor"></a>`_init_executor`[`L28`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/executors/tpu_multiproc_executor.py#L28)
- uses (calls/refs, reference-scoped): [`reconcile_num_gpu_blocks_override`](kv_block_override.md#reconcile_num_gpu_blocks_override), [`_patch_multiproc_worker_global_rank_env`](../__init__.md#_patch_multiproc_worker_global_rank_env)
- used by: [`check_and_update_config`](../platforms/tpu_platform.md#TpuPlatform.check_and_update_config)

