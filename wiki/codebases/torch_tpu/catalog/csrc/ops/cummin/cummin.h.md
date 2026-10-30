---
title: 'Module: csrc/ops/cummin/cummin.h'
type: catalog
provenance: extracted
module: csrc/ops/cummin/cummin.h
status: fresh
symbol_base: cxx . . $ torch_tpu/CumminOutputs#
symbols:
  CumminOutputs.indices: indices.
  CumminOutputs: ''
  CumminOutputs.values: values.
---
# Module: [`csrc/ops/cummin/cummin.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/cummin/cummin.h)

## Classes
### <a id="CumminOutputs"></a>`CumminOutputs`
- def: [`csrc/ops/cummin/cummin.h:27`](../../../../../../../raw/code/torch_tpu/csrc/ops/cummin/cummin.h#L27)
- signature: `struct CumminOutputs`
- members:
  - <a id="CumminOutputs.indices"></a>`indices` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/cummin/cummin.h#L29)
  - <a id="CumminOutputs.values"></a>`values` — [`L28`](../../../../../../../raw/code/torch_tpu/csrc/ops/cummin/cummin.h#L28)
- uses (calls/refs, reference-scoped): [`BuildCumminShlo`](cummin.cc.md#BuildCumminShlo)
- used by: [`AtenCumminHelper`](cummin_aten_kernels.cc.md#AtenCumminHelper), [`BuildCumminShlo`](cummin.cc.md#BuildCumminShlo)

