---
title: 'Module: easydel/modules/olmo3/modeling_olmo3.py'
type: catalog
provenance: extracted
module: easydel/modules/olmo3/modeling_olmo3.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.olmo3.modeling_olmo3`/Olmo3
symbols:
  Olmo3Model.__call__: Model#__call__().
  Olmo3DecoderLayer.__call__: DecoderLayer#__call__().
  Olmo3ForCausalLM.__call__: ForCausalLM#__call__().
  Olmo3ForSequenceClassification.__call__: ForSequenceClassification#__call__().
  Olmo3Model.embed_tokens: Model#embed_tokens.
  Olmo3Model: Model#
  Olmo3ForCausalLM: ForCausalLM#
  Olmo3ForSequenceClassification: ForSequenceClassification#
  Olmo3MLP.__call__: MLP#__call__().
  Olmo3Attention._create_q_norm: Attention#_create_q_norm().
  Olmo3Attention._create_k_norm: Attention#_create_k_norm().
  Olmo3MLP.act_fn: MLP#act_fn.
  Olmo3DecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  Olmo3DecoderLayer.post_feedforward_layernorm: DecoderLayer#post_feedforward_layernorm.
  Olmo3Model.norm: Model#norm.
  Olmo3MLP.precision: MLP#precision.
  Olmo3ForCausalLM.__init__: ForCausalLM#__init__().
  Olmo3ForSequenceClassification.__init__: ForSequenceClassification#__init__().
  Olmo3MLP.gate_proj: MLP#gate_proj.
  Olmo3MLP.down_proj: MLP#down_proj.
  Olmo3MLP.up_proj: MLP#up_proj.
  Olmo3Attention.__init__: Attention#__init__().
  Olmo3Attention.attention_type_name: Attention#attention_type_name.
  Olmo3Attention._preprocess_qkv: Attention#_preprocess_qkv().
  Olmo3Model.__init__: Model#__init__().
  Olmo3ForCausalLM._task_type: ForCausalLM#_task_type.
  Olmo3ForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  Olmo3DecoderLayer.mlp: DecoderLayer#mlp.
  Olmo3Model.layers: Model#layers.
  Olmo3Attention: Attention#
  Olmo3DecoderLayer.self_attn: DecoderLayer#self_attn.
  Olmo3MLP.config: MLP#config.
  Olmo3MLP.__init__: MLP#__init__().
  Olmo3DecoderLayer.__init__: DecoderLayer#__init__().
  Olmo3Model.get_embedding: Model#get_embedding().
  Olmo3ForCausalLM._config_class: ForCausalLM#_config_class.
  Olmo3ForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  Olmo3DecoderLayer.config: DecoderLayer#config.
  Olmo3MLP: MLP#
  Olmo3DecoderLayer: DecoderLayer#
  Olmo3MLP.dtype: MLP#dtype.
  Olmo3MLP.param_dtype: MLP#param_dtype.
  Olmo3DecoderLayer.layer_idx: DecoderLayer#layer_idx.
  Olmo3DecoderLayer.dtype: DecoderLayer#dtype.
  Olmo3DecoderLayer.param_dtype: DecoderLayer#param_dtype.
  Olmo3DecoderLayer.precision: DecoderLayer#precision.
  Olmo3Model.get_encoder: Model#get_encoder().
  Olmo3Model.get_decoder: Model#get_decoder().
  Olmo3Model.get_lm_head: Model#get_lm_head().
  Olmo3ForCausalLM._model_type: ForCausalLM#_model_type.
  Olmo3ForCausalLM.get_encoder: ForCausalLM#get_encoder().
  Olmo3ForCausalLM.get_decoder: ForCausalLM#get_decoder().
  Olmo3ForCausalLM.get_lm_head: ForCausalLM#get_lm_head().
  Olmo3ForCausalLM.get_embedding: ForCausalLM#get_embedding().
  Olmo3ForSequenceClassification._model_type: ForSequenceClassification#_model_type.
  Olmo3ForSequenceClassification.get_encoder: ForSequenceClassification#get_encoder().
  Olmo3ForSequenceClassification.get_decoder: ForSequenceClassification#get_decoder().
  Olmo3ForSequenceClassification.get_lm_head: ForSequenceClassification#get_lm_head().
  Olmo3ForSequenceClassification.get_embedding: ForSequenceClassification#get_embedding().
---
# Module: [`easydel/modules/olmo3/modeling_olmo3.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py)

