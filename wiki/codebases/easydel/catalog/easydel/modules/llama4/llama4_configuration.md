---
title: 'Module: easydel/modules/llama4/llama4_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/llama4/llama4_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.llama4.llama4_configuration`/
symbols:
  Llama4TextConfig: Llama4TextConfig#
  Llama4VisionConfig: Llama4VisionConfig#
  Llama4Config.text_config: Llama4Config#text_config.
  Llama4Config.vision_config: Llama4Config#vision_config.
  Llama4Config: Llama4Config#
  Llama4VisionConfig.hidden_size: Llama4VisionConfig#hidden_size.
  Llama4VisionConfig.get_partition_rules: Llama4VisionConfig#get_partition_rules.
  Llama4TextConfig.head_dim: Llama4TextConfig#head_dim.
  Llama4TextConfig.get_partition_rules: Llama4TextConfig#get_partition_rules.
  Llama4Config.sub_configs: Llama4Config#sub_configs.
  Llama4Config.__init__: Llama4Config#__init__().
  _patch_hf_llama4_pooler_output: _patch_hf_llama4_pooler_output().
  _get_partition_rules: _get_partition_rules().
  Llama4VisionConfig.patch_size: Llama4VisionConfig#patch_size.
  Llama4TextConfig.hidden_size: Llama4TextConfig#hidden_size.
  Llama4VisionConfig.rope_theta: Llama4VisionConfig#rope_theta.
  Llama4TextConfig.__init__: Llama4TextConfig#__init__().
  Llama4TextConfig.router_jitter_noise: Llama4TextConfig#router_jitter_noise.
  Llama4TextConfig.attention_chunk_size: Llama4TextConfig#attention_chunk_size.
  Llama4Config.get_partition_rules: Llama4Config#get_partition_rules.
  logger: logger.
  _patch_hf_llama4_pooler_output._patched_get_image_features: _patch_hf_llama4_pooler_output()._patched_get_image_features().
  Llama4VisionConfig.num_channels: Llama4VisionConfig#num_channels.
  Llama4VisionConfig.num_attention_heads: Llama4VisionConfig#num_attention_heads.
  Llama4TextConfig.rms_norm_eps: Llama4TextConfig#rms_norm_eps.
  Llama4VisionConfig.num_hidden_layers: Llama4VisionConfig#num_hidden_layers.
  Llama4VisionConfig.image_size: Llama4VisionConfig#image_size.
  Llama4VisionConfig.initializer_range: Llama4VisionConfig#initializer_range.
  Llama4VisionConfig.attention_dropout: Llama4VisionConfig#attention_dropout.
  Llama4TextConfig.attn_temperature_tuning: Llama4TextConfig#attn_temperature_tuning.
  Llama4TextConfig.attn_scale: Llama4TextConfig#attn_scale.
  Llama4TextConfig.floor_scale: Llama4TextConfig#floor_scale.
  Llama4TextConfig.intermediate_size_mlp: Llama4TextConfig#intermediate_size_mlp.
  Llama4TextConfig.num_hidden_layers: Llama4TextConfig#num_hidden_layers.
  Llama4TextConfig.num_attention_heads: Llama4TextConfig#num_attention_heads.
  Llama4TextConfig.use_qk_norm: Llama4TextConfig#use_qk_norm.
  Llama4TextConfig.no_rope_layers: Llama4TextConfig#no_rope_layers.
  Llama4TextConfig.moe_layers: Llama4TextConfig#moe_layers.
  Llama4VisionConfig.model_type: Llama4VisionConfig#model_type.
  Llama4VisionConfig.base_config_key: Llama4VisionConfig#base_config_key.
  Llama4VisionConfig.__init__: Llama4VisionConfig#__init__().
  Llama4VisionConfig.hidden_act: Llama4VisionConfig#hidden_act.
  Llama4VisionConfig.intermediate_size: Llama4VisionConfig#intermediate_size.
  Llama4VisionConfig.vision_output_dim: Llama4VisionConfig#vision_output_dim.
  Llama4VisionConfig.norm_eps: Llama4VisionConfig#norm_eps.
  Llama4VisionConfig.pixel_shuffle_ratio: Llama4VisionConfig#pixel_shuffle_ratio.
  Llama4VisionConfig.projector_input_dim: Llama4VisionConfig#projector_input_dim.
  Llama4VisionConfig.projector_output_dim: Llama4VisionConfig#projector_output_dim.
  Llama4VisionConfig.multi_modal_projector_bias: Llama4VisionConfig#multi_modal_projector_bias.
  Llama4VisionConfig.projector_dropout: Llama4VisionConfig#projector_dropout.
  Llama4VisionConfig.vision_feature_layer: Llama4VisionConfig#vision_feature_layer.
  Llama4VisionConfig.vision_feature_select_strategy: Llama4VisionConfig#vision_feature_select_strategy.
  Llama4TextConfig.model_type: Llama4TextConfig#model_type.
  Llama4TextConfig.vocab_size: Llama4TextConfig#vocab_size.
  Llama4TextConfig.max_position_embeddings: Llama4TextConfig#max_position_embeddings.
  Llama4TextConfig.intermediate_size: Llama4TextConfig#intermediate_size.
  Llama4TextConfig.rope_scaling: Llama4TextConfig#rope_scaling.
  Llama4TextConfig.attention_bias: Llama4TextConfig#attention_bias.
  Llama4TextConfig.num_key_value_heads: Llama4TextConfig#num_key_value_heads.
  Llama4TextConfig.hidden_act: Llama4TextConfig#hidden_act.
  Llama4TextConfig.initializer_range: Llama4TextConfig#initializer_range.
  Llama4TextConfig.use_cache: Llama4TextConfig#use_cache.
  Llama4TextConfig.rope_theta: Llama4TextConfig#rope_theta.
  Llama4TextConfig.attention_dropout: Llama4TextConfig#attention_dropout.
  Llama4TextConfig.num_experts_per_tok: Llama4TextConfig#num_experts_per_tok.
  Llama4TextConfig.num_local_experts: Llama4TextConfig#num_local_experts.
  Llama4TextConfig.output_router_logits: Llama4TextConfig#output_router_logits.
  Llama4TextConfig.router_aux_loss_coef: Llama4TextConfig#router_aux_loss_coef.
  Llama4TextConfig.interleave_moe_layer_step: Llama4TextConfig#interleave_moe_layer_step.
  Llama4TextConfig.layer_types: Llama4TextConfig#layer_types.
  Llama4Config.model_type: Llama4Config#model_type.
  Llama4Config.attribute_map: Llama4Config#attribute_map.
  Llama4Config.boi_token_index: Llama4Config#boi_token_index.
  Llama4Config.eoi_token_index: Llama4Config#eoi_token_index.
  Llama4Config.image_token_index: Llama4Config#image_token_index.
  __all__: __all__.
