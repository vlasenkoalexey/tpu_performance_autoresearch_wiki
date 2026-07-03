---
title: 'Module: easydel/modules/gemma4/gemma4_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/gemma4/gemma4_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.gemma4.gemma4_configuration`/Gemma4
symbols:
  Gemma4TextConfig: TextConfig#
  Gemma4VisionConfig: VisionConfig#
  Gemma4TextConfig.hidden_size: TextConfig#hidden_size.
  Gemma4TextConfig.get_mask_details: TextConfig#get_mask_details().
  Gemma4VisionConfig.hidden_size: VisionConfig#hidden_size.
  Gemma4Config: Config#
  Gemma4TextConfig.layer_types: TextConfig#layer_types.
  Gemma4TextConfig.num_hidden_layers: TextConfig#num_hidden_layers.
  Gemma4TextConfig.float32_gate_logits: TextConfig#float32_gate_logits.
  Gemma4Config.vision_config: Config#vision_config.
  Gemma4TextConfig.__init__: TextConfig#__init__().
  Gemma4TextConfig.hidden_size_per_layer_input: TextConfig#hidden_size_per_layer_input.
  Gemma4TextConfig.num_experts: TextConfig#num_experts.
  Gemma4TextConfig.get_kv_shared_layer_mapping: TextConfig#get_kv_shared_layer_mapping().
  Gemma4VisionConfig.__init__: VisionConfig#__init__().
  Gemma4Config.sub_configs: Config#sub_configs.
  Gemma4Config.__init__: Config#__init__().
  Gemma4TextConfig.initializer_range: TextConfig#initializer_range.
  Gemma4TextConfig.sliding_window: TextConfig#sliding_window.
  Gemma4VisionConfig.rms_norm_eps: VisionConfig#rms_norm_eps.
  Gemma4VisionConfig.attention_bias: VisionConfig#attention_bias.
  Gemma4TextConfig.hidden_activation: TextConfig#hidden_activation.
  Gemma4TextConfig.moe_intermediate_size: TextConfig#moe_intermediate_size.
  Gemma4VisionConfig.intermediate_size: VisionConfig#intermediate_size.
  Gemma4Config.text_config: Config#text_config.
  Gemma4TextConfig.scan_layers: TextConfig#scan_layers.
  Gemma4VisionConfig.bits: VisionConfig#bits.
  Gemma4Config.tie_word_embeddings: Config#tie_word_embeddings.
  Gemma4TextConfig.num_global_key_value_heads: TextConfig#num_global_key_value_heads.
  Gemma4TextConfig.global_head_dim: TextConfig#global_head_dim.
  Gemma4TextConfig.activations_in_float32: TextConfig#activations_in_float32.
  Gemma4VisionConfig.model_type: VisionConfig#model_type.
  Gemma4VisionConfig.head_dim: VisionConfig#head_dim.
  Gemma4VisionConfig.patch_size: VisionConfig#patch_size.
  Gemma4VisionConfig.position_embedding_size: VisionConfig#position_embedding_size.
  Gemma4VisionConfig.initializer_range: VisionConfig#initializer_range.
  Gemma4TextConfig.gradient_checkpointing: TextConfig#gradient_checkpointing.
  Gemma4TextConfig.vocab_size: TextConfig#vocab_size.
  Gemma4TextConfig.intermediate_size: TextConfig#intermediate_size.
  Gemma4TextConfig.head_dim: TextConfig#head_dim.
  Gemma4TextConfig.num_key_value_heads: TextConfig#num_key_value_heads.
  Gemma4TextConfig.rms_norm_eps: TextConfig#rms_norm_eps.
  Gemma4TextConfig.vocab_size_per_layer_input: TextConfig#vocab_size_per_layer_input.
  Gemma4TextConfig.attention_k_eq_v: TextConfig#attention_k_eq_v.
  Gemma4TextConfig.num_kv_shared_layers: TextConfig#num_kv_shared_layers.
  Gemma4TextConfig.enable_moe_block: TextConfig#enable_moe_block.
  Gemma4TextConfig.use_double_wide_mlp: TextConfig#use_double_wide_mlp.
  Gemma4TextConfig.top_k_experts: TextConfig#top_k_experts.
  Gemma4VisionConfig.gradient_checkpointing: VisionConfig#gradient_checkpointing.
  Gemma4VisionConfig.num_hidden_layers: VisionConfig#num_hidden_layers.
  Gemma4VisionConfig.num_attention_heads: VisionConfig#num_attention_heads.
  Gemma4VisionConfig.num_key_value_heads: VisionConfig#num_key_value_heads.
  Gemma4VisionConfig.hidden_activation: VisionConfig#hidden_activation.
  Gemma4VisionConfig.max_position_embeddings: VisionConfig#max_position_embeddings.
  Gemma4VisionConfig.attention_dropout: VisionConfig#attention_dropout.
  Gemma4VisionConfig.standardize: VisionConfig#standardize.
  Gemma4VisionConfig.rope_parameters: VisionConfig#rope_parameters.
  Gemma4TextConfig.model_type: TextConfig#model_type.
  Gemma4TextConfig.bits: TextConfig#bits.
  Gemma4TextConfig.max_position_embeddings: TextConfig#max_position_embeddings.
  Gemma4TextConfig.num_attention_heads: TextConfig#num_attention_heads.
  Gemma4TextConfig.use_cache: TextConfig#use_cache.
  Gemma4TextConfig.attention_bias: TextConfig#attention_bias.
  Gemma4TextConfig.attention_dropout: TextConfig#attention_dropout.
  Gemma4TextConfig.final_logit_softcapping: TextConfig#final_logit_softcapping.
  Gemma4TextConfig.use_bidirectional_attention: TextConfig#use_bidirectional_attention.
  Gemma4TextConfig.rope_parameters: TextConfig#rope_parameters.
  Gemma4TextConfig.get_partition_rules: TextConfig#get_partition_rules().
  Gemma4VisionConfig.pooling_kernel_size: VisionConfig#pooling_kernel_size.
  Gemma4VisionConfig.use_clipped_linears: VisionConfig#use_clipped_linears.
  Gemma4VisionConfig.get_partition_rules: VisionConfig#get_partition_rules().
  Gemma4Config.model_type: Config#model_type.
  Gemma4Config.audio_config: Config#audio_config.
  Gemma4Config.boi_token_id: Config#boi_token_id.
  Gemma4Config.eoi_token_id: Config#eoi_token_id.
  Gemma4Config.image_token_id: Config#image_token_id.
  Gemma4Config.video_token_id: Config#video_token_id.
  Gemma4Config.boa_token_id: Config#boa_token_id.
  Gemma4Config.eoa_token_index: Config#eoa_token_index.
  Gemma4Config.audio_token_id: Config#audio_token_id.
  Gemma4Config.initializer_range: Config#initializer_range.
  Gemma4Config.get_partition_rules: Config#get_partition_rules().
