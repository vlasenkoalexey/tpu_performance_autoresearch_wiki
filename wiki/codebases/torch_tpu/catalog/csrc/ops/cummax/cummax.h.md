---
title: 'Module: csrc/ops/cummax/cummax.h'
type: catalog
provenance: extracted
module: csrc/ops/cummax/cummax.h
status: fresh
symbol_base: cxx . . $ torch_tpu/CummaxOutputs#
symbols:
  CummaxOutputs.indices: indices.
  CummaxOutputs: ''
  CummaxOutputs.values: values.
---
# Module: [`csrc/ops/cummax/cummax.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/cummax/cummax.h)

## Classes
### <a id="CummaxOutputs"></a>`CummaxOutputs`
- def: [`csrc/ops/cummax/cummax.h:27`](../../../../../../../raw/code/torch_tpu/csrc/ops/cummax/cummax.h#L27)
- signature: `struct CummaxOutputs`
- members:
  - <a id="CummaxOutputs.indices"></a>`indices` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/cummax/cummax.h#L29)
  - <a id="CummaxOutputs.values"></a>`values` — [`L28`](../../../../../../../raw/code/torch_tpu/csrc/ops/cummax/cummax.h#L28)
- uses (calls/refs, reference-scoped): [`BuildCummaxShlo`](cummax.cc.md#BuildCummaxShlo)
- used by: [`AtenCummaxHelper`](cummax_aten_kernels.cc.md#AtenCummaxHelper), [`BuildCummaxShlo`](cummax.cc.md#BuildCummaxShlo)

