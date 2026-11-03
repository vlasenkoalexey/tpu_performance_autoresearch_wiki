---
title: 'Module: src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.vllm_model_wrapper_context`/
symbols:
  set_vllm_model_wrapper_context: set_vllm_model_wrapper_context().
  get_vllm_model_wrapper_context: get_vllm_model_wrapper_context().
  get_pallas_op_mesh: get_pallas_op_mesh().
  VllmModelWrapperContext.vllm_config: VllmModelWrapperContext#vllm_config.
  _vllm_model_wrapper_context._vllm_model_wrapper_context: _vllm_model_wrapper_context._vllm_model_wrapper_context.
  VllmModelWrapperContext.mesh: VllmModelWrapperContext#mesh.
  VllmModelWrapperContext.kv_cache_bundle: VllmModelWrapperContext#kv_cache_bundle.
  VllmModelWrapperContext: VllmModelWrapperContext#
  VllmModelWrapperContext.kv_caches: VllmModelWrapperContext#kv_caches.
  VllmModelWrapperContext.layer_name_to_kvcache_index: VllmModelWrapperContext#layer_name_to_kvcache_index.
---
# Module: [`src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py)

## Classes
### <a id="VllmModelWrapperContext"></a>`VllmModelWrapperContext`
- def: [`src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py:23`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py#L23)
- signature: `class VllmModelWrapperContext:`
- members:
  - <a id="VllmModelWrapperContext.kv_cache_bundle"></a>`kv_cache_bundle` — [`L33`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py#L33) — documented in [vllm-model-patches](../../../../../concepts/vllm-model-patches.md)
  - <a id="VllmModelWrapperContext.kv_caches"></a>`kv_caches` — [`L27`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py#L27)
  - <a id="VllmModelWrapperContext.layer_name_to_kvcache_index"></a>`layer_name_to_kvcache_index` — [`L28`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py#L28)
  - <a id="VllmModelWrapperContext.mesh"></a>`mesh` — [`L26`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py#L26) — documented in [vllm-model-patches](../../../../../concepts/vllm-model-patches.md)
  - <a id="VllmModelWrapperContext.vllm_config"></a>`vllm_config` — [`L29`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py#L29) — documented in [vllm-model-patches](../../../../../concepts/vllm-model-patches.md)
- used by: [`_build_rpa_kernel`](../../layers/adapter/attention.md#PallasAttentionBackendImpl._build_rpa_kernel), [`forward`](../../layers/adapter/attention.md#PallasAttentionBackendImpl.forward), [`initialize_kernel`](../../layers/adapter/attention.md#PallasAttentionBackendImpl.initialize_kernel), [`_build_gdn_op`](../../layers/adapter/custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention._build_gdn_op), [`set_vllm_model_wrapper_context`](vllm_model_wrapper_context.md#set_vllm_model_wrapper_context), [`_build_pooled_pcp_gdn_op`](../../layers/adapter/custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention._build_pooled_pcp_gdn_op), [`_build_attn_op`](deepseek_v4/attention.md#VllmDeepseekV4MLAAttention._build_attn_op), [`_build_bundled_kernel`](../../layers/adapter/attention.md#PallasAttentionBackendImpl._build_bundled_kernel), [`_build_pooled_gdn_op`](../../layers/adapter/custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention._build_pooled_gdn_op), [`mla_attention_core_tpu`](../../layers/adapter/attention.md#PallasMLAttentionBackendImpl.mla_attention_core_tpu), [`get_vllm_model_wrapper_context`](vllm_model_wrapper_context.md#get_vllm_model_wrapper_context), [`get_pallas_op_mesh`](vllm_model_wrapper_context.md#get_pallas_op_mesh), [`kv_cache`](../../layers/adapter/custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention.kv_cache), [`_vllm_model_wrapper_context`](vllm_model_wrapper_context.md#_vllm_model_wrapper_context._vllm_model_wrapper_context), [`_pcp_streaming_enabled`](../../layers/adapter/custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention._pcp_streaming_enabled), [`sparse_mla_attention_core_tpu`](../../layers/adapter/attention.md#PallasMLAttentionBackendImpl.sparse_mla_attention_core_tpu)

## Functions
- <a id="get_pallas_op_mesh"></a>`get_pallas_op_mesh()` — [`L48`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py#L48) — The wrapper-context mesh to hand to ``pallas.jax_op(mesh=...)``. — documented in [custom-ops](../../../../../concepts/custom-ops.md)
- <a id="get_vllm_model_wrapper_context"></a>`get_vllm_model_wrapper_context()` — [`L39`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py#L39) — documented in [deepseek-v4-model](../../../../../concepts/deepseek-v4-model.md)
- <a id="set_vllm_model_wrapper_context"></a>`set_vllm_model_wrapper_context(*, kv_caches: list[torch.Tensor] | None = None, mesh: Mesh, layer_name_to_kvcache_index: dict[str, int] | None = None, vllm_config: object | None = None, kv_cache_bundle: torch.Tensor | None = None)` — [`L71`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py#L71) — documented in [speculative-decoding](../../../../../concepts/speculative-decoding.md)

## Module values
- <a id="_vllm_model_wrapper_context._vllm_model_wrapper_context"></a>`_vllm_model_wrapper_context` — [`L36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py#L36) — documented in [vllm-model-patches](../../../../../concepts/vllm-model-patches.md)

