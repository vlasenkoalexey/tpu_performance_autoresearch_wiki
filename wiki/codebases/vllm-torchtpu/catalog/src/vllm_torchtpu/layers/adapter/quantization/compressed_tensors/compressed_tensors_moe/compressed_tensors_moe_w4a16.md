---
title: 'Module: src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.quantization.compressed_tensors.compressed_tensors_moe.compressed_tensors_moe_w4a16`/VllmCompressedTensorsW4A16MoEMethod#
symbols:
  VllmCompressedTensorsW4A16MoEMethod.process_weights_after_loading: process_weights_after_loading().
  VllmCompressedTensorsW4A16MoEMethod.create_weights: create_weights().
  VllmCompressedTensorsW4A16MoEMethod.apply_monolithic: apply_monolithic().
  VllmCompressedTensorsW4A16MoEMethod._process_single_weight_pair: _process_single_weight_pair().
  VllmCompressedTensorsW4A16MoEMethod.group_size: group_size.
  VllmCompressedTensorsW4A16MoEMethod.packed_factor: packed_factor.
  VllmCompressedTensorsW4A16MoEMethod._validate_w4a16_scheme: _validate_w4a16_scheme().
  VllmCompressedTensorsW4A16MoEMethod._validate_int32_weight_carriers: _validate_int32_weight_carriers().
  VllmCompressedTensorsW4A16MoEMethod.supports_internal_mk: supports_internal_mk().
  VllmCompressedTensorsW4A16MoEMethod: ''
  VllmCompressedTensorsW4A16MoEMethod.weight_quant: weight_quant.
  VllmCompressedTensorsW4A16MoEMethod.strategy: strategy.
  VllmCompressedTensorsW4A16MoEMethod._loaded_data: _loaded_data().
  VllmCompressedTensorsW4A16MoEMethod._PACKED_WEIGHT_NAMES: _PACKED_WEIGHT_NAMES.
  VllmCompressedTensorsW4A16MoEMethod._INT4_SIGN_XOR: _INT4_SIGN_XOR.
  VllmCompressedTensorsW4A16MoEMethod.num_bits: num_bits.
  VllmCompressedTensorsW4A16MoEMethod.is_transposed: is_transposed.
  VllmCompressedTensorsW4A16MoEMethod.__init__: __init__().
  VllmCompressedTensorsW4A16MoEMethod.input_quant: input_quant.
  VllmCompressedTensorsW4A16MoEMethod.symmetric: symmetric.
  VllmCompressedTensorsW4A16MoEMethod.actorder: actorder.
  VllmCompressedTensorsW4A16MoEMethod.wna16_backend: wna16_backend.
  VllmCompressedTensorsW4A16MoEMethod.experts_cls: experts_cls.
  VllmCompressedTensorsW4A16MoEMethod.is_marlin: is_marlin.
  VllmCompressedTensorsW4A16MoEMethod.input_dtype: input_dtype.
  VllmCompressedTensorsW4A16MoEMethod.moe_kernel: moe_kernel.
  VllmCompressedTensorsW4A16MoEMethod.is_monolithic: is_monolithic().
  VllmCompressedTensorsW4A16MoEMethod.supports_eplb: supports_eplb().
  VllmCompressedTensorsW4A16MoEMethod.get_fused_moe_quant_config: get_fused_moe_quant_config().
---
# Module: [`src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py)

