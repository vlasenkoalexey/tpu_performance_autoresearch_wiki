---
title: 'Module: easydel/modules/gpt_neox/modeling_gpt_neox.py'
type: catalog
provenance: extracted
module: easydel/modules/gpt_neox/modeling_gpt_neox.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.gpt_neox.modeling_gpt_neox`/GPTNeoX
symbols:
  GPTNeoXModel.__call__: Model#__call__().
  GPTNeoXBlock.__call__: Block#__call__().
  GPTNeoXForCausalLM: ForCausalLM#
  GPTNeoXModel: Model#
  GPTNeoXModel.emb_dropout: Model#emb_dropout.
  GPTNeoXAttention._create_rotary: Attention#_create_rotary().
  GPTNeoXMlp.__call__: Mlp#__call__().
  GPTNeoXMlp.dense_h_to_4h: Mlp#dense_h_to_4h.
  GPTNeoXMlp.dense_4h_to_h: Mlp#dense_4h_to_h.
  GPTNeoXModel.final_layer_norm: Model#final_layer_norm.
  GPTNeoXAttention._create_attention_performer: Attention#_create_attention_performer().
  GPTNeoXBlock.post_attention_layernorm: Block#post_attention_layernorm.
  GPTNeoXMlp.act: Mlp#act.
  GPTNeoXBlock.input_layernorm: Block#input_layernorm.
  GPTNeoXForCausalLM.__init__: ForCausalLM#__init__().
  GPTNeoXMlp.config: Mlp#config.
  GPTNeoXModel.embed_in: Model#embed_in.
  GPTNeoXModel.frequencies: Model#frequencies().
  GPTNeoXAttention.__init__: Attention#__init__().
  GPTNeoXModel.__init__: Model#__init__().
  GPTNeoXForCausalLM._task_type: ForCausalLM#_task_type.
  GPTNeoXBlock.mlp: Block#mlp.
  GPTNeoXModel.layers: Model#layers.
  GPTNeoXAttention: Attention#
  GPTNeoXBlock.use_parallel_residual: Block#use_parallel_residual.
  GPTNeoXBlock.attention: Block#attention.
  GPTNeoXMlp.__init__: Mlp#__init__().
  GPTNeoXBlock.__init__: Block#__init__().
  GPTNeoXModel.get_embedding: Model#get_embedding().
  GPTNeoXForCausalLM._config_class: ForCausalLM#_config_class.
  GPTNeoXMlp: Mlp#
  GPTNeoXBlock: Block#
  GPTNeoXAttention.projection_mapping: Attention#projection_mapping.
  GPTNeoXMlp.dtype: Mlp#dtype.
  GPTNeoXMlp.param_dtype: Mlp#param_dtype.
  GPTNeoXMlp.precision: Mlp#precision.
  GPTNeoXBlock.config: Block#config.
  GPTNeoXBlock.dtype: Block#dtype.
  GPTNeoXBlock.param_dtype: Block#param_dtype.
  GPTNeoXBlock.precision: Block#precision.
  GPTNeoXBlock.rngs: Block#rngs.
  GPTNeoXModel.get_encoder: Model#get_encoder().
  GPTNeoXModel.get_decoder: Model#get_decoder().
  GPTNeoXModel.get_lm_head: Model#get_lm_head().
  GPTNeoXForCausalLM._model_type: ForCausalLM#_model_type.
---
# Module: [`easydel/modules/gpt_neox/modeling_gpt_neox.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py)

