---
title: 'Module: easydel/modules/deepseek_v3/modeling_deepseek.py'
type: catalog
provenance: extracted
module: easydel/modules/deepseek_v3/modeling_deepseek.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.deepseek_v3.modeling_deepseek`/
symbols:
  DeepseekV3Attention.define_network: DeepseekV3Attention#define_network().
  DeepseekV3Model.__call__: DeepseekV3Model#__call__().
  DeepseekV3DecoderLayer.__call__: DeepseekV3DecoderLayer#__call__().
  MoEGate.__call__: MoEGate#__call__().
  DeepseekV3MoE.__call__: DeepseekV3MoE#__call__().
  DeepseekV3MoE.__init__: DeepseekV3MoE#__init__().
  DeepseekV3ForCausalLM.__call__: DeepseekV3ForCausalLM#__call__().
  DeepseekV3ForCausalLM.create_ragged_page_cache_config: DeepseekV3ForCausalLM#create_ragged_page_cache_config().
  DeepseekV3ForCausalLM: DeepseekV3ForCausalLM#
  DeepseekV3Model.embed_tokens: DeepseekV3Model#embed_tokens.
  DeepseekV3Model: DeepseekV3Model#
  DeepseekV3MLP.__call__: DeepseekV3MLP#__call__().
  DeepseekV3MLPMoE.__call__: DeepseekV3MLPMoE#__call__().
  DeepseekV3Attention._create_attention_performer: DeepseekV3Attention#_create_attention_performer().
  DeepseekV3MoE.experts: DeepseekV3MoE#experts.
  DeepseekV3MLPMoE.gate_proj: DeepseekV3MLPMoE#gate_proj.
  DeepseekV3MLPMoE.up_proj: DeepseekV3MLPMoE#up_proj.
  DeepseekV3MLPMoE.down_proj: DeepseekV3MLPMoE#down_proj.
  MoEGate.config: MoEGate#config.
  MoEGate.gating_dim: MoEGate#gating_dim.
  DeepseekV3MLP.intermediate_size: DeepseekV3MLP#intermediate_size.
  MoEGate.n_routed_experts: MoEGate#n_routed_experts.
  MoEGate.kernel: MoEGate#kernel.
  MoEGate.e_score_correction_bias: MoEGate#e_score_correction_bias.
  DeepseekV3MoE.gate: DeepseekV3MoE#gate.
  DeepseekV3DecoderLayer.mlp: DeepseekV3DecoderLayer#mlp.
  DeepseekV3DecoderLayer.input_layernorm: DeepseekV3DecoderLayer#input_layernorm.
  DeepseekV3DecoderLayer.post_attention_layernorm: DeepseekV3DecoderLayer#post_attention_layernorm.
  MoEGate.topk_method: MoEGate#topk_method.
  DeepseekV3Attention.projection_mapping: DeepseekV3Attention#projection_mapping.
  DeepseekV3Attention.q_head_dim: DeepseekV3Attention#q_head_dim.
  DeepseekV3Attention.kv_lora_rank: DeepseekV3Attention#kv_lora_rank.
  DeepseekV3Attention.rotary: DeepseekV3Attention#rotary.
  DeepseekV3DecoderLayer.hidden_size: DeepseekV3DecoderLayer#hidden_size.
  DeepseekV3ForCausalLM.__init__: DeepseekV3ForCausalLM#__init__().
  DeepseekV3ForCausalLM.create_transformer_cache_config: DeepseekV3ForCausalLM#create_transformer_cache_config().
  MoEGate.top_k: MoEGate#top_k.
  MoEGate.scoring_func: MoEGate#scoring_func.
  MoEGate.n_group: MoEGate#n_group.
  DeepseekV3MLPMoE.act_fn: DeepseekV3MLPMoE#act_fn.
  DeepseekV3MLP.gate_proj: DeepseekV3MLP#gate_proj.
  DeepseekV3MLP.down_proj: DeepseekV3MLP#down_proj.
  DeepseekV3MLP.up_proj: DeepseekV3MLP#up_proj.
  DeepseekV3MLP.act_fn: DeepseekV3MLP#act_fn.
  MoEGate.routed_scaling_factor: MoEGate#routed_scaling_factor.
  MoEGate.topk_group: MoEGate#topk_group.
  MoEGate.norm_topk_prob: MoEGate#norm_topk_prob.
  DeepseekV3Model.norm: DeepseekV3Model#norm.
  DeepseekV3Model.frequencies: DeepseekV3Model#frequencies().
  DeepseekV3ForCausalLM._compute_aux_loss: DeepseekV3ForCausalLM#_compute_aux_loss().
  DeepseekV3MLP.hidden_size: DeepseekV3MLP#hidden_size.
  MoEGate.seq_aux: MoEGate#seq_aux.
  MoEGate.craft_sharding: MoEGate#craft_sharding().
  DeepseekV3MLPMoE.precision: DeepseekV3MLPMoE#precision.
  DeepseekV3Model.__init__: DeepseekV3Model#__init__().
  DeepseekV3ForCausalLM._task_type: DeepseekV3ForCausalLM#_task_type.
  DeepseekV3Attention.v_head_dim: DeepseekV3Attention#v_head_dim.
  DeepseekV3Model.layers: DeepseekV3Model#layers.
  DeepseekV3MoE: DeepseekV3MoE#
  DeepseekV3MoE.shared_experts: DeepseekV3MoE#shared_experts.
  DeepseekV3Attention: DeepseekV3Attention#
  DeepseekV3DecoderLayer.self_attn: DeepseekV3DecoderLayer#self_attn.
  DeepseekV3Attention.config: DeepseekV3Attention#config.
  DeepseekV3MLP.__init__: DeepseekV3MLP#__init__().
  MoEGate.__init__: MoEGate#__init__().
  DeepseekV3MLPMoE.__init__: DeepseekV3MLPMoE#__init__().
  DeepseekV3MoE.num_experts_per_tok: DeepseekV3MoE#num_experts_per_tok.
  DeepseekV3MoE.experts_per_rank: DeepseekV3MoE#experts_per_rank.
  DeepseekV3Attention.__init__: DeepseekV3Attention#__init__().
  DeepseekV3Attention.qk_nope_head_dim: DeepseekV3Attention#qk_nope_head_dim.
  DeepseekV3Attention.qk_rope_head_dim: DeepseekV3Attention#qk_rope_head_dim.
  DeepseekV3Attention.head_dim: DeepseekV3Attention#head_dim.
  DeepseekV3DecoderLayer.__init__: DeepseekV3DecoderLayer#__init__().
  DeepseekV3Model.get_embedding: DeepseekV3Model#get_embedding().
  DeepseekV3ForCausalLM._config_class: DeepseekV3ForCausalLM#_config_class.
  DeepseekV3MLP: DeepseekV3MLP#
  DeepseekV3MLP.config: DeepseekV3MLP#config.
  DeepseekV3MLPMoE.config: DeepseekV3MLPMoE#config.
  DeepseekV3MoE.config: DeepseekV3MoE#config.
  DeepseekV3DecoderLayer.config: DeepseekV3DecoderLayer#config.
  MoEGate: MoEGate#
  MoEGate.precision: MoEGate#precision.
  DeepseekV3MLPMoE: DeepseekV3MLPMoE#
  DeepseekV3DecoderLayer: DeepseekV3DecoderLayer#
  DeepseekV3MLP.dtype: DeepseekV3MLP#dtype.
  DeepseekV3MLP.param_dtype: DeepseekV3MLP#param_dtype.
  DeepseekV3MLP.precision: DeepseekV3MLP#precision.
  MoEGate.dtype: MoEGate#dtype.
  MoEGate.param_dtype: MoEGate#param_dtype.
  DeepseekV3MLPMoE.reform_param: DeepseekV3MLPMoE#reform_param.
  DeepseekV3MoE.dtype: DeepseekV3MoE#dtype.
  DeepseekV3MoE.param_dtype: DeepseekV3MoE#param_dtype.
  DeepseekV3MoE.precision: DeepseekV3MoE#precision.
  DeepseekV3MoE.rngs: DeepseekV3MoE#rngs.
  DeepseekV3DecoderLayer.dtype: DeepseekV3DecoderLayer#dtype.
  DeepseekV3DecoderLayer.param_dtype: DeepseekV3DecoderLayer#param_dtype.
  DeepseekV3DecoderLayer.precision: DeepseekV3DecoderLayer#precision.
  DeepseekV3DecoderLayer.rngs: DeepseekV3DecoderLayer#rngs.
  DeepseekV3DecoderLayer.layer_idx: DeepseekV3DecoderLayer#layer_idx.
  DeepseekV3Model.get_encoder: DeepseekV3Model#get_encoder().
  DeepseekV3Model.get_decoder: DeepseekV3Model#get_decoder().
  DeepseekV3Model.get_lm_head: DeepseekV3Model#get_lm_head().
  DeepseekV3ForCausalLM._model_type: DeepseekV3ForCausalLM#_model_type.
---
# Module: [`easydel/modules/deepseek_v3/modeling_deepseek.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py)

