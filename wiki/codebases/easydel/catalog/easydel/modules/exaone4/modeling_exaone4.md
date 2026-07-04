---
title: 'Module: easydel/modules/exaone4/modeling_exaone4.py'
type: catalog
provenance: extracted
module: easydel/modules/exaone4/modeling_exaone4.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.exaone4.modeling_exaone4`/Exaone4
symbols:
  Exaone4Model.__call__: Model#__call__().
  Exaone4DecoderLayer.__call__: DecoderLayer#__call__().
  Exaone4Model.embed_tokens: Model#embed_tokens.
  Exaone4Model: Model#
  Exaone4ForCausalLM: ForCausalLM#
  Exaone4ForSequenceClassification: ForSequenceClassification#
  Exaone4MLP.__call__: MLP#__call__().
  Exaone4Attention.is_sliding: Attention#is_sliding.
  Exaone4Attention._create_rotary: Attention#_create_rotary().
  Exaone4Attention._create_q_norm: Attention#_create_q_norm().
  Exaone4Attention._create_k_norm: Attention#_create_k_norm().
  Exaone4DecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  Exaone4DecoderLayer.post_feedforward_layernorm: DecoderLayer#post_feedforward_layernorm.
  Exaone4Model.norm: Model#norm.
  Exaone4MLP.precision: MLP#precision.
  Exaone4ForCausalLM.__init__: ForCausalLM#__init__().
  Exaone4ForSequenceClassification.__init__: ForSequenceClassification#__init__().
  Exaone4MLP.gate_proj: MLP#gate_proj.
  Exaone4MLP.up_proj: MLP#up_proj.
  Exaone4MLP.down_proj: MLP#down_proj.
  Exaone4MLP.act_fn: MLP#act_fn.
  Exaone4Attention._postprocess_qkv: Attention#_postprocess_qkv().
  Exaone4Model.__init__: Model#__init__().
  Exaone4ForCausalLM._task_type: ForCausalLM#_task_type.
  Exaone4ForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  Exaone4DecoderLayer.mlp: DecoderLayer#mlp.
  Exaone4Model.layers: Model#layers.
  Exaone4Attention: Attention#
  Exaone4DecoderLayer.self_attn: DecoderLayer#self_attn.
  Exaone4DecoderLayer.config: DecoderLayer#config.
  Exaone4MLP.__init__: MLP#__init__().
  Exaone4Attention.__init__: Attention#__init__().
  Exaone4DecoderLayer.__init__: DecoderLayer#__init__().
  Exaone4Model.get_embedding: Model#get_embedding().
  Exaone4ForCausalLM._config_class: ForCausalLM#_config_class.
  Exaone4ForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  Exaone4MLP.config: MLP#config.
  Exaone4MLP: MLP#
  Exaone4Attention._dummy: Attention#_dummy().
  Exaone4DecoderLayer: DecoderLayer#
  Exaone4MLP.dtype: MLP#dtype.
  Exaone4MLP.param_dtype: MLP#param_dtype.
  Exaone4DecoderLayer.layer_idx: DecoderLayer#layer_idx.
  Exaone4DecoderLayer.dtype: DecoderLayer#dtype.
  Exaone4DecoderLayer.param_dtype: DecoderLayer#param_dtype.
  Exaone4DecoderLayer.precision: DecoderLayer#precision.
  Exaone4Model.get_decoder: Model#get_decoder().
  Exaone4ForCausalLM._model_type: ForCausalLM#_model_type.
  Exaone4ForSequenceClassification._model_type: ForSequenceClassification#_model_type.
---
# Module: [`easydel/modules/exaone4/modeling_exaone4.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py)

