---
title: 'Module: easydel/modules/cohere/cohere_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/cohere/cohere_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.cohere.cohere_configuration`/CohereConfig#
symbols:
  CohereConfig: ''
  CohereConfig.layer_types: layer_types.
  CohereConfig.__init__: __init__().
  CohereConfig.hidden_size: hidden_size.
  CohereConfig.intermediate_size: intermediate_size.
  CohereConfig.initializer_range: initializer_range.
  CohereConfig.layer_norm_eps: layer_norm_eps.
  CohereConfig.num_hidden_layers: num_hidden_layers.
  CohereConfig.vocab_size: vocab_size.
  CohereConfig.use_qk_norm: use_qk_norm.
  CohereConfig.gradient_checkpointing: gradient_checkpointing.
  CohereConfig.model_type: model_type.
  CohereConfig.max_position_embeddings: max_position_embeddings.
  CohereConfig.logit_scale: logit_scale.
  CohereConfig.num_attention_heads: num_attention_heads.
  CohereConfig.num_key_value_heads: num_key_value_heads.
  CohereConfig.hidden_act: hidden_act.
  CohereConfig.use_cache: use_cache.
  CohereConfig.rope_theta: rope_theta.
  CohereConfig.attention_bias: attention_bias.
  CohereConfig.attention_dropout: attention_dropout.
  CohereConfig.bits: bits.
  CohereConfig.head_dim: head_dim.
  CohereConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/cohere/cohere_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py)

## Classes
### `CohereConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/cohere/cohere_configuration.py:24`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L24)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class CohereConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L150) — Returns partition rules for model sharding.
  - `attention_bias` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L134)
  - `attention_dropout` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L135)
  - `bits` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L137)
  - `gradient_checkpointing` — [`L136`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L136)
  - `head_dim` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L138)
  - `hidden_act` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L129)
  - `hidden_size` — [`L118`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L118)
  - `initializer_range` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L130)
  - `intermediate_size` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L120)
  - `layer_norm_eps` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L131)
  - `layer_types` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L139)
  - `logit_scale` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L119)
  - `max_position_embeddings` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L117)
  - `model_type` — [`L87`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L87)
  - `num_attention_heads` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L122)
  - `num_hidden_layers` — [`L121`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L121)
  - `num_key_value_heads` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L128)
  - `rope_theta` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L133)
  - `use_cache` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L132)
  - `use_qk_norm` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L123)
  - `vocab_size` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L116)
- protocol/private: `__init__`[`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/cohere_configuration.py#L89)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`embed_tokens`](modeling_cohere.md#CohereModel.embed_tokens), [`CohereModel`](modeling_cohere.md#CohereModel), [`CohereForCausalLM`](modeling_cohere.md#CohereForCausalLM), [`CohereForSequenceClassification`](modeling_cohere.md#CohereForSequenceClassification), [`k_norm`](modeling_cohere.md#CohereAttention.k_norm), [`q_norm`](modeling_cohere.md#CohereAttention.q_norm), [`precision`](modeling_cohere.md#CohereMLP.precision), [`input_layernorm`](modeling_cohere.md#CohereBlock.input_layernorm), [`__init__`](modeling_cohere.md#CohereAttention.__init__), [`__init__`](modeling_cohere.md#CohereForCausalLM.__init__), [`__init__`](modeling_cohere.md#CohereForSequenceClassification.__init__), [`_create_rotary`](modeling_cohere.md#CohereAttention._create_rotary), [`down_proj`](modeling_cohere.md#CohereMLP.down_proj), [`gate_proj`](modeling_cohere.md#CohereMLP.gate_proj), [`up_proj`](modeling_cohere.md#CohereMLP.up_proj), [`__init__`](modeling_cohere.md#CohereModel.__init__), [`layers`](modeling_cohere.md#CohereModel.layers), [`__init__`](modeling_cohere.md#CohereBlock.__init__), [`__init__`](modeling_cohere.md#CohereMLP.__init__), [`_config_class`](modeling_cohere.md#CohereForCausalLM._config_class), [`_config_class`](modeling_cohere.md#CohereForSequenceClassification._config_class)

