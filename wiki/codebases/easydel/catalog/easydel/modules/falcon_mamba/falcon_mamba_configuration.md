---
title: 'Module: easydel/modules/falcon_mamba/falcon_mamba_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/falcon_mamba/falcon_mamba_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.falcon_mamba.falcon_mamba_configuration`/FalconMambaConfig#
symbols:
  FalconMambaConfig: ''
  FalconMambaConfig.intermediate_size: intermediate_size.
  FalconMambaConfig.hidden_size: hidden_size.
  FalconMambaConfig.__init__: __init__().
  FalconMambaConfig.time_step_rank: time_step_rank.
  FalconMambaConfig.conv_kernel: conv_kernel.
  FalconMambaConfig.layer_types: layer_types().
  FalconMambaConfig.num_hidden_layers: num_hidden_layers.
  FalconMambaConfig.layer_norm_epsilon: layer_norm_epsilon.
  FalconMambaConfig.use_bias: use_bias.
  FalconMambaConfig.use_conv_bias: use_conv_bias.
  FalconMambaConfig.hidden_act: hidden_act.
  FalconMambaConfig.time_step_min: time_step_min.
  FalconMambaConfig.time_step_init_scheme: time_step_init_scheme.
  FalconMambaConfig.vocab_size: vocab_size.
  FalconMambaConfig.state_size: state_size.
  FalconMambaConfig.initializer_range: initializer_range.
  FalconMambaConfig.residual_in_fp32: residual_in_fp32.
  FalconMambaConfig.time_step_scale: time_step_scale.
  FalconMambaConfig.time_step_max: time_step_max.
  FalconMambaConfig.time_step_floor: time_step_floor.
  FalconMambaConfig.mixer_rms_eps: mixer_rms_eps.
  FalconMambaConfig.gradient_checkpointing: gradient_checkpointing.
  FalconMambaConfig.model_type: model_type.
  FalconMambaConfig.pad_token_id: pad_token_id.
  FalconMambaConfig.bos_token_id: bos_token_id.
  FalconMambaConfig.eos_token_id: eos_token_id.
  FalconMambaConfig.expand: expand.
  FalconMambaConfig.rescale_prenorm_residual: rescale_prenorm_residual.
  FalconMambaConfig.use_cache: use_cache.
  FalconMambaConfig.use_falcon_mambapy: use_falcon_mambapy.
  FalconMambaConfig.use_associative_scan: use_associative_scan.
  FalconMambaConfig.get_partition_rules: get_partition_rules().
  FalconMambaConfig.get_mask_details: get_mask_details().
---
# Module: [`easydel/modules/falcon_mamba/falcon_mamba_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py)

## Classes
### `FalconMambaConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/falcon_mamba/falcon_mamba_configuration.py:35`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L35)
- doc: Configuration for the FalconMamba architecture.
- signature: `class FalconMambaConfig(EasyDeLBaseConfig):`
- members:
  - `get_mask_details(self)` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L139) — Recurrent Mamba layers do not use attention-mask descriptors.
  - `get_partition_rules(self, *args, **kwargs)` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L117) — Returns partition rules for model sharding.
  - `layer_types(self)` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L131) — Expose the recurrent-only layer layout for HF parity and cache helpers.
  - `bos_token_id` — [`L85`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L85)
  - `conv_kernel` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L89)
  - `eos_token_id` — [`L86`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L86)
  - `expand` — [`L88`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L88)
  - `gradient_checkpointing` — [`L108`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L108)
  - `hidden_act` — [`L92`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L92)
  - `hidden_size` — [`L80`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L80)
  - `initializer_range` — [`L93`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L93)
  - `intermediate_size` — [`L110`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L110)
  - `layer_norm_epsilon` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L83)
  - `mixer_rms_eps` — [`L107`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L107)
  - `model_type` — [`L46`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L46)
  - `num_hidden_layers` — [`L82`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L82)
  - `pad_token_id` — [`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L84)
  - `rescale_prenorm_residual` — [`L102`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L102)
  - `residual_in_fp32` — [`L94`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L94)
  - `state_size` — [`L81`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L81)
  - `time_step_floor` — [`L101`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L101)
  - `time_step_init_scheme` — [`L100`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L100)
  - `time_step_max` — [`L99`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L99)
  - `time_step_min` — [`L98`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L98)
  - `time_step_rank` — [`L96`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L96)
  - `time_step_scale` — [`L97`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L97)
  - `use_associative_scan` — [`L106`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L106)
  - `use_bias` — [`L90`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L90)
  - `use_cache` — [`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L104)
  - `use_conv_bias` — [`L91`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L91)
  - `use_falcon_mambapy` — [`L105`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L105)
  - `vocab_size` — [`L79`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L79)
- protocol/private: `__init__`[`L48`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_mamba/falcon_mamba_configuration.py#L48)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`__call__`](modeling_falcon_mamba.md#FalconMambaMixer.__call__), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`norm`](modeling_falcon_mamba.md#FalconMambaBlock.norm), [`FalconMambaForCausalLM`](modeling_falcon_mamba.md#FalconMambaForCausalLM), [`FalconMambaModel`](modeling_falcon_mamba.md#FalconMambaModel), [`rms_eps`](modeling_falcon_mamba.md#FalconMambaMixer.rms_eps), [`precision`](modeling_falcon_mamba.md#FalconMambaMixer.precision), [`conv1d`](modeling_falcon_mamba.md#FalconMambaMixer.conv1d), [`embeddings`](modeling_falcon_mamba.md#FalconMambaModel.embeddings), [`init_bias_dt`](modeling_falcon_mamba.md#FalconMambaMixer.init_bias_dt), [`norm_f`](modeling_falcon_mamba.md#FalconMambaModel.norm_f), [`act`](modeling_falcon_mamba.md#FalconMambaMixer.act), [`__init__`](modeling_falcon_mamba.md#FalconMambaForCausalLM.__init__), [`__init__`](modeling_falcon_mamba.md#FalconMambaMixer.__init__), [`layers`](modeling_falcon_mamba.md#FalconMambaModel.layers), [`__init__`](modeling_falcon_mamba.md#FalconMambaModel.__init__), [`out_proj`](modeling_falcon_mamba.md#FalconMambaMixer.out_proj), [`activation`](modeling_falcon_mamba.md#FalconMambaMixer.activation), [`in_proj`](modeling_falcon_mamba.md#FalconMambaMixer.in_proj), [`residual_in_fp32`](modeling_falcon_mamba.md#FalconMambaBlock.residual_in_fp32), [`__init__`](modeling_falcon_mamba.md#FalconMambaBlock.__init__), [`_config_class`](modeling_falcon_mamba.md#FalconMambaForCausalLM._config_class)

