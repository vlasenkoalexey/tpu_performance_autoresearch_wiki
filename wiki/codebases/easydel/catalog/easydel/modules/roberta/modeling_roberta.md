---
title: 'Module: easydel/modules/roberta/modeling_roberta.py'
type: catalog
provenance: extracted
module: easydel/modules/roberta/modeling_roberta.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.roberta.modeling_roberta`/Roberta
symbols:
  RobertaSelfAttention.__call__: SelfAttention#__call__().
  RobertaEncoder.__call__: Encoder#__call__().
  RobertaModel.__call__: Model#__call__().
  RobertaLayer.__call__: Layer#__call__().
  RobertaModel: Model#
  RobertaAttention.__call__: Attention#__call__().
  RobertaLMHead.__call__: LMHead#__call__().
  RobertaForCausalLM.__call__: ForCausalLM#__call__().
  RobertaForSequenceClassification: ForSequenceClassification#
  RobertaForCausalLM: ForCausalLM#
  RobertaClassificationHead.dense: ClassificationHead#dense.
  RobertaForMultipleChoice.__call__: ForMultipleChoice#__call__().
  RobertaLMHead.decoder: LMHead#decoder.
  RobertaEmbeddings.word_embeddings: Embeddings#word_embeddings.
  RobertaEmbeddings.position_embeddings: Embeddings#position_embeddings.
  RobertaEmbeddings.token_type_embeddings: Embeddings#token_type_embeddings.
  RobertaIntermediate.dense: Intermediate#dense.
  RobertaOutput.dense: Output#dense.
  RobertaLMHead.bias: LMHead#bias.
  RobertaEmbeddings.__call__: Embeddings#__call__().
  RobertaForTokenClassification.__init__: ForTokenClassification#__init__().
  RobertaForTokenClassification.__call__: ForTokenClassification#__call__().
  RobertaEmbeddings.config: Embeddings#config.
  RobertaEmbeddings.LayerNorm: Embeddings#LayerNorm.
  RobertaSelfOutput.dense: SelfOutput#dense.
  RobertaSelfOutput.LayerNorm: SelfOutput#LayerNorm.
  RobertaOutput.LayerNorm: Output#LayerNorm.
  RobertaPooler.dense: Pooler#dense.
  RobertaLMHead.dense: LMHead#dense.
  RobertaLMHead.layer_norm: LMHead#layer_norm.
  RobertaClassificationHead.out_proj: ClassificationHead#out_proj.
  RobertaEncoder.precision: Encoder#precision.
  RobertaForSequenceClassification.__init__: ForSequenceClassification#__init__().
  RobertaForQuestionAnswering.__call__: ForQuestionAnswering#__call__().
  RobertaForCausalLM.__init__: ForCausalLM#__init__().
  RobertaForCausalLM._lm_head_name: ForCausalLM#_lm_head_name.
  RobertaForTokenClassification: ForTokenClassification#
  RobertaForQuestionAnswering: ForQuestionAnswering#
  RobertaLMHead.config: LMHead#config.
  RobertaClassificationHead.config: ClassificationHead#config.
  RobertaIntermediate.activation: Intermediate#activation.
  RobertaLayer.output: Layer#output.
  RobertaSelfAttention._split_heads: SelfAttention#_split_heads().
  RobertaSelfOutput.__call__: SelfOutput#__call__().
  RobertaOutput.__call__: Output#__call__().
  RobertaClassificationHead.__call__: ClassificationHead#__call__().
  RobertaForQuestionAnswering.__init__: ForQuestionAnswering#__init__().
  RobertaForCausalLM.apply_lm_head: ForCausalLM#apply_lm_head().
  RobertaSelfAttention.key: SelfAttention#key.
  RobertaSelfAttention.value: SelfAttention#value.
  RobertaEncoder.layer: Encoder#layer.
  RobertaEmbeddings.dropout: Embeddings#dropout.
  RobertaSelfAttention.attention_performer: SelfAttention#attention_performer.
  RobertaSelfAttention.query: SelfAttention#query.
  RobertaSelfOutput.config: SelfOutput#config.
  RobertaSelfOutput.dropout: SelfOutput#dropout.
  RobertaOutput.config: Output#config.
  RobertaOutput.dropout: Output#dropout.
  RobertaLayer.attention: Layer#attention.
  RobertaForMultipleChoice.classifier: ForMultipleChoice#classifier.
  RobertaForMultipleChoice.roberta: ForMultipleChoice#roberta.
  RobertaSelfAttention.__init__: SelfAttention#__init__().
  RobertaIntermediate.__call__: Intermediate#__call__().
  RobertaModel.__init__: Model#__init__().
  RobertaForSequenceClassification.__call__: ForSequenceClassification#__call__().
  RobertaForMultipleChoice.__init__: ForMultipleChoice#__init__().
  RobertaForMultipleChoice.get_embedding: ForMultipleChoice#get_embedding().
  RobertaForCausalLM._task_type: ForCausalLM#_task_type.
  RobertaSelfAttention.head_dim: SelfAttention#head_dim.
  RobertaModel.embeddings: Model#embeddings.
  RobertaForSequenceClassification.classifier: ForSequenceClassification#classifier.
  RobertaForMultipleChoice: ForMultipleChoice#
  RobertaIntermediate.config: Intermediate#config.
  RobertaSelfAttention: SelfAttention#
  RobertaAttention.self: Attention#self.
  RobertaAttention.output: Attention#output.
  RobertaLayer.intermediate: Layer#intermediate.
  RobertaLayer.crossattention: Layer#crossattention.
  RobertaModel.encoder: Model#encoder.
  RobertaModel.pooler: Model#pooler.
  RobertaModel.get_embedding: Model#get_embedding().
  RobertaForMultipleChoice.dropout: ForMultipleChoice#dropout.
  RobertaPooler.config: Pooler#config.
  RobertaEmbeddings.__init__: Embeddings#__init__().
  RobertaSelfAttention._merge_heads: SelfAttention#_merge_heads().
  RobertaSelfOutput.__init__: SelfOutput#__init__().
  RobertaAttention.__init__: Attention#__init__().
  RobertaIntermediate.__init__: Intermediate#__init__().
  RobertaOutput.__init__: Output#__init__().
  RobertaLayer.__init__: Layer#__init__().
  RobertaEncoder.__init__: Encoder#__init__().
  RobertaPooler.__init__: Pooler#__init__().
  RobertaPooler.__call__: Pooler#__call__().
  RobertaLMHead.__init__: LMHead#__init__().
  RobertaClassificationHead.__init__: ClassificationHead#__init__().
  RobertaForSequenceClassification.get_task_head: ForSequenceClassification#get_task_head().
  RobertaForMultipleChoice.get_encoder: ForMultipleChoice#get_encoder().
  RobertaForTokenClassification.get_task_head: ForTokenClassification#get_task_head().
  RobertaForQuestionAnswering.get_task_head: ForQuestionAnswering#get_task_head().
  RobertaForCausalLM._config_class: ForCausalLM#_config_class.
  RobertaForCausalLM.get_lm_head: ForCausalLM#get_lm_head().
  RobertaAttention: Attention#
  RobertaClassificationHead.dropout: ClassificationHead#dropout.
  RobertaForCausalLM.lm_head: ForCausalLM#lm_head.
  RobertaEmbeddings: Embeddings#
  RobertaSelfAttention.causal: SelfAttention#causal.
  RobertaSelfAttention.dtype: SelfAttention#dtype.
  RobertaSelfOutput: SelfOutput#
  RobertaIntermediate: Intermediate#
  RobertaOutput: Output#
  RobertaLayer: Layer#
  RobertaLayer.config: Layer#config.
  RobertaEncoder: Encoder#
  RobertaPooler: Pooler#
  RobertaLMHead: LMHead#
  RobertaLMHead.dtype: LMHead#dtype.
  RobertaLMHead.param_dtype: LMHead#param_dtype.
  RobertaClassificationHead: ClassificationHead#
  RobertaModel.add_pooling_layer: Model#add_pooling_layer.
  RobertaEmbeddings.dtype: Embeddings#dtype.
  RobertaEmbeddings.param_dtype: Embeddings#param_dtype.
  RobertaEmbeddings.precision: Embeddings#precision.
  RobertaSelfAttention.param_dtype: SelfAttention#param_dtype.
  RobertaSelfAttention.precision: SelfAttention#precision.
  RobertaSelfOutput.dtype: SelfOutput#dtype.
  RobertaSelfOutput.param_dtype: SelfOutput#param_dtype.
  RobertaSelfOutput.precision: SelfOutput#precision.
  RobertaAttention.config: Attention#config.
  RobertaAttention.causal: Attention#causal.
  RobertaAttention.dtype: Attention#dtype.
  RobertaAttention.param_dtype: Attention#param_dtype.
  RobertaAttention.precision: Attention#precision.
  RobertaIntermediate.dtype: Intermediate#dtype.
  RobertaIntermediate.param_dtype: Intermediate#param_dtype.
  RobertaIntermediate.precision: Intermediate#precision.
  RobertaOutput.dtype: Output#dtype.
  RobertaOutput.param_dtype: Output#param_dtype.
  RobertaOutput.precision: Output#precision.
  RobertaLayer.dtype: Layer#dtype.
  RobertaLayer.param_dtype: Layer#param_dtype.
  RobertaLayer.precision: Layer#precision.
  RobertaEncoder.config: Encoder#config.
  RobertaEncoder.dtype: Encoder#dtype.
  RobertaEncoder.param_dtype: Encoder#param_dtype.
  RobertaPooler.dtype: Pooler#dtype.
  RobertaPooler.param_dtype: Pooler#param_dtype.
  RobertaPooler.precision: Pooler#precision.
  RobertaLMHead.precision: LMHead#precision.
  RobertaLMHead.craft_sharding: LMHead#craft_sharding().
  RobertaClassificationHead.dtype: ClassificationHead#dtype.
  RobertaClassificationHead.param_dtype: ClassificationHead#param_dtype.
  RobertaClassificationHead.precision: ClassificationHead#precision.
  RobertaModel.get_encoder: Model#get_encoder().
  RobertaModel.get_decoder: Model#get_decoder().
  RobertaModel.get_lm_head: Model#get_lm_head().
  RobertaForSequenceClassification.get_encoder: ForSequenceClassification#get_encoder().
  RobertaForSequenceClassification.get_decoder: ForSequenceClassification#get_decoder().
  RobertaForSequenceClassification.get_lm_head: ForSequenceClassification#get_lm_head().
  RobertaForSequenceClassification.get_embedding: ForSequenceClassification#get_embedding().
  RobertaForMultipleChoice.get_decoder: ForMultipleChoice#get_decoder().
  RobertaForMultipleChoice.get_lm_head: ForMultipleChoice#get_lm_head().
  RobertaForTokenClassification.get_encoder: ForTokenClassification#get_encoder().
  RobertaForTokenClassification.get_decoder: ForTokenClassification#get_decoder().
  RobertaForTokenClassification.get_lm_head: ForTokenClassification#get_lm_head().
  RobertaForTokenClassification.get_embedding: ForTokenClassification#get_embedding().
  RobertaForQuestionAnswering.get_encoder: ForQuestionAnswering#get_encoder().
  RobertaForQuestionAnswering.get_decoder: ForQuestionAnswering#get_decoder().
  RobertaForQuestionAnswering.get_lm_head: ForQuestionAnswering#get_lm_head().
  RobertaForQuestionAnswering.get_embedding: ForQuestionAnswering#get_embedding().
  RobertaForCausalLM._model_type: ForCausalLM#_model_type.
  RobertaForCausalLM.get_encoder: ForCausalLM#get_encoder().
  RobertaForCausalLM.get_decoder: ForCausalLM#get_decoder().
  RobertaForCausalLM.get_embedding: ForCausalLM#get_embedding().
---
# Module: [`easydel/modules/roberta/modeling_roberta.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py)

