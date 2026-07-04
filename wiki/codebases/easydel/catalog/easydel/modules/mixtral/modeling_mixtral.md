---
title: 'Module: easydel/modules/mixtral/modeling_mixtral.py'
type: catalog
provenance: extracted
module: easydel/modules/mixtral/modeling_mixtral.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.mixtral.modeling_mixtral`/Mixtral
symbols:
  MixtralModel.__call__: Model#__call__().
  MixtralForSequenceClassification.__call__: ForSequenceClassification#__call__().
  MixtralDecoderLayer.__call__: DecoderLayer#__call__().
  MixtralSparseMoeBlock.__init__: SparseMoeBlock#__init__().
  MixtralForCausalLM.__call__: ForCausalLM#__call__().
  MixtralSparseMoeBlock.__call__: SparseMoeBlock#__call__().
  MixtralModel.embed_tokens: Model#embed_tokens.
  MixtralModel: Model#
  MixtralMoEMlp.w1: MoEMlp#w1.
  MixtralMoEMlp.w2: MoEMlp#w2.
  MixtralMoEMlp.w3: MoEMlp#w3.
  MixtralForCausalLM: ForCausalLM#
  MixtralForSequenceClassification: ForSequenceClassification#
  MixtralMoEMlp.__call__: MoEMlp#__call__().
  MixtralSparseMoeBlock.gate: SparseMoeBlock#gate.
  MixtralDecoderLayer.input_layernorm: DecoderLayer#input_layernorm.
  MixtralDecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  MixtralModel.norm: Model#norm.
  MixtralForCausalLM._compute_aux_loss: ForCausalLM#_compute_aux_loss().
  MixtralAttention.__init__: Attention#__init__().
  MixtralAttention._create_rotary: Attention#_create_rotary().
  MixtralSparseMoeBlock.experts: SparseMoeBlock#experts.
  MixtralForCausalLM.__init__: ForCausalLM#__init__().
  MixtralForSequenceClassification.__init__: ForSequenceClassification#__init__().
  MixtralMoEMlp.act_fn: MoEMlp#act_fn.
  MixtralModel.__init__: Model#__init__().
  MixtralForCausalLM._task_type: ForCausalLM#_task_type.
  MixtralForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  MixtralModel.layers: Model#layers.
  MixtralAttention: Attention#
  MixtralSparseMoeBlock: SparseMoeBlock#
  MixtralDecoderLayer.self_attn: DecoderLayer#self_attn.
  MixtralDecoderLayer.block_sparse_moe: DecoderLayer#block_sparse_moe.
  MixtralMoEMlp.__init__: MoEMlp#__init__().
  MixtralDecoderLayer.__init__: DecoderLayer#__init__().
  MixtralModel.get_embedding: Model#get_embedding().
  MixtralForCausalLM._config_class: ForCausalLM#_config_class.
  MixtralForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  MixtralMoEMlp: MoEMlp#
  MixtralDecoderLayer: DecoderLayer#
  MixtralDecoderLayer.config: DecoderLayer#config.
  MixtralMoEMlp.reform_param: MoEMlp#reform_param.
  MixtralMoEMlp.config: MoEMlp#config.
  MixtralMoEMlp.dtype: MoEMlp#dtype.
  MixtralMoEMlp.param_dtype: MoEMlp#param_dtype.
  MixtralMoEMlp.precision: MoEMlp#precision.
  MixtralSparseMoeBlock.dtype: SparseMoeBlock#dtype.
  MixtralSparseMoeBlock.param_dtype: SparseMoeBlock#param_dtype.
  MixtralSparseMoeBlock.precision: SparseMoeBlock#precision.
  MixtralDecoderLayer.reform_param: DecoderLayer#reform_param.
  MixtralDecoderLayer.dtype: DecoderLayer#dtype.
  MixtralDecoderLayer.param_dtype: DecoderLayer#param_dtype.
  MixtralDecoderLayer.precision: DecoderLayer#precision.
  MixtralDecoderLayer.rngs: DecoderLayer#rngs.
  MixtralModel.get_encoder: Model#get_encoder().
  MixtralModel.get_decoder: Model#get_decoder().
  MixtralModel.get_lm_head: Model#get_lm_head().
  MixtralForCausalLM._model_type: ForCausalLM#_model_type.
  MixtralForSequenceClassification._model_type: ForSequenceClassification#_model_type.
---
# Module: [`easydel/modules/mixtral/modeling_mixtral.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py)

