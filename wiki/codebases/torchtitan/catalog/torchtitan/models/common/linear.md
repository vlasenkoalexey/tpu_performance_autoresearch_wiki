---
title: 'Module: torchtitan/models/common/linear.py'
type: catalog
provenance: extracted
module: torchtitan/models/common/linear.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.common.linear`/
symbols:
  Linear: Linear#
  Linear.Config: Linear#Config#
  Linear.Config.out_features: Linear#Config#out_features.
  Linear.Config.in_features: Linear#Config#in_features.
  Linear.Config.bias: Linear#Config#bias.
  RouterGateLinear: RouterGateLinear#
  RouterGateLinear.Config: RouterGateLinear#Config#
  Linear.__init__: Linear#__init__().
  ScaledBiasRowwiseLinear: ScaledBiasRowwiseLinear#
  ScaledBiasRowwiseLinear.Config: ScaledBiasRowwiseLinear#Config#
  ScaledBiasRowwiseLinear.__init__: ScaledBiasRowwiseLinear#__init__().
  RouterGateLinear.forward: RouterGateLinear#forward().
  ScaledBiasRowwiseLinear.parallelize: ScaledBiasRowwiseLinear#parallelize().
  ScaledBiasRowwiseLinear.forward: ScaledBiasRowwiseLinear#forward().
  ScaledBiasRowwiseLinear.tp_degree: ScaledBiasRowwiseLinear#tp_degree.
  _RouterGateLinearFunction: _RouterGateLinearFunction#
  _RouterGateLinearFunction.forward: _RouterGateLinearFunction#forward().
  _RouterGateLinearFunction.backward: _RouterGateLinearFunction#backward().
  __all__: __all__.
---
# Module: [`torchtitan/models/common/linear.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py)

