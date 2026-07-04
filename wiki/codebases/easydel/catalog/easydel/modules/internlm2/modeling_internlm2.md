---
title: 'Module: easydel/modules/internlm2/modeling_internlm2.py'
type: catalog
provenance: extracted
module: easydel/modules/internlm2/modeling_internlm2.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.internlm2.modeling_internlm2`/InternLM2
symbols:
  InternLM2Model.__call__: Model#__call__().
  InternLM2Block.__call__: Block#__call__().
  InternLM2ForCausalLM.__call__: ForCausalLM#__call__().
  InternLM2ForSequenceClassification.__call__: ForSequenceClassification#__call__().
  InternLM2Model.tok_embeddings: Model#tok_embeddings.
  InternLM2Model: Model#
  InternLM2ForCausalLM: ForCausalLM#
  InternLM2ForSequenceClassification: ForSequenceClassification#
  InternLM2MLP.__call__: MLP#__call__().
  InternLM2Attention._create_rotary: Attention#_create_rotary().
  InternLM2ForCausalLM.__init__: ForCausalLM#__init__().
  InternLM2MLP.precision: MLP#precision.
  InternLM2Block.attention_norm: Block#attention_norm.
  InternLM2Block.ffn_norm: Block#ffn_norm.
  InternLM2Model.norm: Model#norm.
  InternLM2Attention._create_attention_performer: Attention#_create_attention_performer().
  InternLM2ForSequenceClassification.__init__: ForSequenceClassification#__init__().
  InternLM2MLP.w1: MLP#w1.
  InternLM2MLP.w3: MLP#w3.
  InternLM2MLP.w2: MLP#w2.
  InternLM2MLP.act_fn: MLP#act_fn.
  InternLM2Attention.__init__: Attention#__init__().
  InternLM2Attention._create_fused_qkv_proj: Attention#_create_fused_qkv_proj().
  InternLM2Attention._create_o_proj: Attention#_create_o_proj().
  InternLM2Model.__init__: Model#__init__().
  InternLM2ForCausalLM._task_type: ForCausalLM#_task_type.
  InternLM2ForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  InternLM2Block.feed_forward: Block#feed_forward.
  InternLM2Model.layers: Model#layers.
  InternLM2Attention: Attention#
  InternLM2Block.attention: Block#attention.
  InternLM2Block.config: Block#config.
  InternLM2MLP.__init__: MLP#__init__().
  InternLM2Block.__init__: Block#__init__().
  InternLM2Model.get_embedding: Model#get_embedding().
  InternLM2ForCausalLM._config_class: ForCausalLM#_config_class.
  InternLM2ForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  InternLM2MLP.config: MLP#config.
  InternLM2MLP: MLP#
  InternLM2Block: Block#
  InternLM2Attention.projection_mapping: Attention#projection_mapping.
  InternLM2MLP.dtype: MLP#dtype.
  InternLM2MLP.param_dtype: MLP#param_dtype.
  InternLM2Block.dtype: Block#dtype.
  InternLM2Block.param_dtype: Block#param_dtype.
  InternLM2Block.precision: Block#precision.
  InternLM2Model.get_encoder: Model#get_encoder().
  InternLM2Model.get_decoder: Model#get_decoder().
  InternLM2Model.get_lm_head: Model#get_lm_head().
  InternLM2ForCausalLM._model_type: ForCausalLM#_model_type.
  InternLM2ForCausalLM.get_encoder: ForCausalLM#get_encoder().
  InternLM2ForCausalLM.get_decoder: ForCausalLM#get_decoder().
  InternLM2ForCausalLM.get_lm_head: ForCausalLM#get_lm_head().
  InternLM2ForCausalLM.get_embedding: ForCausalLM#get_embedding().
  InternLM2ForSequenceClassification._model_type: ForSequenceClassification#_model_type.
  InternLM2ForSequenceClassification.get_encoder: ForSequenceClassification#get_encoder().
  InternLM2ForSequenceClassification.get_decoder: ForSequenceClassification#get_decoder().
  InternLM2ForSequenceClassification.get_lm_head: ForSequenceClassification#get_lm_head().
  InternLM2ForSequenceClassification.get_embedding: ForSequenceClassification#get_embedding().
  InternLM2ForSequenceClassification.get_task_head: ForSequenceClassification#get_task_head().
---
# Module: [`easydel/modules/internlm2/modeling_internlm2.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py)

