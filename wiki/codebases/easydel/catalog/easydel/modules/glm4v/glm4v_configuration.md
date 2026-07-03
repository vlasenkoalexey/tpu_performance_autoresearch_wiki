---
title: 'Module: easydel/modules/glm4v/glm4v_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/glm4v/glm4v_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.glm4v.glm4v_configuration`/
symbols:
  Glm4vTextConfig: Glm4vTextConfig#
  Glm4vVisionConfig: Glm4vVisionConfig#
  Glm4vVisionConfig.hidden_size: Glm4vVisionConfig#hidden_size.
  Glm4vConfig: Glm4vConfig#
  Glm4vConfig.vision_config: Glm4vConfig#vision_config.
  Glm4vConfig.text_config: Glm4vConfig#text_config.
  Glm4vTextConfig.hidden_size: Glm4vTextConfig#hidden_size.
  Glm4vVisionConfig.spatial_merge_size: Glm4vVisionConfig#spatial_merge_size.
  Glm4vVisionConfig.intermediate_size: Glm4vVisionConfig#intermediate_size.
  Glm4vTextConfig.rms_norm_eps: Glm4vTextConfig#rms_norm_eps.
  Glm4vConfig.sub_configs: Glm4vConfig#sub_configs.
  Glm4vConfig.__init__: Glm4vConfig#__init__().
  Glm4vConfig.get_text_config: Glm4vConfig#get_text_config().
  Glm4vConfig.get_vision_config: Glm4vConfig#get_vision_config().
  Glm4vVisionConfig.patch_size: Glm4vVisionConfig#patch_size.
  Glm4vVisionConfig.rms_norm_eps: Glm4vVisionConfig#rms_norm_eps.
  Glm4vVisionConfig.num_heads: Glm4vVisionConfig#num_heads.
  Glm4vTextConfig.vocab_size: Glm4vTextConfig#vocab_size.
  Glm4vTextConfig.initializer_range: Glm4vTextConfig#initializer_range.
  Glm4vVisionConfig.__init__: Glm4vVisionConfig#__init__().
  Glm4vTextConfig.rope_scaling: Glm4vTextConfig#rope_scaling.
  Glm4vTextConfig._external_rope_config_kwargs: Glm4vTextConfig#_external_rope_config_kwargs.
  Glm4vConfig.video_end_token_id: Glm4vConfig#video_end_token_id.
  Glm4vVisionConfig.hidden_act: Glm4vVisionConfig#hidden_act.
  Glm4vVisionConfig.in_channels: Glm4vVisionConfig#in_channels.
  Glm4vVisionConfig.temporal_patch_size: Glm4vVisionConfig#temporal_patch_size.
  Glm4vVisionConfig.out_hidden_size: Glm4vVisionConfig#out_hidden_size.
  Glm4vTextConfig.intermediate_size: Glm4vTextConfig#intermediate_size.
  _rope_scaling_from_rope_parameters: _rope_scaling_from_rope_parameters().
  Glm4vVisionConfig.depth: Glm4vVisionConfig#depth.
  Glm4vVisionConfig.image_size: Glm4vVisionConfig#image_size.
  Glm4vTextConfig.num_hidden_layers: Glm4vTextConfig#num_hidden_layers.
  Glm4vTextConfig.hidden_act: Glm4vTextConfig#hidden_act.
  Glm4vConfig.image_token_id: Glm4vConfig#image_token_id.
  Glm4vConfig.video_token_id: Glm4vConfig#video_token_id.
  Glm4vVisionConfig.model_type: Glm4vVisionConfig#model_type.
  Glm4vVisionConfig.base_config_key: Glm4vVisionConfig#base_config_key.
  Glm4vVisionConfig.attention_bias: Glm4vVisionConfig#attention_bias.
  Glm4vVisionConfig.attention_dropout: Glm4vVisionConfig#attention_dropout.
  Glm4vVisionConfig.num_attention_heads: Glm4vVisionConfig#num_attention_heads.
  Glm4vVisionConfig.initializer_range: Glm4vVisionConfig#initializer_range.
  Glm4vVisionConfig.get_partition_rules: Glm4vVisionConfig#get_partition_rules().
  Glm4vTextConfig.model_type: Glm4vTextConfig#model_type.
  Glm4vTextConfig.base_config_key: Glm4vTextConfig#base_config_key.
  Glm4vTextConfig.keys_to_ignore_at_inference: Glm4vTextConfig#keys_to_ignore_at_inference.
  Glm4vTextConfig.__init__: Glm4vTextConfig#__init__().
  Glm4vTextConfig.num_attention_heads: Glm4vTextConfig#num_attention_heads.
  Glm4vTextConfig.num_key_value_heads: Glm4vTextConfig#num_key_value_heads.
  Glm4vTextConfig.head_dim: Glm4vTextConfig#head_dim.
  Glm4vTextConfig.max_position_embeddings: Glm4vTextConfig#max_position_embeddings.
  Glm4vTextConfig.use_cache: Glm4vTextConfig#use_cache.
  Glm4vTextConfig.attention_dropout: Glm4vTextConfig#attention_dropout.
  Glm4vTextConfig.attention_bias: Glm4vTextConfig#attention_bias.
  Glm4vTextConfig.partial_rotary_factor: Glm4vTextConfig#partial_rotary_factor.
  Glm4vTextConfig.rope_theta: Glm4vTextConfig#rope_theta.
  Glm4vTextConfig.get_partition_rules: Glm4vTextConfig#get_partition_rules().
  Glm4vConfig.model_type: Glm4vConfig#model_type.
  Glm4vConfig.keys_to_ignore_at_inference: Glm4vConfig#keys_to_ignore_at_inference.
  Glm4vConfig.image_start_token_id: Glm4vConfig#image_start_token_id.
  Glm4vConfig.image_end_token_id: Glm4vConfig#image_end_token_id.
  Glm4vConfig.video_start_token_id: Glm4vConfig#video_start_token_id.
  Glm4vConfig.get_partition_rules: Glm4vConfig#get_partition_rules().
  __all__: __all__.
