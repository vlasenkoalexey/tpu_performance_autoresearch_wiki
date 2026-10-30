---
title: 'Module: torchtitan/overrides/fused_swiglu.py'
type: catalog
provenance: extracted
module: torchtitan/overrides/fused_swiglu.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.overrides.fused_swiglu`/
symbols:
  _fused_swiglu_config: _fused_swiglu_config().
  fused_grouped_experts: fused_grouped_experts().
  DistGEMMFusedSwiGLU.forward: DistGEMMFusedSwiGLU#forward().
  FusedGroupedExperts.w13: FusedGroupedExperts#w13.
  fused_swiglu: fused_swiglu().
  dist_gemm_fused_swiglu: dist_gemm_fused_swiglu().
  FusedSwiGLU.w13: FusedSwiGLU#w13.
  FusedSwiGLU: FusedSwiGLU#
  FusedSwiGLU.Config: FusedSwiGLU#Config#
  FusedSwiGLU.forward: FusedSwiGLU#forward().
  FusedGroupedExperts.__init__: FusedGroupedExperts#__init__().
  FusedGroupedExperts.forward: FusedGroupedExperts#forward().
  silu_and_mul_forward_kernel: silu_and_mul_forward_kernel().
  silu_and_mul_backward_kernel: silu_and_mul_backward_kernel().
  FusedSwiGLU.w2: FusedSwiGLU#w2.
  silu_and_mul_op: silu_and_mul_op().
  DistGEMMFusedSwiGLU.Config: DistGEMMFusedSwiGLU#Config#
  FusedGroupedExperts.Config: FusedGroupedExperts#Config#
  _make_fused_linear_init: _make_fused_linear_init().
  FusedSwiGLU.Config.w13: FusedSwiGLU#Config#w13.
  FusedSwiGLU.Config.w2: FusedSwiGLU#Config#w2.
  _fuse_w13_grouped_experts_sharding: _fuse_w13_grouped_experts_sharding().
  FusedSwiGLU.__init__: FusedSwiGLU#__init__().
  silu_and_mul_backward_op: silu_and_mul_backward_op().
  _make_fused_gate_up_init: _make_fused_gate_up_init().
  _silu_and_mul_2d: _silu_and_mul_2d().
  DistGEMMFusedSwiGLU: DistGEMMFusedSwiGLU#
  silu_and_mul_autograd_backward: silu_and_mul_autograd_backward().
  _fused_silu_and_mul: _fused_silu_and_mul().
  FusedGroupedExperts: FusedGroupedExperts#
  _fuse_w13_grouped_experts_param_init: _fuse_w13_grouped_experts_param_init().
  silu_and_mul_op_fake: silu_and_mul_op_fake().
  silu_and_mul_backward_op_fake: silu_and_mul_backward_op_fake().
  _MAX_BLOCK_N: _MAX_BLOCK_N.
  _SILU_AND_MUL_BLOCK_M: _SILU_AND_MUL_BLOCK_M.
  _silu_and_mul_forward_kernel: _silu_and_mul_forward_kernel().
  _silu_and_mul_backward_kernel: _silu_and_mul_backward_kernel().
  silu_and_mul_setup_context: silu_and_mul_setup_context().
  _make_fused_gate_up_init._init: _make_fused_gate_up_init()._init().
  _make_fused_linear_init._init: _make_fused_linear_init()._init().
  FusedSwiGLU._split_w13_on_save: FusedSwiGLU#_split_w13_on_save().
  FusedSwiGLU._merge_w13_on_load: FusedSwiGLU#_merge_w13_on_load().
  FusedGroupedExperts._split_w13_on_save: FusedGroupedExperts#_split_w13_on_save().
  FusedGroupedExperts._merge_w13_on_load: FusedGroupedExperts#_merge_w13_on_load().
  __all__: __all__.
---
# Module: [`torchtitan/overrides/fused_swiglu.py`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py)

## Classes
### <a id="DistGEMMFusedSwiGLU"></a>`DistGEMMFusedSwiGLU`  ·  implements/extends FusedSwiGLU
- def: [`torchtitan/overrides/fused_swiglu.py:507`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L507) — documented in [config-overrides](../../../concepts/config-overrides.md)
- doc: `FusedSwiGLU` with the TP collectives also folded into its GEMMs.
- signature: `class DistGEMMFusedSwiGLU(FusedSwiGLU):`
- members:
  - <a id="DistGEMMFusedSwiGLU.forward"></a>`forward(self, x: torch.Tensor)` — [`L529`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L529) — documented in [config-overrides](../../../concepts/config-overrides.md)
- uses (calls/refs, reference-scoped): [`w13`](fused_swiglu.md#FusedSwiGLU.w13), [`FusedSwiGLU`](fused_swiglu.md#FusedSwiGLU), [`forward`](fused_swiglu.md#FusedSwiGLU.forward), [`_warn_once_unfused`](../models/common/dist_gemm.md#_warn_once_unfused), [`w2`](fused_swiglu.md#FusedSwiGLU.w2), [`_tp_group_from_context`](../models/common/dist_gemm.md#_tp_group_from_context), [`silu_and_mul_op`](fused_swiglu.md#silu_and_mul_op), [`LinearReduceScatter`](../distributed/linear.md#LinearReduceScatter), [`AllGatherLinear`](../distributed/linear.md#AllGatherLinear)
- used by: [`dist_gemm_fused_swiglu`](fused_swiglu.md#dist_gemm_fused_swiglu), [`FusedSwiGLU`](fused_swiglu.md#FusedSwiGLU), [`forward`](fused_swiglu.md#FusedSwiGLU.forward)

### <a id="DistGEMMFusedSwiGLU.Config"></a>`DistGEMMFusedSwiGLU.Config`  ·  implements/extends Config
- def: [`torchtitan/overrides/fused_swiglu.py:525`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L525) — documented in [config-overrides](../../../concepts/config-overrides.md)
- doc: Binds `Config.build()` to this module rather than the parent, so it
- signature: `class Config(FusedSwiGLU.Config):`
- uses (calls/refs, reference-scoped): [`Config`](fused_swiglu.md#FusedSwiGLU.Config), [`FusedSwiGLU`](fused_swiglu.md#FusedSwiGLU)
- used by: [`dist_gemm_fused_swiglu`](fused_swiglu.md#dist_gemm_fused_swiglu)

### <a id="FusedGroupedExperts"></a>`FusedGroupedExperts`  ·  implements/extends GroupedExperts
- def: [`torchtitan/overrides/fused_swiglu.py:600`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L600)
- doc: Routed experts (grouped GEMM) with the gate and up projections fused.
- signature: `class FusedGroupedExperts(GroupedExperts):`
- members:
  - <a id="FusedGroupedExperts._merge_w13_on_load"></a>`_merge_w13_on_load(module, state_dict, prefix, *args)` — [`L668`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L668) — Combine separate ``w1_EFD`` / ``w3_EFD`` back into the fused ``w13`` on load.
  - <a id="FusedGroupedExperts._split_w13_on_save"></a>`_split_w13_on_save(module, state_dict, prefix, local_metadata)` — [`L661`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L661) — Save fused as ``w1_EFD`` / ``w3_EFD`` on save.
  - <a id="FusedGroupedExperts.forward"></a>`forward(self, x_RD: torch.Tensor, num_tokens_per_expert_E: torch.Tensor)` — [`L634`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L634) — documented in [config-overrides](../../../concepts/config-overrides.md)
  - <a id="FusedGroupedExperts.w13"></a>`w13` — [`L627`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L627) — documented in [config-overrides](../../../concepts/config-overrides.md)
- protocol/private: <a id="FusedGroupedExperts.__init__"></a>`__init__`[`L621`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L621)
- uses (calls/refs, reference-scoped): [`GroupedExperts`](../models/common/moe.md#GroupedExperts), [`hidden_dim`](../models/common/moe.md#GroupedExperts.Config.hidden_dim), [`num_experts`](../models/common/moe.md#GroupedExperts.Config.num_experts), [`dim`](../models/common/moe.md#GroupedExperts.Config.dim), [`w2_EDF`](../models/common/moe.md#GroupedExperts.w2_EDF), [`w1_EFD`](../models/common/moe.md#GroupedExperts.w1_EFD), [`w3_EFD`](../models/common/moe.md#GroupedExperts.w3_EFD), [`_grouped_mm`](../models/common/moe.md#GroupedExperts._grouped_mm), [`silu_and_mul_op`](fused_swiglu.md#silu_and_mul_op), [`Config`](fused_swiglu.md#FusedGroupedExperts.Config), [`__init__`](../models/common/moe.md#GroupedExperts.__init__)
- used by: [`GroupedExperts`](../models/common/moe.md#GroupedExperts), [`fused_grouped_experts`](fused_swiglu.md#fused_grouped_experts), [`forward`](../models/common/moe.md#GroupedExperts.forward)

### <a id="FusedGroupedExperts.Config"></a>`FusedGroupedExperts.Config`  ·  implements/extends Config
- def: [`torchtitan/overrides/fused_swiglu.py:618`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L618)
- signature: `class Config(GroupedExperts.Config):`
- uses (calls/refs, reference-scoped): [`GroupedExperts`](../models/common/moe.md#GroupedExperts), [`Config`](../models/common/moe.md#GroupedExperts.Config)
- used by: [`fused_grouped_experts`](fused_swiglu.md#fused_grouped_experts), [`__init__`](fused_swiglu.md#FusedGroupedExperts.__init__)

### <a id="FusedSwiGLU"></a>`FusedSwiGLU`  ·  implements/extends FeedForward
- def: [`torchtitan/overrides/fused_swiglu.py:450`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L450) — documented in [config-overrides](../../../concepts/config-overrides.md)
- doc: SwiGLU FFN with the gate and up projections fused into one linear.
- signature: `class FusedSwiGLU(FeedForward):`
- members:
  - <a id="FusedSwiGLU._merge_w13_on_load"></a>`_merge_w13_on_load(module, state_dict, prefix, *args)` — [`L490`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L490) — Merge stock ``w1.weight`` / ``w3.weight`` back into the fused ``w13``.
  - <a id="FusedSwiGLU._split_w13_on_save"></a>`_split_w13_on_save(module, state_dict, prefix, local_metadata)` — [`L478`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L478) — Emit the fused ``w13`` as the stock ``w1.weight`` / ``w3.weight``.
  - <a id="FusedSwiGLU.forward"></a>`forward(self, x: torch.Tensor)` — [`L472`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L472) — documented in [config-overrides](../../../concepts/config-overrides.md)
  - <a id="FusedSwiGLU.w13"></a>`w13` — [`L468`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L468) — documented in [config-overrides](../../../concepts/config-overrides.md)
  - <a id="FusedSwiGLU.w2"></a>`w2` — [`L467`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L467) — documented in [config-overrides](../../../concepts/config-overrides.md)
- protocol/private: <a id="FusedSwiGLU.__init__"></a>`__init__`[`L465`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L465)
- uses (calls/refs, reference-scoped): [`Module`](../protocols/module.md#Module), [`build`](../protocols/module.md#Module.Config.build), [`FeedForward`](../models/common/feed_forward.md#FeedForward), [`forward`](fused_swiglu.md#DistGEMMFusedSwiGLU.forward), [`Config`](fused_swiglu.md#FusedSwiGLU.Config), [`w13`](fused_swiglu.md#FusedSwiGLU.Config.w13), [`w2`](fused_swiglu.md#FusedSwiGLU.Config.w2), [`DistGEMMFusedSwiGLU`](fused_swiglu.md#DistGEMMFusedSwiGLU), [`_fused_silu_and_mul`](fused_swiglu.md#_fused_silu_and_mul)
- used by: [`FeedForward`](../models/common/feed_forward.md#FeedForward), [`_fused_swiglu_config`](fused_swiglu.md#_fused_swiglu_config), [`forward`](../models/common/feed_forward.md#FeedForward.forward), [`forward`](fused_swiglu.md#DistGEMMFusedSwiGLU.forward), [`fused_swiglu`](fused_swiglu.md#fused_swiglu), [`Config`](fused_swiglu.md#DistGEMMFusedSwiGLU.Config), [`DistGEMMFusedSwiGLU`](fused_swiglu.md#DistGEMMFusedSwiGLU)

### <a id="FusedSwiGLU.Config"></a>`FusedSwiGLU.Config`  ·  implements/extends Config
- def: [`torchtitan/overrides/fused_swiglu.py:461`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L461) — documented in [config-overrides](../../../concepts/config-overrides.md)
- signature: `class Config(Module.Config):`
- members:
  - <a id="FusedSwiGLU.Config.w13"></a>`w13` — [`L462`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L462) — documented in [config-overrides](../../../concepts/config-overrides.md)
  - <a id="FusedSwiGLU.Config.w2"></a>`w2` — [`L463`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L463) — documented in [config-overrides](../../../concepts/config-overrides.md)
- uses (calls/refs, reference-scoped): [`Module`](../protocols/module.md#Module), [`Linear`](../models/common/linear.md#Linear), [`Config`](../models/common/linear.md#Linear.Config), [`Config`](../protocols/module.md#Module.Config)
- used by: [`_fused_swiglu_config`](fused_swiglu.md#_fused_swiglu_config), [`fused_swiglu`](fused_swiglu.md#fused_swiglu), [`w13`](fused_swiglu.md#FusedSwiGLU.w13), [`w2`](fused_swiglu.md#FusedSwiGLU.w2), [`Config`](fused_swiglu.md#DistGEMMFusedSwiGLU.Config), [`__init__`](fused_swiglu.md#FusedSwiGLU.__init__)

## Functions
- <a id="_fuse_w13_grouped_experts_param_init"></a>`_fuse_w13_grouped_experts_param_init(param_init: dict | None)` — [`L677`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L677) — Remap ``w1_EFD`` / ``w3_EFD`` initializers onto the fused ``w13``.
- <a id="_fuse_w13_grouped_experts_sharding"></a>`_fuse_w13_grouped_experts_sharding(base: ShardingConfig)` — [`L692`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L692) — Replace the ``w1_EFD`` / ``w3_EFD`` state shardings with one for ``w13``.
- <a id="_fused_silu_and_mul"></a>`_fused_silu_and_mul(gate: torch.Tensor, up: torch.Tensor)` — [`L414`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L414) — ``silu(gate) * up`` via the fused ``torchtitan::silu_and_mul`` op. — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="_fused_swiglu_config"></a>`_fused_swiglu_config(cfg: FeedForward.Config, target: type[FusedSwiGLU.Config])` — [`L561`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L561) — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="_make_fused_gate_up_init._init"></a>`_init(t: torch.Tensor)` — [`L393`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L393)
- <a id="_make_fused_linear_init._init"></a>`_init(t: torch.Tensor)` — [`L408`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L408)
- <a id="_make_fused_gate_up_init"></a>`_make_fused_gate_up_init(gate_init: Callable, up_init: Callable, *, gate_up_axis: int)` — [`L377`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L377) — Build an initializer for a fused gate/up weight from per-half initializers.
- <a id="_make_fused_linear_init"></a>`_make_fused_linear_init(gate_init: Callable, up_init: Callable)` — [`L404`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L404) — Build an initializer for an interleaved 2D gate/up linear weight.
- <a id="_silu_and_mul_2d"></a>`_silu_and_mul_2d(gate: torch.Tensor, up: torch.Tensor)` — [`L430`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L430)
- <a id="_silu_and_mul_backward_kernel"></a>`_silu_and_mul_backward_kernel(grad_out, gate, up, grad_gate, grad_up, offsets, NUM_ROWS: tl.constexpr, NUM_COLS: tl.constexpr, NUM_OFFSETS: tl.constexpr, HAS_OFFSETS: tl.constexpr, GRAD_OUT_ROW_STRIDE: tl.constexpr, GRAD_OUT_COL_STRIDE: tl.constexpr, GATE_ROW_STRIDE: tl.constexpr, GATE_COL_STRIDE: tl.constexpr, UP_ROW_STRIDE: tl.constexpr, UP_COL_STRIDE: tl.constexpr, GRAD_GATE_ROW_STRIDE: tl.constexpr, GRAD_GATE_COL_STRIDE: tl.constexpr, GRAD_UP_ROW_STRIDE: tl.constexpr, GRAD_UP_COL_STRIDE: tl.constexpr, BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr)` — [`L145`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L145) — Backward for ``_silu_and_mul_forward_kernel`` over defined rows.
- <a id="_silu_and_mul_forward_kernel"></a>`_silu_and_mul_forward_kernel(gate, up, out, offsets, NUM_ROWS: tl.constexpr, NUM_COLS: tl.constexpr, NUM_OFFSETS: tl.constexpr, HAS_OFFSETS: tl.constexpr, GATE_ROW_STRIDE: tl.constexpr, GATE_COL_STRIDE: tl.constexpr, UP_ROW_STRIDE: tl.constexpr, UP_COL_STRIDE: tl.constexpr, OUT_ROW_STRIDE: tl.constexpr, OUT_COL_STRIDE: tl.constexpr, BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr)` — [`L96`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L96) — Compute ``silu(gate) * up`` for optionally offset-limited rows.
- <a id="dist_gemm_fused_swiglu"></a>`dist_gemm_fused_swiglu(cfg: DistGEMMFeedForward.Config)` — [`L594`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L594) — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="fused_grouped_experts"></a>`fused_grouped_experts(cfg: GroupedExperts.Config)` — [`L710`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L710) — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="fused_swiglu"></a>`fused_swiglu(cfg: FeedForward.Config)` — [`L585`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L585) — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="silu_and_mul_autograd_backward"></a>`silu_and_mul_autograd_backward(ctx, grad_out)` — [`L347`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L347)
- <a id="silu_and_mul_backward_kernel"></a>`silu_and_mul_backward_kernel(grad_out: torch.Tensor, gate: torch.Tensor, up: torch.Tensor, offsets: torch.Tensor | None = None)` — [`L254`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L254)
- <a id="silu_and_mul_backward_op"></a>`silu_and_mul_backward_op(grad_out: torch.Tensor, gate: torch.Tensor, up: torch.Tensor, offsets: torch.Tensor | None = None)` — [`L324`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L324) — Compute gradients for ``torchtitan::silu_and_mul``.
- <a id="silu_and_mul_backward_op_fake"></a>`silu_and_mul_backward_op_fake(grad_out: torch.Tensor, gate: torch.Tensor, up: torch.Tensor, offsets: torch.Tensor | None = None)` — [`L335`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L335)
- <a id="silu_and_mul_forward_kernel"></a>`silu_and_mul_forward_kernel(gate: torch.Tensor, up: torch.Tensor, offsets: torch.Tensor | None = None)` — [`L219`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L219) — Compute ``silu(gate) * up`` with optional grouped_mm row offsets. — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="silu_and_mul_op"></a>`silu_and_mul_op(gate: torch.Tensor, up: torch.Tensor, offsets: torch.Tensor | None = None)` — [`L301`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L301) — Compute ``silu(gate) * up`` over optionally offset-limited rows. — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="silu_and_mul_op_fake"></a>`silu_and_mul_op_fake(gate: torch.Tensor, up: torch.Tensor, offsets: torch.Tensor | None = None)` — [`L311`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L311)
- <a id="silu_and_mul_setup_context"></a>`silu_and_mul_setup_context(ctx, inputs, output)` — [`L362`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L362)

## Module values
- <a id="_MAX_BLOCK_N"></a>`_MAX_BLOCK_N` — [`L91`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L91)
- <a id="_SILU_AND_MUL_BLOCK_M"></a>`_SILU_AND_MUL_BLOCK_M` — [`L92`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L92)
- <a id="__all__"></a>`__all__` — [`L79`](../../../../../../raw/code/torchtitan/torchtitan/overrides/fused_swiglu.py#L79)

