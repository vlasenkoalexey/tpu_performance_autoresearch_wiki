---
title: 'Module: src/vllm_torchtpu/runner/kv_cache_manager.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/runner/kv_cache_manager.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.runner.kv_cache_manager`/
symbols:
  KVCacheManager.runner: KVCacheManager#runner.
  KVCacheManager.initialize_kv_cache: KVCacheManager#initialize_kv_cache().
  KVCacheManager._initialize_unified_kv_cache: KVCacheManager#_initialize_unified_kv_cache().
  KVCacheManager.get_kv_cache_spec: KVCacheManager#get_kv_cache_spec().
  KVCacheManager._update_mamba_page_size_padded: KVCacheManager#_update_mamba_page_size_padded().
  KVCacheManager._update_attention_page_size_padded: KVCacheManager#_update_attention_page_size_padded().
  KVCacheManager._maybe_set_compact_mamba_num_blocks_override: KVCacheManager#_maybe_set_compact_mamba_num_blocks_override().
  KVCacheManager._bind_block_major_pool_layers: KVCacheManager#_bind_block_major_pool_layers().
  KVCacheManager._available_kv_cache_hbm: KVCacheManager#_available_kv_cache_hbm().
  KVCacheManager._pad_native_attention_regions: KVCacheManager#_pad_native_attention_regions().
  logger: logger.
  _warn_if_kv_cache_is_padded: _warn_if_kv_cache_is_padded().
  KVCacheManager._maybe_set_num_blocks_override: KVCacheManager#_maybe_set_num_blocks_override().
  KVCacheManager._check_block_major_pool_supported: KVCacheManager#_check_block_major_pool_supported().
  sparse_mla_page_size_bytes: sparse_mla_page_size_bytes().
  KVCacheManager.allocate_attention_region: KVCacheManager#allocate_attention_region().
  KVCacheManager._per_layer_spec: KVCacheManager#_per_layer_spec().
  KVCacheManager.ds_v4: KVCacheManager#ds_v4.
  KVCacheManager._validate_shared_kv_cache_layout: KVCacheManager#_validate_shared_kv_cache_layout().
  KVCacheManager._maybe_add_kv_sharing_layers_to_kv_cache_groups: KVCacheManager#_maybe_add_kv_sharing_layers_to_kv_cache_groups().
  KVCacheManager._add_shared_kv_cache_aliases: KVCacheManager#_add_shared_kv_cache_aliases().
  _TpuKVCacheBackend.get_kv_cache_page_size_bytes: _TpuKVCacheBackend#get_kv_cache_page_size_bytes().
  KVCacheManager.__init__: KVCacheManager#__init__().
  _TpuKVCacheBackend: _TpuKVCacheBackend#
  _TpuKVCacheBackend.get_kv_cache_shape: _TpuKVCacheBackend#get_kv_cache_shape().
  is_cache_for_ds_v4: is_cache_for_ds_v4().
  KVCacheManager: KVCacheManager#
  _TpuKVCacheBackend.get_name: _TpuKVCacheBackend#get_name().
  check_kv_caches_cover_block_ids: check_kv_caches_cover_block_ids().
  KVCacheManager.get_kv_prewarm_shapes: KVCacheManager#get_kv_prewarm_shapes().
  KVCacheManager.prewarm_kv_offload_shape: KVCacheManager#prewarm_kv_offload_shape().
---
# Module: [`src/vllm_torchtpu/runner/kv_cache_manager.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py)

