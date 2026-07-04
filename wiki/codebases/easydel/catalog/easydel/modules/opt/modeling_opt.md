---
title: 'Module: easydel/modules/opt/modeling_opt.py'
type: catalog
provenance: extracted
module: easydel/modules/opt/modeling_opt.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.opt.modeling_opt`/OPT
symbols:
  OPTDecoder.__call__: Decoder#__call__().
  OPTAttention.__call__: Attention#__call__().
  OPTDecoderLayer.__call__: DecoderLayer#__call__().
  OPTModel.__call__: Model#__call__().
  OPTDecoder.final_layer_norm: Decoder#final_layer_norm.
  OPTForCausalLM: ForCausalLM#
  OPTForCausalLM.apply_lm_head: ForCausalLM#apply_lm_head().
  OPTDecoder.embed_tokens: Decoder#embed_tokens.
  OPTDecoder.project_out: Decoder#project_out.
  OPTDecoderLayer.embed_dim: DecoderLayer#embed_dim.
  OPTDecoderLayer.self_attn: DecoderLayer#self_attn.
  OPTDecoder.embed_positions: Decoder#embed_positions.
  OPTAttention.head_dim: Attention#head_dim.
  OPTLearnedPositionalEmbedding.__call__: LearnedPositionalEmbedding#__call__().
  OPTForCausalLM.__init__: ForCausalLM#__init__().
  OPTDecoderLayer.self_attn_layer_norm: DecoderLayer#self_attn_layer_norm.
  OPTDecoderLayer.final_layer_norm: DecoderLayer#final_layer_norm.
  OPTLearnedPositionalEmbedding.kernel: LearnedPositionalEmbedding#kernel.
  OPTDecoderLayer.do_layer_norm_before: DecoderLayer#do_layer_norm_before.
  OPTDecoderLayer.activation_fn: DecoderLayer#activation_fn.
  OPTDecoderLayer.fc1: DecoderLayer#fc1.
  OPTDecoderLayer.fc2: DecoderLayer#fc2.
  OPTModel.decoder: Model#decoder.
  OPTAttention._split_heads: Attention#_split_heads().
  OPTDecoder.project_in: Decoder#project_in.
  OPTForCausalLM.prepare_inputs_for_generation: ForCausalLM#prepare_inputs_for_generation().
  OPTDecoderLayer.dropout_layer: DecoderLayer#dropout_layer.
  OPTModel: Model#
  OPTAttention.attention_module: Attention#attention_module.
  OPTDecoderLayer.config: DecoderLayer#config.
  OPTDecoder.position_offset: Decoder#position_offset.
  OPTAttention.__init__: Attention#__init__().
  OPTDecoder.__init__: Decoder#__init__().
  OPTDecoder.padding_idx: Decoder#padding_idx.
  OPTDecoder.max_target_positions: Decoder#max_target_positions.
  OPTModel.__init__: Model#__init__().
  OPTModel.set_embeddings: Model#set_embeddings().
  OPTModel.get_embedding: Model#get_embedding().
  OPTForCausalLM._task_type: ForCausalLM#_task_type.
  OPTDecoder.layers: Decoder#layers.
  OPTAttention: Attention#
  OPTAttention._merge_heads: Attention#_merge_heads().
  OPTDecoder: Decoder#
  OPTAttention.dropout_layer: Attention#dropout_layer.
  OPTDecoderLayer.__init__: DecoderLayer#__init__().
  OPTDecoder.dropout_layer: Decoder#dropout_layer.
  OPTModel._get_decoder_module: Model#_get_decoder_module().
  OPTModel.get_decoder: Model#get_decoder().
  OPTForCausalLM._config_class: ForCausalLM#_config_class.
  OPTAttention.k_proj: Attention#k_proj.
  OPTAttention.v_proj: Attention#v_proj.
  OPTDecoderLayer.dtype: DecoderLayer#dtype.
  OPTLearnedPositionalEmbedding.dtype: LearnedPositionalEmbedding#dtype.
  OPTAttention.embed_dim: Attention#embed_dim.
  OPTAttention.num_heads: Attention#num_heads.
  OPTAttention.dropout: Attention#dropout.
  OPTAttention.causal: Attention#causal.
  OPTAttention.q_proj: Attention#q_proj.
  OPTAttention.out_proj: Attention#out_proj.
  OPTDecoderLayer: DecoderLayer#
  OPTLearnedPositionalEmbedding.offset: LearnedPositionalEmbedding#offset.
  OPTLearnedPositionalEmbedding.param_dtype: LearnedPositionalEmbedding#param_dtype.
  OPTAttention.config: Attention#config.
  OPTAttention.bias: Attention#bias.
  OPTAttention.dtype: Attention#dtype.
  OPTAttention.param_dtype: Attention#param_dtype.
  OPTAttention.precision: Attention#precision.
  OPTDecoderLayer.param_dtype: DecoderLayer#param_dtype.
  OPTDecoderLayer.precision: DecoderLayer#precision.
  OPTLearnedPositionalEmbedding: LearnedPositionalEmbedding#
  OPTLearnedPositionalEmbedding.__init__: LearnedPositionalEmbedding#__init__().
  OPTLearnedPositionalEmbedding.num_embeddings: LearnedPositionalEmbedding#num_embeddings.
  OPTLearnedPositionalEmbedding.features: LearnedPositionalEmbedding#features.
  OPTLearnedPositionalEmbedding.craft_sharding: LearnedPositionalEmbedding#craft_sharding().
  OPTForCausalLM._model_type: ForCausalLM#_model_type.
  OPTForCausalLM.update_inputs_for_generation: ForCausalLM#update_inputs_for_generation().
---
# Module: [`easydel/modules/opt/modeling_opt.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py)

