---
title: 'Module: easydel/modules/exaone/modeling_exaone.py'
type: catalog
provenance: extracted
module: easydel/modules/exaone/modeling_exaone.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.exaone.modeling_exaone`/
symbols:
  ExaoneModel.__call__: ExaoneModel#__call__().
  ExaoneDecoderLayer.__call__: ExaoneDecoderLayer#__call__().
  ExaoneModel: ExaoneModel#
  ExaoneForCausalLM: ExaoneForCausalLM#
  ExaoneForSequenceClassification: ExaoneForSequenceClassification#
  ExaoneGatedMLP.__call__: ExaoneGatedMLP#__call__().
  ExaoneAttention.__call__: ExaoneAttention#__call__().
  ExaoneModel.drop: ExaoneModel#drop.
  ExaoneDecoderLayer.ln_1: ExaoneDecoderLayer#ln_1.
  ExaoneDecoderLayer.ln_2: ExaoneDecoderLayer#ln_2.
  ExaoneAttentionInner._create_rotary: ExaoneAttentionInner#_create_rotary().
  ExaoneForCausalLM.__init__: ExaoneForCausalLM#__init__().
  ExaoneForSequenceClassification.__init__: ExaoneForSequenceClassification#__init__().
  ExaoneGatedMLP.config: ExaoneGatedMLP#config.
  ExaoneDecoderLayer.config: ExaoneDecoderLayer#config.
  ExaoneModel.wte: ExaoneModel#wte.
  ExaoneGatedMLP.c_fc_0: ExaoneGatedMLP#c_fc_0.
  ExaoneGatedMLP.c_fc_1: ExaoneGatedMLP#c_fc_1.
  ExaoneGatedMLP.c_proj: ExaoneGatedMLP#c_proj.
  ExaoneGatedMLP.act_fn: ExaoneGatedMLP#act_fn.
  ExaoneModel.ln_f: ExaoneModel#ln_f.
  ExaoneModel.frequencies: ExaoneModel#frequencies().
  ExaoneAttentionInner.__init__: ExaoneAttentionInner#__init__().
  ExaoneAttentionInner._create_o_proj: ExaoneAttentionInner#_create_o_proj().
  ExaoneModel.__init__: ExaoneModel#__init__().
  ExaoneForCausalLM._task_type: ExaoneForCausalLM#_task_type.
  ExaoneForSequenceClassification._task_type: ExaoneForSequenceClassification#_task_type.
  ExaoneDecoderLayer.mlp: ExaoneDecoderLayer#mlp.
  ExaoneModel.h: ExaoneModel#h.
  ExaoneAttentionInner: ExaoneAttentionInner#
  ExaoneAttention.attention: ExaoneAttention#attention.
  ExaoneDecoderLayer.attn: ExaoneDecoderLayer#attn.
  ExaoneGatedMLP.__init__: ExaoneGatedMLP#__init__().
  ExaoneAttention.__init__: ExaoneAttention#__init__().
  ExaoneDecoderLayer.__init__: ExaoneDecoderLayer#__init__().
  ExaoneModel.get_embedding: ExaoneModel#get_embedding().
  ExaoneForCausalLM._config_class: ExaoneForCausalLM#_config_class.
  ExaoneForSequenceClassification._config_class: ExaoneForSequenceClassification#_config_class.
  ExaoneGatedMLP: ExaoneGatedMLP#
  ExaoneAttention: ExaoneAttention#
  ExaoneDecoderLayer: ExaoneDecoderLayer#
  logger: logger.
  ExaoneAttentionInner.projection_mapping: ExaoneAttentionInner#projection_mapping.
  ExaoneAttentionInner._get_output_proj: ExaoneAttentionInner#_get_output_proj().
  ExaoneDecoderLayer.dtype: ExaoneDecoderLayer#dtype.
  ExaoneDecoderLayer.param_dtype: ExaoneDecoderLayer#param_dtype.
  ExaoneDecoderLayer.precision: ExaoneDecoderLayer#precision.
  ExaoneDecoderLayer.rngs: ExaoneDecoderLayer#rngs.
  ExaoneModel.get_encoder: ExaoneModel#get_encoder().
  ExaoneModel.get_decoder: ExaoneModel#get_decoder().
  ExaoneModel.get_lm_head: ExaoneModel#get_lm_head().
  ExaoneForCausalLM._model_type: ExaoneForCausalLM#_model_type.
  ExaoneForSequenceClassification._model_type: ExaoneForSequenceClassification#_model_type.
---
# Module: [`easydel/modules/exaone/modeling_exaone.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py)

