---
title: 'Module: torchtitan/models/deepseek_v4/mhc.py'
type: catalog
provenance: extracted
module: torchtitan/models/deepseek_v4/mhc.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.deepseek_v4.mhc`/
symbols:
  HcPre.sinkhorn: HcPre#sinkhorn.
  HcPre.forward: HcPre#forward().
  HcHead.forward: HcHead#forward().
  HcHead.Config: HcHead#Config#
  HcHead: HcHead#
  HcPre.Config: HcPre#Config#
  HcPre: HcPre#
  HcPost.Config: HcPost#Config#
  HcSplitSinkhorn.eps: HcSplitSinkhorn#eps.
  HcSplitSinkhorn.forward: HcSplitSinkhorn#forward().
  HcPre.__init__: HcPre#__init__().
  HcHead.__init__: HcHead#__init__().
  HcSplitSinkhorn.Config: HcSplitSinkhorn#Config#
  HcHead.Config.hc_mult: HcHead#Config#hc_mult.
  HcPost: HcPost#
  HcPre.Config.hc_mult: HcPre#Config#hc_mult.
  HcHead.Config.dim: HcHead#Config#dim.
  HcHead.Config.norm_eps: HcHead#Config#norm_eps.
  HcHead.Config.eps: HcHead#Config#eps.
  HcSplitSinkhorn: HcSplitSinkhorn#
  HcSplitSinkhorn.hc_mult: HcSplitSinkhorn#hc_mult.
  HcSplitSinkhorn.sinkhorn_iters: HcSplitSinkhorn#sinkhorn_iters.
  HcPre.norm_eps: HcPre#norm_eps.
  HcHead.norm_eps: HcHead#norm_eps.
  HcHead.eps: HcHead#eps.
  HcHead.hc_fn: HcHead#hc_fn.
  HcHead.hc_base: HcHead#hc_base.
  HcPre.Config.dim: HcPre#Config#dim.
  HcPre.Config.sinkhorn_iters: HcPre#Config#sinkhorn_iters.
  HcPre.Config.eps: HcPre#Config#eps.
  HcPre.Config.norm_eps: HcPre#Config#norm_eps.
  HcSplitSinkhorn.__init__: HcSplitSinkhorn#__init__().
  HcPre.hc_mult: HcPre#hc_mult.
  HcPost.__init__: HcPost#__init__().
  HcSplitSinkhorn.Config.hc_mult: HcSplitSinkhorn#Config#hc_mult.
  HcSplitSinkhorn.Config.sinkhorn_iters: HcSplitSinkhorn#Config#sinkhorn_iters.
  HcSplitSinkhorn.Config.eps: HcSplitSinkhorn#Config#eps.
  HcPre.hc_fn: HcPre#hc_fn.
  HcPre.hc_base: HcPre#hc_base.
  HcPre.hc_scale: HcPre#hc_scale.
  HcHead.hc_scale: HcHead#hc_scale.
  HcPost.forward: HcPost#forward().
---
# Module: [`torchtitan/models/deepseek_v4/mhc.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py)

## Classes
### <a id="HcHead"></a>`HcHead`  ·  implements/extends Module
- def: [`torchtitan/models/deepseek_v4/mhc.py:148`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L148) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- doc: Merge final HC branches before the output norm and LM head.
- signature: `class HcHead(Module):`
- members:
  - <a id="HcHead.forward"></a>`forward(self, x)` — [`L169`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L169) — Merge HC branches.
  - <a id="HcHead.eps"></a>`eps` — [`L162`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L162)
  - <a id="HcHead.hc_base"></a>`hc_base` — [`L166`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L166)
  - <a id="HcHead.hc_fn"></a>`hc_fn` — [`L163`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L163)
  - <a id="HcHead.hc_scale"></a>`hc_scale` — [`L167`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L167)
  - <a id="HcHead.norm_eps"></a>`norm_eps` — [`L161`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L161)
