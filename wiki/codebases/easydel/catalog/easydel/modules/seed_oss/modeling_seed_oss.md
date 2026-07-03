---
title: 'Module: easydel/modules/seed_oss/modeling_seed_oss.py'
type: catalog
provenance: extracted
module: easydel/modules/seed_oss/modeling_seed_oss.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.seed_oss.modeling_seed_oss`/
symbols:
  SeedOssDecoderLayer.__call__: SeedOssDecoderLayer#__call__().
  SeedOssModel.__call__: SeedOssModel#__call__().
  SeedOssForCausalLM.__call__: SeedOssForCausalLM#__call__().
  SeedOssForSequenceClassification.__call__: SeedOssForSequenceClassification#__call__().
  SeedOssMLP.__call__: SeedOssMLP#__call__().
  SeedOssAttention._create_o_proj: SeedOssAttention#_create_o_proj().
  SeedOssForCausalLM: SeedOssForCausalLM#
  SeedOssForSequenceClassification: SeedOssForSequenceClassification#
  SeedOssModel.dropout: SeedOssModel#dropout.
  SeedOssModel.embed_tokens: SeedOssModel#embed_tokens.
  SeedOssAttention.sliding_window: SeedOssAttention#sliding_window.
  SeedOssMLP.precision: SeedOssMLP#precision.
  SeedOssMLP.act_fn: SeedOssMLP#act_fn.
  SeedOssDecoderLayer.input_layernorm: SeedOssDecoderLayer#input_layernorm.
  SeedOssDecoderLayer.post_attention_layernorm: SeedOssDecoderLayer#post_attention_layernorm.
  SeedOssModel: SeedOssModel#
  SeedOssModel.norm: SeedOssModel#norm.
  SeedOssForCausalLM.__init__: SeedOssForCausalLM#__init__().
  SeedOssForSequenceClassification.__init__: SeedOssForSequenceClassification#__init__().
  SeedOssMLP.gate_proj: SeedOssMLP#gate_proj.
  SeedOssMLP.up_proj: SeedOssMLP#up_proj.
  SeedOssMLP.down_proj: SeedOssMLP#down_proj.
  SeedOssAttention: SeedOssAttention#
  SeedOssModel.__init__: SeedOssModel#__init__().
  SeedOssForCausalLM._task_type: SeedOssForCausalLM#_task_type.
  SeedOssForSequenceClassification._task_type: SeedOssForSequenceClassification#_task_type.
  SeedOssDecoderLayer.mlp: SeedOssDecoderLayer#mlp.
  SeedOssModel.layers: SeedOssModel#layers.
  SeedOssMLP.dropout: SeedOssMLP#dropout.
  SeedOssDecoderLayer.self_attn: SeedOssDecoderLayer#self_attn.
  SeedOssMLP.config: SeedOssMLP#config.
  SeedOssDecoderLayer.config: SeedOssDecoderLayer#config.
  SeedOssMLP.__init__: SeedOssMLP#__init__().
  SeedOssAttention.__init__: SeedOssAttention#__init__().
  SeedOssAttention.layer_idx: SeedOssAttention#layer_idx.
  SeedOssDecoderLayer.__init__: SeedOssDecoderLayer#__init__().
  SeedOssModel.get_embedding: SeedOssModel#get_embedding().
  SeedOssForCausalLM._config_class: SeedOssForCausalLM#_config_class.
  SeedOssForSequenceClassification._config_class: SeedOssForSequenceClassification#_config_class.
  SeedOssMLP: SeedOssMLP#
  SeedOssDecoderLayer: SeedOssDecoderLayer#
  SeedOssMLP.dtype: SeedOssMLP#dtype.
  SeedOssMLP.param_dtype: SeedOssMLP#param_dtype.
  SeedOssDecoderLayer.dtype: SeedOssDecoderLayer#dtype.
  SeedOssDecoderLayer.param_dtype: SeedOssDecoderLayer#param_dtype.
  SeedOssDecoderLayer.precision: SeedOssDecoderLayer#precision.
  SeedOssModel.get_encoder: SeedOssModel#get_encoder().
  SeedOssModel.get_decoder: SeedOssModel#get_decoder().
  SeedOssModel.get_lm_head: SeedOssModel#get_lm_head().
  SeedOssForCausalLM._model_type: SeedOssForCausalLM#_model_type.
  SeedOssForCausalLM.get_encoder: SeedOssForCausalLM#get_encoder().
  SeedOssForCausalLM.get_decoder: SeedOssForCausalLM#get_decoder().
  SeedOssForCausalLM.get_lm_head: SeedOssForCausalLM#get_lm_head().
  SeedOssForCausalLM.get_embedding: SeedOssForCausalLM#get_embedding().
  SeedOssForSequenceClassification._model_type: SeedOssForSequenceClassification#_model_type.
  SeedOssForSequenceClassification.get_encoder: SeedOssForSequenceClassification#get_encoder().
  SeedOssForSequenceClassification.get_decoder: SeedOssForSequenceClassification#get_decoder().
  SeedOssForSequenceClassification.get_lm_head: SeedOssForSequenceClassification#get_lm_head().
  SeedOssForSequenceClassification.get_embedding: SeedOssForSequenceClassification#get_embedding().
  __all__: __all__.
---
# Module: [`easydel/modules/seed_oss/modeling_seed_oss.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py)

