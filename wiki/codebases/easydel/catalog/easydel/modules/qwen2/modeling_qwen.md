---
title: 'Module: easydel/modules/qwen2/modeling_qwen.py'
type: catalog
provenance: extracted
module: easydel/modules/qwen2/modeling_qwen.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.qwen2.modeling_qwen`/Qwen2
symbols:
  Qwen2Model.__call__: Model#__call__().
  Qwen2DecoderLayer.__call__: DecoderLayer#__call__().
  Qwen2ForSequenceClassification.__call__: ForSequenceClassification#__call__().
  Qwen2Model: Model#
  Qwen2MLP.__call__: MLP#__call__().
  Qwen2ForCausalLM: ForCausalLM#
  Qwen2ForSequenceClassification: ForSequenceClassification#
  Qwen2ForEmbedding: ForEmbedding#
  Qwen2Model.dropout: Model#dropout.
  Qwen2Attention._create_rotary: Attention#_create_rotary().
  Qwen2Model.embed_tokens: Model#embed_tokens.
  Qwen2DecoderLayer.input_layernorm: DecoderLayer#input_layernorm.
  Qwen2DecoderLayer.post_attention_layernorm: DecoderLayer#post_attention_layernorm.
  Qwen2Attention.__init__: Attention#__init__().
  Qwen2Attention._create_attention_performer: Attention#_create_attention_performer().
  Qwen2MLP.act_fn: MLP#act_fn.
  Qwen2Model.norm: Model#norm.
  Qwen2MLP.precision: MLP#precision.
  Qwen2ForCausalLM.__init__: ForCausalLM#__init__().
  Qwen2ForSequenceClassification.__init__: ForSequenceClassification#__init__().
  Qwen2ForEmbedding.__init__: ForEmbedding#__init__().
  Qwen2MLP.gate_proj: MLP#gate_proj.
  Qwen2MLP.down_proj: MLP#down_proj.
  Qwen2MLP.up_proj: MLP#up_proj.
  Qwen2MLP.dropout: MLP#dropout.
  Qwen2Attention._create_q_proj: Attention#_create_q_proj().
  Qwen2Attention._create_k_proj: Attention#_create_k_proj().
  Qwen2Attention._create_v_proj: Attention#_create_v_proj().
  Qwen2Attention._create_o_proj: Attention#_create_o_proj().
  Qwen2DecoderLayer.config: DecoderLayer#config.
  Qwen2Model.__init__: Model#__init__().
  Qwen2ForCausalLM._task_type: ForCausalLM#_task_type.
  Qwen2ForSequenceClassification._task_type: ForSequenceClassification#_task_type.
  Qwen2ForEmbedding._task_type: ForEmbedding#_task_type.
  Qwen2DecoderLayer.mlp: DecoderLayer#mlp.
  Qwen2Model.layers: Model#layers.
  Qwen2MLP.config: MLP#config.
  Qwen2Attention: Attention#
  Qwen2DecoderLayer.self_attn: DecoderLayer#self_attn.
  Qwen2MLP.__init__: MLP#__init__().
  Qwen2DecoderLayer.__init__: DecoderLayer#__init__().
  Qwen2Model.get_embedding: Model#get_embedding().
  Qwen2ForCausalLM._config_class: ForCausalLM#_config_class.
  Qwen2ForSequenceClassification._config_class: ForSequenceClassification#_config_class.
  Qwen2ForEmbedding._config_class: ForEmbedding#_config_class.
  Qwen2MLP: MLP#
  Qwen2DecoderLayer: DecoderLayer#
  Qwen2MLP.dtype: MLP#dtype.
  Qwen2MLP.param_dtype: MLP#param_dtype.
  Qwen2DecoderLayer.dtype: DecoderLayer#dtype.
  Qwen2DecoderLayer.param_dtype: DecoderLayer#param_dtype.
  Qwen2DecoderLayer.precision: DecoderLayer#precision.
  Qwen2Model.get_encoder: Model#get_encoder().
  Qwen2Model.get_decoder: Model#get_decoder().
  Qwen2Model.get_lm_head: Model#get_lm_head().
  Qwen2ForCausalLM._model_type: ForCausalLM#_model_type.
  Qwen2ForCausalLM.get_encoder: ForCausalLM#get_encoder().
  Qwen2ForCausalLM.get_decoder: ForCausalLM#get_decoder().
  Qwen2ForCausalLM.get_lm_head: ForCausalLM#get_lm_head().
  Qwen2ForCausalLM.get_embedding: ForCausalLM#get_embedding().
  Qwen2ForSequenceClassification._model_type: ForSequenceClassification#_model_type.
  Qwen2ForSequenceClassification.get_encoder: ForSequenceClassification#get_encoder().
  Qwen2ForSequenceClassification.get_decoder: ForSequenceClassification#get_decoder().
  Qwen2ForSequenceClassification.get_lm_head: ForSequenceClassification#get_lm_head().
  Qwen2ForSequenceClassification.get_embedding: ForSequenceClassification#get_embedding().
  Qwen2ForEmbedding._model_type: ForEmbedding#_model_type.
---
# Module: [`easydel/modules/qwen2/modeling_qwen.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py)

