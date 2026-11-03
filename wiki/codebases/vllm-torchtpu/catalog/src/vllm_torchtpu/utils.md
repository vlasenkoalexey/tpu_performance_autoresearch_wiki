---
title: 'Module: src/vllm_torchtpu/utils.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/utils.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.utils`/
symbols:
  synchronize_tensors: synchronize_tensors().
  fresh_buffer: fresh_buffer().
  compute_hbm_budget: compute_hbm_budget().
  GBYTES: GBYTES.
  align_to: align_to().
  get_dp_size: get_dp_size().
  hbm_usage_bytes: hbm_usage_bytes().
  logger: logger.
  hbm_usage_gb: hbm_usage_gb().
  get_megacore: get_megacore().
  min_across_ep_dp: min_across_ep_dp().
  HbmBudget.available: HbmBudget#available.
  synchronize_device: synchronize_device().
  time_function.wrapper: time_function().wrapper().
  TPU_HEAD_SIZE_ALIGNMENT: TPU_HEAD_SIZE_ALIGNMENT.
  _megacore: _megacore.
  largest_divisor: largest_divisor().
  get_mesh_shape_product: get_mesh_shape_product().
  HbmBudget.total_limit: HbmBudget#total_limit.
  HbmBudget.total_used: HbmBudget#total_used.
  HbmBudget.cap: HbmBudget#cap.
  HbmReserves.lora_slot_write: HbmReserves#lora_slot_write.
  enable_megacore: enable_megacore().
  time_function: time_function().
  get_num_kv_heads_by_tp: get_num_kv_heads_by_tp().
  get_device_name: get_device_name().
  HbmBudget: HbmBudget#
  HbmReserves: HbmReserves#
  HbmReserves.kv_connector: HbmReserves#kv_connector.
  HbmReserves.pp_handoff: HbmReserves#pp_handoff.
  get_dtype_packing: get_dtype_packing().
  tpu_bind_kv_cache: tpu_bind_kv_cache().
  estimate_kv_connector_hbm_reserve: estimate_kv_connector_hbm_reserve().
  _FLOAT8_DTYPES: _FLOAT8_DTYPES.
  TPU_SECOND_LAST_MINOR: TPU_SECOND_LAST_MINOR.
  get_padded_head_dim: get_padded_head_dim().
  get_padded_num_heads: get_padded_num_heads().
  get_hash_fn_by_name: get_hash_fn_by_name().
---
# Module: [`src/vllm_torchtpu/utils.py`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py)

## Classes
### <a id="HbmBudget"></a>`HbmBudget`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/utils.py:190`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L190) — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- doc: HBM accounting for the KV-cache budget, summed across devices.
- signature: `class HbmBudget(NamedTuple):`
- members:
  - <a id="HbmBudget.available"></a>`available` — [`L203`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L203)
  - <a id="HbmBudget.cap"></a>`cap` — [`L202`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L202)
  - <a id="HbmBudget.total_limit"></a>`total_limit` — [`L200`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L200)
  - <a id="HbmBudget.total_used"></a>`total_used` — [`L201`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L201)
