---
title: 'Module: csrc/ops/norm/norm_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/norm/norm_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenNormOut: AtenNormOut(bddac1f27bad83f5).
  AtenNormDtypeOut: AtenNormDtypeOut(cbcbb9478500e319).
  PNormOut: '`$anonymous_namespace_csrc/ops/norm/norm_aten_kernels.cc`/PNormOut(8f24c39378304e39).'
  ValidateNormOutDtype: '`$anonymous_namespace_csrc/ops/norm/norm_aten_kernels.cc`/ValidateNormOutDtype(985237f6cbde967f).'
  BuildZeroNormShlo: '`$anonymous_namespace_csrc/ops/norm/norm_aten_kernels.cc`/BuildZeroNormShlo(ecf6793c361629f0).'
---
# Module: [`csrc/ops/norm/norm_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/norm/norm_aten_kernels.cc)

## Functions
- <a id="AtenNormDtypeOut"></a>`AtenNormDtypeOut(const at::Tensor& self, const std::optional<at::Scalar>& p, at::IntArrayRef dim, bool keepdim, at::ScalarType dtype, at::Tensor& out)` — [`L166`](../../../../../../../raw/code/torch_tpu/csrc/ops/norm/norm_aten_kernels.cc#L166) — aten::norm.dtype_out
- <a id="AtenNormOut"></a>`AtenNormOut(const at::Tensor& self, const std::optional<at::Scalar>& p, at::IntArrayRef dim, bool keepdim, at::Tensor& out)` — [`L151`](../../../../../../../raw/code/torch_tpu/csrc/ops/norm/norm_aten_kernels.cc#L151) — aten::norm.out
- <a id="BuildZeroNormShlo"></a>`BuildZeroNormShlo(mlir::MlirOp input_op, absl::Span<const int64_t> reduce_dims, ReductionMode reduction_mode, mlir::ElementType out_type)` — [`L67`](../../../../../../../raw/code/torch_tpu/csrc/ops/norm/norm_aten_kernels.cc#L67)
- <a id="PNormOut"></a>`PNormOut(const at::Tensor& self, PromotedScalar& promoted_ord, double ord, at::IntArrayRef dim, bool keepdim, std::optional<at::ScalarType> dtype, at::Tensor& out, OpParamCacheKeys op_cache_keys)` — [`L99`](../../../../../../../raw/code/torch_tpu/csrc/ops/norm/norm_aten_kernels.cc#L99)
- <a id="ValidateNormOutDtype"></a>`ValidateNormOutDtype(const at::Tensor& self, const at::Tensor& out, std::optional<at::ScalarType> dtype)` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/norm/norm_aten_kernels.cc#L55)

