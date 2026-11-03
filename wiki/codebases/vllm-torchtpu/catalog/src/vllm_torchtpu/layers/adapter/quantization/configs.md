---
title: 'Module: src/vllm_torchtpu/layers/adapter/quantization/configs.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/quantization/configs.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.quantization.configs`/
symbols:
  VllmQuantConfig: VllmQuantConfig#
  VllmQuantConfig.get_moe_config: VllmQuantConfig#get_moe_config().
  TpuRoutedExperts: TpuRoutedExperts#
  VllmQuantConfig.get_linear_config: VllmQuantConfig#get_linear_config().
  VllmQuantConfig.packed_modules_mapping: VllmQuantConfig#packed_modules_mapping.
  TpuRoutedExperts.w13_weight: TpuRoutedExperts#w13_weight.
  VllmQuantLinearConfig: VllmQuantLinearConfig#
  should_quantize_on_load: should_quantize_on_load().
  VllmQuantConfig.online_fp8_policy: VllmQuantConfig#online_fp8_policy.
  TpuLinear: TpuLinear#
  TpuRoutedExperts.w2_weight: TpuRoutedExperts#w2_weight.
  TpuRoutedExperts.w13_weight_scale: TpuRoutedExperts#w13_weight_scale.
  VllmQuantConfig.set_configs: VllmQuantConfig#set_configs().
  TpuRoutedExperts.w2_weight_scale: TpuRoutedExperts#w2_weight_scale.
  VllmQuantConfig.vllm_config: VllmQuantConfig#vllm_config.
  VllmQuantLinearConfig.enable_quantized_matmul_kernel: VllmQuantLinearConfig#enable_quantized_matmul_kernel.
  VllmQuantLinearConfig.requant_block_size: VllmQuantLinearConfig#requant_block_size.
  VllmQuantLinearConfig.requant_weight_dtype: VllmQuantLinearConfig#requant_weight_dtype.
  VllmQuantLinearConfig.w8a16_max_rows: VllmQuantLinearConfig#w8a16_max_rows.
  logger: logger.
  TpuLinear.weight: TpuLinear#weight.
  TpuLinear.weight_scale: TpuLinear#weight_scale.
  VllmQuantConfig.get_name: VllmQuantConfig#get_name().
  TpuRoutedExperts.w13_weight_packed: TpuRoutedExperts#w13_weight_packed.
  TpuRoutedExperts.w2_weight_packed: TpuRoutedExperts#w2_weight_packed.
  TpuLinear.weight_scale_inv: TpuLinear#weight_scale_inv.
  TpuLinear.logical_widths: TpuLinear#logical_widths.
  TpuLinear.weight_block_size: TpuLinear#weight_block_size.
  TpuLinear.scheme: TpuLinear#scheme.
  TpuRoutedExperts.w13_weight_scale_inv: TpuRoutedExperts#w13_weight_scale_inv.
  TpuRoutedExperts.w2_weight_scale_inv: TpuRoutedExperts#w2_weight_scale_inv.
  TpuRoutedExperts.w13_weight_scale_2: TpuRoutedExperts#w13_weight_scale_2.
  TpuRoutedExperts.w2_weight_scale_2: TpuRoutedExperts#w2_weight_scale_2.
  TpuRoutedExperts.w13_bias: TpuRoutedExperts#w13_bias.
  TpuRoutedExperts.w2_bias: TpuRoutedExperts#w2_bias.
  TpuRoutedExperts.num_groups_w13: TpuRoutedExperts#num_groups_w13.
  TpuRoutedExperts.num_groups_w2: TpuRoutedExperts#num_groups_w2.
  TpuRoutedExperts._experts_start: TpuRoutedExperts#_experts_start.
  TpuRoutedExperts._tpu_fused_w13_scale: TpuRoutedExperts#_tpu_fused_w13_scale.
  TpuRoutedExperts._tpu_fused_w2_scale: TpuRoutedExperts#_tpu_fused_w2_scale.
  TpuRoutedExperts._rhs_quant_dtype: TpuRoutedExperts#_rhs_quant_dtype.
  TpuLinear.weight_scale_2: TpuLinear#weight_scale_2.
  TpuLinear._tpu_online_fp8_processed: TpuLinear#_tpu_online_fp8_processed.
  VllmQuantLinearConfig.__init__: VllmQuantLinearConfig#__init__().
  VllmQuantLinearConfig.vllm_config: VllmQuantLinearConfig#vllm_config.
  VllmQuantLinearConfig.output_sizes: VllmQuantLinearConfig#output_sizes.
  VllmQuantConfig.mesh: VllmQuantConfig#mesh().
