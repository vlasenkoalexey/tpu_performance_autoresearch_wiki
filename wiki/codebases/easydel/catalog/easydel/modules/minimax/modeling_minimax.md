---
title: 'Module: easydel/modules/minimax/modeling_minimax.py'
type: catalog
provenance: extracted
module: easydel/modules/minimax/modeling_minimax.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.minimax.modeling_minimax`/MiniMax
symbols:
  MiniMaxModel.__call__: Model#__call__().
  MiniMaxDecoderLayer.__call__: DecoderLayer#__call__().
  MiniMaxLightningAttention.__call__: LightningAttention#__call__().
  MiniMaxSparseMoeBlock.__init__: SparseMoeBlock#__init__().
  MiniMaxSparseMoeBlock.__call__: SparseMoeBlock#__call__().
  MiniMaxModel.embed_tokens: Model#embed_tokens.
  MiniMaxForCausalLM.__call__: ForCausalLM#__call__().
  MiniMaxDecoderLayer.attn_beta_factor: DecoderLayer#attn_beta_factor.
  MiniMaxExperts.w1: Experts#w1.
  MiniMaxExperts.w2: Experts#w2.
  MiniMaxExperts.w3: Experts#w3.
  MiniMaxForCausalLM: ForCausalLM#
  MiniMaxModel: Model#
  MiniMaxLightningAttention.qkv_proj: LightningAttention#qkv_proj.
  MiniMaxLightningAttention.out_proj: LightningAttention#out_proj.
  MiniMaxLightningAttention.output_gate: LightningAttention#output_gate.
  MiniMaxLightningAttention.head_dim: LightningAttention#head_dim.
  MiniMaxLightningAttention.num_attention_heads: LightningAttention#num_attention_heads.
  MiniMaxLightningAttention.norm: LightningAttention#norm.
  MiniMaxSparseMoeBlock.gate: SparseMoeBlock#gate.
  MiniMaxExperts.__call__: Experts#__call__().
  MiniMaxForCausalLM.__init__: ForCausalLM#__init__().
  MiniMaxDecoderLayer.layer_type: DecoderLayer#layer_type.
  MiniMaxLightningAttention.block_size: LightningAttention#block_size.
  MiniMaxLightningAttention._get_slope_rate: LightningAttention#_get_slope_rate().
  MiniMaxDecoderLayer.input_layernorm: DecoderLayer#input_layernorm.
  MiniMaxDecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  MiniMaxModel.norm: Model#norm.
  MiniMaxSparseMoeBlock.experts: SparseMoeBlock#experts.
  MiniMaxForCausalLM.get_operations_cache_view: ForCausalLM#get_operations_cache_view().
  MiniMaxForCausalLM.create_recurrent_cache_config: ForCausalLM#create_recurrent_cache_config().
  MiniMaxExperts.act_fn: Experts#act_fn.
  MiniMaxLightningAttention.act_fn: LightningAttention#act_fn.
  MiniMaxAttention: Attention#
  MiniMaxSparseMoeBlock.jitter_noise: SparseMoeBlock#jitter_noise.
  MiniMaxAttention.__init__: Attention#__init__().
  MiniMaxModel.__init__: Model#__init__().
  MiniMaxForCausalLM._task_type: ForCausalLM#_task_type.
  MiniMaxDecoderLayer.attn_alpha_factor: DecoderLayer#attn_alpha_factor.
  MiniMaxModel.layers: Model#layers.
  MiniMaxLightningAttention.config: LightningAttention#config.
  MiniMaxLightningAttention.num_hidden_layers: LightningAttention#num_hidden_layers.
  MiniMaxLightningAttention._decay_factors: LightningAttention#_decay_factors().
  MiniMaxSparseMoeBlock: SparseMoeBlock#
  MiniMaxDecoderLayer.mlp_alpha_factor: DecoderLayer#mlp_alpha_factor.
  MiniMaxDecoderLayer.mlp_beta_factor: DecoderLayer#mlp_beta_factor.
  MiniMaxLightningAttention.__init__: LightningAttention#__init__().
  MiniMaxLightningAttention.hidden_size: LightningAttention#hidden_size.
  MiniMaxExperts.__init__: Experts#__init__().
  MiniMaxExperts.precision: Experts#precision.
  MiniMaxDecoderLayer.__init__: DecoderLayer#__init__().
  MiniMaxModel.get_embedding: Model#get_embedding().
  MiniMaxForCausalLM._config_class: ForCausalLM#_config_class.
  MiniMaxDecoderLayer.config: DecoderLayer#config.
  MiniMaxDecoderLayer.self_attn: DecoderLayer#self_attn.
  MiniMaxLightningAttention: LightningAttention#
  MiniMaxLightningAttention.layer_idx: LightningAttention#layer_idx.
  MiniMaxExperts: Experts#
  MiniMaxSparseMoeBlock.rngs: SparseMoeBlock#rngs.
  MiniMaxSparseMoeBlock._normalize_weights: SparseMoeBlock#_normalize_weights().
  MiniMaxDecoderLayer: DecoderLayer#
  MiniMaxDecoderLayer.layer_idx: DecoderLayer#layer_idx.
  MiniMaxDecoderLayer.block_sparse_moe: DecoderLayer#block_sparse_moe.
  MiniMaxExperts.reform_param: Experts#reform_param.
  MiniMaxExperts.config: Experts#config.
  MiniMaxExperts.dtype: Experts#dtype.
  MiniMaxExperts.param_dtype: Experts#param_dtype.
  MiniMaxSparseMoeBlock.config: SparseMoeBlock#config.
  MiniMaxSparseMoeBlock.dtype: SparseMoeBlock#dtype.
  MiniMaxSparseMoeBlock.param_dtype: SparseMoeBlock#param_dtype.
  MiniMaxSparseMoeBlock.precision: SparseMoeBlock#precision.
  MiniMaxDecoderLayer.reform_param: DecoderLayer#reform_param.
  MiniMaxDecoderLayer.dtype: DecoderLayer#dtype.
  MiniMaxDecoderLayer.param_dtype: DecoderLayer#param_dtype.
  MiniMaxDecoderLayer.precision: DecoderLayer#precision.
  MiniMaxModel.get_encoder: Model#get_encoder().
  MiniMaxModel.get_decoder: Model#get_decoder().
  MiniMaxModel.get_lm_head: Model#get_lm_head().
  MiniMaxForCausalLM._model_type: ForCausalLM#_model_type.
  MiniMaxForCausalLM.get_inference_cache_type: ForCausalLM#get_inference_cache_type().
---
# Module: [`easydel/modules/minimax/modeling_minimax.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py)

