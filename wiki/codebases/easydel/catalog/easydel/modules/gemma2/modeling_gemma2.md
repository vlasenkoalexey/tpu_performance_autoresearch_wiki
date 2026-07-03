---
title: 'Module: easydel/modules/gemma2/modeling_gemma2.py'
type: catalog
provenance: extracted
module: easydel/modules/gemma2/modeling_gemma2.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.gemma2.modeling_gemma2`/
symbols:
  Gemma2DecoderLayer.__call__: Gemma2DecoderLayer#__call__().
  Gemma2Model.__call__: Gemma2Model#__call__().
  Gemma2ForCausalLM.__call__: Gemma2ForCausalLM#__call__().
  Gemma2ForSequenceClassification.__call__: Gemma2ForSequenceClassification#__call__().
  Gemma2Model.embed_tokens: Gemma2Model#embed_tokens.
  Gemma2Model: Gemma2Model#
  Gemma2ForCausalLM: Gemma2ForCausalLM#
  Gemma2ForSequenceClassification: Gemma2ForSequenceClassification#
  Gemma2MLP.__call__: Gemma2MLP#__call__().
  Gemma2MLP.act: Gemma2MLP#act.
  Gemma2RMSNorm.kernel: Gemma2RMSNorm#kernel.
  Gemma2Attention._create_attention_performer: Gemma2Attention#_create_attention_performer().
  Gemma2MLP.precision: Gemma2MLP#precision.
  Gemma2DecoderLayer.self_attn: Gemma2DecoderLayer#self_attn.
  Gemma2DecoderLayer.input_layernorm: Gemma2DecoderLayer#input_layernorm.
  Gemma2DecoderLayer.post_attention_layernorm: Gemma2DecoderLayer#post_attention_layernorm.
  Gemma2DecoderLayer.pre_feedforward_layernorm: Gemma2DecoderLayer#pre_feedforward_layernorm.
  Gemma2DecoderLayer.post_feedforward_layernorm: Gemma2DecoderLayer#post_feedforward_layernorm.
  Gemma2Model.norm: Gemma2Model#norm.
  Gemma2DecoderLayer.config: Gemma2DecoderLayer#config.
  Gemma2RMSNorm.__call__: Gemma2RMSNorm#__call__().
  Gemma2Attention.is_cross_attention: Gemma2Attention#is_cross_attention.
  Gemma2Attention._create_rotary: Gemma2Attention#_create_rotary().
  Gemma2ForCausalLM.__init__: Gemma2ForCausalLM#__init__().
  Gemma2ForCausalLM.make_lm_head_fn: Gemma2ForCausalLM#make_lm_head_fn().
  Gemma2ForSequenceClassification.__init__: Gemma2ForSequenceClassification#__init__().
  Gemma2RMSNorm.epsilon: Gemma2RMSNorm#epsilon.
  Gemma2MLP.config: Gemma2MLP#config.
  Gemma2ForCausalLM.compute_lm_logits: Gemma2ForCausalLM#compute_lm_logits().
  Gemma2RMSNorm: Gemma2RMSNorm#
  Gemma2Attention._merge_heads: Gemma2Attention#_merge_heads().
  Gemma2Model.__init__: Gemma2Model#__init__().
  Gemma2ForCausalLM._task_type: Gemma2ForCausalLM#_task_type.
  Gemma2ForSequenceClassification._task_type: Gemma2ForSequenceClassification#_task_type.
  Gemma2DecoderLayer.mlp: Gemma2DecoderLayer#mlp.
  Gemma2Model.layers: Gemma2Model#layers.
  Gemma2DecoderLayer.dtype: Gemma2DecoderLayer#dtype.
  Gemma2Attention: Gemma2Attention#
  Gemma2Model.hidden_size: Gemma2Model#hidden_size.
  Gemma2RMSNorm.__init__: Gemma2RMSNorm#__init__().
  Gemma2Attention.__init__: Gemma2Attention#__init__().
  Gemma2Attention.attention_softmax_in_fp32: Gemma2Attention#attention_softmax_in_fp32.
  Gemma2Attention._split_heads: Gemma2Attention#_split_heads().
  Gemma2MLP.__init__: Gemma2MLP#__init__().
  Gemma2DecoderLayer.__init__: Gemma2DecoderLayer#__init__().
  Gemma2DecoderLayer.is_sliding: Gemma2DecoderLayer#is_sliding.
  Gemma2Model.get_embedding: Gemma2Model#get_embedding().
  Gemma2ForCausalLM._config_class: Gemma2ForCausalLM#_config_class.
  Gemma2ForSequenceClassification._config_class: Gemma2ForSequenceClassification#_config_class.
  Gemma2RMSNorm.config: Gemma2RMSNorm#config.
  Gemma2RMSNorm.dtype: Gemma2RMSNorm#dtype.
  Gemma2DecoderLayer.layer_idx: Gemma2DecoderLayer#layer_idx.
  Gemma2MLP: Gemma2MLP#
  Gemma2MLP.gate_proj: Gemma2MLP#gate_proj.
  Gemma2MLP.down_proj: Gemma2MLP#down_proj.
  Gemma2MLP.up_proj: Gemma2MLP#up_proj.
  Gemma2DecoderLayer: Gemma2DecoderLayer#
  Gemma2ForCausalLM._project: Gemma2ForCausalLM#_project().
  logger: logger.
  Gemma2RMSNorm.kernel_init: Gemma2RMSNorm#kernel_init.
  Gemma2RMSNorm.craft_sharding: Gemma2RMSNorm#craft_sharding().
  Gemma2MLP.dtype: Gemma2MLP#dtype.
  Gemma2MLP.param_dtype: Gemma2MLP#param_dtype.
  Gemma2DecoderLayer.param_dtype: Gemma2DecoderLayer#param_dtype.
  Gemma2DecoderLayer.precision: Gemma2DecoderLayer#precision.
  Gemma2Model.get_encoder: Gemma2Model#get_encoder().
  Gemma2Model.get_decoder: Gemma2Model#get_decoder().
  Gemma2Model.get_lm_head: Gemma2Model#get_lm_head().
  Gemma2ForCausalLM._model_type: Gemma2ForCausalLM#_model_type.
  Gemma2ForCausalLM.get_encoder: Gemma2ForCausalLM#get_encoder().
  Gemma2ForCausalLM.get_decoder: Gemma2ForCausalLM#get_decoder().
  Gemma2ForCausalLM.get_lm_head: Gemma2ForCausalLM#get_lm_head().
  Gemma2ForCausalLM.get_embedding: Gemma2ForCausalLM#get_embedding().
  Gemma2ForSequenceClassification._model_type: Gemma2ForSequenceClassification#_model_type.
  Gemma2ForSequenceClassification.get_encoder: Gemma2ForSequenceClassification#get_encoder().
  Gemma2ForSequenceClassification.get_decoder: Gemma2ForSequenceClassification#get_decoder().
  Gemma2ForSequenceClassification.get_lm_head: Gemma2ForSequenceClassification#get_lm_head().
  Gemma2ForSequenceClassification.get_embedding: Gemma2ForSequenceClassification#get_embedding().
  Gemma2ForSequenceClassification.get_task_head: Gemma2ForSequenceClassification#get_task_head().
---
# Module: [`easydel/modules/gemma2/modeling_gemma2.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py)

