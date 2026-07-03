---
title: 'Module: easydel/modules/glm4/modeling_glm4.py'
type: catalog
provenance: extracted
module: easydel/modules/glm4/modeling_glm4.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.glm4.modeling_glm4`/Glm4
symbols:
  Glm4DecoderLayer.__call__: DecoderLayer#__call__().
  Glm4Model.__call__: Model#__call__().
  Glm4Model: Model#
  Glm4Model.embed_tokens: Model#embed_tokens.
  Glm4ForCausalLM: ForCausalLM#
  Glm4ForSequenceClassification: ForSequenceClassification#
  Glm4MLP.__call__: MLP#__call__().
  Glm4MLP.act_fn: MLP#act_fn.
  Glm4DecoderLayer.input_layernorm: DecoderLayer#input_layernorm.
  Glm4DecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  Glm4DecoderLayer.post_self_attn_layernorm: DecoderLayer#post_self_attn_layernorm.
  Glm4DecoderLayer.post_mlp_layernorm: DecoderLayer#post_mlp_layernorm.
  Glm4MLP.precision: MLP#precision.
  Glm4ForCausalLM.__init__: ForCausalLM#__init__().
  Glm4ForSequenceClassification.__init__: ForSequenceClassification#__init__().
  Glm4MLP.gate_up_proj: MLP#gate_up_proj.
  Glm4MLP.down_proj: MLP#down_proj.
  Glm4Model.norm: Model#norm.
  Glm4Model.__init__: Model#__init__().
  Glm4ForCausalLM._task_type: ForCausalLM#_task_type.
  Glm4ForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  Glm4DecoderLayer.mlp: DecoderLayer#mlp.
  Glm4Model.layers: Model#layers.
  Glm4Attention: Attention#
  Glm4DecoderLayer.self_attn: DecoderLayer#self_attn.
  Glm4MLP.config: MLP#config.
  Glm4DecoderLayer.config: DecoderLayer#config.
  Glm4MLP.__init__: MLP#__init__().
  Glm4Attention.__init__: Attention#__init__().
  Glm4Attention.layer_idx: Attention#layer_idx.
  Glm4DecoderLayer.__init__: DecoderLayer#__init__().
  Glm4Model.padding_idx: Model#padding_idx.
  Glm4Model.vocab_size: Model#vocab_size.
  Glm4Model.get_embedding: Model#get_embedding().
  Glm4ForCausalLM._config_class: ForCausalLM#_config_class.
  Glm4ForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  Glm4MLP: MLP#
  Glm4DecoderLayer: DecoderLayer#
  Glm4MLP.dtype: MLP#dtype.
  Glm4MLP.param_dtype: MLP#param_dtype.
  Glm4DecoderLayer.dtype: DecoderLayer#dtype.
  Glm4DecoderLayer.param_dtype: DecoderLayer#param_dtype.
  Glm4DecoderLayer.precision: DecoderLayer#precision.
  Glm4DecoderLayer.layer_idx: DecoderLayer#layer_idx.
  Glm4Model.get_encoder: Model#get_encoder().
  Glm4Model.get_decoder: Model#get_decoder().
  Glm4Model.get_lm_head: Model#get_lm_head().
  Glm4ForCausalLM._model_type: ForCausalLM#_model_type.
  Glm4ForSequenceClassification._model_type: ForSequenceClassification#_model_type.
---
# Module: [`easydel/modules/glm4/modeling_glm4.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py)