## Classes
### `MiniMaxAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/minimax/modeling_minimax.py:313`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L313)
- doc: Standard multi-head attention module for MiniMax models.
- signature: `class MiniMaxAttention(UnifiedAttention[MiniMaxConfig]):`
- members:
  - `__init__(self, config: MiniMaxConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L324`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L324) — Initialize the MiniMaxAttention module.
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`MiniMaxConfig`](minimax_configuration.md#MiniMaxConfig)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`attn_beta_factor`](modeling_minimax.md#MiniMaxDecoderLayer.attn_beta_factor)

### `MiniMaxDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/minimax/modeling_minimax.py:603`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L603)
- doc: Single decoder layer for MiniMax transformer models.
- signature: `class MiniMaxDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo, position_ids: Int[Array, "batch seq_len"], attention_mask: Bool[Array, "batch seq_len"] | None, mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RecurrentCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, output_router_logits: bool = False, frequencies: Array | None = None)` — [`L724`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L724) — Forward pass through the decoder layer.
  - `__init__(self, config: MiniMaxConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L652`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L652) — Initialize the MiniMaxDecoderLayer module.
  - `attn_alpha_factor` — [`L682`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L682)
  - `attn_beta_factor` — [`L683`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L683)
  - `block_sparse_moe` — [`L699`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L699)
  - `config` — [`L673`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L673)
  - `dtype` — [`L675`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L675)
  - `input_layernorm` — [`L707`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L707)
  - `layer_idx` — [`L674`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L674)
  - `layer_type` — [`L678`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L678)
  - `mlp_alpha_factor` — [`L721`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L721)
  - `mlp_beta_factor` — [`L722`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L722)
  - `param_dtype` — [`L676`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L676)
  - `post_attention_layernorm` — [`L714`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L714)
  - `precision` — [`L677`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L677)
  - `reform_param` — [`L625`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L625)
  - `self_attn` — [`L691`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L691)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`AttentionLayerOutput`](../../infra/modeling_outputs.md#AttentionLayerOutput), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`RecurrentCacheView`](../../caching/recurrent/cache.md#RecurrentCacheView), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`MiniMaxConfig`](minimax_configuration.md#MiniMaxConfig), [`hidden_size`](minimax_configuration.md#MiniMaxConfig.hidden_size), [`mlp_beta_factor`](minimax_configuration.md#MiniMaxConfig.mlp_beta_factor), [`layer_types`](minimax_configuration.md#MiniMaxConfig.layer_types), [`MiniMaxAttention`](modeling_minimax.md#MiniMaxAttention), [`rms_norm_eps`](minimax_configuration.md#MiniMaxConfig.rms_norm_eps), [`MiniMaxSparseMoeBlock`](modeling_minimax.md#MiniMaxSparseMoeBlock), [`MiniMaxLightningAttention`](modeling_minimax.md#MiniMaxLightningAttention), [`full_attn_alpha_factor`](minimax_configuration.md#MiniMaxConfig.full_attn_alpha_factor), [`full_attn_beta_factor`](minimax_configuration.md#MiniMaxConfig.full_attn_beta_factor), [`linear_attn_alpha_factor`](minimax_configuration.md#MiniMaxConfig.linear_attn_alpha_factor), [`linear_attn_beta_factor`](minimax_configuration.md#MiniMaxConfig.linear_attn_beta_factor), [`mlp_alpha_factor`](minimax_configuration.md#MiniMaxConfig.mlp_alpha_factor)
- used by: [`embed_tokens`](modeling_minimax.md#MiniMaxModel.embed_tokens)

### `MiniMaxExperts`  ·  implements/extends Module
- def: [`easydel/modules/minimax/modeling_minimax.py:358`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L358)
- doc: Expert feed-forward networks for MiniMax Mixture-of-Experts layers.
- signature: `class MiniMaxExperts(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "tokens hidden_dim"], group_sizes: Array, sorted_experts: Array | None = None)` — [`L456`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L456) — Forward pass through the expert networks.
  - `__init__(self, config: MiniMaxConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L393`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L393) — Initialize the MiniMaxExperts module.
  - `act_fn` — [`L454`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L454)
  - `config` — [`L412`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L412)
  - `dtype` — [`L413`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L413)
  - `param_dtype` — [`L414`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L414)
  - `precision` — [`L415`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L415)
  - `reform_param` — [`L376`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L376)
  - `w1` — [`L418`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L418)
  - `w2` — [`L430`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L430)
  - `w3` — [`L442`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L442)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`use_expert_tensor_mode`](../../infra/base_config.md#EasyDeLBaseConfig.use_expert_tensor_mode), [`ColumnParallelMoELinear`](../../layers/linears/_linear_moe.md#ColumnParallelMoELinear), [`RowParallelMoELinear`](../../layers/linears/_linear_moe.md#RowParallelMoELinear), [`MiniMaxConfig`](minimax_configuration.md#MiniMaxConfig), [`hidden_size`](minimax_configuration.md#MiniMaxConfig.hidden_size), [`initializer_range`](minimax_configuration.md#MiniMaxConfig.initializer_range), [`num_local_experts`](minimax_configuration.md#MiniMaxConfig.num_local_experts), [`intermediate_size`](minimax_configuration.md#MiniMaxConfig.intermediate_size), [`hidden_act`](minimax_configuration.md#MiniMaxConfig.hidden_act)
- used by: [`__call__`](modeling_minimax.md#MiniMaxSparseMoeBlock.__call__), [`experts`](modeling_minimax.md#MiniMaxSparseMoeBlock.experts)

### `MiniMaxForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/minimax/modeling_minimax.py:1085`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L1085)
- doc: MiniMax model with a causal language modeling head.
- signature: `class MiniMaxForCausalLM(BaseCausalLMModule[MiniMaxModel, MiniMaxConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True)` — [`L1135`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L1135) — Forward pass for causal language modeling.
  - `__init__(self, config: MiniMaxConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1104`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L1104) — Initialize the MiniMaxForCausalLM model.
  - `create_recurrent_cache_config(self, batch_size: int)` — [`L1226`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L1226) — Create configuration for recurrent cache used in lightning attention layers.
  - `get_inference_cache_type(self)` — [`L1201`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L1201) — Get the cache type used for inference.
  - `get_operations_cache_view(self)` — [`L1210`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L1210) — Get the cache view type for each layer.
- protocol/private: `_config_class`[`L1102`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L1102), `_model_type`[`L1101`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L1101), `_task_type`[`L1100`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L1100)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`RecurrentCacheView`](../../caching/recurrent/cache.md#RecurrentCacheView), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`MoeCausalLMOutput`](../../infra/modeling_outputs.md#MoeCausalLMOutput), [`RecurrentCacheConfig`](../../caching/recurrent/cache.md#RecurrentCacheConfig), [`forward_moe`](../_base/causal_lm_module.md#BaseCausalLMModule.forward_moe), [`MiniMaxConfig`](minimax_configuration.md#MiniMaxConfig), [`MiniMaxModel`](modeling_minimax.md#MiniMaxModel), [`create`](../../caching/recurrent/cache.md#RecurrentCacheConfig.create), [`router_aux_loss_coef`](minimax_configuration.md#MiniMaxConfig.router_aux_loss_coef)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_operations_cache_view`](../../infra/mixins/operation_cache.md#OperationCacheMixin.get_operations_cache_view), [`create_recurrent_cache_config`](../../infra/mixins/generation.md#EasyGenerationMixin.create_recurrent_cache_config), [`get_inference_cache_type`](../../infra/mixins/generation.md#EasyGenerationMixin.get_inference_cache_type)

### `MiniMaxLightningAttention`  ·  implements/extends Module
- def: [`easydel/modules/minimax/modeling_minimax.py:60`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L60)
- doc: Lightning Attention module for MiniMax models.
- signature: `class MiniMaxLightningAttention(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], attention_mask: Bool[Array, "batch seq_len"] | None, mode: common_types.RUNTIME_MODE_TYPES, cache_view: RecurrentCacheView | None = None)` — [`L188`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L188) — Perform lightning attention forward pass.
  - `__init__(self, config: MiniMaxConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L78`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L78) — Initialize the MiniMaxLightningAttention module.
  - `_decay_factors(self, slope_rate: Array)` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L162) — Compute decay factors for block-wise attention computation.
  - `_get_slope_rate(self)` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L147) — Compute the slope rate for exponential decay in attention.
  - `act_fn` — [`L107`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L107)
  - `block_size` — [`L106`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L106)
  - `config` — [`L100`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L100)
  - `head_dim` — [`L105`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L105)
  - `hidden_size` — [`L102`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L102)
  - `layer_idx` — [`L101`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L101)
  - `norm` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L139)
  - `num_attention_heads` — [`L103`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L103)
  - `num_hidden_layers` — [`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L104)
  - `out_proj` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L119)
  - `output_gate` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L129)
  - `qkv_proj` — [`L109`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L109)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`RecurrentCacheView`](../../caching/recurrent/cache.md#RecurrentCacheView), [`recurrent_state`](../../caching/recurrent/cache.md#RecurrentCacheView.recurrent_state), [`MiniMaxConfig`](minimax_configuration.md#MiniMaxConfig), [`hidden_size`](minimax_configuration.md#MiniMaxConfig.hidden_size), [`update_recurrent_state`](../../caching/recurrent/cache.md#RecurrentCacheView.update_recurrent_state), [`initializer_range`](minimax_configuration.md#MiniMaxConfig.initializer_range), [`num_hidden_layers`](minimax_configuration.md#MiniMaxConfig.num_hidden_layers), [`rms_norm_eps`](minimax_configuration.md#MiniMaxConfig.rms_norm_eps), [`hidden_act`](minimax_configuration.md#MiniMaxConfig.hidden_act), [`num_attention_heads`](minimax_configuration.md#MiniMaxConfig.num_attention_heads), [`block_size`](minimax_configuration.md#MiniMaxConfig.block_size)
- used by: [`layer_type`](modeling_minimax.md#MiniMaxDecoderLayer.layer_type)

### `MiniMaxModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/minimax/modeling_minimax.py:819`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L819)
- doc: Base transformer model for MiniMax architecture.
- signature: `class MiniMaxModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None)` — [`L900`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L900) — Forward pass through the MiniMax model.
  - `__init__(self, config: MiniMaxConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L836`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L836) — Initialize the MiniMaxModel.
  - `get_decoder(self)` — [`L1057`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L1057) — Get the decoder module.
  - `get_embedding(self)` — [`L1073`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L1073) — Get the token embedding layer.
  - `get_encoder(self)` — [`L1049`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L1049) — Get the encoder module.
  - `get_lm_head(self)` — [`L1065`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L1065) — Get the language model head.
  - `embed_tokens` — [`L863`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L863)
  - `layers` — [`L878`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L878)
  - `norm` — [`L892`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L892)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`MoeModelOutput`](../../infra/modeling_outputs.md#MoeModelOutput), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), `output_hidden_states`, [`views`](../../caching/hybrid/cache.md#HybridCache.views), [`gradient_checkpointing`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing), [`auxiliary_load_balancing_loss_func`](../../infra/loss_utils.md#auxiliary_load_balancing_loss_func), [`router_logits`](../../infra/modeling_outputs.md#DecoderLayerOutput.router_logits), [`MiniMaxConfig`](minimax_configuration.md#MiniMaxConfig), [`num_local_experts`](../../infra/base_config.md#EasyDeLBaseConfig.num_local_experts), [`hidden_size`](minimax_configuration.md#MiniMaxConfig.hidden_size), [`initializer_range`](minimax_configuration.md#MiniMaxConfig.initializer_range), [`num_hidden_layers`](minimax_configuration.md#MiniMaxConfig.num_hidden_layers), [`init_empty`](../../caching/hybrid/cache.md#HybridCache.init_empty), [`rms_norm_eps`](minimax_configuration.md#MiniMaxConfig.rms_norm_eps), [`MiniMaxDecoderLayer`](modeling_minimax.md#MiniMaxDecoderLayer), [`vocab_size`](minimax_configuration.md#MiniMaxConfig.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`MiniMaxForCausalLM`](modeling_minimax.md#MiniMaxForCausalLM), [`__init__`](modeling_minimax.md#MiniMaxForCausalLM.__init__)

### `MiniMaxSparseMoeBlock`  ·  implements/extends BaseMoeModule
- def: [`easydel/modules/minimax/modeling_minimax.py:483`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L483)
- doc: Sparse Mixture-of-Experts block for MiniMax models.
- signature: `class MiniMaxSparseMoeBlock(BaseMoeModule):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], training: bool = False, layer_idx: int | None = None)` — [`L561`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L561) — Forward pass through the sparse MoE block.
  - `__init__(self, config: MiniMaxConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L500`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L500) — Initialize the MiniMaxSparseMoeBlock module.
  - `config` — [`L530`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L530)
  - `dtype` — [`L531`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L531)
  - `experts` — [`L546`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L546)
  - `gate` — [`L536`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L536)
  - `jitter_noise` — [`L559`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L559)
  - `param_dtype` — [`L532`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L532)
  - `precision` — [`L533`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L533)
  - `rngs` — [`L534`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L534)
- protocol/private: `_normalize_weights`[`L554`](../../../../../../../raw/code/EasyDeL/easydel/modules/minimax/modeling_minimax.py#L554)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`kernel`](../../layers/linears/_linear_moe.md#ParallelMoELinear.kernel), [`MoeRoutingStrategy`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy), [`moe_call`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_call), [`MoeLoadBalancingStrategy`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy), [`__init__`](../../layers/moe/_moe_module.md#BaseMoeModule.__init__), [`moe_hooks`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_hooks), [`MiniMaxConfig`](minimax_configuration.md#MiniMaxConfig), [`TOP_K`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy.TOP_K), [`STANDARD`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy.STANDARD), [`w1`](modeling_minimax.md#MiniMaxExperts.w1), [`w2`](modeling_minimax.md#MiniMaxExperts.w2), [`w3`](modeling_minimax.md#MiniMaxExperts.w3), [`hidden_size`](minimax_configuration.md#MiniMaxConfig.hidden_size), [`replace`](../../layers/moe/_communication_utils.md#MoeFusedHooks.replace), [`act_fn`](modeling_minimax.md#MiniMaxExperts.act_fn), [`initializer_range`](minimax_configuration.md#MiniMaxConfig.initializer_range), [`num_local_experts`](minimax_configuration.md#MiniMaxConfig.num_local_experts), [`MiniMaxExperts`](modeling_minimax.md#MiniMaxExperts), [`num_experts_per_tok`](minimax_configuration.md#MiniMaxConfig.num_experts_per_tok), [`router_jitter_noise`](minimax_configuration.md#MiniMaxConfig.router_jitter_noise)
- used by: [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`attn_beta_factor`](modeling_minimax.md#MiniMaxDecoderLayer.attn_beta_factor)

