---
title: 'Module: easydel/modules/glm4_moe/modeling_glm4_moe.py'
type: catalog
provenance: extracted
module: easydel/modules/glm4_moe/modeling_glm4_moe.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.glm4_moe.modeling_glm4_moe`/Glm4Moe
symbols:
  Glm4MoeModel.__call__: Model#__call__().
  Glm4MoeDecoderLayer.__call__: DecoderLayer#__call__().
  Glm4MoeMoE.shared_experts: MoE#shared_experts.
  Glm4MoeMoE.__init__: MoE#__init__().
  Glm4MoeMoE.__call__: MoE#__call__().
  Glm4MoeModel: Model#
  Glm4MoeMLPStack.gate_proj: MLPStack#gate_proj.
  Glm4MoeMLPStack.down_proj: MLPStack#down_proj.
  Glm4MoeMLPStack.up_proj: MLPStack#up_proj.
  Glm4MoeModel.embed_tokens: Model#embed_tokens.
  Glm4MoeForCausalLM: ForCausalLM#
  Glm4MoeForSequenceClassification: ForSequenceClassification#
  Glm4MoeMLP.__call__: MLP#__call__().
  Glm4MoeTopKRouter.kernel: TopKRouter#kernel.
  Glm4MoeMLP.intermediate_size: MLP#intermediate_size.
  Glm4MoeTopKRouter.get_selected_experts: TopKRouter#get_selected_experts().
  Glm4MoeMLPStack.__call__: MLPStack#__call__().
  Glm4MoeDecoderLayer.layer_idx: DecoderLayer#layer_idx.
  Glm4MoeMLP.act_fn: MLP#act_fn.
  Glm4MoeTopKRouter.e_score_correction_bias: TopKRouter#e_score_correction_bias.
  Glm4MoeDecoderLayer.input_layernorm: DecoderLayer#input_layernorm.
  Glm4MoeDecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  Glm4MoeTopKRouter.n_routed_experts: TopKRouter#n_routed_experts.
  Glm4MoeTopKRouter.__call__: TopKRouter#__call__().
  Glm4MoeMoE.experts: MoE#experts.
  Glm4MoeForCausalLM.__init__: ForCausalLM#__init__().
  Glm4MoeForSequenceClassification.__init__: ForSequenceClassification#__init__().
  Glm4MoeMLPStack.act_fn: MLPStack#act_fn.
  Glm4MoeTopKRouter.n_group: TopKRouter#n_group.
  Glm4MoeMLP.gate_proj: MLP#gate_proj.
  Glm4MoeMLP.up_proj: MLP#up_proj.
  Glm4MoeMLP.down_proj: MLP#down_proj.
  Glm4MoeMoE.group_topk_k: MoE#group_topk_k.
  Glm4MoeModel.norm: Model#norm.
  Glm4MoeMoE: MoE#
  Glm4MoeTopKRouter.craft_sharding: TopKRouter#craft_sharding().
  Glm4MoeAttention.layer_idx: Attention#layer_idx.
  Glm4MoeModel.__init__: Model#__init__().
  Glm4MoeForCausalLM._task_type: ForCausalLM#_task_type.
  Glm4MoeForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  Glm4MoeModel.layers: Model#layers.
  Glm4MoeMLP: MLP#
  Glm4MoeMoE.config: MoE#config.
  Glm4MoeTopKRouter.top_k: TopKRouter#top_k.
  Glm4MoeTopKRouter.topk_group: TopKRouter#topk_group.
  Glm4MoeMoE.gate: MoE#gate.
  Glm4MoeAttention: Attention#
  Glm4MoeMLP.config: MLP#config.
  Glm4MoeMLP.__init__: MLP#__init__().
  Glm4MoeMLPStack.__init__: MLPStack#__init__().
  Glm4MoeTopKRouter.__init__: TopKRouter#__init__().
  Glm4MoeTopKRouter.routed_scaling_factor: TopKRouter#routed_scaling_factor.
  Glm4MoeTopKRouter.norm_topk_prob: TopKRouter#norm_topk_prob.
  Glm4MoeAttention.__init__: Attention#__init__().
  Glm4MoeDecoderLayer.__init__: DecoderLayer#__init__().
  Glm4MoeModel.padding_idx: Model#padding_idx.
  Glm4MoeModel.vocab_size: Model#vocab_size.
  Glm4MoeModel.get_embedding: Model#get_embedding().
  Glm4MoeForCausalLM._config_class: ForCausalLM#_config_class.
  Glm4MoeForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  Glm4MoeTopKRouter.config: TopKRouter#config.
  Glm4MoeMLPStack: MLPStack#
  Glm4MoeTopKRouter: TopKRouter#
  Glm4MoeMoE._select_experts_static: MoE#_select_experts_static().
  Glm4MoeDecoderLayer: DecoderLayer#
  Glm4MoeDecoderLayer.config: DecoderLayer#config.
  Glm4MoeDecoderLayer.self_attn: DecoderLayer#self_attn.
  Glm4MoeDecoderLayer.mlp: DecoderLayer#mlp.
  Glm4MoeMLP.dtype: MLP#dtype.
  Glm4MoeMLP.param_dtype: MLP#param_dtype.
  Glm4MoeMLP.precision: MLP#precision.
  Glm4MoeMLPStack.reform_param: MLPStack#reform_param.
  Glm4MoeMLPStack.config: MLPStack#config.
  Glm4MoeMLPStack.dtype: MLPStack#dtype.
  Glm4MoeMLPStack.param_dtype: MLPStack#param_dtype.
  Glm4MoeMLPStack.precision: MLPStack#precision.
  Glm4MoeTopKRouter.dtype: TopKRouter#dtype.
  Glm4MoeTopKRouter.param_dtype: TopKRouter#param_dtype.
  Glm4MoeTopKRouter.precision: TopKRouter#precision.
  Glm4MoeMoE.dtype: MoE#dtype.
  Glm4MoeMoE.param_dtype: MoE#param_dtype.
  Glm4MoeMoE.precision: MoE#precision.
  Glm4MoeDecoderLayer.dtype: DecoderLayer#dtype.
  Glm4MoeDecoderLayer.param_dtype: DecoderLayer#param_dtype.
  Glm4MoeDecoderLayer.precision: DecoderLayer#precision.
  Glm4MoeModel.get_encoder: Model#get_encoder().
  Glm4MoeModel.get_decoder: Model#get_decoder().
  Glm4MoeModel.get_lm_head: Model#get_lm_head().
  Glm4MoeForCausalLM._model_type: ForCausalLM#_model_type.
  Glm4MoeForSequenceClassification._model_type: ForSequenceClassification#_model_type.
---
# Module: [`easydel/modules/glm4_moe/modeling_glm4_moe.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py)

