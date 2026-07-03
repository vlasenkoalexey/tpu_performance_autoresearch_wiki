---
title: 'Module: easydel/modules/qwen3_vl/qwen3_vl_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/qwen3_vl/qwen3_vl_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.qwen3_vl.qwen3_vl_configuration`/Qwen3VL
symbols:
  Qwen3VLVisionConfig: VisionConfig#
  Qwen3VLTextConfig.get_mask_details: TextConfig#get_mask_details().
  Qwen3VLConfig: Config#
  Qwen3VLTextConfig: TextConfig#
  Qwen3VLVisionConfig.hidden_size: VisionConfig#hidden_size.
  Qwen3VLConfig.text_config: Config#text_config.
  Qwen3VLConfig.vision_config: Config#vision_config.
  Qwen3VLTextConfig.hidden_size: TextConfig#hidden_size.
  Qwen3VLTextConfig.layer_types: TextConfig#layer_types.
  Qwen3VLConfig.sub_configs: Config#sub_configs.
  Qwen3VLConfig.__init__: Config#__init__().
  Qwen3VLConfig.get_text_config: Config#get_text_config().
  Qwen3VLVisionConfig.spatial_merge_size: VisionConfig#spatial_merge_size.
  Qwen3VLVisionConfig.__init__: VisionConfig#__init__().
  Qwen3VLVisionConfig.patch_size: VisionConfig#patch_size.
  Qwen3VLVisionConfig.num_heads: VisionConfig#num_heads.
  Qwen3VLTextConfig.initializer_range: TextConfig#initializer_range.
  Qwen3VLTextConfig.intermediate_size: TextConfig#intermediate_size.
  Qwen3VLTextConfig.sliding_window: TextConfig#sliding_window.
  Qwen3VLTextConfig.rms_norm_eps: TextConfig#rms_norm_eps.
  Qwen3VLTextConfig.num_hidden_layers: TextConfig#num_hidden_layers.
  Qwen3VLVisionConfig.embed_dim: VisionConfig#embed_dim.
  Qwen3VLTextConfig.__init__: TextConfig#__init__().
  Qwen3VLConfig.vision_end_token_id: Config#vision_end_token_id.
  Qwen3VLVisionConfig.temporal_patch_size: VisionConfig#temporal_patch_size.
  Qwen3VLVisionConfig.in_channels: VisionConfig#in_channels.
  Qwen3VLVisionConfig.intermediate_size: VisionConfig#intermediate_size.
  Qwen3VLVisionConfig.num_position_embeddings: VisionConfig#num_position_embeddings.
  Qwen3VLTextConfig.use_sliding_window: TextConfig#use_sliding_window.
  Qwen3VLVisionConfig.out_hidden_size: VisionConfig#out_hidden_size.
  Qwen3VLVisionConfig.hidden_act: VisionConfig#hidden_act.
  Qwen3VLVisionConfig.depth: VisionConfig#depth.
  Qwen3VLVisionConfig.deepstack_visual_indexes: VisionConfig#deepstack_visual_indexes.
  Qwen3VLTextConfig.hidden_act: TextConfig#hidden_act.
  Qwen3VLTextConfig.vocab_size: TextConfig#vocab_size.
  Qwen3VLConfig.image_token_id: Config#image_token_id.
  Qwen3VLConfig.video_token_id: Config#video_token_id.
  Qwen3VLTextConfig.max_window_layers: TextConfig#max_window_layers.
  Qwen3VLVisionConfig.model_type: VisionConfig#model_type.
  Qwen3VLVisionConfig.base_config_key: VisionConfig#base_config_key.
  Qwen3VLVisionConfig.num_attention_heads: VisionConfig#num_attention_heads.
  Qwen3VLVisionConfig.tokens_per_second: VisionConfig#tokens_per_second.
  Qwen3VLVisionConfig.initializer_range: VisionConfig#initializer_range.
  Qwen3VLTextConfig.model_type: TextConfig#model_type.
  Qwen3VLTextConfig.base_config_key: TextConfig#base_config_key.
  Qwen3VLTextConfig.num_attention_heads: TextConfig#num_attention_heads.
  Qwen3VLTextConfig.num_key_value_heads: TextConfig#num_key_value_heads.
  Qwen3VLTextConfig.head_dim: TextConfig#head_dim.
  Qwen3VLTextConfig.max_position_embeddings: TextConfig#max_position_embeddings.
  Qwen3VLTextConfig.use_cache: TextConfig#use_cache.
  Qwen3VLTextConfig.tie_word_embeddings: TextConfig#tie_word_embeddings.
  Qwen3VLTextConfig.rope_theta: TextConfig#rope_theta.
  Qwen3VLTextConfig.attention_bias: TextConfig#attention_bias.
  Qwen3VLTextConfig.attention_dropout: TextConfig#attention_dropout.
  Qwen3VLTextConfig.rope_scaling: TextConfig#rope_scaling.
  Qwen3VLConfig.model_type: Config#model_type.
  Qwen3VLConfig.keys_to_ignore_at_inference: Config#keys_to_ignore_at_inference.
  Qwen3VLConfig.vision_start_token_id: Config#vision_start_token_id.
  Qwen3VLConfig.get_partition_rules: Config#get_partition_rules().