## Classes
### `Qwen2Attention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/qwen2/modeling_qwen.py:147`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L147)
- doc: Multi-head attention layer with RoPE embeddings and sliding window support for Qwen2 models.
- signature: `class Qwen2Attention(UnifiedAttention):`
- members:
  - `__init__(self, config: Qwen2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L155) — Initialize Qwen2 attention layer with grouped-query attention and sliding window support.
  - `_create_attention_performer(self, config: Qwen2Config, rngs: nn.Rngs)` — [`L254`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L254) — Create attention performer with Qwen2's attention dropout.
  - `_create_k_proj(self, config, dtype, param_dtype, precision, rngs)` — [`L204`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L204) — Override to use bias=True for key projection (Qwen2-specific).
  - `_create_o_proj(self, config, dtype, param_dtype, precision, rngs)` — [`L230`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L230) — Override to use bias=False for output projection (Qwen2-specific).
  - `_create_q_proj(self, config, dtype, param_dtype, precision, rngs)` — [`L191`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L191) — Override to use bias=True for query projection (Qwen2-specific).
  - `_create_rotary(self, config: Qwen2Config, dtype: jnp.dtype)` — [`L245`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L245) — Create Qwen2-specific rotary embedding layer.
  - `_create_v_proj(self, config, dtype, param_dtype, precision, rngs)` — [`L217`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L217) — Override to use bias=True for value projection (Qwen2-specific).
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`get_basic_rope`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_rope), [`Qwen2Config`](qwen_configuration.md#Qwen2Config), [`layer_types`](qwen_configuration.md#Qwen2Config.layer_types), [`hidden_size`](qwen_configuration.md#Qwen2Config.hidden_size), [`sliding_window`](qwen_configuration.md#Qwen2Config.sliding_window), [`num_attention_heads`](qwen_configuration.md#Qwen2Config.num_attention_heads), [`attention_dropout`](qwen_configuration.md#Qwen2Config.attention_dropout), [`rope_theta`](qwen_configuration.md#Qwen2Config.rope_theta)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_attention_performer`](../../layers/attention/_unified.md#UnifiedAttention._create_attention_performer), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`_create_o_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_o_proj), [`_create_q_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_q_proj), [`_create_k_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_k_proj), [`_create_v_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_v_proj), [`self_attn`](modeling_qwen.md#Qwen2DecoderLayer.self_attn)

### `Qwen2DecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/qwen2/modeling_qwen.py:264`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L264)
- doc: Single decoder layer for Qwen2 models.
- signature: `class Qwen2DecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L326`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L326) — Forward pass through the decoder layer.
  - `__init__(self, config: Qwen2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L271`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L271) — Initialize Qwen2 decoder layer.
  - `config` — [`L291`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L291)
  - `dtype` — [`L292`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L292)
  - `input_layernorm` — [`L311`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L311)
  - `mlp` — [`L304`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L304)
  - `param_dtype` — [`L293`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L293)
  - `post_attention_layernorm` — [`L318`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L318)
  - `precision` — [`L294`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L294)
  - `self_attn` — [`L295`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L295)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`Qwen2Config`](qwen_configuration.md#Qwen2Config), [`hidden_size`](qwen_configuration.md#Qwen2Config.hidden_size), [`Qwen2Attention`](modeling_qwen.md#Qwen2Attention), [`rms_norm_eps`](qwen_configuration.md#Qwen2Config.rms_norm_eps), [`Qwen2MLP`](modeling_qwen.md#Qwen2MLP), [`scan_mlp_chunk_size`](qwen_configuration.md#Qwen2Config.scan_mlp_chunk_size), [`use_scan_mlp`](qwen_configuration.md#Qwen2Config.use_scan_mlp)
- used by: [`dropout`](modeling_qwen.md#Qwen2Model.dropout)

### `Qwen2ForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/qwen2/modeling_qwen.py:621`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L621)
- doc: Qwen2 model with a language modeling head for causal language modeling tasks.
- signature: `class Qwen2ForCausalLM(BaseCausalLMModule[Qwen2Model, Qwen2Config]):`
- members:
  - `__init__(self, config: Qwen2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L638`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L638) — Initialize Qwen2 model for causal language modeling.
  - `get_decoder(self)` — [`L674`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L674) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L686`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L686) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L667`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L667) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L680`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L680) — Returns the language model head of the module.
- protocol/private: `_config_class`[`L636`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L636), `_model_type`[`L635`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L635), `_task_type`[`L634`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L634)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`Qwen2Config`](qwen_configuration.md#Qwen2Config), [`Qwen2Model`](modeling_qwen.md#Qwen2Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.get_lm_head)

### `Qwen2ForEmbedding`  ·  implements/extends BaseEmbeddingModule
- def: [`easydel/modules/qwen2/modeling_qwen.py:857`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L857)
- doc: Qwen2 model for text embedding and similarity tasks.
- signature: `class Qwen2ForEmbedding(BaseEmbeddingModule[Qwen2Model, Qwen2Config]):`
- members:
  - `__init__(self, config: Qwen2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L877`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L877) — Initialize Qwen2 embedding model.
- protocol/private: `_config_class`[`L875`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L875), `_model_type`[`L874`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L874), `_task_type`[`L873`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L873)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`Qwen2Config`](qwen_configuration.md#Qwen2Config), [`Qwen2Model`](modeling_qwen.md#Qwen2Model), [`BaseEmbeddingModule`](../_base/embedding_module.md#BaseEmbeddingModule), [`EMBEDDING`](../../infra/factory.md#TaskType.EMBEDDING), [`__init__`](../_base/embedding_module.md#BaseEmbeddingModule.__init__)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseEmbeddingModule`](../_base/embedding_module.md#BaseEmbeddingModule)

### `Qwen2ForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/qwen2/modeling_qwen.py:694`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L694)
- doc: Qwen2 model for sequence classification tasks.
- signature: `class Qwen2ForSequenceClassification(BaseSequenceClassificationModule[Qwen2Model, Qwen2Config]):`
- members:
  - `__call__(self, input_ids: Array | None = None, inputs_embeds: Array | None = None, attention_mask: Array | None = None, mask_info: MaskInfo | None = None, position_ids: Array | None = None, segment_ids: Array | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L741`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L741) — Forward pass through the Qwen2 sequence classification model.
  - `__init__(self, config: Qwen2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L711`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L711) — Initialize Qwen2 model for sequence classification.
  - `get_decoder(self)` — [`L836`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L836) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L849`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L849) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L829`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L829) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L842`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L842) — Returns the language model head of the module.
- protocol/private: `_config_class`[`L709`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L709), `_model_type`[`L708`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L708), `_task_type`[`L707`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L707)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), `pad_token_id`, [`SequenceClassifierOutput`](../../infra/modeling_outputs.md#SequenceClassifierOutput), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`Qwen2Config`](qwen_configuration.md#Qwen2Config), [`Qwen2Model`](modeling_qwen.md#Qwen2Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_lm_head)

### `Qwen2MLP`  ·  implements/extends Module
- def: [`easydel/modules/qwen2/modeling_qwen.py:53`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L53)
- doc: Multi-Layer Perceptron module for Qwen2 models.
- signature: `class Qwen2MLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L119) — Apply SwiGLU feedforward transformation.
  - `__init__(self, config: Qwen2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L60`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L60) — Initialize Qwen2 MLP block.
  - `act_fn` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L117)
  - `config` — [`L79`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L79)
  - `down_proj` — [`L106`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L106)
  - `dropout` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L116)
  - `dtype` — [`L80`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L80)
  - `gate_proj` — [`L101`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L101)
  - `param_dtype` — [`L81`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L81)
  - `precision` — [`L82`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L82)
  - `up_proj` — [`L111`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L111)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`Qwen2Config`](qwen_configuration.md#Qwen2Config), [`hidden_size`](qwen_configuration.md#Qwen2Config.hidden_size), [`initializer_range`](qwen_configuration.md#Qwen2Config.initializer_range), [`intermediate_size`](qwen_configuration.md#Qwen2Config.intermediate_size), [`hidden_act`](qwen_configuration.md#Qwen2Config.hidden_act), [`resid_pdrop`](qwen_configuration.md#Qwen2Config.resid_pdrop)
- used by: [`mlp`](modeling_qwen.md#Qwen2DecoderLayer.mlp)

### `Qwen2Model`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/qwen2/modeling_qwen.py:397`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L397)
- doc: Qwen2 model implementation.
- signature: `class Qwen2Model(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L473`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L473) — Forward pass through the Qwen2 base model.
  - `__init__(self, config: Qwen2Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L411`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L411) — Initialize Qwen2 base model.
  - `get_decoder(self)` — [`L600`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L600) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L613`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L613) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L593`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L593) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L606`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L606) — Returns the language model head of the module.
  - `dropout` — [`L445`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L445)
  - `embed_tokens` — [`L437`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L437)
  - `layers` — [`L452`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L452)
  - `norm` — [`L465`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/modeling_qwen.py#L465)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`Qwen2Config`](qwen_configuration.md#Qwen2Config), [`hidden_size`](qwen_configuration.md#Qwen2Config.hidden_size), [`initializer_range`](qwen_configuration.md#Qwen2Config.initializer_range), [`num_hidden_layers`](qwen_configuration.md#Qwen2Config.num_hidden_layers), [`rms_norm_eps`](qwen_configuration.md#Qwen2Config.rms_norm_eps), [`Qwen2DecoderLayer`](modeling_qwen.md#Qwen2DecoderLayer), [`embd_pdrop`](qwen_configuration.md#Qwen2Config.embd_pdrop), [`gradient_checkpointing`](qwen_configuration.md#Qwen2Config.gradient_checkpointing), [`vocab_size`](qwen_configuration.md#Qwen2Config.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`Qwen2ForCausalLM`](modeling_qwen.md#Qwen2ForCausalLM), [`Qwen2ForEmbedding`](modeling_qwen.md#Qwen2ForEmbedding), [`Qwen2ForSequenceClassification`](modeling_qwen.md#Qwen2ForSequenceClassification), [`__init__`](modeling_qwen.md#Qwen2ForCausalLM.__init__), [`__init__`](modeling_qwen.md#Qwen2ForEmbedding.__init__), [`__init__`](modeling_qwen.md#Qwen2ForSequenceClassification.__init__)

