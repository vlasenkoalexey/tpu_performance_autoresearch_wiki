---
title: 'Module: src/vllm_torchtpu/offload/block_major_layout.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/offload/block_major_layout.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.offload.block_major_layout`/
symbols:
  resolve_block_major_contract: resolve_block_major_contract().
  _resolve_unified_pool_contract: _resolve_unified_pool_contract().
  BlockMajorContract: BlockMajorContract#
  BlockMajorContract.fragment_count: BlockMajorContract#fragment_count.
  BlockMajorContract.fragment_row_bytes: BlockMajorContract#fragment_row_bytes.
  BlockMajorContract.bundle_row_bytes: BlockMajorContract#bundle_row_bytes.
  BlockMajorContract.logical_fingerprint: BlockMajorContract#logical_fingerprint.
  logger: logger.
  block_major_layer_indices: block_major_layer_indices().
  BLOCK_MAJOR_LAYOUT_VERSION: BLOCK_MAJOR_LAYOUT_VERSION.
  _canonical_layout_fingerprint: _canonical_layout_fingerprint().
---
# Module: [`src/vllm_torchtpu/offload/block_major_layout.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/block_major_layout.py)

## Classes
### <a id="BlockMajorContract"></a>`BlockMajorContract`
- def: [`src/vllm_torchtpu/offload/block_major_layout.py:66`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/block_major_layout.py#L66)
- doc: Immutable specification of the bundled KV layout agreed upon across ranks.
- signature: `class BlockMajorContract:`
- members:
  - <a id="BlockMajorContract.bundle_row_bytes"></a>`bundle_row_bytes` — [`L81`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/block_major_layout.py#L81)
  - <a id="BlockMajorContract.fragment_count"></a>`fragment_count` — [`L79`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/block_major_layout.py#L79)
  - <a id="BlockMajorContract.fragment_row_bytes"></a>`fragment_row_bytes` — [`L80`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/block_major_layout.py#L80)
  - <a id="BlockMajorContract.logical_fingerprint"></a>`logical_fingerprint` — [`L82`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/block_major_layout.py#L82)
- used by: [`resolve_block_major_contract`](block_major_layout.md#resolve_block_major_contract), [`_resolve_unified_pool_contract`](block_major_layout.md#_resolve_unified_pool_contract), [`_backend_configs`](raiden_store.md#RaidenStoreOffloadingWorker._backend_configs), [`derive_offload_namespace`](raiden_store.md#derive_offload_namespace), [`__init__`](raiden_store.md#RaidenStoreOffloadingWorker.__init__)

## Functions
- <a id="_canonical_layout_fingerprint"></a>`_canonical_layout_fingerprint(value: Mapping[str, Any])` — [`L85`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/block_major_layout.py#L85) — Computes a deterministic SHA-256 fingerprint from a canonical
- <a id="_resolve_unified_pool_contract"></a>`_resolve_unified_pool_contract(vllm_config: VllmConfig, kv_cache_config: KVCacheConfig)` — [`L238`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/block_major_layout.py#L238) — Describes the merged unified pool as one block-major offload contract. — documented in [host-offload](../../../../concepts/host-offload.md)
- <a id="block_major_layer_indices"></a>`block_major_layer_indices(kv_cache_config: KVCacheConfig, fragment_row_bytes: int)` — [`L94`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/block_major_layout.py#L94) — Read layer positions from vLLM's native block-outermost placement. — documented in [host-offload](../../../../concepts/host-offload.md)
- <a id="resolve_block_major_contract"></a>`resolve_block_major_contract(vllm_config: VllmConfig, kv_cache_config: KVCacheConfig)` — [`L130`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/block_major_layout.py#L130) — Derives the block-major layout contract from engine and KV cache configurations. — documented in [host-offload](../../../../concepts/host-offload.md)

## Module values
- <a id="BLOCK_MAJOR_LAYOUT_VERSION"></a>`BLOCK_MAJOR_LAYOUT_VERSION` — [`L62`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/block_major_layout.py#L62)
- <a id="logger"></a>`logger` — [`L57`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/block_major_layout.py#L57)

