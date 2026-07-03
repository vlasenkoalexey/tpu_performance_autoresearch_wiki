---
title: 'Module: easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py'
type: catalog
provenance: extracted
module: easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.glm_moe_dsa.modeling_glm_moe_dsa`/
symbols:
  GlmMoeDsaAttention.forward_mla: GlmMoeDsaAttention#forward_mla().
  GlmMoeDsaModel.__call__: GlmMoeDsaModel#__call__().
  GlmMoeDsaAttention.define_network: GlmMoeDsaAttention#define_network().
  GlmMoeDsaDecoderLayer.__call__: GlmMoeDsaDecoderLayer#__call__().
  GlmMoeDsaMoE.shared_experts: GlmMoeDsaMoE#shared_experts.
  GlmMoeDsaIndexer.__call__: GlmMoeDsaIndexer#__call__().
  GlmMoeDsaModel.embed_tokens: GlmMoeDsaModel#embed_tokens.
  GlmMoeDsaMoE.__init__: GlmMoeDsaMoE#__init__().
  GlmMoeDsaMoE.__call__: GlmMoeDsaMoE#__call__().
  GlmMoeDsaForCausalLM.create_ragged_page_cache_config: GlmMoeDsaForCausalLM#create_ragged_page_cache_config().
  GlmMoeDsaAttention.qk_nope_head_dim: GlmMoeDsaAttention#qk_nope_head_dim.
  GlmMoeDsaModel.__init__: GlmMoeDsaModel#__init__().
  GlmMoeDsaMLPStack.gate_proj: GlmMoeDsaMLPStack#gate_proj.
  GlmMoeDsaMLPStack.up_proj: GlmMoeDsaMLPStack#up_proj.
  GlmMoeDsaMLPStack.down_proj: GlmMoeDsaMLPStack#down_proj.
  GlmMoeDsaForCausalLM: GlmMoeDsaForCausalLM#
  GlmMoeDsaModel: GlmMoeDsaModel#
  GlmMoeDsaMLP.__call__: GlmMoeDsaMLP#__call__().
  GlmMoeDsaMLPStack.__call__: GlmMoeDsaMLPStack#__call__().
  GlmMoeDsaIndexer.kernels_proj: GlmMoeDsaIndexer#kernels_proj.
  GlmMoeDsaMLP.intermediate_size: GlmMoeDsaMLP#intermediate_size.
  GlmMoeDsaIndexer.wq_b: GlmMoeDsaIndexer#wq_b.
  GlmMoeDsaIndexer.wk: GlmMoeDsaIndexer#wk.
  GlmMoeDsaAttention.q_head_dim: GlmMoeDsaAttention#q_head_dim.
  GlmMoeDsaAttention._create_attention_performer: GlmMoeDsaAttention#_create_attention_performer().
  GlmMoeDsaDecoderLayer.self_attn: GlmMoeDsaDecoderLayer#self_attn.
  GlmMoeDsaModel.norm: GlmMoeDsaModel#norm.
  GlmMoeDsaForCausalLM.create_unified_attention_cache_config: GlmMoeDsaForCausalLM#create_unified_attention_cache_config().
  GlmMoeDsaAttention.v_head_dim: GlmMoeDsaAttention#v_head_dim.
  GlmMoeDsaDecoderLayer.mlp: GlmMoeDsaDecoderLayer#mlp.
  GlmMoeDsaTopKRouter.kernel: GlmMoeDsaTopKRouter#kernel.
  GlmMoeDsaDecoderLayer.input_layernorm: GlmMoeDsaDecoderLayer#input_layernorm.
  GlmMoeDsaDecoderLayer.post_attention_layernorm: GlmMoeDsaDecoderLayer#post_attention_layernorm.
  GlmMoeDsaAttention.projection_mapping: GlmMoeDsaAttention#projection_mapping.
  GlmMoeDsaLayerNorm.__call__: GlmMoeDsaLayerNorm#__call__().
  GlmMoeDsaTopKRouter.__call__: GlmMoeDsaTopKRouter#__call__().
  GlmMoeDsaMoE.experts: GlmMoeDsaMoE#experts.
  GlmMoeDsaIndexer.index_head_dim: GlmMoeDsaIndexer#index_head_dim.
  GlmMoeDsaAttention.index_topk: GlmMoeDsaAttention#index_topk.
  GlmMoeDsaAttention.rotary: GlmMoeDsaAttention#rotary.
  GlmMoeDsaForCausalLM.__init__: GlmMoeDsaForCausalLM#__init__().
  GlmMoeDsaMLPStack.act_fn: GlmMoeDsaMLPStack#act_fn.
  GlmMoeDsaModel.layers: GlmMoeDsaModel#layers.
  GlmMoeDsaIndexer.index_n_heads: GlmMoeDsaIndexer#index_n_heads.
  GlmMoeDsaMLP.gate_proj: GlmMoeDsaMLP#gate_proj.
  GlmMoeDsaMLP.up_proj: GlmMoeDsaMLP#up_proj.
  GlmMoeDsaMLP.down_proj: GlmMoeDsaMLP#down_proj.
  GlmMoeDsaMLP.act_fn: GlmMoeDsaMLP#act_fn.
  GlmMoeDsaMoE.group_topk_k: GlmMoeDsaMoE#group_topk_k.
  GlmMoeDsaIndexer.indexer_rope_interleave: GlmMoeDsaIndexer#indexer_rope_interleave.
  GlmMoeDsaIndexer.k_norm: GlmMoeDsaIndexer#k_norm.
  GlmMoeDsaModel.frequencies: GlmMoeDsaModel#frequencies().
  GlmMoeDsaMLP.hidden_size: GlmMoeDsaMLP#hidden_size.
  GlmMoeDsaAttention.kv_lora_rank: GlmMoeDsaAttention#kv_lora_rank.
  GlmMoeDsaTopKRouter.craft_sharding: GlmMoeDsaTopKRouter#craft_sharding().
  GlmMoeDsaForCausalLM._task_type: GlmMoeDsaForCausalLM#_task_type.
  GlmMoeDsaTopKRouter.n_routed_experts: GlmMoeDsaTopKRouter#n_routed_experts.
  GlmMoeDsaAttention.qk_rope_head_dim: GlmMoeDsaAttention#qk_rope_head_dim.
  GlmMoeDsaMoE: GlmMoeDsaMoE#
  GlmMoeDsaMoE.n_group: GlmMoeDsaMoE#n_group.
  GlmMoeDsaMoE.topk_group: GlmMoeDsaMoE#topk_group.
  GlmMoeDsaMoE.norm_topk_prob: GlmMoeDsaMoE#norm_topk_prob.
  GlmMoeDsaMoE.routed_scaling_factor: GlmMoeDsaMoE#routed_scaling_factor.
  GlmMoeDsaMoE.gate: GlmMoeDsaMoE#gate.
  GlmMoeDsaIndexer.index_topk: GlmMoeDsaIndexer#index_topk.
  GlmMoeDsaIndexer.softmax_scale: GlmMoeDsaIndexer#softmax_scale.
  GlmMoeDsaIndexer.indexer_op: GlmMoeDsaIndexer#indexer_op.
  GlmMoeDsaAttention: GlmMoeDsaAttention#
  GlmMoeDsaAttention.index_head_dim: GlmMoeDsaAttention#index_head_dim.
  GlmMoeDsaAttention.indexer: GlmMoeDsaAttention#indexer.
  GlmMoeDsaMLP.__init__: GlmMoeDsaMLP#__init__().
  GlmMoeDsaMLPStack.__init__: GlmMoeDsaMLPStack#__init__().
  GlmMoeDsaTopKRouter.__init__: GlmMoeDsaTopKRouter#__init__().
  GlmMoeDsaTopKRouter.e_score_correction_bias: GlmMoeDsaTopKRouter#e_score_correction_bias.
  GlmMoeDsaIndexer.__init__: GlmMoeDsaIndexer#__init__().
  GlmMoeDsaAttention.__init__: GlmMoeDsaAttention#__init__().
  GlmMoeDsaAttention.index_n_heads: GlmMoeDsaAttention#index_n_heads.
  GlmMoeDsaAttention.head_dim: GlmMoeDsaAttention#head_dim.
  GlmMoeDsaDecoderLayer.__init__: GlmMoeDsaDecoderLayer#__init__().
  GlmMoeDsaDecoderLayer.hidden_size: GlmMoeDsaDecoderLayer#hidden_size.
  GlmMoeDsaForCausalLM._config_class: GlmMoeDsaForCausalLM#_config_class.
  GlmMoeDsaMLP: GlmMoeDsaMLP#
  GlmMoeDsaMLP.config: GlmMoeDsaMLP#config.
  GlmMoeDsaMLPStack.config: GlmMoeDsaMLPStack#config.
  GlmMoeDsaTopKRouter.config: GlmMoeDsaTopKRouter#config.
  GlmMoeDsaAttention.config: GlmMoeDsaAttention#config.
  GlmMoeDsaAttention._apply_rope_interleaved: GlmMoeDsaAttention#_apply_rope_interleaved().
  GlmMoeDsaDecoderLayer.config: GlmMoeDsaDecoderLayer#config.
  logger: logger.
  GlmMoeDsaLayerNorm: GlmMoeDsaLayerNorm#
  GlmMoeDsaLayerNorm.eps: GlmMoeDsaLayerNorm#eps.
  GlmMoeDsaLayerNorm.kernel: GlmMoeDsaLayerNorm#kernel.
  GlmMoeDsaLayerNorm.bias: GlmMoeDsaLayerNorm#bias.
  GlmMoeDsaMLPStack: GlmMoeDsaMLPStack#
  GlmMoeDsaTopKRouter: GlmMoeDsaTopKRouter#
  GlmMoeDsaMoE._select_experts_static: GlmMoeDsaMoE#_select_experts_static().
  GlmMoeDsaIndexer: GlmMoeDsaIndexer#
  GlmMoeDsaIndexer.config: GlmMoeDsaIndexer#config.
  GlmMoeDsaDecoderLayer: GlmMoeDsaDecoderLayer#
  GlmMoeDsaMLP.dtype: GlmMoeDsaMLP#dtype.
  GlmMoeDsaMLP.param_dtype: GlmMoeDsaMLP#param_dtype.
  GlmMoeDsaMLP.precision: GlmMoeDsaMLP#precision.
  GlmMoeDsaLayerNorm.__init__: GlmMoeDsaLayerNorm#__init__().
  GlmMoeDsaLayerNorm.hidden_size: GlmMoeDsaLayerNorm#hidden_size.
  GlmMoeDsaLayerNorm.dtype: GlmMoeDsaLayerNorm#dtype.
  GlmMoeDsaLayerNorm.param_dtype: GlmMoeDsaLayerNorm#param_dtype.
  GlmMoeDsaLayerNorm.craft_sharding: GlmMoeDsaLayerNorm#craft_sharding().
  GlmMoeDsaMLPStack.reform_param: GlmMoeDsaMLPStack#reform_param.
  GlmMoeDsaMLPStack.dtype: GlmMoeDsaMLPStack#dtype.
  GlmMoeDsaMLPStack.param_dtype: GlmMoeDsaMLPStack#param_dtype.
  GlmMoeDsaMLPStack.precision: GlmMoeDsaMLPStack#precision.
  GlmMoeDsaTopKRouter.dtype: GlmMoeDsaTopKRouter#dtype.
  GlmMoeDsaTopKRouter.param_dtype: GlmMoeDsaTopKRouter#param_dtype.
  GlmMoeDsaTopKRouter.precision: GlmMoeDsaTopKRouter#precision.
  GlmMoeDsaMoE.config: GlmMoeDsaMoE#config.
  GlmMoeDsaMoE.dtype: GlmMoeDsaMoE#dtype.
  GlmMoeDsaMoE.param_dtype: GlmMoeDsaMoE#param_dtype.
  GlmMoeDsaMoE.precision: GlmMoeDsaMoE#precision.
  GlmMoeDsaIndexer.dtype: GlmMoeDsaIndexer#dtype.
  GlmMoeDsaIndexer.param_dtype: GlmMoeDsaIndexer#param_dtype.
  GlmMoeDsaIndexer.precision: GlmMoeDsaIndexer#precision.
  GlmMoeDsaDecoderLayer.dtype: GlmMoeDsaDecoderLayer#dtype.
  GlmMoeDsaDecoderLayer.param_dtype: GlmMoeDsaDecoderLayer#param_dtype.
  GlmMoeDsaDecoderLayer.precision: GlmMoeDsaDecoderLayer#precision.
  GlmMoeDsaDecoderLayer.rngs: GlmMoeDsaDecoderLayer#rngs.
  GlmMoeDsaDecoderLayer.layer_idx: GlmMoeDsaDecoderLayer#layer_idx.
  GlmMoeDsaForCausalLM._model_type: GlmMoeDsaForCausalLM#_model_type.
  __all__: __all__.
---
# Module: [`easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py)

