---
title: 'Module: easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py'
type: catalog
provenance: extracted
module: easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.glm4_moe_lite.modeling_glm4_moe_lite`/
symbols:
  Glm4MoeLiteAttention.forward_mla: Glm4MoeLiteAttention#forward_mla().
  Glm4MoeLiteModel.__call__: Glm4MoeLiteModel#__call__().
  Glm4MoeLiteAttention.define_network: Glm4MoeLiteAttention#define_network().
  Glm4MoeLiteDecoderLayer.__call__: Glm4MoeLiteDecoderLayer#__call__().
  Glm4MoeLiteMoE.shared_experts: Glm4MoeLiteMoE#shared_experts.
  Glm4MoeLiteModel.embed_tokens: Glm4MoeLiteModel#embed_tokens.
  Glm4MoeLiteMoE.__init__: Glm4MoeLiteMoE#__init__().
  Glm4MoeLiteMoE.__call__: Glm4MoeLiteMoE#__call__().
  Glm4MoeLiteForCausalLM.create_ragged_page_cache_config: Glm4MoeLiteForCausalLM#create_ragged_page_cache_config().
  Glm4MoeLiteAttention.qk_nope_head_dim: Glm4MoeLiteAttention#qk_nope_head_dim.
  Glm4MoeLiteModel.__init__: Glm4MoeLiteModel#__init__().
  Glm4MoeLiteMLPStack.gate_proj: Glm4MoeLiteMLPStack#gate_proj.
  Glm4MoeLiteMLPStack.up_proj: Glm4MoeLiteMLPStack#up_proj.
  Glm4MoeLiteMLPStack.down_proj: Glm4MoeLiteMLPStack#down_proj.
  Glm4MoeLiteForCausalLM: Glm4MoeLiteForCausalLM#
  Glm4MoeLiteModel: Glm4MoeLiteModel#
  Glm4MoeLiteMLP.__call__: Glm4MoeLiteMLP#__call__().
  Glm4MoeLiteMLPStack.__call__: Glm4MoeLiteMLPStack#__call__().
  Glm4MoeLiteMLP.intermediate_size: Glm4MoeLiteMLP#intermediate_size.
  Glm4MoeLiteAttention.q_head_dim: Glm4MoeLiteAttention#q_head_dim.
  Glm4MoeLiteAttention._create_attention_performer: Glm4MoeLiteAttention#_create_attention_performer().
  Glm4MoeLiteDecoderLayer.self_attn: Glm4MoeLiteDecoderLayer#self_attn.
  Glm4MoeLiteModel.norm: Glm4MoeLiteModel#norm.
  Glm4MoeLiteForCausalLM._create_mla_ragged_page_cache_config: Glm4MoeLiteForCausalLM#_create_mla_ragged_page_cache_config().
  Glm4MoeLiteAttention.kv_lora_rank: Glm4MoeLiteAttention#kv_lora_rank.
  Glm4MoeLiteAttention.v_head_dim: Glm4MoeLiteAttention#v_head_dim.
  Glm4MoeLiteTopKRouter.kernel: Glm4MoeLiteTopKRouter#kernel.
  Glm4MoeLiteDecoderLayer.input_layernorm: Glm4MoeLiteDecoderLayer#input_layernorm.
  Glm4MoeLiteDecoderLayer.post_attention_layernorm: Glm4MoeLiteDecoderLayer#post_attention_layernorm.
  Glm4MoeLiteAttention.projection_mapping: Glm4MoeLiteAttention#projection_mapping.
  Glm4MoeLiteTopKRouter.__call__: Glm4MoeLiteTopKRouter#__call__().
  Glm4MoeLiteMoE.experts: Glm4MoeLiteMoE#experts.
  Glm4MoeLiteAttention.rotary: Glm4MoeLiteAttention#rotary.
  Glm4MoeLiteForCausalLM.__init__: Glm4MoeLiteForCausalLM#__init__().
  Glm4MoeLiteMLPStack.act_fn: Glm4MoeLiteMLPStack#act_fn.
  Glm4MoeLiteDecoderLayer.mlp: Glm4MoeLiteDecoderLayer#mlp.
  Glm4MoeLiteModel.layers: Glm4MoeLiteModel#layers.
  Glm4MoeLiteMLP.gate_proj: Glm4MoeLiteMLP#gate_proj.
  Glm4MoeLiteMLP.up_proj: Glm4MoeLiteMLP#up_proj.
  Glm4MoeLiteMLP.down_proj: Glm4MoeLiteMLP#down_proj.
  Glm4MoeLiteMLP.act_fn: Glm4MoeLiteMLP#act_fn.
  Glm4MoeLiteMoE.group_topk_k: Glm4MoeLiteMoE#group_topk_k.
  Glm4MoeLiteModel.frequencies: Glm4MoeLiteModel#frequencies().
  Glm4MoeLiteMLP.hidden_size: Glm4MoeLiteMLP#hidden_size.
  Glm4MoeLiteTopKRouter.craft_sharding: Glm4MoeLiteTopKRouter#craft_sharding().
  Glm4MoeLiteDecoderLayer.hidden_size: Glm4MoeLiteDecoderLayer#hidden_size.
  Glm4MoeLiteForCausalLM._task_type: Glm4MoeLiteForCausalLM#_task_type.
  Glm4MoeLiteTopKRouter.n_routed_experts: Glm4MoeLiteTopKRouter#n_routed_experts.
  Glm4MoeLiteAttention.qk_rope_head_dim: Glm4MoeLiteAttention#qk_rope_head_dim.
  Glm4MoeLiteMoE: Glm4MoeLiteMoE#
  Glm4MoeLiteMoE.n_group: Glm4MoeLiteMoE#n_group.
  Glm4MoeLiteMoE.topk_group: Glm4MoeLiteMoE#topk_group.
  Glm4MoeLiteMoE.norm_topk_prob: Glm4MoeLiteMoE#norm_topk_prob.
  Glm4MoeLiteMoE.routed_scaling_factor: Glm4MoeLiteMoE#routed_scaling_factor.
  Glm4MoeLiteMoE.gate: Glm4MoeLiteMoE#gate.
  Glm4MoeLiteAttention: Glm4MoeLiteAttention#
  Glm4MoeLiteMLP.__init__: Glm4MoeLiteMLP#__init__().
  Glm4MoeLiteMLPStack.__init__: Glm4MoeLiteMLPStack#__init__().
  Glm4MoeLiteTopKRouter.__init__: Glm4MoeLiteTopKRouter#__init__().
  Glm4MoeLiteTopKRouter.e_score_correction_bias: Glm4MoeLiteTopKRouter#e_score_correction_bias.
  Glm4MoeLiteAttention.__init__: Glm4MoeLiteAttention#__init__().
  Glm4MoeLiteAttention.head_dim: Glm4MoeLiteAttention#head_dim.
  Glm4MoeLiteDecoderLayer.__init__: Glm4MoeLiteDecoderLayer#__init__().
  Glm4MoeLiteForCausalLM._config_class: Glm4MoeLiteForCausalLM#_config_class.
  Glm4MoeLiteMLP: Glm4MoeLiteMLP#
  Glm4MoeLiteMLP.config: Glm4MoeLiteMLP#config.
  Glm4MoeLiteMLPStack.config: Glm4MoeLiteMLPStack#config.
  Glm4MoeLiteTopKRouter.config: Glm4MoeLiteTopKRouter#config.
  Glm4MoeLiteAttention.config: Glm4MoeLiteAttention#config.
  Glm4MoeLiteAttention._apply_rope_interleaved: Glm4MoeLiteAttention#_apply_rope_interleaved().
  Glm4MoeLiteDecoderLayer.config: Glm4MoeLiteDecoderLayer#config.
  Glm4MoeLiteMLPStack: Glm4MoeLiteMLPStack#
  Glm4MoeLiteTopKRouter: Glm4MoeLiteTopKRouter#
  Glm4MoeLiteMoE._select_experts_static: Glm4MoeLiteMoE#_select_experts_static().
  Glm4MoeLiteDecoderLayer: Glm4MoeLiteDecoderLayer#
  Glm4MoeLiteMLP.dtype: Glm4MoeLiteMLP#dtype.
  Glm4MoeLiteMLP.param_dtype: Glm4MoeLiteMLP#param_dtype.
  Glm4MoeLiteMLP.precision: Glm4MoeLiteMLP#precision.
  Glm4MoeLiteMLPStack.reform_param: Glm4MoeLiteMLPStack#reform_param.
  Glm4MoeLiteMLPStack.dtype: Glm4MoeLiteMLPStack#dtype.
  Glm4MoeLiteMLPStack.param_dtype: Glm4MoeLiteMLPStack#param_dtype.
  Glm4MoeLiteMLPStack.precision: Glm4MoeLiteMLPStack#precision.
  Glm4MoeLiteTopKRouter.dtype: Glm4MoeLiteTopKRouter#dtype.
  Glm4MoeLiteTopKRouter.param_dtype: Glm4MoeLiteTopKRouter#param_dtype.
  Glm4MoeLiteTopKRouter.precision: Glm4MoeLiteTopKRouter#precision.
  Glm4MoeLiteMoE.config: Glm4MoeLiteMoE#config.
  Glm4MoeLiteMoE.dtype: Glm4MoeLiteMoE#dtype.
  Glm4MoeLiteMoE.param_dtype: Glm4MoeLiteMoE#param_dtype.
  Glm4MoeLiteMoE.precision: Glm4MoeLiteMoE#precision.
  Glm4MoeLiteDecoderLayer.dtype: Glm4MoeLiteDecoderLayer#dtype.
  Glm4MoeLiteDecoderLayer.param_dtype: Glm4MoeLiteDecoderLayer#param_dtype.
  Glm4MoeLiteDecoderLayer.precision: Glm4MoeLiteDecoderLayer#precision.
  Glm4MoeLiteDecoderLayer.rngs: Glm4MoeLiteDecoderLayer#rngs.
  Glm4MoeLiteDecoderLayer.layer_idx: Glm4MoeLiteDecoderLayer#layer_idx.
  Glm4MoeLiteForCausalLM._model_type: Glm4MoeLiteForCausalLM#_model_type.
  __all__: __all__.
---
# Module: [`easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py)

