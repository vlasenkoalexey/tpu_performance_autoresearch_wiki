---
title: 'Module: src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.quantization.compressed_tensors.compressed_tensors`/
symbols:
  VllmCompressedTensorsConfig.get_quant_method: VllmCompressedTensorsConfig#get_quant_method().
  VllmCompressedTensorsConfig: VllmCompressedTensorsConfig#
  _build_fp8_linear_method: _build_fp8_linear_method().
  VllmCompressedTensorsConfig.get_scheme: VllmCompressedTensorsConfig#get_scheme().
  _build_fp8_config: _build_fp8_config().
  VllmCompressedTensorsConfig.set_configs: VllmCompressedTensorsConfig#set_configs().
  _raise_not_implemented: _raise_not_implemented().
  logger: logger.
  _is_weight_fp8: _is_weight_fp8().
  VllmCompressedTensorsConfig.get_name: VllmCompressedTensorsConfig#get_name().
  _is_int4_w4aN: _is_int4_w4aN().
---
# Module: [`src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors.py`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors.py)

## Classes
### <a id="VllmCompressedTensorsConfig"></a>`VllmCompressedTensorsConfig`  ·  implements/extends VllmQuantConfig
- def: [`src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors.py:129`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors.py#L129) — documented in [quantization-methods](../../../../../../../concepts/quantization-methods.md)
- signature: `class VllmCompressedTensorsConfig(CompressedTensorsConfig, VllmQuantConfig):`
- members:
  - <a id="VllmCompressedTensorsConfig.get_name"></a>`get_name(cls)` — [`L131`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors.py#L131)
  - <a id="VllmCompressedTensorsConfig.get_quant_method"></a>`get_quant_method(self, layer: torch.nn.Module, prefix: str)` — [`L202`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors.py#L202) — documented in [quantization-methods](../../../../../../../concepts/quantization-methods.md)
  - <a id="VllmCompressedTensorsConfig.get_scheme"></a>`get_scheme(self, layer: torch.nn.Module, layer_name: str | None = None)` — [`L143`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors.py#L143) — compressed-tensors supports non uniform in the following way:
  - <a id="VllmCompressedTensorsConfig.set_configs"></a>`set_configs(cls, vllm_config)` — [`L135`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors.py#L135)
- uses (calls/refs, reference-scoped): [`VllmQuantConfig`](../configs.md#VllmQuantConfig), [`get_quant_method`](../unquantized.md#VllmUnquantizedConfig.get_quant_method), [`get_moe_method`](compressed_tensors_moe/compressed_tensors_moe.md#VllmCompressedTensorsMoEMethod.get_moe_method), [`VllmFp8Config`](../fp8.md#VllmFp8Config), [`VllmUnquantizedConfig`](../unquantized.md#VllmUnquantizedConfig), [`get_moe_config`](../configs.md#VllmQuantConfig.get_moe_config), [`get_tpu_quant_method`](../../../core/quant_methods.md#get_tpu_quant_method), [`packed_modules_mapping`](../configs.md#VllmQuantConfig.packed_modules_mapping), [`_build_fp8_linear_method`](compressed_tensors.md#_build_fp8_linear_method), [`set_configs`](../configs.md#VllmQuantConfig.set_configs), [`COMPRESSED_TENSORS`](../../../core/quant_methods.md#COMPRESSED_TENSORS), [`_raise_not_implemented`](compressed_tensors.md#_raise_not_implemented), [`logger`](compressed_tensors.md#logger), [`VllmCompressedTensorsMoEMethod`](compressed_tensors_moe/compressed_tensors_moe.md#VllmCompressedTensorsMoEMethod), [`_is_weight_fp8`](compressed_tensors.md#_is_weight_fp8), [`scheme`](../configs.md#TpuLinear.scheme)
- used by: [`get_tpu_quantization_config`](../__init__.md#get_tpu_quantization_config), [`VllmQuantConfig`](../configs.md#VllmQuantConfig), [`get_moe_method`](compressed_tensors_moe/compressed_tensors_moe.md#VllmCompressedTensorsMoEMethod.get_moe_method)

## Functions
- <a id="_build_fp8_config"></a>`_build_fp8_config(weight_quant: QuantizationArgs, input_quant: QuantizationArgs | None)` — [`L86`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors.py#L86) — Adapt a matched compressed-tensors FP8 scheme into a VllmFp8Config.
- <a id="_build_fp8_linear_method"></a>`_build_fp8_linear_method(layer: LinearBase, weight_quant: QuantizationArgs, input_quant: QuantizationArgs | None)` — [`L112`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors.py#L112) — documented in [quantization-methods](../../../../../../../concepts/quantization-methods.md)
- <a id="_is_int4_w4aN"></a>`_is_int4_w4aN(weight_quant: QuantizationArgs | None)` — [`L71`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors.py#L71)
- <a id="_is_weight_fp8"></a>`_is_weight_fp8(weight_quant: QuantizationArgs | None)` — [`L63`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors.py#L63)
- <a id="_raise_not_implemented"></a>`_raise_not_implemented(scheme_class: str)` — [`L121`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors.py#L121)

## Module values
- <a id="logger"></a>`logger` — [`L60`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors.py#L60)

