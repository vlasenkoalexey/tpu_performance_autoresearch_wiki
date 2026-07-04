---
title: 'Module: easydel/modules/cohere2/modeling_cohere2.py'
type: catalog
provenance: extracted
module: easydel/modules/cohere2/modeling_cohere2.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.cohere2.modeling_cohere2`/Cohere2
symbols:
  Cohere2Model.__call__: Model#__call__().
  Cohere2Block.__call__: Block#__call__().
  Cohere2ForCausalLM.__call__: ForCausalLM#__call__().
  Cohere2ForSequenceClassification.__call__: ForSequenceClassification#__call__().
  Cohere2Model.embed_tokens: Model#embed_tokens.
  Cohere2Model: Model#
  Cohere2ForCausalLM: ForCausalLM#
  Cohere2ForSequenceClassification: ForSequenceClassification#
  Cohere2MLP.__call__: MLP#__call__().
  Cohere2MLP.precision: MLP#precision.
  Cohere2LayerNorm.kernel: LayerNorm#kernel.
  Cohere2Block.input_layernorm: Block#input_layernorm.
  Cohere2Attention.__init__: Attention#__init__().
  Cohere2Attention._create_attention_performer: Attention#_create_attention_performer().
  Cohere2LayerNorm.__call__: LayerNorm#__call__().
  Cohere2Attention._create_rotary: Attention#_create_rotary().
  Cohere2ForCausalLM.__init__: ForCausalLM#__init__().
  Cohere2ForCausalLM.make_lm_head_fn: ForCausalLM#make_lm_head_fn().
  Cohere2ForSequenceClassification.__init__: ForSequenceClassification#__init__().
  Cohere2Block.config: Block#config.
  Cohere2MLP.gate_proj: MLP#gate_proj.
  Cohere2MLP.down_proj: MLP#down_proj.
  Cohere2MLP.up_proj: MLP#up_proj.
  Cohere2Model.norm: Model#norm.
  Cohere2ForCausalLM.logit_scale: ForCausalLM#logit_scale.
  Cohere2Attention._apply_rotary: Attention#_apply_rotary().
  Cohere2Block.is_sliding: Block#is_sliding.
  Cohere2Model.__init__: Model#__init__().
  Cohere2ForCausalLM._task_type: ForCausalLM#_task_type.
  Cohere2ForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  Cohere2Block.mlp: Block#mlp.
  Cohere2Model.layers: Model#layers.
  Cohere2LayerNorm.dtype: LayerNorm#dtype.
  Cohere2LayerNorm._norm: LayerNorm#_norm().
  Cohere2Attention: Attention#
  Cohere2Block.self_attn: Block#self_attn.
  Cohere2LayerNorm.dim: LayerNorm#dim.
  Cohere2MLP.__init__: MLP#__init__().
  Cohere2Block.__init__: Block#__init__().
  Cohere2Block.sliding_window: Block#sliding_window.
  Cohere2Model.get_embedding: Model#get_embedding().
  Cohere2ForCausalLM._config_class: ForCausalLM#_config_class.
  Cohere2ForCausalLM.apply_lm_head: ForCausalLM#apply_lm_head().
  Cohere2ForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  Cohere2LayerNorm: LayerNorm#
  Cohere2MLP.config: MLP#config.
  Cohere2LayerNorm.eps: LayerNorm#eps.
  Cohere2LayerNorm.param_dtype: LayerNorm#param_dtype.
  Cohere2MLP: MLP#
  Cohere2Block: Block#
  Cohere2ForCausalLM._project: ForCausalLM#_project().
  Cohere2LayerNorm.kernel_init: LayerNorm#kernel_init.
  Cohere2LayerNorm.__init__: LayerNorm#__init__().
  Cohere2LayerNorm.craft_sharding: LayerNorm#craft_sharding().
  Cohere2MLP.dtype: MLP#dtype.
  Cohere2MLP.param_dtype: MLP#param_dtype.
  Cohere2Block.layer_idx: Block#layer_idx.
  Cohere2Block.dtype: Block#dtype.
  Cohere2Block.param_dtype: Block#param_dtype.
  Cohere2Block.precision: Block#precision.
  Cohere2Block.rngs: Block#rngs.
  Cohere2Model.get_encoder: Model#get_encoder().
  Cohere2Model.get_decoder: Model#get_decoder().
  Cohere2Model.get_lm_head: Model#get_lm_head().
  Cohere2ForCausalLM._model_type: ForCausalLM#_model_type.
  Cohere2ForCausalLM.get_encoder: ForCausalLM#get_encoder().
  Cohere2ForCausalLM.get_decoder: ForCausalLM#get_decoder().
  Cohere2ForCausalLM.get_lm_head: ForCausalLM#get_lm_head().
  Cohere2ForCausalLM.get_embedding: ForCausalLM#get_embedding().
  Cohere2ForSequenceClassification._model_type: ForSequenceClassification#_model_type.
  Cohere2ForSequenceClassification.get_encoder: ForSequenceClassification#get_encoder().
  Cohere2ForSequenceClassification.get_decoder: ForSequenceClassification#get_decoder().
  Cohere2ForSequenceClassification.get_lm_head: ForSequenceClassification#get_lm_head().
  Cohere2ForSequenceClassification.get_embedding: ForSequenceClassification#get_embedding().
---
# Module: [`easydel/modules/cohere2/modeling_cohere2.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py)