---
# Module: [`easydel/modules/glm4v/glm4v_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py)

## Classes
### `Glm4vConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/glm4v/glm4v_configuration.py:278`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L278)
- doc: Configuration class for the GLM4V multimodal vision-language model.
- signature: `class Glm4vConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L373`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L373) — Returns partition rules for model sharding.
  - `get_text_config(self, decoder: bool = True)` — [`L366`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L366)
  - `get_vision_config(self)` — [`L370`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L370)
  - `image_end_token_id` — [`L360`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L360)
  - `image_start_token_id` — [`L359`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L359)
  - `image_token_id` — [`L357`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L357)
  - `keys_to_ignore_at_inference` — [`L328`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L328)
  - `model_type` — [`L323`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L323)
  - `sub_configs` — [`L324`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L324)
  - `text_config` — [`L351`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L351)
  - `video_end_token_id` — [`L362`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L362)
  - `video_start_token_id` — [`L361`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L361)
  - `video_token_id` — [`L358`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L358)
  - `vision_config` — [`L344`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L344)
- protocol/private: `__init__`[`L330`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L330)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_fix_parent_kws`](../../infra/base_config.md#EasyDeLBaseConfig._fix_parent_kws), [`Glm4vTextConfig`](glm4v_configuration.md#Glm4vTextConfig), [`Glm4vVisionConfig`](glm4v_configuration.md#Glm4vVisionConfig)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`Glm4vModel`](modeling_glm4v.md#Glm4vModel), [`Glm4vVisionModel`](modeling_glm4v.md#Glm4vVisionModel), [`__init__`](modeling_glm4v.md#Glm4vForConditionalGeneration.__init__), [`Glm4vForConditionalGeneration`](modeling_glm4v.md#Glm4vForConditionalGeneration), [`visual`](modeling_glm4v.md#Glm4vModel.visual), [`language_model`](modeling_glm4v.md#Glm4vModel.language_model), [`__init__`](modeling_glm4v.md#Glm4vModel.__init__), [`vocab_size`](modeling_glm4v.md#Glm4vForConditionalGeneration.vocab_size), [`_config_class`](modeling_glm4v.md#Glm4vForConditionalGeneration._config_class)

### `Glm4vTextConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/glm4v/glm4v_configuration.py:160`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L160)
- doc: Configuration class for the GLM4V text decoder.
- signature: `class Glm4vTextConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L263`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L263) — Returns partition rules for model sharding.
  - `attention_bias` — [`L248`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L248)
  - `attention_dropout` — [`L247`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L247)
  - `base_config_key` — [`L209`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L209)
  - `head_dim` — [`L241`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L241)
  - `hidden_act` — [`L242`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L242)
  - `hidden_size` — [`L236`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L236)
  - `initializer_range` — [`L244`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L244)
  - `intermediate_size` — [`L237`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L237)
  - `keys_to_ignore_at_inference` — [`L210`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L210)
  - `max_position_embeddings` — [`L243`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L243)
  - `model_type` — [`L208`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L208)
  - `num_attention_heads` — [`L239`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L239)
  - `num_hidden_layers` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L238)
  - `num_key_value_heads` — [`L240`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L240)
  - `partial_rotary_factor` — [`L249`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L249)
  - `rms_norm_eps` — [`L245`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L245)
  - `rope_scaling` — [`L254`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L254)
  - `rope_theta` — [`L253`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L253)
  - `use_cache` — [`L246`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L246)
  - `vocab_size` — [`L235`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L235)
- protocol/private: `__init__`[`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L212), `_external_rope_config_kwargs`[`L256`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L256)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_rope_scaling_from_rope_parameters`](glm4v_configuration.md#_rope_scaling_from_rope_parameters)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`embed_tokens`](modeling_glm4v.md#Glm4vTextModel.embed_tokens), [`Glm4vTextModel`](modeling_glm4v.md#Glm4vTextModel), [`_create_o_proj`](modeling_glm4v.md#Glm4vTextAttention._create_o_proj), [`down_proj`](modeling_glm4v.md#Glm4vTextMLP.down_proj), [`gate_up_proj`](modeling_glm4v.md#Glm4vTextMLP.gate_up_proj), [`input_layernorm`](modeling_glm4v.md#Glm4vTextDecoderLayer.input_layernorm), [`norm`](modeling_glm4v.md#Glm4vTextModel.norm), [`post_attention_layernorm`](modeling_glm4v.md#Glm4vTextDecoderLayer.post_attention_layernorm), [`post_mlp_layernorm`](modeling_glm4v.md#Glm4vTextDecoderLayer.post_mlp_layernorm), [`post_self_attn_layernorm`](modeling_glm4v.md#Glm4vTextDecoderLayer.post_self_attn_layernorm), [`_create_rotary`](modeling_glm4v.md#Glm4vTextAttention._create_rotary), [`act_fn`](modeling_glm4v.md#Glm4vTextMLP.act_fn), [`__init__`](../glm46v/glm46v_configuration.md#Glm46VConfig.__init__), [`__init__`](glm4v_configuration.md#Glm4vConfig.__init__), [`__init__`](modeling_glm4v.md#Glm4vTextAttention.__init__), [`__init__`](modeling_glm4v.md#Glm4vTextModel.__init__), [`get_text_config`](../glm46v/glm46v_configuration.md#Glm46VConfig.get_text_config), [`get_text_config`](glm4v_configuration.md#Glm4vConfig.get_text_config), [`sub_configs`](../glm46v/glm46v_configuration.md#Glm46VConfig.sub_configs), [`sub_configs`](glm4v_configuration.md#Glm4vConfig.sub_configs), [`vocab_size`](../glm46v/modeling_glm46v.md#Glm46VForConditionalGeneration.vocab_size), [`vocab_size`](modeling_glm4v.md#Glm4vForConditionalGeneration.vocab_size), [`layers`](modeling_glm4v.md#Glm4vTextModel.layers), [`__init__`](modeling_glm4v.md#Glm4vTextDecoderLayer.__init__), [`__init__`](modeling_glm4v.md#Glm4vTextMLP.__init__), [`config_class`](modeling_glm4v.md#Glm4vTextModel.config_class)

### `Glm4vVisionConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/glm4v/glm4v_configuration.py:65`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L65)
- doc: Configuration class for the GLM4V vision encoder.
- signature: `class Glm4vVisionConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L145) — Returns partition rules for model sharding.
  - `attention_bias` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L131)
  - `attention_dropout` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L132)
  - `base_config_key` — [`L106`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L106)
  - `depth` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L128)
  - `hidden_act` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L130)
  - `hidden_size` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L129)
  - `image_size` — [`L136`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L136)
  - `in_channels` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L135)
  - `initializer_range` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L143)
  - `intermediate_size` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L142)
  - `model_type` — [`L105`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L105)
  - `num_attention_heads` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L134)
  - `num_heads` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L133)
  - `out_hidden_size` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L141)
  - `patch_size` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L137)
  - `rms_norm_eps` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L138)
  - `spatial_merge_size` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L139)
  - `temporal_patch_size` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L140)
