---
title: 'Module: easydel/modules/deepseek_v2/modeling_deepseek.py'
type: catalog
provenance: extracted
module: easydel/modules/deepseek_v2/modeling_deepseek.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.deepseek_v2.modeling_deepseek`/
symbols:
  DeepseekV2Attention.define_network: DeepseekV2Attention#define_network().
  DeepseekV2Model.__call__: DeepseekV2Model#__call__().
  DeepseekV2DecoderLayer.__call__: DeepseekV2DecoderLayer#__call__().
  DeepseekV2MoE.__call__: DeepseekV2MoE#__call__().
  DeepseekV2MoE.shared_experts: DeepseekV2MoE#shared_experts.
  DeepseekV2MoE.__init__: DeepseekV2MoE#__init__().
  DeepseekV2ForCausalLM.__call__: DeepseekV2ForCausalLM#__call__().
  DeepseekV2ForCausalLM.create_ragged_page_cache_config: DeepseekV2ForCausalLM#create_ragged_page_cache_config().
  DeepseekV2Model.embed_tokens: DeepseekV2Model#embed_tokens.
  DeepseekV2ForCausalLM: DeepseekV2ForCausalLM#
  DeepseekV2Model: DeepseekV2Model#
  DeepseekV2MLPMoE.__call__: DeepseekV2MLPMoE#__call__().
  DeepseekV2MLP.__call__: DeepseekV2MLP#__call__().
  MoEGate.kernel: MoEGate#kernel.
  DeepseekV2Attention._create_attention_performer: DeepseekV2Attention#_create_attention_performer().
  DeepseekV2MoE.experts: DeepseekV2MoE#experts.
  DeepseekV2MLPMoE.gate_proj: DeepseekV2MLPMoE#gate_proj.
  DeepseekV2MLPMoE.up_proj: DeepseekV2MLPMoE#up_proj.
  DeepseekV2MLPMoE.down_proj: DeepseekV2MLPMoE#down_proj.
  DeepseekV2MLP.config: DeepseekV2MLP#config.
  DeepseekV2MoE.gate: DeepseekV2MoE#gate.
  DeepseekV2DecoderLayer.mlp: DeepseekV2DecoderLayer#mlp.
  DeepseekV2DecoderLayer.input_layernorm: DeepseekV2DecoderLayer#input_layernorm.
  DeepseekV2DecoderLayer.post_attention_layernorm: DeepseekV2DecoderLayer#post_attention_layernorm.
  DeepseekV2Attention.projection_mapping: DeepseekV2Attention#projection_mapping.
  DeepseekV2Attention.q_head_dim: DeepseekV2Attention#q_head_dim.
  DeepseekV2Attention.kv_lora_rank: DeepseekV2Attention#kv_lora_rank.
  DeepseekV2Attention.rotary: DeepseekV2Attention#rotary.
  DeepseekV2DecoderLayer.hidden_size: DeepseekV2DecoderLayer#hidden_size.
  DeepseekV2ForCausalLM.__init__: DeepseekV2ForCausalLM#__init__().
  DeepseekV2ForCausalLM.create_transformer_cache_config: DeepseekV2ForCausalLM#create_transformer_cache_config().
  DeepseekV2MLPMoE.config: DeepseekV2MLPMoE#config.
  DeepseekV2MLPMoE.act_fn: DeepseekV2MLPMoE#act_fn.
  DeepseekV2MLP.act_fn: DeepseekV2MLP#act_fn.
  DeepseekV2Model.norm: DeepseekV2Model#norm.
  DeepseekV2Model.frequencies: DeepseekV2Model#frequencies().
  DeepseekV2ForCausalLM._compute_aux_loss: DeepseekV2ForCausalLM#_compute_aux_loss().
  MoEGate.craft_sharding: MoEGate#craft_sharding().
  MoEGate.__call__: MoEGate#__call__().
  DeepseekV2Model.__init__: DeepseekV2Model#__init__().
  DeepseekV2ForCausalLM._task_type: DeepseekV2ForCausalLM#_task_type.
  DeepseekV2Attention.v_head_dim: DeepseekV2Attention#v_head_dim.
  DeepseekV2Model.layers: DeepseekV2Model#layers.
  MoEGate.n_routed_experts: MoEGate#n_routed_experts.
  MoEGate.gating_dim: MoEGate#gating_dim.
  DeepseekV2MoE: DeepseekV2MoE#
  DeepseekV2Attention: DeepseekV2Attention#
  DeepseekV2DecoderLayer.self_attn: DeepseekV2DecoderLayer#self_attn.
  DeepseekV2Attention.config: DeepseekV2Attention#config.
  DeepseekV2MLPMoE.__init__: DeepseekV2MLPMoE#__init__().
  DeepseekV2MLP.__init__: DeepseekV2MLP#__init__().
  MoEGate.__init__: MoEGate#__init__().
  MoEGate.top_k: MoEGate#top_k.
  MoEGate.routed_scaling_factor: MoEGate#routed_scaling_factor.
  MoEGate.scoring_func: MoEGate#scoring_func.
  MoEGate.alpha: MoEGate#alpha.
  MoEGate.seq_aux: MoEGate#seq_aux.
  MoEGate.topk_method: MoEGate#topk_method.
  MoEGate.n_group: MoEGate#n_group.
  MoEGate.topk_group: MoEGate#topk_group.
  MoEGate.norm_topk_prob: MoEGate#norm_topk_prob.
  DeepseekV2MoE.num_experts_per_tok: DeepseekV2MoE#num_experts_per_tok.
  DeepseekV2MoE.experts_per_rank: DeepseekV2MoE#experts_per_rank.
  DeepseekV2Attention.__init__: DeepseekV2Attention#__init__().
  DeepseekV2Attention.qk_nope_head_dim: DeepseekV2Attention#qk_nope_head_dim.
  DeepseekV2Attention.qk_rope_head_dim: DeepseekV2Attention#qk_rope_head_dim.
  DeepseekV2Attention.head_dim: DeepseekV2Attention#head_dim.
  DeepseekV2DecoderLayer.__init__: DeepseekV2DecoderLayer#__init__().
  DeepseekV2Model.get_embedding: DeepseekV2Model#get_embedding().
  DeepseekV2ForCausalLM._config_class: DeepseekV2ForCausalLM#_config_class.
  DeepseekV2MLP: DeepseekV2MLP#
  DeepseekV2MoE.config: DeepseekV2MoE#config.
  DeepseekV2DecoderLayer.config: DeepseekV2DecoderLayer#config.
  DeepseekV2MLPMoE: DeepseekV2MLPMoE#
  DeepseekV2MLP.gate_proj: DeepseekV2MLP#gate_proj.
  DeepseekV2MLP.up_proj: DeepseekV2MLP#up_proj.
  DeepseekV2MLP.down_proj: DeepseekV2MLP#down_proj.
  MoEGate: MoEGate#
  MoEGate.config: MoEGate#config.
  MoEGate.param_dtype: MoEGate#param_dtype.
  MoEGate.precision: MoEGate#precision.
  DeepseekV2MoE._select_experts_static: DeepseekV2MoE#_select_experts_static().
  DeepseekV2DecoderLayer: DeepseekV2DecoderLayer#
  DeepseekV2MLPMoE.reform_param: DeepseekV2MLPMoE#reform_param.
  MoEGate.dtype: MoEGate#dtype.
  MoEGate.rngs: MoEGate#rngs.
  MoEGate.dp: MoEGate#dp.
  DeepseekV2MoE.dtype: DeepseekV2MoE#dtype.
  DeepseekV2MoE.param_dtype: DeepseekV2MoE#param_dtype.
  DeepseekV2MoE.precision: DeepseekV2MoE#precision.
  DeepseekV2MoE.rngs: DeepseekV2MoE#rngs.
  DeepseekV2DecoderLayer.dtype: DeepseekV2DecoderLayer#dtype.
  DeepseekV2DecoderLayer.param_dtype: DeepseekV2DecoderLayer#param_dtype.
  DeepseekV2DecoderLayer.precision: DeepseekV2DecoderLayer#precision.
  DeepseekV2DecoderLayer.rngs: DeepseekV2DecoderLayer#rngs.
  DeepseekV2DecoderLayer.layer_idx: DeepseekV2DecoderLayer#layer_idx.
  DeepseekV2Model.get_encoder: DeepseekV2Model#get_encoder().
  DeepseekV2Model.get_decoder: DeepseekV2Model#get_decoder().
  DeepseekV2Model.get_lm_head: DeepseekV2Model#get_lm_head().
  DeepseekV2ForCausalLM._model_type: DeepseekV2ForCausalLM#_model_type.
---
# Module: [`easydel/modules/deepseek_v2/modeling_deepseek.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py)

