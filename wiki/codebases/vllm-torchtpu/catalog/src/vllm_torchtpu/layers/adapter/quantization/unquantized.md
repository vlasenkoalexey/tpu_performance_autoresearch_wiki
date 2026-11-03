---
title: 'Module: src/vllm_torchtpu/layers/adapter/quantization/unquantized.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/quantization/unquantized.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.quantization.unquantized`/
symbols:
  VllmUnquantizedConfig.get_quant_method: VllmUnquantizedConfig#get_quant_method().
  VllmUnquantizedConfig: VllmUnquantizedConfig#
  VllmUnquantizedFusedMoEMethod.process_weights_after_loading: VllmUnquantizedFusedMoEMethod#process_weights_after_loading().
  VllmUnquantizedFusedMoEMethod._forward_monolithic_tpu: VllmUnquantizedFusedMoEMethod#_forward_monolithic_tpu().
  VllmUnquantizedFusedMoEMethod: VllmUnquantizedFusedMoEMethod#
  VllmUnquantizedLinearMethod: VllmUnquantizedLinearMethod#
  VllmUnquantizedLinearMethod.process_weights_after_loading: VllmUnquantizedLinearMethod#process_weights_after_loading().
  logger: logger.
  VllmUnquantizedFusedMoEMethod._select_monolithic: VllmUnquantizedFusedMoEMethod#_select_monolithic().
  VllmUnquantizedLinearMethod.apply: VllmUnquantizedLinearMethod#apply().
  VllmUnquantizedConfig.get_name: VllmUnquantizedConfig#get_name().
  VllmUnquantizedConfig.from_config: VllmUnquantizedConfig#from_config().
  VllmUnquantizedFusedMoEMethod.apply_monolithic: VllmUnquantizedFusedMoEMethod#apply_monolithic.
  VllmUnquantizedFusedMoEMethod.supports_internal_mk: VllmUnquantizedFusedMoEMethod#supports_internal_mk().
  VllmUnquantizedConfig.get_supported_act_dtypes: VllmUnquantizedConfig#get_supported_act_dtypes().
  VllmUnquantizedConfig.get_min_capability: VllmUnquantizedConfig#get_min_capability().
  VllmUnquantizedConfig.get_config_filenames: VllmUnquantizedConfig#get_config_filenames().
  VllmUnquantizedFusedMoEMethod.__init__: VllmUnquantizedFusedMoEMethod#__init__().
  VllmUnquantizedFusedMoEMethod.is_monolithic: VllmUnquantizedFusedMoEMethod#is_monolithic().
---
# Module: [`src/vllm_torchtpu/layers/adapter/quantization/unquantized.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py)

## Classes
### <a id="VllmUnquantizedConfig"></a>`VllmUnquantizedConfig`  ·  implements/extends VllmQuantConfig
- def: [`src/vllm_torchtpu/layers/adapter/quantization/unquantized.py:150`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L150) — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
- doc: TPU-specific configuration for unquantized models.
- signature: `class VllmUnquantizedConfig(QuantizationConfig, VllmQuantConfig):`
- members:
  - <a id="VllmUnquantizedConfig.from_config"></a>`from_config(cls, config: dict[str, Any])` — [`L177`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L177)
  - <a id="VllmUnquantizedConfig.get_config_filenames"></a>`get_config_filenames(cls)` — [`L173`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L173)
  - <a id="VllmUnquantizedConfig.get_min_capability"></a>`get_min_capability(cls)` — [`L169`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L169)
  - <a id="VllmUnquantizedConfig.get_name"></a>`get_name(cls)` — [`L161`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L161)
  - <a id="VllmUnquantizedConfig.get_quant_method"></a>`get_quant_method(self: VllmQuantConfig, layer: torch.nn.Module, prefix: str)` — [`L181`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L181) — Return the appropriate quantization method for a layer. — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
  - <a id="VllmUnquantizedConfig.get_supported_act_dtypes"></a>`get_supported_act_dtypes(cls)` — [`L165`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L165)
