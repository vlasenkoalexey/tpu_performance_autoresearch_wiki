---
title: 'Module: easydel/modules/minimax/minimax_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/minimax/minimax_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.minimax.minimax_configuration`/MiniMaxConfig#
symbols:
  MiniMaxConfig: ''
  MiniMaxConfig.get_mask_details: get_mask_details().
  MiniMaxConfig.hidden_size: hidden_size.
  MiniMaxConfig.mlp_beta_factor: mlp_beta_factor.
  MiniMaxConfig.layer_types: layer_types.
  MiniMaxConfig.num_hidden_layers: num_hidden_layers.
  MiniMaxConfig.initializer_range: initializer_range.
  MiniMaxConfig.num_local_experts: num_local_experts.
  MiniMaxConfig.rms_norm_eps: rms_norm_eps.
  MiniMaxConfig.intermediate_size: intermediate_size.
  MiniMaxConfig.num_attention_heads: num_attention_heads.
  MiniMaxConfig.sliding_window: sliding_window.
  MiniMaxConfig.hidden_act: hidden_act.
  MiniMaxConfig.vocab_size: vocab_size.
  MiniMaxConfig.max_position_embeddings: max_position_embeddings.
  MiniMaxConfig.num_experts_per_tok: num_experts_per_tok.
  MiniMaxConfig.router_aux_loss_coef: router_aux_loss_coef.
  MiniMaxConfig.router_jitter_noise: router_jitter_noise.
  MiniMaxConfig.block_size: block_size.
  MiniMaxConfig.full_attn_alpha_factor: full_attn_alpha_factor.
  MiniMaxConfig.full_attn_beta_factor: full_attn_beta_factor.
  MiniMaxConfig.linear_attn_alpha_factor: linear_attn_alpha_factor.
  MiniMaxConfig.linear_attn_beta_factor: linear_attn_beta_factor.
  MiniMaxConfig.mlp_alpha_factor: mlp_alpha_factor.
  MiniMaxConfig.model_type: model_type.
  MiniMaxConfig.keys_to_ignore_at_inference: keys_to_ignore_at_inference.
  MiniMaxConfig.__init__: __init__().
  MiniMaxConfig.num_key_value_heads: num_key_value_heads.
  MiniMaxConfig.use_cache: use_cache.
  MiniMaxConfig.rope_theta: rope_theta.
  MiniMaxConfig.attention_dropout: attention_dropout.
  MiniMaxConfig.head_dim: head_dim.
  MiniMaxConfig.output_router_logits: output_router_logits.
  MiniMaxConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/minimax/minimax_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py)

## Classes
### `MiniMaxConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/minimax/minimax_configuration.py:27`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L27)
- doc: This is the configuration class to store the configuration of a \[`MiniMaxModel`\]. It is used to instantiate an
- signature: `class MiniMaxConfig(EasyDeLBaseConfig):`
- members:
  - `get_mask_details(self)` — [`L204`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L204) — Retrieve attention mask details for each layer in the model.
  - `get_partition_rules(self, *args, **kwargs)` — [`L191`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L191) — Returns partition rules for model sharding.
  - `attention_dropout` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L158)
  - `block_size` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L167)
  - `full_attn_alpha_factor` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L168)
  - `full_attn_beta_factor` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L169)
  - `head_dim` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L159)
  - `hidden_act` — [`L153`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L153)
  - `hidden_size` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L142)
  - `initializer_range` — [`L154`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L154)
  - `intermediate_size` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L143)
  - `keys_to_ignore_at_inference` — [`L102`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L102)
  - `layer_types` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L166)
  - `linear_attn_alpha_factor` — [`L170`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L170)
  - `linear_attn_beta_factor` — [`L171`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L171)
  - `max_position_embeddings` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L141)
  - `mlp_alpha_factor` — [`L172`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L172)
  - `mlp_beta_factor` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L173)
  - `model_type` — [`L101`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L101)
  - `num_attention_heads` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L145)
  - `num_experts_per_tok` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L161)
  - `num_hidden_layers` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L144)
  - `num_key_value_heads` — [`L152`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L152)
  - `num_local_experts` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L162)
  - `output_router_logits` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L163)
  - `rms_norm_eps` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L155)
  - `rope_theta` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L157)
  - `router_aux_loss_coef` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L164)
  - `router_jitter_noise` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L165)
  - `sliding_window` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L146)
  - `use_cache` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L156)
  - `vocab_size` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L140)
