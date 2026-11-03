---
title: 'Module: src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.quantization.nvfp4`/
symbols:
  VllmNvfp4MoEMethod.process_weights_after_loading: VllmNvfp4MoEMethod#process_weights_after_loading().
  VllmNvfp4MoEMethod.apply_monolithic: VllmNvfp4MoEMethod#apply_monolithic().
  _requant_moe_w4a8: _requant_moe_w4a8().
  _prebuild_w4a8: _prebuild_w4a8().
  VllmNvfp4Config._get_checkpoint_quant_method: VllmNvfp4Config#_get_checkpoint_quant_method().
  VllmNvfp4LinearMethod.process_weights_after_loading: VllmNvfp4LinearMethod#process_weights_after_loading().
  _prepare_moe_weights: _prepare_moe_weights().
  VllmNvfp4Config: VllmNvfp4Config#
  VllmNvfp4LinearMethod.create_weights: VllmNvfp4LinearMethod#create_weights().
  logger: logger.
  _to_kernel_scale: _to_kernel_scale().
  VllmNvfp4MoEMethod.supports_internal_mk: VllmNvfp4MoEMethod#supports_internal_mk().
  VllmNvfp4MoEMethod._use_adaptive_fused_moe: VllmNvfp4MoEMethod#_use_adaptive_fused_moe.
  VllmNvfp4Config.get_quant_method: VllmNvfp4Config#get_quant_method().
  _NullInputQuantKernel: _NullInputQuantKernel#
  VllmNvfp4LinearMethod.__init__: VllmNvfp4LinearMethod#__init__().
  VllmNvfp4LinearMethod.null_factory: VllmNvfp4LinearMethod#null_factory().
  VllmNvfp4LinearMethod.kernel: VllmNvfp4LinearMethod#kernel.
  VllmNvfp4MoEMethod: VllmNvfp4MoEMethod#
  VllmNvfp4Config.get_name: VllmNvfp4Config#get_name().
  VllmNvfp4Config.apply_vllm_mapper: VllmNvfp4Config#apply_vllm_mapper().
  VllmNvfp4MoEMethod.__init__: VllmNvfp4MoEMethod#__init__().
  VllmNvfp4MoEMethod._resolve_tpu_activation: VllmNvfp4MoEMethod#_resolve_tpu_activation().
  VllmNvfp4LinearMethod.ctx: VllmNvfp4LinearMethod#ctx.
  VllmNvfp4LinearMethod.select_kernel: VllmNvfp4LinearMethod#select_kernel().
  VllmNvfp4LinearMethod.init_kernel: VllmNvfp4LinearMethod#init_kernel().
  VllmNvfp4LinearMethod.apply: VllmNvfp4LinearMethod#apply().
  VllmNvfp4MoEMethod.group_size: VllmNvfp4MoEMethod#group_size.
  VllmNvfp4LinearMethod.group_size: VllmNvfp4LinearMethod#group_size.
  VllmNvfp4LinearMethod.scalar_weight_loader: VllmNvfp4LinearMethod#scalar_weight_loader().
  VllmNvfp4MoEMethod._adaptive_fused_moe_op: VllmNvfp4MoEMethod#_adaptive_fused_moe_op.
  VllmNvfp4LinearMethod: VllmNvfp4LinearMethod#
  VllmNvfp4MoEMethod.quant_config: VllmNvfp4MoEMethod#quant_config.
  VllmNvfp4MoEMethod.use_global_sf: VllmNvfp4MoEMethod#use_global_sf.
  VllmNvfp4MoEMethod.is_monolithic: VllmNvfp4MoEMethod#is_monolithic().
  VllmNvfp4MoEMethod.get_fused_moe_quant_config: VllmNvfp4MoEMethod#get_fused_moe_quant_config().
  VllmNvfp4MoEMethod.create_weights: VllmNvfp4MoEMethod#create_weights().
  _NullInputQuantKernel.input_quant_key: _NullInputQuantKernel#input_quant_key().
  _NullInputQuantKernel.is_supported: _NullInputQuantKernel#is_supported().
  _NullInputQuantKernel.can_implement: _NullInputQuantKernel#can_implement().
  _NullInputQuantKernel.__getattr__: _NullInputQuantKernel#__getattr__().
  VllmNvfp4LinearMethod.quant_config: VllmNvfp4LinearMethod#quant_config.
  VllmNvfp4LinearMethod.linear_config: VllmNvfp4LinearMethod#linear_config.
  VllmNvfp4LinearMethod.wkey: VllmNvfp4LinearMethod#wkey.
  VllmNvfp4LinearMethod.akey: VllmNvfp4LinearMethod#akey.
  VllmNvfp4LinearMethod.fmt: VllmNvfp4LinearMethod#fmt.
  VllmNvfp4LinearMethod.input_dtype: VllmNvfp4LinearMethod#input_dtype.
  VllmNvfp4LinearMethod.out_dtype: VllmNvfp4LinearMethod#out_dtype.
  VllmNvfp4LinearMethod.marlin_input_dtype: VllmNvfp4LinearMethod#marlin_input_dtype.
  VllmNvfp4LinearMethod.spec: VllmNvfp4LinearMethod#spec.
