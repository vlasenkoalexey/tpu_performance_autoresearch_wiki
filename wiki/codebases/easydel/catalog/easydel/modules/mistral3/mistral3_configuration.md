---
title: 'Module: easydel/modules/mistral3/mistral3_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/mistral3/mistral3_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.mistral3.mistral3_configuration`/Mistral3Config#
symbols:
  Mistral3Config: ''
  Mistral3Config.vision_config: vision_config.
  Mistral3Config.vision_feature_layer: vision_feature_layer.
  Mistral3Config.layer_types: layer_types.
  Mistral3Config.__init__: __init__().
  Mistral3Config.sub_configs: sub_configs.
  Mistral3Config.text_config: text_config.
  Mistral3Config.multimodal_projector_bias: multimodal_projector_bias.
  Mistral3Config.image_token_index: image_token_index.
  Mistral3Config.projector_hidden_act: projector_hidden_act.
  Mistral3Config.spatial_merge_size: spatial_merge_size.
  Mistral3Config.model_type: model_type.
  Mistral3Config.attribute_map: attribute_map.
  Mistral3Config.is_composition: is_composition.
  Mistral3Config.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/mistral3/mistral3_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_configuration.py)

## Classes
### `Mistral3Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/mistral3/mistral3_configuration.py:25`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_configuration.py#L25)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class Mistral3Config(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_configuration.py#L119) — Returns partition rules for model sharding.
  - `attribute_map` — [`L50`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_configuration.py#L50)
  - `image_token_index` — [`L67`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_configuration.py#L67)
  - `is_composition` — [`L52`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_configuration.py#L52)
  - `layer_types` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_configuration.py#L115)
  - `model_type` — [`L49`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_configuration.py#L49)
  - `multimodal_projector_bias` — [`L113`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_configuration.py#L113)
  - `projector_hidden_act` — [`L68`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_configuration.py#L68)
  - `spatial_merge_size` — [`L114`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_configuration.py#L114)
  - `sub_configs` — [`L51`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_configuration.py#L51)
  - `text_config` — [`L112`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_configuration.py#L112)
  - `vision_config` — [`L87`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_configuration.py#L87)
  - `vision_feature_layer` — [`L69`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_configuration.py#L69)
- protocol/private: `__init__`[`L54`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_configuration.py#L54)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`registry`](../../infra/factory.md#registry), [`get_config`](../../infra/factory.md#Registry.get_config)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`Mistral3ForConditionalGeneration`](modeling_mistral3.md#Mistral3ForConditionalGeneration), [`Mistral3Model`](modeling_mistral3.md#Mistral3Model), [`__init__`](modeling_mistral3.md#Mistral3ForConditionalGeneration.__init__), [`vision_tower`](modeling_mistral3.md#Mistral3Model.vision_tower), [`linear_1`](modeling_mistral3.md#Mistral3MultiModalProjector.linear_1), [`patch_size`](modeling_mistral3.md#Mistral3PatchMerger.patch_size), [`act`](modeling_mistral3.md#Mistral3MultiModalProjector.act), [`linear_2`](modeling_mistral3.md#Mistral3MultiModalProjector.linear_2), [`norm`](modeling_mistral3.md#Mistral3MultiModalProjector.norm), [`patch_merger`](modeling_mistral3.md#Mistral3MultiModalProjector.patch_merger), [`__init__`](modeling_mistral3.md#Mistral3Model.__init__), [`spatial_merge_size`](modeling_mistral3.md#Mistral3PatchMerger.spatial_merge_size), [`vision_feature_layer`](modeling_mistral3.md#Mistral3Model.vision_feature_layer), [`__init__`](modeling_mistral3.md#Mistral3MultiModalProjector.__init__), [`__init__`](modeling_mistral3.md#Mistral3PatchMerger.__init__), [`_config_class`](modeling_mistral3.md#Mistral3ForConditionalGeneration._config_class), [`rngs`](modeling_mistral3.md#Mistral3PatchMerger.rngs)

