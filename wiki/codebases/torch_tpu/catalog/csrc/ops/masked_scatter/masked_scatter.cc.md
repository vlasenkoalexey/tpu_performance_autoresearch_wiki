---
title: 'Module: csrc/ops/masked_scatter/masked_scatter.cc'
type: catalog
provenance: extracted
module: csrc/ops/masked_scatter/masked_scatter.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildMaskedScatterShlo: BuildMaskedScatterShlo(28dc33d166dda8e).
  ComputeRowPartition: '`$anonymous_namespace_csrc/ops/masked_scatter/masked_scatter.cc`/ComputeRowPartition(c91388552207d892).'
  RowPartition.row_size: '`$anonymous_namespace_csrc/ops/masked_scatter/masked_scatter.cc`/RowPartition#row_size.'
  RowPartition.num_rows: '`$anonymous_namespace_csrc/ops/masked_scatter/masked_scatter.cc`/RowPartition#num_rows.'
  RowPartition: '`$anonymous_namespace_csrc/ops/masked_scatter/masked_scatter.cc`/RowPartition#'
  RowPartition.num_folded_trailing_dims: '`$anonymous_namespace_csrc/ops/masked_scatter/masked_scatter.cc`/RowPartition#num_folded_trailing_dims.'
---
# Module: [`csrc/ops/masked_scatter/masked_scatter.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_scatter/masked_scatter.cc)

## Classes
### <a id="RowPartition"></a>`RowPartition`
- def: [`csrc/ops/masked_scatter/masked_scatter.cc:41`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_scatter/masked_scatter.cc#L41)
- doc: A helper struct describing how a mask in the masked_scatter operation
- signature: `struct RowPartition`
- members:
  - <a id="RowPartition.num_folded_trailing_dims"></a>`num_folded_trailing_dims` — [`L43`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_scatter/masked_scatter.cc#L43) — Number of trailing dimensions folded into one row.
  - <a id="RowPartition.num_rows"></a>`num_rows` — [`L47`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_scatter/masked_scatter.cc#L47) — Number of rows, the number of elements divided by `row_size`.
  - <a id="RowPartition.row_size"></a>`row_size` — [`L45`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_scatter/masked_scatter.cc#L45) — Number of elements per row, i.e. the product of the folded dimensions.
- used by: [`BuildMaskedScatterShlo`](masked_scatter.cc.md#BuildMaskedScatterShlo), [`ComputeRowPartition`](masked_scatter.cc.md#ComputeRowPartition)

## Functions
- <a id="BuildMaskedScatterShlo"></a>`BuildMaskedScatterShlo(mlir::MlirOp input, mlir::MlirOp mask, mlir::MlirOp source)` — [`L77`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_scatter/masked_scatter.cc#L77) — Replaces the elements of `input` that `mask` selects by the leading elements
- <a id="ComputeRowPartition"></a>`ComputeRowPartition(const mlir::ArrayRef<int64_t> input_shape, const mlir::ArrayRef<int64_t> mask_shape)` — [`L52`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_scatter/masked_scatter.cc#L52) — Calculates the RowPartitions of a tensor of shape `input_shape` into the

