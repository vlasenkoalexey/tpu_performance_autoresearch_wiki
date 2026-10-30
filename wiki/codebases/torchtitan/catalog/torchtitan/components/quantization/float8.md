---
title: 'Module: torchtitan/components/quantization/float8.py'
type: catalog
provenance: extracted
module: torchtitan/components/quantization/float8.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.quantization.float8`/
symbols:
  Float8LinearConverter.convert: Float8LinearConverter#convert().
  Float8LinearConverter.config: Float8LinearConverter#config.
  Float8GroupedExpertsConverter.convert: Float8GroupedExpertsConverter#convert().
  Float8LinearConverter: Float8LinearConverter#
  Float8LinearConverter.filter_fn: Float8LinearConverter#filter_fn.
  Float8GroupedExpertsConverter.__init__: Float8GroupedExpertsConverter#__init__().
  Float8Linear: Float8Linear#
  Float8Linear.__init__: Float8Linear#__init__().
  Float8LinearConverter.Config: Float8LinearConverter#Config#
  Float8LinearConverter.torchao_config: Float8LinearConverter#torchao_config.
  Float8LinearConverter.Config.recipe_name: Float8LinearConverter#Config#recipe_name.
  Float8Linear.Config: Float8Linear#Config#
  Float8LinearConverter.Config.filter_fqns: Float8LinearConverter#Config#filter_fqns.
  Float8GroupedExpertsConverter.Config: Float8GroupedExpertsConverter#Config#
  _get_float8_grouped_experts_cls: _get_float8_grouped_experts_cls().
  Float8GroupedExpertsConverter: Float8GroupedExpertsConverter#
  Float8LinearConverter.Config.emulate: Float8LinearConverter#Config#emulate.
  _float8_experts_cache._float8_experts_cache: _float8_experts_cache._float8_experts_cache.
  _get_float8_grouped_experts_cls.Float8GroupedExperts: _get_float8_grouped_experts_cls().Float8GroupedExperts#
  Float8LinearConverter.__init__: Float8LinearConverter#__init__().
  _get_float8_grouped_experts_cls.Float8GroupedExperts.__init__: _get_float8_grouped_experts_cls().Float8GroupedExperts#__init__().
  _get_float8_grouped_experts_cls.Float8GroupedExperts._grouped_mm: _get_float8_grouped_experts_cls().Float8GroupedExperts#_grouped_mm().
  Float8Linear.Config._torchao_config: Float8Linear#Config#_torchao_config.
  Float8LinearConverter.enabled: Float8LinearConverter#enabled.
  _get_float8_grouped_experts_cls.Float8GroupedExperts.Config: _get_float8_grouped_experts_cls().Float8GroupedExperts#Config#
  Float8GroupedExperts._float8_op_config: Float8GroupedExperts#_float8_op_config.
  Float8GroupedExpertsConverter.PAD_MULTIPLE: Float8GroupedExpertsConverter#PAD_MULTIPLE.
  Float8GroupedExpertsConverter.config: Float8GroupedExpertsConverter#config.
---
# Module: [`torchtitan/components/quantization/float8.py`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py)

## Classes
### <a id="Float8GroupedExpertsConverter"></a>`Float8GroupedExpertsConverter`  ·  implements/extends QuantizationConverter
- def: [`torchtitan/components/quantization/float8.py:224`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L224) — documented in [quantization](../../../../concepts/quantization.md)
- doc: Apply FP8 quantization to MoE expert grouped GEMMs.
- signature: `class Float8GroupedExpertsConverter(QuantizationConverter):`
- members:
  - <a id="Float8GroupedExpertsConverter.convert"></a>`convert(self, model_config)` — [`L254`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L254) — documented in [quantization](../../../../concepts/quantization.md)
  - <a id="Float8GroupedExpertsConverter.PAD_MULTIPLE"></a>`PAD_MULTIPLE` — [`L228`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L228)
  - <a id="Float8GroupedExpertsConverter.config"></a>`config` — [`L235`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L235)
- protocol/private: <a id="Float8GroupedExpertsConverter.__init__"></a>`__init__`[`L234`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L234)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`GroupedExperts`](../../models/common/moe.md#GroupedExperts), [`traverse`](../../config/configurable.md#Configurable.Config.traverse), [`model_compile_enabled`](__init__.md#QuantizationConverter.Config.model_compile_enabled), [`swap_token_dispatcher`](utils.md#swap_token_dispatcher), [`QuantizationConverter`](__init__.md#QuantizationConverter), [`has_cuda_capability`](../../tools/utils.md#has_cuda_capability), [`Config`](../../models/common/moe.md#GroupedExperts.Config), [`_owner`](../../config/configurable.md#Configurable.Config._owner), [`Config`](float8.md#Float8GroupedExpertsConverter.Config), [`_get_float8_grouped_experts_cls`](float8.md#_get_float8_grouped_experts_cls), [`has_rocm_capability`](../../tools/utils.md#has_rocm_capability)
- used by: [`model_compile_enabled`](__init__.md#QuantizationConverter.Config.model_compile_enabled), [`convert`](../../protocols/model.md#ModelConfigConverter.convert), [`deepseek_v3_671b_float8`](../../models/deepseek_v3/config_registry.md#deepseek_v3_671b_float8), [`QuantizationConverter`](__init__.md#QuantizationConverter)

### <a id="Float8GroupedExpertsConverter.Config"></a>`Float8GroupedExpertsConverter.Config`  ·  implements/extends Config
- def: [`torchtitan/components/quantization/float8.py:231`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L231)
- signature: `class Config(QuantizationConverter.Config):`
- uses (calls/refs, reference-scoped): [`QuantizationConverter`](__init__.md#QuantizationConverter), [`Config`](__init__.md#QuantizationConverter.Config)
- used by: [`deepseek_v3_671b_float8`](../../models/deepseek_v3/config_registry.md#deepseek_v3_671b_float8), [`__init__`](float8.md#Float8GroupedExpertsConverter.__init__)

### <a id="Float8Linear"></a>`Float8Linear`  ·  implements/extends Module
- def: [`torchtitan/components/quantization/float8.py:27`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L27) — documented in [quantization](../../../../concepts/quantization.md)
- doc: Inherits from Module (not Linear) to satisfy the Module protocol
- signature: `class Float8Linear(TorchAOFloat8Linear, Module):`
- protocol/private: <a id="Float8Linear.__init__"></a>`__init__`[`L40`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L40)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`out_features`](../../models/common/linear.md#Linear.Config.out_features), [`in_features`](../../models/common/linear.md#Linear.Config.in_features), [`bias`](../../models/common/linear.md#Linear.Config.bias), [`Config`](float8.md#Float8Linear.Config), [`_torchao_config`](float8.md#Float8Linear.Config._torchao_config)
- used by: [`Module`](../../protocols/module.md#Module), [`model_compile_enabled`](__init__.md#QuantizationConverter.Config.model_compile_enabled), [`convert`](float8.md#Float8LinearConverter.convert), [`has_quantization`](utils.md#has_quantization), [`config`](float8.md#Float8LinearConverter.config)  (3 test-only)

### <a id="Float8Linear.Config"></a>`Float8Linear.Config`  ·  implements/extends Config
- def: [`torchtitan/components/quantization/float8.py:35`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L35)
- doc: Drop-in replacement for Linear.Config that builds Float8Linear.
- signature: `class Config(Linear.Config):`
- protocol/private: <a id="Float8Linear.Config._torchao_config"></a>`_torchao_config`[`L38`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L38)
- uses (calls/refs, reference-scoped): [`Linear`](../../models/common/linear.md#Linear), [`Config`](../../models/common/linear.md#Linear.Config)
- used by: [`convert`](float8.md#Float8LinearConverter.convert), [`has_quantization`](utils.md#has_quantization), [`__init__`](float8.md#Float8Linear.__init__)  (1 test-only)

### <a id="Float8LinearConverter"></a>`Float8LinearConverter`  ·  implements/extends QuantizationConverter
- def: [`torchtitan/components/quantization/float8.py:53`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L53) — documented in [quantization](../../../../concepts/quantization.md)
- doc: Replace matching Linear.Config with Float8Linear.Config.
- signature: `class Float8LinearConverter(QuantizationConverter):`
- members:
  - <a id="Float8LinearConverter.convert"></a>`convert(self, model_config)` — [`L151`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L151) — documented in [quantization](../../../../concepts/quantization.md)
  - <a id="Float8LinearConverter.config"></a>`config` — [`L75`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L75) — documented in [quantization](../../../../concepts/quantization.md)
  - <a id="Float8LinearConverter.enabled"></a>`enabled` — [`L110`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L110)
  - <a id="Float8LinearConverter.filter_fn"></a>`filter_fn` — [`L137`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L137) — documented in [quantization](../../../../concepts/quantization.md)
  - <a id="Float8LinearConverter.torchao_config"></a>`torchao_config` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L113) — documented in [quantization](../../../../concepts/quantization.md)
- protocol/private: <a id="Float8LinearConverter.__init__"></a>`__init__`[`L74`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L74)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`Linear`](../../models/common/linear.md#Linear), [`param_init`](../../protocols/module.md#Module.Config.param_init), [`Config`](../../models/common/linear.md#Linear.Config), [`out_features`](../../models/common/linear.md#Linear.Config.out_features), [`in_features`](../../models/common/linear.md#Linear.Config.in_features), [`bias`](../../models/common/linear.md#Linear.Config.bias), [`traverse`](../../config/configurable.md#Configurable.Config.traverse), [`model_compile_enabled`](__init__.md#QuantizationConverter.Config.model_compile_enabled), [`QuantizationConverter`](__init__.md#QuantizationConverter), [`has_cuda_capability`](../../tools/utils.md#has_cuda_capability), [`RouterGateLinear`](../../models/common/linear.md#RouterGateLinear), [`Config`](../../models/common/linear.md#RouterGateLinear.Config), [`module_filter_fn`](utils.md#module_filter_fn), [`Float8Linear`](float8.md#Float8Linear), [`TpuFloat8LinearConverter`](../../experiments/tpu/float8_converter.md#TpuFloat8LinearConverter), [`Config`](float8.md#Float8LinearConverter.Config), [`recipe_name`](float8.md#Float8LinearConverter.Config.recipe_name), [`Config`](float8.md#Float8Linear.Config), [`filter_fqns`](float8.md#Float8LinearConverter.Config.filter_fqns), [`emulate`](float8.md#Float8LinearConverter.Config.emulate), [`has_rocm_capability`](../../tools/utils.md#has_rocm_capability), [`_torchao_config`](float8.md#Float8Linear.Config._torchao_config)
- used by: [`llama3_405b`](../../models/llama3/config_registry.md#llama3_405b), [`model_compile_enabled`](__init__.md#QuantizationConverter.Config.model_compile_enabled), [`llama3_debugmodel_float8_emulate_lora`](../../models/llama3/config_registry.md#llama3_debugmodel_float8_emulate_lora), [`convert`](../../protocols/model.md#ModelConfigConverter.convert), [`deepseek_v3_671b_float8`](../../models/deepseek_v3/config_registry.md#deepseek_v3_671b_float8), [`llama3_debugmodel_float8`](../../models/llama3/config_registry.md#llama3_debugmodel_float8), [`QuantizationConverter`](__init__.md#QuantizationConverter), [`TpuFloat8LinearConverter`](../../experiments/tpu/float8_converter.md#TpuFloat8LinearConverter), [`Config`](../../experiments/tpu/float8_converter.md#TpuFloat8LinearConverter.Config)  (1 test-only)

### <a id="Float8LinearConverter.Config"></a>`Float8LinearConverter.Config`  ·  implements/extends Config
- def: [`torchtitan/components/quantization/float8.py:57`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L57) — documented in [quantization](../../../../concepts/quantization.md)
- signature: `class Config(QuantizationConverter.Config):`
- members:
  - <a id="Float8LinearConverter.Config.emulate"></a>`emulate` — [`L68`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L68) — ---
  - <a id="Float8LinearConverter.Config.filter_fqns"></a>`filter_fqns` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L61) — ---
  - <a id="Float8LinearConverter.Config.recipe_name"></a>`recipe_name` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L58) — --- — documented in [quantization](../../../../concepts/quantization.md)
- uses (calls/refs, reference-scoped): [`QuantizationConverter`](__init__.md#QuantizationConverter), [`Config`](__init__.md#QuantizationConverter.Config)
- used by: [`llama3_405b`](../../models/llama3/config_registry.md#llama3_405b), [`llama3_debugmodel_float8_emulate_lora`](../../models/llama3/config_registry.md#llama3_debugmodel_float8_emulate_lora), [`deepseek_v3_671b_float8`](../../models/deepseek_v3/config_registry.md#deepseek_v3_671b_float8), [`llama3_debugmodel_float8`](../../models/llama3/config_registry.md#llama3_debugmodel_float8), [`qwen3_moe_235b_scan_torchao_float8`](../../experiments/tpu/qwen3/config_registry.md#qwen3_moe_235b_scan_torchao_float8), [`_with_float8`](../../experiments/tpu/llama3/config_registry.md#_with_float8), [`config`](float8.md#Float8LinearConverter.config), [`filter_fn`](float8.md#Float8LinearConverter.filter_fn), [`Config`](../../experiments/tpu/float8_converter.md#TpuFloat8LinearConverter.Config), [`torchao_config`](float8.md#Float8LinearConverter.torchao_config), [`config`](../../experiments/tpu/float8_converter.md#TpuFloat8LinearConverter.config), [`enabled`](../../experiments/tpu/float8_converter.md#TpuFloat8LinearConverter.enabled), [`filter_fn`](../../experiments/tpu/float8_converter.md#TpuFloat8LinearConverter.filter_fn), [`__init__`](float8.md#Float8LinearConverter.__init__), [`torchao_config`](../../experiments/tpu/float8_converter.md#TpuFloat8LinearConverter.torchao_config)  (5 test-only)

### <a id="_get_float8_grouped_experts_cls.Float8GroupedExperts"></a>`_get_float8_grouped_experts_cls.Float8GroupedExperts`
- def: [`torchtitan/components/quantization/float8.py:195`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L195)
- signature: `class Float8GroupedExperts(parent_cls):`
- protocol/private: <a id="_get_float8_grouped_experts_cls.Float8GroupedExperts.__init__"></a>`__init__`[`L200`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L200), <a id="_get_float8_grouped_experts_cls.Float8GroupedExperts._grouped_mm"></a>`_grouped_mm`[`L206`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L206)
- uses (calls/refs, reference-scoped): [`Config`](float8.md#_get_float8_grouped_experts_cls.Float8GroupedExperts.Config), [`_float8_op_config`](float8.md#Float8GroupedExperts._float8_op_config)
- used by: [`_get_float8_grouped_experts_cls`](float8.md#_get_float8_grouped_experts_cls)

### <a id="_get_float8_grouped_experts_cls.Float8GroupedExperts.Config"></a>`_get_float8_grouped_experts_cls.Float8GroupedExperts.Config`
- def: [`torchtitan/components/quantization/float8.py:197`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L197)
- signature: `class Config(parent_config_cls):`
- used by: [`__init__`](float8.md#_get_float8_grouped_experts_cls.Float8GroupedExperts.__init__)

## Functions
- <a id="_get_float8_grouped_experts_cls"></a>`_get_float8_grouped_experts_cls(parent_cls: type)` — [`L184`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L184) — Get or create a Float8-quantized subclass of *parent_cls*.

## Module values
- <a id="_float8_experts_cache._float8_experts_cache"></a>`_float8_experts_cache` — [`L181`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L181)

## Other members
- <a id="Float8GroupedExperts._float8_op_config"></a>`Float8GroupedExperts._float8_op_config` — [`L204`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/float8.py#L204)

