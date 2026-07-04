---
title: 'Module: easydel/modules/gemma2/gemma2_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/gemma2/gemma2_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.gemma2.gemma2_configuration`/Gemma2Config#
symbols:
  Gemma2Config: ''
  Gemma2Config.get_mask_details: get_mask_details().
  Gemma2Config.layer_types: layer_types.
  Gemma2Config.__init__: __init__().
  Gemma2Config.hidden_size: hidden_size.
  Gemma2Config.intermediate_size: intermediate_size.
  Gemma2Config.num_hidden_layers: num_hidden_layers.
  Gemma2Config.sliding_window: sliding_window.
  Gemma2Config.gradient_checkpointing: gradient_checkpointing.
  Gemma2Config.hidden_activation: hidden_activation.
  Gemma2Config.initializer_range: initializer_range.
  Gemma2Config.rms_norm_eps: rms_norm_eps.
  Gemma2Config.attention_dropout: attention_dropout.
  Gemma2Config.query_pre_attn_scalar: query_pre_attn_scalar.
  Gemma2Config.model_type: model_type.
  Gemma2Config.bits: bits.
  Gemma2Config.scan_layers: scan_layers.
  Gemma2Config.vocab_size: vocab_size.
  Gemma2Config.max_position_embeddings: max_position_embeddings.
  Gemma2Config.num_attention_heads: num_attention_heads.
  Gemma2Config.head_dim: head_dim.
  Gemma2Config.num_key_value_heads: num_key_value_heads.
  Gemma2Config.use_cache: use_cache.
  Gemma2Config.rope_theta: rope_theta.
  Gemma2Config.attention_bias: attention_bias.
  Gemma2Config.final_logit_softcapping: final_logit_softcapping.
  Gemma2Config.cache_implementation: cache_implementation.
  Gemma2Config.attn_logit_softcapping: attn_logit_softcapping.
  Gemma2Config.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/gemma2/gemma2_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py)

## Classes
### `Gemma2Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/gemma2/gemma2_configuration.py:25`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L25)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class Gemma2Config(EasyDeLBaseConfig):`
- members:
  - `get_mask_details(self)` — [`L174`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L174) — Retrieve attention mask details for each layer in the model.
  - `get_partition_rules(self, *args, **kwargs)` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L161) — Returns partition rules for model sharding.
  - `attention_bias` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L137)
  - `attention_dropout` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L138)
  - `attn_logit_softcapping` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L159)
  - `bits` — [`L121`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L121)
  - `cache_implementation` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L158)
  - `final_logit_softcapping` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L155)
  - `gradient_checkpointing` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L120)
  - `head_dim` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L130)
  - `hidden_activation` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L132)
  - `hidden_size` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L126)
  - `initializer_range` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L133)
  - `intermediate_size` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L127)
  - `layer_types` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L139)
  - `max_position_embeddings` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L125)
  - `model_type` — [`L87`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L87)
  - `num_attention_heads` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L129)
  - `num_hidden_layers` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L128)
  - `num_key_value_heads` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L131)
  - `query_pre_attn_scalar` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L156)
  - `rms_norm_eps` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L134)
  - `rope_theta` — [`L136`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L136)
  - `scan_layers` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L122)
  - `sliding_window` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L157)
  - `use_cache` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L135)
  - `vocab_size` — [`L124`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L124)
- protocol/private: `__init__`[`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/gemma2_configuration.py#L89)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`from_hf`](../../infra/utils.md#AttnMaskType.from_hf)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`embed_tokens`](modeling_gemma2.md#Gemma2Model.embed_tokens), [`Gemma2Model`](modeling_gemma2.md#Gemma2Model), [`Gemma2ForCausalLM`](modeling_gemma2.md#Gemma2ForCausalLM), [`Gemma2ForSequenceClassification`](modeling_gemma2.md#Gemma2ForSequenceClassification), [`act`](modeling_gemma2.md#Gemma2MLP.act), [`kernel`](modeling_gemma2.md#Gemma2RMSNorm.kernel), [`_create_attention_performer`](modeling_gemma2.md#Gemma2Attention._create_attention_performer), [`precision`](modeling_gemma2.md#Gemma2MLP.precision), [`__init__`](modeling_gemma2.md#Gemma2ForCausalLM.__init__), [`__init__`](modeling_gemma2.md#Gemma2ForSequenceClassification.__init__), [`_create_rotary`](modeling_gemma2.md#Gemma2Attention._create_rotary), [`is_cross_attention`](modeling_gemma2.md#Gemma2Attention.is_cross_attention), [`epsilon`](modeling_gemma2.md#Gemma2RMSNorm.epsilon), [`__init__`](modeling_gemma2.md#Gemma2Model.__init__), [`__init__`](modeling_gemma2.md#Gemma2Attention.__init__), [`__init__`](modeling_gemma2.md#Gemma2DecoderLayer.__init__), [`__init__`](modeling_gemma2.md#Gemma2MLP.__init__), [`__init__`](modeling_gemma2.md#Gemma2RMSNorm.__init__), [`_config_class`](modeling_gemma2.md#Gemma2ForCausalLM._config_class), [`_config_class`](modeling_gemma2.md#Gemma2ForSequenceClassification._config_class)

