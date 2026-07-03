---
title: 'Module: easydel/modules/mistral/mistral_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/mistral/mistral_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.mistral.mistral_configuration`/MistralConfig#
symbols:
  MistralConfig: ''
  MistralConfig.get_mask_details: get_mask_details().
  MistralConfig.layer_types: layer_types.
  MistralConfig.hidden_size: hidden_size.
  MistralConfig.__init__: __init__().
  MistralConfig.intermediate_size: intermediate_size.
  MistralConfig.sliding_window: sliding_window.
  MistralConfig.initializer_range: initializer_range.
  MistralConfig.rms_norm_eps: rms_norm_eps.
  MistralConfig.num_hidden_layers: num_hidden_layers.
  MistralConfig.vocab_size: vocab_size.
  MistralConfig.hidden_act: hidden_act.
  MistralConfig.gradient_checkpointing: gradient_checkpointing.
  MistralConfig.use_scan_mlp: use_scan_mlp.
  MistralConfig.scan_mlp_chunk_size: scan_mlp_chunk_size.
  MistralConfig.model_type: model_type.
  MistralConfig.max_position_embeddings: max_position_embeddings.
  MistralConfig.head_dim: head_dim.
  MistralConfig.num_attention_heads: num_attention_heads.
  MistralConfig.bits: bits.
  MistralConfig.num_key_value_heads: num_key_value_heads.
  MistralConfig.use_cache: use_cache.
  MistralConfig.rope_theta: rope_theta.
  MistralConfig.rope_scaling: rope_scaling.
  MistralConfig.number_rep_kv: number_rep_kv.
  MistralConfig.attention_bias: attention_bias.
  MistralConfig.attention_dropout: attention_dropout.
  MistralConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/mistral/mistral_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py)

## Classes
### `MistralConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/mistral/mistral_configuration.py:25`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L25)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class MistralConfig(EasyDeLBaseConfig):`
- members:
  - `get_mask_details(self)` — [`L178`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L178) — Retrieve attention mask details for each layer in the model.
  - `get_partition_rules(self, *args, **kwargs)` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L165) — Returns partition rules for model sharding.
  - `attention_bias` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L146)
  - `attention_dropout` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L147)
  - `bits` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L130)
  - `gradient_checkpointing` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L143)
  - `head_dim` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L127)
  - `hidden_act` — [`L136`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L136)
  - `hidden_size` — [`L124`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L124)
  - `initializer_range` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L137)
  - `intermediate_size` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L125)
  - `layer_types` — [`L148`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L148)
  - `max_position_embeddings` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L123)
  - `model_type` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L89)
  - `num_attention_heads` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L128)
  - `num_hidden_layers` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L126)
  - `num_key_value_heads` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L135)
  - `number_rep_kv` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L142)
  - `rms_norm_eps` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L138)
  - `rope_scaling` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L141)
  - `rope_theta` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L140)
  - `scan_mlp_chunk_size` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L145)
  - `sliding_window` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L129)
  - `use_cache` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L139)
  - `use_scan_mlp` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L144)
  - `vocab_size` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L122)
- protocol/private: `__init__`[`L91`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/mistral_configuration.py#L91)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`from_hf`](../../infra/utils.md#AttnMaskType.from_hf)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`__call__`](modeling_mistral.md#MistralDecoderLayer.__call__), [`embed_tokens`](modeling_mistral.md#MistralModel.embed_tokens), [`MistralModel`](modeling_mistral.md#MistralModel), [`MistralForCausalLM`](modeling_mistral.md#MistralForCausalLM), [`MistralForSequenceClassification`](modeling_mistral.md#MistralForSequenceClassification), [`precision`](modeling_mistral.md#MistralMLP.precision), [`act_fn`](modeling_mistral.md#MistralMLP.act_fn), [`input_layernorm`](modeling_mistral.md#MistralDecoderLayer.input_layernorm), [`norm`](modeling_mistral.md#MistralModel.norm), [`post_attention_layernorm`](modeling_mistral.md#MistralDecoderLayer.post_attention_layernorm), [`__init__`](modeling_mistral.md#MistralAttention.__init__), [`__init__`](modeling_mistral.md#MistralForCausalLM.__init__), [`__init__`](modeling_mistral.md#MistralForSequenceClassification.__init__), [`_create_rotary`](modeling_mistral.md#MistralAttention._create_rotary), [`down_proj`](modeling_mistral.md#MistralMLP.down_proj), [`gate_proj`](modeling_mistral.md#MistralMLP.gate_proj), [`up_proj`](modeling_mistral.md#MistralMLP.up_proj), [`__init__`](modeling_mistral.md#MistralModel.__init__), [`__init__`](modeling_mistral.md#MistralDecoderLayer.__init__), [`__init__`](modeling_mistral.md#MistralMLP.__init__), [`_config_class`](modeling_mistral.md#MistralForCausalLM._config_class), [`_config_class`](modeling_mistral.md#MistralForSequenceClassification._config_class)

