---
title: 'Module: easydel/modules/glm/modeling_glm.py'
type: catalog
provenance: extracted
module: easydel/modules/glm/modeling_glm.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.glm.modeling_glm`/Glm
symbols:
  GlmModel.__call__: Model#__call__().
  GlmDecoderLayer.__call__: DecoderLayer#__call__().
  GlmModel: Model#
  GlmModel.embed_tokens: Model#embed_tokens.
  GlmForCausalLM: ForCausalLM#
  GlmForSequenceClassification: ForSequenceClassification#
  GlmMLP.__call__: MLP#__call__().
  GlmMLP.act_fn: MLP#act_fn.
  GlmDecoderLayer.input_layernorm: DecoderLayer#input_layernorm.
  GlmDecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  GlmMLP.precision: MLP#precision.
  GlmForCausalLM.__init__: ForCausalLM#__init__().
  GlmForSequenceClassification.__init__: ForSequenceClassification#__init__().
  GlmMLP.gate_up_proj: MLP#gate_up_proj.
  GlmMLP.down_proj: MLP#down_proj.
  GlmModel.norm: Model#norm.
  GlmModel.__init__: Model#__init__().
  GlmForCausalLM._task_type: ForCausalLM#_task_type.
  GlmForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  GlmDecoderLayer.mlp: DecoderLayer#mlp.
  GlmModel.layers: Model#layers.
  GlmAttention: Attention#
  GlmDecoderLayer.self_attn: DecoderLayer#self_attn.
  GlmMLP.config: MLP#config.
  GlmDecoderLayer.config: DecoderLayer#config.
  GlmMLP.__init__: MLP#__init__().
  GlmAttention.__init__: Attention#__init__().
  GlmAttention.layer_idx: Attention#layer_idx.
  GlmDecoderLayer.__init__: DecoderLayer#__init__().
  GlmModel.padding_idx: Model#padding_idx.
  GlmModel.vocab_size: Model#vocab_size.
  GlmModel.get_embedding: Model#get_embedding().
  GlmForCausalLM._config_class: ForCausalLM#_config_class.
  GlmForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  GlmMLP: MLP#
  GlmDecoderLayer: DecoderLayer#
  GlmMLP.dtype: MLP#dtype.
  GlmMLP.param_dtype: MLP#param_dtype.
  GlmDecoderLayer.dtype: DecoderLayer#dtype.
  GlmDecoderLayer.param_dtype: DecoderLayer#param_dtype.
  GlmDecoderLayer.precision: DecoderLayer#precision.
  GlmDecoderLayer.layer_idx: DecoderLayer#layer_idx.
  GlmModel.get_encoder: Model#get_encoder().
  GlmModel.get_decoder: Model#get_decoder().
  GlmModel.get_lm_head: Model#get_lm_head().
  GlmForCausalLM._model_type: ForCausalLM#_model_type.
  GlmForSequenceClassification._model_type: ForSequenceClassification#_model_type.
---
# Module: [`easydel/modules/glm/modeling_glm.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py)

