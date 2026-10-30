---
title: 'Module: csrc/ops/sort/sort.h'
type: catalog
provenance: extracted
module: csrc/ops/sort/sort.h
status: fresh
symbol_base: cxx . . $ torch_tpu/SortShloOutputs#
symbols:
  SortShloOutputs.indices: indices.
  SortShloOutputs: ''
  SortShloOutputs.values: values.
---
# Module: [`csrc/ops/sort/sort.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/sort/sort.h)

## Classes
### <a id="SortShloOutputs"></a>`SortShloOutputs`
- def: [`csrc/ops/sort/sort.h:26`](../../../../../../../raw/code/torch_tpu/csrc/ops/sort/sort.h#L26)
- signature: `struct SortShloOutputs`
- members:
  - <a id="SortShloOutputs.indices"></a>`indices` — [`L28`](../../../../../../../raw/code/torch_tpu/csrc/ops/sort/sort.h#L28)
  - <a id="SortShloOutputs.values"></a>`values` — [`L27`](../../../../../../../raw/code/torch_tpu/csrc/ops/sort/sort.h#L27)
- uses (calls/refs, reference-scoped): [`BuildSortShlo`](sort.cc.md#BuildSortShlo)
- used by: [`AtenSortValuesStable`](sort_aten_kernels.cc.md#AtenSortValuesStable), [`BuildUnique2Shlo`](../unique/unique.cc.md#BuildUnique2Shlo), [`BuildNonzeroShlo`](../nonzero/nonzero.cc.md#BuildNonzeroShlo), [`BuildSvdTallAndSquare`](../linalg/linalg_svd_kernels.cc.md#BuildSvdTallAndSquare), [`BuildSortEigenPairs`](../linalg/linalg_svd_kernels.cc.md#BuildSortEigenPairs), [`BuildUniqueGetOutputSizeShlo`](../unique/unique.cc.md#BuildUniqueGetOutputSizeShlo), [`BuildSortShlo`](sort.cc.md#BuildSortShlo)

