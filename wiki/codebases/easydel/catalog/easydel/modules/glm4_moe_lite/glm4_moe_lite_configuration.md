---
title: 'Module: easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.glm4_moe_lite.glm4_moe_lite_configuration`/
symbols:
  Glm4MoeLiteConfig: Glm4MoeLiteConfig#
  Glm4MoeLiteConfig.hidden_size: Glm4MoeLiteConfig#hidden_size.
  Glm4MoeLiteConfig.mlp_layer_types: Glm4MoeLiteConfig#mlp_layer_types.
  Glm4MoeLiteConfig.initializer_range: Glm4MoeLiteConfig#initializer_range.
  Glm4MoeLiteConfig.n_routed_experts: Glm4MoeLiteConfig#n_routed_experts.
  Glm4MoeLiteConfig.q_lora_rank: Glm4MoeLiteConfig#q_lora_rank.
  Glm4MoeLiteConfig.rms_norm_eps: Glm4MoeLiteConfig#rms_norm_eps.
  Glm4MoeLiteConfig.moe_intermediate_size: Glm4MoeLiteConfig#moe_intermediate_size.
  Glm4MoeLiteConfig.num_hidden_layers: Glm4MoeLiteConfig#num_hidden_layers.
  Glm4MoeLiteConfig.num_attention_heads: Glm4MoeLiteConfig#num_attention_heads.
  Glm4MoeLiteConfig.kv_lora_rank: Glm4MoeLiteConfig#kv_lora_rank.
  Glm4MoeLiteConfig.qk_rope_head_dim: Glm4MoeLiteConfig#qk_rope_head_dim.
  Glm4MoeLiteConfig.qk_nope_head_dim: Glm4MoeLiteConfig#qk_nope_head_dim.
  Glm4MoeLiteConfig.attention_bias: Glm4MoeLiteConfig#attention_bias.
  Glm4MoeLiteConfig.rope_scaling: Glm4MoeLiteConfig#rope_scaling.
  Glm4MoeLiteConfig.n_shared_experts: Glm4MoeLiteConfig#n_shared_experts.
  Glm4MoeLiteConfig.v_head_dim: Glm4MoeLiteConfig#v_head_dim.
  Glm4MoeLiteConfig.n_group: Glm4MoeLiteConfig#n_group.
  Glm4MoeLiteConfig.num_experts_per_tok: Glm4MoeLiteConfig#num_experts_per_tok.
  Glm4MoeLiteConfig.hidden_act: Glm4MoeLiteConfig#hidden_act.
  _rope_scaling_from_rope_parameters: _rope_scaling_from_rope_parameters().
  Glm4MoeLiteConfig.vocab_size: Glm4MoeLiteConfig#vocab_size.
  Glm4MoeLiteConfig.intermediate_size: Glm4MoeLiteConfig#intermediate_size.
  Glm4MoeLiteConfig.routed_scaling_factor: Glm4MoeLiteConfig#routed_scaling_factor.
  Glm4MoeLiteConfig.topk_group: Glm4MoeLiteConfig#topk_group.
  Glm4MoeLiteConfig.norm_topk_prob: Glm4MoeLiteConfig#norm_topk_prob.
  Glm4MoeLiteConfig.rope_interleave: Glm4MoeLiteConfig#rope_interleave.
  Glm4MoeLiteConfig.model_type: Glm4MoeLiteConfig#model_type.
  Glm4MoeLiteConfig.attribute_map: Glm4MoeLiteConfig#attribute_map.
  Glm4MoeLiteConfig.__init__: Glm4MoeLiteConfig#__init__().
  Glm4MoeLiteConfig.max_position_embeddings: Glm4MoeLiteConfig#max_position_embeddings.
  Glm4MoeLiteConfig.num_key_value_heads: Glm4MoeLiteConfig#num_key_value_heads.
  Glm4MoeLiteConfig.qk_head_dim: Glm4MoeLiteConfig#qk_head_dim.
  Glm4MoeLiteConfig.head_dim: Glm4MoeLiteConfig#head_dim.
  Glm4MoeLiteConfig.pretraining_tp: Glm4MoeLiteConfig#pretraining_tp.
  Glm4MoeLiteConfig.use_cache: Glm4MoeLiteConfig#use_cache.
  Glm4MoeLiteConfig.attention_dropout: Glm4MoeLiteConfig#attention_dropout.
  Glm4MoeLiteConfig.rope_theta: Glm4MoeLiteConfig#rope_theta.
  Glm4MoeLiteConfig.get_partition_rules: Glm4MoeLiteConfig#get_partition_rules().
  __all__: __all__.
---
# Module: [`easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py)

## Classes
### `Glm4MoeLiteConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py:60`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L60)
- doc: Configuration class for GLM-4-MoE-Lite models.
- signature: `class Glm4MoeLiteConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L241`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L241) — Returns partition rules for model sharding.
  - `attention_bias` — [`L213`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L213)
  - `attention_dropout` — [`L214`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L214)
  - `attribute_map` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L143)
  - `head_dim` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L202)
  - `hidden_act` — [`L208`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L208)
  - `hidden_size` — [`L187`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L187)
  - `initializer_range` — [`L209`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L209)
  - `intermediate_size` — [`L188`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L188)
  - `kv_lora_rank` — [`L196`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L196)
  - `max_position_embeddings` — [`L186`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L186)
  - `mlp_layer_types` — [`L221`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L221)
  - `model_type` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L142)
  - `moe_intermediate_size` — [`L189`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L189)
  - `n_group` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L203)
  - `n_routed_experts` — [`L194`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L194)
  - `n_shared_experts` — [`L193`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L193)
  - `norm_topk_prob` — [`L206`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L206)
  - `num_attention_heads` — [`L191`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L191)
  - `num_experts_per_tok` — [`L205`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L205)
  - `num_hidden_layers` — [`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L190)
  - `num_key_value_heads` — [`L192`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L192)
  - `pretraining_tp` — [`L211`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L211)
  - `q_lora_rank` — [`L197`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L197)
  - `qk_head_dim` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L201)
  - `qk_nope_head_dim` — [`L200`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L200)
  - `qk_rope_head_dim` — [`L198`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L198)
  - `rms_norm_eps` — [`L210`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L210)
  - `rope_interleave` — [`L207`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L207)
  - `rope_scaling` — [`L215`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L215)
  - `rope_theta` — [`L219`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L219)
  - `routed_scaling_factor` — [`L195`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L195)
  - `topk_group` — [`L204`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L204)
  - `use_cache` — [`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L212)
  - `v_head_dim` — [`L199`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L199)
  - `vocab_size` — [`L185`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L185)
