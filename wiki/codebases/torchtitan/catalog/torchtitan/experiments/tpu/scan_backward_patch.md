---
title: 'Module: torchtitan/experiments/tpu/scan_backward_patch.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/scan_backward_patch.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.scan_backward_patch`/
symbols:
  apply_scan_reverse_backward_patch: apply_scan_reverse_backward_patch().
  _ReverseByIndex.scan_op: _ReverseByIndex#scan_op().
  _SCAN_MODULE: _SCAN_MODULE.
  _call_backward_reverse_indexed: _call_backward_reverse_indexed().
  _ReverseByIndex.installed: _ReverseByIndex#installed().
  _ReverseByIndex.flip: _ReverseByIndex#flip().
  _scan_over_descending_index: _scan_over_descending_index().
  _UPSTREAM_CALL_BACKWARD: _UPSTREAM_CALL_BACKWARD.
  _ReverseByIndex._paused: _ReverseByIndex#_paused().
  _TorchWithoutFlip.__init__: _TorchWithoutFlip#__init__().
  _ReverseByIndex.skipped: _ReverseByIndex#skipped.
  _upstream_still_reverses_by_flip: _upstream_still_reverses_by_flip().
  _ScanOpWithOneCallRewritten._rewritten_call: _ScanOpWithOneCallRewritten#_rewritten_call.
  _ReverseByIndex.reversed_by_index: _ReverseByIndex#reversed_by_index.
  _ReverseByIndex._real: _ReverseByIndex#_real.
  _ReverseByIndex: _ReverseByIndex#
  _ScanOpWithOneCallRewritten.__init__: _ScanOpWithOneCallRewritten#__init__().
  _ScanOpWithOneCallRewritten.__call__: _ScanOpWithOneCallRewritten#__call__().
  _ReverseByIndex.written_in_order: _ReverseByIndex#written_in_order.
  _REVERSE_SCAN_DEVICE_TYPE: _REVERSE_SCAN_DEVICE_TYPE.
  _scan_over_descending_index.step: _scan_over_descending_index().step().
  _TorchWithoutFlip: _TorchWithoutFlip#
  _ScanOpWithOneCallRewritten: _ScanOpWithOneCallRewritten#
  _ReverseByIndex.__init__: _ReverseByIndex#__init__().
  _TorchWithoutFlip.flip: _TorchWithoutFlip#flip.
  _TorchWithoutFlip.__getattr__: _TorchWithoutFlip#__getattr__().
---
# Module: [`torchtitan/experiments/tpu/scan_backward_patch.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py)

## Classes
### <a id="_ReverseByIndex"></a>`_ReverseByIndex`
- def: [`torchtitan/experiments/tpu/scan_backward_patch.py:133`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L133)
- members:
  - <a id="_ReverseByIndex._paused"></a>`_paused(self)` — [`L167`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L167) — Puts torch's own two names back while a scan of ours is traced.
  - <a id="_ReverseByIndex.flip"></a>`flip(self, x, dims)` — [`L183`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L183)
  - <a id="_ReverseByIndex.installed"></a>`installed(self)` — [`L151`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L151) — Swaps the two names for the dynamic extent of one call.
  - <a id="_ReverseByIndex.scan_op"></a>`scan_op(self, combine_gm, init, xs, additional_inputs=(), **kwargs)` — [`L199`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L199)
  - <a id="_ReverseByIndex.reversed_by_index"></a>`reversed_by_index` — [`L147`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L147)
  - <a id="_ReverseByIndex.skipped"></a>`skipped` — [`L145`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L145)
  - <a id="_ReverseByIndex.written_in_order"></a>`written_in_order` — [`L146`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L146)
