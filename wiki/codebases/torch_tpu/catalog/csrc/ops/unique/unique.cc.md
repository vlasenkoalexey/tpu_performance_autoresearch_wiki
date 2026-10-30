---
title: 'Module: csrc/ops/unique/unique.cc'
type: catalog
provenance: extracted
module: csrc/ops/unique/unique.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildUnique2Shlo: BuildUnique2Shlo(d06ed5dc9152ce1b).
  BuildUniqueGetOutputSizeShlo: BuildUniqueGetOutputSizeShlo(817781fe40e3dee0).
  BuildUniqueMask: '`$anonymous_namespace_csrc/ops/unique/unique.cc`/BuildUniqueMask(aa90c1a702c5351e).'
  BuildCumsum1D: '`$anonymous_namespace_csrc/ops/unique/unique.cc`/BuildCumsum1D(aa90c1a702c5351e).'
  FlattenIfNeeded: '`$anonymous_namespace_csrc/ops/unique/unique.cc`/FlattenIfNeeded(cf97982c188f832c).'
---
# Module: [`csrc/ops/unique/unique.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique/unique.cc)

## Functions
- <a id="BuildCumsum1D"></a>`BuildCumsum1D(mlir::MlirBuilder& builder, mlir::MlirOp input)` — [`L69`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique/unique.cc#L69)
- <a id="BuildUnique2Shlo"></a>`BuildUnique2Shlo(int64_t output_size, mlir::MlirOp input, bool sorted, bool return_inverse, bool return_counts)` — [`L124`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique/unique.cc#L124)
- <a id="BuildUniqueGetOutputSizeShlo"></a>`BuildUniqueGetOutputSizeShlo(mlir::ElementType element_type, mlir::MlirOp input, bool sorted)` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique/unique.cc#L100)
- <a id="BuildUniqueMask"></a>`BuildUniqueMask(mlir::MlirBuilder& builder, mlir::MlirOp sorted_input)` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique/unique.cc#L48)
- <a id="FlattenIfNeeded"></a>`FlattenIfNeeded(mlir::MlirOp input)` — [`L40`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique/unique.cc#L40)

