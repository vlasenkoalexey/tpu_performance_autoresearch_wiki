---
title: 'Module: csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenUniqueConsecutive: AtenUniqueConsecutive(fb1fa2a07bf275b3).
  AtenUniqueDimConsecutive: AtenUniqueDimConsecutive(6fbb57b2d361a8d0).
  UniqueConsecutiveDispatch: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/UniqueConsecutiveDispatch(46abd538e8c844ad).'
  ValidateUniqueConsecutiveDimInputs: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/ValidateUniqueConsecutiveDimInputs(d1706849fca7ff50).'
  BuildUniqueConsecutiveFlattenedShlo: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/BuildUniqueConsecutiveFlattenedShlo(cea5c0756b9039d5).'
  BuildUniqueConsecutiveGetOutputSizeShlo: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/BuildUniqueConsecutiveGetOutputSizeShlo(246b4823ccf7cdee).'
  BuildUniqueConsecutiveDimShlo: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/BuildUniqueConsecutiveDimShlo(80362498427e90fd).'
  GetUniqueConsecutiveCount: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/GetUniqueConsecutiveCount(adaa04c7089c8095).'
  BuildUniqueConsecutiveScalarShlo: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/BuildUniqueConsecutiveScalarShlo(ba89416f0d58e9ba).'
  UniqueConsecutiveDimHelper: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/UniqueConsecutiveDimHelper(6fbb57b2d361a8d0).'
  BuildUniqueConsecutiveEmptyShlo: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/BuildUniqueConsecutiveEmptyShlo(1961e81556214d85).'
  UniqueConsecutiveFlattenedHelper: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/UniqueConsecutiveFlattenedHelper(1e3971a836fa336d).'
  BuildUniqueConsecutiveMaskDim: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/BuildUniqueConsecutiveMaskDim(4dea081824b5da67).'
  BuildInverseIndices: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/BuildInverseIndices(f14105b93c4db5ae).'
  ExtractOutputSize: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/ExtractOutputSize(31c8c37cc6a727c6).'
  BuildUniqueConsecutiveShlo: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/BuildUniqueConsecutiveShlo(f3518ab16cd19687).'
  BuildUniqueConsecutiveMask1D: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/BuildUniqueConsecutiveMask1D(aa90c1a702c5351e).'
  BuildCounts: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/BuildCounts(ee5195a48b9d168b).'
  BuildUniqueConsecutiveShloOutputs.inverse_indices: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/BuildUniqueConsecutiveShloOutputs#inverse_indices.'
  FlattenIfNeeded: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/FlattenIfNeeded(cf97982c188f832c).'
  BuildUniqueConsecutiveShloOutputs: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/BuildUniqueConsecutiveShloOutputs#'
  BuildCumsum1D: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/BuildCumsum1D(aa90c1a702c5351e).'
  ComputeInverseDimensions: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/ComputeInverseDimensions(fed67977bb48ee7c).'
  BuildUniqueConsecutiveShloOutputs.counts: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/BuildUniqueConsecutiveShloOutputs#counts.'
  BuildUniqueConsecutiveShloOutputs.unique_values: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/BuildUniqueConsecutiveShloOutputs#unique_values.'
  ComputeValuesDimensions: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/ComputeValuesDimensions(d1f6d1c261191ed5).'
  ExtractSortedUniqueIndices: '`$anonymous_namespace_csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`/ExtractSortedUniqueIndices(ee5195a48b9d168b).'
---
# Module: [`csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc)

