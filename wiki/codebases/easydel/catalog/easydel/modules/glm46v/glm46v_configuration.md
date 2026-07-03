---
title: 'Module: easydel/modules/glm46v/glm46v_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/glm46v/glm46v_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.glm46v.glm46v_configuration`/
symbols:
  Glm46VConfig: Glm46VConfig#
  Glm46VConfig.vision_config: Glm46VConfig#vision_config.
  Glm46VConfig.text_config: Glm46VConfig#text_config.
  Glm46VConfig.sub_configs: Glm46VConfig#sub_configs.
  Glm46VConfig.__init__: Glm46VConfig#__init__().
  Glm46VConfig.get_text_config: Glm46VConfig#get_text_config().
  Glm46VConfig.get_vision_config: Glm46VConfig#get_vision_config().
  Glm46VConfig.video_end_token_id: Glm46VConfig#video_end_token_id.
  Glm46VConfig.image_token_id: Glm46VConfig#image_token_id.
  Glm46VConfig.video_token_id: Glm46VConfig#video_token_id.
  Glm46VConfig.model_type: Glm46VConfig#model_type.
  Glm46VConfig.keys_to_ignore_at_inference: Glm46VConfig#keys_to_ignore_at_inference.
  Glm46VConfig.image_start_token_id: Glm46VConfig#image_start_token_id.
  Glm46VConfig.image_end_token_id: Glm46VConfig#image_end_token_id.
  Glm46VConfig.video_start_token_id: Glm46VConfig#video_start_token_id.
  Glm46VConfig.get_partition_rules: Glm46VConfig#get_partition_rules().
  __all__: __all__.
---
# Module: [`easydel/modules/glm46v/glm46v_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py)

## Classes
### `Glm46VConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/glm46v/glm46v_configuration.py:26`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py#L26)
- doc: Configuration class for the GLM-4.6V multimodal vision-language model.
- signature: `class Glm46VConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py#L119) — Returns partition rules for model sharding.
  - `get_text_config(self, decoder: bool = True)` — [`L112`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py#L112)
  - `get_vision_config(self)` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py#L116)
  - `image_end_token_id` — [`L106`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py#L106)
  - `image_start_token_id` — [`L105`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py#L105)
  - `image_token_id` — [`L103`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py#L103)
  - `keys_to_ignore_at_inference` — [`L74`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py#L74)
  - `model_type` — [`L72`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py#L72)
  - `sub_configs` — [`L73`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py#L73)
  - `text_config` — [`L97`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py#L97)
  - `video_end_token_id` — [`L108`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py#L108)
  - `video_start_token_id` — [`L107`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py#L107)
  - `video_token_id` — [`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py#L104)
  - `vision_config` — [`L90`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py#L90)
- protocol/private: `__init__`[`L76`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py#L76)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_fix_parent_kws`](../../infra/base_config.md#EasyDeLBaseConfig._fix_parent_kws), [`Glm4vTextConfig`](../glm4v/glm4v_configuration.md#Glm4vTextConfig), [`Glm4vVisionConfig`](../glm4v/glm4v_configuration.md#Glm4vVisionConfig)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`__init__`](modeling_glm46v.md#Glm46VForConditionalGeneration.__init__), [`Glm46VForConditionalGeneration`](modeling_glm46v.md#Glm46VForConditionalGeneration), [`Glm46VModel`](modeling_glm46v.md#Glm46VModel), [`__init__`](modeling_glm46v.md#Glm46VModel.__init__), [`vocab_size`](modeling_glm46v.md#Glm46VForConditionalGeneration.vocab_size), [`_config_class`](modeling_glm46v.md#Glm46VForConditionalGeneration._config_class)

## Module values
- `__all__` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/glm46v_configuration.py#L133)