## Classes
### `InternLM2Attention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/internlm2/modeling_internlm2.py:54`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L54)
- doc: Multi-head attention layer with full RoPE embeddings for InternLM2 models.
- signature: `class InternLM2Attention(UnifiedAttention):`
- members:
  - `__init__(self, config: InternLM2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L67`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L67) — Initialize InternLM2 attention layer with grouped-query attention support.
  - `_create_attention_performer(self, config: InternLM2Config, rngs: nn.Rngs)` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L133) — Create attention performer with zero dropout.
  - `_create_rotary(self, config: InternLM2Config, dtype: jnp.dtype)` — [`L124`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L124) — Create InternLM2-specific rotary embedding with full RoPE.
  - `projection_mapping` — [`L62`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L62)
- protocol/private: `_create_fused_qkv_proj`[`L100`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L100), `_create_o_proj`[`L112`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L112)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`get_basic_rope`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_rope), [`InternLM2Config`](internlm2_configuration.md#InternLM2Config), [`rope_theta`](internlm2_configuration.md#InternLM2Config.rope_theta)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_attention_performer`](../../layers/attention/_unified.md#UnifiedAttention._create_attention_performer), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`_create_o_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_o_proj), [`_create_fused_qkv_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_fused_qkv_proj), [`attention`](modeling_internlm2.md#InternLM2Block.attention)

### `InternLM2Block`  ·  implements/extends Module
- def: [`easydel/modules/internlm2/modeling_internlm2.py:217`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L217)
- doc: Single decoder layer for InternLM2 models.
- signature: `class InternLM2Block(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L281`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L281) — Forward pass through the decoder layer.
  - `__init__(self, config: InternLM2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L224`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L224) — Initialize InternLM2 decoder layer.
  - `attention` — [`L249`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L249)
  - `attention_norm` — [`L266`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L266)
  - `config` — [`L244`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L244)
  - `dtype` — [`L245`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L245)
  - `feed_forward` — [`L258`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L258)
  - `ffn_norm` — [`L273`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L273)
  - `param_dtype` — [`L246`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L246)
  - `precision` — [`L247`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L247)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`InternLM2Config`](internlm2_configuration.md#InternLM2Config), [`hidden_size`](internlm2_configuration.md#InternLM2Config.hidden_size), [`InternLM2Attention`](modeling_internlm2.md#InternLM2Attention), [`rms_norm_eps`](internlm2_configuration.md#InternLM2Config.rms_norm_eps), [`InternLM2MLP`](modeling_internlm2.md#InternLM2MLP)
- used by: [`tok_embeddings`](modeling_internlm2.md#InternLM2Model.tok_embeddings)

### `InternLM2ForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/internlm2/modeling_internlm2.py:569`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L569)
- doc: InternLM2 model with a language modeling head for causal language modeling tasks.
- signature: `class InternLM2ForCausalLM(BaseCausalLMModule[InternLM2Model, InternLM2Config]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L617`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L617) — Forward pass through the InternLM2 causal language model.
  - `__init__(self, config: InternLM2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L586`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L586) — Initialize InternLM2 model for causal language modeling.
  - `get_decoder(self)` — [`L703`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L703) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L715`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L715) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L696`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L696) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L709`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L709) — Returns the language model head of the module.
- protocol/private: `_config_class`[`L584`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L584), `_model_type`[`L583`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L583), `_task_type`[`L582`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L582)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`CausalLMOutput`](../../infra/modeling_outputs.md#CausalLMOutput), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`compute_lm_logits`](../_base/causal_lm_module.md#BaseCausalLMModule.compute_lm_logits), [`InternLM2Config`](internlm2_configuration.md#InternLM2Config), [`InternLM2Model`](modeling_internlm2.md#InternLM2Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.get_lm_head)

### `InternLM2ForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/internlm2/modeling_internlm2.py:723`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L723)
- doc: InternLM2 model for sequence classification tasks.
- signature: `class InternLM2ForSequenceClassification(BaseSequenceClassificationModule[InternLM2Model, InternLM2Config]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L770`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L770) — Forward pass through the InternLM2 sequence classification model.
  - `__init__(self, config: InternLM2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L740`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L740) — Initialize InternLM2 model for sequence classification.
  - `get_decoder(self)` — [`L864`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L864) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L877`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L877) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L857`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L857) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L870`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L870) — Returns the language model head of the module.
  - `get_task_head(self)` — [`L883`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L883) — Returns the sequence classification head.
