---
title: 'Module: easydel/modules/llava/llava_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/llava/llava_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.llava.llava_configuration`/
symbols:
  LlavaConfig: LlavaConfig#
  LlavaConfig.vision_feature_layer: LlavaConfig#vision_feature_layer.
  LlavaConfig.vision_config: LlavaConfig#vision_config.
  LlavaConfig.multimodal_projector_bias: LlavaConfig#multimodal_projector_bias.
  logger: logger.
  LlavaConfig.sub_configs: LlavaConfig#sub_configs.
  LlavaConfig.__init__: LlavaConfig#__init__().
  LlavaConfig.image_token_id: LlavaConfig#image_token_id.
  LlavaConfig.projector_hidden_act: LlavaConfig#projector_hidden_act.
  LlavaConfig.model_type: LlavaConfig#model_type.
  LlavaConfig.image_seq_length: LlavaConfig#image_seq_length.
  LlavaConfig.vision_feature_select_strategy: LlavaConfig#vision_feature_select_strategy.
  LlavaConfig.text_config: LlavaConfig#text_config.
  LlavaConfig.get_partition_rules: LlavaConfig#get_partition_rules().
---
# Module: [`easydel/modules/llava/llava_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/llava_configuration.py)

## Classes
### `LlavaConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/llava/llava_configuration.py:30`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/llava_configuration.py#L30)
- doc: This is the configuration class to store the configuration of a \[`LlavaForConditionalGeneration`\].
- signature: `class LlavaConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L121`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/llava_configuration.py#L121) — Returns partition rules for model sharding.
  - `image_seq_length` — [`L80`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/llava_configuration.py#L80)
  - `image_token_id` — [`L78`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/llava_configuration.py#L78)
  - `model_type` — [`L63`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/llava_configuration.py#L63)
  - `multimodal_projector_bias` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/llava_configuration.py#L117)
  - `projector_hidden_act` — [`L79`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/llava_configuration.py#L79)
  - `sub_configs` — [`L64`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/llava_configuration.py#L64)
  - `text_config` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/llava_configuration.py#L116)
  - `vision_config` — [`L108`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/llava_configuration.py#L108)
  - `vision_feature_layer` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/llava_configuration.py#L89)
  - `vision_feature_select_strategy` — [`L88`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/llava_configuration.py#L88)
- protocol/private: `__init__`[`L66`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/llava_configuration.py#L66)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`registry`](../../infra/factory.md#registry), [`get_config`](../../infra/factory.md#Registry.get_config), [`AutoEasyDeLConfig`](../auto/auto_configuration.md#AutoEasyDeLConfig)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`LlavaForConditionalGeneration`](modeling_llava.md#LlavaForConditionalGeneration), [`LlavaModel`](modeling_llava.md#LlavaModel), [`__init__`](modeling_llava.md#LlavaForConditionalGeneration.__init__), [`vision_tower`](modeling_llava.md#LlavaModel.vision_tower), [`linear_1`](modeling_llava.md#LlavaMultiModalProjector.linear_1), [`act`](modeling_llava.md#LlavaMultiModalProjector.act), [`linear_2`](modeling_llava.md#LlavaMultiModalProjector.linear_2), [`__init__`](modeling_llava.md#LlavaModel.__init__), [`vision_feature_layer`](modeling_llava.md#LlavaModel.vision_feature_layer), [`__init__`](modeling_llava.md#LlavaMultiModalProjector.__init__), [`_config_class`](modeling_llava.md#LlavaForConditionalGeneration._config_class), [`rngs`](modeling_llava.md#LlavaMultiModalProjector.rngs)

## Module values
- `logger` — [`L26`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/llava_configuration.py#L26)

