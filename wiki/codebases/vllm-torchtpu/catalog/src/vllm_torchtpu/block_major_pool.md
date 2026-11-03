---
title: 'Module: src/vllm_torchtpu/block_major_pool.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/block_major_pool.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.block_major_pool`/
symbols:
  BlockMajorPoolLayout: BlockMajorPoolLayout#
  unified_block_major_enabled: unified_block_major_enabled().
  BlockMajorPoolLayout.num_pools: BlockMajorPoolLayout#num_pools.
  BlockMajorPoolLayout.split: BlockMajorPoolLayout#split.
  BlockMajorPoolLayout.rows_per_block: BlockMajorPoolLayout#rows_per_block().
  kernel_view: kernel_view().
  BlockMajorPoolLayout.pool_index_by_layer: BlockMajorPoolLayout#pool_index_by_layer.
  BlockMajorPoolLayout.num_blocks: BlockMajorPoolLayout#num_blocks.
  flat_manager_ids: flat_manager_ids().
  flat_kernel_ids: flat_kernel_ids().
---
# Module: [`src/vllm_torchtpu/block_major_pool.py`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/block_major_pool.py)

## Classes
### <a id="BlockMajorPoolLayout"></a>`BlockMajorPoolLayout`
- def: [`src/vllm_torchtpu/block_major_pool.py:61`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/block_major_pool.py#L61) — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- doc: Geometry of the merged block-major unified pool.
- signature: `class BlockMajorPoolLayout:`
- members:
  - <a id="BlockMajorPoolLayout.rows_per_block"></a>`rows_per_block(self)` — [`L77`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/block_major_pool.py#L77) — Total kernel blocks per scheduler block row (`shape[1]`).
  - <a id="BlockMajorPoolLayout.num_blocks"></a>`num_blocks` — [`L71`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/block_major_pool.py#L71)
  - <a id="BlockMajorPoolLayout.num_pools"></a>`num_pools` — [`L72`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/block_major_pool.py#L72) — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
  - <a id="BlockMajorPoolLayout.pool_index_by_layer"></a>`pool_index_by_layer` — [`L74`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/block_major_pool.py#L74)
  - <a id="BlockMajorPoolLayout.split"></a>`split` — [`L73`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/block_major_pool.py#L73)
- used by: [`build_qwen35_pool_manifest`](distributed/kv_transfer/raiden/pool_manifest.md#build_qwen35_pool_manifest), [`_initialize_unified_kv_cache`](runner/kv_cache_manager.md#KVCacheManager._initialize_unified_kv_cache), [`forward`](layers/adapter/attention.md#PallasAttentionBackendImpl.forward), [`_resolve_unified_pool_contract`](offload/block_major_layout.md#_resolve_unified_pool_contract), [`_region_placement`](distributed/kv_transfer/raiden/pool_manifest.md#_region_placement), [`_bm_kernel`](layers/adapter/attention.md#PallasAttentionBackendImpl._bm_kernel), [`resolve_block_major_pool_layout`](kv_cache_materializer.md#resolve_block_major_pool_layout), [`resolve_kernel_geometry`](offload/raiden_store.md#resolve_kernel_geometry), [`_bind_block_major_pool_layers`](runner/kv_cache_manager.md#KVCacheManager._bind_block_major_pool_layers), [`_copy_mamba_state_blocks`](runner/tpu_runner.md#TPUModelRunner._copy_mamba_state_blocks), [`allocate_raw_kv_cache_tensors`](kv_cache_materializer.md#allocate_raw_kv_cache_tensors), [`_bm_state_ids`](layers/adapter/custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention._bm_state_ids), [`bm_pool_layout`](kv_cache_materializer.md#MaterializedKVCache.bm_pool_layout), [`bm_pool_layout`](runner/tpu_runner.md#TPUModelRunner.bm_pool_layout), [`set_block_major_pool`](layers/adapter/custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention.set_block_major_pool), [`_build_mamba_copy_plan`](runner/tpu_runner.md#TPUModelRunner._build_mamba_copy_plan), [`set_block_major_pool`](layers/adapter/attention.md#PallasAttentionBackendImpl.set_block_major_pool), [`_bm_region`](layers/adapter/custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention._bm_region)

## Functions
- <a id="flat_kernel_ids"></a>`flat_kernel_ids(ids: torch.Tensor, pool_index: int, num_pools: int, split: int)` — [`L102`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/block_major_pool.py#L102) — Maps region-local kernel block IDs to flat `kernel_view(pool)` block IDs.
- <a id="flat_manager_ids"></a>`flat_manager_ids(ids: torch.Tensor, pool_index: int, num_pools: int)` — [`L93`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/block_major_pool.py#L93) — Maps region-local manager block IDs to flat row indices in the merged pool.
- <a id="kernel_view"></a>`kernel_view(pool)` — [`L82`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/block_major_pool.py#L82) — Folds the merged pool's leading `(num_blocks, rows_per_block)` axes into dim 0.
- <a id="unified_block_major_enabled"></a>`unified_block_major_enabled(vllm_config: VllmConfig)` — [`L45`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/block_major_pool.py#L45) — Returns whether unified hybrid pools are merged into one block-major pool. — documented in [host-offload](../../../concepts/host-offload.md)