## Classes
### `Glm4Attention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/glm4/modeling_glm4.py:126`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L126)
- doc: Multi-head attention layer with RoPE embeddings for GLM-4 models.
- signature: `class Glm4Attention(UnifiedAttention):`
- members:
  - `__init__(self, config: Glm4Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L129) — Initialize GLM-4 attention layer with grouped-query attention support.
  - `layer_idx` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L149)
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`Glm4Config`](glm4_configuration.md#Glm4Config)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`self_attn`](modeling_glm4.md#Glm4DecoderLayer.self_attn)

### `Glm4DecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/glm4/modeling_glm4.py:160`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L160)
- doc: Single decoder layer for GLM-4 models.
- signature: `class Glm4DecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L237`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L237) — Forward pass through the decoder layer.
  - `__init__(self, config: Glm4Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L168) — Initialize GLM-4 decoder layer.
  - `config` — [`L188`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L188)
  - `dtype` — [`L189`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L189)
  - `input_layernorm` — [`L208`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L208)
  - `layer_idx` — [`L192`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L192)
  - `mlp` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L201)
  - `param_dtype` — [`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L190)
  - `post_attention_layernorm` — [`L215`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L215)
  - `post_mlp_layernorm` — [`L229`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L229)
  - `post_self_attn_layernorm` — [`L222`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L222)
  - `precision` — [`L191`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L191)
  - `self_attn` — [`L193`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L193)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`Glm4Config`](glm4_configuration.md#Glm4Config), [`hidden_size`](glm4_configuration.md#Glm4Config.hidden_size), [`rms_norm_eps`](glm4_configuration.md#Glm4Config.rms_norm_eps), [`Glm4Attention`](modeling_glm4.md#Glm4Attention), [`Glm4MLP`](modeling_glm4.md#Glm4MLP)
- used by: [`embed_tokens`](modeling_glm4.md#Glm4Model.embed_tokens)

### `Glm4ForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/glm4/modeling_glm4.py:524`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L524)
- doc: GLM-4 model with a language modeling head for causal language modeling tasks.
- signature: `class Glm4ForCausalLM(BaseCausalLMModule[Glm4Model, Glm4Config]):`
- members:
  - `__init__(self, config: Glm4Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L541`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L541) — Initialize GLM-4 model for causal language modeling.
- protocol/private: `_config_class`[`L539`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L539), `_model_type`[`L538`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L538), `_task_type`[`L537`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L537)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`Glm4Config`](glm4_configuration.md#Glm4Config), [`Glm4Model`](modeling_glm4.md#Glm4Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `Glm4ForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/glm4/modeling_glm4.py:572`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L572)
- doc: GLM-4 model for sequence classification tasks.
- signature: `class Glm4ForSequenceClassification(BaseSequenceClassificationModule[Glm4Model, Glm4Config]):`
- members:
  - `__init__(self, config: Glm4Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L589`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L589) — Initialize GLM-4 model for sequence classification.
- protocol/private: `_config_class`[`L587`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L587), `_model_type`[`L586`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L586), `_task_type`[`L585`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L585)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`Glm4Config`](glm4_configuration.md#Glm4Config), [`Glm4Model`](modeling_glm4.md#Glm4Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule)

### `Glm4MLP`  ·  implements/extends Module
- def: [`easydel/modules/glm4/modeling_glm4.py:46`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L46)
- doc: Multi-Layer Perceptron module for GLM-4 models.
- signature: `class Glm4MLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L99`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L99) — Apply gated feedforward transformation.
  - `__init__(self, config: Glm4Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L54`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L54) — Initialize GLM-4 MLP block.
  - `act_fn` — [`L97`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L97)
  - `config` — [`L73`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L73)
  - `down_proj` — [`L96`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L96)
  - `dtype` — [`L74`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L74)
  - `gate_up_proj` — [`L95`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L95)
  - `param_dtype` — [`L75`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L75)
  - `precision` — [`L76`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L76)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`Glm4Config`](glm4_configuration.md#Glm4Config), [`hidden_size`](glm4_configuration.md#Glm4Config.hidden_size), [`initializer_range`](glm4_configuration.md#Glm4Config.initializer_range), [`intermediate_size`](glm4_configuration.md#Glm4Config.intermediate_size), [`hidden_act`](glm4_configuration.md#Glm4Config.hidden_act)
- used by: [`mlp`](modeling_glm4.md#Glm4DecoderLayer.mlp)

### `Glm4Model`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/glm4/modeling_glm4.py:309`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L309)
- doc: GLM-4 model implementation.
- signature: `class Glm4Model(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L386`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L386) — Forward pass through the GLM-4 base model.
  - `__init__(self, config: Glm4Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L323`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L323) — Initialize GLM-4 base model.
  - `get_decoder(self)` — [`L503`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L503) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L516`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L516) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L496`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L496) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L509`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L509) — Returns the language model head of the module.
  - `embed_tokens` — [`L351`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L351)
  - `layers` — [`L365`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L365)
  - `norm` — [`L378`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L378)
  - `padding_idx` — [`L348`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L348)
  - `vocab_size` — [`L349`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/modeling_glm4.py#L349)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), `pad_token_id`, [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`gradient_checkpointing`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing), [`Glm4Config`](glm4_configuration.md#Glm4Config), [`Glm4DecoderLayer`](modeling_glm4.md#Glm4DecoderLayer), [`vocab_size`](glm4_configuration.md#Glm4Config.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`Glm4ForCausalLM`](modeling_glm4.md#Glm4ForCausalLM), [`Glm4ForSequenceClassification`](modeling_glm4.md#Glm4ForSequenceClassification), [`__init__`](modeling_glm4.md#Glm4ForCausalLM.__init__), [`__init__`](modeling_glm4.md#Glm4ForSequenceClassification.__init__)

