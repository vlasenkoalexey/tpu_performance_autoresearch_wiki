---
title: 'Module: src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.custom_ops.deepseek_v4.deepseek_v4_indexer`/
symbols:
  VllmDeepseekV4Indexer._build_indexer_op: VllmDeepseekV4Indexer#_build_indexer_op().
  _indexer_jax._indexer_local: _indexer_jax()._indexer_local().
  static_verify_q_len: static_verify_q_len().
  VllmDeepseekV4IndexerCache.get_kv_cache_spec: VllmDeepseekV4IndexerCache#get_kv_cache_spec().
  VllmDeepseekV4Indexer.forward: VllmDeepseekV4Indexer#forward().
  VllmDeepseekV4Indexer.__init__: VllmDeepseekV4Indexer#__init__().
  _indexer_jax: _indexer_jax().
  _indexer_op_cache: _indexer_op_cache.
  logger: logger.
  VllmDeepseekV4Indexer: VllmDeepseekV4Indexer#
  STATIC_VERIFY_MODEL_TYPES: STATIC_VERIFY_MODEL_TYPES.
  BATCH_AXIS: BATCH_AXIS.
  VllmDeepseekV4IndexerCache: VllmDeepseekV4IndexerCache#
  VllmDeepseekV4Indexer._fake_indexer: VllmDeepseekV4Indexer#_fake_indexer().
---
# Module: [`src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py)

## Classes
### <a id="VllmDeepseekV4Indexer"></a>`VllmDeepseekV4Indexer`
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py:199`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py#L199)
- doc: TPU indexer: ranks compressed KV rows via the streamindex top-k kernel.
- signature: `class VllmDeepseekV4Indexer(DeepseekV4Indexer):`
- members:
  - <a id="VllmDeepseekV4Indexer.forward"></a>`forward(self, hidden_states: torch.Tensor, query: torch.Tensor, indexer_weights: torch.Tensor, positions: torch.Tensor, rotary_emb: nn.Module, slot_mapping: torch.Tensor | None = None)` — [`L274`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py#L274)
- protocol/private: <a id="VllmDeepseekV4Indexer.__init__"></a>`__init__`[`L202`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py#L202), <a id="VllmDeepseekV4Indexer._build_indexer_op"></a>`_build_indexer_op`[`L215`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py#L215), <a id="VllmDeepseekV4Indexer._fake_indexer"></a>`_fake_indexer`[`L264`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py#L264)
- uses (calls/refs, reference-scoped): [`get_pallas_op_mesh`](../../../../models/vllm/vllm_model_wrapper_context.md#get_pallas_op_mesh), [`request_distribution`](../../../core/attention_metadata.md#AttentionMetadata.request_distribution), [`query_start_loc`](../../../core/attention_metadata.md#AttentionMetadata.query_start_loc), [`seq_lens`](../../../core/attention_metadata.md#AttentionMetadata.seq_lens), [`block_tables`](../../../core/attention_metadata.md#AttentionMetadata.block_tables), [`static_verify_q_len`](deepseek_v4_indexer.md#static_verify_q_len), [`VllmDeepseekCompressor`](deepseek_v4_compressor.md#VllmDeepseekCompressor), [`_indexer_jax`](deepseek_v4_indexer.md#_indexer_jax), [`_indexer_op_cache`](deepseek_v4_indexer.md#_indexer_op_cache), [`VllmDeepseekV4IndexerCache`](deepseek_v4_indexer.md#VllmDeepseekV4IndexerCache), [`BATCH_AXIS`](deepseek_v4_indexer.md#BATCH_AXIS)
- used by: [`__init__`](../../../../models/vllm/deepseek_v4/attention.md#VllmDeepseekV4MLAAttention.__init__)

### <a id="VllmDeepseekV4IndexerCache"></a>`VllmDeepseekV4IndexerCache`
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py:178`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py#L178)
- doc: Indexer K cache as a packed uint8 record on TPU.
- signature: `class VllmDeepseekV4IndexerCache(DeepseekV4IndexerCache):`
- members:
  - <a id="VllmDeepseekV4IndexerCache.get_kv_cache_spec"></a>`get_kv_cache_spec(self, vllm_config: VllmConfig)` — [`L181`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py#L181) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- uses (calls/refs, reference-scoped): [`get_kv_cache_shape`](../../../../kernels/deepseek_v4/streamindex_topk/streamindex_topk.md#get_kv_cache_shape), [`KVLayout`](../../../../kernels/deepseek_v4/streamindex_topk/config.md#KVLayout), [`SEQ_ALONG_LANE`](../../../../kernels/deepseek_v4/streamindex_topk/config.md#KVLayout.SEQ_ALONG_LANE), [`SAL_PAGE_SIZE`](../../../../kernels/deepseek_v4/compress_and_store/config.md#SAL_PAGE_SIZE)
- used by: [`__init__`](deepseek_v4_indexer.md#VllmDeepseekV4Indexer.__init__)

## Functions
- <a id="_indexer_jax"></a>`_indexer_jax(q: jax.Array, positions: jax.Array, cos_sin_cache: jax.Array, indexer_weights: jax.Array, cache_kv: jax.Array, seq_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, *, k: int, compression_ratio: int, softmax_scale: float, n_head: int, verify_q_len: int | None = None)` — [`L96`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py#L96)
- <a id="_indexer_jax._indexer_local"></a>`_indexer_local(q, positions, cos_sin_cache, indexer_weights, cache_kv, seq_lens, page_indices, cu_q_lens, distribution)` — [`L124`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py#L124) — documented in [custom-ops](../../../../../../../concepts/custom-ops.md)
- <a id="static_verify_q_len"></a>`static_verify_q_len(vllm_config: VllmConfig | Any | None)` — [`L60`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py#L60) — Query length of a full speculative verify window, 1 + K, or None. — documented in [custom-ops](../../../../../../../concepts/custom-ops.md)

## Module values
- <a id="BATCH_AXIS"></a>`BATCH_AXIS` — [`L92`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py#L92)
- <a id="STATIC_VERIFY_MODEL_TYPES"></a>`STATIC_VERIFY_MODEL_TYPES` — [`L57`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py#L57)
- <a id="_indexer_op_cache"></a>`_indexer_op_cache` — [`L53`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py#L53)
- <a id="logger"></a>`logger` — [`L51`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.py#L51)