## Classes
### <a id="KVCacheManager"></a>`KVCacheManager`
- def: [`src/vllm_torchtpu/runner/kv_cache_manager.py:222`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L222)
- doc: Owns the KV-cache spec/sizing half of `TPUModelRunner`.
- signature: `class KVCacheManager:`
- members:
  - <a id="KVCacheManager._available_kv_cache_hbm"></a>`_available_kv_cache_hbm(self)` — [`L897`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L897) — KV-cache HBM budget for the block-count override paths. — documented in [kv-cache-layout-and-hbm-budget](../../../../concepts/kv-cache-layout-and-hbm-budget.md)
  - <a id="KVCacheManager._bind_block_major_pool_layers"></a>`_bind_block_major_pool_layers(self, layout: BlockMajorPoolLayout)` — [`L1329`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L1329) — Binds each unified-pool layer to its region index within the merged pool. — documented in [kv-cache-layout-and-hbm-budget](../../../../concepts/kv-cache-layout-and-hbm-budget.md)
  - <a id="KVCacheManager._check_block_major_pool_supported"></a>`_check_block_major_pool_supported(self)` — [`L1306`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L1306) — Refuses execution features the block-major unified pool cannot index.
  - <a id="KVCacheManager._maybe_set_compact_mamba_num_blocks_override"></a>`_maybe_set_compact_mamba_num_blocks_override(self, attn_page_size_bytes: int, unpadded_mamba_page_size_bytes: int, num_attn_groups: int, num_mamba_groups: int, group_size: int)` — [`L918`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L918) — Cap mamba layers at `max_num_reqs + 1` recurrent slots and pin
  - <a id="KVCacheManager._maybe_set_num_blocks_override"></a>`_maybe_set_num_blocks_override(self, attn_page_size_bytes: int, uniform_page_size_bytes: int, group_size: int)` — [`L1051`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L1051) — Pin `cache_config.num_gpu_blocks_override` to the two-step
  - <a id="KVCacheManager._update_attention_page_size_padded"></a>`_update_attention_page_size_padded(self, layers: dict[str, AttentionLayerBase], block_size: int)` — [`L653`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L653) — Pad attention page sizes so vLLM's num_blocks matches what
  - <a id="KVCacheManager._update_mamba_page_size_padded"></a>`_update_mamba_page_size_padded(self, layers: dict[str, AttentionLayerBase], block_size: int | None = None)` — [`L737`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L737) — Pad attention and mamba page sizes so vLLM's num_blocks matches
  - <a id="KVCacheManager.allocate_attention_region"></a>`allocate_attention_region(region: tuple[int, int], geometry: list[tuple[tuple[int, ...], torch.dtype]])` — [`L1603`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L1603)
  - <a id="KVCacheManager.get_kv_cache_spec"></a>`get_kv_cache_spec(self)` — [`L229`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L229) — Generates the KVCacheSpec by parsing the kv cache format from each — documented in [kv-cache-layout-and-hbm-budget](../../../../concepts/kv-cache-layout-and-hbm-budget.md)
  - <a id="KVCacheManager.get_kv_prewarm_shapes"></a>`get_kv_prewarm_shapes(self)` — [`L1116`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L1116)
  - <a id="KVCacheManager.initialize_kv_cache"></a>`initialize_kv_cache(self, kv_cache_config: KVCacheConfig)` — [`L1360`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L1360) — Initialize KV cache based on `kv_cache_config`. — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="KVCacheManager.prewarm_kv_offload_shape"></a>`prewarm_kv_offload_shape(self, p: int)` — [`L1129`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L1129)
  - <a id="KVCacheManager.ds_v4"></a>`ds_v4` — [`L227`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L227)
  - <a id="KVCacheManager.runner"></a>`runner` — [`L226`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L226) — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
