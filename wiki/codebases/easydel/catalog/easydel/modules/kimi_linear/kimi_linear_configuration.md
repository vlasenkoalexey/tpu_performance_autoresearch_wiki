---
title: 'Module: easydel/modules/kimi_linear/kimi_linear_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/kimi_linear/kimi_linear_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.kimi_linear.kimi_linear_configuration`/K
symbols:
  KimiLinearConfig.hidden_size: imiLinearConfig#hidden_size.
  KimiLinearConfig: imiLinearConfig#
  KimiLinearConfig.is_mla: imiLinearConfig#is_mla().
  KimiLinearConfig.linear_attn_config: imiLinearConfig#linear_attn_config.
  KimiLinearConfig.initializer_range: imiLinearConfig#initializer_range.
  KimiLinearConfig.get_layer_types: imiLinearConfig#get_layer_types().
  KimiLinearConfig.get_rope_config: imiLinearConfig#get_rope_config().
  KimiLinearConfig.is_moe_layer: imiLinearConfig#is_moe_layer().
  KimiLinearConfig.num_experts: imiLinearConfig#num_experts.
  KimiLinearConfig.q_head_dim: imiLinearConfig#q_head_dim().
  KimiLinearConfig.rms_norm_eps: imiLinearConfig#rms_norm_eps.
  KimiLinearConfig.q_lora_rank: imiLinearConfig#q_lora_rank.
  KimiLinearConfig.qk_nope_head_dim: imiLinearConfig#qk_nope_head_dim.
  KimiLinearConfig.qk_rope_head_dim: imiLinearConfig#qk_rope_head_dim.
  KimiLinearConfig.num_attention_heads: imiLinearConfig#num_attention_heads.
  KimiLinearConfig.kv_lora_rank: imiLinearConfig#kv_lora_rank.
  KimiLinearConfig.num_shared_experts: imiLinearConfig#num_shared_experts.
  KimiLinearConfig.is_kda_layer: imiLinearConfig#is_kda_layer().
  KimiLinearConfig.v_head_dim: imiLinearConfig#v_head_dim.
  KimiLinearConfig.moe_router_activation_func: imiLinearConfig#moe_router_activation_func.
  KimiLinearConfig.num_experts_per_token: imiLinearConfig#num_experts_per_token.
  KimiLinearConfig.moe_intermediate_size: imiLinearConfig#moe_intermediate_size.
  KIMI_LINEAR_PRETRAINED_CONFIG_ARCHIVE_MAP: IMI_LINEAR_PRETRAINED_CONFIG_ARCHIVE_MAP.
  KimiLinearConfig.is_moe: imiLinearConfig#is_moe().
  KimiLinearConfig.is_linear_attn: imiLinearConfig#is_linear_attn().
  KimiLinearConfig.is_mla_layer: imiLinearConfig#is_mla_layer().
  KimiLinearConfig.intermediate_size: imiLinearConfig#intermediate_size.
  KimiLinearConfig.num_hidden_layers: imiLinearConfig#num_hidden_layers.
  KimiLinearConfig.hidden_act: imiLinearConfig#hidden_act.
  KimiLinearConfig.num_expert_group: imiLinearConfig#num_expert_group.
  KimiLinearConfig.vocab_size: imiLinearConfig#vocab_size.
  KimiLinearConfig.head_dim: imiLinearConfig#head_dim.
  KimiLinearConfig.rope_theta: imiLinearConfig#rope_theta.
  KimiLinearConfig.mla_use_nope: imiLinearConfig#mla_use_nope.
  KimiLinearConfig.moe_renormalize: imiLinearConfig#moe_renormalize.
  KimiLinearConfig.routed_scaling_factor: imiLinearConfig#routed_scaling_factor.
  KimiLinearConfig.first_k_dense_replace: imiLinearConfig#first_k_dense_replace.
  KimiLinearConfig.moe_layer_freq: imiLinearConfig#moe_layer_freq.
  KimiLinearConfig.topk_group: imiLinearConfig#topk_group.
  KimiLinearConfig.max_position_embeddings: imiLinearConfig#max_position_embeddings.
  KimiLinearConfig.model_type: imiLinearConfig#model_type.
  KimiLinearConfig.keys_to_ignore_at_inference: imiLinearConfig#keys_to_ignore_at_inference.
  KimiLinearConfig.__init__: imiLinearConfig#__init__().
  KimiLinearConfig.num_key_value_heads: imiLinearConfig#num_key_value_heads.
  KimiLinearConfig.use_cache: imiLinearConfig#use_cache.
  KimiLinearConfig.rope_scaling: imiLinearConfig#rope_scaling.
  KimiLinearConfig.use_grouped_topk: imiLinearConfig#use_grouped_topk.
  KimiLinearConfig.num_nextn_predict_layers: imiLinearConfig#num_nextn_predict_layers.
  KimiLinearConfig.get_partition_rules: imiLinearConfig#get_partition_rules().