- protocol/private: `__init__`[`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L145)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_rope_scaling_from_rope_parameters`](glm4_moe_lite_configuration.md#_rope_scaling_from_rope_parameters)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`forward_mla`](modeling_glm4_moe_lite.md#Glm4MoeLiteAttention.forward_mla), [`define_network`](modeling_glm4_moe_lite.md#Glm4MoeLiteAttention.define_network), [`shared_experts`](modeling_glm4_moe_lite.md#Glm4MoeLiteMoE.shared_experts), [`embed_tokens`](modeling_glm4_moe_lite.md#Glm4MoeLiteModel.embed_tokens), [`__init__`](modeling_glm4_moe_lite.md#Glm4MoeLiteMoE.__init__), [`__init__`](modeling_glm4_moe_lite.md#Glm4MoeLiteModel.__init__), [`qk_nope_head_dim`](modeling_glm4_moe_lite.md#Glm4MoeLiteAttention.qk_nope_head_dim), [`Glm4MoeLiteForCausalLM`](modeling_glm4_moe_lite.md#Glm4MoeLiteForCausalLM), [`down_proj`](modeling_glm4_moe_lite.md#Glm4MoeLiteMLPStack.down_proj), [`gate_proj`](modeling_glm4_moe_lite.md#Glm4MoeLiteMLPStack.gate_proj), [`up_proj`](modeling_glm4_moe_lite.md#Glm4MoeLiteMLPStack.up_proj), [`Glm4MoeLiteModel`](modeling_glm4_moe_lite.md#Glm4MoeLiteModel), [`intermediate_size`](modeling_glm4_moe_lite.md#Glm4MoeLiteMLP.intermediate_size), [`norm`](modeling_glm4_moe_lite.md#Glm4MoeLiteModel.norm), [`q_head_dim`](modeling_glm4_moe_lite.md#Glm4MoeLiteAttention.q_head_dim), [`self_attn`](modeling_glm4_moe_lite.md#Glm4MoeLiteDecoderLayer.self_attn), [`kv_lora_rank`](modeling_glm4_moe_lite.md#Glm4MoeLiteAttention.kv_lora_rank), [`v_head_dim`](modeling_glm4_moe_lite.md#Glm4MoeLiteAttention.v_head_dim), [`input_layernorm`](modeling_glm4_moe_lite.md#Glm4MoeLiteDecoderLayer.input_layernorm), [`kernel`](modeling_glm4_moe_lite.md#Glm4MoeLiteTopKRouter.kernel), [`post_attention_layernorm`](modeling_glm4_moe_lite.md#Glm4MoeLiteDecoderLayer.post_attention_layernorm), [`__call__`](modeling_glm4_moe_lite.md#Glm4MoeLiteTopKRouter.__call__), [`__init__`](modeling_glm4_moe_lite.md#Glm4MoeLiteForCausalLM.__init__), [`act_fn`](modeling_glm4_moe_lite.md#Glm4MoeLiteMLPStack.act_fn), [`layers`](modeling_glm4_moe_lite.md#Glm4MoeLiteModel.layers), [`act_fn`](modeling_glm4_moe_lite.md#Glm4MoeLiteMLP.act_fn), [`group_topk_k`](modeling_glm4_moe_lite.md#Glm4MoeLiteMoE.group_topk_k), [`hidden_size`](modeling_glm4_moe_lite.md#Glm4MoeLiteMLP.hidden_size), [`hidden_size`](modeling_glm4_moe_lite.md#Glm4MoeLiteDecoderLayer.hidden_size), [`n_routed_experts`](modeling_glm4_moe_lite.md#Glm4MoeLiteTopKRouter.n_routed_experts), [`qk_rope_head_dim`](modeling_glm4_moe_lite.md#Glm4MoeLiteAttention.qk_rope_head_dim), [`n_group`](modeling_glm4_moe_lite.md#Glm4MoeLiteMoE.n_group), [`norm_topk_prob`](modeling_glm4_moe_lite.md#Glm4MoeLiteMoE.norm_topk_prob), [`routed_scaling_factor`](modeling_glm4_moe_lite.md#Glm4MoeLiteMoE.routed_scaling_factor), [`topk_group`](modeling_glm4_moe_lite.md#Glm4MoeLiteMoE.topk_group), [`__init__`](modeling_glm4_moe_lite.md#Glm4MoeLiteAttention.__init__), [`__init__`](modeling_glm4_moe_lite.md#Glm4MoeLiteDecoderLayer.__init__)  (+4 more)

## Functions
- `_rope_scaling_from_rope_parameters(rope_parameters: dict[str, typing.Any] | None, rope_scaling: dict[str, typing.Any] | None)` — [`L24`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L24)

## Module values
- `__all__` — [`L255`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/glm4_moe_lite_configuration.py#L255)

