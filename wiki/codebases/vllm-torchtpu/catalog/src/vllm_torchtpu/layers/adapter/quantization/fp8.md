---
title: 'Module: src/vllm_torchtpu/layers/adapter/quantization/fp8.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/quantization/fp8.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.quantization.fp8`/
symbols:
  VllmFp8LinearMethodTPU.process_weights_after_loading: VllmFp8LinearMethodTPU#process_weights_after_loading().
  VllmFp8MoEMethodTPU.process_weights_after_loading: VllmFp8MoEMethodTPU#process_weights_after_loading().
  VllmFp8MoEMethodTPU.apply_monolithic: VllmFp8MoEMethodTPU#apply_monolithic().
  _process_fp8_linear_weights: _process_fp8_linear_weights().
  _get_linear_quant_config: _get_linear_quant_config().
  resolve_online_fp8: resolve_online_fp8().
  _process_fp8_moe_weights: _process_fp8_moe_weights().
  VllmFp8Config: VllmFp8Config#
  VllmFp8Config._get_checkpoint_quant_method: VllmFp8Config#_get_checkpoint_quant_method().
  VllmFp8LinearMethodTPU.create_weights: VllmFp8LinearMethodTPU#create_weights().
  _quantize_bf16_moe_weights: _quantize_bf16_moe_weights().
  _wrap_block_scale_weight_loader._wrapped: _wrap_block_scale_weight_loader()._wrapped().
  VllmFp8LinearMethodTPU: VllmFp8LinearMethodTPU#
  VllmFp8MoEMethodTPU.maybe_roundup_sizes: VllmFp8MoEMethodTPU#maybe_roundup_sizes().
  _get_moe_quant_config: _get_moe_quant_config().
  _requantize_expert_chunks: _requantize_expert_chunks().
  VllmFp8MoEMethodTPU: VllmFp8MoEMethodTPU#
  VllmFp8MoEMethodTPU.supports_internal_mk: VllmFp8MoEMethodTPU#supports_internal_mk().
  VllmFp8MoEMethodTPU.create_weights: VllmFp8MoEMethodTPU#create_weights().
  BlockQuantScaleParameterTPU._maybe_refine: BlockQuantScaleParameterTPU#_maybe_refine().
  VllmFp8LinearMethodTPU._linear_quant_config: VllmFp8LinearMethodTPU#_linear_quant_config.
  VllmFp8MoEMethodTPU.weight_scale_name: VllmFp8MoEMethodTPU#weight_scale_name.
  _quantize_and_format_single_moe_weight: _quantize_and_format_single_moe_weight().
  _MOE_REQUANT_WEIGHT_DTYPES: _MOE_REQUANT_WEIGHT_DTYPES.
  VllmFp8LinearMethodTPU.apply: VllmFp8LinearMethodTPU#apply().
  VllmFp8MoEMethodTPU.weight_block_size: VllmFp8MoEMethodTPU#weight_block_size.
  VllmFp8LinearMethodTPU.w8a16_max_rows: VllmFp8LinearMethodTPU#w8a16_max_rows.
  VllmFp8LinearMethodTPU.online_fp8: VllmFp8LinearMethodTPU#online_fp8.
  logger: logger.
  _process_fp8_moe_weights.dequantize_w13: _process_fp8_moe_weights().dequantize_w13().
  VllmFp8MoEMethodTPU.block_quant: VllmFp8MoEMethodTPU#block_quant.
  VllmFp8LinearMethodTPU.online_fp8_policy: VllmFp8LinearMethodTPU#online_fp8_policy.
  VllmFp8Config.get_quant_method: VllmFp8Config#get_quant_method().
  VllmFp8LinearMethodTPU.weight_block_size: VllmFp8LinearMethodTPU#weight_block_size.
  VllmFp8LinearMethodTPU.block_quant: VllmFp8LinearMethodTPU#block_quant.
  VllmFp8MoEMethodTPU._use_adaptive_fused_moe: VllmFp8MoEMethodTPU#_use_adaptive_fused_moe.
  VllmFp8MoEMethodTPU.quant_config: VllmFp8MoEMethodTPU#quant_config.
  VllmFp8MoEMethodTPU.moe_block_shape: VllmFp8MoEMethodTPU#moe_block_shape.
  _wrap_block_scale_weight_loader: _wrap_block_scale_weight_loader().
  BlockQuantScaleParameterTPU: BlockQuantScaleParameterTPU#
  BlockQuantScaleParameterTPU.refine_n: BlockQuantScaleParameterTPU#refine_n().
  BlockQuantScaleParameterTPU.refine_k: BlockQuantScaleParameterTPU#refine_k().
  VllmFp8LinearMethodTPU.quant_config: VllmFp8LinearMethodTPU#quant_config.
  VllmFp8LinearMethodTPU.linear_config: VllmFp8LinearMethodTPU#linear_config.
  _quantize_and_format_moe_weights: _quantize_and_format_moe_weights().
  VllmFp8Config.get_name: VllmFp8Config#get_name().
  VllmFp8Config.from_config: VllmFp8Config#from_config().
  VllmFp8Config.apply_vllm_mapper: VllmFp8Config#apply_vllm_mapper().
  BlockQuantScaleParameterTPU.load_column_parallel_weight: BlockQuantScaleParameterTPU#load_column_parallel_weight().
  BlockQuantScaleParameterTPU.load_merged_column_weight: BlockQuantScaleParameterTPU#load_merged_column_weight().
  BlockQuantScaleParameterTPU.load_qkv_weight: BlockQuantScaleParameterTPU#load_qkv_weight().
  BlockQuantScaleParameterTPU.load_row_parallel_weight: BlockQuantScaleParameterTPU#load_row_parallel_weight().
  VllmFp8LinearMethodTPU.__init__: VllmFp8LinearMethodTPU#__init__().
  VllmFp8LinearMethodTPU.tie_weights: VllmFp8LinearMethodTPU#tie_weights().
  LinearQuantConfig: LinearQuantConfig.
  _format_linear_scale_for_runtime: _format_linear_scale_for_runtime().
  _quantize_bf16_moe_weights.to_fp32: _quantize_bf16_moe_weights().to_fp32().
  BlockQuantScaleParameterTPU._pre_refined: BlockQuantScaleParameterTPU#_pre_refined.
  _dequantize_fp8_linear: _dequantize_fp8_linear().
  _REQUANT_CHUNK_BYTES: _REQUANT_CHUNK_BYTES.
  VllmFp8Config.is_channel_quant: VllmFp8Config#is_channel_quant.
  VllmFp8MoEMethodTPU._adaptive_fused_moe_op: VllmFp8MoEMethodTPU#_adaptive_fused_moe_op.
  VllmFp8MoEMethodTPU.weight_scale_refine: VllmFp8MoEMethodTPU#weight_scale_refine.
  ChannelQuantScaleParameterTPU: ChannelQuantScaleParameterTPU#
  VllmFp8LinearMethodTPU.prefix: VllmFp8LinearMethodTPU#prefix.
  VllmFp8Config.__init__: VllmFp8Config#__init__().
  VllmFp8Config.is_checkpoint_fp8_serialized: VllmFp8Config#is_checkpoint_fp8_serialized.
  VllmFp8MoEMethodTPU.__init__: VllmFp8MoEMethodTPU#__init__().
  VllmFp8MoEMethodTPU.fp8_backend: VllmFp8MoEMethodTPU#fp8_backend.
  VllmFp8MoEMethodTPU.is_monolithic: VllmFp8MoEMethodTPU#is_monolithic().
  ChannelQuantScaleParameterTPU.load_column_parallel_weight: ChannelQuantScaleParameterTPU#load_column_parallel_weight().
  ChannelQuantScaleParameterTPU.load_merged_column_weight: ChannelQuantScaleParameterTPU#load_merged_column_weight().
  ChannelQuantScaleParameterTPU.load_qkv_weight: ChannelQuantScaleParameterTPU#load_qkv_weight().
  ChannelQuantScaleParameterTPU.load_row_parallel_weight: ChannelQuantScaleParameterTPU#load_row_parallel_weight().
  BlockQuantScaleParameterTPU.__init__: BlockQuantScaleParameterTPU#__init__().
  BlockQuantScaleParameterTPU._refine_n: BlockQuantScaleParameterTPU#_refine_n.
  BlockQuantScaleParameterTPU._refine_k: BlockQuantScaleParameterTPU#_refine_k.
  VllmFp8LinearMethodTPU.act_q_static: VllmFp8LinearMethodTPU#act_q_static.
  VllmFp8LinearMethodTPU.use_marlin: VllmFp8LinearMethodTPU#use_marlin.
  VllmFp8LinearMethodTPU.use_deep_gemm: VllmFp8LinearMethodTPU#use_deep_gemm.
  VllmFp8LinearMethodTPU.cutlass_block_fp8_supported: VllmFp8LinearMethodTPU#cutlass_block_fp8_supported.
  VllmFp8LinearMethodTPU.is_scale_e8m0: VllmFp8LinearMethodTPU#is_scale_e8m0.
  VllmFp8LinearMethodTPU.activation_quant_key: VllmFp8LinearMethodTPU#activation_quant_key.
  VllmFp8LinearMethodTPU.weight_quant_key: VllmFp8LinearMethodTPU#weight_quant_key.
  VllmFp8LinearMethodTPU.input_dtype: VllmFp8LinearMethodTPU#input_dtype.
  VllmFp8LinearMethodTPU.out_dtype: VllmFp8LinearMethodTPU#out_dtype.
  VllmFp8LinearMethodTPU.embedding: VllmFp8LinearMethodTPU#embedding().