---
# Module: [`src/vllm_torchtpu/layers/adapter/quantization/configs.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py)

## Classes
### <a id="TpuLinear"></a>`TpuLinear`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/configs.py:61`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L61)
- doc: Typing-only view of a LinearBase layer with the parameters and
- signature: `class TpuLinear(LinearBase):`
- members:
  - <a id="TpuLinear.logical_widths"></a>`logical_widths` — [`L69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L69)
  - <a id="TpuLinear.scheme"></a>`scheme` — [`L71`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L71)
  - <a id="TpuLinear.weight"></a>`weight` — [`L65`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L65)
  - <a id="TpuLinear.weight_block_size"></a>`weight_block_size` — [`L70`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L70)
  - <a id="TpuLinear.weight_scale"></a>`weight_scale` — [`L66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L66)
  - <a id="TpuLinear.weight_scale_2"></a>`weight_scale_2` — [`L68`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L68)
  - <a id="TpuLinear.weight_scale_inv"></a>`weight_scale_inv` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L67)
- protocol/private: <a id="TpuLinear._tpu_online_fp8_processed"></a>`_tpu_online_fp8_processed`[`L72`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L72)
- used by: [`validate_online_fp8`](online_fp8.md#validate_online_fp8), [`_process_fp8_linear_weights`](fp8.md#_process_fp8_linear_weights), [`get_quant_method`](compressed_tensors/compressed_tensors.md#VllmCompressedTensorsConfig.get_quant_method)

### <a id="TpuRoutedExperts"></a>`TpuRoutedExperts`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/configs.py:38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L38)
- doc: Typing-only view of a RoutedExperts layer with the parameters and
- signature: `class TpuRoutedExperts(RoutedExperts):`
- members:
  - <a id="TpuRoutedExperts.num_groups_w13"></a>`num_groups_w13` — [`L54`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L54)
  - <a id="TpuRoutedExperts.num_groups_w2"></a>`num_groups_w2` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L55)
  - <a id="TpuRoutedExperts.w13_bias"></a>`w13_bias` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L52)
  - <a id="TpuRoutedExperts.w13_weight"></a>`w13_weight` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L42)
  - <a id="TpuRoutedExperts.w13_weight_packed"></a>`w13_weight_packed` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L50)
  - <a id="TpuRoutedExperts.w13_weight_scale"></a>`w13_weight_scale` — [`L44`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L44)
  - <a id="TpuRoutedExperts.w13_weight_scale_2"></a>`w13_weight_scale_2` — [`L48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L48)
  - <a id="TpuRoutedExperts.w13_weight_scale_inv"></a>`w13_weight_scale_inv` — [`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L46)
  - <a id="TpuRoutedExperts.w2_bias"></a>`w2_bias` — [`L53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L53)
  - <a id="TpuRoutedExperts.w2_weight"></a>`w2_weight` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L43)
  - <a id="TpuRoutedExperts.w2_weight_packed"></a>`w2_weight_packed` — [`L51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L51)
  - <a id="TpuRoutedExperts.w2_weight_scale"></a>`w2_weight_scale` — [`L45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L45)
  - <a id="TpuRoutedExperts.w2_weight_scale_2"></a>`w2_weight_scale_2` — [`L49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L49)
  - <a id="TpuRoutedExperts.w2_weight_scale_inv"></a>`w2_weight_scale_inv` — [`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L47)
- protocol/private: <a id="TpuRoutedExperts._experts_start"></a>`_experts_start`[`L56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L56), <a id="TpuRoutedExperts._rhs_quant_dtype"></a>`_rhs_quant_dtype`[`L59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L59), <a id="TpuRoutedExperts._tpu_fused_w13_scale"></a>`_tpu_fused_w13_scale`[`L57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L57), <a id="TpuRoutedExperts._tpu_fused_w2_scale"></a>`_tpu_fused_w2_scale`[`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L58)
- used by: [`_dequantize_and_pad`](mxfp4.md#VllmDeepseekV4Mxfp4MoEMethod._dequantize_and_pad), [`_process_fp8_moe_weights`](fp8.md#_process_fp8_moe_weights), [`_initialize_dummy_quantized_weights`](compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4an_mxfp4.md#VllmCompressedTensorsW4ANMxfp4MoEMethod._initialize_dummy_quantized_weights), [`_quantize_bf16_moe_weights`](fp8.md#_quantize_bf16_moe_weights), [`_neutralize_padded_scales`](compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4an_mxfp4.md#VllmCompressedTensorsW4ANMxfp4MoEMethod._neutralize_padded_scales)

### <a id="VllmQuantConfig"></a>`VllmQuantConfig`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/configs.py:110`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L110) — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
- doc: Base class for all TPU quantization configurations.
- signature: `class VllmQuantConfig:`
- members:
  - <a id="VllmQuantConfig.get_linear_config"></a>`get_linear_config(self, layer: LinearBase)` — [`L153`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L153) — Get configuration for a linear layer.
  - <a id="VllmQuantConfig.get_moe_config"></a>`get_moe_config(self, layer: RoutedExperts)` — [`L166`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L166) — Get configuration for a MoE layer.
  - <a id="VllmQuantConfig.get_name"></a>`get_name(cls)` — [`L145`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L145) — Return the name of this quantization method.
  - <a id="VllmQuantConfig.mesh"></a>`mesh(self)` — [`L184`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L184)
  - <a id="VllmQuantConfig.set_configs"></a>`set_configs(cls, vllm_config: VllmConfig)` — [`L133`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L133) — Set the shared configuration for this quantization class.
  - <a id="VllmQuantConfig.online_fp8_policy"></a>`online_fp8_policy` — [`L124`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L124) — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
  - <a id="VllmQuantConfig.packed_modules_mapping"></a>`packed_modules_mapping` — [`L130`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L130) — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
  - <a id="VllmQuantConfig.vllm_config"></a>`vllm_config` — [`L127`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L127)