## Classes
### `RobertaAttention`  ·  implements/extends Module
- def: [`easydel/modules/roberta/modeling_roberta.py:470`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L470)
- doc: Full attention module combining self-attention and output projection.
- signature: `class RobertaAttention(nn.Module):`
- members:
  - `__call__(self, hidden_states, mask_info: MaskInfo | None, layer_head_mask, mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, key_value_states=None, output_attentions: bool = False)` — [`L527`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L527) — Forward pass of the RobertaAttention module.
  - `__init__(self, config: RobertaConfig, causal: bool = False, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L486`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L486) — Initialize RoBERTa attention module.
  - `causal` — [`L507`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L507)
  - `config` — [`L506`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L506)
  - `dtype` — [`L508`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L508)
  - `output` — [`L519`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L519)
  - `param_dtype` — [`L509`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L509)
  - `precision` — [`L510`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L510)
  - `self` — [`L511`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L511)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`RobertaConfig`](roberta_configuration.md#RobertaConfig), [`RobertaSelfAttention`](modeling_roberta.md#RobertaSelfAttention), [`RobertaSelfOutput`](modeling_roberta.md#RobertaSelfOutput)
- used by: [`attention`](modeling_roberta.md#RobertaLayer.attention), [`crossattention`](modeling_roberta.md#RobertaLayer.crossattention)

### `RobertaClassificationHead`  ·  implements/extends Module
- def: [`easydel/modules/roberta/modeling_roberta.py:1193`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1193)
- doc: Classification head for sequence-level classification tasks.
- signature: `class RobertaClassificationHead(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L1261`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1261) — Forward pass of the RobertaClassificationHead.
  - `__init__(self, config: RobertaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L1211`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1211) — Initialize RoBERTa classification head.
  - `config` — [`L1229`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1229)
  - `dense` — [`L1233`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1233)
  - `dropout` — [`L1247`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1247)
  - `dtype` — [`L1230`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1230)
  - `out_proj` — [`L1251`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1251)
  - `param_dtype` — [`L1231`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1231)
  - `precision` — [`L1232`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1232)