## Classes
### `GPTNeoXAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/gpt_neox/modeling_gpt_neox.py:50`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L50)
- doc: GPT-NeoX Attention module with partial Rotary Position Embeddings (RoPE).
- signature: `class GPTNeoXAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: GPTNeoXConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L88`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L88) — Initialize GPT-NeoX attention module.
  - `_create_attention_performer(self, config: GPTNeoXConfig, rngs: nn.Rngs)` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L141) — Create the attention performer with GPT-NeoX specific settings.
  - `_create_rotary(self, config: GPTNeoXConfig, dtype: jnp.dtype)` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L120) — Create GPT-NeoX specific rotary embedding with partial RoPE.
  - `projection_mapping` — [`L72`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L72)
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`get_basic_rope`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_rope), [`GPTNeoXConfig`](gpt_neox_configuration.md#GPTNeoXConfig), [`attention_dropout`](gpt_neox_configuration.md#GPTNeoXConfig.attention_dropout), [`rotary_emb_base`](gpt_neox_configuration.md#GPTNeoXConfig.rotary_emb_base), [`rotary_pct`](gpt_neox_configuration.md#GPTNeoXConfig.rotary_pct)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_attention_performer`](../../layers/attention/_unified.md#UnifiedAttention._create_attention_performer), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`attention`](modeling_gpt_neox.md#GPTNeoXBlock.attention)

### `GPTNeoXBlock`  ·  implements/extends Module
- def: [`easydel/modules/gpt_neox/modeling_gpt_neox.py:250`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L250)
- doc: GPT-NeoX Transformer block.
- signature: `class GPTNeoXBlock(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L335`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L335) — Forward pass of the GPTNeoXBlock module.
  - `__init__(self, config: GPTNeoXConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L277`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L277) — Initialize GPT-NeoX transformer block.
  - `attention` — [`L318`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L318)
  - `config` — [`L297`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L297)
  - `dtype` — [`L298`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L298)
  - `input_layernorm` — [`L304`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L304)
  - `mlp` — [`L326`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L326)
  - `param_dtype` — [`L299`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L299)
  - `post_attention_layernorm` — [`L311`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L311)
  - `precision` — [`L300`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L300)
  - `rngs` — [`L301`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L301)
  - `use_parallel_residual` — [`L302`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L302)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`GPTNeoXConfig`](gpt_neox_configuration.md#GPTNeoXConfig), [`hidden_size`](gpt_neox_configuration.md#GPTNeoXConfig.hidden_size), [`GPTNeoXAttention`](modeling_gpt_neox.md#GPTNeoXAttention), [`layer_norm_eps`](gpt_neox_configuration.md#GPTNeoXConfig.layer_norm_eps), [`GPTNeoXMlp`](modeling_gpt_neox.md#GPTNeoXMlp), [`use_parallel_residual`](gpt_neox_configuration.md#GPTNeoXConfig.use_parallel_residual)
- used by: [`emb_dropout`](modeling_gpt_neox.md#GPTNeoXModel.emb_dropout)

### `GPTNeoXForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/gpt_neox/modeling_gpt_neox.py:650`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L650)
- doc: GPT-NeoX model with a language modeling head for autoregressive text generation.
- signature: `class GPTNeoXForCausalLM(BaseCausalLMModule[GPTNeoXModel, GPTNeoXConfig]):`
- members:
  - `__init__(self, config: GPTNeoXConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L673`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L673) — Initialize GPT-NeoX for causal language modeling.
- protocol/private: `_config_class`[`L671`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L671), `_model_type`[`L670`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L670), `_task_type`[`L669`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L669)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`GPTNeoXConfig`](gpt_neox_configuration.md#GPTNeoXConfig), [`GPTNeoXModel`](modeling_gpt_neox.md#GPTNeoXModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `GPTNeoXMlp`  ·  implements/extends Module
- def: [`easydel/modules/gpt_neox/modeling_gpt_neox.py:159`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L159)
- doc: GPT-NeoX MLP (Feed-Forward Network) module.
- signature: `class GPTNeoXMlp(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L221`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L221) — Forward pass of the GPTNeoXMlp module.
  - `__init__(self, config: GPTNeoXConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L179) — Initialize GPT-NeoX MLP module.
  - `act` — [`L219`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L219)
  - `config` — [`L199`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L199)
  - `dense_4h_to_h` — [`L211`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L211)
  - `dense_h_to_4h` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L203)
  - `dtype` — [`L200`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L200)
  - `param_dtype` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L201)
  - `precision` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L202)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`GPTNeoXConfig`](gpt_neox_configuration.md#GPTNeoXConfig), [`hidden_size`](gpt_neox_configuration.md#GPTNeoXConfig.hidden_size), [`intermediate_size`](gpt_neox_configuration.md#GPTNeoXConfig.intermediate_size), [`hidden_act`](gpt_neox_configuration.md#GPTNeoXConfig.hidden_act)
- used by: [`mlp`](modeling_gpt_neox.md#GPTNeoXBlock.mlp)

### `GPTNeoXModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/gpt_neox/modeling_gpt_neox.py:395`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L395)
- doc: GPT-NeoX base transformer model.
- signature: `class GPTNeoXModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, extra_embedding: Float[Array, "batch seq_len hidden_dim"] | None = None, output_attentions: bool = False, output_hidden_states: bool = False)` — [`L499`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L499) — Performs forward pass through the GPT-NeoX transformer model.
  - `__init__(self, config: GPTNeoXConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L420`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L420) — Initialize GPT-NeoX base model.
  - `frequencies(self)` — [`L481`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L481) — Compute and cache the rotary position embedding frequencies.
  - `get_decoder(self)` — [`L629`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L629) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L642`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L642) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L622`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L622) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L635`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L635) — Returns the language model head of the module.
  - `emb_dropout` — [`L452`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L452)
  - `embed_in` — [`L445`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L445)
  - `final_layer_norm` — [`L472`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L472) — documented in [easydel-layers-norms-_norms](../../../../concepts/easydel-layers-norms-_norms.md)
  - `layers` — [`L459`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/modeling_gpt_neox.py#L459)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`dtype`](../../infra/base_module.md#EasyDeLBaseModule.dtype), [`get_basic_frequencies`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_frequencies), [`GPTNeoXConfig`](gpt_neox_configuration.md#GPTNeoXConfig), [`hidden_size`](gpt_neox_configuration.md#GPTNeoXConfig.hidden_size), [`num_hidden_layers`](gpt_neox_configuration.md#GPTNeoXConfig.num_hidden_layers), [`GPTNeoXBlock`](modeling_gpt_neox.md#GPTNeoXBlock), [`gradient_checkpointing`](gpt_neox_configuration.md#GPTNeoXConfig.gradient_checkpointing), [`hidden_dropout`](gpt_neox_configuration.md#GPTNeoXConfig.hidden_dropout)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`GPTNeoXForCausalLM`](modeling_gpt_neox.md#GPTNeoXForCausalLM), [`__init__`](modeling_gpt_neox.md#GPTNeoXForCausalLM.__init__)

