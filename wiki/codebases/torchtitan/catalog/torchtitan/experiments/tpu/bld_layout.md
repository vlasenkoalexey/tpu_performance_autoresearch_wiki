---
title: 'Module: torchtitan/experiments/tpu/bld_layout.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/bld_layout.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.bld_layout`/
symbols:
  apply_bld_layout: apply_bld_layout().
  _BLDGQAttention._bld_qkv: _BLDGQAttention#_bld_qkv().
  _BLDGQAttention.forward: _BLDGQAttention#forward().
  _attention_eligible: _attention_eligible().
  _BLDGQAttention._bld_rope: _BLDGQAttention#_bld_rope().
  _QKV_FORWARDS: _QKV_FORWARDS.
  _BLOCK_FORWARDS: _BLOCK_FORWARDS.
  _BLDGQAttention: _BLDGQAttention#
  _swap_class: _swap_class().
  cossin_rotate: cossin_rotate().
  _class_forward: _class_forward().
  bld_skip_reason: bld_skip_reason().
  _SUBCLASSES._SUBCLASSES: _SUBCLASSES._SUBCLASSES.
  _bld_seq_len: _bld_seq_len().
  _BLDBlock.forward: _BLDBlock#forward().
  _BLDBlock: _BLDBlock#
  _BLDMoE: _BLDMoE#
  _BLDMoE.forward: _BLDMoE#forward().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/bld_layout.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py)

## Classes
### <a id="_BLDBlock"></a>`_BLDBlock`
- def: [`torchtitan/experiments/tpu/bld_layout.py:199`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L199)
- doc: Mixin: compute a \[T, D\]-in/\[T, D\]-out block on a \[B, L, D\] view.
- signature: `class _BLDBlock(nn.Module):`
- members:
  - <a id="_BLDBlock.forward"></a>`forward(self, x, attention_masks, positions=None, segment_ids=None)` — [`L202`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L202)
