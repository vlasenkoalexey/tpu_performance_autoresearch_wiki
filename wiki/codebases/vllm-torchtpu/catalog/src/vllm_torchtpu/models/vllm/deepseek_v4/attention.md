---
title: 'Module: src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.deepseek_v4.attention`/
symbols:
  VllmDeepseekV4MLAAttention.mla_attn: VllmDeepseekV4MLAAttention#mla_attn.
  VllmDeepseekV4MLAAttention._build_attn_op: VllmDeepseekV4MLAAttention#_build_attn_op().
  VllmDeepseekV4MLAAttention.forward_mqa: VllmDeepseekV4MLAAttention#forward_mqa().
  VllmDeepseekV4MLAAttention.qnorm_rope_op: VllmDeepseekV4MLAAttention#qnorm_rope_op().
  VllmDeepseekV4MLAAttention.o_proj_op: VllmDeepseekV4MLAAttention#o_proj_op().
  VllmDeepseekV4MLAAttention.attention_impl: VllmDeepseekV4MLAAttention#attention_impl().
  VllmDeepseekV4MLAAttention.__init__: VllmDeepseekV4MLAAttention#__init__().
  VllmDeepseekV4MLAAttention.kv_rope_op: VllmDeepseekV4MLAAttention#kv_rope_op().
  VllmDeepseekV4MLAAttention._get_active_sw_cache: VllmDeepseekV4MLAAttention#_get_active_sw_cache().
  VllmDeepseekV4MLAAttention.forward: VllmDeepseekV4MLAAttention#forward().
  VllmDeepseekV4MLAAttention.custom_prefix: VllmDeepseekV4MLAAttention#custom_prefix.
  _pallas_op_cache._pallas_op_cache: _pallas_op_cache._pallas_op_cache.
  VllmDeepseekV4MLAAttention.attn_op: VllmDeepseekV4MLAAttention#attn_op().
  VllmDeepseekV4MLAAttention._get_field: VllmDeepseekV4MLAAttention#_get_field().
  VllmDeepseekV4MLAAttention: VllmDeepseekV4MLAAttention#
  _live_cache: _live_cache().
  VllmDeepseekV4MLAAttention.qnorm_rope: VllmDeepseekV4MLAAttention#qnorm_rope().
  VllmDeepseekV4MLAAttention.kv_rope: VllmDeepseekV4MLAAttention#kv_rope().
  VllmDeepseekV4MLAAttention._project_q: VllmDeepseekV4MLAAttention#_project_q().
  VllmDeepseekV4MLAAttention.process_weights_after_loading: VllmDeepseekV4MLAAttention#process_weights_after_loading().
  VllmDeepseekV4MLAAttention._o_proj: VllmDeepseekV4MLAAttention#_o_proj().
  DeepseekV4TPUAttentionBackend: DeepseekV4TPUAttentionBackend#
  logger: logger.
  _qnorm_rope_jax: _qnorm_rope_jax().
  _rope_jax: _rope_jax().
  _o_proj_jax: _o_proj_jax().
  VllmDeepseekV4MLAAttention.get_kv_cache_spec: VllmDeepseekV4MLAAttention#get_kv_cache_spec().
  VllmDeepseekV4MLAAttention._fake_attn: VllmDeepseekV4MLAAttention#_fake_attn().
  VllmDeepseekV4MLAAttention._as_kernel_cache_view: VllmDeepseekV4MLAAttention#_as_kernel_cache_view().
  VllmDeepseekV4MLAAttention.backend_cls: VllmDeepseekV4MLAAttention#backend_cls.
  VllmDeepseekV4MLAAttention.swa_backend_cls: VllmDeepseekV4MLAAttention#swa_backend_cls.
  VllmDeepseekV4MLAAttention.num_layers: VllmDeepseekV4MLAAttention#num_layers.
  VllmDeepseekV4MLAAttention.get_attn_backend: VllmDeepseekV4MLAAttention#get_attn_backend().
  _fake_rope: _fake_rope().
  _fake_o_proj: _fake_o_proj().
  _name_float: _name_float().
  VllmDeepseekV4MLAAttention.non_causal_multi_token_decode: VllmDeepseekV4MLAAttention#non_causal_multi_token_decode.
  VllmDeepseekV4MLAAttention._attn_sink_loader: VllmDeepseekV4MLAAttention#_attn_sink_loader().
  VllmDeepseekV4MLAAttention.attn_gemm: VllmDeepseekV4MLAAttention#attn_gemm().
  VllmDeepseekV4MLAAttention._assert_o_proj_supported: VllmDeepseekV4MLAAttention#_assert_o_proj_supported().
  DeepseekV4TPUAttentionBackend.supported_kv_cache_layouts: DeepseekV4TPUAttentionBackend#supported_kv_cache_layouts().
  VllmDeepseekV4MLAAttention.get_padded_num_q_heads: VllmDeepseekV4MLAAttention#get_padded_num_q_heads().
