---
title: 'Module: easydel/modules/siglip/configuration_siglip.py'
type: catalog
provenance: extracted
module: easydel/modules/siglip/configuration_siglip.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.siglip.configuration_siglip`/
symbols:
  SiglipTextConfig: SiglipTextConfig#
  SiglipVisionConfig: SiglipVisionConfig#
  SiglipConfig.vision_config: SiglipConfig#vision_config.
  SiglipTextConfig.hidden_size: SiglipTextConfig#hidden_size.
  SiglipConfig: SiglipConfig#
  SiglipConfig.from_text_vision_configs: SiglipConfig#from_text_vision_configs().
  SiglipVisionConfig.hidden_size: SiglipVisionConfig#hidden_size.
  SiglipTextConfig.layer_norm_eps: SiglipTextConfig#layer_norm_eps.
  SiglipTextConfig.get_partition_rules: SiglipTextConfig#get_partition_rules.
  SiglipVisionConfig.get_partition_rules: SiglipVisionConfig#get_partition_rules.
  SiglipConfig.sub_configs: SiglipConfig#sub_configs.
  SiglipConfig.__init__: SiglipConfig#__init__().
  SiglipConfig.text_config: SiglipConfig#text_config.
  _get_partition_rules: _get_partition_rules().
  SiglipTextConfig.__init__: SiglipTextConfig#__init__().
  SiglipVisionConfig.__init__: SiglipVisionConfig#__init__().
  SiglipConfig.get_partition_rules: SiglipConfig#get_partition_rules.
  SiglipVisionConfig.image_size: SiglipVisionConfig#image_size.
  SiglipVisionConfig.patch_size: SiglipVisionConfig#patch_size.
  logger: logger.
  SiglipTextConfig.intermediate_size: SiglipTextConfig#intermediate_size.
  SiglipVisionConfig.layer_norm_eps: SiglipVisionConfig#layer_norm_eps.
  SiglipTextConfig.vocab_size: SiglipTextConfig#vocab_size.
  SiglipTextConfig.num_hidden_layers: SiglipTextConfig#num_hidden_layers.
  SiglipTextConfig.num_attention_heads: SiglipTextConfig#num_attention_heads.
  SiglipTextConfig.max_position_embeddings: SiglipTextConfig#max_position_embeddings.
  SiglipTextConfig.hidden_act: SiglipTextConfig#hidden_act.
  SiglipTextConfig.projection_size: SiglipTextConfig#projection_size.
  SiglipVisionConfig.num_channels: SiglipVisionConfig#num_channels.
  SiglipTextConfig.model_type: SiglipTextConfig#model_type.
  SiglipTextConfig.base_config_key: SiglipTextConfig#base_config_key.
  SiglipTextConfig.attention_dropout: SiglipTextConfig#attention_dropout.
  SiglipVisionConfig.model_type: SiglipVisionConfig#model_type.
  SiglipVisionConfig.base_config_key: SiglipVisionConfig#base_config_key.
  SiglipVisionConfig.intermediate_size: SiglipVisionConfig#intermediate_size.
  SiglipVisionConfig.num_hidden_layers: SiglipVisionConfig#num_hidden_layers.
  SiglipVisionConfig.num_attention_heads: SiglipVisionConfig#num_attention_heads.
  SiglipVisionConfig.attention_dropout: SiglipVisionConfig#attention_dropout.
  SiglipVisionConfig.hidden_act: SiglipVisionConfig#hidden_act.
  SiglipConfig.model_type: SiglipConfig#model_type.
  SiglipConfig.initializer_factor: SiglipConfig#initializer_factor.
  __all__: __all__.
---
# Module: [`easydel/modules/siglip/configuration_siglip.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py)

