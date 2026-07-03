---
title: 'Module: easydel/modules/stablelm/modeling_stablelm.py'
type: catalog
provenance: extracted
module: easydel/modules/stablelm/modeling_stablelm.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.stablelm.modeling_stablelm`/StableLm
symbols:
  StableLmAttention.__call__: Attention#__call__().
  StableLmDecoderLayer.__call__: DecoderLayer#__call__().
  StableLmModel.__call__: Model#__call__().
  StableLmForCausalLM.__call__: ForCausalLM#__call__().
  StableLmModel.embed_tokens: Model#embed_tokens.
  StableLmForCausalLM: ForCausalLM#
  StableLmModel: Model#
  StableLmMLP.__call__: MLP#__call__().
  StableLmAttention.head_dim: Attention#head_dim.
  StableLmAttention.rotary_emb_dim: Attention#rotary_emb_dim.
  StableLmDecoderLayer.input_layernorm: DecoderLayer#input_layernorm.
  StableLmDecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  StableLmModel.norm: Model#norm.
  StableLmDecoderLayer.config: DecoderLayer#config.
  StableLmMLP.precision: MLP#precision.
  StableLmAttention._create_q_norm: Attention#_create_q_norm().
  StableLmAttention._create_k_norm: Attention#_create_k_norm().
  StableLmForCausalLM.__init__: ForCausalLM#__init__().
  StableLmDecoderLayer.use_parallel_residual: DecoderLayer#use_parallel_residual.
  StableLmDecoderLayer.dropout: DecoderLayer#dropout.
  StableLmDecoderLayer.mlp: DecoderLayer#mlp.
  StableLmMLP.gate_proj: MLP#gate_proj.
  StableLmMLP.down_proj: MLP#down_proj.
  StableLmMLP.up_proj: MLP#up_proj.
  StableLmMLP.act_fn: MLP#act_fn.
  StableLmAttention.qk_layernorm: Attention#qk_layernorm.
  StableLmAttention._create_rotary: Attention#_create_rotary().
  StableLmModel.__init__: Model#__init__().
  StableLmModel._frequencies: Model#_frequencies.
  StableLmForCausalLM._task_type: ForCausalLM#_task_type.
  StableLmModel.layers: Model#layers.
  StableLmLayerNormPerHead.norms: LayerNormPerHead#norms.
  StableLmAttention: Attention#
  StableLmDecoderLayer.self_attn: DecoderLayer#self_attn.
  StableLmModel.frequencies: Model#frequencies().
  StableLmMLP.__init__: MLP#__init__().
  StableLmLayerNormPerHead.__call__: LayerNormPerHead#__call__().
  StableLmAttention.__init__: Attention#__init__().
  StableLmAttention.partial_rotary_factor: Attention#partial_rotary_factor.
  StableLmDecoderLayer.__init__: DecoderLayer#__init__().
  StableLmModel.padding_idx: Model#padding_idx.
  StableLmModel.vocab_size: Model#vocab_size.
  StableLmModel.get_embedding: Model#get_embedding().
  StableLmForCausalLM._config_class: ForCausalLM#_config_class.
  StableLmMLP.config: MLP#config.
  StableLmLayerNormPerHead: LayerNormPerHead#
  StableLmMLP: MLP#
  StableLmDecoderLayer: DecoderLayer#
  StableLmMLP.dtype: MLP#dtype.
  StableLmMLP.param_dtype: MLP#param_dtype.
  StableLmLayerNormPerHead.__init__: LayerNormPerHead#__init__().
  StableLmAttention.norms_mapping: Attention#norms_mapping.
  StableLmDecoderLayer.dtype: DecoderLayer#dtype.
  StableLmDecoderLayer.param_dtype: DecoderLayer#param_dtype.
  StableLmDecoderLayer.precision: DecoderLayer#precision.
  StableLmModel.get_encoder: Model#get_encoder().
  StableLmModel.get_decoder: Model#get_decoder().
  StableLmModel.get_lm_head: Model#get_lm_head().
  StableLmForCausalLM._model_type: ForCausalLM#_model_type.
  StableLmForCausalLM.get_encoder: ForCausalLM#get_encoder().
  StableLmForCausalLM.get_decoder: ForCausalLM#get_decoder().
  StableLmForCausalLM.get_lm_head: ForCausalLM#get_lm_head().
  StableLmForCausalLM.get_embedding: ForCausalLM#get_embedding().
---
# Module: [`easydel/modules/stablelm/modeling_stablelm.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py)

