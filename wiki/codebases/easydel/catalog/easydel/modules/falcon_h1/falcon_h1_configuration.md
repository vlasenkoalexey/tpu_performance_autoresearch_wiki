---
title: 'Module: easydel/modules/falcon_h1/falcon_h1_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/falcon_h1/falcon_h1_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.falcon_h1.falcon_h1_configuration`/FalconH1Config#
symbols:
  FalconH1Config: ''
  FalconH1Config.hidden_size: hidden_size.
  FalconH1Config.head_dim: head_dim.
  FalconH1Config.mamba_intermediate_size: mamba_intermediate_size().
  FalconH1Config.mamba_d_ssm: mamba_d_ssm.
  FalconH1Config.rms_norm_eps: rms_norm_eps.
  FalconH1Config.intermediate_size: intermediate_size.
  FalconH1Config.num_hidden_layers: num_hidden_layers.
  FalconH1Config.mlp_bias: mlp_bias.
  FalconH1Config.hidden_act: hidden_act.
  FalconH1Config.mamba_expand: mamba_expand.
  FalconH1Config.layers_block_type: layers_block_type().
  FalconH1Config.layer_types: layer_types().
  FalconH1Config.mamba_n_heads: mamba_n_heads.
  FalconH1Config.mamba_n_groups: mamba_n_groups.
  FalconH1Config.mamba_d_state: mamba_d_state.
  FalconH1Config.vocab_size: vocab_size.
  FalconH1Config.num_attention_heads: num_attention_heads.
  FalconH1Config.projectors_bias: projectors_bias.
  FalconH1Config.mamba_d_head: mamba_d_head.
  FalconH1Config.mamba_d_conv: mamba_d_conv.
  FalconH1Config.mamba_chunk_size: mamba_chunk_size.
  FalconH1Config.mamba_conv_bias: mamba_conv_bias.
  FalconH1Config.mamba_proj_bias: mamba_proj_bias.
  FalconH1Config.mamba_norm_before_gate: mamba_norm_before_gate.
  FalconH1Config.mamba_rms_norm: mamba_rms_norm.
  FalconH1Config.lm_head_multiplier: lm_head_multiplier.
  FalconH1Config.embedding_multiplier: embedding_multiplier.
  FalconH1Config.mlp_multipliers: mlp_multipliers.
  FalconH1Config.attention_out_multiplier: attention_out_multiplier.
  FalconH1Config.attention_in_multiplier: attention_in_multiplier.
  FalconH1Config.key_multiplier: key_multiplier.
  FalconH1Config.ssm_multipliers: ssm_multipliers.
  FalconH1Config.ssm_in_multiplier: ssm_in_multiplier.
  FalconH1Config.ssm_out_multiplier: ssm_out_multiplier.
  FalconH1Config.model_type: model_type.
  FalconH1Config.__init__: __init__().
  FalconH1Config.max_position_embeddings: max_position_embeddings.
  FalconH1Config.attention_dropout: attention_dropout.
  FalconH1Config.attention_bias: attention_bias.
  FalconH1Config.num_key_value_heads: num_key_value_heads.
  FalconH1Config.initializer_range: initializer_range.
  FalconH1Config.use_cache: use_cache.
  FalconH1Config.num_logits_to_keep: num_logits_to_keep.
  FalconH1Config.rope_theta: rope_theta.
  FalconH1Config.rope_scaling: rope_scaling.
  FalconH1Config.time_step_min: time_step_min.
  FalconH1Config.time_step_max: time_step_max.
  FalconH1Config.time_step_limit: time_step_limit.
  FalconH1Config.rope_parameters: rope_parameters.
  FalconH1Config.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/falcon_h1/falcon_h1_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py)

