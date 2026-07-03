---
title: 'Module: easydel/modules/phi/modeling_phi.py'
type: catalog
provenance: extracted
module: easydel/modules/phi/modeling_phi.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.phi.modeling_phi`/Phi
symbols:
  PhiDecoderLayer.__call__: DecoderLayer#__call__().
  PhiModel.__call__: Model#__call__().
  PhiForCausalLM.__call__: ForCausalLM#__call__().
  PhiForCausalLM: ForCausalLM#
  PhiModel: Model#
  PhiMLP.__call__: MLP#__call__().
  PhiModel.embed_dropout: Model#embed_dropout.
  PhiMLP.fc1: MLP#fc1.
  PhiMLP.fc2: MLP#fc2.
  PhiModel.embed_tokens: Model#embed_tokens.
  PhiMLP.act: MLP#act.
  PhiDecoderLayer.input_layernorm: DecoderLayer#input_layernorm.
  PhiModel.final_layernorm: Model#final_layernorm.
  PhiAttention._preprocess_qkv: Attention#_preprocess_qkv().
  PhiForCausalLM.__init__: ForCausalLM#__init__().
  PhiDecoderLayer.resid_dropout: DecoderLayer#resid_dropout.
  PhiModel.frequencies: Model#frequencies().
  PhiAttention.qk_layernorm: Attention#qk_layernorm.
  PhiAttention.rotary_emb_dim: Attention#rotary_emb_dim.
  PhiDecoderLayer.config: DecoderLayer#config.
  PhiModel.__init__: Model#__init__().
  PhiForCausalLM._task_type: ForCausalLM#_task_type.
  PhiDecoderLayer.mlp: DecoderLayer#mlp.
  PhiModel.layers: Model#layers.
  PhiAttention: Attention#
  PhiDecoderLayer.self_attn: DecoderLayer#self_attn.
  PhiMLP.config: MLP#config.
  PhiMLP.__init__: MLP#__init__().
  PhiAttention.__init__: Attention#__init__().
  PhiAttention.attention_dropout: Attention#attention_dropout.
  PhiAttention.partial_rotary_factor: Attention#partial_rotary_factor.
  PhiAttention._create_q_norm: Attention#_create_q_norm().
  PhiAttention._create_k_norm: Attention#_create_k_norm().
  PhiAttention._create_rotary: Attention#_create_rotary().
  PhiDecoderLayer.__init__: DecoderLayer#__init__().
  PhiModel.padding_idx: Model#padding_idx.
  PhiModel.vocab_size: Model#vocab_size.
  PhiModel.get_embedding: Model#get_embedding().
  PhiForCausalLM._config_class: ForCausalLM#_config_class.
  PhiMLP: MLP#
  PhiDecoderLayer: DecoderLayer#
  PhiMLP.layer_idx: MLP#layer_idx.
  PhiMLP.dtype: MLP#dtype.
  PhiMLP.param_dtype: MLP#param_dtype.
  PhiMLP.precision: MLP#precision.
  PhiMLP.rngs: MLP#rngs.
  PhiAttention.norms_mapping: Attention#norms_mapping.
  PhiAttention.projection_mapping: Attention#projection_mapping.
  PhiAttention.layer_idx: Attention#layer_idx.
  PhiAttention.is_causal: Attention#is_causal.
  PhiDecoderLayer.layer_idx: DecoderLayer#layer_idx.
  PhiDecoderLayer.dtype: DecoderLayer#dtype.
  PhiDecoderLayer.param_dtype: DecoderLayer#param_dtype.
  PhiDecoderLayer.precision: DecoderLayer#precision.
  PhiDecoderLayer.rngs: DecoderLayer#rngs.
  PhiModel.get_encoder: Model#get_encoder().
  PhiModel.get_decoder: Model#get_decoder().
  PhiModel.get_lm_head: Model#get_lm_head().
  PhiForCausalLM._model_type: ForCausalLM#_model_type.
  PhiForCausalLM.get_encoder: ForCausalLM#get_encoder().
  PhiForCausalLM.get_decoder: ForCausalLM#get_decoder().
  PhiForCausalLM.get_lm_head: ForCausalLM#get_lm_head().
  PhiForCausalLM.get_embedding: ForCausalLM#get_embedding().
---
# Module: [`easydel/modules/phi/modeling_phi.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py)