## Classes
### `StableLmAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/stablelm/modeling_stablelm.py:205`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L205)
- doc: Multi-head attention layer with Q/K normalization for StableLM models.
- signature: `class StableLmAttention(UnifiedAttention):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L318`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L318) — Forward pass through the attention layer with optional Q/K normalization.
  - `__init__(self, config: StableLmConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L217`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L217) — Initialize StableLM attention layer with optional Q/K normalization.
  - `_create_k_norm(self, config, dtype, param_dtype, rngs)` — [`L278`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L278) — Create key normalization layer using per-head LayerNorm.
  - `_create_q_norm(self, config, dtype, param_dtype, rngs)` — [`L255`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L255) — Create query normalization layer using per-head LayerNorm.
  - `_create_rotary(self, config, dtype)` — [`L301`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L301) — Create partial rotary position embeddings.
  - `head_dim` — [`L240`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L240)
  - `norms_mapping` — [`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L212)
  - `partial_rotary_factor` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L238)
  - `qk_layernorm` — [`L237`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L237)
  - `rotary_emb_dim` — [`L241`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L241)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`config`](../../layers/attention/_flexible.md#AttentionModule.config), [`forward`](../../layers/attention/_flexible.md#FlexibleAttentionModule.forward), [`AttentionLayerOutput`](../../infra/modeling_outputs.md#AttentionLayerOutput), [`concatenate`](../../layers/attention/_flexible.md#AttentionModule.concatenate), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`attention_outputs`](../../operations/_attention_outputs.md#AttentionOutput.attention_outputs), [`attention_performer`](../../layers/attention/_unified.md#UnifiedAttention.attention_performer), [`get_basic_rope`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_rope), [`shard_attention_prod`](../../layers/attention/_flexible.md#AttentionModule.shard_attention_prod), [`_merge_heads`](../../layers/attention/_unified.md#UnifiedAttention._merge_heads), [`apply_qkv_shardings`](../../layers/attention/_flexible.md#AttentionModule.apply_qkv_shardings), [`attention_weights`](../../operations/_attention_outputs.md#AttentionOutput.attention_weights), [`key_normalization`](../../layers/attention/_unified.md#UnifiedAttention.key_normalization), [`query_normalization`](../../layers/attention/_unified.md#UnifiedAttention.query_normalization), [`StableLmConfig`](stablelm_configuration.md#StableLmConfig), [`output_projection`](../../layers/attention/_unified.md#UnifiedAttention.output_projection), [`_apply_rotary`](../../layers/attention/_unified.md#UnifiedAttention._apply_rotary), [`query_projection`](../../layers/attention/_unified.md#UnifiedAttention.query_projection), [`key_projection`](../../layers/attention/_unified.md#UnifiedAttention.key_projection), [`value_projection`](../../layers/attention/_unified.md#UnifiedAttention.value_projection), [`hidden_size`](stablelm_configuration.md#StableLmConfig.hidden_size), [`StableLmLayerNormPerHead`](modeling_stablelm.md#StableLmLayerNormPerHead), [`partial_rotary_factor`](stablelm_configuration.md#StableLmConfig.partial_rotary_factor), [`qk_layernorm`](stablelm_configuration.md#StableLmConfig.qk_layernorm), [`num_attention_heads`](stablelm_configuration.md#StableLmConfig.num_attention_heads)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`_create_k_norm`](../../layers/attention/_unified.md#UnifiedAttention._create_k_norm), [`_create_q_norm`](../../layers/attention/_unified.md#UnifiedAttention._create_q_norm), [`self_attn`](modeling_stablelm.md#StableLmDecoderLayer.self_attn)

### `StableLmDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/stablelm/modeling_stablelm.py:422`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L422)
- doc: Single decoder layer for StableLM models.
- signature: `class StableLmDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L487`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L487) — Forward pass through the decoder layer.
  - `__init__(self, config: StableLmConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L429`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L429) — Initialize StableLM decoder layer.
  - `config` — [`L449`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L449)
  - `dropout` — [`L485`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L485)
  - `dtype` — [`L450`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L450)
  - `input_layernorm` — [`L470`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L470) — documented in [easydel-layers-norms-_norms](../../../../concepts/easydel-layers-norms-_norms.md)
  - `mlp` — [`L462`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L462)
  - `param_dtype` — [`L451`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L451)
  - `post_attention_layernorm` — [`L478`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L478)
  - `precision` — [`L452`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L452)
  - `self_attn` — [`L454`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L454)
  - `use_parallel_residual` — [`L453`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L453)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`StableLmConfig`](stablelm_configuration.md#StableLmConfig), [`hidden_size`](stablelm_configuration.md#StableLmConfig.hidden_size), [`StableLmAttention`](modeling_stablelm.md#StableLmAttention), [`layer_norm_eps`](stablelm_configuration.md#StableLmConfig.layer_norm_eps), [`StableLmMLP`](modeling_stablelm.md#StableLmMLP), [`hidden_dropout`](stablelm_configuration.md#StableLmConfig.hidden_dropout), [`use_parallel_residual`](stablelm_configuration.md#StableLmConfig.use_parallel_residual)
- used by: [`embed_tokens`](modeling_stablelm.md#StableLmModel.embed_tokens)

### `StableLmForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/stablelm/modeling_stablelm.py:812`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L812)
- doc: StableLM model with a language modeling head for causal language modeling tasks.
- signature: `class StableLmForCausalLM(BaseCausalLMModule[StableLmModel, StableLmConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True)` — [`L858`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L858) — Forward pass through the StableLM model for causal language modeling.
  - `__init__(self, config: StableLmConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L829`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L829) — Initialize StableLM model for causal language modeling.
  - `get_decoder(self)` — [`L942`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L942) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L954`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L954) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L935`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L935) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L948`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L948) — Returns the language model head of the module.
- protocol/private: `_config_class`[`L827`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L827), `_model_type`[`L826`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L826), `_task_type`[`L825`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L825)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`CausalLMOutput`](../../infra/modeling_outputs.md#CausalLMOutput), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`compute_lm_logits`](../_base/causal_lm_module.md#BaseCausalLMModule.compute_lm_logits), [`StableLmConfig`](stablelm_configuration.md#StableLmConfig), [`StableLmModel`](modeling_stablelm.md#StableLmModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.get_lm_head)

### `StableLmLayerNormPerHead`  ·  implements/extends Module
- def: [`easydel/modules/stablelm/modeling_stablelm.py:144`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L144)
- doc: Layer normalization applied independently to each attention head.
- signature: `class StableLmLayerNormPerHead(nn.Module):`
- members:
  - `__call__(self, hidden_states)` — [`L187`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L187) — Apply layer normalization independently to each head.
  - `__init__(self, head_dim: int, num_heads: int, eps: float = 0.00001, bias: bool = False, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, *, rngs: nn.Rngs)` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L151) — Initialize per-head layer normalization.
  - `norms` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L173)
