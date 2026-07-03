---
title: 'Module: easydel/modules/falcon/modeling_falcon.py'
type: catalog
provenance: extracted
module: easydel/modules/falcon/modeling_falcon.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.falcon.modeling_falcon`/
symbols:
  FalconBlock.__call__: FalconBlock#__call__().
  FalconModel.__call__: FalconModel#__call__().
  FalconBlock.input_layernorm: FalconBlock#input_layernorm.
  FalconModel.word_embeddings: FalconModel#word_embeddings.
  FalconBlock.ln_mlp: FalconBlock#ln_mlp.
  FalconBlock.config: FalconBlock#config.
  FalconAttention._create_fused_qkv_proj: FalconAttention#_create_fused_qkv_proj().
  FalconForCausalLM: FalconForCausalLM#
  FalconModel: FalconModel#
  FalconBlock.post_attention_layernorm: FalconBlock#post_attention_layernorm.
  FalconBlock.ln_attn: FalconBlock#ln_attn.
  FalconAttention._create_o_proj: FalconAttention#_create_o_proj().
  FalconAttention.__init__: FalconAttention#__init__().
  FalconMlp.__call__: FalconMlp#__call__().
  FalconMlp.config: FalconMlp#config.
  FalconAttention.projection_mapping: FalconAttention#projection_mapping.
  FalconMlp.dense_h_to_4h: FalconMlp#dense_h_to_4h.
  FalconMlp.dense_4h_to_h: FalconMlp#dense_4h_to_h.
  FalconModel.ln_f: FalconModel#ln_f.
  FalconMlp.rngs: FalconMlp#rngs.
  FalconBlock.rngs: FalconBlock#rngs.
  FalconForCausalLM.__init__: FalconForCausalLM#__init__().
  FalconBlock.dropout: FalconBlock#dropout.
  FalconBlock.dropout_mlp: FalconBlock#dropout_mlp.
  FalconBlock.dtype: FalconBlock#dtype.
  FalconBlock.param_dtype: FalconBlock#param_dtype.
  FalconModel.__init__: FalconModel#__init__().
  FalconForCausalLM._task_type: FalconForCausalLM#_task_type.
  FalconBlock.mlp: FalconBlock#mlp.
  FalconModel.h: FalconModel#h.
  FalconAttention: FalconAttention#
  FalconBlock.self_attention: FalconBlock#self_attention.
  FalconMlp.__init__: FalconMlp#__init__().
  FalconBlock.__init__: FalconBlock#__init__().
  FalconModel.get_embedding: FalconModel#get_embedding().
  FalconForCausalLM._config_class: FalconForCausalLM#_config_class.
  dropout_add: dropout_add().
  built_bloom_alibi: built_bloom_alibi().
  FalconMlp: FalconMlp#
  FalconBlock: FalconBlock#
  FalconMlp.dtype: FalconMlp#dtype.
  FalconMlp.param_dtype: FalconMlp#param_dtype.
  FalconMlp.precision: FalconMlp#precision.
  FalconBlock.precision: FalconBlock#precision.
  FalconModel.get_encoder: FalconModel#get_encoder().
  FalconModel.get_decoder: FalconModel#get_decoder().
  FalconModel.get_lm_head: FalconModel#get_lm_head().
  FalconForCausalLM._model_type: FalconForCausalLM#_model_type.
---
# Module: [`easydel/modules/falcon/modeling_falcon.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py)

