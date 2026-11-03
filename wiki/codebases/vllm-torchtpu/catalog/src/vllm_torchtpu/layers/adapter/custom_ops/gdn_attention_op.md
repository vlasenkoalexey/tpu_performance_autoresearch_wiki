---
title: 'Module: src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.custom_ops.gdn_attention_op`/
symbols:
  VllmGatedDeltaNetAttention.forward: VllmGatedDeltaNetAttention#forward().
  VllmGatedDeltaNetAttention._build_gdn_op: VllmGatedDeltaNetAttention#_build_gdn_op().
  VllmGatedDeltaNetAttention._build_pooled_pcp_gdn_op: VllmGatedDeltaNetAttention#_build_pooled_pcp_gdn_op().
  VllmGatedDeltaNetAttention._build_pooled_gdn_op: VllmGatedDeltaNetAttention#_build_pooled_gdn_op().
  _GDN_TP_AXIS_NAME: _GDN_TP_AXIS_NAME.
  VllmGatedDeltaNetAttention.conv1d: VllmGatedDeltaNetAttention#conv1d.
  VllmGatedDeltaNetAttention._forward_fused_pooled_pcp: VllmGatedDeltaNetAttention#_forward_fused_pooled_pcp().
  _GDN_PCP_AXIS_NAME: _GDN_PCP_AXIS_NAME.
  VllmGatedDeltaNetAttention.tp_head_geometry: VllmGatedDeltaNetAttention#tp_head_geometry().
  VllmGatedDeltaNetAttention.get_kv_cache_spec: VllmGatedDeltaNetAttention#get_kv_cache_spec().
  VllmGatedDeltaNetAttention._bm_state_ids: VllmGatedDeltaNetAttention#_bm_state_ids().
  _GDN_PCP_TP_STATE_AXIS: _GDN_PCP_TP_STATE_AXIS.
  VllmGatedDeltaNetAttention.kv_cache: VllmGatedDeltaNetAttention#kv_cache.
  VllmGatedDeltaNetAttention._create_conv1d: VllmGatedDeltaNetAttention#_create_conv1d().
  VllmGatedDeltaNetAttention.wrapped_fn: VllmGatedDeltaNetAttention#wrapped_fn().
  VllmGatedDeltaNetAttention.gdn_pooled_op: VllmGatedDeltaNetAttention#gdn_pooled_op.
  VllmGatedDeltaNetAttention.set_block_major_pool: VllmGatedDeltaNetAttention#set_block_major_pool().
  VllmGatedDeltaNetAttention.create_qkvz_proj: VllmGatedDeltaNetAttention#create_qkvz_proj().
  VllmGatedDeltaNetAttention.process_weights_after_loading: VllmGatedDeltaNetAttention#process_weights_after_loading().
  _localize_gdn_mamba_spec_for_pcp: _localize_gdn_mamba_spec_for_pcp().
  _get_shared_gdn_op: _get_shared_gdn_op().
  VllmGatedDeltaNetAttention.gdn_pooled_pcp_op: VllmGatedDeltaNetAttention#gdn_pooled_pcp_op.
  VllmGatedDeltaNetAttention._pcp_streaming_enabled: VllmGatedDeltaNetAttention#_pcp_streaming_enabled().
  VllmGatedDeltaNetAttention.build_op: VllmGatedDeltaNetAttention#build_op().
  VllmGatedDeltaNetAttention._bm_region: VllmGatedDeltaNetAttention#_bm_region.
  VllmGatedDeltaNetAttention._bm_kernel: VllmGatedDeltaNetAttention#_bm_kernel.
  VllmGatedDeltaNetAttention.__init__: VllmGatedDeltaNetAttention#__init__().
  VllmGatedDeltaNetAttention.create_ba_proj: VllmGatedDeltaNetAttention#create_ba_proj().
  VllmGatedDeltaNetAttention.get_state_shape: VllmGatedDeltaNetAttention#get_state_shape().
  VllmGatedDeltaNetAttention.get_state_dtype: VllmGatedDeltaNetAttention#get_state_dtype().
  _GdnAttentionMetadata.seq_lens: _GdnAttentionMetadata#seq_lens.
  _GdnAttentionMetadata.mamba_state_indices: _GdnAttentionMetadata#mamba_state_indices.
  logger: logger.
  gdn_attention_core_tpu: gdn_attention_core_tpu().
  gdn_attention_pooled_core_tpu: gdn_attention_pooled_core_tpu().
  gdn_attention_core_tpu_pcp_prefill: gdn_attention_core_tpu_pcp_prefill().
  VllmGatedDeltaNetAttention.gdn_op: VllmGatedDeltaNetAttention#gdn_op.
  VllmGatedDeltaNetAttention.gdn_pcp_op: VllmGatedDeltaNetAttention#gdn_pcp_op.
  VllmGatedDeltaNetAttention._require_pcp_projection_parameters: VllmGatedDeltaNetAttention#_require_pcp_projection_parameters().
  VllmGatedDeltaNetAttention._has_active_pooled_pcp_state: VllmGatedDeltaNetAttention#_has_active_pooled_pcp_state().
  _GdnAttentionMetadata.query_start_loc: _GdnAttentionMetadata#query_start_loc.
  _GdnAttentionMetadata.request_distribution: _GdnAttentionMetadata#request_distribution.
  VllmGatedDeltaNetAttention._fake_gdn: VllmGatedDeltaNetAttention#_fake_gdn().
  VllmGatedDeltaNetAttention.gdn_impl: VllmGatedDeltaNetAttention#gdn_impl().
  _GdnAttentionMetadata.block_tables: _GdnAttentionMetadata#block_tables.
  _to_jax_ssm_state_dtype: _to_jax_ssm_state_dtype().
  VllmGatedDeltaNetAttention: VllmGatedDeltaNetAttention#
  VllmGatedDeltaNetAttention._apply_output_projection: VllmGatedDeltaNetAttention#_apply_output_projection().
  _shared_gdn_ops._shared_gdn_ops: _shared_gdn_ops._shared_gdn_ops.
  _get_pcp_size: _get_pcp_size().
  _shared_gdn_op_ids: _shared_gdn_op_ids.
  VllmGatedDeltaNetAttention._pcp_streaming_configured: VllmGatedDeltaNetAttention#_pcp_streaming_configured.
  _GdnAttentionMetadata: _GdnAttentionMetadata#