## Classes
### `Cohere2Attention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/cohere2/modeling_cohere2.py:144`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L144)
- doc: Multi-head attention layer with layer-specific sliding window for Cohere2 models.
- signature: `class Cohere2Attention(UnifiedAttention):`
- members:
  - `__init__(self, config: Cohere2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L153`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L153) — Initialize Cohere2 attention with layer-specific sliding window configuration.
  - `_apply_rotary(self, query_states, key_states, position_ids, frequencies)` — [`L218`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L218) — Apply rotary position embeddings only when sliding window is enabled.
  - `_create_attention_performer(self, config: Cohere2Config, rngs: nn.Rngs)` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L201) — Create attention performer with Cohere2's attention dropout.
  - `_create_rotary(self, config: Cohere2Config, dtype: jnp.dtype)` — [`L189`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L189) — Create Cohere2-specific rotary embedding layer.
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`get_basic_rope`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_rope), [`Cohere2Config`](cohere2_configuration.md#Cohere2Config), [`layer_types`](cohere2_configuration.md#Cohere2Config.layer_types), [`sliding_window`](../../layers/attention/_unified.md#UnifiedAttention.sliding_window), [`rotary`](../../layers/attention/_unified.md#UnifiedAttention.rotary), [`sliding_window`](cohere2_configuration.md#Cohere2Config.sliding_window), [`attention_dropout`](cohere2_configuration.md#Cohere2Config.attention_dropout)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_attention_performer`](../../layers/attention/_unified.md#UnifiedAttention._create_attention_performer), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`_apply_rotary`](../../layers/attention/_unified.md#UnifiedAttention._apply_rotary), [`self_attn`](modeling_cohere2.md#Cohere2Block.self_attn)

### `Cohere2Block`  ·  implements/extends Module
- def: [`easydel/modules/cohere2/modeling_cohere2.py:324`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L324)
- doc: Single decoder layer for Cohere2 models.
- signature: `class Cohere2Block(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L387`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L387) — Forward pass through the decoder block.
  - `__init__(self, config: Cohere2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L334`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L334) — Initialize Cohere2 decoder block.
  - `config` — [`L355`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L355)
  - `dtype` — [`L357`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L357)
  - `input_layernorm` — [`L377`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L377)
  - `is_sliding` — [`L384`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L384)
  - `layer_idx` — [`L356`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L356)
  - `mlp` — [`L370`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L370)
  - `param_dtype` — [`L358`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L358)
  - `precision` — [`L359`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L359)
  - `rngs` — [`L360`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L360)
  - `self_attn` — [`L362`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L362)
  - `sliding_window` — [`L385`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L385)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`Cohere2Config`](cohere2_configuration.md#Cohere2Config), [`hidden_size`](cohere2_configuration.md#Cohere2Config.hidden_size), [`Cohere2Attention`](modeling_cohere2.md#Cohere2Attention), [`sliding_window`](cohere2_configuration.md#Cohere2Config.sliding_window), [`Cohere2LayerNorm`](modeling_cohere2.md#Cohere2LayerNorm), [`sliding_window_pattern`](cohere2_configuration.md#Cohere2Config.sliding_window_pattern), [`Cohere2MLP`](modeling_cohere2.md#Cohere2MLP), [`layer_norm_eps`](cohere2_configuration.md#Cohere2Config.layer_norm_eps)
- used by: [`embed_tokens`](modeling_cohere2.md#Cohere2Model.embed_tokens)

### `Cohere2ForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/cohere2/modeling_cohere2.py:683`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L683)
- doc: Cohere2 model with a language modeling head for causal language modeling tasks.
- signature: `class Cohere2ForCausalLM(BaseCausalLMModule[Cohere2Model, Cohere2Config]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L731`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L731) — Forward pass through the Cohere2 model for causal language modeling.
  - `__init__(self, config: Cohere2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L701`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L701) — Initialize Cohere2 model for causal language modeling.
  - `apply_lm_head(self, hidden_states: Array)` — [`L811`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L811) — Applies the language model head to the hidden states.
  - `get_decoder(self)` — [`L846`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L846) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L859`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L859) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L839`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L839) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L853`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L853) — Returns the language model head of the module.
  - `make_lm_head_fn(self)` — [`L826`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L826) — Trace-safe projection with Cohere2 logit scaling.
  - `logit_scale` — [`L729`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L729)
- protocol/private: `_config_class`[`L699`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L699), `_model_type`[`L698`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L698), `_project`[`L831`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L831), `_task_type`[`L697`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L697)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`CausalLMOutput`](../../infra/modeling_outputs.md#CausalLMOutput), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`make_lm_head_fn`](../_base/_base_task_module.md#BaseTaskModule.make_lm_head_fn), [`compute_lm_logits`](../_base/causal_lm_module.md#BaseCausalLMModule.compute_lm_logits), [`Cohere2Config`](cohere2_configuration.md#Cohere2Config), [`Cohere2Model`](modeling_cohere2.md#Cohere2Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.get_lm_head), [`make_lm_head_fn`](../_base/_base_task_module.md#BaseTaskModule.make_lm_head_fn), [`apply_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.apply_lm_head)

