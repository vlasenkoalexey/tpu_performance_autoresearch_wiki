---
title: 'Module: easydel/modules/qwen2_vl/qwen2_vl_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/qwen2_vl/qwen2_vl_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.qwen2_vl.qwen2_vl_configuration`/Qwen2VL
symbols:
  Qwen2VLTextConfig.layer_types: TextConfig#layer_types.
  Qwen2VLVisionConfig: VisionConfig#
  Qwen2VLTextConfig: TextConfig#
  Qwen2VLTextConfig.rope_scaling: TextConfig#rope_scaling.
  Qwen2VLConfig: Config#
  Qwen2VLVisionConfig.embed_dim: VisionConfig#embed_dim.
  Qwen2VLConfig.__init__: Config#__init__().
  Qwen2VLConfig.get_mask_details: Config#get_mask_details().
  Qwen2VLConfig.vision_config: Config#vision_config.
  Qwen2VLTextConfig.hidden_size: TextConfig#hidden_size.
  Qwen2VLConfig.sub_configs: Config#sub_configs.
  Qwen2VLTextConfig.sliding_window: TextConfig#sliding_window.
  Qwen2VLConfig.text_config: Config#text_config.
  Qwen2VLTextConfig.intermediate_size: TextConfig#intermediate_size.
  Qwen2VLVisionConfig.__init__: VisionConfig#__init__().
  Qwen2VLVisionConfig.initializer_range: VisionConfig#initializer_range.
  Qwen2VLTextConfig.__init__: TextConfig#__init__().
  Qwen2VLTextConfig.initializer_range: TextConfig#initializer_range.
  Qwen2VLTextConfig.use_sliding_window: TextConfig#use_sliding_window.
  Qwen2VLTextConfig.rms_norm_eps: TextConfig#rms_norm_eps.
  Qwen2VLVisionConfig.spatial_merge_size: VisionConfig#spatial_merge_size.
  Qwen2VLVisionConfig.mlp_ratio: VisionConfig#mlp_ratio.
  Qwen2VLVisionConfig.hidden_act: VisionConfig#hidden_act.
  Qwen2VLTextConfig.hidden_act: TextConfig#hidden_act.
  Qwen2VLVisionConfig.patch_size: VisionConfig#patch_size.
  Qwen2VLVisionConfig.temporal_patch_size: VisionConfig#temporal_patch_size.
  Qwen2VLVisionConfig.in_channels: VisionConfig#in_channels.
  Qwen2VLVisionConfig.num_heads: VisionConfig#num_heads.
  Qwen2VLVisionConfig.depth: VisionConfig#depth.
  Qwen2VLVisionConfig.hidden_size: VisionConfig#hidden_size.
  Qwen2VLConfig.image_token_id: Config#image_token_id.
  Qwen2VLConfig.video_token_id: Config#video_token_id.
  Qwen2VLTextConfig.num_hidden_layers: TextConfig#num_hidden_layers.
  Qwen2VLTextConfig.max_window_layers: TextConfig#max_window_layers.
  Qwen2VLVisionConfig.model_type: VisionConfig#model_type.
  Qwen2VLVisionConfig.base_config_key: VisionConfig#base_config_key.
  Qwen2VLTextConfig.model_type: TextConfig#model_type.
  Qwen2VLTextConfig.base_config_key: TextConfig#base_config_key.
  Qwen2VLTextConfig.keys_to_ignore_at_inference: TextConfig#keys_to_ignore_at_inference.
  Qwen2VLTextConfig.vocab_size: TextConfig#vocab_size.
  Qwen2VLTextConfig.max_position_embeddings: TextConfig#max_position_embeddings.
  Qwen2VLTextConfig.num_attention_heads: TextConfig#num_attention_heads.
  Qwen2VLTextConfig.num_key_value_heads: TextConfig#num_key_value_heads.
  Qwen2VLTextConfig.use_cache: TextConfig#use_cache.
  Qwen2VLTextConfig.rope_theta: TextConfig#rope_theta.
  Qwen2VLTextConfig.attention_dropout: TextConfig#attention_dropout.
  Qwen2VLTextConfig.tie_word_embeddings: TextConfig#tie_word_embeddings.
  Qwen2VLTextConfig.head_dim: TextConfig#head_dim.
  Qwen2VLConfig.model_type: Config#model_type.
  Qwen2VLConfig.keys_to_ignore_at_inference: Config#keys_to_ignore_at_inference.
  Qwen2VLConfig.vision_start_token_id: Config#vision_start_token_id.
  Qwen2VLConfig.vision_end_token_id: Config#vision_end_token_id.
  Qwen2VLConfig.get_partition_rules: Config#get_partition_rules().
