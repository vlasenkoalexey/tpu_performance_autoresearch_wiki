---
title: 'Module: easydel/modules/gidd/modeling_gidd.py'
type: catalog
provenance: extracted
module: easydel/modules/gidd/modeling_gidd.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.gidd.modeling_gidd`/Gidd
symbols:
  GiddAttention.__call__: Attention#__call__().
  GiddModel.__call__: Model#__call__().
  GiddLayer.__call__: Layer#__call__().
  GiddForDiffusionLM.__call__: ForDiffusionLM#__call__().
  GiddAttention.qk_scale: Attention#qk_scale.
  GiddModel.embed_tokens: Model#embed_tokens.
  GiddAttention.concatenate: Attention#concatenate().
  GiddModel: Model#
  GiddForDiffusionLM: ForDiffusionLM#
  GiddAttention.qk_norm_eps: Attention#qk_norm_eps.
  GiddForDiffusionLM.lm_head: ForDiffusionLM#lm_head.
  GiddMLP.precision: MLP#precision.
  GiddAttention.attention_performer: Attention#attention_performer.
  GiddRMSNorm.kernel: RMSNorm#kernel.
  GiddMLP.__call__: MLP#__call__().
  GiddAttention.head_dim: Attention#head_dim.
  GiddAttention.q_proj: Attention#q_proj.
  GiddAttention.k_proj: Attention#k_proj.
  GiddAttention.v_proj: Attention#v_proj.
  GiddAttention.o_proj: Attention#o_proj.
  GiddAttention.rotary: Attention#rotary.
  GiddRMSNorm.__call__: RMSNorm#__call__().
  GiddModel.layers: Model#layers.
  GiddMLP.up_proj: MLP#up_proj.
  GiddMLP.down_proj: MLP#down_proj.
  GiddRMSNorm.epsilon: RMSNorm#epsilon.
  GiddModel.resid_scale: Model#resid_scale.
  GiddAttention.use_qk_norm: Attention#use_qk_norm.
  GiddForDiffusionLM.model: ForDiffusionLM#model.
  GiddAttention.__init__: Attention#__init__().
  GiddAttention.hidden_size: Attention#hidden_size.
  GiddAttention.craft_sharding: Attention#craft_sharding().
  GiddModel.__init__: Model#__init__().
  GiddForDiffusionLM.__init__: ForDiffusionLM#__init__().
  GiddForDiffusionLM.get_embedding: ForDiffusionLM#get_embedding().
  GiddAttention: Attention#
  GiddAttention._norm: Attention#_norm().
  GiddLayer.mlp: Layer#mlp.
  GiddMLP.config: MLP#config.
  GiddAttention.dtype: Attention#dtype.
  GiddAttention.init_attention_bias: Attention#init_attention_bias().
  GiddLayer.self_attn: Layer#self_attn.
  GiddLayer.input_layernorm: Layer#input_layernorm.
  GiddLayer.post_attention_layernorm: Layer#post_attention_layernorm.
  GiddModel.norm: Model#norm.
  GiddRMSNorm: RMSNorm#
  GiddLayer.config: Layer#config.
  GiddMLP.__init__: MLP#__init__().
  GiddRMSNorm.__init__: RMSNorm#__init__().
  GiddLayer.__init__: Layer#__init__().
  GiddModel.get_embedding: Model#get_embedding().
  GiddForDiffusionLM.get_decoder: ForDiffusionLM#get_decoder().
  GiddForDiffusionLM.get_lm_head: ForDiffusionLM#get_lm_head().
  GiddMLP: MLP#
  GiddAttention.param_dtype: Attention#param_dtype.
  GiddRMSNorm.config: RMSNorm#config.
  GiddRMSNorm.dtype: RMSNorm#dtype.
  GiddLayer.resid_scale: Layer#resid_scale.
  GiddLayer: Layer#
  GiddMLP.dtype: MLP#dtype.
  GiddMLP.param_dtype: MLP#param_dtype.
  GiddAttention.precision: Attention#precision.
  GiddAttention.rngs: Attention#rngs.
  GiddRMSNorm.kernel_init: RMSNorm#kernel_init.
  GiddRMSNorm.param_dtype: RMSNorm#param_dtype.
  GiddLayer.dtype: Layer#dtype.
  GiddLayer.param_dtype: Layer#param_dtype.
  GiddLayer.precision: Layer#precision.
  GiddModel.get_encoder: Model#get_encoder().
  GiddModel.get_decoder: Model#get_decoder().
  GiddModel.get_lm_head: Model#get_lm_head().
  GiddForDiffusionLM.get_encoder: ForDiffusionLM#get_encoder().
---
# Module: [`easydel/modules/gidd/modeling_gidd.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py)