## Classes
### `MixtralAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/mixtral/modeling_mixtral.py:63`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L63)
- doc: Mixtral Attention module with sliding window support.
- signature: `class MixtralAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: MixtralConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L71`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L71) — Initialize Mixtral attention with sliding window configuration.
  - `_create_rotary(self, config: MixtralConfig, dtype: jnp.dtype)` — [`L103`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L103) — Create Mixtral-specific rotary embedding layer.
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`get_basic_rope`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_rope), [`MixtralConfig`](mixtral_configuration.md#MixtralConfig), [`sliding_window`](mixtral_configuration.md#MixtralConfig.sliding_window)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`self_attn`](modeling_mixtral.md#MixtralDecoderLayer.self_attn)

### `MixtralDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/mixtral/modeling_mixtral.py:306`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L306)
- doc: Single decoder layer for Mixtral models.
- signature: `class MixtralDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, output_router_logits: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L402`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L402) — Forward pass through the decoder layer.
  - `__init__(self, config: MixtralConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L342`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L342) — Initialize Mixtral decoder layer.
  - `block_sparse_moe` — [`L378`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L378)
  - `config` — [`L363`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L363)
  - `dtype` — [`L364`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L364)
  - `input_layernorm` — [`L386`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L386)
  - `param_dtype` — [`L365`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L365)
  - `post_attention_layernorm` — [`L394`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L394)
  - `precision` — [`L366`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L366)
  - `reform_param` — [`L315`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L315)
  - `rngs` — [`L367`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L367)
  - `self_attn` — [`L369`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L369)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`MixtralConfig`](mixtral_configuration.md#MixtralConfig), [`hidden_size`](mixtral_configuration.md#MixtralConfig.hidden_size), [`MixtralAttention`](modeling_mixtral.md#MixtralAttention), [`MixtralSparseMoeBlock`](modeling_mixtral.md#MixtralSparseMoeBlock), [`rms_norm_eps`](mixtral_configuration.md#MixtralConfig.rms_norm_eps)
- used by: [`embed_tokens`](modeling_mixtral.md#MixtralModel.embed_tokens)

### `MixtralForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/mixtral/modeling_mixtral.py:718`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L718)
- doc: Mixtral model with a language modeling head for causal language modeling tasks.
- signature: `class MixtralForCausalLM(BaseCausalLMModule[MixtralModel, MixtralConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True)` — [`L765`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L765) — Forward pass through the Mixtral causal language model.
  - `__init__(self, config: MixtralConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L735`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L735) — Initialize Mixtral model for causal language modeling.
  - `_compute_aux_loss(self, outputs, attention_mask)` — [`L828`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L828) — Compute auxiliary load balancing loss from router logits.
- protocol/private: `_config_class`[`L733`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L733), `_model_type`[`L732`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L732), `_task_type`[`L731`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L731)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`MoeCausalLMOutput`](../../infra/modeling_outputs.md#MoeCausalLMOutput), [`auxiliary_load_balancing_loss_func`](../../infra/loss_utils.md#auxiliary_load_balancing_loss_func), [`forward_moe`](../_base/causal_lm_module.md#BaseCausalLMModule.forward_moe), [`MixtralConfig`](mixtral_configuration.md#MixtralConfig), [`MixtralModel`](modeling_mixtral.md#MixtralModel), [`num_local_experts`](../../infra/base_config.md#EasyDeLBaseConfig.num_local_experts)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `MixtralForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/mixtral/modeling_mixtral.py:850`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L850)
- doc: Mixtral model for sequence classification tasks.
- signature: `class MixtralForSequenceClassification(BaseSequenceClassificationModule[MixtralModel, MixtralConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None)` — [`L898`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L898) — Forward pass through the Mixtral sequence classification model.
  - `__init__(self, config: MixtralConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L867`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L867) — Initialize Mixtral model for sequence classification.