- protocol/private: <a id="KVCacheManager.__init__"></a>`__init__`[`L225`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L225), <a id="KVCacheManager._add_shared_kv_cache_aliases"></a>`_add_shared_kv_cache_aliases`[`L633`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L633), <a id="KVCacheManager._initialize_unified_kv_cache"></a>`_initialize_unified_kv_cache`[`L1137`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L1137), <a id="KVCacheManager._maybe_add_kv_sharing_layers_to_kv_cache_groups"></a>`_maybe_add_kv_sharing_layers_to_kv_cache_groups`[`L599`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L599), <a id="KVCacheManager._pad_native_attention_regions"></a>`_pad_native_attention_regions`[`L480`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L480), <a id="KVCacheManager._per_layer_spec"></a>`_per_layer_spec`[`L1469`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L1469), <a id="KVCacheManager._validate_shared_kv_cache_layout"></a>`_validate_shared_kv_cache_layout`[`L533`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L533)
- uses (calls/refs, reference-scoped): [`device`](tpu_runner.md#TPUModelRunner.device), [`synchronize_tensors`](../utils.md#synchronize_tensors), [`speculative_config`](tpu_runner.md#TPUModelRunner.speculative_config), [`_initialize_attention_kernels`](tpu_runner.md#TPUModelRunner._initialize_attention_kernels), [`shape`](../kernels/mla/kv_cache_utils.md#SparseMLAKVCacheSpec.shape), [`set_vllm_model_wrapper_context`](../models/vllm/vllm_model_wrapper_context.md#set_vllm_model_wrapper_context), [`_initialize_ds_v4_kv_cache`](kv_cache_dsv4.md#DsV4KVCacheAllocator._initialize_ds_v4_kv_cache), [`max_num_reqs`](tpu_runner.md#TPUModelRunner.max_num_reqs), [`get_sparse_kv_cache_specs`](../layers/adapter/attention.md#PallasMLAttentionBackend.get_sparse_kv_cache_specs), [`materialize_kv_cache_tensors`](../kv_cache_materializer.md#materialize_kv_cache_tensors), [`PallasAttentionBackend`](../layers/adapter/attention.md#PallasAttentionBackend), [`_precompile_substitute_placeholder_token`](tpu_runner.md#TPUModelRunner._precompile_substitute_placeholder_token), [`kv_cache_config`](tpu_runner.md#TPUModelRunner.kv_cache_config), [`TpuPlatform`](../platforms/tpu_platform.md#TpuPlatform), [`_precompile_mamba_state_seed_copies`](tpu_runner.md#TPUModelRunner._precompile_mamba_state_seed_copies), [`get_kv_cache_shape`](../layers/adapter/attention.md#PallasMLAttentionBackend.get_kv_cache_shape), [`kv_cache_dtype`](tpu_runner.md#TPUModelRunner.kv_cache_dtype), [`mamba_slot_read_offsets`](tpu_runner.md#TPUModelRunner.mamba_slot_read_offsets), [`PallasMLAttentionBackend`](../layers/adapter/attention.md#PallasMLAttentionBackend), [`TPUModelRunner`](tpu_runner.md#TPUModelRunner), [`_is_async_drafter`](tpu_runner.md#TPUModelRunner._is_async_drafter), [`_precompile_dense_kv_cache_block_copies`](tpu_runner.md#TPUModelRunner._precompile_dense_kv_cache_block_copies), [`PallasAttentionBackendImpl`](../layers/adapter/attention.md#PallasAttentionBackendImpl), [`post_profile_hbm_reserves`](tpu_runner.md#TPUModelRunner.post_profile_hbm_reserves), [`BlockMajorPoolLayout`](../block_major_pool.md#BlockMajorPoolLayout), [`kv_cache_quantized_dtype`](../layers/adapter/attention.md#PallasAttentionBackendImpl.kv_cache_quantized_dtype), [`mesh`](tpu_runner.md#TPUModelRunner.mesh), [`normalize_kv_cache_specs_for_tpu`](../kv_cache_spec_normalizer.md#normalize_kv_cache_specs_for_tpu), [`compute_hbm_budget`](../utils.md#compute_hbm_budget), [`get_kv_cache_shape`](../layers/adapter/attention.md#PallasAttentionBackend.get_kv_cache_shape), [`unified_block_major_enabled`](../block_major_pool.md#unified_block_major_enabled), [`logger`](kv_cache_manager.md#logger), [`may_reinitialize_input_batch`](tpu_runner.md#TPUModelRunner.may_reinitialize_input_batch), [`admit_layer`](../kernels/mla/dispatch.md#admit_layer), [`_unified_kv_layout`](tpu_runner.md#TPUModelRunner._unified_kv_layout), [`kv_cache_raw_tensors`](tpu_runner.md#TPUModelRunner.kv_cache_raw_tensors), [`_init_mamba_slot_pool`](tpu_runner.md#TPUModelRunner._init_mamba_slot_pool), [`_warn_if_kv_cache_is_padded`](kv_cache_manager.md#_warn_if_kv_cache_is_padded), [`bm_pool_layout`](../kv_cache_materializer.md#MaterializedKVCache.bm_pool_layout), [`get_kv_cache_page_size_bytes`](../layers/adapter/attention.md#PallasMLAttentionBackend.get_kv_cache_page_size_bytes)  (+46 more)
- used by: [`get_kv_cache_spec`](tpu_runner.md#TPUModelRunner.get_kv_cache_spec), [`kv_cache_manager`](tpu_runner.md#TPUModelRunner.kv_cache_manager), [`get_kv_prewarm_shapes`](tpu_runner.md#TPUModelRunner.get_kv_prewarm_shapes), [`initialize_kv_cache`](tpu_runner.md#TPUModelRunner.initialize_kv_cache), [`prewarm_kv_offload_shape`](tpu_runner.md#TPUModelRunner.prewarm_kv_offload_shape)

### <a id="_TpuKVCacheBackend"></a>`_TpuKVCacheBackend`  ·  implements/extends Protocol
- def: [`src/vllm_torchtpu/runner/kv_cache_manager.py:96`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L96)
- doc: Typing-only view of the KV cache methods on TPU attention backends.
- signature: `class _TpuKVCacheBackend(Protocol):`
- members:
  - <a id="_TpuKVCacheBackend.get_kv_cache_page_size_bytes"></a>`get_kv_cache_page_size_bytes(block_size: int, num_kv_heads: int, head_size: int, cache_dtype_str: str | torch.dtype = "auto")` — [`L109`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L109)
  - <a id="_TpuKVCacheBackend.get_kv_cache_shape"></a>`get_kv_cache_shape(num_blocks: int, block_size: int, num_kv_heads: int, head_size: int, cache_dtype_str: str | torch.dtype = "auto")` — [`L100`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L100)
  - <a id="_TpuKVCacheBackend.get_name"></a>`get_name()` — [`L117`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L117)
- used by: [`initialize_kv_cache`](kv_cache_manager.md#KVCacheManager.initialize_kv_cache), [`get_kv_cache_spec`](kv_cache_manager.md#KVCacheManager.get_kv_cache_spec), [`_update_mamba_page_size_padded`](kv_cache_manager.md#KVCacheManager._update_mamba_page_size_padded), [`_update_attention_page_size_padded`](kv_cache_manager.md#KVCacheManager._update_attention_page_size_padded), [`_pad_native_attention_regions`](kv_cache_manager.md#KVCacheManager._pad_native_attention_regions), [`_warn_if_kv_cache_is_padded`](kv_cache_manager.md#_warn_if_kv_cache_is_padded)

## Functions
- <a id="_warn_if_kv_cache_is_padded"></a>`_warn_if_kv_cache_is_padded(backend: type[_TpuKVCacheBackend], block_size: int, num_kv_heads: int, head_size: int, dtype: torch.dtype)` — [`L184`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L184) — Warn when a page costs more than its shape and dtype imply.
- <a id="check_kv_caches_cover_block_ids"></a>`check_kv_caches_cover_block_ids(kv_caches: dict[str, torch.Tensor], kv_cache_tensors: Iterable[KVCacheTensor], num_blocks: int, spec_for_layer: Callable[[str], KVCacheSpec])` — [`L155`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L155) — Check block coverage for dense caches in scheduler-page layout.
- <a id="is_cache_for_ds_v4"></a>`is_cache_for_ds_v4(attn_module: AttentionLayerBase)` — [`L123`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L123) — Whether this module owns one of DeepSeek-V4's custom KV caches.
- <a id="sparse_mla_page_size_bytes"></a>`sparse_mla_page_size_bytes(attn_module: MLAAttention, block_size: int, kv_cache_dtype: torch.dtype)` — [`L140`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L140) — A sparse MLA layer's page bytes from its (nope, rope) layout specs.

## Module values
- <a id="logger"></a>`logger` — [`L120`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_manager.py#L120)

