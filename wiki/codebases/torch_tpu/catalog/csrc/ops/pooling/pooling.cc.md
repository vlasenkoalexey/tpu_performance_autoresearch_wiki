---
title: 'Module: csrc/ops/pooling/pooling.cc'
type: catalog
provenance: extracted
module: csrc/ops/pooling/pooling.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  CreateBatchInput: CreateBatchInput(2f5970c6771db595).
  GetPoolingOutputSize: GetPoolingOutputSize(ea17215a0473aa77).
  ExpandAttribute: ExpandAttribute(de042eb575cea805).
  RemoveTrivialBatch: RemoveTrivialBatch(f12dcdc849a72837).
  GetReduceWindowAttributes: GetReduceWindowAttributes(973c09db4519667a).
  CeilModePadding: CeilModePadding(8399695f43a74284).
  GetSingleDim: '`$anonymous_namespace_csrc/ops/pooling/pooling.cc`/GetSingleDim(efc9fdad993f89f).'
---
# Module: [`csrc/ops/pooling/pooling.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.cc)

## Functions
- `CeilModePadding(const mlir::RankedTensorType& input_shape, mlir::ArrayRef<int64_t> kernel_size, mlir::ArrayRef<int64_t> stride, mlir::ArrayRef<int64_t> padding, mlir::ArrayRef<int64_t> dilation, bool ceil_mode)` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.cc#L100) — Calculates the adjusted (left_padding, right_padding) pairs given the padding
- <a id="CeilModePadding"></a>`CeilModePadding(const mlir::RankedTensorType& input_shape, mlir::ArrayRef<int64_t> kernel_size, mlir::ArrayRef<int64_t> stride, mlir::ArrayRef<int64_t> padding, mlir::ArrayRef<int64_t> dilation, bool ceil_mode)` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.cc#L100) — Calculates the adjusted (left_padding, right_padding) pairs given the padding
- <a id="CreateBatchInput"></a>`CreateBatchInput(mlir::MlirOp input, const int64_t spatial_dim_count)` — [`L42`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.cc#L42) — Adds a batch dimension of size 1 if the input tensor doesn't have it.
- <a id="ExpandAttribute"></a>`ExpandAttribute(const Dimensions& values, const int64_t dim)` — [`L67`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.cc#L67) — Expands the attribute to match the dim size.
- <a id="GetPoolingOutputSize"></a>`GetPoolingOutputSize(at::IntArrayRef input_size, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, const bool ceil_mode, const int64_t spatial_dim_count)` — [`L229`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.cc#L229) — Calculates the output dimensions for N-dimensional pooling operations (max
- <a id="GetReduceWindowAttributes"></a>`GetReduceWindowAttributes(mlir::MlirBuilder& builder, Dimensions kernel_size_attr, Dimensions stride_attr, Dimensions dilation_attr, std::vector<PaddingParams> padding_pairs, const int64_t spatial_dim_count, const int64_t total_num_dims)` — [`L155`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.cc#L155) — Creates the padding config to be used to pad the input tensor and iota tensor
- `GetReduceWindowAttributes(mlir::MlirBuilder& builder, Dimensions kernel_size_attr, Dimensions stride_attr, Dimensions dilation_attr, std::vector<PaddingParams> padding_pairs, const int64_t spatial_dim_count, const int64_t total_num_dims)` — [`L155`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.cc#L155) — Creates the padding config to be used to pad the input tensor and iota tensor
- <a id="GetSingleDim"></a>`GetSingleDim(const int64_t in, const int64_t i, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, const bool ceil_mode)` — [`L205`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.cc#L205)
- <a id="RemoveTrivialBatch"></a>`RemoveTrivialBatch(mlir::MlirOp batch_op, int64_t original_dim_size, int64_t spatial_dim_count)` — [`L82`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.cc#L82) — Removes the batch dimension if it doesn't have it at the beginning.

