---
title: 'Module: easydel/modules/qwen3_moe/modeling_qwen3_moe.py'
type: catalog
provenance: extracted
module: easydel/modules/qwen3_moe/modeling_qwen3_moe.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.qwen3_moe.modeling_qwen3_moe`/Qwen3Moe
symbols:
  Qwen3MoeModel.__call__: Model#__call__().
  Qwen3MoeDecoderLayer.__call__: DecoderLayer#__call__().
  Qwen3MoeSparseBlock.__init__: SparseBlock#__init__().
  Qwen3MoeForCausalLM.__call__: ForCausalLM#__call__().
  Qwen3MoeForSequenceClassification.__call__: ForSequenceClassification#__call__().
  Qwen3MoeModel.embed_tokens: Model#embed_tokens.
  Qwen3MoeSparseBlock.__call__: SparseBlock#__call__().
  Qwen3MoeModel: Model#
  Qwen3MoeMLPStack.gate_proj: MLPStack#gate_proj.
  Qwen3MoeMLPStack.down_proj: MLPStack#down_proj.
  Qwen3MoeMLPStack.up_proj: MLPStack#up_proj.
  Qwen3MoeForCausalLM: ForCausalLM#
  Qwen3MoeForSequenceClassification: ForSequenceClassification#
  Qwen3MoeMLP.__call__: MLP#__call__().
  Qwen3MoeAttention.__init__: Attention#__init__().
  Qwen3MoeDecoderLayer.is_moe: DecoderLayer#is_moe.
  Qwen3MoeSparseBlock.gate: SparseBlock#gate.
  Qwen3MoeDecoderLayer.input_layernorm: DecoderLayer#input_layernorm.
  Qwen3MoeDecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  Qwen3MoeMLPStack.__call__: MLPStack#__call__().
  Qwen3MoeMLP.precision: MLP#precision.
  Qwen3MoeDecoderLayer.mlp: DecoderLayer#mlp.
  Qwen3MoeMLP.act_fn: MLP#act_fn.
  Qwen3MoeModel.norm: Model#norm.
  Qwen3MoeSparseBlock.experts: SparseBlock#experts.
  Qwen3MoeForCausalLM.__init__: ForCausalLM#__init__().
  Qwen3MoeForSequenceClassification.__init__: ForSequenceClassification#__init__().
  Qwen3MoeMLPStack.act_fn: MLPStack#act_fn.
  Qwen3MoeForCausalLM._compute_aux_loss: ForCausalLM#_compute_aux_loss().
  Qwen3MoeAttention._postprocess_qkv: Attention#_postprocess_qkv().
  Qwen3MoeModel.__init__: Model#__init__().
  Qwen3MoeForCausalLM._task_type: ForCausalLM#_task_type.
  Qwen3MoeForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  Qwen3MoeModel.layers: Model#layers.
  Qwen3MoeMLP.gate_proj: MLP#gate_proj.
  Qwen3MoeMLP.down_proj: MLP#down_proj.
  Qwen3MoeMLP.up_proj: MLP#up_proj.
  Qwen3MoeSparseBlock: SparseBlock#
  Qwen3MoeAttention: Attention#
  Qwen3MoeDecoderLayer.self_attn: DecoderLayer#self_attn.
  Qwen3MoeMLP.config: MLP#config.
  Qwen3MoeMLPStack.__init__: MLPStack#__init__().
  Qwen3MoeMLP.__init__: MLP#__init__().
  Qwen3MoeDecoderLayer.__init__: DecoderLayer#__init__().
  Qwen3MoeModel.get_embedding: Model#get_embedding().
  Qwen3MoeForCausalLM._config_class: ForCausalLM#_config_class.
  Qwen3MoeForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  Qwen3MoeDecoderLayer.config: DecoderLayer#config.
  Qwen3MoeMLPStack: MLPStack#
  Qwen3MoeMLP: MLP#
  Qwen3MoeDecoderLayer: DecoderLayer#
  Qwen3MoeMLPStack.reform_param: MLPStack#reform_param.
  Qwen3MoeMLPStack.config: MLPStack#config.
  Qwen3MoeMLPStack.dtype: MLPStack#dtype.
  Qwen3MoeMLPStack.param_dtype: MLPStack#param_dtype.
  Qwen3MoeMLPStack.precision: MLPStack#precision.
  Qwen3MoeMLP.dtype: MLP#dtype.
  Qwen3MoeMLP.param_dtype: MLP#param_dtype.
  Qwen3MoeSparseBlock.config: SparseBlock#config.
  Qwen3MoeSparseBlock.dtype: SparseBlock#dtype.
  Qwen3MoeSparseBlock.param_dtype: SparseBlock#param_dtype.
  Qwen3MoeSparseBlock.precision: SparseBlock#precision.
  Qwen3MoeAttention.layer_idx: Attention#layer_idx.
  Qwen3MoeDecoderLayer.dtype: DecoderLayer#dtype.
  Qwen3MoeDecoderLayer.param_dtype: DecoderLayer#param_dtype.
  Qwen3MoeDecoderLayer.precision: DecoderLayer#precision.
  Qwen3MoeModel.get_encoder: Model#get_encoder().
  Qwen3MoeModel.get_decoder: Model#get_decoder().
  Qwen3MoeModel.get_lm_head: Model#get_lm_head().
  Qwen3MoeForCausalLM._model_type: ForCausalLM#_model_type.
  Qwen3MoeForSequenceClassification._model_type: ForSequenceClassification#_model_type.
  Qwen3MoeForSequenceClassification.get_encoder: ForSequenceClassification#get_encoder().
  Qwen3MoeForSequenceClassification.get_decoder: ForSequenceClassification#get_decoder().
  Qwen3MoeForSequenceClassification.get_lm_head: ForSequenceClassification#get_lm_head().
  Qwen3MoeForSequenceClassification.get_embedding: ForSequenceClassification#get_embedding().
  Qwen3MoeForSequenceClassification.get_task_head: ForSequenceClassification#get_task_head().
---
# Module: [`easydel/modules/qwen3_moe/modeling_qwen3_moe.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py)

