---
title: 'Module: csrc/ops/softplus/softplus_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/softplus/softplus_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenSoftplusBackwardGradInput: AtenSoftplusBackwardGradInput(748a141ca95b5f86).
  AtenSoftplusOut: AtenSoftplusOut(55309b41a6fed6d1).
  BuildSoftplusShlo: '`$anonymous_namespace_csrc/ops/softplus/softplus_aten_kernels.cc`/BuildSoftplusShlo(28dc33d166dda8e).'
  BuildSoftplusBackwardShlo: '`$anonymous_namespace_csrc/ops/softplus/softplus_aten_kernels.cc`/BuildSoftplusBackwardShlo(ac48754f9fea6edd).'
---
# Module: [`csrc/ops/softplus/softplus_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/softplus/softplus_aten_kernels.cc)

## Functions
- <a id="AtenSoftplusBackwardGradInput"></a>`AtenSoftplusBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, const at::Scalar& beta, const at::Scalar& threshold, at::Tensor& grad_input)` — [`L124`](../../../../../../../raw/code/torch_tpu/csrc/ops/softplus/softplus_aten_kernels.cc#L124)
- <a id="AtenSoftplusOut"></a>`AtenSoftplusOut(const at::Tensor& self, const at::Scalar& beta, const at::Scalar& threshold, at::Tensor& out)` — [`L84`](../../../../../../../raw/code/torch_tpu/csrc/ops/softplus/softplus_aten_kernels.cc#L84)
- <a id="BuildSoftplusBackwardShlo"></a>`BuildSoftplusBackwardShlo(mlir::MlirOp grad_output_op, mlir::MlirOp input_op, mlir::MlirOp beta_op, mlir::MlirOp threshold_op)` — [`L62`](../../../../../../../raw/code/torch_tpu/csrc/ops/softplus/softplus_aten_kernels.cc#L62)
- <a id="BuildSoftplusShlo"></a>`BuildSoftplusShlo(mlir::MlirOp input_op, mlir::MlirOp beta_op, mlir::MlirOp threshold_op)` — [`L43`](../../../../../../../raw/code/torch_tpu/csrc/ops/softplus/softplus_aten_kernels.cc#L43)