---
# Module: [`easydel/modules/kimi_linear/kimi_linear_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py)

## Classes
### `KimiLinearConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/kimi_linear/kimi_linear_configuration.py:39`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L39)
- doc: Configuration class for Kimi Linear models.
- signature: `class KimiLinearConfig(EasyDeLBaseConfig):`
- members:
  - `get_layer_types(self)` — [`L308`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L308) — Get layer types tuple for HybridCache initialization.
  - `get_partition_rules(self, *args, **kwargs)` — [`L329`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L329) — Returns partition rules for model sharding.
  - `get_rope_config(self)` — [`L342`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L342) — Get RoPE configuration.
  - `is_kda_layer(self, layer_idx: int)` — [`L269`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L269) — Check if a layer uses KDA linear attention (1-indexed in config).
  - `is_linear_attn(self)` — [`L258`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L258) — Check if model uses linear attention (KDA).
  - `is_mla(self)` — [`L241`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L241) — Check if model uses Multi-Latent Attention.
  - `is_mla_layer(self, layer_idx: int)` — [`L280`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L280) — Check if a layer uses MLA full attention (1-indexed in config).
  - `is_moe(self)` — [`L253`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L253) — Check if model uses Mixture of Experts.
  - `is_moe_layer(self, layer_idx: int)` — [`L293`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L293) — Check if a layer uses MoE.
  - `q_head_dim(self)` — [`L323`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L323) — Get query head dimension for MLA.
  - `first_k_dense_replace` — [`L218`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L218)
  - `head_dim` — [`L195`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L195)
  - `hidden_act` — [`L196`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L196)
  - `hidden_size` — [`L186`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L186)
  - `initializer_range` — [`L197`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L197)
  - `intermediate_size` — [`L187`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L187)
  - `keys_to_ignore_at_inference` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L141)
  - `kv_lora_rank` — [`L204`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L204)
  - `linear_attn_config` — [`L228`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L228)
  - `max_position_embeddings` — [`L224`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L224)
  - `mla_use_nope` — [`L208`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L208)
  - `model_type` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L140)
  - `moe_intermediate_size` — [`L217`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L217)
  - `moe_layer_freq` — [`L219`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L219)
  - `moe_renormalize` — [`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L212)
  - `moe_router_activation_func` — [`L215`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L215)
  - `num_attention_heads` — [`L189`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L189)
  - `num_expert_group` — [`L221`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L221)
  - `num_experts` — [`L210`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L210)
  - `num_experts_per_token` — [`L211`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L211)
  - `num_hidden_layers` — [`L188`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L188)
  - `num_key_value_heads` — [`L193`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L193)
  - `num_nextn_predict_layers` — [`L223`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L223)
  - `num_shared_experts` — [`L213`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L213)
  - `q_lora_rank` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L203)
  - `qk_nope_head_dim` — [`L205`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L205)
  - `qk_rope_head_dim` — [`L206`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L206)
  - `rms_norm_eps` — [`L198`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L198)
  - `rope_scaling` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L201)
  - `rope_theta` — [`L200`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L200)
  - `routed_scaling_factor` — [`L214`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L214)
  - `topk_group` — [`L222`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L222)
  - `use_cache` — [`L199`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L199)
  - `use_grouped_topk` — [`L220`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L220)
  - `v_head_dim` — [`L207`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L207)
  - `vocab_size` — [`L185`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L185)
- protocol/private: `__init__`[`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L143)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`RopeConfig`](../../layers/rotary/_configs.md#RopeConfig), [`FULL_ATTENTION`](../../caching/hybrid/cache.md#FULL_ATTENTION), [`KDA_LINEAR_ATTENTION`](../../caching/hybrid/cache.md#KDA_LINEAR_ATTENTION), [`rope_type`](../../layers/rotary/_configs.md#RopeConfig.rope_type)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`define_network`](modeling_kimi_linear.md#KimiMLAAttention.define_network), [`__call__`](modeling_kimi_linear.md#KimiSparseMoeBlock.__call__), [`__init__`](modeling_kimi_linear.md#KimiSparseMoeBlock.__init__), [`embed_tokens`](modeling_kimi_linear.md#KimiLinearModel.embed_tokens), [`KimiLinearForCausalLM`](modeling_kimi_linear.md#KimiLinearForCausalLM), [`KimiLinearModel`](modeling_kimi_linear.md#KimiLinearModel), [`value_dim`](modeling_kimi_linear.md#KimiDeltaAttention.value_dim), [`self_attn`](modeling_kimi_linear.md#KimiDecoderLayer.self_attn), [`down_proj`](modeling_kimi_linear.md#KimiMLPMoE.down_proj), [`gate_proj`](modeling_kimi_linear.md#KimiMLPMoE.gate_proj), [`up_proj`](modeling_kimi_linear.md#KimiMLPMoE.up_proj), [`experts`](modeling_kimi_linear.md#KimiSparseMoeBlock.experts), [`num_heads`](modeling_kimi_linear.md#KimiDeltaAttention.num_heads), [`o_proj`](modeling_kimi_linear.md#KimiDeltaAttention.o_proj), [`down_proj`](modeling_kimi_linear.md#KimiMLP.down_proj), [`input_layernorm`](modeling_kimi_linear.md#KimiDecoderLayer.input_layernorm), [`norm`](modeling_kimi_linear.md#KimiLinearModel.norm), [`o_norm`](modeling_kimi_linear.md#KimiDeltaAttention.o_norm), [`post_attention_layernorm`](modeling_kimi_linear.md#KimiDecoderLayer.post_attention_layernorm), [`precision`](modeling_kimi_linear.md#KimiMoEGate.precision), [`__init__`](modeling_kimi_linear.md#KimiLinearForCausalLM.__init__), [`kv_lora_rank`](modeling_kimi_linear.md#KimiMLAAttention.kv_lora_rank), [`precision`](modeling_kimi_linear.md#KimiMLP.precision), [`act_fn`](modeling_kimi_linear.md#KimiMLPMoE.act_fn), [`is_moe_layer`](modeling_kimi_linear.md#KimiDecoderLayer.is_moe_layer), [`q_head_dim`](modeling_kimi_linear.md#KimiMLAAttention.q_head_dim), [`act_fn`](modeling_kimi_linear.md#KimiMLP.act_fn), [`b_proj`](modeling_kimi_linear.md#KimiDeltaAttention.b_proj), [`f_a_proj`](modeling_kimi_linear.md#KimiDeltaAttention.f_a_proj), [`g_a_proj`](modeling_kimi_linear.md#KimiDeltaAttention.g_a_proj), [`k_proj`](modeling_kimi_linear.md#KimiDeltaAttention.k_proj), [`q_proj`](modeling_kimi_linear.md#KimiDeltaAttention.q_proj), [`v_proj`](modeling_kimi_linear.md#KimiDeltaAttention.v_proj), [`n_routed_experts`](modeling_kimi_linear.md#KimiMoEGate.n_routed_experts), [`__init__`](modeling_kimi_linear.md#KimiLinearModel.__init__), [`precision`](modeling_kimi_linear.md#KimiMLPMoE.precision), [`is_kda_layer`](modeling_kimi_linear.md#KimiDecoderLayer.is_kda_layer)  (+20 more)

## Module values
- `KIMI_LINEAR_PRETRAINED_CONFIG_ARCHIVE_MAP` — [`L35`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_linear/kimi_linear_configuration.py#L35)

