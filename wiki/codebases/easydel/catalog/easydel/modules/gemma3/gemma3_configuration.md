---
title: 'Module: easydel/modules/gemma3/gemma3_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/gemma3/gemma3_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.gemma3.gemma3_configuration`/Gemma3
symbols:
  Gemma3TextConfig: TextConfig#
  Gemma3TextConfig.get_mask_details: TextConfig#get_mask_details().
  Gemma3Config: Config#
  Gemma3TextConfig.rope_scaling: TextConfig#rope_scaling.
  Gemma3TextConfig.use_bidirectional_attention: TextConfig#use_bidirectional_attention.
  Gemma3TextConfig.layer_types: TextConfig#layer_types.
  Gemma3Config.vision_config: Config#vision_config.
  Gemma3TextConfig.__init__: TextConfig#__init__().
  Gemma3TextConfig.sliding_window: TextConfig#sliding_window.
  Gemma3Config.sub_configs: Config#sub_configs.
  Gemma3Config.__init__: Config#__init__().
  Gemma3TextConfig.scan_layers: TextConfig#scan_layers.
  Gemma3Config.initializer_range: Config#initializer_range.
  Gemma3TextConfig.hidden_size: TextConfig#hidden_size.
  Gemma3TextConfig.intermediate_size: TextConfig#intermediate_size.
  Gemma3TextConfig.num_hidden_layers: TextConfig#num_hidden_layers.
  Gemma3TextConfig.rope_theta: TextConfig#rope_theta.
  Gemma3TextConfig.gradient_checkpointing: TextConfig#gradient_checkpointing.
  Gemma3TextConfig.initializer_range: TextConfig#initializer_range.
  Gemma3TextConfig.rms_norm_eps: TextConfig#rms_norm_eps.
  Gemma3TextConfig.hidden_activation: TextConfig#hidden_activation.
  Gemma3TextConfig.rope_local_base_freq: TextConfig#rope_local_base_freq.
  Gemma3TextConfig.sliding_window_pattern: TextConfig#sliding_window_pattern.
  Gemma3Config.mm_tokens_per_image: Config#mm_tokens_per_image.
  Gemma3TextConfig.model_type: TextConfig#model_type.
  Gemma3TextConfig.bits: TextConfig#bits.
  Gemma3TextConfig.vocab_size: TextConfig#vocab_size.
  Gemma3TextConfig.max_position_embeddings: TextConfig#max_position_embeddings.
  Gemma3TextConfig.num_attention_heads: TextConfig#num_attention_heads.
  Gemma3TextConfig.head_dim: TextConfig#head_dim.
  Gemma3TextConfig.num_key_value_heads: TextConfig#num_key_value_heads.
  Gemma3TextConfig.use_cache: TextConfig#use_cache.
  Gemma3TextConfig.attention_bias: TextConfig#attention_bias.
  Gemma3TextConfig.attention_dropout: TextConfig#attention_dropout.
  Gemma3TextConfig.query_pre_attn_scalar: TextConfig#query_pre_attn_scalar.
  Gemma3TextConfig.final_logit_softcapping: TextConfig#final_logit_softcapping.
  Gemma3TextConfig.attn_logit_softcapping: TextConfig#attn_logit_softcapping.
  Gemma3TextConfig.cache_implementation: TextConfig#cache_implementation.
  Gemma3TextConfig.rope_parameters: TextConfig#rope_parameters.
  Gemma3TextConfig.get_partition_rules: TextConfig#get_partition_rules().
  Gemma3Config.model_type: Config#model_type.
  Gemma3Config.text_config: Config#text_config.
  Gemma3Config.boi_token_index: Config#boi_token_index.
  Gemma3Config.eoi_token_index: Config#eoi_token_index.
  Gemma3Config.image_token_id: Config#image_token_id.
  Gemma3Config.get_partition_rules: Config#get_partition_rules().
---
# Module: [`easydel/modules/gemma3/gemma3_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py)

