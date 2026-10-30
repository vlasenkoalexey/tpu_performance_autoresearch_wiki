---
title: 'Module: csrc/ops/masked_fill/masked_fill_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/masked_fill/masked_fill_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenMaskedFill_Scalar: AtenMaskedFill_Scalar(cce46649d371e38e).
  AtenMaskedFill_Tensor: AtenMaskedFill_Tensor(2db65acdbc4fe769).
  ResolveTensorValueAndDispatch: '`$anonymous_namespace_csrc/ops/masked_fill/masked_fill_aten_kernels.cc`/ResolveTensorValueAndDispatch(2f39fa3ef24bd956).'
  AtenMaskedFillScalar: AtenMaskedFillScalar(a0ca19c1acd361a3).
  AtenMaskedFillTensor: AtenMaskedFillTensor(7048bed50d562265).
  ValidateInferredOutputShapeMatchesSelf: '`$anonymous_namespace_csrc/ops/masked_fill/masked_fill_aten_kernels.cc`/ValidateInferredOutputShapeMatchesSelf(ee17b71def4d9c7f).'
  DispatchOutOfPlace: '`$anonymous_namespace_csrc/ops/masked_fill/masked_fill_aten_kernels.cc`/DispatchOutOfPlace(c9b9a898fa9ca706).'
  DispatchInPlace: '`$anonymous_namespace_csrc/ops/masked_fill/masked_fill_aten_kernels.cc`/DispatchInPlace(ebd2290dc28654a0).'
  ValidateValueCastableWithoutOverflow: '`$anonymous_namespace_csrc/ops/masked_fill/masked_fill_aten_kernels.cc`/ValidateValueCastableWithoutOverflow(b963352d59a79759).'
  ValidateMaskIsBool: '`$anonymous_namespace_csrc/ops/masked_fill/masked_fill_aten_kernels.cc`/ValidateMaskIsBool(fd0458bfc68bb174).'
  ResolveScalarValueAndDispatch: '`$anonymous_namespace_csrc/ops/masked_fill/masked_fill_aten_kernels.cc`/ResolveScalarValueAndDispatch(b5e602b4d024ecd9).'
  MakeMaskedFillBuilder: '`$anonymous_namespace_csrc/ops/masked_fill/masked_fill_aten_kernels.cc`/MakeMaskedFillBuilder(fff76b6d6a4e3346).'
---
# Module: [`csrc/ops/masked_fill/masked_fill_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_fill/masked_fill_aten_kernels.cc)

## Functions
- <a id="AtenMaskedFillScalar"></a>`AtenMaskedFillScalar(const at::Tensor& self, const at::Tensor& mask, const at::Scalar& value)` — [`L172`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_fill/masked_fill_aten_kernels.cc#L172) — masked_fill.Scalar
- <a id="AtenMaskedFillTensor"></a>`AtenMaskedFillTensor(const at::Tensor& self, const at::Tensor& mask, const at::Tensor& value)` — [`L187`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_fill/masked_fill_aten_kernels.cc#L187) — masked_fill.Tensor
- <a id="AtenMaskedFill_Scalar"></a>`AtenMaskedFill_Scalar(at::Tensor& self, const at::Tensor& mask, const at::Scalar& value)` — [`L200`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_fill/masked_fill_aten_kernels.cc#L200) — masked_fill_.Scalar
- <a id="AtenMaskedFill_Tensor"></a>`AtenMaskedFill_Tensor(at::Tensor& self, const at::Tensor& mask, const at::Tensor& value)` — [`L213`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_fill/masked_fill_aten_kernels.cc#L213) — masked_fill_.Tensor
- <a id="DispatchInPlace"></a>`DispatchInPlace(at::Tensor& self, const at::Tensor& mask, const at::Tensor& value)` — [`L111`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_fill/masked_fill_aten_kernels.cc#L111) — Dispatch logic for in-place masked fill op.
- <a id="DispatchOutOfPlace"></a>`DispatchOutOfPlace(const at::Tensor& self, const at::Tensor& mask, const at::Tensor& value)` — [`L93`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_fill/masked_fill_aten_kernels.cc#L93) — Dispatch logic for out-of-place masked fill op.
- <a id="MakeMaskedFillBuilder"></a>`MakeMaskedFillBuilder(const mlir::ElementType self_mlir_type)` — [`L84`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_fill/masked_fill_aten_kernels.cc#L84)
- <a id="ResolveScalarValueAndDispatch"></a>`ResolveScalarValueAndDispatch(const at::ScalarType self_dtype, PromotedScalar& value, DispatchFn&& dispatch_fn)` — [`L129`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_fill/masked_fill_aten_kernels.cc#L129) — Validates that scalar `value` can be cast to `self_dtype` without overflow,
- <a id="ResolveTensorValueAndDispatch"></a>`ResolveTensorValueAndDispatch(const at::ScalarType self_dtype, const at::Tensor& value, DispatchFn&& dispatch_fn)` — [`L146`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_fill/masked_fill_aten_kernels.cc#L146) — Validates a 0D tensor `value` (on either TPU or CPU) for scalar overflow
- <a id="ValidateInferredOutputShapeMatchesSelf"></a>`ValidateInferredOutputShapeMatchesSelf(const at::Tensor& self, const Dimensions& out_dims)` — [`L64`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_fill/masked_fill_aten_kernels.cc#L64) — Validates that the broadcasted output shape matches `self`'s shape.
- <a id="ValidateMaskIsBool"></a>`ValidateMaskIsBool(const at::Tensor& mask)` — [`L52`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_fill/masked_fill_aten_kernels.cc#L52) — Validates that `mask` has boolean data type.
- <a id="ValidateValueCastableWithoutOverflow"></a>`ValidateValueCastableWithoutOverflow(const at::Scalar& value, const at::ScalarType dtype)` — [`L74`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_fill/masked_fill_aten_kernels.cc#L74) — Validates that `value` can be safely cast to `dtype` without overflow.

