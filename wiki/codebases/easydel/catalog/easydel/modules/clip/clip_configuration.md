---
title: 'Module: easydel/modules/clip/clip_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/clip/clip_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.clip.clip_configuration`/
symbols:
  CLIPVisionConfig: CLIPVisionConfig#
  CLIPTextConfig: CLIPTextConfig#
  CLIPConfig.__init__: CLIPConfig#__init__().
  CLIPConfig: CLIPConfig#
  CLIPConfig.from_text_vision_configs: CLIPConfig#from_text_vision_configs().
  CLIPTextConfig.hidden_size: CLIPTextConfig#hidden_size.
  CLIPTextConfig.get_partition_rules: CLIPTextConfig#get_partition_rules.
  CLIPVisionConfig.hidden_size: CLIPVisionConfig#hidden_size.
  CLIPVisionConfig.get_partition_rules: CLIPVisionConfig#get_partition_rules.
  CLIPConfig.sub_configs: CLIPConfig#sub_configs.
  logger: logger.
  CLIPConfig.vision_config: CLIPConfig#vision_config.
  _get_partition_rules: _get_partition_rules().
  CLIPTextConfig.layer_norm_eps: CLIPTextConfig#layer_norm_eps.
  CLIPTextConfig.__init__: CLIPTextConfig#__init__().
  CLIPVisionConfig.__init__: CLIPVisionConfig#__init__().
  CLIPConfig.text_config: CLIPConfig#text_config.
  CLIPTextConfig.intermediate_size: CLIPTextConfig#intermediate_size.
  CLIPTextConfig.attention_dropout: CLIPTextConfig#attention_dropout.
  CLIPVisionConfig.patch_size: CLIPVisionConfig#patch_size.
  CLIPVisionConfig.image_size: CLIPVisionConfig#image_size.
  CLIPVisionConfig.layer_norm_eps: CLIPVisionConfig#layer_norm_eps.
  CLIPTextConfig.projection_dim: CLIPTextConfig#projection_dim.
  CLIPTextConfig.num_hidden_layers: CLIPTextConfig#num_hidden_layers.
  CLIPTextConfig.num_attention_heads: CLIPTextConfig#num_attention_heads.
  CLIPTextConfig.hidden_act: CLIPTextConfig#hidden_act.
  CLIPVisionConfig.num_channels: CLIPVisionConfig#num_channels.
  CLIPTextConfig.model_type: CLIPTextConfig#model_type.
  CLIPTextConfig.base_config_key: CLIPTextConfig#base_config_key.
  CLIPTextConfig.vocab_size: CLIPTextConfig#vocab_size.
  CLIPTextConfig.max_position_embeddings: CLIPTextConfig#max_position_embeddings.
  CLIPTextConfig.initializer_range: CLIPTextConfig#initializer_range.
  CLIPTextConfig.initializer_factor: CLIPTextConfig#initializer_factor.
  CLIPVisionConfig.model_type: CLIPVisionConfig#model_type.
  CLIPVisionConfig.base_config_key: CLIPVisionConfig#base_config_key.
  CLIPVisionConfig.intermediate_size: CLIPVisionConfig#intermediate_size.
  CLIPVisionConfig.projection_dim: CLIPVisionConfig#projection_dim.
  CLIPVisionConfig.num_hidden_layers: CLIPVisionConfig#num_hidden_layers.
  CLIPVisionConfig.num_attention_heads: CLIPVisionConfig#num_attention_heads.
  CLIPVisionConfig.initializer_range: CLIPVisionConfig#initializer_range.
  CLIPVisionConfig.initializer_factor: CLIPVisionConfig#initializer_factor.
  CLIPVisionConfig.attention_dropout: CLIPVisionConfig#attention_dropout.
  CLIPVisionConfig.hidden_act: CLIPVisionConfig#hidden_act.
  CLIPConfig.model_type: CLIPConfig#model_type.
  CLIPConfig.projection_dim: CLIPConfig#projection_dim.
  CLIPConfig.logit_scale_init_value: CLIPConfig#logit_scale_init_value.
  CLIPConfig.initializer_factor: CLIPConfig#initializer_factor.
  CLIPConfig.get_partition_rules: CLIPConfig#get_partition_rules.
