---
title: 'Module: easydel/modules/falcon/falcon_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/falcon/falcon_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.falcon.falcon_configuration`/FalconConfig#
symbols:
  FalconConfig: ''
  FalconConfig.hidden_size: hidden_size.
  FalconConfig.layer_types: layer_types.
  FalconConfig.layer_norm_epsilon: layer_norm_epsilon.
  FalconConfig.__init__: __init__().
  FalconConfig.num_ln_in_parallel_attn: num_ln_in_parallel_attn.
  FalconConfig.new_decoder_architecture: new_decoder_architecture.
  FalconConfig.head_dim: head_dim.
  FalconConfig.parallel_attn: parallel_attn.
  FalconConfig.num_attention_heads: num_attention_heads.
  FalconConfig.bias: bias.
  FalconConfig.rotary: rotary().
  FalconConfig.num_key_value_heads: num_key_value_heads().
  FalconConfig.alibi: alibi.
  FalconConfig.ff_factor: ff_factor.
  FalconConfig.vocab_size: vocab_size.
  FalconConfig.num_hidden_layers: num_hidden_layers.
  FalconConfig.hidden_dropout: hidden_dropout.
  FalconConfig.attention_dropout: attention_dropout.
  FalconConfig.multi_query: multi_query.
  FalconConfig.gradient_checkpointing: gradient_checkpointing.
  FalconConfig.num_kv_heads: num_kv_heads.
  FalconConfig.model_type: model_type.
  FalconConfig.initializer_range: initializer_range.
  FalconConfig.rope_theta: rope_theta.
  FalconConfig.rope_scaling: rope_scaling.
  FalconConfig.max_position_embeddings: max_position_embeddings.
  FalconConfig.use_cache: use_cache.
  FalconConfig.bos_token_id: bos_token_id.
  FalconConfig.activation: activation.
  FalconConfig.eos_token_id: eos_token_id.
  FalconConfig.bits: bits.
  FalconConfig.from_pt: from_pt.
  FalconConfig.ffn_hidden_size: ffn_hidden_size.
  FalconConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/falcon/falcon_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py)

## Classes
### `FalconConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/falcon/falcon_configuration.py:24`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L24)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class FalconConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L186`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L186) — Returns partition rules for model sharding.
  - `num_key_value_heads(self)` — [`L182`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L182) — Alias for num_kv_heads to match UnifiedAttention expectations.
  - `rotary(self)` — [`L178`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L178)
  - `activation` — [`L152`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L152)
  - `alibi` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L155)
  - `attention_dropout` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L150)
  - `bias` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L156)
  - `bits` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L163)
  - `bos_token_id` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L151)
  - `eos_token_id` — [`L153`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L153)
  - `ff_factor` — [`L171`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L171)
  - `ffn_hidden_size` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L168)
  - `from_pt` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L164)
  - `gradient_checkpointing` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L157)
  - `head_dim` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L165)
  - `hidden_dropout` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L149)
  - `hidden_size` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L139)
  - `initializer_range` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L144)
  - `layer_norm_epsilon` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L143)
  - `layer_types` — [`L172`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L172)
  - `max_position_embeddings` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L147)
  - `model_type` — [`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L104)
  - `multi_query` — [`L154`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L154)
  - `new_decoder_architecture` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L162)
  - `num_attention_heads` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L142)
  - `num_hidden_layers` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L140)
  - `num_kv_heads` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L161)
  - `num_ln_in_parallel_attn` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L141)
  - `parallel_attn` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L158)
  - `rope_scaling` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L146)
  - `rope_theta` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L145)
  - `use_cache` — [`L148`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L148)
  - `vocab_size` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L137)
- protocol/private: `__init__`[`L106`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/falcon_configuration.py#L106)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`__call__`](modeling_falcon.md#FalconBlock.__call__), [`input_layernorm`](modeling_falcon.md#FalconBlock.input_layernorm), [`word_embeddings`](modeling_falcon.md#FalconModel.word_embeddings), [`ln_mlp`](modeling_falcon.md#FalconBlock.ln_mlp), [`_create_fused_qkv_proj`](modeling_falcon.md#FalconAttention._create_fused_qkv_proj), [`FalconForCausalLM`](modeling_falcon.md#FalconForCausalLM), [`FalconModel`](modeling_falcon.md#FalconModel), [`ln_attn`](modeling_falcon.md#FalconBlock.ln_attn), [`post_attention_layernorm`](modeling_falcon.md#FalconBlock.post_attention_layernorm), [`_create_o_proj`](modeling_falcon.md#FalconAttention._create_o_proj), [`__init__`](modeling_falcon.md#FalconAttention.__init__), [`dense_4h_to_h`](modeling_falcon.md#FalconMlp.dense_4h_to_h), [`dense_h_to_4h`](modeling_falcon.md#FalconMlp.dense_h_to_4h), [`ln_f`](modeling_falcon.md#FalconModel.ln_f), [`__init__`](modeling_falcon.md#FalconForCausalLM.__init__), [`rngs`](modeling_falcon.md#FalconBlock.rngs), [`rngs`](modeling_falcon.md#FalconMlp.rngs), [`dropout`](modeling_falcon.md#FalconBlock.dropout), [`dropout_mlp`](modeling_falcon.md#FalconBlock.dropout_mlp), [`__init__`](modeling_falcon.md#FalconModel.__init__), [`__init__`](modeling_falcon.md#FalconBlock.__init__), [`__init__`](modeling_falcon.md#FalconMlp.__init__), [`_config_class`](modeling_falcon.md#FalconForCausalLM._config_class)