## Classes
### `ExaoneAttention`  ·  implements/extends Module
- def: [`easydel/modules/exaone/modeling_exaone.py:208`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L208)
- doc: Wrapper around ExaoneAttentionInner for Exaone decoder layers.
- signature: `class ExaoneAttention(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L245`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L245) — Forward pass through the attention layer.
  - `__init__(self, config: ExaoneConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L215`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L215) — Initialize Exaone attention wrapper.
  - `attention` — [`L236`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L236)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`ExaoneConfig`](exaone_configuration.md#ExaoneConfig), [`ExaoneAttentionInner`](modeling_exaone.md#ExaoneAttentionInner)
- used by: [`attn`](modeling_exaone.md#ExaoneDecoderLayer.attn)

### `ExaoneAttentionInner`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/exaone/modeling_exaone.py:133`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L133)
- doc: Multi-head attention layer with partial RoPE embeddings for Exaone models.
- signature: `class ExaoneAttentionInner(UnifiedAttention):`
- members:
  - `__init__(self, config: ExaoneConfig, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L148`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L148) — Initialize Exaone attention layer with partial rotary embeddings.
  - `_create_o_proj(self, config, dtype, param_dtype, precision, rngs)` — [`L191`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L191) — Create output projection with Exaone's custom naming (out_proj).
  - `_create_rotary(self, config: ExaoneConfig, dtype: jnp.dtype)` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L179) — Override to use partial rotary factor.
  - `_get_output_proj(self)` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L203) — Access output projection using Exaone's naming.
  - `projection_mapping` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L140)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`get_basic_rope`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_rope), [`ExaoneConfig`](exaone_configuration.md#ExaoneConfig), [`hidden_size`](exaone_configuration.md#ExaoneConfig.hidden_size), [`num_attention_heads`](exaone_configuration.md#ExaoneConfig.num_attention_heads)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`_create_o_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_o_proj), [`attention`](modeling_exaone.md#ExaoneAttention.attention)

### `ExaoneDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/exaone/modeling_exaone.py:285`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L285)
- doc: Single decoder layer for Exaone models.
- signature: `class ExaoneDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L349`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L349) — Forward pass through the decoder layer.
  - `__init__(self, config: ExaoneConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L292`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L292) — Initialize Exaone decoder layer.
  - `attn` — [`L319`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L319)
  - `config` — [`L313`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L313)
  - `dtype` — [`L314`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L314)
  - `ln_1` — [`L334`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L334)
  - `ln_2` — [`L341`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L341)
  - `mlp` — [`L327`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L327)
  - `param_dtype` — [`L315`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L315)
  - `precision` — [`L316`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L316)
  - `rngs` — [`L317`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L317)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`ExaoneConfig`](exaone_configuration.md#ExaoneConfig), [`hidden_size`](exaone_configuration.md#ExaoneConfig.hidden_size), [`layer_norm_epsilon`](exaone_configuration.md#ExaoneConfig.layer_norm_epsilon), [`ExaoneAttention`](modeling_exaone.md#ExaoneAttention), [`ExaoneGatedMLP`](modeling_exaone.md#ExaoneGatedMLP), [`scan_mlp_chunk_size`](exaone_configuration.md#ExaoneConfig.scan_mlp_chunk_size), [`use_scan_mlp`](exaone_configuration.md#ExaoneConfig.use_scan_mlp)
- used by: [`drop`](modeling_exaone.md#ExaoneModel.drop)

### `ExaoneForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/exaone/modeling_exaone.py:658`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L658)
- doc: Exaone model with a language modeling head for causal language modeling tasks.
- signature: `class ExaoneForCausalLM(BaseCausalLMModule[ExaoneModel, ExaoneConfig]):`
- members:
  - `__init__(self, config: ExaoneConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L675`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L675) — Initialize Exaone model for causal language modeling.
- protocol/private: `_config_class`[`L673`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L673), `_model_type`[`L672`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L672), `_task_type`[`L671`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L671)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`ExaoneConfig`](exaone_configuration.md#ExaoneConfig), [`ExaoneModel`](modeling_exaone.md#ExaoneModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `ExaoneForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/exaone/modeling_exaone.py:706`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L706)
- doc: Exaone model for sequence classification tasks.
- signature: `class ExaoneForSequenceClassification(BaseSequenceClassificationModule[ExaoneModel, ExaoneConfig]):`
- members:
  - `__init__(self, config: ExaoneConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L723`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L723) — Initialize Exaone model for sequence classification.
