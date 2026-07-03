---
title: 'Module: easydel/modules/olmo2/modeling_olmo2.py'
type: catalog
provenance: extracted
module: easydel/modules/olmo2/modeling_olmo2.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.olmo2.modeling_olmo2`/Olmo2
symbols:
  Olmo2Model.__call__: Model#__call__().
  Olmo2DecoderLayer.__call__: DecoderLayer#__call__().
  Olmo2ForCausalLM.__call__: ForCausalLM#__call__().
  Olmo2ForSequenceClassification.__call__: ForSequenceClassification#__call__().
  Olmo2Model.embed_tokens: Model#embed_tokens.
  Olmo2Model: Model#
  Olmo2ForCausalLM: ForCausalLM#
  Olmo2ForSequenceClassification: ForSequenceClassification#
  Olmo2MLP.__call__: MLP#__call__().
  Olmo2Attention._create_k_norm: Attention#_create_k_norm().
  Olmo2Attention._create_q_norm: Attention#_create_q_norm().
  Olmo2MLP.act_fn: MLP#act_fn.
  Olmo2DecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  Olmo2DecoderLayer.post_feedforward_layernorm: DecoderLayer#post_feedforward_layernorm.
  Olmo2Model.norm: Model#norm.
  Olmo2MLP.precision: MLP#precision.
  Olmo2ForCausalLM.__init__: ForCausalLM#__init__().
  Olmo2ForSequenceClassification.__init__: ForSequenceClassification#__init__().
  Olmo2MLP.gate_proj: MLP#gate_proj.
  Olmo2MLP.down_proj: MLP#down_proj.
  Olmo2MLP.up_proj: MLP#up_proj.
  Olmo2Attention.__init__: Attention#__init__().
  Olmo2Attention._preprocess_qkv: Attention#_preprocess_qkv().
  Olmo2Model.__init__: Model#__init__().
  Olmo2ForCausalLM._task_type: ForCausalLM#_task_type.
  Olmo2ForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  Olmo2DecoderLayer.mlp: DecoderLayer#mlp.
  Olmo2Model.layers: Model#layers.
  Olmo2Attention: Attention#
  Olmo2DecoderLayer.self_attn: DecoderLayer#self_attn.
  Olmo2MLP.config: MLP#config.
  Olmo2MLP.__init__: MLP#__init__().
  Olmo2DecoderLayer.__init__: DecoderLayer#__init__().
  Olmo2Model.get_embedding: Model#get_embedding().
  Olmo2ForCausalLM._config_class: ForCausalLM#_config_class.
  Olmo2ForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  Olmo2DecoderLayer.config: DecoderLayer#config.
  Olmo2MLP: MLP#
  Olmo2DecoderLayer: DecoderLayer#
  Olmo2MLP.dtype: MLP#dtype.
  Olmo2MLP.param_dtype: MLP#param_dtype.
  Olmo2DecoderLayer.dtype: DecoderLayer#dtype.
  Olmo2DecoderLayer.param_dtype: DecoderLayer#param_dtype.
  Olmo2DecoderLayer.precision: DecoderLayer#precision.
  Olmo2Model.get_encoder: Model#get_encoder().
  Olmo2Model.get_decoder: Model#get_decoder().
  Olmo2Model.get_lm_head: Model#get_lm_head().
  Olmo2ForCausalLM._model_type: ForCausalLM#_model_type.
  Olmo2ForCausalLM.get_encoder: ForCausalLM#get_encoder().
  Olmo2ForCausalLM.get_decoder: ForCausalLM#get_decoder().
  Olmo2ForCausalLM.get_lm_head: ForCausalLM#get_lm_head().
  Olmo2ForCausalLM.get_embedding: ForCausalLM#get_embedding().
  Olmo2ForSequenceClassification._model_type: ForSequenceClassification#_model_type.
  Olmo2ForSequenceClassification.get_encoder: ForSequenceClassification#get_encoder().
  Olmo2ForSequenceClassification.get_decoder: ForSequenceClassification#get_decoder().
  Olmo2ForSequenceClassification.get_lm_head: ForSequenceClassification#get_lm_head().
  Olmo2ForSequenceClassification.get_embedding: ForSequenceClassification#get_embedding().
---
# Module: [`easydel/modules/olmo2/modeling_olmo2.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py)

