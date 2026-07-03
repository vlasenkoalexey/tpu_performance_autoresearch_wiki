---
title: 'Module: easydel/modules/mosaic_mpt/modeling_mosaic.py'
type: catalog
provenance: extracted
module: easydel/modules/mosaic_mpt/modeling_mosaic.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.mosaic_mpt.modeling_mosaic`/
symbols:
  MptAttention.forward_alibi: MptAttention#forward_alibi().
  MptModel.__call__: MptModel#__call__().
  MptBlock.__call__: MptBlock#__call__().
  MptModel.wte: MptModel#wte.
  MptForCausalLM: MptForCausalLM#
  MptMLP.config: MptMLP#config.
  MptModel: MptModel#
  MptAttention._create_attention_performer: MptAttention#_create_attention_performer().
  MptAttention._compute_alibi_bias: MptAttention#_compute_alibi_bias().
  MptAttention.resid_dropout: MptAttention#resid_dropout.
  MptMLP.__call__: MptMLP#__call__().
  MptForCausalLM.__init__: MptForCausalLM#__init__().
  MptMLP.hidden_dropout: MptMLP#hidden_dropout.
  MptAttention.Wqkv: MptAttention#Wqkv.
  MptAttention.out_proj: MptAttention#out_proj.
  MptBlock.norm_1: MptBlock#norm_1.
  MptBlock.norm_2: MptBlock#norm_2.
  MptBlock.dropout_rate: MptBlock#dropout_rate.
  MptModel.norm_f: MptModel#norm_f.
  MptMLP.up_proj: MptMLP#up_proj.
  MptMLP.down_proj: MptMLP#down_proj.
  MptModel.alibi: MptModel#alibi().
  MptAttention.__init__: MptAttention#__init__().
  MptModel.__init__: MptModel#__init__().
  MptForCausalLM._task_type: MptForCausalLM#_task_type.
  MptModel.blocks: MptModel#blocks.
  MptAttention: MptAttention#
  MptBlock.attn: MptBlock#attn.
  MptBlock.ffn: MptBlock#ffn.
  MptBlock.resid_attn_dropout: MptBlock#resid_attn_dropout.
  MptMLP.__init__: MptMLP#__init__().
  MptAttention.define_network: MptAttention#define_network().
  MptBlock.__init__: MptBlock#__init__().
  MptModel.get_embedding: MptModel#get_embedding().
  MptForCausalLM._config_class: MptForCausalLM#_config_class.
  build_mpt_alibi_tensor: build_mpt_alibi_tensor().
  MptMLP: MptMLP#
  MptBlock: MptBlock#
  MptBlock.config: MptBlock#config.
  MptBlock.dtype: MptBlock#dtype.
  MptBlock.param_dtype: MptBlock#param_dtype.
  MptBlock.precision: MptBlock#precision.
  MptBlock.rngs: MptBlock#rngs.
  MptModel.get_encoder: MptModel#get_encoder().
  MptModel.get_decoder: MptModel#get_decoder().
  MptModel.get_lm_head: MptModel#get_lm_head().
  MptForCausalLM._model_type: MptForCausalLM#_model_type.
---
# Module: [`easydel/modules/mosaic_mpt/modeling_mosaic.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py)

