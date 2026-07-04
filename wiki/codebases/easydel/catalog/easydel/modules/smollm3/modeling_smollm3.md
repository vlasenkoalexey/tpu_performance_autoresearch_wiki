---
title: 'Module: easydel/modules/smollm3/modeling_smollm3.py'
type: catalog
provenance: extracted
module: easydel/modules/smollm3/modeling_smollm3.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.smollm3.modeling_smollm3`/SmolLM3
symbols:
  SmolLM3DecoderLayer.__call__: DecoderLayer#__call__().
  SmolLM3Model.__call__: Model#__call__().
  SmolLM3Model.embed_tokens: Model#embed_tokens.
  SmolLM3Model: Model#
  SmolLM3ForCausalLM: ForCausalLM#
  SmolLM3ForSequenceClassification: ForSequenceClassification#
  SmolLM3MLP.__call__: MLP#__call__().
  SmolLM3Attention._create_rotary: Attention#_create_rotary().
  SmolLM3MLP.precision: MLP#precision.
  SmolLM3Attention.is_sliding: Attention#is_sliding.
  SmolLM3DecoderLayer.input_layernorm: DecoderLayer#input_layernorm.
  SmolLM3DecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  SmolLM3Model.norm: Model#norm.
  SmolLM3ForCausalLM.__init__: ForCausalLM#__init__().
  SmolLM3ForSequenceClassification.__init__: ForSequenceClassification#__init__().
  SmolLM3Attention.use_rope: Attention#use_rope.
  SmolLM3DecoderLayer._create_mlp: DecoderLayer#_create_mlp().
  SmolLM3MLP.gate_proj: MLP#gate_proj.
  SmolLM3MLP.up_proj: MLP#up_proj.
  SmolLM3MLP.down_proj: MLP#down_proj.
  SmolLM3MLP.hidden_size: MLP#hidden_size.
  SmolLM3MLP.intermediate_size: MLP#intermediate_size.
  SmolLM3Model.__init__: Model#__init__().
  SmolLM3ForCausalLM._task_type: ForCausalLM#_task_type.
  SmolLM3ForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  SmolLM3DecoderLayer.mlp: DecoderLayer#mlp.
  SmolLM3Attention: Attention#
  SmolLM3DecoderLayer.self_attn: DecoderLayer#self_attn.
  SmolLM3Model.layers: Model#layers.
  SmolLM3DecoderLayer.config: DecoderLayer#config.
  SmolLM3Attention.__init__: Attention#__init__().
  SmolLM3DecoderLayer.__init__: DecoderLayer#__init__().
  SmolLM3DecoderLayer.hidden_size: DecoderLayer#hidden_size.
  SmolLM3MLP.__init__: MLP#__init__().
  SmolLM3Model.get_embedding: Model#get_embedding().
  SmolLM3ForCausalLM._config_class: ForCausalLM#_config_class.
  SmolLM3ForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  SmolLM3MLP.config: MLP#config.
  SmolLM3Attention._dummy: Attention#_dummy().
  SmolLM3DecoderLayer: DecoderLayer#
  SmolLM3MLP: MLP#
  SmolLM3Attention.layer_idx: Attention#layer_idx.
  SmolLM3DecoderLayer.layer_idx: DecoderLayer#layer_idx.
  SmolLM3DecoderLayer.dtype: DecoderLayer#dtype.
  SmolLM3DecoderLayer.param_dtype: DecoderLayer#param_dtype.
  SmolLM3DecoderLayer.precision: DecoderLayer#precision.
  SmolLM3MLP.dtype: MLP#dtype.
  SmolLM3MLP.param_dtype: MLP#param_dtype.
  SmolLM3Model.get_decoder: Model#get_decoder().
  SmolLM3ForCausalLM._model_type: ForCausalLM#_model_type.
  SmolLM3ForSequenceClassification._model_type: ForSequenceClassification#_model_type.
---
# Module: [`easydel/modules/smollm3/modeling_smollm3.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py)