## Classes
### <a id="VllmCompressedTensorsW4A16MoEMethod"></a>`VllmCompressedTensorsW4A16MoEMethod`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py:61`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L61)
- doc: TPU compressed-tensors packed-weight W4 MoE implementation.
- signature: `class VllmCompressedTensorsW4A16MoEMethod(CompressedTensorsWNA16MoEMethod):`
- members:
  - <a id="VllmCompressedTensorsW4A16MoEMethod._loaded_data"></a>`_loaded_data(parameter: torch.nn.Parameter)` — [`L140`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L140) — Return checkpoint scratch data or an already-materialized weight.
  - <a id="VllmCompressedTensorsW4A16MoEMethod.apply_monolithic"></a>`apply_monolithic(self, layer: RoutedExperts, x: torch.Tensor, router_logits: torch.Tensor, input_ids: torch.Tensor | None = None)` — [`L372`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L372)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.create_weights"></a>`create_weights(self, layer: torch.nn.Module, num_experts: int, hidden_size: int, intermediate_size_per_partition: int, params_dtype: torch.dtype, **extra_weight_attrs)` — [`L174`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L174) — documented in [quantization-methods](../../../../../../../../concepts/quantization-methods.md)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.get_fused_moe_quant_config"></a>`get_fused_moe_quant_config(self, layer: torch.nn.Module)` — [`L123`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L123)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.is_monolithic"></a>`is_monolithic(self)` — [`L114`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L114)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.process_weights_after_loading"></a>`process_weights_after_loading(self, layer: torch.nn.Module)` — [`L313`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L313) — Process W4 MoE weights after loading. — documented in [quantization-methods](../../../../../../../../concepts/quantization-methods.md)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.supports_eplb"></a>`supports_eplb(self)` — [`L120`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L120)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.supports_internal_mk"></a>`supports_internal_mk(self)` — [`L134`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L134)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.actorder"></a>`actorder` — [`L88`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L88)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.experts_cls"></a>`experts_cls` — [`L108`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L108)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.group_size"></a>`group_size` — [`L90`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L90)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.input_dtype"></a>`input_dtype` — [`L110`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L110)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.input_quant"></a>`input_quant` — [`L81`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L81)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.is_marlin"></a>`is_marlin` — [`L109`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L109)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.is_transposed"></a>`is_transposed` — [`L91`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L91)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.moe_kernel"></a>`moe_kernel` — [`L111`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L111)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.num_bits"></a>`num_bits` — [`L82`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L82)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.packed_factor"></a>`packed_factor` — [`L85`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L85)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.strategy"></a>`strategy` — [`L86`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L86)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.symmetric"></a>`symmetric` — [`L87`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L87)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.weight_quant"></a>`weight_quant` — [`L80`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L80)
  - <a id="VllmCompressedTensorsW4A16MoEMethod.wna16_backend"></a>`wna16_backend` — [`L106`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L106)
- protocol/private: <a id="VllmCompressedTensorsW4A16MoEMethod._INT4_SIGN_XOR"></a>`_INT4_SIGN_XOR`[`L69`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L69), <a id="VllmCompressedTensorsW4A16MoEMethod._PACKED_WEIGHT_NAMES"></a>`_PACKED_WEIGHT_NAMES`[`L64`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L64), <a id="VllmCompressedTensorsW4A16MoEMethod.__init__"></a>`__init__`[`L71`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L71), <a id="VllmCompressedTensorsW4A16MoEMethod._process_single_weight_pair"></a>`_process_single_weight_pair`[`L266`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L266), <a id="VllmCompressedTensorsW4A16MoEMethod._validate_int32_weight_carriers"></a>`_validate_int32_weight_carriers`[`L161`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L161), <a id="VllmCompressedTensorsW4A16MoEMethod._validate_w4a16_scheme"></a>`_validate_w4a16_scheme`[`L145`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.py#L145)
- uses (calls/refs, reference-scoped): [`pipelined_fused_moe_gmm`](../../../pipelined_fused_moe.md#pipelined_fused_moe_gmm), [`enable_pipelined_collective_and_compute`](../../../pipelined_fused_moe.md#enable_pipelined_collective_and_compute), [`fused_moe_gmm`](../../../fused_moe.md#fused_moe_gmm), [`prebuild_fused_moe_kernel`](../../../fused_moe.md#prebuild_fused_moe_kernel), [`route`](../../../moe_routing.md#route), [`register_experts_start_buffer`](../../../moe_routing.md#register_experts_start_buffer), [`requantize_int4_to_fp4_weights`](utils.md#requantize_int4_to_fp4_weights), [`get_cpu_weight_loader_hook`](utils.md#get_cpu_weight_loader_hook), [`get_fused_moe_activation`](../../../fused_moe.md#get_fused_moe_activation), [`MOE_REQUANTIZE_BLOCK_SIZE`](../../../../../envs.md#MOE_REQUANTIZE_BLOCK_SIZE), [`release_memory_to_os`](utils.md#release_memory_to_os), [`requantize_int4_weights`](utils.md#requantize_int4_weights), [`MOE_REQUANTIZE_WEIGHT_DTYPE`](../../../../../envs.md#MOE_REQUANTIZE_WEIGHT_DTYPE), [`_orig_shape`](utils.md#StagedParameter._orig_shape)
- used by: [`get_moe_method`](compressed_tensors_moe.md#VllmCompressedTensorsMoEMethod.get_moe_method)