## Classes
### `SiglipConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/siglip/configuration_siglip.py:189`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L189)
- doc: \[`SiglipConfig`\] is the configuration class to store the configuration of a \[`SiglipModel`\]. It is used to
- signature: `class SiglipConfig(EasyDeLBaseConfig):`
- members:
  - `from_text_vision_configs(cls, text_config: SiglipTextConfig, vision_config: SiglipVisionConfig, **kwargs)` — [`L240`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L240) — Instantiate a [`SiglipConfig`] (or a derived class) from siglip text model configuration and siglip vision
  - `get_partition_rules` — [`L260`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L260)
  - `initializer_factor` — [`L237`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L237)
  - `model_type` — [`L209`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L209)
  - `sub_configs` — [`L215`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L215) — ---
  - `text_config` — [`L233`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L233)
  - `vision_config` — [`L234`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L234)
- protocol/private: `__init__`[`L222`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L222)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`SiglipTextConfig`](configuration_siglip.md#SiglipTextConfig), [`SiglipVisionConfig`](configuration_siglip.md#SiglipVisionConfig), [`to_dict`](../../infra/base_config.md#EasyDeLBaseConfig.to_dict), [`read_basics_from_config`](../../infra/base_config.md#EasyDeLBaseConfig.read_basics_from_config), [`_get_partition_rules`](configuration_siglip.md#_get_partition_rules), [`logger`](configuration_siglip.md#logger)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](modeling_siglip.md#SiglipModel.__init__), [`SiglipForImageClassification`](modeling_siglip.md#SiglipForImageClassification), [`SiglipModel`](modeling_siglip.md#SiglipModel), [`__init__`](modeling_siglip.md#SiglipForImageClassification.__init__)

### `SiglipTextConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/siglip/configuration_siglip.py:31`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L31)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read the
- signature: `class SiglipTextConfig(EasyDeLBaseConfig):`
- members:
  - `attention_dropout` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L119)
  - `base_config_key` — [`L85`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L85)
  - `get_partition_rules` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L122)
  - `hidden_act` — [`L118`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L118)
  - `hidden_size` — [`L112`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L112)
  - `intermediate_size` — [`L113`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L113)
  - `layer_norm_eps` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L117)
  - `max_position_embeddings` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L116)
  - `model_type` — [`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L84)
  - `num_attention_heads` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L115)
  - `num_hidden_layers` — [`L114`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L114)
  - `projection_size` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L120)
  - `vocab_size` — [`L111`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L111)
- protocol/private: `__init__`[`L87`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L87)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_get_partition_rules`](configuration_siglip.md#_get_partition_rules)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](modeling_siglip.md#SiglipModel.__init__), [`SiglipTextModel`](modeling_siglip.md#SiglipTextModel), [`activation_fn`](modeling_siglip.md#SiglipMLP.activation_fn), [`attention`](modeling_siglip.md#SiglipMultiheadAttentionPoolingHead.attention), [`final_layer_norm`](modeling_siglip.md#SiglipTextTransformer.final_layer_norm), [`layer_norm1`](modeling_siglip.md#SiglipEncoderLayer.layer_norm1), [`layer_norm2`](modeling_siglip.md#SiglipEncoderLayer.layer_norm2), [`layernorm`](modeling_siglip.md#SiglipMultiheadAttentionPoolingHead.layernorm), [`probe`](modeling_siglip.md#SiglipMultiheadAttentionPoolingHead.probe), [`__init__`](modeling_siglip.md#SiglipTextTransformer.__init__), [`__init__`](modeling_siglip.md#SiglipVisionTransformer.__init__), [`from_text_vision_configs`](configuration_siglip.md#SiglipConfig.from_text_vision_configs), [`position_embedding`](modeling_siglip.md#SiglipTextEmbeddings.position_embedding), [`fc1`](modeling_siglip.md#SiglipMLP.fc1), [`fc2`](modeling_siglip.md#SiglipMLP.fc2), [`head`](modeling_siglip.md#SiglipTextTransformer.head), [`post_layernorm`](modeling_siglip.md#SiglipVisionTransformer.post_layernorm), [`token_embedding`](modeling_siglip.md#SiglipTextEmbeddings.token_embedding), [`__init__`](modeling_siglip.md#SiglipTextEmbeddings.__init__), [`__init__`](modeling_siglip.md#SiglipTextModel.__init__), [`sub_configs`](configuration_siglip.md#SiglipConfig.sub_configs), [`layers`](modeling_siglip.md#SiglipEncoder.layers), [`text_config`](configuration_siglip.md#SiglipConfig.text_config), [`__init__`](modeling_siglip.md#SiglipEncoder.__init__), [`__init__`](modeling_siglip.md#SiglipEncoderLayer.__init__), [`__init__`](modeling_siglip.md#SiglipMLP.__init__), [`__init__`](modeling_siglip.md#SiglipMultiheadAttentionPoolingHead.__init__)

### `SiglipVisionConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/siglip/configuration_siglip.py:126`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L126)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read the
- signature: `class SiglipVisionConfig(EasyDeLBaseConfig):`
- members:
  - `attention_dropout` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L181)
  - `base_config_key` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L156)
  - `get_partition_rules` — [`L185`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L185)
  - `hidden_act` — [`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L183)
  - `hidden_size` — [`L174`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L174)
  - `image_size` — [`L180`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L180)
  - `intermediate_size` — [`L175`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L175)
  - `layer_norm_eps` — [`L182`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L182)
  - `model_type` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L155)
  - `num_attention_heads` — [`L177`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L177)
  - `num_channels` — [`L178`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L178)
  - `num_hidden_layers` — [`L176`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L176)
  - `patch_size` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L179)
- protocol/private: `__init__`[`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L158)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_get_partition_rules`](configuration_siglip.md#_get_partition_rules)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`SiglipVisionModel`](modeling_siglip.md#SiglipVisionModel), [`__init__`](modeling_siglip.md#SiglipModel.__init__), [`vision_config`](configuration_siglip.md#SiglipConfig.vision_config), [`layernorm`](../aya_vision/modeling_aya_vision.md#AyaVisionMultiModalProjector.layernorm), [`linear_1`](../aya_vision/modeling_aya_vision.md#AyaVisionMultiModalProjector.linear_1), [`mm_input_projection_weight`](../gemma3/modeling_gemma3.md#Gemma3MultiModalProjector.mm_input_projection_weight), [`mm_soft_emb_norm`](../gemma3/modeling_gemma3.md#Gemma3MultiModalProjector.mm_soft_emb_norm), [`patches_per_image`](../gemma3/modeling_gemma3.md#Gemma3MultiModalProjector.patches_per_image), [`patch_embedding`](modeling_siglip.md#SiglipVisionEmbeddings.patch_embedding), [`patch_size`](modeling_siglip.md#SiglipVisionEmbeddings.patch_size), [`vision_feature_layer`](../aya_vision/aya_vision_configuration.md#AyaVisionConfig.vision_feature_layer), [`from_text_vision_configs`](configuration_siglip.md#SiglipConfig.from_text_vision_configs), [`__init__`](../gemma3/gemma3_configuration.md#Gemma3Config.__init__), [`__init__`](modeling_siglip.md#SiglipVisionModel.__init__), [`sub_configs`](../gemma3/gemma3_configuration.md#Gemma3Config.sub_configs), [`sub_configs`](configuration_siglip.md#SiglipConfig.sub_configs), [`embed_dim`](modeling_siglip.md#SiglipVisionEmbeddings.embed_dim), [`image_size`](modeling_siglip.md#SiglipVisionEmbeddings.image_size), [`__init__`](modeling_siglip.md#SiglipVisionEmbeddings.__init__)

## Functions
- `_get_partition_rules(self, *args, **kwargs)` — [`L26`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L26)

## Module values
- `__all__` — [`L263`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L263)
- `logger` — [`L23`](../../../../../../../raw/code/EasyDeL/easydel/modules/siglip/configuration_siglip.py#L23)