## Classes
### `Gemma2Attention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/gemma2/modeling_gemma2.py:105`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L105)
- doc: Multi-head attention layer for Gemma2 with sliding window and softcapping support.
- signature: `class Gemma2Attention(UnifiedAttention):`
- members:
  - `__init__(self, config: Gemma2Config, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, causal: bool = True, is_cross_attention: bool = False, *, rngs: nn.Rngs)` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L120) — Initialize Gemma2 attention with sliding window configuration.
  - `_create_attention_performer(self, config: Gemma2Config, rngs: nn.Rngs)` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L169) — Create attention performer with Gemma2's custom softmax scale.
  - `_create_rotary(self, config: Gemma2Config, dtype: jnp.dtype)` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L165) — Create Gemma2-specific rotary embedding layer.
  - `_merge_heads(self, hidden_states)` — [`L178`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L178) — Merges the attention heads into a single hidden state tensor.
  - `_split_heads(self, hidden_states, num_heads)` — [`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L190) — Split hidden states into separate attention heads.
  - `attention_softmax_in_fp32` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L163)
  - `is_cross_attention` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L146)
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`num_heads`](../../layers/attention/_unified.md#UnifiedAttention.num_heads), [`get_basic_rope`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_rope), [`Gemma2Config`](gemma2_configuration.md#Gemma2Config), [`layer_types`](gemma2_configuration.md#Gemma2Config.layer_types), [`dtype`](../../layers/attention/_unified.md#UnifiedAttention.dtype), [`sliding_window`](gemma2_configuration.md#Gemma2Config.sliding_window), [`attention_dropout`](gemma2_configuration.md#Gemma2Config.attention_dropout), [`query_pre_attn_scalar`](gemma2_configuration.md#Gemma2Config.query_pre_attn_scalar)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_attention_performer`](../../layers/attention/_unified.md#UnifiedAttention._create_attention_performer), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`_merge_heads`](../../layers/attention/_unified.md#UnifiedAttention._merge_heads), [`self_attn`](modeling_gemma2.md#Gemma2DecoderLayer.self_attn)

### `Gemma2DecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/gemma2/modeling_gemma2.py:311`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L311)
- doc: Single decoder layer for Gemma2 models with post-norm architecture.
- signature: `class Gemma2DecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L381`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L381) — Forward pass through the decoder layer.
  - `__init__(self, config: Gemma2Config, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L331`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L331) — Initialize Gemma2 decoder layer.
  - `config` — [`L353`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L353)
  - `dtype` — [`L355`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L355)
  - `input_layernorm` — [`L376`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L376)
  - `is_sliding` — [`L359`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L359)
  - `layer_idx` — [`L354`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L354)
  - `mlp` — [`L368`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L368)
  - `param_dtype` — [`L356`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L356)
  - `post_attention_layernorm` — [`L377`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L377)
  - `post_feedforward_layernorm` — [`L379`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L379)
  - `pre_feedforward_layernorm` — [`L378`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L378)
  - `precision` — [`L357`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L357)
  - `self_attn` — [`L360`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L360)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`Gemma2Config`](gemma2_configuration.md#Gemma2Config), [`Gemma2RMSNorm`](modeling_gemma2.md#Gemma2RMSNorm), [`Gemma2Attention`](modeling_gemma2.md#Gemma2Attention), [`Gemma2MLP`](modeling_gemma2.md#Gemma2MLP)
- used by: [`embed_tokens`](modeling_gemma2.md#Gemma2Model.embed_tokens)

### `Gemma2ForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/gemma2/modeling_gemma2.py:694`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L694)
- doc: Gemma2 model with a language modeling head for causal language modeling tasks.
- signature: `class Gemma2ForCausalLM(BaseCausalLMModule[Gemma2Model, Gemma2Config]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L742`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L742) — Forward pass of the Gemma2 causal language model.
  - `__init__(self, config: Gemma2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L712`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L712) — Initialize Gemma2 model for causal language modeling.
  - `compute_lm_logits(self, hidden_states: Array)` — [`L838`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L838) — Project hidden states to vocabulary logits with optional soft-capping.
  - `get_decoder(self)` — [`L872`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L872) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L884`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L884) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L831`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L831) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L878`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L878) — Returns the language model head of the module.
  - `make_lm_head_fn(self)` — [`L858`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L858) — Trace-safe projection with Gemma-2 soft-capping.
- protocol/private: `_config_class`[`L710`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L710), `_model_type`[`L709`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L709), `_project`[`L865`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L865), `_task_type`[`L708`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L708)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`CausalLMOutput`](../../infra/modeling_outputs.md#CausalLMOutput), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`make_lm_head_fn`](../_base/_base_task_module.md#BaseTaskModule.make_lm_head_fn), [`compute_lm_logits`](../_base/causal_lm_module.md#BaseCausalLMModule.compute_lm_logits), [`Gemma2Config`](gemma2_configuration.md#Gemma2Config), [`Gemma2Model`](modeling_gemma2.md#Gemma2Model), [`prepare_lm_head_inputs`](../_base/causal_lm_module.md#BaseCausalLMModule.prepare_lm_head_inputs)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.get_lm_head), [`make_lm_head_fn`](../_base/_base_task_module.md#BaseTaskModule.make_lm_head_fn), [`compute_lm_logits`](../_base/causal_lm_module.md#BaseCausalLMModule.compute_lm_logits)

### `Gemma2ForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/gemma2/modeling_gemma2.py:892`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L892)
- doc: Gemma2 model for sequence classification tasks.
- signature: `class Gemma2ForSequenceClassification(BaseSequenceClassificationModule[Gemma2Model, Gemma2Config]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L940`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L940) — Forward pass through the Gemma2 sequence classification model.
  - `__init__(self, config: Gemma2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L909`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L909) — Initialize Gemma2 model for sequence classification.
  - `get_decoder(self)` — [`L1027`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L1027) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L1040`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L1040) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L1020`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L1020) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L1033`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L1033) — Returns the language model head of the module.
  - `get_task_head(self)` — [`L1046`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L1046) — Returns the sequence classification head.