## Classes
### <a id="Linear"></a>`Linear`  ·  implements/extends Module
- def: [`torchtitan/models/common/linear.py:31`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L31) — documented in [config-overrides](../../../../concepts/config-overrides.md)
- doc: Configurable nn.Linear.
- signature: `class Linear(nn.Linear, Module):`
- protocol/private: <a id="Linear.__init__"></a>`__init__`[`L40`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L40)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](linear.md#Linear.Config), [`out_features`](linear.md#Linear.Config.out_features), [`in_features`](linear.md#Linear.Config.in_features), [`bias`](linear.md#Linear.Config.bias), [`RouterGateLinear`](linear.md#RouterGateLinear), [`SoftCappedLinear`](../muse_glimmer/model.md#SoftCappedLinear), [`ScaledBiasRowwiseLinear`](linear.md#ScaledBiasRowwiseLinear), [`FusedLossLinearWrapper`](../../experiments/tpu/overrides/fused_loss.md#FusedLossLinearWrapper), [`MXFP8Linear`](../../components/quantization/mxfp8/linear.md#MXFP8Linear), [`CastLinear`](../../experiments/rl/models/cast_linear.md#CastLinear), [`RowParallelLinear`](dist_gemm.md#RowParallelLinear)
- used by: [`Module`](../../protocols/module.md#Module), [`_flux_debug`](../flux/__init__.md#_flux_debug), [`_flux_dev`](../flux/__init__.md#_flux_dev), [`_flux_schnell`](../flux/__init__.md#_flux_schnell), [`_flux_test`](../flux/__init__.md#_flux_test), [`_build_mtp_layers`](../deepseek_v4/__init__.md#_build_mtp_layers), [`_debugmodel`](../deepseek_v4/__init__.md#_debugmodel), [`_deepseek_v4_flash`](../deepseek_v4/__init__.md#_deepseek_v4_flash), [`_deepseek_v4_pro`](../deepseek_v4/__init__.md#_deepseek_v4_pro), [`_make_v4_attn_config`](../deepseek_v4/__init__.md#_make_v4_attn_config), [`_make_double_block_config`](../flux/__init__.md#_make_double_block_config), [`_muse_glimmer_config`](../muse_glimmer/__init__.md#_muse_glimmer_config), [`_build_muse_glimmer_attention`](../muse_glimmer/__init__.md#_build_muse_glimmer_attention), [`_16b`](../deepseek_v3/__init__.md#_16b), [`_236b`](../deepseek_v3/__init__.md#_236b), [`_671b`](../deepseek_v3/__init__.md#_671b), [`_debugmodel`](../deepseek_v3/__init__.md#_debugmodel), [`_testmodel`](../deepseek_v3/__init__.md#_testmodel), [`_debugmodel`](../kimi_k2_7/__init__.md#_debugmodel), [`_kimi_k2_5`](../kimi_k2_7/__init__.md#_kimi_k2_5), [`_make_gptoss_attn_config`](../gpt_oss/__init__.md#_make_gptoss_attn_config), [`make_gqa_config`](config_utils.md#make_gqa_config), [`_120b`](../gpt_oss/__init__.md#_120b), [`_20b`](../gpt_oss/__init__.md#_20b), [`_debugmodel`](../gpt_oss/__init__.md#_debugmodel), [`_testmodel`](../../experiments/tpu/deepseek_v3/__init__.md#_testmodel), [`_testmodel_moe`](../../experiments/tpu/deepseek_v3/__init__.md#_testmodel_moe), [`make_mla_attention_config`](../deepseek_v3/__init__.md#make_mla_attention_config), [`_1b`](../llama3/__init__.md#_1b), [`_3b`](../llama3/__init__.md#_3b), [`_moonlight_16b_a3b_config`](../kimi_k2_7/__init__.md#_moonlight_16b_a3b_config), [`_405b`](../llama3/__init__.md#_405b), [`_70b`](../llama3/__init__.md#_70b), [`_8b`](../llama3/__init__.md#_8b), [`_debugmodel`](../llama3/__init__.md#_debugmodel), [`_make_single_block_config`](../flux/__init__.md#_make_single_block_config), [`_27b`](../qwen3_5/__init__.md#_27b), [`_debugmodel`](../qwen3_5/__init__.md#_debugmodel), [`_debugmodel_moe`](../qwen3_5/__init__.md#_debugmodel_moe), [`_35b_a3b`](../qwen3_5/__init__.md#_35b_a3b)  (+166 more; 12 test-only)

### <a id="Linear.Config"></a>`Linear.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/linear.py:35`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L35) — documented in [config-overrides](../../../../concepts/config-overrides.md)
- signature: `class Config(Module.Config):`
- members:
  - <a id="Linear.Config.bias"></a>`bias` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L38) — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
  - <a id="Linear.Config.in_features"></a>`in_features` — [`L36`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L36) — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
  - <a id="Linear.Config.out_features"></a>`out_features` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L37) — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_flux_debug`](../flux/__init__.md#_flux_debug), [`_flux_dev`](../flux/__init__.md#_flux_dev), [`_flux_schnell`](../flux/__init__.md#_flux_schnell), [`_flux_test`](../flux/__init__.md#_flux_test), [`_build_mtp_layers`](../deepseek_v4/__init__.md#_build_mtp_layers), [`_debugmodel`](../deepseek_v4/__init__.md#_debugmodel), [`_deepseek_v4_flash`](../deepseek_v4/__init__.md#_deepseek_v4_flash), [`_deepseek_v4_pro`](../deepseek_v4/__init__.md#_deepseek_v4_pro), [`_make_v4_attn_config`](../deepseek_v4/__init__.md#_make_v4_attn_config), [`_make_double_block_config`](../flux/__init__.md#_make_double_block_config), [`_muse_glimmer_config`](../muse_glimmer/__init__.md#_muse_glimmer_config), [`_build_muse_glimmer_attention`](../muse_glimmer/__init__.md#_build_muse_glimmer_attention), [`_latent_moe_config`](../kimi_k3/__init__.md#_latent_moe_config), [`_16b`](../deepseek_v3/__init__.md#_16b), [`_236b`](../deepseek_v3/__init__.md#_236b), [`_671b`](../deepseek_v3/__init__.md#_671b), [`_debugmodel`](../deepseek_v3/__init__.md#_debugmodel), [`_testmodel`](../deepseek_v3/__init__.md#_testmodel), [`_build_gptoss_layers`](../gpt_oss/__init__.md#_build_gptoss_layers), [`_debugmodel`](../kimi_k2_7/__init__.md#_debugmodel), [`_kimi_k2_5`](../kimi_k2_7/__init__.md#_kimi_k2_5), [`_make_gptoss_attn_config`](../gpt_oss/__init__.md#_make_gptoss_attn_config), [`make_gqa_config`](config_utils.md#make_gqa_config), [`_120b`](../gpt_oss/__init__.md#_120b), [`_20b`](../gpt_oss/__init__.md#_20b), [`_debugmodel`](../gpt_oss/__init__.md#_debugmodel), [`_testmodel`](../../experiments/tpu/deepseek_v3/__init__.md#_testmodel), [`_testmodel_moe`](../../experiments/tpu/deepseek_v3/__init__.md#_testmodel_moe), [`make_mla_attention_config`](../deepseek_v3/__init__.md#make_mla_attention_config), [`_1b`](../llama3/__init__.md#_1b), [`_3b`](../llama3/__init__.md#_3b), [`_moonlight_16b_a3b_config`](../kimi_k2_7/__init__.md#_moonlight_16b_a3b_config), [`_405b`](../llama3/__init__.md#_405b), [`_70b`](../llama3/__init__.md#_70b), [`_8b`](../llama3/__init__.md#_8b), [`_debugmodel`](../llama3/__init__.md#_debugmodel), [`_make_single_block_config`](../flux/__init__.md#_make_single_block_config), [`_27b`](../qwen3_5/__init__.md#_27b), [`_debugmodel`](../qwen3_5/__init__.md#_debugmodel), [`_debugmodel_moe`](../qwen3_5/__init__.md#_debugmodel_moe)  (+167 more; 17 test-only)

### <a id="RouterGateLinear"></a>`RouterGateLinear`  ·  implements/extends Linear
- def: [`torchtitan/models/common/linear.py:101`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L101) — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- doc: Router projection with FP32 output and backward compute.
- signature: `class RouterGateLinear(Linear):`
- members:
  - <a id="RouterGateLinear.forward"></a>`forward(self, input: torch.Tensor)` — [`L112`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L112)
- uses (calls/refs, reference-scoped): [`Linear`](linear.md#Linear), [`_RouterGateLinearFunction`](linear.md#_RouterGateLinearFunction)
- used by: [`Linear`](linear.md#Linear), [`_latent_moe_config`](../kimi_k3/__init__.md#_latent_moe_config), [`_build_gptoss_layers`](../gpt_oss/__init__.md#_build_gptoss_layers), [`_make_v4_moe_config`](../deepseek_v4/__init__.md#_make_v4_moe_config), [`make_router_config`](config_utils.md#make_router_config), [`convert`](../../components/quantization/float8.md#Float8LinearConverter.convert), [`convert`](../../components/quantization/mxfp8/converter.md#MXFP8LinearConverter.convert), [`convert`](../../components/quantization/nvfp4.md#NVFP4LinearConverter.convert), [`gate`](moe.md#TokenChoiceTopKRouter.Config.gate)  (3 test-only)

### <a id="RouterGateLinear.Config"></a>`RouterGateLinear.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/linear.py:109`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L109)
- signature: `class Config(Linear.Config):`
- uses (calls/refs, reference-scoped): [`Linear`](linear.md#Linear), [`Config`](linear.md#Linear.Config)
- used by: [`_latent_moe_config`](../kimi_k3/__init__.md#_latent_moe_config), [`_build_gptoss_layers`](../gpt_oss/__init__.md#_build_gptoss_layers), [`_make_v4_moe_config`](../deepseek_v4/__init__.md#_make_v4_moe_config), [`make_router_config`](config_utils.md#make_router_config), [`convert`](../../components/quantization/float8.md#Float8LinearConverter.convert), [`convert`](../../components/quantization/mxfp8/converter.md#MXFP8LinearConverter.convert), [`convert`](../../components/quantization/nvfp4.md#NVFP4LinearConverter.convert), [`gate`](moe.md#TokenChoiceTopKRouter.Config.gate)  (3 test-only)

### <a id="ScaledBiasRowwiseLinear"></a>`ScaledBiasRowwiseLinear`  ·  implements/extends Linear
- def: [`torchtitan/models/common/linear.py:119`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L119)
- doc: Rowwise linear whose local bias contribution is scaled by TP degree.
- signature: `class ScaledBiasRowwiseLinear(Linear):`
- members:
  - <a id="ScaledBiasRowwiseLinear.forward"></a>`forward(self, input: torch.Tensor)` — [`L141`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L141)
  - <a id="ScaledBiasRowwiseLinear.parallelize"></a>`parallelize(self, parallel_dims)` — [`L137`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L137)
  - <a id="ScaledBiasRowwiseLinear.tp_degree"></a>`tp_degree` — [`L135`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L135)
- protocol/private: <a id="ScaledBiasRowwiseLinear.__init__"></a>`__init__`[`L133`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L133)
- uses (calls/refs, reference-scoped): [`Linear`](linear.md#Linear), [`__init__`](linear.md#Linear.__init__), [`Config`](linear.md#ScaledBiasRowwiseLinear.Config)
- used by: [`Linear`](linear.md#Linear), [`_make_gptoss_attn_config`](../gpt_oss/__init__.md#_make_gptoss_attn_config), [`_scaled_bias_rowwise_linear`](../kimi_k2_7/__init__.md#_scaled_bias_rowwise_linear), [`_scaled_bias_rowwise_linear`](../qwen3_5/__init__.md#_scaled_bias_rowwise_linear), [`_vision_scaled_bias_rowwise_linear`](../muse_glimmer/__init__.md#_vision_scaled_bias_rowwise_linear)

### <a id="ScaledBiasRowwiseLinear.Config"></a>`ScaledBiasRowwiseLinear.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/linear.py:130`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L130)
- signature: `class Config(Linear.Config):`
- uses (calls/refs, reference-scoped): [`Linear`](linear.md#Linear), [`Config`](linear.md#Linear.Config)
- used by: [`_make_gptoss_attn_config`](../gpt_oss/__init__.md#_make_gptoss_attn_config), [`_scaled_bias_rowwise_linear`](../kimi_k2_7/__init__.md#_scaled_bias_rowwise_linear), [`_scaled_bias_rowwise_linear`](../qwen3_5/__init__.md#_scaled_bias_rowwise_linear), [`_vision_scaled_bias_rowwise_linear`](../muse_glimmer/__init__.md#_vision_scaled_bias_rowwise_linear), [`__init__`](linear.md#ScaledBiasRowwiseLinear.__init__)

### <a id="_RouterGateLinearFunction"></a>`_RouterGateLinearFunction`
- def: [`torchtitan/models/common/linear.py:49`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L49)
- doc: Router projection with FP32 output and backward GEMMs.
- signature: `class _RouterGateLinearFunction(torch.autograd.Function):`
- members:
  - <a id="_RouterGateLinearFunction.backward"></a>`backward(ctx, grad_output_TE: torch.Tensor)` — [`L82`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L82)
  - <a id="_RouterGateLinearFunction.forward"></a>`forward(ctx, input_TD: torch.Tensor, weight_ED: torch.Tensor)` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L53)
- used by: [`forward`](linear.md#RouterGateLinear.forward)

## Module values
- <a id="__all__"></a>`__all__` — [`L150`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/linear.py#L150)

