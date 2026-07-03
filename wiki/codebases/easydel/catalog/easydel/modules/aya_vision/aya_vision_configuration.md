---
title: 'Module: easydel/modules/aya_vision/aya_vision_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/aya_vision/aya_vision_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.aya_vision.aya_vision_configuration`/
symbols:
  AyaVisionConfig: AyaVisionConfig#
  AyaVisionConfig.vision_config: AyaVisionConfig#vision_config.
  AyaVisionConfig.vision_feature_layer: AyaVisionConfig#vision_feature_layer.
  AyaVisionConfig.downsample_factor: AyaVisionConfig#downsample_factor.
  logger: logger.
  AyaVisionConfig.sub_configs: AyaVisionConfig#sub_configs.
  AyaVisionConfig.__init__: AyaVisionConfig#__init__().
  AyaVisionConfig.text_config: AyaVisionConfig#text_config.
  AyaVisionConfig.adapter_layer_norm_eps: AyaVisionConfig#adapter_layer_norm_eps.
  AyaVisionConfig.model_type: AyaVisionConfig#model_type.
  AyaVisionConfig.attribute_map: AyaVisionConfig#attribute_map.
  AyaVisionConfig.image_token_index: AyaVisionConfig#image_token_index.
  AyaVisionConfig.vision_feature_select_strategy: AyaVisionConfig#vision_feature_select_strategy.
  AyaVisionConfig.get_partition_rules: AyaVisionConfig#get_partition_rules().
---
# Module: [`easydel/modules/aya_vision/aya_vision_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/aya_vision/aya_vision_configuration.py)

## Classes
### `AyaVisionConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/aya_vision/aya_vision_configuration.py:30`](../../../../../../../raw/code/EasyDeL/easydel/modules/aya_vision/aya_vision_configuration.py#L30)
- doc: This is the configuration class to store the configuration of a \[`AyaVisionForConditionalGeneration`\]. It is used
- signature: `class AyaVisionConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L118`](../../../../../../../raw/code/EasyDeL/easydel/modules/aya_vision/aya_vision_configuration.py#L118) — Returns partition rules for model sharding.
  - `adapter_layer_norm_eps` — [`L76`](../../../../../../../raw/code/EasyDeL/easydel/modules/aya_vision/aya_vision_configuration.py#L76)
  - `attribute_map` — [`L60`](../../../../../../../raw/code/EasyDeL/easydel/modules/aya_vision/aya_vision_configuration.py#L60)
  - `downsample_factor` — [`L75`](../../../../../../../raw/code/EasyDeL/easydel/modules/aya_vision/aya_vision_configuration.py#L75)
  - `image_token_index` — [`L74`](../../../../../../../raw/code/EasyDeL/easydel/modules/aya_vision/aya_vision_configuration.py#L74)
  - `model_type` — [`L59`](../../../../../../../raw/code/EasyDeL/easydel/modules/aya_vision/aya_vision_configuration.py#L59)
  - `sub_configs` — [`L61`](../../../../../../../raw/code/EasyDeL/easydel/modules/aya_vision/aya_vision_configuration.py#L61)
  - `text_config` — [`L114`](../../../../../../../raw/code/EasyDeL/easydel/modules/aya_vision/aya_vision_configuration.py#L114)
  - `vision_config` — [`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/aya_vision/aya_vision_configuration.py#L104)
  - `vision_feature_layer` — [`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/aya_vision/aya_vision_configuration.py#L84)
  - `vision_feature_select_strategy` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/aya_vision/aya_vision_configuration.py#L83)
- protocol/private: `__init__`[`L63`](../../../../../../../raw/code/EasyDeL/easydel/modules/aya_vision/aya_vision_configuration.py#L63)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`Cohere2Config`](../cohere2/cohere2_configuration.md#Cohere2Config), [`registry`](../../infra/factory.md#registry), [`get_config`](../../infra/factory.md#Registry.get_config), [`SiglipVisionConfig`](../siglip/configuration_siglip.md#SiglipVisionConfig), [`AutoEasyDeLConfig`](../auto/auto_configuration.md#AutoEasyDeLConfig)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`AyaVisionForConditionalGeneration`](modeling_aya_vision.md#AyaVisionForConditionalGeneration), [`AyaVisionModel`](modeling_aya_vision.md#AyaVisionModel), [`layernorm`](modeling_aya_vision.md#AyaVisionMultiModalProjector.layernorm), [`linear_1`](modeling_aya_vision.md#AyaVisionMultiModalProjector.linear_1), [`vision_tower`](modeling_aya_vision.md#AyaVisionModel.vision_tower), [`__init__`](modeling_aya_vision.md#AyaVisionForConditionalGeneration.__init__), [`downsample_factor`](modeling_aya_vision.md#AyaVisionMultiModalProjector.downsample_factor), [`__init__`](modeling_aya_vision.md#AyaVisionModel.__init__), [`vision_feature_layer`](modeling_aya_vision.md#AyaVisionModel.vision_feature_layer), [`__init__`](modeling_aya_vision.md#AyaVisionMultiModalProjector.__init__), [`_config_class`](modeling_aya_vision.md#AyaVisionForConditionalGeneration._config_class)

## Module values
- `logger` — [`L26`](../../../../../../../raw/code/EasyDeL/easydel/modules/aya_vision/aya_vision_configuration.py#L26)

