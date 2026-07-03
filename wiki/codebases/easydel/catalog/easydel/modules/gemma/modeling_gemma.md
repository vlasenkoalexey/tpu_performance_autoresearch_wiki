---
title: 'Module: easydel/modules/gemma/modeling_gemma.py'
type: catalog
provenance: extracted
module: easydel/modules/gemma/modeling_gemma.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.gemma.modeling_gemma`/
symbols:
  GemmaDecoderLayer.__call__: GemmaDecoderLayer#__call__().
  GemmaModel.__call__: GemmaModel#__call__().
  GemmaForCausalLM.__call__: GemmaForCausalLM#__call__().
  GemmaForSequenceClassification.__call__: GemmaForSequenceClassification#__call__().
  GemmaModel.embed_tokens: GemmaModel#embed_tokens.
  GemmaModel: GemmaModel#
  GemmaForCausalLM: GemmaForCausalLM#
  GemmaForSequenceClassification: GemmaForSequenceClassification#
  GemmaMLP.precision: GemmaMLP#precision.
  GemmaMLP.__call__: GemmaMLP#__call__().
  GemmaRMSNorm.kernel: GemmaRMSNorm#kernel.
  GemmaAttention._create_rotary: GemmaAttention#_create_rotary().
  GemmaMLP.config: GemmaMLP#config.
  GemmaMLP.act: GemmaMLP#act.
  GemmaDecoderLayer.input_layernorm: GemmaDecoderLayer#input_layernorm.
  GemmaDecoderLayer.post_attention_layernorm: GemmaDecoderLayer#post_attention_layernorm.
  GemmaModel.norm: GemmaModel#norm.
  GemmaRMSNorm.__call__: GemmaRMSNorm#__call__().
  GemmaForCausalLM.__init__: GemmaForCausalLM#__init__().
  GemmaForSequenceClassification.__init__: GemmaForSequenceClassification#__init__().
  GemmaRMSNorm.epsilon: GemmaRMSNorm#epsilon.
  GemmaDecoderLayer.config: GemmaDecoderLayer#config.
  GemmaAttention.__init__: GemmaAttention#__init__().
  GemmaModel.__init__: GemmaModel#__init__().
  GemmaForCausalLM._task_type: GemmaForCausalLM#_task_type.
  GemmaForSequenceClassification._task_type: GemmaForSequenceClassification#_task_type.
  GemmaDecoderLayer.mlp: GemmaDecoderLayer#mlp.
  GemmaModel.layers: GemmaModel#layers.
  GemmaAttention: GemmaAttention#
  GemmaDecoderLayer.self_attn: GemmaDecoderLayer#self_attn.
  GemmaModel.hidden_size: GemmaModel#hidden_size.
  GemmaRMSNorm: GemmaRMSNorm#
  GemmaRMSNorm.__init__: GemmaRMSNorm#__init__().
  GemmaMLP.__init__: GemmaMLP#__init__().
  GemmaDecoderLayer.__init__: GemmaDecoderLayer#__init__().
  GemmaModel.get_embedding: GemmaModel#get_embedding().
  GemmaForCausalLM._config_class: GemmaForCausalLM#_config_class.
  GemmaForSequenceClassification._config_class: GemmaForSequenceClassification#_config_class.
  GemmaRMSNorm.config: GemmaRMSNorm#config.
  GemmaRMSNorm.dtype: GemmaRMSNorm#dtype.
  GemmaDecoderLayer.dtype: GemmaDecoderLayer#dtype.
  GemmaMLP: GemmaMLP#
  GemmaMLP.gate_proj: GemmaMLP#gate_proj.
  GemmaMLP.down_proj: GemmaMLP#down_proj.
  GemmaMLP.up_proj: GemmaMLP#up_proj.
  GemmaDecoderLayer: GemmaDecoderLayer#
  logger: logger.
  GemmaRMSNorm.kernel_init: GemmaRMSNorm#kernel_init.
  GemmaRMSNorm.craft_sharding: GemmaRMSNorm#craft_sharding().
  GemmaMLP.dtype: GemmaMLP#dtype.
  GemmaMLP.param_dtype: GemmaMLP#param_dtype.
  GemmaDecoderLayer.param_dtype: GemmaDecoderLayer#param_dtype.
  GemmaDecoderLayer.precision: GemmaDecoderLayer#precision.
  GemmaModel.get_encoder: GemmaModel#get_encoder().
  GemmaModel.get_decoder: GemmaModel#get_decoder().
  GemmaModel.get_lm_head: GemmaModel#get_lm_head().
  GemmaForCausalLM._model_type: GemmaForCausalLM#_model_type.
  GemmaForCausalLM.get_encoder: GemmaForCausalLM#get_encoder().
  GemmaForCausalLM.get_decoder: GemmaForCausalLM#get_decoder().
  GemmaForCausalLM.get_lm_head: GemmaForCausalLM#get_lm_head().
  GemmaForCausalLM.get_embedding: GemmaForCausalLM#get_embedding().
  GemmaForSequenceClassification._model_type: GemmaForSequenceClassification#_model_type.
  GemmaForSequenceClassification.get_encoder: GemmaForSequenceClassification#get_encoder().
  GemmaForSequenceClassification.get_decoder: GemmaForSequenceClassification#get_decoder().
  GemmaForSequenceClassification.get_lm_head: GemmaForSequenceClassification#get_lm_head().
  GemmaForSequenceClassification.get_embedding: GemmaForSequenceClassification#get_embedding().
  GemmaForSequenceClassification.get_task_head: GemmaForSequenceClassification#get_task_head().
---
# Module: [`easydel/modules/gemma/modeling_gemma.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py)