## Classes
### `Olmo3Attention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/olmo3/modeling_olmo3.py:167`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L167)
- doc: Multi-head attention layer with Q/K normalization for OLMo-3 models.
- signature: `class Olmo3Attention(UnifiedAttention):`
- members:
  - `__init__(self, config: Olmo3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L185`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L185) — Initialize OLMo-3 attention with Q/K normalization and per-layer attention type.
  - `_create_k_norm(self, config: Olmo3Config, dtype: jnp.dtype, param_dtype: jnp.dtype, rngs: nn.Rngs)` — [`L253`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L253) — Create key normalization layer using RMSNorm.
  - `_create_q_norm(self, config: Olmo3Config, dtype: jnp.dtype, param_dtype: jnp.dtype, rngs: nn.Rngs)` — [`L232`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L232) — Create query normalization layer using RMSNorm.
  - `_preprocess_qkv(self, query_states, key_states, value_states)` — [`L274`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L274) — Apply Q/K normalization before attention computation.
  - `attention_type_name` — [`L213`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L213)
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`Olmo3Config`](olmo3_configuration.md#Olmo3Config), [`key_normalization`](../../layers/attention/_unified.md#UnifiedAttention.key_normalization), [`query_normalization`](../../layers/attention/_unified.md#UnifiedAttention.query_normalization), [`layer_types`](olmo3_configuration.md#Olmo3Config.layer_types), [`rms_norm_eps`](olmo3_configuration.md#Olmo3Config.rms_norm_eps), [`num_attention_heads`](olmo3_configuration.md#Olmo3Config.num_attention_heads), [`num_key_value_heads`](olmo3_configuration.md#Olmo3Config.num_key_value_heads), [`sliding_window`](olmo3_configuration.md#Olmo3Config.sliding_window)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_k_norm`](../../layers/attention/_unified.md#UnifiedAttention._create_k_norm), [`_create_q_norm`](../../layers/attention/_unified.md#UnifiedAttention._create_q_norm), [`_preprocess_qkv`](../../layers/attention/_unified.md#UnifiedAttention._preprocess_qkv), [`self_attn`](modeling_olmo3.md#Olmo3DecoderLayer.self_attn)

### `Olmo3DecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/olmo3/modeling_olmo3.py:293`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L293)
- doc: OLMo-3 Transformer Decoder Layer.
- signature: `class Olmo3DecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L370`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L370) — Forward pass of the Olmo3DecoderLayer with post-normalization architecture.
  - `__init__(self, config: Olmo3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L313`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L313) — Initializes the Olmo3DecoderLayer.
  - `config` — [`L333`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L333)
  - `dtype` — [`L335`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L335)
  - `layer_idx` — [`L334`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L334)
  - `mlp` — [`L347`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L347)
  - `param_dtype` — [`L336`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L336)
  - `post_attention_layernorm` — [`L355`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L355)
  - `post_feedforward_layernorm` — [`L362`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L362)
  - `precision` — [`L337`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L337)
  - `self_attn` — [`L339`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L339)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`Olmo3Config`](olmo3_configuration.md#Olmo3Config), [`hidden_size`](olmo3_configuration.md#Olmo3Config.hidden_size), [`rms_norm_eps`](olmo3_configuration.md#Olmo3Config.rms_norm_eps), [`Olmo3Attention`](modeling_olmo3.md#Olmo3Attention), [`Olmo3MLP`](modeling_olmo3.md#Olmo3MLP), [`scan_mlp_chunk_size`](olmo3_configuration.md#Olmo3Config.scan_mlp_chunk_size), [`use_scan_mlp`](olmo3_configuration.md#Olmo3Config.use_scan_mlp)
- used by: [`embed_tokens`](modeling_olmo3.md#Olmo3Model.embed_tokens)

### `Olmo3ForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/olmo3/modeling_olmo3.py:706`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L706)
- doc: OLMo-3 model with a language modeling head for causal language modeling tasks.
- signature: `class Olmo3ForCausalLM(BaseCausalLMModule[Olmo3Model, Olmo3Config]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L754`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L754) — Forward pass of the Olmo3ForCausalLM model for next-token prediction.
  - `__init__(self, config: Olmo3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L725`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L725) — Initialize OLMo-3 model for causal language modeling.
  - `get_decoder(self)` — [`L847`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L847) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L859`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L859) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L840`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L840) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L853`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L853) — Returns the language model head of the module.
- protocol/private: `_config_class`[`L723`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L723), `_model_type`[`L722`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L722), `_task_type`[`L721`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L721)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`CausalLMOutput`](../../infra/modeling_outputs.md#CausalLMOutput), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`compute_lm_logits`](../_base/causal_lm_module.md#BaseCausalLMModule.compute_lm_logits), [`Olmo3Config`](olmo3_configuration.md#Olmo3Config), [`Olmo3Model`](modeling_olmo3.md#Olmo3Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.get_lm_head)

### `Olmo3ForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/olmo3/modeling_olmo3.py:867`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L867)
- doc: OLMo-3 model for sequence classification tasks.
- signature: `class Olmo3ForSequenceClassification(BaseSequenceClassificationModule[Olmo3Model, Olmo3Config]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L916`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L916) — Forward pass of the Olmo3ForSequenceClassification model for sequence classification.
  - `__init__(self, config: Olmo3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L886`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L886) — Initialize OLMo-3 model for sequence classification.
  - `get_decoder(self)` — [`L1018`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L1018) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L1031`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L1031) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L1011`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L1011) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L1024`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L1024) — Returns the language model head of the module.