- uses (calls/refs, reference-scoped): [`VllmQuantConfig`](configs.md#VllmQuantConfig), [`VllmFp8Config`](fp8.md#VllmFp8Config), [`get_moe_config`](configs.md#VllmQuantConfig.get_moe_config), [`VllmFp8LinearMethodTPU`](fp8.md#VllmFp8LinearMethodTPU), [`VllmUnquantizedFusedMoEMethod`](unquantized.md#VllmUnquantizedFusedMoEMethod), [`get_tpu_quant_method`](../../core/quant_methods.md#get_tpu_quant_method), [`VllmUnquantizedLinearMethod`](unquantized.md#VllmUnquantizedLinearMethod), [`get_linear_config`](configs.md#VllmQuantConfig.get_linear_config), [`should_quantize_on_load`](configs.md#should_quantize_on_load), [`UNQUANTIZED`](../../core/quant_methods.md#UNQUANTIZED)
- used by: [`get_tpu_quantization_config`](__init__.md#get_tpu_quantization_config), [`VllmQuantConfig`](configs.md#VllmQuantConfig), [`get_quant_method`](compressed_tensors/compressed_tensors.md#VllmCompressedTensorsConfig.get_quant_method)

### <a id="VllmUnquantizedFusedMoEMethod"></a>`VllmUnquantizedFusedMoEMethod`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/unquantized.py:233`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L233)
- members:
  - <a id="VllmUnquantizedFusedMoEMethod._forward_monolithic_tpu"></a>`_forward_monolithic_tpu(self, layer: RoutedExperts, x: torch.Tensor, router_logits: torch.Tensor, input_ids: torch.Tensor | None = None)` — [`L346`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L346) — Forward pass using TPU-native GMM kernel.
  - <a id="VllmUnquantizedFusedMoEMethod.is_monolithic"></a>`is_monolithic(self)` — [`L249`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L249)
  - <a id="VllmUnquantizedFusedMoEMethod.process_weights_after_loading"></a>`process_weights_after_loading(self, layer: torch.nn.Module)` — [`L261`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L261)
  - <a id="VllmUnquantizedFusedMoEMethod.supports_internal_mk"></a>`supports_internal_mk(self)` — [`L253`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L253)
  - <a id="VllmUnquantizedFusedMoEMethod.apply_monolithic"></a>`apply_monolithic` — [`L246`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L246) — ---
- protocol/private: <a id="VllmUnquantizedFusedMoEMethod.__init__"></a>`__init__`[`L242`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L242), <a id="VllmUnquantizedFusedMoEMethod._select_monolithic"></a>`_select_monolithic`[`L258`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L258)
- uses (calls/refs, reference-scoped): [`synchronize_tensors`](../../../utils.md#synchronize_tensors), [`pipelined_fused_moe_gmm`](../pipelined_fused_moe.md#pipelined_fused_moe_gmm), [`enable_pipelined_collective_and_compute`](../pipelined_fused_moe.md#enable_pipelined_collective_and_compute), [`fused_moe_gmm`](../fused_moe.md#fused_moe_gmm), [`prebuild_fused_moe_kernel`](../fused_moe.md#prebuild_fused_moe_kernel), [`TpuMoEActivationMixin`](../fused_moe.md#TpuMoEActivationMixin), [`route`](../moe_routing.md#route), [`_set_tpu_activation`](../fused_moe.md#TpuMoEActivationMixin._set_tpu_activation), [`_tpu_activation_str`](../fused_moe.md#TpuMoEActivationMixin._tpu_activation_str), [`register_experts_start_buffer`](../moe_routing.md#register_experts_start_buffer), [`validate_linear_ep_placement`](../moe_routing.md#validate_linear_ep_placement), [`logger`](unquantized.md#logger)
- used by: [`get_quant_method`](unquantized.md#VllmUnquantizedConfig.get_quant_method), [`get_moe_method`](compressed_tensors/compressed_tensors_moe/compressed_tensors_moe.md#VllmCompressedTensorsMoEMethod.get_moe_method), [`get_quant_method`](deepseek_v4_fp8.md#VllmDeepseekV4Fp8Config.get_quant_method), [`_get_checkpoint_quant_method`](fp8.md#VllmFp8Config._get_checkpoint_quant_method), [`_get_checkpoint_quant_method`](nvfp4.md#VllmNvfp4Config._get_checkpoint_quant_method), [`create_weights`](fp8.md#VllmFp8MoEMethodTPU.create_weights)

### <a id="VllmUnquantizedLinearMethod"></a>`VllmUnquantizedLinearMethod`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/unquantized.py:88`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L88)
- doc: Dense linear on the canonical (k, n) weight layout.
- signature: `class VllmUnquantizedLinearMethod(UnquantizedLinearMethod):`
- members:
  - <a id="VllmUnquantizedLinearMethod.apply"></a>`apply(self, layer: torch.nn.Module, x: torch.Tensor, bias: torch.Tensor | None = None)` — [`L124`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L124)
  - <a id="VllmUnquantizedLinearMethod.process_weights_after_loading"></a>`process_weights_after_loading(self, layer: torch.nn.Module)` — [`L104`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L104)
- uses (calls/refs, reference-scoped): [`synchronize_tensors`](../../../utils.md#synchronize_tensors), [`WEIGHT_FLIPPED_ATTR`](../linear_common.md#WEIGHT_FLIPPED_ATTR), [`KEEP_VLLM_LAYOUT_ATTR`](../linear_common.md#KEEP_VLLM_LAYOUT_ATTR)
- used by: [`get_quant_method`](unquantized.md#VllmUnquantizedConfig.get_quant_method), [`get_quant_method`](deepseek_v4_fp8.md#VllmDeepseekV4Fp8Config.get_quant_method), [`_get_checkpoint_quant_method`](fp8.md#VllmFp8Config._get_checkpoint_quant_method), [`_get_checkpoint_quant_method`](nvfp4.md#VllmNvfp4Config._get_checkpoint_quant_method), [`get_quant_method`](mxfp4.md#VllmMxfp4Config.get_quant_method)

## Module values
- <a id="logger"></a>`logger` — [`L85`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/unquantized.py#L85)