## Classes
### `Gemma3Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/gemma3/gemma3_configuration.py:290`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L290)
- doc: Args:
- signature: `class Gemma3Config(EasyDeLBaseConfig):`
- members:
  - `__init__(self, text_config: Gemma3TextConfig | None = None, vision_config: SiglipVisionConfig | None = None, mm_tokens_per_image: int = 256, boi_token_index: int = 255999, eoi_token_index: int = 256000, image_token_id: int = 262144, initializer_range: float = 0.02, **kwargs)` — [`L333`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L333) — Initialize a Gemma3Config instance.
  - `get_partition_rules(self, *args, **kwargs)` — [`L378`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L378) — Returns partition rules for model sharding.
  - `boi_token_index` — [`L371`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L371)
  - `eoi_token_index` — [`L372`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L372)
  - `image_token_id` — [`L373`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L373)
  - `initializer_range` — [`L374`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L374)
  - `mm_tokens_per_image` — [`L370`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L370)
  - `model_type` — [`L330`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L330)
  - `sub_configs` — [`L331`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L331)
  - `text_config` — [`L368`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L368)
  - `vision_config` — [`L369`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L369)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`Gemma3TextConfig`](gemma3_configuration.md#Gemma3TextConfig), [`SiglipVisionConfig`](../siglip/configuration_siglip.md#SiglipVisionConfig)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`Gemma3ForConditionalGeneration`](modeling_gemma3.md#Gemma3ForConditionalGeneration), [`Gemma3Model`](modeling_gemma3.md#Gemma3Model), [`mm_input_projection_weight`](modeling_gemma3.md#Gemma3MultiModalProjector.mm_input_projection_weight), [`mm_soft_emb_norm`](modeling_gemma3.md#Gemma3MultiModalProjector.mm_soft_emb_norm), [`patches_per_image`](modeling_gemma3.md#Gemma3MultiModalProjector.patches_per_image), [`vision_tower`](modeling_gemma3.md#Gemma3Model.vision_tower), [`tokens_per_side`](modeling_gemma3.md#Gemma3MultiModalProjector.tokens_per_side), [`__init__`](modeling_gemma3.md#Gemma3ForConditionalGeneration.__init__), [`__init__`](modeling_gemma3.md#Gemma3Model.__init__), [`__init__`](modeling_gemma3.md#Gemma3MultiModalProjector.__init__), [`_config_class`](modeling_gemma3.md#Gemma3ForConditionalGeneration._config_class)

### `Gemma3TextConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/gemma3/gemma3_configuration.py:29`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L29)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class Gemma3TextConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 262208, hidden_size: int = 2304, intermediate_size: int | None = 9216, num_hidden_layers: int = 26, num_attention_heads: int = 8, num_key_value_heads: int = 4, head_dim: int = 256, hidden_activation: str = "gelu_pytorch_tanh", max_position_embeddings: int = 131072, initializer_range: float = 0.02, rms_norm_eps: float = 0.000001, use_cache: bool = True, pad_token_id: int = 0, eos_token_id: int = 1, bos_token_id: int = 2, tie_word_embeddings: bool = True, rope_theta: float = 1, attention_bias: bool = False, attention_dropout: float = 0, query_pre_attn_scalar: int = 256, sliding_window: int = 4096, final_logit_softcapping: float | None = None, attn_logit_softcapping: float | None = None, cache_implementation: str = "hybrid", rope_scaling: dict | None = None, rope_local_base_freq: float = 10, sliding_window_pattern: int = 6, layer_types: list[str] | None = None, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, bits: int | None = None, scan_layers: bool = False, use_bidirectional_attention: bool = False, **kwargs)` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L140) — The __init__ function is called when the class is instantiated.
  - `get_mask_details(self)` — [`L264`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L264) — Retrieve attention mask details for each layer in the model.
  - `get_partition_rules(self, *args, **kwargs)` — [`L251`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L251) — Returns partition rules for model sharding.
  - `attention_bias` — [`L206`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L206)
  - `attention_dropout` — [`L207`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L207)
  - `attn_logit_softcapping` — [`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L212)
  - `bits` — [`L182`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L182)
  - `cache_implementation` — [`L213`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L213)
  - `final_logit_softcapping` — [`L211`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L211)
  - `gradient_checkpointing` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L181)
  - `head_dim` — [`L200`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L200)
  - `hidden_activation` — [`L208`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L208)
  - `hidden_size` — [`L196`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L196)
  - `initializer_range` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L202)
  - `intermediate_size` — [`L197`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L197)
  - `layer_types` — [`L217`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L217)
  - `max_position_embeddings` — [`L195`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L195)
  - `model_type` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L138)
  - `num_attention_heads` — [`L199`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L199)
  - `num_hidden_layers` — [`L198`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L198)
  - `num_key_value_heads` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L201)
  - `query_pre_attn_scalar` — [`L209`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L209)
  - `rms_norm_eps` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L203)
  - `rope_local_base_freq` — [`L215`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L215)
  - `rope_parameters` — [`L249`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L249)
  - `rope_scaling` — [`L226`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L226)
  - `rope_theta` — [`L205`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L205)
  - `scan_layers` — [`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L183)
  - `sliding_window` — [`L210`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L210)
  - `sliding_window_pattern` — [`L216`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L216)
  - `use_bidirectional_attention` — [`L218`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L218)
  - `use_cache` — [`L204`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L204)
  - `vocab_size` — [`L194`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma3/gemma3_configuration.py#L194)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`from_hf`](../../infra/utils.md#AttnMaskType.from_hf)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`Gemma3TextModel`](modeling_gemma3.md#Gemma3TextModel), [`embed_tokens`](modeling_gemma3.md#Gemma3TextModel.embed_tokens), [`Gemma3ForCausalLM`](modeling_gemma3.md#Gemma3ForCausalLM), [`Gemma3ForSequenceClassification`](modeling_gemma3.md#Gemma3ForSequenceClassification), [`act`](modeling_gemma3.md#Gemma3MLP.act), [`is_sliding`](modeling_gemma3.md#Gemma3Attention.is_sliding), [`__init__`](modeling_gemma3.md#Gemma3ForCausalLM.__init__), [`precision`](modeling_gemma3.md#Gemma3MLP.precision), [`__init__`](modeling_gemma3.md#Gemma3ForSequenceClassification.__init__), [`param_dtype`](modeling_gemma3.md#Gemma3RMSNorm.param_dtype), [`epsilon`](modeling_gemma3.md#Gemma3RMSNorm.epsilon), [`__init__`](gemma3_configuration.md#Gemma3Config.__init__), [`__init__`](modeling_gemma3.md#Gemma3TextModel.__init__), [`sub_configs`](gemma3_configuration.md#Gemma3Config.sub_configs), [`__init__`](modeling_gemma3.md#Gemma3Attention.__init__), [`__init__`](modeling_gemma3.md#Gemma3DecoderLayer.__init__), [`__init__`](modeling_gemma3.md#Gemma3MLP.__init__), [`__init__`](modeling_gemma3.md#Gemma3RMSNorm.__init__), [`_config_class`](modeling_gemma3.md#Gemma3ForCausalLM._config_class), [`_config_class`](modeling_gemma3.md#Gemma3ForSequenceClassification._config_class), [`sliding_window`](modeling_gemma3.md#Gemma3DecoderLayer.sliding_window)