### `Cohere2ForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/cohere2/modeling_cohere2.py:868`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L868)
- doc: Cohere2 model for sequence classification tasks.
- signature: `class Cohere2ForSequenceClassification(BaseSequenceClassificationModule[Cohere2Model, Cohere2Config]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None)` — [`L915`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L915) — Forward pass for sequence classification.
  - `__init__(self, config: Cohere2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L885`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L885) — Initialize Cohere2 model for sequence classification.
  - `get_decoder(self)` — [`L1011`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L1011) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L1027`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L1027) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L1002`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L1002) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L1018`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L1018) — Returns the language model head of the module.
- protocol/private: `_config_class`[`L883`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L883), `_model_type`[`L882`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L882), `_task_type`[`L881`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L881)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), `pad_token_id`, [`SequenceClassifierOutput`](../../infra/modeling_outputs.md#SequenceClassifierOutput), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`Cohere2Config`](cohere2_configuration.md#Cohere2Config), [`Cohere2Model`](modeling_cohere2.md#Cohere2Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_lm_head)

### `Cohere2LayerNorm`  ·  implements/extends Module
- def: [`easydel/modules/cohere2/modeling_cohere2.py:54`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L54)
- doc: Layer Normalization for Cohere2 models.
- signature: `class Cohere2LayerNorm(nn.Module):`
- members:
  - `__call__(self, x: jnp.ndarray)` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L120) — Apply layer normalization with learnable scale.
  - `__init__(self, dim: int | tuple, eps: float = 0.000001, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, rngs: nn.Rngs | None = None)` — [`L64`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L64) — Initialize Cohere2LayerNorm layer.
  - `_norm(self, x: jnp.ndarray)` — [`L96`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L96) — Compute layer normalization with mean centering.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L109`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L109) — Return sharding specifications for Cohere2LayerNorm parameters.
  - `dim` — [`L85`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L85)
  - `dtype` — [`L87`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L87)
  - `eps` — [`L86`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L86)
  - `kernel` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L89)
  - `kernel_init` — [`L62`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L62)
  - `param_dtype` — [`L88`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L88)