---
# Module: [`src/vllm_torchtpu/layers/adapter/quantization/fp8.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py)

## Classes
### <a id="BlockQuantScaleParameterTPU"></a>`BlockQuantScaleParameterTPU`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/fp8.py:1248`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1248)
- doc: Block-quantized scale parameter that refines checkpoint block scales when
- signature: `class BlockQuantScaleParameterTPU(BlockQuantScaleParameter):`
- members:
  - <a id="BlockQuantScaleParameterTPU.load_column_parallel_weight"></a>`load_column_parallel_weight(self, loaded_weight: torch.Tensor)` — [`L1294`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1294)
  - <a id="BlockQuantScaleParameterTPU.load_merged_column_weight"></a>`load_merged_column_weight(self, loaded_weight: torch.Tensor, **kwargs)` — [`L1298`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1298)
  - <a id="BlockQuantScaleParameterTPU.load_qkv_weight"></a>`load_qkv_weight(self, loaded_weight: torch.Tensor, **kwargs)` — [`L1302`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1302)
  - <a id="BlockQuantScaleParameterTPU.load_row_parallel_weight"></a>`load_row_parallel_weight(self, loaded_weight: torch.Tensor, **kwargs)` — [`L1306`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1306)
  - <a id="BlockQuantScaleParameterTPU.refine_k"></a>`refine_k(self)` — [`L1278`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1278)
  - <a id="BlockQuantScaleParameterTPU.refine_n"></a>`refine_n(self)` — [`L1274`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1274)
