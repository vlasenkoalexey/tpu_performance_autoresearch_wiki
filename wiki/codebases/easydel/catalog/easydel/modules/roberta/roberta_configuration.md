---
title: 'Module: easydel/modules/roberta/roberta_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/roberta/roberta_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.roberta.roberta_configuration`/RobertaConfig#
symbols:
  RobertaConfig: ''
  RobertaConfig.hidden_size: hidden_size.
  RobertaConfig.initializer_range: initializer_range.
  RobertaConfig.layer_types: layer_types.
  RobertaConfig.hidden_dropout_prob: hidden_dropout_prob.
  RobertaConfig.layer_norm_eps: layer_norm_eps.
  RobertaConfig.classifier_dropout: classifier_dropout.
  RobertaConfig.vocab_size: vocab_size.
  RobertaConfig.intermediate_size: intermediate_size.
  RobertaConfig.gradient_checkpointing: gradient_checkpointing.
  RobertaConfig.num_hidden_layers: num_hidden_layers.
  RobertaConfig.max_position_embeddings: max_position_embeddings.
  RobertaConfig.type_vocab_size: type_vocab_size.
  RobertaConfig.hidden_act: hidden_act.
  RobertaConfig.model_type: model_type.
  RobertaConfig.__init__: __init__().
  RobertaConfig.num_attention_heads: num_attention_heads.
  RobertaConfig.attention_probs_dropout_prob: attention_probs_dropout_prob.
  RobertaConfig.position_embedding_type: position_embedding_type.
  RobertaConfig.use_cache: use_cache.
  RobertaConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/roberta/roberta_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py)

## Classes
### `RobertaConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/roberta/roberta_configuration.py:23`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L23)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class RobertaConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L125) — Returns partition rules for model sharding.
  - `attention_probs_dropout_prob` — [`L106`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L106)
  - `classifier_dropout` — [`L113`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L113)
  - `gradient_checkpointing` — [`L114`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L114)
  - `hidden_act` — [`L103`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L103)
  - `hidden_dropout_prob` — [`L105`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L105)
  - `hidden_size` — [`L100`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L100)
  - `initializer_range` — [`L109`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L109)
  - `intermediate_size` — [`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L104)
  - `layer_norm_eps` — [`L110`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L110)
  - `layer_types` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L115)
  - `max_position_embeddings` — [`L107`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L107)
  - `model_type` — [`L73`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L73)
  - `num_attention_heads` — [`L102`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L102)
  - `num_hidden_layers` — [`L101`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L101)
  - `position_embedding_type` — [`L111`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L111)
  - `type_vocab_size` — [`L108`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L108)
  - `use_cache` — [`L112`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L112)
  - `vocab_size` — [`L99`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L99)
- protocol/private: `__init__`[`L75`](../../../../../../../raw/code/EasyDeL/easydel/modules/roberta/roberta_configuration.py#L75)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`RobertaModel`](modeling_roberta.md#RobertaModel), [`RobertaForCausalLM`](modeling_roberta.md#RobertaForCausalLM), [`RobertaForSequenceClassification`](modeling_roberta.md#RobertaForSequenceClassification), [`dense`](modeling_roberta.md#RobertaClassificationHead.dense), [`decoder`](modeling_roberta.md#RobertaLMHead.decoder), [`bias`](modeling_roberta.md#RobertaLMHead.bias), [`dense`](modeling_roberta.md#RobertaIntermediate.dense), [`dense`](modeling_roberta.md#RobertaOutput.dense), [`position_embeddings`](modeling_roberta.md#RobertaEmbeddings.position_embeddings), [`token_type_embeddings`](modeling_roberta.md#RobertaEmbeddings.token_type_embeddings), [`word_embeddings`](modeling_roberta.md#RobertaEmbeddings.word_embeddings), [`__init__`](modeling_roberta.md#RobertaForTokenClassification.__init__), [`LayerNorm`](modeling_roberta.md#RobertaEmbeddings.LayerNorm), [`LayerNorm`](modeling_roberta.md#RobertaOutput.LayerNorm), [`LayerNorm`](modeling_roberta.md#RobertaSelfOutput.LayerNorm), [`dense`](modeling_roberta.md#RobertaLMHead.dense), [`dense`](modeling_roberta.md#RobertaPooler.dense), [`dense`](modeling_roberta.md#RobertaSelfOutput.dense), [`layer_norm`](modeling_roberta.md#RobertaLMHead.layer_norm), [`out_proj`](modeling_roberta.md#RobertaClassificationHead.out_proj), [`__init__`](modeling_roberta.md#RobertaForCausalLM.__init__), [`__init__`](modeling_roberta.md#RobertaForSequenceClassification.__init__), [`_lm_head_name`](modeling_roberta.md#RobertaForCausalLM._lm_head_name), [`precision`](modeling_roberta.md#RobertaEncoder.precision), [`RobertaForQuestionAnswering`](modeling_roberta.md#RobertaForQuestionAnswering), [`RobertaForTokenClassification`](modeling_roberta.md#RobertaForTokenClassification), [`activation`](modeling_roberta.md#RobertaIntermediate.activation), [`__init__`](modeling_roberta.md#RobertaForQuestionAnswering.__init__), [`layer`](modeling_roberta.md#RobertaEncoder.layer), [`dropout`](modeling_roberta.md#RobertaEmbeddings.dropout), [`dropout`](modeling_roberta.md#RobertaOutput.dropout), [`dropout`](modeling_roberta.md#RobertaSelfOutput.dropout), [`__init__`](modeling_roberta.md#RobertaForMultipleChoice.__init__), [`__init__`](modeling_roberta.md#RobertaModel.__init__), [`__init__`](modeling_roberta.md#RobertaSelfAttention.__init__), [`__init__`](modeling_roberta.md#RobertaAttention.__init__), [`__init__`](modeling_roberta.md#RobertaClassificationHead.__init__)  (+9 more)

