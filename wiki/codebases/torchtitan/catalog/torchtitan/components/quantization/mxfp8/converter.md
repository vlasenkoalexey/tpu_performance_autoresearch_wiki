---
title: 'Module: torchtitan/components/quantization/mxfp8/converter.py'
type: catalog
provenance: extracted
module: torchtitan/components/quantization/mxfp8/converter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.quantization.mxfp8.converter`/
symbols:
  MXFP8LinearConverter.convert: MXFP8LinearConverter#convert().
  MXFP8GroupedExpertsConverter.convert: MXFP8GroupedExpertsConverter#convert().
  MXFP8LinearConverter: MXFP8LinearConverter#
  MXFP8LinearConverter.__init__: MXFP8LinearConverter#__init__().
  MXFP8GroupedExpertsConverter.__init__: MXFP8GroupedExpertsConverter#__init__().
  MXFP8LinearConverter.Config: MXFP8LinearConverter#Config#
  MXFP8GroupedExpertsConverter: MXFP8GroupedExpertsConverter#
  import_error: import_error.
  MXFP8GroupedExpertsConverter.Config: MXFP8GroupedExpertsConverter#Config#
  _get_mxfp8_grouped_experts_cls: _get_mxfp8_grouped_experts_cls().
  _get_mxfp8_grouped_experts_cls.MXFP8GroupedExperts.__init__: _get_mxfp8_grouped_experts_cls().MXFP8GroupedExperts#__init__().
  _mxfp8_experts_cache._mxfp8_experts_cache: _mxfp8_experts_cache._mxfp8_experts_cache.
  _mxfp8_linear_import_error._mxfp8_linear_import_error: _mxfp8_linear_import_error._mxfp8_linear_import_error.
  MXFP8LinearConverter.Config.fqns: MXFP8LinearConverter#Config#fqns.
  MXFP8LinearConverter.Config.linears_saving_inputs_for_backward_in_mxfp8: MXFP8LinearConverter#Config#linears_saving_inputs_for_backward_in_mxfp8.
  _get_mxfp8_grouped_experts_cls.MXFP8GroupedExperts: _get_mxfp8_grouped_experts_cls().MXFP8GroupedExperts#
  MXFP8GroupedExpertsConverter.config: MXFP8GroupedExpertsConverter#config.
  MXFP8GroupedExpertsConverter.Config.pad_multiple: MXFP8GroupedExpertsConverter#Config#pad_multiple.
  MXFP8LinearConverter.Config.__post_init__: MXFP8LinearConverter#Config#__post_init__().
  _get_mxfp8_grouped_experts_cls.MXFP8GroupedExperts._grouped_mm: _get_mxfp8_grouped_experts_cls().MXFP8GroupedExperts#_grouped_mm().
  MXFP8LinearConverter.config: MXFP8LinearConverter#config.
  MXFP8GroupedExpertsConverter.Config.recipe_name: MXFP8GroupedExpertsConverter#Config#recipe_name.
  _torchao_nightly_install_command: _torchao_nightly_install_command().
  _get_mxfp8_grouped_experts_cls.MXFP8GroupedExperts.Config: _get_mxfp8_grouped_experts_cls().MXFP8GroupedExperts#Config#
  _get_mxfp8_grouped_experts_cls.MXFP8GroupedExperts.Config.recipe_name: _get_mxfp8_grouped_experts_cls().MXFP8GroupedExperts#Config#recipe_name.
  MXFP8GroupedExperts._mxfp8_op_config: MXFP8GroupedExperts#_mxfp8_op_config.
---
# Module: [`torchtitan/components/quantization/mxfp8/converter.py`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py)

## Classes
### <a id="MXFP8GroupedExpertsConverter"></a>`MXFP8GroupedExpertsConverter`  ·  implements/extends QuantizationConverter
- def: [`torchtitan/components/quantization/mxfp8/converter.py:236`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L236) — documented in [quantization](../../../../../concepts/quantization.md)
- doc: Apply MXFP8 quantization to MoE expert grouped GEMMs.
- signature: `class MXFP8GroupedExpertsConverter(QuantizationConverter):`
- members:
  - <a id="MXFP8GroupedExpertsConverter.convert"></a>`convert(self, model_config)` — [`L271`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L271) — documented in [quantization](../../../../../concepts/quantization.md)
  - <a id="MXFP8GroupedExpertsConverter.config"></a>`config` — [`L255`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L255)
- protocol/private: <a id="MXFP8GroupedExpertsConverter.__init__"></a>`__init__`[`L254`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L254)
- uses (calls/refs, reference-scoped): [`logger`](../../../tools/logging.md#logger), [`GroupedExperts`](../../../models/common/moe.md#GroupedExperts), [`traverse`](../../../config/configurable.md#Configurable.Config.traverse), [`model_compile_enabled`](../__init__.md#QuantizationConverter.Config.model_compile_enabled), [`swap_token_dispatcher`](../utils.md#swap_token_dispatcher), [`QuantizationConverter`](../__init__.md#QuantizationConverter), [`has_cuda_capability`](../../../tools/utils.md#has_cuda_capability), [`Config`](../../../models/common/moe.md#GroupedExperts.Config), [`_owner`](../../../config/configurable.md#Configurable.Config._owner), [`Config`](converter.md#MXFP8GroupedExpertsConverter.Config), [`_get_mxfp8_grouped_experts_cls`](converter.md#_get_mxfp8_grouped_experts_cls), [`pad_multiple`](converter.md#MXFP8GroupedExpertsConverter.Config.pad_multiple), [`recipe_name`](converter.md#MXFP8GroupedExpertsConverter.Config.recipe_name)
- used by: [`model_compile_enabled`](../__init__.md#QuantizationConverter.Config.model_compile_enabled), [`graph_trainer_deepseek_v3_debugmodel_mxfp8`](../../../experiments/graph_trainer/deepseek_v3/config_registry.md#graph_trainer_deepseek_v3_debugmodel_mxfp8), [`convert`](../../../protocols/model.md#ModelConfigConverter.convert), [`deepseek_v3_debugmodel_mxfp8`](../../../models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel_mxfp8), [`QuantizationConverter`](../__init__.md#QuantizationConverter)

### <a id="MXFP8GroupedExpertsConverter.Config"></a>`MXFP8GroupedExpertsConverter.Config`  ·  implements/extends Config
- def: [`torchtitan/components/quantization/mxfp8/converter.py:240`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L240)
- signature: `class Config(QuantizationConverter.Config):`
- members:
  - <a id="MXFP8GroupedExpertsConverter.Config.pad_multiple"></a>`pad_multiple` — [`L248`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L248) — ---
  - <a id="MXFP8GroupedExpertsConverter.Config.recipe_name"></a>`recipe_name` — [`L241`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L241) — ---
- uses (calls/refs, reference-scoped): [`QuantizationConverter`](../__init__.md#QuantizationConverter), [`Config`](../__init__.md#QuantizationConverter.Config)
- used by: [`graph_trainer_deepseek_v3_debugmodel_mxfp8`](../../../experiments/graph_trainer/deepseek_v3/config_registry.md#graph_trainer_deepseek_v3_debugmodel_mxfp8), [`deepseek_v3_debugmodel_mxfp8`](../../../models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel_mxfp8), [`convert`](converter.md#MXFP8GroupedExpertsConverter.convert), [`__init__`](converter.md#MXFP8GroupedExpertsConverter.__init__)

### <a id="MXFP8LinearConverter"></a>`MXFP8LinearConverter`  ·  implements/extends QuantizationConverter
- def: [`torchtitan/components/quantization/mxfp8/converter.py:58`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L58) — documented in [quantization](../../../../../concepts/quantization.md)
- doc: Replace matching Linear.Config with MXFP8Linear.Config.
- signature: `class MXFP8LinearConverter(QuantizationConverter):`
- members:
  - <a id="MXFP8LinearConverter.convert"></a>`convert(self, model_config)` — [`L121`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L121) — documented in [quantization](../../../../../concepts/quantization.md)
  - <a id="MXFP8LinearConverter.config"></a>`config` — [`L108`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L108)
- protocol/private: <a id="MXFP8LinearConverter.__init__"></a>`__init__`[`L107`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L107)
- uses (calls/refs, reference-scoped): [`logger`](../../../tools/logging.md#logger), [`Linear`](../../../models/common/linear.md#Linear), [`param_init`](../../../protocols/module.md#Module.Config.param_init), [`Config`](../../../models/common/linear.md#Linear.Config), [`out_features`](../../../models/common/linear.md#Linear.Config.out_features), [`in_features`](../../../models/common/linear.md#Linear.Config.in_features), [`bias`](../../../models/common/linear.md#Linear.Config.bias), [`traverse`](../../../config/configurable.md#Configurable.Config.traverse), [`QuantizationConverter`](../__init__.md#QuantizationConverter), [`has_cuda_capability`](../../../tools/utils.md#has_cuda_capability), [`RouterGateLinear`](../../../models/common/linear.md#RouterGateLinear), [`Config`](../../../models/common/linear.md#RouterGateLinear.Config), [`MXFP8Linear`](linear.md#MXFP8Linear), [`Config`](converter.md#MXFP8LinearConverter.Config), [`Config`](linear.md#MXFP8Linear.Config), [`input_activation_format_for_backward`](linear.md#MXFP8Linear.Config.input_activation_format_for_backward), [`_mxfp8_linear_import_error`](converter.md#_mxfp8_linear_import_error._mxfp8_linear_import_error), [`fqns`](converter.md#MXFP8LinearConverter.Config.fqns), [`linears_saving_inputs_for_backward_in_mxfp8`](converter.md#MXFP8LinearConverter.Config.linears_saving_inputs_for_backward_in_mxfp8), [`_torchao_nightly_install_command`](converter.md#_torchao_nightly_install_command)
- used by: [`model_compile_enabled`](../__init__.md#QuantizationConverter.Config.model_compile_enabled), [`convert`](../../../protocols/model.md#ModelConfigConverter.convert), [`flux_dev_mxfp8`](../../../models/flux/config_registry.md#flux_dev_mxfp8), [`flux_schnell_mxfp8`](../../../models/flux/config_registry.md#flux_schnell_mxfp8), [`QuantizationConverter`](../__init__.md#QuantizationConverter), [`deepseek_v3_mxfp8_linear_converter_config`](../../../models/deepseek_v3/config_registry.md#deepseek_v3_mxfp8_linear_converter_config), [`llama3_mxfp8_linear_converter_config`](../../../models/llama3/config_registry.md#llama3_mxfp8_linear_converter_config)

### <a id="MXFP8LinearConverter.Config"></a>`MXFP8LinearConverter.Config`  ·  implements/extends Config
- def: [`torchtitan/components/quantization/mxfp8/converter.py:62`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L62) — documented in [quantization](../../../../../concepts/quantization.md)
- signature: `class Config(QuantizationConverter.Config):`
- members:
  - <a id="MXFP8LinearConverter.Config.fqns"></a>`fqns` — [`L63`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L63) — ---
  - <a id="MXFP8LinearConverter.Config.linears_saving_inputs_for_backward_in_mxfp8"></a>`linears_saving_inputs_for_backward_in_mxfp8` — [`L69`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L69) — ---
- protocol/private: <a id="MXFP8LinearConverter.Config.__post_init__"></a>`__post_init__`[`L100`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L100)
- uses (calls/refs, reference-scoped): [`QuantizationConverter`](../__init__.md#QuantizationConverter), [`Config`](../__init__.md#QuantizationConverter.Config)
- used by: [`convert`](converter.md#MXFP8LinearConverter.convert), [`flux_dev_mxfp8`](../../../models/flux/config_registry.md#flux_dev_mxfp8), [`flux_schnell_mxfp8`](../../../models/flux/config_registry.md#flux_schnell_mxfp8), [`deepseek_v3_mxfp8_linear_converter_config`](../../../models/deepseek_v3/config_registry.md#deepseek_v3_mxfp8_linear_converter_config), [`llama3_mxfp8_linear_converter_config`](../../../models/llama3/config_registry.md#llama3_mxfp8_linear_converter_config), [`__init__`](converter.md#MXFP8LinearConverter.__init__)

### <a id="_get_mxfp8_grouped_experts_cls.MXFP8GroupedExperts"></a>`_get_mxfp8_grouped_experts_cls.MXFP8GroupedExperts`
- def: [`torchtitan/components/quantization/mxfp8/converter.py:203`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L203)
- signature: `class MXFP8GroupedExperts(parent_cls):`
- protocol/private: <a id="_get_mxfp8_grouped_experts_cls.MXFP8GroupedExperts.__init__"></a>`__init__`[`L208`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L208), <a id="_get_mxfp8_grouped_experts_cls.MXFP8GroupedExperts._grouped_mm"></a>`_grouped_mm`[`L218`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L218)
- uses (calls/refs, reference-scoped): [`Config`](converter.md#_get_mxfp8_grouped_experts_cls.MXFP8GroupedExperts.Config), [`_mxfp8_op_config`](converter.md#MXFP8GroupedExperts._mxfp8_op_config), [`recipe_name`](converter.md#_get_mxfp8_grouped_experts_cls.MXFP8GroupedExperts.Config.recipe_name)
- used by: [`_get_mxfp8_grouped_experts_cls`](converter.md#_get_mxfp8_grouped_experts_cls)

### <a id="_get_mxfp8_grouped_experts_cls.MXFP8GroupedExperts.Config"></a>`_get_mxfp8_grouped_experts_cls.MXFP8GroupedExperts.Config`
- def: [`torchtitan/components/quantization/mxfp8/converter.py:205`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L205)
- signature: `class Config(parent_config_cls):`
- members:
  - <a id="_get_mxfp8_grouped_experts_cls.MXFP8GroupedExperts.Config.recipe_name"></a>`recipe_name` — [`L206`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L206)
- used by: [`__init__`](converter.md#_get_mxfp8_grouped_experts_cls.MXFP8GroupedExperts.__init__)

## Functions
- <a id="_get_mxfp8_grouped_experts_cls"></a>`_get_mxfp8_grouped_experts_cls(parent_cls: type)` — [`L188`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L188) — Get or create an MXFP8-quantized subclass of *parent_cls*.
- <a id="_torchao_nightly_install_command"></a>`_torchao_nightly_install_command()` — [`L37`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L37) — Return the pip command that installs a torchao nightly for this torch.

## Module values
- <a id="_mxfp8_experts_cache._mxfp8_experts_cache"></a>`_mxfp8_experts_cache` — [`L185`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L185)
- <a id="_mxfp8_linear_import_error._mxfp8_linear_import_error"></a>`_mxfp8_linear_import_error` — [`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L21)
- <a id="import_error"></a>`import_error` — [`L32`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L32)

## Other members
- <a id="MXFP8GroupedExperts._mxfp8_op_config"></a>`MXFP8GroupedExperts._mxfp8_op_config` — [`L216`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/converter.py#L216)