---
# Module: [`easydel/modules/qwen3_vl/qwen3_vl_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py)

## Classes
### `Qwen3VLConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/qwen3_vl/qwen3_vl_configuration.py:195`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L195)
- doc: Main configuration class for Qwen3-VL multimodal model.
- signature: `class Qwen3VLConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L256`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L256) — Returns partition rules for model sharding.
  - `get_text_config(self, decoder: bool = True)` — [`L245`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L245) — Get the text configuration for the model.
  - `image_token_id` — [`L239`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L239)
  - `keys_to_ignore_at_inference` — [`L216`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L216)
  - `model_type` — [`L211`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L211)
  - `sub_configs` — [`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L212)
  - `text_config` — [`L235`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L235)
  - `video_token_id` — [`L240`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L240)
  - `vision_config` — [`L230`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L230)
  - `vision_end_token_id` — [`L242`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L242)
  - `vision_start_token_id` — [`L241`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L241)
- protocol/private: `__init__`[`L218`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L218)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_fix_parent_kws`](../../infra/base_config.md#EasyDeLBaseConfig._fix_parent_kws), [`Qwen3VLVisionConfig`](qwen3_vl_configuration.md#Qwen3VLVisionConfig), [`Qwen3VLTextConfig`](qwen3_vl_configuration.md#Qwen3VLTextConfig)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`__init__`](../qwen3_5/modeling_qwen3_5.md#Qwen3_5Model.__init__), [`Qwen3VLModel`](modeling_qwen3_vl.md#Qwen3VLModel), [`Qwen3VisionTransformerPretrainedModel`](modeling_qwen3_vl.md#Qwen3VisionTransformerPretrainedModel), [`Qwen3VLForConditionalGeneration`](modeling_qwen3_vl.md#Qwen3VLForConditionalGeneration), [`__init__`](modeling_qwen3_vl.md#Qwen3VLForConditionalGeneration.__init__), [`language_model`](modeling_qwen3_vl.md#Qwen3VLModel.language_model), [`visual`](modeling_qwen3_vl.md#Qwen3VLModel.visual), [`__init__`](modeling_qwen3_vl.md#Qwen3VLModel.__init__), [`_config_class`](modeling_qwen3_vl.md#Qwen3VLForConditionalGeneration._config_class), [`vocab_size`](modeling_qwen3_vl.md#Qwen3VLForConditionalGeneration.vocab_size)

### `Qwen3VLTextConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/qwen3_vl/qwen3_vl_configuration.py:97`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L97)
- doc: Configuration class for Qwen3-VL text/language model.
- signature: `class Qwen3VLTextConfig(EasyDeLBaseConfig):`
- members:
  - `get_mask_details(self)` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L181) — Get attention mask details for sliding window attention.
  - `attention_bias` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L169)
  - `attention_dropout` — [`L170`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L170)
  - `base_config_key` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L127)
  - `head_dim` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L161)
  - `hidden_act` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L162)
  - `hidden_size` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L156)
  - `initializer_range` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L164)
  - `intermediate_size` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L157)
  - `layer_types` — [`L177`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L177)
  - `max_position_embeddings` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L163)
  - `max_window_layers` — [`L176`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L176)
  - `model_type` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L126)
  - `num_attention_heads` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L159)
  - `num_hidden_layers` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L158)
  - `num_key_value_heads` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L160)
  - `rms_norm_eps` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L165)
  - `rope_scaling` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L173)
  - `rope_theta` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L168)
  - `sliding_window` — [`L175`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L175)
  - `tie_word_embeddings` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L167)
  - `use_cache` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L166)
  - `use_sliding_window` — [`L174`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L174)
  - `vocab_size` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L155)
