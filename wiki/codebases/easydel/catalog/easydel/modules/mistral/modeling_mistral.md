---
title: 'Module: easydel/modules/mistral/modeling_mistral.py'
type: catalog
provenance: extracted
module: easydel/modules/mistral/modeling_mistral.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.mistral.modeling_mistral`/
symbols:
  MistralModel.__call__: MistralModel#__call__().
  MistralDecoderLayer.__call__: MistralDecoderLayer#__call__().
  MistralForCausalLM.__call__: MistralForCausalLM#__call__().
  MistralForSequenceClassification.__call__: MistralForSequenceClassification#__call__().
  MistralModel.embed_tokens: MistralModel#embed_tokens.
  MistralModel: MistralModel#
  MistralForCausalLM: MistralForCausalLM#
  MistralForSequenceClassification: MistralForSequenceClassification#
  MistralMLP.__call__: MistralMLP#__call__().
  MistralMLP.precision: MistralMLP#precision.
  MistralMLP.act_fn: MistralMLP#act_fn.
  MistralDecoderLayer.input_layernorm: MistralDecoderLayer#input_layernorm.
  MistralDecoderLayer.post_attention_layernorm: MistralDecoderLayer#post_attention_layernorm.
  MistralModel.norm: MistralModel#norm.
  MistralAttention.__init__: MistralAttention#__init__().
  MistralAttention._create_rotary: MistralAttention#_create_rotary().
  MistralForCausalLM.__init__: MistralForCausalLM#__init__().
  MistralForSequenceClassification.__init__: MistralForSequenceClassification#__init__().
  MistralMLP.gate_proj: MistralMLP#gate_proj.
  MistralMLP.down_proj: MistralMLP#down_proj.
  MistralMLP.up_proj: MistralMLP#up_proj.
  MistralModel.__init__: MistralModel#__init__().
  MistralForCausalLM._task_type: MistralForCausalLM#_task_type.
  MistralForSequenceClassification._task_type: MistralForSequenceClassification#_task_type.
  MistralDecoderLayer.mlp: MistralDecoderLayer#mlp.
  MistralModel.layers: MistralModel#layers.
  MistralAttention: MistralAttention#
  MistralDecoderLayer.self_attn: MistralDecoderLayer#self_attn.
  MistralMLP.config: MistralMLP#config.
  MistralMLP.__init__: MistralMLP#__init__().
  MistralDecoderLayer.__init__: MistralDecoderLayer#__init__().
  MistralModel.get_embedding: MistralModel#get_embedding().
  MistralForCausalLM._config_class: MistralForCausalLM#_config_class.
  MistralForSequenceClassification._config_class: MistralForSequenceClassification#_config_class.
  MistralDecoderLayer.config: MistralDecoderLayer#config.
  MistralMLP: MistralMLP#
  MistralDecoderLayer: MistralDecoderLayer#
  logger: logger.
  MistralMLP.dtype: MistralMLP#dtype.
  MistralMLP.param_dtype: MistralMLP#param_dtype.
  MistralDecoderLayer.dtype: MistralDecoderLayer#dtype.
  MistralDecoderLayer.param_dtype: MistralDecoderLayer#param_dtype.
  MistralDecoderLayer.precision: MistralDecoderLayer#precision.
  MistralModel.get_encoder: MistralModel#get_encoder().
  MistralModel.get_decoder: MistralModel#get_decoder().
  MistralModel.get_lm_head: MistralModel#get_lm_head().
  MistralForCausalLM._model_type: MistralForCausalLM#_model_type.
  MistralForCausalLM.get_encoder: MistralForCausalLM#get_encoder().
  MistralForCausalLM.get_decoder: MistralForCausalLM#get_decoder().
  MistralForCausalLM.get_lm_head: MistralForCausalLM#get_lm_head().
  MistralForCausalLM.get_embedding: MistralForCausalLM#get_embedding().
  MistralForSequenceClassification._model_type: MistralForSequenceClassification#_model_type.
  MistralForSequenceClassification.get_encoder: MistralForSequenceClassification#get_encoder().
  MistralForSequenceClassification.get_decoder: MistralForSequenceClassification#get_decoder().
  MistralForSequenceClassification.get_lm_head: MistralForSequenceClassification#get_lm_head().
  MistralForSequenceClassification.get_embedding: MistralForSequenceClassification#get_embedding().
---
# Module: [`easydel/modules/mistral/modeling_mistral.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py)

