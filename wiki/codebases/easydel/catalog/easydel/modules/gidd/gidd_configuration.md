---
title: 'Module: easydel/modules/gidd/gidd_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/gidd/gidd_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.gidd.gidd_configuration`/GiddConfig#
symbols:
  GiddConfig.attach_custom_arguments: attach_custom_arguments().
  GiddConfig: ''
  GiddConfig.hidden_size: hidden_size.
  GiddConfig.layer_types: layer_types.
  GiddConfig.__init__: __init__().
  GiddConfig.num_attention_heads: num_attention_heads.
  GiddConfig.init_scale: init_scale.
  GiddConfig.max_position_embeddings: max_position_embeddings.
  GiddConfig.attention_bias: attention_bias.
  GiddConfig.mlp_bias: mlp_bias.
  GiddConfig.granted_freq_max_position_embedding: granted_freq_max_position_embedding().
  GiddConfig.granted_mask_max_position_embedding: granted_mask_max_position_embedding().
  GiddConfig.intermediate_size: intermediate_size.
  GiddConfig.num_hidden_layers: num_hidden_layers.
  GiddConfig.gradient_checkpointing: gradient_checkpointing.
  GiddConfig.vocab_size: vocab_size.
  GiddConfig.head_init_scale: head_init_scale.
  GiddConfig.rope_theta: rope_theta.
  GiddConfig.resid_scale: resid_scale.
  GiddConfig.rms_norm_eps: rms_norm_eps.
  GiddConfig.use_qk_norm: use_qk_norm.
  GiddConfig.qk_norm_eps: qk_norm_eps.
  GiddConfig.tie_word_embeddings: tie_word_embeddings.
  GiddConfig.bits: bits.
  GiddConfig.scan_layers: scan_layers.
  GiddConfig.model_type: model_type.
  GiddConfig.emb_init_scale: emb_init_scale.
  GiddConfig.pretraining_tp: pretraining_tp.
  GiddConfig.rope_scaling: rope_scaling.
  GiddConfig.head_dim: head_dim.
  GiddConfig.get_partition_rules: get_partition_rules().
  GiddConfig.get_weight_decay_exclusions: get_weight_decay_exclusions().
  GiddConfig.rng_keys: rng_keys().
---
# Module: [`easydel/modules/gidd/gidd_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py)

## Classes
### `GiddConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/gidd/gidd_configuration.py:23`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L23)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class GiddConfig(EasyDeLBaseConfig):`
- members:
  - `attach_custom_arguments(self, tie_word_embeddings: bool = False, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, bits: int | None = None, rope_theta: float = 10000, attention_bias: bool = False, mlp_bias: bool = False, scan_layers: bool = True, **kwargs)` — [`L174`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L174) — The attach_custom_arguments function adds the following arguments to the Transformer class:
  - `get_partition_rules(self, *args, **kwargs)` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L161) — Returns partition rules for model sharding.
  - `get_weight_decay_exclusions()` — [`L222`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L222)
  - `granted_freq_max_position_embedding(self)` — [`L230`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L230)
  - `granted_mask_max_position_embedding(self)` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L238)
  - `rng_keys()` — [`L226`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L226)
  - `attention_bias` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L144)
  - `bits` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L147)
  - `emb_init_scale` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L130)
  - `gradient_checkpointing` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L143)
  - `head_dim` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L149)
  - `head_init_scale` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L131)
  - `hidden_size` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L128)
  - `init_scale` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L129)
  - `intermediate_size` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L132)
  - `layer_types` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L150)
  - `max_position_embeddings` — [`L136`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L136)
  - `mlp_bias` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L145)
  - `model_type` — [`L93`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L93)
  - `num_attention_heads` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L135)
  - `num_hidden_layers` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L133)
  - `pretraining_tp` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L141)
  - `qk_norm_eps` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L140)
  - `resid_scale` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L137)
  - `rms_norm_eps` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L138)
  - `rope_scaling` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L146)
  - `rope_theta` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L134)
  - `scan_layers` — [`L148`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L148)
  - `tie_word_embeddings` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L142)
  - `use_qk_norm` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L139)
  - `vocab_size` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L126)
- protocol/private: `__init__`[`L95`](../../../../../../../raw/code/EasyDeL/easydel/modules/gidd/gidd_configuration.py#L95)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`granted_freq_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_freq_max_position_embedding), [`qk_scale`](modeling_gidd.md#GiddAttention.qk_scale), [`granted_mask_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_mask_max_position_embedding), [`embed_tokens`](modeling_gidd.md#GiddModel.embed_tokens), [`GiddModel`](modeling_gidd.md#GiddModel), [`GiddForDiffusionLM`](modeling_gidd.md#GiddForDiffusionLM), [`lm_head`](modeling_gidd.md#GiddForDiffusionLM.lm_head), [`qk_norm_eps`](modeling_gidd.md#GiddAttention.qk_norm_eps), [`precision`](modeling_gidd.md#GiddMLP.precision), [`kernel`](modeling_gidd.md#GiddRMSNorm.kernel), [`k_proj`](modeling_gidd.md#GiddAttention.k_proj), [`o_proj`](modeling_gidd.md#GiddAttention.o_proj), [`q_proj`](modeling_gidd.md#GiddAttention.q_proj), [`v_proj`](modeling_gidd.md#GiddAttention.v_proj), [`attach_custom_arguments`](../../infra/base_config.md#EasyDeLBaseConfig.attach_custom_arguments), [`down_proj`](modeling_gidd.md#GiddMLP.down_proj), [`epsilon`](modeling_gidd.md#GiddRMSNorm.epsilon), [`resid_scale`](modeling_gidd.md#GiddModel.resid_scale), [`up_proj`](modeling_gidd.md#GiddMLP.up_proj), [`use_qk_norm`](modeling_gidd.md#GiddAttention.use_qk_norm), [`__init__`](modeling_gidd.md#GiddAttention.__init__), [`__init__`](modeling_gidd.md#GiddForDiffusionLM.__init__), [`__init__`](modeling_gidd.md#GiddModel.__init__), [`hidden_size`](modeling_gidd.md#GiddAttention.hidden_size), [`__init__`](modeling_gidd.md#GiddLayer.__init__), [`__init__`](modeling_gidd.md#GiddMLP.__init__), [`__init__`](modeling_gidd.md#GiddRMSNorm.__init__)

