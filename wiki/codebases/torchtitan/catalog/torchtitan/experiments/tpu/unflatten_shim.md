---
title: 'Module: torchtitan/experiments/tpu/unflatten_shim.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/unflatten_shim.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.unflatten_shim`/
symbols:
  set_unflatten_seq_len: set_unflatten_seq_len().
  unflatten_tensor: unflatten_tensor().
  get_unflatten_seq_len: get_unflatten_seq_len().
  flatten_tensor: flatten_tensor().
  UnflattenShim.forward: UnflattenShim#forward().
  _ACTIVE_SEQ_LEN._ACTIVE_SEQ_LEN: _ACTIVE_SEQ_LEN._ACTIVE_SEQ_LEN.
  UnflattenShim: UnflattenShim#
  UnflattenShim.inner: UnflattenShim#inner.
  UnflattenShim.__init__: UnflattenShim#__init__().
---
# Module: [`torchtitan/experiments/tpu/unflatten_shim.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/unflatten_shim.py)

## Classes
### <a id="UnflattenShim"></a>`UnflattenShim`
- def: [`torchtitan/experiments/tpu/unflatten_shim.py:75`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/unflatten_shim.py#L75)
- doc: TT-UNFLATTEN-SHIM: nn.Module wrapper acting as a kernel boundary unflatten/flatten mechanism.
- signature: `class UnflattenShim(torch.nn.Module):`
- members:
  - <a id="UnflattenShim.forward"></a>`forward(self, *args, **kwargs)` — [`L83`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/unflatten_shim.py#L83)
  - <a id="UnflattenShim.inner"></a>`inner` — [`L81`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/unflatten_shim.py#L81)
- protocol/private: <a id="UnflattenShim.__init__"></a>`__init__`[`L79`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/unflatten_shim.py#L79)
- uses (calls/refs, reference-scoped): [`unflatten_tensor`](unflatten_shim.md#unflatten_tensor), [`flatten_tensor`](unflatten_shim.md#flatten_tensor)
- used by: [`forward`](bld_layout.md#_BLDGQAttention.forward), [`use_splash_attention_patch`](workarounds.md#use_splash_attention_patch)

## Functions
- <a id="flatten_tensor"></a>`flatten_tensor(t: torch.Tensor, original_flat_ndim: int = 3)` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/unflatten_shim.py#L62) — Flattens [B, S] back to [T] if and only if tensor length is original_flat_ndim + 1.
- <a id="get_unflatten_seq_len"></a>`get_unflatten_seq_len()` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/unflatten_shim.py#L34)
- <a id="set_unflatten_seq_len"></a>`set_unflatten_seq_len(seq_len: int)` — [`L24`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/unflatten_shim.py#L24) — Context manager to activate unflatten mapping with the exact S dimension.
- <a id="unflatten_tensor"></a>`unflatten_tensor(t: torch.Tensor, expected_flat_ndim: int = 3)` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/unflatten_shim.py#L37) — Unflattens dim 0 from [T] to [B, S].

## Module values
- <a id="_ACTIVE_SEQ_LEN._ACTIVE_SEQ_LEN"></a>`_ACTIVE_SEQ_LEN` — [`L21`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/unflatten_shim.py#L21)