- uses (calls/refs, reference-scoped): [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`RobertaConfig`](roberta_configuration.md#RobertaConfig), [`hidden_size`](roberta_configuration.md#RobertaConfig.hidden_size), [`initializer_range`](roberta_configuration.md#RobertaConfig.initializer_range), [`hidden_dropout_prob`](roberta_configuration.md#RobertaConfig.hidden_dropout_prob), [`classifier_dropout`](roberta_configuration.md#RobertaConfig.classifier_dropout)
- used by: [`classifier`](modeling_roberta.md#RobertaForSequenceClassification.classifier)

### `RobertaEmbeddings`  ·  implements/extends Module
- def: [`easydel/modules/roberta/modeling_roberta.py:66`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L66)
- doc: Embedding layer for RoBERTa model.
- signature: `class RobertaEmbeddings(nn.Module):`
- members:
  - `__call__(self, input_ids, token_type_ids, position_ids, attention_mask)` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L143) — Forward pass of the RobertaEmbeddings layer.
  - `__init__(self, config: RobertaConfig, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L85`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L85) — Initialize RoBERTa embeddings layer.
  - `LayerNorm` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L131) — documented in [easydel-layers-norms-_norms](../../../../concepts/easydel-layers-norms-_norms.md)
  - `config` — [`L103`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L103)
  - `dropout` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L138)
  - `dtype` — [`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L104)
  - `param_dtype` — [`L105`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L105)
  - `position_embeddings` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L115)
  - `precision` — [`L106`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L106)
  - `token_type_embeddings` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L123)
  - `word_embeddings` — [`L107`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L107)
- uses (calls/refs, reference-scoped): [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`RobertaConfig`](roberta_configuration.md#RobertaConfig), [`hidden_size`](roberta_configuration.md#RobertaConfig.hidden_size), [`initializer_range`](roberta_configuration.md#RobertaConfig.initializer_range), [`hidden_dropout_prob`](roberta_configuration.md#RobertaConfig.hidden_dropout_prob), [`layer_norm_eps`](roberta_configuration.md#RobertaConfig.layer_norm_eps), [`vocab_size`](roberta_configuration.md#RobertaConfig.vocab_size), [`max_position_embeddings`](roberta_configuration.md#RobertaConfig.max_position_embeddings), [`type_vocab_size`](roberta_configuration.md#RobertaConfig.type_vocab_size)
- used by: [`embeddings`](modeling_roberta.md#RobertaModel.embeddings)

### `RobertaEncoder`  ·  implements/extends Module
- def: [`easydel/modules/roberta/modeling_roberta.py:867`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L867)
- doc: Stack of RoBERTa encoder layers.
- signature: `class RobertaEncoder(nn.Module):`
- members:
  - `__call__(self, hidden_states, mask_info: MaskInfo | None, head_mask, mode: common_types.RUNTIME_MODE_TYPES, encoder_hidden_states: Float[Array, "batch seq_len hidden_dim"] | None = None, encoder_mask_info: MaskInfo | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, output_hidden_states: bool = False)` — [`L924`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L924) — Forward pass through all RoBERTa encoder layers.
  - `__init__(self, config: RobertaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L882`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L882) — Initialize the RoBERTa encoder layer stack.
  - `config` — [`L900`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L900)
  - `dtype` — [`L901`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L901)
  - `layer` — [`L911`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L911)
  - `param_dtype` — [`L902`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L902)
  - `precision` — [`L903`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L903)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`auto_remat`](../../infra/utils.md#auto_remat), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`RobertaConfig`](roberta_configuration.md#RobertaConfig), [`BaseModelOutputWithPastAndCrossAttentions`](../../infra/modeling_outputs.md#BaseModelOutputWithPastAndCrossAttentions), [`gradient_checkpointing`](roberta_configuration.md#RobertaConfig.gradient_checkpointing), [`num_hidden_layers`](roberta_configuration.md#RobertaConfig.num_hidden_layers), [`RobertaLayer`](modeling_roberta.md#RobertaLayer), [`cross_attention`](../../infra/modeling_outputs.md#DecoderLayerOutput.cross_attention)
- used by: [`encoder`](modeling_roberta.md#RobertaModel.encoder)

### `RobertaForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/roberta/modeling_roberta.py:2079`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2079)
- doc: RoBERTa model with a causal language modeling head.
- signature: `class RobertaForCausalLM(BaseCausalLMModule[RobertaModel, RobertaConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"], attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, token_type_ids: Int[Array, "batch seq_len"] | None = None, head_mask: Bool[Array, num_heads] | None = None, encoder_hidden_states: Float[Array, "batch seq_len hidden_dim"] | None = None, encoder_attention_mask: Bool[Array, "batch seq_len"] | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, output_attentions: bool = False, output_hidden_states: bool = False)` — [`L2166`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2166) — Forward pass for causal language modeling.
  - `__init__(self, config: RobertaConfig, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L2099`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2099) — Initialize RoBERTa for causal language modeling.
  - `apply_lm_head(self, hidden_states: Array)` — [`L2151`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2151) — Apply the language modeling head to hidden states.
  - `get_decoder(self)` — [`L2242`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2242) — Returns the decoder part of the model.
  - `get_embedding(self)` — [`L2250`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2250) — Returns the embedding layer of the model.
  - `get_encoder(self)` — [`L2234`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2234) — Returns the encoder part of the model.
  - `get_lm_head(self)` — [`L2246`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2246) — Returns the language model head.
  - `lm_head` — [`L2143`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2143)
- protocol/private: `_config_class`[`L2097`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2097), `_lm_head_name`[`L2135`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2135), `_model_type`[`L2096`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2096), `_task_type`[`L2095`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2095)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`auto_remat`](../../infra/utils.md#auto_remat), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`BaseTaskModule`](../_base/_base_task_module.md#BaseTaskModule), [`compute_lm_logits`](../_base/causal_lm_module.md#BaseCausalLMModule.compute_lm_logits), [`RobertaConfig`](roberta_configuration.md#RobertaConfig), [`RobertaModel`](modeling_roberta.md#RobertaModel), [`__init__`](../_base/_base_task_module.md#BaseTaskModule.__init__), `tie_word_embeddings`, [`CausalLMOutputWithCrossAttentions`](../../infra/modeling_outputs.md#CausalLMOutputWithCrossAttentions), [`gradient_checkpointing`](roberta_configuration.md#RobertaConfig.gradient_checkpointing), [`RobertaLMHead`](modeling_roberta.md#RobertaLMHead)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.get_lm_head), [`apply_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.apply_lm_head)

### `RobertaForMultipleChoice`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/roberta/modeling_roberta.py:1649`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1649)
- doc: RoBERTa model for multiple-choice classification tasks.
- signature: `class RobertaForMultipleChoice(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, output_attentions: bool = False, output_hidden_states: bool = False)` — [`L1711`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1711) — Forward pass for multiple-choice classification.
  - `__init__(self, config: RobertaConfig, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L1666`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1666) — Initialize RoBERTa for multiple-choice classification.
  - `get_decoder(self)` — [`L1774`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1774) — Returns the decoder part of the model.
  - `get_embedding(self)` — [`L1790`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1790) — Returns the embedding layer of the model.
  - `get_encoder(self)` — [`L1770`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1770) — Returns the encoder part of the model.
  - `get_lm_head(self)` — [`L1782`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1782) — Returns the language model head.
  - `classifier` — [`L1702`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1702)
  - `dropout` — [`L1698`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1698)
  - `roberta` — [`L1691`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1691)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`RobertaConfig`](roberta_configuration.md#RobertaConfig), [`RobertaModel`](modeling_roberta.md#RobertaModel), [`MultipleChoiceModelOutput`](../../infra/modeling_outputs.md#MultipleChoiceModelOutput), [`get_embedding`](modeling_roberta.md#RobertaModel.get_embedding), [`attentions`](../../infra/modeling_outputs.md#BaseModelOutputWithPoolingAndCrossAttentions.attentions), [`hidden_states`](../../infra/modeling_outputs.md#BaseModelOutputWithPoolingAndCrossAttentions.hidden_states)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder)

### `RobertaForQuestionAnswering`  ·  implements/extends BaseQuestionAnsweringModule
- def: [`easydel/modules/roberta/modeling_roberta.py:1937`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1937)
- doc: RoBERTa model for extractive question answering.
- signature: `class RobertaForQuestionAnswering(BaseQuestionAnsweringModule[RobertaModel, RobertaConfig]):`
- members:
  - `__call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, output_attentions: bool = False, output_hidden_states: bool = False)` — [`L1990`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1990) — Forward pass for question answering.
  - `__init__(self, config: RobertaConfig, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L1953`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1953) — Initialize RoBERTa for extractive question answering.
  - `get_decoder(self)` — [`L2053`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2053) — Returns the decoder part of the model.
  - `get_embedding(self)` — [`L2069`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2069) — Returns the embedding layer of the model.
  - `get_encoder(self)` — [`L2049`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2049) — Returns the encoder part of the model.
  - `get_lm_head(self)` — [`L2061`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2061) — Returns the language model head.
  - `get_task_head(self)` — [`L2073`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L2073) — Returns the question answering head.
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RobertaConfig`](roberta_configuration.md#RobertaConfig), [`RobertaModel`](modeling_roberta.md#RobertaModel), [`__init__`](../_base/question_answering_module.md#BaseQuestionAnsweringModule.__init__), [`BaseQuestionAnsweringModule`](../_base/question_answering_module.md#BaseQuestionAnsweringModule), [`QuestionAnsweringModelOutput`](../../infra/modeling_outputs.md#QuestionAnsweringModelOutput), [`qa_outputs`](../_base/question_answering_module.md#BaseQuestionAnsweringModule.qa_outputs)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`BaseQuestionAnsweringModule`](../_base/question_answering_module.md#BaseQuestionAnsweringModule), [`get_task_head`](../_base/question_answering_module.md#BaseQuestionAnsweringModule.get_task_head), [`get_lm_head`](../_base/question_answering_module.md#BaseQuestionAnsweringModule.get_lm_head)

### `RobertaForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/roberta/modeling_roberta.py:1512`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1512)
- doc: RoBERTa model with a classification head for sequence classification.
- signature: `class RobertaForSequenceClassification(BaseSequenceClassificationModule[RobertaModel, RobertaConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"], attention_mask: Bool[Array, "batch seq_len"] | None = None, token_type_ids: Int[Array, "batch seq_len"] | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, head_mask: Bool[Array, num_heads] | None = None, output_attentions: bool = False, output_hidden_states: bool = False)` — [`L1573`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1573) — Forward pass for sequence classification.
  - `__init__(self, config: RobertaConfig, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L1528`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1528) — Initialize RoBERTa for sequence classification.
  - `get_decoder(self)` — [`L1624`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1624) — Returns the decoder part of the model.
  - `get_embedding(self)` — [`L1640`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1640) — Returns the embedding layer of the model.
  - `get_encoder(self)` — [`L1620`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1620) — Returns the encoder part of the model.
  - `get_lm_head(self)` — [`L1632`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1632) — Returns the language model head.
  - `get_task_head(self)` — [`L1644`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1644) — Returns the sequence classification head.
  - `classifier` — [`L1565`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1565)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`SequenceClassifierOutput`](../../infra/modeling_outputs.md#SequenceClassifierOutput), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`BaseTaskModule`](../_base/_base_task_module.md#BaseTaskModule), [`RobertaConfig`](roberta_configuration.md#RobertaConfig), [`RobertaModel`](modeling_roberta.md#RobertaModel), [`__init__`](../_base/_base_task_module.md#BaseTaskModule.__init__), [`RobertaClassificationHead`](modeling_roberta.md#RobertaClassificationHead)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_lm_head), [`get_task_head`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.get_task_head)

### `RobertaForTokenClassification`  ·  implements/extends BaseTokenClassificationModule
- def: [`easydel/modules/roberta/modeling_roberta.py:1795`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1795)
- doc: RoBERTa model with a token classification head.
- signature: `class RobertaForTokenClassification(BaseTokenClassificationModule[RobertaModel, RobertaConfig]):`
- members:
  - `__call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, output_attentions: bool = False, output_hidden_states: bool = False)` — [`L1853`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1853) — Forward pass for token classification.
  - `__init__(self, config: RobertaConfig, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L1812`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1812) — Initialize RoBERTa for token classification.
  - `get_decoder(self)` — [`L1912`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1912) — Returns the decoder part of the model.
  - `get_embedding(self)` — [`L1928`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1928) — Returns the embedding layer of the model.
  - `get_encoder(self)` — [`L1908`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1908) — Returns the encoder part of the model.
  - `get_lm_head(self)` — [`L1920`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1920) — Returns the language model head.
  - `get_task_head(self)` — [`L1932`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1932) — Returns the token classification head.
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RobertaConfig`](roberta_configuration.md#RobertaConfig), [`RobertaModel`](modeling_roberta.md#RobertaModel), [`BaseTokenClassificationModule`](../_base/token_classification_module.md#BaseTokenClassificationModule), [`dropout`](../_base/token_classification_module.md#BaseTokenClassificationModule.dropout), [`TokenClassifierOutput`](../../infra/modeling_outputs.md#TokenClassifierOutput), [`classifier`](../_base/token_classification_module.md#BaseTokenClassificationModule.classifier), [`__init__`](../_base/token_classification_module.md#BaseTokenClassificationModule.__init__), [`hidden_dropout_prob`](roberta_configuration.md#RobertaConfig.hidden_dropout_prob), [`classifier_dropout`](roberta_configuration.md#RobertaConfig.classifier_dropout)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`BaseTokenClassificationModule`](../_base/token_classification_module.md#BaseTokenClassificationModule), [`get_task_head`](../_base/token_classification_module.md#BaseTokenClassificationModule.get_task_head), [`get_lm_head`](../_base/token_classification_module.md#BaseTokenClassificationModule.get_lm_head)

### `RobertaIntermediate`  ·  implements/extends Module
- def: [`easydel/modules/roberta/modeling_roberta.py:572`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L572)
- doc: Intermediate (up-projection) layer of the RoBERTa feed-forward network.
- signature: `class RobertaIntermediate(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L621`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L621) — Forward pass of the RobertaIntermediate layer.
  - `__init__(self, config: RobertaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L588`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L588) — Initialize RoBERTa intermediate (up-projection) layer.
  - `activation` — [`L619`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L619)
  - `config` — [`L606`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L606)
  - `dense` — [`L610`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L610)
  - `dtype` — [`L607`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L607)
  - `param_dtype` — [`L608`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L608)
  - `precision` — [`L609`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L609)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`RobertaConfig`](roberta_configuration.md#RobertaConfig), [`hidden_size`](roberta_configuration.md#RobertaConfig.hidden_size), [`initializer_range`](roberta_configuration.md#RobertaConfig.initializer_range), [`intermediate_size`](roberta_configuration.md#RobertaConfig.intermediate_size), [`hidden_act`](roberta_configuration.md#RobertaConfig.hidden_act)
- used by: [`intermediate`](modeling_roberta.md#RobertaLayer.intermediate)

### `RobertaLMHead`  ·  implements/extends Module
- def: [`easydel/modules/roberta/modeling_roberta.py:1088`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1088)
- doc: Language modeling head for masked language modeling.
- signature: `class RobertaLMHead(nn.Module):`
- members:
  - `__call__(self, hidden_states, shared_embedding=None)` — [`L1165`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1165) — Forward pass of the RobertaLMHead.
  - `__init__(self, config: RobertaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L1106`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1106) — Initialize RoBERTa language modeling head.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L1161`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1161) — Return sharding specs for LM head bias.
  - `bias` — [`L1154`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1154)
  - `config` — [`L1124`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1124)
  - `decoder` — [`L1144`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1144) — documented in [easydel-layers-linears-_linear](../../../../concepts/easydel-layers-linears-_linear.md)
  - `dense` — [`L1128`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1128)
  - `dtype` — [`L1125`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1125)
  - `layer_norm` — [`L1137`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1137)
  - `param_dtype` — [`L1126`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1126)
  - `precision` — [`L1127`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1127)
- uses (calls/refs, reference-scoped): [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`ArrayParam`](../../infra/utils.md#ArrayParam), [`bound`](../../infra/utils.md#ArrayParam.bound), [`RobertaConfig`](roberta_configuration.md#RobertaConfig), [`hidden_size`](roberta_configuration.md#RobertaConfig.hidden_size), [`kernel`](../../layers/linears/_linear.md#ParallelLinear.kernel), [`initializer_range`](roberta_configuration.md#RobertaConfig.initializer_range), [`layer_norm_eps`](roberta_configuration.md#RobertaConfig.layer_norm_eps), [`vocab_size`](roberta_configuration.md#RobertaConfig.vocab_size)
- used by: [`_lm_head_name`](modeling_roberta.md#RobertaForCausalLM._lm_head_name)

### `RobertaLayer`  ·  implements/extends Module
- def: [`easydel/modules/roberta/modeling_roberta.py:718`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L718)
- doc: Single RoBERTa transformer encoder layer.
- signature: `class RobertaLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states, mask_info: MaskInfo | None, layer_head_mask, mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, encoder_hidden_states: Float[Array, "batch seq_len hidden_dim"] | None = None, encoder_mask_info: MaskInfo | None = None, output_attentions: bool = False)` — [`L791`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L791) — Forward pass of a single RobertaLayer.
  - `__init__(self, config: RobertaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L737`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L737) — Initialize a single RoBERTa encoder layer.
  - `attention` — [`L759`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L759)
  - `config` — [`L755`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L755)
  - `crossattention` — [`L782`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L782)
  - `dtype` — [`L756`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L756)
  - `intermediate` — [`L767`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L767)
  - `output` — [`L774`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L774)
  - `param_dtype` — [`L757`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L757)
  - `precision` — [`L758`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L758)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`RobertaConfig`](roberta_configuration.md#RobertaConfig), [`RobertaAttention`](modeling_roberta.md#RobertaAttention), `add_cross_attention`, [`RobertaIntermediate`](modeling_roberta.md#RobertaIntermediate), [`RobertaOutput`](modeling_roberta.md#RobertaOutput), `is_decoder`
- used by: [`precision`](modeling_roberta.md#RobertaEncoder.precision)

### `RobertaModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/roberta/modeling_roberta.py:1285`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1285)
- doc: RoBERTa base model implementation.
- signature: `class RobertaModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"], attention_mask: Bool[Array, "batch seq_len"] | None = None, token_type_ids: Int[Array, "batch seq_len"] | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, head_mask: Bool[Array, num_heads] | None = None, encoder_hidden_states: Float[Array, "batch seq_len hidden_dim"] | None = None, encoder_attention_mask: Bool[Array, "batch seq_len"] | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, output_attentions: bool = False, output_hidden_states: bool = False)` — [`L1358`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1358) — Forward pass through the RoBERTa model.
  - `__init__(self, config: RobertaConfig, dtype: jnp.dtype = jnp.float32, param_dtype: jnp.dtype = jnp.float32, precision: lax.Precision | None = None, add_pooling_layer: bool = True, *, rngs: nn.Rngs)` — [`L1304`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1304) — Initialize the RoBERTa base model.
  - `get_decoder(self)` — [`L1490`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1490) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L1504`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1504) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L1484`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1484) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L1497`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1497) — Returns the language model head of the module.
  - `add_pooling_layer` — [`L1356`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1356)
  - `embeddings` — [`L1331`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1331)
  - `encoder` — [`L1338`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1338)
  - `pooler` — [`L1345`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1345)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`RobertaConfig`](roberta_configuration.md#RobertaConfig), [`BaseModelOutputWithPoolingAndCrossAttentions`](../../infra/modeling_outputs.md#BaseModelOutputWithPoolingAndCrossAttentions), [`attentions`](../../infra/modeling_outputs.md#BaseModelOutputWithPastAndCrossAttentions.attentions), [`cross_attentions`](../../infra/modeling_outputs.md#BaseModelOutputWithPastAndCrossAttentions.cross_attentions), [`hidden_states`](../../infra/modeling_outputs.md#BaseModelOutputWithPastAndCrossAttentions.hidden_states), [`last_hidden_state`](../../infra/modeling_outputs.md#BaseModelOutputWithPastAndCrossAttentions.last_hidden_state), [`RobertaEmbeddings`](modeling_roberta.md#RobertaEmbeddings), [`RobertaEncoder`](modeling_roberta.md#RobertaEncoder), [`RobertaPooler`](modeling_roberta.md#RobertaPooler)
- used by: [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`RobertaForCausalLM`](modeling_roberta.md#RobertaForCausalLM), [`RobertaForSequenceClassification`](modeling_roberta.md#RobertaForSequenceClassification), [`__init__`](modeling_roberta.md#RobertaForTokenClassification.__init__), [`__init__`](modeling_roberta.md#RobertaForCausalLM.__init__), [`__init__`](modeling_roberta.md#RobertaForSequenceClassification.__init__), [`RobertaForQuestionAnswering`](modeling_roberta.md#RobertaForQuestionAnswering), [`RobertaForTokenClassification`](modeling_roberta.md#RobertaForTokenClassification), [`__init__`](modeling_roberta.md#RobertaForQuestionAnswering.__init__), [`roberta`](modeling_roberta.md#RobertaForMultipleChoice.roberta), [`get_embedding`](modeling_roberta.md#RobertaForMultipleChoice.get_embedding)

### `RobertaOutput`  ·  implements/extends Module
- def: [`easydel/modules/roberta/modeling_roberta.py:639`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L639)
- doc: Output (down-projection) layer of the RoBERTa feed-forward network.
- signature: `class RobertaOutput(nn.Module):`
- members:
  - `__call__(self, hidden_states, attention_output)` — [`L699`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L699) — Forward pass of the RobertaOutput layer.
  - `__init__(self, config: RobertaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L656`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L656) — Initialize RoBERTa output (down-projection) layer.
  - `LayerNorm` — [`L691`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L691)
  - `config` — [`L674`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L674)
  - `dense` — [`L678`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L678)
  - `dropout` — [`L687`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L687)
  - `dtype` — [`L675`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L675)
  - `param_dtype` — [`L676`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L676)
  - `precision` — [`L677`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L677)
- uses (calls/refs, reference-scoped): [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`RobertaConfig`](roberta_configuration.md#RobertaConfig), [`hidden_size`](roberta_configuration.md#RobertaConfig.hidden_size), [`initializer_range`](roberta_configuration.md#RobertaConfig.initializer_range), [`hidden_dropout_prob`](roberta_configuration.md#RobertaConfig.hidden_dropout_prob), [`layer_norm_eps`](roberta_configuration.md#RobertaConfig.layer_norm_eps), [`intermediate_size`](roberta_configuration.md#RobertaConfig.intermediate_size)
- used by: [`output`](modeling_roberta.md#RobertaLayer.output)

### `RobertaPooler`  ·  implements/extends Module
- def: [`easydel/modules/roberta/modeling_roberta.py:1020`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1020)
- doc: Pooling layer for sequence-level representations.
- signature: `class RobertaPooler(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L1067`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1067) — Forward pass of the RobertaPooler layer.
  - `__init__(self, config: RobertaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L1035`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1035) — Initialize RoBERTa pooler layer.
  - `config` — [`L1053`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1053)
  - `dense` — [`L1057`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1057)
  - `dtype` — [`L1054`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1054)
  - `param_dtype` — [`L1055`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1055)
  - `precision` — [`L1056`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L1056)
- uses (calls/refs, reference-scoped): [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`RobertaConfig`](roberta_configuration.md#RobertaConfig), [`hidden_size`](roberta_configuration.md#RobertaConfig.hidden_size), [`initializer_range`](roberta_configuration.md#RobertaConfig.initializer_range)
- used by: [`pooler`](modeling_roberta.md#RobertaModel.pooler)

### `RobertaSelfAttention`  ·  implements/extends AttentionModule
- def: [`easydel/modules/roberta/modeling_roberta.py:179`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L179)
- doc: Multi-head self-attention module for RoBERTa.
- signature: `class RobertaSelfAttention(AttentionModule):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, layer_head_mask: Bool[Array, num_heads] | None, mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, key_value_states: Float[Array, "batch seq_len hidden_dim"] | None = None, output_attentions: bool = False)` — [`L289`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L289) — Forward pass of the RobertaSelfAttention module.
  - `__init__(self, config: RobertaConfig, causal: bool = False, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L200`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L200) — Initialize RoBERTa self-attention module.
  - `_merge_heads(self, hidden_states)` — [`L277`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L277) — Merges the attention heads into a single hidden state tensor.
  - `_split_heads(self, hidden_states)` — [`L266`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L266) — Splits the hidden states into multiple attention heads.
  - `attention_performer` — [`L234`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L234)
  - `causal` — [`L224`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L224)
  - `dtype` — [`L225`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L225)
  - `head_dim` — [`L228`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L228)
  - `key` — [`L249`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L249)
  - `param_dtype` — [`L226`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L226)
  - `precision` — [`L227`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L227)
  - `query` — [`L241`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L241)
  - `value` — [`L257`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L257)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`config`](../../layers/attention/_flexible.md#AttentionModule.config), [`forward`](../../layers/attention/_flexible.md#FlexibleAttentionModule.forward), [`AttentionLayerOutput`](../../infra/modeling_outputs.md#AttentionLayerOutput), [`concatenate`](../../layers/attention/_flexible.md#AttentionModule.concatenate), [`attention_outputs`](../../operations/_attention_outputs.md#AttentionOutput.attention_outputs), [`AttentionModule`](../../layers/attention/_flexible.md#AttentionModule), [`RobertaConfig`](roberta_configuration.md#RobertaConfig), [`shard_attention_prod`](../../layers/attention/_flexible.md#AttentionModule.shard_attention_prod), [`apply_qkv_shardings`](../../layers/attention/_flexible.md#AttentionModule.apply_qkv_shardings), [`attention_weights`](../../operations/_attention_outputs.md#AttentionOutput.attention_weights), [`__init__`](../../layers/attention/_flexible.md#AttentionModule.__init__)
- used by: [`AttentionModule`](../../layers/attention/_flexible.md#AttentionModule), [`_merge_heads`](../../layers/attention/_flexible.md#AttentionModule._merge_heads), [`self`](modeling_roberta.md#RobertaAttention.self)

### `RobertaSelfOutput`  ·  implements/extends Module
- def: [`easydel/modules/roberta/modeling_roberta.py:395`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L395)
- doc: Output projection layer following RoBERTa self-attention.
- signature: `class RobertaSelfOutput(nn.Module):`
- members:
  - `__call__(self, hidden_states, input_tensor)` — [`L451`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L451) — Forward pass of the RobertaSelfOutput layer.
  - `__init__(self, config: RobertaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L411`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L411) — Initialize RoBERTa self-output projection layer.
  - `LayerNorm` — [`L442`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L442) — documented in [easydel-layers-norms-_norms](../../../../concepts/easydel-layers-norms-_norms.md)
  - `config` — [`L429`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L429)
  - `dense` — [`L433`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L433)
  - `dropout` — [`L449`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L449)
  - `dtype` — [`L430`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L430)
  - `param_dtype` — [`L431`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L431)
  - `precision` — [`L432`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/modeling_roberta.py#L432)
- uses (calls/refs, reference-scoped): [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`RobertaConfig`](roberta_configuration.md#RobertaConfig), [`hidden_size`](roberta_configuration.md#RobertaConfig.hidden_size), [`initializer_range`](roberta_configuration.md#RobertaConfig.initializer_range), [`hidden_dropout_prob`](roberta_configuration.md#RobertaConfig.hidden_dropout_prob), [`layer_norm_eps`](roberta_configuration.md#RobertaConfig.layer_norm_eps)
- used by: [`output`](modeling_roberta.md#RobertaAttention.output)

