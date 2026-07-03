---
title: 'Module: easydel/modules/cohere/modeling_cohere.py'
type: catalog
provenance: extracted
module: easydel/modules/cohere/modeling_cohere.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.cohere.modeling_cohere`/
symbols:
  CohereModel.__call__: CohereModel#__call__().
  CohereBlock.__call__: CohereBlock#__call__().
  CohereForCausalLM.__call__: CohereForCausalLM#__call__().
  CohereForSequenceClassification.__call__: CohereForSequenceClassification#__call__().
  CohereModel.embed_tokens: CohereModel#embed_tokens.
  CohereModel: CohereModel#
  CohereForCausalLM: CohereForCausalLM#
  CohereForSequenceClassification: CohereForSequenceClassification#
  CohereAttention.q_norm: CohereAttention#q_norm.
  CohereAttention.k_norm: CohereAttention#k_norm.
  CohereMLP.__call__: CohereMLP#__call__().
  CohereMLP.precision: CohereMLP#precision.
  RMSNorm.kernel: RMSNorm#kernel.
  CohereBlock.input_layernorm: CohereBlock#input_layernorm.
  RMSNorm.__call__: RMSNorm#__call__().
  CohereAttention.__init__: CohereAttention#__init__().
  CohereAttention._create_rotary: CohereAttention#_create_rotary().
  CohereAttention._postprocess_qkv: CohereAttention#_postprocess_qkv().
  CohereForCausalLM.__init__: CohereForCausalLM#__init__().
  CohereForCausalLM.make_lm_head_fn: CohereForCausalLM#make_lm_head_fn().
  CohereForSequenceClassification.__init__: CohereForSequenceClassification#__init__().
  CohereMLP.gate_proj: CohereMLP#gate_proj.
  CohereMLP.down_proj: CohereMLP#down_proj.
  CohereMLP.up_proj: CohereMLP#up_proj.
  CohereBlock.config: CohereBlock#config.
  CohereModel.norm: CohereModel#norm.
  CohereForCausalLM.compute_lm_logits: CohereForCausalLM#compute_lm_logits().
  CohereModel.__init__: CohereModel#__init__().
  CohereForCausalLM._task_type: CohereForCausalLM#_task_type.
  CohereForSequenceClassification._task_type: CohereForSequenceClassification#_task_type.
  CohereBlock.mlp: CohereBlock#mlp.
  CohereModel.layers: CohereModel#layers.
  CohereForCausalLM.logit_scale: CohereForCausalLM#logit_scale.
  RMSNorm: RMSNorm#
  RMSNorm.dtype: RMSNorm#dtype.
  RMSNorm._norm: RMSNorm#_norm().
  CohereAttention: CohereAttention#
  CohereBlock.self_attn: CohereBlock#self_attn.
  RMSNorm.dim: RMSNorm#dim.
  CohereMLP.__init__: CohereMLP#__init__().
  CohereBlock.__init__: CohereBlock#__init__().
  CohereModel.get_embedding: CohereModel#get_embedding().
  CohereForCausalLM._config_class: CohereForCausalLM#_config_class.
  CohereForSequenceClassification._config_class: CohereForSequenceClassification#_config_class.
  CohereMLP.config: CohereMLP#config.
  RMSNorm.eps: RMSNorm#eps.
  RMSNorm.param_dtype: RMSNorm#param_dtype.
  RMSNorm.do_t: RMSNorm#do_t.
  CohereMLP: CohereMLP#
  CohereBlock: CohereBlock#
  CohereForCausalLM._project: CohereForCausalLM#_project().
  repeat_kv: repeat_kv().
  RMSNorm.kernel_init: RMSNorm#kernel_init.
  RMSNorm.__init__: RMSNorm#__init__().
  RMSNorm.craft_sharding: RMSNorm#craft_sharding().
  CohereMLP.dtype: CohereMLP#dtype.
  CohereMLP.param_dtype: CohereMLP#param_dtype.
  CohereBlock.dtype: CohereBlock#dtype.
  CohereBlock.param_dtype: CohereBlock#param_dtype.
  CohereBlock.precision: CohereBlock#precision.
  CohereBlock.rngs: CohereBlock#rngs.
  CohereModel.get_encoder: CohereModel#get_encoder().
  CohereModel.get_decoder: CohereModel#get_decoder().
  CohereModel.get_lm_head: CohereModel#get_lm_head().
  CohereForCausalLM._model_type: CohereForCausalLM#_model_type.
  CohereForCausalLM.get_encoder: CohereForCausalLM#get_encoder().
  CohereForCausalLM.get_decoder: CohereForCausalLM#get_decoder().
  CohereForCausalLM.get_lm_head: CohereForCausalLM#get_lm_head().
  CohereForCausalLM.get_embedding: CohereForCausalLM#get_embedding().
  CohereForSequenceClassification._model_type: CohereForSequenceClassification#_model_type.
  CohereForSequenceClassification.get_encoder: CohereForSequenceClassification#get_encoder().
  CohereForSequenceClassification.get_decoder: CohereForSequenceClassification#get_decoder().
  CohereForSequenceClassification.get_lm_head: CohereForSequenceClassification#get_lm_head().
  CohereForSequenceClassification.get_embedding: CohereForSequenceClassification#get_embedding().
---
# Module: [`easydel/modules/cohere/modeling_cohere.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py)

