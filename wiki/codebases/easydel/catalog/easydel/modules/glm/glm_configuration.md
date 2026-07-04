---
title: 'Module: easydel/modules/glm/glm_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/glm/glm_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.glm.glm_configuration`/GlmConfig#
symbols:
  GlmConfig: ''
  GlmConfig.layer_types: layer_types.
  GlmConfig.hidden_size: hidden_size.
  GlmConfig.intermediate_size: intermediate_size.
  GlmConfig.initializer_range: initializer_range.
  GlmConfig.rms_norm_eps: rms_norm_eps.
  GlmConfig.vocab_size: vocab_size.
  GlmConfig.num_hidden_layers: num_hidden_layers.
  GlmConfig.hidden_act: hidden_act.
  GlmConfig.model_type: model_type.
  GlmConfig.__init__: __init__().
  GlmConfig.max_position_embeddings: max_position_embeddings.
  GlmConfig.num_attention_heads: num_attention_heads.
  GlmConfig.partial_rotary_factor: partial_rotary_factor.
  GlmConfig.head_dim: head_dim.
  GlmConfig.num_key_value_heads: num_key_value_heads.
  GlmConfig.use_cache: use_cache.
  GlmConfig.rope_theta: rope_theta.
  GlmConfig.attention_bias: attention_bias.
  GlmConfig.attention_dropout: attention_dropout.
  GlmConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/glm/glm_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py)

## Classes
### `GlmConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/glm/glm_configuration.py:23`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L23)
- doc: This is the configuration class to store the configuration of a \[`GlmModel`\]. It is used to instantiate an Glm
- signature: `class GlmConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L146) — Returns partition rules for model sharding.
  - `attention_bias` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L132)
  - `attention_dropout` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L133)
  - `head_dim` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L125)
  - `hidden_act` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L127)
  - `hidden_size` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L120)
  - `initializer_range` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L128)
  - `intermediate_size` — [`L121`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L121)
  - `layer_types` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L134)
  - `max_position_embeddings` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L119)
  - `model_type` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L89)
  - `num_attention_heads` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L123)
  - `num_hidden_layers` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L122)
  - `num_key_value_heads` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L126)
  - `partial_rotary_factor` — [`L124`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L124)
  - `rms_norm_eps` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L129)
  - `rope_theta` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L131)
  - `use_cache` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L130)
  - `vocab_size` — [`L118`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L118)
- protocol/private: `__init__`[`L91`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm/glm_configuration.py#L91)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`GlmModel`](modeling_glm.md#GlmModel), [`GlmForCausalLM`](modeling_glm.md#GlmForCausalLM), [`GlmForSequenceClassification`](modeling_glm.md#GlmForSequenceClassification), [`act_fn`](modeling_glm.md#GlmMLP.act_fn), [`input_layernorm`](modeling_glm.md#GlmDecoderLayer.input_layernorm), [`post_attention_layernorm`](modeling_glm.md#GlmDecoderLayer.post_attention_layernorm), [`__init__`](modeling_glm.md#GlmForCausalLM.__init__), [`__init__`](modeling_glm.md#GlmForSequenceClassification.__init__), [`precision`](modeling_glm.md#GlmMLP.precision), [`down_proj`](modeling_glm.md#GlmMLP.down_proj), [`gate_up_proj`](modeling_glm.md#GlmMLP.gate_up_proj), [`__init__`](modeling_glm.md#GlmModel.__init__), [`__init__`](modeling_glm.md#GlmAttention.__init__), [`__init__`](modeling_glm.md#GlmDecoderLayer.__init__), [`__init__`](modeling_glm.md#GlmMLP.__init__), [`_config_class`](modeling_glm.md#GlmForCausalLM._config_class), [`_config_class`](modeling_glm.md#GlmForSequenceClassification._config_class), [`vocab_size`](modeling_glm.md#GlmModel.vocab_size)

