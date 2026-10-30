---
title: 'Module: csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenLeakyReluOut: AtenLeakyReluOut(95f92c0e0348af54).
  AtenLeakyReluBackwardGradInput: AtenLeakyReluBackwardGradInput(a5314925babb2785).
  AtenLeakyReluBackwardTensorHelper: '`$anonymous_namespace_csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc`/AtenLeakyReluBackwardTensorHelper(c22d115553b4d79d).'
  AtenLeakyReluTensorHelper: '`$anonymous_namespace_csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc`/AtenLeakyReluTensorHelper(c55a4aea24ae5a63).'
  LeakyReluBackwardScalarHelper: '`$anonymous_namespace_csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc`/LeakyReluBackwardScalarHelper(f90547bcd9fcc766).'
  LeakyReluScalarHelper: '`$anonymous_namespace_csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc`/LeakyReluScalarHelper(57dd4cb93de61043).'
  BuildLeakyReluBackwardShlo: '`$anonymous_namespace_csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc`/BuildLeakyReluBackwardShlo(6949d37ea308da71).'
  BuildLeakyReluShlo: '`$anonymous_namespace_csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc`/BuildLeakyReluShlo(4e058530975e9b5a).'
---
# Module: [`csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc)

## Functions
- <a id="AtenLeakyReluBackwardGradInput"></a>`AtenLeakyReluBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self_or_result, const at::Scalar& negative_slope, bool self_is_result, at::Tensor& grad_input)` — [`L192`](../../../../../../../raw/code/torch_tpu/csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc#L192)
- <a id="AtenLeakyReluBackwardTensorHelper"></a>`AtenLeakyReluBackwardTensorHelper(const at::Tensor& grad_output, const at::Tensor& self_or_result, const at::Tensor& negative_slope, bool self_is_result, OpParamCacheKeys param_keys, at::Tensor& grad_input)` — [`L116`](../../../../../../../raw/code/torch_tpu/csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc#L116)
- <a id="AtenLeakyReluOut"></a>`AtenLeakyReluOut(const at::Tensor& self, const at::Scalar& negative_slope, at::Tensor& out)` — [`L179`](../../../../../../../raw/code/torch_tpu/csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc#L179)
- <a id="AtenLeakyReluTensorHelper"></a>`AtenLeakyReluTensorHelper(const at::Tensor& self, const at::Tensor& negative_slope, at::Tensor& out, OpParamCacheKeys param_keys)` — [`L88`](../../../../../../../raw/code/torch_tpu/csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc#L88)
- <a id="BuildLeakyReluBackwardShlo"></a>`BuildLeakyReluBackwardShlo(mlir::MlirOp grad_output_op, mlir::MlirOp self_or_result_op, mlir::MlirOp negative_slope_op, mlir::ElementType out_dtype)` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc#L65)
- <a id="BuildLeakyReluShlo"></a>`BuildLeakyReluShlo(mlir::MlirOp self_op, mlir::MlirOp negative_slope_op, mlir::ElementType out_dtype)` — [`L44`](../../../../../../../raw/code/torch_tpu/csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc#L44)
- <a id="LeakyReluBackwardScalarHelper"></a>`LeakyReluBackwardScalarHelper(const at::Tensor& grad_output, const at::Tensor& self_or_result, PromotedScalar negative_slope, bool self_is_result, OpParamCacheKeys param_keys, at::Tensor& grad_input)` — [`L160`](../../../../../../../raw/code/torch_tpu/csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc#L160)
- <a id="LeakyReluScalarHelper"></a>`LeakyReluScalarHelper(const at::Tensor& self, PromotedScalar negative_slope, at::Tensor& out, OpParamCacheKeys param_keys)` — [`L150`](../../../../../../../raw/code/torch_tpu/csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc#L150)