## Classes
### `MistralAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/mistral/modeling_mistral.py:147`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L147)
- doc: Multi-head attention layer with RoPE embeddings for Mistral models.
- signature: `class MistralAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: MistralConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L155) — Initialize Mistral attention layer with sliding window and grouped-query attention support.
  - `_create_rotary(self, config: MistralConfig, dtype: jnp.dtype)` — [`L189`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L189) — Create Mistral-specific rotary embedding layer.
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`get_basic_rope`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_rope), [`MistralConfig`](mistral_configuration.md#MistralConfig), [`sliding_window`](mistral_configuration.md#MistralConfig.sliding_window)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`self_attn`](modeling_mistral.md#MistralDecoderLayer.self_attn)

### `MistralDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/mistral/modeling_mistral.py:194`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L194)
- doc: Single decoder layer for Mistral models.
- signature: `class MistralDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L256`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L256) — Forward pass through the decoder layer.
  - `__init__(self, config: MistralConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L201) — Initialize Mistral decoder layer.
  - `config` — [`L221`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L221)
  - `dtype` — [`L222`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L222)
  - `input_layernorm` — [`L241`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L241)
  - `mlp` — [`L234`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L234)
  - `param_dtype` — [`L223`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L223)
  - `post_attention_layernorm` — [`L248`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L248)
  - `precision` — [`L224`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L224)
  - `self_attn` — [`L226`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L226)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`MistralConfig`](mistral_configuration.md#MistralConfig), [`hidden_size`](mistral_configuration.md#MistralConfig.hidden_size), [`MistralAttention`](modeling_mistral.md#MistralAttention), [`rms_norm_eps`](mistral_configuration.md#MistralConfig.rms_norm_eps), [`MistralMLP`](modeling_mistral.md#MistralMLP), [`scan_mlp_chunk_size`](mistral_configuration.md#MistralConfig.scan_mlp_chunk_size), [`use_scan_mlp`](mistral_configuration.md#MistralConfig.use_scan_mlp)
- used by: [`embed_tokens`](modeling_mistral.md#MistralModel.embed_tokens)

### `MistralForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/mistral/modeling_mistral.py:541`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L541)
- doc: Mistral model with a language modeling head for causal language modeling tasks.
- signature: `class MistralForCausalLM(BaseCausalLMModule[MistralModel, MistralConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L587`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L587) — Forward pass through the Mistral model for causal language modeling.
  - `__init__(self, config: MistralConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L558`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L558) — Initialize Mistral model for causal language modeling.
  - `get_decoder(self)` — [`L671`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L671) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L683`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L683) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L664`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L664) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L677`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L677) — Returns the language model head of the module.
- protocol/private: `_config_class`[`L556`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L556), `_model_type`[`L555`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L555), `_task_type`[`L554`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L554)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`CausalLMOutput`](../../infra/modeling_outputs.md#CausalLMOutput), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`compute_lm_logits`](../_base/causal_lm_module.md#BaseCausalLMModule.compute_lm_logits), [`MistralConfig`](mistral_configuration.md#MistralConfig), [`MistralModel`](modeling_mistral.md#MistralModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.get_lm_head)

### `MistralForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/mistral/modeling_mistral.py:691`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L691)
- doc: Mistral model for sequence classification tasks.
- signature: `class MistralForSequenceClassification(BaseSequenceClassificationModule[MistralModel, MistralConfig]):`
- members:
  - `__call__(self, input_ids: Array | None = None, inputs_embeds: Array | None = None, attention_mask: Array | None = None, mask_info: MaskInfo | None = None, position_ids: Array | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L738`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L738) — Forward pass through the Mistral model for sequence classification.
  - `__init__(self, config: MistralConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L708`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L708) — Initialize Mistral model for sequence classification.
  - `get_decoder(self)` — [`L828`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L828) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L841`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L841) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L821`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L821) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L834`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L834) — Returns the language model head of the module.
- protocol/private: `_config_class`[`L706`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L706), `_model_type`[`L705`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L705), `_task_type`[`L704`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L704)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), `pad_token_id`, [`SequenceClassifierOutput`](../../infra/modeling_outputs.md#SequenceClassifierOutput), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`MistralConfig`](mistral_configuration.md#MistralConfig), [`MistralModel`](modeling_mistral.md#MistralModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_lm_head)

### `MistralMLP`  ·  implements/extends Module
- def: [`easydel/modules/mistral/modeling_mistral.py:55`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L55)
- doc: Multi-Layer Perceptron module for Mistral models.
- signature: `class MistralMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L120) — Apply SiLU feedforward transformation.
  - `__init__(self, config: MistralConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L62`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L62) — Initialize Mistral MLP block.
  - `act_fn` — [`L118`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L118)
  - `config` — [`L81`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L81)
  - `down_proj` — [`L108`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L108)
  - `dtype` — [`L82`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L82)
  - `gate_proj` — [`L103`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L103)
  - `param_dtype` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L83)
  - `precision` — [`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L84)
  - `up_proj` — [`L113`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L113)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`MistralConfig`](mistral_configuration.md#MistralConfig), [`hidden_size`](mistral_configuration.md#MistralConfig.hidden_size), [`initializer_range`](mistral_configuration.md#MistralConfig.initializer_range), [`intermediate_size`](mistral_configuration.md#MistralConfig.intermediate_size), [`hidden_act`](mistral_configuration.md#MistralConfig.hidden_act)
- used by: [`mlp`](modeling_mistral.md#MistralDecoderLayer.mlp)

### `MistralModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/mistral/modeling_mistral.py:315`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L315)
- doc: Mistral model implementation.
- signature: `class MistralModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L390`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L390) — Forward pass through the Mistral base model.
  - `__init__(self, config: MistralConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L328`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L328) — Initialize Mistral base model.
  - `get_decoder(self)` — [`L520`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L520) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L533`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L533) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L513`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L513) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L526`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L526) — Returns the language model head of the module.
  - `embed_tokens` — [`L354`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L354)
  - `layers` — [`L369`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L369)
  - `norm` — [`L382`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L382)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`MistralConfig`](mistral_configuration.md#MistralConfig), [`hidden_size`](mistral_configuration.md#MistralConfig.hidden_size), [`initializer_range`](mistral_configuration.md#MistralConfig.initializer_range), [`rms_norm_eps`](mistral_configuration.md#MistralConfig.rms_norm_eps), [`MistralDecoderLayer`](modeling_mistral.md#MistralDecoderLayer), [`gradient_checkpointing`](mistral_configuration.md#MistralConfig.gradient_checkpointing), [`vocab_size`](mistral_configuration.md#MistralConfig.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`MistralForCausalLM`](modeling_mistral.md#MistralForCausalLM), [`MistralForSequenceClassification`](modeling_mistral.md#MistralForSequenceClassification), [`__init__`](modeling_mistral.md#MistralForCausalLM.__init__), [`__init__`](modeling_mistral.md#MistralForSequenceClassification.__init__)

## Module values
- `logger` — [`L52`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral/modeling_mistral.py#L52)

