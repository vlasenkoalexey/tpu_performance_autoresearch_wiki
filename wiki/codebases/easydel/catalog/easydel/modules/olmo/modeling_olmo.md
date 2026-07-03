---
title: 'Module: easydel/modules/olmo/modeling_olmo.py'
type: catalog
provenance: extracted
module: easydel/modules/olmo/modeling_olmo.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.olmo.modeling_olmo`/Olmo
symbols:
  OlmoModel.__call__: Model#__call__().
  OlmoDecoderLayer.__call__: DecoderLayer#__call__().
  OlmoModel.embed_tokens: Model#embed_tokens.
  OlmoModel: Model#
  OlmoForCausalLM: ForCausalLM#
  OlmoForSequenceClassification: ForSequenceClassification#
  OlmoMLP.__call__: MLP#__call__().
  OlmoMLP.act_fn: MLP#act_fn.
  OlmoMLP.precision: MLP#precision.
  OlmoForCausalLM.__init__: ForCausalLM#__init__().
  OlmoForSequenceClassification.__init__: ForSequenceClassification#__init__().
  OlmoMLP.gate_proj: MLP#gate_proj.
  OlmoMLP.down_proj: MLP#down_proj.
  OlmoMLP.up_proj: MLP#up_proj.
  OlmoDecoderLayer.input_layernorm: DecoderLayer#input_layernorm.
  OlmoDecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  OlmoModel.norm: Model#norm.
  OlmoAttention._preprocess_qkv: Attention#_preprocess_qkv().
  OlmoModel.__init__: Model#__init__().
  OlmoForCausalLM._task_type: ForCausalLM#_task_type.
  OlmoForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  OlmoAttention.clip_qkv: Attention#clip_qkv.
  OlmoDecoderLayer.mlp: DecoderLayer#mlp.
  OlmoModel.layers: Model#layers.
  OlmoAttention: Attention#
  OlmoDecoderLayer.self_attn: DecoderLayer#self_attn.
  OlmoMLP.config: MLP#config.
  OlmoMLP.__init__: MLP#__init__().
  OlmoAttention.__init__: Attention#__init__().
  OlmoDecoderLayer.__init__: DecoderLayer#__init__().
  OlmoModel.get_embedding: Model#get_embedding().
  OlmoForCausalLM._config_class: ForCausalLM#_config_class.
  OlmoForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  OlmoDecoderLayer.config: DecoderLayer#config.
  OlmoMLP: MLP#
  OlmoDecoderLayer: DecoderLayer#
  OlmoMLP.dtype: MLP#dtype.
  OlmoMLP.param_dtype: MLP#param_dtype.
  OlmoDecoderLayer.dtype: DecoderLayer#dtype.
  OlmoDecoderLayer.param_dtype: DecoderLayer#param_dtype.
  OlmoDecoderLayer.precision: DecoderLayer#precision.
  OlmoModel.get_encoder: Model#get_encoder().
  OlmoModel.get_decoder: Model#get_decoder().
  OlmoModel.get_lm_head: Model#get_lm_head().
  OlmoForCausalLM._model_type: ForCausalLM#_model_type.
  OlmoForSequenceClassification._model_type: ForSequenceClassification#_model_type.
---
# Module: [`easydel/modules/olmo/modeling_olmo.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py)