## Classes
### `SmolLM3Attention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/smollm3/modeling_smollm3.py:56`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L56)
- doc: SmolLM3 Attention module with conditional RoPE (NoPE).
- signature: `class SmolLM3Attention(UnifiedAttention):`
- members:
  - `__init__(self, config: SmolLM3Config, layer_idx: int, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: jax.lax.Precision = jax.lax.Precision.DEFAULT, *, rngs: nn.Rngs)` — [`L77`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L77) — Initialize SmolLM3 attention layer with conditional RoPE support.
  - `_create_rotary(self, config: SmolLM3Config, dtype: jnp.dtype)` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L122) — Create rotary embedding function, returning a dummy for NoPE layers.
  - `_dummy(query, key, positions=None, frequencies=None)` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L138) — Dummy RoPE function that returns query/key unchanged (NoPE).
  - `is_sliding` — [`L105`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L105)
  - `layer_idx` — [`L100`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L100)
  - `use_rope` — [`L102`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L102)
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`SmolLM3Config`](smollm3_configuration.md#SmolLM3Config), [`layer_types`](smollm3_configuration.md#SmolLM3Config.layer_types), [`no_rope_layers`](smollm3_configuration.md#SmolLM3Config.no_rope_layers), [`sliding_window`](smollm3_configuration.md#SmolLM3Config.sliding_window)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`self_attn`](modeling_smollm3.md#SmolLM3DecoderLayer.self_attn)

### `SmolLM3DecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/smollm3/modeling_smollm3.py:147`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L147)
- doc: Single decoder layer for SmolLM3 models with pre-norm architecture.
- signature: `class SmolLM3DecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L256`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L256) — Forward pass through the SmolLM3 decoder layer.
  - `__init__(self, config: SmolLM3Config, layer_idx: int, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: jax.lax.Precision = jax.lax.Precision.DEFAULT, *, rngs: nn.Rngs)` — [`L171`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L171) — Initialize SmolLM3 decoder layer.
  - `_create_mlp(self, config: SmolLM3Config, dtype: jnp.dtype, param_dtype: jnp.dtype, precision: jax.lax.Precision, rngs: nn.Rngs)` — [`L228`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L228) — Create the MLP module for this decoder layer.
  - `config` — [`L192`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L192)
  - `dtype` — [`L195`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L195)
  - `hidden_size` — [`L194`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L194)
  - `input_layernorm` — [`L213`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L213)
  - `layer_idx` — [`L193`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L193)
  - `mlp` — [`L210`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L210)
  - `param_dtype` — [`L196`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L196)
  - `post_attention_layernorm` — [`L220`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L220)
  - `precision` — [`L197`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L197)
  - `self_attn` — [`L200`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L200)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`SmolLM3Config`](smollm3_configuration.md#SmolLM3Config), [`hidden_size`](smollm3_configuration.md#SmolLM3Config.hidden_size), [`SmolLM3Attention`](modeling_smollm3.md#SmolLM3Attention), [`rms_norm_eps`](smollm3_configuration.md#SmolLM3Config.rms_norm_eps), [`SmolLM3MLP`](modeling_smollm3.md#SmolLM3MLP)
- used by: [`embed_tokens`](modeling_smollm3.md#SmolLM3Model.embed_tokens)

### `SmolLM3ForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/smollm3/modeling_smollm3.py:691`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L691)
- doc: SmolLM3 model with a language modeling head for causal language modeling tasks.
- signature: `class SmolLM3ForCausalLM(BaseCausalLMModule[SmolLM3Model, SmolLM3Config]):`
- members:
  - `__init__(self, config: SmolLM3Config, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L711`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L711) — Initialize SmolLM3 model for causal language modeling.
- protocol/private: `_config_class`[`L709`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L709), `_model_type`[`L708`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L708), `_task_type`[`L707`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L707)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`SmolLM3Config`](smollm3_configuration.md#SmolLM3Config), [`SmolLM3Model`](modeling_smollm3.md#SmolLM3Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `SmolLM3ForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/smollm3/modeling_smollm3.py:744`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L744)
- doc: SmolLM3 model for sequence classification tasks.
- signature: `class SmolLM3ForSequenceClassification(BaseSequenceClassificationModule[SmolLM3Model, SmolLM3Config]):`
- members:
  - `__init__(self, config: SmolLM3Config, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L764`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L764) — Initialize SmolLM3 model for sequence classification.