## Classes
### `Glm4MoeAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/glm4_moe/modeling_glm4_moe.py:516`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L516)
- doc: Multi-head attention layer with RoPE embeddings for GLM-4-MoE models.
- signature: `class Glm4MoeAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: Glm4MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L523`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L523) — Initialize GLM-4 MoE attention layer with grouped-query attention support.
  - `layer_idx` — [`L543`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L543)
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`Glm4MoeConfig`](glm4_moe_configuration.md#Glm4MoeConfig), [`use_qk_norm`](glm4_moe_configuration.md#Glm4MoeConfig.use_qk_norm)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`layer_idx`](modeling_glm4_moe.md#Glm4MoeDecoderLayer.layer_idx)

### `Glm4MoeDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/glm4_moe/modeling_glm4_moe.py:555`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L555)
- doc: Single decoder layer for GLM-4-MoE models.
- signature: `class Glm4MoeDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, output_router_logits: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L622`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L622) — Forward pass through the decoder layer.
  - `__init__(self, config: Glm4MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L564`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L564) — Initialize GLM-4 MoE decoder layer.
  - `config` — [`L585`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L585)
  - `dtype` — [`L586`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L586)
  - `input_layernorm` — [`L607`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L607)
  - `layer_idx` — [`L589`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L589)
  - `mlp` — [`L600`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L600)
  - `param_dtype` — [`L587`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L587)
  - `post_attention_layernorm` — [`L614`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L614)
  - `precision` — [`L588`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L588)
  - `self_attn` — [`L592`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L592)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`Glm4MoeConfig`](glm4_moe_configuration.md#Glm4MoeConfig), [`hidden_size`](glm4_moe_configuration.md#Glm4MoeConfig.hidden_size), [`Glm4MoeMoE`](modeling_glm4_moe.md#Glm4MoeMoE), [`Glm4MoeMLP`](modeling_glm4_moe.md#Glm4MoeMLP), [`Glm4MoeAttention`](modeling_glm4_moe.md#Glm4MoeAttention), [`rms_norm_eps`](glm4_moe_configuration.md#Glm4MoeConfig.rms_norm_eps), [`first_k_dense_replace`](glm4_moe_configuration.md#Glm4MoeConfig.first_k_dense_replace)
- used by: [`embed_tokens`](modeling_glm4_moe.md#Glm4MoeModel.embed_tokens)

### `Glm4MoeForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/glm4_moe/modeling_glm4_moe.py:936`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L936)
- doc: GLM-4 MoE model with a language modeling head for causal language modeling tasks.
- signature: `class Glm4MoeForCausalLM(BaseCausalLMModule[Glm4MoeModel, Glm4MoeConfig]):`
- members:
  - `__init__(self, config: Glm4MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L953`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L953) — Initialize GLM-4 MoE model for causal language modeling.
- protocol/private: `_config_class`[`L951`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L951), `_model_type`[`L950`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L950), `_task_type`[`L949`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L949)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`Glm4MoeConfig`](glm4_moe_configuration.md#Glm4MoeConfig), [`Glm4MoeModel`](modeling_glm4_moe.md#Glm4MoeModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `Glm4MoeForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/glm4_moe/modeling_glm4_moe.py:985`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L985)
- doc: GLM-4 MoE model for sequence classification tasks.
- signature: `class Glm4MoeForSequenceClassification(BaseSequenceClassificationModule[Glm4MoeModel, Glm4MoeConfig]):`
- members:
  - `__init__(self, config: Glm4MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1002`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L1002) — Initialize GLM-4 MoE model for sequence classification.
