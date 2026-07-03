---
title: 'Module: easydel/modules/qwen3/modeling_qwen3.py'
type: catalog
provenance: extracted
module: easydel/modules/qwen3/modeling_qwen3.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.qwen3.modeling_qwen3`/Qwen3
symbols:
  Qwen3Model.__call__: Model#__call__().
  Qwen3DecoderLayer.__call__: DecoderLayer#__call__().
  Qwen3Model.embed_tokens: Model#embed_tokens.
  Qwen3Model: Model#
  Qwen3ForCausalLM: ForCausalLM#
  Qwen3ForSequenceClassification: ForSequenceClassification#
  Qwen3ForEmbedding: ForEmbedding#
  Qwen3MLP.__call__: MLP#__call__().
  Qwen3DecoderLayer.input_layernorm: DecoderLayer#input_layernorm.
  Qwen3DecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  Qwen3Attention.__init__: Attention#__init__().
  Qwen3MLP.act_fn: MLP#act_fn.
  Qwen3Model.norm: Model#norm.
  Qwen3MLP.precision: MLP#precision.
  Qwen3ForCausalLM.__init__: ForCausalLM#__init__().
  Qwen3ForSequenceClassification.__init__: ForSequenceClassification#__init__().
  Qwen3ForEmbedding.__init__: ForEmbedding#__init__().
  Qwen3MLP.gate_proj: MLP#gate_proj.
  Qwen3MLP.down_proj: MLP#down_proj.
  Qwen3MLP.up_proj: MLP#up_proj.
  Qwen3Attention._postprocess_qkv: Attention#_postprocess_qkv().
  Qwen3DecoderLayer.config: DecoderLayer#config.
  Qwen3Model.__init__: Model#__init__().
  Qwen3Model.get_embedding: Model#get_embedding().
  Qwen3ForCausalLM._task_type: ForCausalLM#_task_type.
  Qwen3ForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  Qwen3ForEmbedding._task_type: ForEmbedding#_task_type.
  Qwen3DecoderLayer.mlp: DecoderLayer#mlp.
  Qwen3Model.layers: Model#layers.
  Qwen3Attention: Attention#
  Qwen3DecoderLayer.self_attn: DecoderLayer#self_attn.
  Qwen3MLP.config: MLP#config.
  Qwen3MLP.__init__: MLP#__init__().
  Qwen3DecoderLayer.__init__: DecoderLayer#__init__().
  Qwen3Model.get_decoder: Model#get_decoder().
  Qwen3ForCausalLM._config_class: ForCausalLM#_config_class.
  Qwen3ForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  Qwen3ForEmbedding._config_class: ForEmbedding#_config_class.
  Qwen3MLP: MLP#
  Qwen3DecoderLayer: DecoderLayer#
  Qwen3MLP.dtype: MLP#dtype.
  Qwen3MLP.param_dtype: MLP#param_dtype.
  Qwen3DecoderLayer.dtype: DecoderLayer#dtype.
  Qwen3DecoderLayer.param_dtype: DecoderLayer#param_dtype.
  Qwen3DecoderLayer.precision: DecoderLayer#precision.
  Qwen3Model.get_encoder: Model#get_encoder().
  Qwen3Model.get_lm_head: Model#get_lm_head().
  Qwen3ForCausalLM._model_type: ForCausalLM#_model_type.
  Qwen3ForSequenceClassification._model_type: ForSequenceClassification#_model_type.
  Qwen3ForEmbedding._model_type: ForEmbedding#_model_type.
---
# Module: [`easydel/modules/qwen3/modeling_qwen3.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py)

