---
title: 'Module: easydel/modules/olmo/olmo_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/olmo/olmo_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.olmo.olmo_configuration`/OlmoConfig#
symbols:
  OlmoConfig: ''
  OlmoConfig.layer_types: layer_types.
  OlmoConfig.hidden_size: hidden_size.
  OlmoConfig.__init__: __init__().
  OlmoConfig.initializer_range: initializer_range.
  OlmoConfig.intermediate_size: intermediate_size.
  OlmoConfig.num_hidden_layers: num_hidden_layers.
  OlmoConfig.hidden_act: hidden_act.
  OlmoConfig.use_scan_mlp: use_scan_mlp.
  OlmoConfig.scan_mlp_chunk_size: scan_mlp_chunk_size.
  OlmoConfig.vocab_size: vocab_size.
  OlmoConfig.gradient_checkpointing: gradient_checkpointing.
  OlmoConfig.model_type: model_type.
  OlmoConfig.max_position_embeddings: max_position_embeddings.
  OlmoConfig.num_attention_heads: num_attention_heads.
  OlmoConfig.num_key_value_heads: num_key_value_heads.
  OlmoConfig.head_dim: head_dim.
  OlmoConfig.use_cache: use_cache.
  OlmoConfig.rope_theta: rope_theta.
  OlmoConfig.rope_scaling: rope_scaling.
  OlmoConfig.attention_bias: attention_bias.
  OlmoConfig.attention_dropout: attention_dropout.
  OlmoConfig.clip_qkv: clip_qkv.
  OlmoConfig.bits: bits.
  OlmoConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/olmo/olmo_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py)

## Classes
### `OlmoConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/olmo/olmo_configuration.py:24`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L24)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class OlmoConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 50304, hidden_size: int = 4096, intermediate_size: int = 11008, num_hidden_layers: int = 32, num_attention_heads: int = 32, num_key_value_heads: int | None = None, head_dim: int | None = None, hidden_act: str = "silu", max_position_embeddings: int = 2048, initializer_range: float = 0.02, use_cache: bool = True, pad_token_id: int = 1, bos_token_id: int | None = None, eos_token_id: int = 50279, tie_word_embeddings: bool = False, rope_theta: float = 10000, rope_scaling: dict | None = None, attention_bias: bool = False, attention_dropout: float = 0, clip_qkv: float | None = None, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, use_scan_mlp: bool = False, scan_mlp_chunk_size: int = 1024, bits: int | None = None, layer_types: list[str] | None = None, **kwargs)` — [`L88`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L88) — Initializes an OlmoConfig object.
  - `get_partition_rules(self, *args, **kwargs)` — [`L182`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L182) — Returns partition rules for model sharding.
  - `attention_bias` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L164)
  - `attention_dropout` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L165)
  - `bits` — [`L170`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L170)
  - `clip_qkv` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L166)
  - `gradient_checkpointing` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L167)
  - `head_dim` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L158)
  - `hidden_act` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L159)
  - `hidden_size` — [`L148`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L148)
  - `initializer_range` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L160)
  - `intermediate_size` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L149)
  - `layer_types` — [`L171`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L171)
  - `max_position_embeddings` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L147)
  - `model_type` — [`L86`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L86)
  - `num_attention_heads` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L151)
  - `num_hidden_layers` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L150)
  - `num_key_value_heads` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L157)
  - `rope_scaling` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L163)
  - `rope_theta` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L162)
  - `scan_mlp_chunk_size` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L169)
  - `use_cache` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L161)
  - `use_scan_mlp` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L168)
  - `vocab_size` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/olmo_configuration.py#L146)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`__call__`](modeling_olmo.md#OlmoDecoderLayer.__call__), [`embed_tokens`](modeling_olmo.md#OlmoModel.embed_tokens), [`OlmoModel`](modeling_olmo.md#OlmoModel), [`OlmoForCausalLM`](modeling_olmo.md#OlmoForCausalLM), [`OlmoForSequenceClassification`](modeling_olmo.md#OlmoForSequenceClassification), [`act_fn`](modeling_olmo.md#OlmoMLP.act_fn), [`__init__`](modeling_olmo.md#OlmoForCausalLM.__init__), [`__init__`](modeling_olmo.md#OlmoForSequenceClassification.__init__), [`precision`](modeling_olmo.md#OlmoMLP.precision), [`down_proj`](modeling_olmo.md#OlmoMLP.down_proj), [`gate_proj`](modeling_olmo.md#OlmoMLP.gate_proj), [`input_layernorm`](modeling_olmo.md#OlmoDecoderLayer.input_layernorm), [`norm`](modeling_olmo.md#OlmoModel.norm), [`post_attention_layernorm`](modeling_olmo.md#OlmoDecoderLayer.post_attention_layernorm), [`up_proj`](modeling_olmo.md#OlmoMLP.up_proj), [`__init__`](modeling_olmo.md#OlmoModel.__init__), [`layers`](modeling_olmo.md#OlmoModel.layers), [`__init__`](modeling_olmo.md#OlmoAttention.__init__), [`__init__`](modeling_olmo.md#OlmoDecoderLayer.__init__), [`__init__`](modeling_olmo.md#OlmoMLP.__init__), [`_config_class`](modeling_olmo.md#OlmoForCausalLM._config_class), [`_config_class`](modeling_olmo.md#OlmoForSequenceClassification._config_class)