---
# Module: [`easydel/modules/clip/clip_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py)

## Classes
### `CLIPConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/clip/clip_configuration.py:232`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L232)
- doc: \[`CLIPConfig`\] is the configuration class to store the configuration of a \[`CLIPModel`\]. It is used to instantiate
- signature: `class CLIPConfig(EasyDeLBaseConfig):`
- members:
  - `from_text_vision_configs(cls, text_config: CLIPTextConfig, vision_config: CLIPVisionConfig, **kwargs)` — [`L365`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L365) — Instantiate a [`CLIPConfig`] (or a derived class) from clip text model configuration and clip vision model
  - `get_partition_rules` — [`L385`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L385)
  - `initializer_factor` — [`L362`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L362)
  - `logit_scale_init_value` — [`L361`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L361)
  - `model_type` — [`L279`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L279)
  - `projection_dim` — [`L360`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L360)
  - `sub_configs` — [`L280`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L280)
  - `text_config` — [`L357`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L357)
  - `vision_config` — [`L358`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L358)
- protocol/private: `__init__`[`L282`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L282)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`CLIPVisionConfig`](clip_configuration.md#CLIPVisionConfig), [`CLIPTextConfig`](clip_configuration.md#CLIPTextConfig), [`to_dict`](../../infra/base_config.md#EasyDeLBaseConfig.to_dict), [`logger`](clip_configuration.md#logger), [`_get_partition_rules`](clip_configuration.md#_get_partition_rules)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`CLIPModel`](modeling_clip.md#CLIPModel), [`visual_projection`](modeling_clip.md#CLIPModel.visual_projection), [`__init__`](modeling_clip.md#CLIPModel.__init__)

### `CLIPTextConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/clip/clip_configuration.py:30`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L30)
- doc: This is the configuration class to store the configuration of a \[`CLIPTextModel`\]. It is used to instantiate a CLIP
- signature: `class CLIPTextConfig(EasyDeLBaseConfig):`
- members:
  - `attention_dropout` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L131)
  - `base_config_key` — [`L92`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L92)
  - `get_partition_rules` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L133)
  - `hidden_act` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L128)
  - `hidden_size` — [`L121`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L121)
  - `initializer_factor` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L130)
  - `initializer_range` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L129)
  - `intermediate_size` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L122)
  - `layer_norm_eps` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L127)
  - `max_position_embeddings` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L126)
  - `model_type` — [`L91`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L91)
  - `num_attention_heads` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L125)
  - `num_hidden_layers` — [`L124`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L124)
  - `projection_dim` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L123)
  - `vocab_size` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L120)
