---
title: 'Module: csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenReflectionPad2dBackward: AtenReflectionPad2dBackward(7a3ba4552e2a8785).
  AtenReflectionPad2dOut: AtenReflectionPad2dOut(b80b45ac1719e16d).
  AtenReflectionPad2dBackwardGradInput: AtenReflectionPad2dBackwardGradInput(67ea18198051e64b).
  AtenReflectionPad3dOut: AtenReflectionPad3dOut(b80b45ac1719e16d).
  AtenReflectionPad1dOut: AtenReflectionPad1dOut(b80b45ac1719e16d).
  AtenReflectionPad3dBackwardGradInput: AtenReflectionPad3dBackwardGradInput(67ea18198051e64b).
  AtenReflectionPad1dBackwardGradInput: AtenReflectionPad1dBackwardGradInput(67ea18198051e64b).
  AtenReflectionPad2d: AtenReflectionPad2d(c65c0bc6367ce7f5).
  ReflectionPadHelper: '`$anonymous_namespace_csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc`/ReflectionPadHelper(97c374cfe47a43b6).'
  BuildReflectionPadBackwardShlo: '`$anonymous_namespace_csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc`/BuildReflectionPadBackwardShlo(4637dcfe7f09c56b).'
  BuildReflectionPadShlo: '`$anonymous_namespace_csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc`/BuildReflectionPadShlo(615e6e27e2b53b6f).'
  BuildReflectionPadBackwardSidePositivePaddingShlo: '`$anonymous_namespace_csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc`/BuildReflectionPadBackwardSidePositivePaddingShlo(e3f29004b5f149b9).'
  BuildReflectionPadBackwardSideNegativePaddingShlo: '`$anonymous_namespace_csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc`/BuildReflectionPadBackwardSideNegativePaddingShlo(e3f29004b5f149b9).'
  PaddingDirection: '`$anonymous_namespace_csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc`/PaddingDirection#'
  PaddingDirection.kLeft: '`$anonymous_namespace_csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc`/PaddingDirection#kLeft.'
  PaddingDirection.kRight: '`$anonymous_namespace_csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc`/PaddingDirection#kRight.'
---
# Module: [`csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc)

## Classes
### <a id="PaddingDirection"></a>`PaddingDirection`
- def: [`csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc:109`](../../../../../../../raw/code/torch_tpu/csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc#L109)
- signature: `enum class PaddingDirection`
- members:
  - <a id="PaddingDirection.kLeft"></a>`kLeft` — [`L110`](../../../../../../../raw/code/torch_tpu/csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc#L110)
  - <a id="PaddingDirection.kRight"></a>`kRight` — [`L111`](../../../../../../../raw/code/torch_tpu/csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc#L111)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildReflectionPadBackwardShlo`](reflection_pad_aten_kernels.cc.md#BuildReflectionPadBackwardShlo), [`BuildReflectionPadBackwardSideNegativePaddingShlo`](reflection_pad_aten_kernels.cc.md#BuildReflectionPadBackwardSideNegativePaddingShlo), [`BuildReflectionPadBackwardSidePositivePaddingShlo`](reflection_pad_aten_kernels.cc.md#BuildReflectionPadBackwardSidePositivePaddingShlo)

## Functions
- <a id="AtenReflectionPad1dBackwardGradInput"></a>`AtenReflectionPad1dBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef padding, at::Tensor& grad_input)` — [`L370`](../../../../../../../raw/code/torch_tpu/csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc#L370)
- <a id="AtenReflectionPad1dOut"></a>`AtenReflectionPad1dOut(const at::Tensor& self, at::IntArrayRef padding, at::Tensor& out)` — [`L321`](../../../../../../../raw/code/torch_tpu/csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc#L321)
- <a id="AtenReflectionPad2d"></a>`AtenReflectionPad2d(const at::Tensor& self, at::IntArrayRef padding)` — [`L332`](../../../../../../../raw/code/torch_tpu/csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc#L332)
- <a id="AtenReflectionPad2dBackward"></a>`AtenReflectionPad2dBackward(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef padding)` — [`L413`](../../../../../../../raw/code/torch_tpu/csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc#L413)
- <a id="AtenReflectionPad2dBackwardGradInput"></a>`AtenReflectionPad2dBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef padding, at::Tensor& grad_input)` — [`L385`](../../../../../../../raw/code/torch_tpu/csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc#L385)
- <a id="AtenReflectionPad2dOut"></a>`AtenReflectionPad2dOut(const at::Tensor& self, at::IntArrayRef padding, at::Tensor& out)` — [`L349`](../../../../../../../raw/code/torch_tpu/csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc#L349)
- <a id="AtenReflectionPad3dBackwardGradInput"></a>`AtenReflectionPad3dBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef padding, at::Tensor& grad_input)` — [`L399`](../../../../../../../raw/code/torch_tpu/csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc#L399)
- <a id="AtenReflectionPad3dOut"></a>`AtenReflectionPad3dOut(const at::Tensor& self, at::IntArrayRef padding, at::Tensor& out)` — [`L360`](../../../../../../../raw/code/torch_tpu/csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc#L360)
- <a id="BuildReflectionPadBackwardShlo"></a>`BuildReflectionPadBackwardShlo(mlir::MlirOp input, Dimensions padding, Dimensions output_shape, int num_pad_dimensions)` — [`L231`](../../../../../../../raw/code/torch_tpu/csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc#L231)
- <a id="BuildReflectionPadBackwardSideNegativePaddingShlo"></a>`BuildReflectionPadBackwardSideNegativePaddingShlo(mlir::MlirOp op, PaddingDirection direction, int64_t padding_size, int64_t dimension)` — [`L201`](../../../../../../../raw/code/torch_tpu/csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc#L201) — Generate code to handle accumulation of the padding slice, or propagation of
- <a id="BuildReflectionPadBackwardSidePositivePaddingShlo"></a>`BuildReflectionPadBackwardSidePositivePaddingShlo(mlir::MlirOp op, PaddingDirection direction, int64_t padding_size, int64_t dimension)` — [`L116`](../../../../../../../raw/code/torch_tpu/csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc#L116) — Generate code to handle accumulation of the padding slice, or propagation of
- <a id="BuildReflectionPadShlo"></a>`BuildReflectionPadShlo(mlir::MlirOp input, Dimensions padding, Dimensions output_shape, size_t num_pad_dimensions)` — [`L52`](../../../../../../../raw/code/torch_tpu/csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc#L52)
- <a id="ReflectionPadHelper"></a>`ReflectionPadHelper(absl::AnyInvocable<absl::StatusOr<mlir::MlirOp>(mlir::MlirOp input, Dimensions padding, Dimensions output_shape, int num_pad_dimensions) const> shlo_builder_function, OpParamCacheKeys param_keys, const at::Tensor& self, at::IntArrayRef padding, at::Tensor& out, int num_pad_dimensions)` — [`L275`](../../../../../../../raw/code/torch_tpu/csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc#L275)

