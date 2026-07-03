---
title: 'Module: easydel/modules/glm4_moe/glm4_moe_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/glm4_moe/glm4_moe_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.glm4_moe.glm4_moe_configuration`/
symbols:
  Glm4MoeConfig: Glm4MoeConfig#
  Glm4MoeConfig.hidden_size: Glm4MoeConfig#hidden_size.
  Glm4MoeConfig.layer_types: Glm4MoeConfig#layer_types.
  Glm4MoeConfig.n_routed_experts: Glm4MoeConfig#n_routed_experts.
  Glm4MoeConfig.rope_scaling: Glm4MoeConfig#rope_scaling.
  Glm4MoeConfig.moe_intermediate_size: Glm4MoeConfig#moe_intermediate_size.
  Glm4MoeConfig.initializer_range: Glm4MoeConfig#initializer_range.
  Glm4MoeConfig.n_group: Glm4MoeConfig#n_group.
  Glm4MoeConfig.attention_dropout: Glm4MoeConfig#attention_dropout.
  Glm4MoeConfig.hidden_act: Glm4MoeConfig#hidden_act.
  Glm4MoeConfig.rms_norm_eps: Glm4MoeConfig#rms_norm_eps.
  Glm4MoeConfig.num_experts_per_tok: Glm4MoeConfig#num_experts_per_tok.
  Glm4MoeConfig.topk_group: Glm4MoeConfig#topk_group.
  Glm4MoeConfig.routed_scaling_factor: Glm4MoeConfig#routed_scaling_factor.
  Glm4MoeConfig.norm_topk_prob: Glm4MoeConfig#norm_topk_prob.
  Glm4MoeConfig.vocab_size: Glm4MoeConfig#vocab_size.
  Glm4MoeConfig.intermediate_size: Glm4MoeConfig#intermediate_size.
  Glm4MoeConfig.num_hidden_layers: Glm4MoeConfig#num_hidden_layers.
  Glm4MoeConfig.n_shared_experts: Glm4MoeConfig#n_shared_experts.
  Glm4MoeConfig.first_k_dense_replace: Glm4MoeConfig#first_k_dense_replace.
  Glm4MoeConfig.use_qk_norm: Glm4MoeConfig#use_qk_norm.
  Glm4MoeConfig.model_type: Glm4MoeConfig#model_type.
  Glm4MoeConfig.__init__: Glm4MoeConfig#__init__().
  Glm4MoeConfig.max_position_embeddings: Glm4MoeConfig#max_position_embeddings.
  Glm4MoeConfig.num_attention_heads: Glm4MoeConfig#num_attention_heads.
  Glm4MoeConfig.partial_rotary_factor: Glm4MoeConfig#partial_rotary_factor.
  Glm4MoeConfig.num_key_value_heads: Glm4MoeConfig#num_key_value_heads.
  Glm4MoeConfig.use_cache: Glm4MoeConfig#use_cache.
  Glm4MoeConfig.rope_theta: Glm4MoeConfig#rope_theta.
  Glm4MoeConfig.attention_bias: Glm4MoeConfig#attention_bias.
  Glm4MoeConfig.head_dim: Glm4MoeConfig#head_dim.
  Glm4MoeConfig.get_partition_rules: Glm4MoeConfig#get_partition_rules().
  __all__: __all__.
---
# Module: [`easydel/modules/glm4_moe/glm4_moe_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py)

## Classes
### `Glm4MoeConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/glm4_moe/glm4_moe_configuration.py:23`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L23)
- doc: This is the configuration class to store the configuration of a \[`Glm4MoeModel`\]. It is used to instantiate a
- signature: `class Glm4MoeConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L217`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L217) — Returns partition rules for model sharding.
  - `attention_bias` — [`L194`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L194)
  - `attention_dropout` — [`L195`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L195)
  - `first_k_dense_replace` — [`L207`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L207)
  - `head_dim` — [`L210`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L210)
  - `hidden_act` — [`L188`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L188)
  - `hidden_size` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L181)
  - `initializer_range` — [`L189`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L189)
  - `intermediate_size` — [`L182`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L182)
  - `layer_types` — [`L211`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L211)
  - `max_position_embeddings` — [`L180`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L180)
  - `model_type` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L145)
  - `moe_intermediate_size` — [`L200`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L200)
  - `n_group` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L202)
  - `n_routed_experts` — [`L205`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L205)
  - `n_shared_experts` — [`L204`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L204)
  - `norm_topk_prob` — [`L208`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L208)
  - `num_attention_heads` — [`L184`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L184)
  - `num_experts_per_tok` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L201)
  - `num_hidden_layers` — [`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L183)
  - `num_key_value_heads` — [`L187`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L187)
  - `partial_rotary_factor` — [`L185`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L185)
  - `rms_norm_eps` — [`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L190)
  - `rope_scaling` — [`L193`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L193)
  - `rope_theta` — [`L192`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L192)
  - `routed_scaling_factor` — [`L206`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L206)
  - `topk_group` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L203)
  - `use_cache` — [`L191`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L191)
  - `use_qk_norm` — [`L209`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L209)
  - `vocab_size` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L179)
