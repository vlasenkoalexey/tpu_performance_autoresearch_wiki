---
title: 'Module: src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.custom_ops.mla_attention_op`/
symbols:
  VllmTPUMultiHeadLatentAttentionWrapper.forward: VllmTPUMultiHeadLatentAttentionWrapper#forward().
  VllmTPUSparseAttnIndexer._build_streamidx_dcp_op: VllmTPUSparseAttnIndexer#_build_streamidx_dcp_op().
  VllmTPUMLAAttention.W_UK_T_dcp_qrep_scale: VllmTPUMLAAttention#W_UK_T_dcp_qrep_scale.
  VllmTPUMultiHeadLatentAttentionWrapper.mla_attn: VllmTPUMultiHeadLatentAttentionWrapper#mla_attn.
  _resolve_indexer_kv_cache_mode: _resolve_indexer_kv_cache_mode().
  VllmTPUSparseAttnIndexer.forward_oot: VllmTPUSparseAttnIndexer#forward_oot().
  VllmTPUSparseAttnIndexer._build_streamidx_op: VllmTPUSparseAttnIndexer#_build_streamidx_op().
  VllmTPUSparseAttnIndexer._streamidx_topk_dcp_jax: VllmTPUSparseAttnIndexer#_streamidx_topk_dcp_jax().
  VllmTPUMLAAttention.process_weights_after_loading: VllmTPUMLAAttention#process_weights_after_loading().
  VllmTPUSparseAttnIndexer._streamidx_topk_jax: VllmTPUSparseAttnIndexer#_streamidx_topk_jax().
  _log_indexer_kv_cache_once: _log_indexer_kv_cache_once().
  VllmTPUMultiHeadLatentAttentionWrapper.gate_is_fused: VllmTPUMultiHeadLatentAttentionWrapper#gate_is_fused.
  _cp_scatter_indexer_k: _cp_scatter_indexer_k().
  _cp_scatter_indexer_k._local: _cp_scatter_indexer_k()._local().
  _streamidx_block_sizes: _streamidx_block_sizes().
  VllmTPUMultiHeadLatentAttentionWrapper._q_proj_layer: VllmTPUMultiHeadLatentAttentionWrapper#_q_proj_layer().
  VllmTPUMLAAttention.W_UV_scale: VllmTPUMLAAttention#W_UV_scale.
  VllmTPUMLAAttention.sparse_mla_dcp_op: VllmTPUMLAAttention#sparse_mla_dcp_op.
  VllmTPUMultiHeadLatentAttentionWrapper.kimi_preprocess: VllmTPUMultiHeadLatentAttentionWrapper#kimi_preprocess.
  VllmTPUMultiHeadLatentAttentionWrapper.topk_indices_buffer: VllmTPUMultiHeadLatentAttentionWrapper#topk_indices_buffer.
  _warn_indexer_kv_cache_fallback_once: _warn_indexer_kv_cache_fallback_once().
  _unsupported_indexer_kv_cache_reason: _unsupported_indexer_kv_cache_reason().
  VllmTPUSparseAttnIndexer._write_topk_rows: VllmTPUSparseAttnIndexer#_write_topk_rows().
  VllmTPUIndexer.rebind: VllmTPUIndexer#rebind().
  VllmTPUMLAAttention.kv_cache_quantized_dtype: VllmTPUMLAAttention#kv_cache_quantized_dtype.
  VllmTPUMLAAttention.W_UK_T: VllmTPUMLAAttention#W_UK_T.
  VllmTPUMultiHeadLatentAttentionWrapper.q_lora_rank: VllmTPUMultiHeadLatentAttentionWrapper#q_lora_rank.
  VllmTPUMultiHeadLatentAttentionWrapper.rotary_emb: VllmTPUMultiHeadLatentAttentionWrapper#rotary_emb.
  VllmTPUMultiHeadLatentAttentionWrapper.indexer: VllmTPUMultiHeadLatentAttentionWrapper#indexer.
  VllmTPUSparseAttnIndexer.dcp_size: VllmTPUSparseAttnIndexer#dcp_size.
  VllmTPUMLAAttention.forward: VllmTPUMLAAttention#forward().
  VllmTPUMultiHeadLatentAttentionWrapper.qk_rope_head_dim: VllmTPUMultiHeadLatentAttentionWrapper#qk_rope_head_dim.
  VllmTPUMultiHeadLatentAttentionWrapper.fused_qkv_a_proj: VllmTPUMultiHeadLatentAttentionWrapper#fused_qkv_a_proj.
  VllmTPUMultiHeadLatentAttentionWrapper.q_b_proj: VllmTPUMultiHeadLatentAttentionWrapper#q_b_proj.
  VllmTPUMultiHeadLatentAttentionWrapper.topk_tokens: VllmTPUMultiHeadLatentAttentionWrapper#topk_tokens.
  logger: logger.
  _TOPK_ROWS_UPDATE_OP: _TOPK_ROWS_UPDATE_OP.
  VllmTPUMLAAttention.W_UK_T_scale: VllmTPUMLAAttention#W_UK_T_scale.
  VllmTPUMLAAttention.W_UV: VllmTPUMLAAttention#W_UV.
  VllmTPUMultiHeadLatentAttentionWrapper.kv_lora_rank: VllmTPUMultiHeadLatentAttentionWrapper#kv_lora_rank.
  VllmTPUMultiHeadLatentAttentionWrapper.num_heads: VllmTPUMultiHeadLatentAttentionWrapper#num_heads.
  VllmTPUMultiHeadLatentAttentionWrapper.q_a_layernorm: VllmTPUMultiHeadLatentAttentionWrapper#q_a_layernorm.
  VllmTPUMultiHeadLatentAttentionWrapper.is_sparse: VllmTPUMultiHeadLatentAttentionWrapper#is_sparse.
  VllmTPUSparseAttnIndexer.topk_op: VllmTPUSparseAttnIndexer#topk_op.
  VllmTPUMLAAttention.mla_op: VllmTPUMLAAttention#mla_op.
  VllmTPUMultiHeadLatentAttentionWrapper.dcp_group_size: VllmTPUMultiHeadLatentAttentionWrapper#dcp_group_size.
  VllmTPUSparseAttnIndexer.topk_op_dcp: VllmTPUSparseAttnIndexer#topk_op_dcp.
  VllmTPUSparseAttnIndexer.op: VllmTPUSparseAttnIndexer#op().
  VllmTPUMLAAttention: VllmTPUMLAAttention#
  VllmTPUMultiHeadLatentAttentionWrapper.v_head_dim: VllmTPUMultiHeadLatentAttentionWrapper#v_head_dim.
  VllmTPUMultiHeadLatentAttentionWrapper.q_proj: VllmTPUMultiHeadLatentAttentionWrapper#q_proj.
  VllmTPUMultiHeadLatentAttentionWrapper.g_proj: VllmTPUMultiHeadLatentAttentionWrapper#g_proj.
  VllmTPUMultiHeadLatentAttentionWrapper.dcp_q_replicate: VllmTPUMultiHeadLatentAttentionWrapper#dcp_q_replicate.
  VllmTPUSparseAttnIndexer._streamidx_op: VllmTPUSparseAttnIndexer#_streamidx_op.
  VllmTPUIndexerCache.get_attn_backend: VllmTPUIndexerCache#get_attn_backend().
  VllmTPUIndexer.forward: VllmTPUIndexer#forward().
  VllmTPUMLAAttention.__init__: VllmTPUMLAAttention#__init__().
  VllmTPUMLAAttention.sparse_mla_op: VllmTPUMLAAttention#sparse_mla_op.
  VllmMLAAttention: VllmMLAAttention.
  VllmTPUMultiHeadLatentAttentionWrapper.process_weights_after_loading: VllmTPUMultiHeadLatentAttentionWrapper#process_weights_after_loading().
  VllmMultiHeadLatentAttentionWrapper: VllmMultiHeadLatentAttentionWrapper.
  STREAMIDX_KV_PAGES_PER_BLOCK: STREAMIDX_KV_PAGES_PER_BLOCK.
  STREAMIDX_QUERIES_PER_BLOCK: STREAMIDX_QUERIES_PER_BLOCK.
  VllmTPUIndexer: VllmTPUIndexer#
  TPUDummyMLAPrefillBackend: TPUDummyMLAPrefillBackend#
  VllmTPUMLAAttention.W_UK_T_dcp_qrep: VllmTPUMLAAttention#W_UK_T_dcp_qrep.
  VllmTPUMultiHeadLatentAttentionWrapper.qk_nope_head_dim: VllmTPUMultiHeadLatentAttentionWrapper#qk_nope_head_dim.
  VllmTPUMultiHeadLatentAttentionWrapper.kv_a_proj_with_mqa: VllmTPUMultiHeadLatentAttentionWrapper#kv_a_proj_with_mqa.
  VllmTPUMultiHeadLatentAttentionWrapper.kv_a_layernorm: VllmTPUMultiHeadLatentAttentionWrapper#kv_a_layernorm.
  VllmTPUMultiHeadLatentAttentionWrapper.o_proj: VllmTPUMultiHeadLatentAttentionWrapper#o_proj.
  VllmTPUMultiHeadLatentAttentionWrapper.skip_topk: VllmTPUMultiHeadLatentAttentionWrapper#skip_topk.
  _INDEXER_KV_CACHE_FALLBACK_LOGGED._INDEXER_KV_CACHE_FALLBACK_LOGGED: _INDEXER_KV_CACHE_FALLBACK_LOGGED._INDEXER_KV_CACHE_FALLBACK_LOGGED.
  _INDEXER_KV_CACHE_INFO_LOGGED._INDEXER_KV_CACHE_INFO_LOGGED: _INDEXER_KV_CACHE_INFO_LOGGED._INDEXER_KV_CACHE_INFO_LOGGED.
  STREAMIDX_ENABLE_EARLY_EXIT: STREAMIDX_ENABLE_EARLY_EXIT.
  STREAMIDX_SMALL_BUCKET_DEFAULT_BKVP: STREAMIDX_SMALL_BUCKET_DEFAULT_BKVP.
  _dcp_indexer_a2a_for_bucket: _dcp_indexer_a2a_for_bucket().
  _topk_rows_update_jax: _topk_rows_update_jax().
  _fake_topk_rows_update: _fake_topk_rows_update().
  _topk_rows: _topk_rows().
  VllmTPUSparseAttnIndexer._fake: VllmTPUSparseAttnIndexer#_fake().
  VllmTPUSparseAttnIndexer._fake_streamidx_topk_dcp: VllmTPUSparseAttnIndexer#_fake_streamidx_topk_dcp().
  VllmTPUIndexerCache: VllmTPUIndexerCache#
  VllmTPUMLAAttention.dcp_q_replicate: VllmTPUMLAAttention#dcp_q_replicate.
  VllmTPUMLAAttention.prefix: VllmTPUMLAAttention#prefix.
  VllmTPUMultiHeadLatentAttentionWrapper: VllmTPUMultiHeadLatentAttentionWrapper#
  VllmTPUMultiHeadLatentAttentionWrapper.qk_head_dim: VllmTPUMultiHeadLatentAttentionWrapper#qk_head_dim.
  VllmTPUMultiHeadLatentAttentionWrapper.kv_b_proj: VllmTPUMultiHeadLatentAttentionWrapper#kv_b_proj.
  VllmTPUMultiHeadLatentAttentionWrapper.indexer_rope_emb: VllmTPUMultiHeadLatentAttentionWrapper#indexer_rope_emb.
  VllmTPUSparseAttnIndexer: VllmTPUSparseAttnIndexer#
  VllmTPUSparseAttnIndexer.__init__: VllmTPUSparseAttnIndexer#__init__().
  TPUDummyMLAPrefillBackend.__init__: TPUDummyMLAPrefillBackend#__init__().
  TPUDummyMLAPrefillBackend.forward: TPUDummyMLAPrefillBackend#forward().
  VllmTPUMLAAttention.topk_indices_buffer: VllmTPUMLAAttention#topk_indices_buffer.
  VllmTPUMLAAttention.kv_sharing_target_layer_name: VllmTPUMLAAttention#kv_sharing_target_layer_name.
  VllmTPUMLAAttention.attn_type: VllmTPUMLAAttention#attn_type.
  VllmTPUMLAAttention.sliding_window: VllmTPUMLAAttention#sliding_window.
  VllmTPUMultiHeadLatentAttentionWrapper.__init__: VllmTPUMultiHeadLatentAttentionWrapper#__init__().
  VllmTPUMultiHeadLatentAttentionWrapper.hidden_size: VllmTPUMultiHeadLatentAttentionWrapper#hidden_size.
  VllmTPUMultiHeadLatentAttentionWrapper.prefix: VllmTPUMultiHeadLatentAttentionWrapper#prefix.
  VllmDeepseekScalingRotaryEmbedding: VllmDeepseekScalingRotaryEmbedding#
  VllmDeepseekScalingRotaryEmbedding.forward_native: VllmDeepseekScalingRotaryEmbedding#forward_native().
