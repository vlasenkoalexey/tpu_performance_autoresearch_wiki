---
title: 'Module: easydel/modules/mixtral/mixtral_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/mixtral/mixtral_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.mixtral.mixtral_configuration`/MixtralConfig#
symbols:
  MixtralConfig: ''
  MixtralConfig.get_mask_details: get_mask_details().
  MixtralConfig.head_dim: head_dim.
  MixtralConfig.hidden_size: hidden_size.
  MixtralConfig.__init__: __init__().
  MixtralConfig.num_local_experts: num_local_experts.
  MixtralConfig.layer_types: layer_types.
  MixtralConfig.intermediate_size: intermediate_size.
  MixtralConfig.num_hidden_layers: num_hidden_layers.
  MixtralConfig.sliding_window: sliding_window.
  MixtralConfig.rms_norm_eps: rms_norm_eps.
  MixtralConfig.granted_freq_max_position_embedding: granted_freq_max_position_embedding().
  MixtralConfig.granted_mask_max_position_embedding: granted_mask_max_position_embedding().
  MixtralConfig.max_position_embeddings: max_position_embeddings.
  MixtralConfig.vocab_size: vocab_size.
  MixtralConfig.num_experts_per_tok: num_experts_per_tok.
  MixtralConfig.hidden_act: hidden_act.
  MixtralConfig.gradient_checkpointing: gradient_checkpointing.
  MixtralConfig.model_type: model_type.
  MixtralConfig.num_attention_heads: num_attention_heads.
  MixtralConfig.bits: bits.
  MixtralConfig.attention_dropout: attention_dropout.
  MixtralConfig.output_router_logits: output_router_logits.
  MixtralConfig.router_aux_loss_coef: router_aux_loss_coef.
  MixtralConfig.attention_bias: attention_bias.
  MixtralConfig.rope_scaling: rope_scaling.
  MixtralConfig.num_key_value_heads: num_key_value_heads.
  MixtralConfig.initialization_of_moe: initialization_of_moe.
  MixtralConfig.initializer_range: initializer_range.
  MixtralConfig.use_cache: use_cache.
  MixtralConfig.rope_theta: rope_theta.
  MixtralConfig.number_rep_kv: number_rep_kv.
  MixtralConfig.use_scan_mlp: use_scan_mlp.
  MixtralConfig.scan_mlp_chunk_size: scan_mlp_chunk_size.
  MixtralConfig.router_jitter_noise: router_jitter_noise.
  MixtralConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/mixtral/mixtral_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py)

## Classes
### `MixtralConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/mixtral/mixtral_configuration.py:25`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L25)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class MixtralConfig(EasyDeLBaseConfig):`
- members:
  - `get_mask_details(self)` — [`L240`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L240) — Retrieve attention mask details for each layer in the model.
  - `get_partition_rules(self, *args, **kwargs)` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L203) — Returns partition rules for model sharding.
  - `granted_freq_max_position_embedding(self)` — [`L217`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L217) — Returns the maximum position embedding size specifically for frequency-based position embeddings.
  - `granted_mask_max_position_embedding(self)` — [`L229`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L229) — Returns the maximum position embedding size specifically for mask-based position embeddings.
  - `attention_bias` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L167)
  - `attention_dropout` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L162)
  - `bits` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L161)
  - `gradient_checkpointing` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L181)
  - `head_dim` — [`L186`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L186)
  - `hidden_act` — [`L174`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L174)
  - `hidden_size` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L156)
  - `initialization_of_moe` — [`L175`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L175)
  - `initializer_range` — [`L176`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L176)
  - `intermediate_size` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L157)
  - `layer_types` — [`L185`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L185)
  - `max_position_embeddings` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L155)
  - `model_type` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L115)
  - `num_attention_heads` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L159)
  - `num_experts_per_tok` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L164)
  - `num_hidden_layers` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L158)
  - `num_key_value_heads` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L173)
  - `num_local_experts` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L163)
  - `number_rep_kv` — [`L180`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L180)
  - `output_router_logits` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L165)
  - `rms_norm_eps` — [`L177`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L177)
  - `rope_scaling` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L169)
  - `rope_theta` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L179)
  - `router_aux_loss_coef` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L166)
  - `router_jitter_noise` — [`L184`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L184)
  - `scan_mlp_chunk_size` — [`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L183)
  - `sliding_window` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L160)
  - `use_cache` — [`L178`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L178)
  - `use_scan_mlp` — [`L182`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L182)
  - `vocab_size` — [`L154`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L154)
- protocol/private: `__init__`[`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/mixtral_configuration.py#L117)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`from_hf`](../../infra/utils.md#AttnMaskType.from_hf)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`granted_freq_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_freq_max_position_embedding), [`granted_mask_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_mask_max_position_embedding), [`__init__`](modeling_mixtral.md#MixtralSparseMoeBlock.__init__), [`embed_tokens`](modeling_mixtral.md#MixtralModel.embed_tokens), [`MixtralModel`](modeling_mixtral.md#MixtralModel), [`MixtralForCausalLM`](modeling_mixtral.md#MixtralForCausalLM), [`MixtralForSequenceClassification`](modeling_mixtral.md#MixtralForSequenceClassification), [`w1`](modeling_mixtral.md#MixtralMoEMlp.w1), [`w2`](modeling_mixtral.md#MixtralMoEMlp.w2), [`w3`](modeling_mixtral.md#MixtralMoEMlp.w3), [`gate`](modeling_mixtral.md#MixtralSparseMoeBlock.gate), [`input_layernorm`](modeling_mixtral.md#MixtralDecoderLayer.input_layernorm), [`norm`](modeling_mixtral.md#MixtralModel.norm), [`post_attention_layernorm`](modeling_mixtral.md#MixtralDecoderLayer.post_attention_layernorm), [`__init__`](modeling_mixtral.md#MixtralAttention.__init__), [`__init__`](modeling_mixtral.md#MixtralForCausalLM.__init__), [`__init__`](modeling_mixtral.md#MixtralForSequenceClassification.__init__), [`_create_rotary`](modeling_mixtral.md#MixtralAttention._create_rotary), [`act_fn`](modeling_mixtral.md#MixtralMoEMlp.act_fn), [`__init__`](modeling_mixtral.md#MixtralModel.__init__), [`layers`](modeling_mixtral.md#MixtralModel.layers), [`__init__`](modeling_mixtral.md#MixtralDecoderLayer.__init__), [`__init__`](modeling_mixtral.md#MixtralMoEMlp.__init__), [`_config_class`](modeling_mixtral.md#MixtralForCausalLM._config_class), [`_config_class`](modeling_mixtral.md#MixtralForSequenceClassification._config_class)