- protocol/private: `_config_class`[`L865`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L865), `_model_type`[`L864`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L864), `_task_type`[`L863`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L863)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`base_model`](../_base/_base_task_module.md#BaseTaskModule.base_model), `pad_token_id`, [`SequenceClassifierOutput`](../../infra/modeling_outputs.md#SequenceClassifierOutput), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`auxiliary_load_balancing_loss_func`](../../infra/loss_utils.md#auxiliary_load_balancing_loss_func), [`MixtralConfig`](mixtral_configuration.md#MixtralConfig), [`MixtralModel`](modeling_mixtral.md#MixtralModel), [`num_local_experts`](../../infra/base_config.md#EasyDeLBaseConfig.num_local_experts), [`attentions`](../../infra/modeling_outputs.md#MoeModelOutput.attentions), [`hidden_states`](../../infra/modeling_outputs.md#MoeModelOutput.hidden_states), [`last_hidden_state`](../../infra/modeling_outputs.md#MoeModelOutput.last_hidden_state), [`router_logits`](../../infra/modeling_outputs.md#MoeModelOutput.router_logits)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule)

### `MixtralMoEMlp`  ·  implements/extends Module
- def: [`easydel/modules/mixtral/modeling_mixtral.py:108`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L108)
- doc: Mixture of Experts MLP module for Mixtral models.
- signature: `class MixtralMoEMlp(nn.Module):`
- members:
  - `__call__(self, x: Array, group_sizes: Array, sorted_experts: Array | None = None)` — [`L196`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L196) — Apply SwiGLU feedforward transformation for MoE.
  - `__init__(self, config: MixtralConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L134) — Initialize Mixtral MoE MLP block.
  - `act_fn` — [`L194`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L194)
  - `config` — [`L154`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L154)
  - `dtype` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L155)
  - `param_dtype` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L156)
  - `precision` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L157)
  - `reform_param` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L115)
  - `w1` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L158)
  - `w2` — [`L170`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L170)
  - `w3` — [`L182`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L182)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`use_expert_tensor_mode`](../../infra/base_config.md#EasyDeLBaseConfig.use_expert_tensor_mode), [`ColumnParallelMoELinear`](../../layers/linears/_linear_moe.md#ColumnParallelMoELinear), [`RowParallelMoELinear`](../../layers/linears/_linear_moe.md#RowParallelMoELinear), [`MixtralConfig`](mixtral_configuration.md#MixtralConfig), [`hidden_size`](mixtral_configuration.md#MixtralConfig.hidden_size), [`num_local_experts`](mixtral_configuration.md#MixtralConfig.num_local_experts), [`intermediate_size`](mixtral_configuration.md#MixtralConfig.intermediate_size), [`hidden_act`](mixtral_configuration.md#MixtralConfig.hidden_act)
- used by: [`__call__`](modeling_mixtral.md#MixtralSparseMoeBlock.__call__), [`experts`](modeling_mixtral.md#MixtralSparseMoeBlock.experts)

### `MixtralModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/mixtral/modeling_mixtral.py:470`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L470)
- doc: The base Mixtral model transformer.
- signature: `class MixtralModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None)` — [`L551`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L551) — Forward pass through the Mixtral base model.
  - `__init__(self, config: MixtralConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L489`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L489) — Initialize Mixtral base model.
  - `get_decoder(self)` — [`L697`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L697) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L710`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L710) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L690`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L690) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L703`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L703) — Returns the language model head of the module.
  - `embed_tokens` — [`L515`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L515)
  - `layers` — [`L529`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L529)
  - `norm` — [`L543`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L543)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`MoeModelOutput`](../../infra/modeling_outputs.md#MoeModelOutput), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), `output_hidden_states`, [`router_logits`](../../infra/modeling_outputs.md#DecoderLayerOutput.router_logits), [`MixtralConfig`](mixtral_configuration.md#MixtralConfig), [`hidden_size`](mixtral_configuration.md#MixtralConfig.hidden_size), [`num_hidden_layers`](mixtral_configuration.md#MixtralConfig.num_hidden_layers), [`rms_norm_eps`](mixtral_configuration.md#MixtralConfig.rms_norm_eps), [`MixtralDecoderLayer`](modeling_mixtral.md#MixtralDecoderLayer), [`gradient_checkpointing`](mixtral_configuration.md#MixtralConfig.gradient_checkpointing), [`vocab_size`](mixtral_configuration.md#MixtralConfig.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`MixtralForCausalLM`](modeling_mixtral.md#MixtralForCausalLM), [`MixtralForSequenceClassification`](modeling_mixtral.md#MixtralForSequenceClassification), [`__init__`](modeling_mixtral.md#MixtralForCausalLM.__init__), [`__init__`](modeling_mixtral.md#MixtralForSequenceClassification.__init__)

### `MixtralSparseMoeBlock`  ·  implements/extends BaseMoeModule
- def: [`easydel/modules/mixtral/modeling_mixtral.py:219`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L219)
- doc: Sparse Mixture of Experts block for Mixtral models.
- signature: `class MixtralSparseMoeBlock(BaseMoeModule):`
- members:
  - `__call__(self, hidden_state: Array)` — [`L281`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L281) — Forward pass through the Sparse MoE block.
  - `__init__(self, config: MixtralConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L226`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L226) — Initialize Mixtral Sparse MoE block.
  - `dtype` — [`L256`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L256)
  - `experts` — [`L273`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L273)
  - `gate` — [`L261`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L261)
  - `param_dtype` — [`L257`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L257)
  - `precision` — [`L258`](../../../../../../../raw/code/EasyDeL/easydel/modules/mixtral/modeling_mixtral.py#L258)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`kernel`](../../layers/linears/_linear_moe.md#ParallelMoELinear.kernel), [`MoeRoutingStrategy`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy), [`moe_call`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_call), [`MoeLoadBalancingStrategy`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy), [`__init__`](../../layers/moe/_moe_module.md#BaseMoeModule.__init__), [`MixtralConfig`](mixtral_configuration.md#MixtralConfig), [`TOP_K`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy.TOP_K), [`STANDARD`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy.STANDARD), [`w1`](modeling_mixtral.md#MixtralMoEMlp.w1), [`w2`](modeling_mixtral.md#MixtralMoEMlp.w2), [`w3`](modeling_mixtral.md#MixtralMoEMlp.w3), [`hidden_size`](mixtral_configuration.md#MixtralConfig.hidden_size), [`act_fn`](modeling_mixtral.md#MixtralMoEMlp.act_fn), [`num_local_experts`](mixtral_configuration.md#MixtralConfig.num_local_experts), [`MixtralMoEMlp`](modeling_mixtral.md#MixtralMoEMlp), [`num_experts_per_tok`](mixtral_configuration.md#MixtralConfig.num_experts_per_tok)
- used by: [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`block_sparse_moe`](modeling_mixtral.md#MixtralDecoderLayer.block_sparse_moe)