- protocol/private: <a id="BlockQuantScaleParameterTPU.__init__"></a>`__init__`[`L1260`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1260), <a id="BlockQuantScaleParameterTPU._maybe_refine"></a>`_maybe_refine`[`L1281`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1281), <a id="BlockQuantScaleParameterTPU._pre_refined"></a>`_pre_refined`[`L1271`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1271), <a id="BlockQuantScaleParameterTPU._refine_k"></a>`_refine_k`[`L1270`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1270), <a id="BlockQuantScaleParameterTPU._refine_n"></a>`_refine_n`[`L1269`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1269)
- used by: [`create_weights`](fp8.md#VllmFp8LinearMethodTPU.create_weights), [`_wrapped`](fp8.md#_wrap_block_scale_weight_loader._wrapped)

### <a id="ChannelQuantScaleParameterTPU"></a>`ChannelQuantScaleParameterTPU`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/fp8.py:1225`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1225)
- signature: `class ChannelQuantScaleParameterTPU(ChannelQuantScaleParameter):`
- members:
  - <a id="ChannelQuantScaleParameterTPU.load_column_parallel_weight"></a>`load_column_parallel_weight(self, loaded_weight: torch.Tensor)` — [`L1226`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1226)
  - <a id="ChannelQuantScaleParameterTPU.load_merged_column_weight"></a>`load_merged_column_weight(self, loaded_weight: torch.Tensor, **kwargs)` — [`L1231`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1231)
  - <a id="ChannelQuantScaleParameterTPU.load_qkv_weight"></a>`load_qkv_weight(self, loaded_weight: torch.Tensor, **kwargs)` — [`L1236`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1236)
  - <a id="ChannelQuantScaleParameterTPU.load_row_parallel_weight"></a>`load_row_parallel_weight(self, loaded_weight: torch.Tensor, **kwargs)` — [`L1241`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1241)
- used by: [`create_weights`](fp8.md#VllmFp8LinearMethodTPU.create_weights)

### <a id="VllmFp8Config"></a>`VllmFp8Config`  ·  implements/extends VllmQuantConfig
- def: [`src/vllm_torchtpu/layers/adapter/quantization/fp8.py:663`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L663) — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
- doc: Native "fp8" quant_method config.
- signature: `class VllmFp8Config(Fp8Config, VllmQuantConfig):`
- members:
  - <a id="VllmFp8Config.apply_vllm_mapper"></a>`apply_vllm_mapper(self, hf_to_vllm_mapper: WeightsMapper)` — [`L722`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L722)
  - <a id="VllmFp8Config.from_config"></a>`from_config(cls, config: dict)` — [`L705`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L705)
  - <a id="VllmFp8Config.get_name"></a>`get_name(cls)` — [`L701`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L701)
  - <a id="VllmFp8Config.get_quant_method"></a>`get_quant_method(self, layer: torch.nn.Module, prefix: str)` — [`L726`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L726)
  - <a id="VllmFp8Config.is_channel_quant"></a>`is_channel_quant` — [`L673`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L673)
  - <a id="VllmFp8Config.is_checkpoint_fp8_serialized"></a>`is_checkpoint_fp8_serialized` — [`L698`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L698)
- protocol/private: <a id="VllmFp8Config.__init__"></a>`__init__`[`L675`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L675), <a id="VllmFp8Config._get_checkpoint_quant_method"></a>`_get_checkpoint_quant_method`[`L732`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L732)
- uses (calls/refs, reference-scoped): [`VllmQuantConfig`](configs.md#VllmQuantConfig), [`resolve_online_fp8`](fp8.md#resolve_online_fp8), [`get_moe_config`](configs.md#VllmQuantConfig.get_moe_config), [`VllmFp8LinearMethodTPU`](fp8.md#VllmFp8LinearMethodTPU), [`VllmUnquantizedFusedMoEMethod`](unquantized.md#VllmUnquantizedFusedMoEMethod), [`get_tpu_quant_method`](../../core/quant_methods.md#get_tpu_quant_method), [`VllmFp8MoEMethodTPU`](fp8.md#VllmFp8MoEMethodTPU), [`map_online_fp8`](online_fp8.md#map_online_fp8), [`VllmUnquantizedLinearMethod`](unquantized.md#VllmUnquantizedLinearMethod), [`get_linear_config`](configs.md#VllmQuantConfig.get_linear_config), [`packed_modules_mapping`](configs.md#VllmQuantConfig.packed_modules_mapping), [`FP8`](../../core/quant_methods.md#FP8)
- used by: [`get_tpu_quantization_config`](__init__.md#get_tpu_quantization_config), [`VllmQuantConfig`](configs.md#VllmQuantConfig), [`resolve_online_fp8`](fp8.md#resolve_online_fp8), [`get_quant_method`](unquantized.md#VllmUnquantizedConfig.get_quant_method), [`_build_fp8_config`](compressed_tensors/compressed_tensors.md#_build_fp8_config), [`set_configs`](compressed_tensors/compressed_tensors.md#VllmCompressedTensorsConfig.set_configs)

### <a id="VllmFp8LinearMethodTPU"></a>`VllmFp8LinearMethodTPU`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/fp8.py:1343`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1343) — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
- members:
  - <a id="VllmFp8LinearMethodTPU.apply"></a>`apply(self, layer: torch.nn.Module, x: torch.Tensor, bias: torch.Tensor | None = None)` — [`L1669`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1669)
  - <a id="VllmFp8LinearMethodTPU.create_weights"></a>`create_weights(self, layer, input_size_per_partition, output_partition_sizes, input_size, output_size, params_dtype, **extra_weight_attrs)` — [`L1406`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1406) — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
  - <a id="VllmFp8LinearMethodTPU.embedding"></a>`embedding(self, layer: torch.nn.Module, input_: torch.Tensor)` — [`L1692`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1692)
  - <a id="VllmFp8LinearMethodTPU.process_weights_after_loading"></a>`process_weights_after_loading(self, layer: torch.nn.Module)` — [`L1535`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1535) — Convert dense linear checkpoint weights to runtime FP8. — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
  - <a id="VllmFp8LinearMethodTPU.tie_weights"></a>`tie_weights(self, layer: torch.nn.Module, embed_tokens: torch.nn.Module)` — [`L1700`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1700)
  - <a id="VllmFp8LinearMethodTPU.act_q_static"></a>`act_q_static` — [`L1373`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1373)
  - <a id="VllmFp8LinearMethodTPU.activation_quant_key"></a>`activation_quant_key` — [`L1382`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1382)
  - <a id="VllmFp8LinearMethodTPU.block_quant"></a>`block_quant` — [`L1372`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1372)
  - <a id="VllmFp8LinearMethodTPU.cutlass_block_fp8_supported"></a>`cutlass_block_fp8_supported` — [`L1378`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1378)
  - <a id="VllmFp8LinearMethodTPU.input_dtype"></a>`input_dtype` — [`L1385`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1385)
  - <a id="VllmFp8LinearMethodTPU.is_scale_e8m0"></a>`is_scale_e8m0` — [`L1379`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1379)
  - <a id="VllmFp8LinearMethodTPU.linear_config"></a>`linear_config` — [`L1388`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1388)
  - <a id="VllmFp8LinearMethodTPU.online_fp8"></a>`online_fp8` — [`L1368`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1368) — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
  - <a id="VllmFp8LinearMethodTPU.online_fp8_policy"></a>`online_fp8_policy` — [`L1369`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1369)
  - <a id="VllmFp8LinearMethodTPU.out_dtype"></a>`out_dtype` — [`L1386`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1386)
  - <a id="VllmFp8LinearMethodTPU.prefix"></a>`prefix` — [`L1367`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1367)
  - <a id="VllmFp8LinearMethodTPU.quant_config"></a>`quant_config` — [`L1370`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1370)
  - <a id="VllmFp8LinearMethodTPU.use_deep_gemm"></a>`use_deep_gemm` — [`L1377`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1377)
  - <a id="VllmFp8LinearMethodTPU.use_marlin"></a>`use_marlin` — [`L1376`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1376)
  - <a id="VllmFp8LinearMethodTPU.w8a16_max_rows"></a>`w8a16_max_rows` — [`L1389`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1389)
  - <a id="VllmFp8LinearMethodTPU.weight_block_size"></a>`weight_block_size` — [`L1371`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1371)
  - <a id="VllmFp8LinearMethodTPU.weight_quant_key"></a>`weight_quant_key` — [`L1384`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1384)
- protocol/private: <a id="VllmFp8LinearMethodTPU.__init__"></a>`__init__`[`L1358`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1358), <a id="VllmFp8LinearMethodTPU._linear_quant_config"></a>`_linear_quant_config`[`L1396`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1396)
- uses (calls/refs, reference-scoped): [`synchronize_tensors`](../../../utils.md#synchronize_tensors), [`fresh_buffer`](../../../utils.md#fresh_buffer), [`_process_fp8_linear_weights`](fp8.md#_process_fp8_linear_weights), [`_get_linear_quant_config`](fp8.md#_get_linear_quant_config), [`quantize_tensor`](../../core/quantization.md#quantize_tensor), [`WEIGHT_FLIPPED_ATTR`](../linear_common.md#WEIGHT_FLIPPED_ATTR), [`quantize_online_fp8`](online_fp8.md#quantize_online_fp8), [`KEEP_VLLM_LAYOUT_ATTR`](../linear_common.md#KEEP_VLLM_LAYOUT_ATTR), [`VllmQuantLinearConfig`](configs.md#VllmQuantLinearConfig), [`OnlineFp8Policy`](online_fp8.md#OnlineFp8Policy), [`logger`](fp8.md#logger), [`quantized_matmul`](../linear_common.md#quantized_matmul), [`_wrap_block_scale_weight_loader`](fp8.md#_wrap_block_scale_weight_loader), [`w8a16_max_rows`](configs.md#VllmQuantLinearConfig.w8a16_max_rows), [`BlockQuantScaleParameterTPU`](fp8.md#BlockQuantScaleParameterTPU), [`TPU_FP8_LINEAR_W8A16_MAX_ROWS`](../../../envs.md#TPU_FP8_LINEAR_W8A16_MAX_ROWS), [`_format_linear_scale_for_runtime`](fp8.md#_format_linear_scale_for_runtime), [`ChannelQuantScaleParameterTPU`](fp8.md#ChannelQuantScaleParameterTPU)
- used by: [`resolve_online_fp8`](fp8.md#resolve_online_fp8), [`get_quant_method`](unquantized.md#VllmUnquantizedConfig.get_quant_method), [`get_quant_method`](deepseek_v4_fp8.md#VllmDeepseekV4Fp8Config.get_quant_method), [`_get_checkpoint_quant_method`](fp8.md#VllmFp8Config._get_checkpoint_quant_method), [`_owners`](../../../model_loader_patches.md#_OnlineFp8LayerFinisher._owners), [`consumed`](../../../model_loader_patches.md#_OnlineFp8LayerFinisher.consumed), [`_build_fp8_linear_method`](compressed_tensors/compressed_tensors.md#_build_fp8_linear_method), [`_shared_slice`](../moe_tp_decode.md#_shared_slice), [`_layers`](../../../model_loader_patches.md#_OnlineFp8LayerFinisher._layers), [`__init__`](../../../model_loader_patches.md#_OnlineFp8LayerFinisher.__init__)

### <a id="VllmFp8MoEMethodTPU"></a>`VllmFp8MoEMethodTPU`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/fp8.py:771`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L771) — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
- members:
  - <a id="VllmFp8MoEMethodTPU.apply_monolithic"></a>`apply_monolithic(self, layer: RoutedExperts, x: torch.Tensor, router_logits: torch.Tensor, input_ids: torch.Tensor | None = None)` — [`L1108`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1108) — Forward pass using TPU-native GMM kernel with FP8 weights. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
  - <a id="VllmFp8MoEMethodTPU.create_weights"></a>`create_weights(self, layer, num_experts, hidden_size, intermediate_size_per_partition, params_dtype, **extra_weight_attrs)` — [`L890`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L890)
  - <a id="VllmFp8MoEMethodTPU.is_monolithic"></a>`is_monolithic(self)` — [`L979`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L979)
  - <a id="VllmFp8MoEMethodTPU.maybe_roundup_sizes"></a>`maybe_roundup_sizes(self, hidden_size: int, intermediate_size_per_partition: int, act_dtype: torch.dtype, moe_parallel_config)` — [`L835`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L835)
  - <a id="VllmFp8MoEMethodTPU.process_weights_after_loading"></a>`process_weights_after_loading(self, layer: torch.nn.Module)` — [`L982`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L982) — Process MoE weights into the runtime FP8 layout used by the GMM kernel. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
  - <a id="VllmFp8MoEMethodTPU.supports_internal_mk"></a>`supports_internal_mk(self)` — [`L804`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L804) — Whether this method owns the DP/EP dispatch and combine.
  - <a id="VllmFp8MoEMethodTPU.block_quant"></a>`block_quant` — [`L790`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L790)
  - <a id="VllmFp8MoEMethodTPU.fp8_backend"></a>`fp8_backend` — [`L801`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L801)
  - <a id="VllmFp8MoEMethodTPU.moe_block_shape"></a>`moe_block_shape` — [`L797`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L797)
  - <a id="VllmFp8MoEMethodTPU.quant_config"></a>`quant_config` — [`L788`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L788)
  - <a id="VllmFp8MoEMethodTPU.weight_block_size"></a>`weight_block_size` — [`L789`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L789)
  - <a id="VllmFp8MoEMethodTPU.weight_scale_name"></a>`weight_scale_name` — [`L791`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L791)
  - <a id="VllmFp8MoEMethodTPU.weight_scale_refine"></a>`weight_scale_refine` — [`L798`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L798)
- protocol/private: <a id="VllmFp8MoEMethodTPU.__init__"></a>`__init__`[`L786`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L786), <a id="VllmFp8MoEMethodTPU._adaptive_fused_moe_op"></a>`_adaptive_fused_moe_op`[`L784`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L784), <a id="VllmFp8MoEMethodTPU._use_adaptive_fused_moe"></a>`_use_adaptive_fused_moe`[`L783`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L783)
- uses (calls/refs, reference-scoped): [`synchronize_tensors`](../../../utils.md#synchronize_tensors), [`prebuild_fused_moe_ep`](../fused_moe_ep.md#prebuild_fused_moe_ep), [`prebuild_adaptive_fused_moe`](../../../kernels/experimental/adaptive_fused_moe/vllm_adapter.md#prebuild_adaptive_fused_moe), [`pipelined_fused_moe_gmm`](../pipelined_fused_moe.md#pipelined_fused_moe_gmm), [`enable_pipelined_collective_and_compute`](../pipelined_fused_moe.md#enable_pipelined_collective_and_compute), [`fused_moe_ep`](../fused_moe_ep.md#fused_moe_ep), [`fused_moe_ep_supported`](../fused_moe_ep.md#fused_moe_ep_supported), [`_process_fp8_moe_weights`](fp8.md#_process_fp8_moe_weights), [`fused_moe_gmm`](../fused_moe.md#fused_moe_gmm), [`_quantize_bf16_moe_weights`](fp8.md#_quantize_bf16_moe_weights), [`prebuild_fused_moe_kernel`](../fused_moe.md#prebuild_fused_moe_kernel), [`moe_tp_decode_forward`](../moe_tp_decode.md#moe_tp_decode_forward), [`VllmUnquantizedFusedMoEMethod`](unquantized.md#VllmUnquantizedFusedMoEMethod), [`TpuMoEActivationMixin`](../fused_moe.md#TpuMoEActivationMixin), [`route`](../moe_routing.md#route), [`run_adaptive_fused_moe`](../../../kernels/experimental/adaptive_fused_moe/vllm_adapter.md#run_adaptive_fused_moe), [`_set_tpu_activation`](../fused_moe.md#TpuMoEActivationMixin._set_tpu_activation), [`_tpu_activation_str`](../fused_moe.md#TpuMoEActivationMixin._tpu_activation_str), [`fused_moe_decode`](../fused_moe_decode.md#fused_moe_decode), [`register_experts_start_buffer`](../moe_routing.md#register_experts_start_buffer), [`zero_routing_weights_for_padding`](../token_padding.md#zero_routing_weights_for_padding), [`register_score_bias_buffer`](../fused_moe_ep.md#register_score_bias_buffer), [`score_bias_operand`](../fused_moe_ep.md#score_bias_operand), [`FUSED_MOE_EP_OP_ATTR`](../fused_moe_ep.md#FUSED_MOE_EP_OP_ATTR), [`adaptive_fused_moe_supported`](../../../kernels/experimental/adaptive_fused_moe/vllm_adapter.md#adaptive_fused_moe_supported), [`moe_tp_decode_supported`](../moe_tp_decode.md#moe_tp_decode_supported), [`TPU_MOE_SKIP_PADDED_TOKENS`](../../../envs.md#TPU_MOE_SKIP_PADDED_TOKENS), [`validate_linear_ep_placement`](../moe_routing.md#validate_linear_ep_placement), [`logger`](fp8.md#logger), [`fused_moe_decode_supported`](../fused_moe_decode.md#fused_moe_decode_supported), [`TPU_MOE_FP8_ALL_GATHER`](../../../envs.md#TPU_MOE_FP8_ALL_GATHER), [`MOE_FUSED_EP_KERNEL_IMPL`](../../../envs.md#MOE_FUSED_EP_KERNEL_IMPL)
- used by: [`_admit`](../moe_tp_decode.md#_admit), [`get_moe_method`](compressed_tensors/compressed_tensors_moe/compressed_tensors_moe.md#VllmCompressedTensorsMoEMethod.get_moe_method), [`get_quant_method`](deepseek_v4_fp8.md#VllmDeepseekV4Fp8Config.get_quant_method), [`_get_checkpoint_quant_method`](fp8.md#VllmFp8Config._get_checkpoint_quant_method), [`_admit`](../fused_moe_decode.md#_admit)

## Functions
- <a id="_dequantize_fp8_linear"></a>`_dequantize_fp8_linear(weight: torch.Tensor, *, weight_scale: torch.Tensor | None, weight_scale_inv: torch.Tensor | None, block_quant: bool, weight_block_size: tuple[int, int] | None, logical_widths: list[int] | None = None, out_dtype: torch.dtype = torch.bfloat16)` — [`L132`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L132) — Dequantize FP8 linear weights.
- <a id="_format_linear_scale_for_runtime"></a>`_format_linear_scale_for_runtime(weight_scale: torch.Tensor, *, blockwise_kernel: bool)` — [`L270`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L270) — Reshape `weight_scale` to the layout expected by the matmul bridge.
- <a id="_get_linear_quant_config"></a>`_get_linear_quant_config(linear_config: VllmQuantLinearConfig | None)` — [`L216`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L216) — Parse dense-linear quantization settings from env-gated overrides. — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
- <a id="_get_moe_quant_config"></a>`_get_moe_quant_config(log_prefix: str)` — [`L185`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L185) — Parse MoE quantization env vars and return (dtype_name, dtype, block_size).
- <a id="_process_fp8_linear_weights"></a>`_process_fp8_linear_weights(layer: TpuLinear, *, block_quant: bool, weight_block_size: tuple[int, int] | None, linear_config: VllmQuantLinearConfig | None, linear_quant_config: LinearQuantConfig | None = None)` — [`L297`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L297) — Convert checkpoint FP8 dense linear weights to the runtime FP8 layout. — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
- <a id="_process_fp8_moe_weights"></a>`_process_fp8_moe_weights(layer: TpuRoutedExperts, *, weight_block_size: tuple[int, int] | None = None, activation: str)` — [`L486`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L486) — Dequantize and requantize FP8 MoE weights for the TPU GMM kernel. — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
- <a id="_quantize_and_format_moe_weights"></a>`_quantize_and_format_moe_weights(w13: torch.Tensor, w2: torch.Tensor, *, quant_dtype: torch.dtype, block_size: int | None, activation: str)` — [`L456`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L456) — Quantize float32 MoE weights to FP8 and format for the GMM kernel.
- <a id="_quantize_and_format_single_moe_weight"></a>`_quantize_and_format_single_moe_weight(w: torch.Tensor, *, name: str, quant_dtype: torch.dtype, block_size: int | None, activation: str = "")` — [`L351`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L351) — Quantize a float32 MoE weight tensor to FP8 and format for the GMM kernel.
- <a id="_quantize_bf16_moe_weights"></a>`_quantize_bf16_moe_weights(layer: TpuRoutedExperts, *, activation: str)` — [`L620`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L620) — Quantize BF16 MoE weights to FP8 for the TPU GMM kernel.
- <a id="_requantize_expert_chunks"></a>`_requantize_expert_chunks(weight: torch.Tensor, scale: torch.Tensor | None, dequantize: Callable[[torch.Tensor, torch.Tensor | None], torch.Tensor], zero_padding: Callable[[torch.Tensor], None] | None, **format_kwargs)` — [`L414`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L414) — Dequantize, requantize and format ``weight`` a few experts at a time.
- <a id="_wrap_block_scale_weight_loader"></a>`_wrap_block_scale_weight_loader(weight_loader: Callable)` — [`L1311`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1311) — Ensure pre-fused checkpoint calls (`loaded_shard_id=None` or `tuple`)
- <a id="_wrap_block_scale_weight_loader._wrapped"></a>`_wrapped(param: torch.nn.Parameter, loaded_weight: torch.Tensor, *args, **kwargs)` — [`L1319`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1319)
- <a id="_process_fp8_moe_weights.dequantize_w13"></a>`dequantize_w13(w_q: torch.Tensor, scale: torch.Tensor | None)` — [`L552`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L552)
- <a id="resolve_online_fp8"></a>`resolve_online_fp8(config: VllmFp8Config | VllmNvfp4Config, layer: torch.nn.Module, prefix: str, base_method: QuantizeMethodBase | None)` — [`L1707`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L1707) — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
- <a id="_quantize_bf16_moe_weights.to_fp32"></a>`to_fp32(w: torch.Tensor, _scale: torch.Tensor | None)` — [`L634`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L634)

## Module values
- <a id="LinearQuantConfig"></a>`LinearQuantConfig` — [`L129`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L129)
- <a id="_MOE_REQUANT_WEIGHT_DTYPES"></a>`_MOE_REQUANT_WEIGHT_DTYPES` — [`L122`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L122)
- <a id="_REQUANT_CHUNK_BYTES"></a>`_REQUANT_CHUNK_BYTES` — [`L411`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L411)
- <a id="logger"></a>`logger` — [`L120`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/fp8.py#L120)

