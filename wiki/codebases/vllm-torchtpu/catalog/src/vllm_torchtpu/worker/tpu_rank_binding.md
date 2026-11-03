---
title: 'Module: src/vllm_torchtpu/worker/tpu_rank_binding.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/worker/tpu_rank_binding.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.worker.tpu_rank_binding`/
symbols:
  _slice_binding_from_env: _slice_binding_from_env().
  get_tpu_worker_binding: get_tpu_worker_binding().
  _SLICE_BINDING_ENV_VARS: _SLICE_BINDING_ENV_VARS.
  TpuWorkerBinding.as_env: TpuWorkerBinding#as_env().
  slice_binding_env: slice_binding_env().
  TpuWorkerBinding.local_rank: TpuWorkerBinding#local_rank.
  TpuWorkerBinding.world_size: TpuWorkerBinding#world_size.
  TpuWorkerBinding.rank: TpuWorkerBinding#rank.
  TpuWorkerBinding.init_local_rank: TpuWorkerBinding#init_local_rank.
  TpuWorkerBinding.local_world_size: TpuWorkerBinding#local_world_size.
  TpuWorkerBinding.init_world_size: TpuWorkerBinding#init_world_size.
  TpuWorkerBinding: TpuWorkerBinding#
  TpuWorkerBinding.init_rank: TpuWorkerBinding#init_rank.
  TpuWorkerBinding.native_local_rank: TpuWorkerBinding#native_local_rank.
  TpuWorkerBinding.dp_rank: TpuWorkerBinding#dp_rank.
  _get_spawned_pcp_local_rank: _get_spawned_pcp_local_rank().
  SLICE_RANK_ENV: SLICE_RANK_ENV.
  SLICE_LOCAL_RANK_ENV: SLICE_LOCAL_RANK_ENV.
  SLICE_WORLD_SIZE_ENV: SLICE_WORLD_SIZE_ENV.
  SLICE_LOCAL_WORLD_SIZE_ENV: SLICE_LOCAL_WORLD_SIZE_ENV.
  _get_int_env: _get_int_env().
  TpuWorkerBinding.dp_size: TpuWorkerBinding#dp_size.
  TpuWorkerBinding.local_rank_offset: TpuWorkerBinding#local_rank_offset.
  logger: logger.
---
# Module: [`src/vllm_torchtpu/worker/tpu_rank_binding.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py)

## Classes
### <a id="TpuWorkerBinding"></a>`TpuWorkerBinding`
- def: [`src/vllm_torchtpu/worker/tpu_rank_binding.py:82`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L82)
- signature: `class TpuWorkerBinding:`
- members:
  - <a id="TpuWorkerBinding.as_env"></a>`as_env(self)` — [`L95`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L95)
  - <a id="TpuWorkerBinding.dp_rank"></a>`dp_rank` — [`L91`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L91)
  - <a id="TpuWorkerBinding.dp_size"></a>`dp_size` — [`L92`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L92)
  - <a id="TpuWorkerBinding.init_local_rank"></a>`init_local_rank` — [`L89`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L89)
  - <a id="TpuWorkerBinding.init_rank"></a>`init_rank` — [`L87`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L87)
  - <a id="TpuWorkerBinding.init_world_size"></a>`init_world_size` — [`L88`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L88)
  - <a id="TpuWorkerBinding.local_rank"></a>`local_rank` — [`L84`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L84)
  - <a id="TpuWorkerBinding.local_rank_offset"></a>`local_rank_offset` — [`L93`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L93)
  - <a id="TpuWorkerBinding.local_world_size"></a>`local_world_size` — [`L86`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L86)
  - <a id="TpuWorkerBinding.native_local_rank"></a>`native_local_rank` — [`L90`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L90)
  - <a id="TpuWorkerBinding.rank"></a>`rank` — [`L83`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L83)
  - <a id="TpuWorkerBinding.world_size"></a>`world_size` — [`L85`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L85)
- used by: [`init_device`](tpu_worker.md#TPUWorker.init_device), [`_slice_binding_from_env`](tpu_rank_binding.md#_slice_binding_from_env), [`get_tpu_worker_binding`](tpu_rank_binding.md#get_tpu_worker_binding), [`_wrapped`](../__init__.md#_patch_multiproc_worker_global_rank_env._wrapped)

## Functions
- <a id="_get_int_env"></a>`_get_int_env(env: Mapping[str, str], name: str, default: int)` — [`L74`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L74)
- <a id="_get_spawned_pcp_local_rank"></a>`_get_spawned_pcp_local_rank(*, env: Mapping[str, str], local_rank_offset: int, local_world: int)` — [`L104`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L104) — LOCAL_RANK a spawned PCP worker was handed by its parent.
- <a id="_slice_binding_from_env"></a>`_slice_binding_from_env(env: Mapping[str, str], *, parallel_config, rank: int, dp_rank: int, dp_size: int, pcp_size: int, local_rank_offset: int)` — [`L142`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L142) — Return the executor-assigned binding, or None when none was supplied.
- <a id="get_tpu_worker_binding"></a>`get_tpu_worker_binding(parallel_config, rank: int, local_rank: int, *, env: Mapping[str, str], use_spawned_pcp_local_rank: bool = False)` — [`L212`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L212)
- <a id="slice_binding_env"></a>`slice_binding_env(*, rank: int, local_rank: int, world_size: int, local_world_size: int)` — [`L121`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L121) — Return env describing an executor-assigned slice-global placement.

## Module values
- <a id="SLICE_LOCAL_RANK_ENV"></a>`SLICE_LOCAL_RANK_ENV` — [`L62`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L62)
- <a id="SLICE_LOCAL_WORLD_SIZE_ENV"></a>`SLICE_LOCAL_WORLD_SIZE_ENV` — [`L64`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L64)
- <a id="SLICE_RANK_ENV"></a>`SLICE_RANK_ENV` — [`L61`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L61)
- <a id="SLICE_WORLD_SIZE_ENV"></a>`SLICE_WORLD_SIZE_ENV` — [`L63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L63)
- <a id="_SLICE_BINDING_ENV_VARS"></a>`_SLICE_BINDING_ENV_VARS` — [`L66`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L66)
- <a id="logger"></a>`logger` — [`L54`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_rank_binding.py#L54)

