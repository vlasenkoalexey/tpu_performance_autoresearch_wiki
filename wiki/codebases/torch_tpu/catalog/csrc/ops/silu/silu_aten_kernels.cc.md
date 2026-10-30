---
title: 'Module: csrc/ops/silu/silu_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/silu/silu_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenSiluOut: AtenSiluOut(4655895dd4ef7692).
  AtenSiluBackward: AtenSiluBackward(91c7cc726c97ea99).
  AtenSiluBackwardGradInput: AtenSiluBackwardGradInput(dcc870e438d8791).
  ValidateSiluBackwardInputs: '`$anonymous_namespace_csrc/ops/silu/silu_aten_kernels.cc`/ValidateSiluBackwardInputs(b2d6689cde60befb).'
  BuildSiluShlo: '`$anonymous_namespace_csrc/ops/silu/silu_aten_kernels.cc`/BuildSiluShlo(a7867b6222e713f9).'
  BuildSiluBackwardShlo: '`$anonymous_namespace_csrc/ops/silu/silu_aten_kernels.cc`/BuildSiluBackwardShlo(9dd408ac7de815bd).'
  ValidateSiluBackwardInputsOrThrow: '`$anonymous_namespace_csrc/ops/silu/silu_aten_kernels.cc`/ValidateSiluBackwardInputsOrThrow(c0f540083bc2c76f).'
  AtenSiluBackwardAutograd: AtenSiluBackwardAutograd(91c7cc726c97ea99).
  IsFakeOrFunctorchTensor: '`$anonymous_namespace_csrc/ops/silu/silu_aten_kernels.cc`/IsFakeOrFunctorchTensor(b580d0b7e29ca914).'
  SiluBackwardComposite: '`$anonymous_namespace_csrc/ops/silu/silu_aten_kernels.cc`/SiluBackwardComposite(91c7cc726c97ea99).'
  IsFunctorchActive: '`$anonymous_namespace_csrc/ops/silu/silu_aten_kernels.cc`/IsFunctorchActive(c9857a73d68e59ba).'
---
# Module: [`csrc/ops/silu/silu_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/silu/silu_aten_kernels.cc)

## Functions
- <a id="AtenSiluBackward"></a>`AtenSiluBackward(const at::Tensor& grad_output, const at::Tensor& self)` — [`L232`](../../../../../../../raw/code/torch_tpu/csrc/ops/silu/silu_aten_kernels.cc#L232)
- <a id="AtenSiluBackwardAutograd"></a>`AtenSiluBackwardAutograd(const at::Tensor& grad_output, const at::Tensor& self)` — [`L213`](../../../../../../../raw/code/torch_tpu/csrc/ops/silu/silu_aten_kernels.cc#L213)
- <a id="AtenSiluBackwardGradInput"></a>`AtenSiluBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, at::Tensor& grad_input)` — [`L179`](../../../../../../../raw/code/torch_tpu/csrc/ops/silu/silu_aten_kernels.cc#L179)
- <a id="AtenSiluOut"></a>`AtenSiluOut(const at::Tensor& self, at::Tensor& out)` — [`L157`](../../../../../../../raw/code/torch_tpu/csrc/ops/silu/silu_aten_kernels.cc#L157)
- <a id="BuildSiluBackwardShlo"></a>`BuildSiluBackwardShlo(mlir::MlirOp grad_output_op, mlir::MlirOp input_op)` — [`L72`](../../../../../../../raw/code/torch_tpu/csrc/ops/silu/silu_aten_kernels.cc#L72)
- <a id="BuildSiluShlo"></a>`BuildSiluShlo(mlir::MlirOp input_op)` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/ops/silu/silu_aten_kernels.cc#L53)
- <a id="IsFakeOrFunctorchTensor"></a>`IsFakeOrFunctorchTensor(const at::Tensor& tensor)` — [`L117`](../../../../../../../raw/code/torch_tpu/csrc/ops/silu/silu_aten_kernels.cc#L117)
- <a id="IsFunctorchActive"></a>`IsFunctorchActive()` — [`L111`](../../../../../../../raw/code/torch_tpu/csrc/ops/silu/silu_aten_kernels.cc#L111)
- <a id="SiluBackwardComposite"></a>`SiluBackwardComposite(const at::Tensor& grad_output, const at::Tensor& self)` — [`L148`](../../../../../../../raw/code/torch_tpu/csrc/ops/silu/silu_aten_kernels.cc#L148) — Composite formulation used for `FakeTensor`s, functorch transforms and
- <a id="ValidateSiluBackwardInputs"></a>`ValidateSiluBackwardInputs(const at::Tensor& grad_output, const at::Tensor& self)` — [`L128`](../../../../../../../raw/code/torch_tpu/csrc/ops/silu/silu_aten_kernels.cc#L128) — Matches PyTorch's `silu_backward` meta function, which builds a
- <a id="ValidateSiluBackwardInputsOrThrow"></a>`ValidateSiluBackwardInputsOrThrow(const at::Tensor& grad_output, const at::Tensor& self)` — [`L137`](../../../../../../../raw/code/torch_tpu/csrc/ops/silu/silu_aten_kernels.cc#L137)

