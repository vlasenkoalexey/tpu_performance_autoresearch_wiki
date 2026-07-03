---
title: 'Module: easydel/modules/phi3/modeling_phi3.py'
type: catalog
provenance: extracted
module: easydel/modules/phi3/modeling_phi3.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.phi3.modeling_phi3`/Phi3
symbols:
  Phi3Attention.__call__: Attention#__call__().
  Phi3DecoderLayer.__call__: DecoderLayer#__call__().
  Phi3Model.__call__: Model#__call__().
  Phi3ForCausalLM.__call__: ForCausalLM#__call__().
  Phi3ForCausalLM: ForCausalLM#
  Phi3Model: Model#
  Phi3MLP.__call__: MLP#__call__().
  Phi3Model.embed_dropout: Model#embed_dropout.
  Phi3Attention._create_rotary: Attention#_create_rotary().
  Phi3DecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  Phi3Attention.define_network: Attention#define_network().
  Phi3Model.embed_tokens: Model#embed_tokens.
  Phi3MLP.activation_fn: MLP#activation_fn.
  Phi3Attention.qkv_proj: Attention#qkv_proj.
  Phi3DecoderLayer.input_layernorm: DecoderLayer#input_layernorm.
  Phi3Model.norm: Model#norm.
  Phi3Attention.resid_dropout: Attention#resid_dropout.
  Phi3DecoderLayer.config: DecoderLayer#config.
  Phi3MLP.precision: MLP#precision.
  Phi3Attention.__init__: Attention#__init__().
  Phi3Attention.o_proj: Attention#o_proj.
  Phi3ForCausalLM.__init__: ForCausalLM#__init__().
  Phi3MLP.gate_up_proj: MLP#gate_up_proj.
  Phi3MLP.down_proj: MLP#down_proj.
  Phi3DecoderLayer.resid_attn_dropout: DecoderLayer#resid_attn_dropout.
  Phi3DecoderLayer.resid_mlp_dropout: DecoderLayer#resid_mlp_dropout.
  Phi3Model.frequencies: Model#frequencies().
  Phi3Attention.rotary: Attention#rotary.
  Phi3Model.__init__: Model#__init__().
  Phi3ForCausalLM._task_type: ForCausalLM#_task_type.
  Phi3DecoderLayer.mlp: DecoderLayer#mlp.
  Phi3Model.layers: Model#layers.
  Phi3Attention: Attention#
  Phi3DecoderLayer.self_attn: DecoderLayer#self_attn.
  Phi3MLP.config: MLP#config.
  Phi3MLP.__init__: MLP#__init__().
  Phi3DecoderLayer.__init__: DecoderLayer#__init__().
  Phi3Model.padding_idx: Model#padding_idx.
  Phi3Model.vocab_size: Model#vocab_size.
  Phi3Model.get_embedding: Model#get_embedding().
  Phi3ForCausalLM._config_class: ForCausalLM#_config_class.
  Phi3MLP: MLP#
  Phi3DecoderLayer: DecoderLayer#
  Phi3MLP.dtype: MLP#dtype.
  Phi3MLP.param_dtype: MLP#param_dtype.
  Phi3Attention.projection_mapping: Attention#projection_mapping.
  Phi3DecoderLayer.dtype: DecoderLayer#dtype.
  Phi3DecoderLayer.param_dtype: DecoderLayer#param_dtype.
  Phi3DecoderLayer.precision: DecoderLayer#precision.
  Phi3Model.get_encoder: Model#get_encoder().
  Phi3Model.get_decoder: Model#get_decoder().
  Phi3Model.get_lm_head: Model#get_lm_head().
  Phi3ForCausalLM._model_type: ForCausalLM#_model_type.
  Phi3ForCausalLM.get_encoder: ForCausalLM#get_encoder().
  Phi3ForCausalLM.get_decoder: ForCausalLM#get_decoder().
  Phi3ForCausalLM.get_lm_head: ForCausalLM#get_lm_head().
  Phi3ForCausalLM.get_embedding: ForCausalLM#get_embedding().
---
# Module: [`easydel/modules/phi3/modeling_phi3.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py)

