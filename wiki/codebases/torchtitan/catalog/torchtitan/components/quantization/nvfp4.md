---
title: 'Module: torchtitan/components/quantization/nvfp4.py'
type: catalog
provenance: extracted
module: torchtitan/components/quantization/nvfp4.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.quantization.nvfp4`/
symbols:
  NVFP4LinearConverter.convert: NVFP4LinearConverter#convert().
  NVFP4Linear.Config.build: NVFP4Linear#Config#build().
  NVFP4LinearConverter.__init__: NVFP4LinearConverter#__init__().
  NVFP4Linear.__init__: NVFP4Linear#__init__().
  NVFP4LinearConverter.Config: NVFP4LinearConverter#Config#
  NVFP4LinearConverter: NVFP4LinearConverter#
  NVFP4Linear: NVFP4Linear#
  NVFP4Linear._refresh_rht_sign_vector_tuple: NVFP4Linear#_refresh_rht_sign_vector_tuple().
  TP: TP.
  NVFP4Linear.Config: NVFP4Linear#Config#
  NVFP4LinearConverter.Config.fqns: NVFP4LinearConverter#Config#fqns.
  NVFP4Linear._rht_sign_vector: NVFP4Linear#_rht_sign_vector.
  NVFP4Linear.rht_sign_vector: NVFP4Linear#rht_sign_vector().
  nvfp4_bf16_tail_fqns: nvfp4_bf16_tail_fqns().
  NVFP4Linear.forward: NVFP4Linear#forward().
  NVFP4Linear._rht_sign_vector_tuple: NVFP4Linear#_rht_sign_vector_tuple.
  NVFP4Linear._local_rht_sign_vector: NVFP4Linear#_local_rht_sign_vector().
  NVFP4Linear.Config.__post_init__: NVFP4Linear#Config#__post_init__().
  NVFP4Linear._load_from_state_dict: NVFP4Linear#_load_from_state_dict().
  _NVFP4_BLOCK: _NVFP4_BLOCK.
  NVFP4LinearConverter.config: NVFP4LinearConverter#config.
  _HARDCODED_SIGN_VECTOR: _HARDCODED_SIGN_VECTOR.
  NVFP4Linear._sr_seed: NVFP4Linear#_sr_seed.
  NVFP4Linear._init_self_buffers: NVFP4Linear#_init_self_buffers().
---
# Module: [`torchtitan/components/quantization/nvfp4.py`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py)

## Classes
### <a id="NVFP4Linear"></a>`NVFP4Linear`  ·  implements/extends Module
- def: [`torchtitan/components/quantization/nvfp4.py:84`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L84) — documented in [quantization](../../../../concepts/quantization.md)
- doc: NVFP4 Linear satisfying torchtitan's Module protocol.
- signature: `class NVFP4Linear(TorchAONVFP4Linear, Module):`
- members:
  - <a id="NVFP4Linear.forward"></a>`forward(self, x: torch.Tensor)` — [`L234`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L234)
  - <a id="NVFP4Linear.rht_sign_vector"></a>`rht_sign_vector(self)` — [`L203`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L203)
- protocol/private: <a id="NVFP4Linear.__init__"></a>`__init__`[`L159`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L159), <a id="NVFP4Linear._init_self_buffers"></a>`_init_self_buffers`[`L210`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L210), <a id="NVFP4Linear._load_from_state_dict"></a>`_load_from_state_dict`[`L198`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L198), <a id="NVFP4Linear._local_rht_sign_vector"></a>`_local_rht_sign_vector`[`L186`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L186), <a id="NVFP4Linear._refresh_rht_sign_vector_tuple"></a>`_refresh_rht_sign_vector_tuple`[`L192`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L192), <a id="NVFP4Linear._rht_sign_vector"></a>`_rht_sign_vector`[`L229`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L229), <a id="NVFP4Linear._rht_sign_vector_tuple"></a>`_rht_sign_vector_tuple`[`L184`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L184), <a id="NVFP4Linear._sr_seed"></a>`_sr_seed`[`L220`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L220)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](../../models/common/linear.md#Linear), [`Config`](../../models/common/linear.md#Linear.Config), [`out_features`](../../models/common/linear.md#Linear.Config.out_features), [`in_features`](../../models/common/linear.md#Linear.Config.in_features), [`bias`](../../models/common/linear.md#Linear.Config.bias), [`_HARDCODED_SIGN_VECTOR`](nvfp4.md#_HARDCODED_SIGN_VECTOR)
- used by: [`Module`](../../protocols/module.md#Module), [`model_compile_enabled`](__init__.md#QuantizationConverter.Config.model_compile_enabled), [`convert`](nvfp4.md#NVFP4LinearConverter.convert), [`has_quantization`](utils.md#has_quantization), [`__init__`](nvfp4.md#NVFP4LinearConverter.__init__)

### <a id="NVFP4Linear.Config"></a>`NVFP4Linear.Config`  ·  implements/extends Config
- def: [`torchtitan/components/quantization/nvfp4.py:95`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L95)
- doc: Drop-in replacement for Linear.Config that builds NVFP4Linear.
- signature: `class Config(Linear.Config):`
- members:
  - <a id="NVFP4Linear.Config.build"></a>`build(self, **kwargs)` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L113) — documented in [quantization](../../../../concepts/quantization.md)
- protocol/private: <a id="NVFP4Linear.Config.__post_init__"></a>`__post_init__`[`L98`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L98)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`Linear`](../../models/common/linear.md#Linear), [`Config`](../../models/common/linear.md#Linear.Config), [`dense_activation_placement`](../../models/common/decoder_sharding.md#dense_activation_placement), [`MeshAxisName`](../../distributed/parallel_dims.md#MeshAxisName), [`LocalMapConfig`](../../protocols/sharding.md#LocalMapConfig), [`CP`](../../distributed/parallel_dims.md#MeshAxisName.CP), [`in_grad_placements`](../../protocols/sharding.md#LocalMapConfig.in_grad_placements), [`DP`](../../distributed/parallel_dims.md#MeshAxisName.DP), [`TP`](nvfp4.md#TP), [`_NVFP4_BLOCK`](nvfp4.md#_NVFP4_BLOCK)
- used by: [`convert`](nvfp4.md#NVFP4LinearConverter.convert), [`has_quantization`](utils.md#has_quantization)

### <a id="NVFP4LinearConverter"></a>`NVFP4LinearConverter`  ·  implements/extends QuantizationConverter
- def: [`torchtitan/components/quantization/nvfp4.py:267`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L267) — documented in [quantization](../../../../concepts/quantization.md)
- doc: Replace matching Linear.Config with NVFP4Linear.Config.
- signature: `class NVFP4LinearConverter(QuantizationConverter):`
- members:
  - <a id="NVFP4LinearConverter.convert"></a>`convert(self, model_config)` — [`L299`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L299) — documented in [quantization](../../../../concepts/quantization.md)
  - <a id="NVFP4LinearConverter.config"></a>`config` — [`L281`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L281)
- protocol/private: <a id="NVFP4LinearConverter.__init__"></a>`__init__`[`L280`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L280)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`Linear`](../../models/common/linear.md#Linear), [`param_init`](../../protocols/module.md#Module.Config.param_init), [`Config`](../../models/common/linear.md#Linear.Config), [`out_features`](../../models/common/linear.md#Linear.Config.out_features), [`in_features`](../../models/common/linear.md#Linear.Config.in_features), [`bias`](../../models/common/linear.md#Linear.Config.bias), [`traverse`](../../config/configurable.md#Configurable.Config.traverse), [`model_compile_enabled`](__init__.md#QuantizationConverter.Config.model_compile_enabled), [`QuantizationConverter`](__init__.md#QuantizationConverter), [`has_cuda_capability`](../../tools/utils.md#has_cuda_capability), [`RouterGateLinear`](../../models/common/linear.md#RouterGateLinear), [`Config`](../../models/common/linear.md#RouterGateLinear.Config), [`Config`](nvfp4.md#NVFP4LinearConverter.Config), [`NVFP4Linear`](nvfp4.md#NVFP4Linear), [`Config`](nvfp4.md#NVFP4Linear.Config), [`fqns`](nvfp4.md#NVFP4LinearConverter.Config.fqns)
- used by: [`llama3_8b_first_85_pct_layers_nvfp4`](../../models/llama3/config_registry.md#llama3_8b_first_85_pct_layers_nvfp4), [`llama3_debugmodel_first_85_pct_layers_nvfp4`](../../models/llama3/config_registry.md#llama3_debugmodel_first_85_pct_layers_nvfp4), [`qwen3_8b_first_85_pct_layers_nvfp4`](../../models/qwen3/config_registry.md#qwen3_8b_first_85_pct_layers_nvfp4), [`qwen3_debugmodel_first_85_pct_layers_nvfp4`](../../models/qwen3/config_registry.md#qwen3_debugmodel_first_85_pct_layers_nvfp4), [`model_compile_enabled`](__init__.md#QuantizationConverter.Config.model_compile_enabled), [`llama3_debugmodel_nvfp4`](../../models/llama3/config_registry.md#llama3_debugmodel_nvfp4), [`qwen3_debugmodel_nvfp4`](../../models/qwen3/config_registry.md#qwen3_debugmodel_nvfp4), [`convert`](../../protocols/model.md#ModelConfigConverter.convert), [`QuantizationConverter`](__init__.md#QuantizationConverter)

### <a id="NVFP4LinearConverter.Config"></a>`NVFP4LinearConverter.Config`  ·  implements/extends Config
- def: [`torchtitan/components/quantization/nvfp4.py:271`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L271) — documented in [quantization](../../../../concepts/quantization.md)
- signature: `class Config(QuantizationConverter.Config):`
- members:
  - <a id="NVFP4LinearConverter.Config.fqns"></a>`fqns` — [`L272`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L272) — --- — documented in [quantization](../../../../concepts/quantization.md)
- uses (calls/refs, reference-scoped): [`QuantizationConverter`](__init__.md#QuantizationConverter), [`Config`](__init__.md#QuantizationConverter.Config)
- used by: [`llama3_8b_first_85_pct_layers_nvfp4`](../../models/llama3/config_registry.md#llama3_8b_first_85_pct_layers_nvfp4), [`llama3_debugmodel_first_85_pct_layers_nvfp4`](../../models/llama3/config_registry.md#llama3_debugmodel_first_85_pct_layers_nvfp4), [`qwen3_8b_first_85_pct_layers_nvfp4`](../../models/qwen3/config_registry.md#qwen3_8b_first_85_pct_layers_nvfp4), [`qwen3_debugmodel_first_85_pct_layers_nvfp4`](../../models/qwen3/config_registry.md#qwen3_debugmodel_first_85_pct_layers_nvfp4), [`llama3_debugmodel_nvfp4`](../../models/llama3/config_registry.md#llama3_debugmodel_nvfp4), [`qwen3_debugmodel_nvfp4`](../../models/qwen3/config_registry.md#qwen3_debugmodel_nvfp4), [`convert`](nvfp4.md#NVFP4LinearConverter.convert), [`__init__`](nvfp4.md#NVFP4LinearConverter.__init__)

## Functions
- <a id="nvfp4_bf16_tail_fqns"></a>`nvfp4_bf16_tail_fqns(num_layers: int, bf16_tail_fraction: float)` — [`L247`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L247) — Converter ``fqns`` selecting the leading decoder layers for NVFP4 while

## Module values
- <a id="TP"></a>`TP` — [`L36`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L36)
- <a id="_HARDCODED_SIGN_VECTOR"></a>`_HARDCODED_SIGN_VECTOR` — [`L48`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L48)
- <a id="_NVFP4_BLOCK"></a>`_NVFP4_BLOCK` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/nvfp4.py#L40)

