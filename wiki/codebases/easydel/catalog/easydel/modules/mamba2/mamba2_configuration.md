---
title: 'Module: easydel/modules/mamba2/mamba2_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/mamba2/mamba2_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.mamba2.mamba2_configuration`/Mamba2Config#
symbols:
  Mamba2Config: ''
  Mamba2Config.__init__: __init__().
  Mamba2Config.hidden_size: hidden_size.
  Mamba2Config.time_step_rank: time_step_rank.
  Mamba2Config.rms_norm: rms_norm.
  Mamba2Config.layer_norm_epsilon: layer_norm_epsilon.
  Mamba2Config.conv_kernel: conv_kernel.
  Mamba2Config.time_step_min: time_step_min.
  Mamba2Config.intermediate_size: intermediate_size.
  Mamba2Config.state_size: state_size.
  Mamba2Config.use_bias: use_bias.
  Mamba2Config.use_conv_bias: use_conv_bias.
  Mamba2Config.hidden_act: hidden_act.
  Mamba2Config.time_step_max: time_step_max.
  Mamba2Config.num_heads: num_heads.
  Mamba2Config.vocab_size: vocab_size.
  Mamba2Config.num_hidden_layers: num_hidden_layers.
  Mamba2Config.expand: expand.
  Mamba2Config.time_step_floor: time_step_floor.
  Mamba2Config.residual_in_fp32: residual_in_fp32.
  Mamba2Config.n_groups: n_groups.
  Mamba2Config.head_dim: head_dim.
  Mamba2Config.norm_before_gate: norm_before_gate.
  Mamba2Config.chunk_size: chunk_size.
  Mamba2Config.time_step_limit: time_step_limit.
  Mamba2Config.gradient_checkpointing: gradient_checkpointing.
  Mamba2Config.model_type: model_type.
  Mamba2Config.bos_token_id: bos_token_id.
  Mamba2Config.eos_token_id: eos_token_id.
  Mamba2Config.pad_token_id: pad_token_id.
  Mamba2Config.initializer_range: initializer_range.
  Mamba2Config.rescale_prenorm_residual: rescale_prenorm_residual.
  Mamba2Config.use_cache: use_cache.
  Mamba2Config.tie_word_embeddings: tie_word_embeddings.
  Mamba2Config.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/mamba2/mamba2_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py)

## Classes
### `Mamba2Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/mamba2/mamba2_configuration.py:26`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L26)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class Mamba2Config(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L169) — Returns partition rules for model sharding.
  - `bos_token_id` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L142)
  - `chunk_size` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L162)
  - `conv_kernel` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L139)
  - `eos_token_id` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L143)
  - `expand` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L140)
  - `gradient_checkpointing` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L165)
  - `head_dim` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L158)
  - `hidden_act` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L147)
  - `hidden_size` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L135)
  - `initializer_range` — [`L148`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L148)
  - `intermediate_size` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L166)
  - `layer_norm_epsilon` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L138)
  - `model_type` — [`L98`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L98)
  - `n_groups` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L156)
  - `norm_before_gate` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L159)
  - `num_heads` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L157)
  - `num_hidden_layers` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L137)
  - `pad_token_id` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L144)
  - `rescale_prenorm_residual` — [`L153`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L153)
  - `residual_in_fp32` — [`L154`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L154)
  - `rms_norm` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L160)
  - `state_size` — [`L136`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L136)
  - `tie_word_embeddings` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L164)
  - `time_step_floor` — [`L152`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L152)
  - `time_step_limit` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L163)
  - `time_step_max` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L151)
  - `time_step_min` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L150)
  - `time_step_rank` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L149)
  - `use_bias` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L145)
  - `use_cache` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L155)
  - `use_conv_bias` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L146)
  - `vocab_size` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L134)
- protocol/private: `__init__`[`L100`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba2/mamba2_configuration.py#L100)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`in_proj`](modeling_mamba2.md#Mamba2Mixer.in_proj), [`conv1d`](modeling_mamba2.md#Mamba2Mixer.conv1d), [`norm`](modeling_mamba2.md#Mamba2Block.norm), [`Mamba2ForCausalLM`](modeling_mamba2.md#Mamba2ForCausalLM), [`Mamba2Model`](modeling_mamba2.md#Mamba2Model), [`out_proj`](modeling_mamba2.md#Mamba2Mixer.out_proj), [`intermediate_size`](modeling_mamba2.md#Mamba2Mixer.intermediate_size), [`num_heads`](modeling_mamba2.md#Mamba2Mixer.num_heads), [`embeddings`](modeling_mamba2.md#Mamba2Model.embeddings), [`n_groups`](modeling_mamba2.md#Mamba2Mixer.n_groups), [`norm_f`](modeling_mamba2.md#Mamba2Model.norm_f), [`__init__`](modeling_mamba2.md#Mamba2ForCausalLM.__init__), [`conv_kernel_size`](modeling_mamba2.md#Mamba2Mixer.conv_kernel_size), [`ssm_state_size`](modeling_mamba2.md#Mamba2Mixer.ssm_state_size), [`act`](modeling_mamba2.md#Mamba2Mixer.act), [`layers`](modeling_mamba2.md#Mamba2Model.layers), [`hidden_size`](modeling_mamba2.md#Mamba2Mixer.hidden_size), [`__init__`](modeling_mamba2.md#Mamba2Model.__init__), [`head_dim`](modeling_mamba2.md#Mamba2Mixer.head_dim), [`time_step_limit`](modeling_mamba2.md#Mamba2Mixer.time_step_limit), [`layer_norm_epsilon`](modeling_mamba2.md#Mamba2Mixer.layer_norm_epsilon), [`residual_in_fp32`](modeling_mamba2.md#Mamba2Block.residual_in_fp32), [`__init__`](modeling_mamba2.md#Mamba2Block.__init__), [`__init__`](modeling_mamba2.md#Mamba2Mixer.__init__), [`_config_class`](modeling_mamba2.md#Mamba2ForCausalLM._config_class), [`activation`](modeling_mamba2.md#Mamba2Mixer.activation), [`chunk_size`](modeling_mamba2.md#Mamba2Mixer.chunk_size), [`norm_before_gate`](modeling_mamba2.md#Mamba2Mixer.norm_before_gate), [`rms_norm`](modeling_mamba2.md#Mamba2Mixer.rms_norm), [`time_step_max`](modeling_mamba2.md#Mamba2Mixer.time_step_max), [`time_step_min`](modeling_mamba2.md#Mamba2Mixer.time_step_min), [`time_step_rank`](modeling_mamba2.md#Mamba2Mixer.time_step_rank), [`use_conv_bias`](modeling_mamba2.md#Mamba2Mixer.use_conv_bias)