---
# Module: [`easydel/modules/qwen2_vl/qwen2_vl_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py)

## Classes
### `Qwen2VLConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/qwen2_vl/qwen2_vl_configuration.py:226`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L226)
- doc: This is the configuration class to store the configuration of a \[`Qwen2VLModel`\]. It is used to instantiate a
- signature: `class Qwen2VLConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, text_config: Mapping[str, typing.Any] | Qwen2VLTextConfig | None = None, vision_config: Mapping[str, typing.Any] | Qwen2VLVisionConfig | None = None, image_token_id: int = 151655, video_token_id: int = 151656, vision_start_token_id: int = 151652, vision_end_token_id: int = 151653, **kwargs)` — [`L252`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L252) — Initialize Qwen2VL composite configuration with text and vision sub-configs.
  - `get_mask_details(self)` — [`L296`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L296) — Retrieve attention mask details for each layer in the model.
  - `get_partition_rules(self, *args, **kwargs)` — [`L283`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L283) — Returns partition rules for model sharding.
  - `image_token_id` — [`L278`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L278)
  - `keys_to_ignore_at_inference` — [`L250`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L250)
  - `model_type` — [`L248`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L248)
  - `sub_configs` — [`L249`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L249)
  - `text_config` — [`L274`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L274)
  - `video_token_id` — [`L279`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L279)
  - `vision_config` — [`L269`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L269)
  - `vision_end_token_id` — [`L281`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L281)
  - `vision_start_token_id` — [`L280`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L280)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`Qwen2VLVisionConfig`](qwen2_vl_configuration.md#Qwen2VLVisionConfig), [`SLIDING`](../../infra/utils.md#AttnMaskType.SLIDING), [`Qwen2VLTextConfig`](qwen2_vl_configuration.md#Qwen2VLTextConfig)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`Qwen2VLForConditionalGeneration`](modeling_qwen2_vl.md#Qwen2VLForConditionalGeneration), [`Qwen2VLModel`](modeling_qwen2_vl.md#Qwen2VLModel), [`__init__`](modeling_qwen2_vl.md#Qwen2VLForConditionalGeneration.__init__), [`visual`](modeling_qwen2_vl.md#Qwen2VLModel.visual), [`language_model`](modeling_qwen2_vl.md#Qwen2VLModel.language_model), [`__init__`](modeling_qwen2_vl.md#Qwen2VLModel.__init__), [`_config_class`](modeling_qwen2_vl.md#Qwen2VLForConditionalGeneration._config_class)

### `Qwen2VLTextConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/qwen2_vl/qwen2_vl_configuration.py:93`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L93)
- doc: Configuration for the Qwen2-VL text decoder backbone.
- signature: `class Qwen2VLTextConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 152064, hidden_size: int = 8192, intermediate_size: int = 29568, num_hidden_layers: int = 80, num_attention_heads: int = 64, num_key_value_heads: int | None = None, hidden_act: str = "silu", max_position_embeddings: int = 32768, initializer_range: float = 0.02, rms_norm_eps: float = 0.00001, use_cache: bool = True, tie_word_embeddings: bool = False, rope_theta: float = 1000000, use_sliding_window: bool = False, sliding_window: int = 4096, max_window_layers: int = 80, attention_dropout: float = 0, rope_scaling: dict | None = None, rope_parameters: dict | None = None, layer_types: list[str] | None = None, **kwargs)` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L151) — Initialize Qwen2VL text decoder configuration.
  - `attention_dropout` — [`L200`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L200)
  - `base_config_key` — [`L148`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L148)
  - `head_dim` — [`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L212)
  - `hidden_act` — [`L195`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L195)
  - `hidden_size` — [`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L183)
  - `initializer_range` — [`L196`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L196)
  - `intermediate_size` — [`L184`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L184)
  - `keys_to_ignore_at_inference` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L149)
  - `layer_types` — [`L213`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L213)
  - `max_position_embeddings` — [`L182`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L182)
  - `max_window_layers` — [`L189`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L189)
  - `model_type` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L147)
  - `num_attention_heads` — [`L186`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L186)
  - `num_hidden_layers` — [`L185`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L185)
  - `num_key_value_heads` — [`L194`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L194)
  - `rms_norm_eps` — [`L197`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L197)
  - `rope_scaling` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L203)
  - `rope_theta` — [`L199`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L199)
  - `sliding_window` — [`L188`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L188)
  - `tie_word_embeddings` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L201)
  - `use_cache` — [`L198`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L198)
  - `use_sliding_window` — [`L187`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L187)
  - `vocab_size` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L181)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__)