## Classes
### `OPTAttention`  ·  implements/extends AttentionModule
- def: [`easydel/modules/opt/modeling_opt.py:68`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L68)
- doc: OPT Attention mechanism module.
- signature: `class OPTAttention(AttentionModule):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, key_value_states: Array | None = None, output_attentions: bool = False)` — [`L185`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L185) — Forward pass of the OPTAttention module.
  - `__init__(self, config: OPTConfig, embed_dim: int, num_heads: int, dropout: float = 0, causal: bool = False, bias: bool = True, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L92`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L92) — Initializes the OPTAttention module.
  - `_merge_heads(self, hidden_states)` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L173) — Merges the attention heads back into a single hidden state tensor.
  - `_split_heads(self, hidden_states)` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L160) — Splits the hidden states into multiple attention heads.
  - `attention_module` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L158)
  - `bias` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L130)
  - `causal` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L129)
  - `config` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L125)
  - `dropout` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L128)
  - `dropout_layer` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L157)
  - `dtype` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L131)
  - `embed_dim` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L126)
  - `head_dim` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L135)
  - `k_proj` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L150)
  - `num_heads` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L127)
  - `out_proj` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L155)
  - `param_dtype` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L132)
  - `precision` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L133)
  - `q_proj` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L150)
  - `v_proj` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L150)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`forward`](../../layers/attention/_flexible.md#FlexibleAttentionModule.forward), [`AttentionLayerOutput`](../../infra/modeling_outputs.md#AttentionLayerOutput), [`concatenate`](../../layers/attention/_flexible.md#AttentionModule.concatenate), [`attention_outputs`](../../operations/_attention_outputs.md#AttentionOutput.attention_outputs), [`AttentionModule`](../../layers/attention/_flexible.md#AttentionModule), [`shard_attention_prod`](../../layers/attention/_flexible.md#AttentionModule.shard_attention_prod), [`apply_qkv_shardings`](../../layers/attention/_flexible.md#AttentionModule.apply_qkv_shardings), [`attention_weights`](../../operations/_attention_outputs.md#AttentionOutput.attention_weights), [`OPTConfig`](opt_configuration.md#OPTConfig), [`__init__`](../../layers/attention/_flexible.md#AttentionModule.__init__), [`init_std`](opt_configuration.md#OPTConfig.init_std)
- used by: [`AttentionModule`](../../layers/attention/_flexible.md#AttentionModule), [`_merge_heads`](../../layers/attention/_flexible.md#AttentionModule._merge_heads), [`self_attn`](modeling_opt.md#OPTDecoderLayer.self_attn)

### `OPTDecoder`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/opt/modeling_opt.py:534`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L534)
- doc: OPT Decoder stack.
- signature: `class OPTDecoder(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"], attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool = False, output_hidden_states: bool = False)` — [`L671`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L671) — Performs forward pass through the OPT decoder stack.
  - `__init__(self, config: OPTConfig, offset: int = 2, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L559`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L559) — Initializes the OPTDecoder.
  - `dropout_layer` — [`L589`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L589)
  - `embed_positions` — [`L608`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L608)
  - `embed_tokens` — [`L595`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L595)
  - `final_layer_norm` — [`L642`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L642) — documented in [easydel-layers-norms-_norms](../../../../concepts/easydel-layers-norms-_norms.md)
  - `layers` — [`L658`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L658)
  - `max_target_positions` — [`L593`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L593)
  - `padding_idx` — [`L592`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L592)
  - `position_offset` — [`L604`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L604)
  - `project_in` — [`L618`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L618)
  - `project_out` — [`L627`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L627)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`views`](../../caching/transformer/cache.md#TransformerCache.views), `pad_token_id`, [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`dtype`](../../infra/base_module.md#EasyDeLBaseModule.dtype), [`OPTConfig`](opt_configuration.md#OPTConfig), [`init_std`](opt_configuration.md#OPTConfig.init_std), [`num_hidden_layers`](opt_configuration.md#OPTConfig.num_hidden_layers), [`OPTDecoderLayer`](modeling_opt.md#OPTDecoderLayer), [`gradient_checkpointing`](opt_configuration.md#OPTConfig.gradient_checkpointing), [`vocab_size`](opt_configuration.md#OPTConfig.vocab_size), [`word_embed_proj_dim`](opt_configuration.md#OPTConfig.word_embed_proj_dim)
- used by: [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`apply_lm_head`](modeling_opt.md#OPTForCausalLM.apply_lm_head), [`decoder`](modeling_opt.md#OPTModel.decoder), [`get_embedding`](modeling_opt.md#OPTModel.get_embedding), [`set_embeddings`](modeling_opt.md#OPTModel.set_embeddings)

### `OPTDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/opt/modeling_opt.py:263`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L263)
- doc: OPT Decoder Layer.
- signature: `class OPTDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False)` — [`L359`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L359) — Forward pass of the OPTDecoderLayer.
  - `__init__(self, config: OPTConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L286`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L286) — Initialize OPT decoder layer.
  - `activation_fn` — [`L324`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L324)
  - `config` — [`L306`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L306)
  - `do_layer_norm_before` — [`L322`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L322)
  - `dropout_layer` — [`L323`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L323)
  - `dtype` — [`L307`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L307)
  - `embed_dim` — [`L310`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L310)
  - `fc1` — [`L333`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L333)
  - `fc2` — [`L342`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L342)
  - `final_layer_norm` — [`L351`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L351)
  - `param_dtype` — [`L308`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L308)
  - `precision` — [`L309`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L309)
  - `self_attn` — [`L311`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L311)
  - `self_attn_layer_norm` — [`L326`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L326)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`OPTConfig`](opt_configuration.md#OPTConfig), [`init_std`](opt_configuration.md#OPTConfig.init_std), [`OPTAttention`](modeling_opt.md#OPTAttention), [`activation_function`](opt_configuration.md#OPTConfig.activation_function), [`attention_dropout`](opt_configuration.md#OPTConfig.attention_dropout), [`do_layer_norm_before`](opt_configuration.md#OPTConfig.do_layer_norm_before), [`dropout`](opt_configuration.md#OPTConfig.dropout), [`hidden_size`](opt_configuration.md#OPTConfig.hidden_size), [`num_attention_heads`](opt_configuration.md#OPTConfig.num_attention_heads)
- used by: [`final_layer_norm`](modeling_opt.md#OPTDecoder.final_layer_norm)

### `OPTForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/opt/modeling_opt.py:944`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L944)
- doc: OPT model with a causal language modeling head.
- signature: `class OPTForCausalLM(BaseCausalLMModule[OPTModel, OPTConfig]):`
- members:
  - `__init__(self, config: OPTConfig, offset: int = 2, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L969`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L969) — Initializes the OPTForCausalLM model.
  - `apply_lm_head(self, hidden_states: Array)` — [`L1013`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L1013) — Applies the language model head to project hidden states to vocabulary logits.
  - `prepare_inputs_for_generation(self, input_ids, max_length: int, pad_token_id: int, starts: int | None = None, shardings=None, attention_mask: Bool[Array, "batch seq_len"] | None = None)` — [`L1033`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L1033) — Prepares inputs for autoregressive text generation.
  - `update_inputs_for_generation(self, model_outputs, model_kwargs)` — [`L1092`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L1092) — Updates model inputs for the next generation step.
- protocol/private: `_config_class`[`L967`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L967), `_model_type`[`L966`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L966), `_task_type`[`L965`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L965)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`base_model`](../_base/_base_task_module.md#BaseTaskModule.base_model), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`init_cache`](../../infra/mixins/generation.md#EasyGenerationMixin.init_cache), [`OPTConfig`](opt_configuration.md#OPTConfig), [`embed_tokens`](modeling_opt.md#OPTDecoder.embed_tokens), [`embedding`](../../layers/embeddings/_embeddings.md#Embed.embedding), [`prepare_inputs_for_call`](../../infra/base_module.md#EasyDeLBaseModule.prepare_inputs_for_call), [`decoder`](modeling_opt.md#OPTModel.decoder), [`OPTModel`](modeling_opt.md#OPTModel), [`compute_prefill_length`](../../infra/mixins/generation.md#EasyGenerationMixin.compute_prefill_length), `tie_word_embeddings`
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`prepare_inputs_for_generation`](../../infra/mixins/generation.md#EasyGenerationMixin.prepare_inputs_for_generation), [`update_inputs_for_generation`](../../infra/mixins/generation.md#EasyGenerationMixin.update_inputs_for_generation), [`apply_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.apply_lm_head)

### `OPTLearnedPositionalEmbedding`  ·  implements/extends Module
- def: [`easydel/modules/opt/modeling_opt.py:446`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L446)
- doc: Learned positional embedding for OPT.
- signature: `class OPTLearnedPositionalEmbedding(nn.Module):`
- members:
  - `__call__(self, inputs: Array)` — [`L515`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L515) — Apply learned positional embeddings with offset.
  - `__init__(self, num_embeddings: int, features: int, *, offset: int = 2, dtype: jnp.dtype | None = None, param_dtype: jnp.dtype = jnp.float32, embedding_init=None, rngs: nn.Rngs)` — [`L456`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L456) — Initializes the OPTLearnedPositionalEmbedding module.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L506`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L506) — Return sharding specifications for positional embedding parameters.
  - `dtype` — [`L482`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L482)
  - `features` — [`L481`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L481)
  - `kernel` — [`L489`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L489)
  - `num_embeddings` — [`L480`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L480)
  - `offset` — [`L479`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L479)
  - `param_dtype` — [`L483`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L483)
- uses (calls/refs, reference-scoped): [`ArrayParam`](../../infra/utils.md#ArrayParam), [`bound`](../../infra/utils.md#ArrayParam.bound)

### `OPTModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/opt/modeling_opt.py:790`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L790)
- doc: OPT model implementation.
- signature: `class OPTModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"], attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool = False, output_hidden_states: bool = False)` — [`L856`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L856) — Performs forward pass through the OPT transformer model.
  - `__init__(self, config: OPTConfig, offset: int = 2, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L810`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L810) — Initializes the OPTModel.
  - `_get_decoder_module(self)` — [`L848`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L848) — Returns the decoder module.
  - `get_decoder(self)` — [`L934`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L934) — Returns the decoder part of the model.
  - `get_embedding(self)` — [`L926`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L926) — Gets the input embeddings from the model.
  - `set_embeddings(self, value)` — [`L918`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L918) — Sets the input embeddings for the model.
  - `decoder` — [`L839`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/modeling_opt.py#L839)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`last_hidden_state`](../../infra/modeling_outputs.md#BaseModelOutput.last_hidden_state), [`attentions`](../../infra/modeling_outputs.md#BaseModelOutput.attentions), [`hidden_states`](../../infra/modeling_outputs.md#BaseModelOutput.hidden_states), [`OPTConfig`](opt_configuration.md#OPTConfig), [`embed_tokens`](modeling_opt.md#OPTDecoder.embed_tokens), [`past_key_values`](../../infra/modeling_outputs.md#BaseModelOutput.past_key_values), [`OPTDecoder`](modeling_opt.md#OPTDecoder)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`OPTForCausalLM`](modeling_opt.md#OPTForCausalLM), [`apply_lm_head`](modeling_opt.md#OPTForCausalLM.apply_lm_head), [`__init__`](modeling_opt.md#OPTForCausalLM.__init__)

