---
title: 'Module: csrc/ops/index/index.cc'
type: catalog
provenance: extracted
module: csrc/ops/index/index.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildIndexShlo: BuildIndexShlo(41bc2f71c8dc98d1).
  BuildBooleanMaskIndexShlo: BuildBooleanMaskIndexShlo(10f519958a87962f).
  AreConsecutive: '`$anonymous_namespace_csrc/ops/index/index.cc`/AreConsecutive(3af0d499e8ef0de).'
  DynamicUnindexedDim: '`$anonymous_namespace_csrc/ops/index/index.cc`/DynamicUnindexedDim#'
  DynamicUnindexedDim.out_dim: '`$anonymous_namespace_csrc/ops/index/index.cc`/DynamicUnindexedDim#out_dim.'
  DynamicUnindexedDim.dim_info: '`$anonymous_namespace_csrc/ops/index/index.cc`/DynamicUnindexedDim#dim_info.'
---
# Module: [`csrc/ops/index/index.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/index/index.cc)

## Classes
### <a id="DynamicUnindexedDim"></a>`DynamicUnindexedDim`
- def: [`csrc/ops/index/index.cc:45`](../../../../../../../raw/code/torch_tpu/csrc/ops/index/index.cc#L45)
- signature: `struct DynamicUnindexedDim`
- members:
  - <a id="DynamicUnindexedDim.dim_info"></a>`dim_info` — [`L46`](../../../../../../../raw/code/torch_tpu/csrc/ops/index/index.cc#L46)
  - <a id="DynamicUnindexedDim.out_dim"></a>`out_dim` — [`L47`](../../../../../../../raw/code/torch_tpu/csrc/ops/index/index.cc#L47)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildIndexShlo`](index.cc.md#BuildIndexShlo)

## Functions
- <a id="AreConsecutive"></a>`AreConsecutive(const Indices& indexed_dims)` — [`L50`](../../../../../../../raw/code/torch_tpu/csrc/ops/index/index.cc#L50)
- <a id="BuildBooleanMaskIndexShlo"></a>`BuildBooleanMaskIndexShlo(mlir::MlirOp self, mlir::MlirOp mask, int64_t dim_indexed, int64_t num_non_zero_elements)` — [`L186`](../../../../../../../raw/code/torch_tpu/csrc/ops/index/index.cc#L186) — Builds StableHLO for tensor indexing with a single boolean mask at
- <a id="BuildIndexShlo"></a>`BuildIndexShlo(mlir::ArrayRef<mlir::MlirOp> input_ops, Indices indexed_dims)` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/index/index.cc#L63) — Builds StableHLO for tensor indexing with integer index tensors.

