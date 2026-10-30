---
title: 'Module: csrc/ops/glu/glu_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/glu/glu_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenGluOut: AtenGluOut(bb14b1a8f74bfba5).
  AtenGluBackwardGradInput: AtenGluBackwardGradInput(fe3a9f4a9a9fbd7).
  BuildGluBackwardOut: '`$anonymous_namespace_csrc/ops/glu/glu_aten_kernels.cc`/BuildGluBackwardOut(2b2d8cf4976eb044).'
  AtenGluBackward: AtenGluBackward(908133a331202ae3).
  ValidateIsFloatingPoint: '`$anonymous_namespace_csrc/ops/glu/glu_aten_kernels.cc`/ValidateIsFloatingPoint(d8359b99282c084c).'
  BuildGluBackwardShlo: '`$anonymous_namespace_csrc/ops/glu/glu_aten_kernels.cc`/BuildGluBackwardShlo(33905599cf21d92f).'
  BuildGluShlo: '`$anonymous_namespace_csrc/ops/glu/glu_aten_kernels.cc`/BuildGluShlo(acd22fadc08999ad).'
---
# Module: [`csrc/ops/glu/glu_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/glu/glu_aten_kernels.cc)

## Functions
- <a id="AtenGluBackward"></a>`AtenGluBackward(const at::Tensor& grad_output, const at::Tensor& self, int64_t dim)` — [`L244`](../../../../../../../raw/code/torch_tpu/csrc/ops/glu/glu_aten_kernels.cc#L244)
- <a id="AtenGluBackwardGradInput"></a>`AtenGluBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, int64_t dim, at::Tensor& grad_input)` — [`L256`](../../../../../../../raw/code/torch_tpu/csrc/ops/glu/glu_aten_kernels.cc#L256)
- <a id="AtenGluOut"></a>`AtenGluOut(const at::Tensor& self, int64_t dim, at::Tensor& out)` — [`L214`](../../../../../../../raw/code/torch_tpu/csrc/ops/glu/glu_aten_kernels.cc#L214)
- <a id="BuildGluBackwardOut"></a>`BuildGluBackwardOut(const at::Tensor& grad_output, const at::Tensor& self, int64_t dim, at::Tensor& grad_input, OpParamCacheKeys param_keys)` — [`L161`](../../../../../../../raw/code/torch_tpu/csrc/ops/glu/glu_aten_kernels.cc#L161)
- <a id="BuildGluBackwardShlo"></a>`BuildGluBackwardShlo(int64_t dim, mlir::MlirOp grad_output, mlir::MlirOp self)` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/glu/glu_aten_kernels.cc#L100) — Builds the backward pass for Gated Linear Unit
- <a id="BuildGluShlo"></a>`BuildGluShlo(int64_t dim, mlir::MlirOp input)` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/ops/glu/glu_aten_kernels.cc#L49)
- <a id="ValidateIsFloatingPoint"></a>`ValidateIsFloatingPoint(const at::Tensor& tensor, const std::string_view name)` — [`L82`](../../../../../../../raw/code/torch_tpu/csrc/ops/glu/glu_aten_kernels.cc#L82)