## Classes
### `MptAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/mosaic_mpt/modeling_mosaic.py:144`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L144)
- doc: MPT Attention module with ALiBi positional bias.
- signature: `class MptAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: MptConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L161) — Initialize MPT attention with ALiBi support.
  - `_compute_alibi_bias(self, sequence_length)` — [`L263`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L263) — Compute ALiBi positional bias tensor.
  - `_create_attention_performer(self, config: MptConfig, rngs: nn.Rngs)` — [`L242`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L242) — Create attention performer with MPT-specific settings.
  - `define_network(self, config: MptConfig, dtype: jnp.dtype, param_dtype: jnp.dtype, precision: jax.lax.PrecisionLike, rngs: nn.Rngs)` — [`L192`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L192) — Define MPT-specific network with fused QKV projection.
  - `forward_alibi(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, alibi: Float[Array, "batch_or_1 heads qseq_len_or_1 kvseq_len_or_1"] | None = None)` — [`L275`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L275) — Forward pass with ALiBi positional bias and fused QKV projection.
  - `Wqkv` — [`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L212)
  - `out_proj` — [`L223`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L223)
  - `resid_dropout` — [`L234`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L234)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`config`](../../layers/attention/_flexible.md#AttentionModule.config), [`forward`](../../layers/attention/_flexible.md#FlexibleAttentionModule.forward), [`AttentionLayerOutput`](../../infra/modeling_outputs.md#AttentionLayerOutput), [`concatenate`](../../layers/attention/_flexible.md#AttentionModule.concatenate), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`attention_outputs`](../../operations/_attention_outputs.md#AttentionOutput.attention_outputs), [`attention_performer`](../../layers/attention/_unified.md#UnifiedAttention.attention_performer), [`shard_attention_prod`](../../layers/attention/_flexible.md#AttentionModule.shard_attention_prod), [`apply_qkv_shardings`](../../layers/attention/_flexible.md#AttentionModule.apply_qkv_shardings), [`attention_weights`](../../operations/_attention_outputs.md#AttentionOutput.attention_weights), [`MptConfig`](mosaic_configuration.md#MptConfig), [`attn_config`](mosaic_configuration.md#MptConfig.attn_config), [`causal`](../../layers/attention/_unified.md#UnifiedAttention.causal), [`_create_alibi_slopes`](../../layers/attention/_unified.md#UnifiedAttention._create_alibi_slopes), [`attn_pdrop`](mosaic_configuration.md#MptAttentionConfig.attn_pdrop), [`dtype`](../../layers/attention/_unified.md#UnifiedAttention.dtype), [`use_bias`](mosaic_configuration.md#MptConfig.use_bias), [`initializer_range`](mosaic_configuration.md#MptConfig.initializer_range), [`build_mpt_alibi_tensor`](modeling_mosaic.md#build_mpt_alibi_tensor), [`alibi_bias_max`](mosaic_configuration.md#MptAttentionConfig.alibi_bias_max), [`n_heads`](mosaic_configuration.md#MptConfig.n_heads), [`softmax_scale`](mosaic_configuration.md#MptAttentionConfig.softmax_scale)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_attention_performer`](../../layers/attention/_unified.md#UnifiedAttention._create_attention_performer), [`forward_alibi`](../../layers/attention/_unified.md#UnifiedAttention.forward_alibi), [`define_network`](../../layers/attention/_unified.md#UnifiedAttention.define_network), [`_compute_alibi_bias`](../../layers/attention/_unified.md#UnifiedAttention._compute_alibi_bias), [`attn`](modeling_mosaic.md#MptBlock.attn)

### `MptBlock`  ·  implements/extends Module
- def: [`easydel/modules/mosaic_mpt/modeling_mosaic.py:392`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L392)
- doc: MPT Transformer block.
- signature: `class MptBlock(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None, position_bias: Float[Array, "batch heads seq_len seq_len"] | None = None)` — [`L474`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L474) — Forward pass of the MptBlock.
  - `__init__(self, config: MptConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L412`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L412) — Initializes the MptBlock module.
  - `attn` — [`L445`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L445)
  - `config` — [`L431`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L431)
  - `dropout_rate` — [`L471`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L471)
  - `dtype` — [`L432`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L432)
  - `ffn` — [`L462`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L462)
  - `norm_1` — [`L437`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L437)
  - `norm_2` — [`L454`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L454)
  - `param_dtype` — [`L433`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L433)
  - `precision` — [`L434`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L434)
  - `resid_attn_dropout` — [`L472`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L472)
  - `rngs` — [`L435`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L435)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`MptConfig`](mosaic_configuration.md#MptConfig), [`attn_config`](mosaic_configuration.md#MptConfig.attn_config), [`attn_pdrop`](mosaic_configuration.md#MptAttentionConfig.attn_pdrop), [`MptAttention`](modeling_mosaic.md#MptAttention), [`layer_norm_epsilon`](mosaic_configuration.md#MptConfig.layer_norm_epsilon), [`use_norm_bias`](mosaic_configuration.md#MptConfig.use_norm_bias), [`MptMLP`](modeling_mosaic.md#MptMLP)
- used by: [`wte`](modeling_mosaic.md#MptModel.wte)

### `MptForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/mosaic_mpt/modeling_mosaic.py:806`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L806)
- doc: MPT model with a language modeling head for causal language modeling.
- signature: `class MptForCausalLM(BaseCausalLMModule[MptModel, MptConfig]):`
- members:
  - `__init__(self, config: MptConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L827`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L827) — Initialize the MPT causal language model.
- protocol/private: `_config_class`[`L825`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L825), `_model_type`[`L824`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L824), `_task_type`[`L823`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L823)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`MptConfig`](mosaic_configuration.md#MptConfig), [`MptModel`](modeling_mosaic.md#MptModel), [`use_bias`](mosaic_configuration.md#MptConfig.use_bias)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `MptMLP`  ·  implements/extends Module
- def: [`easydel/modules/mosaic_mpt/modeling_mosaic.py:51`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L51)
- doc: MPT MLP module.
- signature: `class MptMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], residual: Float[Array, "batch seq_len hidden_dim"])` — [`L110`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L110) — Forward pass of the MptMLP module.
  - `__init__(self, config: MptConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L67`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L67) — Initializes the MptMLP module.
  - `config` — [`L86`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L86)
  - `down_proj` — [`L100`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L100)
  - `hidden_dropout` — [`L105`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L105)
  - `up_proj` — [`L95`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L95)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`MptConfig`](mosaic_configuration.md#MptConfig), [`attn_config`](mosaic_configuration.md#MptConfig.attn_config), [`attn_pdrop`](mosaic_configuration.md#MptAttentionConfig.attn_pdrop), [`use_bias`](mosaic_configuration.md#MptConfig.use_bias), [`initializer_range`](mosaic_configuration.md#MptConfig.initializer_range), [`expansion_ratio`](mosaic_configuration.md#MptConfig.expansion_ratio)
- used by: [`ffn`](modeling_mosaic.md#MptBlock.ffn)

### `MptModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/mosaic_mpt/modeling_mosaic.py:576`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L576)
- doc: MPT model implementation.
- signature: `class MptModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L671`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L671) — Forward pass through the MPT transformer model.
  - `__init__(self, config: MptConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L596`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L596) — Initializes the MptModel.
  - `alibi(self)` — [`L659`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L659) — Compute and cache the ALiBi positional bias tensor.
  - `get_decoder(self)` — [`L785`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L785) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L798`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L798) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L778`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L778) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L791`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L791) — Returns the language model head of the module.
  - `blocks` — [`L635`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L635)
  - `norm_f` — [`L649`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L649)
  - `wte` — [`L621`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L621)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`MptConfig`](mosaic_configuration.md#MptConfig), [`layer_norm_epsilon`](mosaic_configuration.md#MptConfig.layer_norm_epsilon), [`use_norm_bias`](mosaic_configuration.md#MptConfig.use_norm_bias), [`build_mpt_alibi_tensor`](modeling_mosaic.md#build_mpt_alibi_tensor), [`MptBlock`](modeling_mosaic.md#MptBlock), [`d_model`](mosaic_configuration.md#MptConfig.d_model), [`gradient_checkpointing`](mosaic_configuration.md#MptConfig.gradient_checkpointing), [`vocab_size`](mosaic_configuration.md#MptConfig.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`MptForCausalLM`](modeling_mosaic.md#MptForCausalLM), [`__init__`](modeling_mosaic.md#MptForCausalLM.__init__)

## Functions
- `build_mpt_alibi_tensor(num_heads, sequence_length, alibi_bias_max=8)` — [`L528`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/modeling_mosaic.py#L528) — Builds the ALiBi tensor for MPT models.

