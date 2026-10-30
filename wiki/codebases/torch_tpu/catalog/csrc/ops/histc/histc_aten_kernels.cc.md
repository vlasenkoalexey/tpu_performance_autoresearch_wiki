---
title: 'Module: csrc/ops/histc/histc_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/histc/histc_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  HistcHelperOut: '`$anonymous_namespace_csrc/ops/histc/histc_aten_kernels.cc`/HistcHelperOut(cb422abf03d6d30).'
  AtenHistcOut: AtenHistcOut(846d5006fbf741b).
  AtenHistc: AtenHistc(580cd91ff842185f).
  ValidateBounds: '`$anonymous_namespace_csrc/ops/histc/histc_aten_kernels.cc`/ValidateBounds(76c7aba5bfb8c383).'
  eq: '`$anonymous_namespace_csrc/ops/histc/histc_aten_kernels.cc`/eq(7c7601f869c6dfab).'
  lt: '`$anonymous_namespace_csrc/ops/histc/histc_aten_kernels.cc`/lt(7c7601f869c6dfab).'
---
# Module: [`csrc/ops/histc/histc_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc_aten_kernels.cc)

## Functions
- <a id="AtenHistc"></a>`AtenHistc(const at::Tensor& self, const int64_t bins, const at::Scalar& min, const at::Scalar& max)` — [`L237`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc_aten_kernels.cc#L237)
- <a id="AtenHistcOut"></a>`AtenHistcOut(const at::Tensor& self, const int64_t bins, const at::Scalar& min, const at::Scalar& max, at::Tensor& out)` — [`L252`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc_aten_kernels.cc#L252)
- <a id="HistcHelperOut"></a>`HistcHelperOut(const at::Tensor& self, const int64_t bins, const at::Scalar& min, const at::Scalar& max, PromotedScalar& promoted_min, PromotedScalar& promoted_max, at::Tensor& out, OpParamCacheKeys param_keys)` — [`L138`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc_aten_kernels.cc#L138)
- <a id="ValidateBounds"></a>`ValidateBounds(const at::Scalar& min, const at::Scalar& max, const std::optional<at::Scalar>& min_prev = std::nullopt, const std::optional<at::Scalar>& max_prev = std::nullopt)` — [`L98`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc_aten_kernels.cc#L98) — Validates whether the given min and max values are valid. If min_prev
- <a id="eq"></a>`eq(const at::Scalar& a, const at::Scalar& b)` — [`L73`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc_aten_kernels.cc#L73)
- <a id="lt"></a>`lt(const at::Scalar& a, const at::Scalar& b)` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc_aten_kernels.cc#L53)

