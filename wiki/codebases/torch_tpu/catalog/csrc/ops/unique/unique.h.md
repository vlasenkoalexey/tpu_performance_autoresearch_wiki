---
title: 'Module: csrc/ops/unique/unique.h'
type: catalog
provenance: extracted
module: csrc/ops/unique/unique.h
status: fresh
symbol_base: cxx . . $ torch_tpu/BuildUniqueShloOutputs#
symbols:
  BuildUniqueShloOutputs.counts: counts.
  BuildUniqueShloOutputs.inverse_indices: inverse_indices.
  BuildUniqueShloOutputs: ''
  BuildUniqueShloOutputs.unique_values: unique_values.
---
# Module: [`csrc/ops/unique/unique.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique/unique.h)

## Classes
### <a id="BuildUniqueShloOutputs"></a>`BuildUniqueShloOutputs`
- def: [`csrc/ops/unique/unique.h:28`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique/unique.h#L28)
- signature: `struct BuildUniqueShloOutputs`
- members:
  - <a id="BuildUniqueShloOutputs.counts"></a>`counts` — [`L31`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique/unique.h#L31)
  - <a id="BuildUniqueShloOutputs.inverse_indices"></a>`inverse_indices` — [`L30`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique/unique.h#L30)
  - <a id="BuildUniqueShloOutputs.unique_values"></a>`unique_values` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique/unique.h#L29)
- uses (calls/refs, reference-scoped): [`BuildUnique2Shlo`](unique.cc.md#BuildUnique2Shlo), [`BuildUniqueGetOutputSizeShlo`](unique.cc.md#BuildUniqueGetOutputSizeShlo)
- used by: [`Unique2`](unique_aten_kernels.cc.md#Unique2), [`BuildUnique2Shlo`](unique.cc.md#BuildUnique2Shlo), [`BuildUniqueGetOutputSizeShlo`](unique.cc.md#BuildUniqueGetOutputSizeShlo)