## Classes
### `Qwen3MoeAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/qwen3_moe/modeling_qwen3_moe.py:351`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L351)
- doc: Multi-head attention layer with RoPE embeddings and Q/K normalization for Qwen3 MoE models.
- signature: `class Qwen3MoeAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: Qwen3MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L358`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L358) — Initialize Qwen3 MoE attention layer with grouped-query attention support.
  - `_postprocess_qkv(self, query_states, key_states, value_states)` — [`L401`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L401) — Apply Q/K normalization after computing query, key, and value projections.
  - `layer_idx` — [`L399`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L399)
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`Qwen3MoeConfig`](qwen3_moe_configuration.md#Qwen3MoeConfig), [`key_normalization`](../../layers/attention/_unified.md#UnifiedAttention.key_normalization), [`query_normalization`](../../layers/attention/_unified.md#UnifiedAttention.query_normalization), [`sliding_window`](qwen3_moe_configuration.md#Qwen3MoeConfig.sliding_window), [`max_window_layers`](qwen3_moe_configuration.md#Qwen3MoeConfig.max_window_layers), [`use_sliding_window`](qwen3_moe_configuration.md#Qwen3MoeConfig.use_sliding_window)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_postprocess_qkv`](../../layers/attention/_unified.md#UnifiedAttention._postprocess_qkv), [`self_attn`](modeling_qwen3_moe.md#Qwen3MoeDecoderLayer.self_attn)

### `Qwen3MoeDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/qwen3_moe/modeling_qwen3_moe.py:415`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L415)
- doc: Single decoder layer for Qwen3 MoE models.
- signature: `class Qwen3MoeDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, output_router_logits: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L489`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L489) — Forward pass through the decoder layer.
  - `__init__(self, config: Qwen3MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L422`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L422) — Initialize Qwen3 MoE decoder layer.
  - `config` — [`L442`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L442)
  - `dtype` — [`L443`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L443)
  - `input_layernorm` — [`L474`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L474)
  - `is_moe` — [`L455`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L455)
  - `mlp` — [`L459`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L459)
  - `param_dtype` — [`L444`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L444)
  - `post_attention_layernorm` — [`L481`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L481)
  - `precision` — [`L445`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L445)
  - `self_attn` — [`L447`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L447)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`Qwen3MoeConfig`](qwen3_moe_configuration.md#Qwen3MoeConfig), [`hidden_size`](qwen3_moe_configuration.md#Qwen3MoeConfig.hidden_size), [`num_experts`](qwen3_moe_configuration.md#Qwen3MoeConfig.num_experts), [`Qwen3MoeAttention`](modeling_qwen3_moe.md#Qwen3MoeAttention), [`Qwen3MoeSparseBlock`](modeling_qwen3_moe.md#Qwen3MoeSparseBlock), [`rms_norm_eps`](qwen3_moe_configuration.md#Qwen3MoeConfig.rms_norm_eps), [`Qwen3MoeMLP`](modeling_qwen3_moe.md#Qwen3MoeMLP), [`decoder_sparse_step`](qwen3_moe_configuration.md#Qwen3MoeConfig.decoder_sparse_step), [`mlp_only_layers`](qwen3_moe_configuration.md#Qwen3MoeConfig.mlp_only_layers)
- used by: [`embed_tokens`](modeling_qwen3_moe.md#Qwen3MoeModel.embed_tokens)

### `Qwen3MoeForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/qwen3_moe/modeling_qwen3_moe.py:784`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L784)
- doc: Qwen3 MoE model with a language modeling head for causal language modeling tasks.
- signature: `class Qwen3MoeForCausalLM(BaseCausalLMModule[Qwen3MoeModel, Qwen3MoeConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True)` — [`L832`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L832) — Forward pass through the Qwen3 MoE causal language model.
  - `__init__(self, config: Qwen3MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L802`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L802) — Initialize Qwen3 MoE model for causal language modeling.
  - `_compute_aux_loss(self, outputs, attention_mask)` — [`L883`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L883) — Compute auxiliary load balancing loss from router logits.
- protocol/private: `_config_class`[`L800`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L800), `_model_type`[`L799`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L799), `_task_type`[`L798`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L798)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`MoeCausalLMOutput`](../../infra/modeling_outputs.md#MoeCausalLMOutput), [`auxiliary_load_balancing_loss_func`](../../infra/loss_utils.md#auxiliary_load_balancing_loss_func), [`forward_moe`](../_base/causal_lm_module.md#BaseCausalLMModule.forward_moe), [`Qwen3MoeConfig`](qwen3_moe_configuration.md#Qwen3MoeConfig), [`Qwen3MoeModel`](modeling_qwen3_moe.md#Qwen3MoeModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `Qwen3MoeForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/qwen3_moe/modeling_qwen3_moe.py:905`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L905)
- doc: Qwen3 MoE model for sequence classification tasks.
- signature: `class Qwen3MoeForSequenceClassification(BaseSequenceClassificationModule[Qwen3MoeModel, Qwen3MoeConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L952`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L952) — Forward pass through the Qwen3 MoE sequence classification model.
  - `__init__(self, config: Qwen3MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L922`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L922) — Initialize Qwen3 MoE model for sequence classification.
  - `get_decoder(self)` — [`L1034`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L1034) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L1047`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L1047) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L1027`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L1027) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L1040`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L1040) — Returns the language model head of the module.
  - `get_task_head(self)` — [`L1053`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L1053) — Returns the sequence classification head.
- protocol/private: `_config_class`[`L920`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L920), `_model_type`[`L919`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L919), `_task_type`[`L918`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L918)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), `pad_token_id`, [`SequenceClassifierOutput`](../../infra/modeling_outputs.md#SequenceClassifierOutput), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`Qwen3MoeConfig`](qwen3_moe_configuration.md#Qwen3MoeConfig), [`Qwen3MoeModel`](modeling_qwen3_moe.md#Qwen3MoeModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_lm_head), [`get_task_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_task_head)