- protocol/private: `_config_class`[`L721`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L721), `_model_type`[`L720`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L720), `_task_type`[`L719`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L719)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`ExaoneConfig`](exaone_configuration.md#ExaoneConfig), [`ExaoneModel`](modeling_exaone.md#ExaoneModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule)

### `ExaoneGatedMLP`  ·  implements/extends Module
- def: [`easydel/modules/exaone/modeling_exaone.py:53`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L53)
- doc: Gated Multi-Layer Perceptron module for Exaone models.
- signature: `class ExaoneGatedMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L102`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L102) — Apply gated feedforward transformation.
  - `__init__(self, config: ExaoneConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L60`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L60) — Initialize Exaone gated MLP block.
  - `act_fn` — [`L100`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L100)
  - `c_fc_0` — [`L97`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L97)
  - `c_fc_1` — [`L98`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L98)
  - `c_proj` — [`L99`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L99)
  - `config` — [`L79`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L79)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`ExaoneConfig`](exaone_configuration.md#ExaoneConfig), [`hidden_size`](exaone_configuration.md#ExaoneConfig.hidden_size), [`intermediate_size`](exaone_configuration.md#ExaoneConfig.intermediate_size), [`activation_function`](exaone_configuration.md#ExaoneConfig.activation_function)
- used by: [`mlp`](modeling_exaone.md#ExaoneDecoderLayer.mlp)

### `ExaoneModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/exaone/modeling_exaone.py:419`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L419)
- doc: Exaone model implementation.
- signature: `class ExaoneModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L516`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L516) — Forward pass through the Exaone base model.
  - `__init__(self, config: ExaoneConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L432`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L432) — Initialize Exaone base model.
  - `frequencies(self)` — [`L496`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L496) — Compute and cache rotary position embedding frequencies.
  - `get_decoder(self)` — [`L637`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L637) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L650`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L650) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L630`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L630) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L643`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L643) — Returns the language model head of the module.
  - `drop` — [`L466`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L466)
  - `h` — [`L474`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L474)
  - `ln_f` — [`L487`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L487)
  - `wte` — [`L457`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L457)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`get_basic_frequencies`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_frequencies), [`ExaoneConfig`](exaone_configuration.md#ExaoneConfig), [`ExaoneDecoderLayer`](modeling_exaone.md#ExaoneDecoderLayer), [`gradient_checkpointing`](exaone_configuration.md#ExaoneConfig.gradient_checkpointing)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`ExaoneForCausalLM`](modeling_exaone.md#ExaoneForCausalLM), [`ExaoneForSequenceClassification`](modeling_exaone.md#ExaoneForSequenceClassification), [`__init__`](modeling_exaone.md#ExaoneForCausalLM.__init__), [`__init__`](modeling_exaone.md#ExaoneForSequenceClassification.__init__)

## Module values
- `logger` — [`L50`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/modeling_exaone.py#L50)

