---
title: 'Module: torchtitan/experiments/tpu/kernels/sbd_splash/base.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/sbd_splash/base.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.sbd_splash.base`/
symbols:
  _attention_reference_impl: _attention_reference_impl().
  SegmentIds: SegmentIds#
  attention_reference: attention_reference().
  SegmentIds.q: SegmentIds#q.
  SegmentIds.kv: SegmentIds#kv.
  DEFAULT_MASK_VALUE.DEFAULT_MASK_VALUE: DEFAULT_MASK_VALUE.DEFAULT_MASK_VALUE.
  MaskInfo: MaskInfo.
  _attention_reference_custom_bwd: _attention_reference_custom_bwd().
  attention_reference_vjp: attention_reference_vjp().
---
# Module: [`torchtitan/experiments/tpu/kernels/sbd_splash/base.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/base.py)

## Classes
### <a id="SegmentIds"></a>`SegmentIds`  ·  implements/extends NamedTuple
- def: [`torchtitan/experiments/tpu/kernels/sbd_splash/base.py:20`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/base.py#L20)
- doc: SegmentIds for Q and KV sequences.
- signature: `class SegmentIds(NamedTuple):`
- members:
  - <a id="SegmentIds.kv"></a>`kv` — [`L41`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/base.py#L41)
  - <a id="SegmentIds.q"></a>`q` — [`L40`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/base.py#L40)
- used by: [`_splash_attention_forward`](splash_attention_kernel.md#_splash_attention_forward), [`_splash_attention_bwd`](splash_attention_kernel.md#_splash_attention_bwd), [`_splash_attention_custom`](splash_attention_kernel.md#_splash_attention_custom), [`_splash_attention_fwd`](splash_attention_kernel.md#_splash_attention_fwd), [`_splash_attention`](splash_attention_kernel.md#_splash_attention), [`_attention_reference_impl`](base.md#_attention_reference_impl), [`attention_reference`](base.md#attention_reference)

## Functions
- <a id="_attention_reference_custom_bwd"></a>`_attention_reference_custom_bwd(do, q, k, v, mask, segment_ids, sinks, o, logsumexp, mask_value: float = DEFAULT_MASK_VALUE, backward_impl: str = "vanilla", attn_logits_soft_cap: float | None = None)` — [`L102`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/base.py#L102)
- <a id="_attention_reference_impl"></a>`_attention_reference_impl(q: jax.Array, k: jax.Array, v: jax.Array, mask: jax.Array, segment_ids: SegmentIds | None, sinks: jax.Array | None, mask_value: float, save_residuals: bool, attn_logits_soft_cap: float | None)` — [`L61`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/base.py#L61)
- <a id="attention_reference"></a>`attention_reference(q: jax.Array, k: jax.Array, v: jax.Array, mask: jax.Array, segment_ids: SegmentIds | None = None, sinks: jax.Array | None = None, *, is_mqa: bool, mask_value: float = DEFAULT_MASK_VALUE, save_residuals: bool = False, attn_logits_soft_cap: float | None = None)` — [`L172`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/base.py#L172) — A JIT-compiled reference implementation of attention, handles MQA and MHA.
- <a id="attention_reference_vjp"></a>`attention_reference_vjp(do, q, k, v, mask, segment_ids, sinks, o, logsumexp, *, is_mqa: bool, backward_impl: str = "vanilla", attn_logits_soft_cap: float | None = None)` — [`L222`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/base.py#L222) — Wrapper for backward reference that handles GQA/MQA broadcasting and reduction.

## Module values
- <a id="DEFAULT_MASK_VALUE.DEFAULT_MASK_VALUE"></a>`DEFAULT_MASK_VALUE` — [`L15`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/base.py#L15)
- <a id="MaskInfo"></a>`MaskInfo` — [`L12`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/base.py#L12) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)