- protocol/private: `__init__`[`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L129)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`SLIDING`](../../infra/utils.md#AttnMaskType.SLIDING)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../qwen3_5/modeling_qwen3_5.md#Qwen3_5Model.__init__), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`embed_tokens`](modeling_qwen3_vl.md#Qwen3VLTextModel.embed_tokens), [`Qwen3VLTextModel`](modeling_qwen3_vl.md#Qwen3VLTextModel), [`__init__`](modeling_qwen3_vl.md#Qwen3VLTextAttention.__init__), [`input_layernorm`](modeling_qwen3_vl.md#Qwen3VLTextDecoderLayer.input_layernorm), [`norm`](modeling_qwen3_vl.md#Qwen3VLTextModel.norm), [`post_attention_layernorm`](modeling_qwen3_vl.md#Qwen3VLTextDecoderLayer.post_attention_layernorm), [`layer_idx`](modeling_qwen3_vl.md#Qwen3VLTextMLP.layer_idx), [`act_fn`](modeling_qwen3_vl.md#Qwen3VLTextMLP.act_fn), [`down_proj`](modeling_qwen3_vl.md#Qwen3VLTextMLP.down_proj), [`gate_proj`](modeling_qwen3_vl.md#Qwen3VLTextMLP.gate_proj), [`up_proj`](modeling_qwen3_vl.md#Qwen3VLTextMLP.up_proj), [`__init__`](modeling_qwen3_vl.md#Qwen3VLTextModel.__init__), [`__init__`](qwen3_vl_configuration.md#Qwen3VLConfig.__init__), [`get_text_config`](qwen3_vl_configuration.md#Qwen3VLConfig.get_text_config), [`sub_configs`](qwen3_vl_configuration.md#Qwen3VLConfig.sub_configs), [`layers`](modeling_qwen3_vl.md#Qwen3VLTextModel.layers), [`__init__`](modeling_qwen3_vl.md#Qwen3VLTextDecoderLayer.__init__), [`__init__`](modeling_qwen3_vl.md#Qwen3VLTextMLP.__init__)

### `Qwen3VLVisionConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/qwen3_vl/qwen3_vl_configuration.py:32`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L32)
- doc: Configuration class for Qwen3-VL vision encoder.
- signature: `class Qwen3VLVisionConfig(EasyDeLBaseConfig):`
- members:
  - `base_config_key` — [`L56`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L56)
  - `deepstack_visual_indexes` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L89)
  - `depth` — [`L77`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L77)
  - `embed_dim` — [`L93`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L93)
  - `hidden_act` — [`L79`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L79)
  - `hidden_size` — [`L78`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L78)
  - `in_channels` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L83)
  - `initializer_range` — [`L91`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L91)
  - `intermediate_size` — [`L80`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L80)
  - `model_type` — [`L55`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L55)
  - `num_attention_heads` — [`L82`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L82)
  - `num_heads` — [`L81`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L81)
  - `num_position_embeddings` — [`L88`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L88)
  - `out_hidden_size` — [`L87`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L87)
  - `patch_size` — [`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L84)
  - `spatial_merge_size` — [`L85`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L85)
  - `temporal_patch_size` — [`L86`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L86)
  - `tokens_per_second` — [`L90`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L90)
