---
title: 'Module: easydel/modules/qwen2_moe/modeling_qwen2_moe.py'
type: catalog
provenance: extracted
module: easydel/modules/qwen2_moe/modeling_qwen2_moe.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.qwen2_moe.modeling_qwen2_moe`/Qwen2Moe
symbols:
  Qwen2MoeModel.__call__: Model#__call__().
  Qwen2MoeDecoderLayer.__call__: DecoderLayer#__call__().
  Qwen2MoeSparseBlock.__init__: SparseBlock#__init__().
  Qwen2MoeSparseBlock.__call__: SparseBlock#__call__().
  Qwen2MoeForCausalLM.__call__: ForCausalLM#__call__().
  Qwen2MoeForSequenceClassification.__call__: ForSequenceClassification#__call__().
  Qwen2MoeModel.embed_tokens: Model#embed_tokens.
  Qwen2MoeDecoderLayer.precision: DecoderLayer#precision.
  Qwen2MoeModel: Model#
  Qwen2MoeMLPStack.gate_proj: MLPStack#gate_proj.
  Qwen2MoeMLPStack.down_proj: MLPStack#down_proj.
  Qwen2MoeMLPStack.up_proj: MLPStack#up_proj.
  Qwen2MoeForCausalLM: ForCausalLM#
  Qwen2MoeForSequenceClassification: ForSequenceClassification#
  Qwen2MoeMLP.__call__: MLP#__call__().
  Qwen2MoeAttention._create_rotary: Attention#_create_rotary().
  Qwen2MoeSparseBlock.gate: SparseBlock#gate.
  Qwen2MoeSparseBlock.shared_expert_gate: SparseBlock#shared_expert_gate.
  Qwen2MoeDecoderLayer.input_layernorm: DecoderLayer#input_layernorm.
  Qwen2MoeDecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  Qwen2MoeMLPStack.__call__: MLPStack#__call__().
  Qwen2MoeAttention.__init__: Attention#__init__().
  Qwen2MoeAttention._create_attention_performer: Attention#_create_attention_performer().
  Qwen2MoeDecoderLayer.config: DecoderLayer#config.
  Qwen2MoeMLP.precision: MLP#precision.
  Qwen2MoeSparseBlock.experts: SparseBlock#experts.
  Qwen2MoeForCausalLM.__init__: ForCausalLM#__init__().
  Qwen2MoeForSequenceClassification.__init__: ForSequenceClassification#__init__().
  Qwen2MoeSparseBlock.shared_expert: SparseBlock#shared_expert.
  Qwen2MoeModel.norm: Model#norm.
  Qwen2MoeForCausalLM._compute_aux_loss: ForCausalLM#_compute_aux_loss().
  Qwen2MoeAttention._create_q_proj: Attention#_create_q_proj().
  Qwen2MoeAttention._create_k_proj: Attention#_create_k_proj().
  Qwen2MoeAttention._create_v_proj: Attention#_create_v_proj().
  Qwen2MoeAttention._create_o_proj: Attention#_create_o_proj().
  Qwen2MoeModel.__init__: Model#__init__().
  Qwen2MoeForCausalLM._task_type: ForCausalLM#_task_type.
  Qwen2MoeForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  Qwen2MoeModel.layers: Model#layers.
  Qwen2MoeMLP.gate_proj: MLP#gate_proj.
  Qwen2MoeMLP.down_proj: MLP#down_proj.
  Qwen2MoeMLP.up_proj: MLP#up_proj.
  Qwen2MoeAttention: Attention#
  Qwen2MoeSparseBlock: SparseBlock#
  Qwen2MoeMLPStack.__init__: MLPStack#__init__().
  Qwen2MoeMLP.__init__: MLP#__init__().
  Qwen2MoeDecoderLayer.__init__: DecoderLayer#__init__().
  Qwen2MoeModel.get_embedding: Model#get_embedding().
  Qwen2MoeForCausalLM._config_class: ForCausalLM#_config_class.
  Qwen2MoeForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  Qwen2MoeMLPStack.act_fn: MLPStack#act_fn.
  Qwen2MoeMLP: MLP#
  Qwen2MoeMLP.config: MLP#config.
  Qwen2MoeDecoderLayer.layer_idx: DecoderLayer#layer_idx.
  Qwen2MoeMLPStack: MLPStack#
  Qwen2MoeMLP.act_fn: MLP#act_fn.
  Qwen2MoeDecoderLayer: DecoderLayer#
  Qwen2MoeDecoderLayer.self_attn: DecoderLayer#self_attn.
  Qwen2MoeDecoderLayer.mlp: DecoderLayer#mlp.
  Qwen2MoeMLPStack.reform_param: MLPStack#reform_param.
  Qwen2MoeMLPStack.config: MLPStack#config.
  Qwen2MoeMLPStack.dtype: MLPStack#dtype.
  Qwen2MoeMLPStack.param_dtype: MLPStack#param_dtype.
  Qwen2MoeMLPStack.precision: MLPStack#precision.
  Qwen2MoeMLP.dtype: MLP#dtype.
  Qwen2MoeMLP.param_dtype: MLP#param_dtype.
  Qwen2MoeSparseBlock.config: SparseBlock#config.
  Qwen2MoeSparseBlock.dtype: SparseBlock#dtype.
  Qwen2MoeSparseBlock.param_dtype: SparseBlock#param_dtype.
  Qwen2MoeSparseBlock.precision: SparseBlock#precision.
  Qwen2MoeDecoderLayer.dtype: DecoderLayer#dtype.
  Qwen2MoeDecoderLayer.param_dtype: DecoderLayer#param_dtype.
  Qwen2MoeModel.get_encoder: Model#get_encoder().
  Qwen2MoeModel.get_decoder: Model#get_decoder().
  Qwen2MoeModel.get_lm_head: Model#get_lm_head().
  Qwen2MoeForCausalLM._model_type: ForCausalLM#_model_type.
  Qwen2MoeForSequenceClassification._model_type: ForSequenceClassification#_model_type.
  Qwen2MoeForSequenceClassification.get_encoder: ForSequenceClassification#get_encoder().
  Qwen2MoeForSequenceClassification.get_decoder: ForSequenceClassification#get_decoder().
  Qwen2MoeForSequenceClassification.get_lm_head: ForSequenceClassification#get_lm_head().
  Qwen2MoeForSequenceClassification.get_embedding: ForSequenceClassification#get_embedding().
  Qwen2MoeForSequenceClassification.get_task_head: ForSequenceClassification#get_task_head().
---
# Module: [`easydel/modules/qwen2_moe/modeling_qwen2_moe.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py)

