---
title: 'Module: easydel/modules/arctic/arctic_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/arctic/arctic_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.arctic.arctic_configuration`/ArcticConfig#
symbols:
  ArcticConfig: ''
  ArcticConfig.get_mask_details: get_mask_details().
  ArcticConfig.layer_types: layer_types.
  ArcticConfig.hidden_size: hidden_size.
  ArcticConfig.num_local_experts: num_local_experts.
  ArcticConfig.__init__: __init__().
  ArcticConfig.num_hidden_layers: num_hidden_layers.
  ArcticConfig.sliding_window: sliding_window.
  ArcticConfig.rms_norm_eps: rms_norm_eps.
  ArcticConfig.intermediate_size: intermediate_size.
  ArcticConfig.hidden_act: hidden_act.
  ArcticConfig.num_experts_per_tok: num_experts_per_tok.
  ArcticConfig.moe_layer_frequency: moe_layer_frequency.
  ArcticConfig.parallel_attn_mlp_res: parallel_attn_mlp_res.
  ArcticConfig.gradient_checkpointing: gradient_checkpointing.
  ArcticConfig.model_type: model_type.
  ArcticConfig.vocab_size: vocab_size.
  ArcticConfig.max_position_embeddings: max_position_embeddings.
  ArcticConfig.num_attention_heads: num_attention_heads.
  ArcticConfig.num_key_value_heads: num_key_value_heads.
  ArcticConfig.head_dim: head_dim.
  ArcticConfig.initializer_range: initializer_range.
  ArcticConfig.use_cache: use_cache.
  ArcticConfig.rope_theta: rope_theta.
  ArcticConfig.attention_dropout: attention_dropout.
  ArcticConfig.router_aux_loss_coef: router_aux_loss_coef.
  ArcticConfig.moe_train_capacity_factor: moe_train_capacity_factor.
  ArcticConfig.moe_eval_capacity_factor: moe_eval_capacity_factor.
  ArcticConfig.enable_expert_tensor_parallelism: enable_expert_tensor_parallelism.
  ArcticConfig.moe_min_capacity: moe_min_capacity.
  ArcticConfig.moe_token_dropping: moe_token_dropping.
  ArcticConfig.quantization: quantization.
  ArcticConfig.use_scan_mlp: use_scan_mlp.
  ArcticConfig.scan_mlp_chunk_size: scan_mlp_chunk_size.
  ArcticConfig.bits: bits.
  ArcticConfig.rope_scaling: rope_scaling.
  ArcticConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/arctic/arctic_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py)

## Classes
### `ArcticConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/arctic/arctic_configuration.py:25`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L25)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class ArcticConfig(EasyDeLBaseConfig):`
- members:
  - `get_mask_details(self)` — [`L217`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L217) — Retrieve attention mask details for each layer in the model.
  - `get_partition_rules(self, *args, **kwargs)` — [`L204`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L204) — Returns partition rules for model sharding.
  - `attention_dropout` — [`L171`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L171)
  - `bits` — [`L188`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L188)
  - `enable_expert_tensor_parallelism` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L179)
  - `gradient_checkpointing` — [`L185`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L185)
  - `head_dim` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L165)
  - `hidden_act` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L166)
  - `hidden_size` — [`L154`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L154)
  - `initializer_range` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L167)
  - `intermediate_size` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L155)
  - `layer_types` — [`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L190)
  - `max_position_embeddings` — [`L153`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L153)
  - `model_type` — [`L110`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L110)
  - `moe_eval_capacity_factor` — [`L178`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L178)
  - `moe_layer_frequency` — [`L176`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L176)
  - `moe_min_capacity` — [`L180`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L180)
  - `moe_token_dropping` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L181)
  - `moe_train_capacity_factor` — [`L177`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L177)
  - `num_attention_heads` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L157)
  - `num_experts_per_tok` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L173)
  - `num_hidden_layers` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L156)
  - `num_key_value_heads` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L164)
  - `num_local_experts` — [`L174`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L174)
  - `parallel_attn_mlp_res` — [`L182`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L182)
  - `quantization` — [`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L183)
  - `rms_norm_eps` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L168)
  - `rope_scaling` — [`L189`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L189)
  - `rope_theta` — [`L170`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L170)
  - `router_aux_loss_coef` — [`L175`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L175)
  - `scan_mlp_chunk_size` — [`L187`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L187)
  - `sliding_window` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L158)
  - `use_cache` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L169)
  - `use_scan_mlp` — [`L186`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L186)
  - `vocab_size` — [`L152`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L152)
- protocol/private: `__init__`[`L112`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/arctic_configuration.py#L112)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`from_hf`](../../infra/utils.md#AttnMaskType.from_hf)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`__init__`](modeling_arctic.md#ArcticMoeBlock.__init__), [`ArcticModel`](modeling_arctic.md#ArcticModel), [`ArcticForCausalLM`](modeling_arctic.md#ArcticForCausalLM), [`embed_tokens`](modeling_arctic.md#ArcticModel.embed_tokens), [`w1`](modeling_arctic.md#ArcticMLPMoE.w1), [`w2`](modeling_arctic.md#ArcticMLPMoE.w2), [`w3`](modeling_arctic.md#ArcticMLPMoE.w3), [`ArcticForSequenceClassification`](modeling_arctic.md#ArcticForSequenceClassification), [`parallel_attn_mlp_res`](modeling_arctic.md#ArcticDecoderLayer.parallel_attn_mlp_res), [`ffn_dim`](modeling_arctic.md#ArcticMLP.ffn_dim), [`ffn_dim`](modeling_arctic.md#ArcticMLPMoE.ffn_dim), [`act_fn`](modeling_arctic.md#ArcticMLPMoE.act_fn), [`post_attention_layernorm`](modeling_arctic.md#ArcticDecoderLayer.post_attention_layernorm), [`act_fn`](modeling_arctic.md#ArcticMLP.act_fn), [`gate`](modeling_arctic.md#ArcticMoeBlock.gate), [`input_layernorm`](modeling_arctic.md#ArcticDecoderLayer.input_layernorm), [`residual_layernorm`](modeling_arctic.md#ArcticDecoderLayer.residual_layernorm), [`is_moe_layer`](modeling_arctic.md#ArcticMoeBlock.is_moe_layer), [`__init__`](modeling_arctic.md#ArcticAttention.__init__), [`__init__`](modeling_arctic.md#ArcticForCausalLM.__init__), [`__init__`](modeling_arctic.md#ArcticForSequenceClassification.__init__), [`_create_attention_performer`](modeling_arctic.md#ArcticAttention._create_attention_performer), [`_create_rotary`](modeling_arctic.md#ArcticAttention._create_rotary), [`hidden_dim`](modeling_arctic.md#ArcticMLP.hidden_dim), [`hidden_dim`](modeling_arctic.md#ArcticMLPMoE.hidden_dim), [`__init__`](modeling_arctic.md#ArcticModel.__init__), [`layers`](modeling_arctic.md#ArcticModel.layers), [`__init__`](modeling_arctic.md#ArcticDecoderLayer.__init__), [`__init__`](modeling_arctic.md#ArcticMLP.__init__), [`__init__`](modeling_arctic.md#ArcticMLPMoE.__init__), [`_config_class`](modeling_arctic.md#ArcticForCausalLM._config_class), [`_config_class`](modeling_arctic.md#ArcticForSequenceClassification._config_class), [`hidden_dim`](modeling_arctic.md#ArcticMoeBlock.hidden_dim), [`num_experts`](modeling_arctic.md#ArcticMoeBlock.num_experts), [`top_k`](modeling_arctic.md#ArcticMoeBlock.top_k)

