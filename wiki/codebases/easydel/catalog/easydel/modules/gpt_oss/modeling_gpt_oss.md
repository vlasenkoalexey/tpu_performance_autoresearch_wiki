---
title: 'Module: easydel/modules/gpt_oss/modeling_gpt_oss.py'
type: catalog
provenance: extracted
module: easydel/modules/gpt_oss/modeling_gpt_oss.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.gpt_oss.modeling_gpt_oss`/GptOss
symbols:
  GptOssModel.__call__: Model#__call__().
  GptOssDecoderLayer.__call__: DecoderLayer#__call__().
  GptOssMLP.__init__: MLP#__init__().
  GptOssForSequenceClassification.__call__: ForSequenceClassification#__call__().
  GptOssMLP.__call__: MLP#__call__().
  GptOssForCausalLM.__call__: ForCausalLM#__call__().
  GptOssModel.embed_tokens: Model#embed_tokens.
  GptOssModel: Model#
  GptOssExperts.gate_proj: Experts#gate_proj.
  GptOssExperts.down_proj: Experts#down_proj.
  GptOssExperts.up_proj: Experts#up_proj.
  GptOssForCausalLM: ForCausalLM#
  GptOssForSequenceClassification: ForSequenceClassification#
  GptOssMLP.experts: MLP#experts.
  GptOssMLP.router: MLP#router.
  GptOssExperts.__call__: Experts#__call__().
  GptOssAttention.__init__: Attention#__init__().
  GptOssAttention.sinks: Attention#sinks.
  GptOssForCausalLM.__init__: ForCausalLM#__init__().
  GptOssDecoderLayer.input_layernorm: DecoderLayer#input_layernorm.
  GptOssDecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  GptOssModel.norm: Model#norm.
  GptOssForCausalLM._aux_loss_fn: ForCausalLM#_aux_loss_fn().
  GptOssForSequenceClassification.__init__: ForSequenceClassification#__init__().
  GptOssExperts.act_fn: Experts#act_fn.
  GptOssMLP.ffn_activation: MLP#ffn_activation().
  GptOssRMSNorm: RMSNorm#
  GptOssModel.__init__: Model#__init__().
  GptOssForCausalLM._task_type: ForCausalLM#_task_type.
  GptOssForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  GptOssModel.layers: Model#layers.
  GptOssExperts.intermediate_size: Experts#intermediate_size.
  GptOssMLP: MLP#
  GptOssMLP._scatter_topk_probs: MLP#_scatter_topk_probs().
  GptOssAttention: Attention#
  GptOssDecoderLayer.self_attn: DecoderLayer#self_attn.
  GptOssDecoderLayer.mlp: DecoderLayer#mlp.
  GptOssExperts.__init__: Experts#__init__().
  GptOssExperts.num_experts: Experts#num_experts.
  GptOssExperts.hidden_size: Experts#hidden_size.
  GptOssExperts.expert_dim: Experts#expert_dim.
  GptOssDecoderLayer.__init__: DecoderLayer#__init__().
  GptOssDecoderLayer.attention_type: DecoderLayer#attention_type.
  GptOssModel.get_embedding: Model#get_embedding().
  GptOssForCausalLM._config_class: ForCausalLM#_config_class.
  GptOssForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  GptOssExperts.alpha: Experts#alpha.
  GptOssExperts: Experts#
  GptOssMLP._softmax_topk_weights: MLP#_softmax_topk_weights().
  GptOssDecoderLayer: DecoderLayer#
  GptOssDecoderLayer.config: DecoderLayer#config.
  GptOssExperts.reform_param: Experts#reform_param.
  GptOssExperts.config: Experts#config.
  GptOssExperts.dtype: Experts#dtype.
  GptOssExperts.param_dtype: Experts#param_dtype.
  GptOssExperts.precision: Experts#precision.
  GptOssAttention.craft_sharding: Attention#craft_sharding().
  GptOssDecoderLayer.dtype: DecoderLayer#dtype.
  GptOssDecoderLayer.param_dtype: DecoderLayer#param_dtype.
  GptOssDecoderLayer.precision: DecoderLayer#precision.
  GptOssDecoderLayer.layer_idx: DecoderLayer#layer_idx.
  GptOssModel.get_encoder: Model#get_encoder().
  GptOssModel.get_decoder: Model#get_decoder().
  GptOssModel.get_lm_head: Model#get_lm_head().
  GptOssForCausalLM._model_type: ForCausalLM#_model_type.
  GptOssForSequenceClassification._model_type: ForSequenceClassification#_model_type.
  GptOssForSequenceClassification.get_encoder: ForSequenceClassification#get_encoder().
  GptOssForSequenceClassification.get_decoder: ForSequenceClassification#get_decoder().
  GptOssForSequenceClassification.get_lm_head: ForSequenceClassification#get_lm_head().
  GptOssForSequenceClassification.get_embedding: ForSequenceClassification#get_embedding().
  GptOssForSequenceClassification.get_task_head: ForSequenceClassification#get_task_head().
---
# Module: [`easydel/modules/gpt_oss/modeling_gpt_oss.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py)

