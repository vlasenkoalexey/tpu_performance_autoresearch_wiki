---
title: 'Module: csrc/ops/native_norm/native_norm_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/native_norm/native_norm_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenNativeNormScalarOptDimDtype: AtenNativeNormScalarOptDimDtype(1a60d904b8d156f6).
  AtenNativeNormScalar: AtenNativeNormScalar(a1c6e5169a4320a1).
  PNorm: '`$anonymous_namespace_csrc/ops/native_norm/native_norm_aten_kernels.cc`/PNorm(6825106f3f293921).'
---
# Module: [`csrc/ops/native_norm/native_norm_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_norm/native_norm_aten_kernels.cc)

## Functions
- <a id="AtenNativeNormScalar"></a>`AtenNativeNormScalar(const at::Tensor& self, const at::Scalar& p)` — [`L99`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_norm/native_norm_aten_kernels.cc#L99) — ATen kernel handler for aten::linalg_vector_norm (or native_norm) when only
- <a id="AtenNativeNormScalarOptDimDtype"></a>`AtenNativeNormScalarOptDimDtype(const at::Tensor& self, const std::optional<at::Scalar>& p, at::IntArrayRef dim, bool keepdim, std::optional<at::ScalarType> dtype)` — [`L123`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_norm/native_norm_aten_kernels.cc#L123) — ATen kernel handler for aten::linalg_vector_norm with optional scalar order
- <a id="PNorm"></a>`PNorm(const at::Tensor& self, MaybePromotedScalar& promoted_ord, double ord, at::OptionalIntArrayRef dim, ReductionMode reduction_mode, std::optional<at::ScalarType> dtype, OpParamCacheKeys op_cache_keys)` — [`L52`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_norm/native_norm_aten_kernels.cc#L52) — Helper function that builds and dispatches the MLIR/SHLO operation to compute