- protocol/private: `_config_class`[`L907`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L907), `_model_type`[`L906`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L906), `_task_type`[`L905`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L905)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), `pad_token_id`, [`SequenceClassifierOutput`](../../infra/modeling_outputs.md#SequenceClassifierOutput), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`Gemma2Config`](gemma2_configuration.md#Gemma2Config), [`Gemma2Model`](modeling_gemma2.md#Gemma2Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_lm_head), [`get_task_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_task_head)

### `Gemma2MLP`  ·  implements/extends Module
- def: [`easydel/modules/gemma2/modeling_gemma2.py:203`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L203)
- doc: Gated MLP (GeGLU) feedforward network for Gemma2 models.
- signature: `class Gemma2MLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L282`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L282) — Forward pass through the MLP block.
  - `__init__(self, config: Gemma2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L218`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L218) — Initialize Gemma2 MLP block.
  - `act` — [`L246`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L246) — documented in [easydel-layers-linears-_linear](../../../../concepts/easydel-layers-linears-_linear.md)
  - `config` — [`L237`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L237)
  - `down_proj` — [`L271`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L271)
  - `dtype` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L238)
  - `gate_proj` — [`L266`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L266)
  - `param_dtype` — [`L239`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L239)
  - `precision` — [`L240`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L240)
  - `up_proj` — [`L276`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L276)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`Gemma2Config`](gemma2_configuration.md#Gemma2Config), [`hidden_size`](gemma2_configuration.md#Gemma2Config.hidden_size), [`intermediate_size`](gemma2_configuration.md#Gemma2Config.intermediate_size), [`hidden_activation`](gemma2_configuration.md#Gemma2Config.hidden_activation), [`initializer_range`](gemma2_configuration.md#Gemma2Config.initializer_range)
- used by: [`mlp`](modeling_gemma2.md#Gemma2DecoderLayer.mlp)

### `Gemma2Model`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/gemma2/modeling_gemma2.py:457`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L457)
- doc: Gemma2 model implementation.
- signature: `class Gemma2Model(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L529`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L529) — Forward pass through the Gemma2 base model.
  - `__init__(self, config: Gemma2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L472`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L472) — Initialize Gemma2 base model.
  - `get_decoder(self)` — [`L673`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L673) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L686`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L686) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L666`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L666) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L679`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L679) — Returns the language model head of the module.
  - `embed_tokens` — [`L500`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L500)
  - `hidden_size` — [`L498`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L498)
  - `layers` — [`L514`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L514)
  - `norm` — [`L527`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L527)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`dtype`](../../infra/base_module.md#EasyDeLBaseModule.dtype), [`Gemma2Config`](gemma2_configuration.md#Gemma2Config), [`Gemma2RMSNorm`](modeling_gemma2.md#Gemma2RMSNorm), [`Gemma2DecoderLayer`](modeling_gemma2.md#Gemma2DecoderLayer), [`gradient_checkpointing`](gemma2_configuration.md#Gemma2Config.gradient_checkpointing)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`Gemma2ForCausalLM`](modeling_gemma2.md#Gemma2ForCausalLM), [`Gemma2ForSequenceClassification`](modeling_gemma2.md#Gemma2ForSequenceClassification), [`__init__`](modeling_gemma2.md#Gemma2ForCausalLM.__init__), [`__init__`](modeling_gemma2.md#Gemma2ForSequenceClassification.__init__)

### `Gemma2RMSNorm`  ·  implements/extends Module
- def: [`easydel/modules/gemma2/modeling_gemma2.py:57`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L57)
- doc: Root Mean Square Layer Normalization for Gemma2 models.
- signature: `class Gemma2RMSNorm(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L83) — Apply RMS normalization with learnable scale.
  - `__init__(self, config: Gemma2Config, dtype: jnp.dtype = jnp.float32)` — [`L66`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L66) — Initialize Gemma2 RMS normalization layer.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L101`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L101)
  - `config` — [`L73`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L73)
  - `dtype` — [`L75`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L75)
  - `epsilon` — [`L74`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L74)
  - `kernel` — [`L76`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L76)
  - `kernel_init` — [`L64`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L64)
- uses (calls/refs, reference-scoped): [`ArrayParam`](../../infra/utils.md#ArrayParam), [`bound`](../../infra/utils.md#ArrayParam.bound), [`Gemma2Config`](gemma2_configuration.md#Gemma2Config), [`hidden_size`](gemma2_configuration.md#Gemma2Config.hidden_size), [`rms_norm_eps`](gemma2_configuration.md#Gemma2Config.rms_norm_eps)
- used by: [`input_layernorm`](modeling_gemma2.md#Gemma2DecoderLayer.input_layernorm), [`norm`](modeling_gemma2.md#Gemma2Model.norm), [`post_attention_layernorm`](modeling_gemma2.md#Gemma2DecoderLayer.post_attention_layernorm), [`post_feedforward_layernorm`](modeling_gemma2.md#Gemma2DecoderLayer.post_feedforward_layernorm), [`pre_feedforward_layernorm`](modeling_gemma2.md#Gemma2DecoderLayer.pre_feedforward_layernorm)

## Module values
- `logger` — [`L54`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma2/modeling_gemma2.py#L54)

