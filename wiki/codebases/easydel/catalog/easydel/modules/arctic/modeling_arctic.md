---
title: 'Module: easydel/modules/arctic/modeling_arctic.py'
type: catalog
provenance: extracted
module: easydel/modules/arctic/modeling_arctic.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.arctic.modeling_arctic`/Arctic
symbols:
  ArcticModel.__call__: Model#__call__().
  ArcticDecoderLayer.__call__: DecoderLayer#__call__().
  ArcticForSequenceClassification.__call__: ForSequenceClassification#__call__().
  ArcticMoeBlock.__call__: MoeBlock#__call__().
  ArcticMoeBlock.__init__: MoeBlock#__init__().
  ArcticForCausalLM.__call__: ForCausalLM#__call__().
  ArcticModel: Model#
  ArcticMLPMoE.w1: MLPMoE#w1.
  ArcticMLPMoE.w3: MLPMoE#w3.
  ArcticMLPMoE.w2: MLPMoE#w2.
  ArcticModel.embed_tokens: Model#embed_tokens.
  ArcticForCausalLM: ForCausalLM#
  ArcticForSequenceClassification: ForSequenceClassification#
  ArcticMLPMoE.__call__: MLPMoE#__call__().
  ArcticMLP.__call__: MLP#__call__().
  ArcticDecoderLayer.parallel_attn_mlp_res: DecoderLayer#parallel_attn_mlp_res.
  ArcticMLP.ffn_dim: MLP#ffn_dim.
  ArcticMLPMoE.ffn_dim: MLPMoE#ffn_dim.
  ArcticMLPMoE.act_fn: MLPMoE#act_fn.
  ArcticDecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  ArcticMLP.act_fn: MLP#act_fn.
  ArcticMoeBlock.gate: MoeBlock#gate.
  ArcticDecoderLayer.input_layernorm: DecoderLayer#input_layernorm.
  ArcticDecoderLayer.residual_layernorm: DecoderLayer#residual_layernorm.
  ArcticForCausalLM._compute_aux_loss: ForCausalLM#_compute_aux_loss().
  ArcticMoeBlock.is_moe_layer: MoeBlock#is_moe_layer.
  ArcticAttention.__init__: Attention#__init__().
  ArcticAttention._create_rotary: Attention#_create_rotary().
  ArcticAttention._create_attention_performer: Attention#_create_attention_performer().
  ArcticMoeBlock.experts: MoeBlock#experts.
  ArcticForCausalLM.__init__: ForCausalLM#__init__().
  ArcticForSequenceClassification.__init__: ForSequenceClassification#__init__().
  ArcticMLPMoE.hidden_dim: MLPMoE#hidden_dim.
  ArcticMLP.hidden_dim: MLP#hidden_dim.
  ArcticMLP.w1: MLP#w1.
  ArcticMLP.w3: MLP#w3.
  ArcticMLP.w2: MLP#w2.
  ArcticModel.norm: Model#norm.
  ArcticDecoderLayer.block_sparse_moe: DecoderLayer#block_sparse_moe.
  ArcticAttention._create_q_proj: Attention#_create_q_proj().
  ArcticAttention._create_k_proj: Attention#_create_k_proj().
  ArcticAttention._create_v_proj: Attention#_create_v_proj().
  ArcticAttention._create_o_proj: Attention#_create_o_proj().
  ArcticModel.__init__: Model#__init__().
  ArcticForCausalLM._task_type: ForCausalLM#_task_type.
  ArcticForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  ArcticModel.layers: Model#layers.
  ArcticDecoderLayer.config: DecoderLayer#config.
  ArcticAttention: Attention#
  ArcticMoeBlock: MoeBlock#
  ArcticMoeBlock.mlp: MoeBlock#mlp.
  ArcticDecoderLayer.self_attn: DecoderLayer#self_attn.
  ArcticDecoderLayer.residual_mlp: DecoderLayer#residual_mlp.
  ArcticMLPMoE.config: MLPMoE#config.
  ArcticMLP.config: MLP#config.
  ArcticMLPMoE.__init__: MLPMoE#__init__().
  ArcticMLP.__init__: MLP#__init__().
  ArcticMoeBlock.hidden_dim: MoeBlock#hidden_dim.
  ArcticMoeBlock.num_experts: MoeBlock#num_experts.
  ArcticMoeBlock.top_k: MoeBlock#top_k.
  ArcticDecoderLayer.__init__: DecoderLayer#__init__().
  ArcticModel.get_embedding: Model#get_embedding().
  ArcticForCausalLM._config_class: ForCausalLM#_config_class.
  ArcticForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  ArcticMLP: MLP#
  ArcticMLPMoE: MLPMoE#
  ArcticMLPMoE.is_residual_mlp: MLPMoE#is_residual_mlp.
  ArcticMLP.is_residual_mlp: MLP#is_residual_mlp.
  ArcticDecoderLayer: DecoderLayer#
  ArcticMLPMoE.reform_param: MLPMoE#reform_param.
  ArcticMLPMoE.dtype: MLPMoE#dtype.
  ArcticMLPMoE.param_dtype: MLPMoE#param_dtype.
  ArcticMLPMoE.precision: MLPMoE#precision.
  ArcticMLP.dtype: MLP#dtype.
  ArcticMLP.param_dtype: MLP#param_dtype.
  ArcticMLP.precision: MLP#precision.
  ArcticMoeBlock.config: MoeBlock#config.
  ArcticMoeBlock.layer_idx: MoeBlock#layer_idx.
  ArcticMoeBlock.dtype: MoeBlock#dtype.
  ArcticMoeBlock.param_dtype: MoeBlock#param_dtype.
  ArcticMoeBlock.rngs: MoeBlock#rngs.
  ArcticDecoderLayer.layer_idx: DecoderLayer#layer_idx.
  ArcticDecoderLayer.dtype: DecoderLayer#dtype.
  ArcticDecoderLayer.param_dtype: DecoderLayer#param_dtype.
  ArcticDecoderLayer.rngs: DecoderLayer#rngs.
  ArcticModel.get_encoder: Model#get_encoder().
  ArcticModel.get_decoder: Model#get_decoder().
  ArcticModel.get_lm_head: Model#get_lm_head().
  ArcticForCausalLM._model_type: ForCausalLM#_model_type.
  ArcticForSequenceClassification._model_type: ForSequenceClassification#_model_type.
---
# Module: [`easydel/modules/arctic/modeling_arctic.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py)