- uses (calls/refs, reference-scoped): [`_bld_seq_len`](bld_layout.md#_bld_seq_len)
- used by: [`apply_bld_layout`](bld_layout.md#apply_bld_layout)

### <a id="_BLDGQAttention"></a>`_BLDGQAttention`  ·  implements/extends GQAttention
- def: [`torchtitan/experiments/tpu/bld_layout.py:96`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L96)
- doc: `GQAttention` that also accepts, and then returns, \[B, L, D\].
- signature: `class _BLDGQAttention(GQAttention):`
- members:
  - <a id="_BLDGQAttention.forward"></a>`forward(self, x_TD: torch.Tensor, attention_masks, positions: torch.Tensor | None = None, segment_ids: torch.Tensor | None = None)` — [`L146`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L146)
- protocol/private: <a id="_BLDGQAttention._bld_qkv"></a>`_bld_qkv`[`L99`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L99), <a id="_BLDGQAttention._bld_rope"></a>`_bld_rope`[`L135`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L135)
- uses (calls/refs, reference-scoped): [`CosSinRoPE`](../../models/common/rope.md#CosSinRoPE), [`GQAttention`](../../models/common/attention.md#GQAttention), [`forward`](../../models/common/attention.md#GQAttention.forward), [`FusedQKVLinear`](../../models/common/attention.md#FusedQKVLinear), [`k_norm`](../../models/common/attention.md#GQAttention.k_norm), [`QKVLinear`](../../models/common/attention.md#QKVLinear), [`rope`](../../models/common/attention.md#GQAttention.rope), [`kv_rows`](qkv.md#TpuPackedQKVLinear.kv_rows), [`q_norm`](../../models/common/attention.md#GQAttention.q_norm), [`wqkv_packed`](qkv.md#TpuPackedQKVLinear.wqkv_packed), [`TpuPackedQKVLinear`](qkv.md#TpuPackedQKVLinear), [`apply_rotary_emb`](../../models/common/rope.md#CosSinRoPE.apply_rotary_emb), [`inner_attention`](../../models/common/attention.md#GQAttention.inner_attention), [`qkv_linear`](../../models/common/attention.md#GQAttention.qkv_linear), [`remat_should_recompute`](../../protocols/module.md#Module.remat_should_recompute), [`remat_region_name`](../../protocols/module.md#Module.remat_region_name), [`enable_gqa`](../../models/common/attention.md#GQAttention.enable_gqa), [`wo`](../../models/common/attention.md#GQAttention.wo), [`wqkv`](../../models/common/attention.md#FusedQKVLinear.wqkv), [`heads_per_kv`](../../models/common/attention.md#FusedQKVLinear.heads_per_kv), [`scaling`](../../models/common/attention.md#GQAttention.scaling), [`apply_rotary_emb`](../../models/common/rope.md#RoPE.apply_rotary_emb), [`q_rows`](qkv.md#TpuPackedQKVLinear.q_rows), [`_reshape_cache`](../../models/common/rope.md#RoPE._reshape_cache), [`wk`](../../models/common/attention.md#QKVLinear.wk), [`wq`](../../models/common/attention.md#QKVLinear.wq), [`wv`](../../models/common/attention.md#QKVLinear.wv), [`cossin_rotate`](bld_layout.md#cossin_rotate), [`UnflattenShim`](unflatten_shim.md#UnflattenShim), [`r_dim`](../../models/common/attention.md#FusedQKVLinear.r_dim)
- used by: [`apply_bld_layout`](bld_layout.md#apply_bld_layout), [`GQAttention`](../../models/common/attention.md#GQAttention), [`forward`](../../models/common/attention.md#GQAttention.forward), [`_attention_eligible`](bld_layout.md#_attention_eligible)

### <a id="_BLDMoE"></a>`_BLDMoE`
- def: [`torchtitan/experiments/tpu/bld_layout.py:216`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L216)
- doc: Mixin: run a \[T, D\] MoE on the flattened tokens of a \[B, L, D\] input.
- signature: `class _BLDMoE(nn.Module):`
- members:
  - <a id="_BLDMoE.forward"></a>`forward(self, x, *args, **kwargs)` — [`L219`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L219)
- used by: [`apply_bld_layout`](bld_layout.md#apply_bld_layout)

## Functions
- <a id="_attention_eligible"></a>`_attention_eligible(attn: nn.Module)` — [`L263`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L263)
- <a id="_bld_seq_len"></a>`_bld_seq_len(x: torch.Tensor)` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L63) — The L of a [T, D] activation's [B, L] split, or None for the [T] path.
- <a id="_class_forward"></a>`_class_forward(module: nn.Module)` — [`L251`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L251) — The module's class ``forward``, or None if an instance attribute shadows it.
- <a id="_swap_class"></a>`_swap_class(module: nn.Module, mixin: type)` — [`L236`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L236)
- <a id="apply_bld_layout"></a>`apply_bld_layout(model: nn.Module, *, skip_reason: str | None = None)` — [`L285`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L285) — Patch eligible dense blocks in ``model`` in place; returns how many. — documented in [tpu-layer-loop-remat-and-layouts](../../../../concepts/tpu-layer-loop-remat-and-layouts.md)
- <a id="bld_skip_reason"></a>`bld_skip_reason(parallelism)` — [`L274`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L274) — Why the [B, L] layout must stay off for this recipe, or None. — documented in [tpu-layer-loop-remat-and-layouts](../../../../concepts/tpu-layer-loop-remat-and-layouts.md)
- <a id="cossin_rotate"></a>`cossin_rotate(x: torch.Tensor, cos_h: torch.Tensor, sin_h: torch.Tensor)` — [`L78`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L78) — ``CosSinRoPE`` rotate-half on half-width FP32 cos/sin, without ``cat`` on x.

## Module values
- <a id="_BLOCK_FORWARDS"></a>`_BLOCK_FORWARDS` — [`L227`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L227)
- <a id="_QKV_FORWARDS"></a>`_QKV_FORWARDS` — [`L228`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L228)
- <a id="_SUBCLASSES._SUBCLASSES"></a>`_SUBCLASSES` — [`L233`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L233)
- <a id="__all__"></a>`__all__` — [`L322`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/bld_layout.py#L322)