## Classes
### `Exaone4Attention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/exaone4/modeling_exaone4.py:151`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L151)
- doc: Multi-head attention layer with NoPE (No Position Embedding) for Exaone4 models.
- signature: `class Exaone4Attention(UnifiedAttention):`
- members:
  - `__init__(self, config: Exaone4Config, layer_idx: int, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L159) — Initialize Exaone4 attention layer with conditional RoPE (NoPE).
  - `_create_k_norm(self, config: Exaone4Config, dtype: jnp.dtype, param_dtype: jnp.dtype, rngs: nn.Rngs)` — [`L245`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L245) — Create key normalization layer using RMSNorm.
  - `_create_q_norm(self, config: Exaone4Config, dtype: jnp.dtype, param_dtype: jnp.dtype, rngs: nn.Rngs)` — [`L222`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L222) — Create query normalization layer using RMSNorm.
  - `_create_rotary(self, config: Exaone4Config, dtype: jnp.dtype)` — [`L195`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L195) — Create rotary embedding based on layer type (NoPE for full attention).
  - `_dummy(query, key, positions=None, frequencies=None)` — [`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L212) — Dummy RoPE function that returns query/key unchanged (NoPE).
  - `_postprocess_qkv(self, query_states: jnp.ndarray, key_states: jnp.ndarray, value_states: jnp.ndarray)` — [`L268`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L268) — Apply Q/K normalization per-head for training stability.
  - `is_sliding` — [`L180`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L180)
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`Exaone4Config`](exaone4_configuration.md#Exaone4Config), [`key_normalization`](../../layers/attention/_unified.md#UnifiedAttention.key_normalization), [`query_normalization`](../../layers/attention/_unified.md#UnifiedAttention.query_normalization), [`layer_types`](exaone4_configuration.md#Exaone4Config.layer_types), [`rms_norm_eps`](exaone4_configuration.md#Exaone4Config.rms_norm_eps), [`head_dim`](exaone4_configuration.md#Exaone4Config.head_dim), [`sliding_window`](exaone4_configuration.md#Exaone4Config.sliding_window)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`_postprocess_qkv`](../../layers/attention/_unified.md#UnifiedAttention._postprocess_qkv), [`_create_k_norm`](../../layers/attention/_unified.md#UnifiedAttention._create_k_norm), [`_create_q_norm`](../../layers/attention/_unified.md#UnifiedAttention._create_q_norm), [`self_attn`](modeling_exaone4.md#Exaone4DecoderLayer.self_attn)

### `Exaone4DecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/exaone4/modeling_exaone4.py:298`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L298)
- doc: Single decoder layer for Exaone4 models.
- signature: `class Exaone4DecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L366`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L366) — Forward pass through the decoder layer.
  - `__init__(self, config: Exaone4Config, layer_idx: int, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L306`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L306) — Initialize Exaone4 decoder layer.
  - `config` — [`L326`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L326)
  - `dtype` — [`L328`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L328)
  - `layer_idx` — [`L327`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L327)
  - `mlp` — [`L341`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L341)
  - `param_dtype` — [`L329`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L329)
  - `post_attention_layernorm` — [`L350`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L350)
  - `post_feedforward_layernorm` — [`L358`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L358)
  - `precision` — [`L330`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L330)
  - `self_attn` — [`L332`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L332)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`Exaone4Config`](exaone4_configuration.md#Exaone4Config), [`hidden_size`](exaone4_configuration.md#Exaone4Config.hidden_size), [`rms_norm_eps`](exaone4_configuration.md#Exaone4Config.rms_norm_eps), [`Exaone4Attention`](modeling_exaone4.md#Exaone4Attention), [`Exaone4MLP`](modeling_exaone4.md#Exaone4MLP)
- used by: [`embed_tokens`](modeling_exaone4.md#Exaone4Model.embed_tokens)

### `Exaone4ForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/exaone4/modeling_exaone4.py:655`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L655)
- doc: Exaone4 model with a language modeling head for causal language modeling tasks.
- signature: `class Exaone4ForCausalLM(BaseCausalLMModule[Exaone4Model, Exaone4Config]):`
- members:
  - `__init__(self, config: Exaone4Config, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L673`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L673) — Initialize Exaone4 model for causal language modeling.
- protocol/private: `_config_class`[`L671`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L671), `_model_type`[`L670`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L670), `_task_type`[`L669`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L669)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`Exaone4Config`](exaone4_configuration.md#Exaone4Config), [`Exaone4Model`](modeling_exaone4.md#Exaone4Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `Exaone4ForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/exaone4/modeling_exaone4.py:704`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L704)
- doc: Exaone4 model for sequence classification tasks.
- signature: `class Exaone4ForSequenceClassification(BaseSequenceClassificationModule[Exaone4Model, Exaone4Config]):`
- members:
  - `__init__(self, config: Exaone4Config, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L721`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L721) — Initialize Exaone4 model for sequence classification.