## Classes
### <a id="BuildUniqueConsecutiveShloOutputs"></a>`BuildUniqueConsecutiveShloOutputs`
- def: [`csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc:62`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L62)
- signature: `struct BuildUniqueConsecutiveShloOutputs`
- members:
  - <a id="BuildUniqueConsecutiveShloOutputs.counts"></a>`counts` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L65)
  - <a id="BuildUniqueConsecutiveShloOutputs.inverse_indices"></a>`inverse_indices` — [`L64`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L64)
  - <a id="BuildUniqueConsecutiveShloOutputs.unique_values"></a>`unique_values` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L63)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`UniqueConsecutiveDispatch`](unique_consecutive_aten_kernels.cc.md#UniqueConsecutiveDispatch), [`BuildUniqueConsecutiveDimShlo`](unique_consecutive_aten_kernels.cc.md#BuildUniqueConsecutiveDimShlo), [`BuildUniqueConsecutiveFlattenedShlo`](unique_consecutive_aten_kernels.cc.md#BuildUniqueConsecutiveFlattenedShlo), [`BuildUniqueConsecutiveGetOutputSizeShlo`](unique_consecutive_aten_kernels.cc.md#BuildUniqueConsecutiveGetOutputSizeShlo), [`BuildUniqueConsecutiveScalarShlo`](unique_consecutive_aten_kernels.cc.md#BuildUniqueConsecutiveScalarShlo), [`BuildUniqueConsecutiveEmptyShlo`](unique_consecutive_aten_kernels.cc.md#BuildUniqueConsecutiveEmptyShlo)

## Functions
- <a id="AtenUniqueConsecutive"></a>`AtenUniqueConsecutive(const at::Tensor& self, const bool return_inverse, const bool return_counts, std::optional<int64_t> dim)` — [`L622`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L622)
- <a id="AtenUniqueDimConsecutive"></a>`AtenUniqueDimConsecutive(const at::Tensor& self, const int64_t dim, const bool return_inverse, const bool return_counts)` — [`L639`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L639)
- <a id="BuildCounts"></a>`BuildCounts(mlir::MlirBuilder& builder, mlir::MlirOp unique_indices, const int64_t total_elements, const int64_t output_size)` — [`L238`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L238)
- <a id="BuildCumsum1D"></a>`BuildCumsum1D(mlir::MlirBuilder& builder, mlir::MlirOp input)` — [`L154`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L154)
- <a id="BuildInverseIndices"></a>`BuildInverseIndices(mlir::MlirBuilder& builder, mlir::MlirOp mask, const mlir::RankedTensorType& original_type, std::optional<int64_t> dim)` — [`L220`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L220)
- <a id="BuildUniqueConsecutiveDimShlo"></a>`BuildUniqueConsecutiveDimShlo(mlir::MlirBuilder& builder, mlir::MlirOp input, const mlir::RankedTensorType& input_type, const int64_t dim, const int64_t output_size, const bool return_inverse, const bool return_counts)` — [`L341`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L341)
- <a id="BuildUniqueConsecutiveEmptyShlo"></a>`BuildUniqueConsecutiveEmptyShlo(mlir::MlirBuilder& builder, const mlir::RankedTensorType& input_type, const mlir::ElementType val_type, const bool return_inverse, std::optional<int64_t> dim)` — [`L308`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L308)
- <a id="BuildUniqueConsecutiveFlattenedShlo"></a>`BuildUniqueConsecutiveFlattenedShlo(mlir::MlirBuilder& builder, mlir::MlirOp input, const mlir::RankedTensorType& input_type, const int64_t output_size, const bool return_inverse, const bool return_counts)` — [`L373`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L373)
- <a id="BuildUniqueConsecutiveGetOutputSizeShlo"></a>`BuildUniqueConsecutiveGetOutputSizeShlo(mlir::MlirOp input, std::optional<int64_t> dim)` — [`L253`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L253)
- <a id="BuildUniqueConsecutiveMask1D"></a>`BuildUniqueConsecutiveMask1D(mlir::MlirBuilder& builder, mlir::MlirOp flat_input)` — [`L76`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L76)
- <a id="BuildUniqueConsecutiveMaskDim"></a>`BuildUniqueConsecutiveMaskDim(mlir::MlirBuilder& builder, mlir::MlirOp input, const int64_t dim)` — [`L97`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L97)
- <a id="BuildUniqueConsecutiveScalarShlo"></a>`BuildUniqueConsecutiveScalarShlo(mlir::MlirBuilder& builder, mlir::MlirOp input, const bool return_inverse, const bool return_counts)` — [`L286`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L286)
- <a id="BuildUniqueConsecutiveShlo"></a>`BuildUniqueConsecutiveShlo(const int64_t output_size, mlir::MlirOp input, const bool return_inverse, const bool return_counts, std::optional<int64_t> dim)` — [`L420`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L420)
- <a id="ComputeInverseDimensions"></a>`ComputeInverseDimensions(const at::Tensor& self, const bool return_inverse, std::optional<int64_t> dim)` — [`L499`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L499)
- <a id="ComputeValuesDimensions"></a>`ComputeValuesDimensions(const at::Tensor& self, const int64_t output_size, std::optional<int64_t> dim)` — [`L488`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L488)
- <a id="ExtractOutputSize"></a>`ExtractOutputSize(const at::Tensor& count_tensor)` — [`L445`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L445)
- <a id="ExtractSortedUniqueIndices"></a>`ExtractSortedUniqueIndices(mlir::MlirBuilder& builder, mlir::MlirOp mask, const int64_t total_elements, const int64_t output_size)` — [`L187`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L187)
- <a id="FlattenIfNeeded"></a>`FlattenIfNeeded(mlir::MlirOp input)` — [`L68`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L68)
- <a id="GetUniqueConsecutiveCount"></a>`GetUniqueConsecutiveCount(const at::Tensor& self, std::optional<int64_t> dim)` — [`L473`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L473)
- <a id="UniqueConsecutiveDimHelper"></a>`UniqueConsecutiveDimHelper(const at::Tensor& self, const int64_t dim, const bool return_inverse, const bool return_counts)` — [`L563`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L563)
- <a id="UniqueConsecutiveDispatch"></a>`UniqueConsecutiveDispatch(const at::Tensor& self, const int64_t output_size, const bool return_inverse, const bool return_counts, std::optional<int64_t> dim)` — [`L512`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L512)
- <a id="UniqueConsecutiveFlattenedHelper"></a>`UniqueConsecutiveFlattenedHelper(const at::Tensor& self, const bool return_inverse, const bool return_counts)` — [`L593`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L593)
- <a id="ValidateUniqueConsecutiveDimInputs"></a>`ValidateUniqueConsecutiveDimInputs(const at::Tensor& self, const int64_t wrapped_dim)` — [`L453`](../../../../../../../raw/code/torch_tpu/csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc#L453)