## Classes
### `CohereAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/cohere/modeling_cohere.py:159`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L159)
- doc: Multi-head attention layer with RoPE embeddings for Cohere models.
- signature: `class CohereAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: CohereConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L167) — Initialize Cohere attention with optional Q/K normalization.
  - `_create_rotary(self, config: CohereConfig, dtype: jnp.dtype)` — [`L217`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L217) — Create Cohere-specific rotary embedding layer.
  - `_postprocess_qkv(self, query_states, key_states, value_states)` — [`L229`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L229) — Apply Q/K normalization if configured.
  - `k_norm` — [`L206`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L206)
  - `q_norm` — [`L199`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L199)
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`config`](../../layers/attention/_flexible.md#AttentionModule.config), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`get_basic_rope`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_rope), [`CohereConfig`](cohere_configuration.md#CohereConfig), [`dtype`](../../layers/attention/_unified.md#UnifiedAttention.dtype), [`RMSNorm`](modeling_cohere.md#RMSNorm), [`layer_norm_eps`](cohere_configuration.md#CohereConfig.layer_norm_eps), [`param_dtype`](../../layers/attention/_unified.md#UnifiedAttention.param_dtype), [`use_qk_norm`](cohere_configuration.md#CohereConfig.use_qk_norm)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`_postprocess_qkv`](../../layers/attention/_unified.md#UnifiedAttention._postprocess_qkv), [`self_attn`](modeling_cohere.md#CohereBlock.self_attn)

### `CohereBlock`  ·  implements/extends Module
- def: [`easydel/modules/cohere/modeling_cohere.py:327`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L327)
- doc: Single decoder layer for Cohere models.
- signature: `class CohereBlock(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L388`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L388) — Forward pass through the decoder block.
  - `__init__(self, config: CohereConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L336`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L336) — Initialize Cohere decoder block.
  - `config` — [`L357`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L357)
  - `dtype` — [`L358`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L358)
  - `input_layernorm` — [`L380`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L380)
  - `mlp` — [`L372`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L372)
  - `param_dtype` — [`L359`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L359)
  - `precision` — [`L360`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L360)
  - `rngs` — [`L361`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L361)
  - `self_attn` — [`L363`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L363)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`CohereConfig`](cohere_configuration.md#CohereConfig), [`hidden_size`](cohere_configuration.md#CohereConfig.hidden_size), [`RMSNorm`](modeling_cohere.md#RMSNorm), [`CohereAttention`](modeling_cohere.md#CohereAttention), [`layer_norm_eps`](cohere_configuration.md#CohereConfig.layer_norm_eps), [`CohereMLP`](modeling_cohere.md#CohereMLP)
- used by: [`embed_tokens`](modeling_cohere.md#CohereModel.embed_tokens)

### `CohereForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/cohere/modeling_cohere.py:683`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L683)
- doc: Cohere model with a language modeling head for causal language modeling tasks.
- signature: `class CohereForCausalLM(BaseCausalLMModule[CohereModel, CohereConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L731`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L731) — Forward pass through the Cohere model for causal language modeling.
  - `__init__(self, config: CohereConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L701`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L701) — Initialize Cohere model for causal language modeling.
  - `compute_lm_logits(self, hidden_states: Array)` — [`L810`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L810) — Project hidden states to vocabulary logits and apply Cohere's logit scaling.
  - `get_decoder(self)` — [`L836`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L836) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L849`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L849) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L803`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L803) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L843`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L843) — Returns the language model head of the module.
  - `make_lm_head_fn(self)` — [`L826`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L826) — Trace-safe projection with Cohere logit scaling.
  - `logit_scale` — [`L729`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L729)
- protocol/private: `_config_class`[`L699`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L699), `_model_type`[`L698`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L698), `_project`[`L831`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L831), `_task_type`[`L697`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L697)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`CausalLMOutput`](../../infra/modeling_outputs.md#CausalLMOutput), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`make_lm_head_fn`](../_base/_base_task_module.md#BaseTaskModule.make_lm_head_fn), [`compute_lm_logits`](../_base/causal_lm_module.md#BaseCausalLMModule.compute_lm_logits), [`CohereConfig`](cohere_configuration.md#CohereConfig), [`CohereModel`](modeling_cohere.md#CohereModel), [`prepare_lm_head_inputs`](../_base/causal_lm_module.md#BaseCausalLMModule.prepare_lm_head_inputs)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.get_lm_head), [`make_lm_head_fn`](../_base/_base_task_module.md#BaseTaskModule.make_lm_head_fn), [`compute_lm_logits`](../_base/causal_lm_module.md#BaseCausalLMModule.compute_lm_logits)

### `CohereForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/cohere/modeling_cohere.py:858`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L858)
- doc: Cohere model for sequence classification tasks.
- signature: `class CohereForSequenceClassification(BaseSequenceClassificationModule[CohereModel, CohereConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None)` — [`L905`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L905) — Forward pass for sequence classification.
  - `__init__(self, config: CohereConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L875`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L875) — Initialize Cohere model for sequence classification.
  - `get_decoder(self)` — [`L1001`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L1001) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L1017`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L1017) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L992`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L992) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L1008`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L1008) — Returns the language model head of the module.
- protocol/private: `_config_class`[`L873`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L873), `_model_type`[`L872`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L872), `_task_type`[`L871`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L871)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), `pad_token_id`, [`SequenceClassifierOutput`](../../infra/modeling_outputs.md#SequenceClassifierOutput), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`CohereConfig`](cohere_configuration.md#CohereConfig), [`CohereModel`](modeling_cohere.md#CohereModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_lm_head)

### `CohereMLP`  ·  implements/extends Module
- def: [`easydel/modules/cohere/modeling_cohere.py:246`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L246)
- doc: Multi-Layer Perceptron module for Cohere models.
- signature: `class CohereMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L300`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L300) — Apply SwiGLU feedforward transformation.
  - `__init__(self, config: CohereConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L253`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L253) — Initialize Cohere MLP block.
  - `config` — [`L274`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L274)
  - `down_proj` — [`L297`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L297)
  - `dtype` — [`L275`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L275)
  - `gate_proj` — [`L296`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L296)
  - `param_dtype` — [`L276`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L276)
  - `precision` — [`L277`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L277)
  - `up_proj` — [`L298`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L298)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`CohereConfig`](cohere_configuration.md#CohereConfig), [`hidden_size`](cohere_configuration.md#CohereConfig.hidden_size), [`initializer_range`](cohere_configuration.md#CohereConfig.initializer_range), [`intermediate_size`](cohere_configuration.md#CohereConfig.intermediate_size)
- used by: [`mlp`](modeling_cohere.md#CohereBlock.mlp)

### `CohereModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/cohere/modeling_cohere.py:463`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L463)
- doc: Cohere model implementation.
- signature: `class CohereModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L537`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L537) — Performs forward pass through the Cohere transformer model.
  - `__init__(self, config: CohereConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L477`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L477) — Initialize Cohere base model.
  - `get_decoder(self)` — [`L661`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L661) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L675`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L675) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L654`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L654) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L668`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L668) — Returns the language model head of the module.
  - `embed_tokens` — [`L503`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L503)
  - `layers` — [`L517`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L517)
  - `norm` — [`L530`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L530)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`CohereConfig`](cohere_configuration.md#CohereConfig), [`hidden_size`](cohere_configuration.md#CohereConfig.hidden_size), [`RMSNorm`](modeling_cohere.md#RMSNorm), [`initializer_range`](cohere_configuration.md#CohereConfig.initializer_range), [`num_hidden_layers`](cohere_configuration.md#CohereConfig.num_hidden_layers), [`CohereBlock`](modeling_cohere.md#CohereBlock), [`gradient_checkpointing`](cohere_configuration.md#CohereConfig.gradient_checkpointing), [`vocab_size`](cohere_configuration.md#CohereConfig.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`CohereForCausalLM`](modeling_cohere.md#CohereForCausalLM), [`CohereForSequenceClassification`](modeling_cohere.md#CohereForSequenceClassification), [`__init__`](modeling_cohere.md#CohereForCausalLM.__init__), [`__init__`](modeling_cohere.md#CohereForSequenceClassification.__init__)

### `RMSNorm`  ·  implements/extends Module
- def: [`easydel/modules/cohere/modeling_cohere.py:67`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L67)
- doc: Root Mean Square Layer Normalization for Cohere models.
- signature: `class RMSNorm(nn.Module):`
- members:
  - `__call__(self, x: jnp.ndarray)` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L133) — Apply RMS normalization with learnable scale.
  - `__init__(self, dim: int | tuple, eps: float = 0.000001, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, do_t: bool = False, rngs: nn.Rngs | None = None)` — [`L76`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L76) — Initialize RMSNorm layer.
  - `_norm(self, x: jnp.ndarray)` — [`L111`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L111) — Compute RMS normalization.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L122) — Return sharding specifications for RMSNorm parameters.
  - `dim` — [`L99`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L99)
  - `do_t` — [`L103`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L103)
  - `dtype` — [`L101`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L101)
  - `eps` — [`L100`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L100)
  - `kernel` — [`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L104)
  - `kernel_init` — [`L74`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L74)
  - `param_dtype` — [`L102`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L102)
- uses (calls/refs, reference-scoped): [`ArrayParam`](../../infra/utils.md#ArrayParam), [`bound`](../../infra/utils.md#ArrayParam.bound)
- used by: [`k_norm`](modeling_cohere.md#CohereAttention.k_norm), [`q_norm`](modeling_cohere.md#CohereAttention.q_norm), [`input_layernorm`](modeling_cohere.md#CohereBlock.input_layernorm), [`norm`](modeling_cohere.md#CohereModel.norm)

## Functions
- `repeat_kv(x: Float[Array, "batch seq_len num_kv_heads head_dim"], n_rep: int)` — [`L54`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere/modeling_cohere.py#L54) — Tile key/value heads to match the requested number of attention heads.