## Classes
### `OlmoAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/olmo/modeling_olmo.py:143`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L143)
- doc: Multi-head attention layer with RoPE embeddings for OLMo models.
- signature: `class OlmoAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: OlmoConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L149) — Initialize OLMo attention layer with grouped-query attention support.
  - `_preprocess_qkv(self, query_states: jnp.ndarray, key_states: jnp.ndarray, value_states: jnp.ndarray)` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L181) — Apply optional clipping before reshaping QKV tensors.
  - `clip_qkv` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L169)
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`OlmoConfig`](olmo_configuration.md#OlmoConfig), [`_preprocess_qkv`](../../layers/attention/_unified.md#UnifiedAttention._preprocess_qkv)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_preprocess_qkv`](../../layers/attention/_unified.md#UnifiedAttention._preprocess_qkv), [`self_attn`](modeling_olmo.md#OlmoDecoderLayer.self_attn)

### `OlmoDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/olmo/modeling_olmo.py:209`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L209)
- doc: Single decoder layer for OLMo models.
- signature: `class OlmoDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L272`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L272) — Forward pass through the decoder layer.
  - `__init__(self, config: OlmoConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L216`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L216) — Initialize OLMo decoder layer.
  - `config` — [`L236`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L236)
  - `dtype` — [`L237`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L237)
  - `input_layernorm` — [`L257`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L257)
  - `mlp` — [`L249`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L249)
  - `param_dtype` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L238)
  - `post_attention_layernorm` — [`L264`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L264)
  - `precision` — [`L239`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L239)
  - `self_attn` — [`L241`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L241)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`OlmoConfig`](olmo_configuration.md#OlmoConfig), [`hidden_size`](olmo_configuration.md#OlmoConfig.hidden_size), [`OlmoAttention`](modeling_olmo.md#OlmoAttention), [`OlmoMLP`](modeling_olmo.md#OlmoMLP), [`scan_mlp_chunk_size`](olmo_configuration.md#OlmoConfig.scan_mlp_chunk_size), [`use_scan_mlp`](olmo_configuration.md#OlmoConfig.use_scan_mlp)
- used by: [`embed_tokens`](modeling_olmo.md#OlmoModel.embed_tokens)

### `OlmoForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/olmo/modeling_olmo.py:552`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L552)
- doc: OLMo model with a language modeling head for causal language modeling tasks.
- signature: `class OlmoForCausalLM(BaseCausalLMModule[OlmoModel, OlmoConfig]):`
- members:
  - `__init__(self, config: OlmoConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L569`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L569) — Initialize OLMo model for causal language modeling.
- protocol/private: `_config_class`[`L567`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L567), `_model_type`[`L566`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L566), `_task_type`[`L565`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L565)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`OlmoConfig`](olmo_configuration.md#OlmoConfig), [`OlmoModel`](modeling_olmo.md#OlmoModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `OlmoForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/olmo/modeling_olmo.py:600`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L600)
- doc: OLMo model for sequence classification tasks.
- signature: `class OlmoForSequenceClassification(BaseSequenceClassificationModule[OlmoModel, OlmoConfig]):`
- members:
  - `__init__(self, config: OlmoConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L617`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L617) — Initialize OLMo model for sequence classification.
- protocol/private: `_config_class`[`L615`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L615), `_model_type`[`L614`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L614), `_task_type`[`L613`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L613)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`OlmoConfig`](olmo_configuration.md#OlmoConfig), [`OlmoModel`](modeling_olmo.md#OlmoModel)
- used by: [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule)

### `OlmoMLP`  ·  implements/extends Module
- def: [`easydel/modules/olmo/modeling_olmo.py:49`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L49)
- doc: Multi-Layer Perceptron module for OLMo models.
- signature: `class OlmoMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L116) — Apply SwiGLU feedforward transformation.
  - `__init__(self, config: OlmoConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L56`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L56) — Initialize OLMo MLP block.
  - `act_fn` — [`L114`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L114)
  - `config` — [`L77`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L77)
  - `down_proj` — [`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L104)
  - `dtype` — [`L78`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L78)
  - `gate_proj` — [`L99`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L99)
  - `param_dtype` — [`L79`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L79)
  - `precision` — [`L80`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L80)
  - `up_proj` — [`L109`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L109)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`OlmoConfig`](olmo_configuration.md#OlmoConfig), [`hidden_size`](olmo_configuration.md#OlmoConfig.hidden_size), [`initializer_range`](olmo_configuration.md#OlmoConfig.initializer_range), [`intermediate_size`](olmo_configuration.md#OlmoConfig.intermediate_size), [`hidden_act`](olmo_configuration.md#OlmoConfig.hidden_act)
- used by: [`mlp`](modeling_olmo.md#OlmoDecoderLayer.mlp)

### `OlmoModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/olmo/modeling_olmo.py:330`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L330)
- doc: OLMo model implementation.
- signature: `class OlmoModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L405`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L405) — Forward pass through the OLMo base model.
  - `__init__(self, config: OlmoConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L343`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L343) — Initialize OLMo base model.
  - `get_decoder(self)` — [`L531`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L531) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L544`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L544) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L524`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L524) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L537`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L537) — Returns the language model head of the module.
  - `embed_tokens` — [`L369`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L369)
  - `layers` — [`L384`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L384)
  - `norm` — [`L397`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo/modeling_olmo.py#L397)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`OlmoConfig`](olmo_configuration.md#OlmoConfig), [`hidden_size`](olmo_configuration.md#OlmoConfig.hidden_size), [`initializer_range`](olmo_configuration.md#OlmoConfig.initializer_range), [`num_hidden_layers`](olmo_configuration.md#OlmoConfig.num_hidden_layers), [`OlmoDecoderLayer`](modeling_olmo.md#OlmoDecoderLayer), [`gradient_checkpointing`](olmo_configuration.md#OlmoConfig.gradient_checkpointing), [`vocab_size`](olmo_configuration.md#OlmoConfig.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`OlmoForCausalLM`](modeling_olmo.md#OlmoForCausalLM), [`OlmoForSequenceClassification`](modeling_olmo.md#OlmoForSequenceClassification), [`__init__`](modeling_olmo.md#OlmoForCausalLM.__init__), [`__init__`](modeling_olmo.md#OlmoForSequenceClassification.__init__)

