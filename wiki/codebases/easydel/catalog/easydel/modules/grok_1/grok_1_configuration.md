---
title: 'Module: easydel/modules/grok_1/grok_1_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/grok_1/grok_1_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.grok_1.grok_1_configuration`/Grok1Config#
symbols:
  Grok1Config: ''
  Grok1Config.hidden_size: hidden_size.
  Grok1Config.layer_types: layer_types.
  Grok1Config.initializer_range: initializer_range.
  Grok1Config.__init__: __init__().
  Grok1Config.rms_norm_eps: rms_norm_eps.
  Grok1Config.intermediate_size: intermediate_size.
  Grok1Config.num_experts: num_experts.
  Grok1Config.num_attention_heads: num_attention_heads.
  Grok1Config.num_key_value_heads: num_key_value_heads.
  Grok1Config.num_hidden_layers: num_hidden_layers.
  Grok1Config.attention_dropout: attention_dropout.
  Grok1Config.resid_pdrop: resid_pdrop.
  Grok1Config.num_experts_per_tok: num_experts_per_tok.
  Grok1Config.gradient_checkpointing: gradient_checkpointing.
  Grok1Config.model_type: model_type.
  Grok1Config.vocab_size: vocab_size.
  Grok1Config.attn_output_multiplier: attn_output_multiplier.
  Grok1Config.max_attn_value: max_attn_value.
  Grok1Config.max_position_embeddings: max_position_embeddings.
  Grok1Config.embedding_multiplier_scale: embedding_multiplier_scale.
  Grok1Config.output_multiplier_scale: output_multiplier_scale.
  Grok1Config.use_cache: use_cache.
  Grok1Config.rope_theta: rope_theta.
  Grok1Config.output_router_logits: output_router_logits.
  Grok1Config.router_aux_loss_coef: router_aux_loss_coef.
  Grok1Config.bits: bits.
  Grok1Config.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/grok_1/grok_1_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py)

## Classes
### `Grok1Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/grok_1/grok_1_configuration.py:24`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L24)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class Grok1Config(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 32000, hidden_size: int = 4096, intermediate_size: int = 32768, num_hidden_layers: int = 32, num_attention_heads: int = 32, num_key_value_heads: int | None = 32, attn_output_multiplier: float = 1, max_attn_value: float = 1, max_position_embeddings: int = 4096, embedding_multiplier_scale: float = 1, output_multiplier_scale: float = 1, initializer_range: float = 0.02, rms_norm_eps: float = 0.00001, attention_dropout: float = 0, resid_pdrop: float = 0, use_cache: bool = True, pad_token_id: int | None = None, bos_token_id: int = 1, eos_token_id: int = 2, tie_word_embeddings: bool = True, num_experts_per_tok: int = 2, num_experts: int = 8, output_router_logits: bool = False, router_aux_loss_coef: float = 0.001, rope_theta: float = 10000, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, bits: int | None = None, layer_types: list[str] | None = None, **kwargs)` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L83) — Initializes a Grok1Config object.
  - `get_partition_rules(self, *args, **kwargs)` — [`L182`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L182) — Returns partition rules for model sharding.
  - `attention_dropout` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L161)
  - `attn_output_multiplier` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L145)
  - `bits` — [`L170`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L170)
  - `embedding_multiplier_scale` — [`L148`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L148)
  - `gradient_checkpointing` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L169)
  - `hidden_size` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L150)
  - `initializer_range` — [`L154`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L154)
  - `intermediate_size` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L151)
  - `layer_types` — [`L171`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L171)
  - `max_attn_value` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L146)
  - `max_position_embeddings` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L147)
  - `model_type` — [`L81`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L81)
  - `num_attention_heads` — [`L153`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L153)
  - `num_experts` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L166)
  - `num_experts_per_tok` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L165)
  - `num_hidden_layers` — [`L152`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L152)
  - `num_key_value_heads` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L159)
  - `output_multiplier_scale` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L149)
  - `output_router_logits` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L167)
  - `resid_pdrop` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L162)
  - `rms_norm_eps` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L160)
  - `rope_theta` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L164)
  - `router_aux_loss_coef` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L168)
  - `use_cache` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L163)
  - `vocab_size` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/grok_1_configuration.py#L144)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`__call__`](modeling_grok_1.md#Grok1SparseMoeBlock.__call__), [`Grok1ForCausalLM`](modeling_grok_1.md#Grok1ForCausalLM), [`embed_tokens`](modeling_grok_1.md#Grok1Model.embed_tokens), [`Grok1Model`](modeling_grok_1.md#Grok1Model), [`k_proj`](modeling_grok_1.md#Grok1Attention.k_proj), [`o_proj`](modeling_grok_1.md#Grok1Attention.o_proj), [`q_proj`](modeling_grok_1.md#Grok1Attention.q_proj), [`v_proj`](modeling_grok_1.md#Grok1Attention.v_proj), [`linear`](modeling_grok_1.md#Grok1BLockSparseMLP.linear), [`linear_1`](modeling_grok_1.md#Grok1BLockSparseMLP.linear_1), [`linear_v`](modeling_grok_1.md#Grok1BLockSparseMLP.linear_v), [`gate`](modeling_grok_1.md#Grok1SparseMoeBlock.gate), [`post_attn_norm`](modeling_grok_1.md#Grok1DecoderLayer.post_attn_norm), [`post_moe_norm`](modeling_grok_1.md#Grok1DecoderLayer.post_moe_norm), [`pre_attn_norm`](modeling_grok_1.md#Grok1DecoderLayer.pre_attn_norm), [`pre_moe_norm`](modeling_grok_1.md#Grok1DecoderLayer.pre_moe_norm), [`experts`](modeling_grok_1.md#Grok1SparseMoeBlock.experts), [`attention_performer`](modeling_grok_1.md#Grok1Attention.attention_performer), [`__init__`](modeling_grok_1.md#Grok1ForCausalLM.__init__), [`__init__`](modeling_grok_1.md#Grok1Attention.__init__), [`__init__`](modeling_grok_1.md#Grok1Model.__init__), [`hidden_size`](modeling_grok_1.md#Grok1Attention.hidden_size), [`resid_dropout`](modeling_grok_1.md#Grok1Attention.resid_dropout), [`__init__`](modeling_grok_1.md#Grok1BLockSparseMLP.__init__), [`__init__`](modeling_grok_1.md#Grok1DecoderLayer.__init__), [`__init__`](modeling_grok_1.md#Grok1SparseMoeBlock.__init__), [`_config_class`](modeling_grok_1.md#Grok1ForCausalLM._config_class)

