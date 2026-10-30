---
title: 'Module: csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenAdaptiveAvgPool3dOut: AtenAdaptiveAvgPool3dOut(95e61dcc9986dc60).
  AtenAdaptiveAvgPool2dBackward: AtenAdaptiveAvgPool2dBackward(91c7cc726c97ea99).
  AtenAdaptiveAvgPool3dBackwardGradInput: AtenAdaptiveAvgPool3dBackwardGradInput(dcc870e438d8791).
  AtenAdaptiveAvgPool3d: AtenAdaptiveAvgPool3d(9fe15d6baae0848c).
  AtenAdaptiveAvgPool2dOut: AtenAdaptiveAvgPool2dOut(95e61dcc9986dc60).
  AtenAdaptiveAvgPool2d: AtenAdaptiveAvgPool2d(9fe15d6baae0848c).
  AtenAdaptiveAvgPool3dBackward: AtenAdaptiveAvgPool3dBackward(91c7cc726c97ea99).
  AdaptiveAvgPool2dHelper: AdaptiveAvgPool2dHelper(6aa255671c4218a1).
  BuildScatterAdd1D: '`$anonymous_namespace_csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc`/BuildScatterAdd1D(b93c96fe0cc7f37a).'
  BuildGatherPool1D: '`$anonymous_namespace_csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc`/BuildGatherPool1D(b93c96fe0cc7f37a).'
  ValidateAdaptiveAvgPool2dInputs: ValidateAdaptiveAvgPool2dInputs(fd0458bfc68bb174).
  BuildAdaptiveAvgPool2dBackwardShlo: '`$anonymous_namespace_csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc`/BuildAdaptiveAvgPool2dBackwardShlo(9dd408ac7de815bd).'
  BuildAdaptiveAvgPool3dShlo: '`$anonymous_namespace_csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc`/BuildAdaptiveAvgPool3dShlo(5733c81291a2a72b).'
  BuildAdaptiveAvgPool3dBackwardShlo: '`$anonymous_namespace_csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc`/BuildAdaptiveAvgPool3dBackwardShlo(9dd408ac7de815bd).'
  BuildAdaptiveAvgPool2dShlo: '`$anonymous_namespace_csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc`/BuildAdaptiveAvgPool2dShlo(911fafcde469b297).'
  CreateI64Const: '`$anonymous_namespace_csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc`/CreateI64Const(8cd8424e6f8d1166).'
  ComputeAdaptiveIndices: '`$anonymous_namespace_csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc`/ComputeAdaptiveIndices(813704aa4be72f54).'
---
# Module: [`csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc)

## Functions
- <a id="AdaptiveAvgPool2dHelper"></a>`AdaptiveAvgPool2dHelper(const at::Tensor& self, c10::SymIntArrayRef output_size, at::ScalarType output_dtype, OpParamCacheKeys param_keys, std::optional<std::reference_wrapper<at::Tensor>> out = std::nullopt)` — [`L601`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc#L601)
- <a id="AtenAdaptiveAvgPool2d"></a>`AtenAdaptiveAvgPool2d(const at::Tensor& self, c10::SymIntArrayRef output_size)` — [`L694`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc#L694)
- <a id="AtenAdaptiveAvgPool2dBackward"></a>`AtenAdaptiveAvgPool2dBackward(const at::Tensor& grad_output, const at::Tensor& self)` — [`L847`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc#L847)
- <a id="AtenAdaptiveAvgPool2dOut"></a>`AtenAdaptiveAvgPool2dOut(const at::Tensor& self, c10::SymIntArrayRef output_size, at::Tensor& out)` — [`L681`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc#L681)
- <a id="AtenAdaptiveAvgPool3d"></a>`AtenAdaptiveAvgPool3d(const at::Tensor& self, c10::SymIntArrayRef output_size)` — [`L809`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc#L809)
- <a id="AtenAdaptiveAvgPool3dBackward"></a>`AtenAdaptiveAvgPool3dBackward(const at::Tensor& grad_output, const at::Tensor& self)` — [`L969`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc#L969)
- <a id="AtenAdaptiveAvgPool3dBackwardGradInput"></a>`AtenAdaptiveAvgPool3dBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, at::Tensor& grad_input)` — [`L907`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc#L907)
- <a id="AtenAdaptiveAvgPool3dOut"></a>`AtenAdaptiveAvgPool3dOut(const at::Tensor& self, c10::SymIntArrayRef output_size, at::Tensor& out)` — [`L704`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc#L704)
- <a id="BuildAdaptiveAvgPool2dBackwardShlo"></a>`BuildAdaptiveAvgPool2dBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp input)` — [`L502`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc#L502)
- <a id="BuildAdaptiveAvgPool2dShlo"></a>`BuildAdaptiveAvgPool2dShlo(mlir::MlirOp input_op, const int64_t in_h, const int64_t in_w, const int64_t out_h, const int64_t out_w, const int64_t spatial_dim_count)` — [`L266`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc#L266) — Implements the general case of 2D adaptive average pooling using separate 1D
- <a id="BuildAdaptiveAvgPool3dBackwardShlo"></a>`BuildAdaptiveAvgPool3dBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp input)` — [`L536`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc#L536)
- <a id="BuildAdaptiveAvgPool3dShlo"></a>`BuildAdaptiveAvgPool3dShlo(mlir::MlirOp input_op, const int64_t in_d, const int64_t in_h, const int64_t in_w, const int64_t out_d, const int64_t out_h, const int64_t out_w, const int64_t spatial_dim_count)` — [`L295`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc#L295) — Implements the general case of 3D adaptive average pooling using separate 1D
- <a id="BuildGatherPool1D"></a>`BuildGatherPool1D(mlir::MlirBuilder& builder, mlir::MlirOp input, const int64_t dim, const int64_t in_size, const int64_t out_size)` — [`L116`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc#L116) — 2. Padding: Pad the input tensor to the maximum length along the dimension,
- <a id="BuildScatterAdd1D"></a>`BuildScatterAdd1D(mlir::MlirBuilder& builder, mlir::MlirOp grad_output, const int64_t dim, const int64_t in_size, const int64_t out_size)` — [`L341`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc#L341) — Builds a 1D scatter-add operation (Backward of GatherPool).
- <a id="ComputeAdaptiveIndices"></a>`ComputeAdaptiveIndices(const int64_t in_size, const int64_t out_size, Dimensions& starts, Dimensions& lengths, int64_t& max_k)` — [`L70`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc#L70) — Computes the start and length of each interval along a given dimension based
- <a id="CreateI64Const"></a>`CreateI64Const(mlir::MlirBuilder& builder, const Dimensions& data)` — [`L86`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc#L86) — Helper: Create a 1D [N] int64 constant tensor.
- <a id="ValidateAdaptiveAvgPool2dInputs"></a>`ValidateAdaptiveAvgPool2dInputs(const at::Tensor& self)` — [`L578`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc#L578)