- protocol/private: `_config_class`[`L1000`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L1000), `_model_type`[`L999`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L999), `_task_type`[`L998`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L998)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`Glm4MoeConfig`](glm4_moe_configuration.md#Glm4MoeConfig), [`Glm4MoeModel`](modeling_glm4_moe.md#Glm4MoeModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule)

### `Glm4MoeMLP`  ·  implements/extends Module
- def: [`easydel/modules/glm4_moe/modeling_glm4_moe.py:62`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L62)
- doc: Dense feed-forward block used in non-MoE GLM-4-MoE layers.
- signature: `class Glm4MoeMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L120) — Apply gated feedforward transformation.
  - `__init__(self, config: Glm4MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, intermediate_size: int | None = None, *, rngs: nn.Rngs)` — [`L70`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L70) — Initialize GLM-4 MoE dense MLP block.
  - `act_fn` — [`L118`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L118)
  - `config` — [`L92`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L92)
  - `down_proj` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L117)
  - `dtype` — [`L93`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L93)
  - `gate_proj` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L115)
  - `intermediate_size` — [`L96`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L96)
  - `param_dtype` — [`L94`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L94)
  - `precision` — [`L95`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L95)
  - `up_proj` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L116)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`Glm4MoeConfig`](glm4_moe_configuration.md#Glm4MoeConfig), [`hidden_size`](glm4_moe_configuration.md#Glm4MoeConfig.hidden_size), [`initializer_range`](glm4_moe_configuration.md#Glm4MoeConfig.initializer_range), [`hidden_act`](glm4_moe_configuration.md#Glm4MoeConfig.hidden_act), [`intermediate_size`](glm4_moe_configuration.md#Glm4MoeConfig.intermediate_size)
- used by: [`shared_experts`](modeling_glm4_moe.md#Glm4MoeMoE.shared_experts), [`layer_idx`](modeling_glm4_moe.md#Glm4MoeDecoderLayer.layer_idx), [`layer_idx`](../glm4v_moe/modeling_glm4v_moe.md#Glm4vMoeTextDecoderLayer.layer_idx)

### `Glm4MoeMLPStack`  ·  implements/extends Module
- def: [`easydel/modules/glm4_moe/modeling_glm4_moe.py:146`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L146)
- doc: Expert MLP stack for GLM-4-MoE using parallel MoE linear layers.
- signature: `class Glm4MoeMLPStack(nn.Module):`
- members:
  - `__call__(self, x: Array, group_sizes: Array, sorted_experts: Array | None = None)` — [`L241`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L241) — Forward pass through expert MLP stack.
  - `__init__(self, config: Glm4MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L179) — Initialize GLM-4 MoE expert MLP stack.
  - `act_fn` — [`L239`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L239)
  - `config` — [`L199`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L199)
  - `down_proj` — [`L215`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L215)
  - `dtype` — [`L200`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L200)
  - `gate_proj` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L203)
  - `param_dtype` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L201)
  - `precision` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L202)
  - `reform_param` — [`L154`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L154)
  - `up_proj` — [`L227`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L227)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`use_expert_tensor_mode`](../../infra/base_config.md#EasyDeLBaseConfig.use_expert_tensor_mode), [`ColumnParallelMoELinear`](../../layers/linears/_linear_moe.md#ColumnParallelMoELinear), [`RowParallelMoELinear`](../../layers/linears/_linear_moe.md#RowParallelMoELinear), [`Glm4MoeConfig`](glm4_moe_configuration.md#Glm4MoeConfig), [`hidden_size`](glm4_moe_configuration.md#Glm4MoeConfig.hidden_size), [`n_routed_experts`](glm4_moe_configuration.md#Glm4MoeConfig.n_routed_experts), [`moe_intermediate_size`](glm4_moe_configuration.md#Glm4MoeConfig.moe_intermediate_size), [`hidden_act`](glm4_moe_configuration.md#Glm4MoeConfig.hidden_act)
- used by: [`__call__`](modeling_glm4_moe.md#Glm4MoeMoE.__call__), [`experts`](modeling_glm4_moe.md#Glm4MoeMoE.experts)

### `Glm4MoeMoE`  ·  implements/extends BaseMoeModule
- def: [`easydel/modules/glm4_moe/modeling_glm4_moe.py:373`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L373)
- doc: Mixture-of-Experts feed-forward module for GLM-4-MoE.
- signature: `class Glm4MoeMoE(BaseMoeModule):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L489`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L489) — Forward pass through the MoE layer.
  - `__init__(self, config: Glm4MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L381`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L381) — Initialize GLM-4 MoE layer.
  - `config` — [`L410`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L410)
  - `dtype` — [`L411`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L411)
  - `experts` — [`L416`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L416)
  - `gate` — [`L424`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L424)
  - `group_topk_k` — [`L414`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L414)
  - `param_dtype` — [`L412`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L412)
  - `precision` — [`L413`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L413)
  - `shared_experts` — [`L432`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L432)
