---
title: 'Module: torchtitan/models/gpt_oss/moe.py'
type: catalog
provenance: extracted
module: torchtitan/models/gpt_oss/moe.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.gpt_oss.moe`/
symbols:
  GptOssGroupedExperts.forward: GptOssGroupedExperts#forward().
  GptOssGroupedExperts.__init__: GptOssGroupedExperts#__init__().
  GptOssGroupedExperts.Config: GptOssGroupedExperts#Config#
  GptOssGroupedExperts.mlp1_weight_EGD: GptOssGroupedExperts#mlp1_weight_EGD.
  GptOssMoE.Config: GptOssMoE#Config#
  GptOssGroupedExperts: GptOssGroupedExperts#
  GptOssMoE: GptOssMoE#
  GptOssGroupedExperts.swiglu_limit: GptOssGroupedExperts#swiglu_limit.
  ScaleBiasForward.spmd_typecheck: ScaleBiasForward#spmd_typecheck().
  GptOssGroupedExperts.mlp1_bias_EG: GptOssGroupedExperts#mlp1_bias_EG.
  GptOssGroupedExperts.mlp2_weight_EDF: GptOssGroupedExperts#mlp2_weight_EDF.
  GptOssGroupedExperts.mlp2_bias_ED: GptOssGroupedExperts#mlp2_bias_ED.
  ScaleBiasForward: ScaleBiasForward#
  swiglu: swiglu().
  GptOssGroupedExperts.Config.swiglu_limit: GptOssGroupedExperts#Config#swiglu_limit.
  ScaleBiasForward.forward: ScaleBiasForward#forward().
  ScaleBiasForward.backward: ScaleBiasForward#backward().
  GptOssGroupedExperts.num_experts: GptOssGroupedExperts#num_experts.
---
# Module: [`torchtitan/models/gpt_oss/moe.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py)

## Classes
### <a id="GptOssGroupedExperts"></a>`GptOssGroupedExperts`  ·  implements/extends GroupedExperts
- def: [`torchtitan/models/gpt_oss/moe.py:74`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L74) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- signature: `class GptOssGroupedExperts(GroupedExperts):`
- members:
  - <a id="GptOssGroupedExperts.forward"></a>`forward(self, x_RD: torch.Tensor, num_tokens_per_expert_E: torch.Tensor)` — [`L96`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L96) — Raw expert computation without dispatch/combine. — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
  - <a id="GptOssGroupedExperts.mlp1_bias_EG"></a>`mlp1_bias_EG` — [`L90`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L90)
  - <a id="GptOssGroupedExperts.mlp1_weight_EGD"></a>`mlp1_weight_EGD` — [`L87`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L87) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
  - <a id="GptOssGroupedExperts.mlp2_bias_ED"></a>`mlp2_bias_ED` — [`L94`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L94)
  - <a id="GptOssGroupedExperts.mlp2_weight_EDF"></a>`mlp2_weight_EDF` — [`L91`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L91)
  - <a id="GptOssGroupedExperts.num_experts"></a>`num_experts` — [`L84`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L84)
  - <a id="GptOssGroupedExperts.swiglu_limit"></a>`swiglu_limit` — [`L85`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L85) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- protocol/private: <a id="GptOssGroupedExperts.__init__"></a>`__init__`[`L79`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L79)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`get_spmd_backend`](../../distributed/utils.md#get_spmd_backend), [`GroupedExperts`](../common/moe.md#GroupedExperts), [`hidden_dim`](../common/moe.md#GroupedExperts.Config.hidden_dim), [`num_experts`](../common/moe.md#GroupedExperts.Config.num_experts), [`dim`](../common/moe.md#GroupedExperts.Config.dim), [`spmd_mesh_size`](../../distributed/spmd_types.md#spmd_mesh_size), [`_grouped_mm`](../common/moe.md#GroupedExperts._grouped_mm), [`Config`](moe.md#GptOssGroupedExperts.Config), [`ScaleBiasForward`](moe.md#ScaleBiasForward), [`swiglu`](moe.md#swiglu), [`swiglu_limit`](moe.md#GptOssGroupedExperts.Config.swiglu_limit)
- used by: [`GroupedExperts`](../common/moe.md#GroupedExperts), [`_make_gptoss_experts_config`](__init__.md#_make_gptoss_experts_config), [`forward`](../common/moe.md#GroupedExperts.forward)

### <a id="GptOssGroupedExperts.Config"></a>`GptOssGroupedExperts.Config`  ·  implements/extends Config
- def: [`torchtitan/models/gpt_oss/moe.py:76`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L76)
- signature: `class Config(GroupedExperts.Config):`
- members:
  - <a id="GptOssGroupedExperts.Config.swiglu_limit"></a>`swiglu_limit` — [`L77`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L77)
- uses (calls/refs, reference-scoped): [`GroupedExperts`](../common/moe.md#GroupedExperts), [`Config`](../common/moe.md#GroupedExperts.Config)
- used by: [`_make_gptoss_experts_config`](__init__.md#_make_gptoss_experts_config), [`__init__`](moe.md#GptOssGroupedExperts.__init__), [`swiglu_limit`](moe.md#GptOssGroupedExperts.swiglu_limit)

### <a id="GptOssMoE"></a>`GptOssMoE`  ·  implements/extends MoE
- def: [`torchtitan/models/gpt_oss/moe.py:191`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L191)
- doc: GptOss MoE implementation that inherits from the base MoE class.
- signature: `class GptOssMoE(MoE):`
- uses (calls/refs, reference-scoped): [`MoE`](../common/moe.md#MoE)
- used by: [`_build_gptoss_layers`](__init__.md#_build_gptoss_layers), [`MoE`](../common/moe.md#MoE)

### <a id="GptOssMoE.Config"></a>`GptOssMoE.Config`  ·  implements/extends Config
- def: [`torchtitan/models/gpt_oss/moe.py:195`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L195)
- signature: `class Config(MoE.Config):`
- uses (calls/refs, reference-scoped): [`MoE`](../common/moe.md#MoE), [`Config`](../common/moe.md#MoE.Config)
- used by: [`_build_gptoss_layers`](__init__.md#_build_gptoss_layers)

### <a id="ScaleBiasForward"></a>`ScaleBiasForward`
- def: [`torchtitan/models/gpt_oss/moe.py:23`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L23)
- doc: Custom autograd function that scales bias in forward pass but not in backward.
- signature: `class ScaleBiasForward(torch.autograd.Function):`
- members:
  - <a id="ScaleBiasForward.backward"></a>`backward(ctx, grad_output)` — [`L59`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L59)
  - <a id="ScaleBiasForward.forward"></a>`forward(ctx, bias, tp_degree, dtype)` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L33)
  - <a id="ScaleBiasForward.spmd_typecheck"></a>`spmd_typecheck(out, *, bias)` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L40) — Typecheck for bias scaling, already interleaved to num tokens shape.
- uses (calls/refs, reference-scoped): [`spmd_mesh_size`](../../distributed/spmd_types.md#spmd_mesh_size)
- used by: [`forward`](moe.md#GptOssGroupedExperts.forward)

## Functions
- <a id="swiglu"></a>`swiglu(x, alpha: float = 1.702, limit: float = 7)` — [`L64`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/moe.py#L64)