## Classes
### `ArcticAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/arctic/modeling_arctic.py:64`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L64)
- doc: Multi-head attention layer with sliding window support for Arctic models.
- signature: `class ArcticAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: ArcticConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L71`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L71) — Initialize Arctic attention layer with sliding window configuration.
  - `_create_attention_performer(self, config: ArcticConfig, rngs: nn.Rngs)` — [`L214`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L214) — Create flexible attention module with Arctic configuration.
  - `_create_k_proj(self, config, dtype, param_dtype, precision, rngs)` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L128) — Create key projection layer with Arctic-specific bias configuration.
  - `_create_o_proj(self, config, dtype, param_dtype, precision, rngs)` — [`L176`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L176) — Create output projection layer with Arctic-specific bias configuration.
  - `_create_q_proj(self, config, dtype, param_dtype, precision, rngs)` — [`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L104) — Create query projection layer with Arctic-specific bias configuration.
  - `_create_rotary(self, config: ArcticConfig, dtype: jnp.dtype)` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L202) — Create rotary position embedding layer for Arctic attention.
  - `_create_v_proj(self, config, dtype, param_dtype, precision, rngs)` — [`L152`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L152) — Create value projection layer with Arctic-specific bias configuration.
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`get_basic_rope`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_rope), [`ArcticConfig`](arctic_configuration.md#ArcticConfig), [`sliding_window`](arctic_configuration.md#ArcticConfig.sliding_window)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_attention_performer`](../../layers/attention/_unified.md#UnifiedAttention._create_attention_performer), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`_create_o_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_o_proj), [`_create_q_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_q_proj), [`_create_k_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_k_proj), [`_create_v_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_v_proj), [`self_attn`](modeling_arctic.md#ArcticDecoderLayer.self_attn)

### `ArcticDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/arctic/modeling_arctic.py:541`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L541)
- doc: Single decoder layer for Arctic models.
- signature: `class ArcticDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, output_router_logits: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L624`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L624) — Forward pass through the decoder layer.
  - `__init__(self, config: ArcticConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L549`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L549) — Initialize Arctic decoder layer.
  - `block_sparse_moe` — [`L584`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L584)
  - `config` — [`L570`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L570)
  - `dtype` — [`L572`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L572)
  - `input_layernorm` — [`L592`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L592)
  - `layer_idx` — [`L571`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L571)
  - `parallel_attn_mlp_res` — [`L606`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L606)
  - `param_dtype` — [`L573`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L573)
  - `post_attention_layernorm` — [`L599`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L599)
  - `residual_layernorm` — [`L608`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L608)
  - `residual_mlp` — [`L615`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L615)
  - `rngs` — [`L574`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L574)
  - `self_attn` — [`L576`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L576)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`ArcticConfig`](arctic_configuration.md#ArcticConfig), [`hidden_size`](arctic_configuration.md#ArcticConfig.hidden_size), [`is_moe_layer`](modeling_arctic.md#ArcticMoeBlock.is_moe_layer), [`ArcticAttention`](modeling_arctic.md#ArcticAttention), [`ArcticMoeBlock`](modeling_arctic.md#ArcticMoeBlock), [`rms_norm_eps`](arctic_configuration.md#ArcticConfig.rms_norm_eps), [`ArcticMLP`](modeling_arctic.md#ArcticMLP), [`parallel_attn_mlp_res`](arctic_configuration.md#ArcticConfig.parallel_attn_mlp_res)
- used by: [`embed_tokens`](modeling_arctic.md#ArcticModel.embed_tokens)

### `ArcticForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/arctic/modeling_arctic.py:964`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L964)
- doc: Arctic model with a language modeling head for causal language modeling tasks.
- signature: `class ArcticForCausalLM(BaseCausalLMModule[ArcticModel, ArcticConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True)` — [`L1011`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L1011) — Forward pass through the Arctic causal language model.
  - `__init__(self, config: ArcticConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L981`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L981) — Initialize Arctic model for causal language modeling.
  - `_compute_aux_loss(self, outputs, attention_mask)` — [`L1064`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L1064) — Compute auxiliary load balancing loss from router logits.
- protocol/private: `_config_class`[`L979`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L979), `_model_type`[`L978`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L978), `_task_type`[`L977`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L977)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`MoeCausalLMOutput`](../../infra/modeling_outputs.md#MoeCausalLMOutput), [`auxiliary_load_balancing_loss_func`](../../infra/loss_utils.md#auxiliary_load_balancing_loss_func), [`forward_moe`](../_base/causal_lm_module.md#BaseCausalLMModule.forward_moe), [`ArcticConfig`](arctic_configuration.md#ArcticConfig), [`ArcticModel`](modeling_arctic.md#ArcticModel), [`num_local_experts`](../../infra/base_config.md#EasyDeLBaseConfig.num_local_experts)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `ArcticForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/arctic/modeling_arctic.py:1090`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L1090)
- doc: Arctic model for sequence classification tasks.
- signature: `class ArcticForSequenceClassification(BaseSequenceClassificationModule[ArcticModel, ArcticConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L1138`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L1138) — Forward pass through the Arctic sequence classification model.
  - `__init__(self, config: ArcticConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1107`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L1107) — Initialize Arctic model for sequence classification.