## Classes
### `GemmaAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/gemma/modeling_gemma.py:106`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L106)
- doc: Multi-head attention layer for Gemma models with rotary position embeddings.
- signature: `class GemmaAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: GemmaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L119) — Initialize Gemma attention layer.
  - `_create_rotary(self, config: GemmaConfig, dtype: jnp.dtype)` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L151) — Create Gemma-specific rotary embedding layer.
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`get_basic_rope`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_rope), [`GemmaConfig`](gemma_configuration.md#GemmaConfig), [`rope_theta`](gemma_configuration.md#GemmaConfig.rope_theta)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`self_attn`](modeling_gemma.md#GemmaDecoderLayer.self_attn)

### `GemmaDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/gemma/modeling_gemma.py:288`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L288)
- doc: Single decoder layer for Gemma models.
- signature: `class GemmaDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L352`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L352) — Forward pass through the decoder layer.
  - `__init__(self, config: GemmaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L306`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L306) — Initialize Gemma decoder layer.
  - `config` — [`L327`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L327)
  - `dtype` — [`L328`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L328)
  - `input_layernorm` — [`L333`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L333)
  - `mlp` — [`L343`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L343)
  - `param_dtype` — [`L329`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L329)
  - `post_attention_layernorm` — [`L334`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L334)
  - `precision` — [`L330`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L330)
  - `self_attn` — [`L335`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L335)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`GemmaConfig`](gemma_configuration.md#GemmaConfig), [`GemmaAttention`](modeling_gemma.md#GemmaAttention), [`GemmaRMSNorm`](modeling_gemma.md#GemmaRMSNorm), [`GemmaMLP`](modeling_gemma.md#GemmaMLP)
- used by: [`embed_tokens`](modeling_gemma.md#GemmaModel.embed_tokens)

### `GemmaForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/gemma/modeling_gemma.py:651`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L651)
- doc: Gemma model with a language modeling head for causal language modeling tasks.
- signature: `class GemmaForCausalLM(BaseCausalLMModule[GemmaModel, GemmaConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L698`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L698) — Forward pass through the Gemma causal language model.
  - `__init__(self, config: GemmaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L668`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L668) — Initialize Gemma model for causal language modeling.
  - `get_decoder(self)` — [`L781`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L781) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L793`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L793) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L774`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L774) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L787`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L787) — Returns the language model head of the module.
- protocol/private: `_config_class`[`L666`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L666), `_model_type`[`L665`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L665), `_task_type`[`L664`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L664)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`CausalLMOutput`](../../infra/modeling_outputs.md#CausalLMOutput), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`compute_lm_logits`](../_base/causal_lm_module.md#BaseCausalLMModule.compute_lm_logits), [`GemmaConfig`](gemma_configuration.md#GemmaConfig), [`GemmaModel`](modeling_gemma.md#GemmaModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.get_lm_head)

### `GemmaForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/gemma/modeling_gemma.py:801`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L801)
- doc: Gemma model for sequence classification tasks.
- signature: `class GemmaForSequenceClassification(BaseSequenceClassificationModule[GemmaModel, GemmaConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L849`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L849) — Forward pass through the Gemma sequence classification model.
  - `__init__(self, config: GemmaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L818`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L818) — Initialize Gemma model for sequence classification.
  - `get_decoder(self)` — [`L936`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L936) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L949`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L949) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L929`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L929) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L942`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L942) — Returns the language model head of the module.
  - `get_task_head(self)` — [`L955`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L955) — Returns the sequence classification head.
- protocol/private: `_config_class`[`L816`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L816), `_model_type`[`L815`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L815), `_task_type`[`L814`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L814)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), `pad_token_id`, [`SequenceClassifierOutput`](../../infra/modeling_outputs.md#SequenceClassifierOutput), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`GemmaConfig`](gemma_configuration.md#GemmaConfig), [`GemmaModel`](modeling_gemma.md#GemmaModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_lm_head), [`get_task_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_task_head)