---
# Module: [`easydel/modules/llama4/llama4_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py)

## Classes
### `Llama4Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/llama4/llama4_configuration.py:352`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L352)
- doc: Top-level configuration for the Llama4 multimodal (vision-language) model.
- signature: `class Llama4Config(EasyDeLBaseConfig):`
- members:
  - `attribute_map` — [`L378`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L378)
  - `boi_token_index` — [`L402`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L402)
  - `eoi_token_index` — [`L403`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L403)
  - `get_partition_rules` — [`L416`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L416)
  - `image_token_index` — [`L404`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L404)
  - `model_type` — [`L376`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L376)
  - `sub_configs` — [`L377`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L377)
  - `text_config` — [`L407`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L407)
  - `vision_config` — [`L395`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L395)
- protocol/private: `__init__`[`L384`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L384)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_fix_parent_kws`](../../infra/base_config.md#EasyDeLBaseConfig._fix_parent_kws), [`Llama4TextConfig`](llama4_configuration.md#Llama4TextConfig), [`Llama4VisionConfig`](llama4_configuration.md#Llama4VisionConfig), [`_get_partition_rules`](llama4_configuration.md#_get_partition_rules), [`logger`](llama4_configuration.md#logger)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](modeling_llama4.md#Llama4TextMoe.__init__), [`Llama4ForConditionalGeneration`](modeling_llama4.md#Llama4ForConditionalGeneration), [`vision_model`](modeling_llama4.md#Llama4ForConditionalGeneration.vision_model), [`__init__`](modeling_llama4.md#Llama4ForConditionalGeneration.__init__), [`__init__`](modeling_llama4.md#Llama4TextExperts.__init__), [`__init__`](modeling_llama4.md#Llama4TextMLP.__init__), [`_config_class`](modeling_llama4.md#Llama4ForConditionalGeneration._config_class)

### `Llama4TextConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/llama4/llama4_configuration.py:175`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L175)
- doc: Configuration for the Llama4 text decoder with interleaved MoE layers.
- signature: `class Llama4TextConfig(EasyDeLBaseConfig):`
- members:
  - `attention_bias` — [`L309`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L309)
  - `attention_chunk_size` — [`L343`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L343)
  - `attention_dropout` — [`L321`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L321)
  - `attn_scale` — [`L299`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L299)
  - `attn_temperature_tuning` — [`L298`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L298)
  - `floor_scale` — [`L300`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L300)
  - `get_partition_rules` — [`L348`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L348)
  - `head_dim` — [`L322`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L322)
  - `hidden_act` — [`L316`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L316)
  - `hidden_size` — [`L303`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L303)
  - `initializer_range` — [`L317`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L317)
  - `interleave_moe_layer_step` — [`L337`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L337)
  - `intermediate_size` — [`L304`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L304)
  - `intermediate_size_mlp` — [`L305`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L305)
  - `layer_types` — [`L346`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L346)
  - `max_position_embeddings` — [`L302`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L302)
  - `model_type` — [`L250`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L250)
  - `moe_layers` — [`L338`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L338)
  - `no_rope_layers` — [`L335`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L335)
  - `num_attention_heads` — [`L307`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L307)
  - `num_experts_per_tok` — [`L325`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L325)
  - `num_hidden_layers` — [`L306`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L306)
  - `num_key_value_heads` — [`L315`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L315)
  - `num_local_experts` — [`L326`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L326)
  - `output_router_logits` — [`L328`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L328)
  - `rms_norm_eps` — [`L318`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L318)
  - `rope_scaling` — [`L308`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L308)
  - `rope_theta` — [`L320`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L320)
  - `router_aux_loss_coef` — [`L329`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L329)
  - `router_jitter_noise` — [`L330`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L330)
  - `use_cache` — [`L319`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L319)
  - `use_qk_norm` — [`L323`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L323)
  - `vocab_size` — [`L301`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L301)
- protocol/private: `__init__`[`L252`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L252)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_get_partition_rules`](llama4_configuration.md#_get_partition_rules)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`Llama4ForCausalLM`](modeling_llama4.md#Llama4ForCausalLM), [`Llama4TextModel`](modeling_llama4.md#Llama4TextModel), [`Llama4ForSequenceClassification`](modeling_llama4.md#Llama4ForSequenceClassification), [`text_config`](llama4_configuration.md#Llama4Config.text_config), [`feed_forward`](modeling_llama4.md#Llama4TextDecoderLayer.feed_forward), [`qk_norm`](modeling_llama4.md#Llama4TextAttention.qk_norm), [`input_layernorm`](modeling_llama4.md#Llama4TextDecoderLayer.input_layernorm), [`post_attention_layernorm`](modeling_llama4.md#Llama4TextDecoderLayer.post_attention_layernorm), [`__init__`](modeling_llama4.md#Llama4ForCausalLM.__init__), [`__init__`](modeling_llama4.md#Llama4ForSequenceClassification.__init__), [`_create_attention_performer`](modeling_llama4.md#Llama4TextAttention._create_attention_performer), [`_create_rotary`](modeling_llama4.md#Llama4TextAttention._create_rotary), [`is_moe_layer`](modeling_llama4.md#Llama4TextDecoderLayer.is_moe_layer), [`attn_temperature_tuning`](modeling_llama4.md#Llama4TextAttention.attn_temperature_tuning), [`__init__`](llama4_configuration.md#Llama4Config.__init__), [`__init__`](modeling_llama4.md#Llama4TextModel.__init__), [`sub_configs`](llama4_configuration.md#Llama4Config.sub_configs), [`attn_scale`](modeling_llama4.md#Llama4TextAttention.attn_scale), [`floor_scale`](modeling_llama4.md#Llama4TextAttention.floor_scale), [`__init__`](modeling_llama4.md#Llama4TextAttention.__init__), [`__init__`](modeling_llama4.md#Llama4TextDecoderLayer.__init__), [`_config_class`](modeling_llama4.md#Llama4ForCausalLM._config_class), [`_config_class`](modeling_llama4.md#Llama4ForSequenceClassification._config_class)

### `Llama4VisionConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/llama4/llama4_configuration.py:72`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L72)
- doc: Configuration for the Llama4 vision encoder and multi-modal projector.
- signature: `class Llama4VisionConfig(EasyDeLBaseConfig):`
- members:
  - `attention_dropout` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L165)
  - `base_config_key` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L123)
  - `get_partition_rules` — [`L171`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L171)
  - `hidden_act` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L150)
  - `hidden_size` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L149)
  - `image_size` — [`L154`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L154)
  - `initializer_range` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L159)
  - `intermediate_size` — [`L153`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L153)
  - `model_type` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L122)
  - `multi_modal_projector_bias` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L163)
  - `norm_eps` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L157)
  - `num_attention_heads` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L158)
  - `num_channels` — [`L152`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L152)
  - `num_hidden_layers` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L151)
  - `patch_size` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L156)
  - `pixel_shuffle_ratio` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L160)
  - `projector_dropout` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L164)
  - `projector_input_dim` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L161)
  - `projector_output_dim` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L162)
  - `rope_theta` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L168)
  - `vision_feature_layer` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L166)
  - `vision_feature_select_strategy` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L167)
  - `vision_output_dim` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L155)