---
# Module: [`src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py)

## Classes
### <a id="TPUDummyMLAPrefillBackend"></a>`TPUDummyMLAPrefillBackend`
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py:873`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L873)
- signature: `class TPUDummyMLAPrefillBackend:`
- members:
  - <a id="TPUDummyMLAPrefillBackend.forward"></a>`forward(self, *args, **kwargs)` — [`L877`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L877)
- protocol/private: <a id="TPUDummyMLAPrefillBackend.__init__"></a>`__init__`[`L874`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L874)
- used by: [`__init__`](mla_attention_op.md#VllmTPUMLAAttention.__init__)

### <a id="VllmDeepseekScalingRotaryEmbedding"></a>`VllmDeepseekScalingRotaryEmbedding`
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py:1354`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1354)
- doc: TPU-compatible DeepSeek Scaling RoPE implementation.
- signature: `class VllmDeepseekScalingRotaryEmbedding(DeepseekScalingRotaryEmbedding):`
- members:
  - <a id="VllmDeepseekScalingRotaryEmbedding.forward_native"></a>`forward_native(self, positions: torch.Tensor, query: torch.Tensor, key: torch.Tensor | None = None, offsets: torch.Tensor | None = None)` — [`L1357`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1357)

### <a id="VllmTPUIndexer"></a>`VllmTPUIndexer`
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py:793`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L793)
- doc: TPU-optimized out-of-tree wrapper for Indexer.
- signature: `class VllmTPUIndexer(Indexer):`
- members:
  - <a id="VllmTPUIndexer.forward"></a>`forward(self, hidden_states: torch.Tensor, qr: torch.Tensor, positions, rotary_emb)` — [`L824`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L824)
  - <a id="VllmTPUIndexer.rebind"></a>`rebind(cls, indexer: Indexer)` — [`L804`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L804) — Retype an in-tree `Indexer`, and its K cache, onto the TPU path.
- uses (calls/refs, reference-scoped): [`quantize_tensor`](../../core/quantization.md#quantize_tensor), [`VllmTPUIndexerCache`](mla_attention_op.md#VllmTPUIndexerCache)
- used by: [`kimi_preprocess`](mla_attention_op.md#VllmTPUMultiHeadLatentAttentionWrapper.kimi_preprocess)

### <a id="VllmTPUIndexerCache"></a>`VllmTPUIndexerCache`
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py:786`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L786)
- doc: Indexer K cache retyped onto the TPU backend. See `VllmTPUIndexer`.
- signature: `class VllmTPUIndexerCache(DeepseekV32IndexerCache):`
- members:
  - <a id="VllmTPUIndexerCache.get_attn_backend"></a>`get_attn_backend(self)` — [`L789`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L789)