## Classes
### `GptOssAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/gpt_oss/modeling_gpt_oss.py:375`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L375)
- doc: GPT-OSS Attention module with sink tokens support.
- signature: `class GptOssAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: GptOssConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L395`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L395) — Initialize GPT-OSS attention with sink tokens.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L444`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L444) — Return sharding specs for sink parameters.
  - `sinks` — [`L436`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L436)
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`ArrayParam`](../../infra/utils.md#ArrayParam), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`bound`](../../infra/utils.md#ArrayParam.bound), [`GptOssConfig`](gpt_oss_configuration.md#GptOssConfig), [`layer_types`](gpt_oss_configuration.md#GptOssConfig.layer_types), [`initializer_range`](gpt_oss_configuration.md#GptOssConfig.initializer_range), [`num_attention_heads`](gpt_oss_configuration.md#GptOssConfig.num_attention_heads), [`sliding_window`](gpt_oss_configuration.md#GptOssConfig.sliding_window)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`self_attn`](modeling_gpt_oss.md#GptOssDecoderLayer.self_attn)

### `GptOssDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/gpt_oss/modeling_gpt_oss.py:449`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L449)
- doc: GPT-OSS decoder layer with attention and Mixture-of-Experts MLP.
- signature: `class GptOssDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, output_router_logits: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L534`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L534) — Forward pass of the GPT-OSS decoder layer.
  - `__init__(self, config: GptOssConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L475`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L475) — Initialize the GPT-OSS decoder layer.
  - `attention_type` — [`L532`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L532)
  - `config` — [`L496`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L496)
  - `dtype` — [`L497`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L497)
  - `input_layernorm` — [`L518`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L518)
  - `layer_idx` — [`L500`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L500)
  - `mlp` — [`L511`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L511)
  - `param_dtype` — [`L498`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L498)
  - `post_attention_layernorm` — [`L525`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L525)
  - `precision` — [`L499`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L499)
  - `self_attn` — [`L502`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L502)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`GptOssConfig`](gpt_oss_configuration.md#GptOssConfig), [`layer_types`](gpt_oss_configuration.md#GptOssConfig.layer_types), [`hidden_size`](gpt_oss_configuration.md#GptOssConfig.hidden_size), [`GptOssRMSNorm`](modeling_gpt_oss.md#GptOssRMSNorm), [`GptOssAttention`](modeling_gpt_oss.md#GptOssAttention), [`GptOssMLP`](modeling_gpt_oss.md#GptOssMLP), [`rms_norm_eps`](gpt_oss_configuration.md#GptOssConfig.rms_norm_eps)
- used by: [`embed_tokens`](modeling_gpt_oss.md#GptOssModel.embed_tokens)

### `GptOssExperts`  ·  implements/extends Module
- def: [`easydel/modules/gpt_oss/modeling_gpt_oss.py:81`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L81)
- doc: Grouped expert feed-forward network used inside GPT-OSS MoE layers.
- signature: `class GptOssExperts(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], group_sizes: Array, sorted_experts: Array | None = None)` — [`L208`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L208) — Forward pass through the expert MLP network.
  - `__init__(self, config: GptOssConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L140) — Initialize the GptOssExperts module.
  - `act_fn` — [`L206`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L206)
  - `alpha` — [`L205`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L205)
  - `config` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L159)
  - `down_proj` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L181)
  - `dtype` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L160)
  - `expert_dim` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L167)
  - `gate_proj` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L169)
  - `hidden_size` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L166)
  - `intermediate_size` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L164)
  - `num_experts` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L165)
  - `param_dtype` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L161)
  - `precision` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L162)
  - `reform_param` — [`L111`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L111)
  - `up_proj` — [`L193`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L193)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`use_expert_tensor_mode`](../../infra/base_config.md#EasyDeLBaseConfig.use_expert_tensor_mode), [`ColumnParallelMoELinear`](../../layers/linears/_linear_moe.md#ColumnParallelMoELinear), [`RowParallelMoELinear`](../../layers/linears/_linear_moe.md#RowParallelMoELinear), [`GptOssConfig`](gpt_oss_configuration.md#GptOssConfig), [`hidden_size`](gpt_oss_configuration.md#GptOssConfig.hidden_size), [`num_local_experts`](gpt_oss_configuration.md#GptOssConfig.num_local_experts), [`intermediate_size`](gpt_oss_configuration.md#GptOssConfig.intermediate_size), [`hidden_act`](gpt_oss_configuration.md#GptOssConfig.hidden_act)
- used by: [`__call__`](modeling_gpt_oss.md#GptOssMLP.__call__), [`experts`](modeling_gpt_oss.md#GptOssMLP.experts), [`ffn_activation`](modeling_gpt_oss.md#GptOssMLP.ffn_activation)

### `GptOssForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/gpt_oss/modeling_gpt_oss.py:863`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L863)
- doc: GPT-OSS model with a Causal Language Modeling head.
- signature: `class GptOssForCausalLM(BaseCausalLMModule[GptOssModel, GptOssConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True)` — [`L918`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L918) — Forward pass for GPT-OSS Causal Language Model.
  - `__init__(self, config: GptOssConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L888`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L888) — Initialize the GPT-OSS Causal LM module.
  - `_aux_loss_fn(outputs, attention_mask)` — [`L978`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L978) — Custom auxiliary loss for GPT-OSS.
- protocol/private: `_config_class`[`L886`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L886), `_model_type`[`L885`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L885), `_task_type`[`L884`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L884)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`MoeCausalLMOutput`](../../infra/modeling_outputs.md#MoeCausalLMOutput), [`auxiliary_load_balancing_loss_func`](../../infra/loss_utils.md#auxiliary_load_balancing_loss_func), [`forward_moe`](../_base/causal_lm_module.md#BaseCausalLMModule.forward_moe), [`GptOssConfig`](gpt_oss_configuration.md#GptOssConfig), [`GptOssModel`](modeling_gpt_oss.md#GptOssModel), [`num_local_experts`](../../infra/base_config.md#EasyDeLBaseConfig.num_local_experts), [`router_aux_loss_coef`](gpt_oss_configuration.md#GptOssConfig.router_aux_loss_coef)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `GptOssForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/gpt_oss/modeling_gpt_oss.py:1007`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L1007)
- doc: GptOss model with a Sequence Classification head.
- signature: `class GptOssForSequenceClassification(BaseSequenceClassificationModule[GptOssModel, GptOssConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None)` — [`L1065`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L1065) — Forward pass of the GptOssForSequenceClassification model.
  - `__init__(self, config: GptOssConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1031`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L1031) — Initializes the GptOssForSequenceClassification model.
  - `get_decoder(self)` — [`L1168`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L1168) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L1181`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L1181) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L1161`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L1161) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L1174`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L1174) — Returns the language model head of the module.
  - `get_task_head(self)` — [`L1187`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L1187) — Returns the sequence classification head.
- protocol/private: `_config_class`[`L1029`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L1029), `_model_type`[`L1028`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L1028), `_task_type`[`L1027`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L1027)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), `pad_token_id`, [`SequenceClassifierOutput`](../../infra/modeling_outputs.md#SequenceClassifierOutput), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`auxiliary_load_balancing_loss_func`](../../infra/loss_utils.md#auxiliary_load_balancing_loss_func), [`GptOssConfig`](gpt_oss_configuration.md#GptOssConfig), [`GptOssModel`](modeling_gpt_oss.md#GptOssModel), [`num_local_experts`](../../infra/base_config.md#EasyDeLBaseConfig.num_local_experts)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_lm_head), [`get_task_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_task_head)