- protocol/private: `_config_class`[`L719`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L719), `_model_type`[`L718`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L718), `_task_type`[`L717`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L717)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`Exaone4Config`](exaone4_configuration.md#Exaone4Config), [`Exaone4Model`](modeling_exaone4.md#Exaone4Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule)

### `Exaone4MLP`  ·  implements/extends Module
- def: [`easydel/modules/exaone4/modeling_exaone4.py:52`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L52)
- doc: Gated Multi-Layer Perceptron module for Exaone4 models.
- signature: `class Exaone4MLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L122) — Apply gated feedforward transformation.
  - `__init__(self, config: Exaone4Config, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L61`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L61) — Initialize Exaone4 gated MLP block.
  - `act_fn` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L120)
  - `config` — [`L81`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L81)
  - `down_proj` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L115)
  - `dtype` — [`L82`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L82)
  - `gate_proj` — [`L105`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L105)
  - `param_dtype` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L83)
  - `precision` — [`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L84)
  - `up_proj` — [`L110`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L110)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`Exaone4Config`](exaone4_configuration.md#Exaone4Config), [`hidden_size`](exaone4_configuration.md#Exaone4Config.hidden_size), [`intermediate_size`](exaone4_configuration.md#Exaone4Config.intermediate_size), [`initializer_range`](exaone4_configuration.md#Exaone4Config.initializer_range), [`hidden_act`](exaone4_configuration.md#Exaone4Config.hidden_act)
- used by: [`mlp`](modeling_exaone4.md#Exaone4DecoderLayer.mlp)

### `Exaone4Model`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/exaone4/modeling_exaone4.py:441`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L441)
- doc: Exaone4 model implementation.
- signature: `class Exaone4Model(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L516`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L516) — Forward pass through the Exaone4 base model.
  - `__init__(self, config: Exaone4Config, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L455`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L455) — Initialize Exaone4 base model.
  - `get_decoder(self)` — [`L645`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L645) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L637`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L637) — Returns the embedding layer of the module.
  - `embed_tokens` — [`L480`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L480)
  - `layers` — [`L494`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L494)
  - `norm` — [`L508`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone4/modeling_exaone4.py#L508)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`gradient_checkpointing`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing), [`Exaone4Config`](exaone4_configuration.md#Exaone4Config), [`hidden_size`](exaone4_configuration.md#Exaone4Config.hidden_size), [`rms_norm_eps`](exaone4_configuration.md#Exaone4Config.rms_norm_eps), [`num_hidden_layers`](exaone4_configuration.md#Exaone4Config.num_hidden_layers), [`Exaone4DecoderLayer`](modeling_exaone4.md#Exaone4DecoderLayer), [`vocab_size`](exaone4_configuration.md#Exaone4Config.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`Exaone4ForCausalLM`](modeling_exaone4.md#Exaone4ForCausalLM), [`Exaone4ForSequenceClassification`](modeling_exaone4.md#Exaone4ForSequenceClassification), [`__init__`](modeling_exaone4.md#Exaone4ForCausalLM.__init__), [`__init__`](modeling_exaone4.md#Exaone4ForSequenceClassification.__init__)

