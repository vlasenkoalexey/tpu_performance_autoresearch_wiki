---
title: 'Module: easydel/modules/llama/modeling_llama.py'
type: catalog
provenance: extracted
module: easydel/modules/llama/modeling_llama.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.llama.modeling_llama`/Llama
symbols:
  LlamaModel.__call__: Model#__call__().
  LlamaDecoderLayer.__call__: DecoderLayer#__call__().
  LlamaModel: Model#
  LlamaMLP.__call__: MLP#__call__().
  LlamaForCausalLM: ForCausalLM#
  LlamaForSequenceClassification: ForSequenceClassification#
  LlamaModel.dropout: Model#dropout.
  LlamaMLP.precision: MLP#precision.
  LlamaMLP.act_fn: MLP#act_fn.
  LlamaDecoderLayer.input_layernorm: DecoderLayer#input_layernorm.
  LlamaDecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  LlamaForCausalLM.__init__: ForCausalLM#__init__().
  LlamaForSequenceClassification.__init__: ForSequenceClassification#__init__().
  LlamaModel.embed_tokens: Model#embed_tokens.
  LlamaMLP.config: MLP#config.
  LlamaMLP.gate_proj: MLP#gate_proj.
  LlamaMLP.down_proj: MLP#down_proj.
  LlamaMLP.up_proj: MLP#up_proj.
  LlamaMLP.dropout: MLP#dropout.
  LlamaModel.norm: Model#norm.
  LlamaAttention.__init__: Attention#__init__().
  LlamaModel.__init__: Model#__init__().
  LlamaForCausalLM._task_type: ForCausalLM#_task_type.
  LlamaForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  LlamaDecoderLayer.mlp: DecoderLayer#mlp.
  LlamaModel.layers: Model#layers.
  LlamaAttention: Attention#
  LlamaDecoderLayer.self_attn: DecoderLayer#self_attn.
  LlamaDecoderLayer.config: DecoderLayer#config.
  LlamaMLP.__init__: MLP#__init__().
  LlamaDecoderLayer.__init__: DecoderLayer#__init__().
  LlamaModel.get_embedding: Model#get_embedding().
  LlamaForCausalLM._config_class: ForCausalLM#_config_class.
  LlamaForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  LlamaMLP: MLP#
  LlamaDecoderLayer: DecoderLayer#
  LlamaMLP.dtype: MLP#dtype.
  LlamaMLP.param_dtype: MLP#param_dtype.
  LlamaDecoderLayer.dtype: DecoderLayer#dtype.
  LlamaDecoderLayer.param_dtype: DecoderLayer#param_dtype.
  LlamaDecoderLayer.precision: DecoderLayer#precision.
  LlamaModel.get_encoder: Model#get_encoder().
  LlamaModel.get_decoder: Model#get_decoder().
  LlamaModel.get_lm_head: Model#get_lm_head().
  LlamaForCausalLM._model_type: ForCausalLM#_model_type.
  LlamaForSequenceClassification._model_type: ForSequenceClassification#_model_type.
---
# Module: [`easydel/modules/llama/modeling_llama.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py)