### `Qwen3MoeMLP`  ·  implements/extends Module
- def: [`easydel/modules/qwen3_moe/modeling_qwen3_moe.py:184`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L184)
- doc: Multi-Layer Perceptron module for Qwen3 MoE models.
- signature: `class Qwen3MoeMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L242`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L242) — Apply SwiGLU feedforward transformation.
  - `__init__(self, config: Qwen3MoeConfig, intermediate_size=None, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L192`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L192) — Initialize Qwen3 MoE MLP block.
  - `act_fn` — [`L240`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L240)
  - `config` — [`L214`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L214)
  - `down_proj` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L238)
  - `dtype` — [`L215`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L215)
  - `gate_proj` — [`L237`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L237)
  - `param_dtype` — [`L216`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L216)
  - `precision` — [`L217`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L217)
  - `up_proj` — [`L239`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L239)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`Qwen3MoeConfig`](qwen3_moe_configuration.md#Qwen3MoeConfig), [`hidden_size`](qwen3_moe_configuration.md#Qwen3MoeConfig.hidden_size), [`initializer_range`](qwen3_moe_configuration.md#Qwen3MoeConfig.initializer_range), [`hidden_act`](qwen3_moe_configuration.md#Qwen3MoeConfig.hidden_act), [`intermediate_size`](qwen3_moe_configuration.md#Qwen3MoeConfig.intermediate_size)
- used by: [`mlp`](modeling_qwen3_moe.md#Qwen3MoeDecoderLayer.mlp)

### `Qwen3MoeMLPStack`  ·  implements/extends Module
- def: [`easydel/modules/qwen3_moe/modeling_qwen3_moe.py:65`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L65)
- doc: Stacked MoE MLP module using ParallelMoELinear layers for Qwen3 MoE models.
- signature: `class Qwen3MoeMLPStack(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], group_sizes: Array, sorted_experts: Array | None = None)` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L160) — Apply SwiGLU feedforward transformation through MoE experts.
  - `__init__(self, config: Qwen3MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L97`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L97) — Initialize Qwen3 MoE MLP stack.
  - `act_fn` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L158)
  - `config` — [`L118`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L118)
  - `down_proj` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L134)
  - `dtype` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L119)
  - `gate_proj` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L122)
  - `param_dtype` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L120)
  - `precision` — [`L121`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L121)
  - `reform_param` — [`L72`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L72)
  - `up_proj` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L146)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`use_expert_tensor_mode`](../../infra/base_config.md#EasyDeLBaseConfig.use_expert_tensor_mode), [`ColumnParallelMoELinear`](../../layers/linears/_linear_moe.md#ColumnParallelMoELinear), [`RowParallelMoELinear`](../../layers/linears/_linear_moe.md#RowParallelMoELinear), [`Qwen3MoeConfig`](qwen3_moe_configuration.md#Qwen3MoeConfig), [`hidden_size`](qwen3_moe_configuration.md#Qwen3MoeConfig.hidden_size), [`num_experts`](qwen3_moe_configuration.md#Qwen3MoeConfig.num_experts), [`moe_intermediate_size`](qwen3_moe_configuration.md#Qwen3MoeConfig.moe_intermediate_size), [`hidden_act`](qwen3_moe_configuration.md#Qwen3MoeConfig.hidden_act)
- used by: [`__call__`](modeling_qwen3_moe.md#Qwen3MoeSparseBlock.__call__), [`experts`](modeling_qwen3_moe.md#Qwen3MoeSparseBlock.experts)

### `Qwen3MoeModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/qwen3_moe/modeling_qwen3_moe.py:552`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L552)
- doc: Qwen3 MoE model implementation.
- signature: `class Qwen3MoeModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None)` — [`L627`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L627) — Forward pass through the Qwen3 MoE base model.
  - `__init__(self, config: Qwen3MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L566`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L566) — Initialize Qwen3 MoE base model.
  - `get_decoder(self)` — [`L763`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L763) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L776`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L776) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L756`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L756) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L769`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L769) — Returns the language model head of the module.
  - `embed_tokens` — [`L592`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L592)
  - `layers` — [`L606`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L606)
  - `norm` — [`L619`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L619)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`MoeModelOutput`](../../infra/modeling_outputs.md#MoeModelOutput), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), `output_hidden_states`, [`gradient_checkpointing`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing), [`Qwen3MoeConfig`](qwen3_moe_configuration.md#Qwen3MoeConfig), [`hidden_size`](qwen3_moe_configuration.md#Qwen3MoeConfig.hidden_size), [`initializer_range`](qwen3_moe_configuration.md#Qwen3MoeConfig.initializer_range), [`num_hidden_layers`](qwen3_moe_configuration.md#Qwen3MoeConfig.num_hidden_layers), [`rms_norm_eps`](qwen3_moe_configuration.md#Qwen3MoeConfig.rms_norm_eps), [`Qwen3MoeDecoderLayer`](modeling_qwen3_moe.md#Qwen3MoeDecoderLayer), [`vocab_size`](qwen3_moe_configuration.md#Qwen3MoeConfig.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`Qwen3MoeForCausalLM`](modeling_qwen3_moe.md#Qwen3MoeForCausalLM), [`Qwen3MoeForSequenceClassification`](modeling_qwen3_moe.md#Qwen3MoeForSequenceClassification), [`__init__`](modeling_qwen3_moe.md#Qwen3MoeForCausalLM.__init__), [`__init__`](modeling_qwen3_moe.md#Qwen3MoeForSequenceClassification.__init__)

### `Qwen3MoeSparseBlock`  ·  implements/extends BaseMoeModule
- def: [`easydel/modules/qwen3_moe/modeling_qwen3_moe.py:267`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L267)
- doc: Sparse Mixture of Experts (MoE) block for Qwen3 MoE models.
- signature: `class Qwen3MoeSparseBlock(BaseMoeModule):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L327`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L327) — Route tokens through experts and combine outputs.
  - `__init__(self, config: Qwen3MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L274`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L274) — Initialize Qwen3 MoE sparse block.
  - `config` — [`L304`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L304)
  - `dtype` — [`L305`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L305)
  - `experts` — [`L319`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L319)
  - `gate` — [`L308`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L308)
  - `param_dtype` — [`L306`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L306)
  - `precision` — [`L307`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/modeling_qwen3_moe.py#L307)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`kernel`](../../layers/linears/_linear_moe.md#ParallelMoELinear.kernel), [`MoeRoutingStrategy`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy), [`moe_call`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_call), [`MoeLoadBalancingStrategy`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy), [`__init__`](../../layers/moe/_moe_module.md#BaseMoeModule.__init__), [`TOP_K`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy.TOP_K), [`Qwen3MoeConfig`](qwen3_moe_configuration.md#Qwen3MoeConfig), [`STANDARD`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy.STANDARD), [`down_proj`](modeling_qwen3_moe.md#Qwen3MoeMLPStack.down_proj), [`gate_proj`](modeling_qwen3_moe.md#Qwen3MoeMLPStack.gate_proj), [`up_proj`](modeling_qwen3_moe.md#Qwen3MoeMLPStack.up_proj), [`hidden_size`](qwen3_moe_configuration.md#Qwen3MoeConfig.hidden_size), [`TOP_K_NDIV`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy.TOP_K_NDIV), [`act_fn`](modeling_qwen3_moe.md#Qwen3MoeMLPStack.act_fn), [`num_experts`](qwen3_moe_configuration.md#Qwen3MoeConfig.num_experts), [`initializer_range`](qwen3_moe_configuration.md#Qwen3MoeConfig.initializer_range), [`Qwen3MoeMLPStack`](modeling_qwen3_moe.md#Qwen3MoeMLPStack), [`norm_topk_prob`](qwen3_moe_configuration.md#Qwen3MoeConfig.norm_topk_prob), [`num_experts_per_tok`](qwen3_moe_configuration.md#Qwen3MoeConfig.num_experts_per_tok)
- used by: [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`mlp`](modeling_qwen3_moe.md#Qwen3MoeDecoderLayer.mlp)