- protocol/private: `_config_class`[`L1105`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L1105), `_model_type`[`L1104`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L1104), `_task_type`[`L1103`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L1103)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`base_model`](../_base/_base_task_module.md#BaseTaskModule.base_model), `pad_token_id`, [`SequenceClassifierOutput`](../../infra/modeling_outputs.md#SequenceClassifierOutput), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`ArcticConfig`](arctic_configuration.md#ArcticConfig), [`ArcticModel`](modeling_arctic.md#ArcticModel), [`compute_router_aux_loss`](../_base/_base_task_module.md#BaseTaskModule.compute_router_aux_loss), [`attentions`](../../infra/modeling_outputs.md#MoeModelOutput.attentions), [`hidden_states`](../../infra/modeling_outputs.md#MoeModelOutput.hidden_states), [`last_hidden_state`](../../infra/modeling_outputs.md#MoeModelOutput.last_hidden_state)
- used by: [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule)

### `ArcticMLP`  ·  implements/extends Module
- def: [`easydel/modules/arctic/modeling_arctic.py:356`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L356)
- doc: Multi-Layer Perceptron module for Arctic models.
- signature: `class ArcticMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L405`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L405) — Apply SwiGLU feedforward transformation.
  - `__init__(self, config: ArcticConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, is_residual_mlp: bool = False, *, rngs: nn.Rngs)` — [`L363`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L363) — Initialize Arctic MLP block.
  - `act_fn` — [`L403`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L403)
  - `config` — [`L385`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L385)
  - `dtype` — [`L386`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L386)
  - `ffn_dim` — [`L391`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L391)
  - `hidden_dim` — [`L390`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L390)
  - `is_residual_mlp` — [`L389`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L389)
  - `param_dtype` — [`L387`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L387)
  - `precision` — [`L388`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L388)
  - `w1` — [`L400`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L400)
  - `w2` — [`L402`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L402)
  - `w3` — [`L401`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L401)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`ArcticConfig`](arctic_configuration.md#ArcticConfig), [`hidden_size`](arctic_configuration.md#ArcticConfig.hidden_size), [`hidden_act`](arctic_configuration.md#ArcticConfig.hidden_act), [`intermediate_size`](arctic_configuration.md#ArcticConfig.intermediate_size)
- used by: [`mlp`](modeling_arctic.md#ArcticMoeBlock.mlp), [`residual_mlp`](modeling_arctic.md#ArcticDecoderLayer.residual_mlp)

### `ArcticMLPMoE`  ·  implements/extends Module
- def: [`easydel/modules/arctic/modeling_arctic.py:231`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L231)
- doc: Mixture-of-Experts MLP block for Arctic models.
- signature: `class ArcticMLPMoE(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], group_sizes: Array, sorted_experts: Array | None = None)` — [`L322`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L322) — Apply SwiGLU feedforward transformation through experts.
  - `__init__(self, config: ArcticConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, is_residual_mlp: bool = False, *, rngs: nn.Rngs)` — [`L254`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L254) — Initialize Arctic MoE MLP block.
  - `act_fn` — [`L320`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L320)
  - `config` — [`L276`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L276)
  - `dtype` — [`L277`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L277)
  - `ffn_dim` — [`L282`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L282)
  - `hidden_dim` — [`L281`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L281)
  - `is_residual_mlp` — [`L280`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L280)
  - `param_dtype` — [`L278`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L278)
  - `precision` — [`L279`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L279)
  - `reform_param` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L238)
  - `w1` — [`L284`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L284)
  - `w2` — [`L308`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L308)
  - `w3` — [`L296`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L296)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`use_expert_tensor_mode`](../../infra/base_config.md#EasyDeLBaseConfig.use_expert_tensor_mode), [`ColumnParallelMoELinear`](../../layers/linears/_linear_moe.md#ColumnParallelMoELinear), [`RowParallelMoELinear`](../../layers/linears/_linear_moe.md#RowParallelMoELinear), [`ArcticConfig`](arctic_configuration.md#ArcticConfig), [`hidden_size`](arctic_configuration.md#ArcticConfig.hidden_size), [`num_local_experts`](arctic_configuration.md#ArcticConfig.num_local_experts), [`hidden_act`](arctic_configuration.md#ArcticConfig.hidden_act), [`intermediate_size`](arctic_configuration.md#ArcticConfig.intermediate_size)
- used by: [`__call__`](modeling_arctic.md#ArcticMoeBlock.__call__), [`experts`](modeling_arctic.md#ArcticMoeBlock.experts)

### `ArcticModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/arctic/modeling_arctic.py:714`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L714)
- doc: Arctic model implementation.
- signature: `class ArcticModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None)` — [`L790`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L790) — Forward pass through the Arctic base model.
  - `__init__(self, config: ArcticConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L728`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L728) — Initialize Arctic base model.
  - `get_decoder(self)` — [`L938`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L938) — Returns the decoder part of the model.
  - `get_embedding(self)` — [`L954`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L954) — Returns the embedding layer.
  - `get_encoder(self)` — [`L930`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L930) — Returns the encoder part of the model.
  - `get_lm_head(self)` — [`L946`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L946) — Returns the language model head.
  - `embed_tokens` — [`L754`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L754)
  - `layers` — [`L768`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L768)
  - `norm` — [`L782`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L782)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`MoeModelOutput`](../../infra/modeling_outputs.md#MoeModelOutput), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), `output_hidden_states`, [`router_logits`](../../infra/modeling_outputs.md#DecoderLayerOutput.router_logits), [`ArcticConfig`](arctic_configuration.md#ArcticConfig), [`num_hidden_layers`](arctic_configuration.md#ArcticConfig.num_hidden_layers), [`ArcticDecoderLayer`](modeling_arctic.md#ArcticDecoderLayer), [`gradient_checkpointing`](arctic_configuration.md#ArcticConfig.gradient_checkpointing)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`ArcticForCausalLM`](modeling_arctic.md#ArcticForCausalLM), [`ArcticForSequenceClassification`](modeling_arctic.md#ArcticForSequenceClassification), [`__init__`](modeling_arctic.md#ArcticForCausalLM.__init__), [`__init__`](modeling_arctic.md#ArcticForSequenceClassification.__init__)

### `ArcticMoeBlock`  ·  implements/extends BaseMoeModule
- def: [`easydel/modules/arctic/modeling_arctic.py:432`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L432)
- doc: Mixture-of-Experts block for Arctic models.
- signature: `class ArcticMoeBlock(BaseMoeModule):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L511`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L511) — Forward pass through the MoE or MLP block.
  - `__init__(self, config: ArcticConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L439`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L439) — Initialize Arctic MoE block.
  - `config` — [`L471`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L471)
  - `dtype` — [`L473`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L473)
  - `experts` — [`L494`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L494)
  - `gate` — [`L484`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L484)
  - `hidden_dim` — [`L477`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L477)
  - `is_moe_layer` — [`L481`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L481)
  - `layer_idx` — [`L472`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L472)
  - `mlp` — [`L502`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L502)
  - `num_experts` — [`L478`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L478)
  - `param_dtype` — [`L474`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L474)
  - `rngs` — [`L475`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L475)
  - `top_k` — [`L480`](../../../../../../../raw/code/EasyDeL/easydel/modules/arctic/modeling_arctic.py#L480)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`kernel`](../../layers/linears/_linear_moe.md#ParallelMoELinear.kernel), [`MoeRoutingStrategy`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy), [`moe_call`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_call), [`MoeLoadBalancingStrategy`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy), [`__init__`](../../layers/moe/_moe_module.md#BaseMoeModule.__init__), [`ArcticConfig`](arctic_configuration.md#ArcticConfig), [`TOP_K`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy.TOP_K), [`STANDARD`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy.STANDARD), [`w1`](modeling_arctic.md#ArcticMLPMoE.w1), [`w2`](modeling_arctic.md#ArcticMLPMoE.w2), [`w3`](modeling_arctic.md#ArcticMLPMoE.w3), [`act_fn`](modeling_arctic.md#ArcticMLPMoE.act_fn), [`hidden_size`](arctic_configuration.md#ArcticConfig.hidden_size), [`num_local_experts`](arctic_configuration.md#ArcticConfig.num_local_experts), [`ArcticMLP`](modeling_arctic.md#ArcticMLP), [`num_experts_per_tok`](arctic_configuration.md#ArcticConfig.num_experts_per_tok), [`ArcticMLPMoE`](modeling_arctic.md#ArcticMLPMoE), [`moe_layer_frequency`](arctic_configuration.md#ArcticConfig.moe_layer_frequency)
- used by: [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`parallel_attn_mlp_res`](modeling_arctic.md#ArcticDecoderLayer.parallel_attn_mlp_res), [`block_sparse_moe`](modeling_arctic.md#ArcticDecoderLayer.block_sparse_moe)