- used by: [`determine_available_memory`](worker/tpu_worker.md#TPUWorker.determine_available_memory), [`fit_num_blocks_to_hbm`](experimental/export/universal_adapter.md#UniversalVllmExportableLLM.fit_num_blocks_to_hbm), [`_available_kv_cache_hbm`](runner/kv_cache_manager.md#KVCacheManager._available_kv_cache_hbm), [`compute_hbm_budget`](utils.md#compute_hbm_budget)

### <a id="HbmReserves"></a>`HbmReserves`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/utils.py:206`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L206)
- doc: HBM allocated after profile_run, which the KV-cache budget must leave
- signature: `class HbmReserves(NamedTuple):`
- members:
  - <a id="HbmReserves.kv_connector"></a>`kv_connector` — [`L217`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L217)
  - <a id="HbmReserves.lora_slot_write"></a>`lora_slot_write` — [`L218`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L218)
  - <a id="HbmReserves.pp_handoff"></a>`pp_handoff` — [`L219`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L219)
- used by: [`determine_available_memory`](worker/tpu_worker.md#TPUWorker.determine_available_memory), [`post_profile_hbm_reserves`](runner/tpu_runner.md#TPUModelRunner.post_profile_hbm_reserves)

## Functions
- <a id="align_to"></a>`align_to(unpadded_dim, pad_multiple)` — [`L38`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L38) — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- <a id="compute_hbm_budget"></a>`compute_hbm_budget(devices: Any, gpu_memory_utilization: float)` — [`L222`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L222) — Compute the HBM budget available for the KV cache. — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- <a id="enable_megacore"></a>`enable_megacore()` — [`L42`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L42)
- <a id="estimate_kv_connector_hbm_reserve"></a>`estimate_kv_connector_hbm_reserve(vllm_config: Any)` — [`L237`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L237) — Return HBM allocated after profiling by the configured KV connector. — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- <a id="fresh_buffer"></a>`fresh_buffer(t: torch.Tensor)` — [`L395`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L395) — Return a copy of `t` backed by a fresh device buffer of its own shape. — documented in [kimi-k3-model](../../../concepts/kimi-k3-model.md)
- <a id="get_device_name"></a>`get_device_name(num_devices: int | None = None)` — [`L123`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L123) — documented in [ragged-paged-attention-kernel](../../../concepts/ragged-paged-attention-kernel.md)
- <a id="get_dp_size"></a>`get_dp_size(parallel_config)` — [`L68`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L68) — documented in [compilation-and-graph-capture](../../../concepts/compilation-and-graph-capture.md)
- <a id="get_dtype_packing"></a>`get_dtype_packing(dtype)` — [`L282`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L282)
- <a id="get_hash_fn_by_name"></a>`get_hash_fn_by_name(hash_fn_name: str)` — [`L287`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L287) — A wrapper function of vllm.utils.hashing.get_hash_fn_by_name to support builtin
- <a id="get_megacore"></a>`get_megacore()` — [`L47`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L47)
- <a id="get_mesh_shape_product"></a>`get_mesh_shape_product(mesh: Mesh, axes: str | list[str] | None)` — [`L152`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L152) — Get the product of mesh dimensions for one or more axes.
- <a id="get_num_kv_heads_by_tp"></a>`get_num_kv_heads_by_tp(num_kv_heads: int, tp_size: int)` — [`L59`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L59)
- <a id="get_padded_head_dim"></a>`get_padded_head_dim(head_dim: int)` — [`L264`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L264) — Pads head_dim up to the nearest multiple of 128 for kernel performance.
- <a id="get_padded_num_heads"></a>`get_padded_num_heads(num_heads: int, sharding_size: int)` — [`L273`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L273)
- <a id="hbm_usage_bytes"></a>`hbm_usage_bytes(devices: Any)` — [`L92`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L92)
- <a id="hbm_usage_gb"></a>`hbm_usage_gb(devices: Any)` — [`L182`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L182)
- <a id="largest_divisor"></a>`largest_divisor(x: int, cap: int)` — [`L51`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L51) — Largest divisor of `x` that is <= `cap`.
- <a id="min_across_ep_dp"></a>`min_across_ep_dp(parallel_config, value: int)` — [`L75`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L75) — Return the minimum of `value` across the DP engines coupled by EP.
- <a id="synchronize_device"></a>`synchronize_device()` — [`L344`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L344) — Synchronize the TPU hardware execution stream (Device Stream Barrier).
- <a id="synchronize_tensors"></a>`synchronize_tensors(tensors: torch.Tensor | Sequence[torch.Tensor] | None = None, wait: bool = True)` — [`L358`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L358) — Synchronize TPU execution and force materialization of deferred tensors — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- <a id="time_function"></a>`time_function(func)` — [`L296`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L296) — A decorator to measure the execution time of a function.
- <a id="tpu_bind_kv_cache"></a>`tpu_bind_kv_cache(kv_caches: Mapping[str, torch.Tensor | Sequence[torch.Tensor]], forward_context: dict[str, Any], runner_kv_caches: list[torch.Tensor], num_attn_module: int = 1)` — [`L315`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L315) — Bind kv_caches to ModelRunner and forward context.
- <a id="time_function.wrapper"></a>`wrapper(*args, **kwargs)` — [`L302`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L302)

## Module values
- <a id="GBYTES"></a>`GBYTES` — [`L30`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L30)
- <a id="TPU_HEAD_SIZE_ALIGNMENT"></a>`TPU_HEAD_SIZE_ALIGNMENT` — [`L31`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L31)
- <a id="TPU_SECOND_LAST_MINOR"></a>`TPU_SECOND_LAST_MINOR` — [`L32`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L32)
- <a id="_FLOAT8_DTYPES"></a>`_FLOAT8_DTYPES` — [`L384`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L384)
- <a id="_megacore"></a>`_megacore` — [`L34`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L34)
- <a id="logger"></a>`logger` — [`L35`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/utils.py#L35)