- used by: [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`Qwen2VLTextModel`](modeling_qwen2_vl.md#Qwen2VLTextModel), [`__init__`](modeling_qwen2_vl.md#Qwen2VLAttention.__init__), [`act_fn`](modeling_qwen2_vl.md#Qwen2VLMLP.act_fn), [`input_layernorm`](modeling_qwen2_vl.md#Qwen2VLDecoderLayer.input_layernorm), [`post_attention_layernorm`](modeling_qwen2_vl.md#Qwen2VLDecoderLayer.post_attention_layernorm), [`__init__`](qwen2_vl_configuration.md#Qwen2VLConfig.__init__), [`precision`](modeling_qwen2_vl.md#Qwen2VLMLP.precision), [`down_proj`](modeling_qwen2_vl.md#Qwen2VLMLP.down_proj), [`gate_proj`](modeling_qwen2_vl.md#Qwen2VLMLP.gate_proj), [`up_proj`](modeling_qwen2_vl.md#Qwen2VLMLP.up_proj), [`__init__`](modeling_qwen2_vl.md#Qwen2VLTextModel.__init__), [`sub_configs`](qwen2_vl_configuration.md#Qwen2VLConfig.sub_configs), [`__init__`](modeling_qwen2_vl.md#Qwen2VLDecoderLayer.__init__), [`__init__`](modeling_qwen2_vl.md#Qwen2VLMLP.__init__)

### `Qwen2VLVisionConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/qwen2_vl/qwen2_vl_configuration.py:27`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L27)
- doc: Configuration class for the vision component of Qwen2VL model.
- signature: `class Qwen2VLVisionConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, depth: int = 32, embed_dim: int = 1280, hidden_size: int = 3584, hidden_act: str = "quick_gelu", mlp_ratio: int = 4, num_heads: int = 16, in_channels: int = 3, patch_size: int = 14, spatial_merge_size: int = 2, temporal_patch_size: int = 2, initializer_range: float = 0.02, **kwargs)` — [`L58`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L58) — Initialize Qwen2VL vision encoder configuration.
  - `base_config_key` — [`L56`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L56)
  - `depth` — [`L79`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L79)
  - `embed_dim` — [`L80`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L80)
  - `hidden_act` — [`L82`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L82)
  - `hidden_size` — [`L81`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L81)
  - `in_channels` — [`L85`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L85)
  - `initializer_range` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L89)
  - `mlp_ratio` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L83)
  - `model_type` — [`L55`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L55)
  - `num_heads` — [`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L84)
  - `patch_size` — [`L86`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L86)
  - `spatial_merge_size` — [`L87`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L87)
  - `temporal_patch_size` — [`L88`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_vl/qwen2_vl_configuration.py#L88)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__)
- used by: [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`spatial_merge_size`](modeling_qwen2_vl.md#Qwen2VLVisionTransformer.spatial_merge_size), [`patch_embed`](modeling_qwen2_vl.md#Qwen2VLVisionTransformer.patch_embed), [`Qwen2VLVisionTransformer`](modeling_qwen2_vl.md#Qwen2VLVisionTransformer), [`merger`](modeling_qwen2_vl.md#Qwen2VLVisionTransformer.merger), [`mlp`](modeling_qwen2_vl.md#Qwen2VLVisionBlock.mlp), [`norm2`](modeling_qwen2_vl.md#Qwen2VLVisionBlock.norm2), [`__init__`](qwen2_vl_configuration.md#Qwen2VLConfig.__init__), [`blocks`](modeling_qwen2_vl.md#Qwen2VLVisionTransformer.blocks), [`attn`](modeling_qwen2_vl.md#Qwen2VLVisionBlock.attn), [`norm1`](modeling_qwen2_vl.md#Qwen2VLVisionBlock.norm1), [`__init__`](modeling_qwen2_vl.md#Qwen2VLVisionTransformer.__init__), [`sub_configs`](qwen2_vl_configuration.md#Qwen2VLConfig.sub_configs), [`__init__`](modeling_qwen2_vl.md#Qwen2VLVisionBlock.__init__), [`config_class`](modeling_qwen2_vl.md#Qwen2VLVisionTransformer.config_class)