- uses (calls/refs, reference-scoped): [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm)
- used by: [`_create_k_norm`](modeling_stablelm.md#StableLmAttention._create_k_norm), [`_create_q_norm`](modeling_stablelm.md#StableLmAttention._create_q_norm)

### `StableLmMLP`  ·  implements/extends Module
- def: [`easydel/modules/stablelm/modeling_stablelm.py:50`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L50)
- doc: Multi-Layer Perceptron module for StableLM models.
- signature: `class StableLmMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L116) — Apply SwiGLU feedforward transformation.
  - `__init__(self, config: StableLmConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L57`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L57) — Initialize StableLM MLP block.
  - `act_fn` — [`L114`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L114)
  - `config` — [`L78`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L78)
  - `down_proj` — [`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L104)
  - `dtype` — [`L79`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L79)
  - `gate_proj` — [`L99`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L99)
  - `param_dtype` — [`L80`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L80)
  - `precision` — [`L81`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L81)
  - `up_proj` — [`L109`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L109)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`StableLmConfig`](stablelm_configuration.md#StableLmConfig), [`hidden_size`](stablelm_configuration.md#StableLmConfig.hidden_size), [`intermediate_size`](stablelm_configuration.md#StableLmConfig.intermediate_size), [`initializer_range`](stablelm_configuration.md#StableLmConfig.initializer_range), [`hidden_act`](stablelm_configuration.md#StableLmConfig.hidden_act)
- used by: [`mlp`](modeling_stablelm.md#StableLmDecoderLayer.mlp)

### `StableLmModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/stablelm/modeling_stablelm.py:572`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L572)
- doc: StableLM base model implementation.
- signature: `class StableLmModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L664`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L664) — Forward pass through the StableLM base model.
  - `__init__(self, config: StableLmConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L585`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L585) — Initialize StableLM base model.
  - `frequencies(self)` — [`L650`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L650) — Precomputed partial rotary position embedding frequencies.
  - `get_decoder(self)` — [`L791`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L791) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L804`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L804) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L784`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L784) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L797`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L797) — Returns the language model head of the module.
  - `embed_tokens` — [`L614`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L614)
  - `layers` — [`L627`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L627)
  - `norm` — [`L641`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L641)
  - `padding_idx` — [`L611`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L611)
  - `vocab_size` — [`L612`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L612)
- protocol/private: `_frequencies`[`L659`](../../../../../../../raw/code/EasyDeL/easydel/modules/stablelm/modeling_stablelm.py#L659)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), `pad_token_id`, [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`get_basic_frequencies`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_frequencies), [`StableLmConfig`](stablelm_configuration.md#StableLmConfig), [`hidden_size`](stablelm_configuration.md#StableLmConfig.hidden_size), [`layer_norm_eps`](stablelm_configuration.md#StableLmConfig.layer_norm_eps), [`num_hidden_layers`](stablelm_configuration.md#StableLmConfig.num_hidden_layers), [`vocab_size`](stablelm_configuration.md#StableLmConfig.vocab_size), [`StableLmDecoderLayer`](modeling_stablelm.md#StableLmDecoderLayer), [`gradient_checkpointing`](stablelm_configuration.md#StableLmConfig.gradient_checkpointing)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`StableLmForCausalLM`](modeling_stablelm.md#StableLmForCausalLM), [`__init__`](modeling_stablelm.md#StableLmForCausalLM.__init__)

