---
title: 'Module: torchtitan/models/common/nn_modules.py'
type: catalog
provenance: extracted
module: torchtitan/models/common/nn_modules.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.common.nn_modules`/
symbols:
  RMSNorm: RMSNorm#
  RMSNorm.Config: RMSNorm#Config#
  RMSNorm.Config.normalized_shape: RMSNorm#Config#normalized_shape.
  RMSNorm.Config.eps: RMSNorm#Config#eps.
  LayerNorm: LayerNorm#
  GELU: GELU#
  LayerNorm.Config: LayerNorm#Config#
  Conv1d.__init__: Conv1d#__init__().
  GELU.Config: GELU#Config#
  Conv1d: Conv1d#
  Conv2d.__init__: Conv2d#__init__().
  Conv1d.Config: Conv1d#Config#
  Conv2d.Config: Conv2d#Config#
  Conv2d: Conv2d#
  Conv2d.Config.in_channels: Conv2d#Config#in_channels.
  Conv2d.Config.out_channels: Conv2d#Config#out_channels.
  Conv2d.Config.kernel_size: Conv2d#Config#kernel_size.
  RMSNorm.__init__: RMSNorm#__init__().
  GroupNorm.__init__: GroupNorm#__init__().
  LayerNorm.__init__: LayerNorm#__init__().
  Conv2d.Config.padding: Conv2d#Config#padding.
  GroupNorm.Config: GroupNorm#Config#
  LayerNorm.Config.normalized_shape: LayerNorm#Config#normalized_shape.
  LayerNorm.Config.eps: LayerNorm#Config#eps.
  SiLU.Config: SiLU#Config#
  GELU.Config.approximate: GELU#Config#approximate.
  Identity.Config: Identity#Config#
  GroupNorm: GroupNorm#
  SiLU: SiLU#
  Identity: Identity#
  GELU.__init__: GELU#__init__().
  RMSNorm.Config.elementwise_affine: RMSNorm#Config#elementwise_affine.
  LayerNorm.Config.elementwise_affine: LayerNorm#Config#elementwise_affine.
  Conv1d.Config.in_channels: Conv1d#Config#in_channels.
  Conv1d.Config.out_channels: Conv1d#Config#out_channels.
  Conv1d.Config.kernel_size: Conv1d#Config#kernel_size.
  Conv1d.Config.groups: Conv1d#Config#groups.
  Conv1d.Config.bias: Conv1d#Config#bias.
  Identity.__init__: Identity#__init__().
  SiLU.__init__: SiLU#__init__().
  Conv1d.Config.padding: Conv1d#Config#padding.
  Conv2d.Config.stride: Conv2d#Config#stride.
  GroupNorm.Config.num_groups: GroupNorm#Config#num_groups.
  GroupNorm.Config.num_channels: GroupNorm#Config#num_channels.
  GroupNorm.Config.eps: GroupNorm#Config#eps.
  Conv1d.Config.stride: Conv1d#Config#stride.
  Conv2d.Config.bias: Conv2d#Config#bias.
  __all__: __all__.
---
# Module: [`torchtitan/models/common/nn_modules.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py)

