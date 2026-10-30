---
title: 'Module: csrc/ops/convolution/convolution.cc'
type: catalog
provenance: extracted
module: csrc/ops/convolution/convolution.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildConvolution: '`$anonymous_namespace_csrc/ops/convolution/convolution.cc`/BuildConvolution(98edd42340ff85bd).'
  BuildConvolutionBackwardInput: BuildConvolutionBackwardInput(1ffe7945c2b26eef).
  BuildConvolutionBackwardBias: BuildConvolutionBackwardBias(c116150205aa322e).
  BuildTransposedConvolution: '`$anonymous_namespace_csrc/ops/convolution/convolution.cc`/BuildTransposedConvolution(c9d0b896904222df).'
  BuildConvolutionBackwardWeight: BuildConvolutionBackwardWeight(1ffe7945c2b26eef).
  CalculateWindowAlignedPadding: '`$anonymous_namespace_csrc/ops/convolution/convolution.cc`/CalculateWindowAlignedPadding(74d013c033ec7970).'
  CalculateAdjointPadding: '`$anonymous_namespace_csrc/ops/convolution/convolution.cc`/CalculateAdjointPadding(74d013c033ec7970).'
  SpatialPadding.hi: '`$anonymous_namespace_csrc/ops/convolution/convolution.cc`/SpatialPadding#hi.'
  SpatialPadding: '`$anonymous_namespace_csrc/ops/convolution/convolution.cc`/SpatialPadding#'
  SpatialPadding.lo: '`$anonymous_namespace_csrc/ops/convolution/convolution.cc`/SpatialPadding#lo.'
---
# Module: [`csrc/ops/convolution/convolution.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution.cc)

