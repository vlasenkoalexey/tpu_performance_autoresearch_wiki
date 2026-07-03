---
title: 'Module: easydel/modules/phimoe/modeling_phimoe.py'
type: catalog
provenance: extracted
module: easydel/modules/phimoe/modeling_phimoe.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.phimoe.modeling_phimoe`/PhiMo
symbols:
  PhiMoeModel.__call__: eModel#__call__().
  PhiMoeDecoderLayer.__call__: eDecoderLayer#__call__().
  PhiMoeSparseMoeBlock.__call__: eSparseMoeBlock#__call__().
  PhiMoeForCausalLM.__call__: eForCausalLM#__call__().
  PhiMoeForCausalLM: eForCausalLM#
  PhiMoeModel: eModel#
  PhiMoEBlockSparseTop2MLP.precision: EBlockSparseTop2MLP#precision.
  PhiMoEAttention.__init__: EAttention#__init__().
  PhiMoeModel.embed_dropout: eModel#embed_dropout.
  PhiMoeSparseMoeBlock.gate: eSparseMoeBlock#gate.
  PhiMoEBlockSparseTop2MLP.__call__: EBlockSparseTop2MLP#__call__().
  PhiMoeForCausalLM.__init__: eForCausalLM#__init__().
  PhiMoeSparseMoeBlock.experts: eSparseMoeBlock#experts.
  PhiMoeModel.embed_tokens: eModel#embed_tokens.
  PhiMoEBlockSparseTop2MLP.act_fn: EBlockSparseTop2MLP#act_fn.
  PhiMoeDecoderLayer.input_layernorm: eDecoderLayer#input_layernorm.
  PhiMoeDecoderLayer.post_attention_layernorm: eDecoderLayer#post_attention_layernorm.
  PhiMoeModel.norm: eModel#norm.
  PhiMoeSparseMoeBlock.config: eSparseMoeBlock#config.
  PhiMoeModel.__init__: eModel#__init__().
  PhiMoeForCausalLM._task_type: eForCausalLM#_task_type.
  PhiMoeModel.layers: eModel#layers.
  PhiMoEAttention: EAttention#
  PhiMoeSparseMoeBlock.router_jitter_noise: eSparseMoeBlock#router_jitter_noise.
  PhiMoeDecoderLayer.self_attn: eDecoderLayer#self_attn.
  PhiMoeDecoderLayer.block_sparse_moe: eDecoderLayer#block_sparse_moe.
  PhiMoEBlockSparseTop2MLP.__init__: EBlockSparseTop2MLP#__init__().
  PhiMoeSparseMoeBlock.__init__: eSparseMoeBlock#__init__().
  PhiMoeSparseMoeBlock.hidden_dim: eSparseMoeBlock#hidden_dim.
  PhiMoeSparseMoeBlock.ffn_dim: eSparseMoeBlock#ffn_dim.
  PhiMoeSparseMoeBlock.num_experts: eSparseMoeBlock#num_experts.
  PhiMoeSparseMoeBlock.top_k: eSparseMoeBlock#top_k.
  PhiMoeSparseMoeBlock.input_jitter_noise: eSparseMoeBlock#input_jitter_noise.
  PhiMoeDecoderLayer.__init__: eDecoderLayer#__init__().
  PhiMoeDecoderLayer.precision: eDecoderLayer#precision.
  PhiMoeModel.padding_idx: eModel#padding_idx.
  PhiMoeModel.vocab_size: eModel#vocab_size.
  PhiMoeModel.get_embedding: eModel#get_embedding().
  PhiMoeForCausalLM._config_class: eForCausalLM#_config_class.
  PhiMoeSparseMoeBlock.dtype: eSparseMoeBlock#dtype.
  PhiMoEBlockSparseTop2MLP: EBlockSparseTop2MLP#
  PhiMoEBlockSparseTop2MLP.config: EBlockSparseTop2MLP#config.
  PhiMoEBlockSparseTop2MLP.w1: EBlockSparseTop2MLP#w1.
  PhiMoEBlockSparseTop2MLP.w2: EBlockSparseTop2MLP#w2.
  PhiMoEBlockSparseTop2MLP.w3: EBlockSparseTop2MLP#w3.
  PhiMoeSparseMoeBlock: eSparseMoeBlock#
  PhiMoeSparseMoeBlock._sparsemixer_eval: eSparseMoeBlock#_sparsemixer_eval().
  PhiMoeDecoderLayer: eDecoderLayer#
  PhiMoeDecoderLayer.config: eDecoderLayer#config.
  PhiMoEBlockSparseTop2MLP.dtype: EBlockSparseTop2MLP#dtype.
  PhiMoEBlockSparseTop2MLP.param_dtype: EBlockSparseTop2MLP#param_dtype.
  PhiMoeSparseMoeBlock.layer_idx: eSparseMoeBlock#layer_idx.
  PhiMoeSparseMoeBlock.param_dtype: eSparseMoeBlock#param_dtype.
  PhiMoeSparseMoeBlock.precision: eSparseMoeBlock#precision.
  PhiMoeDecoderLayer.dtype: eDecoderLayer#dtype.
  PhiMoeDecoderLayer.param_dtype: eDecoderLayer#param_dtype.
  PhiMoeDecoderLayer.reform_param: eDecoderLayer#reform_param.
  PhiMoeModel.get_encoder: eModel#get_encoder().
  PhiMoeModel.get_decoder: eModel#get_decoder().
  PhiMoeModel.get_lm_head: eModel#get_lm_head().
  PhiMoeForCausalLM._model_type: eForCausalLM#_model_type.
  PhiMoeForCausalLM.get_encoder: eForCausalLM#get_encoder().
  PhiMoeForCausalLM.get_decoder: eForCausalLM#get_decoder().
  PhiMoeForCausalLM.get_lm_head: eForCausalLM#get_lm_head().
  PhiMoeForCausalLM.get_embedding: eForCausalLM#get_embedding().
---
# Module: [`easydel/modules/phimoe/modeling_phimoe.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py)