## Classes
### `DeepseekV2Attention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/deepseek_v2/modeling_deepseek.py:516`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L516)
- doc: Multi-head Latent Attention (MLA) layer for DeepSeek V2 models.
- signature: `class DeepseekV2Attention(UnifiedAttention):`
- members:
  - `__init__(self, config: DeepseekV2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L534`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L534) — Initialize DeepSeek V2 MLA attention layer.
  - `_create_attention_performer(self, config, rngs)` — [`L713`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L713) — Create attention performer module with custom softmax scale.
  - `define_network(self, config: DeepseekV2Config, dtype: jnp.dtype, param_dtype: jnp.dtype, precision: jax.lax.Precision, rngs: nn.Rngs)` — [`L576`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L576) — Define MLA-specific network structure. — documented in [easydel-layers-attention-_unified](../../../../concepts/easydel-layers-attention-_unified.md)
  - `config` — [`L555`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L555)
  - `head_dim` — [`L574`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L574)
  - `kv_lora_rank` — [`L560`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L560)
  - `projection_mapping` — [`L523`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L523)
  - `q_head_dim` — [`L556`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L556)
  - `qk_nope_head_dim` — [`L557`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L557)
  - `qk_rope_head_dim` — [`L558`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L558)
  - `rotary` — [`L710`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L710)
  - `v_head_dim` — [`L559`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L559)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`attention_performer`](../../layers/attention/_unified.md#UnifiedAttention.attention_performer), [`DeepseekV2Config`](deepseek_configuration.md#DeepseekV2Config), [`yarn_get_mscale`](../../layers/rotary/_utils.md#yarn_get_mscale), [`hidden_size`](deepseek_configuration.md#DeepseekV2Config.hidden_size), [`use_mla_lora`](../../layers/attention/_unified.md#UnifiedAttention.use_mla_lora), [`initializer_range`](deepseek_configuration.md#DeepseekV2Config.initializer_range), [`rope_scaling`](deepseek_configuration.md#DeepseekV2Config.rope_scaling), [`kv_lora_rank`](deepseek_configuration.md#DeepseekV2Config.kv_lora_rank), [`num_attention_heads`](deepseek_configuration.md#DeepseekV2Config.num_attention_heads), [`q_lora_rank`](deepseek_configuration.md#DeepseekV2Config.q_lora_rank), [`rms_norm_eps`](deepseek_configuration.md#DeepseekV2Config.rms_norm_eps), [`attention_bias`](deepseek_configuration.md#DeepseekV2Config.attention_bias), [`qk_nope_head_dim`](deepseek_configuration.md#DeepseekV2Config.qk_nope_head_dim), [`qk_rope_head_dim`](deepseek_configuration.md#DeepseekV2Config.qk_rope_head_dim), [`v_head_dim`](deepseek_configuration.md#DeepseekV2Config.v_head_dim)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_attention_performer`](../../layers/attention/_unified.md#UnifiedAttention._create_attention_performer), [`define_network`](../../layers/attention/_unified.md#UnifiedAttention.define_network), [`self_attn`](modeling_deepseek.md#DeepseekV2DecoderLayer.self_attn)

### `DeepseekV2DecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/deepseek_v2/modeling_deepseek.py:741`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L741)
- doc: Single decoder layer for DeepSeek V2 models.
- signature: `class DeepseekV2DecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Array, mask_info: MaskInfo, position_ids: Array, mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: tuple[Array, Array] | None = None)` — [`L826`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L826) — Forward pass through the decoder layer.
  - `__init__(self, config: DeepseekV2Config, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L748`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L748) — Initialize DeepSeek V2 decoder layer.
  - `config` — [`L770`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L770)
  - `dtype` — [`L771`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L771)
  - `hidden_size` — [`L776`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L776)
  - `input_layernorm` — [`L811`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L811)
  - `layer_idx` — [`L775`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L775)
  - `mlp` — [`L790`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L790)
  - `param_dtype` — [`L772`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L772)
  - `post_attention_layernorm` — [`L818`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L818)
  - `precision` — [`L773`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L773)
  - `rngs` — [`L774`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L774)
  - `self_attn` — [`L781`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L781)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`DeepseekV2Config`](deepseek_configuration.md#DeepseekV2Config), [`hidden_size`](deepseek_configuration.md#DeepseekV2Config.hidden_size), [`n_routed_experts`](deepseek_configuration.md#DeepseekV2Config.n_routed_experts), [`rms_norm_eps`](deepseek_configuration.md#DeepseekV2Config.rms_norm_eps), [`DeepseekV2Attention`](modeling_deepseek.md#DeepseekV2Attention), [`DeepseekV2MoE`](modeling_deepseek.md#DeepseekV2MoE), [`DeepseekV2MLP`](modeling_deepseek.md#DeepseekV2MLP), [`first_k_dense_replace`](deepseek_configuration.md#DeepseekV2Config.first_k_dense_replace), [`moe_layer_freq`](deepseek_configuration.md#DeepseekV2Config.moe_layer_freq)
- used by: [`embed_tokens`](modeling_deepseek.md#DeepseekV2Model.embed_tokens)

### `DeepseekV2ForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/deepseek_v2/modeling_deepseek.py:1151`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L1151)
- doc: DeepSeek V2 model with a language modeling head for causal language modeling tasks.
- signature: `class DeepseekV2ForCausalLM(BaseCausalLMModule[DeepseekV2Model, DeepseekV2Config]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None)` — [`L1198`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L1198) — Forward pass of the causal language model.
  - `__init__(self, config: DeepseekV2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1168`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L1168) — Initialize DeepSeek V2 model for causal language modeling.
  - `_compute_aux_loss(self, outputs, attention_mask)` — [`L1264`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L1264) — Compute auxiliary loss for MoE load balancing.
  - `create_ragged_page_cache_config(self, max_length: int, *, page_size: int = 128, hbm_utilization: float = 0.9, dtype: jnp.dtype | None = None)` — [`L1320`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L1320) — Create paged cache configuration for MLA attention.
  - `create_transformer_cache_config(self, batch_size: int, max_length: int, **kwargs)` — [`L1287`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L1287) — Create cache configuration for MLA attention.
- protocol/private: `_config_class`[`L1166`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L1166), `_model_type`[`L1165`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L1165), `_task_type`[`L1164`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L1164)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`RaggedPagesCacheConfig`](../../caching/ragged_page/cache.md#RaggedPagesCacheConfig), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`mesh`](../../infra/base_module.md#EasyDeLBaseModule.mesh), [`MoeCausalLMOutput`](../../infra/modeling_outputs.md#MoeCausalLMOutput), [`AttentionMechanisms`](../../layers/attention/_flexible.md#AttentionMechanisms), [`create`](../../caching/ragged_page/cache.md#RaggedPagesCacheConfig.create), [`auxiliary_load_balancing_loss_func`](../../infra/loss_utils.md#auxiliary_load_balancing_loss_func), [`forward_moe`](../_base/causal_lm_module.md#BaseCausalLMModule.forward_moe), [`create`](../../caching/mla_ragged_page/cache.md#MLARaggedPagesCacheConfig.create), [`MLARaggedPagesCacheConfig`](../../caching/mla_ragged_page/cache.md#MLARaggedPagesCacheConfig), [`DeepseekV2Config`](deepseek_configuration.md#DeepseekV2Config), [`TransformerCacheConfig`](../../caching/transformer/cache.md#TransformerCacheConfig), [`DeepseekV2Model`](modeling_deepseek.md#DeepseekV2Model), [`create`](../../caching/transformer/cache.md#TransformerCacheConfig.create), [`RAGGED_PAGE_ATTENTION_V3`](../../layers/attention/_flexible.md#AttentionMechanisms.RAGGED_PAGE_ATTENTION_V3), [`RAGGED_PAGE_ATTENTION_V2`](../../layers/attention/_flexible.md#AttentionMechanisms.RAGGED_PAGE_ATTENTION_V2)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`create_ragged_page_cache_config`](../../infra/mixins/generation.md#EasyGenerationMixin.create_ragged_page_cache_config), [`create_transformer_cache_config`](../../infra/mixins/generation.md#EasyGenerationMixin.create_transformer_cache_config)

### `DeepseekV2MLP`  ·  implements/extends Module
- def: [`easydel/modules/deepseek_v2/modeling_deepseek.py:197`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L197)
- doc: Multi-Layer Perceptron module for DeepSeek V2 dense layers.
- signature: `class DeepseekV2MLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L244`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L244) — Apply SwiGLU feedforward transformation.
  - `__init__(self, config: DeepseekV2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, hidden_size: int | None = None, intermediate_size: int | None = None, *, rngs: nn.Rngs)` — [`L204`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L204) — Initialize DeepSeek V2 MLP block.
  - `act_fn` — [`L242`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L242)
  - `config` — [`L228`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L228)
  - `down_proj` — [`L241`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L241)
  - `gate_proj` — [`L239`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L239)
  - `up_proj` — [`L240`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L240)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`DeepseekV2Config`](deepseek_configuration.md#DeepseekV2Config), [`hidden_size`](deepseek_configuration.md#DeepseekV2Config.hidden_size), [`hidden_act`](deepseek_configuration.md#DeepseekV2Config.hidden_act), [`intermediate_size`](deepseek_configuration.md#DeepseekV2Config.intermediate_size)
- used by: [`shared_experts`](modeling_deepseek.md#DeepseekV2MoE.shared_experts), [`hidden_size`](modeling_deepseek.md#DeepseekV2DecoderLayer.hidden_size)

### `DeepseekV2MLPMoE`  ·  implements/extends Module
- def: [`easydel/modules/deepseek_v2/modeling_deepseek.py:69`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L69)
- doc: Mixture-of-experts feed-forward module for DeepSeek V2 MoE layers.
- signature: `class DeepseekV2MLPMoE(nn.Module):`
- members:
  - `__call__(self, hidden_states: Array, group_sizes: Array, sorted_experts: Array | None = None)` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L158) — Apply SwiGLU feedforward transformation through MoE experts.
  - `__init__(self, config: DeepseekV2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, hidden_size: int | None = None, intermediate_size: int | None = None, *, rngs: nn.Rngs)` — [`L92`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L92) — Initialize DeepSeek V2 MoE MLP block.
  - `act_fn` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L156)
  - `config` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L116)
  - `down_proj` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L144)
  - `gate_proj` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L120)
  - `reform_param` — [`L76`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L76)
  - `up_proj` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L132)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`use_expert_tensor_mode`](../../infra/base_config.md#EasyDeLBaseConfig.use_expert_tensor_mode), [`ColumnParallelMoELinear`](../../layers/linears/_linear_moe.md#ColumnParallelMoELinear), [`RowParallelMoELinear`](../../layers/linears/_linear_moe.md#RowParallelMoELinear), [`DeepseekV2Config`](deepseek_configuration.md#DeepseekV2Config), [`hidden_size`](deepseek_configuration.md#DeepseekV2Config.hidden_size), [`n_routed_experts`](deepseek_configuration.md#DeepseekV2Config.n_routed_experts), [`hidden_act`](deepseek_configuration.md#DeepseekV2Config.hidden_act), [`intermediate_size`](deepseek_configuration.md#DeepseekV2Config.intermediate_size)
- used by: [`__call__`](modeling_deepseek.md#DeepseekV2MoE.__call__), [`experts`](modeling_deepseek.md#DeepseekV2MoE.experts)

### `DeepseekV2MoE`  ·  implements/extends BaseMoeModule
- def: [`easydel/modules/deepseek_v2/modeling_deepseek.py:370`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L370)
- doc: Mixture-of-experts module combining gating and expert networks for DeepSeek V2.
- signature: `class DeepseekV2MoE(BaseMoeModule):`
- members:
  - `__call__(self, hidden_states: Array)` — [`L491`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L491) — Process tokens through MoE experts with routing.
  - `__init__(self, config: DeepseekV2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L377`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L377) — Initialize DeepSeek V2 MoE layer.
  - `config` — [`L406`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L406)
  - `dtype` — [`L407`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L407)
  - `experts` — [`L413`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L413)
  - `experts_per_rank` — [`L412`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L412)
  - `gate` — [`L421`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L421)
  - `num_experts_per_tok` — [`L411`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L411)
  - `param_dtype` — [`L408`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L408)
  - `precision` — [`L409`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L409)
  - `rngs` — [`L410`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L410)
  - `shared_experts` — [`L430`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L430)
- protocol/private: `_select_experts_static`[`L452`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L452)
- uses (calls/refs, reference-scoped): [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`kernel`](../../layers/linears/_linear_moe.md#ParallelMoELinear.kernel), [`MoeRoutingStrategy`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy), [`moe_call`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_call), [`MoeLoadBalancingStrategy`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy), [`__init__`](../../layers/moe/_moe_module.md#BaseMoeModule.__init__), [`moe_hooks`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_hooks), [`DeepseekV2Config`](deepseek_configuration.md#DeepseekV2Config), [`TOP_K`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy.TOP_K), [`STANDARD`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy.STANDARD), [`down_proj`](modeling_deepseek.md#DeepseekV2MLPMoE.down_proj), [`gate_proj`](modeling_deepseek.md#DeepseekV2MLPMoE.gate_proj), [`up_proj`](modeling_deepseek.md#DeepseekV2MLPMoE.up_proj), [`hidden_size`](deepseek_configuration.md#DeepseekV2Config.hidden_size), [`replace`](../../layers/moe/_communication_utils.md#MoeFusedHooks.replace), [`n_routed_experts`](deepseek_configuration.md#DeepseekV2Config.n_routed_experts), [`act_fn`](modeling_deepseek.md#DeepseekV2MLPMoE.act_fn), [`n_shared_experts`](deepseek_configuration.md#DeepseekV2Config.n_shared_experts), [`num_experts_per_tok`](deepseek_configuration.md#DeepseekV2Config.num_experts_per_tok), [`DeepseekV2MLP`](modeling_deepseek.md#DeepseekV2MLP), [`moe_intermediate_size`](deepseek_configuration.md#DeepseekV2Config.moe_intermediate_size), [`n_group`](deepseek_configuration.md#DeepseekV2Config.n_group), [`norm_topk_prob`](deepseek_configuration.md#DeepseekV2Config.norm_topk_prob), [`routed_scaling_factor`](deepseek_configuration.md#DeepseekV2Config.routed_scaling_factor), [`topk_group`](deepseek_configuration.md#DeepseekV2Config.topk_group), [`topk_method`](deepseek_configuration.md#DeepseekV2Config.topk_method), [`DeepseekV2MLPMoE`](modeling_deepseek.md#DeepseekV2MLPMoE), [`MoEGate`](modeling_deepseek.md#MoEGate)
- used by: [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`hidden_size`](modeling_deepseek.md#DeepseekV2DecoderLayer.hidden_size)

### `DeepseekV2Model`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/deepseek_v2/modeling_deepseek.py:904`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L904)
- doc: DeepSeek V2 base model implementation.
- signature: `class DeepseekV2Model(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None)` — [`L995`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L995) — Forward pass through the DeepSeek V2 base model.
  - `__init__(self, config: DeepseekV2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L917`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L917) — Initialize DeepSeek V2 base model.
  - `frequencies(self)` — [`L980`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L980) — Compute RoPE frequencies for rotary position embeddings.
  - `get_decoder(self)` — [`L1129`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L1129) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L1143`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L1143) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L1122`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L1122) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L1136`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L1136) — Returns the language model head of the module.
  - `embed_tokens` — [`L943`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L943)
  - `layers` — [`L958`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L958)
  - `norm` — [`L971`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L971)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`MoeModelOutput`](../../infra/modeling_outputs.md#MoeModelOutput), [`get_basic_frequencies`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_frequencies), [`DeepseekV2Config`](deepseek_configuration.md#DeepseekV2Config), [`DeepseekV2DecoderLayer`](modeling_deepseek.md#DeepseekV2DecoderLayer), [`gradient_checkpointing`](deepseek_configuration.md#DeepseekV2Config.gradient_checkpointing)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`DeepseekV2ForCausalLM`](modeling_deepseek.md#DeepseekV2ForCausalLM), [`__init__`](modeling_deepseek.md#DeepseekV2ForCausalLM.__init__)

### `MoEGate`  ·  implements/extends Module
- def: [`easydel/modules/deepseek_v2/modeling_deepseek.py:273`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L273)
- doc: Router module that scores tokens and selects experts for DeepSeek V2 MoE.
- signature: `class MoEGate(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L341`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L341) — Compute pre-softmax router logits for input tokens.
  - `__init__(self, config: DeepseekV2Config, layer_idx: int | None = None, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L280`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L280) — Initialize MoE gating module.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L328`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L328) — Return sharding specifications for MoEGate parameters.
  - `alpha` — [`L312`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L312)
  - `config` — [`L303`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L303)
  - `dp` — [`L326`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L326)
  - `dtype` — [`L304`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L304)
  - `gating_dim` — [`L319`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L319)
  - `kernel` — [`L320`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L320)
  - `n_group` — [`L315`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L315)
  - `n_routed_experts` — [`L309`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L309)
  - `norm_topk_prob` — [`L318`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L318)
  - `param_dtype` — [`L305`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L305)
  - `precision` — [`L306`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L306)
  - `rngs` — [`L307`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L307)
  - `routed_scaling_factor` — [`L310`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L310)
  - `scoring_func` — [`L311`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L311)
  - `seq_aux` — [`L313`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L313)
  - `top_k` — [`L308`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L308)
  - `topk_group` — [`L316`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L316)
  - `topk_method` — [`L314`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/modeling_deepseek.py#L314)
- uses (calls/refs, reference-scoped): [`ArrayParam`](../../infra/utils.md#ArrayParam), [`bound`](../../infra/utils.md#ArrayParam.bound), [`use_expert_tensor_mode`](../../infra/base_config.md#EasyDeLBaseConfig.use_expert_tensor_mode), [`DeepseekV2Config`](deepseek_configuration.md#DeepseekV2Config), [`hidden_size`](deepseek_configuration.md#DeepseekV2Config.hidden_size), [`n_routed_experts`](deepseek_configuration.md#DeepseekV2Config.n_routed_experts), [`num_experts_per_tok`](deepseek_configuration.md#DeepseekV2Config.num_experts_per_tok), [`n_group`](deepseek_configuration.md#DeepseekV2Config.n_group), [`norm_topk_prob`](deepseek_configuration.md#DeepseekV2Config.norm_topk_prob), [`routed_scaling_factor`](deepseek_configuration.md#DeepseekV2Config.routed_scaling_factor), [`topk_group`](deepseek_configuration.md#DeepseekV2Config.topk_group), [`topk_method`](deepseek_configuration.md#DeepseekV2Config.topk_method), [`aux_loss_alpha`](deepseek_configuration.md#DeepseekV2Config.aux_loss_alpha), [`scoring_func`](deepseek_configuration.md#DeepseekV2Config.scoring_func), [`seq_aux`](deepseek_configuration.md#DeepseekV2Config.seq_aux)
- used by: [`gate`](modeling_deepseek.md#DeepseekV2MoE.gate)

