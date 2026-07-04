---
title: 'Module: easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.glm_moe_dsa.glm_moe_dsa_configuration`/
symbols:
  GlmMoeDsaConfig: GlmMoeDsaConfig#
  GlmMoeDsaConfig.mlp_layer_types: GlmMoeDsaConfig#mlp_layer_types.
  GlmMoeDsaConfig.hidden_size: GlmMoeDsaConfig#hidden_size.
  GlmMoeDsaConfig.initializer_range: GlmMoeDsaConfig#initializer_range.
  GlmMoeDsaConfig.n_routed_experts: GlmMoeDsaConfig#n_routed_experts.
  GlmMoeDsaConfig.q_lora_rank: GlmMoeDsaConfig#q_lora_rank.
  GlmMoeDsaConfig.num_hidden_layers: GlmMoeDsaConfig#num_hidden_layers.
  GlmMoeDsaConfig.n_group: GlmMoeDsaConfig#n_group.
  GlmMoeDsaConfig.moe_intermediate_size: GlmMoeDsaConfig#moe_intermediate_size.
  GlmMoeDsaConfig.num_attention_heads: GlmMoeDsaConfig#num_attention_heads.
  GlmMoeDsaConfig.kv_lora_rank: GlmMoeDsaConfig#kv_lora_rank.
  GlmMoeDsaConfig.qk_rope_head_dim: GlmMoeDsaConfig#qk_rope_head_dim.
  GlmMoeDsaConfig.qk_nope_head_dim: GlmMoeDsaConfig#qk_nope_head_dim.
  GlmMoeDsaConfig.rms_norm_eps: GlmMoeDsaConfig#rms_norm_eps.
  GlmMoeDsaConfig.attention_bias: GlmMoeDsaConfig#attention_bias.
  GlmMoeDsaConfig.rope_scaling: GlmMoeDsaConfig#rope_scaling.
  GlmMoeDsaConfig.n_shared_experts: GlmMoeDsaConfig#n_shared_experts.
  GlmMoeDsaConfig.v_head_dim: GlmMoeDsaConfig#v_head_dim.
  GlmMoeDsaConfig.num_experts_per_tok: GlmMoeDsaConfig#num_experts_per_tok.
  GlmMoeDsaConfig.hidden_act: GlmMoeDsaConfig#hidden_act.
  GlmMoeDsaConfig.index_topk: GlmMoeDsaConfig#index_topk.
  GlmMoeDsaConfig.index_head_dim: GlmMoeDsaConfig#index_head_dim.
  GlmMoeDsaConfig.index_n_heads: GlmMoeDsaConfig#index_n_heads.
  _rope_scaling_from_rope_parameters: _rope_scaling_from_rope_parameters().
  GlmMoeDsaConfig.vocab_size: GlmMoeDsaConfig#vocab_size.
  GlmMoeDsaConfig.intermediate_size: GlmMoeDsaConfig#intermediate_size.
  GlmMoeDsaConfig.routed_scaling_factor: GlmMoeDsaConfig#routed_scaling_factor.
  GlmMoeDsaConfig.topk_group: GlmMoeDsaConfig#topk_group.
  GlmMoeDsaConfig.norm_topk_prob: GlmMoeDsaConfig#norm_topk_prob.
  GlmMoeDsaConfig.rope_interleave: GlmMoeDsaConfig#rope_interleave.
  GlmMoeDsaConfig.model_type: GlmMoeDsaConfig#model_type.
  GlmMoeDsaConfig.attribute_map: GlmMoeDsaConfig#attribute_map.
  GlmMoeDsaConfig.__init__: GlmMoeDsaConfig#__init__().
  GlmMoeDsaConfig.max_position_embeddings: GlmMoeDsaConfig#max_position_embeddings.
  GlmMoeDsaConfig.num_key_value_heads: GlmMoeDsaConfig#num_key_value_heads.
  GlmMoeDsaConfig.qk_head_dim: GlmMoeDsaConfig#qk_head_dim.
  GlmMoeDsaConfig.head_dim: GlmMoeDsaConfig#head_dim.
  GlmMoeDsaConfig.pretraining_tp: GlmMoeDsaConfig#pretraining_tp.
  GlmMoeDsaConfig.use_cache: GlmMoeDsaConfig#use_cache.
  GlmMoeDsaConfig.attention_dropout: GlmMoeDsaConfig#attention_dropout.
  GlmMoeDsaConfig.indexer_rope_interleave: GlmMoeDsaConfig#indexer_rope_interleave.
  GlmMoeDsaConfig.rope_theta: GlmMoeDsaConfig#rope_theta.
  GlmMoeDsaConfig.get_partition_rules: GlmMoeDsaConfig#get_partition_rules().
  __all__: __all__.