- protocol/private: `_select_experts_static`[`L454`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L454)
- uses (calls/refs, reference-scoped): [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`kernel`](../../layers/linears/_linear_moe.md#ParallelMoELinear.kernel), [`MoeRoutingStrategy`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy), [`moe_call`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_call), [`MoeLoadBalancingStrategy`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy), [`__init__`](../../layers/moe/_moe_module.md#BaseMoeModule.__init__), [`moe_hooks`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_hooks), [`n_routed_experts`](../../layers/moe/_moe_module.md#BaseMoeModule.n_routed_experts), [`Glm4MoeConfig`](glm4_moe_configuration.md#Glm4MoeConfig), [`TOP_K`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy.TOP_K), [`STANDARD`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy.STANDARD), [`down_proj`](modeling_glm4_moe.md#Glm4MoeMLPStack.down_proj), [`gate_proj`](modeling_glm4_moe.md#Glm4MoeMLPStack.gate_proj), [`up_proj`](modeling_glm4_moe.md#Glm4MoeMLPStack.up_proj), [`hidden_size`](glm4_moe_configuration.md#Glm4MoeConfig.hidden_size), [`replace`](../../layers/moe/_communication_utils.md#MoeFusedHooks.replace), [`act_fn`](modeling_glm4_moe.md#Glm4MoeMLPStack.act_fn), [`n_routed_experts`](glm4_moe_configuration.md#Glm4MoeConfig.n_routed_experts), [`Glm4MoeMLP`](modeling_glm4_moe.md#Glm4MoeMLP), [`moe_intermediate_size`](glm4_moe_configuration.md#Glm4MoeConfig.moe_intermediate_size), [`n_group`](glm4_moe_configuration.md#Glm4MoeConfig.n_group), [`norm_topk_prob`](glm4_moe_configuration.md#Glm4MoeConfig.norm_topk_prob), [`num_experts_per_tok`](glm4_moe_configuration.md#Glm4MoeConfig.num_experts_per_tok), [`routed_scaling_factor`](glm4_moe_configuration.md#Glm4MoeConfig.routed_scaling_factor), [`topk_group`](glm4_moe_configuration.md#Glm4MoeConfig.topk_group), [`Glm4MoeMLPStack`](modeling_glm4_moe.md#Glm4MoeMLPStack), [`Glm4MoeTopKRouter`](modeling_glm4_moe.md#Glm4MoeTopKRouter), [`n_shared_experts`](glm4_moe_configuration.md#Glm4MoeConfig.n_shared_experts)
- used by: [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`layer_idx`](modeling_glm4_moe.md#Glm4MoeDecoderLayer.layer_idx), [`layer_idx`](../glm4v_moe/modeling_glm4v_moe.md#Glm4vMoeTextDecoderLayer.layer_idx)

### `Glm4MoeModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/glm4_moe/modeling_glm4_moe.py:690`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L690)
- doc: GLM-4 MoE (Mixture-of-Experts) model implementation.
- signature: `class Glm4MoeModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None)` — [`L768`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L768) — Forward pass through GLM-4-MoE base model with grouped expert routing.
  - `__init__(self, config: Glm4MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L705`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L705) — Initialize GLM-4 MoE base model.
  - `get_decoder(self)` — [`L910`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L910) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L926`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L926) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L902`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L902) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L918`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L918) — Returns the language model head of the module.
  - `embed_tokens` — [`L733`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L733)
  - `layers` — [`L747`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L747)
  - `norm` — [`L760`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L760)
  - `padding_idx` — [`L730`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L730)
  - `vocab_size` — [`L731`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L731)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), `pad_token_id`, [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`MoeModelOutput`](../../infra/modeling_outputs.md#MoeModelOutput), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`gradient_checkpointing`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing), [`router_logits`](../../infra/modeling_outputs.md#DecoderLayerOutput.router_logits), [`Glm4MoeConfig`](glm4_moe_configuration.md#Glm4MoeConfig), [`Glm4MoeDecoderLayer`](modeling_glm4_moe.md#Glm4MoeDecoderLayer), [`vocab_size`](glm4_moe_configuration.md#Glm4MoeConfig.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`Glm4MoeForCausalLM`](modeling_glm4_moe.md#Glm4MoeForCausalLM), [`Glm4MoeForSequenceClassification`](modeling_glm4_moe.md#Glm4MoeForSequenceClassification), [`__init__`](modeling_glm4_moe.md#Glm4MoeForCausalLM.__init__), [`__init__`](modeling_glm4_moe.md#Glm4MoeForSequenceClassification.__init__)

### `Glm4MoeTopKRouter`  ·  implements/extends Module
- def: [`easydel/modules/glm4_moe/modeling_glm4_moe.py:263`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L263)
- doc: Top-K expert router for GLM-4-MoE with grouped expert selection.
- signature: `class Glm4MoeTopKRouter(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L355`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L355) — Compute pre-activation router logits for input tokens.
  - `__init__(self, config: Glm4MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L271`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L271) — Initialize GLM-4 MoE Top-K router.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L316`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L316)
  - `get_selected_experts(self, scores)` — [`L320`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L320) — Select top-k experts using grouped routing strategy.
  - `config` — [`L290`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L290)
  - `dtype` — [`L291`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L291)
  - `e_score_correction_bias` — [`L308`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L308)
  - `kernel` — [`L301`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L301)
  - `n_group` — [`L297`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L297)
  - `n_routed_experts` — [`L295`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L295)
  - `norm_topk_prob` — [`L299`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L299)
  - `param_dtype` — [`L292`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L292)
  - `precision` — [`L293`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L293)
  - `routed_scaling_factor` — [`L296`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L296)
  - `top_k` — [`L294`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L294)
  - `topk_group` — [`L298`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe/modeling_glm4_moe.py#L298)
- uses (calls/refs, reference-scoped): [`ArrayParam`](../../infra/utils.md#ArrayParam), [`bound`](../../infra/utils.md#ArrayParam.bound), [`use_expert_tensor_mode`](../../infra/base_config.md#EasyDeLBaseConfig.use_expert_tensor_mode), [`Glm4MoeConfig`](glm4_moe_configuration.md#Glm4MoeConfig), [`hidden_size`](glm4_moe_configuration.md#Glm4MoeConfig.hidden_size), [`n_routed_experts`](glm4_moe_configuration.md#Glm4MoeConfig.n_routed_experts), [`initializer_range`](glm4_moe_configuration.md#Glm4MoeConfig.initializer_range), [`n_group`](glm4_moe_configuration.md#Glm4MoeConfig.n_group), [`norm_topk_prob`](glm4_moe_configuration.md#Glm4MoeConfig.norm_topk_prob), [`num_experts_per_tok`](glm4_moe_configuration.md#Glm4MoeConfig.num_experts_per_tok), [`routed_scaling_factor`](glm4_moe_configuration.md#Glm4MoeConfig.routed_scaling_factor), [`topk_group`](glm4_moe_configuration.md#Glm4MoeConfig.topk_group)
- used by: [`gate`](modeling_glm4_moe.md#Glm4MoeMoE.gate)