## Classes
### `Glm4MoeLiteAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py:405`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L405)
- doc: Multi-head Latent Attention (MLA) for GLM-4-MoE-Lite.
- signature: `class Glm4MoeLiteAttention(UnifiedAttention):`
- members:
  - `define_network(self, config: Glm4MoeLiteConfig, dtype: jnp.dtype, param_dtype: jnp.dtype, precision: jax.lax.Precision, rngs: nn.Rngs)` — [`L455`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L455)
  - `forward_mla(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None, alibi: Float[Array, "batch_or_1 heads qseq_len_or_1 kvseq_len_or_1"] | None = None)` — [`L600`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L600)
  - `config` — [`L435`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L435)
  - `head_dim` — [`L453`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L453)
  - `kv_lora_rank` — [`L440`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L440)
  - `projection_mapping` — [`L414`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L414)
  - `q_head_dim` — [`L436`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L436)
  - `qk_nope_head_dim` — [`L437`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L437)
  - `qk_rope_head_dim` — [`L438`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L438)
  - `rotary` — [`L573`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L573)
  - `v_head_dim` — [`L439`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L439)
- protocol/private: `__init__`[`L425`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L425), `_apply_rope_interleaved`[`L593`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L593), `_create_attention_performer`[`L576`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L576)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`forward`](../../layers/attention/_flexible.md#FlexibleAttentionModule.forward), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`AttentionLayerOutput`](../../infra/modeling_outputs.md#AttentionLayerOutput), [`concatenate`](../../layers/attention/_flexible.md#AttentionModule.concatenate), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`attention_outputs`](../../operations/_attention_outputs.md#AttentionOutput.attention_outputs), [`attention_performer`](../../layers/attention/_unified.md#UnifiedAttention.attention_performer), [`num_heads`](../../layers/attention/_unified.md#UnifiedAttention.num_heads), [`MLARaggedPagesCacheView`](../../caching/mla_ragged_page/cache.md#MLARaggedPagesCacheView), [`shard_attention_prod`](../../layers/attention/_flexible.md#AttentionModule.shard_attention_prod), [`_merge_heads`](../../layers/attention/_unified.md#UnifiedAttention._merge_heads), [`Glm4MoeLiteConfig`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig), [`attention_weights`](../../operations/_attention_outputs.md#AttentionOutput.attention_weights), [`kernel`](../../layers/linears/_linear.md#ParallelLinear.kernel), [`hidden_size`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.hidden_size), [`output_projection`](../../layers/attention/_unified.md#UnifiedAttention.output_projection), [`sliding_window`](../../layers/attention/_unified.md#UnifiedAttention.sliding_window), [`yarn_get_mscale`](../../layers/rotary/_utils.md#yarn_get_mscale), [`mla_kv_b_proj`](../../layers/attention/_unified.md#UnifiedAttention.mla_kv_b_proj), [`initializer_range`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.initializer_range), [`mla_kv_a_layernorm`](../../layers/attention/_unified.md#UnifiedAttention.mla_kv_a_layernorm), [`causal`](../../layers/attention/_unified.md#UnifiedAttention.causal), [`use_mla_lora`](../../layers/attention/_unified.md#UnifiedAttention.use_mla_lora), [`mla_kv_a_proj_with_mqa`](../../layers/attention/_unified.md#UnifiedAttention.mla_kv_a_proj_with_mqa), [`mla_q_a_layernorm`](../../layers/attention/_unified.md#UnifiedAttention.mla_q_a_layernorm), [`mla_q_a_proj`](../../layers/attention/_unified.md#UnifiedAttention.mla_q_a_proj), [`mla_q_b_proj`](../../layers/attention/_unified.md#UnifiedAttention.mla_q_b_proj), [`mla_q_proj`](../../layers/attention/_unified.md#UnifiedAttention.mla_q_proj), [`q_lora_rank`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.q_lora_rank), [`rms_norm_eps`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.rms_norm_eps)  (+7 more)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_attention_performer`](../../layers/attention/_unified.md#UnifiedAttention._create_attention_performer), [`forward_mla`](../../layers/attention/_unified.md#UnifiedAttention.forward_mla), [`define_network`](../../layers/attention/_unified.md#UnifiedAttention.define_network), [`self_attn`](modeling_glm4_moe_lite.md#Glm4MoeLiteDecoderLayer.self_attn)

### `Glm4MoeLiteDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py:781`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L781)
- doc: Single decoder layer for GLM-4-MoE-Lite.
- signature: `class Glm4MoeLiteDecoderLayer(nn.Module):`
- members:
  - `config` — [`L800`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L800)
  - `dtype` — [`L801`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L801)
  - `hidden_size` — [`L806`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L806)
  - `input_layernorm` — [`L841`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L841)
  - `layer_idx` — [`L805`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L805)
  - `mlp` — [`L825`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L825)
  - `param_dtype` — [`L802`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L802)
  - `post_attention_layernorm` — [`L848`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L848)
  - `precision` — [`L803`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L803)
  - `rngs` — [`L804`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L804)
  - `self_attn` — [`L810`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L810)
- protocol/private: `__call__`[`L856`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L856), `__init__`[`L790`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L790)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`Glm4MoeLiteConfig`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig), [`hidden_size`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.hidden_size), [`mlp_layer_types`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.mlp_layer_types), [`n_routed_experts`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.n_routed_experts), [`rms_norm_eps`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.rms_norm_eps), [`Glm4MoeLiteAttention`](modeling_glm4_moe_lite.md#Glm4MoeLiteAttention), [`Glm4MoeLiteMoE`](modeling_glm4_moe_lite.md#Glm4MoeLiteMoE), [`Glm4MoeLiteMLP`](modeling_glm4_moe_lite.md#Glm4MoeLiteMLP), [`num_experts_per_tok`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.num_experts_per_tok)
- used by: [`embed_tokens`](modeling_glm4_moe_lite.md#Glm4MoeLiteModel.embed_tokens)

### `Glm4MoeLiteForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py:1081`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L1081)
- doc: GLM-4-MoE-Lite model with a language modeling head for causal language modeling.
- signature: `class Glm4MoeLiteForCausalLM(BaseCausalLMModule[Glm4MoeLiteModel, Glm4MoeLiteConfig]):`
- members:
  - `_create_mla_ragged_page_cache_config(self, max_length: int, *, page_size: int = 128, hbm_utilization: float = 0.9, dtype: jnp.dtype | None = None, num_hidden_layers_override: int | None = None)` — [`L1173`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L1173) — Create the MLA ragged cache using GLM4-MoE-Lite's compressed KV width.
  - `create_ragged_page_cache_config(self, max_length: int, *, page_size: int = 128, hbm_utilization: float = 0.9, dtype: jnp.dtype | None = None)` — [`L1114`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L1114) — Create paged cache configuration for MLA attention.
- protocol/private: `__init__`[`L1093`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L1093), `_config_class`[`L1091`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L1091), `_model_type`[`L1090`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L1090), `_task_type`[`L1089`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L1089)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`RaggedPagesCacheConfig`](../../caching/ragged_page/cache.md#RaggedPagesCacheConfig), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`mesh`](../../infra/base_module.md#EasyDeLBaseModule.mesh), [`AttentionMechanisms`](../../layers/attention/_flexible.md#AttentionMechanisms), [`create`](../../caching/ragged_page/cache.md#RaggedPagesCacheConfig.create), [`create`](../../caching/mla_ragged_page/cache.md#MLARaggedPagesCacheConfig.create), [`MLARaggedPagesCacheConfig`](../../caching/mla_ragged_page/cache.md#MLARaggedPagesCacheConfig), [`Glm4MoeLiteConfig`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig), [`Glm4MoeLiteModel`](modeling_glm4_moe_lite.md#Glm4MoeLiteModel), [`RAGGED_PAGE_ATTENTION_V3`](../../layers/attention/_flexible.md#AttentionMechanisms.RAGGED_PAGE_ATTENTION_V3), [`RAGGED_PAGE_ATTENTION_V2`](../../layers/attention/_flexible.md#AttentionMechanisms.RAGGED_PAGE_ATTENTION_V2)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`create_ragged_page_cache_config`](../../infra/mixins/generation.md#EasyGenerationMixin.create_ragged_page_cache_config), [`_create_mla_ragged_page_cache_config`](../../infra/mixins/generation.md#EasyGenerationMixin._create_mla_ragged_page_cache_config)

### `Glm4MoeLiteMLP`  ·  implements/extends Module
- def: [`easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py:64`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L64)
- doc: Dense MLP block for GLM-4-MoE-Lite layers.
- signature: `class Glm4MoeLiteMLP(nn.Module):`
- members:
  - `act_fn` — [`L110`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L110)
  - `config` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L83)
  - `down_proj` — [`L109`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L109)
  - `dtype` — [`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L84)
  - `gate_proj` — [`L107`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L107)
  - `hidden_size` — [`L87`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L87)
  - `intermediate_size` — [`L88`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L88)
  - `param_dtype` — [`L85`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L85)
  - `precision` — [`L86`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L86)
  - `up_proj` — [`L108`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L108)
- protocol/private: `__call__`[`L112`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L112), `__init__`[`L72`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L72)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`Glm4MoeLiteConfig`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig), [`hidden_size`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.hidden_size), [`initializer_range`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.initializer_range), [`hidden_act`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.hidden_act), [`intermediate_size`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.intermediate_size)
- used by: [`shared_experts`](modeling_glm4_moe_lite.md#Glm4MoeLiteMoE.shared_experts), [`mlp`](modeling_glm4_moe_lite.md#Glm4MoeLiteDecoderLayer.mlp)

### `Glm4MoeLiteMLPStack`  ·  implements/extends Module
- def: [`easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py:129`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L129)
- doc: Expert MLP stack for GLM-4-MoE-Lite using parallel MoE linear layers.
- signature: `class Glm4MoeLiteMLPStack(nn.Module):`
- members:
  - `act_fn` — [`L205`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L205)
  - `config` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L165)
  - `down_proj` — [`L193`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L193)
  - `dtype` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L166)
  - `gate_proj` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L169)
  - `param_dtype` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L167)
  - `precision` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L168)
  - `reform_param` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L137)
  - `up_proj` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L181)
- protocol/private: `__call__`[`L207`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L207), `__init__`[`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L156)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`use_expert_tensor_mode`](../../infra/base_config.md#EasyDeLBaseConfig.use_expert_tensor_mode), [`ColumnParallelMoELinear`](../../layers/linears/_linear_moe.md#ColumnParallelMoELinear), [`RowParallelMoELinear`](../../layers/linears/_linear_moe.md#RowParallelMoELinear), [`Glm4MoeLiteConfig`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig), [`hidden_size`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.hidden_size), [`n_routed_experts`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.n_routed_experts), [`moe_intermediate_size`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.moe_intermediate_size), [`hidden_act`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.hidden_act)
- used by: [`__call__`](modeling_glm4_moe_lite.md#Glm4MoeLiteMoE.__call__), [`experts`](modeling_glm4_moe_lite.md#Glm4MoeLiteMoE.experts)

### `Glm4MoeLiteMoE`  ·  implements/extends BaseMoeModule
- def: [`easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py:278`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L278)
- doc: Mixture-of-Experts feed-forward module for GLM-4-MoE-Lite.
- signature: `class Glm4MoeLiteMoE(BaseMoeModule):`
- members:
  - `config` — [`L306`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L306)
  - `dtype` — [`L307`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L307)
  - `experts` — [`L316`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L316)
  - `gate` — [`L323`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L323)
  - `group_topk_k` — [`L314`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L314)
  - `n_group` — [`L310`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L310)
  - `norm_topk_prob` — [`L312`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L312)
  - `param_dtype` — [`L308`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L308)
  - `precision` — [`L309`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L309)
  - `routed_scaling_factor` — [`L313`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L313)
  - `shared_experts` — [`L330`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L330)
  - `topk_group` — [`L311`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L311)
- protocol/private: `__call__`[`L390`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L390), `__init__`[`L287`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L287), `_select_experts_static`[`L356`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L356)
- uses (calls/refs, reference-scoped): [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`kernel`](../../layers/linears/_linear_moe.md#ParallelMoELinear.kernel), [`MoeRoutingStrategy`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy), [`moe_call`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_call), [`MoeLoadBalancingStrategy`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy), [`__init__`](../../layers/moe/_moe_module.md#BaseMoeModule.__init__), [`moe_hooks`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_hooks), [`n_routed_experts`](../../layers/moe/_moe_module.md#BaseMoeModule.n_routed_experts), [`Glm4MoeLiteConfig`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig), [`TOP_K`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy.TOP_K), [`STANDARD`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy.STANDARD), [`down_proj`](modeling_glm4_moe_lite.md#Glm4MoeLiteMLPStack.down_proj), [`gate_proj`](modeling_glm4_moe_lite.md#Glm4MoeLiteMLPStack.gate_proj), [`up_proj`](modeling_glm4_moe_lite.md#Glm4MoeLiteMLPStack.up_proj), [`MoeFusedHooks`](../../layers/moe/_communication_utils.md#MoeFusedHooks), [`hidden_size`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.hidden_size), [`select_hook`](../../layers/moe/_communication_utils.md#MoeFusedHooks.select_hook), [`act_fn`](modeling_glm4_moe_lite.md#Glm4MoeLiteMLPStack.act_fn), [`n_routed_experts`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.n_routed_experts), [`normalize_gate_logits`](../../layers/moe/_communication_utils.md#MoeFusedHooks.normalize_gate_logits), [`moe_intermediate_size`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.moe_intermediate_size), [`Glm4MoeLiteMLP`](modeling_glm4_moe_lite.md#Glm4MoeLiteMLP), [`n_group`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.n_group), [`n_shared_experts`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.n_shared_experts), [`num_experts_per_tok`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.num_experts_per_tok), [`Glm4MoeLiteMLPStack`](modeling_glm4_moe_lite.md#Glm4MoeLiteMLPStack), [`Glm4MoeLiteTopKRouter`](modeling_glm4_moe_lite.md#Glm4MoeLiteTopKRouter), [`norm_topk_prob`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.norm_topk_prob), [`routed_scaling_factor`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.routed_scaling_factor), [`topk_group`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.topk_group)
- used by: [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`hidden_size`](modeling_glm4_moe_lite.md#Glm4MoeLiteDecoderLayer.hidden_size)

### `Glm4MoeLiteModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py:909`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L909)
- doc: GLM-4-MoE-Lite base model implementation.
- signature: `class Glm4MoeLiteModel(EasyDeLBaseModule):`
- members:
  - `frequencies(self)` — [`L976`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L976)
  - `embed_tokens` — [`L940`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L940)
  - `layers` — [`L954`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L954)
  - `norm` — [`L967`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L967) — documented in [easydel-layers-norms-_norms](../../../../concepts/easydel-layers-norms-_norms.md)
- protocol/private: `__call__`[`L983`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L983), `__init__`[`L918`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L918)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`MoeModelOutput`](../../infra/modeling_outputs.md#MoeModelOutput), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`dtype`](../../infra/base_module.md#EasyDeLBaseModule.dtype), [`gradient_checkpointing`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing), [`get_basic_frequencies`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_frequencies), [`param_dtype`](../../infra/base_module.md#EasyDeLBaseModule.param_dtype), [`router_logits`](../../infra/modeling_outputs.md#DecoderLayerOutput.router_logits), [`Glm4MoeLiteConfig`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig), [`rngs`](../../infra/base_module.md#EasyDeLBaseModule.rngs), [`hidden_size`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.hidden_size), [`initializer_range`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.initializer_range), [`precision`](../../infra/base_module.md#EasyDeLBaseModule.precision), [`rms_norm_eps`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.rms_norm_eps), [`num_hidden_layers`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.num_hidden_layers), [`Glm4MoeLiteDecoderLayer`](modeling_glm4_moe_lite.md#Glm4MoeLiteDecoderLayer), [`vocab_size`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`Glm4MoeLiteForCausalLM`](modeling_glm4_moe_lite.md#Glm4MoeLiteForCausalLM), [`__init__`](modeling_glm4_moe_lite.md#Glm4MoeLiteForCausalLM.__init__)

### `Glm4MoeLiteTopKRouter`  ·  implements/extends Module
- def: [`easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py:235`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L235)
- doc: Top-K expert router for GLM-4-MoE-Lite with grouped expert selection.
- signature: `class Glm4MoeLiteTopKRouter(nn.Module):`
- members:
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L266`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L266)
  - `config` — [`L252`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L252)
  - `dtype` — [`L253`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L253)
  - `e_score_correction_bias` — [`L264`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L264)
  - `kernel` — [`L257`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L257)
  - `n_routed_experts` — [`L256`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L256)
  - `param_dtype` — [`L254`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L254)
  - `precision` — [`L255`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L255)
- protocol/private: `__call__`[`L270`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L270), `__init__`[`L243`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L243)
- uses (calls/refs, reference-scoped): [`use_expert_tensor_mode`](../../infra/base_config.md#EasyDeLBaseConfig.use_expert_tensor_mode), [`Glm4MoeLiteConfig`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig), [`hidden_size`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.hidden_size), [`initializer_range`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.initializer_range), [`n_routed_experts`](glm4_moe_lite_configuration.md#Glm4MoeLiteConfig.n_routed_experts)
- used by: [`gate`](modeling_glm4_moe_lite.md#Glm4MoeLiteMoE.gate)

## Module values
- `__all__` — [`L1207`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4_moe_lite/modeling_glm4_moe_lite.py#L1207)

