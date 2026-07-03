---
title: 'Module: easydel/modules/gemma/gemma_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/gemma/gemma_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.gemma.gemma_configuration`/GemmaConfig#
symbols:
  GemmaConfig: ''
  GemmaConfig.layer_types: layer_types.
  GemmaConfig.__init__: __init__().
  GemmaConfig.hidden_size: hidden_size.
  GemmaConfig.intermediate_size: intermediate_size.
  GemmaConfig.hidden_act: hidden_act.
  GemmaConfig.hidden_activation: hidden_activation.
  GemmaConfig.gradient_checkpointing: gradient_checkpointing.
  GemmaConfig.num_hidden_layers: num_hidden_layers.
  GemmaConfig.initializer_range: initializer_range.
  GemmaConfig.rms_norm_eps: rms_norm_eps.
  GemmaConfig.rope_theta: rope_theta.
  GemmaConfig.model_type: model_type.
  GemmaConfig.bits: bits.
  GemmaConfig.scan_layers: scan_layers.
  GemmaConfig.vocab_size: vocab_size.
  GemmaConfig.max_position_embeddings: max_position_embeddings.
  GemmaConfig.num_attention_heads: num_attention_heads.
  GemmaConfig.head_dim: head_dim.
  GemmaConfig.num_key_value_heads: num_key_value_heads.
  GemmaConfig.use_cache: use_cache.
  GemmaConfig.attention_bias: attention_bias.
  GemmaConfig.attention_dropout: attention_dropout.
  GemmaConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/gemma/gemma_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py)

## Classes
### `GemmaConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/gemma/gemma_configuration.py:24`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L24)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class GemmaConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L143) — Returns partition rules for model sharding.
  - `attention_bias` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L128)
  - `attention_dropout` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L129)
  - `bits` — [`L113`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L113)
  - `gradient_checkpointing` — [`L112`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L112)
  - `head_dim` — [`L121`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L121)
  - `hidden_act` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L123)
  - `hidden_activation` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L130)
  - `hidden_size` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L117)
  - `initializer_range` — [`L124`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L124)
  - `intermediate_size` — [`L118`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L118)
  - `layer_types` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L131)
  - `max_position_embeddings` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L116)
  - `model_type` — [`L82`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L82)
  - `num_attention_heads` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L120)
  - `num_hidden_layers` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L119)
  - `num_key_value_heads` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L122)
  - `rms_norm_eps` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L125)
  - `rope_theta` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L127)
  - `scan_layers` — [`L114`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L114)
  - `use_cache` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L126)
  - `vocab_size` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L115)
- protocol/private: `__init__`[`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/gemma/gemma_configuration.py#L84)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`embed_tokens`](modeling_gemma.md#GemmaModel.embed_tokens), [`GemmaModel`](modeling_gemma.md#GemmaModel), [`GemmaForCausalLM`](modeling_gemma.md#GemmaForCausalLM), [`GemmaForSequenceClassification`](modeling_gemma.md#GemmaForSequenceClassification), [`precision`](modeling_gemma.md#GemmaMLP.precision), [`kernel`](modeling_gemma.md#GemmaRMSNorm.kernel), [`_create_rotary`](modeling_gemma.md#GemmaAttention._create_rotary), [`__init__`](modeling_gemma.md#GemmaForCausalLM.__init__), [`__init__`](modeling_gemma.md#GemmaForSequenceClassification.__init__), [`epsilon`](modeling_gemma.md#GemmaRMSNorm.epsilon), [`__init__`](modeling_gemma.md#GemmaAttention.__init__), [`__init__`](modeling_gemma.md#GemmaModel.__init__), [`__init__`](modeling_gemma.md#GemmaDecoderLayer.__init__), [`__init__`](modeling_gemma.md#GemmaMLP.__init__), [`__init__`](modeling_gemma.md#GemmaRMSNorm.__init__), [`_config_class`](modeling_gemma.md#GemmaForCausalLM._config_class), [`_config_class`](modeling_gemma.md#GemmaForSequenceClassification._config_class)