- protocol/private: `_config_class`[`L738`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L738), `_model_type`[`L737`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L737), `_task_type`[`L736`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L736)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), `pad_token_id`, [`SequenceClassifierOutput`](../../infra/modeling_outputs.md#SequenceClassifierOutput), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`InternLM2Config`](internlm2_configuration.md#InternLM2Config), [`InternLM2Model`](modeling_internlm2.md#InternLM2Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_lm_head), [`get_task_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_task_head)

### `InternLM2MLP`  ·  implements/extends Module
- def: [`easydel/modules/internlm2/modeling_internlm2.py:143`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L143)
- doc: Multi-Layer Perceptron module for InternLM2 models.
- signature: `class InternLM2MLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L188`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L188) — Apply SwiGLU feedforward transformation.
  - `__init__(self, config: InternLM2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L150) — Initialize InternLM2 MLP block.
  - `act_fn` — [`L186`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L186)
  - `config` — [`L171`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L171)
  - `dtype` — [`L172`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L172)
  - `param_dtype` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L173)
  - `precision` — [`L174`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L174)
  - `w1` — [`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L183)
  - `w2` — [`L185`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L185)
  - `w3` — [`L184`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L184)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`InternLM2Config`](internlm2_configuration.md#InternLM2Config), [`hidden_size`](internlm2_configuration.md#InternLM2Config.hidden_size), [`intermediate_size`](internlm2_configuration.md#InternLM2Config.intermediate_size), [`initializer_range`](internlm2_configuration.md#InternLM2Config.initializer_range), [`hidden_act`](internlm2_configuration.md#InternLM2Config.hidden_act)
- used by: [`feed_forward`](modeling_internlm2.md#InternLM2Block.feed_forward)

### `InternLM2Model`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/internlm2/modeling_internlm2.py:347`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L347)
- doc: InternLM2 model implementation.
- signature: `class InternLM2Model(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L421`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L421) — Forward pass through the InternLM2 base model.
  - `__init__(self, config: InternLM2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L360`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L360) — Initialize InternLM2 base model.
  - `get_decoder(self)` — [`L548`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L548) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L561`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L561) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L541`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L541) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L554`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L554) — Returns the language model head of the module.
  - `layers` — [`L400`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L400)
  - `norm` — [`L413`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L413)
  - `tok_embeddings` — [`L386`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/modeling_internlm2.py#L386)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`InternLM2Config`](internlm2_configuration.md#InternLM2Config), [`hidden_size`](internlm2_configuration.md#InternLM2Config.hidden_size), [`rms_norm_eps`](internlm2_configuration.md#InternLM2Config.rms_norm_eps), [`initializer_range`](internlm2_configuration.md#InternLM2Config.initializer_range), [`num_hidden_layers`](internlm2_configuration.md#InternLM2Config.num_hidden_layers), [`InternLM2Block`](modeling_internlm2.md#InternLM2Block), [`gradient_checkpointing`](internlm2_configuration.md#InternLM2Config.gradient_checkpointing), [`vocab_size`](internlm2_configuration.md#InternLM2Config.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`InternLM2ForCausalLM`](modeling_internlm2.md#InternLM2ForCausalLM), [`InternLM2ForSequenceClassification`](modeling_internlm2.md#InternLM2ForSequenceClassification), [`__init__`](modeling_internlm2.md#InternLM2ForCausalLM.__init__), [`__init__`](modeling_internlm2.md#InternLM2ForSequenceClassification.__init__)

