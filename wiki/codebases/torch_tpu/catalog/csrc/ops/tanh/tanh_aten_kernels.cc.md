---
title: 'Module: csrc/ops/tanh/tanh_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/tanh/tanh_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenTanhBackwardGradInput: AtenTanhBackwardGradInput(dcc870e438d8791).
  BuildTanhBackwardGradInputShlo: '`$anonymous_namespace_csrc/ops/tanh/tanh_aten_kernels.cc`/BuildTanhBackwardGradInputShlo(9dd408ac7de815bd).'
---
# Module: [`csrc/ops/tanh/tanh_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/tanh/tanh_aten_kernels.cc)

## Functions
- <a id="AtenTanhBackwardGradInput"></a>`AtenTanhBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& output, at::Tensor& grad_input)` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/tanh/tanh_aten_kernels.cc#L63)
- <a id="BuildTanhBackwardGradInputShlo"></a>`BuildTanhBackwardGradInputShlo(mlir::MlirOp grad_output_op, mlir::MlirOp output_op)` — [`L44`](../../../../../../../raw/code/torch_tpu/csrc/ops/tanh/tanh_aten_kernels.cc#L44) — Builds the StableHLO graph for the backward pass of tanh.