## Classes
### `Qwen2MoeAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/qwen2_moe/modeling_qwen2_moe.py:265`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L265)
- doc: Multi-head attention layer with RoPE embeddings and sliding window support for Qwen2 MoE models.
- signature: `class Qwen2MoeAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: Qwen2MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L273`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L273) — Initialize Qwen2 MoE attention layer with grouped-query attention and sliding window support.
  - `_create_attention_performer(self, config: Qwen2MoeConfig, rngs: nn.Rngs)` — [`L370`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L370) — Create attention performer with Qwen2Moe's attention dropout.
  - `_create_k_proj(self, config, dtype, param_dtype, precision, rngs)` — [`L320`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L320) — Override to use qkv_bias for key projection (Qwen2Moe-specific).
  - `_create_o_proj(self, config, dtype, param_dtype, precision, rngs)` — [`L346`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L346) — Override to use bias=False for output projection (Qwen2Moe-specific).
  - `_create_q_proj(self, config, dtype, param_dtype, precision, rngs)` — [`L307`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L307) — Override to use qkv_bias for query projection (Qwen2Moe-specific).
  - `_create_rotary(self, config: Qwen2MoeConfig, dtype: jnp.dtype)` — [`L361`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L361) — Create Qwen2Moe-specific rotary embedding layer.
  - `_create_v_proj(self, config, dtype, param_dtype, precision, rngs)` — [`L333`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L333) — Override to use qkv_bias for value projection (Qwen2Moe-specific).
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`get_basic_rope`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_rope), [`Qwen2MoeConfig`](qwen2_moe_configuration.md#Qwen2MoeConfig), [`hidden_size`](qwen2_moe_configuration.md#Qwen2MoeConfig.hidden_size), [`sliding_window`](qwen2_moe_configuration.md#Qwen2MoeConfig.sliding_window), [`num_attention_heads`](qwen2_moe_configuration.md#Qwen2MoeConfig.num_attention_heads), [`use_sliding_window`](qwen2_moe_configuration.md#Qwen2MoeConfig.use_sliding_window), [`attention_dropout`](qwen2_moe_configuration.md#Qwen2MoeConfig.attention_dropout), [`rope_theta`](qwen2_moe_configuration.md#Qwen2MoeConfig.rope_theta)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_attention_performer`](../../layers/attention/_unified.md#UnifiedAttention._create_attention_performer), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`_create_o_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_o_proj), [`_create_q_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_q_proj), [`_create_k_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_k_proj), [`_create_v_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_v_proj), [`precision`](modeling_qwen2_moe.md#Qwen2MoeDecoderLayer.precision)

### `Qwen2MoeDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/qwen2_moe/modeling_qwen2_moe.py:495`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L495)
- doc: Single decoder layer for Qwen2 MoE models.
- signature: `class Qwen2MoeDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, output_router_logits: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L567`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L567) — Forward pass of the decoder layer.
  - `__init__(self, config: Qwen2MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L503`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L503) — Initialize Qwen2 MoE decoder layer.
  - `config` — [`L523`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L523)
  - `dtype` — [`L525`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L525)
  - `input_layernorm` — [`L552`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L552)
  - `layer_idx` — [`L524`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L524)
  - `mlp` — [`L545`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L545)
  - `param_dtype` — [`L526`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L526)
  - `post_attention_layernorm` — [`L559`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L559)
  - `precision` — [`L527`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L527)
  - `self_attn` — [`L536`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L536)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`Qwen2MoeConfig`](qwen2_moe_configuration.md#Qwen2MoeConfig), [`hidden_size`](qwen2_moe_configuration.md#Qwen2MoeConfig.hidden_size), [`num_experts`](qwen2_moe_configuration.md#Qwen2MoeConfig.num_experts), [`Qwen2MoeAttention`](modeling_qwen2_moe.md#Qwen2MoeAttention), [`Qwen2MoeSparseBlock`](modeling_qwen2_moe.md#Qwen2MoeSparseBlock), [`Qwen2MoeMLP`](modeling_qwen2_moe.md#Qwen2MoeMLP), [`rms_norm_eps`](qwen2_moe_configuration.md#Qwen2MoeConfig.rms_norm_eps), [`decoder_sparse_step`](qwen2_moe_configuration.md#Qwen2MoeConfig.decoder_sparse_step), [`mlp_only_layers`](qwen2_moe_configuration.md#Qwen2MoeConfig.mlp_only_layers)
- used by: [`embed_tokens`](modeling_qwen2_moe.md#Qwen2MoeModel.embed_tokens)

### `Qwen2MoeForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/qwen2_moe/modeling_qwen2_moe.py:883`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L883)
- doc: Qwen2 MoE model with a language modeling head for causal language modeling tasks.
- signature: `class Qwen2MoeForCausalLM(BaseCausalLMModule[Qwen2MoeModel, Qwen2MoeConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True)` — [`L931`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L931) — Forward pass of the Qwen2MoeForCausalLM model.
  - `__init__(self, config: Qwen2MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L901`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L901) — Initialize Qwen2 MoE model for causal language modeling.
  - `_compute_aux_loss(self, outputs, attention_mask)` — [`L992`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L992) — Compute auxiliary load balancing loss from router logits.
- protocol/private: `_config_class`[`L899`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L899), `_model_type`[`L898`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L898), `_task_type`[`L897`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L897)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`MoeCausalLMOutput`](../../infra/modeling_outputs.md#MoeCausalLMOutput), [`auxiliary_load_balancing_loss_func`](../../infra/loss_utils.md#auxiliary_load_balancing_loss_func), [`forward_moe`](../_base/causal_lm_module.md#BaseCausalLMModule.forward_moe), [`Qwen2MoeConfig`](qwen2_moe_configuration.md#Qwen2MoeConfig), [`Qwen2MoeModel`](modeling_qwen2_moe.md#Qwen2MoeModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `Qwen2MoeForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/qwen2_moe/modeling_qwen2_moe.py:1014`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L1014)
- doc: Qwen2 MoE model for sequence classification tasks.
- signature: `class Qwen2MoeForSequenceClassification(BaseSequenceClassificationModule[Qwen2MoeModel, Qwen2MoeConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L1061`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L1061) — Forward pass of the Qwen2 MoE model for sequence classification.
  - `__init__(self, config: Qwen2MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1031`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L1031) — Initialize Qwen2 MoE model for sequence classification.
  - `get_decoder(self)` — [`L1150`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L1150) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L1163`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L1163) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L1143`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L1143) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L1156`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L1156) — Returns the language model head of the module.
  - `get_task_head(self)` — [`L1169`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L1169) — Returns the sequence classification head.
- protocol/private: `_config_class`[`L1029`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L1029), `_model_type`[`L1028`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L1028), `_task_type`[`L1027`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L1027)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), `pad_token_id`, [`SequenceClassifierOutput`](../../infra/modeling_outputs.md#SequenceClassifierOutput), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`Qwen2MoeConfig`](qwen2_moe_configuration.md#Qwen2MoeConfig), [`Qwen2MoeModel`](modeling_qwen2_moe.md#Qwen2MoeModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_lm_head), [`get_task_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_task_head)

