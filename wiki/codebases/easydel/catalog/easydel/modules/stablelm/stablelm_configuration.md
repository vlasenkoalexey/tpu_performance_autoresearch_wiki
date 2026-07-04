---
title: 'Module: easydel/modules/stablelm/stablelm_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/stablelm/stablelm_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.stablelm.stablelm_configuration`/StableLmConfig#
symbols:
  StableLmConfig: ''
  StableLmConfig.layer_types: layer_types.
  StableLmConfig.hidden_size: hidden_size.
  StableLmConfig.__init__: __init__().
  StableLmConfig.intermediate_size: intermediate_size.
  StableLmConfig.layer_norm_eps: layer_norm_eps.
  StableLmConfig.initializer_range: initializer_range.
  StableLmConfig.qk_layernorm: qk_layernorm.
  StableLmConfig.partial_rotary_factor: partial_rotary_factor.
  StableLmConfig.vocab_size: vocab_size.
  StableLmConfig.num_hidden_layers: num_hidden_layers.
  StableLmConfig.hidden_act: hidden_act.
  StableLmConfig.num_attention_heads: num_attention_heads.
  StableLmConfig.use_parallel_residual: use_parallel_residual.
  StableLmConfig.hidden_dropout: hidden_dropout.
  StableLmConfig.gradient_checkpointing: gradient_checkpointing.
  StableLmConfig.model_type: model_type.
  StableLmConfig.num_key_value_heads: num_key_value_heads.
  StableLmConfig.use_qkv_bias: use_qkv_bias.
  StableLmConfig.attention_dropout: attention_dropout.
  StableLmConfig.max_position_embeddings: max_position_embeddings.
  StableLmConfig.use_cache: use_cache.
  StableLmConfig.rope_theta: rope_theta.
  StableLmConfig.rope_scaling: rope_scaling.
  StableLmConfig.bits: bits.
  StableLmConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/stablelm/stablelm_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py)

## Classes
### `StableLmConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/stablelm/stablelm_configuration.py:24`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L24)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class StableLmConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size=50304, intermediate_size=6912, hidden_size=2560, num_hidden_layers=32, num_attention_heads=32, num_key_value_heads: int | None = 32, hidden_act="silu", max_position_embeddings=4096, initializer_range=0.02, layer_norm_eps=0.00001, use_cache=True, tie_word_embeddings=False, rope_theta=10000, rope_scaling=None, use_qkv_bias=False, qk_layernorm=False, use_parallel_residual=False, hidden_dropout=0, attention_dropout=0, partial_rotary_factor=0.25, bos_token_id=0, eos_token_id=0, bits: int | None = None, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, layer_types: list[str] | None = None, **kwargs)` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L83) — Initializes the StableLmConfig object.
  - `get_partition_rules(self, *args, **kwargs)` — [`L177`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L177) — Returns partition rules for model sharding.
  - `attention_dropout` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L155)
  - `bits` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L164)
  - `gradient_checkpointing` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L165)
  - `hidden_act` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L156)
  - `hidden_dropout` — [`L154`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L154)
  - `hidden_size` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L143)
  - `initializer_range` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L158)
  - `intermediate_size` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L144)
  - `layer_norm_eps` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L159)
  - `layer_types` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L166)
  - `max_position_embeddings` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L157)
  - `model_type` — [`L81`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L81)
  - `num_attention_heads` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L146)
  - `num_hidden_layers` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L145)
  - `num_key_value_heads` — [`L152`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L152)
  - `partial_rotary_factor` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L163)
  - `qk_layernorm` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L150)
  - `rope_scaling` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L162)
  - `rope_theta` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L161)
  - `use_cache` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L160)
  - `use_parallel_residual` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L151)
  - `use_qkv_bias` — [`L153`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L153)
  - `vocab_size` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/stablelm_configuration.py#L142)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`embed_tokens`](modeling_stablelm.md#StableLmModel.embed_tokens), [`StableLmForCausalLM`](modeling_stablelm.md#StableLmForCausalLM), [`StableLmModel`](modeling_stablelm.md#StableLmModel), [`head_dim`](modeling_stablelm.md#StableLmAttention.head_dim), [`input_layernorm`](modeling_stablelm.md#StableLmDecoderLayer.input_layernorm), [`rotary_emb_dim`](modeling_stablelm.md#StableLmAttention.rotary_emb_dim), [`post_attention_layernorm`](modeling_stablelm.md#StableLmDecoderLayer.post_attention_layernorm), [`norm`](modeling_stablelm.md#StableLmModel.norm), [`__init__`](modeling_stablelm.md#StableLmForCausalLM.__init__), [`precision`](modeling_stablelm.md#StableLmMLP.precision), [`dropout`](modeling_stablelm.md#StableLmDecoderLayer.dropout), [`use_parallel_residual`](modeling_stablelm.md#StableLmDecoderLayer.use_parallel_residual), [`act_fn`](modeling_stablelm.md#StableLmMLP.act_fn), [`down_proj`](modeling_stablelm.md#StableLmMLP.down_proj), [`gate_proj`](modeling_stablelm.md#StableLmMLP.gate_proj), [`up_proj`](modeling_stablelm.md#StableLmMLP.up_proj), [`qk_layernorm`](modeling_stablelm.md#StableLmAttention.qk_layernorm), [`__init__`](modeling_stablelm.md#StableLmModel.__init__), [`layers`](modeling_stablelm.md#StableLmModel.layers), [`__init__`](modeling_stablelm.md#StableLmAttention.__init__), [`__init__`](modeling_stablelm.md#StableLmDecoderLayer.__init__), [`__init__`](modeling_stablelm.md#StableLmMLP.__init__), [`_config_class`](modeling_stablelm.md#StableLmForCausalLM._config_class), [`partial_rotary_factor`](modeling_stablelm.md#StableLmAttention.partial_rotary_factor), [`vocab_size`](modeling_stablelm.md#StableLmModel.vocab_size)

