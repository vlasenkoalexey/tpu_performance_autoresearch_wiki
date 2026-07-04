---
title: 'Module: easydel/modules/olmo3/olmo3_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/olmo3/olmo3_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.olmo3.olmo3_configuration`/Olmo3Config#
symbols:
  Olmo3Config: ''
  Olmo3Config.layer_types: layer_types.
  Olmo3Config.rope_scaling: rope_scaling.
  Olmo3Config.hidden_size: hidden_size.
  Olmo3Config._validate_layer_types: _validate_layer_types().
  Olmo3Config.rms_norm_eps: rms_norm_eps.
  Olmo3Config.__init__: __init__().
  Olmo3Config._rope_scaling_validation: _rope_scaling_validation().
  Olmo3Config.initializer_range: initializer_range.
  Olmo3Config.intermediate_size: intermediate_size.
  Olmo3Config.num_hidden_layers: num_hidden_layers.
  Olmo3Config.bits: bits.
  Olmo3Config.hidden_act: hidden_act.
  Olmo3Config.sliding_window: sliding_window.
  Olmo3Config.num_attention_heads: num_attention_heads.
  Olmo3Config.num_key_value_heads: num_key_value_heads.
  Olmo3Config.use_scan_mlp: use_scan_mlp.
  Olmo3Config.scan_mlp_chunk_size: scan_mlp_chunk_size.
  Olmo3Config.vocab_size: vocab_size.
  Olmo3Config.gradient_checkpointing: gradient_checkpointing.
  Olmo3Config.model_type: model_type.
  Olmo3Config.keys_to_ignore_at_inference: keys_to_ignore_at_inference.
  Olmo3Config.max_position_embeddings: max_position_embeddings.
  Olmo3Config.use_cache: use_cache.
  Olmo3Config.rope_theta: rope_theta.
  Olmo3Config.attention_bias: attention_bias.
  Olmo3Config.attention_dropout: attention_dropout.
  Olmo3Config.head_dim: head_dim.
  Olmo3Config.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/olmo3/olmo3_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py)

## Classes
### `Olmo3Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/olmo3/olmo3_configuration.py:26`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L26)
- doc: This is the configuration class to store the configuration of a \[`Olmo3Model`\]. It is used to instantiate an OLMo3
- signature: `class Olmo3Config(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 50304, hidden_size: int = 4096, intermediate_size: int = 11008, num_hidden_layers: int = 32, num_attention_heads: int = 32, num_key_value_heads: int | None = None, hidden_act: str = "silu", max_position_embeddings: int = 2048, initializer_range: float = 0.02, use_cache: bool = True, pad_token_id: int = 1, bos_token_id: int | None = None, eos_token_id: int = 50279, tie_word_embeddings: bool = False, rope_theta: float = 10000, rope_scaling: dict | None = None, attention_bias: bool = False, attention_dropout: float = 0, rms_norm_eps: float = 0.00001, sliding_window: int = 4096, layer_types: list[str] | None = None, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, use_scan_mlp: bool = False, scan_mlp_chunk_size: int = 1024, bits: int | None = None, **kwargs)` — [`L111`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L111) — Initializes an Olmo3Config object.
  - `_rope_scaling_validation(self)` — [`L216`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L216) — Validates the `rope_scaling` configuration dictionary to ensure it meets the expected format and values.
  - `_validate_layer_types(self)` — [`L245`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L245) — Validates the `layer_types` list to ensure it has correct length and valid values.
  - `get_partition_rules(self, *args, **kwargs)` — [`L263`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L263) — Returns partition rules for model sharding.
  - `attention_bias` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L201)
  - `attention_dropout` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L202)
  - `bits` — [`L175`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L175)
  - `gradient_checkpointing` — [`L172`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L172)
  - `head_dim` — [`L205`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L205)
  - `hidden_act` — [`L195`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L195)
  - `hidden_size` — [`L185`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L185)
  - `initializer_range` — [`L196`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L196)
  - `intermediate_size` — [`L186`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L186)
  - `keys_to_ignore_at_inference` — [`L109`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L109)
  - `layer_types` — [`L209`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L209)
  - `max_position_embeddings` — [`L184`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L184)
  - `model_type` — [`L108`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L108)
  - `num_attention_heads` — [`L188`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L188)
  - `num_hidden_layers` — [`L187`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L187)
  - `num_key_value_heads` — [`L194`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L194)
  - `rms_norm_eps` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L203)
  - `rope_scaling` — [`L199`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L199)
  - `rope_theta` — [`L198`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L198)
  - `scan_mlp_chunk_size` — [`L174`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L174)
  - `sliding_window` — [`L204`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L204)
  - `use_cache` — [`L197`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L197)
  - `use_scan_mlp` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L173)
  - `vocab_size` — [`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/olmo3_configuration.py#L183)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`__call__`](modeling_olmo3.md#Olmo3DecoderLayer.__call__), [`embed_tokens`](modeling_olmo3.md#Olmo3Model.embed_tokens), [`Olmo3Model`](modeling_olmo3.md#Olmo3Model), [`Olmo3ForCausalLM`](modeling_olmo3.md#Olmo3ForCausalLM), [`Olmo3ForSequenceClassification`](modeling_olmo3.md#Olmo3ForSequenceClassification), [`_create_k_norm`](modeling_olmo3.md#Olmo3Attention._create_k_norm), [`_create_q_norm`](modeling_olmo3.md#Olmo3Attention._create_q_norm), [`act_fn`](modeling_olmo3.md#Olmo3MLP.act_fn), [`norm`](modeling_olmo3.md#Olmo3Model.norm), [`post_attention_layernorm`](modeling_olmo3.md#Olmo3DecoderLayer.post_attention_layernorm), [`post_feedforward_layernorm`](modeling_olmo3.md#Olmo3DecoderLayer.post_feedforward_layernorm), [`__init__`](modeling_olmo3.md#Olmo3ForCausalLM.__init__), [`__init__`](modeling_olmo3.md#Olmo3ForSequenceClassification.__init__), [`precision`](modeling_olmo3.md#Olmo3MLP.precision), [`down_proj`](modeling_olmo3.md#Olmo3MLP.down_proj), [`gate_proj`](modeling_olmo3.md#Olmo3MLP.gate_proj), [`up_proj`](modeling_olmo3.md#Olmo3MLP.up_proj), [`__init__`](modeling_olmo3.md#Olmo3Attention.__init__), [`__init__`](modeling_olmo3.md#Olmo3Model.__init__), [`attention_type_name`](modeling_olmo3.md#Olmo3Attention.attention_type_name), [`__init__`](modeling_olmo3.md#Olmo3DecoderLayer.__init__), [`__init__`](modeling_olmo3.md#Olmo3MLP.__init__), [`_config_class`](modeling_olmo3.md#Olmo3ForCausalLM._config_class), [`_config_class`](modeling_olmo3.md#Olmo3ForSequenceClassification._config_class)