- protocol/private: `_config_class`[`L884`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L884), `_model_type`[`L883`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L883), `_task_type`[`L882`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L882)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), `pad_token_id`, [`SequenceClassifierOutput`](../../infra/modeling_outputs.md#SequenceClassifierOutput), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`Olmo3Config`](olmo3_configuration.md#Olmo3Config), [`Olmo3Model`](modeling_olmo3.md#Olmo3Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_lm_head)

### `Olmo3MLP`  ·  implements/extends Module
- def: [`easydel/modules/olmo3/modeling_olmo3.py:53`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L53)
- doc: OLMo-3 MLP module.
- signature: `class Olmo3MLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L127) — Forward pass of the Olmo3MLP module implementing a Gated Linear Unit structure.
  - `__init__(self, config: Olmo3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L70`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L70) — Initializes the Olmo3MLP module.
  - `act_fn` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L125)
  - `config` — [`L88`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L88)
  - `down_proj` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L115)
  - `dtype` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L89)
  - `gate_proj` — [`L110`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L110)
  - `param_dtype` — [`L90`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L90)
  - `precision` — [`L91`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L91)
  - `up_proj` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L120)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`Olmo3Config`](olmo3_configuration.md#Olmo3Config), [`hidden_size`](olmo3_configuration.md#Olmo3Config.hidden_size), [`initializer_range`](olmo3_configuration.md#Olmo3Config.initializer_range), [`intermediate_size`](olmo3_configuration.md#Olmo3Config.intermediate_size), [`hidden_act`](olmo3_configuration.md#Olmo3Config.hidden_act)
- used by: [`mlp`](modeling_olmo3.md#Olmo3DecoderLayer.mlp)

### `Olmo3Model`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/olmo3/modeling_olmo3.py:462`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L462)
- doc: The base OLMo-3 model transformer.
- signature: `class Olmo3Model(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L543`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L543) — Forward pass of the Olmo3Model base transformer.
  - `__init__(self, config: Olmo3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L481`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L481) — Initializes the Olmo3Model.
  - `get_decoder(self)` — [`L685`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L685) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L698`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L698) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L678`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L678) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L691`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L691) — Returns the language model head of the module.
  - `embed_tokens` — [`L507`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L507)
  - `layers` — [`L522`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L522)
  - `norm` — [`L535`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo3/modeling_olmo3.py#L535)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`Olmo3Config`](olmo3_configuration.md#Olmo3Config), [`hidden_size`](olmo3_configuration.md#Olmo3Config.hidden_size), [`rms_norm_eps`](olmo3_configuration.md#Olmo3Config.rms_norm_eps), [`initializer_range`](olmo3_configuration.md#Olmo3Config.initializer_range), [`Olmo3DecoderLayer`](modeling_olmo3.md#Olmo3DecoderLayer), [`gradient_checkpointing`](olmo3_configuration.md#Olmo3Config.gradient_checkpointing), [`vocab_size`](olmo3_configuration.md#Olmo3Config.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`Olmo3ForCausalLM`](modeling_olmo3.md#Olmo3ForCausalLM), [`Olmo3ForSequenceClassification`](modeling_olmo3.md#Olmo3ForSequenceClassification), [`__init__`](modeling_olmo3.md#Olmo3ForCausalLM.__init__), [`__init__`](modeling_olmo3.md#Olmo3ForSequenceClassification.__init__)