### `GemmaMLP`  ·  implements/extends Module
- def: [`easydel/modules/gemma/modeling_gemma.py:164`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L164)
- doc: Gated MLP (GeGLU) feedforward network for Gemma models.
- signature: `class GemmaMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L257`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L257) — Forward pass through the MLP block.
  - `__init__(self, config: GemmaConfig, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L179) — Initialize Gemma MLP block.
  - `act` — [`L220`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L220)
  - `config` — [`L200`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L200)
  - `down_proj` — [`L246`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L246)
  - `dtype` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L201)
  - `gate_proj` — [`L241`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L241)
  - `param_dtype` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L202)
  - `precision` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L203)
  - `up_proj` — [`L251`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L251)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`GemmaConfig`](gemma_configuration.md#GemmaConfig), [`hidden_act`](gemma_configuration.md#GemmaConfig.hidden_act), [`hidden_activation`](gemma_configuration.md#GemmaConfig.hidden_activation), [`hidden_size`](gemma_configuration.md#GemmaConfig.hidden_size), [`intermediate_size`](gemma_configuration.md#GemmaConfig.intermediate_size), [`initializer_range`](gemma_configuration.md#GemmaConfig.initializer_range)
- used by: [`mlp`](modeling_gemma.md#GemmaDecoderLayer.mlp)

### `GemmaModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/gemma/modeling_gemma.py:431`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L431)
- doc: Gemma model implementation.
- signature: `class GemmaModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L503`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L503) — Forward pass through the Gemma base model.
  - `__init__(self, config: GemmaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L445`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L445) — Initialize Gemma base model.
  - `get_decoder(self)` — [`L630`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L630) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L643`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L643) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L623`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L623) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L636`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L636) — Returns the language model head of the module.
  - `embed_tokens` — [`L473`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L473)
  - `hidden_size` — [`L471`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L471)
  - `layers` — [`L487`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L487)
  - `norm` — [`L500`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L500)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`dtype`](../../infra/base_module.md#EasyDeLBaseModule.dtype), [`GemmaConfig`](gemma_configuration.md#GemmaConfig), [`GemmaRMSNorm`](modeling_gemma.md#GemmaRMSNorm), [`GemmaDecoderLayer`](modeling_gemma.md#GemmaDecoderLayer), [`gradient_checkpointing`](gemma_configuration.md#GemmaConfig.gradient_checkpointing)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`GemmaForCausalLM`](modeling_gemma.md#GemmaForCausalLM), [`GemmaForSequenceClassification`](modeling_gemma.md#GemmaForSequenceClassification), [`__init__`](modeling_gemma.md#GemmaForCausalLM.__init__), [`__init__`](modeling_gemma.md#GemmaForSequenceClassification.__init__)

### `GemmaRMSNorm`  ·  implements/extends Module
- def: [`easydel/modules/gemma/modeling_gemma.py:58`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L58)
- doc: Root Mean Square Layer Normalization for Gemma models.
- signature: `class GemmaRMSNorm(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L84) — Apply RMS normalization with learnable scale.
  - `__init__(self, config: GemmaConfig, dtype: jnp.dtype = jnp.float32)` — [`L67`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L67) — Initialize Gemma RMS normalization layer.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L102`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L102)
  - `config` — [`L74`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L74)
  - `dtype` — [`L76`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L76)
  - `epsilon` — [`L75`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L75)
  - `kernel` — [`L77`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L77)
  - `kernel_init` — [`L65`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L65)
- uses (calls/refs, reference-scoped): [`ArrayParam`](../../infra/utils.md#ArrayParam), [`bound`](../../infra/utils.md#ArrayParam.bound), [`GemmaConfig`](gemma_configuration.md#GemmaConfig), [`hidden_size`](gemma_configuration.md#GemmaConfig.hidden_size), [`rms_norm_eps`](gemma_configuration.md#GemmaConfig.rms_norm_eps)
- used by: [`input_layernorm`](modeling_gemma.md#GemmaDecoderLayer.input_layernorm), [`norm`](modeling_gemma.md#GemmaModel.norm), [`post_attention_layernorm`](modeling_gemma.md#GemmaDecoderLayer.post_attention_layernorm)

## Module values
- `logger` — [`L55`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/modeling_gemma.py#L55)