- uses (calls/refs, reference-scoped): [`ArrayParam`](../../infra/utils.md#ArrayParam), [`bound`](../../infra/utils.md#ArrayParam.bound)
- used by: [`input_layernorm`](modeling_cohere2.md#Cohere2Block.input_layernorm), [`norm`](modeling_cohere2.md#Cohere2Model.norm)

### `Cohere2MLP`  ·  implements/extends Module
- def: [`easydel/modules/cohere2/modeling_cohere2.py:244`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L244)
- doc: Multi-Layer Perceptron module for Cohere2 models.
- signature: `class Cohere2MLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L297`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L297) — Apply SwiGLU feedforward transformation.
  - `__init__(self, config: Cohere2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L252`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L252) — Initialize Cohere2 MLP block.
  - `config` — [`L271`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L271)
  - `down_proj` — [`L294`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L294)
  - `dtype` — [`L272`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L272)
  - `gate_proj` — [`L293`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L293)
  - `param_dtype` — [`L273`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L273)
  - `precision` — [`L274`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L274)
  - `up_proj` — [`L295`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L295)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`Cohere2Config`](cohere2_configuration.md#Cohere2Config), [`hidden_size`](cohere2_configuration.md#Cohere2Config.hidden_size), [`initializer_range`](cohere2_configuration.md#Cohere2Config.initializer_range), [`intermediate_size`](cohere2_configuration.md#Cohere2Config.intermediate_size)
- used by: [`mlp`](modeling_cohere2.md#Cohere2Block.mlp)

### `Cohere2Model`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/cohere2/modeling_cohere2.py:462`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L462)
- doc: Cohere2 model implementation.
- signature: `class Cohere2Model(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L536`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L536) — Performs forward pass through the Cohere2 transformer model.
  - `__init__(self, config: Cohere2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L476`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L476) — Initialize Cohere2 base model.
  - `get_decoder(self)` — [`L661`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L661) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L675`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L675) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L654`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L654) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L668`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L668) — Returns the language model head of the module.
  - `embed_tokens` — [`L502`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L502)
  - `layers` — [`L516`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L516)
  - `norm` — [`L529`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/modeling_cohere2.py#L529)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`Cohere2Config`](cohere2_configuration.md#Cohere2Config), [`hidden_size`](cohere2_configuration.md#Cohere2Config.hidden_size), [`initializer_range`](cohere2_configuration.md#Cohere2Config.initializer_range), [`num_hidden_layers`](cohere2_configuration.md#Cohere2Config.num_hidden_layers), [`Cohere2LayerNorm`](modeling_cohere2.md#Cohere2LayerNorm), [`Cohere2Block`](modeling_cohere2.md#Cohere2Block), [`gradient_checkpointing`](cohere2_configuration.md#Cohere2Config.gradient_checkpointing), [`vocab_size`](cohere2_configuration.md#Cohere2Config.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`Cohere2ForCausalLM`](modeling_cohere2.md#Cohere2ForCausalLM), [`Cohere2ForSequenceClassification`](modeling_cohere2.md#Cohere2ForSequenceClassification), [`__init__`](modeling_cohere2.md#Cohere2ForCausalLM.__init__), [`__init__`](modeling_cohere2.md#Cohere2ForSequenceClassification.__init__)

