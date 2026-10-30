---
title: 'Module: csrc/ops/all_any/all_any_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/all_any/all_any_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenAllAllOut: AtenAllAllOut(4655895dd4ef7692).
  AtenAnyAllOut: AtenAnyAllOut(4655895dd4ef7692).
  AtenAnyOut: AtenAnyOut(d2726ba75db4162d).
  AtenAllOut: AtenAllOut(d2726ba75db4162d).
  ValidateAllAnyOut: '`$anonymous_namespace_csrc/ops/all_any/all_any_aten_kernels.cc`/ValidateAllAnyOut(fd0458bfc68bb174).'
  GetAllAnyReductionParams: '`$anonymous_namespace_csrc/ops/all_any/all_any_aten_kernels.cc`/GetAllAnyReductionParams(98884800e9cb0593).'
  GetAllBuilder: '`$anonymous_namespace_csrc/ops/all_any/all_any_aten_kernels.cc`/GetAllBuilder(f09973f8eab72125).'
  GetAnyBuilder: '`$anonymous_namespace_csrc/ops/all_any/all_any_aten_kernels.cc`/GetAnyBuilder(f09973f8eab72125).'
  GetAllAnyOutDtype: '`$anonymous_namespace_csrc/ops/all_any/all_any_aten_kernels.cc`/GetAllAnyOutDtype(88ffc26431632baf).'
  AllAnyReductionParams.reduced_shape: '`$anonymous_namespace_csrc/ops/all_any/all_any_aten_kernels.cc`/AllAnyReductionParams#reduced_shape.'
  AllAnyReductionParams.reduction_mode: '`$anonymous_namespace_csrc/ops/all_any/all_any_aten_kernels.cc`/AllAnyReductionParams#reduction_mode.'
  AllAnyReductionParams.dims_to_reduce: '`$anonymous_namespace_csrc/ops/all_any/all_any_aten_kernels.cc`/AllAnyReductionParams#dims_to_reduce.'
  AllAnyReductionParams: '`$anonymous_namespace_csrc/ops/all_any/all_any_aten_kernels.cc`/AllAnyReductionParams#'
---
# Module: [`csrc/ops/all_any/all_any_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/all_any/all_any_aten_kernels.cc)

## Classes
### <a id="AllAnyReductionParams"></a>`AllAnyReductionParams`
- def: [`csrc/ops/all_any/all_any_aten_kernels.cc:64`](../../../../../../../raw/code/torch_tpu/csrc/ops/all_any/all_any_aten_kernels.cc#L64)
- signature: `struct AllAnyReductionParams`
- members:
  - <a id="AllAnyReductionParams.dims_to_reduce"></a>`dims_to_reduce` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/ops/all_any/all_any_aten_kernels.cc#L65)
  - <a id="AllAnyReductionParams.reduced_shape"></a>`reduced_shape` — [`L67`](../../../../../../../raw/code/torch_tpu/csrc/ops/all_any/all_any_aten_kernels.cc#L67)
  - <a id="AllAnyReductionParams.reduction_mode"></a>`reduction_mode` — [`L66`](../../../../../../../raw/code/torch_tpu/csrc/ops/all_any/all_any_aten_kernels.cc#L66)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions), [`ReductionMode`](../reductions/reductions.h.md#ReductionMode)
- used by: [`AtenAllAllOut`](all_any_aten_kernels.cc.md#AtenAllAllOut), [`AtenAnyAllOut`](all_any_aten_kernels.cc.md#AtenAnyAllOut), [`AtenAllOut`](all_any_aten_kernels.cc.md#AtenAllOut), [`AtenAnyOut`](all_any_aten_kernels.cc.md#AtenAnyOut), [`GetAllAnyReductionParams`](all_any_aten_kernels.cc.md#GetAllAnyReductionParams)

## Functions
- <a id="AtenAllAllOut"></a>`AtenAllAllOut(const at::Tensor& self, at::Tensor& out)` — [`L133`](../../../../../../../raw/code/torch_tpu/csrc/ops/all_any/all_any_aten_kernels.cc#L133) — This is all.all_out, NOT all.out.
- <a id="AtenAllOut"></a>`AtenAllOut(const at::Tensor& self, int64_t dim, bool keep_dim, at::Tensor& out)` — [`L115`](../../../../../../../raw/code/torch_tpu/csrc/ops/all_any/all_any_aten_kernels.cc#L115)
- <a id="AtenAnyAllOut"></a>`AtenAnyAllOut(const at::Tensor& self, at::Tensor& out)` — [`L167`](../../../../../../../raw/code/torch_tpu/csrc/ops/all_any/all_any_aten_kernels.cc#L167) — Kernels for the 'any' operation
- <a id="AtenAnyOut"></a>`AtenAnyOut(const at::Tensor& self, int64_t dim, bool keep_dim, at::Tensor& out)` — [`L150`](../../../../../../../raw/code/torch_tpu/csrc/ops/all_any/all_any_aten_kernels.cc#L150)
- <a id="GetAllAnyOutDtype"></a>`GetAllAnyOutDtype(const at::Tensor& out)` — [`L108`](../../../../../../../raw/code/torch_tpu/csrc/ops/all_any/all_any_aten_kernels.cc#L108) — Returns the output element type for `all` and `any` out-variants.
- <a id="GetAllAnyReductionParams"></a>`GetAllAnyReductionParams(const at::Tensor& self, c10::OptionalArrayRef<int64_t> dims, bool keep_dims)` — [`L70`](../../../../../../../raw/code/torch_tpu/csrc/ops/all_any/all_any_aten_kernels.cc#L70)
- <a id="GetAllBuilder"></a>`GetAllBuilder(Dimensions reduce_dims, ReductionMode reduction_mode)` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/ops/all_any/all_any_aten_kernels.cc#L48)
- <a id="GetAnyBuilder"></a>`GetAnyBuilder(Dimensions reduce_dims, ReductionMode reduction_mode)` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/all_any/all_any_aten_kernels.cc#L56)
- <a id="ValidateAllAnyOut"></a>`ValidateAllAnyOut(const at::Tensor& out)` — [`L97`](../../../../../../../raw/code/torch_tpu/csrc/ops/all_any/all_any_aten_kernels.cc#L97) — Verifies that the out tensor has a valid dtype for `all` and `any`.