## Classes
### `Qwen3Attention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/qwen3/modeling_qwen3.py:143`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L143)
- doc: Multi-head attention layer with RoPE embeddings and Q/K normalization for Qwen3 models.
- signature: `class Qwen3Attention(UnifiedAttention):`
- members:
  - `__init__(self, config: Qwen3Config, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike | None = None, *, rngs: nn.Rngs)` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L150) — Initialize Qwen3 attention layer with grouped-query attention support.
  - `_postprocess_qkv(self, query_states, key_states, value_states)` — [`L185`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L185) — Apply Q/K normalization after computing query, key, and value projections.
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`Qwen3Config`](qwen3_configuration.md#Qwen3Config), [`layer_types`](qwen3_configuration.md#Qwen3Config.layer_types), [`key_normalization`](../../layers/attention/_unified.md#UnifiedAttention.key_normalization), [`query_normalization`](../../layers/attention/_unified.md#UnifiedAttention.query_normalization), [`sliding_window`](qwen3_configuration.md#Qwen3Config.sliding_window)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_postprocess_qkv`](../../layers/attention/_unified.md#UnifiedAttention._postprocess_qkv), [`self_attn`](modeling_qwen3.md#Qwen3DecoderLayer.self_attn)

### `Qwen3DecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/qwen3/modeling_qwen3.py:199`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L199)
- doc: Single decoder layer for Qwen3 models.
- signature: `class Qwen3DecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim//2 2"] | None = None)` — [`L261`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L261) — Forward pass through the decoder layer.
  - `__init__(self, config: Qwen3Config, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike | None = None, *, rngs: nn.Rngs)` — [`L206`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L206) — Initialize Qwen3 decoder layer.
  - `config` — [`L226`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L226)
  - `dtype` — [`L227`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L227)
  - `input_layernorm` — [`L246`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L246) — documented in [easydel-layers-norms-_norms](../../../../concepts/easydel-layers-norms-_norms.md)
  - `mlp` — [`L239`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L239)
  - `param_dtype` — [`L228`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L228)
  - `post_attention_layernorm` — [`L253`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L253)
  - `precision` — [`L229`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L229)
  - `self_attn` — [`L230`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L230)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`Qwen3Config`](qwen3_configuration.md#Qwen3Config), [`hidden_size`](qwen3_configuration.md#Qwen3Config.hidden_size), [`Qwen3Attention`](modeling_qwen3.md#Qwen3Attention), [`rms_norm_eps`](qwen3_configuration.md#Qwen3Config.rms_norm_eps), [`Qwen3MLP`](modeling_qwen3.md#Qwen3MLP)
- used by: [`embed_tokens`](modeling_qwen3.md#Qwen3Model.embed_tokens)

### `Qwen3ForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/qwen3/modeling_qwen3.py:561`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L561)
- doc: Qwen3 model with a language modeling head for causal language modeling tasks.
- signature: `class Qwen3ForCausalLM(BaseCausalLMModule[Qwen3Model, Qwen3Config]):`
- members:
  - `__init__(self, config: Qwen3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike | None = None, *, rngs: nn.Rngs)` — [`L578`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L578) — Initialize Qwen3 model for causal language modeling.
- protocol/private: `_config_class`[`L576`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L576), `_model_type`[`L575`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L575), `_task_type`[`L574`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L574)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`Qwen3Config`](qwen3_configuration.md#Qwen3Config), [`Qwen3Model`](modeling_qwen3.md#Qwen3Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `Qwen3ForEmbedding`  ·  implements/extends BaseEmbeddingModule
- def: [`easydel/modules/qwen3/modeling_qwen3.py:658`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L658)
- doc: Qwen3 model for text embedding and similarity tasks.
- signature: `class Qwen3ForEmbedding(BaseEmbeddingModule[Qwen3Model, Qwen3Config]):`
- members:
  - `__init__(self, config: Qwen3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike | None = None, *, rngs: nn.Rngs)` — [`L678`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L678) — Initialize Qwen3 embedding model.
- protocol/private: `_config_class`[`L676`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L676), `_model_type`[`L675`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L675), `_task_type`[`L674`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L674)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`Qwen3Config`](qwen3_configuration.md#Qwen3Config), [`Qwen3Model`](modeling_qwen3.md#Qwen3Model), [`BaseEmbeddingModule`](../_base/embedding_module.md#BaseEmbeddingModule), [`EMBEDDING`](../../infra/factory.md#TaskType.EMBEDDING), [`__init__`](../_base/embedding_module.md#BaseEmbeddingModule.__init__)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseEmbeddingModule`](../_base/embedding_module.md#BaseEmbeddingModule)

### `Qwen3ForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/qwen3/modeling_qwen3.py:609`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L609)
- doc: Qwen3 model for sequence classification tasks.
- signature: `class Qwen3ForSequenceClassification(BaseSequenceClassificationModule[Qwen3Model, Qwen3Config]):`
- members:
  - `__init__(self, config: Qwen3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike | None = None, *, rngs: nn.Rngs)` — [`L626`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L626) — Initialize Qwen3 model for sequence classification.
- protocol/private: `_config_class`[`L624`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L624), `_model_type`[`L623`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L623), `_task_type`[`L622`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L622)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`Qwen3Config`](qwen3_configuration.md#Qwen3Config), [`Qwen3Model`](modeling_qwen3.md#Qwen3Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule)

### `Qwen3MLP`  ·  implements/extends Module
- def: [`easydel/modules/qwen3/modeling_qwen3.py:49`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L49)
- doc: Multi-Layer Perceptron module for Qwen3 models.
- signature: `class Qwen3MLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L114`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L114) — Apply SwiGLU feedforward transformation.
  - `__init__(self, config: Qwen3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike | None = None, *, rngs: nn.Rngs)` — [`L56`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L56) — Initialize Qwen3 MLP block.
  - `act_fn` — [`L112`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L112)
  - `config` — [`L75`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L75)
  - `down_proj` — [`L102`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L102)
  - `dtype` — [`L76`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L76)
  - `gate_proj` — [`L97`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L97)
  - `param_dtype` — [`L77`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L77)
  - `precision` — [`L78`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L78)
  - `up_proj` — [`L107`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L107)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`Qwen3Config`](qwen3_configuration.md#Qwen3Config), [`hidden_size`](qwen3_configuration.md#Qwen3Config.hidden_size), [`initializer_range`](qwen3_configuration.md#Qwen3Config.initializer_range), [`intermediate_size`](qwen3_configuration.md#Qwen3Config.intermediate_size), [`hidden_act`](qwen3_configuration.md#Qwen3Config.hidden_act)
- used by: [`mlp`](modeling_qwen3.md#Qwen3DecoderLayer.mlp)

### `Qwen3Model`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/qwen3/modeling_qwen3.py:333`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L333)
- doc: Qwen3 model implementation.
- signature: `class Qwen3Model(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L408`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L408) — Forward pass through the Qwen3 base model.
  - `__init__(self, config: Qwen3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike | None = None, *, rngs: nn.Rngs)` — [`L347`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L347) — Initialize Qwen3 base model.
  - `get_decoder(self)` — [`L540`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L540) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L553`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L553) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L533`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L533) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L546`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L546) — Returns the language model head of the module.
  - `embed_tokens` — [`L373`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L373)
  - `layers` — [`L387`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L387)
  - `norm` — [`L400`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/modeling_qwen3.py#L400)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`gradient_checkpointing`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing), [`Qwen3Config`](qwen3_configuration.md#Qwen3Config), [`hidden_size`](qwen3_configuration.md#Qwen3Config.hidden_size), [`initializer_range`](qwen3_configuration.md#Qwen3Config.initializer_range), [`num_hidden_layers`](qwen3_configuration.md#Qwen3Config.num_hidden_layers), [`rms_norm_eps`](qwen3_configuration.md#Qwen3Config.rms_norm_eps), [`Qwen3DecoderLayer`](modeling_qwen3.md#Qwen3DecoderLayer), [`vocab_size`](qwen3_configuration.md#Qwen3Config.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`Qwen3ForCausalLM`](modeling_qwen3.md#Qwen3ForCausalLM), [`Qwen3ForEmbedding`](modeling_qwen3.md#Qwen3ForEmbedding), [`Qwen3ForSequenceClassification`](modeling_qwen3.md#Qwen3ForSequenceClassification), [`__init__`](modeling_qwen3.md#Qwen3ForCausalLM.__init__), [`__init__`](modeling_qwen3.md#Qwen3ForEmbedding.__init__), [`__init__`](modeling_qwen3.md#Qwen3ForSequenceClassification.__init__)