---
# Module: [`src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py)

## Classes
### <a id="VllmGatedDeltaNetAttention"></a>`VllmGatedDeltaNetAttention`
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py:366`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L366)
- signature: `class VllmGatedDeltaNetAttention(QwenGatedDeltaNetAttention):`
- members:
  - <a id="VllmGatedDeltaNetAttention._forward_fused_pooled_pcp"></a>`_forward_fused_pooled_pcp(self, hidden_states: torch.Tensor, state_pool: torch.Tensor, attn_metadata)` — [`L1076`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L1076) — Run the mandatory fused path for an allocated pooled PCP call. — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
  - <a id="VllmGatedDeltaNetAttention._has_active_pooled_pcp_state"></a>`_has_active_pooled_pcp_state(self, kv_cache)` — [`L1055`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L1055) — Whether a PCP-configured worker owns an allocated unified pool.
  - <a id="VllmGatedDeltaNetAttention._require_pcp_projection_parameters"></a>`_require_pcp_projection_parameters(self)` — [`L1020`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L1020) — Return BF16/FP8 QKVZ parameters in canonical runtime layout. — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="VllmGatedDeltaNetAttention.build_op"></a>`build_op(op_name: str)` — [`L783`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L783)
  - <a id="VllmGatedDeltaNetAttention.create_ba_proj"></a>`create_ba_proj(self, hidden_size: int, num_v_heads: int, quant_config: QuantizationConfig | None, prefix: str)` — [`L457`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L457)
  - <a id="VllmGatedDeltaNetAttention.create_qkvz_proj"></a>`create_qkvz_proj(self, hidden_size: int, key_dim: int, value_dim: int, quant_config: QuantizationConfig | None, prefix: str)` — [`L429`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L429)
  - <a id="VllmGatedDeltaNetAttention.forward"></a>`forward(self, hidden_states: torch.Tensor)` — [`L1118`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L1118) — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
  - <a id="VllmGatedDeltaNetAttention.gdn_impl"></a>`gdn_impl(mixed_qkv: torch.Tensor, b: torch.Tensor, a: torch.Tensor, conv_state: torch.Tensor, recurrent_state: torch.Tensor, conv_weight: torch.Tensor, conv_bias: torch.Tensor | None, A_log: torch.Tensor, dt_bias: torch.Tensor, state_indices: torch.Tensor, query_start_loc: torch.Tensor, request_distribution: torch.Tensor, seq_lens: torch.Tensor, slot_read_offsets: torch.Tensor | None = None)` — [`L659`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L659)
  - <a id="VllmGatedDeltaNetAttention.get_kv_cache_spec"></a>`get_kv_cache_spec(self, vllm_config: VllmConfig)` — [`L491`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L491) — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
  - <a id="VllmGatedDeltaNetAttention.get_state_dtype"></a>`get_state_dtype(self)` — [`L505`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L505)
  - <a id="VllmGatedDeltaNetAttention.get_state_shape"></a>`get_state_shape(self)` — [`L532`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L532)
  - <a id="VllmGatedDeltaNetAttention.process_weights_after_loading"></a>`process_weights_after_loading(self, act_dtype: torch.dtype)` — [`L517`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L517) — Back the conv weight with a buffer of its own 3-D shape.
  - <a id="VllmGatedDeltaNetAttention.set_block_major_pool"></a>`set_block_major_pool(self, pool_index: int, layout: BlockMajorPoolLayout)` — [`L409`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L409) — Binds this layer to its region index within the merged block-major pool. — documented in [kv-cache-layout-and-hbm-budget](../../../../../../concepts/kv-cache-layout-and-hbm-budget.md)
  - <a id="VllmGatedDeltaNetAttention.tp_head_geometry"></a>`tp_head_geometry(self)` — [`L424`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L424) — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
  - <a id="VllmGatedDeltaNetAttention.wrapped_fn"></a>`wrapped_fn(mixed_qkv: jax.Array, b: jax.Array, a: jax.Array, recurrent_state: jax.Array, conv_weight: jax.Array, conv_bias: jax.Array | None, A_log: jax.Array, dt_bias: jax.Array, state_indices: jax.Array, query_start_loc: jax.Array, distribution: jax.Array, seq_lens: jax.Array, slot_read_offsets: jax.Array | None = None, ckpt_indices: jax.Array | None = None)` — [`L721`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L721)
  - <a id="VllmGatedDeltaNetAttention.conv1d"></a>`conv1d` — [`L375`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L375) — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
  - <a id="VllmGatedDeltaNetAttention.gdn_op"></a>`gdn_op` — [`L396`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L396)
  - <a id="VllmGatedDeltaNetAttention.gdn_pcp_op"></a>`gdn_pcp_op` — [`L400`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L400)
  - <a id="VllmGatedDeltaNetAttention.gdn_pooled_op"></a>`gdn_pooled_op` — [`L397`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L397)
  - <a id="VllmGatedDeltaNetAttention.gdn_pooled_pcp_op"></a>`gdn_pooled_pcp_op` — [`L403`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L403)
  - <a id="VllmGatedDeltaNetAttention.kv_cache"></a>`kv_cache` — [`L388`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L388)
- protocol/private: <a id="VllmGatedDeltaNetAttention.__init__"></a>`__init__`[`L377`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L377), <a id="VllmGatedDeltaNetAttention._apply_output_projection"></a>`_apply_output_projection`[`L1064`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L1064), <a id="VllmGatedDeltaNetAttention._bm_kernel"></a>`_bm_kernel`[`L370`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L370), <a id="VllmGatedDeltaNetAttention._bm_region"></a>`_bm_region`[`L371`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L371), <a id="VllmGatedDeltaNetAttention._bm_state_ids"></a>`_bm_state_ids`[`L416`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L416), <a id="VllmGatedDeltaNetAttention._build_gdn_op"></a>`_build_gdn_op`[`L553`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L553), <a id="VllmGatedDeltaNetAttention._build_pooled_gdn_op"></a>`_build_pooled_gdn_op`[`L702`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L702), <a id="VllmGatedDeltaNetAttention._build_pooled_pcp_gdn_op"></a>`_build_pooled_pcp_gdn_op`[`L849`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L849), <a id="VllmGatedDeltaNetAttention._create_conv1d"></a>`_create_conv1d`[`L476`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L476), <a id="VllmGatedDeltaNetAttention._fake_gdn"></a>`_fake_gdn`[`L563`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L563), <a id="VllmGatedDeltaNetAttention._pcp_streaming_configured"></a>`_pcp_streaming_configured`[`L399`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L399), <a id="VllmGatedDeltaNetAttention._pcp_streaming_enabled"></a>`_pcp_streaming_enabled`[`L546`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L546)
- uses (calls/refs, reference-scoped): [`fresh_buffer`](../../../utils.md#fresh_buffer), [`derive_gdn_head_geometry`](../../../kernels/gdn/head_geometry.md#derive_gdn_head_geometry), [`get_or_create_pcp_mesh`](../../../distributed/pcp.md#get_or_create_pcp_mesh), [`_GDN_TP_AXIS_NAME`](gdn_attention_op.md#_GDN_TP_AXIS_NAME), [`get_vllm_model_wrapper_context`](../../../models/vllm/vllm_model_wrapper_context.md#get_vllm_model_wrapper_context), [`run_jax_gdn_attention_pooled_pcp_prefill_projection`](../../core/gdn_attention.md#run_jax_gdn_attention_pooled_pcp_prefill_projection), [`BlockMajorPoolLayout`](../../../block_major_pool.md#BlockMajorPoolLayout), [`get_pcp_rank`](../../../distributed/pcp.md#get_pcp_rank), [`is_pcp_streaming_attention_metadata`](../../core/sequence_layout.md#is_pcp_streaming_attention_metadata), [`_GDN_PCP_AXIS_NAME`](gdn_attention_op.md#_GDN_PCP_AXIS_NAME), [`local_num_kq_heads`](../../../kernels/gdn/head_geometry.md#GdnHeadGeometry.local_num_kq_heads), [`get_pcp_world_size`](../../../distributed/pcp.md#get_pcp_world_size), [`unified_block_major_enabled`](../../../block_major_pool.md#unified_block_major_enabled), [`projection_scale_layout`](../../../kernels/experimental/gdn_pcp_fused/projection_scale.md#projection_scale_layout), [`KEEP_VLLM_LAYOUT_ATTR`](../linear_common.md#KEEP_VLLM_LAYOUT_ATTR), [`GdnHeadGeometry`](../../../kernels/gdn/head_geometry.md#GdnHeadGeometry), [`local_num_v_heads`](../../../kernels/gdn/head_geometry.md#GdnHeadGeometry.local_num_v_heads), [`vllm_config`](../../../models/vllm/vllm_model_wrapper_context.md#VllmModelWrapperContext.vllm_config), [`_GDN_PCP_TP_STATE_AXIS`](gdn_attention_op.md#_GDN_PCP_TP_STATE_AXIS), [`local_conv_dim`](../../../kernels/gdn/head_geometry.md#GdnHeadGeometry.local_conv_dim), [`local_state_shapes`](../../../kernels/gdn/head_geometry.md#GdnHeadGeometry.local_state_shapes), [`num_pools`](../../../block_major_pool.md#BlockMajorPoolLayout.num_pools), [`weight`](../gdn_linear.md#GdnColumnParallelLinear.weight), [`mesh`](../../../models/vllm/vllm_model_wrapper_context.md#VllmModelWrapperContext.mesh), [`_get_shared_gdn_op`](gdn_attention_op.md#_get_shared_gdn_op), [`_localize_gdn_mamba_spec_for_pcp`](gdn_attention_op.md#_localize_gdn_mamba_spec_for_pcp), [`GdnInterleavedColumnParallelLinear`](../gdn_linear.md#GdnInterleavedColumnParallelLinear), [`kernel_view`](../../../block_major_pool.md#kernel_view), [`GdnColumnParallelLinear`](../gdn_linear.md#GdnColumnParallelLinear), [`mamba_state_indices`](gdn_attention_op.md#_GdnAttentionMetadata.mamba_state_indices), [`seq_lens`](gdn_attention_op.md#_GdnAttentionMetadata.seq_lens), [`gdn_attention_core_tpu`](gdn_attention_op.md#gdn_attention_core_tpu), [`gdn_attention_core_tpu_pcp_prefill`](gdn_attention_op.md#gdn_attention_core_tpu_pcp_prefill), [`gdn_attention_pooled_core_tpu`](gdn_attention_op.md#gdn_attention_pooled_core_tpu), [`logger`](gdn_attention_op.md#logger), [`query_start_loc`](gdn_attention_op.md#_GdnAttentionMetadata.query_start_loc), [`request_distribution`](gdn_attention_op.md#_GdnAttentionMetadata.request_distribution), [`_to_jax_ssm_state_dtype`](gdn_attention_op.md#_to_jax_ssm_state_dtype), [`block_tables`](gdn_attention_op.md#_GdnAttentionMetadata.block_tables), [`flat_manager_ids`](../../../block_major_pool.md#flat_manager_ids)  (+1 more)
- used by: [`_bind_block_major_pool_layers`](../../../runner/kv_cache_manager.md#KVCacheManager._bind_block_major_pool_layers)

### <a id="_GdnAttentionMetadata"></a>`_GdnAttentionMetadata`  ·  implements/extends Protocol
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py:79`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L79)
- doc: The per-layer AttentionMetadata fields that GDN reads.
- signature: `class _GdnAttentionMetadata(Protocol):`
- members:
  - <a id="_GdnAttentionMetadata.block_tables"></a>`block_tables` — [`L86`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L86)
  - <a id="_GdnAttentionMetadata.mamba_state_indices"></a>`mamba_state_indices` — [`L90`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L90)
  - <a id="_GdnAttentionMetadata.query_start_loc"></a>`query_start_loc` — [`L88`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L88)
  - <a id="_GdnAttentionMetadata.request_distribution"></a>`request_distribution` — [`L89`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L89)
  - <a id="_GdnAttentionMetadata.seq_lens"></a>`seq_lens` — [`L87`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L87)