### `GptOssMLP`  ·  implements/extends BaseMoeModule
- def: [`easydel/modules/gpt_oss/modeling_gpt_oss.py:241`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L241)
- doc: Mixture-of-Experts MLP module for GPT-OSS.
- signature: `class GptOssMLP(BaseMoeModule):`
- members:
  - `__call__(self, hidden_states, training=False, layer_idx=None)` — [`L329`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L329) — Forward pass through the MoE MLP.
  - `__init__(self, config: GptOssConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L263`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L263) — Initialize the GptOssMLP module.
  - `ffn_activation(w0, w1)` — [`L352`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L352)
  - `experts` — [`L306`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L306)
  - `router` — [`L296`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L296)
- protocol/private: `_scatter_topk_probs`[`L314`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L314), `_softmax_topk_weights`[`L321`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L321)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`kernel`](../../layers/linears/_linear_moe.md#ParallelMoELinear.kernel), [`MoeRoutingStrategy`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy), [`moe_call`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_call), [`MoeLoadBalancingStrategy`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy), [`__init__`](../../layers/moe/_moe_module.md#BaseMoeModule.__init__), [`moe_hooks`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_hooks), [`GptOssConfig`](gpt_oss_configuration.md#GptOssConfig), [`TOP_K`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy.TOP_K), [`STANDARD`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy.STANDARD), [`down_proj`](modeling_gpt_oss.md#GptOssExperts.down_proj), [`gate_proj`](modeling_gpt_oss.md#GptOssExperts.gate_proj), [`up_proj`](modeling_gpt_oss.md#GptOssExperts.up_proj), [`num_experts_per_tok`](../../layers/moe/_moe_module.md#BaseMoeModule.num_experts_per_tok), [`bias`](../../layers/linears/_linear_moe.md#ParallelMoELinear.bias), [`hidden_size`](gpt_oss_configuration.md#GptOssConfig.hidden_size), [`replace`](../../layers/moe/_communication_utils.md#MoeFusedHooks.replace), [`act_fn`](modeling_gpt_oss.md#GptOssExperts.act_fn), [`num_local_experts`](gpt_oss_configuration.md#GptOssConfig.num_local_experts), [`alpha`](modeling_gpt_oss.md#GptOssExperts.alpha), [`initializer_range`](gpt_oss_configuration.md#GptOssConfig.initializer_range), [`GptOssExperts`](modeling_gpt_oss.md#GptOssExperts), [`num_experts_per_tok`](gpt_oss_configuration.md#GptOssConfig.num_experts_per_tok)
- used by: [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`mlp`](modeling_gpt_oss.md#GptOssDecoderLayer.mlp)

### `GptOssModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/gpt_oss/modeling_gpt_oss.py:605`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L605)
- doc: The base GptOss model transformer.
- signature: `class GptOssModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None)` — [`L686`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L686) — Performs forward pass through the GPT-OSS transformer model.
  - `__init__(self, config: GptOssConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L624`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L624) — Initializes the GptOssModel.
  - `get_decoder(self)` — [`L842`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L842) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L855`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L855) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L835`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L835) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L848`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L848) — Returns the language model head of the module.
  - `embed_tokens` — [`L650`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L650)
  - `layers` — [`L664`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L664)
  - `norm` — [`L678`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L678)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`MoeModelOutput`](../../infra/modeling_outputs.md#MoeModelOutput), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), `output_hidden_states`, [`gradient_checkpointing`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing), [`router_logits`](../../infra/modeling_outputs.md#DecoderLayerOutput.router_logits), [`GptOssConfig`](gpt_oss_configuration.md#GptOssConfig), [`hidden_size`](gpt_oss_configuration.md#GptOssConfig.hidden_size), [`GptOssRMSNorm`](modeling_gpt_oss.md#GptOssRMSNorm), [`rms_norm_eps`](gpt_oss_configuration.md#GptOssConfig.rms_norm_eps), [`num_hidden_layers`](gpt_oss_configuration.md#GptOssConfig.num_hidden_layers), [`GptOssDecoderLayer`](modeling_gpt_oss.md#GptOssDecoderLayer), [`vocab_size`](gpt_oss_configuration.md#GptOssConfig.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`GptOssForCausalLM`](modeling_gpt_oss.md#GptOssForCausalLM), [`GptOssForSequenceClassification`](modeling_gpt_oss.md#GptOssForSequenceClassification), [`__init__`](modeling_gpt_oss.md#GptOssForCausalLM.__init__), [`__init__`](modeling_gpt_oss.md#GptOssForSequenceClassification.__init__)

### `GptOssRMSNorm`  ·  implements/extends RMSNorm
- def: [`easydel/modules/gpt_oss/modeling_gpt_oss.py:64`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/modeling_gpt_oss.py#L64)
- doc: GPT-OSS RMS Normalization layer.
- signature: `class GptOssRMSNorm(RMSNorm):`
- uses (calls/refs, reference-scoped): [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm)
- used by: [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`input_layernorm`](modeling_gpt_oss.md#GptOssDecoderLayer.input_layernorm), [`norm`](modeling_gpt_oss.md#GptOssModel.norm), [`post_attention_layernorm`](modeling_gpt_oss.md#GptOssDecoderLayer.post_attention_layernorm)

