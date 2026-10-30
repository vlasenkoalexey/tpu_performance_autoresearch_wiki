---
title: 'Module: torchtitan/models/kimi_k3/moe.py'
type: catalog
provenance: extracted
module: torchtitan/models/kimi_k3/moe.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.kimi_k3.moe`/
symbols:
  KimiLatentMoE.forward: KimiLatentMoE#forward().
  KimiGroupedExperts.forward: KimiGroupedExperts#forward().
  KimiFeedForward.forward: KimiFeedForward#forward().
  KimiFeedForward.Config: KimiFeedForward#Config#
  KimiLatentMoE.Config: KimiLatentMoE#Config#
  KimiFeedForward: KimiFeedForward#
  KimiLatentMoE: KimiLatentMoE#
  KimiGroupedExperts.Config: KimiGroupedExperts#Config#
  KimiLatentMoE.Config.routed_down: KimiLatentMoE#Config#routed_down.
  KimiLatentMoE.Config.routed_norm: KimiLatentMoE#Config#routed_norm.
  KimiLatentMoE.Config.routed_up: KimiLatentMoE#Config#routed_up.
  KimiLatentMoE.routed_down: KimiLatentMoE#routed_down.
  KimiLatentMoE.routed_norm: KimiLatentMoE#routed_norm.
  KimiLatentMoE.routed_up: KimiLatentMoE#routed_up.
  KimiFeedForward.__init__: KimiFeedForward#__init__().
  KimiGroupedExperts.__init__: KimiGroupedExperts#__init__().
  KimiLatentMoE.__init__: KimiLatentMoE#__init__().
  KimiGroupedExperts: KimiGroupedExperts#
  KimiFeedForward.beta: KimiFeedForward#beta.
  KimiFeedForward.linear_beta: KimiFeedForward#linear_beta.
  KimiGroupedExperts.beta: KimiGroupedExperts#beta.
  KimiGroupedExperts.linear_beta: KimiGroupedExperts#linear_beta.
  _situ_glu: _situ_glu().
  KimiFeedForward.Config.beta: KimiFeedForward#Config#beta.
  KimiFeedForward.Config.linear_beta: KimiFeedForward#Config#linear_beta.
  KimiGroupedExperts.Config.beta: KimiGroupedExperts#Config#beta.
  KimiGroupedExperts.Config.linear_beta: KimiGroupedExperts#Config#linear_beta.
---
# Module: [`torchtitan/models/kimi_k3/moe.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py)

## Classes
### <a id="KimiFeedForward"></a>`KimiFeedForward`  ·  implements/extends FeedForward
- def: [`torchtitan/models/kimi_k3/moe.py:40`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L40)
- doc: FeedForward with Kimi's SiTU activation.
- signature: `class KimiFeedForward(FeedForward):`
- members:
  - <a id="KimiFeedForward.forward"></a>`forward(self, x: torch.Tensor)` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L53) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KimiFeedForward.beta"></a>`beta` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L50)
  - <a id="KimiFeedForward.linear_beta"></a>`linear_beta` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L51)
- protocol/private: <a id="KimiFeedForward.__init__"></a>`__init__`[`L48`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L48)
- uses (calls/refs, reference-scoped): [`FeedForward`](../common/feed_forward.md#FeedForward), [`w2`](../common/feed_forward.md#FeedForward.w2), [`Config`](moe.md#KimiFeedForward.Config), [`w1`](../common/feed_forward.md#FeedForward.w1), [`w3`](../common/feed_forward.md#FeedForward.w3), [`__init__`](../common/feed_forward.md#FeedForward.__init__), [`_situ_glu`](moe.md#_situ_glu), [`beta`](moe.md#KimiFeedForward.Config.beta), [`linear_beta`](moe.md#KimiFeedForward.Config.linear_beta)
- used by: [`FeedForward`](../common/feed_forward.md#FeedForward), [`_feed_forward_config`](__init__.md#_feed_forward_config), [`forward`](../common/feed_forward.md#FeedForward.forward), [`feed_forward`](model.md#KimiK3TransformerBlock.Config.feed_forward)

### <a id="KimiFeedForward.Config"></a>`KimiFeedForward.Config`  ·  implements/extends Config
- def: [`torchtitan/models/kimi_k3/moe.py:44`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L44)
- signature: `class Config(FeedForward.Config):`
- members:
  - <a id="KimiFeedForward.Config.beta"></a>`beta` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L45)
  - <a id="KimiFeedForward.Config.linear_beta"></a>`linear_beta` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L46)
