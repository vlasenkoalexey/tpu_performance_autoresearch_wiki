---
title: 'Module: torchtitan/components/quantization/__init__.py'
type: catalog
provenance: extracted
module: torchtitan/components/quantization/__init__.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.quantization`/
symbols:
  QuantizationConverter.Config.model_compile_enabled: QuantizationConverter#Config#model_compile_enabled.
  QuantizationConverter: QuantizationConverter#
  QuantizationConverter.Config: QuantizationConverter#Config#
  __all__: __all__.
---
# Module: [`torchtitan/components/quantization/__init__.py`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/__init__.py)

## Classes
### <a id="QuantizationConverter"></a>`QuantizationConverter`  ·  implements/extends ModelConfigConverter
- def: [`torchtitan/components/quantization/__init__.py:21`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/__init__.py#L21) — documented in [quantization](../../../../concepts/quantization.md)
- doc: Base class for quantization converters.
- signature: `class QuantizationConverter(ModelConfigConverter):`
- uses (calls/refs, reference-scoped): [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`Float8LinearConverter`](float8.md#Float8LinearConverter), [`MXFP8LinearConverter`](mxfp8/converter.md#MXFP8LinearConverter), [`NVFP4LinearConverter`](nvfp4.md#NVFP4LinearConverter), [`MXFP8GroupedExpertsConverter`](mxfp8/converter.md#MXFP8GroupedExpertsConverter), [`Float8GroupedExpertsConverter`](float8.md#Float8GroupedExpertsConverter)
- used by: [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`validate_converter_order`](../../models/utils.md#validate_converter_order), [`Float8LinearConverter`](float8.md#Float8LinearConverter), [`MXFP8LinearConverter`](mxfp8/converter.md#MXFP8LinearConverter), [`Config`](float8.md#Float8LinearConverter.Config), [`Config`](mxfp8/converter.md#MXFP8LinearConverter.Config), [`Config`](nvfp4.md#NVFP4LinearConverter.Config), [`NVFP4LinearConverter`](nvfp4.md#NVFP4LinearConverter), [`MXFP8GroupedExpertsConverter`](mxfp8/converter.md#MXFP8GroupedExpertsConverter), [`Config`](mxfp8/converter.md#MXFP8GroupedExpertsConverter.Config), [`Config`](float8.md#Float8GroupedExpertsConverter.Config), [`Float8GroupedExpertsConverter`](float8.md#Float8GroupedExpertsConverter)

### <a id="QuantizationConverter.Config"></a>`QuantizationConverter.Config`  ·  implements/extends Config
- def: [`torchtitan/components/quantization/__init__.py:29`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/__init__.py#L29) — documented in [quantization](../../../../concepts/quantization.md)
- signature: `class Config(ModelConfigConverter.Config):`
- members:
  - <a id="QuantizationConverter.Config.model_compile_enabled"></a>`model_compile_enabled` — [`L30`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/__init__.py#L30) — --- — documented in [quantization](../../../../concepts/quantization.md)
- uses (calls/refs, reference-scoped): [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`Config`](../../protocols/model.md#ModelConfigConverter.Config), [`Float8LinearConverter`](float8.md#Float8LinearConverter), [`Float8Linear`](float8.md#Float8Linear), [`MXFP8LinearConverter`](mxfp8/converter.md#MXFP8LinearConverter), [`MXFP8Linear`](mxfp8/linear.md#MXFP8Linear), [`NVFP4LinearConverter`](nvfp4.md#NVFP4LinearConverter), [`NVFP4Linear`](nvfp4.md#NVFP4Linear), [`MXFP8GroupedExpertsConverter`](mxfp8/converter.md#MXFP8GroupedExpertsConverter), [`Float8GroupedExpertsConverter`](float8.md#Float8GroupedExpertsConverter)
- used by: [`llama3_405b`](../../models/llama3/config_registry.md#llama3_405b), [`llama3_8b_first_85_pct_layers_nvfp4`](../../models/llama3/config_registry.md#llama3_8b_first_85_pct_layers_nvfp4), [`llama3_debugmodel_first_85_pct_layers_nvfp4`](../../models/llama3/config_registry.md#llama3_debugmodel_first_85_pct_layers_nvfp4), [`qwen3_8b_first_85_pct_layers_nvfp4`](../../models/qwen3/config_registry.md#qwen3_8b_first_85_pct_layers_nvfp4), [`qwen3_debugmodel_first_85_pct_layers_nvfp4`](../../models/qwen3/config_registry.md#qwen3_debugmodel_first_85_pct_layers_nvfp4), [`graph_trainer_deepseek_v3_debugmodel_mxfp8`](../../experiments/graph_trainer/deepseek_v3/config_registry.md#graph_trainer_deepseek_v3_debugmodel_mxfp8), [`llama3_debugmodel_float8_emulate_lora`](../../models/llama3/config_registry.md#llama3_debugmodel_float8_emulate_lora), [`llama3_debugmodel_nvfp4`](../../models/llama3/config_registry.md#llama3_debugmodel_nvfp4), [`qwen3_debugmodel_nvfp4`](../../models/qwen3/config_registry.md#qwen3_debugmodel_nvfp4), [`validate_converter_order`](../../models/utils.md#validate_converter_order), [`deepseek_v3_671b_float8`](../../models/deepseek_v3/config_registry.md#deepseek_v3_671b_float8), [`deepseek_v3_debugmodel_mxfp8`](../../models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel_mxfp8), [`llama3_debugmodel_float8`](../../models/llama3/config_registry.md#llama3_debugmodel_float8), [`flux_dev_mxfp8`](../../models/flux/config_registry.md#flux_dev_mxfp8), [`flux_schnell_mxfp8`](../../models/flux/config_registry.md#flux_schnell_mxfp8), [`config`](float8.md#Float8LinearConverter.config), [`deepseek_v3_mxfp8_linear_converter_config`](../../models/deepseek_v3/config_registry.md#deepseek_v3_mxfp8_linear_converter_config), [`__init__`](float8.md#Float8GroupedExpertsConverter.__init__), [`__init__`](nvfp4.md#NVFP4LinearConverter.__init__), [`llama3_mxfp8_linear_converter_config`](../../models/llama3/config_registry.md#llama3_mxfp8_linear_converter_config), [`__init__`](mxfp8/converter.md#MXFP8GroupedExpertsConverter.__init__), [`Config`](float8.md#Float8LinearConverter.Config), [`Config`](mxfp8/converter.md#MXFP8LinearConverter.Config), [`Config`](nvfp4.md#NVFP4LinearConverter.Config), [`Config`](mxfp8/converter.md#MXFP8GroupedExpertsConverter.Config), [`Config`](float8.md#Float8GroupedExpertsConverter.Config)

## Module values
- <a id="__all__"></a>`__all__` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/__init__.py#L47)