- protocol/private: `__init__`[`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/minimax_configuration.py#L104)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`SLIDING`](../../infra/utils.md#AttnMaskType.SLIDING), [`FULL`](../../infra/utils.md#AttnMaskType.FULL)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`__init__`](modeling_minimax.md#MiniMaxSparseMoeBlock.__init__), [`embed_tokens`](modeling_minimax.md#MiniMaxModel.embed_tokens), [`attn_beta_factor`](modeling_minimax.md#MiniMaxDecoderLayer.attn_beta_factor), [`MiniMaxForCausalLM`](modeling_minimax.md#MiniMaxForCausalLM), [`w1`](modeling_minimax.md#MiniMaxExperts.w1), [`w2`](modeling_minimax.md#MiniMaxExperts.w2), [`w3`](modeling_minimax.md#MiniMaxExperts.w3), [`MiniMaxModel`](modeling_minimax.md#MiniMaxModel), [`out_proj`](modeling_minimax.md#MiniMaxLightningAttention.out_proj), [`output_gate`](modeling_minimax.md#MiniMaxLightningAttention.output_gate), [`qkv_proj`](modeling_minimax.md#MiniMaxLightningAttention.qkv_proj), [`head_dim`](modeling_minimax.md#MiniMaxLightningAttention.head_dim), [`num_attention_heads`](modeling_minimax.md#MiniMaxLightningAttention.num_attention_heads), [`gate`](modeling_minimax.md#MiniMaxSparseMoeBlock.gate), [`norm`](modeling_minimax.md#MiniMaxLightningAttention.norm), [`__init__`](modeling_minimax.md#MiniMaxForCausalLM.__init__), [`layer_type`](modeling_minimax.md#MiniMaxDecoderLayer.layer_type), [`block_size`](modeling_minimax.md#MiniMaxLightningAttention.block_size), [`input_layernorm`](modeling_minimax.md#MiniMaxDecoderLayer.input_layernorm), [`norm`](modeling_minimax.md#MiniMaxModel.norm), [`post_attention_layernorm`](modeling_minimax.md#MiniMaxDecoderLayer.post_attention_layernorm), [`act_fn`](modeling_minimax.md#MiniMaxExperts.act_fn), [`MiniMaxAttention`](modeling_minimax.md#MiniMaxAttention), [`act_fn`](modeling_minimax.md#MiniMaxLightningAttention.act_fn), [`jitter_noise`](modeling_minimax.md#MiniMaxSparseMoeBlock.jitter_noise), [`__init__`](modeling_minimax.md#MiniMaxAttention.__init__), [`__init__`](modeling_minimax.md#MiniMaxModel.__init__), [`attn_alpha_factor`](modeling_minimax.md#MiniMaxDecoderLayer.attn_alpha_factor), [`layers`](modeling_minimax.md#MiniMaxModel.layers), [`mlp_alpha_factor`](modeling_minimax.md#MiniMaxDecoderLayer.mlp_alpha_factor), [`mlp_beta_factor`](modeling_minimax.md#MiniMaxDecoderLayer.mlp_beta_factor), [`num_hidden_layers`](modeling_minimax.md#MiniMaxLightningAttention.num_hidden_layers), [`__init__`](modeling_minimax.md#MiniMaxDecoderLayer.__init__), [`__init__`](modeling_minimax.md#MiniMaxExperts.__init__), [`__init__`](modeling_minimax.md#MiniMaxLightningAttention.__init__), [`_config_class`](modeling_minimax.md#MiniMaxForCausalLM._config_class)  (+2 more)

