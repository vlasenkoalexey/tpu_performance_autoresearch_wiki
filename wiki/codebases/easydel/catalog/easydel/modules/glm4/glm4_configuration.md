---
title: 'Module: easydel/modules/glm4/glm4_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/glm4/glm4_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.glm4.glm4_configuration`/
symbols:
  Glm4Config: Glm4Config#
  Glm4Config.layer_types: Glm4Config#layer_types.
  Glm4Config.hidden_size: Glm4Config#hidden_size.
  Glm4Config.rms_norm_eps: Glm4Config#rms_norm_eps.
  Glm4Config.intermediate_size: Glm4Config#intermediate_size.
  Glm4Config.initializer_range: Glm4Config#initializer_range.
  Glm4Config.vocab_size: Glm4Config#vocab_size.
  Glm4Config.num_hidden_layers: Glm4Config#num_hidden_layers.
  Glm4Config.hidden_act: Glm4Config#hidden_act.
  Glm4Config.model_type: Glm4Config#model_type.
  Glm4Config.__init__: Glm4Config#__init__().
  Glm4Config.max_position_embeddings: Glm4Config#max_position_embeddings.
  Glm4Config.num_attention_heads: Glm4Config#num_attention_heads.
  Glm4Config.partial_rotary_factor: Glm4Config#partial_rotary_factor.
  Glm4Config.head_dim: Glm4Config#head_dim.
  Glm4Config.num_key_value_heads: Glm4Config#num_key_value_heads.
  Glm4Config.use_cache: Glm4Config#use_cache.
  Glm4Config.rope_theta: Glm4Config#rope_theta.
  Glm4Config.attention_bias: Glm4Config#attention_bias.
  Glm4Config.attention_dropout: Glm4Config#attention_dropout.
  Glm4Config.get_partition_rules: Glm4Config#get_partition_rules().
  __all__: __all__.
---
# Module: [`easydel/modules/glm4/glm4_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py)

## Classes
### `Glm4Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/glm4/glm4_configuration.py:23`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L23)
- doc: This is the configuration class to store the configuration of a \[`Glm4Model`\]. It is used to instantiate an Glm4
- signature: `class Glm4Config(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L146) — Returns partition rules for model sharding.
  - `attention_bias` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L132)
  - `attention_dropout` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L133)
  - `head_dim` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L125)
  - `hidden_act` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L127)
  - `hidden_size` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L120)
  - `initializer_range` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L128)
  - `intermediate_size` — [`L121`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L121)
  - `layer_types` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L134)
  - `max_position_embeddings` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L119)
  - `model_type` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L89)
  - `num_attention_heads` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L123)
  - `num_hidden_layers` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L122)
  - `num_key_value_heads` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L126)
  - `partial_rotary_factor` — [`L124`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L124)
  - `rms_norm_eps` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L129)
  - `rope_theta` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L131)
  - `use_cache` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L130)
  - `vocab_size` — [`L118`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L118)
- protocol/private: `__init__`[`L91`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L91)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`Glm4Model`](modeling_glm4.md#Glm4Model), [`Glm4ForCausalLM`](modeling_glm4.md#Glm4ForCausalLM), [`Glm4ForSequenceClassification`](modeling_glm4.md#Glm4ForSequenceClassification), [`act_fn`](modeling_glm4.md#Glm4MLP.act_fn), [`input_layernorm`](modeling_glm4.md#Glm4DecoderLayer.input_layernorm), [`post_attention_layernorm`](modeling_glm4.md#Glm4DecoderLayer.post_attention_layernorm), [`post_mlp_layernorm`](modeling_glm4.md#Glm4DecoderLayer.post_mlp_layernorm), [`post_self_attn_layernorm`](modeling_glm4.md#Glm4DecoderLayer.post_self_attn_layernorm), [`__init__`](modeling_glm4.md#Glm4ForCausalLM.__init__), [`__init__`](modeling_glm4.md#Glm4ForSequenceClassification.__init__), [`precision`](modeling_glm4.md#Glm4MLP.precision), [`down_proj`](modeling_glm4.md#Glm4MLP.down_proj), [`gate_up_proj`](modeling_glm4.md#Glm4MLP.gate_up_proj), [`__init__`](modeling_glm4.md#Glm4Model.__init__), [`__init__`](modeling_glm4.md#Glm4Attention.__init__), [`__init__`](modeling_glm4.md#Glm4DecoderLayer.__init__), [`__init__`](modeling_glm4.md#Glm4MLP.__init__), [`_config_class`](modeling_glm4.md#Glm4ForCausalLM._config_class), [`_config_class`](modeling_glm4.md#Glm4ForSequenceClassification._config_class), [`vocab_size`](modeling_glm4.md#Glm4Model.vocab_size)

## Module values
- `__all__` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm4/glm4_configuration.py#L160)

