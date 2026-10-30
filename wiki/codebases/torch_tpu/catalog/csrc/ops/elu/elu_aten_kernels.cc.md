---
title: 'Module: csrc/ops/elu/elu_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/elu/elu_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenEluBackwardGradInput: AtenEluBackwardGradInput(d01dc91b3f88c634).
  AtenEluOut: AtenEluOut(ef9106b3773a8adf).
  ValidateIsFloatingPoint: '`$anonymous_namespace_csrc/ops/elu/elu_aten_kernels.cc`/ValidateIsFloatingPoint(d8359b99282c084c).'
  BuildEluBackwardGradInputShlo: '`$anonymous_namespace_csrc/ops/elu/elu_aten_kernels.cc`/BuildEluBackwardGradInputShlo(ee50317e3c305f8f).'
  BuildEluShlo: '`$anonymous_namespace_csrc/ops/elu/elu_aten_kernels.cc`/BuildEluShlo(ac48754f9fea6edd).'
---
# Module: [`csrc/ops/elu/elu_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/elu/elu_aten_kernels.cc)

## Functions
- <a id="AtenEluBackwardGradInput"></a>`AtenEluBackwardGradInput(const at::Tensor& grad_output, const at::Scalar& alpha, const at::Scalar& scale, const at::Scalar& input_scale, bool is_result, const at::Tensor& self_or_result, at::Tensor& grad_input)` — [`L166`](../../../../../../../raw/code/torch_tpu/csrc/ops/elu/elu_aten_kernels.cc#L166)
- <a id="AtenEluOut"></a>`AtenEluOut(const at::Tensor& input, const at::Scalar& alpha, const at::Scalar& scale, const at::Scalar& input_scale, at::Tensor& out)` — [`L129`](../../../../../../../raw/code/torch_tpu/csrc/ops/elu/elu_aten_kernels.cc#L129)
- <a id="BuildEluBackwardGradInputShlo"></a>`BuildEluBackwardGradInputShlo(mlir::MlirOp grad_output_op, mlir::MlirOp self_or_result_op, mlir::MlirOp alpha_op, mlir::MlirOp scale_op, mlir::MlirOp input_scale_op, bool is_result)` — [`L75`](../../../../../../../raw/code/torch_tpu/csrc/ops/elu/elu_aten_kernels.cc#L75)
- <a id="BuildEluShlo"></a>`BuildEluShlo(mlir::MlirOp input_op, mlir::MlirOp alpha_op, mlir::MlirOp scale_op, mlir::MlirOp input_scale_op)` — [`L44`](../../../../../../../raw/code/torch_tpu/csrc/ops/elu/elu_aten_kernels.cc#L44)
- <a id="ValidateIsFloatingPoint"></a>`ValidateIsFloatingPoint(const at::Tensor& tensor, const std::string_view name)` — [`L119`](../../../../../../../raw/code/torch_tpu/csrc/ops/elu/elu_aten_kernels.cc#L119)