- uses (calls/refs, reference-scoped): [`FeedForward`](../common/feed_forward.md#FeedForward), [`Config`](../common/feed_forward.md#FeedForward.Config)
- used by: [`_feed_forward_config`](__init__.md#_feed_forward_config), [`feed_forward`](model.md#KimiK3TransformerBlock.Config.feed_forward), [`__init__`](moe.md#KimiFeedForward.__init__), [`beta`](moe.md#KimiFeedForward.beta), [`linear_beta`](moe.md#KimiFeedForward.linear_beta)

### <a id="KimiGroupedExperts"></a>`KimiGroupedExperts`  ·  implements/extends GroupedExperts
- def: [`torchtitan/models/kimi_k3/moe.py:59`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L59)
- doc: `common/moe.py::GroupedExperts` with Kimi's SiTU activation.
- signature: `class KimiGroupedExperts(GroupedExperts):`
- members:
  - <a id="KimiGroupedExperts.forward"></a>`forward(self, x_RD: torch.Tensor, num_tokens_per_expert_E: torch.Tensor)` — [`L72`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L72) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KimiGroupedExperts.beta"></a>`beta` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L69)
  - <a id="KimiGroupedExperts.linear_beta"></a>`linear_beta` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L70)
- protocol/private: <a id="KimiGroupedExperts.__init__"></a>`__init__`[`L67`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L67)
- uses (calls/refs, reference-scoped): [`GroupedExperts`](../common/moe.md#GroupedExperts), [`w2_EDF`](../common/moe.md#GroupedExperts.w2_EDF), [`w1_EFD`](../common/moe.md#GroupedExperts.w1_EFD), [`w3_EFD`](../common/moe.md#GroupedExperts.w3_EFD), [`_grouped_mm`](../common/moe.md#GroupedExperts._grouped_mm), [`Config`](moe.md#KimiGroupedExperts.Config), [`__init__`](../common/moe.md#GroupedExperts.__init__), [`_situ_glu`](moe.md#_situ_glu), [`beta`](moe.md#KimiGroupedExperts.Config.beta), [`linear_beta`](moe.md#KimiGroupedExperts.Config.linear_beta)
- used by: [`_latent_moe_config`](__init__.md#_latent_moe_config), [`GroupedExperts`](../common/moe.md#GroupedExperts), [`forward`](../common/moe.md#GroupedExperts.forward)

### <a id="KimiGroupedExperts.Config"></a>`KimiGroupedExperts.Config`  ·  implements/extends Config
- def: [`torchtitan/models/kimi_k3/moe.py:63`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L63)
- signature: `class Config(GroupedExperts.Config):`
- members:
  - <a id="KimiGroupedExperts.Config.beta"></a>`beta` — [`L64`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L64)
  - <a id="KimiGroupedExperts.Config.linear_beta"></a>`linear_beta` — [`L65`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L65)
- uses (calls/refs, reference-scoped): [`GroupedExperts`](../common/moe.md#GroupedExperts), [`Config`](../common/moe.md#GroupedExperts.Config)
- used by: [`_latent_moe_config`](__init__.md#_latent_moe_config), [`__init__`](moe.md#KimiGroupedExperts.__init__), [`beta`](moe.md#KimiGroupedExperts.beta), [`linear_beta`](moe.md#KimiGroupedExperts.linear_beta)

### <a id="KimiLatentMoE"></a>`KimiLatentMoE`  ·  implements/extends MoE
- def: [`torchtitan/models/kimi_k3/moe.py:110`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L110)
- doc: `common/moe.py::MoE` with Kimi's latent routed-expert path.
- signature: `class KimiLatentMoE(MoE):`
- members:
  - <a id="KimiLatentMoE.forward"></a>`forward(self, x_TD: torch.Tensor, **router_kwargs)` — [`L125`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L125) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KimiLatentMoE.routed_down"></a>`routed_down` — [`L121`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L121)
  - <a id="KimiLatentMoE.routed_norm"></a>`routed_norm` — [`L122`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L122)
  - <a id="KimiLatentMoE.routed_up"></a>`routed_up` — [`L123`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L123)
- protocol/private: <a id="KimiLatentMoE.__init__"></a>`__init__`[`L119`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L119)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`MoE`](../common/moe.md#MoE), [`routed_experts`](../common/moe.md#MoE.routed_experts), [`router`](../common/moe.md#MoE.router), [`shared_experts`](../common/moe.md#MoE.shared_experts), [`Config`](moe.md#KimiLatentMoE.Config), [`__init__`](../common/moe.md#MoE.__init__), [`routed_down`](moe.md#KimiLatentMoE.Config.routed_down), [`routed_norm`](moe.md#KimiLatentMoE.Config.routed_norm), [`routed_up`](moe.md#KimiLatentMoE.Config.routed_up), [`tokens_per_expert_E`](../common/moe.md#MoE.tokens_per_expert_E), [`_tokens_per_expert`](../common/moe.md#_tokens_per_expert), [`expert_bias_E`](../common/moe.md#MoE.expert_bias_E)
- used by: [`_latent_moe_config`](__init__.md#_latent_moe_config), [`MoE`](../common/moe.md#MoE), [`forward`](../common/moe.md#MoE.forward), [`moe`](model.md#KimiK3TransformerBlock.Config.moe)

### <a id="KimiLatentMoE.Config"></a>`KimiLatentMoE.Config`  ·  implements/extends Config
- def: [`torchtitan/models/kimi_k3/moe.py:114`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L114)
- signature: `class Config(MoE.Config):`
- members:
  - <a id="KimiLatentMoE.Config.routed_down"></a>`routed_down` — [`L115`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L115)
  - <a id="KimiLatentMoE.Config.routed_norm"></a>`routed_norm` — [`L116`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L116)
  - <a id="KimiLatentMoE.Config.routed_up"></a>`routed_up` — [`L117`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L117)
- uses (calls/refs, reference-scoped): [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`Config`](../common/nn_modules.md#RMSNorm.Config), [`MoE`](../common/moe.md#MoE), [`Config`](../common/moe.md#MoE.Config)
- used by: [`_latent_moe_config`](__init__.md#_latent_moe_config), [`moe`](model.md#KimiK3TransformerBlock.Config.moe), [`routed_down`](moe.md#KimiLatentMoE.routed_down), [`routed_norm`](moe.md#KimiLatentMoE.routed_norm), [`routed_up`](moe.md#KimiLatentMoE.routed_up), [`__init__`](moe.md#KimiLatentMoE.__init__)

## Functions
- <a id="_situ_glu"></a>`_situ_glu(gate: torch.Tensor, up: torch.Tensor, beta: float, linear_beta: float | None)` — [`L24`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/moe.py#L24) — Kimi's SiTU-GLU activation, evaluated in FP32.

