---
title: 'Module: src/vllm_torchtpu/kv_cache_materializer.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kv_cache_materializer.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kv_cache_materializer`/
symbols:
  materialize_kv_cache_tensors: materialize_kv_cache_tensors().
  resolve_block_major_pool_layout: resolve_block_major_pool_layout().
  allocate_raw_kv_cache_tensors: allocate_raw_kv_cache_tensors().
  MaterializedKVCache.bm_pool_layout: MaterializedKVCache#bm_pool_layout.
  format_kv_cache_layout_summary: format_kv_cache_layout_summary().
  MaterializedKVCache.kv_caches: MaterializedKVCache#kv_caches.
  build_kernel_block_size_by_group_id: build_kernel_block_size_by_group_id().
  MaterializedKVCache.raw_tensors: MaterializedKVCache#raw_tensors.
  _tensor_layout_summary: _tensor_layout_summary().
  _raw_tensor_index: _raw_tensor_index().
  MaterializedKVCache: MaterializedKVCache#
  can_share_attention_cache: can_share_attention_cache().
  MaterializedKVCache.layer_to_raw: MaterializedKVCache#layer_to_raw.
  _storage_ptr: _storage_ptr().
  layer_to_pool_index: layer_to_pool_index().
  materialize_shared_attention_cache: materialize_shared_attention_cache().
  _FP8_DTYPES: _FP8_DTYPES.
  _pool_attention_geometry: _pool_attention_geometry().
  make_attention_cache_tensor: make_attention_cache_tensor().
  _can_allocate_attention_cache_directly: _can_allocate_attention_cache_directly().
  _select_representative_kv_cache_spec: _select_representative_kv_cache_spec().
---
# Module: [`src/vllm_torchtpu/kv_cache_materializer.py`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py)

## Classes
### <a id="MaterializedKVCache"></a>`MaterializedKVCache`
- def: [`src/vllm_torchtpu/kv_cache_materializer.py:39`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L39) — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- signature: `class MaterializedKVCache:`
- members:
  - <a id="MaterializedKVCache.bm_pool_layout"></a>`bm_pool_layout` — [`L48`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L48) — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
  - <a id="MaterializedKVCache.kv_caches"></a>`kv_caches` — [`L40`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L40)
  - <a id="MaterializedKVCache.layer_to_raw"></a>`layer_to_raw` — [`L44`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L44)
  - <a id="MaterializedKVCache.raw_tensors"></a>`raw_tensors` — [`L41`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L41)
- uses (calls/refs, reference-scoped): [`BlockMajorPoolLayout`](block_major_pool.md#BlockMajorPoolLayout)
- used by: [`_initialize_unified_kv_cache`](runner/kv_cache_manager.md#KVCacheManager._initialize_unified_kv_cache), [`materialize_kv_cache_tensors`](kv_cache_materializer.md#materialize_kv_cache_tensors)

## Functions
- <a id="_can_allocate_attention_cache_directly"></a>`_can_allocate_attention_cache_directly(kv_cache_config: KVCacheConfig)` — [`L407`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L407)
- <a id="_pool_attention_geometry"></a>`_pool_attention_geometry(kv_cache_config: KVCacheConfig, attn_groups: Sequence[Sequence[AttentionGroup]], kernel_block_size_by_gid: dict[int, int])` — [`L138`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L138) — (attention spec, backend, kernel block size) of the unified pool,
- <a id="_raw_tensor_index"></a>`_raw_tensor_index(tensor: torch.Tensor, raw_tensors: Sequence[torch.Tensor])` — [`L55`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L55)
- <a id="_select_representative_kv_cache_spec"></a>`_select_representative_kv_cache_spec(kv_cache_spec: KVCacheSpec)` — [`L416`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L416)
- <a id="_storage_ptr"></a>`_storage_ptr(tensor: torch.Tensor)` — [`L51`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L51)
- <a id="_tensor_layout_summary"></a>`_tensor_layout_summary(tensor: torch.Tensor, raw_tensors: Sequence[torch.Tensor])` — [`L66`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L66)
- <a id="allocate_raw_kv_cache_tensors"></a>`allocate_raw_kv_cache_tensors(kv_cache_config: KVCacheConfig, device: torch.device, pool_geometry: tuple[AttentionSpec, Any, int], cache_dtype: str | torch.dtype = "auto", block_major: bool = False)` — [`L237`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L237) — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- <a id="build_kernel_block_size_by_group_id"></a>`build_kernel_block_size_by_group_id(*, kv_cache_config: KVCacheConfig, kernel_block_sizes: Sequence[int])` — [`L427`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L427) — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- <a id="can_share_attention_cache"></a>`can_share_attention_cache(specs: Sequence[KVCacheSpec], attn_backend: Any)` — [`L330`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L330)
- <a id="format_kv_cache_layout_summary"></a>`format_kv_cache_layout_summary(*, kv_cache_config: KVCacheConfig, kv_caches: dict[str, LayerKVCache], raw_tensors: Sequence[torch.Tensor], attn_groups: Sequence[Sequence[AttentionGroup]] | None = None)` — [`L81`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L81) — Format stable KV/mamba cache layout diagnostics for TPU validation.
- <a id="layer_to_pool_index"></a>`layer_to_pool_index(kv_cache_config: KVCacheConfig)` — [`L164`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L164) — Maps native vLLM layer placements to disjoint TPU pool region indices.
- <a id="make_attention_cache_tensor"></a>`make_attention_cache_tensor(*, spec: AttentionSpec, attn_backend: Any, num_blocks: int, kernel_block_size: int, cache_dtype: str | torch.dtype, device: torch.device)` — [`L309`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L309)
- <a id="materialize_kv_cache_tensors"></a>`materialize_kv_cache_tensors(*, kv_cache_config: KVCacheConfig, attn_groups: Sequence[Sequence[AttentionGroup]], kernel_block_sizes: Sequence[int], device: torch.device, cache_dtype: str | torch.dtype, block_major: bool = False)` — [`L463`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L463) — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- <a id="materialize_shared_attention_cache"></a>`materialize_shared_attention_cache(*, layer_specs: Sequence[tuple[str, AttentionSpec]], tensor_size: int, num_blocks: int, attn_backend: Any, device: torch.device)` — [`L356`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L356) — Allocate one tensor for attention groups sharing scheduler pages. — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- <a id="resolve_block_major_pool_layout"></a>`resolve_block_major_pool_layout(kv_cache_config: KVCacheConfig, kernel_block_size: int)` — [`L208`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L208) — Derives the merged block-major pool geometry from `KVCacheConfig` alone. — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)

## Module values
- <a id="_FP8_DTYPES"></a>`_FP8_DTYPES` — [`L33`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_materializer.py#L33)

