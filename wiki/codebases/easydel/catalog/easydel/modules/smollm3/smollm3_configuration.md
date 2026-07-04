---
title: 'Module: easydel/modules/smollm3/smollm3_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/smollm3/smollm3_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.smollm3.smollm3_configuration`/SmolLM3Config#
symbols:
  SmolLM3Config: ''
  SmolLM3Config.layer_types: layer_types.
  SmolLM3Config.rope_scaling: rope_scaling.
  SmolLM3Config.no_rope_layers: no_rope_layers.
  SmolLM3Config.hidden_size: hidden_size.
  SmolLM3Config._validate_no_rope_layers: _validate_no_rope_layers().
  SmolLM3Config._validate_layer_types: _validate_layer_types().
  SmolLM3Config.num_hidden_layers: num_hidden_layers.
  SmolLM3Config._rope_scaling_validation: _rope_scaling_validation().
  SmolLM3Config.rms_norm_eps: rms_norm_eps.
  SmolLM3Config.mlp_bias: mlp_bias.
  SmolLM3Config.initializer_range: initializer_range.
  SmolLM3Config.sliding_window: sliding_window.
  SmolLM3Config.intermediate_size: intermediate_size.
  SmolLM3Config.vocab_size: vocab_size.
  SmolLM3Config.model_type: model_type.
  SmolLM3Config.keys_to_ignore_at_inference: keys_to_ignore_at_inference.
  SmolLM3Config.__init__: __init__().
  SmolLM3Config.num_attention_heads: num_attention_heads.
  SmolLM3Config.hidden_act: hidden_act.
  SmolLM3Config.max_position_embeddings: max_position_embeddings.
  SmolLM3Config.use_cache: use_cache.
  SmolLM3Config.attention_bias: attention_bias.
  SmolLM3Config.attention_dropout: attention_dropout.
  SmolLM3Config.use_sliding_window: use_sliding_window.
  SmolLM3Config.no_rope_layer_interval: no_rope_layer_interval.
  SmolLM3Config.rope_theta: rope_theta.
  SmolLM3Config.num_key_value_heads: num_key_value_heads.
  SmolLM3Config.head_dim: head_dim.
  SmolLM3Config.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/smollm3/smollm3_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py)

## Classes
### `SmolLM3Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/smollm3/smollm3_configuration.py:25`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L25)
- doc: This is the configuration class to store the configuration of a \[`SmolLM3Model`\]. It is used to
- signature: `class SmolLM3Config(EasyDeLBaseConfig):`
- members:
  - `_rope_scaling_validation(self)` — [`L180`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L180) — Validate rope_scaling configuration.
  - `_validate_layer_types(self)` — [`L223`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L223) — Validate layer_types list.
  - `_validate_no_rope_layers(self)` — [`L211`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L211) — Validate no_rope_layers list.
  - `get_partition_rules(self, *args, **kwargs)` — [`L236`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L236) — Returns partition rules for model sharding.
  - `attention_bias` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L135)
  - `attention_dropout` — [`L136`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L136)
  - `head_dim` — [`L148`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L148)
  - `hidden_act` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L130)
  - `hidden_size` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L126)
  - `initializer_range` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L132)
  - `intermediate_size` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L129)
  - `keys_to_ignore_at_inference` — [`L94`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L94)
  - `layer_types` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L165)
  - `max_position_embeddings` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L131)
  - `mlp_bias` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L137)
  - `model_type` — [`L93`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L93)
  - `no_rope_layer_interval` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L140)
  - `no_rope_layers` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L151)
  - `num_attention_heads` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L128)
  - `num_hidden_layers` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L127)
  - `num_key_value_heads` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L147)
  - `rms_norm_eps` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L133)
  - `rope_scaling` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L142)
  - `rope_theta` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L141)
  - `sliding_window` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L139)
  - `use_cache` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L134)
  - `use_sliding_window` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L138)
  - `vocab_size` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L125)
- protocol/private: `__init__`[`L96`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/smollm3_configuration.py#L96)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`embed_tokens`](modeling_smollm3.md#SmolLM3Model.embed_tokens), [`SmolLM3Model`](modeling_smollm3.md#SmolLM3Model), [`SmolLM3ForCausalLM`](modeling_smollm3.md#SmolLM3ForCausalLM), [`SmolLM3ForSequenceClassification`](modeling_smollm3.md#SmolLM3ForSequenceClassification), [`_create_rotary`](modeling_smollm3.md#SmolLM3Attention._create_rotary), [`precision`](modeling_smollm3.md#SmolLM3MLP.precision), [`input_layernorm`](modeling_smollm3.md#SmolLM3DecoderLayer.input_layernorm), [`is_sliding`](modeling_smollm3.md#SmolLM3Attention.is_sliding), [`norm`](modeling_smollm3.md#SmolLM3Model.norm), [`post_attention_layernorm`](modeling_smollm3.md#SmolLM3DecoderLayer.post_attention_layernorm), [`__init__`](modeling_smollm3.md#SmolLM3ForCausalLM.__init__), [`__init__`](modeling_smollm3.md#SmolLM3ForSequenceClassification.__init__), [`_create_mlp`](modeling_smollm3.md#SmolLM3DecoderLayer._create_mlp), [`use_rope`](modeling_smollm3.md#SmolLM3Attention.use_rope), [`hidden_size`](modeling_smollm3.md#SmolLM3MLP.hidden_size), [`intermediate_size`](modeling_smollm3.md#SmolLM3MLP.intermediate_size), [`__init__`](modeling_smollm3.md#SmolLM3Model.__init__), [`layers`](modeling_smollm3.md#SmolLM3Model.layers), [`__init__`](modeling_smollm3.md#SmolLM3Attention.__init__), [`__init__`](modeling_smollm3.md#SmolLM3DecoderLayer.__init__), [`__init__`](modeling_smollm3.md#SmolLM3MLP.__init__), [`_config_class`](modeling_smollm3.md#SmolLM3ForCausalLM._config_class), [`_config_class`](modeling_smollm3.md#SmolLM3ForSequenceClassification._config_class), [`hidden_size`](modeling_smollm3.md#SmolLM3DecoderLayer.hidden_size)