---
# Module: [`easydel/modules/gemma4/gemma4_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py)

## Classes
### `Gemma4Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/gemma4/gemma4_configuration.py:477`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L477)
- doc: Top-level multimodal configuration for Gemma4.
- signature: `class Gemma4Config(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L565`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L565) — Return tensor-parallelism partition rules.
  - `audio_config` — [`L552`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L552)
  - `audio_token_id` — [`L559`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L559)
  - `boa_token_id` — [`L557`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L557)
  - `boi_token_id` — [`L553`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L553)
  - `eoa_token_index` — [`L558`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L558)
  - `eoi_token_id` — [`L554`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L554)
  - `image_token_id` — [`L555`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L555)
  - `initializer_range` — [`L560`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L560)
  - `model_type` — [`L520`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L520)
  - `sub_configs` — [`L521`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L521)
  - `text_config` — [`L550`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L550)
  - `tie_word_embeddings` — [`L561`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L561)
  - `video_token_id` — [`L556`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L556)
  - `vision_config` — [`L551`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L551)
- protocol/private: `__init__`[`L526`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L526)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`Gemma4TextConfig`](gemma4_configuration.md#Gemma4TextConfig), [`Gemma4VisionConfig`](gemma4_configuration.md#Gemma4VisionConfig)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`embed_vision`](modeling_gemma4.md#Gemma4Model.embed_vision), [`Gemma4ForConditionalGeneration`](modeling_gemma4.md#Gemma4ForConditionalGeneration), [`Gemma4Model`](modeling_gemma4.md#Gemma4Model), [`vision_tower`](modeling_gemma4.md#Gemma4Model.vision_tower), [`language_model`](modeling_gemma4.md#Gemma4Model.language_model), [`__init__`](modeling_gemma4.md#Gemma4ForConditionalGeneration.__init__), [`_missing_vision_backend_model_type`](modeling_gemma4.md#Gemma4Model._missing_vision_backend_model_type), [`__init__`](modeling_gemma4.md#Gemma4Model.__init__)

### `Gemma4TextConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/gemma4/gemma4_configuration.py:44`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L44)
- doc: Configuration for the Gemma4 text decoder.
- signature: `class Gemma4TextConfig(EasyDeLBaseConfig):`
- members:
  - `get_kv_shared_layer_mapping(self)` — [`L306`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L306) — Return a mapping from KV-shared layer indices to their donor indices.
  - `get_mask_details(self)` — [`L333`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L333) — Return per-layer attention mask metadata for eSurge and cache setup.
  - `get_partition_rules(self, *args, **kwargs)` — [`L298`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L298) — Return tensor-parallelism partition rules.
  - `activations_in_float32` — [`L274`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L274)
  - `attention_bias` — [`L257`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L257)
  - `attention_dropout` — [`L258`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L258)
  - `attention_k_eq_v` — [`L267`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L267)
  - `bits` — [`L234`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L234)
  - `enable_moe_block` — [`L269`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L269)
  - `final_logit_softcapping` — [`L261`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L261)
  - `float32_gate_logits` — [`L275`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L275)
  - `global_head_dim` — [`L266`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L266)
  - `gradient_checkpointing` — [`L233`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L233)
  - `head_dim` — [`L252`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L252)
  - `hidden_activation` — [`L259`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L259)
  - `hidden_size` — [`L248`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L248)
  - `hidden_size_per_layer_input` — [`L264`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L264)
  - `initializer_range` — [`L254`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L254)
  - `intermediate_size` — [`L249`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L249)
  - `layer_types` — [`L288`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L288)
  - `max_position_embeddings` — [`L247`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L247)
  - `model_type` — [`L188`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L188)
  - `moe_intermediate_size` — [`L273`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L273)
  - `num_attention_heads` — [`L251`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L251)
  - `num_experts` — [`L271`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L271)
  - `num_global_key_value_heads` — [`L265`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L265)
  - `num_hidden_layers` — [`L250`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L250)
  - `num_key_value_heads` — [`L253`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L253)
  - `num_kv_shared_layers` — [`L268`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L268)
  - `rms_norm_eps` — [`L255`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L255)
  - `rope_parameters` — [`L296`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L296)
  - `scan_layers` — [`L235`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L235)
  - `sliding_window` — [`L260`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L260)
  - `top_k_experts` — [`L272`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L272)
  - `use_bidirectional_attention` — [`L262`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L262)
  - `use_cache` — [`L256`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L256)
  - `use_double_wide_mlp` — [`L270`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L270)
  - `vocab_size` — [`L246`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L246)
  - `vocab_size_per_layer_input` — [`L263`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L263)
- protocol/private: `__init__`[`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L190)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`from_hf`](../../infra/utils.md#AttnMaskType.from_hf)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`embed_vision`](modeling_gemma4.md#Gemma4Model.embed_vision), [`embed_tokens`](modeling_gemma4.md#Gemma4TextModel.embed_tokens), [`__init__`](modeling_gemma4.md#Gemma4TextRouter.__init__), [`__call__`](modeling_gemma4.md#Gemma4MLP.__call__), [`Gemma4TextModel`](modeling_gemma4.md#Gemma4TextModel), [`__call__`](modeling_gemma4.md#Gemma4TextMLPStack.__call__), [`Gemma4ForCausalLM`](modeling_gemma4.md#Gemma4ForCausalLM), [`kv_shared_layer_index`](modeling_gemma4.md#Gemma4Attention.kv_shared_layer_index), [`precision`](modeling_gemma4.md#Gemma4MLP.precision), [`embed_tokens_per_layer`](modeling_gemma4.md#Gemma4TextModel.embed_tokens_per_layer), [`proj`](modeling_gemma4.md#Gemma4TextRouter.proj), [`reform_router_probs`](modeling_gemma4.md#Gemma4TextRouter.reform_router_probs), [`_resolve_head_dim`](modeling_gemma4.md#Gemma4Attention._resolve_head_dim), [`_resolve_num_kv_heads`](modeling_gemma4.md#Gemma4Attention._resolve_num_kv_heads), [`act`](modeling_gemma4.md#Gemma4MLP.act), [`hidden_size_per_layer_input`](modeling_gemma4.md#Gemma4TextModel.hidden_size_per_layer_input), [`precision`](modeling_gemma4.md#Gemma4TextMLPStack.precision), [`hidden_size_per_layer_input`](modeling_gemma4.md#Gemma4DecoderLayer.hidden_size_per_layer_input), [`use_alternative_attention`](modeling_gemma4.md#Gemma4Attention.use_alternative_attention), [`per_expert_scale`](modeling_gemma4.md#Gemma4TextRouter.per_expert_scale), [`per_layer_model_projection`](modeling_gemma4.md#Gemma4TextModel.per_layer_model_projection), [`scale`](modeling_gemma4.md#Gemma4TextRouter.scale), [`__init__`](modeling_gemma4.md#Gemma4ForCausalLM.__init__), [`_num_kv_heads`](modeling_gemma4.md#Gemma4Attention._num_kv_heads), [`act_fn`](modeling_gemma4.md#Gemma4TextMLPStack.act_fn), [`down_proj`](modeling_gemma4.md#Gemma4TextMLPStack.down_proj), [`enable_moe_block`](modeling_gemma4.md#Gemma4DecoderLayer.enable_moe_block), [`gate_proj`](modeling_gemma4.md#Gemma4TextMLPStack.gate_proj), [`up_proj`](modeling_gemma4.md#Gemma4TextMLPStack.up_proj), [`norm`](modeling_gemma4.md#Gemma4TextRouter.norm), [`per_layer_act`](modeling_gemma4.md#Gemma4DecoderLayer.per_layer_act), [`per_layer_input_gate`](modeling_gemma4.md#Gemma4DecoderLayer.per_layer_input_gate), [`per_layer_projection`](modeling_gemma4.md#Gemma4DecoderLayer.per_layer_projection), [`per_layer_projection_norm`](modeling_gemma4.md#Gemma4TextModel.per_layer_projection_norm), [`__init__`](gemma4_configuration.md#Gemma4Config.__init__), [`__init__`](modeling_gemma4.md#Gemma4RMSNorm.__init__)  (+16 more)

### `Gemma4VisionConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/gemma4/gemma4_configuration.py:356`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L356)
- doc: Configuration for the Gemma4 vision encoder.
- signature: `class Gemma4VisionConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L468`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L468) — Return tensor-parallelism partition rules.
  - `attention_bias` — [`L455`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L455)
  - `attention_dropout` — [`L456`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L456)
  - `bits` — [`L442`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L442)
  - `gradient_checkpointing` — [`L441`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L441)
  - `head_dim` — [`L451`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L451)
  - `hidden_activation` — [`L452`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L452)
  - `hidden_size` — [`L446`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L446)
  - `initializer_range` — [`L462`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L462)
  - `intermediate_size` — [`L447`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L447)
  - `max_position_embeddings` — [`L454`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L454)
  - `model_type` — [`L415`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L415)
  - `num_attention_heads` — [`L449`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L449)
  - `num_hidden_layers` — [`L448`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L448)
  - `num_key_value_heads` — [`L450`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L450)
  - `patch_size` — [`L458`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L458)
  - `pooling_kernel_size` — [`L457`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L457)
  - `position_embedding_size` — [`L459`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L459)
  - `rms_norm_eps` — [`L453`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L453)
  - `rope_parameters` — [`L466`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L466)
  - `standardize` — [`L461`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L461)
  - `use_clipped_linears` — [`L460`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L460)
- protocol/private: `__init__`[`L417`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma4/gemma4_configuration.py#L417)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`embed_vision`](modeling_gemma4.md#Gemma4Model.embed_vision), [`Gemma4VisionModel`](modeling_gemma4.md#Gemma4VisionModel), [`_has_registered_gemma4_vision_backend`](modeling_gemma4.md#_has_registered_gemma4_vision_backend), [`k_proj`](modeling_gemma4.md#Gemma4VisionAttention.k_proj), [`o_proj`](modeling_gemma4.md#Gemma4VisionAttention.o_proj), [`q_proj`](modeling_gemma4.md#Gemma4VisionAttention.q_proj), [`rotary_emb`](modeling_gemma4.md#Gemma4VisionEncoder.rotary_emb), [`v_proj`](modeling_gemma4.md#Gemma4VisionAttention.v_proj), [`head_dim`](modeling_gemma4.md#Gemma4VisionAttention.head_dim), [`frequencies`](modeling_gemma4.md#Gemma4VisionRotaryEmbedding.frequencies), [`position_embedding_table`](modeling_gemma4.md#Gemma4VisionPatchEmbedder.position_embedding_table), [`__init__`](modeling_gemma4.md#Gemma4VisionClippableLinear.__init__), [`_position_embeddings`](modeling_gemma4.md#Gemma4VisionPatchEmbedder._position_embeddings), [`down_proj`](modeling_gemma4.md#Gemma4VisionMLP.down_proj), [`gate_proj`](modeling_gemma4.md#Gemma4VisionMLP.gate_proj), [`k_norm`](modeling_gemma4.md#Gemma4VisionAttention.k_norm), [`q_norm`](modeling_gemma4.md#Gemma4VisionAttention.q_norm), [`std_bias`](modeling_gemma4.md#Gemma4VisionModel.std_bias), [`std_scale`](modeling_gemma4.md#Gemma4VisionModel.std_scale), [`up_proj`](modeling_gemma4.md#Gemma4VisionMLP.up_proj), [`v_norm`](modeling_gemma4.md#Gemma4VisionAttention.v_norm), [`input_proj`](modeling_gemma4.md#Gemma4VisionPatchEmbedder.input_proj), [`num_key_value_heads`](modeling_gemma4.md#Gemma4VisionAttention.num_key_value_heads), [`num_attention_heads`](modeling_gemma4.md#Gemma4VisionAttention.num_attention_heads), [`act`](modeling_gemma4.md#Gemma4VisionMLP.act), [`attention_performer`](modeling_gemma4.md#Gemma4VisionAttention.attention_performer), [`config`](modeling_gemma4.md#Gemma4VisionPatchEmbedder.config), [`pooler`](modeling_gemma4.md#Gemma4VisionModel.pooler), [`__init__`](gemma4_configuration.md#Gemma4Config.__init__), [`__init__`](modeling_gemma4.md#Gemma4RMSNorm.__init__), [`__init__`](modeling_gemma4.md#Gemma4VisionModel.__init__), [`__init__`](modeling_gemma4.md#Gemma4VisionRotaryEmbedding.__init__), [`sub_configs`](gemma4_configuration.md#Gemma4Config.sub_configs), [`head_dim`](modeling_gemma4.md#Gemma4VisionRotaryEmbedding.head_dim), [`base`](modeling_gemma4.md#Gemma4VisionRotaryEmbedding.base), [`layers`](modeling_gemma4.md#Gemma4VisionEncoder.layers), [`root_hidden_size`](modeling_gemma4.md#Gemma4VisionPooler.root_hidden_size)  (+8 more)

