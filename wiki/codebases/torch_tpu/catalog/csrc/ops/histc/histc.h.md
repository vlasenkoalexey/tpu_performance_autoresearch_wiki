---
title: 'Module: csrc/ops/histc/histc.h'
type: catalog
provenance: extracted
module: csrc/ops/histc/histc.h
status: fresh
symbol_base: cxx . . $ torch_tpu/HistcBounds#
symbols:
  HistcBounds.max: max.
  HistcBounds: ''
  HistcBounds.min: min.
---
# Module: [`csrc/ops/histc/histc.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc.h)

## Classes
### <a id="HistcBounds"></a>`HistcBounds`
- def: [`csrc/ops/histc/histc.h:27`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc.h#L27)
- signature: `struct HistcBounds`
- members:
  - <a id="HistcBounds.max"></a>`max` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc.h#L29)
  - <a id="HistcBounds.min"></a>`min` — [`L28`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc.h#L28)
- uses (calls/refs, reference-scoped): [`BuildHistcShlo`](histc.cc.md#BuildHistcShlo), [`BuildHistcBoundsShlo`](histc.cc.md#BuildHistcBoundsShlo)
- used by: [`HistcHelperOut`](histc_aten_kernels.cc.md#HistcHelperOut), [`BuildScatterAdd`](histc.cc.md#BuildScatterAdd), [`BuildHistcBoundsShlo`](histc.cc.md#BuildHistcBoundsShlo)

