---
title: 'Module: csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenSegmentReduce: AtenSegmentReduce(56db75c82d68b7e9).
  BuildSegmentReduceShlo: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/BuildSegmentReduceShlo(388a8e5c91a4a41c).'
  ComputeSegmentIdsAndMaskedData: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/ComputeSegmentIdsAndMaskedData(fbf3b48940e1a6a8).'
  ParseSegmentReduceOp: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/ParseSegmentReduceOp(f05b60f956fcd271).'
  ExecuteScatterReduction: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/ExecuteScatterReduction(1ba8a130f4ecc4f1).'
  ComputeSegmentBoundariesAndLengths: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/ComputeSegmentBoundariesAndLengths(2b1c45c168d269e5).'
  ApplyInitialValue: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/ApplyInitialValue(d53955a9edf963d2).'
  PostProcessMeanReduction: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/PostProcessMeanReduction(dd4aaf918f9466c2).'
  SegmentReduceOp: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/SegmentReduceOp#'
  GetNeutralScalar: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/GetNeutralScalar(658dc855a222aab0).'
  SegmentReduceOp.kProd: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/SegmentReduceOp#kProd.'
  ComputeScatterIndices: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/ComputeScatterIndices(4868b366f9bdfd1c).'
  SegmentBoundariesAndLengths: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/SegmentBoundariesAndLengths#'
  SegmentReduceOp.kMean: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/SegmentReduceOp#kMean.'
  SegmentIdsAndMaskedData.data_masked: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/SegmentIdsAndMaskedData#data_masked.'
  SegmentIdsAndMaskedData: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/SegmentIdsAndMaskedData#'
  SegmentReduceOp.kMax: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/SegmentReduceOp#kMax.'
  SegmentReduceOp.kMin: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/SegmentReduceOp#kMin.'
  SegmentReduceOp.kSum: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/SegmentReduceOp#kSum.'
  SegmentIdsAndMaskedData.segment_ids: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/SegmentIdsAndMaskedData#segment_ids.'
  SegmentBoundariesAndLengths.boundary_indices: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/SegmentBoundariesAndLengths#boundary_indices.'
  SegmentBoundariesAndLengths.num_segments: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/SegmentBoundariesAndLengths#num_segments.'
  SegmentBoundariesAndLengths.lengths: '`$anonymous_namespace_csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`/SegmentBoundariesAndLengths#lengths.'
---
# Module: [`csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc)

