---
title: 'Module: csrc/ops/pooling/avg_pool_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/pooling/avg_pool_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenAvgPool1d: AtenAvgPool1d(560f735d3c19f29).
  AtenAvgPool3dOut: AtenAvgPool3dOut(436f2214755c3aa5).
  AtenAvgPool2dOut: AtenAvgPool2dOut(436f2214755c3aa5).
  AtenAvgPool1dOut: AtenAvgPool1dOut(3861ee97ad8354b0).
  AtenAvgPool3dBackwardGradInput: AtenAvgPool3dBackwardGradInput(e42e959afc2d3fe).
  AtenAvgPool2dBackwardGradInput: AtenAvgPool2dBackwardGradInput(e42e959afc2d3fe).
  ScaleAvgPoolOutput: '`$anonymous_namespace_csrc/ops/pooling/avg_pool_aten_kernels.cc`/ScaleAvgPoolOutput(b750e038267c779).'
  BuildAvgPoolOutNd: BuildAvgPoolOutNd(59474f2b1286499d).
  BuildAvgPoolBackwardGradInputNd: BuildAvgPoolBackwardGradInputNd(6c6d1070f49e0ba8).
  BuildAvgPoolShlo: '`$anonymous_namespace_csrc/ops/pooling/avg_pool_aten_kernels.cc`/BuildAvgPoolShlo(382cc80664689551).'
  BuildAvgPoolBackwardShlo: '`$anonymous_namespace_csrc/ops/pooling/avg_pool_aten_kernels.cc`/BuildAvgPoolBackwardShlo(f7f2f0f75939dc9).'
  ValidateAvgPool1dDtype: '`$anonymous_namespace_csrc/ops/pooling/avg_pool_aten_kernels.cc`/ValidateAvgPool1dDtype(fd0458bfc68bb174).'
  BuildAvgPoolNd: BuildAvgPoolNd(f0db10bfbd3ec137).
  SliceBackwardResult: '`$anonymous_namespace_csrc/ops/pooling/avg_pool_aten_kernels.cc`/SliceBackwardResult(10e4c303ceff765f).'
  GetAvgPoolOpBuilder: '`$anonymous_namespace_csrc/ops/pooling/avg_pool_aten_kernels.cc`/GetAvgPoolOpBuilder(b15b7a90cdc65b02).'
  k3dSpatialDimCount: '`$anonymous_namespace_csrc/ops/pooling/avg_pool_aten_kernels.cc`/k3dSpatialDimCount.'
---
# Module: [`csrc/ops/pooling/avg_pool_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc)

## Functions
- <a id="AtenAvgPool1d"></a>`AtenAvgPool1d(const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, bool ceil_mode, bool count_include_pad)` — [`L611`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc#L611)
- <a id="AtenAvgPool1dOut"></a>`AtenAvgPool1dOut(const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, bool ceil_mode, bool count_include_pad, at::Tensor& out)` — [`L637`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc#L637)
- <a id="AtenAvgPool2dBackwardGradInput"></a>`AtenAvgPool2dBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, bool ceil_mode, bool count_include_pad, std::optional<int64_t> divisor_override, at::Tensor& grad_input)` — [`L729`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc#L729)
- <a id="AtenAvgPool2dOut"></a>`AtenAvgPool2dOut(const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, bool ceil_mode, bool count_include_pad, std::optional<int64_t> divisor_override, at::Tensor& out)` — [`L657`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc#L657)
- <a id="AtenAvgPool3dBackwardGradInput"></a>`AtenAvgPool3dBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, bool ceil_mode, bool count_include_pad, std::optional<int64_t> divisor_override, at::Tensor& grad_input)` — [`L749`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc#L749)
- <a id="AtenAvgPool3dOut"></a>`AtenAvgPool3dOut(const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, bool ceil_mode, bool count_include_pad, std::optional<int64_t> divisor_override, at::Tensor& out)` — [`L693`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc#L693)
- <a id="BuildAvgPoolBackwardGradInputNd"></a>`BuildAvgPoolBackwardGradInputNd(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, bool ceil_mode, bool count_include_pad, std::optional<int64_t> divisor_override, at::Tensor& grad_input, int64_t spatial_dim_count, OpParamCacheKeys param_keys)` — [`L578`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc#L578) — Helper function to build and dispatch N-dimensional average pooling backward
- <a id="BuildAvgPoolBackwardShlo"></a>`BuildAvgPoolBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp input, int64_t spatial_dim_count, const Dimensions& kernel_size, const Dimensions& stride, const Dimensions& padding, bool ceil_mode, bool count_include_pad, std::optional<int64_t> divisor_override)` — [`L382`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc#L382)
- <a id="BuildAvgPoolNd"></a>`BuildAvgPoolNd(const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, bool ceil_mode, bool count_include_pad, std::optional<int64_t> divisor_override, mlir::ElementType out_dtype, at::IntArrayRef out_sizes, int64_t spatial_dim_count, OpParamCacheKeys param_keys, std::optional<OpName> override_op_name)` — [`L535`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc#L535) — Helper function to build and dispatch N-dimensional average pooling
- <a id="BuildAvgPoolOutNd"></a>`BuildAvgPoolOutNd(const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, bool ceil_mode, bool count_include_pad, std::optional<int64_t> divisor_override, at::Tensor& out, int64_t spatial_dim_count, OpParamCacheKeys param_keys)` — [`L552`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc#L552)
- <a id="BuildAvgPoolShlo"></a>`BuildAvgPoolShlo(mlir::MlirOp input, int64_t spatial_dim_count, Dimensions kernel_size, Dimensions stride, Dimensions padding, bool ceil_mode, bool count_include_pad, std::optional<int64_t> divisor_override)` — [`L213`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc#L213)
- <a id="GetAvgPoolOpBuilder"></a>`GetAvgPoolOpBuilder(at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, bool ceil_mode, bool count_include_pad, std::optional<int64_t> divisor_override, int64_t spatial_dim_count)` — [`L498`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc#L498)
- <a id="ScaleAvgPoolOutput"></a>`ScaleAvgPoolOutput(mlir::MlirOp dividend, const mlir::RankedTensorType& input_type, const ReduceWindowAttributes& reduce_window_attributes, bool count_include_pad, std::optional<int64_t> divisor_override)` — [`L76`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc#L76) — Scales the output of the pooling reduction (sum) by the divisor.
- `SliceBackwardResult(mlir::MlirOp full_conv_result, mlir::MlirOp init_value, const mlir::RankedTensorType& input_type, const std::vector<PaddingParams>& ceil_padding_pairs, int64_t num_dims, int64_t spatial_dim_count)` — [`L337`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc#L337) — Mathematically, average pooling is a linear transformation that can be
- <a id="SliceBackwardResult"></a>`SliceBackwardResult(mlir::MlirOp full_conv_result, mlir::MlirOp init_value, const mlir::RankedTensorType& input_type, const std::vector<PaddingParams>& ceil_padding_pairs, int64_t num_dims, int64_t spatial_dim_count)` — [`L337`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc#L337) — Mathematically, average pooling is a linear transformation that can be
- <a id="ValidateAvgPool1dDtype"></a>`ValidateAvgPool1dDtype(const at::Tensor& self)` — [`L514`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc#L514)

## Module values
- <a id="k3dSpatialDimCount"></a>`k3dSpatialDimCount` — [`L66`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/avg_pool_aten_kernels.cc#L66) — Number of spatial dimensions (D, H, W) for 3D average pooling.

