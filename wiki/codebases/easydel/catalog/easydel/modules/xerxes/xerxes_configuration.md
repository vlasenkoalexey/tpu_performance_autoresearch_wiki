---
title: 'Module: easydel/modules/xerxes/xerxes_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/xerxes/xerxes_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.xerxes.xerxes_configuration`/XerxesConfig#
symbols:
  XerxesConfig.layer_types: layer_types.
  XerxesConfig: ''
  XerxesConfig.get_mask_details: get_mask_details().
  XerxesConfig.hidden_size: hidden_size.
  XerxesConfig.xe_kvnorm: xe_kvnorm.
  XerxesConfig.__init__: __init__().
  XerxesConfig.window_pattern: window_pattern.
  XerxesConfig.xe_moe: xe_moe.
  XerxesConfig.intermediate_size: intermediate_size.
  XerxesConfig.sliding_window: sliding_window.
  XerxesConfig.num_local_experts: num_local_experts.
  XerxesConfig.num_hidden_layers: num_hidden_layers.
  XerxesConfig.initializer_range: initializer_range.
  XerxesConfig.swish_run: swish_run.
  XerxesConfig.xe_mlpnorm: xe_mlpnorm.
  XerxesConfig.num_experts_per_tok: num_experts_per_tok.
  XerxesConfig.rms_norm_eps: rms_norm_eps.
  XerxesConfig.gradient_checkpointing: gradient_checkpointing.
  XerxesConfig.model_type: model_type.
  XerxesConfig.bits: bits.
  XerxesConfig.scan_layers: scan_layers.
  XerxesConfig.vocab_size: vocab_size.
  XerxesConfig.max_position_embeddings: max_position_embeddings.
  XerxesConfig.num_attention_heads: num_attention_heads.
  XerxesConfig.head_dim: head_dim.
  XerxesConfig.num_key_value_heads: num_key_value_heads.
  XerxesConfig.use_cache: use_cache.
  XerxesConfig.rope_theta: rope_theta.
  XerxesConfig.rope_scaling: rope_scaling.
  XerxesConfig.cache_implementation: cache_implementation.
  XerxesConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/xerxes/xerxes_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py)

## Classes
### `XerxesConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/xerxes/xerxes_configuration.py:25`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L25)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class XerxesConfig(EasyDeLBaseConfig):`
- members:
  - `get_mask_details(self)` — [`L177`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L177) — Retrieve attention mask details for each layer in the model.
  - `get_partition_rules(self, *args, **kwargs)` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L164) — Returns partition rules for model sharding.
  - `bits` — [`L114`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L114)
  - `cache_implementation` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L162)
  - `gradient_checkpointing` — [`L113`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L113)
  - `head_dim` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L122)
  - `hidden_size` — [`L118`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L118)
  - `initializer_range` — [`L124`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L124)
  - `intermediate_size` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L119)
  - `layer_types` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L138)
  - `max_position_embeddings` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L117)
  - `model_type` — [`L78`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L78)
  - `num_attention_heads` — [`L121`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L121)
  - `num_experts_per_tok` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L129)
  - `num_hidden_layers` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L120)
  - `num_key_value_heads` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L123)
  - `num_local_experts` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L128)
  - `rms_norm_eps` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L125)
  - `rope_scaling` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L137)
  - `rope_theta` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L127)
  - `scan_layers` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L115)
  - `sliding_window` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L135)
  - `swish_run` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L130)
  - `use_cache` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L126)
  - `vocab_size` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L116)
  - `window_pattern` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L134)
  - `xe_kvnorm` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L132)
  - `xe_mlpnorm` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L133)
  - `xe_moe` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L131)
- protocol/private: `__init__`[`L80`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes/xerxes_configuration.py#L80)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`from_hf`](../../infra/utils.md#AttnMaskType.from_hf)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`__call__`](modeling_xerxes.md#XerxesDecoderLayer.__call__), [`__call__`](modeling_xerxes.md#XerxesSparseMoeBlock.__call__), [`embed_tokens`](modeling_xerxes.md#XerxesModel.embed_tokens), [`mlp`](modeling_xerxes.md#XerxesDecoderLayer.mlp), [`XerxesForCausalLM`](modeling_xerxes.md#XerxesForCausalLM), [`XerxesModel`](modeling_xerxes.md#XerxesModel), [`gate`](modeling_xerxes.md#XerxesSparseMoeBlock.gate), [`is_local_attn`](modeling_xerxes.md#XerxesAttention.is_local_attn), [`__init__`](modeling_xerxes.md#XerxesForCausalLM.__init__), [`rngs`](modeling_xerxes.md#XerxesDecoderLayer.rngs), [`experts`](modeling_xerxes.md#XerxesSparseMoeBlock.experts), [`act`](modeling_xerxes.md#XerxesMLP.act), [`down_proj`](modeling_xerxes.md#XerxesMLP.down_proj), [`embedding_scale`](modeling_xerxes.md#XerxesModel.embedding_scale), [`gate_proj`](modeling_xerxes.md#XerxesMLP.gate_proj), [`up_proj`](modeling_xerxes.md#XerxesMLP.up_proj), [`xe_kvnorm`](modeling_xerxes.md#XerxesAttention.xe_kvnorm), [`__init__`](modeling_xerxes.md#XerxesModel.__init__), [`__init__`](modeling_xerxes.md#XerxesSparseMoeBlock.__init__), [`__init__`](modeling_xerxes.md#XerxesAttention.__init__), [`__init__`](modeling_xerxes.md#XerxesDecoderLayer.__init__), [`__init__`](modeling_xerxes.md#XerxesMLP.__init__), [`_config_class`](modeling_xerxes.md#XerxesForCausalLM._config_class), [`rngs`](modeling_xerxes.md#XerxesMLP.rngs)

