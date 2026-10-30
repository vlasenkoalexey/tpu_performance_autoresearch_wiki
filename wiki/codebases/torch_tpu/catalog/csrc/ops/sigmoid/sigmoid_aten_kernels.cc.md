---
title: 'Module: csrc/ops/sigmoid/sigmoid_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/sigmoid/sigmoid_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenSigmoidBackwardGradInput: AtenSigmoidBackwardGradInput(dcc870e438d8791).
  AtenSigmoidOut: AtenSigmoidOut(4655895dd4ef7692).
  AtenLogSigmoidForward: AtenLogSigmoidForward(9e2535fa0f011b65).
  AtenLogSigmoidBackward: AtenLogSigmoidBackward(7048bed50d562265).
  AtenLogSigmoidBackwardGradInput: AtenLogSigmoidBackwardGradInput(5c91f28b56e0652e).
  AtenLogSigmoidForwardOut: AtenLogSigmoidForwardOut(2f5532e1ad90f43e).
  LogSigmoidForward: '`$anonymous_namespace_csrc/ops/sigmoid/sigmoid_aten_kernels.cc`/LogSigmoidForward(913c4d2381e9ecb8).'
  LogSigmoidBackward: '`$anonymous_namespace_csrc/ops/sigmoid/sigmoid_aten_kernels.cc`/LogSigmoidBackward(89b8fee546f12a08).'
  BuildSigmoidShlo: BuildSigmoidShlo(a7867b6222e713f9).
  BuildSigmoidBackwardShlo: '`$anonymous_namespace_csrc/ops/sigmoid/sigmoid_aten_kernels.cc`/BuildSigmoidBackwardShlo(9dd408ac7de815bd).'
---
# Module: [`csrc/ops/sigmoid/sigmoid_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/sigmoid/sigmoid_aten_kernels.cc)

## Functions
- <a id="AtenLogSigmoidBackward"></a>`AtenLogSigmoidBackward(const at::Tensor& grad_output, const at::Tensor& self, const at::Tensor& buffer)` — [`L315`](../../../../../../../raw/code/torch_tpu/csrc/ops/sigmoid/sigmoid_aten_kernels.cc#L315)
- <a id="AtenLogSigmoidBackwardGradInput"></a>`AtenLogSigmoidBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, const at::Tensor& buffer, at::Tensor& grad_input)` — [`L303`](../../../../../../../raw/code/torch_tpu/csrc/ops/sigmoid/sigmoid_aten_kernels.cc#L303)
- <a id="AtenLogSigmoidForward"></a>`AtenLogSigmoidForward(const at::Tensor& self)` — [`L289`](../../../../../../../raw/code/torch_tpu/csrc/ops/sigmoid/sigmoid_aten_kernels.cc#L289)
- <a id="AtenLogSigmoidForwardOut"></a>`AtenLogSigmoidForwardOut(const at::Tensor& self, at::Tensor& out, at::Tensor& buffer)` — [`L281`](../../../../../../../raw/code/torch_tpu/csrc/ops/sigmoid/sigmoid_aten_kernels.cc#L281)
- <a id="AtenSigmoidBackwardGradInput"></a>`AtenSigmoidBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& output, at::Tensor& grad_input)` — [`L245`](../../../../../../../raw/code/torch_tpu/csrc/ops/sigmoid/sigmoid_aten_kernels.cc#L245)
- <a id="AtenSigmoidOut"></a>`AtenSigmoidOut(const at::Tensor& self, at::Tensor& out)` — [`L229`](../../../../../../../raw/code/torch_tpu/csrc/ops/sigmoid/sigmoid_aten_kernels.cc#L229)
- <a id="BuildSigmoidBackwardShlo"></a>`BuildSigmoidBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp output)` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/sigmoid/sigmoid_aten_kernels.cc#L54) — Sigmoid backward formula:
- <a id="BuildSigmoidShlo"></a>`BuildSigmoidShlo(mlir::MlirOp input_op)` — [`L209`](../../../../../../../raw/code/torch_tpu/csrc/ops/sigmoid/sigmoid_aten_kernels.cc#L209)
- <a id="LogSigmoidBackward"></a>`LogSigmoidBackward(const at::Tensor& grad_output, const at::Tensor& self, const at::Tensor& buffer, at::Tensor& grad_input)` — [`L160`](../../../../../../../raw/code/torch_tpu/csrc/ops/sigmoid/sigmoid_aten_kernels.cc#L160)
- <a id="LogSigmoidForward"></a>`LogSigmoidForward(const at::Tensor& self, at::Tensor& out, at::Tensor& buffer)` — [`L73`](../../../../../../../raw/code/torch_tpu/csrc/ops/sigmoid/sigmoid_aten_kernels.cc#L73)