- protocol/private: <a id="_ReverseByIndex.__init__"></a>`__init__`[`L144`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L144), <a id="_ReverseByIndex._real"></a>`_real`[`L148`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L148)
- uses (calls/refs, reference-scoped): [`_SCAN_MODULE`](scan_backward_patch.md#_SCAN_MODULE), [`_scan_over_descending_index`](scan_backward_patch.md#_scan_over_descending_index), [`_ScanOpWithOneCallRewritten`](scan_backward_patch.md#_ScanOpWithOneCallRewritten), [`_TorchWithoutFlip`](scan_backward_patch.md#_TorchWithoutFlip)
- used by: [`_call_backward_reverse_indexed`](scan_backward_patch.md#_call_backward_reverse_indexed), [`__init__`](scan_backward_patch.md#_TorchWithoutFlip.__init__), [`_rewritten_call`](scan_backward_patch.md#_ScanOpWithOneCallRewritten._rewritten_call), [`__init__`](scan_backward_patch.md#_ScanOpWithOneCallRewritten.__init__)

### <a id="_ScanOpWithOneCallRewritten"></a>`_ScanOpWithOneCallRewritten`
- def: [`torchtitan/experiments/tpu/scan_backward_patch.py:235`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L235)
- protocol/private: <a id="_ScanOpWithOneCallRewritten.__call__"></a>`__call__`[`L248`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L248), <a id="_ScanOpWithOneCallRewritten.__init__"></a>`__init__`[`L244`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L244), <a id="_ScanOpWithOneCallRewritten._rewritten_call"></a>`_rewritten_call`[`L246`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L246)
- uses (calls/refs, reference-scoped): [`scan_op`](scan_backward_patch.md#_ReverseByIndex.scan_op), [`_ReverseByIndex`](scan_backward_patch.md#_ReverseByIndex)
- used by: [`installed`](scan_backward_patch.md#_ReverseByIndex.installed)

### <a id="_TorchWithoutFlip"></a>`_TorchWithoutFlip`
- def: [`torchtitan/experiments/tpu/scan_backward_patch.py:225`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L225)
- members:
  - <a id="_TorchWithoutFlip.flip"></a>`flip` — [`L229`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L229)
- protocol/private: <a id="_TorchWithoutFlip.__getattr__"></a>`__getattr__`[`L231`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L231), <a id="_TorchWithoutFlip.__init__"></a>`__init__`[`L228`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L228)
- uses (calls/refs, reference-scoped): [`flip`](scan_backward_patch.md#_ReverseByIndex.flip), [`_ReverseByIndex`](scan_backward_patch.md#_ReverseByIndex)
- used by: [`installed`](scan_backward_patch.md#_ReverseByIndex.installed)

## Functions
- <a id="_call_backward_reverse_indexed"></a>`_call_backward_reverse_indexed(self, *grad_fw_outputs)` — [`L105`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L105)
- <a id="_scan_over_descending_index"></a>`_scan_over_descending_index(combine_gm, init, xs, additional_inputs)` — [`L259`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L259) — `scan(combine_gm, init, xs, reverse=True)` without reversing the inputs.
- <a id="_upstream_still_reverses_by_flip"></a>`_upstream_still_reverses_by_flip()` — [`L88`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L88) — The startup check, so the usual break is caught before any work.
- <a id="apply_scan_reverse_backward_patch"></a>`apply_scan_reverse_backward_patch()` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L61) — Installs the patch. Returns whether it took. — documented in [tpu-layer-loop-remat-and-layouts](../../../../concepts/tpu-layer-loop-remat-and-layouts.md)
- <a id="_scan_over_descending_index.step"></a>`step(*args)` — [`L300`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L300)

## Module values
- <a id="_REVERSE_SCAN_DEVICE_TYPE"></a>`_REVERSE_SCAN_DEVICE_TYPE` — [`L256`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L256)
- <a id="_SCAN_MODULE"></a>`_SCAN_MODULE` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L55)
- <a id="_UPSTREAM_CALL_BACKWARD"></a>`_UPSTREAM_CALL_BACKWARD` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/scan_backward_patch.py#L51)