## Classes
### `LlamaAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/llama/modeling_llama.py:130`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L130)
- doc: Multi-head attention layer with RoPE embeddings for Llama models.
- signature: `class LlamaAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: LlamaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L133) — Initialize Llama attention layer with grouped-query attention support.
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`LlamaConfig`](llama_configuration.md#LlamaConfig)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`self_attn`](modeling_llama.md#LlamaDecoderLayer.self_attn)

### `LlamaDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/llama/modeling_llama.py:165`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L165)
- doc: Single decoder layer for Llama models.
- signature: `class LlamaDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L228`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L228) — Forward pass through the decoder layer.
  - `__init__(self, config: LlamaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L172`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L172) — Initialize Llama decoder layer.
  - `config` — [`L192`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L192)
  - `dtype` — [`L193`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L193)
  - `input_layernorm` — [`L213`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L213)
  - `mlp` — [`L206`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L206)
  - `param_dtype` — [`L194`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L194)
  - `post_attention_layernorm` — [`L220`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L220)
  - `precision` — [`L195`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L195)
  - `self_attn` — [`L197`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L197)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`LlamaConfig`](llama_configuration.md#LlamaConfig), [`hidden_size`](llama_configuration.md#LlamaConfig.hidden_size), [`LlamaAttention`](modeling_llama.md#LlamaAttention), [`rms_norm_eps`](llama_configuration.md#LlamaConfig.rms_norm_eps), [`LlamaMLP`](modeling_llama.md#LlamaMLP)
- used by: [`dropout`](modeling_llama.md#LlamaModel.dropout)

### `LlamaForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/llama/modeling_llama.py:520`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L520)
- doc: Llama model with a language modeling head for causal language modeling tasks.
- signature: `class LlamaForCausalLM(BaseCausalLMModule[LlamaModel, LlamaConfig]):`
- members:
  - `__init__(self, config: LlamaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L537`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L537) — Initialize Llama model for causal language modeling.
- protocol/private: `_config_class`[`L535`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L535), `_model_type`[`L534`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L534), `_task_type`[`L533`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L533)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`LlamaConfig`](llama_configuration.md#LlamaConfig), [`LlamaModel`](modeling_llama.md#LlamaModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `LlamaForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/llama/modeling_llama.py:568`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L568)
- doc: Llama model for sequence classification tasks.
- signature: `class LlamaForSequenceClassification(BaseSequenceClassificationModule[LlamaModel, LlamaConfig]):`
- members:
  - `__init__(self, config: LlamaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L585`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L585) — Initialize Llama model for sequence classification.
- protocol/private: `_config_class`[`L583`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L583), `_model_type`[`L582`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L582), `_task_type`[`L581`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L581)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`LlamaConfig`](llama_configuration.md#LlamaConfig), [`LlamaModel`](modeling_llama.md#LlamaModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule)

### `LlamaMLP`  ·  implements/extends Module
- def: [`easydel/modules/llama/modeling_llama.py:48`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L48)
- doc: Multi-Layer Perceptron module for Llama models.
- signature: `class LlamaMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L102`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L102) — Apply SwiGLU feedforward transformation.
  - `__init__(self, config: LlamaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L55`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L55) — Initialize Llama MLP block.
  - `act_fn` — [`L100`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L100)
  - `config` — [`L74`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L74)
  - `down_proj` — [`L97`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L97)
  - `dropout` — [`L99`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L99)
  - `dtype` — [`L75`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L75)
  - `gate_proj` — [`L96`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L96)
  - `param_dtype` — [`L76`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L76)
  - `precision` — [`L77`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L77)
  - `up_proj` — [`L98`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L98)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`LlamaConfig`](llama_configuration.md#LlamaConfig), [`hidden_size`](llama_configuration.md#LlamaConfig.hidden_size), [`intermediate_size`](llama_configuration.md#LlamaConfig.intermediate_size), [`initializer_range`](llama_configuration.md#LlamaConfig.initializer_range), [`mlp_bias`](llama_configuration.md#LlamaConfig.mlp_bias), [`hidden_act`](llama_configuration.md#LlamaConfig.hidden_act), [`resid_pdrop`](llama_configuration.md#LlamaConfig.resid_pdrop)
- used by: [`mlp`](modeling_llama.md#LlamaDecoderLayer.mlp)

### `LlamaModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/llama/modeling_llama.py:296`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L296)
- doc: Llama model implementation.
- signature: `class LlamaModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L371`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L371) — Forward pass through the Llama base model.
  - `__init__(self, config: LlamaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L309`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L309) — Initialize Llama base model.
  - `get_decoder(self)` — [`L499`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L499) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L512`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L512) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L492`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L492) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L505`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L505) — Returns the language model head of the module.
  - `dropout` — [`L343`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L343)
  - `embed_tokens` — [`L335`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L335)
  - `layers` — [`L350`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L350)
  - `norm` — [`L363`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama/modeling_llama.py#L363)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`LlamaConfig`](llama_configuration.md#LlamaConfig), [`LlamaDecoderLayer`](modeling_llama.md#LlamaDecoderLayer), [`gradient_checkpointing`](llama_configuration.md#LlamaConfig.gradient_checkpointing)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`LlamaForCausalLM`](modeling_llama.md#LlamaForCausalLM), [`LlamaForSequenceClassification`](modeling_llama.md#LlamaForSequenceClassification), [`__init__`](modeling_llama.md#LlamaForCausalLM.__init__), [`__init__`](modeling_llama.md#LlamaForSequenceClassification.__init__)