## Classes
### <a id="SegmentBoundariesAndLengths"></a>`SegmentBoundariesAndLengths`
- def: [`csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc:132`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L132)
- signature: `struct SegmentBoundariesAndLengths`
- members:
  - <a id="SegmentBoundariesAndLengths.boundary_indices"></a>`boundary_indices` — [`L133`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L133)
  - <a id="SegmentBoundariesAndLengths.lengths"></a>`lengths` — [`L134`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L134)
  - <a id="SegmentBoundariesAndLengths.num_segments"></a>`num_segments` — [`L135`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L135)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ComputeSegmentBoundariesAndLengths`](segment_reduce_aten_kernels.cc.md#ComputeSegmentBoundariesAndLengths), [`data_masked`](segment_reduce_aten_kernels.cc.md#SegmentIdsAndMaskedData.data_masked)

### <a id="SegmentIdsAndMaskedData"></a>`SegmentIdsAndMaskedData`
- def: [`csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc:138`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L138)
- signature: `struct SegmentIdsAndMaskedData`
- members:
  - <a id="SegmentIdsAndMaskedData.data_masked"></a>`data_masked` — [`L140`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L140)
  - <a id="SegmentIdsAndMaskedData.segment_ids"></a>`segment_ids` — [`L139`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L139)
- uses (calls/refs, reference-scoped): [`SegmentBoundariesAndLengths`](segment_reduce_aten_kernels.cc.md#SegmentBoundariesAndLengths)
- used by: [`ComputeSegmentIdsAndMaskedData`](segment_reduce_aten_kernels.cc.md#ComputeSegmentIdsAndMaskedData), [`ComputeSegmentBoundariesAndLengths`](segment_reduce_aten_kernels.cc.md#ComputeSegmentBoundariesAndLengths)

### <a id="SegmentReduceOp"></a>`SegmentReduceOp`
- def: [`csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc:61`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L61)
- signature: `enum class SegmentReduceOp`
- members:
  - <a id="SegmentReduceOp.kMax"></a>`kMax` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L61)
  - <a id="SegmentReduceOp.kMean"></a>`kMean` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L61)
  - <a id="SegmentReduceOp.kMin"></a>`kMin` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L61)
  - <a id="SegmentReduceOp.kProd"></a>`kProd` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L61)
  - <a id="SegmentReduceOp.kSum"></a>`kSum` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L61)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`AtenSegmentReduce`](segment_reduce_aten_kernels.cc.md#AtenSegmentReduce), [`BuildSegmentReduceShlo`](segment_reduce_aten_kernels.cc.md#BuildSegmentReduceShlo), [`ComputeSegmentIdsAndMaskedData`](segment_reduce_aten_kernels.cc.md#ComputeSegmentIdsAndMaskedData), [`ParseSegmentReduceOp`](segment_reduce_aten_kernels.cc.md#ParseSegmentReduceOp), [`ExecuteScatterReduction`](segment_reduce_aten_kernels.cc.md#ExecuteScatterReduction), [`ApplyInitialValue`](segment_reduce_aten_kernels.cc.md#ApplyInitialValue), [`GetNeutralScalar`](segment_reduce_aten_kernels.cc.md#GetNeutralScalar)

## Functions
- <a id="ApplyInitialValue"></a>`ApplyInitialValue(mlir::MlirOp scatter_res, SegmentReduceOp reduce_op, mlir::MlirOp initial_op, const Dimensions& init_shape)` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L112)
- <a id="AtenSegmentReduce"></a>`AtenSegmentReduce(const at::Tensor& data, c10::string_view reduce, const std::optional<at::Tensor>& lengths, const std::optional<at::Tensor>& indices, const std::optional<at::Tensor>& offsets, int64_t axis, bool unsafe, const std::optional<at::Scalar>& initial)` — [`L459`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L459)
- <a id="BuildSegmentReduceShlo"></a>`BuildSegmentReduceShlo(mlir::MlirOp data, SegmentReduceOp reduce_op, std::optional<mlir::MlirOp> lengths_opt, std::optional<mlir::MlirOp> offsets_opt, int64_t axis, std::optional<mlir::MlirOp> initial_op)` — [`L409`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L409)
- <a id="ComputeScatterIndices"></a>`ComputeScatterIndices(mlir::MlirBuilder& builder, mlir::MlirOp segment_ids, int64_t axis, const Dimensions& data_shape, int64_t n_data_axis, mlir::Type index_type)` — [`L281`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L281)
- <a id="ComputeSegmentBoundariesAndLengths"></a>`ComputeSegmentBoundariesAndLengths(std::optional<mlir::MlirOp> lengths_opt, std::optional<mlir::MlirOp> offsets_opt, int64_t axis)` — [`L143`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L143)
- <a id="ComputeSegmentIdsAndMaskedData"></a>`ComputeSegmentIdsAndMaskedData(mlir::MlirOp data, mlir::MlirOp boundary_indices, mlir::MlirOp lengths, int64_t num_segments, int64_t axis, SegmentReduceOp reduce_op, mlir::Type computation_type, mlir::ElementType comp_elem_type, const Dimensions& data_shape, int64_t n_data_axis)` — [`L182`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L182)
- <a id="ExecuteScatterReduction"></a>`ExecuteScatterReduction(mlir::MlirBuilder& builder, mlir::MlirOp data_masked, mlir::MlirOp scatter_indices, SegmentReduceOp reduce_op, mlir::Type computation_type, mlir::ElementType comp_elem_type, const Dimensions& init_shape, int64_t axis, int64_t rank, std::optional<mlir::MlirOp> initial_op)` — [`L311`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L311)
- <a id="GetNeutralScalar"></a>`GetNeutralScalar(SegmentReduceOp reduce_op, mlir::Type computation_type)` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L85)
- <a id="ParseSegmentReduceOp"></a>`ParseSegmentReduceOp(std::string_view reduce_str)` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L63)
- <a id="PostProcessMeanReduction"></a>`PostProcessMeanReduction(mlir::MlirOp scatter_res, mlir::MlirOp lengths, int64_t axis, mlir::Type computation_type, const Dimensions& init_shape, std::optional<mlir::MlirOp> initial_op)` — [`L381`](../../../../../../../raw/code/torch_tpu/csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc#L381)