- used by: [`forward`](gdn_attention_op.md#VllmGatedDeltaNetAttention.forward)

## Functions
- <a id="_get_pcp_size"></a>`_get_pcp_size(vllm_config: VllmConfig)` — [`L291`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L291)
- <a id="_get_shared_gdn_op"></a>`_get_shared_gdn_op(kind: str, key: tuple, build: Callable[[str], Any])` — [`L352`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L352) — Return the ``pallas::<kind>_<n>`` op for ``(kind, key)``, building it once.
- <a id="_localize_gdn_mamba_spec_for_pcp"></a>`_localize_gdn_mamba_spec_for_pcp(spec: MambaSpec, pcp_size: int, *, num_kq_heads: int, num_v_heads: int, d_k: int, d_v: int)` — [`L296`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L296)
- <a id="_to_jax_ssm_state_dtype"></a>`_to_jax_ssm_state_dtype(dtype: torch.dtype)` — [`L96`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L96)
- <a id="gdn_attention_core_tpu"></a>`gdn_attention_core_tpu(mixed_qkv: jax.Array, b: jax.Array, a: jax.Array, conv_state: jax.Array, recurrent_state: jax.Array, conv_weight: jax.Array, conv_bias: jax.Array | None, A_log: jax.Array, dt_bias: jax.Array, state_indices: jax.Array, query_start_loc: jax.Array, distribution: jax.Array, seq_lens: jax.Array, slot_read_offsets: jax.Array | None = None, *, mesh: jax.sharding.Mesh, n_kq: int, n_v: int, d_k: int, d_v: int, kernel_size: int, num_spec_tokens: int = 0)` — [`L107`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L107)
- <a id="gdn_attention_core_tpu_pcp_prefill"></a>`gdn_attention_core_tpu_pcp_prefill(mixed_qkv: jax.Array, b: jax.Array, a: jax.Array, conv_state: jax.Array, recurrent_state: jax.Array, conv_weight: jax.Array, conv_bias: jax.Array | None, A_log: jax.Array, dt_bias: jax.Array, state_indices: jax.Array, query_start_loc: jax.Array, distribution: jax.Array, seq_lens: jax.Array, *, mesh: jax.sharding.Mesh, n_kq: int, n_v: int, d_k: int, d_v: int, kernel_size: int, pcp_size: int, interleave_size: int)` — [`L231`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L231)
- <a id="gdn_attention_pooled_core_tpu"></a>`gdn_attention_pooled_core_tpu(mixed_qkv: jax.Array, b: jax.Array, a: jax.Array, recurrent_state: jax.Array, conv_weight: jax.Array, conv_bias: jax.Array | None, A_log: jax.Array, dt_bias: jax.Array, state_indices: jax.Array, query_start_loc: jax.Array, distribution: jax.Array, seq_lens: jax.Array, slot_read_offsets: jax.Array | None = None, ckpt_indices: jax.Array | None = None, *, mesh: jax.sharding.Mesh, n_kq: int, n_v: int, d_k: int, d_v: int, kernel_size: int, pool_block_tokens: int, recurrent_state_dtype: jnp.dtype, num_spec_tokens: int = 0)` — [`L178`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L178)

## Module values
- <a id="_GDN_PCP_AXIS_NAME"></a>`_GDN_PCP_AXIS_NAME` — [`L73`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L73) — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
- <a id="_GDN_PCP_TP_STATE_AXIS"></a>`_GDN_PCP_TP_STATE_AXIS` — [`L75`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L75)
- <a id="_GDN_TP_AXIS_NAME"></a>`_GDN_TP_AXIS_NAME` — [`L74`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L74) — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
- <a id="_shared_gdn_op_ids"></a>`_shared_gdn_op_ids` — [`L349`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L349)
- <a id="_shared_gdn_ops._shared_gdn_ops"></a>`_shared_gdn_ops` — [`L348`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L348)
- <a id="logger"></a>`logger` — [`L93`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/gdn_attention_op.py#L93)