- protocol/private: `__init__`[`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L147)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`shared_experts`](modeling_glm4_moe.md#Glm4MoeMoE.shared_experts), [`__init__`](modeling_glm4_moe.md#Glm4MoeMoE.__init__), [`Glm4MoeModel`](modeling_glm4_moe.md#Glm4MoeModel), [`Glm4MoeForCausalLM`](modeling_glm4_moe.md#Glm4MoeForCausalLM), [`Glm4MoeForSequenceClassification`](modeling_glm4_moe.md#Glm4MoeForSequenceClassification), [`down_proj`](modeling_glm4_moe.md#Glm4MoeMLPStack.down_proj), [`gate_proj`](modeling_glm4_moe.md#Glm4MoeMLPStack.gate_proj), [`up_proj`](modeling_glm4_moe.md#Glm4MoeMLPStack.up_proj), [`kernel`](modeling_glm4_moe.md#Glm4MoeTopKRouter.kernel), [`intermediate_size`](modeling_glm4_moe.md#Glm4MoeMLP.intermediate_size), [`layer_idx`](modeling_glm4_moe.md#Glm4MoeDecoderLayer.layer_idx), [`act_fn`](modeling_glm4_moe.md#Glm4MoeMLP.act_fn), [`input_layernorm`](modeling_glm4_moe.md#Glm4MoeDecoderLayer.input_layernorm), [`post_attention_layernorm`](modeling_glm4_moe.md#Glm4MoeDecoderLayer.post_attention_layernorm), [`__call__`](modeling_glm4_moe.md#Glm4MoeTopKRouter.__call__), [`__init__`](modeling_glm4_moe.md#Glm4MoeForCausalLM.__init__), [`__init__`](modeling_glm4_moe.md#Glm4MoeForSequenceClassification.__init__), [`n_routed_experts`](modeling_glm4_moe.md#Glm4MoeTopKRouter.n_routed_experts), [`act_fn`](modeling_glm4_moe.md#Glm4MoeMLPStack.act_fn), [`n_group`](modeling_glm4_moe.md#Glm4MoeTopKRouter.n_group), [`down_proj`](modeling_glm4_moe.md#Glm4MoeMLP.down_proj), [`gate_proj`](modeling_glm4_moe.md#Glm4MoeMLP.gate_proj), [`group_topk_k`](modeling_glm4_moe.md#Glm4MoeMoE.group_topk_k), [`up_proj`](modeling_glm4_moe.md#Glm4MoeMLP.up_proj), [`__init__`](modeling_glm4_moe.md#Glm4MoeModel.__init__), [`layer_idx`](modeling_glm4_moe.md#Glm4MoeAttention.layer_idx), [`top_k`](modeling_glm4_moe.md#Glm4MoeTopKRouter.top_k), [`topk_group`](modeling_glm4_moe.md#Glm4MoeTopKRouter.topk_group), [`__init__`](modeling_glm4_moe.md#Glm4MoeAttention.__init__), [`__init__`](modeling_glm4_moe.md#Glm4MoeDecoderLayer.__init__), [`__init__`](modeling_glm4_moe.md#Glm4MoeMLP.__init__), [`__init__`](modeling_glm4_moe.md#Glm4MoeMLPStack.__init__), [`__init__`](modeling_glm4_moe.md#Glm4MoeTopKRouter.__init__), [`_config_class`](modeling_glm4_moe.md#Glm4MoeForCausalLM._config_class), [`_config_class`](modeling_glm4_moe.md#Glm4MoeForSequenceClassification._config_class), [`norm_topk_prob`](modeling_glm4_moe.md#Glm4MoeTopKRouter.norm_topk_prob), [`routed_scaling_factor`](modeling_glm4_moe.md#Glm4MoeTopKRouter.routed_scaling_factor)  (+1 more)

## Module values
- `__all__` — [`L231`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/glm4_moe_configuration.py#L231)