## Classes
### `PhiMoEAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/phimoe/modeling_phimoe.py:123`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L123)
- doc: PhiMoE Attention module with sliding window support.
- signature: `class PhiMoEAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: PhiMoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L132) — Initialize PhiMoE attention with sliding window configuration.
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`PhiMoeConfig`](phimoe_configuration.md#PhiMoeConfig), [`attn_dtype`](../../infra/base_config.md#EasyDeLBaseConfig.attn_dtype), [`attn_softmax_dtype`](../../infra/base_config.md#EasyDeLBaseConfig.attn_softmax_dtype), [`sliding_window`](phimoe_configuration.md#PhiMoeConfig.sliding_window)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`self_attn`](modeling_phimoe.md#PhiMoeDecoderLayer.self_attn)

### `PhiMoEBlockSparseTop2MLP`  ·  implements/extends Module
- def: [`easydel/modules/phimoe/modeling_phimoe.py:49`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L49)
- doc: Expert MLP module for PhiMoE Sparse Mixture of Experts.
- signature: `class PhiMoEBlockSparseTop2MLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Array)` — [`L106`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L106) — Apply SwiGLU feedforward transformation for expert processing.
  - `__init__(self, config: PhiMoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L57`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L57) — Initialize PhiMoE expert MLP block.
  - `act_fn` — [`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L104)
  - `config` — [`L76`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L76)
  - `dtype` — [`L77`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L77)
  - `param_dtype` — [`L78`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L78)
  - `precision` — [`L79`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L79)
  - `w1` — [`L101`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L101)
  - `w2` — [`L102`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L102)
  - `w3` — [`L103`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L103)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`PhiMoeConfig`](phimoe_configuration.md#PhiMoeConfig), [`hidden_size`](phimoe_configuration.md#PhiMoeConfig.hidden_size), [`initializer_range`](phimoe_configuration.md#PhiMoeConfig.initializer_range), [`intermediate_size`](phimoe_configuration.md#PhiMoeConfig.intermediate_size), [`hidden_act`](phimoe_configuration.md#PhiMoeConfig.hidden_act)
- used by: [`experts`](modeling_phimoe.md#PhiMoeSparseMoeBlock.experts)

### `PhiMoeDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/phimoe/modeling_phimoe.py:326`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L326)
- doc: Single decoder layer for PhiMoE models.
- signature: `class PhiMoeDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, output_router_logits: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L425`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L425) — Forward pass through the decoder layer.
  - `__init__(self, config: PhiMoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L333`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L333) — Initialize PhiMoE decoder layer.
  - `block_sparse_moe` — [`L401`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L401)
  - `config` — [`L353`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L353)
  - `dtype` — [`L354`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L354)
  - `input_layernorm` — [`L409`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L409)
  - `param_dtype` — [`L355`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L355)
  - `post_attention_layernorm` — [`L417`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L417)
  - `precision` — [`L356`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L356)
  - `reform_param` — [`L385`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L385)
  - `self_attn` — [`L393`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L393)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`PhiMoeConfig`](phimoe_configuration.md#PhiMoeConfig), [`hidden_size`](phimoe_configuration.md#PhiMoeConfig.hidden_size), [`num_local_experts`](phimoe_configuration.md#PhiMoeConfig.num_local_experts), [`PhiMoEAttention`](modeling_phimoe.md#PhiMoEAttention), [`rms_norm_eps`](phimoe_configuration.md#PhiMoeConfig.rms_norm_eps), [`PhiMoeSparseMoeBlock`](modeling_phimoe.md#PhiMoeSparseMoeBlock)
- used by: [`embed_dropout`](modeling_phimoe.md#PhiMoeModel.embed_dropout)

### `PhiMoeForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/phimoe/modeling_phimoe.py:729`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L729)
- doc: PhiMoE model with a language modeling head for causal language modeling tasks.
- signature: `class PhiMoeForCausalLM(BaseCausalLMModule[PhiMoeModel, PhiMoeConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_router_logits: bool | None = None)` — [`L775`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L775) — Forward pass through the PhiMoE causal language model.
  - `__init__(self, config: PhiMoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L746`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L746) — Initialize PhiMoE model for causal language modeling.
  - `get_decoder(self)` — [`L853`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L853) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L865`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L865) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L846`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L846) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L859`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L859) — Returns the language model head of the module.
- protocol/private: `_config_class`[`L744`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L744), `_model_type`[`L743`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L743), `_task_type`[`L742`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L742)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`CausalLMOutput`](../../infra/modeling_outputs.md#CausalLMOutput), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`compute_lm_logits`](../_base/causal_lm_module.md#BaseCausalLMModule.compute_lm_logits), [`PhiMoeConfig`](phimoe_configuration.md#PhiMoeConfig), [`PhiMoeModel`](modeling_phimoe.md#PhiMoeModel), [`lm_head_bias`](phimoe_configuration.md#PhiMoeConfig.lm_head_bias)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.get_lm_head)

### `PhiMoeModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/phimoe/modeling_phimoe.py:499`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L499)
- doc: The base PhiMoE model transformer.
- signature: `class PhiMoeModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None)` — [`L578`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L578) — Forward pass through the PhiMoE base model.
  - `__init__(self, config: PhiMoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L514`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L514) — Initialize PhiMoE base model.
  - `get_decoder(self)` — [`L708`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L708) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L721`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L721) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L701`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L701) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L714`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L714) — Returns the language model head of the module.
  - `embed_dropout` — [`L550`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L550)
  - `embed_tokens` — [`L542`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L542)
  - `layers` — [`L557`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L557)
  - `norm` — [`L570`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L570)
  - `padding_idx` — [`L539`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L539)
  - `vocab_size` — [`L540`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L540)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), `pad_token_id`, [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`PhiMoeConfig`](phimoe_configuration.md#PhiMoeConfig), [`hidden_size`](phimoe_configuration.md#PhiMoeConfig.hidden_size), [`rms_norm_eps`](phimoe_configuration.md#PhiMoeConfig.rms_norm_eps), [`vocab_size`](phimoe_configuration.md#PhiMoeConfig.vocab_size), [`PhiMoeDecoderLayer`](modeling_phimoe.md#PhiMoeDecoderLayer), [`embd_pdrop`](phimoe_configuration.md#PhiMoeConfig.embd_pdrop), [`gradient_checkpointing`](phimoe_configuration.md#PhiMoeConfig.gradient_checkpointing)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`PhiMoeForCausalLM`](modeling_phimoe.md#PhiMoeForCausalLM), [`__init__`](modeling_phimoe.md#PhiMoeForCausalLM.__init__)

### `PhiMoeSparseMoeBlock`  ·  implements/extends Module
- def: [`easydel/modules/phimoe/modeling_phimoe.py:173`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L173)
- doc: Sparse Mixture of Experts block for PhiMoE models.
- signature: `class PhiMoeSparseMoeBlock(nn.Module):`
- members:
  - `__call__(self, hidden_states: Array, deterministic: bool = True)` — [`L237`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L237) — Forward pass through the Sparse MoE block.
  - `__init__(self, config: PhiMoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L181) — Initialize PhiMoE Sparse MoE block.
  - `config` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L202)
  - `dtype` — [`L204`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L204)
  - `experts` — [`L224`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L224)
  - `ffn_dim` — [`L208`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L208)
  - `gate` — [`L213`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L213)
  - `hidden_dim` — [`L207`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L207)
  - `input_jitter_noise` — [`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L212)
  - `layer_idx` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L203)
  - `num_experts` — [`L209`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L209)
  - `param_dtype` — [`L205`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L205)
  - `precision` — [`L206`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L206)
  - `router_jitter_noise` — [`L211`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L211)
  - `top_k` — [`L210`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L210)
- protocol/private: `_sparsemixer_eval`[`L265`](../../../../../../../raw/code/EasyDeL/easydel/modules/phimoe/modeling_phimoe.py#L265)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`PhiMoeConfig`](phimoe_configuration.md#PhiMoeConfig), [`hidden_size`](phimoe_configuration.md#PhiMoeConfig.hidden_size), [`num_local_experts`](phimoe_configuration.md#PhiMoeConfig.num_local_experts), [`intermediate_size`](phimoe_configuration.md#PhiMoeConfig.intermediate_size), [`num_experts_per_tok`](phimoe_configuration.md#PhiMoeConfig.num_experts_per_tok), [`PhiMoEBlockSparseTop2MLP`](modeling_phimoe.md#PhiMoEBlockSparseTop2MLP), [`input_jitter_noise`](phimoe_configuration.md#PhiMoeConfig.input_jitter_noise), [`router_jitter_noise`](phimoe_configuration.md#PhiMoeConfig.router_jitter_noise)
- used by: [`block_sparse_moe`](modeling_phimoe.md#PhiMoeDecoderLayer.block_sparse_moe)