- protocol/private: `__init__`[`L108`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L108)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`__init__`](../glm46v/modeling_glm46v.md#Glm46VForConditionalGeneration.__init__), [`__init__`](modeling_glm4v.md#Glm4vForConditionalGeneration.__init__), [`post_layernorm`](modeling_glm4v.md#Glm4vVisionModel.post_layernorm), [`merger`](modeling_glm4v.md#Glm4vVisionModel.merger), [`down_proj`](modeling_glm4v.md#Glm4vVisionMLP.down_proj), [`downsample`](modeling_glm4v.md#Glm4vVisionModel.downsample), [`gate_proj`](modeling_glm4v.md#Glm4vVisionMLP.gate_proj), [`hidden_size`](modeling_glm4v.md#Glm4vVisionPatchEmbed.hidden_size), [`norm1`](modeling_glm4v.md#Glm4vVisionBlock.norm1), [`norm2`](modeling_glm4v.md#Glm4vVisionBlock.norm2), [`post_conv_layernorm`](modeling_glm4v.md#Glm4vVisionModel.post_conv_layernorm), [`up_proj`](modeling_glm4v.md#Glm4vVisionMLP.up_proj), [`spatial_merge_size`](modeling_glm4v.md#Glm4vVisionModel.spatial_merge_size), [`pos_embed`](modeling_glm4v.md#Glm4vVisionModel.pos_embed), [`hidden_size`](modeling_glm4v.md#Glm4vVisionAttention.hidden_size), [`act`](modeling_glm4v.md#Glm4vVisionMLP.act), [`blocks`](modeling_glm4v.md#Glm4vVisionModel.blocks), [`head_dim`](modeling_glm4v.md#Glm4vVisionAttention.head_dim), [`proj`](modeling_glm4v.md#Glm4vVisionPatchEmbed.proj), [`__init__`](../glm46v/glm46v_configuration.md#Glm46VConfig.__init__), [`__init__`](glm4v_configuration.md#Glm4vConfig.__init__), [`__init__`](modeling_glm4v.md#Glm4vVisionModel.__init__), [`get_vision_config`](../glm46v/glm46v_configuration.md#Glm46VConfig.get_vision_config), [`get_vision_config`](glm4v_configuration.md#Glm4vConfig.get_vision_config), [`reform_param`](modeling_glm4v.md#Glm4vVisionModel.reform_param), [`sub_configs`](../glm46v/glm46v_configuration.md#Glm46VConfig.sub_configs), [`sub_configs`](glm4v_configuration.md#Glm4vConfig.sub_configs), [`num_heads`](modeling_glm4v.md#Glm4vVisionAttention.num_heads), [`patch_size`](modeling_glm4v.md#Glm4vVisionPatchEmbed.patch_size), [`in_channels`](modeling_glm4v.md#Glm4vVisionPatchEmbed.in_channels), [`temporal_patch_size`](modeling_glm4v.md#Glm4vVisionPatchEmbed.temporal_patch_size), [`__init__`](modeling_glm4v.md#Glm4vVisionAttention.__init__), [`__init__`](modeling_glm4v.md#Glm4vVisionBlock.__init__), [`__init__`](modeling_glm4v.md#Glm4vVisionMLP.__init__), [`__init__`](modeling_glm4v.md#Glm4vVisionPatchEmbed.__init__), [`config_class`](modeling_glm4v.md#Glm4vVisionModel.config_class), [`define_network`](modeling_glm4v.md#Glm4vVisionAttention.define_network)  (+2 more)

## Functions
- `_rope_scaling_from_rope_parameters(rope_parameters: dict[str, typing.Any] | None, rope_scaling: dict[str, typing.Any] | None)` — [`L24`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L24)

## Module values
- `__all__` — [`L387`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4v/glm4v_configuration.py#L387)