## Classes
### `Olmo2Attention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/olmo2/modeling_olmo2.py:167`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L167)
- doc: Multi-head attention layer with Q/K normalization for OLMo-2 models.
- signature: `class Olmo2Attention(UnifiedAttention):`
- members:
  - `__init__(self, config: Olmo2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L180`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L180) — Initialize OLMo-2 attention layer with Q/K normalization.
  - `_create_k_norm(self, config: Olmo2Config, dtype: jnp.dtype, param_dtype: jnp.dtype, rngs: nn.Rngs)` — [`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L212) — Create key normalization layer using RMSNorm.
  - `_create_q_norm(self, config: Olmo2Config, dtype: jnp.dtype, param_dtype: jnp.dtype, rngs: nn.Rngs)` — [`L232`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L232) — Create query normalization layer using RMSNorm. — documented in [easydel-layers-norms-_norms](../../../../concepts/easydel-layers-norms-_norms.md)
  - `_preprocess_qkv(self, query_states, key_states, value_states)` — [`L252`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L252) — Apply Q/K normalization before attention computation.
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`config`](../../layers/attention/_flexible.md#AttentionModule.config), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`Olmo2Config`](olmo2_configuration.md#Olmo2Config), [`key_normalization`](../../layers/attention/_unified.md#UnifiedAttention.key_normalization), [`query_normalization`](../../layers/attention/_unified.md#UnifiedAttention.query_normalization), [`rms_norm_eps`](olmo2_configuration.md#Olmo2Config.rms_norm_eps)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_k_norm`](../../layers/attention/_unified.md#UnifiedAttention._create_k_norm), [`_create_q_norm`](../../layers/attention/_unified.md#UnifiedAttention._create_q_norm), [`_preprocess_qkv`](../../layers/attention/_unified.md#UnifiedAttention._preprocess_qkv), [`self_attn`](modeling_olmo2.md#Olmo2DecoderLayer.self_attn)

### `Olmo2DecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/olmo2/modeling_olmo2.py:269`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L269)
- doc: OLMo-2 Transformer Decoder Layer.
- signature: `class Olmo2DecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L343`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L343) — Forward pass of the Olmo2DecoderLayer with post-normalization architecture.
  - `__init__(self, config: Olmo2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L288`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L288) — Initializes the Olmo2DecoderLayer.
  - `config` — [`L307`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L307)
  - `dtype` — [`L308`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L308)
  - `mlp` — [`L320`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L320)
  - `param_dtype` — [`L309`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L309)
  - `post_attention_layernorm` — [`L328`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L328)
  - `post_feedforward_layernorm` — [`L335`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L335)
  - `precision` — [`L310`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L310)
  - `self_attn` — [`L312`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L312)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`Olmo2Config`](olmo2_configuration.md#Olmo2Config), [`hidden_size`](olmo2_configuration.md#Olmo2Config.hidden_size), [`rms_norm_eps`](olmo2_configuration.md#Olmo2Config.rms_norm_eps), [`Olmo2Attention`](modeling_olmo2.md#Olmo2Attention), [`Olmo2MLP`](modeling_olmo2.md#Olmo2MLP), [`scan_mlp_chunk_size`](olmo2_configuration.md#Olmo2Config.scan_mlp_chunk_size), [`use_scan_mlp`](olmo2_configuration.md#Olmo2Config.use_scan_mlp)
- used by: [`embed_tokens`](modeling_olmo2.md#Olmo2Model.embed_tokens)

### `Olmo2ForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/olmo2/modeling_olmo2.py:676`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L676)
- doc: OLMo-2 model with a language modeling head for causal language modeling tasks.
- signature: `class Olmo2ForCausalLM(BaseCausalLMModule[Olmo2Model, Olmo2Config]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L723`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L723) — Forward pass of the Olmo2ForCausalLM model for next-token prediction.
  - `__init__(self, config: Olmo2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L694`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L694) — Initialize OLMo-2 model for causal language modeling.
  - `get_decoder(self)` — [`L816`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L816) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L828`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L828) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L809`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L809) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L822`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L822) — Returns the language model head of the module.
- protocol/private: `_config_class`[`L692`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L692), `_model_type`[`L691`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L691), `_task_type`[`L690`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L690)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`CausalLMOutput`](../../infra/modeling_outputs.md#CausalLMOutput), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`compute_lm_logits`](../_base/causal_lm_module.md#BaseCausalLMModule.compute_lm_logits), [`Olmo2Config`](olmo2_configuration.md#Olmo2Config), [`Olmo2Model`](modeling_olmo2.md#Olmo2Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.get_lm_head)

### `Olmo2ForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/olmo2/modeling_olmo2.py:836`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L836)
- doc: OLMo-2 model for sequence classification tasks.
- signature: `class Olmo2ForSequenceClassification(BaseSequenceClassificationModule[Olmo2Model, Olmo2Config]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L884`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L884) — Forward pass of the Olmo2ForSequenceClassification model for sequence classification.
  - `__init__(self, config: Olmo2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L854`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L854) — Initialize OLMo-2 model for sequence classification.
  - `get_decoder(self)` — [`L986`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L986) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L999`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L999) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L979`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L979) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L992`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L992) — Returns the language model head of the module.