### `Qwen2MoeMLP`  ·  implements/extends Module
- def: [`easydel/modules/qwen2_moe/modeling_qwen2_moe.py:182`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L182)
- doc: Multi-Layer Perceptron module for Qwen2 MoE models.
- signature: `class Qwen2MoeMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L238) — Apply SwiGLU feedforward transformation.
  - `__init__(self, config: Qwen2MoeConfig, intermediate_size: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L190) — Initialize Qwen2 MoE MLP block.
  - `act_fn` — [`L236`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L236) — ---
  - `config` — [`L211`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L211)
  - `down_proj` — [`L234`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L234)
  - `dtype` — [`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L212)
  - `gate_proj` — [`L233`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L233)
  - `param_dtype` — [`L213`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L213)
  - `precision` — [`L214`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L214)
  - `up_proj` — [`L235`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L235)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`Qwen2MoeConfig`](qwen2_moe_configuration.md#Qwen2MoeConfig), [`hidden_size`](qwen2_moe_configuration.md#Qwen2MoeConfig.hidden_size), [`initializer_range`](qwen2_moe_configuration.md#Qwen2MoeConfig.initializer_range)
- used by: [`precision`](modeling_qwen2_moe.md#Qwen2MoeDecoderLayer.precision), [`shared_expert`](modeling_qwen2_moe.md#Qwen2MoeSparseBlock.shared_expert)

### `Qwen2MoeMLPStack`  ·  implements/extends Module
- def: [`easydel/modules/qwen2_moe/modeling_qwen2_moe.py:66`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L66)
- doc: Mixture of Experts MLP stack module for Qwen2 MoE models.
- signature: `class Qwen2MoeMLPStack(nn.Module):`
- members:
  - `__call__(self, x: Array, group_sizes: Array, sorted_experts: Array | None = None)` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L163) — Forward pass through MoE MLP stack.
  - `__init__(self, config: Qwen2MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int | None = None)` — [`L99`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L99) — Initialize Qwen2 MoE MLP stack block.
  - `act_fn` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L161) — ---
  - `config` — [`L121`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L121)
  - `down_proj` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L137)
  - `dtype` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L122)
  - `gate_proj` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L125)
  - `param_dtype` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L123)
  - `precision` — [`L124`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L124)
  - `reform_param` — [`L74`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L74)
  - `up_proj` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L149)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`use_expert_tensor_mode`](../../infra/base_config.md#EasyDeLBaseConfig.use_expert_tensor_mode), [`ColumnParallelMoELinear`](../../layers/linears/_linear_moe.md#ColumnParallelMoELinear), [`RowParallelMoELinear`](../../layers/linears/_linear_moe.md#RowParallelMoELinear), [`Qwen2MoeConfig`](qwen2_moe_configuration.md#Qwen2MoeConfig), [`hidden_size`](qwen2_moe_configuration.md#Qwen2MoeConfig.hidden_size), [`num_experts`](qwen2_moe_configuration.md#Qwen2MoeConfig.num_experts), [`moe_intermediate_size`](qwen2_moe_configuration.md#Qwen2MoeConfig.moe_intermediate_size)
- used by: [`__call__`](modeling_qwen2_moe.md#Qwen2MoeSparseBlock.__call__), [`experts`](modeling_qwen2_moe.md#Qwen2MoeSparseBlock.experts)

### `Qwen2MoeModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/qwen2_moe/modeling_qwen2_moe.py:640`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L640)
- doc: The base Qwen2 MoE model transformer.
- signature: `class Qwen2MoeModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True)` — [`L716`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L716) — Forward pass of the Qwen2 MoE model.
  - `__init__(self, config: Qwen2MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L655`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L655) — Initialize Qwen2 MoE base model.
  - `get_decoder(self)` — [`L862`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L862) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L875`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L875) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L855`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L855) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L868`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L868) — Returns the language model head of the module.
  - `embed_tokens` — [`L681`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L681)
  - `layers` — [`L695`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L695)
  - `norm` — [`L709`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L709)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`MoeModelOutput`](../../infra/modeling_outputs.md#MoeModelOutput), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), `output_hidden_states`, [`router_logits`](../../infra/modeling_outputs.md#DecoderLayerOutput.router_logits), [`Qwen2MoeConfig`](qwen2_moe_configuration.md#Qwen2MoeConfig), [`hidden_size`](qwen2_moe_configuration.md#Qwen2MoeConfig.hidden_size), [`Qwen2MoeDecoderLayer`](modeling_qwen2_moe.md#Qwen2MoeDecoderLayer), [`gradient_checkpointing`](qwen2_moe_configuration.md#Qwen2MoeConfig.gradient_checkpointing), [`vocab_size`](qwen2_moe_configuration.md#Qwen2MoeConfig.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`Qwen2MoeForCausalLM`](modeling_qwen2_moe.md#Qwen2MoeForCausalLM), [`Qwen2MoeForSequenceClassification`](modeling_qwen2_moe.md#Qwen2MoeForSequenceClassification), [`__init__`](modeling_qwen2_moe.md#Qwen2MoeForCausalLM.__init__), [`__init__`](modeling_qwen2_moe.md#Qwen2MoeForSequenceClassification.__init__)

### `Qwen2MoeSparseBlock`  ·  implements/extends BaseMoeModule
- def: [`easydel/modules/qwen2_moe/modeling_qwen2_moe.py:380`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L380)
- doc: Sparse Mixture of Experts block for Qwen2 MoE models.
- signature: `class Qwen2MoeSparseBlock(BaseMoeModule):`
- members:
  - `__call__(self, hidden_states: Array)` — [`L459`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L459) — Forward pass of the Sparse MoE block.
  - `__init__(self, config: Qwen2MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L388`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L388) — Initialize Qwen2 MoE Sparse MoE block.
  - `config` — [`L417`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L417)
  - `dtype` — [`L418`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L418)
  - `experts` — [`L432`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L432)
  - `gate` — [`L421`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L421)
  - `param_dtype` — [`L419`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L419)
  - `precision` — [`L420`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L420)
  - `shared_expert` — [`L440`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L440)
  - `shared_expert_gate` — [`L448`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/modeling_qwen2_moe.py#L448)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`kernel`](../../layers/linears/_linear_moe.md#ParallelMoELinear.kernel), [`MoeRoutingStrategy`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy), [`moe_call`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_call), [`MoeLoadBalancingStrategy`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy), [`__init__`](../../layers/moe/_moe_module.md#BaseMoeModule.__init__), [`moe_hooks`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_hooks), [`Qwen2MoeConfig`](qwen2_moe_configuration.md#Qwen2MoeConfig), [`TOP_K`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy.TOP_K), [`down_proj`](modeling_qwen2_moe.md#Qwen2MoeMLPStack.down_proj), [`gate_proj`](modeling_qwen2_moe.md#Qwen2MoeMLPStack.gate_proj), [`up_proj`](modeling_qwen2_moe.md#Qwen2MoeMLPStack.up_proj), [`MoeFusedHooks`](../../layers/moe/_communication_utils.md#MoeFusedHooks), [`hidden_size`](qwen2_moe_configuration.md#Qwen2MoeConfig.hidden_size), [`TOP_K_NDIV`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy.TOP_K_NDIV), [`num_experts`](qwen2_moe_configuration.md#Qwen2MoeConfig.num_experts), [`initializer_range`](qwen2_moe_configuration.md#Qwen2MoeConfig.initializer_range), [`Qwen2MoeMLP`](modeling_qwen2_moe.md#Qwen2MoeMLP), [`NONE`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy.NONE), [`act_fn`](modeling_qwen2_moe.md#Qwen2MoeMLPStack.act_fn), [`Qwen2MoeMLPStack`](modeling_qwen2_moe.md#Qwen2MoeMLPStack), [`norm_topk_prob`](qwen2_moe_configuration.md#Qwen2MoeConfig.norm_topk_prob), [`num_experts_per_tok`](qwen2_moe_configuration.md#Qwen2MoeConfig.num_experts_per_tok), [`shared_expert_intermediate_size`](qwen2_moe_configuration.md#Qwen2MoeConfig.shared_expert_intermediate_size)
- used by: [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`precision`](modeling_qwen2_moe.md#Qwen2MoeDecoderLayer.precision)

