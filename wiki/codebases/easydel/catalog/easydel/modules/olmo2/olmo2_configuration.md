---
title: 'Module: easydel/modules/olmo2/olmo2_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/olmo2/olmo2_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.olmo2.olmo2_configuration`/Olmo2Config#
symbols:
  Olmo2Config: ''
  Olmo2Config.rope_scaling: rope_scaling.
  Olmo2Config.hidden_size: hidden_size.
  Olmo2Config.layer_types: layer_types.
  Olmo2Config.rms_norm_eps: rms_norm_eps.
  Olmo2Config.__init__: __init__().
  Olmo2Config._rope_scaling_validation: _rope_scaling_validation().
  Olmo2Config.initializer_range: initializer_range.
  Olmo2Config.intermediate_size: intermediate_size.
  Olmo2Config.bits: bits.
  Olmo2Config.hidden_act: hidden_act.
  Olmo2Config.use_scan_mlp: use_scan_mlp.
  Olmo2Config.scan_mlp_chunk_size: scan_mlp_chunk_size.
  Olmo2Config.vocab_size: vocab_size.
  Olmo2Config.gradient_checkpointing: gradient_checkpointing.
  Olmo2Config.num_hidden_layers: num_hidden_layers.
  Olmo2Config.model_type: model_type.
  Olmo2Config.keys_to_ignore_at_inference: keys_to_ignore_at_inference.
  Olmo2Config.max_position_embeddings: max_position_embeddings.
  Olmo2Config.num_attention_heads: num_attention_heads.
  Olmo2Config.num_key_value_heads: num_key_value_heads.
  Olmo2Config.head_dim: head_dim.
  Olmo2Config.use_cache: use_cache.
  Olmo2Config.rope_theta: rope_theta.
  Olmo2Config.attention_bias: attention_bias.
  Olmo2Config.attention_dropout: attention_dropout.
  Olmo2Config.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/olmo2/olmo2_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py)

## Classes
### `Olmo2Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/olmo2/olmo2_configuration.py:26`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L26)
- doc: This is the configuration class to store the configuration of a \[`Olmo2Model`\]. It is used to instantiate an OLMo2
- signature: `class Olmo2Config(EasyDeLBaseConfig):`
- members:
  - `_rope_scaling_validation(self)` — [`L177`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L177) — Validates the `rope_scaling` configuration dictionary to ensure it meets the expected format and values.
  - `get_partition_rules(self, *args, **kwargs)` — [`L206`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L206) — Returns partition rules for model sharding.
  - `attention_bias` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L169)
  - `attention_dropout` — [`L170`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L170)
  - `bits` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L142)
  - `gradient_checkpointing` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L139)
  - `head_dim` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L162)
  - `hidden_act` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L163)
  - `hidden_size` — [`L152`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L152)
  - `initializer_range` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L164)
  - `intermediate_size` — [`L153`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L153)
  - `keys_to_ignore_at_inference` — [`L108`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L108)
  - `layer_types` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L173)
  - `max_position_embeddings` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L151)
  - `model_type` — [`L107`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L107)
  - `num_attention_heads` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L155)
  - `num_hidden_layers` — [`L154`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L154)
  - `num_key_value_heads` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L161)
  - `rms_norm_eps` — [`L172`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L172)
  - `rope_scaling` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L167)
  - `rope_theta` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L166)
  - `scan_mlp_chunk_size` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L141)
  - `use_cache` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L165)
  - `use_scan_mlp` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L140)
  - `vocab_size` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L150)
- protocol/private: `__init__`[`L110`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/olmo2_configuration.py#L110)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`__call__`](modeling_olmo2.md#Olmo2DecoderLayer.__call__), [`embed_tokens`](modeling_olmo2.md#Olmo2Model.embed_tokens), [`Olmo2Model`](modeling_olmo2.md#Olmo2Model), [`Olmo2ForCausalLM`](modeling_olmo2.md#Olmo2ForCausalLM), [`Olmo2ForSequenceClassification`](modeling_olmo2.md#Olmo2ForSequenceClassification), [`_create_k_norm`](modeling_olmo2.md#Olmo2Attention._create_k_norm), [`_create_q_norm`](modeling_olmo2.md#Olmo2Attention._create_q_norm), [`act_fn`](modeling_olmo2.md#Olmo2MLP.act_fn), [`norm`](modeling_olmo2.md#Olmo2Model.norm), [`post_attention_layernorm`](modeling_olmo2.md#Olmo2DecoderLayer.post_attention_layernorm), [`post_feedforward_layernorm`](modeling_olmo2.md#Olmo2DecoderLayer.post_feedforward_layernorm), [`__init__`](modeling_olmo2.md#Olmo2ForCausalLM.__init__), [`__init__`](modeling_olmo2.md#Olmo2ForSequenceClassification.__init__), [`precision`](modeling_olmo2.md#Olmo2MLP.precision), [`down_proj`](modeling_olmo2.md#Olmo2MLP.down_proj), [`gate_proj`](modeling_olmo2.md#Olmo2MLP.gate_proj), [`up_proj`](modeling_olmo2.md#Olmo2MLP.up_proj), [`__init__`](modeling_olmo2.md#Olmo2Attention.__init__), [`__init__`](modeling_olmo2.md#Olmo2Model.__init__), [`__init__`](modeling_olmo2.md#Olmo2DecoderLayer.__init__), [`__init__`](modeling_olmo2.md#Olmo2MLP.__init__), [`_config_class`](modeling_olmo2.md#Olmo2ForCausalLM._config_class), [`_config_class`](modeling_olmo2.md#Olmo2ForSequenceClassification._config_class)