## Classes
### `GlmAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/glm/modeling_glm.py:127`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L127)
- doc: Multi-head attention layer with RoPE embeddings for GLM models.
- signature: `class GlmAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: GlmConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L130) — Initialize GLM attention layer with grouped-query attention support.
  - `layer_idx` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L150)
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`GlmConfig`](glm_configuration.md#GlmConfig)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`self_attn`](modeling_glm.md#GlmDecoderLayer.self_attn)

### `GlmDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/glm/modeling_glm.py:161`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L161)
- doc: Single decoder layer for GLM models.
- signature: `class GlmDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L224`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L224) — Forward pass through the decoder layer.
  - `__init__(self, config: GlmConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L168) — Initialize GLM decoder layer.
  - `config` — [`L188`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L188)
  - `dtype` — [`L189`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L189)
  - `input_layernorm` — [`L209`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L209)
  - `layer_idx` — [`L192`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L192)
  - `mlp` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L202)
  - `param_dtype` — [`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L190)
  - `post_attention_layernorm` — [`L216`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L216)
  - `precision` — [`L191`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L191)
  - `self_attn` — [`L194`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L194)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`GlmConfig`](glm_configuration.md#GlmConfig), [`hidden_size`](glm_configuration.md#GlmConfig.hidden_size), [`GlmAttention`](modeling_glm.md#GlmAttention), [`rms_norm_eps`](glm_configuration.md#GlmConfig.rms_norm_eps), [`GlmMLP`](modeling_glm.md#GlmMLP)
- used by: [`embed_tokens`](modeling_glm.md#GlmModel.embed_tokens)

### `GlmForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/glm/modeling_glm.py:529`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L529)
- doc: GLM model with a language modeling head for causal language modeling tasks.
- signature: `class GlmForCausalLM(BaseCausalLMModule[GlmModel, GlmConfig]):`
- members:
  - `__init__(self, config: GlmConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L546`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L546) — Initialize GLM model for causal language modeling.
- protocol/private: `_config_class`[`L544`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L544), `_model_type`[`L543`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L543), `_task_type`[`L542`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L542)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`GlmConfig`](glm_configuration.md#GlmConfig), [`GlmModel`](modeling_glm.md#GlmModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `GlmForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/glm/modeling_glm.py:577`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L577)
- doc: GLM model for sequence classification tasks.
- signature: `class GlmForSequenceClassification(BaseSequenceClassificationModule[GlmModel, GlmConfig]):`
- members:
  - `__init__(self, config: GlmConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L594`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L594) — Initialize GLM model for sequence classification.
- protocol/private: `_config_class`[`L592`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L592), `_model_type`[`L591`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L591), `_task_type`[`L590`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L590)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`GlmConfig`](glm_configuration.md#GlmConfig), [`GlmModel`](modeling_glm.md#GlmModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule)

### `GlmMLP`  ·  implements/extends Module
- def: [`easydel/modules/glm/modeling_glm.py:47`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L47)
- doc: Multi-Layer Perceptron module for GLM models.
- signature: `class GlmMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L100`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L100) — Apply gated feedforward transformation.
  - `__init__(self, config: GlmConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L55`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L55) — Initialize GLM MLP block.
  - `act_fn` — [`L98`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L98)
  - `config` — [`L74`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L74)
  - `down_proj` — [`L97`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L97)
  - `dtype` — [`L75`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L75)
  - `gate_up_proj` — [`L96`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L96)
  - `param_dtype` — [`L76`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L76)
  - `precision` — [`L77`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L77)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`GlmConfig`](glm_configuration.md#GlmConfig), [`hidden_size`](glm_configuration.md#GlmConfig.hidden_size), [`initializer_range`](glm_configuration.md#GlmConfig.initializer_range), [`intermediate_size`](glm_configuration.md#GlmConfig.intermediate_size), [`hidden_act`](glm_configuration.md#GlmConfig.hidden_act)
- used by: [`mlp`](modeling_glm.md#GlmDecoderLayer.mlp)

### `GlmModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/glm/modeling_glm.py:298`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L298)
- doc: GLM model implementation.
- signature: `class GlmModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L374`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L374) — Forward pass through the GLM base model.
  - `__init__(self, config: GlmConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L311`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L311) — Initialize GLM base model.
  - `get_decoder(self)` — [`L508`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L508) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L521`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L521) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L501`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L501) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L514`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L514) — Returns the language model head of the module.
  - `embed_tokens` — [`L339`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L339)
  - `layers` — [`L353`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L353)
  - `norm` — [`L366`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L366)
  - `padding_idx` — [`L336`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L336)
  - `vocab_size` — [`L337`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/modeling_glm.py#L337)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), `pad_token_id`, [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`gradient_checkpointing`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing), [`GlmConfig`](glm_configuration.md#GlmConfig), [`GlmDecoderLayer`](modeling_glm.md#GlmDecoderLayer), [`vocab_size`](glm_configuration.md#GlmConfig.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`GlmForCausalLM`](modeling_glm.md#GlmForCausalLM), [`GlmForSequenceClassification`](modeling_glm.md#GlmForSequenceClassification), [`__init__`](modeling_glm.md#GlmForCausalLM.__init__), [`__init__`](modeling_glm.md#GlmForSequenceClassification.__init__)