- protocol/private: `_config_class`[`L852`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L852), `_model_type`[`L851`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L851), `_task_type`[`L850`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L850)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), `pad_token_id`, [`SequenceClassifierOutput`](../../infra/modeling_outputs.md#SequenceClassifierOutput), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`Olmo2Config`](olmo2_configuration.md#Olmo2Config), [`Olmo2Model`](modeling_olmo2.md#Olmo2Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_lm_head)

### `Olmo2MLP`  ·  implements/extends Module
- def: [`easydel/modules/olmo2/modeling_olmo2.py:53`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L53)
- doc: OLMo-2 MLP module.
- signature: `class Olmo2MLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L127) — Forward pass of the Olmo2MLP module implementing a Gated Linear Unit structure.
  - `__init__(self, config: Olmo2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L70`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L70) — Initializes the Olmo2MLP module.
  - `act_fn` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L125)
  - `config` — [`L88`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L88)
  - `down_proj` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L115)
  - `dtype` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L89)
  - `gate_proj` — [`L110`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L110)
  - `param_dtype` — [`L90`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L90)
  - `precision` — [`L91`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L91)
  - `up_proj` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L120)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`Olmo2Config`](olmo2_configuration.md#Olmo2Config), [`hidden_size`](olmo2_configuration.md#Olmo2Config.hidden_size), [`initializer_range`](olmo2_configuration.md#Olmo2Config.initializer_range), [`intermediate_size`](olmo2_configuration.md#Olmo2Config.intermediate_size), [`hidden_act`](olmo2_configuration.md#Olmo2Config.hidden_act)
- used by: [`mlp`](modeling_olmo2.md#Olmo2DecoderLayer.mlp)

### `Olmo2Model`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/olmo2/modeling_olmo2.py:433`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L433)
- doc: The base OLMo-2 model transformer.
- signature: `class Olmo2Model(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L514`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L514) — Forward pass of the Olmo2Model base transformer.
  - `__init__(self, config: Olmo2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L452`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L452) — Initializes the Olmo2Model.
  - `get_decoder(self)` — [`L655`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L655) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L668`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L668) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L648`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L648) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L661`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L661) — Returns the language model head of the module.
  - `embed_tokens` — [`L478`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L478)
  - `layers` — [`L493`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L493)
  - `norm` — [`L506`](../../../../../../../raw/code/EasyDeL/easydel/modules/olmo2/modeling_olmo2.py#L506)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`Olmo2Config`](olmo2_configuration.md#Olmo2Config), [`hidden_size`](olmo2_configuration.md#Olmo2Config.hidden_size), [`rms_norm_eps`](olmo2_configuration.md#Olmo2Config.rms_norm_eps), [`initializer_range`](olmo2_configuration.md#Olmo2Config.initializer_range), [`Olmo2DecoderLayer`](modeling_olmo2.md#Olmo2DecoderLayer), [`gradient_checkpointing`](olmo2_configuration.md#Olmo2Config.gradient_checkpointing), [`vocab_size`](olmo2_configuration.md#Olmo2Config.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`Olmo2ForCausalLM`](modeling_olmo2.md#Olmo2ForCausalLM), [`Olmo2ForSequenceClassification`](modeling_olmo2.md#Olmo2ForSequenceClassification), [`__init__`](modeling_olmo2.md#Olmo2ForCausalLM.__init__), [`__init__`](modeling_olmo2.md#Olmo2ForSequenceClassification.__init__)

