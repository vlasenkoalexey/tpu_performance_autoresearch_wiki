---
title: 'Module: easydel/modules/gpt_oss/gpt_oss_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/gpt_oss/gpt_oss_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.gpt_oss.gpt_oss_configuration`/
symbols:
  GptOssConfig: GptOssConfig#
  GptOssConfig.layer_types: GptOssConfig#layer_types.
  GptOssConfig.hidden_size: GptOssConfig#hidden_size.
  GptOssConfig.num_local_experts: GptOssConfig#num_local_experts.
  GptOssConfig.head_dim: GptOssConfig#head_dim.
  GptOssConfig.intermediate_size: GptOssConfig#intermediate_size.
  GptOssConfig.rms_norm_eps: GptOssConfig#rms_norm_eps.
  GptOssConfig.rope_scaling: GptOssConfig#rope_scaling.
  GptOssConfig.mlp_activations_limit: GptOssConfig#mlp_activations_limit.
  GptOssConfig.num_hidden_layers: GptOssConfig#num_hidden_layers.
  GptOssConfig.num_attention_heads: GptOssConfig#num_attention_heads.
  GptOssConfig.initializer_range: GptOssConfig#initializer_range.
  GptOssConfig.vocab_size: GptOssConfig#vocab_size.
  GptOssConfig.sliding_window: GptOssConfig#sliding_window.
  GptOssConfig.num_experts_per_tok: GptOssConfig#num_experts_per_tok.
  GptOssConfig.hidden_act: GptOssConfig#hidden_act.
  GptOssConfig.router_aux_loss_coef: GptOssConfig#router_aux_loss_coef.
  GptOssConfig.model_type: GptOssConfig#model_type.
  GptOssConfig.__init__: GptOssConfig#__init__().
  GptOssConfig.num_key_value_heads: GptOssConfig#num_key_value_heads.
  GptOssConfig.rope_theta: GptOssConfig#rope_theta.
  GptOssConfig.attention_dropout: GptOssConfig#attention_dropout.
  GptOssConfig.attention_bias: GptOssConfig#attention_bias.
  GptOssConfig.max_position_embeddings: GptOssConfig#max_position_embeddings.
  GptOssConfig.output_router_logits: GptOssConfig#output_router_logits.
  GptOssConfig.use_cache: GptOssConfig#use_cache.
  GptOssConfig.get_partition_rules: GptOssConfig#get_partition_rules().
  __all__: __all__.
---
# Module: [`easydel/modules/gpt_oss/gpt_oss_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py)

## Classes
### `GptOssConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/gpt_oss/gpt_oss_configuration.py:33`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L33)
- doc: Configuration class for GPT-OSS model.
- signature: `class GptOssConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L144) — Returns partition rules for model sharding.
  - `attention_bias` — [`L136`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L136)
  - `attention_dropout` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L125)
  - `head_dim` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L126)
  - `hidden_act` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L120)
  - `hidden_size` — [`L109`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L109)
  - `initializer_range` — [`L121`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L121)
  - `intermediate_size` — [`L110`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L110)
  - `layer_types` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L127)
  - `max_position_embeddings` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L137)
  - `mlp_activations_limit` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L141)
  - `model_type` — [`L77`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L77)
  - `num_attention_heads` — [`L112`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L112)
  - `num_experts_per_tok` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L115)
  - `num_hidden_layers` — [`L111`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L111)
  - `num_key_value_heads` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L119)
  - `num_local_experts` — [`L113`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L113)
  - `output_router_logits` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L139)
  - `rms_norm_eps` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L122)
  - `rope_scaling` — [`L124`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L124)
  - `rope_theta` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L123)
  - `router_aux_loss_coef` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L138)
  - `sliding_window` — [`L114`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L114)
  - `use_cache` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L140)
  - `vocab_size` — [`L108`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L108)
- protocol/private: `__init__`[`L79`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L79)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`__init__`](modeling_gpt_oss.md#GptOssMLP.__init__), [`embed_tokens`](modeling_gpt_oss.md#GptOssModel.embed_tokens), [`GptOssModel`](modeling_gpt_oss.md#GptOssModel), [`down_proj`](modeling_gpt_oss.md#GptOssExperts.down_proj), [`gate_proj`](modeling_gpt_oss.md#GptOssExperts.gate_proj), [`up_proj`](modeling_gpt_oss.md#GptOssExperts.up_proj), [`GptOssForCausalLM`](modeling_gpt_oss.md#GptOssForCausalLM), [`GptOssForSequenceClassification`](modeling_gpt_oss.md#GptOssForSequenceClassification), [`router`](modeling_gpt_oss.md#GptOssMLP.router), [`__init__`](modeling_gpt_oss.md#GptOssAttention.__init__), [`__init__`](modeling_gpt_oss.md#GptOssForCausalLM.__init__), [`sinks`](modeling_gpt_oss.md#GptOssAttention.sinks), [`input_layernorm`](modeling_gpt_oss.md#GptOssDecoderLayer.input_layernorm), [`norm`](modeling_gpt_oss.md#GptOssModel.norm), [`post_attention_layernorm`](modeling_gpt_oss.md#GptOssDecoderLayer.post_attention_layernorm), [`__init__`](modeling_gpt_oss.md#GptOssForSequenceClassification.__init__), [`act_fn`](modeling_gpt_oss.md#GptOssExperts.act_fn), [`__init__`](modeling_gpt_oss.md#GptOssModel.__init__), [`layers`](modeling_gpt_oss.md#GptOssModel.layers), [`intermediate_size`](modeling_gpt_oss.md#GptOssExperts.intermediate_size), [`__init__`](modeling_gpt_oss.md#GptOssDecoderLayer.__init__), [`__init__`](modeling_gpt_oss.md#GptOssExperts.__init__), [`_config_class`](modeling_gpt_oss.md#GptOssForCausalLM._config_class), [`_config_class`](modeling_gpt_oss.md#GptOssForSequenceClassification._config_class), [`attention_type`](modeling_gpt_oss.md#GptOssDecoderLayer.attention_type), [`hidden_size`](modeling_gpt_oss.md#GptOssExperts.hidden_size), [`num_experts`](modeling_gpt_oss.md#GptOssExperts.num_experts)

## Module values
- `__all__` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_oss/gpt_oss_configuration.py#L158)