- protocol/private: `__init__`[`L94`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L94)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_get_partition_rules`](clip_configuration.md#_get_partition_rules)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`CLIPTextModel`](modeling_clip.md#CLIPTextModel), [`embed_dim`](modeling_clip.md#CLIPAttention.embed_dim), [`__init__`](clip_configuration.md#CLIPConfig.__init__), [`activation_fn`](modeling_clip.md#CLIPMLP.activation_fn), [`attention_performer`](modeling_clip.md#CLIPAttention.attention_performer), [`final_layer_norm`](modeling_clip.md#CLIPTextTransformer.final_layer_norm), [`layer_norm1`](modeling_clip.md#CLIPEncoderLayer.layer_norm1), [`layer_norm2`](modeling_clip.md#CLIPEncoderLayer.layer_norm2), [`text_projection`](modeling_clip.md#CLIPTextModelWithProjection.text_projection), [`__init__`](modeling_clip.md#CLIPAttention.__init__), [`causal_mask`](modeling_clip.md#CLIPEncoder.causal_mask), [`from_text_vision_configs`](clip_configuration.md#CLIPConfig.from_text_vision_configs), [`num_heads`](modeling_clip.md#CLIPAttention.num_heads), [`fc1`](modeling_clip.md#CLIPMLP.fc1), [`fc2`](modeling_clip.md#CLIPMLP.fc2), [`__init__`](modeling_clip.md#CLIPEncoder.__init__), [`__init__`](modeling_clip.md#CLIPEncoderLayer.__init__), [`__init__`](modeling_clip.md#CLIPMLP.__init__), [`__init__`](modeling_clip.md#CLIPTextModel.__init__), [`__init__`](modeling_clip.md#CLIPTextModelWithProjection.__init__), [`__init__`](modeling_clip.md#CLIPTextTransformer.__init__), [`dropout`](modeling_clip.md#CLIPAttention.dropout), [`sub_configs`](clip_configuration.md#CLIPConfig.sub_configs), [`causal`](modeling_clip.md#CLIPAttention.causal), [`layers`](modeling_clip.md#CLIPEncoder.layers), [`text_config`](clip_configuration.md#CLIPConfig.text_config)

### `CLIPVisionConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/clip/clip_configuration.py:137`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L137)
- doc: This is the configuration class to store the configuration of a \[`CLIPVisionModel`\]. It is used to instantiate a
- signature: `class CLIPVisionConfig(EasyDeLBaseConfig):`
- members:
  - `attention_dropout` — [`L224`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L224)
  - `base_config_key` — [`L193`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L193)
  - `get_partition_rules` — [`L228`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L228)
  - `hidden_act` — [`L226`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L226)
  - `hidden_size` — [`L214`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L214)
  - `image_size` — [`L221`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L221)
  - `initializer_factor` — [`L223`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L223)
  - `initializer_range` — [`L222`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L222)
  - `intermediate_size` — [`L215`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L215)
  - `layer_norm_eps` — [`L225`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L225)
  - `model_type` — [`L192`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L192)
  - `num_attention_heads` — [`L218`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L218)
  - `num_channels` — [`L219`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L219)
  - `num_hidden_layers` — [`L217`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L217)
  - `patch_size` — [`L220`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L220)
  - `projection_dim` — [`L216`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L216)
- protocol/private: `__init__`[`L195`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L195)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_get_partition_rules`](clip_configuration.md#_get_partition_rules)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`CLIPForImageClassification`](modeling_clip.md#CLIPForImageClassification), [`CLIPVisionModel`](modeling_clip.md#CLIPVisionModel), [`__call__`](modeling_clip.md#CLIPVisionEmbeddings.__call__), [`__init__`](clip_configuration.md#CLIPConfig.__init__), [`config`](modeling_clip.md#CLIPVisionEmbeddings.config), [`visual_projection`](modeling_clip.md#CLIPModel.visual_projection), [`post_layernorm`](modeling_clip.md#CLIPVisionTransformer.post_layernorm), [`pre_layrnorm`](modeling_clip.md#CLIPVisionTransformer.pre_layrnorm), [`__init__`](modeling_clip.md#CLIPAttention.__init__), [`__init__`](modeling_clip.md#CLIPForImageClassification.__init__), [`from_text_vision_configs`](clip_configuration.md#CLIPConfig.from_text_vision_configs), [`__init__`](modeling_clip.md#CLIPEncoder.__init__), [`__init__`](modeling_clip.md#CLIPEncoderLayer.__init__), [`__init__`](modeling_clip.md#CLIPMLP.__init__), [`__init__`](modeling_clip.md#CLIPTextEmbeddings.__init__), [`__init__`](modeling_clip.md#CLIPVisionModel.__init__), [`__init__`](modeling_clip.md#CLIPVisionTransformer.__init__), [`sub_configs`](clip_configuration.md#CLIPConfig.sub_configs), [`patch_embedding`](modeling_clip.md#CLIPVisionEmbeddings.patch_embedding), [`vision_config`](clip_configuration.md#CLIPConfig.vision_config), [`__init__`](modeling_clip.md#CLIPVisionEmbeddings.__init__)

## Functions
- `_get_partition_rules(self, *arg, **kwargs)` — [`L25`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L25)

## Module values
- `logger` — [`L22`](../../../../../../../raw/code/EasyDeL/easydel/modules/clip/clip_configuration.py#L22)