## Classes
### `FalconH1Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/falcon_h1/falcon_h1_configuration.py:24`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L24)
- doc: Configuration for the FalconH1 architecture.
- signature: `class FalconH1Config(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L190) — Returns partition rules for model sharding.
  - `layer_types(self)` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L173) — Return layer types for hybrid cache configuration.
  - `layers_block_type(self)` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L168)
  - `mamba_intermediate_size(self)` — [`L184`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L184) — Return the intermediate size for Mamba SSM.
  - `attention_bias` — [`L102`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L102)
  - `attention_dropout` — [`L99`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L99)
  - `attention_in_multiplier` — [`L152`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L152)
  - `attention_out_multiplier` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L151)
  - `embedding_multiplier` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L147)
  - `head_dim` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L158)
  - `hidden_act` — [`L109`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L109)
  - `hidden_size` — [`L94`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L94)
  - `initializer_range` — [`L110`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L110)
  - `intermediate_size` — [`L95`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L95)
  - `key_multiplier` — [`L153`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L153)
  - `lm_head_multiplier` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L146)
  - `mamba_chunk_size` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L137)
  - `mamba_conv_bias` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L138)
  - `mamba_d_conv` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L135)
  - `mamba_d_head` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L132)
  - `mamba_d_ssm` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L130)
  - `mamba_d_state` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L134)
  - `mamba_expand` — [`L136`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L136)
  - `mamba_n_groups` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L133)
  - `mamba_n_heads` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L131)
  - `mamba_norm_before_gate` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L140)
  - `mamba_proj_bias` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L139)
  - `mamba_rms_norm` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L141)
  - `max_position_embeddings` — [`L98`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L98)
  - `mlp_bias` — [`L103`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L103)
  - `mlp_multipliers` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L150)
  - `model_type` — [`L37`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L37)
  - `num_attention_heads` — [`L97`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L97)
  - `num_hidden_layers` — [`L96`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L96)
  - `num_key_value_heads` — [`L107`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L107)
  - `num_logits_to_keep` — [`L114`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L114)
  - `projectors_bias` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L119)
  - `rms_norm_eps` — [`L111`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L111)
  - `rope_parameters` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L149)
  - `rope_scaling` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L117)
  - `rope_theta` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L116)
  - `ssm_in_multiplier` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L156)
  - `ssm_multipliers` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L155)
  - `ssm_out_multiplier` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L157)
  - `time_step_limit` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L144)
  - `time_step_max` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L143)
  - `time_step_min` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L142)
  - `use_cache` — [`L113`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L113)
  - `vocab_size` — [`L93`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L93)
- protocol/private: `__init__`[`L39`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/falcon_h1_configuration.py#L39)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`intermediate_size`](modeling_falcon_h1.md#FalconH1Mixer.intermediate_size), [`compute_mup_vector`](modeling_falcon_h1.md#compute_mup_vector), [`embed_tokens`](modeling_falcon_h1.md#FalconH1Model.embed_tokens), [`FalconH1ForCausalLM`](modeling_falcon_h1.md#FalconH1ForCausalLM), [`FalconH1Model`](modeling_falcon_h1.md#FalconH1Model), [`norm`](modeling_falcon_h1.md#FalconH1Mixer.norm), [`out_proj`](modeling_falcon_h1.md#FalconH1Mixer.out_proj), [`n_groups`](modeling_falcon_h1.md#FalconH1Mixer.n_groups), [`chunk_size`](modeling_falcon_h1.md#FalconH1Mixer.chunk_size), [`num_heads`](modeling_falcon_h1.md#FalconH1Mixer.num_heads), [`__init__`](modeling_falcon_h1.md#FalconH1ForCausalLM.__init__), [`conv_kernel_size`](modeling_falcon_h1.md#FalconH1Mixer.conv_kernel_size), [`ssm_state_size`](modeling_falcon_h1.md#FalconH1Mixer.ssm_state_size), [`down_proj`](modeling_falcon_h1.md#FalconH1MLP.down_proj), [`final_layernorm`](modeling_falcon_h1.md#FalconH1Model.final_layernorm), [`gate_proj`](modeling_falcon_h1.md#FalconH1MLP.gate_proj), [`input_layernorm`](modeling_falcon_h1.md#FalconH1DecoderLayer.input_layernorm), [`pre_ff_layernorm`](modeling_falcon_h1.md#FalconH1DecoderLayer.pre_ff_layernorm), [`up_proj`](modeling_falcon_h1.md#FalconH1MLP.up_proj), [`act`](modeling_falcon_h1.md#FalconH1Mixer.act), [`act_fn`](modeling_falcon_h1.md#FalconH1MLP.act_fn), [`head_dim`](modeling_falcon_h1.md#FalconH1Mixer.head_dim), [`hidden_size`](modeling_falcon_h1.md#FalconH1Mixer.hidden_size), [`mamba_rms_norm`](modeling_falcon_h1.md#FalconH1Mixer.mamba_rms_norm), [`__init__`](modeling_falcon_h1.md#FalconH1Attention.__init__), [`__init__`](modeling_falcon_h1.md#FalconH1Model.__init__), [`layers`](modeling_falcon_h1.md#FalconH1Model.layers), [`use_conv_bias`](modeling_falcon_h1.md#FalconH1Mixer.use_conv_bias), [`attention_in_multiplier`](modeling_falcon_h1.md#FalconH1DecoderLayer.attention_in_multiplier), [`attn_out_multiplier`](modeling_falcon_h1.md#FalconH1DecoderLayer.attn_out_multiplier), [`down_multiplier`](modeling_falcon_h1.md#FalconH1MLP.down_multiplier), [`embedding_multiplier`](modeling_falcon_h1.md#FalconH1Model.embedding_multiplier), [`key_multiplier`](modeling_falcon_h1.md#FalconH1Attention.key_multiplier), [`layer_norm_epsilon`](modeling_falcon_h1.md#FalconH1Mixer.layer_norm_epsilon), [`lm_head_multiplier`](modeling_falcon_h1.md#FalconH1Model.lm_head_multiplier), [`ssm_in_multiplier`](modeling_falcon_h1.md#FalconH1Mixer.ssm_in_multiplier), [`ssm_out_multiplier`](modeling_falcon_h1.md#FalconH1DecoderLayer.ssm_out_multiplier)  (+5 more)

