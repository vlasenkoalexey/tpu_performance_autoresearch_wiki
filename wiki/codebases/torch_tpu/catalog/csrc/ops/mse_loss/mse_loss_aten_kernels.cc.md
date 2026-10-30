---
title: 'Module: csrc/ops/mse_loss/mse_loss_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/mse_loss/mse_loss_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenMseLossBackward: AtenMseLossBackward(2f4a0512dc7e15bc).
  AtenMseLossOut: AtenMseLossOut(fe3a9f4a9a9fbd7).
  BuildMseLossShlo: '`$anonymous_namespace_csrc/ops/mse_loss/mse_loss_aten_kernels.cc`/BuildMseLossShlo(bf6ee81c4c258460).'
  BuildMseLossBackwardShlo: '`$anonymous_namespace_csrc/ops/mse_loss/mse_loss_aten_kernels.cc`/BuildMseLossBackwardShlo(ab0bcbaedd8b267f).'
---
# Module: [`csrc/ops/mse_loss/mse_loss_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/mse_loss/mse_loss_aten_kernels.cc)

## Functions
- <a id="AtenMseLossBackward"></a>`AtenMseLossBackward(const at::Tensor& grad_output, const at::Tensor& self, const at::Tensor& target, int64_t reduction)` — [`L165`](../../../../../../../raw/code/torch_tpu/csrc/ops/mse_loss/mse_loss_aten_kernels.cc#L165)
- <a id="AtenMseLossOut"></a>`AtenMseLossOut(const at::Tensor& self, const at::Tensor& target, int64_t reduction, at::Tensor& out)` — [`L109`](../../../../../../../raw/code/torch_tpu/csrc/ops/mse_loss/mse_loss_aten_kernels.cc#L109)
- <a id="BuildMseLossBackwardShlo"></a>`BuildMseLossBackwardShlo(mlir::MlirOp grad_output_op, mlir::MlirOp self_op, mlir::MlirOp target_op, int64_t reduction)` — [`L74`](../../../../../../../raw/code/torch_tpu/csrc/ops/mse_loss/mse_loss_aten_kernels.cc#L74)
- <a id="BuildMseLossShlo"></a>`BuildMseLossShlo(mlir::MlirOp self_op, mlir::MlirOp target_op, int64_t reduction)` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/ops/mse_loss/mse_loss_aten_kernels.cc#L48)

