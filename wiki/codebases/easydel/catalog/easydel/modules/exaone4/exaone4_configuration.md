---
title: 'Module: easydel/modules/exaone4/exaone4_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/exaone4/exaone4_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.exaone4.exaone4_configuration`/Exaone4Config#
symbols:
  Exaone4Config: ''
  Exaone4Config.layer_types: layer_types.
  Exaone4Config.rope_scaling: rope_scaling.
  Exaone4Config.hidden_size: hidden_size.
  Exaone4Config._validate_layer_types: _validate_layer_types().
  Exaone4Config.rms_norm_eps: rms_norm_eps.
  Exaone4Config.head_dim: head_dim.
  Exaone4Config._rope_scaling_validation: _rope_scaling_validation().
  Exaone4Config.num_hidden_layers: num_hidden_layers.
  Exaone4Config.intermediate_size: intermediate_size.
  Exaone4Config.initializer_range: initializer_range.
  Exaone4Config.sliding_window: sliding_window.
  Exaone4Config.vocab_size: vocab_size.
  Exaone4Config.hidden_act: hidden_act.
  Exaone4Config.model_type: model_type.
  Exaone4Config.keys_to_ignore_at_inference: keys_to_ignore_at_inference.
  Exaone4Config.__init__: __init__().
  Exaone4Config.num_attention_heads: num_attention_heads.
  Exaone4Config.max_position_embeddings: max_position_embeddings.
  Exaone4Config.use_cache: use_cache.
  Exaone4Config.attention_dropout: attention_dropout.
  Exaone4Config.sliding_window_pattern: sliding_window_pattern.
  Exaone4Config.rope_theta: rope_theta.
  Exaone4Config.num_key_value_heads: num_key_value_heads.
  Exaone4Config.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/exaone4/exaone4_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py)

## Classes
### `Exaone4Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/exaone4/exaone4_configuration.py:25`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L25)
- doc: This is the configuration class to store the configuration of a \[`Exaone4Model`\]. It is used to
- signature: `class Exaone4Config(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 102400, hidden_size: int = 4096, intermediate_size: int = 16384, num_hidden_layers: int = 32, num_attention_heads: int = 32, num_key_value_heads: int | None = None, hidden_act: str = "silu", max_position_embeddings: int = 2048, initializer_range: float = 0.02, rms_norm_eps: float = 0.00001, use_cache: bool = True, pad_token_id: int = 1, bos_token_id: int = 0, eos_token_id: int = 2, tie_word_embeddings: bool = False, rope_theta: float = 10000, rope_scaling: dict | None = None, attention_dropout: float = 0, sliding_window: int | None = 4096, sliding_window_pattern: int = 4, layer_types: list[str] | None = None, **kwargs)` — [`L86`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L86) — Initialize Exaone4Config.
  - `_rope_scaling_validation(self)` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L162) — Validate rope_scaling configuration.
  - `_validate_layer_types(self)` — [`L193`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L193) — Validate layer_types list.
  - `get_partition_rules(self, *args, **kwargs)` — [`L206`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L206) — Returns partition rules for model sharding.
  - `attention_dropout` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L123)
  - `head_dim` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L134)
  - `hidden_act` — [`L118`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L118)
  - `hidden_size` — [`L114`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L114)
  - `initializer_range` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L120)
  - `intermediate_size` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L117)
  - `keys_to_ignore_at_inference` — [`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L84)
  - `layer_types` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L141)
  - `max_position_embeddings` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L119)
  - `model_type` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L83)
  - `num_attention_heads` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L116)
  - `num_hidden_layers` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L115)
  - `num_key_value_heads` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L133)
  - `rms_norm_eps` — [`L121`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L121)
  - `rope_scaling` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L127)
  - `rope_theta` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L126)
  - `sliding_window` — [`L124`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L124)
  - `sliding_window_pattern` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L125)
  - `use_cache` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L122)
  - `vocab_size` — [`L113`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/exaone4_configuration.py#L113)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`embed_tokens`](modeling_exaone4.md#Exaone4Model.embed_tokens), [`Exaone4Model`](modeling_exaone4.md#Exaone4Model), [`Exaone4ForCausalLM`](modeling_exaone4.md#Exaone4ForCausalLM), [`Exaone4ForSequenceClassification`](modeling_exaone4.md#Exaone4ForSequenceClassification), [`is_sliding`](modeling_exaone4.md#Exaone4Attention.is_sliding), [`_create_k_norm`](modeling_exaone4.md#Exaone4Attention._create_k_norm), [`_create_q_norm`](modeling_exaone4.md#Exaone4Attention._create_q_norm), [`_create_rotary`](modeling_exaone4.md#Exaone4Attention._create_rotary), [`norm`](modeling_exaone4.md#Exaone4Model.norm), [`post_attention_layernorm`](modeling_exaone4.md#Exaone4DecoderLayer.post_attention_layernorm), [`post_feedforward_layernorm`](modeling_exaone4.md#Exaone4DecoderLayer.post_feedforward_layernorm), [`__init__`](modeling_exaone4.md#Exaone4ForCausalLM.__init__), [`__init__`](modeling_exaone4.md#Exaone4ForSequenceClassification.__init__), [`precision`](modeling_exaone4.md#Exaone4MLP.precision), [`act_fn`](modeling_exaone4.md#Exaone4MLP.act_fn), [`down_proj`](modeling_exaone4.md#Exaone4MLP.down_proj), [`gate_proj`](modeling_exaone4.md#Exaone4MLP.gate_proj), [`up_proj`](modeling_exaone4.md#Exaone4MLP.up_proj), [`__init__`](modeling_exaone4.md#Exaone4Model.__init__), [`layers`](modeling_exaone4.md#Exaone4Model.layers), [`__init__`](modeling_exaone4.md#Exaone4Attention.__init__), [`__init__`](modeling_exaone4.md#Exaone4DecoderLayer.__init__), [`__init__`](modeling_exaone4.md#Exaone4MLP.__init__), [`_config_class`](modeling_exaone4.md#Exaone4ForCausalLM._config_class), [`_config_class`](modeling_exaone4.md#Exaone4ForSequenceClassification._config_class)