## Classes
### `GiddAttention`  ·  implements/extends AttentionModule
- def: [`easydel/modules/gidd/modeling_gidd.py:146`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L146)
- doc: Multi-head attention layer with RoPE embeddings and optional QK normalization for GIDD models.
- signature: `class GiddAttention(AttentionModule):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo, noise_mask: Array, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L334`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L334) — Forward pass through the attention module.
  - `__init__(self, config: GiddConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L152`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L152) — Initialize GIDD attention layer with optional query-key normalization.
  - `_norm(self, x: jnp.ndarray)` — [`L323`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L323) — Apply L2 normalization to query or key vectors.
  - `concatenate(self, *, query: Array, key: Array, value: Array, mask_info: MaskInfo, noise_mask: Array | None, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None)` — [`L257`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L257) — Prepare and concatenate key, value, and attention mask for attention computation.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L251`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L251)
  - `init_attention_bias()` — [`L314`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L314)
  - `attention_performer` — [`L245`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L245)
  - `dtype` — [`L171`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L171)
  - `head_dim` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L179)
  - `hidden_size` — [`L175`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L175)
  - `k_proj` — [`L226`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L226)
  - `o_proj` — [`L236`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L236)
  - `param_dtype` — [`L172`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L172)
  - `precision` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L173)
  - `q_proj` — [`L221`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L221)
  - `qk_norm_eps` — [`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L183)
  - `qk_scale` — [`L191`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L191)
  - `rngs` — [`L174`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L174)
  - `rotary` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L238)
  - `use_qk_norm` — [`L182`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L182)
  - `v_proj` — [`L231`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L231)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ArrayParam`](../../infra/utils.md#ArrayParam), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`config`](../../layers/attention/_flexible.md#AttentionModule.config), [`forward`](../../layers/attention/_flexible.md#FlexibleAttentionModule.forward), [`AttentionLayerOutput`](../../infra/modeling_outputs.md#AttentionLayerOutput), [`bound`](../../infra/utils.md#ArrayParam.bound), [`attention_outputs`](../../operations/_attention_outputs.md#AttentionOutput.attention_outputs), [`AttentionModule`](../../layers/attention/_flexible.md#AttentionModule), [`shard_attention_prod`](../../layers/attention/_flexible.md#AttentionModule.shard_attention_prod), [`apply_qkv_shardings`](../../layers/attention/_flexible.md#AttentionModule.apply_qkv_shardings), [`attention_weights`](../../operations/_attention_outputs.md#AttentionOutput.attention_weights), [`_merge_heads`](../../layers/attention/_flexible.md#AttentionModule._merge_heads), [`GiddConfig`](gidd_configuration.md#GiddConfig), [`__init__`](../../layers/attention/_flexible.md#AttentionModule.__init__), [`hidden_size`](gidd_configuration.md#GiddConfig.hidden_size), [`num_attention_heads`](gidd_configuration.md#GiddConfig.num_attention_heads), [`init_scale`](gidd_configuration.md#GiddConfig.init_scale), [`attention_bias`](gidd_configuration.md#GiddConfig.attention_bias), [`max_position_embeddings`](gidd_configuration.md#GiddConfig.max_position_embeddings), [`qk_norm_eps`](gidd_configuration.md#GiddConfig.qk_norm_eps), [`use_qk_norm`](gidd_configuration.md#GiddConfig.use_qk_norm)
- used by: [`concatenate`](../../layers/attention/_flexible.md#AttentionModule.concatenate), [`AttentionModule`](../../layers/attention/_flexible.md#AttentionModule), [`self_attn`](modeling_gidd.md#GiddLayer.self_attn)

### `GiddForDiffusionLM`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/gidd/modeling_gidd.py:874`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L874)
- doc: GIDD model with a language modeling head for diffusion language modeling tasks.
- signature: `class GiddForDiffusionLM(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, log_snr: Array | None = None, noise_mask: Array | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L934`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L934) — Forward pass through the GIDD diffusion language model.
  - `__init__(self, config: GiddConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L887`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L887) — Initialize GIDD model for diffusion language modeling.
  - `get_decoder(self)` — [`L1028`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L1028) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L1044`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L1044) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L1018`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L1018) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L1036`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L1036) — Returns the language model head of the module.
  - `lm_head` — [`L923`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L923)
  - `model` — [`L914`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L914)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`CausalLMOutput`](../../infra/modeling_outputs.md#CausalLMOutput), [`last_hidden_state`](../../infra/modeling_outputs.md#BaseModelOutput.last_hidden_state), [`attentions`](../../infra/modeling_outputs.md#BaseModelOutput.attentions), [`hidden_states`](../../infra/modeling_outputs.md#BaseModelOutput.hidden_states), [`embed_tokens`](modeling_gidd.md#GiddModel.embed_tokens), [`GiddConfig`](gidd_configuration.md#GiddConfig), [`GiddModel`](modeling_gidd.md#GiddModel), [`past_key_values`](../../infra/modeling_outputs.md#BaseModelOutput.past_key_values), [`hidden_size`](gidd_configuration.md#GiddConfig.hidden_size), [`precision`](../../infra/base_module.md#EasyDeLBaseModule.precision), [`DIFFUSION_LM`](../../infra/factory.md#TaskType.DIFFUSION_LM), [`head_init_scale`](gidd_configuration.md#GiddConfig.head_init_scale), [`vocab_size`](gidd_configuration.md#GiddConfig.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder)

### `GiddLayer`  ·  implements/extends Module
- def: [`easydel/modules/gidd/modeling_gidd.py:501`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L501)
- doc: Single transformer layer for GIDD models.
- signature: `class GiddLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo, position_ids: Int[Array, "batch seq_len"], noise_mask: Array, mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L551`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L551) — Forward pass through the transformer layer.
  - `__init__(self, config: GiddConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, resid_scale: float = 1)` — [`L508`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L508) — Initialize GIDD transformer layer.
  - `config` — [`L528`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L528)
  - `dtype` — [`L529`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L529)
  - `input_layernorm` — [`L548`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L548)
  - `mlp` — [`L541`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L541)
  - `param_dtype` — [`L530`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L530)
  - `post_attention_layernorm` — [`L549`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L549)
  - `precision` — [`L531`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L531)
  - `resid_scale` — [`L532`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L532)
  - `self_attn` — [`L534`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L534)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`GiddConfig`](gidd_configuration.md#GiddConfig), [`GiddAttention`](modeling_gidd.md#GiddAttention), [`GiddRMSNorm`](modeling_gidd.md#GiddRMSNorm), [`GiddMLP`](modeling_gidd.md#GiddMLP)
- used by: [`embed_tokens`](modeling_gidd.md#GiddModel.embed_tokens)

### `GiddMLP`  ·  implements/extends Module
- def: [`easydel/modules/gidd/modeling_gidd.py:62`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L62)
- doc: Multi-Layer Perceptron module for GIDD models.
- signature: `class GiddMLP(nn.Module):`
- members:
  - `__call__(self, h: jnp.ndarray)` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L117) — Apply squared ReLU feedforward transformation.
  - `__init__(self, config: GiddConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L69`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L69) — Initialize GIDD MLP block.
  - `config` — [`L88`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L88)
  - `down_proj` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L115)
  - `dtype` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L89)
  - `param_dtype` — [`L90`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L90)
  - `precision` — [`L91`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L91)
  - `up_proj` — [`L114`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L114)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`GiddConfig`](gidd_configuration.md#GiddConfig), [`hidden_size`](gidd_configuration.md#GiddConfig.hidden_size), [`init_scale`](gidd_configuration.md#GiddConfig.init_scale), [`mlp_bias`](gidd_configuration.md#GiddConfig.mlp_bias), [`intermediate_size`](gidd_configuration.md#GiddConfig.intermediate_size)
- used by: [`mlp`](modeling_gidd.md#GiddLayer.mlp)

### `GiddModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/gidd/modeling_gidd.py:624`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L624)
- doc: GIDD model implementation for diffusion language modeling.
- signature: `class GiddModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, log_snr: Array | None = None, noise_mask: Array | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L697`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L697) — Forward pass through the GIDD base model.
  - `__init__(self, config: GiddConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L637`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L637) — Initialize GIDD base model.
  - `get_decoder(self)` — [`L846`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L846) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L864`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L864) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L836`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L836) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L854`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L854) — Returns the language model head of the module.
  - `embed_tokens` — [`L666`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L666)
  - `layers` — [`L681`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L681)
  - `norm` — [`L695`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L695)
  - `resid_scale` — [`L664`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L664)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`GiddConfig`](gidd_configuration.md#GiddConfig), [`GiddRMSNorm`](modeling_gidd.md#GiddRMSNorm), [`gradient_checkpointing`](gidd_configuration.md#GiddConfig.gradient_checkpointing), [`num_hidden_layers`](gidd_configuration.md#GiddConfig.num_hidden_layers), [`GiddLayer`](modeling_gidd.md#GiddLayer), [`resid_scale`](gidd_configuration.md#GiddConfig.resid_scale)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`model`](modeling_gidd.md#GiddForDiffusionLM.model), [`get_embedding`](modeling_gidd.md#GiddForDiffusionLM.get_embedding)

### `GiddRMSNorm`  ·  implements/extends Module
- def: [`easydel/modules/gidd/modeling_gidd.py:449`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L449)
- doc: Root Mean Square Layer Normalization for GIDD models.
- signature: `class GiddRMSNorm(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L481`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L481) — Apply RMSNorm to the input tensor.
  - `__init__(self, config: GiddConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16)` — [`L457`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L457) — Initialize GIDD RMSNorm layer.
  - `config` — [`L470`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L470)
  - `dtype` — [`L472`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L472)
  - `epsilon` — [`L471`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L471)
  - `kernel` — [`L474`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L474)
  - `kernel_init` — [`L455`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L455)
  - `param_dtype` — [`L473`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/modeling_gidd.py#L473)
- uses (calls/refs, reference-scoped): [`ArrayParam`](../../infra/utils.md#ArrayParam), [`bound`](../../infra/utils.md#ArrayParam.bound), [`GiddConfig`](gidd_configuration.md#GiddConfig), [`hidden_size`](gidd_configuration.md#GiddConfig.hidden_size), [`rms_norm_eps`](gidd_configuration.md#GiddConfig.rms_norm_eps)
- used by: [`input_layernorm`](modeling_gidd.md#GiddLayer.input_layernorm), [`norm`](modeling_gidd.md#GiddModel.norm), [`post_attention_layernorm`](modeling_gidd.md#GiddLayer.post_attention_layernorm)