## Classes
### `Phi3Attention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/phi3/modeling_phi3.py:142`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L142)
- doc: Multi-head attention layer with fused QKV projection for Phi-3 models.
- signature: `class Phi3Attention(UnifiedAttention):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L250`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L250) — Compute attention with fused QKV projection and optional sliding window. — documented in [easydel-layers-attention-_unified](../../../../concepts/easydel-layers-attention-_unified.md)
  - `__init__(self, config: Phi3Config, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L155) — Initialize Phi-3 attention layer with fused QKV projection and sliding window.
  - `_create_rotary(self, config: Phi3Config, dtype: jnp.dtype)` — [`L230`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L230) — Create rotary position embedding for Phi-3 attention.
  - `define_network(self, config: Phi3Config, dtype: jnp.dtype, param_dtype: jnp.dtype, precision: jax.lax.PrecisionLike, rngs: nn.Rngs)` — [`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L190) — Create fused QKV projection instead of separate Q/K/V projections.
  - `o_proj` — [`L222`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L222)
  - `projection_mapping` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L150)
  - `qkv_proj` — [`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L212)
  - `resid_dropout` — [`L226`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L226)
  - `rotary` — [`L224`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L224)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`_create_attention_performer`](../../layers/attention/_unified.md#UnifiedAttention._create_attention_performer), [`config`](../../layers/attention/_flexible.md#AttentionModule.config), [`forward`](../../layers/attention/_flexible.md#FlexibleAttentionModule.forward), [`AttentionLayerOutput`](../../infra/modeling_outputs.md#AttentionLayerOutput), [`concatenate`](../../layers/attention/_flexible.md#AttentionModule.concatenate), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`attention_outputs`](../../operations/_attention_outputs.md#AttentionOutput.attention_outputs), [`attention_performer`](../../layers/attention/_unified.md#UnifiedAttention.attention_performer), [`_create_o_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_o_proj), [`get_basic_rope`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_rope), [`shard_attention_prod`](../../layers/attention/_flexible.md#AttentionModule.shard_attention_prod), [`_merge_heads`](../../layers/attention/_unified.md#UnifiedAttention._merge_heads), [`apply_qkv_shardings`](../../layers/attention/_flexible.md#AttentionModule.apply_qkv_shardings), [`attention_weights`](../../operations/_attention_outputs.md#AttentionOutput.attention_weights), [`Phi3Config`](phi3_configuration.md#Phi3Config), [`output_projection`](../../layers/attention/_unified.md#UnifiedAttention.output_projection), [`_apply_rotary`](../../layers/attention/_unified.md#UnifiedAttention._apply_rotary), [`sliding_window`](../../layers/attention/_unified.md#UnifiedAttention.sliding_window), [`hidden_size`](phi3_configuration.md#Phi3Config.hidden_size), [`resid_pdrop`](phi3_configuration.md#Phi3Config.resid_pdrop), [`initializer_range`](phi3_configuration.md#Phi3Config.initializer_range), [`sliding_window`](phi3_configuration.md#Phi3Config.sliding_window), [`num_attention_heads`](phi3_configuration.md#Phi3Config.num_attention_heads), [`num_key_value_heads`](phi3_configuration.md#Phi3Config.num_key_value_heads), [`rope_theta`](phi3_configuration.md#Phi3Config.rope_theta)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`define_network`](../../layers/attention/_unified.md#UnifiedAttention.define_network), [`self_attn`](modeling_phi3.md#Phi3DecoderLayer.self_attn)

### `Phi3DecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/phi3/modeling_phi3.py:354`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L354)
- doc: Single decoder layer for Phi-3 models.
- signature: `class Phi3DecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L426`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L426) — Forward pass through the decoder layer.
  - `__init__(self, config: Phi3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L362`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L362) — Initialize Phi-3 decoder layer.
  - `config` — [`L382`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L382)
  - `dtype` — [`L383`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L383)
  - `input_layernorm` — [`L402`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L402)
  - `mlp` — [`L394`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L394)
  - `param_dtype` — [`L384`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L384)
  - `post_attention_layernorm` — [`L418`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L418) — documented in [easydel-layers-norms-_norms](../../../../concepts/easydel-layers-norms-_norms.md)
  - `precision` — [`L385`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L385)
  - `resid_attn_dropout` — [`L410`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L410)
  - `resid_mlp_dropout` — [`L414`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L414)
  - `self_attn` — [`L386`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L386)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`Phi3Config`](phi3_configuration.md#Phi3Config), [`hidden_size`](phi3_configuration.md#Phi3Config.hidden_size), [`resid_pdrop`](phi3_configuration.md#Phi3Config.resid_pdrop), [`Phi3Attention`](modeling_phi3.md#Phi3Attention), [`rms_norm_eps`](phi3_configuration.md#Phi3Config.rms_norm_eps), [`Phi3MLP`](modeling_phi3.md#Phi3MLP)
- used by: [`embed_dropout`](modeling_phi3.md#Phi3Model.embed_dropout)

### `Phi3ForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/phi3/modeling_phi3.py:748`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L748)
- doc: Phi-3 model with a language modeling head for causal language modeling tasks.
- signature: `class Phi3ForCausalLM(BaseCausalLMModule[Phi3Model, Phi3Config]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True)` — [`L795`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L795) — Performs forward pass for causal language modeling with Phi-3.
  - `__init__(self, config: Phi3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L766`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L766) — Initialize Phi-3 model for causal language modeling.
  - `get_decoder(self)` — [`L875`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L875) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L887`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L887) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L868`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L868) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L881`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L881) — Returns the language model head of the module.
- protocol/private: `_config_class`[`L764`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L764), `_model_type`[`L763`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L763), `_task_type`[`L762`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L762)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`CausalLMOutput`](../../infra/modeling_outputs.md#CausalLMOutput), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`compute_lm_logits`](../_base/causal_lm_module.md#BaseCausalLMModule.compute_lm_logits), [`Phi3Config`](phi3_configuration.md#Phi3Config), [`Phi3Model`](modeling_phi3.md#Phi3Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.get_lm_head)

### `Phi3MLP`  ·  implements/extends Module
- def: [`easydel/modules/phi3/modeling_phi3.py:50`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L50)
- doc: Multi-Layer Perceptron module for Phi-3 models.
- signature: `class Phi3MLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L113`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L113) — Apply gated feedforward transformation.
  - `__init__(self, config: Phi3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L58`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L58) — Initialize Phi-3 MLP block with gated activation.
  - `activation_fn` — [`L111`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L111)
  - `config` — [`L79`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L79)
  - `down_proj` — [`L106`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L106)
  - `dtype` — [`L80`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L80)
  - `gate_up_proj` — [`L101`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L101)
  - `param_dtype` — [`L81`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L81)
  - `precision` — [`L82`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L82)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`Phi3Config`](phi3_configuration.md#Phi3Config), [`hidden_size`](phi3_configuration.md#Phi3Config.hidden_size), [`initializer_range`](phi3_configuration.md#Phi3Config.initializer_range), [`intermediate_size`](phi3_configuration.md#Phi3Config.intermediate_size), [`hidden_act`](phi3_configuration.md#Phi3Config.hidden_act)
- used by: [`mlp`](modeling_phi3.md#Phi3DecoderLayer.mlp)

### `Phi3Model`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/phi3/modeling_phi3.py:503`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L503)
- doc: Phi-3 base model implementation.
- signature: `class Phi3Model(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L594`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L594) — Performs a forward pass through the Phi-3 transformer model.
  - `__init__(self, config: Phi3Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L517`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L517) — Initialize Phi-3 base model.
  - `frequencies(self)` — [`L582`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L582) — Compute rotary position embedding frequencies.
  - `get_decoder(self)` — [`L727`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L727) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L740`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L740) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L720`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L720) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L733`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L733) — Returns the language model head of the module.
  - `embed_dropout` — [`L554`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L554)
  - `embed_tokens` — [`L546`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L546)
  - `layers` — [`L561`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L561)
  - `norm` — [`L574`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L574)
  - `padding_idx` — [`L543`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L543)
  - `vocab_size` — [`L544`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/modeling_phi3.py#L544)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), `pad_token_id`, [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`get_basic_frequencies`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_frequencies), [`Phi3Config`](phi3_configuration.md#Phi3Config), [`hidden_size`](phi3_configuration.md#Phi3Config.hidden_size), [`rms_norm_eps`](phi3_configuration.md#Phi3Config.rms_norm_eps), [`vocab_size`](phi3_configuration.md#Phi3Config.vocab_size), [`Phi3DecoderLayer`](modeling_phi3.md#Phi3DecoderLayer), [`embd_pdrop`](phi3_configuration.md#Phi3Config.embd_pdrop), [`gradient_checkpointing`](phi3_configuration.md#Phi3Config.gradient_checkpointing)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`Phi3ForCausalLM`](modeling_phi3.md#Phi3ForCausalLM), [`__init__`](modeling_phi3.md#Phi3ForCausalLM.__init__)