## Classes
### `SeedOssAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/seed_oss/modeling_seed_oss.py:150`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L150)
- doc: Seed OSS attention with biased QKV projections and bias-free output projection.
- signature: `class SeedOssAttention(UnifiedAttention[SeedOssConfig]):`
- members:
  - `__init__(self, config: SeedOssConfig, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L163) — Initialize the SeedOssAttention layer.
  - `_create_o_proj(self, config: SeedOssConfig, dtype: jnp.dtype, param_dtype: jnp.dtype, precision: jax.lax.PrecisionLike, rngs: nn.Rngs)` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L201) — Create the output projection layer without bias.
  - `layer_idx` — [`L184`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L184)
  - `sliding_window` — [`L186`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L186)
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`config`](../../layers/attention/_flexible.md#AttentionModule.config), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`num_heads`](../../layers/attention/_unified.md#UnifiedAttention.num_heads), [`SeedOssConfig`](seed_oss_configuration.md#SeedOssConfig), [`hidden_size`](seed_oss_configuration.md#SeedOssConfig.hidden_size), [`layer_types`](seed_oss_configuration.md#SeedOssConfig.layer_types), [`initializer_range`](seed_oss_configuration.md#SeedOssConfig.initializer_range), [`sliding_window`](seed_oss_configuration.md#SeedOssConfig.sliding_window)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_o_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_o_proj), [`self_attn`](modeling_seed_oss.md#SeedOssDecoderLayer.self_attn)

### `SeedOssDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/seed_oss/modeling_seed_oss.py:233`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L233)
- doc: Single transformer decoder layer for Seed OSS.
- signature: `class SeedOssDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L311`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L311) — Process input through attention and MLP sublayers.
  - `__init__(self, config: SeedOssConfig, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L254`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L254) — Initialize the SeedOssDecoderLayer.
  - `config` — [`L274`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L274)
  - `dtype` — [`L275`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L275)
  - `input_layernorm` — [`L296`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L296)
  - `mlp` — [`L288`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L288)
  - `param_dtype` — [`L276`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L276)
  - `post_attention_layernorm` — [`L303`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L303)
  - `precision` — [`L277`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L277)
  - `self_attn` — [`L279`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L279)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`SeedOssConfig`](seed_oss_configuration.md#SeedOssConfig), [`hidden_size`](seed_oss_configuration.md#SeedOssConfig.hidden_size), [`SeedOssAttention`](modeling_seed_oss.md#SeedOssAttention), [`rms_norm_eps`](seed_oss_configuration.md#SeedOssConfig.rms_norm_eps), [`SeedOssMLP`](modeling_seed_oss.md#SeedOssMLP), [`scan_mlp_chunk_size`](seed_oss_configuration.md#SeedOssConfig.scan_mlp_chunk_size), [`use_scan_mlp`](seed_oss_configuration.md#SeedOssConfig.use_scan_mlp)
- used by: [`dropout`](modeling_seed_oss.md#SeedOssModel.dropout)

### `SeedOssForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/seed_oss/modeling_seed_oss.py:607`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L607)
- doc: Seed OSS model with a causal language modeling head.
- signature: `class SeedOssForCausalLM(BaseCausalLMModule[SeedOssModel, SeedOssConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True)` — [`L653`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L653) — Perform forward pass for causal language modeling.
  - `__init__(self, config: SeedOssConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L623`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L623) — Initialize the SeedOssForCausalLM model.
  - `get_decoder(self)` — [`L726`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L726) — Get the decoder module.
  - `get_embedding(self)` — [`L742`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L742) — Get the token embedding layer.
  - `get_encoder(self)` — [`L718`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L718) — Get the encoder module.
  - `get_lm_head(self)` — [`L734`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L734) — Get the language modeling head.
- protocol/private: `_config_class`[`L621`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L621), `_model_type`[`L620`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L620), `_task_type`[`L619`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L619)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`CausalLMOutput`](../../infra/modeling_outputs.md#CausalLMOutput), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`compute_lm_logits`](../_base/causal_lm_module.md#BaseCausalLMModule.compute_lm_logits), [`SeedOssConfig`](seed_oss_configuration.md#SeedOssConfig), [`SeedOssModel`](modeling_seed_oss.md#SeedOssModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.get_lm_head)

### `SeedOssForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/seed_oss/modeling_seed_oss.py:752`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L752)
- doc: Seed OSS model with a sequence classification head.
- signature: `class SeedOssForSequenceClassification(BaseSequenceClassificationModule[SeedOssModel, SeedOssConfig]):`
- members:
  - `__call__(self, input_ids: Array | None = None, inputs_embeds: Array | None = None, attention_mask: Array | None = None, mask_info: MaskInfo | None = None, position_ids: Array | None = None, segment_ids: Array | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L803`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L803) — Perform forward pass for sequence classification.
  - `__init__(self, config: SeedOssConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L772`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L772) — Initialize the SeedOssForSequenceClassification model.
  - `get_decoder(self)` — [`L894`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L894) — Get the decoder module.
  - `get_embedding(self)` — [`L910`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L910) — Get the token embedding layer.
  - `get_encoder(self)` — [`L886`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L886) — Get the encoder module.
  - `get_lm_head(self)` — [`L902`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L902) — Get the classification head.
- protocol/private: `_config_class`[`L770`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L770), `_model_type`[`L769`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L769), `_task_type`[`L768`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L768)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), `pad_token_id`, [`SequenceClassifierOutput`](../../infra/modeling_outputs.md#SequenceClassifierOutput), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`SeedOssConfig`](seed_oss_configuration.md#SeedOssConfig), [`SeedOssModel`](modeling_seed_oss.md#SeedOssModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_lm_head)

### `SeedOssMLP`  ·  implements/extends Module
- def: [`easydel/modules/seed_oss/modeling_seed_oss.py:54`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L54)
- doc: Seed OSS gated MLP with SiLU activation.
- signature: `class SeedOssMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L122) — Apply the gated MLP transformation.
  - `__init__(self, config: SeedOssConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L73`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L73) — Initialize the SeedOssMLP layer.
  - `act_fn` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L120)
  - `config` — [`L92`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L92)
  - `down_proj` — [`L118`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L118)
  - `dropout` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L119)
  - `dtype` — [`L93`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L93)
  - `gate_proj` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L116)
  - `param_dtype` — [`L94`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L94)
  - `precision` — [`L95`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L95)
  - `up_proj` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L117)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`SeedOssConfig`](seed_oss_configuration.md#SeedOssConfig), [`mlp_bias`](seed_oss_configuration.md#SeedOssConfig.mlp_bias), [`hidden_size`](seed_oss_configuration.md#SeedOssConfig.hidden_size), [`initializer_range`](seed_oss_configuration.md#SeedOssConfig.initializer_range), [`intermediate_size`](seed_oss_configuration.md#SeedOssConfig.intermediate_size), [`hidden_act`](seed_oss_configuration.md#SeedOssConfig.hidden_act), [`resid_pdrop`](seed_oss_configuration.md#SeedOssConfig.resid_pdrop)
- used by: [`mlp`](modeling_seed_oss.md#SeedOssDecoderLayer.mlp)

### `SeedOssModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/seed_oss/modeling_seed_oss.py:374`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L374)
- doc: Base Seed OSS transformer model without task-specific heads.
- signature: `class SeedOssModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L457`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L457) — Process input through the transformer encoder stack.
  - `__init__(self, config: SeedOssConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L394`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L394) — Initialize the SeedOssModel.
  - `get_decoder(self)` — [`L581`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L581) — Get the decoder module.
  - `get_embedding(self)` — [`L597`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L597) — Get the token embedding layer.
  - `get_encoder(self)` — [`L573`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L573) — Get the encoder module.
  - `get_lm_head(self)` — [`L589`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L589) — Get the language modeling head.
  - `dropout` — [`L429`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L429)
  - `embed_tokens` — [`L421`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L421)
  - `layers` — [`L436`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L436)
  - `norm` — [`L449`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L449)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`SeedOssConfig`](seed_oss_configuration.md#SeedOssConfig), [`hidden_size`](seed_oss_configuration.md#SeedOssConfig.hidden_size), [`initializer_range`](seed_oss_configuration.md#SeedOssConfig.initializer_range), [`rms_norm_eps`](seed_oss_configuration.md#SeedOssConfig.rms_norm_eps), [`gradient_checkpointing_targets`](seed_oss_configuration.md#SeedOssConfig.gradient_checkpointing_targets), [`num_hidden_layers`](seed_oss_configuration.md#SeedOssConfig.num_hidden_layers), [`SeedOssDecoderLayer`](modeling_seed_oss.md#SeedOssDecoderLayer), [`embd_pdrop`](seed_oss_configuration.md#SeedOssConfig.embd_pdrop), [`gradient_checkpointing`](seed_oss_configuration.md#SeedOssConfig.gradient_checkpointing), [`vocab_size`](seed_oss_configuration.md#SeedOssConfig.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`SeedOssForCausalLM`](modeling_seed_oss.md#SeedOssForCausalLM), [`SeedOssForSequenceClassification`](modeling_seed_oss.md#SeedOssForSequenceClassification), [`__init__`](modeling_seed_oss.md#SeedOssForCausalLM.__init__), [`__init__`](modeling_seed_oss.md#SeedOssForSequenceClassification.__init__)

## Module values
- `__all__` — [`L919`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/modeling_seed_oss.py#L919)