## Classes
### <a id="SpatialPadding"></a>`SpatialPadding`
- def: [`csrc/ops/convolution/convolution.cc:52`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution.cc#L52)
- signature: `struct SpatialPadding`
- members:
  - <a id="SpatialPadding.hi"></a>`hi` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution.cc#L54)
  - <a id="SpatialPadding.lo"></a>`lo` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution.cc#L53)
- used by: [`CalculateAdjointPadding`](convolution.cc.md#CalculateAdjointPadding)

## Functions
- `BuildConvolution(mlir::MlirOp input, mlir::MlirOp weight, std::optional<mlir::MlirOp> bias, absl::Span<const int64_t> stride, absl::Span<const int64_t> padding, absl::Span<const int64_t> dilation, bool transposed, absl::Span<const int64_t> output_padding, int64_t groups, absl::Span<const int64_t> output_dims, mlir::ElementType output_dtype, mlir::stablehlo::Precision precision)` — [`L348`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution.cc#L348)
- `BuildConvolution(mlir::MlirOp input, mlir::MlirOp weight, std::optional<mlir::MlirOp> bias, absl::Span<const int64_t> stride, absl::Span<const int64_t> padding, absl::Span<const int64_t> dilation, bool transposed, absl::Span<const int64_t> output_padding, int64_t groups, absl::Span<const int64_t> output_dims, mlir::ElementType output_dtype, mlir::stablehlo::Precision precision)` — [`L348`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution.cc#L348)
- <a id="BuildConvolution"></a>`BuildConvolution(mlir::MlirOp input, mlir::MlirOp weight, std::optional<mlir::MlirOp> bias, absl::Span<const int64_t> stride, absl::Span<const int64_t> padding, absl::Span<const int64_t> dilation, int64_t groups, absl::Span<const int64_t> output_dims, mlir::ElementType output_dtype, mlir::stablehlo::Precision precision, const std::optional<stablehlo::Dimensions>& result_dims = std::nullopt)` — [`L237`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution.cc#L237)
- `BuildConvolution(mlir::MlirOp input, mlir::MlirOp weight, std::optional<mlir::MlirOp> bias, absl::Span<const int64_t> stride, absl::Span<const int64_t> padding, absl::Span<const int64_t> dilation, int64_t groups, absl::Span<const int64_t> output_dims, mlir::ElementType output_dtype, mlir::stablehlo::Precision precision, const std::optional<stablehlo::Dimensions>& result_dims = std::nullopt)` — [`L237`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution.cc#L237)
- <a id="BuildConvolutionBackwardBias"></a>`BuildConvolutionBackwardBias(mlir::MlirOp grad_output, mlir::ElementType output_dtype)` — [`L683`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution.cc#L683)
- <a id="BuildConvolutionBackwardInput"></a>`BuildConvolutionBackwardInput(mlir::MlirOp grad_output, mlir::MlirOp input, mlir::MlirOp weight, absl::Span<const int64_t> stride, absl::Span<const int64_t> padding, absl::Span<const int64_t> dilation, int64_t groups, bool transposed, mlir::ElementType output_dtype, mlir::stablehlo::Precision precision)` — [`L379`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution.cc#L379) — From the chain The gradient of loss function L w.r.t. input x equals dL/y *
- `BuildConvolutionBackwardInput(mlir::MlirOp grad_output, mlir::MlirOp input, mlir::MlirOp weight, absl::Span<const int64_t> stride, absl::Span<const int64_t> padding, absl::Span<const int64_t> dilation, int64_t groups, bool transposed, mlir::ElementType output_dtype, mlir::stablehlo::Precision precision)` — [`L379`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution.cc#L379) — From the chain The gradient of loss function L w.r.t. input x equals dL/y *
- <a id="BuildConvolutionBackwardWeight"></a>`BuildConvolutionBackwardWeight(mlir::MlirOp input, mlir::MlirOp grad_output, mlir::MlirOp weight, absl::Span<const int64_t> stride, absl::Span<const int64_t> padding, absl::Span<const int64_t> dilation, int64_t groups, bool transposed, mlir::ElementType output_dtype, mlir::stablehlo::Precision precision)` — [`L571`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution.cc#L571) — Builds the gradient w.r.t. the convolution weight. `weight` is only used for
- `BuildConvolutionBackwardWeight(mlir::MlirOp input, mlir::MlirOp grad_output, mlir::MlirOp weight, absl::Span<const int64_t> stride, absl::Span<const int64_t> padding, absl::Span<const int64_t> dilation, int64_t groups, bool transposed, mlir::ElementType output_dtype, mlir::stablehlo::Precision precision)` — [`L571`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution.cc#L571) — Builds the gradient w.r.t. the convolution weight. `weight` is only used for
- <a id="BuildTransposedConvolution"></a>`BuildTransposedConvolution(mlir::MlirOp input, mlir::MlirOp weight, std::optional<mlir::MlirOp> bias, absl::Span<const int64_t> stride, absl::Span<const int64_t> padding, absl::Span<const int64_t> dilation, absl::Span<const int64_t> output_padding, int64_t groups, absl::Span<const int64_t> output_dims, mlir::ElementType output_dtype, mlir::stablehlo::Precision precision)` — [`L98`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution.cc#L98)
- `BuildTransposedConvolution(mlir::MlirOp input, mlir::MlirOp weight, std::optional<mlir::MlirOp> bias, absl::Span<const int64_t> stride, absl::Span<const int64_t> padding, absl::Span<const int64_t> dilation, absl::Span<const int64_t> output_padding, int64_t groups, absl::Span<const int64_t> output_dims, mlir::ElementType output_dtype, mlir::stablehlo::Precision precision)` — [`L98`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution.cc#L98)
- <a id="CalculateAdjointPadding"></a>`CalculateAdjointPadding(int64_t input_dim, int64_t output_dim, int64_t kernel, int64_t stride, int64_t padding, int64_t dilation)` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution.cc#L63) — Calculates the padding required for the adjoint (backward/transposed)
- <a id="CalculateWindowAlignedPadding"></a>`CalculateWindowAlignedPadding(int64_t operand_dim, int64_t num_windows, int64_t kernel, int64_t stride, int64_t padding, int64_t dilation)` — [`L87`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution.cc#L87) — Calculates the asymmetric padding of a convolution operand of size

