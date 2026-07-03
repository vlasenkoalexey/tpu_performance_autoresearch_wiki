---
title: 'Module: easydel/modules/exaone/exaone_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/exaone/exaone_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.exaone.exaone_configuration`/ExaoneConfig#
symbols:
  ExaoneConfig: ''
  ExaoneConfig.layer_types: layer_types.
  ExaoneConfig.hidden_size: hidden_size.
  ExaoneConfig.intermediate_size: intermediate_size.
  ExaoneConfig.__init__: __init__().
  ExaoneConfig.granted_freq_max_position_embedding: granted_freq_max_position_embedding().
  ExaoneConfig.granted_mask_max_position_embedding: granted_mask_max_position_embedding().
  ExaoneConfig.max_position_embeddings: max_position_embeddings.
  ExaoneConfig.num_attention_heads: num_attention_heads.
  ExaoneConfig.layer_norm_epsilon: layer_norm_epsilon.
  ExaoneConfig.num_hidden_layers: num_hidden_layers.
  ExaoneConfig.activation_function: activation_function.
  ExaoneConfig.gradient_checkpointing: gradient_checkpointing.
  ExaoneConfig.use_scan_mlp: use_scan_mlp.
  ExaoneConfig.scan_mlp_chunk_size: scan_mlp_chunk_size.
  ExaoneConfig.model_type: model_type.
  ExaoneConfig.attribute_map: attribute_map.
  ExaoneConfig.vocab_size: vocab_size.
  ExaoneConfig.num_layers: num_layers.
  ExaoneConfig.num_key_value_heads: num_key_value_heads.
  ExaoneConfig.embed_dropout: embed_dropout.
  ExaoneConfig.attention_dropout: attention_dropout.
  ExaoneConfig.initializer_range: initializer_range.
  ExaoneConfig.use_cache: use_cache.
  ExaoneConfig.rope_theta: rope_theta.
  ExaoneConfig.rope_scaling: rope_scaling.
  ExaoneConfig.bos_token_id: bos_token_id.
  ExaoneConfig.eos_token_id: eos_token_id.
  ExaoneConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/exaone/exaone_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py)

## Classes
### `ExaoneConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/exaone/exaone_configuration.py:26`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L26)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class ExaoneConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 102400, hidden_size: int = 2048, intermediate_size: int = 14336, num_layers: int = 32, num_attention_heads: int = 32, num_key_value_heads: int | None = 8, activation_function: str = "silu", max_position_embeddings: int = 2048, initializer_range: float = 0.02, layer_norm_epsilon: float = 0.00001, use_cache: bool = True, embed_dropout: float = 0, pad_token_id: int | None = None, bos_token_id: int = 1, eos_token_id: int = 2, tie_word_embeddings: bool = False, rope_theta: float = 10000, rope_scaling: dict[str, str | float] | None = None, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, attention_dropout: float = 0, use_scan_mlp: bool = False, scan_mlp_chunk_size: int = 1024, bits: int | None = None, layer_types: list[str] | None = None, **kwargs)` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L89) — Initialize a new ExaoneConfig instance.
  - `get_partition_rules(self, *args, **kwargs)` — [`L196`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L196) — Returns partition rules for model sharding.
  - `granted_freq_max_position_embedding(self)` — [`L210`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L210) — Returns the maximum position embedding size for frequency-based position embeddings.
  - `granted_mask_max_position_embedding(self)` — [`L223`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L223) — Returns the maximum position embedding size for mask-based position embeddings.
  - `activation_function` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L167)
  - `attention_dropout` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L169)
  - `attribute_map` — [`L87`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L87)
  - `bos_token_id` — [`L176`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L176)
  - `embed_dropout` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L168)
  - `eos_token_id` — [`L177`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L177)
  - `gradient_checkpointing` — [`L178`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L178)
  - `hidden_size` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L156)
  - `initializer_range` — [`L171`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L171)
  - `intermediate_size` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L164)
  - `layer_norm_epsilon` — [`L170`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L170)
  - `layer_types` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L181)
  - `max_position_embeddings` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L155)
  - `model_type` — [`L86`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L86)
  - `num_attention_heads` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L158)
  - `num_hidden_layers` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L159)
  - `num_key_value_heads` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L162)
  - `num_layers` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L157)
  - `rope_scaling` — [`L174`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L174)
  - `rope_theta` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L173)
  - `scan_mlp_chunk_size` — [`L180`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L180)
  - `use_cache` — [`L172`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L172)
  - `use_scan_mlp` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L179)
  - `vocab_size` — [`L154`](../../../../../../../raw/code/EasyDeL/easydel/modules/exaone/exaone_configuration.py#L154)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`__call__`](modeling_exaone.md#ExaoneDecoderLayer.__call__), [`granted_freq_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_freq_max_position_embedding), [`granted_mask_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_mask_max_position_embedding), [`ExaoneModel`](modeling_exaone.md#ExaoneModel), [`ExaoneForCausalLM`](modeling_exaone.md#ExaoneForCausalLM), [`ExaoneForSequenceClassification`](modeling_exaone.md#ExaoneForSequenceClassification), [`drop`](modeling_exaone.md#ExaoneModel.drop), [`ln_1`](modeling_exaone.md#ExaoneDecoderLayer.ln_1), [`ln_2`](modeling_exaone.md#ExaoneDecoderLayer.ln_2), [`_create_rotary`](modeling_exaone.md#ExaoneAttentionInner._create_rotary), [`__init__`](modeling_exaone.md#ExaoneForCausalLM.__init__), [`__init__`](modeling_exaone.md#ExaoneForSequenceClassification.__init__), [`act_fn`](modeling_exaone.md#ExaoneGatedMLP.act_fn), [`c_fc_0`](modeling_exaone.md#ExaoneGatedMLP.c_fc_0), [`c_fc_1`](modeling_exaone.md#ExaoneGatedMLP.c_fc_1), [`c_proj`](modeling_exaone.md#ExaoneGatedMLP.c_proj), [`__init__`](modeling_exaone.md#ExaoneAttentionInner.__init__), [`__init__`](modeling_exaone.md#ExaoneModel.__init__), [`__init__`](modeling_exaone.md#ExaoneAttention.__init__), [`__init__`](modeling_exaone.md#ExaoneDecoderLayer.__init__), [`__init__`](modeling_exaone.md#ExaoneGatedMLP.__init__), [`_config_class`](modeling_exaone.md#ExaoneForCausalLM._config_class), [`_config_class`](modeling_exaone.md#ExaoneForSequenceClassification._config_class)