## Classes
### `PhiAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/phi/modeling_phi.py:132`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L132)
- doc: Multi-head attention layer with optional Q/K normalization for Phi models.
- signature: `class PhiAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: PhiConfig, layer_idx: int | None = None, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L152`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L152) — Initialize Phi attention layer with partial RoPE and optional Q/K normalization.
  - `_create_k_norm(self, config, dtype, param_dtype, rngs)` — [`L216`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L216) — Create key normalization layer.
  - `_create_q_norm(self, config, dtype, param_dtype, rngs)` — [`L192`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L192) — Create query normalization layer.
  - `_create_rotary(self, config, dtype)` — [`L240`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L240) — Create rotary position embedding for partial RoPE.
  - `_preprocess_qkv(self, query_states, key_states, value_states)` — [`L259`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L259) — Preprocess query, key, and value states before attention computation.
  - `attention_dropout` — [`L187`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L187)
  - `is_causal` — [`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L190)
  - `layer_idx` — [`L186`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L186)
  - `norms_mapping` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L141)
  - `partial_rotary_factor` — [`L188`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L188)
  - `projection_mapping` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L145)
  - `qk_layernorm` — [`L172`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L172)
  - `rotary_emb_dim` — [`L189`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L189)
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`get_basic_rope`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_rope), [`key_normalization`](../../layers/attention/_unified.md#UnifiedAttention.key_normalization), [`query_normalization`](../../layers/attention/_unified.md#UnifiedAttention.query_normalization), [`PhiConfig`](phi_configuration.md#PhiConfig), [`use_qk_norm`](../../layers/attention/_unified.md#UnifiedAttention.use_qk_norm), [`partial_rotary_factor`](phi_configuration.md#PhiConfig.partial_rotary_factor), [`qk_layernorm`](phi_configuration.md#PhiConfig.qk_layernorm), [`attention_dropout`](phi_configuration.md#PhiConfig.attention_dropout)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`_create_k_norm`](../../layers/attention/_unified.md#UnifiedAttention._create_k_norm), [`_create_q_norm`](../../layers/attention/_unified.md#UnifiedAttention._create_q_norm), [`_preprocess_qkv`](../../layers/attention/_unified.md#UnifiedAttention._preprocess_qkv), [`self_attn`](modeling_phi.md#PhiDecoderLayer.self_attn)

### `PhiDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/phi/modeling_phi.py:277`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L277)
- doc: Single decoder layer for Phi models.
- signature: `class PhiDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L338`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L338) — Forward pass through the decoder layer.
  - `__init__(self, config: PhiConfig, layer_idx: int | None = None, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L286`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L286) — Initialize Phi decoder layer.
  - `config` — [`L306`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L306)
  - `dtype` — [`L308`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L308)
  - `input_layernorm` — [`L329`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L329)
  - `layer_idx` — [`L307`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L307)
  - `mlp` — [`L321`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L321)
  - `param_dtype` — [`L309`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L309)
  - `precision` — [`L310`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L310)
  - `resid_dropout` — [`L336`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L336)
  - `rngs` — [`L311`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L311)
  - `self_attn` — [`L313`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L313)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`PhiConfig`](phi_configuration.md#PhiConfig), [`hidden_size`](phi_configuration.md#PhiConfig.hidden_size), [`PhiAttention`](modeling_phi.md#PhiAttention), [`layer_norm_eps`](phi_configuration.md#PhiConfig.layer_norm_eps), [`PhiMLP`](modeling_phi.md#PhiMLP), [`resid_pdrop`](phi_configuration.md#PhiConfig.resid_pdrop)
- used by: [`embed_dropout`](modeling_phi.md#PhiModel.embed_dropout)

### `PhiForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/phi/modeling_phi.py:663`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L663)
- doc: Phi model with a language modeling head for causal language modeling tasks.
- signature: `class PhiForCausalLM(BaseCausalLMModule[PhiModel, PhiConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True)` — [`L710`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L710) — Performs forward pass for causal language modeling with Phi.
  - `__init__(self, config: PhiConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L681`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L681) — Initialize Phi model for causal language modeling.
  - `get_decoder(self)` — [`L788`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L788) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L800`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L800) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L781`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L781) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L794`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L794) — Returns the language model head of the module.
- protocol/private: `_config_class`[`L679`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L679), `_model_type`[`L678`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L678), `_task_type`[`L677`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L677)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`CausalLMOutput`](../../infra/modeling_outputs.md#CausalLMOutput), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`compute_lm_logits`](../_base/causal_lm_module.md#BaseCausalLMModule.compute_lm_logits), [`PhiConfig`](phi_configuration.md#PhiConfig), [`PhiModel`](modeling_phi.md#PhiModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.get_lm_head)

### `PhiMLP`  ·  implements/extends Module
- def: [`easydel/modules/phi/modeling_phi.py:50`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L50)
- doc: Multi-Layer Perceptron module for Phi models.
- signature: `class PhiMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L106`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L106) — Apply feedforward transformation.
  - `__init__(self, config: PhiConfig, layer_idx: int | None = None, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L58`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L58) — Initialize Phi MLP block.
  - `act` — [`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L104)
  - `config` — [`L79`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L79)
  - `dtype` — [`L81`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L81)
  - `fc1` — [`L86`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L86)
  - `fc2` — [`L95`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L95)
  - `layer_idx` — [`L80`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L80)
  - `param_dtype` — [`L82`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L82)
  - `precision` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L83)
  - `rngs` — [`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L84)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`PhiConfig`](phi_configuration.md#PhiConfig), [`hidden_size`](phi_configuration.md#PhiConfig.hidden_size), [`initializer_range`](phi_configuration.md#PhiConfig.initializer_range), [`intermediate_size`](phi_configuration.md#PhiConfig.intermediate_size), [`hidden_act`](phi_configuration.md#PhiConfig.hidden_act)
- used by: [`mlp`](modeling_phi.md#PhiDecoderLayer.mlp)

### `PhiModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/phi/modeling_phi.py:415`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L415)
- doc: Phi model implementation.
- signature: `class PhiModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L509`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L509) — Performs a forward pass through the Phi transformer model.
  - `__init__(self, config: PhiConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L429`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L429) — Initialize Phi base model.
  - `frequencies(self)` — [`L493`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L493) — Compute rotary position embedding frequencies for partial RoPE.
  - `get_decoder(self)` — [`L642`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L642) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L655`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L655) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L635`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L635) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L648`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L648) — Returns the language model head of the module.
  - `embed_dropout` — [`L464`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L464)
  - `embed_tokens` — [`L457`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L457)
  - `final_layernorm` — [`L484`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L484)
  - `layers` — [`L471`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L471)
  - `padding_idx` — [`L454`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L454)
  - `vocab_size` — [`L455`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/modeling_phi.py#L455)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), `pad_token_id`, [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`get_basic_frequencies`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_frequencies), [`PhiConfig`](phi_configuration.md#PhiConfig), [`hidden_size`](phi_configuration.md#PhiConfig.hidden_size), [`layer_norm_eps`](phi_configuration.md#PhiConfig.layer_norm_eps), [`vocab_size`](phi_configuration.md#PhiConfig.vocab_size), [`PhiDecoderLayer`](modeling_phi.md#PhiDecoderLayer), [`embd_pdrop`](phi_configuration.md#PhiConfig.embd_pdrop), [`gradient_checkpointing`](phi_configuration.md#PhiConfig.gradient_checkpointing)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`PhiForCausalLM`](modeling_phi.md#PhiForCausalLM), [`__init__`](modeling_phi.md#PhiForCausalLM.__init__)