- protocol/private: `__init__`[`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L125)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_get_partition_rules`](llama4_configuration.md#_get_partition_rules)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`Llama4VisionModel`](modeling_llama4.md#Llama4VisionModel), [`vision_config`](llama4_configuration.md#Llama4Config.vision_config), [`head_dim`](modeling_llama4.md#Llama4VisionAttention.head_dim), [`stride`](modeling_llama4.md#Llama4UnfoldConvolution.stride), [`hidden_size`](modeling_llama4.md#Llama4UnfoldConvolution.hidden_size), [`post_attention_layernorm`](modeling_llama4.md#Llama4VisionEncoderLayer.post_attention_layernorm), [`attention_dropout`](modeling_llama4.md#Llama4VisionAttention.attention_dropout), [`embed_dim`](modeling_llama4.md#Llama4VisionAttention.embed_dim), [`hidden_size`](modeling_llama4.md#Llama4VisionModel.hidden_size), [`num_heads`](modeling_llama4.md#Llama4VisionAttention.num_heads), [`input_layernorm`](modeling_llama4.md#Llama4VisionEncoderLayer.input_layernorm), [`layers`](modeling_llama4.md#Llama4VisionEncoder.layers), [`__init__`](llama4_configuration.md#Llama4Config.__init__), [`__init__`](modeling_llama4.md#Llama4UnfoldConvolution.__init__), [`__init__`](modeling_llama4.md#Llama4VisionAttention.__init__), [`__init__`](modeling_llama4.md#Llama4VisionModel.__init__), [`sub_configs`](llama4_configuration.md#Llama4Config.sub_configs), [`scale`](modeling_llama4.md#Llama4VisionModel.scale), [`image_size`](modeling_llama4.md#Llama4VisionModel.image_size), [`num_channels`](modeling_llama4.md#Llama4UnfoldConvolution.num_channels), [`patch_size`](modeling_llama4.md#Llama4VisionModel.patch_size), [`__init__`](modeling_llama4.md#Llama4VisionEncoder.__init__), [`__init__`](modeling_llama4.md#Llama4VisionEncoderLayer.__init__), [`num_channels`](modeling_llama4.md#Llama4VisionModel.num_channels)

## Functions
- `_get_partition_rules(self, *args, **kwargs)` — [`L67`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L67)
- `_patch_hf_llama4_pooler_output()` — [`L26`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L26) — HF compatibility: ensure Llama4 image features expose `pooler_output`.
- `_patched_get_image_features(self, *args, **kwargs)` — [`L42`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L42)

## Module values
- `__all__` — [`L419`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L419)
- `logger` — [`L23`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/llama4_configuration.py#L23)