- protocol/private: `_config_class`[`L762`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L762), `_model_type`[`L761`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L761), `_task_type`[`L760`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L760)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`SmolLM3Config`](smollm3_configuration.md#SmolLM3Config), [`SmolLM3Model`](modeling_smollm3.md#SmolLM3Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule)

### `SmolLM3MLP`
- def: [`easydel/modules/smollm3/modeling_smollm3.py:343`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L343)
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L421`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L421) — Apply SwiGLU feedforward transformation.
  - `__init__(self, config: SmolLM3Config, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: jax.lax.Precision = jax.lax.Precision.DEFAULT, *, rngs: nn.Rngs)` — [`L362`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L362) — Initialize SmolLM3 MLP block.
  - `config` — [`L382`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L382)
  - `down_proj` — [`L416`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L416)
  - `dtype` — [`L385`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L385)
  - `gate_proj` — [`L408`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L408)
  - `hidden_size` — [`L383`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L383)
  - `intermediate_size` — [`L384`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L384)
  - `param_dtype` — [`L386`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L386)
  - `precision` — [`L387`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L387)
  - `up_proj` — [`L412`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L412)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`SmolLM3Config`](smollm3_configuration.md#SmolLM3Config), [`hidden_size`](smollm3_configuration.md#SmolLM3Config.hidden_size), [`initializer_range`](smollm3_configuration.md#SmolLM3Config.initializer_range), [`mlp_bias`](smollm3_configuration.md#SmolLM3Config.mlp_bias), [`intermediate_size`](smollm3_configuration.md#SmolLM3Config.intermediate_size)
- used by: [`_create_mlp`](modeling_smollm3.md#SmolLM3DecoderLayer._create_mlp)

### `SmolLM3Model`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/smollm3/modeling_smollm3.py:460`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L460)
- doc: SmolLM3 base model implementation (decoder-only transformer).
- signature: `class SmolLM3Model(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L542`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L542) — Forward pass through SmolLM3 base model.
  - `__init__(self, config: SmolLM3Config, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: jax.lax.Precision = jax.lax.Precision.DEFAULT, *, rngs: nn.Rngs)` — [`L479`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L479) — Initialize SmolLM3 base model.
  - `get_decoder(self)` — [`L681`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L681) — Returns the decoder part of the model.
  - `get_embedding(self)` — [`L673`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L673) — Returns the embedding layer of the module.
  - `embed_tokens` — [`L506`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L506)
  - `layers` — [`L520`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L520)
  - `norm` — [`L534`](../../../../../../../raw/code/EasyDeL/easydel/modules/smollm3/modeling_smollm3.py#L534)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`gradient_checkpointing`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing), [`SmolLM3Config`](smollm3_configuration.md#SmolLM3Config), [`hidden_size`](smollm3_configuration.md#SmolLM3Config.hidden_size), [`num_hidden_layers`](smollm3_configuration.md#SmolLM3Config.num_hidden_layers), [`rms_norm_eps`](smollm3_configuration.md#SmolLM3Config.rms_norm_eps), [`SmolLM3DecoderLayer`](modeling_smollm3.md#SmolLM3DecoderLayer), [`init_empty`](../../caching/ragged_page/cache.md#RaggedPagesCache.init_empty), [`vocab_size`](smollm3_configuration.md#SmolLM3Config.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`SmolLM3ForCausalLM`](modeling_smollm3.md#SmolLM3ForCausalLM), [`SmolLM3ForSequenceClassification`](modeling_smollm3.md#SmolLM3ForSequenceClassification), [`__init__`](modeling_smollm3.md#SmolLM3ForCausalLM.__init__), [`__init__`](modeling_smollm3.md#SmolLM3ForSequenceClassification.__init__)

