---
title: 'Module: src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.quantization.compressed_tensors.compressed_tensors_moe.compressed_tensors_moe`/VllmCompressedTensorsMoEMethod#
symbols:
  VllmCompressedTensorsMoEMethod.get_moe_method: get_moe_method().
  VllmCompressedTensorsMoEMethod: ''
---
# Module: [`src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe.py`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe.py)

## Classes
### <a id="VllmCompressedTensorsMoEMethod"></a>`VllmCompressedTensorsMoEMethod`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe.py:43`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe.py#L43)
- doc: TPU dispatcher for Compressed Tensors MoE schemes.
- signature: `class VllmCompressedTensorsMoEMethod(CompressedTensorsMoEMethod):`
- members:
  - <a id="VllmCompressedTensorsMoEMethod.get_moe_method"></a>`get_moe_method(quant_config: VllmCompressedTensorsConfig, layer: torch.nn.Module, layer_name: str)` — [`L49`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe.py#L49) — documented in [quantization-methods](../../../../../../../../concepts/quantization-methods.md)
- uses (calls/refs, reference-scoped): [`get_moe_config`](../../configs.md#VllmQuantConfig.get_moe_config), [`VllmUnquantizedFusedMoEMethod`](../../unquantized.md#VllmUnquantizedFusedMoEMethod), [`VllmCompressedTensorsConfig`](../compressed_tensors.md#VllmCompressedTensorsConfig), [`VllmFp8MoEMethodTPU`](../../fp8.md#VllmFp8MoEMethodTPU), [`_build_fp8_config`](../compressed_tensors.md#_build_fp8_config), [`VllmCompressedTensorsW4ANMxfp4MoEMethod`](compressed_tensors_moe_w4an_mxfp4.md#VllmCompressedTensorsW4ANMxfp4MoEMethod), [`_is_weight_fp8`](../compressed_tensors.md#_is_weight_fp8), [`VllmCompressedTensorsW4A16MoEMethod`](compressed_tensors_moe_w4a16.md#VllmCompressedTensorsW4A16MoEMethod), [`_is_int4_w4aN`](../compressed_tensors.md#_is_int4_w4aN)
- used by: [`get_quant_method`](../compressed_tensors.md#VllmCompressedTensorsConfig.get_quant_method)