## Classes
### `FalconAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/falcon/modeling_falcon.py:109`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L109)
- doc: Multi-head attention layer for Falcon models.
- signature: `class FalconAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: FalconConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L124`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L124) — Initialize Falcon attention layer with ALiBi or RoPE support.
  - `_create_fused_qkv_proj(self, config: FalconConfig, dtype: jnp.dtype, param_dtype: jnp.dtype, precision: jax.lax.PrecisionLike, rngs: nn.Rngs)` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L160) — Create the fused query-key-value projection layer. — documented in [easydel-layers-linears-_linear](../../../../concepts/easydel-layers-linears-_linear.md)
  - `_create_o_proj(self, config: FalconConfig, dtype: jnp.dtype, param_dtype: jnp.dtype, precision: jax.lax.PrecisionLike, rngs: nn.Rngs)` — [`L191`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L191) — Create the output projection layer. — documented in [easydel-layers-linears-_linear](../../../../concepts/easydel-layers-linears-_linear.md)
  - `projection_mapping` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L116)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`num_heads`](../../layers/attention/_unified.md#UnifiedAttention.num_heads), [`FalconConfig`](falcon_configuration.md#FalconConfig), [`projection_mapping`](../../layers/attention/_unified.md#UnifiedAttention.projection_mapping), [`num_key_value_heads`](../../layers/attention/_unified.md#UnifiedAttention.num_key_value_heads), [`hidden_size`](falcon_configuration.md#FalconConfig.hidden_size), [`bias`](falcon_configuration.md#FalconConfig.bias), [`num_attention_heads`](falcon_configuration.md#FalconConfig.num_attention_heads), [`alibi`](falcon_configuration.md#FalconConfig.alibi), [`multi_query`](falcon_configuration.md#FalconConfig.multi_query)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_o_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_o_proj), [`_create_fused_qkv_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_fused_qkv_proj), [`self_attention`](modeling_falcon.md#FalconBlock.self_attention)

### `FalconBlock`  ·  implements/extends Module
- def: [`easydel/modules/falcon/modeling_falcon.py:302`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L302)
- doc: Single decoder layer for Falcon models.
- signature: `class FalconBlock(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None, alibi: Array | None = None)` — [`L401`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L401) — Forward pass through the decoder layer.
  - `__init__(self, config: FalconConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L310`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L310) — Initialize Falcon decoder layer.
  - `config` — [`L331`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L331)
  - `dropout` — [`L398`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L398)
  - `dropout_mlp` — [`L399`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L399)
  - `dtype` — [`L332`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L332)
  - `input_layernorm` — [`L349`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L349)
  - `ln_attn` — [`L358`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L358) — documented in [easydel-layers-norms-_norms](../../../../concepts/easydel-layers-norms-_norms.md)
  - `ln_mlp` — [`L365`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L365) — documented in [easydel-layers-norms-_norms](../../../../concepts/easydel-layers-norms-_norms.md)
  - `mlp` — [`L381`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L381)
  - `param_dtype` — [`L333`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L333)
  - `post_attention_layernorm` — [`L342`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L342)
  - `precision` — [`L334`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L334)
  - `rngs` — [`L335`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L335)
  - `self_attention` — [`L389`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L389)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`FalconConfig`](falcon_configuration.md#FalconConfig), [`hidden_size`](falcon_configuration.md#FalconConfig.hidden_size), [`layer_norm_epsilon`](falcon_configuration.md#FalconConfig.layer_norm_epsilon), [`new_decoder_architecture`](falcon_configuration.md#FalconConfig.new_decoder_architecture), [`num_ln_in_parallel_attn`](falcon_configuration.md#FalconConfig.num_ln_in_parallel_attn), [`parallel_attn`](falcon_configuration.md#FalconConfig.parallel_attn), [`FalconAttention`](modeling_falcon.md#FalconAttention), [`dropout_add`](modeling_falcon.md#dropout_add), [`FalconMlp`](modeling_falcon.md#FalconMlp), [`attention_dropout`](falcon_configuration.md#FalconConfig.attention_dropout), [`hidden_dropout`](falcon_configuration.md#FalconConfig.hidden_dropout)
- used by: [`word_embeddings`](modeling_falcon.md#FalconModel.word_embeddings)

### `FalconForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/falcon/modeling_falcon.py:706`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L706)
- doc: Falcon model with a language modeling head for causal language modeling tasks.
- signature: `class FalconForCausalLM(BaseCausalLMModule[FalconModel, FalconConfig]):`
- members:
  - `__init__(self, config: FalconConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L723`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L723) — Initialize Falcon model for causal language modeling.
- protocol/private: `_config_class`[`L721`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L721), `_model_type`[`L720`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L720), `_task_type`[`L719`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L719)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`FalconConfig`](falcon_configuration.md#FalconConfig), [`FalconModel`](modeling_falcon.md#FalconModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `FalconMlp`  ·  implements/extends Module
- def: [`easydel/modules/falcon/modeling_falcon.py:223`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L223)
- doc: Multi-Layer Perceptron module for Falcon models.
- signature: `class FalconMlp(nn.Module):`
- members:
  - `__call__(self, x: Array, deterministic: bool = True)` — [`L275`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L275) — Apply GELU feedforward transformation.
  - `__init__(self, config: FalconConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L230`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L230) — Initialize Falcon MLP block.
  - `config` — [`L252`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L252)
  - `dense_4h_to_h` — [`L269`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L269)
  - `dense_h_to_4h` — [`L264`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L264)
  - `dtype` — [`L253`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L253)
  - `param_dtype` — [`L254`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L254)
  - `precision` — [`L255`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L255)
  - `rngs` — [`L256`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L256)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`FalconConfig`](falcon_configuration.md#FalconConfig), [`hidden_size`](falcon_configuration.md#FalconConfig.hidden_size), [`bias`](falcon_configuration.md#FalconConfig.bias), [`ff_factor`](falcon_configuration.md#FalconConfig.ff_factor)
- used by: [`mlp`](modeling_falcon.md#FalconBlock.mlp)

### `FalconModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/falcon/modeling_falcon.py:492`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L492)
- doc: Falcon model implementation.
- signature: `class FalconModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L565`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L565) — Performs forward pass through the Falcon transformer model.
  - `__init__(self, config: FalconConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L506`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L506) — Initialize Falcon base model.
  - `get_decoder(self)` — [`L685`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L685) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L698`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L698) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L678`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L678) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L691`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L691) — Returns the language model head of the module.
  - `h` — [`L544`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L544)
  - `ln_f` — [`L557`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L557)
  - `word_embeddings` — [`L531`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L531)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`FalconConfig`](falcon_configuration.md#FalconConfig), [`hidden_size`](falcon_configuration.md#FalconConfig.hidden_size), [`layer_norm_epsilon`](falcon_configuration.md#FalconConfig.layer_norm_epsilon), [`FalconBlock`](modeling_falcon.md#FalconBlock), [`built_bloom_alibi`](modeling_falcon.md#built_bloom_alibi), [`gradient_checkpointing`](falcon_configuration.md#FalconConfig.gradient_checkpointing), [`vocab_size`](falcon_configuration.md#FalconConfig.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`FalconForCausalLM`](modeling_falcon.md#FalconForCausalLM), [`__init__`](modeling_falcon.md#FalconForCausalLM.__init__)

## Functions
- `built_bloom_alibi(attention_mask, num_attention_heads)` — [`L51`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L51) — The built_bloom_alibi function is used to create a bloom alibi for the attention mask.
- `dropout_add(nn_drop: nn.Dropout, x: Array, residual: Array)` — [`L82`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon/modeling_falcon.py#L82) — The dropout_add function is a helper function that adds the residual to the output of

