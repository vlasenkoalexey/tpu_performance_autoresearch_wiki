---
title: 'Module: src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.quantization.mxfp4`/
symbols:
  VllmDeepseekV4Mxfp4MoEMethod.process_weights_after_loading: VllmDeepseekV4Mxfp4MoEMethod#process_weights_after_loading().
  VllmDeepseekV4Mxfp4MoEMethod._dequantize_and_pad: VllmDeepseekV4Mxfp4MoEMethod#_dequantize_and_pad().
  VllmMxfp4MoEMethod.process_weights_after_loading: VllmMxfp4MoEMethod#process_weights_after_loading().
  VllmMxfp4MoEMethod._forward_monolithic_tpu: VllmMxfp4MoEMethod#_forward_monolithic_tpu().
  logger: logger.
  VllmDeepseekV4Mxfp4MoEMethod._prebuild_w4a8: VllmDeepseekV4Mxfp4MoEMethod#_prebuild_w4a8().
  VllmMxfp4Config.get_quant_method: VllmMxfp4Config#get_quant_method().
  VllmDeepseekV4Mxfp4MoEMethod._forward_monolithic_tpu: VllmDeepseekV4Mxfp4MoEMethod#_forward_monolithic_tpu().
  _dequantize_mxfp4_packed_on_device: _dequantize_mxfp4_packed_on_device().
  REQUANTIZED_BLOCK_SIZE: REQUANTIZED_BLOCK_SIZE.
  VllmMxfp4MoEMethod: VllmMxfp4MoEMethod#
  VllmMxfp4MoEMethod._resolve_tpu_activation: VllmMxfp4MoEMethod#_resolve_tpu_activation().
  VllmDeepseekV4Mxfp4MoEMethod._requantize_native_fp4: VllmDeepseekV4Mxfp4MoEMethod#_requantize_native_fp4().
  VllmMxfp4MoEMethod.supports_internal_mk: VllmMxfp4MoEMethod#supports_internal_mk().
  VllmDeepseekV4Mxfp4MoEMethod.supports_internal_mk: VllmDeepseekV4Mxfp4MoEMethod#supports_internal_mk().
  VllmMxfp4Config: VllmMxfp4Config#
  VllmDeepseekV4Mxfp4MoEMethod: VllmDeepseekV4Mxfp4MoEMethod#
  VllmMxfp4MoEMethod._select_monolithic: VllmMxfp4MoEMethod#_select_monolithic().
  VllmMxfp4Config.get_name: VllmMxfp4Config#get_name().
  VllmMxfp4MoEMethod.apply_monolithic: VllmMxfp4MoEMethod#apply_monolithic.
  VllmDeepseekV4Mxfp4MoEMethod._resolve_tpu_activation: VllmDeepseekV4Mxfp4MoEMethod#_resolve_tpu_activation().
  _dequantize_mxfp4_packed_on_device.decode: _dequantize_mxfp4_packed_on_device().decode().
  _get_activation_str: _get_activation_str().
  VllmMxfp4MoEMethod.rhs_quant_dtype: VllmMxfp4MoEMethod#rhs_quant_dtype.
  VllmDeepseekV4Mxfp4MoEMethod._release_source_weights: VllmDeepseekV4Mxfp4MoEMethod#_release_source_weights().
  VllmMxfp4MoEMethod.is_k3_situ_aiter: VllmMxfp4MoEMethod#is_k3_situ_aiter.
  VllmMxfp4MoEMethod.is_monolithic: VllmMxfp4MoEMethod#is_monolithic().
  VllmMxfp4MoEMethod.__init__: VllmMxfp4MoEMethod#__init__().
  VllmMxfp4MoEMethod.mxfp4_backend: VllmMxfp4MoEMethod#mxfp4_backend.
  VllmDeepseekV4Mxfp4MoEMethod.rhs_quant_dtype: VllmDeepseekV4Mxfp4MoEMethod#rhs_quant_dtype.
  VllmDeepseekV4Mxfp4MoEMethod.create_weights: VllmDeepseekV4Mxfp4MoEMethod#create_weights().
---
# Module: [`src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py)