- uses (calls/refs, reference-scoped): [`VllmFp8Config`](fp8.md#VllmFp8Config), [`VllmUnquantizedConfig`](unquantized.md#VllmUnquantizedConfig), [`VllmNvfp4Config`](nvfp4.md#VllmNvfp4Config), [`VllmCompressedTensorsConfig`](compressed_tensors/compressed_tensors.md#VllmCompressedTensorsConfig), [`VllmQuantLinearConfig`](configs.md#VllmQuantLinearConfig), [`OnlineFp8Policy`](online_fp8.md#OnlineFp8Policy), [`VllmDeepseekV4Fp8Config`](deepseek_v4_fp8.md#VllmDeepseekV4Fp8Config), [`VllmMxfp4Config`](mxfp4.md#VllmMxfp4Config)
- used by: [`get_tpu_quantization_config`](__init__.md#get_tpu_quantization_config), [`validate_online_fp8`](online_fp8.md#validate_online_fp8), [`resolve_online_fp8`](fp8.md#resolve_online_fp8), [`get_quant_method`](compressed_tensors/compressed_tensors.md#VllmCompressedTensorsConfig.get_quant_method), [`get_quant_method`](unquantized.md#VllmUnquantizedConfig.get_quant_method), [`get_moe_method`](compressed_tensors/compressed_tensors_moe/compressed_tensors_moe.md#VllmCompressedTensorsMoEMethod.get_moe_method), [`get_quant_method`](deepseek_v4_fp8.md#VllmDeepseekV4Fp8Config.get_quant_method), [`attach_online_fp8`](online_fp8.md#attach_online_fp8), [`VllmFp8Config`](fp8.md#VllmFp8Config), [`_get_checkpoint_quant_method`](fp8.md#VllmFp8Config._get_checkpoint_quant_method), [`_get_checkpoint_quant_method`](nvfp4.md#VllmNvfp4Config._get_checkpoint_quant_method), [`VllmUnquantizedConfig`](unquantized.md#VllmUnquantizedConfig), [`VllmNvfp4Config`](nvfp4.md#VllmNvfp4Config), [`get_quant_method`](mxfp4.md#VllmMxfp4Config.get_quant_method), [`VllmCompressedTensorsConfig`](compressed_tensors/compressed_tensors.md#VllmCompressedTensorsConfig), [`map_online_fp8`](online_fp8.md#map_online_fp8), [`_build_fp8_linear_method`](compressed_tensors/compressed_tensors.md#_build_fp8_linear_method), [`get_scheme`](compressed_tensors/compressed_tensors.md#VllmCompressedTensorsConfig.get_scheme), [`set_configs`](compressed_tensors/compressed_tensors.md#VllmCompressedTensorsConfig.set_configs), [`VllmDeepseekV4Fp8Config`](deepseek_v4_fp8.md#VllmDeepseekV4Fp8Config), [`VllmMxfp4Config`](mxfp4.md#VllmMxfp4Config)

### <a id="VllmQuantLinearConfig"></a>`VllmQuantLinearConfig`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/configs.py:85`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L85)
- doc: Configuration for quantized linear layers on TPU.
- signature: `class VllmQuantLinearConfig:`
- members:
  - <a id="VllmQuantLinearConfig.enable_quantized_matmul_kernel"></a>`enable_quantized_matmul_kernel` — [`L100`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L100)
  - <a id="VllmQuantLinearConfig.output_sizes"></a>`output_sizes` — [`L99`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L99)
  - <a id="VllmQuantLinearConfig.requant_block_size"></a>`requant_block_size` — [`L101`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L101)
  - <a id="VllmQuantLinearConfig.requant_weight_dtype"></a>`requant_weight_dtype` — [`L102`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L102)
  - <a id="VllmQuantLinearConfig.vllm_config"></a>`vllm_config` — [`L98`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L98)
  - <a id="VllmQuantLinearConfig.w8a16_max_rows"></a>`w8a16_max_rows` — [`L103`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L103)
- protocol/private: <a id="VllmQuantLinearConfig.__init__"></a>`__init__`[`L92`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L92)
- uses (calls/refs, reference-scoped): [`ENABLE_QUANTIZED_MATMUL_KERNEL`](../../../envs.md#ENABLE_QUANTIZED_MATMUL_KERNEL), [`REQUANTIZE_BLOCK_SIZE`](../../../envs.md#REQUANTIZE_BLOCK_SIZE), [`REQUANTIZE_WEIGHT_DTYPE`](../../../envs.md#REQUANTIZE_WEIGHT_DTYPE), [`TPU_FP8_LINEAR_W8A16_MAX_ROWS`](../../../envs.md#TPU_FP8_LINEAR_W8A16_MAX_ROWS)
- used by: [`_process_fp8_linear_weights`](fp8.md#_process_fp8_linear_weights), [`_get_linear_quant_config`](fp8.md#_get_linear_quant_config), [`get_linear_config`](configs.md#VllmQuantConfig.get_linear_config), [`w8a16_max_rows`](fp8.md#VllmFp8LinearMethodTPU.w8a16_max_rows), [`__init__`](nvfp4.md#VllmNvfp4LinearMethod.__init__), [`__init__`](fp8.md#VllmFp8LinearMethodTPU.__init__)

## Functions
- <a id="should_quantize_on_load"></a>`should_quantize_on_load(prefix: str)` — [`L78`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L78) — Return True if prefix matches any dot-bounded pattern in — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)

## Module values
- <a id="logger"></a>`logger` — [`L75`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/configs.py#L75)