---
# Module: [`easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py)

## Classes
### `GlmMoeDsaConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py:74`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L74)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class GlmMoeDsaConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L263`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L263)
  - `attention_bias` — [`L224`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L224)
  - `attention_dropout` — [`L225`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L225)
  - `attribute_map` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L151)
  - `head_dim` — [`L214`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L214)
  - `hidden_act` — [`L219`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L219)
  - `hidden_size` — [`L199`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L199)
  - `index_head_dim` — [`L228`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L228)
  - `index_n_heads` — [`L229`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L229)
  - `index_topk` — [`L227`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L227)
  - `indexer_rope_interleave` — [`L230`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L230)
  - `initializer_range` — [`L220`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L220)
  - `intermediate_size` — [`L200`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L200)
  - `kv_lora_rank` — [`L208`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L208)
  - `max_position_embeddings` — [`L198`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L198)
  - `mlp_layer_types` — [`L237`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L237)
  - `model_type` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L150)
  - `moe_intermediate_size` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L201)
  - `n_group` — [`L215`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L215)
  - `n_routed_experts` — [`L206`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L206)
  - `n_shared_experts` — [`L205`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L205)
  - `norm_topk_prob` — [`L218`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L218)
  - `num_attention_heads` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L203)
  - `num_experts_per_tok` — [`L217`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L217)
  - `num_hidden_layers` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L202)
  - `num_key_value_heads` — [`L204`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L204)
  - `pretraining_tp` — [`L222`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L222)
  - `q_lora_rank` — [`L209`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L209)
  - `qk_head_dim` — [`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L212)
  - `qk_nope_head_dim` — [`L211`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L211)
  - `qk_rope_head_dim` — [`L210`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L210)
  - `rms_norm_eps` — [`L221`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L221)
  - `rope_interleave` — [`L226`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L226)
  - `rope_scaling` — [`L231`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L231)
  - `rope_theta` — [`L235`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L235)
  - `routed_scaling_factor` — [`L207`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L207)
  - `topk_group` — [`L216`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L216)
  - `use_cache` — [`L223`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L223)
  - `v_head_dim` — [`L213`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L213)
  - `vocab_size` — [`L197`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L197)
- protocol/private: `__init__`[`L153`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L153)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_rope_scaling_from_rope_parameters`](glm_moe_dsa_configuration.md#_rope_scaling_from_rope_parameters)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`forward_mla`](modeling_glm_moe_dsa.md#GlmMoeDsaAttention.forward_mla), [`define_network`](modeling_glm_moe_dsa.md#GlmMoeDsaAttention.define_network), [`shared_experts`](modeling_glm_moe_dsa.md#GlmMoeDsaMoE.shared_experts), [`__call__`](modeling_glm_moe_dsa.md#GlmMoeDsaIndexer.__call__), [`embed_tokens`](modeling_glm_moe_dsa.md#GlmMoeDsaModel.embed_tokens), [`__init__`](modeling_glm_moe_dsa.md#GlmMoeDsaMoE.__init__), [`__init__`](modeling_glm_moe_dsa.md#GlmMoeDsaModel.__init__), [`qk_nope_head_dim`](modeling_glm_moe_dsa.md#GlmMoeDsaAttention.qk_nope_head_dim), [`GlmMoeDsaForCausalLM`](modeling_glm_moe_dsa.md#GlmMoeDsaForCausalLM), [`down_proj`](modeling_glm_moe_dsa.md#GlmMoeDsaMLPStack.down_proj), [`gate_proj`](modeling_glm_moe_dsa.md#GlmMoeDsaMLPStack.gate_proj), [`up_proj`](modeling_glm_moe_dsa.md#GlmMoeDsaMLPStack.up_proj), [`GlmMoeDsaModel`](modeling_glm_moe_dsa.md#GlmMoeDsaModel), [`kernels_proj`](modeling_glm_moe_dsa.md#GlmMoeDsaIndexer.kernels_proj), [`intermediate_size`](modeling_glm_moe_dsa.md#GlmMoeDsaMLP.intermediate_size), [`norm`](modeling_glm_moe_dsa.md#GlmMoeDsaModel.norm), [`q_head_dim`](modeling_glm_moe_dsa.md#GlmMoeDsaAttention.q_head_dim), [`self_attn`](modeling_glm_moe_dsa.md#GlmMoeDsaDecoderLayer.self_attn), [`wk`](modeling_glm_moe_dsa.md#GlmMoeDsaIndexer.wk), [`wq_b`](modeling_glm_moe_dsa.md#GlmMoeDsaIndexer.wq_b), [`v_head_dim`](modeling_glm_moe_dsa.md#GlmMoeDsaAttention.v_head_dim), [`input_layernorm`](modeling_glm_moe_dsa.md#GlmMoeDsaDecoderLayer.input_layernorm), [`kernel`](modeling_glm_moe_dsa.md#GlmMoeDsaTopKRouter.kernel), [`post_attention_layernorm`](modeling_glm_moe_dsa.md#GlmMoeDsaDecoderLayer.post_attention_layernorm), [`__call__`](modeling_glm_moe_dsa.md#GlmMoeDsaTopKRouter.__call__), [`__init__`](modeling_glm_moe_dsa.md#GlmMoeDsaForCausalLM.__init__), [`index_head_dim`](modeling_glm_moe_dsa.md#GlmMoeDsaIndexer.index_head_dim), [`index_topk`](modeling_glm_moe_dsa.md#GlmMoeDsaAttention.index_topk), [`act_fn`](modeling_glm_moe_dsa.md#GlmMoeDsaMLPStack.act_fn), [`layers`](modeling_glm_moe_dsa.md#GlmMoeDsaModel.layers), [`index_n_heads`](modeling_glm_moe_dsa.md#GlmMoeDsaIndexer.index_n_heads), [`act_fn`](modeling_glm_moe_dsa.md#GlmMoeDsaMLP.act_fn), [`group_topk_k`](modeling_glm_moe_dsa.md#GlmMoeDsaMoE.group_topk_k), [`indexer_rope_interleave`](modeling_glm_moe_dsa.md#GlmMoeDsaIndexer.indexer_rope_interleave), [`hidden_size`](modeling_glm_moe_dsa.md#GlmMoeDsaMLP.hidden_size), [`kv_lora_rank`](modeling_glm_moe_dsa.md#GlmMoeDsaAttention.kv_lora_rank), [`n_routed_experts`](modeling_glm_moe_dsa.md#GlmMoeDsaTopKRouter.n_routed_experts)  (+16 more)

## Functions
- `_rope_scaling_from_rope_parameters(rope_parameters: dict[str, typing.Any] | None, rope_scaling: dict[str, typing.Any] | None)` — [`L24`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L24) — Convert ``rope_parameters`` or ``rope_scaling`` dict into a normalised rope-scaling dict.

## Module values
- `__all__` — [`L267`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/glm_moe_dsa_configuration.py#L267)