---
# Module: [`src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py)

## Classes
### <a id="VllmNvfp4Config"></a>`VllmNvfp4Config`  ·  implements/extends VllmQuantConfig
- def: [`src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py:257`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L257) — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
- doc: NVFP4 config for TPU. Inherits ModelOpt checkpoint parsing from upstream;
- signature: `class VllmNvfp4Config(ModelOptNvFp4Config, VllmQuantConfig):`
- members:
  - <a id="VllmNvfp4Config.apply_vllm_mapper"></a>`apply_vllm_mapper(self, hf_to_vllm_mapper: WeightsMapper)` — [`L265`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L265)
  - <a id="VllmNvfp4Config.get_name"></a>`get_name(cls)` — [`L262`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L262)
  - <a id="VllmNvfp4Config.get_quant_method"></a>`get_quant_method(self, layer: torch.nn.Module, prefix: str)` — [`L269`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L269)
- protocol/private: <a id="VllmNvfp4Config._get_checkpoint_quant_method"></a>`_get_checkpoint_quant_method`[`L275`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L275)
- uses (calls/refs, reference-scoped): [`VllmQuantConfig`](configs.md#VllmQuantConfig), [`resolve_online_fp8`](fp8.md#resolve_online_fp8), [`get_moe_config`](configs.md#VllmQuantConfig.get_moe_config), [`VllmUnquantizedFusedMoEMethod`](unquantized.md#VllmUnquantizedFusedMoEMethod), [`get_tpu_quant_method`](../../core/quant_methods.md#get_tpu_quant_method), [`map_online_fp8`](online_fp8.md#map_online_fp8), [`VllmUnquantizedLinearMethod`](unquantized.md#VllmUnquantizedLinearMethod), [`get_linear_config`](configs.md#VllmQuantConfig.get_linear_config), [`NVFP4`](../../core/quant_methods.md#NVFP4), [`VllmNvfp4MoEMethod`](nvfp4.md#VllmNvfp4MoEMethod), [`VllmNvfp4LinearMethod`](nvfp4.md#VllmNvfp4LinearMethod)
- used by: [`get_tpu_quantization_config`](__init__.md#get_tpu_quantization_config), [`VllmQuantConfig`](configs.md#VllmQuantConfig), [`resolve_online_fp8`](fp8.md#resolve_online_fp8), [`__init__`](nvfp4.md#VllmNvfp4LinearMethod.__init__), [`__init__`](nvfp4.md#VllmNvfp4MoEMethod.__init__)

### <a id="VllmNvfp4LinearMethod"></a>`VllmNvfp4LinearMethod`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py:606`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L606)
- members:
  - <a id="VllmNvfp4LinearMethod.apply"></a>`apply(self, layer: torch.nn.Module, x: torch.Tensor, bias: torch.Tensor | None = None)` — [`L754`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L754)
  - <a id="VllmNvfp4LinearMethod.create_weights"></a>`create_weights(self, layer, input_size_per_partition, output_partition_sizes, input_size, output_size, params_dtype, **extra_weight_attrs)` — [`L641`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L641)
  - <a id="VllmNvfp4LinearMethod.init_kernel"></a>`init_kernel(self, *args: Any, **kwargs: Any)` — [`L638`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L638)
  - <a id="VllmNvfp4LinearMethod.null_factory"></a>`null_factory(*args: Any, **kwargs: Any)` — [`L658`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L658)
  - <a id="VllmNvfp4LinearMethod.process_weights_after_loading"></a>`process_weights_after_loading(self, layer: torch.nn.Module)` — [`L709`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L709)
  - <a id="VllmNvfp4LinearMethod.scalar_weight_loader"></a>`scalar_weight_loader(param, loaded_weight, *args, **kwargs)` — [`L692`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L692)
  - <a id="VllmNvfp4LinearMethod.select_kernel"></a>`select_kernel(self, *args: Any, **kwargs: Any)` — [`L635`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L635)
  - <a id="VllmNvfp4LinearMethod.akey"></a>`akey` — [`L628`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L628)
  - <a id="VllmNvfp4LinearMethod.ctx"></a>`ctx` — [`L627`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L627)
  - <a id="VllmNvfp4LinearMethod.fmt"></a>`fmt` — [`L629`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L629)
  - <a id="VllmNvfp4LinearMethod.group_size"></a>`group_size` — [`L622`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L622)
  - <a id="VllmNvfp4LinearMethod.input_dtype"></a>`input_dtype` — [`L630`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L630)
  - <a id="VllmNvfp4LinearMethod.kernel"></a>`kernel` — [`L625`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L625)
  - <a id="VllmNvfp4LinearMethod.linear_config"></a>`linear_config` — [`L621`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L621)
  - <a id="VllmNvfp4LinearMethod.marlin_input_dtype"></a>`marlin_input_dtype` — [`L632`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L632)
  - <a id="VllmNvfp4LinearMethod.out_dtype"></a>`out_dtype` — [`L631`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L631)
  - <a id="VllmNvfp4LinearMethod.quant_config"></a>`quant_config` — [`L620`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L620)
  - <a id="VllmNvfp4LinearMethod.spec"></a>`spec` — [`L633`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L633)
  - <a id="VllmNvfp4LinearMethod.wkey"></a>`wkey` — [`L626`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L626)
- protocol/private: <a id="VllmNvfp4LinearMethod.__init__"></a>`__init__`[`L615`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L615)
- uses (calls/refs, reference-scoped): [`synchronize_tensors`](../../../utils.md#synchronize_tensors), [`fresh_buffer`](../../../utils.md#fresh_buffer), [`VllmNvfp4Config`](nvfp4.md#VllmNvfp4Config), [`load_kmajor_fp4`](../fused_moe.md#load_kmajor_fp4), [`VllmQuantLinearConfig`](configs.md#VllmQuantLinearConfig), [`_to_kernel_scale`](nvfp4.md#_to_kernel_scale), [`logger`](nvfp4.md#logger), [`_NullInputQuantKernel`](nvfp4.md#_NullInputQuantKernel), [`quantized_matmul_fp4`](../linear_common.md#quantized_matmul_fp4)
- used by: [`_get_checkpoint_quant_method`](nvfp4.md#VllmNvfp4Config._get_checkpoint_quant_method)

### <a id="VllmNvfp4MoEMethod"></a>`VllmNvfp4MoEMethod`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py:302`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L302)
- members:
  - <a id="VllmNvfp4MoEMethod.apply_monolithic"></a>`apply_monolithic(self, layer: RoutedExperts, x: torch.Tensor, router_logits: torch.Tensor, input_ids: torch.Tensor | None = None)` — [`L510`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L510) — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
  - <a id="VllmNvfp4MoEMethod.create_weights"></a>`create_weights(self, layer, num_experts, hidden_size, intermediate_size_per_partition, params_dtype, **extra_weight_attrs)` — [`L343`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L343)
  - <a id="VllmNvfp4MoEMethod.get_fused_moe_quant_config"></a>`get_fused_moe_quant_config(self, layer)` — [`L340`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L340)
  - <a id="VllmNvfp4MoEMethod.is_monolithic"></a>`is_monolithic(self)` — [`L325`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L325)
  - <a id="VllmNvfp4MoEMethod.process_weights_after_loading"></a>`process_weights_after_loading(self, layer: torch.nn.Module)` — [`L388`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L388) — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
  - <a id="VllmNvfp4MoEMethod.supports_internal_mk"></a>`supports_internal_mk(self)` — [`L329`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L329)
  - <a id="VllmNvfp4MoEMethod.group_size"></a>`group_size` — [`L319`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L319)
  - <a id="VllmNvfp4MoEMethod.quant_config"></a>`quant_config` — [`L318`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L318)
  - <a id="VllmNvfp4MoEMethod.use_global_sf"></a>`use_global_sf` — [`L322`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L322)
- protocol/private: <a id="VllmNvfp4MoEMethod.__init__"></a>`__init__`[`L315`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L315), <a id="VllmNvfp4MoEMethod._adaptive_fused_moe_op"></a>`_adaptive_fused_moe_op`[`L313`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L313), <a id="VllmNvfp4MoEMethod._resolve_tpu_activation"></a>`_resolve_tpu_activation`[`L379`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L379), <a id="VllmNvfp4MoEMethod._use_adaptive_fused_moe"></a>`_use_adaptive_fused_moe`[`L312`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L312)
- uses (calls/refs, reference-scoped): [`synchronize_tensors`](../../../utils.md#synchronize_tensors), [`pipelined_fused_moe_gmm`](../pipelined_fused_moe.md#pipelined_fused_moe_gmm), [`enable_pipelined_collective_and_compute`](../pipelined_fused_moe.md#enable_pipelined_collective_and_compute), [`fused_moe_ep`](../fused_moe_ep.md#fused_moe_ep), [`fused_moe_ep_supported`](../fused_moe_ep.md#fused_moe_ep_supported), [`_prebuild_w4a8`](nvfp4.md#_prebuild_w4a8), [`fused_moe_ep_unsupported_reason`](../fused_moe_ep.md#fused_moe_ep_unsupported_reason), [`fused_moe_gmm`](../fused_moe.md#fused_moe_gmm), [`prebuild_fused_moe_kernel`](../fused_moe.md#prebuild_fused_moe_kernel), [`fused_moe_ep_unsupported_reason`](../../../kernels/experimental/adaptive_fused_moe/vllm_adapter.md#fused_moe_ep_unsupported_reason), [`VllmNvfp4Config`](nvfp4.md#VllmNvfp4Config), [`_prepare_moe_weights`](nvfp4.md#_prepare_moe_weights), [`TpuMoEActivationMixin`](../fused_moe.md#TpuMoEActivationMixin), [`route`](../moe_routing.md#route), [`run_adaptive_fused_moe`](../../../kernels/experimental/adaptive_fused_moe/vllm_adapter.md#run_adaptive_fused_moe), [`_set_tpu_activation`](../fused_moe.md#TpuMoEActivationMixin._set_tpu_activation), [`_tpu_activation_str`](../fused_moe.md#TpuMoEActivationMixin._tpu_activation_str), [`prebuild_adaptive_nvfp4`](../../../kernels/experimental/adaptive_fused_moe/vllm_adapter.md#prebuild_adaptive_nvfp4), [`_resolve_tpu_activation`](../fused_moe.md#TpuMoEActivationMixin._resolve_tpu_activation), [`register_experts_start_buffer`](../moe_routing.md#register_experts_start_buffer), [`register_fused_scale_buffers`](../fused_moe_ep.md#register_fused_scale_buffers), [`register_score_bias_buffer`](../fused_moe_ep.md#register_score_bias_buffer), [`score_bias_operand`](../fused_moe_ep.md#score_bias_operand), [`FUSED_MOE_EP_OP_ATTR`](../fused_moe_ep.md#FUSED_MOE_EP_OP_ATTR), [`adaptive_fused_moe_supported`](../../../kernels/experimental/adaptive_fused_moe/vllm_adapter.md#adaptive_fused_moe_supported), [`logger`](nvfp4.md#logger), [`MOE_REQUANTIZE_BLOCK_SIZE`](../../../envs.md#MOE_REQUANTIZE_BLOCK_SIZE), [`validate_linear_ep_placement`](../moe_routing.md#validate_linear_ep_placement), [`MOE_FUSED_EP_KERNEL_IMPL`](../../../envs.md#MOE_FUSED_EP_KERNEL_IMPL)
- used by: [`_get_checkpoint_quant_method`](nvfp4.md#VllmNvfp4Config._get_checkpoint_quant_method), [`_resolve_tpu_activation`](../fused_moe.md#TpuMoEActivationMixin._resolve_tpu_activation)

### <a id="_NullInputQuantKernel"></a>`_NullInputQuantKernel`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py:582`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L582)
- doc: Placeholder kernel so upstream create_weights' expose_input_quant_key
- signature: `class _NullInputQuantKernel:`
- members:
  - <a id="_NullInputQuantKernel.can_implement"></a>`can_implement(cls, *args: Any, **kwargs: Any)` — [`L598`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L598)
  - <a id="_NullInputQuantKernel.input_quant_key"></a>`input_quant_key()` — [`L588`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L588)
  - <a id="_NullInputQuantKernel.is_supported"></a>`is_supported(cls, compute_capability: int | None = None)` — [`L592`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L592)
- protocol/private: <a id="_NullInputQuantKernel.__getattr__"></a>`__getattr__`[`L601`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L601)
- used by: [`create_weights`](nvfp4.md#VllmNvfp4LinearMethod.create_weights), [`null_factory`](nvfp4.md#VllmNvfp4LinearMethod.null_factory), [`kernel`](nvfp4.md#VllmNvfp4LinearMethod.kernel), [`init_kernel`](nvfp4.md#VllmNvfp4LinearMethod.init_kernel), [`select_kernel`](nvfp4.md#VllmNvfp4LinearMethod.select_kernel)

## Functions
- <a id="_prebuild_w4a8"></a>`_prebuild_w4a8(layer, activation, configured_block)` — [`L203`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L203) — Admit the proposed runtime layout while checkpoint weights are intact. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="_prepare_moe_weights"></a>`_prepare_moe_weights(layer, w13_scale_f, w2_scale_f, requant_block)` — [`L177`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L177) — Prepare a candidate weight set without replacing checkpoint tensors.
- <a id="_requant_moe_w4a8"></a>`_requant_moe_w4a8(w13_u8: torch.Tensor, w13_scale_f: torch.Tensor, w2_u8: torch.Tensor, w2_scale_f: torch.Tensor, block: int)` — [`L124`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L124) — Requantize NVFP4 MoE weights from native block-16 to block-`block` fp4 — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
- <a id="_to_kernel_scale"></a>`_to_kernel_scale(scale_f32: torch.Tensor)` — [`L117`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L117) — [*, out, num_blocks] fp32 -> [*, num_blocks, 1, out] fp32 (gmm_v2 rhs

## Module values
- <a id="logger"></a>`logger` — [`L114`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.py#L114)