---
# Module: [`src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py)

## Classes
### <a id="DeepseekV4TPUAttentionBackend"></a>`DeepseekV4TPUAttentionBackend`  ·  implements/extends PallasAttentionBackend
- def: [`src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py:72`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L72) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
- signature: `class DeepseekV4TPUAttentionBackend(PallasAttentionBackend):`
- members:
  - <a id="DeepseekV4TPUAttentionBackend.supported_kv_cache_layouts"></a>`supported_kv_cache_layouts(cls)` — [`L74`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L74) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
- uses (calls/refs, reference-scoped): [`PallasAttentionBackend`](../../../layers/adapter/attention.md#PallasAttentionBackend)
- used by: [`PallasAttentionBackend`](../../../layers/adapter/attention.md#PallasAttentionBackend), [`supported_kv_cache_layouts`](../../../layers/adapter/attention.md#PallasAttentionBackend.supported_kv_cache_layouts), [`backend_cls`](attention.md#VllmDeepseekV4MLAAttention.backend_cls), [`get_attn_backend`](attention.md#VllmDeepseekV4MLAAttention.get_attn_backend)

### <a id="VllmDeepseekV4MLAAttention"></a>`VllmDeepseekV4MLAAttention`
- def: [`src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py:146`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L146) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
- doc: Sparse MLA attention on TPU, over the SWA and compressed-KV caches.
- signature: `class VllmDeepseekV4MLAAttention(dsv4_attention.DeepseekV4Attention, AttentionLayerBase):`
- members:
  - <a id="VllmDeepseekV4MLAAttention._as_kernel_cache_view"></a>`_as_kernel_cache_view(cache: torch.Tensor | None)` — [`L587`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L587) — Bitcast 1-byte cache allocations to uint8 required by Pallas kernels.
  - <a id="VllmDeepseekV4MLAAttention._assert_o_proj_supported"></a>`_assert_o_proj_supported(self)` — [`L803`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L803) — Check what the fused `wo_a` kernel requires.
  - <a id="VllmDeepseekV4MLAAttention._fake_attn"></a>`_fake_attn(q, new_kv, sw_cache, *args, **kwargs)` — [`L450`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L450) — Abstract fake tensor implementation for PyTorch Dynamo graph tracing.
  - <a id="VllmDeepseekV4MLAAttention._get_active_sw_cache"></a>`_get_active_sw_cache(self)` — [`L595`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L595) — Retrieve active sliding-window cache buffer if allocated. — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="VllmDeepseekV4MLAAttention._o_proj"></a>`_o_proj(self, o: torch.Tensor | Any, positions: torch.Tensor)` — [`L854`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L854) — Apply inverse RoPE and low-rank output projections wo_a and wo_b.
  - <a id="VllmDeepseekV4MLAAttention._project_q"></a>`_project_q(self, qr: torch.Tensor)` — [`L543`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L543) — Project the q latent to query heads: [num_tokens, heads, head_dim].
  - <a id="VllmDeepseekV4MLAAttention.attention_impl"></a>`attention_impl(self, hidden_states: torch.Tensor, qr: torch.Tensor, kv: torch.Tensor, indexer_weights: torch.Tensor | None, positions: torch.Tensor, out: torch.Tensor | None)` — [`L549`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L549) — Execute indexing, state compression, and kernel attention dispatch. — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="VllmDeepseekV4MLAAttention.attn_gemm"></a>`attn_gemm(self, hidden_states: torch.Tensor)` — [`L464`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L464)
  - <a id="VllmDeepseekV4MLAAttention.attn_op"></a>`attn_op(self)` — [`L281`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L281) — The Pallas attention op, built lazily on first forward — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="VllmDeepseekV4MLAAttention.forward"></a>`forward(self, positions: torch.Tensor, hidden_states: torch.Tensor)` — [`L880`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L880) — Forward pass for DeepSeek-V4 attention layer.
  - <a id="VllmDeepseekV4MLAAttention.forward_mqa"></a>`forward_mqa(self, q: torch.Tensor, kv: torch.Tensor, positions: torch.Tensor, output: torch.Tensor | None, *, topk_indices: torch.Tensor | None)` — [`L604`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L604) — Prepare metadata operands and dispatch the Pallas attention op. — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="VllmDeepseekV4MLAAttention.get_attn_backend"></a>`get_attn_backend(self)` — [`L250`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L250)
  - <a id="VllmDeepseekV4MLAAttention.get_kv_cache_spec"></a>`get_kv_cache_spec(self, vllm_config: VllmConfig)` — [`L253`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L253) — Derive the main compressed-KV cache spec, or None for SWA-only layers.
  - <a id="VllmDeepseekV4MLAAttention.get_padded_num_q_heads"></a>`get_padded_num_q_heads(cls, num_heads: int)` — [`L247`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L247)
  - <a id="VllmDeepseekV4MLAAttention.kv_rope"></a>`kv_rope(self, kv: torch.Tensor, positions: torch.Tensor)` — [`L535`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L535) — Apply scaling RoPE to decoupled key states.
  - <a id="VllmDeepseekV4MLAAttention.kv_rope_op"></a>`kv_rope_op(self)` — [`L503`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L503) — The RoPE op for the decoupled key states, built lazily. — documented in [vllm-model-patches](../../../../../../concepts/vllm-model-patches.md)
  - <a id="VllmDeepseekV4MLAAttention.o_proj_op"></a>`o_proj_op(self)` — [`L753`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L753) — The fused inverse-RoPE + `wo_a` projection op, built lazily. — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="VllmDeepseekV4MLAAttention.process_weights_after_loading"></a>`process_weights_after_loading(self, act_dtype: torch.dtype)` — [`L781`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L781) — Store `wo_a` in the layout the fused o-projection kernel wants,
  - <a id="VllmDeepseekV4MLAAttention.qnorm_rope"></a>`qnorm_rope(self, q: torch.Tensor, positions: torch.Tensor)` — [`L527`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L527) — Apply RMSNorm and scaling RoPE to query head states.
  - <a id="VllmDeepseekV4MLAAttention.qnorm_rope_op"></a>`qnorm_rope_op(self)` — [`L477`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L477) — The fused q-RMSNorm + RoPE op, built lazily on first forward. — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="VllmDeepseekV4MLAAttention.backend_cls"></a>`backend_cls` — [`L151`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L151)
  - <a id="VllmDeepseekV4MLAAttention.custom_prefix"></a>`custom_prefix` — [`L184`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L184) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="VllmDeepseekV4MLAAttention.mla_attn"></a>`mla_attn` — [`L154`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L154) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="VllmDeepseekV4MLAAttention.non_causal_multi_token_decode"></a>`non_causal_multi_token_decode` — [`L156`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L156)
  - <a id="VllmDeepseekV4MLAAttention.num_layers"></a>`num_layers` — [`L223`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L223)
  - <a id="VllmDeepseekV4MLAAttention.swa_backend_cls"></a>`swa_backend_cls` — [`L152`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L152)
- protocol/private: <a id="VllmDeepseekV4MLAAttention.__init__"></a>`__init__`[`L158`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L158), <a id="VllmDeepseekV4MLAAttention._attn_sink_loader"></a>`_attn_sink_loader`[`L210`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L210), <a id="VllmDeepseekV4MLAAttention._build_attn_op"></a>`_build_attn_op`[`L304`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L304), <a id="VllmDeepseekV4MLAAttention._get_field"></a>`_get_field`[`L619`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L619)
- uses (calls/refs, reference-scoped): [`fresh_buffer`](../../../utils.md#fresh_buffer), [`get_vllm_model_wrapper_context`](../vllm_model_wrapper_context.md#get_vllm_model_wrapper_context), [`get_pallas_op_mesh`](../vllm_model_wrapper_context.md#get_pallas_op_mesh), [`_o_proj`](attn_intra_chip.md#VllmDeepseekV4MLAAttentionIntraChip._o_proj), [`vllm_config`](../vllm_model_wrapper_context.md#VllmModelWrapperContext.vllm_config), [`_project_q`](attn_intra_chip.md#VllmDeepseekV4MLAAttentionIntraChip._project_q), [`static_verify_q_len`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.md#static_verify_q_len), [`_pallas_op_cache`](attention.md#_pallas_op_cache._pallas_op_cache), [`process_weights_after_loading`](attn_intra_chip.md#VllmDeepseekV4MLAAttentionIntraChip.process_weights_after_loading), [`_attention_csa`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.md#_attention_csa), [`_attention_hca`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.md#_attention_hca), [`_live_cache`](attention.md#_live_cache), [`VllmDeepseekCompressor`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.md#VllmDeepseekCompressor), [`DeepseekV4TPUAttentionBackend`](attention.md#DeepseekV4TPUAttentionBackend), [`get_packed_mla_head_size`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.md#get_packed_mla_head_size), [`VllmDeepseekV4MLAAttentionIntraChip`](attn_intra_chip.md#VllmDeepseekV4MLAAttentionIntraChip), [`_o_proj_jax`](attention.md#_o_proj_jax), [`_qnorm_rope_jax`](attention.md#_qnorm_rope_jax), [`_rope_jax`](attention.md#_rope_jax), [`logger`](attention.md#logger), [`VllmDeepseekSparseSWABackend`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.md#VllmDeepseekSparseSWABackend), [`VllmDeepseekV4SWACache`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.md#VllmDeepseekV4SWACache), [`_swa_block_size`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.md#VllmDeepseekV4SWACache._swa_block_size), [`VllmDeepseekV4Indexer`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.md#VllmDeepseekV4Indexer), [`BATCH_AXIS`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.md#BATCH_AXIS), [`_fake_rope`](attention.md#_fake_rope), [`_fake_o_proj`](attention.md#_fake_o_proj), [`_name_float`](attention.md#_name_float)
- used by: [`layers`](dspark.md#DSparkDeepseekV4Model.layers), [`precompute_and_store_context_kv`](dspark.md#DSparkDeepseekV4Model.precompute_and_store_context_kv), [`_o_proj`](attn_intra_chip.md#VllmDeepseekV4MLAAttentionIntraChip._o_proj), [`rms_norm_eps`](model.md#DeepseekV4DecoderLayer.rms_norm_eps), [`_project_q`](attn_intra_chip.md#VllmDeepseekV4MLAAttentionIntraChip._project_q), [`n_local_groups`](attn_intra_chip.md#VllmDeepseekV4MLAAttentionIntraChip.n_local_groups), [`__init__`](attn_intra_chip.md#VllmDeepseekV4MLAAttentionIntraChip.__init__), [`VllmDeepseekV4MLAAttentionIntraChip`](attn_intra_chip.md#VllmDeepseekV4MLAAttentionIntraChip)

## Functions
- <a id="_fake_o_proj"></a>`_fake_o_proj(x, positions, cos_sin_cache, wo_a, wo_a_scale, *args, **kwargs)` — [`L126`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L126) — Abstract implementation for PyTorch Dynamo graph tracing.
- <a id="_fake_rope"></a>`_fake_rope(x, positions, cos_sin_cache, *args, **kwargs)` — [`L121`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L121) — Abstract implementation for PyTorch Dynamo graph tracing.
- <a id="_live_cache"></a>`_live_cache(entry: Any)` — [`L137`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L137) — The array bound to a layer, or None while it has none. — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
- <a id="_name_float"></a>`_name_float(value: float)` — [`L131`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L131) — A float rendered so it is safe inside a torch op name.
- <a id="_o_proj_jax"></a>`_o_proj_jax(x: jax.Array, positions: jax.Array, cos_sin_cache: jax.Array, wo_a: jax.Array, wo_a_scale: jax.Array, *, head_dim: int)` — [`L99`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L99) — Inverse RoPE fused into the per-group `wo_a` projection.
- <a id="_qnorm_rope_jax"></a>`_qnorm_rope_jax(x: jax.Array, positions: jax.Array, cos_sin_cache: jax.Array, *, eps: float)` — [`L79`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L79) — Per-head RMSNorm (no weight) fused with RoPE on the query heads.
- <a id="_rope_jax"></a>`_rope_jax(x: jax.Array, positions: jax.Array, cos_sin_cache: jax.Array)` — [`L90`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L90) — RoPE over the trailing `rotary_dim` channels of `x`.

## Module values
- <a id="_pallas_op_cache._pallas_op_cache"></a>`_pallas_op_cache` — [`L69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L69) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
- <a id="logger"></a>`logger` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py#L67)

