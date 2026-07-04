---
title: 'Module: easydel/modules/mamba/mamba_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/mamba/mamba_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.mamba.mamba_configuration`/MambaConfig#
symbols:
  MambaConfig: ''
  MambaConfig.hidden_size: hidden_size.
  MambaConfig.__init__: __init__().
  MambaConfig.intermediate_size: intermediate_size.
  MambaConfig.time_step_rank: time_step_rank.
  MambaConfig.conv_kernel: conv_kernel.
  MambaConfig.use_mambapy: use_mambapy.
  MambaConfig.layer_types: layer_types().
  MambaConfig.num_hidden_layers: num_hidden_layers.
  MambaConfig.layer_norm_epsilon: layer_norm_epsilon.
  MambaConfig.use_bias: use_bias.
  MambaConfig.hidden_act: hidden_act.
  MambaConfig.time_step_min: time_step_min.
  MambaConfig.time_step_max: time_step_max.
  MambaConfig.time_step_init_scheme: time_step_init_scheme.
  MambaConfig.vocab_size: vocab_size.
  MambaConfig.state_size: state_size.
  MambaConfig.use_conv_bias: use_conv_bias.
  MambaConfig.initializer_range: initializer_range.
  MambaConfig.time_step_scale: time_step_scale.
  MambaConfig.time_step_floor: time_step_floor.
  MambaConfig.residual_in_fp32: residual_in_fp32.
  MambaConfig.gradient_checkpointing: gradient_checkpointing.
  MambaConfig.model_type: model_type.
  MambaConfig.expand: expand.
  MambaConfig.bos_token_id: bos_token_id.
  MambaConfig.eos_token_id: eos_token_id.
  MambaConfig.pad_token_id: pad_token_id.
  MambaConfig.rescale_prenorm_residual: rescale_prenorm_residual.
  MambaConfig.use_cache: use_cache.
  MambaConfig.use_associative_scan: use_associative_scan.
  MambaConfig.get_mask_details: get_mask_details().
  MambaConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/mamba/mamba_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py)

## Classes
### `MambaConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/mamba/mamba_configuration.py:26`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L26)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class MambaConfig(EasyDeLBaseConfig):`
- members:
  - `get_mask_details(self)` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L159) — Recurrent Mamba layers do not use attention-mask descriptors.
  - `get_partition_rules(self, *args, **kwargs)` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L167) — Returns partition rules for model sharding.
  - `layer_types(self)` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L151) — Return a uniform recurrent layer type list for pure Mamba models.
  - `bos_token_id` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L129)
  - `conv_kernel` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L126)
  - `eos_token_id` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L130)
  - `expand` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L127)
  - `gradient_checkpointing` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L146)
  - `hidden_act` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L134)
  - `hidden_size` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L122)
  - `initializer_range` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L135)
  - `intermediate_size` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L128)
  - `layer_norm_epsilon` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L125)
  - `model_type` — [`L88`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L88)
  - `num_hidden_layers` — [`L124`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L124)
  - `pad_token_id` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L131)
  - `rescale_prenorm_residual` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L142)
  - `residual_in_fp32` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L143)
  - `state_size` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L123)
  - `time_step_floor` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L141)
  - `time_step_init_scheme` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L140)
  - `time_step_max` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L139)
  - `time_step_min` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L138)
  - `time_step_rank` — [`L136`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L136)
  - `time_step_scale` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L137)
  - `use_associative_scan` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L145)
  - `use_bias` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L132)
  - `use_cache` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L144)
  - `use_conv_bias` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L133)
  - `use_mambapy` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L147)
  - `vocab_size` — [`L121`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L121)
- protocol/private: `__init__`[`L90`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/mamba_configuration.py#L90)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`norm`](modeling_mamba.md#MambaBlock.norm), [`MambaForCausalLM`](modeling_mamba.md#MambaForCausalLM), [`MambaModel`](modeling_mamba.md#MambaModel), [`act`](modeling_mamba.md#MambaMixer.act), [`precision`](modeling_mamba.md#MambaMixer.precision), [`conv1d`](modeling_mamba.md#MambaMixer.conv1d), [`embeddings`](modeling_mamba.md#MambaModel.embeddings), [`init_bias_dt`](modeling_mamba.md#MambaMixer.init_bias_dt), [`norm_f`](modeling_mamba.md#MambaModel.norm_f), [`__init__`](modeling_mamba.md#MambaForCausalLM.__init__), [`layers`](modeling_mamba.md#MambaModel.layers), [`__init__`](modeling_mamba.md#MambaMixer.__init__), [`__init__`](modeling_mamba.md#MambaModel.__init__), [`activation`](modeling_mamba.md#MambaMixer.activation), [`in_proj`](modeling_mamba.md#MambaMixer.in_proj), [`out_proj`](modeling_mamba.md#MambaMixer.out_proj), [`residual_in_fp32`](modeling_mamba.md#MambaBlock.residual_in_fp32), [`__init__`](modeling_mamba.md#MambaBlock.__init__), [`_config_class`](modeling_mamba.md#MambaForCausalLM._config_class)