## Classes
### <a id="VllmDeepseekV4Mxfp4MoEMethod"></a>`VllmDeepseekV4Mxfp4MoEMethod`  ·  implements/extends VllmMxfp4MoEMethod
- def: [`src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py:372`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L372)
- doc: DeepSeek-V4 MXFP4 MoE quantization and weight loading method.
- signature: `class VllmDeepseekV4Mxfp4MoEMethod(VllmMxfp4MoEMethod):`
- members:
  - <a id="VllmDeepseekV4Mxfp4MoEMethod._dequantize_and_pad"></a>`_dequantize_and_pad(self, layer: TpuRoutedExperts)` — [`L486`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L486) — Dequantize staged shards, concatenate w13, and pad to strided block — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
  - <a id="VllmDeepseekV4Mxfp4MoEMethod._prebuild_w4a8"></a>`_prebuild_w4a8(self, layer: RoutedExperts, activation: str, w13_weight_padded: torch.Tensor, w2_weight_padded: torch.Tensor, orig_intermediate_size: int)` — [`L385`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L385) — Admit the fused EP layout before the weights are quantized to it.
  - <a id="VllmDeepseekV4Mxfp4MoEMethod._requantize_native_fp4"></a>`_requantize_native_fp4(self, w13_weight_padded: torch.Tensor, w2_weight_padded: torch.Tensor, orig_intermediate_size: int, device: torch.device, pack: bool = True)` — [`L583`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L583) — Quantize padded tensors to native FP4 K-major layout on TPU.
  - <a id="VllmDeepseekV4Mxfp4MoEMethod.create_weights"></a>`create_weights(self, layer: RoutedExperts, num_experts: int, hidden_size: int, intermediate_size_per_partition: int, params_dtype: torch.dtype, **extra_weight_attrs)` — [`L467`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L467)
  - <a id="VllmDeepseekV4Mxfp4MoEMethod.process_weights_after_loading"></a>`process_weights_after_loading(self, layer: torch.nn.Module)` — [`L620`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L620) — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
  - <a id="VllmDeepseekV4Mxfp4MoEMethod.supports_internal_mk"></a>`supports_internal_mk(self)` — [`L378`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L378)
  - <a id="VllmDeepseekV4Mxfp4MoEMethod.rhs_quant_dtype"></a>`rhs_quant_dtype` — [`L375`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L375)