## Classes
### `DeepseekV3Attention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/deepseek_v3/modeling_deepseek.py:502`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L502)
- doc: Multi-head Latent Attention (MLA) layer for DeepSeek V3 models.
- signature: `class DeepseekV3Attention(UnifiedAttention):`
- members:
  - `__init__(self, config: DeepseekV3Config, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L520`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L520) — Initialize DeepSeek V3 MLA attention layer.
  - `_create_attention_performer(self, config, rngs)` — [`L702`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L702) — Create attention performer module with custom softmax scale.
  - `define_network(self, config: DeepseekV3Config, dtype: jnp.dtype, param_dtype: jnp.dtype, precision: jax.lax.Precision, rngs: nn.Rngs)` — [`L565`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L565) — Define MLA-specific network structure. — documented in [easydel-layers-attention-_unified](../../../../concepts/easydel-layers-attention-_unified.md)
  - `config` — [`L543`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L543)
  - `head_dim` — [`L563`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L563)
  - `kv_lora_rank` — [`L548`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L548)
  - `projection_mapping` — [`L509`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L509)
  - `q_head_dim` — [`L544`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L544)
  - `qk_nope_head_dim` — [`L545`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L545)
  - `qk_rope_head_dim` — [`L546`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L546)
  - `rotary` — [`L699`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L699)
  - `v_head_dim` — [`L547`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L547)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`attention_performer`](../../layers/attention/_unified.md#UnifiedAttention.attention_performer), [`DeepseekV3Config`](deepseek_configuration.md#DeepseekV3Config), [`yarn_get_mscale`](../../layers/rotary/_utils.md#yarn_get_mscale), [`hidden_size`](deepseek_configuration.md#DeepseekV3Config.hidden_size), [`use_mla_lora`](../../layers/attention/_unified.md#UnifiedAttention.use_mla_lora), [`initializer_range`](deepseek_configuration.md#DeepseekV3Config.initializer_range), [`rope_scaling`](deepseek_configuration.md#DeepseekV3Config.rope_scaling), [`kv_lora_rank`](deepseek_configuration.md#DeepseekV3Config.kv_lora_rank), [`num_attention_heads`](deepseek_configuration.md#DeepseekV3Config.num_attention_heads), [`q_lora_rank`](deepseek_configuration.md#DeepseekV3Config.q_lora_rank), [`rms_norm_eps`](deepseek_configuration.md#DeepseekV3Config.rms_norm_eps), [`attention_bias`](deepseek_configuration.md#DeepseekV3Config.attention_bias), [`qk_nope_head_dim`](deepseek_configuration.md#DeepseekV3Config.qk_nope_head_dim), [`qk_rope_head_dim`](deepseek_configuration.md#DeepseekV3Config.qk_rope_head_dim), [`v_head_dim`](deepseek_configuration.md#DeepseekV3Config.v_head_dim)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_attention_performer`](../../layers/attention/_unified.md#UnifiedAttention._create_attention_performer), [`define_network`](../../layers/attention/_unified.md#UnifiedAttention.define_network), [`self_attn`](modeling_deepseek.md#DeepseekV3DecoderLayer.self_attn)

### `DeepseekV3DecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/deepseek_v3/modeling_deepseek.py:730`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L730)
- doc: Single decoder layer for DeepSeek V3 models.
- signature: `class DeepseekV3DecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Array, mask_info: MaskInfo, position_ids: Array, mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: tuple[Array, Array] | None = None)` — [`L816`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L816) — Forward pass through the decoder layer.
  - `__init__(self, config: DeepseekV3Config, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L737`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L737) — Initialize DeepSeek V3 decoder layer.
  - `config` — [`L759`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L759)
  - `dtype` — [`L760`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L760)
  - `hidden_size` — [`L765`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L765)
  - `input_layernorm` — [`L801`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L801)
  - `layer_idx` — [`L764`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L764)
  - `mlp` — [`L779`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L779)
  - `param_dtype` — [`L761`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L761)
  - `post_attention_layernorm` — [`L808`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L808)
  - `precision` — [`L762`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L762)
  - `rngs` — [`L763`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L763)
  - `self_attn` — [`L770`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L770)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`DeepseekV3Config`](deepseek_configuration.md#DeepseekV3Config), [`hidden_size`](deepseek_configuration.md#DeepseekV3Config.hidden_size), [`n_routed_experts`](deepseek_configuration.md#DeepseekV3Config.n_routed_experts), [`rms_norm_eps`](deepseek_configuration.md#DeepseekV3Config.rms_norm_eps), [`DeepseekV3Attention`](modeling_deepseek.md#DeepseekV3Attention), [`DeepseekV3MoE`](modeling_deepseek.md#DeepseekV3MoE), [`DeepseekV3MLP`](modeling_deepseek.md#DeepseekV3MLP), [`first_k_dense_replace`](deepseek_configuration.md#DeepseekV3Config.first_k_dense_replace), [`moe_layer_freq`](deepseek_configuration.md#DeepseekV3Config.moe_layer_freq)
- used by: [`embed_tokens`](modeling_deepseek.md#DeepseekV3Model.embed_tokens)

### `DeepseekV3ForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/deepseek_v3/modeling_deepseek.py:1143`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L1143)
- doc: DeepSeek V3 model with a language modeling head for causal language modeling tasks.
- signature: `class DeepseekV3ForCausalLM(BaseCausalLMModule[DeepseekV3Model, DeepseekV3Config]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None)` — [`L1190`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L1190) — Forward pass of the causal language model.
  - `__init__(self, config: DeepseekV3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1160`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L1160) — Initialize DeepSeek V3 model for causal language modeling.
  - `_compute_aux_loss(self, outputs, attention_mask)` — [`L1256`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L1256) — Compute auxiliary loss for MoE load balancing.
  - `create_ragged_page_cache_config(self, max_length: int, *, page_size: int = 128, hbm_utilization: float = 0.9, dtype: jnp.dtype | None = None)` — [`L1312`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L1312) — Create paged cache configuration for MLA attention.
  - `create_transformer_cache_config(self, batch_size: int, max_length: int, **kwargs)` — [`L1279`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L1279) — Create cache configuration for MLA attention.
- protocol/private: `_config_class`[`L1158`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L1158), `_model_type`[`L1157`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L1157), `_task_type`[`L1156`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L1156)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`RaggedPagesCacheConfig`](../../caching/ragged_page/cache.md#RaggedPagesCacheConfig), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`mesh`](../../infra/base_module.md#EasyDeLBaseModule.mesh), [`MoeCausalLMOutput`](../../infra/modeling_outputs.md#MoeCausalLMOutput), [`AttentionMechanisms`](../../layers/attention/_flexible.md#AttentionMechanisms), [`create`](../../caching/ragged_page/cache.md#RaggedPagesCacheConfig.create), [`auxiliary_load_balancing_loss_func`](../../infra/loss_utils.md#auxiliary_load_balancing_loss_func), [`forward_moe`](../_base/causal_lm_module.md#BaseCausalLMModule.forward_moe), [`create`](../../caching/mla_ragged_page/cache.md#MLARaggedPagesCacheConfig.create), [`MLARaggedPagesCacheConfig`](../../caching/mla_ragged_page/cache.md#MLARaggedPagesCacheConfig), [`DeepseekV3Config`](deepseek_configuration.md#DeepseekV3Config), [`TransformerCacheConfig`](../../caching/transformer/cache.md#TransformerCacheConfig), [`DeepseekV3Model`](modeling_deepseek.md#DeepseekV3Model), [`create`](../../caching/transformer/cache.md#TransformerCacheConfig.create), [`RAGGED_PAGE_ATTENTION_V3`](../../layers/attention/_flexible.md#AttentionMechanisms.RAGGED_PAGE_ATTENTION_V3), [`RAGGED_PAGE_ATTENTION_V2`](../../layers/attention/_flexible.md#AttentionMechanisms.RAGGED_PAGE_ATTENTION_V2)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`create_ragged_page_cache_config`](../../infra/mixins/generation.md#EasyGenerationMixin.create_ragged_page_cache_config), [`create_transformer_cache_config`](../../infra/mixins/generation.md#EasyGenerationMixin.create_transformer_cache_config), [`KimiVLForConditionalGeneration`](../kimi_vl/modeling_kimi_vl.md#KimiVLForConditionalGeneration), [`__init__`](../kimi_vl/modeling_kimi_vl.md#KimiVLForConditionalGeneration.__init__)

### `DeepseekV3MLP`  ·  implements/extends Module
- def: [`easydel/modules/deepseek_v3/modeling_deepseek.py:68`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L68)
- doc: Multi-Layer Perceptron module for DeepSeek V3 dense layers.
- signature: `class DeepseekV3MLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L119) — Apply SwiGLU feedforward transformation.
  - `__init__(self, config: DeepseekV3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, hidden_size=None, intermediate_size=None, *, rngs: nn.Rngs)` — [`L75`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L75) — Initialize DeepSeek V3 MLP block.
  - `act_fn` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L117)
  - `config` — [`L99`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L99)
  - `down_proj` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L115)
  - `dtype` — [`L100`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L100)
  - `gate_proj` — [`L114`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L114)
  - `hidden_size` — [`L103`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L103)
  - `intermediate_size` — [`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L104)
  - `param_dtype` — [`L101`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L101)
  - `precision` — [`L102`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L102)
  - `up_proj` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L116)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`DeepseekV3Config`](deepseek_configuration.md#DeepseekV3Config), [`hidden_size`](deepseek_configuration.md#DeepseekV3Config.hidden_size), [`initializer_range`](deepseek_configuration.md#DeepseekV3Config.initializer_range), [`hidden_act`](deepseek_configuration.md#DeepseekV3Config.hidden_act), [`intermediate_size`](deepseek_configuration.md#DeepseekV3Config.intermediate_size)
- used by: [`hidden_size`](modeling_deepseek.md#DeepseekV3DecoderLayer.hidden_size), [`shared_experts`](modeling_deepseek.md#DeepseekV3MoE.shared_experts)

### `DeepseekV3MLPMoE`  ·  implements/extends Module
- def: [`easydel/modules/deepseek_v3/modeling_deepseek.py:281`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L281)
- doc: Mixture-of-experts feed-forward module for DeepSeek V3 MoE layers.
- signature: `class DeepseekV3MLPMoE(nn.Module):`
- members:
  - `__call__(self, hidden_states: Array, group_sizes: Array, sorted_experts: Array | None = None)` — [`L371`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L371) — Apply SwiGLU feedforward transformation through MoE experts.
  - `__init__(self, config: DeepseekV3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, hidden_size: int | None = None, intermediate_size: int | None = None, *, rngs: nn.Rngs)` — [`L304`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L304) — Initialize DeepSeek V3 MoE MLP block.
  - `act_fn` — [`L369`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L369)
  - `config` — [`L328`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L328)
  - `down_proj` — [`L357`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L357)
  - `gate_proj` — [`L333`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L333)
  - `precision` — [`L329`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L329)
  - `reform_param` — [`L288`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L288)
  - `up_proj` — [`L345`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L345)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`use_expert_tensor_mode`](../../infra/base_config.md#EasyDeLBaseConfig.use_expert_tensor_mode), [`ColumnParallelMoELinear`](../../layers/linears/_linear_moe.md#ColumnParallelMoELinear), [`RowParallelMoELinear`](../../layers/linears/_linear_moe.md#RowParallelMoELinear), [`DeepseekV3Config`](deepseek_configuration.md#DeepseekV3Config), [`hidden_size`](deepseek_configuration.md#DeepseekV3Config.hidden_size), [`n_routed_experts`](deepseek_configuration.md#DeepseekV3Config.n_routed_experts), [`hidden_act`](deepseek_configuration.md#DeepseekV3Config.hidden_act), [`intermediate_size`](deepseek_configuration.md#DeepseekV3Config.intermediate_size)
- used by: [`__call__`](modeling_deepseek.md#DeepseekV3MoE.__call__), [`experts`](modeling_deepseek.md#DeepseekV3MoE.experts)

### `DeepseekV3MoE`  ·  implements/extends BaseMoeModule
- def: [`easydel/modules/deepseek_v3/modeling_deepseek.py:406`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L406)
- doc: Mixture-of-experts module combining gating and expert networks for DeepSeek V3.
- signature: `class DeepseekV3MoE(BaseMoeModule):`
- members:
  - `__call__(self, hidden_states: Array)` — [`L477`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L477) — Process tokens through MoE experts with routing.
  - `__init__(self, config: DeepseekV3Config, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L413`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L413) — Initialize DeepSeek V3 MoE layer.
  - `config` — [`L444`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L444)
  - `dtype` — [`L445`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L445)
  - `experts` — [`L451`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L451)
  - `experts_per_rank` — [`L450`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L450)
  - `gate` — [`L459`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L459)
  - `num_experts_per_tok` — [`L449`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L449)
  - `param_dtype` — [`L446`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L446)
  - `precision` — [`L447`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L447)
  - `rngs` — [`L448`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L448)
  - `shared_experts` — [`L468`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L468)
- uses (calls/refs, reference-scoped): [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`kernel`](../../layers/linears/_linear_moe.md#ParallelMoELinear.kernel), [`MoeRoutingStrategy`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy), [`moe_call`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_call), [`MoeLoadBalancingStrategy`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy), [`__init__`](../../layers/moe/_moe_module.md#BaseMoeModule.__init__), [`DeepseekV3Config`](deepseek_configuration.md#DeepseekV3Config), [`TOP_K`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy.TOP_K), [`STANDARD`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy.STANDARD), [`down_proj`](modeling_deepseek.md#DeepseekV3MLPMoE.down_proj), [`gate_proj`](modeling_deepseek.md#DeepseekV3MLPMoE.gate_proj), [`hidden_size`](deepseek_configuration.md#DeepseekV3Config.hidden_size), [`up_proj`](modeling_deepseek.md#DeepseekV3MLPMoE.up_proj), [`act_fn`](modeling_deepseek.md#DeepseekV3MLPMoE.act_fn), [`n_routed_experts`](deepseek_configuration.md#DeepseekV3Config.n_routed_experts), [`n_shared_experts`](deepseek_configuration.md#DeepseekV3Config.n_shared_experts), [`num_experts_per_tok`](deepseek_configuration.md#DeepseekV3Config.num_experts_per_tok), [`DeepseekV3MLP`](modeling_deepseek.md#DeepseekV3MLP), [`moe_intermediate_size`](deepseek_configuration.md#DeepseekV3Config.moe_intermediate_size), [`DeepseekV3MLPMoE`](modeling_deepseek.md#DeepseekV3MLPMoE), [`MoEGate`](modeling_deepseek.md#MoEGate)
- used by: [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`hidden_size`](modeling_deepseek.md#DeepseekV3DecoderLayer.hidden_size)

### `DeepseekV3Model`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/deepseek_v3/modeling_deepseek.py:895`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L895)
- doc: DeepSeek V3 base model implementation.
- signature: `class DeepseekV3Model(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None)` — [`L986`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L986) — Forward pass through the DeepSeek V3 base model.
  - `__init__(self, config: DeepseekV3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L908`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L908) — Initialize DeepSeek V3 base model.
  - `frequencies(self)` — [`L971`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L971) — Compute RoPE frequencies for rotary position embeddings.
  - `get_decoder(self)` — [`L1122`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L1122) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L1135`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L1135) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L1115`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L1115) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L1128`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L1128) — Returns the language model head of the module.
  - `embed_tokens` — [`L934`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L934)
  - `layers` — [`L949`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L949)
  - `norm` — [`L962`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L962)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`MoeModelOutput`](../../infra/modeling_outputs.md#MoeModelOutput), [`gradient_checkpointing`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing), [`get_basic_frequencies`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_frequencies), [`DeepseekV3Config`](deepseek_configuration.md#DeepseekV3Config), [`DeepseekV3DecoderLayer`](modeling_deepseek.md#DeepseekV3DecoderLayer)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`DeepseekV3ForCausalLM`](modeling_deepseek.md#DeepseekV3ForCausalLM), [`__init__`](modeling_deepseek.md#DeepseekV3ForCausalLM.__init__)

### `MoEGate`  ·  implements/extends Module
- def: [`easydel/modules/deepseek_v3/modeling_deepseek.py:148`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L148)
- doc: Router module that scores tokens and selects experts for DeepSeek V3 MoE.
- signature: `class MoEGate(nn.Module):`
- members:
  - `__call__(self, hidden_states)` — [`L226`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L226) — Compute expert routing weights for input tokens.
  - `__init__(self, config: DeepseekV3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L155) — Initialize MoE gating module.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L209`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L209) — Return sharding specifications for MoEGate parameters.
  - `config` — [`L174`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L174)
  - `dtype` — [`L175`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L175)
  - `e_score_correction_bias` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L202)
  - `gating_dim` — [`L187`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L187)
  - `kernel` — [`L194`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L194)
  - `n_group` — [`L184`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L184)
  - `n_routed_experts` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L179)
  - `norm_topk_prob` — [`L186`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L186)
  - `param_dtype` — [`L176`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L176)
  - `precision` — [`L177`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L177)
  - `routed_scaling_factor` — [`L180`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L180)
  - `scoring_func` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L181)
  - `seq_aux` — [`L182`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L182)
  - `top_k` — [`L178`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L178)
  - `topk_group` — [`L185`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L185)
  - `topk_method` — [`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/modeling_deepseek.py#L183)
- uses (calls/refs, reference-scoped): [`ArrayParam`](../../infra/utils.md#ArrayParam), [`bound`](../../infra/utils.md#ArrayParam.bound), [`use_expert_tensor_mode`](../../infra/base_config.md#EasyDeLBaseConfig.use_expert_tensor_mode), [`DeepseekV3Config`](deepseek_configuration.md#DeepseekV3Config), [`hidden_size`](deepseek_configuration.md#DeepseekV3Config.hidden_size), [`n_routed_experts`](deepseek_configuration.md#DeepseekV3Config.n_routed_experts), [`num_experts_per_tok`](deepseek_configuration.md#DeepseekV3Config.num_experts_per_tok), [`n_group`](deepseek_configuration.md#DeepseekV3Config.n_group), [`norm_topk_prob`](deepseek_configuration.md#DeepseekV3Config.norm_topk_prob), [`routed_scaling_factor`](deepseek_configuration.md#DeepseekV3Config.routed_scaling_factor), [`scoring_func`](deepseek_configuration.md#DeepseekV3Config.scoring_func), [`seq_aux`](deepseek_configuration.md#DeepseekV3Config.seq_aux), [`topk_group`](deepseek_configuration.md#DeepseekV3Config.topk_group), [`topk_method`](deepseek_configuration.md#DeepseekV3Config.topk_method)
- used by: [`gate`](modeling_deepseek.md#DeepseekV3MoE.gate)