- protocol/private: <a id="HcHead.__init__"></a>`__init__`[`L158`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L158)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](mhc.md#HcHead.Config), [`hc_mult`](mhc.md#HcHead.Config.hc_mult), [`dim`](mhc.md#HcHead.Config.dim), [`eps`](mhc.md#HcHead.Config.eps), [`norm_eps`](mhc.md#HcHead.Config.norm_eps)
- used by: [`Module`](../../protocols/module.md#Module), [`_build_mtp_layers`](__init__.md#_build_mtp_layers), [`_debugmodel`](__init__.md#_debugmodel), [`_deepseek_v4_flash`](__init__.md#_deepseek_v4_flash), [`_deepseek_v4_pro`](__init__.md#_deepseek_v4_pro), [`hc_head`](model.md#DeepSeekV4Model.Config.hc_head), [`hc_head`](mtp.md#MTPBlock.Config.hc_head)

### <a id="HcHead.Config"></a>`HcHead.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v4/mhc.py:152`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L152)
- signature: `class Config(Module.Config):`
- members:
  - <a id="HcHead.Config.dim"></a>`dim` — [`L154`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L154)
  - <a id="HcHead.Config.eps"></a>`eps` — [`L156`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L156)
  - <a id="HcHead.Config.hc_mult"></a>`hc_mult` — [`L153`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L153)
  - <a id="HcHead.Config.norm_eps"></a>`norm_eps` — [`L155`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L155)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_build_mtp_layers`](__init__.md#_build_mtp_layers), [`_debugmodel`](__init__.md#_debugmodel), [`_deepseek_v4_flash`](__init__.md#_deepseek_v4_flash), [`_deepseek_v4_pro`](__init__.md#_deepseek_v4_pro), [`hc_head`](model.md#DeepSeekV4Model.Config.hc_head), [`hc_head`](mtp.md#MTPBlock.Config.hc_head), [`__init__`](mhc.md#HcHead.__init__), [`eps`](mhc.md#HcHead.eps), [`hc_base`](mhc.md#HcHead.hc_base), [`hc_fn`](mhc.md#HcHead.hc_fn), [`norm_eps`](mhc.md#HcHead.norm_eps)

### <a id="HcPost"></a>`HcPost`  ·  implements/extends Module
- def: [`torchtitan/models/deepseek_v4/mhc.py:120`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L120)
- doc: Expand a single-branch output back to HC branches with residual mixing.
- signature: `class HcPost(Module):`
- members:
  - <a id="HcPost.forward"></a>`forward(self, x, residual, post, comb)` — [`L130`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L130) — Apply HC post mixing.
- protocol/private: <a id="HcPost.__init__"></a>`__init__`[`L127`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L127)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](mhc.md#HcPost.Config)
- used by: [`Module`](../../protocols/module.md#Module), [`_build_v4_layers`](__init__.md#_build_v4_layers), [`hc_post`](model.md#DeepSeekV4TransformerBlock.Config.hc_post)

### <a id="HcPost.Config"></a>`HcPost.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v4/mhc.py:124`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L124)
- signature: `class Config(Module.Config):`
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_build_v4_layers`](__init__.md#_build_v4_layers), [`hc_post`](model.md#DeepSeekV4TransformerBlock.Config.hc_post), [`__init__`](mhc.md#HcPost.__init__)

### <a id="HcPre"></a>`HcPre`  ·  implements/extends Module
- def: [`torchtitan/models/deepseek_v4/mhc.py:72`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L72)
- doc: Reduce HC branches before attention or FFN computation.
- signature: `class HcPre(Module):`
- members:
  - <a id="HcPre.forward"></a>`forward(self, x)` — [`L99`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L99) — Project multi-branch hidden states into a single branch.
  - <a id="HcPre.hc_base"></a>`hc_base` — [`L91`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L91)
  - <a id="HcPre.hc_fn"></a>`hc_fn` — [`L90`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L90)
  - <a id="HcPre.hc_mult"></a>`hc_mult` — [`L88`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L88)
  - <a id="HcPre.hc_scale"></a>`hc_scale` — [`L92`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L92)
  - <a id="HcPre.norm_eps"></a>`norm_eps` — [`L89`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L89)
  - <a id="HcPre.sinkhorn"></a>`sinkhorn` — [`L93`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L93) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- protocol/private: <a id="HcPre.__init__"></a>`__init__`[`L83`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L83)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`Config`](mhc.md#HcPre.Config), [`Config`](mhc.md#HcSplitSinkhorn.Config), [`hc_mult`](mhc.md#HcPre.Config.hc_mult), [`HcSplitSinkhorn`](mhc.md#HcSplitSinkhorn), [`dim`](mhc.md#HcPre.Config.dim), [`eps`](mhc.md#HcPre.Config.eps), [`norm_eps`](mhc.md#HcPre.Config.norm_eps), [`sinkhorn_iters`](mhc.md#HcPre.Config.sinkhorn_iters), [`eps`](mhc.md#HcSplitSinkhorn.Config.eps), [`hc_mult`](mhc.md#HcSplitSinkhorn.Config.hc_mult), [`sinkhorn_iters`](mhc.md#HcSplitSinkhorn.Config.sinkhorn_iters)
- used by: [`Module`](../../protocols/module.md#Module), [`_build_v4_layers`](__init__.md#_build_v4_layers), [`hc_attn_pre`](model.md#DeepSeekV4TransformerBlock.Config.hc_attn_pre), [`hc_ffn_pre`](model.md#DeepSeekV4TransformerBlock.Config.hc_ffn_pre)

### <a id="HcPre.Config"></a>`HcPre.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v4/mhc.py:76`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L76)
- signature: `class Config(Module.Config):`
- members:
  - <a id="HcPre.Config.dim"></a>`dim` — [`L78`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L78)
  - <a id="HcPre.Config.eps"></a>`eps` — [`L80`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L80)
  - <a id="HcPre.Config.hc_mult"></a>`hc_mult` — [`L77`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L77)
  - <a id="HcPre.Config.norm_eps"></a>`norm_eps` — [`L81`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L81)
  - <a id="HcPre.Config.sinkhorn_iters"></a>`sinkhorn_iters` — [`L79`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L79)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_build_v4_layers`](__init__.md#_build_v4_layers), [`sinkhorn`](mhc.md#HcPre.sinkhorn), [`hc_attn_pre`](model.md#DeepSeekV4TransformerBlock.Config.hc_attn_pre), [`hc_ffn_pre`](model.md#DeepSeekV4TransformerBlock.Config.hc_ffn_pre), [`__init__`](mhc.md#HcPre.__init__), [`norm_eps`](mhc.md#HcPre.norm_eps), [`hc_mult`](mhc.md#HcPre.hc_mult)

### <a id="HcSplitSinkhorn"></a>`HcSplitSinkhorn`  ·  implements/extends Module
- def: [`torchtitan/models/deepseek_v4/mhc.py:16`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L16)
- doc: Convert HC mix logits into pre, post, and combination weights.
- signature: `class HcSplitSinkhorn(Module):`
- members:
  - <a id="HcSplitSinkhorn.forward"></a>`forward(self, mixes, hc_scale, hc_base)` — [`L31`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L31) — Split and normalize HC mixing logits.
  - <a id="HcSplitSinkhorn.eps"></a>`eps` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L29)
  - <a id="HcSplitSinkhorn.hc_mult"></a>`hc_mult` — [`L27`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L27)
  - <a id="HcSplitSinkhorn.sinkhorn_iters"></a>`sinkhorn_iters` — [`L28`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L28)
- protocol/private: <a id="HcSplitSinkhorn.__init__"></a>`__init__`[`L25`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L25)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](mhc.md#HcSplitSinkhorn.Config), [`eps`](mhc.md#HcSplitSinkhorn.Config.eps), [`hc_mult`](mhc.md#HcSplitSinkhorn.Config.hc_mult), [`sinkhorn_iters`](mhc.md#HcSplitSinkhorn.Config.sinkhorn_iters)
- used by: [`Module`](../../protocols/module.md#Module), [`sinkhorn`](mhc.md#HcPre.sinkhorn)

### <a id="HcSplitSinkhorn.Config"></a>`HcSplitSinkhorn.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v4/mhc.py:20`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L20)
- signature: `class Config(Module.Config):`
- members:
  - <a id="HcSplitSinkhorn.Config.eps"></a>`eps` — [`L23`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L23)
  - <a id="HcSplitSinkhorn.Config.hc_mult"></a>`hc_mult` — [`L21`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L21)
  - <a id="HcSplitSinkhorn.Config.sinkhorn_iters"></a>`sinkhorn_iters` — [`L22`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mhc.py#L22)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`sinkhorn`](mhc.md#HcPre.sinkhorn), [`eps`](mhc.md#HcSplitSinkhorn.eps), [`hc_mult`](mhc.md#HcSplitSinkhorn.hc_mult), [`sinkhorn_iters`](mhc.md#HcSplitSinkhorn.sinkhorn_iters), [`__init__`](mhc.md#HcSplitSinkhorn.__init__)