- protocol/private: <a id="VllmDeepseekV4Mxfp4MoEMethod._forward_monolithic_tpu"></a>`_forward_monolithic_tpu`[`L730`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L730), <a id="VllmDeepseekV4Mxfp4MoEMethod._release_source_weights"></a>`_release_source_weights`[`L614`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L614), <a id="VllmDeepseekV4Mxfp4MoEMethod._resolve_tpu_activation"></a>`_resolve_tpu_activation`[`L458`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L458)
- uses (calls/refs, reference-scoped): [`synchronize_tensors`](../../../utils.md#synchronize_tensors), [`prebuild_fused_moe_ep`](../fused_moe_ep.md#prebuild_fused_moe_ep), [`enable_pipelined_collective_and_compute`](../pipelined_fused_moe.md#enable_pipelined_collective_and_compute), [`fused_moe_ep`](../fused_moe_ep.md#fused_moe_ep), [`_forward_monolithic_tpu`](mxfp4.md#VllmMxfp4MoEMethod._forward_monolithic_tpu), [`fused_moe_ep_supported`](../fused_moe_ep.md#fused_moe_ep_supported), [`fused_moe_ep_unsupported_reason`](../fused_moe_ep.md#fused_moe_ep_unsupported_reason), [`prebuild_fused_moe_kernel`](../fused_moe.md#prebuild_fused_moe_kernel), [`logger`](mxfp4.md#logger), [`TpuRoutedExperts`](configs.md#TpuRoutedExperts), [`dequantize_mxfp4_packed`](../../core/quantization.md#dequantize_mxfp4_packed), [`_set_tpu_activation`](../fused_moe.md#TpuMoEActivationMixin._set_tpu_activation), [`register_experts_start_buffer`](../moe_routing.md#register_experts_start_buffer), [`register_fused_scale_buffers`](../fused_moe_ep.md#register_fused_scale_buffers), [`REQUANTIZED_BLOCK_SIZE`](mxfp4.md#REQUANTIZED_BLOCK_SIZE), [`_dequantize_mxfp4_packed_on_device`](mxfp4.md#_dequantize_mxfp4_packed_on_device), [`register_score_bias_buffer`](../fused_moe_ep.md#register_score_bias_buffer), [`score_bias_operand`](../fused_moe_ep.md#score_bias_operand), [`FUSED_MOE_EP_OP_ATTR`](../fused_moe_ep.md#FUSED_MOE_EP_OP_ATTR), [`quantize_native_fp4_kmajor`](../fused_moe.md#quantize_native_fp4_kmajor), [`w13_weight`](configs.md#TpuRoutedExperts.w13_weight), [`VllmMxfp4MoEMethod`](mxfp4.md#VllmMxfp4MoEMethod), [`USE_MOE_FUSED_EP_KERNEL`](../../../envs.md#USE_MOE_FUSED_EP_KERNEL), [`_resolve_tpu_activation`](mxfp4.md#VllmMxfp4MoEMethod._resolve_tpu_activation), [`validate_linear_ep_placement`](../moe_routing.md#validate_linear_ep_placement), [`w13_weight_scale`](configs.md#TpuRoutedExperts.w13_weight_scale), [`w2_weight`](configs.md#TpuRoutedExperts.w2_weight), [`w2_weight_scale`](configs.md#TpuRoutedExperts.w2_weight_scale), [`MOE_FUSED_EP_ENABLE_W4A8`](../../../envs.md#MOE_FUSED_EP_ENABLE_W4A8), [`hash_topk_ids_operand`](../fused_moe_ep.md#hash_topk_ids_operand), [`VLLM_TPU_MXFP4_DEVICE_DEQUANT`](../../../envs.md#VLLM_TPU_MXFP4_DEVICE_DEQUANT)
- used by: [`get_quant_method`](deepseek_v4_fp8.md#VllmDeepseekV4Fp8Config.get_quant_method), [`process_weights_after_loading`](mxfp4.md#VllmMxfp4MoEMethod.process_weights_after_loading), [`_forward_monolithic_tpu`](mxfp4.md#VllmMxfp4MoEMethod._forward_monolithic_tpu), [`VllmMxfp4MoEMethod`](mxfp4.md#VllmMxfp4MoEMethod), [`_resolve_tpu_activation`](mxfp4.md#VllmMxfp4MoEMethod._resolve_tpu_activation), [`supports_internal_mk`](mxfp4.md#VllmMxfp4MoEMethod.supports_internal_mk)

### <a id="VllmMxfp4Config"></a>`VllmMxfp4Config`  ·  implements/extends VllmQuantConfig
- def: [`src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py:96`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L96)
- doc: TPU-specific MXFP4 quantization configuration.
- signature: `class VllmMxfp4Config(Mxfp4Config, VllmQuantConfig):`
- members:
  - <a id="VllmMxfp4Config.get_name"></a>`get_name(cls)` — [`L106`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L106) — Return the base quantization method name.
  - <a id="VllmMxfp4Config.get_quant_method"></a>`get_quant_method(self, layer: torch.nn.Module, prefix: str)` — [`L110`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L110) — Return the appropriate quantization method for a layer.
- uses (calls/refs, reference-scoped): [`VllmQuantConfig`](configs.md#VllmQuantConfig), [`get_moe_config`](configs.md#VllmQuantConfig.get_moe_config), [`logger`](mxfp4.md#logger), [`VllmUnquantizedLinearMethod`](unquantized.md#VllmUnquantizedLinearMethod), [`packed_modules_mapping`](configs.md#VllmQuantConfig.packed_modules_mapping), [`VllmMxfp4MoEMethod`](mxfp4.md#VllmMxfp4MoEMethod), [`MXFP4`](../../core/quant_methods.md#MXFP4)
- used by: [`get_tpu_quantization_config`](__init__.md#get_tpu_quantization_config), [`VllmQuantConfig`](configs.md#VllmQuantConfig)

### <a id="VllmMxfp4MoEMethod"></a>`VllmMxfp4MoEMethod`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py:205`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L205)
- members:
  - <a id="VllmMxfp4MoEMethod._forward_monolithic_tpu"></a>`_forward_monolithic_tpu(self, layer: RoutedExperts, x: torch.Tensor, router_logits: torch.Tensor, input_ids: torch.Tensor | None = None)` — [`L320`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L320) — Forward pass using GMM kernel. — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
  - <a id="VllmMxfp4MoEMethod.is_monolithic"></a>`is_monolithic(self)` — [`L222`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L222)
  - <a id="VllmMxfp4MoEMethod.process_weights_after_loading"></a>`process_weights_after_loading(self, layer: torch.nn.Module)` — [`L245`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L245) — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
  - <a id="VllmMxfp4MoEMethod.supports_internal_mk"></a>`supports_internal_mk(self)` — [`L226`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L226)
  - <a id="VllmMxfp4MoEMethod.apply_monolithic"></a>`apply_monolithic` — [`L235`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L235) — ---
  - <a id="VllmMxfp4MoEMethod.is_k3_situ_aiter"></a>`is_k3_situ_aiter` — [`L219`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L219)
  - <a id="VllmMxfp4MoEMethod.mxfp4_backend"></a>`mxfp4_backend` — [`L234`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L234)
  - <a id="VllmMxfp4MoEMethod.rhs_quant_dtype"></a>`rhs_quant_dtype` — [`L318`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L318)
- protocol/private: <a id="VllmMxfp4MoEMethod.__init__"></a>`__init__`[`L231`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L231), <a id="VllmMxfp4MoEMethod._resolve_tpu_activation"></a>`_resolve_tpu_activation`[`L240`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L240), <a id="VllmMxfp4MoEMethod._select_monolithic"></a>`_select_monolithic`[`L237`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L237)
- uses (calls/refs, reference-scoped): [`synchronize_tensors`](../../../utils.md#synchronize_tensors), [`process_weights_after_loading`](mxfp4.md#VllmDeepseekV4Mxfp4MoEMethod.process_weights_after_loading), [`pipelined_fused_moe_gmm`](../pipelined_fused_moe.md#pipelined_fused_moe_gmm), [`enable_pipelined_collective_and_compute`](../pipelined_fused_moe.md#enable_pipelined_collective_and_compute), [`fused_moe_gmm`](../fused_moe.md#fused_moe_gmm), [`prebuild_fused_moe_kernel`](../fused_moe.md#prebuild_fused_moe_kernel), [`logger`](mxfp4.md#logger), [`TpuMoEActivationMixin`](../fused_moe.md#TpuMoEActivationMixin), [`_forward_monolithic_tpu`](mxfp4.md#VllmDeepseekV4Mxfp4MoEMethod._forward_monolithic_tpu), [`route`](../moe_routing.md#route), [`dequantize_mxfp4_packed`](../../core/quantization.md#dequantize_mxfp4_packed), [`_set_tpu_activation`](../fused_moe.md#TpuMoEActivationMixin._set_tpu_activation), [`_tpu_activation_str`](../fused_moe.md#TpuMoEActivationMixin._tpu_activation_str), [`register_experts_start_buffer`](../moe_routing.md#register_experts_start_buffer), [`validate_linear_ep_placement`](../moe_routing.md#validate_linear_ep_placement), [`supports_internal_mk`](mxfp4.md#VllmDeepseekV4Mxfp4MoEMethod.supports_internal_mk), [`VllmDeepseekV4Mxfp4MoEMethod`](mxfp4.md#VllmDeepseekV4Mxfp4MoEMethod), [`_resolve_tpu_activation`](mxfp4.md#VllmDeepseekV4Mxfp4MoEMethod._resolve_tpu_activation), [`_get_activation_str`](mxfp4.md#_get_activation_str)
- used by: [`_forward_monolithic_tpu`](mxfp4.md#VllmDeepseekV4Mxfp4MoEMethod._forward_monolithic_tpu), [`get_quant_method`](mxfp4.md#VllmMxfp4Config.get_quant_method), [`_resolve_tpu_activation`](../fused_moe.md#TpuMoEActivationMixin._resolve_tpu_activation), [`VllmDeepseekV4Mxfp4MoEMethod`](mxfp4.md#VllmDeepseekV4Mxfp4MoEMethod), [`_resolve_tpu_activation`](mxfp4.md#VllmDeepseekV4Mxfp4MoEMethod._resolve_tpu_activation)

## Functions
- <a id="_dequantize_mxfp4_packed_on_device"></a>`_dequantize_mxfp4_packed_on_device(weight_packed: torch.Tensor, scale_u8: torch.Tensor, axis: int, out_dtype: torch.dtype)` — [`L166`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L166) — Dequantize packed FP4 weights and scales on their current device.
- <a id="_get_activation_str"></a>`_get_activation_str(activation)` — [`L200`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L200) — Convert MoEActivation enum or string to plain string.
- <a id="_dequantize_mxfp4_packed_on_device.decode"></a>`decode(nibble: torch.Tensor)` — [`L179`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L179)

## Module values
- <a id="REQUANTIZED_BLOCK_SIZE"></a>`REQUANTIZED_BLOCK_SIZE` — [`L365`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L365)
- <a id="logger"></a>`logger` — [`L92`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.py#L92)

