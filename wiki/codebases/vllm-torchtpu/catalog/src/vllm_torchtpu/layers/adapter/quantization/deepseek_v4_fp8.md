---
title: 'Module: src/vllm_torchtpu/layers/adapter/quantization/deepseek_v4_fp8.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/quantization/deepseek_v4_fp8.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.quantization.deepseek_v4_fp8`/
symbols:
  VllmDeepseekV4Fp8Config.get_quant_method: VllmDeepseekV4Fp8Config#get_quant_method().
  logger: logger.
  VllmDeepseekV4Fp8Config: VllmDeepseekV4Fp8Config#
  VllmDeepseekV4Fp8Config.get_name: VllmDeepseekV4Fp8Config#get_name().
  VllmDeepseekV4Fp8Config.is_scale_e8m0: VllmDeepseekV4Fp8Config#is_scale_e8m0().
---
# Module: [`src/vllm_torchtpu/layers/adapter/quantization/deepseek_v4_fp8.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/deepseek_v4_fp8.py)

## Classes
### <a id="VllmDeepseekV4Fp8Config"></a>`VllmDeepseekV4Fp8Config`  ·  implements/extends VllmQuantConfig
- def: [`src/vllm_torchtpu/layers/adapter/quantization/deepseek_v4_fp8.py:46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/deepseek_v4_fp8.py#L46)
- doc: TPU quantization config for "deepseek_v4_fp8" format.
- signature: `class VllmDeepseekV4Fp8Config(DeepseekV4FP8Config, VllmQuantConfig):`
- members:
  - <a id="VllmDeepseekV4Fp8Config.get_name"></a>`get_name(cls)` — [`L70`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/deepseek_v4_fp8.py#L70)
  - <a id="VllmDeepseekV4Fp8Config.get_quant_method"></a>`get_quant_method(self, layer: torch.nn.Module, prefix: str)` — [`L73`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/deepseek_v4_fp8.py#L73) — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
  - <a id="VllmDeepseekV4Fp8Config.is_scale_e8m0"></a>`is_scale_e8m0(self)` — [`L57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/deepseek_v4_fp8.py#L57)
- uses (calls/refs, reference-scoped): [`VllmQuantConfig`](configs.md#VllmQuantConfig), [`get_moe_config`](configs.md#VllmQuantConfig.get_moe_config), [`VllmFp8LinearMethodTPU`](fp8.md#VllmFp8LinearMethodTPU), [`VllmUnquantizedFusedMoEMethod`](unquantized.md#VllmUnquantizedFusedMoEMethod), [`VllmFp8MoEMethodTPU`](fp8.md#VllmFp8MoEMethodTPU), [`VllmUnquantizedLinearMethod`](unquantized.md#VllmUnquantizedLinearMethod), [`get_linear_config`](configs.md#VllmQuantConfig.get_linear_config), [`packed_modules_mapping`](configs.md#VllmQuantConfig.packed_modules_mapping), [`DEEPSEEK_V4_FP8`](../../core/quant_methods.md#DEEPSEEK_V4_FP8), [`VllmDeepseekV4Mxfp4MoEMethod`](mxfp4.md#VllmDeepseekV4Mxfp4MoEMethod)
- used by: [`get_tpu_quantization_config`](__init__.md#get_tpu_quantization_config), [`VllmQuantConfig`](configs.md#VllmQuantConfig)

## Module values
- <a id="logger"></a>`logger` — [`L41`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/deepseek_v4_fp8.py#L41)