- uses (calls/refs, reference-scoped): [`VllmTPUDeepseekV32IndexerBackend`](../attention.md#VllmTPUDeepseekV32IndexerBackend)
- used by: [`rebind`](mla_attention_op.md#VllmTPUIndexer.rebind)

### <a id="VllmTPUMLAAttention"></a>`VllmTPUMLAAttention`
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py:881`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L881)
- doc: TPU-optimized out-of-tree wrapper for Multi-Head Latent Attention.
- signature: `class VllmTPUMLAAttention(MLAAttention):`
- members:
  - <a id="VllmTPUMLAAttention.forward"></a>`forward(self, q: tuple[torch.Tensor, torch.Tensor], kv_c_normed: torch.Tensor, k_pe: torch.Tensor, output: torch.Tensor | None = None, **kwargs)` — [`L1073`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1073)
  - <a id="VllmTPUMLAAttention.process_weights_after_loading"></a>`process_weights_after_loading(self, act_dtype: torch.dtype)` — [`L967`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L967) — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
  - <a id="VllmTPUMLAAttention.W_UK_T"></a>`W_UK_T` — [`L998`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L998)
  - <a id="VllmTPUMLAAttention.W_UK_T_dcp_qrep"></a>`W_UK_T_dcp_qrep` — [`L1022`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1022)
  - <a id="VllmTPUMLAAttention.W_UK_T_dcp_qrep_scale"></a>`W_UK_T_dcp_qrep_scale` — [`L1023`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1023) — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
  - <a id="VllmTPUMLAAttention.W_UK_T_scale"></a>`W_UK_T_scale` — [`L1000`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1000)
  - <a id="VllmTPUMLAAttention.W_UV"></a>`W_UV` — [`L999`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L999)
  - <a id="VllmTPUMLAAttention.W_UV_scale"></a>`W_UV_scale` — [`L1003`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1003)
  - <a id="VllmTPUMLAAttention.attn_type"></a>`attn_type` — [`L958`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L958)
  - <a id="VllmTPUMLAAttention.dcp_q_replicate"></a>`dcp_q_replicate` — [`L950`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L950)
  - <a id="VllmTPUMLAAttention.kv_cache_quantized_dtype"></a>`kv_cache_quantized_dtype` — [`L961`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L961)
  - <a id="VllmTPUMLAAttention.kv_sharing_target_layer_name"></a>`kv_sharing_target_layer_name` — [`L957`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L957)
  - <a id="VllmTPUMLAAttention.mla_op"></a>`mla_op` — [`L1061`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1061)
  - <a id="VllmTPUMLAAttention.prefix"></a>`prefix` — [`L956`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L956)
  - <a id="VllmTPUMLAAttention.sliding_window"></a>`sliding_window` — [`L959`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L959)
  - <a id="VllmTPUMLAAttention.sparse_mla_dcp_op"></a>`sparse_mla_dcp_op` — [`L1067`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1067)
  - <a id="VllmTPUMLAAttention.sparse_mla_op"></a>`sparse_mla_op` — [`L1064`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1064)
  - <a id="VllmTPUMLAAttention.topk_indices_buffer"></a>`topk_indices_buffer` — [`L953`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L953)
- protocol/private: <a id="VllmTPUMLAAttention.__init__"></a>`__init__`[`L884`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L884)
- uses (calls/refs, reference-scoped): [`synchronize_tensors`](../../../utils.md#synchronize_tensors), [`fresh_buffer`](../../../utils.md#fresh_buffer), [`quantize_tensor`](../../core/quantization.md#quantize_tensor), [`_build_sparse_mla_dcp_op`](../attention.md#PallasMLAttentionBackendImpl._build_sparse_mla_dcp_op), [`forward`](../attention.md#PallasMLAttentionBackendImpl.forward), [`_build_sparse_mla_op`](../attention.md#PallasMLAttentionBackendImpl._build_sparse_mla_op), [`WEIGHT_FLIPPED_ATTR`](../linear_common.md#WEIGHT_FLIPPED_ATTR), [`get_dcp_group`](../../../distributed/dcp.md#get_dcp_group), [`_build_mla_op`](../attention.md#PallasMLAttentionBackendImpl._build_mla_op), [`TPU_STR_DTYPE_TO_TORCH_DTYPE`](../attention.md#TPU_STR_DTYPE_TO_TORCH_DTYPE), [`PallasMLAttentionBackendImpl`](../attention.md#PallasMLAttentionBackendImpl), [`should_quantize_on_load`](../quantization/configs.md#should_quantize_on_load), [`_get_kv_scales`](../attention.md#PallasMLAttentionBackendImpl._get_kv_scales), [`dcp_interleave_size`](../attention.md#PallasMLAttentionBackendImpl.dcp_interleave_size), [`TPUDummyMLAPrefillBackend`](mla_attention_op.md#TPUDummyMLAPrefillBackend)
- used by: [`mla_attn`](mla_attention_op.md#VllmTPUMultiHeadLatentAttentionWrapper.mla_attn), [`precompute_and_store_context_kv`](../../../models/vllm/kimi_k3/dspark.md#K3DSparkModel.precompute_and_store_context_kv), [`VllmMLAAttention`](mla_attention_op.md#VllmMLAAttention)

### <a id="VllmTPUMultiHeadLatentAttentionWrapper"></a>`VllmTPUMultiHeadLatentAttentionWrapper`
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py:1101`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1101)
- signature: `class VllmTPUMultiHeadLatentAttentionWrapper(MultiHeadLatentAttentionWrapper):`
- members:
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper._q_proj_layer"></a>`_q_proj_layer(self)` — [`L1196`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1196) — The projection that produces `q`, whichever of the two is wired.
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.forward"></a>`forward(self, positions: torch.Tensor, hidden_states: torch.Tensor, llama_4_scaling: torch.Tensor | None = None, prefill_group=None)` — [`L1209`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1209) — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.process_weights_after_loading"></a>`process_weights_after_loading(self, act_dtype: torch.dtype)` — [`L1200`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1200)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.dcp_group_size"></a>`dcp_group_size` — [`L1171`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1171)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.dcp_q_replicate"></a>`dcp_q_replicate` — [`L1170`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1170)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.fused_qkv_a_proj"></a>`fused_qkv_a_proj` — [`L1131`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1131)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.g_proj"></a>`g_proj` — [`L1140`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1140)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.gate_is_fused"></a>`gate_is_fused` — [`L1141`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1141)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.hidden_size"></a>`hidden_size` — [`L1123`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1123)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.indexer"></a>`indexer` — [`L1157`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1157)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.indexer_rope_emb"></a>`indexer_rope_emb` — [`L1158`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1158)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.is_sparse"></a>`is_sparse` — [`L1159`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1159)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.kimi_preprocess"></a>`kimi_preprocess` — [`L1148`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1148)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.kv_a_layernorm"></a>`kv_a_layernorm` — [`L1136`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1136)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.kv_a_proj_with_mqa"></a>`kv_a_proj_with_mqa` — [`L1132`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1132)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.kv_b_proj"></a>`kv_b_proj` — [`L1137`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1137)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.kv_lora_rank"></a>`kv_lora_rank` — [`L1129`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1129)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.mla_attn"></a>`mla_attn` — [`L1175`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1175) — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.num_heads"></a>`num_heads` — [`L1130`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1130)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.o_proj"></a>`o_proj` — [`L1139`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1139)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.prefix"></a>`prefix` — [`L1194`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1194)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.q_a_layernorm"></a>`q_a_layernorm` — [`L1133`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1133)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.q_b_proj"></a>`q_b_proj` — [`L1134`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1134)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.q_lora_rank"></a>`q_lora_rank` — [`L1128`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1128)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.q_proj"></a>`q_proj` — [`L1135`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1135)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.qk_head_dim"></a>`qk_head_dim` — [`L1126`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1126)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.qk_nope_head_dim"></a>`qk_nope_head_dim` — [`L1124`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1124)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.qk_rope_head_dim"></a>`qk_rope_head_dim` — [`L1125`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1125)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.rotary_emb"></a>`rotary_emb` — [`L1138`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1138)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.skip_topk"></a>`skip_topk` — [`L1160`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1160)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.topk_indices_buffer"></a>`topk_indices_buffer` — [`L1161`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1161)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.topk_tokens"></a>`topk_tokens` — [`L1165`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1165)
  - <a id="VllmTPUMultiHeadLatentAttentionWrapper.v_head_dim"></a>`v_head_dim` — [`L1127`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1127)
- protocol/private: <a id="VllmTPUMultiHeadLatentAttentionWrapper.__init__"></a>`__init__`[`L1102`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1102)
- uses (calls/refs, reference-scoped): [`rebind`](mla_attention_op.md#VllmTPUIndexer.rebind), [`VllmTPUMLAAttention`](mla_attention_op.md#VllmTPUMLAAttention), [`VllmTPUIndexer`](mla_attention_op.md#VllmTPUIndexer)
- used by: [`VllmMultiHeadLatentAttentionWrapper`](mla_attention_op.md#VllmMultiHeadLatentAttentionWrapper)

### <a id="VllmTPUSparseAttnIndexer"></a>`VllmTPUSparseAttnIndexer`
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py:413`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L413)
- signature: `class VllmTPUSparseAttnIndexer(SparseAttnIndexer):`
- members:
  - <a id="VllmTPUSparseAttnIndexer._build_streamidx_dcp_op"></a>`_build_streamidx_dcp_op(self, dcp_size: int, interleave_size: int)` — [`L550`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L550) — The DCP twin of `_build_streamidx_op`. — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
  - <a id="VllmTPUSparseAttnIndexer._write_topk_rows"></a>`_write_topk_rows(self, num_tokens: int, topk_indices: torch.Tensor)` — [`L768`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L768) — The rows the -1 fill plus partial write would leave, in one update.
  - <a id="VllmTPUSparseAttnIndexer.forward_oot"></a>`forward_oot(self, hidden_states: torch.Tensor, q_values: torch.Tensor, k: torch.Tensor, weights: torch.Tensor)` — [`L697`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L697) — documented in [attention-and-layer-core](../../../../../../concepts/attention-and-layer-core.md)
  - <a id="VllmTPUSparseAttnIndexer.op"></a>`op(*args)` — [`L542`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L542)
  - <a id="VllmTPUSparseAttnIndexer.dcp_size"></a>`dcp_size` — [`L428`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L428)
  - <a id="VllmTPUSparseAttnIndexer.topk_op"></a>`topk_op` — [`L418`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L418)
  - <a id="VllmTPUSparseAttnIndexer.topk_op_dcp"></a>`topk_op_dcp` — [`L427`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L427)
- protocol/private: <a id="VllmTPUSparseAttnIndexer.__init__"></a>`__init__`[`L414`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L414), <a id="VllmTPUSparseAttnIndexer._build_streamidx_op"></a>`_build_streamidx_op`[`L442`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L442), <a id="VllmTPUSparseAttnIndexer._fake"></a>`_fake`[`L535`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L535), <a id="VllmTPUSparseAttnIndexer._fake_streamidx_topk_dcp"></a>`_fake_streamidx_topk_dcp`[`L662`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L662), <a id="VllmTPUSparseAttnIndexer._streamidx_op"></a>`_streamidx_op`[`L547`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L547), <a id="VllmTPUSparseAttnIndexer._streamidx_topk_dcp_jax"></a>`_streamidx_topk_dcp_jax`[`L576`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L576), <a id="VllmTPUSparseAttnIndexer._streamidx_topk_jax"></a>`_streamidx_topk_jax`[`L458`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L458)
- uses (calls/refs, reference-scoped): [`AttentionMetadata`](../../core/attention_metadata.md#AttentionMetadata), [`streamindex_topk`](../../../kernels/deepseek_v4/streamindex_topk/streamindex_topk.md#streamindex_topk), [`_resolve_indexer_kv_cache_mode`](mla_attention_op.md#_resolve_indexer_kv_cache_mode), [`quantize_tensor`](../../core/quantization.md#quantize_tensor), [`get_or_create_dcp_mesh`](../../../distributed/dcp.md#get_or_create_dcp_mesh), [`pcp_streaming_jax_op`](../../../kernels/experimental/pcp_streaming_rpa/vllm_adapter.md#pcp_streaming_jax_op), [`coalesced_kv_append`](../../../kernels/deepseek_v4/streamindex_topk/kv_cache_append.md#coalesced_kv_append), [`request_distribution`](../../core/attention_metadata.md#AttentionMetadata.request_distribution), [`streamindex_topk_dcp`](../../../kernels/deepseek_v4/streamindex_topk/streamindex_topk.md#streamindex_topk_dcp), [`query_start_loc`](../../core/attention_metadata.md#AttentionMetadata.query_start_loc), [`seq_lens`](../../core/attention_metadata.md#AttentionMetadata.seq_lens), [`DCP_AXIS_NAME`](../../../kernels/deepseek_v4/streamindex_topk/streamindex_topk.md#DCP_AXIS_NAME), [`block_tables`](../../core/attention_metadata.md#AttentionMetadata.block_tables), [`_cp_scatter_indexer_k`](mla_attention_op.md#_cp_scatter_indexer_k), [`_streamidx_block_sizes`](mla_attention_op.md#_streamidx_block_sizes), [`_TOPK_ROWS_UPDATE_OP`](mla_attention_op.md#_TOPK_ROWS_UPDATE_OP), [`VLLM_TPU_INDEXER_KV_CACHE_MODE`](../../../envs.md#VLLM_TPU_INDEXER_KV_CACHE_MODE), [`TPU_STREAMIDX_CHUNK_TOKENS`](../../../envs.md#TPU_STREAMIDX_CHUNK_TOKENS), [`is_indexer_kv_cache_mode_explicit`](../../../envs.md#is_indexer_kv_cache_mode_explicit), [`TPU_STREAMIDX_SMALL_BUCKET_BKVP`](../../../envs.md#TPU_STREAMIDX_SMALL_BUCKET_BKVP), [`TPU_STREAMIDX_SMALL_BUCKET_BQ`](../../../envs.md#TPU_STREAMIDX_SMALL_BUCKET_BQ), [`TPU_STREAMIDX_SMALL_BUCKET_TOKENS`](../../../envs.md#TPU_STREAMIDX_SMALL_BUCKET_TOKENS), [`STREAMIDX_ENABLE_EARLY_EXIT`](mla_attention_op.md#STREAMIDX_ENABLE_EARLY_EXIT), [`TPU_DCP_INDEXER_A2A_MERGE`](../../../envs.md#TPU_DCP_INDEXER_A2A_MERGE), [`TPU_DCP_INDEXER_A2A_MIN_TOKENS`](../../../envs.md#TPU_DCP_INDEXER_A2A_MIN_TOKENS), [`_dcp_indexer_a2a_for_bucket`](mla_attention_op.md#_dcp_indexer_a2a_for_bucket), [`_topk_rows`](mla_attention_op.md#_topk_rows)

## Functions
- <a id="_cp_scatter_indexer_k"></a>`_cp_scatter_indexer_k(cache_kv: jax.Array, k_packed: jax.Array, seq_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, *, mesh, cp_size: int, interleave_size: int, axis_name: str = DCP_AXIS_NAME, writer: str = "xla", kv_layout: KVLayout = KVLayout.HEAD_ALONG_SUBLANE)` — [`L305`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L305) — Scatter this step's indexer K rows into the DCP-sharded K cache.
- <a id="_dcp_indexer_a2a_for_bucket"></a>`_dcp_indexer_a2a_for_bucket(num_tokens: int, enabled: bool, min_tokens: int)` — [`L242`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L242) — Whether the DCP indexer merge for this token bucket uses the all-to-all.
- <a id="_fake_topk_rows_update"></a>`_fake_topk_rows_update(buf: torch.Tensor, rows: torch.Tensor)` — [`L279`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L279)
- <a id="_cp_scatter_indexer_k._local"></a>`_local(cache_kv, k_packed, seq_lens, page_indices, cu_q_lens)` — [`L341`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L341)
- <a id="_log_indexer_kv_cache_once"></a>`_log_indexer_kv_cache_once(mode: str, writer: str, kv_layout: KVLayout, cache_shape: tuple[int, ...])` — [`L127`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L127) — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
- <a id="_resolve_indexer_kv_cache_mode"></a>`_resolve_indexer_kv_cache_mode(cache_kv: jax.Array, k_packed: jax.Array, *, mode: str | None = None)` — [`L164`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L164) — Resolves the indexer K-cache `(writer, kv_layout)` for `cache_kv` and `k_packed`. — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
- <a id="_streamidx_block_sizes"></a>`_streamidx_block_sizes(num_tokens: int, small_bucket_bq: int | None, small_bucket_bkvp: int | None, small_bucket_tokens: int)` — [`L90`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L90) — (num_kv_pages_per_block, num_queries_per_block) for a padded token bucket.
- <a id="_topk_rows"></a>`_topk_rows(buf: torch.Tensor, topk_tokens: int, num_tokens: int, topk_indices: torch.Tensor)` — [`L287`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L287) — The `[num_tokens, buf.shape[1]]` rows the -1 fill plus partial write
- <a id="_topk_rows_update_jax"></a>`_topk_rows_update_jax(buf: jax.Array, rows: jax.Array)` — [`L254`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L254) — `buf[:rows.shape[0]] = rows` as one row update of a donated buffer.
- <a id="_unsupported_indexer_kv_cache_reason"></a>`_unsupported_indexer_kv_cache_reason(cache_kv: jax.Array, k_packed: jax.Array, kv_layout: KVLayout)` — [`L148`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L148) — Returns a human-readable reason if `cache_kv`/`k_packed` cannot use Pallas.
- <a id="_warn_indexer_kv_cache_fallback_once"></a>`_warn_indexer_kv_cache_fallback_once(mode: str, reason: str)` — [`L115`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L115)

## Module values
- <a id="STREAMIDX_ENABLE_EARLY_EXIT"></a>`STREAMIDX_ENABLE_EARLY_EXIT` — [`L82`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L82)
- <a id="STREAMIDX_KV_PAGES_PER_BLOCK"></a>`STREAMIDX_KV_PAGES_PER_BLOCK` — [`L84`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L84)
- <a id="STREAMIDX_QUERIES_PER_BLOCK"></a>`STREAMIDX_QUERIES_PER_BLOCK` — [`L85`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L85)
- <a id="STREAMIDX_SMALL_BUCKET_DEFAULT_BKVP"></a>`STREAMIDX_SMALL_BUCKET_DEFAULT_BKVP` — [`L87`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L87)
- <a id="VllmMLAAttention"></a>`VllmMLAAttention` — [`L1097`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1097)
- <a id="VllmMultiHeadLatentAttentionWrapper"></a>`VllmMultiHeadLatentAttentionWrapper` — [`L1350`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L1350)
- <a id="_INDEXER_KV_CACHE_FALLBACK_LOGGED._INDEXER_KV_CACHE_FALLBACK_LOGGED"></a>`_INDEXER_KV_CACHE_FALLBACK_LOGGED` — [`L111`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L111)
- <a id="_INDEXER_KV_CACHE_INFO_LOGGED._INDEXER_KV_CACHE_INFO_LOGGED"></a>`_INDEXER_KV_CACHE_INFO_LOGGED` — [`L112`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L112)
- <a id="_TOPK_ROWS_UPDATE_OP"></a>`_TOPK_ROWS_UPDATE_OP` — [`L269`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L269)
- <a id="logger"></a>`logger` — [`L75`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/mla_attention_op.py#L75)

