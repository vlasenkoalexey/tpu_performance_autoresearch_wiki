---
title: 'Module: csrc/ops/threshold/threshold_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/threshold/threshold_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenThresholdOut: AtenThresholdOut(55309b41a6fed6d1).
  AtenThresholdBackwardGradInput: AtenThresholdBackwardGradInput(82d77f320475bbd9).
  ValidateThresholdInputs: '`$anonymous_namespace_csrc/ops/threshold/threshold_aten_kernels.cc`/ValidateThresholdInputs(fd0458bfc68bb174).'
  BuildThresholdBackwardShlo: '`$anonymous_namespace_csrc/ops/threshold/threshold_aten_kernels.cc`/BuildThresholdBackwardShlo(28dc33d166dda8e).'
  BuildThresholdShlo: '`$anonymous_namespace_csrc/ops/threshold/threshold_aten_kernels.cc`/BuildThresholdShlo(28dc33d166dda8e).'
---
# Module: [`csrc/ops/threshold/threshold_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/threshold/threshold_aten_kernels.cc)

## Functions
- <a id="AtenThresholdBackwardGradInput"></a>`AtenThresholdBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, const at::Scalar& threshold, at::Tensor& grad_input)` — [`L101`](../../../../../../../raw/code/torch_tpu/csrc/ops/threshold/threshold_aten_kernels.cc#L101)
- <a id="AtenThresholdOut"></a>`AtenThresholdOut(const at::Tensor& self, const at::Scalar& threshold, const at::Scalar& value, at::Tensor& out)` — [`L70`](../../../../../../../raw/code/torch_tpu/csrc/ops/threshold/threshold_aten_kernels.cc#L70)
- <a id="BuildThresholdBackwardShlo"></a>`BuildThresholdBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp self, mlir::MlirOp threshold)` — [`L52`](../../../../../../../raw/code/torch_tpu/csrc/ops/threshold/threshold_aten_kernels.cc#L52)
- <a id="BuildThresholdShlo"></a>`BuildThresholdShlo(mlir::MlirOp input, mlir::MlirOp threshold, mlir::MlirOp value)` — [`L44`](../../../../../../../raw/code/torch_tpu/csrc/ops/threshold/threshold_aten_kernels.cc#L44)
- <a id="ValidateThresholdInputs"></a>`ValidateThresholdInputs(const at::Tensor& self)` — [`L60`](../../../../../../../raw/code/torch_tpu/csrc/ops/threshold/threshold_aten_kernels.cc#L60)