- protocol/private: `__init__`[`L58`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_vl/qwen3_vl_configuration.py#L58)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`Qwen3_5VisionConfig`](../qwen3_5/qwen3_5_configuration.md#Qwen3_5VisionConfig)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../qwen3_5/modeling_qwen3_5.md#Qwen3_5ForConditionalGeneration.__init__), [`hidden_size`](modeling_qwen3_vl.md#Qwen3VLVisionPatchMerger.hidden_size), [`spatial_merge_size`](modeling_qwen3_vl.md#Qwen3VisionTransformerPretrainedModel.spatial_merge_size), [`linear_fc2`](modeling_qwen3_vl.md#Qwen3VLVisionMLP.linear_fc2), [`Qwen3_5VisionConfig`](../qwen3_5/qwen3_5_configuration.md#Qwen3_5VisionConfig), [`hidden_size`](modeling_qwen3_vl.md#Qwen3VLVisionPatchEmbed.hidden_size), [`linear_fc1`](modeling_qwen3_vl.md#Qwen3VLVisionMLP.linear_fc1), [`linear_fc2`](modeling_qwen3_vl.md#Qwen3VLVisionPatchMerger.linear_fc2), [`norm`](modeling_qwen3_vl.md#Qwen3VLVisionPatchMerger.norm), [`num_grid_per_side`](modeling_qwen3_vl.md#Qwen3VisionTransformerPretrainedModel.num_grid_per_side), [`pos_embed`](modeling_qwen3_vl.md#Qwen3VisionTransformerPretrainedModel.pos_embed), [`blocks`](modeling_qwen3_vl.md#Qwen3VisionTransformerPretrainedModel.blocks), [`hidden_size`](modeling_qwen3_vl.md#Qwen3VLVisionAttention.hidden_size), [`act`](modeling_qwen3_vl.md#Qwen3VLVisionMLP.act), [`deepstack_merger_list`](modeling_qwen3_vl.md#Qwen3VisionTransformerPretrainedModel.deepstack_merger_list), [`head_dim`](modeling_qwen3_vl.md#Qwen3VLVisionAttention.head_dim), [`norm1`](modeling_qwen3_vl.md#Qwen3VLVisionBlock.norm1), [`norm2`](modeling_qwen3_vl.md#Qwen3VLVisionBlock.norm2), [`proj`](modeling_qwen3_vl.md#Qwen3VLVisionPatchEmbed.proj), [`__init__`](modeling_qwen3_vl.md#Qwen3VisionTransformerPretrainedModel.__init__), [`__init__`](qwen3_vl_configuration.md#Qwen3VLConfig.__init__), [`sub_configs`](qwen3_vl_configuration.md#Qwen3VLConfig.sub_configs), [`num_heads`](modeling_qwen3_vl.md#Qwen3VLVisionAttention.num_heads), [`patch_size`](modeling_qwen3_vl.md#Qwen3VLVisionPatchEmbed.patch_size), [`in_channels`](modeling_qwen3_vl.md#Qwen3VLVisionPatchEmbed.in_channels), [`temporal_patch_size`](modeling_qwen3_vl.md#Qwen3VLVisionPatchEmbed.temporal_patch_size), [`__init__`](../qwen3_5/qwen3_5_configuration.md#Qwen3_5VisionConfig.__init__), [`__init__`](modeling_qwen3_vl.md#Qwen3VLVisionAttention.__init__), [`__init__`](modeling_qwen3_vl.md#Qwen3VLVisionBlock.__init__), [`__init__`](modeling_qwen3_vl.md#Qwen3VLVisionMLP.__init__), [`__init__`](modeling_qwen3_vl.md#Qwen3VLVisionPatchEmbed.__init__), [`__init__`](modeling_qwen3_vl.md#Qwen3VLVisionPatchMerger.__init__), [`config_class`](modeling_qwen3_vl.md#Qwen3VisionTransformerPretrainedModel.config_class), [`define_network`](modeling_qwen3_vl.md#Qwen3VLVisionAttention.define_network), [`spatial_merge_size`](modeling_qwen3_vl.md#Qwen3VLVisionPatchMerger.spatial_merge_size)