## Classes
### <a id="Conv1d"></a>`Conv1d`  ·  implements/extends Module
- def: [`torchtitan/models/common/nn_modules.py:26`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L26)
- doc: Configurable nn.Conv1d.
- signature: `class Conv1d(nn.Conv1d, Module):`
- protocol/private: <a id="Conv1d.__init__"></a>`__init__`[`L41`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L41)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](nn_modules.md#Conv1d.Config), [`bias`](nn_modules.md#Conv1d.Config.bias), [`groups`](nn_modules.md#Conv1d.Config.groups), [`in_channels`](nn_modules.md#Conv1d.Config.in_channels), [`kernel_size`](nn_modules.md#Conv1d.Config.kernel_size), [`out_channels`](nn_modules.md#Conv1d.Config.out_channels), [`padding`](nn_modules.md#Conv1d.Config.padding), [`stride`](nn_modules.md#Conv1d.Config.stride)
- used by: [`Module`](../../protocols/module.md#Module), [`conv`](../kimi_k3/__init__.md#_kda_config.conv), [`_conv`](../qwen3_5/__init__.md#_qwen35_deltanet_config._conv), [`conv_k`](../qwen3_5/gdn.md#GatedDeltaNet.Config.conv_k), [`conv_q`](../qwen3_5/gdn.md#GatedDeltaNet.Config.conv_q), [`conv_v`](../qwen3_5/gdn.md#GatedDeltaNet.Config.conv_v), [`k_conv`](../kimi_k3/kda.md#KDA.Config.k_conv), [`q_conv`](../kimi_k3/kda.md#KDA.Config.q_conv), [`v_conv`](../kimi_k3/kda.md#KDA.Config.v_conv)

### <a id="Conv1d.Config"></a>`Conv1d.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/nn_modules.py:30`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L30)
- signature: `class Config(Module.Config):`
- members:
  - <a id="Conv1d.Config.bias"></a>`bias` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L39)
  - <a id="Conv1d.Config.groups"></a>`groups` — [`L36`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L36)
  - <a id="Conv1d.Config.in_channels"></a>`in_channels` — [`L31`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L31)
  - <a id="Conv1d.Config.kernel_size"></a>`kernel_size` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L33)
  - <a id="Conv1d.Config.out_channels"></a>`out_channels` — [`L32`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L32)
  - <a id="Conv1d.Config.padding"></a>`padding` — [`L35`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L35)
  - <a id="Conv1d.Config.stride"></a>`stride` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L34)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`conv`](../kimi_k3/__init__.md#_kda_config.conv), [`_conv`](../qwen3_5/__init__.md#_qwen35_deltanet_config._conv), [`__init__`](nn_modules.md#Conv1d.__init__), [`conv_k`](../qwen3_5/gdn.md#GatedDeltaNet.Config.conv_k), [`conv_q`](../qwen3_5/gdn.md#GatedDeltaNet.Config.conv_q), [`conv_v`](../qwen3_5/gdn.md#GatedDeltaNet.Config.conv_v), [`k_conv`](../kimi_k3/kda.md#KDA.Config.k_conv), [`q_conv`](../kimi_k3/kda.md#KDA.Config.q_conv), [`v_conv`](../kimi_k3/kda.md#KDA.Config.v_conv)

### <a id="Conv2d"></a>`Conv2d`  ·  implements/extends Module
- def: [`torchtitan/models/common/nn_modules.py:53`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L53)
- doc: Configurable nn.Conv2d.
- signature: `class Conv2d(nn.Conv2d, Module):`
- protocol/private: <a id="Conv2d.__init__"></a>`__init__`[`L67`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L67)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](nn_modules.md#Conv2d.Config), [`in_channels`](nn_modules.md#Conv2d.Config.in_channels), [`kernel_size`](nn_modules.md#Conv2d.Config.kernel_size), [`out_channels`](nn_modules.md#Conv2d.Config.out_channels), [`padding`](nn_modules.md#Conv2d.Config.padding), [`stride`](nn_modules.md#Conv2d.Config.stride), [`bias`](nn_modules.md#Conv2d.Config.bias)
- used by: [`Module`](../../protocols/module.md#Module), [`conv_in`](../flux/model/autoencoder.md#Encoder.conv_in), [`conv2`](../flux/model/autoencoder.md#ResnetBlock.conv2), [`conv1`](../flux/model/autoencoder.md#ResnetBlock.conv1), [`conv`](../flux/model/autoencoder.md#Downsample.conv), [`conv`](../flux/model/autoencoder.md#Upsample.conv), [`conv_in`](../flux/model/autoencoder.md#Decoder.conv_in), [`conv_out`](../flux/model/autoencoder.md#Decoder.conv_out), [`conv_out`](../flux/model/autoencoder.md#Encoder.conv_out), [`nin_shortcut`](../flux/model/autoencoder.md#ResnetBlock.nin_shortcut), [`norm`](../flux/model/autoencoder.md#AttnBlock.norm)

### <a id="Conv2d.Config"></a>`Conv2d.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/nn_modules.py:57`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L57)
- signature: `class Config(Module.Config):`
- members:
  - <a id="Conv2d.Config.bias"></a>`bias` — [`L65`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L65)
  - <a id="Conv2d.Config.in_channels"></a>`in_channels` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L58)
  - <a id="Conv2d.Config.kernel_size"></a>`kernel_size` — [`L60`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L60)
  - <a id="Conv2d.Config.out_channels"></a>`out_channels` — [`L59`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L59)
  - <a id="Conv2d.Config.padding"></a>`padding` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L62)
  - <a id="Conv2d.Config.stride"></a>`stride` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L61)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`conv_in`](../flux/model/autoencoder.md#Encoder.conv_in), [`conv2`](../flux/model/autoencoder.md#ResnetBlock.conv2), [`conv1`](../flux/model/autoencoder.md#ResnetBlock.conv1), [`conv`](../flux/model/autoencoder.md#Downsample.conv), [`conv`](../flux/model/autoencoder.md#Upsample.conv), [`conv_in`](../flux/model/autoencoder.md#Decoder.conv_in), [`conv_out`](../flux/model/autoencoder.md#Decoder.conv_out), [`conv_out`](../flux/model/autoencoder.md#Encoder.conv_out), [`nin_shortcut`](../flux/model/autoencoder.md#ResnetBlock.nin_shortcut), [`norm`](../flux/model/autoencoder.md#AttnBlock.norm), [`__init__`](nn_modules.md#Conv2d.__init__)

### <a id="GELU"></a>`GELU`  ·  implements/extends Module
- def: [`torchtitan/models/common/nn_modules.py:78`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L78)
- doc: Configurable nn.GELU.
- signature: `class GELU(nn.GELU, Module):`
- protocol/private: <a id="GELU.__init__"></a>`__init__`[`L85`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L85)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](nn_modules.md#GELU.Config), [`approximate`](nn_modules.md#GELU.Config.approximate)
- used by: [`Module`](../../protocols/module.md#Module), [`_vision_encoder_config`](../kimi_k3/__init__.md#_vision_encoder_config), [`muse_glimmer_vision_encoder_config`](../muse_glimmer/__init__.md#muse_glimmer_vision_encoder_config), [`hidden_size`](../flux/model/layers.md#DoubleStreamBlock.hidden_size), [`mlp_act`](../flux/model/layers.md#SingleStreamBlock.mlp_act), [`act_fn`](vision_encoder.md#VisionMLP.Config.act_fn), [`act_fn`](../qwen3_5/vision_encoder.md#PatchMerger.Config.act_fn), [`activation`](../kimi_k3/vision_encoder.md#KimiK3VisionProjector.Config.activation), [`act_fn`](../kimi_k2_7/vision_encoder.md#VisionProjector.Config.act_fn)

### <a id="GELU.Config"></a>`GELU.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/nn_modules.py:82`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L82)
- signature: `class Config(Module.Config):`
- members:
  - <a id="GELU.Config.approximate"></a>`approximate` — [`L83`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L83)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_vision_encoder_config`](../kimi_k3/__init__.md#_vision_encoder_config), [`muse_glimmer_vision_encoder_config`](../muse_glimmer/__init__.md#muse_glimmer_vision_encoder_config), [`hidden_size`](../flux/model/layers.md#DoubleStreamBlock.hidden_size), [`mlp_act`](../flux/model/layers.md#SingleStreamBlock.mlp_act), [`act_fn`](vision_encoder.md#VisionMLP.Config.act_fn), [`act_fn`](../qwen3_5/vision_encoder.md#PatchMerger.Config.act_fn), [`activation`](../kimi_k3/vision_encoder.md#KimiK3VisionProjector.Config.activation), [`act_fn`](../kimi_k2_7/vision_encoder.md#VisionProjector.Config.act_fn), [`__init__`](nn_modules.md#GELU.__init__)

### <a id="GroupNorm"></a>`GroupNorm`  ·  implements/extends Module
- def: [`torchtitan/models/common/nn_modules.py:89`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L89)
- doc: Configurable nn.GroupNorm.
- signature: `class GroupNorm(nn.GroupNorm, Module):`
- protocol/private: <a id="GroupNorm.__init__"></a>`__init__`[`L98`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L98)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](nn_modules.md#GroupNorm.Config), [`eps`](nn_modules.md#GroupNorm.Config.eps), [`num_channels`](nn_modules.md#GroupNorm.Config.num_channels), [`num_groups`](nn_modules.md#GroupNorm.Config.num_groups)
- used by: [`Module`](../../protocols/module.md#Module), [`_norm`](../flux/model/autoencoder.md#_norm)

### <a id="GroupNorm.Config"></a>`GroupNorm.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/nn_modules.py:93`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L93)
- signature: `class Config(Module.Config):`
- members:
  - <a id="GroupNorm.Config.eps"></a>`eps` — [`L96`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L96)
  - <a id="GroupNorm.Config.num_channels"></a>`num_channels` — [`L95`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L95)
  - <a id="GroupNorm.Config.num_groups"></a>`num_groups` — [`L94`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L94)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_norm`](../flux/model/autoencoder.md#_norm), [`__init__`](nn_modules.md#GroupNorm.__init__)

### <a id="Identity"></a>`Identity`  ·  implements/extends Module
- def: [`torchtitan/models/common/nn_modules.py:106`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L106)
- doc: Configurable nn.Identity.
- signature: `class Identity(nn.Identity, Module):`
- protocol/private: <a id="Identity.__init__"></a>`__init__`[`L113`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L113)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](nn_modules.md#Identity.Config)
- used by: [`Module`](../../protocols/module.md#Module), [`_build_stage_from_modules`](../../experiments/transformers_modeling_backend/pipeline.md#pipeline_module_split._build_stage_from_modules)

### <a id="Identity.Config"></a>`Identity.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/nn_modules.py:110`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L110)
- signature: `class Config(Module.Config):`
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_build_stage_from_modules`](../../experiments/transformers_modeling_backend/pipeline.md#pipeline_module_split._build_stage_from_modules), [`__init__`](nn_modules.md#Identity.__init__)

### <a id="LayerNorm"></a>`LayerNorm`  ·  implements/extends Module
- def: [`torchtitan/models/common/nn_modules.py:117`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L117)
- doc: Configurable nn.LayerNorm.
- signature: `class LayerNorm(nn.LayerNorm, Module):`
- protocol/private: <a id="LayerNorm.__init__"></a>`__init__`[`L126`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L126)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](nn_modules.md#LayerNorm.Config), [`eps`](nn_modules.md#LayerNorm.Config.eps), [`normalized_shape`](nn_modules.md#LayerNorm.Config.normalized_shape), [`elementwise_affine`](nn_modules.md#LayerNorm.Config.elementwise_affine)
- used by: [`Module`](../../protocols/module.md#Module), [`_qwen35_vision_encoder_config`](../qwen3_5/__init__.md#_qwen35_vision_encoder_config), [`hidden_size`](../flux/model/layers.md#DoubleStreamBlock.hidden_size), [`norm_final`](../flux/model/layers.md#LastLayer.norm_final), [`pre_norm`](../flux/model/layers.md#SingleStreamBlock.pre_norm), [`_vision_layer_norm`](../muse_glimmer/__init__.md#_vision_layer_norm), [`norm1`](vision_encoder.md#VisionTransformerBlock.Config.norm1), [`norm2`](vision_encoder.md#VisionTransformerBlock.Config.norm2), [`_vl_layernorm`](../kimi_k2_7/__init__.md#_vl_layernorm), [`final_norm`](../kimi_k2_7/vision_encoder.md#MoonViTEncoder.Config.final_norm), [`ln_post`](../muse_glimmer/vision_encoder.md#MuseGlimmerVisionEncoder.Config.ln_post), [`ln_pre`](../muse_glimmer/vision_encoder.md#MuseGlimmerVisionEncoder.Config.ln_pre), [`norm`](../qwen3_5/vision_encoder.md#PatchMerger.Config.norm), [`pre_norm`](../kimi_k2_7/vision_encoder.md#VisionProjector.Config.pre_norm), [`final_norm`](../kimi_k2_7/vision_encoder.md#KimiK25VisionEncoder.Config.final_norm)

### <a id="LayerNorm.Config"></a>`LayerNorm.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/nn_modules.py:121`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L121)
- signature: `class Config(Module.Config):`
- members:
  - <a id="LayerNorm.Config.elementwise_affine"></a>`elementwise_affine` — [`L124`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L124)
  - <a id="LayerNorm.Config.eps"></a>`eps` — [`L123`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L123)
  - <a id="LayerNorm.Config.normalized_shape"></a>`normalized_shape` — [`L122`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L122)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_qwen35_vision_encoder_config`](../qwen3_5/__init__.md#_qwen35_vision_encoder_config), [`hidden_size`](../flux/model/layers.md#DoubleStreamBlock.hidden_size), [`norm_final`](../flux/model/layers.md#LastLayer.norm_final), [`pre_norm`](../flux/model/layers.md#SingleStreamBlock.pre_norm), [`_vision_layer_norm`](../muse_glimmer/__init__.md#_vision_layer_norm), [`norm1`](vision_encoder.md#VisionTransformerBlock.Config.norm1), [`norm2`](vision_encoder.md#VisionTransformerBlock.Config.norm2), [`_vl_layernorm`](../kimi_k2_7/__init__.md#_vl_layernorm), [`final_norm`](../kimi_k2_7/vision_encoder.md#MoonViTEncoder.Config.final_norm), [`__init__`](nn_modules.md#LayerNorm.__init__), [`ln_post`](../muse_glimmer/vision_encoder.md#MuseGlimmerVisionEncoder.Config.ln_post), [`ln_pre`](../muse_glimmer/vision_encoder.md#MuseGlimmerVisionEncoder.Config.ln_pre), [`norm`](../qwen3_5/vision_encoder.md#PatchMerger.Config.norm), [`pre_norm`](../kimi_k2_7/vision_encoder.md#VisionProjector.Config.pre_norm), [`final_norm`](../kimi_k2_7/vision_encoder.md#KimiK25VisionEncoder.Config.final_norm)

### <a id="RMSNorm"></a>`RMSNorm`  ·  implements/extends Module
- def: [`torchtitan/models/common/nn_modules.py:134`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L134) — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)
- doc: Configurable nn.RMSNorm.
- signature: `class RMSNorm(nn.RMSNorm, Module):`
- protocol/private: <a id="RMSNorm.__init__"></a>`__init__`[`L143`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L143)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](nn_modules.md#RMSNorm.Config), [`normalized_shape`](nn_modules.md#RMSNorm.Config.normalized_shape), [`eps`](nn_modules.md#RMSNorm.Config.eps), [`RMSGainCenterNorm`](../muse_glimmer/model.md#RMSGainCenterNorm), [`elementwise_affine`](nn_modules.md#RMSNorm.Config.elementwise_affine)
- used by: [`Module`](../../protocols/module.md#Module), [`_vision_encoder_config`](../kimi_k3/__init__.md#_vision_encoder_config), [`_build_mtp_layers`](../deepseek_v4/__init__.md#_build_mtp_layers), [`_debugmodel`](../deepseek_v4/__init__.md#_debugmodel), [`_deepseek_v4_flash`](../deepseek_v4/__init__.md#_deepseek_v4_flash), [`_deepseek_v4_pro`](../deepseek_v4/__init__.md#_deepseek_v4_pro), [`_make_v4_attn_config`](../deepseek_v4/__init__.md#_make_v4_attn_config), [`_make_double_block_config`](../flux/__init__.md#_make_double_block_config), [`_16b`](../deepseek_v3/__init__.md#_16b), [`_236b`](../deepseek_v3/__init__.md#_236b), [`_671b`](../deepseek_v3/__init__.md#_671b), [`_debugmodel`](../deepseek_v3/__init__.md#_debugmodel), [`_testmodel`](../deepseek_v3/__init__.md#_testmodel), [`_build_gptoss_layers`](../gpt_oss/__init__.md#_build_gptoss_layers), [`_debugmodel`](../kimi_k2_7/__init__.md#_debugmodel), [`_kimi_k2_5`](../kimi_k2_7/__init__.md#_kimi_k2_5), [`make_gqa_config`](config_utils.md#make_gqa_config), [`_120b`](../gpt_oss/__init__.md#_120b), [`_20b`](../gpt_oss/__init__.md#_20b), [`_debugmodel`](../gpt_oss/__init__.md#_debugmodel), [`_testmodel`](../../experiments/tpu/deepseek_v3/__init__.md#_testmodel), [`_testmodel_moe`](../../experiments/tpu/deepseek_v3/__init__.md#_testmodel_moe), [`make_mla_attention_config`](../deepseek_v3/__init__.md#make_mla_attention_config), [`_1b`](../llama3/__init__.md#_1b), [`_3b`](../llama3/__init__.md#_3b), [`_moonlight_16b_a3b_config`](../kimi_k2_7/__init__.md#_moonlight_16b_a3b_config), [`_405b`](../llama3/__init__.md#_405b), [`_70b`](../llama3/__init__.md#_70b), [`_8b`](../llama3/__init__.md#_8b), [`_debugmodel`](../llama3/__init__.md#_debugmodel), [`_build_v4_layers`](../deepseek_v4/__init__.md#_build_v4_layers), [`_make_single_block_config`](../flux/__init__.md#_make_single_block_config), [`_testmodel`](../../experiments/tpu/llama3/__init__.md#_testmodel), [`build_mla_moe_layers`](../deepseek_v3/__init__.md#build_mla_moe_layers), [`_build_llama3_layers`](../llama3/__init__.md#_build_llama3_layers), [`_make_compressor_config`](../deepseek_v4/__init__.md#_make_compressor_config), [`_build_mtp_layers`](../deepseek_v3/__init__.md#_build_mtp_layers), [`norm`](decoder.md#Decoder.Config.norm), [`_qwen3_norm`](../qwen3/__init__.md#_qwen3_norm), [`attention_norm`](decoder.md#TransformerBlock.Config.attention_norm)  (+40 more; 15 test-only)

### <a id="RMSNorm.Config"></a>`RMSNorm.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/nn_modules.py:138`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L138) — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- signature: `class Config(Module.Config):`
- members:
  - <a id="RMSNorm.Config.elementwise_affine"></a>`elementwise_affine` — [`L141`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L141)
  - <a id="RMSNorm.Config.eps"></a>`eps` — [`L140`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L140)
  - <a id="RMSNorm.Config.normalized_shape"></a>`normalized_shape` — [`L139`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L139) — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_vision_encoder_config`](../kimi_k3/__init__.md#_vision_encoder_config), [`_build_mtp_layers`](../deepseek_v4/__init__.md#_build_mtp_layers), [`_debugmodel`](../deepseek_v4/__init__.md#_debugmodel), [`_deepseek_v4_flash`](../deepseek_v4/__init__.md#_deepseek_v4_flash), [`_deepseek_v4_pro`](../deepseek_v4/__init__.md#_deepseek_v4_pro), [`_make_v4_attn_config`](../deepseek_v4/__init__.md#_make_v4_attn_config), [`_make_double_block_config`](../flux/__init__.md#_make_double_block_config), [`_16b`](../deepseek_v3/__init__.md#_16b), [`_236b`](../deepseek_v3/__init__.md#_236b), [`_671b`](../deepseek_v3/__init__.md#_671b), [`_debugmodel`](../deepseek_v3/__init__.md#_debugmodel), [`_testmodel`](../deepseek_v3/__init__.md#_testmodel), [`_build_gptoss_layers`](../gpt_oss/__init__.md#_build_gptoss_layers), [`_debugmodel`](../kimi_k2_7/__init__.md#_debugmodel), [`_kimi_k2_5`](../kimi_k2_7/__init__.md#_kimi_k2_5), [`make_gqa_config`](config_utils.md#make_gqa_config), [`_120b`](../gpt_oss/__init__.md#_120b), [`_20b`](../gpt_oss/__init__.md#_20b), [`_debugmodel`](../gpt_oss/__init__.md#_debugmodel), [`_testmodel`](../../experiments/tpu/deepseek_v3/__init__.md#_testmodel), [`_testmodel_moe`](../../experiments/tpu/deepseek_v3/__init__.md#_testmodel_moe), [`make_mla_attention_config`](../deepseek_v3/__init__.md#make_mla_attention_config), [`_1b`](../llama3/__init__.md#_1b), [`_3b`](../llama3/__init__.md#_3b), [`_moonlight_16b_a3b_config`](../kimi_k2_7/__init__.md#_moonlight_16b_a3b_config), [`_405b`](../llama3/__init__.md#_405b), [`_70b`](../llama3/__init__.md#_70b), [`_8b`](../llama3/__init__.md#_8b), [`_debugmodel`](../llama3/__init__.md#_debugmodel), [`_build_v4_layers`](../deepseek_v4/__init__.md#_build_v4_layers), [`_make_single_block_config`](../flux/__init__.md#_make_single_block_config), [`_testmodel`](../../experiments/tpu/llama3/__init__.md#_testmodel), [`build_mla_moe_layers`](../deepseek_v3/__init__.md#build_mla_moe_layers), [`_build_llama3_layers`](../llama3/__init__.md#_build_llama3_layers), [`_make_compressor_config`](../deepseek_v4/__init__.md#_make_compressor_config), [`_build_mtp_layers`](../deepseek_v3/__init__.md#_build_mtp_layers), [`norm`](decoder.md#Decoder.Config.norm), [`_qwen3_norm`](../qwen3/__init__.md#_qwen3_norm), [`attention_norm`](decoder.md#TransformerBlock.Config.attention_norm), [`ffn_norm`](decoder.md#TransformerBlock.Config.ffn_norm)  (+36 more; 13 test-only)

### <a id="SiLU"></a>`SiLU`  ·  implements/extends Module
- def: [`torchtitan/models/common/nn_modules.py:151`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L151)
- doc: Configurable nn.SiLU.
- signature: `class SiLU(nn.SiLU, Module):`
- protocol/private: <a id="SiLU.__init__"></a>`__init__`[`L158`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L158)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](nn_modules.md#SiLU.Config)
- used by: [`Module`](../../protocols/module.md#Module), [`adaLN_modulation`](../flux/model/layers.md#LastLayer.adaLN_modulation), [`silu`](../flux/model/layers.md#MLPEmbedder.silu)

### <a id="SiLU.Config"></a>`SiLU.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/nn_modules.py:155`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L155)
- signature: `class Config(Module.Config):`
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`adaLN_modulation`](../flux/model/layers.md#LastLayer.adaLN_modulation), [`silu`](../flux/model/layers.md#MLPEmbedder.silu), [`__init__`](nn_modules.md#SiLU.__init__)

## Module values
- <a id="__all__"></a>`__all__` — [`L162`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/nn_modules.py#L162)