## Classes
### `GlmMoeDsaAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py:632`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L632)
- doc: Multi-head Latent Attention (MLA) for GLM-MoE-DSA.
- signature: `class GlmMoeDsaAttention(UnifiedAttention):`
- members:
  - `define_network(self, config: GlmMoeDsaConfig, dtype: jnp.dtype, param_dtype: jnp.dtype, precision: jax.lax.Precision, rngs: nn.Rngs)` — [`L699`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L699) — Creates all projection layers, rotary embeddings, attention performer, and DSA indexer.
  - `forward_mla(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None, alibi: Float[Array, "batch_or_1 heads qseq_len_or_1 kvseq_len_or_1"] | None = None)` — [`L863`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L863)
  - `config` — [`L676`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L676)
  - `head_dim` — [`L697`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L697)
  - `index_head_dim` — [`L683`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L683)
  - `index_n_heads` — [`L682`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L682)
  - `index_topk` — [`L684`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L684)
  - `indexer` — [`L831`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L831)
  - `kv_lora_rank` — [`L681`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L681)
  - `projection_mapping` — [`L651`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L651)
  - `q_head_dim` — [`L677`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L677)
  - `qk_nope_head_dim` — [`L678`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L678)
  - `qk_rope_head_dim` — [`L679`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L679)
  - `rotary` — [`L829`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L829)
  - `v_head_dim` — [`L680`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L680)
