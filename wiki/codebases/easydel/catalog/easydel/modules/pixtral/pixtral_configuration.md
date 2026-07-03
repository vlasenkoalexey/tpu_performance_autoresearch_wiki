---
title: 'Module: easydel/modules/pixtral/pixtral_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/pixtral/pixtral_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.pixtral.pixtral_configuration`/PixtralVisionConfig#
symbols:
  PixtralVisionConfig: ''
  PixtralVisionConfig.hidden_size: hidden_size.
  PixtralVisionConfig.initializer_range: initializer_range.
  PixtralVisionConfig.num_attention_heads: num_attention_heads.
  PixtralVisionConfig.intermediate_size: intermediate_size.
  PixtralVisionConfig.__init__: __init__().
  PixtralVisionConfig.patch_size: patch_size.
  PixtralVisionConfig.hidden_act: hidden_act.
  PixtralVisionConfig.attention_dropout: attention_dropout.
  PixtralVisionConfig.num_hidden_layers: num_hidden_layers.
  PixtralVisionConfig.num_channels: num_channels.
  PixtralVisionConfig.model_type: model_type.
  PixtralVisionConfig.image_size: image_size.
  PixtralVisionConfig.rope_theta: rope_theta.
  PixtralVisionConfig.head_dim: head_dim.
  PixtralVisionConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/pixtral/pixtral_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/pixtral_configuration.py)

## Classes
### `PixtralVisionConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/pixtral/pixtral_configuration.py:23`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/pixtral_configuration.py#L23)
- doc: This is the configuration class to store the configuration of a \[`PixtralVisionModel`\]. It is used to instantiate an
- signature: `class PixtralVisionConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, hidden_size: int = 1024, intermediate_size: int = 4096, num_hidden_layers: int = 24, num_attention_heads: int = 16, num_channels: int = 3, image_size: int = 1024, patch_size: int = 16, hidden_act: str = "gelu", attention_dropout: float = 0, rope_theta: float = 10000, initializer_range: int = 0.02, **kwargs)` — [`L76`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/pixtral_configuration.py#L76) — Initialize PixtralVisionConfig with vision encoder hyperparameters.
  - `get_partition_rules(self, *args, **kwargs)` — [`L110`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/pixtral_configuration.py#L110) — Returns partition rules for model sharding.
  - `attention_dropout` — [`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/pixtral_configuration.py#L104)
  - `head_dim` — [`L107`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/pixtral_configuration.py#L107)
  - `hidden_act` — [`L105`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/pixtral_configuration.py#L105)
  - `hidden_size` — [`L97`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/pixtral_configuration.py#L97)
  - `image_size` — [`L103`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/pixtral_configuration.py#L103)
  - `initializer_range` — [`L108`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/pixtral_configuration.py#L108)
  - `intermediate_size` — [`L98`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/pixtral_configuration.py#L98)
  - `model_type` — [`L74`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/pixtral_configuration.py#L74)
  - `num_attention_heads` — [`L100`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/pixtral_configuration.py#L100)
  - `num_channels` — [`L101`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/pixtral_configuration.py#L101)
  - `num_hidden_layers` — [`L99`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/pixtral_configuration.py#L99)
  - `patch_size` — [`L102`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/pixtral_configuration.py#L102)
  - `rope_theta` — [`L106`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/pixtral_configuration.py#L106)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`PixtralVisionModel`](modeling_pixtral.md#PixtralVisionModel), [`num_key_value_groups`](modeling_pixtral.md#PixtralAttention.num_key_value_groups), [`patch_conv`](modeling_pixtral.md#PixtralVisionModel.patch_conv), [`act_fn`](modeling_pixtral.md#PixtralMLP.act_fn), [`attention_performer`](modeling_pixtral.md#PixtralAttention.attention_performer), [`k_proj`](modeling_pixtral.md#PixtralAttention.k_proj), [`o_proj`](modeling_pixtral.md#PixtralAttention.o_proj), [`q_proj`](modeling_pixtral.md#PixtralAttention.q_proj), [`v_proj`](modeling_pixtral.md#PixtralAttention.v_proj), [`precision`](modeling_pixtral.md#PixtralMLP.precision), [`attention_norm`](modeling_pixtral.md#PixtralBlock.attention_norm), [`down_proj`](modeling_pixtral.md#PixtralMLP.down_proj), [`ffn_norm`](modeling_pixtral.md#PixtralBlock.ffn_norm), [`gate_proj`](modeling_pixtral.md#PixtralMLP.gate_proj), [`layers`](modeling_pixtral.md#PixtralTransformer.layers), [`ln_pre`](modeling_pixtral.md#PixtralVisionModel.ln_pre), [`up_proj`](modeling_pixtral.md#PixtralMLP.up_proj), [`__init__`](modeling_pixtral.md#PixtralAttention.__init__), [`__init__`](modeling_pixtral.md#PixtralVisionModel.__init__), [`__init__`](modeling_pixtral.md#PixtralBlock.__init__), [`__init__`](modeling_pixtral.md#PixtralMLP.__init__), [`__init__`](modeling_pixtral.md#PixtralTransformer.__init__), [`hidden_size`](modeling_pixtral.md#PixtralAttention.hidden_size)