- protocol/private: `__init__`[`L666`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L666), `_apply_rope_interleaved`[`L856`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L856), `_create_attention_performer`[`L839`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L839)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`forward`](../../layers/attention/_flexible.md#FlexibleAttentionModule.forward), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`AttentionLayerOutput`](../../infra/modeling_outputs.md#AttentionLayerOutput), [`concatenate`](../../layers/attention/_flexible.md#AttentionModule.concatenate), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`attention_outputs`](../../operations/_attention_outputs.md#AttentionOutput.attention_outputs), [`attention_performer`](../../layers/attention/_unified.md#UnifiedAttention.attention_performer), [`num_heads`](../../layers/attention/_unified.md#UnifiedAttention.num_heads), [`MLARaggedPagesCacheView`](../../caching/mla_ragged_page/cache.md#MLARaggedPagesCacheView), [`ParallelHybridCacheView`](../../caching/hybrid/cache.md#ParallelHybridCacheView), [`shard_attention_prod`](../../layers/attention/_flexible.md#AttentionModule.shard_attention_prod), [`GlmMoeDsaConfig`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig), [`_merge_heads`](../../layers/attention/_unified.md#UnifiedAttention._merge_heads), [`attention_weights`](../../operations/_attention_outputs.md#AttentionOutput.attention_weights), [`hidden_size`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.hidden_size), [`kernel`](../../layers/linears/_linear.md#ParallelLinear.kernel), [`output_projection`](../../layers/attention/_unified.md#UnifiedAttention.output_projection), [`sliding_window`](../../layers/attention/_unified.md#UnifiedAttention.sliding_window), [`yarn_get_mscale`](../../layers/rotary/_utils.md#yarn_get_mscale), [`initializer_range`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.initializer_range), [`mla_kv_b_proj`](../../layers/attention/_unified.md#UnifiedAttention.mla_kv_b_proj), [`mla_kv_a_layernorm`](../../layers/attention/_unified.md#UnifiedAttention.mla_kv_a_layernorm), [`causal`](../../layers/attention/_unified.md#UnifiedAttention.causal), [`use_mla_lora`](../../layers/attention/_unified.md#UnifiedAttention.use_mla_lora), [`mla_kv_a_proj_with_mqa`](../../layers/attention/_unified.md#UnifiedAttention.mla_kv_a_proj_with_mqa), [`mla_q_a_layernorm`](../../layers/attention/_unified.md#UnifiedAttention.mla_q_a_layernorm), [`mla_q_a_proj`](../../layers/attention/_unified.md#UnifiedAttention.mla_q_a_proj), [`mla_q_b_proj`](../../layers/attention/_unified.md#UnifiedAttention.mla_q_b_proj), [`mla_q_proj`](../../layers/attention/_unified.md#UnifiedAttention.mla_q_proj), [`q_lora_rank`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.q_lora_rank)  (+14 more)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_attention_performer`](../../layers/attention/_unified.md#UnifiedAttention._create_attention_performer), [`forward_mla`](../../layers/attention/_unified.md#UnifiedAttention.forward_mla), [`define_network`](../../layers/attention/_unified.md#UnifiedAttention.define_network), [`self_attn`](modeling_glm_moe_dsa.md#GlmMoeDsaDecoderLayer.self_attn)

### `GlmMoeDsaDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py:1118`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1118)
- doc: Single transformer decoder layer for GLM-MoE-DSA.
- signature: `class GlmMoeDsaDecoderLayer(nn.Module):`
- members:
  - `config` — [`L1144`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1144)
  - `dtype` — [`L1145`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1145)
  - `hidden_size` — [`L1150`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1150)
  - `input_layernorm` — [`L1183`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1183)
  - `layer_idx` — [`L1149`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1149)
  - `mlp` — [`L1167`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1167)
  - `param_dtype` — [`L1146`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1146)
  - `post_attention_layernorm` — [`L1190`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1190)
  - `precision` — [`L1147`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1147)
  - `rngs` — [`L1148`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1148)
  - `self_attn` — [`L1152`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1152)
- protocol/private: `__call__`[`L1198`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1198), `__init__`[`L1134`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1134)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`GlmMoeDsaConfig`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig), [`mlp_layer_types`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.mlp_layer_types), [`hidden_size`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.hidden_size), [`n_routed_experts`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.n_routed_experts), [`GlmMoeDsaAttention`](modeling_glm_moe_dsa.md#GlmMoeDsaAttention), [`GlmMoeDsaMoE`](modeling_glm_moe_dsa.md#GlmMoeDsaMoE), [`rms_norm_eps`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.rms_norm_eps), [`GlmMoeDsaMLP`](modeling_glm_moe_dsa.md#GlmMoeDsaMLP), [`num_experts_per_tok`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.num_experts_per_tok)
- used by: [`embed_tokens`](modeling_glm_moe_dsa.md#GlmMoeDsaModel.embed_tokens)

### `GlmMoeDsaForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py:1431`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1431)
- doc: GLM-MoE-DSA model with a causal language-modelling head.
- signature: `class GlmMoeDsaForCausalLM(BaseCausalLMModule[GlmMoeDsaModel, GlmMoeDsaConfig]):`
- members:
  - `create_ragged_page_cache_config(self, max_length: int, *, page_size: int = 128, hbm_utilization: float = 0.9, dtype: jnp.dtype | None = None)` — [`L1470`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1470) — Create paged cache configuration for MLA attention.
  - `create_unified_attention_cache_config(self, max_length: int, *, page_size: int = 128, hbm_utilization: float = 0.9, dtype: jnp.dtype | None = None)` — [`L1529`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1529) — Create unified-attention cache configuration for MLA attention.
- protocol/private: `__init__`[`L1449`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1449), `_config_class`[`L1447`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1447), `_model_type`[`L1446`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1446), `_task_type`[`L1445`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1445)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`RaggedPagesCacheConfig`](../../caching/ragged_page/cache.md#RaggedPagesCacheConfig), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`mesh`](../../infra/base_module.md#EasyDeLBaseModule.mesh), [`AttentionMechanisms`](../../layers/attention/_flexible.md#AttentionMechanisms), [`UnifiedAttentionCacheConfig`](../../caching/unified_attention/cache.md#UnifiedAttentionCacheConfig), [`create`](../../caching/ragged_page/cache.md#RaggedPagesCacheConfig.create), [`GlmMoeDsaConfig`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig), [`create`](../../caching/unified_attention/cache.md#UnifiedAttentionCacheConfig.create), [`GlmMoeDsaModel`](modeling_glm_moe_dsa.md#GlmMoeDsaModel), [`_create_mla_ragged_page_cache_config`](../../infra/mixins/generation.md#EasyGenerationMixin._create_mla_ragged_page_cache_config), [`RAGGED_PAGE_ATTENTION_V3`](../../layers/attention/_flexible.md#AttentionMechanisms.RAGGED_PAGE_ATTENTION_V3), [`RAGGED_PAGE_ATTENTION_V2`](../../layers/attention/_flexible.md#AttentionMechanisms.RAGGED_PAGE_ATTENTION_V2)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`create_unified_attention_cache_config`](../../infra/mixins/generation.md#EasyGenerationMixin.create_unified_attention_cache_config), [`create_ragged_page_cache_config`](../../infra/mixins/generation.md#EasyGenerationMixin.create_ragged_page_cache_config)

### `GlmMoeDsaIndexer`  ·  implements/extends Module
- def: [`easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py:514`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L514)
- doc: Dynamic Sparse Attention (DSA) indexer for GLM-MoE-DSA.
- signature: `class GlmMoeDsaIndexer(nn.Module):`
- members:
  - `config` — [`L539`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L539)
  - `dtype` — [`L540`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L540)
  - `index_head_dim` — [`L544`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L544)
  - `index_n_heads` — [`L543`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L543)
  - `index_topk` — [`L545`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L545)
  - `indexer_op` — [`L593`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L593)
  - `indexer_rope_interleave` — [`L547`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L547)
  - `k_norm` — [`L570`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L570)
  - `kernels_proj` — [`L577`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L577)
  - `param_dtype` — [`L541`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L541)
  - `precision` — [`L542`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L542)
  - `softmax_scale` — [`L546`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L546)
  - `wk` — [`L560`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L560)
  - `wq_b` — [`L550`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L550)
- protocol/private: `__call__`[`L595`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L595), `__init__`[`L530`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L530)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`OperationMetadata`](../../operations/_operation_meta.md#OperationMetadata), [`GlmMoeDsaConfig`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig), [`hidden_size`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.hidden_size), [`GlmMoeDsaIndexerOutput`](../../operations/kernels/glm_moe_dsa_indexer.md#GlmMoeDsaIndexerOutput), [`initializer_range`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.initializer_range), [`q_lora_rank`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.q_lora_rank), [`GlmMoeDsaIndexerOp`](../../operations/kernels/glm_moe_dsa_indexer.md#GlmMoeDsaIndexerOp), [`qk_rope_head_dim`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.qk_rope_head_dim), [`index_head_dim`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.index_head_dim), [`index_n_heads`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.index_n_heads), [`index_topk`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.index_topk), [`GlmMoeDsaLayerNorm`](modeling_glm_moe_dsa.md#GlmMoeDsaLayerNorm)
- used by: [`indexer`](modeling_glm_moe_dsa.md#GlmMoeDsaAttention.indexer)

### `GlmMoeDsaLayerNorm`  ·  implements/extends Module
- def: [`easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py:150`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L150)
- doc: Standard Layer Normalisation with `kernel`/`bias` parameter names matching HF checkpoints.
- signature: `class GlmMoeDsaLayerNorm(nn.Module):`
- members:
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L177`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L177)
  - `bias` — [`L175`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L175)
  - `dtype` — [`L172`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L172)
  - `eps` — [`L171`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L171)
  - `hidden_size` — [`L170`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L170)
  - `kernel` — [`L174`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L174)
  - `param_dtype` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L173)
- protocol/private: `__call__`[`L180`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L180), `__init__`[`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L161)
- used by: [`k_norm`](modeling_glm_moe_dsa.md#GlmMoeDsaIndexer.k_norm)

### `GlmMoeDsaMLP`  ·  implements/extends Module
- def: [`easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py:70`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L70)
- doc: Dense gated MLP block used in the first few (dense) layers of GLM-MoE-DSA.
- signature: `class GlmMoeDsaMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L125) — Applies the gated MLP transformation.
  - `act_fn` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L123)
  - `config` — [`L96`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L96)
  - `down_proj` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L122)
  - `dtype` — [`L97`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L97)
  - `gate_proj` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L120)
  - `hidden_size` — [`L100`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L100)
  - `intermediate_size` — [`L101`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L101)
  - `param_dtype` — [`L98`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L98)
  - `precision` — [`L99`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L99)
  - `up_proj` — [`L121`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L121)
- protocol/private: `__init__`[`L85`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L85)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`GlmMoeDsaConfig`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig), [`hidden_size`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.hidden_size), [`initializer_range`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.initializer_range), [`hidden_act`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.hidden_act), [`intermediate_size`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.intermediate_size)
- used by: [`shared_experts`](modeling_glm_moe_dsa.md#GlmMoeDsaMoE.shared_experts), [`mlp`](modeling_glm_moe_dsa.md#GlmMoeDsaDecoderLayer.mlp)

### `GlmMoeDsaMLPStack`  ·  implements/extends Module
- def: [`easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py:190`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L190)
- doc: Stacked expert MLP kernels for GLM-MoE-DSA MoE layers.
- signature: `class GlmMoeDsaMLPStack(nn.Module):`
- members:
  - `__call__(self, hidden_states: Array, group_sizes: Array, sorted_experts: Array | None = None)` — [`L278`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L278) — Applies the gated MLP across all experts in a fused manner.
  - `act_fn` — [`L276`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L276)
  - `config` — [`L236`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L236)
  - `down_proj` — [`L264`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L264)
  - `dtype` — [`L237`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L237)
  - `gate_proj` — [`L240`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L240)
  - `param_dtype` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L238)
  - `precision` — [`L239`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L239)
  - `reform_param` — [`L208`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L208)
  - `up_proj` — [`L252`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L252)
- protocol/private: `__init__`[`L227`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L227)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`use_expert_tensor_mode`](../../infra/base_config.md#EasyDeLBaseConfig.use_expert_tensor_mode), [`ColumnParallelMoELinear`](../../layers/linears/_linear_moe.md#ColumnParallelMoELinear), [`RowParallelMoELinear`](../../layers/linears/_linear_moe.md#RowParallelMoELinear), [`GlmMoeDsaConfig`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig), [`hidden_size`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.hidden_size), [`n_routed_experts`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.n_routed_experts), [`moe_intermediate_size`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.moe_intermediate_size), [`hidden_act`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.hidden_act)
- used by: [`__call__`](modeling_glm_moe_dsa.md#GlmMoeDsaMoE.__call__), [`experts`](modeling_glm_moe_dsa.md#GlmMoeDsaMoE.experts)

### `GlmMoeDsaMoE`  ·  implements/extends BaseMoeModule
- def: [`easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py:373`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L373)
- doc: Mixture-of-Experts feed-forward block for GLM-MoE-DSA sparse layers.
- signature: `class GlmMoeDsaMoE(BaseMoeModule):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L491`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L491) — Routes tokens through selected experts and combines outputs.
  - `config` — [`L407`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L407)
  - `dtype` — [`L408`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L408)
  - `experts` — [`L417`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L417)
  - `gate` — [`L424`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L424)
  - `group_topk_k` — [`L415`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L415)
  - `n_group` — [`L411`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L411)
  - `norm_topk_prob` — [`L413`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L413)
  - `param_dtype` — [`L409`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L409)
  - `precision` — [`L410`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L410)
  - `routed_scaling_factor` — [`L414`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L414)
  - `shared_experts` — [`L431`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L431)
  - `topk_group` — [`L412`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L412)
- protocol/private: `__init__`[`L388`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L388), `_select_experts_static`[`L457`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L457)
- uses (calls/refs, reference-scoped): [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`kernel`](../../layers/linears/_linear_moe.md#ParallelMoELinear.kernel), [`MoeRoutingStrategy`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy), [`moe_call`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_call), [`MoeLoadBalancingStrategy`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy), [`__init__`](../../layers/moe/_moe_module.md#BaseMoeModule.__init__), [`moe_hooks`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_hooks), [`n_routed_experts`](../../layers/moe/_moe_module.md#BaseMoeModule.n_routed_experts), [`GlmMoeDsaConfig`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig), [`TOP_K`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy.TOP_K), [`STANDARD`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy.STANDARD), [`hidden_size`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.hidden_size), [`down_proj`](modeling_glm_moe_dsa.md#GlmMoeDsaMLPStack.down_proj), [`gate_proj`](modeling_glm_moe_dsa.md#GlmMoeDsaMLPStack.gate_proj), [`up_proj`](modeling_glm_moe_dsa.md#GlmMoeDsaMLPStack.up_proj), [`MoeFusedHooks`](../../layers/moe/_communication_utils.md#MoeFusedHooks), [`select_hook`](../../layers/moe/_communication_utils.md#MoeFusedHooks.select_hook), [`n_routed_experts`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.n_routed_experts), [`act_fn`](modeling_glm_moe_dsa.md#GlmMoeDsaMLPStack.act_fn), [`n_group`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.n_group), [`normalize_gate_logits`](../../layers/moe/_communication_utils.md#MoeFusedHooks.normalize_gate_logits), [`moe_intermediate_size`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.moe_intermediate_size), [`GlmMoeDsaMLP`](modeling_glm_moe_dsa.md#GlmMoeDsaMLP), [`n_shared_experts`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.n_shared_experts), [`num_experts_per_tok`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.num_experts_per_tok), [`GlmMoeDsaMLPStack`](modeling_glm_moe_dsa.md#GlmMoeDsaMLPStack), [`GlmMoeDsaTopKRouter`](modeling_glm_moe_dsa.md#GlmMoeDsaTopKRouter), [`norm_topk_prob`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.norm_topk_prob), [`routed_scaling_factor`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.routed_scaling_factor), [`topk_group`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.topk_group)
- used by: [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`mlp`](modeling_glm_moe_dsa.md#GlmMoeDsaDecoderLayer.mlp)

### `GlmMoeDsaModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py:1251`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1251)
- doc: GLM-MoE-DSA base transformer model (no language-model head).
- signature: `class GlmMoeDsaModel(EasyDeLBaseModule):`
- members:
  - `frequencies(self)` — [`L1325`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1325) — Computes and caches RoPE frequency tensor for the model's rope head dimension.
  - `embed_tokens` — [`L1289`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1289)
  - `layers` — [`L1303`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1303)
  - `norm` — [`L1316`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1316)
- protocol/private: `__call__`[`L1333`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1333), `__init__`[`L1267`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1267)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`MoeModelOutput`](../../infra/modeling_outputs.md#MoeModelOutput), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`dtype`](../../infra/base_module.md#EasyDeLBaseModule.dtype), [`gradient_checkpointing`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing), [`get_basic_frequencies`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_frequencies), [`param_dtype`](../../infra/base_module.md#EasyDeLBaseModule.param_dtype), [`router_logits`](../../infra/modeling_outputs.md#DecoderLayerOutput.router_logits), [`GlmMoeDsaConfig`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig), [`rngs`](../../infra/base_module.md#EasyDeLBaseModule.rngs), [`hidden_size`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.hidden_size), [`initializer_range`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.initializer_range), [`precision`](../../infra/base_module.md#EasyDeLBaseModule.precision), [`num_hidden_layers`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.num_hidden_layers), [`rms_norm_eps`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.rms_norm_eps), [`GlmMoeDsaDecoderLayer`](modeling_glm_moe_dsa.md#GlmMoeDsaDecoderLayer), [`vocab_size`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`GlmMoeDsaForCausalLM`](modeling_glm_moe_dsa.md#GlmMoeDsaForCausalLM), [`__init__`](modeling_glm_moe_dsa.md#GlmMoeDsaForCausalLM.__init__)

### `GlmMoeDsaTopKRouter`  ·  implements/extends Module
- def: [`easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py:316`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L316)
- doc: Routing gate for GLM-MoE-DSA grouped top-k expert selection.
- signature: `class GlmMoeDsaTopKRouter(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "tokens hidden_dim"])` — [`L357`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L357) — Computes per-expert routing logits for all tokens.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L353`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L353)
  - `config` — [`L339`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L339)
  - `dtype` — [`L340`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L340)
  - `e_score_correction_bias` — [`L351`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L351)
  - `kernel` — [`L344`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L344)
  - `n_routed_experts` — [`L343`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L343)
  - `param_dtype` — [`L341`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L341)
  - `precision` — [`L342`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L342)
- protocol/private: `__init__`[`L330`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L330)
- uses (calls/refs, reference-scoped): [`use_expert_tensor_mode`](../../infra/base_config.md#EasyDeLBaseConfig.use_expert_tensor_mode), [`GlmMoeDsaConfig`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig), [`hidden_size`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.hidden_size), [`initializer_range`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.initializer_range), [`n_routed_experts`](glm_moe_dsa_configuration.md#GlmMoeDsaConfig.n_routed_experts)
- used by: [`gate`](modeling_glm_moe_dsa.md#GlmMoeDsaMoE.gate)

## Module values
- `__all__` — [`L1565`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L1565)
- `logger` — [`L67`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm_moe_dsa/modeling_glm_moe_dsa.py#L67)

