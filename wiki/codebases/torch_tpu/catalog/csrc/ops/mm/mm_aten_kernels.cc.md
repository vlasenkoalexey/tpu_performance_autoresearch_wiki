---
title: 'Module: csrc/ops/mm/mm_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/mm/mm_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenMmDtype: AtenMmDtype(f2aa9cd43ebdcffe).
  AtenMmOut: AtenMmOut(dcc870e438d8791).
  AtenMmDtypeOut: AtenMmDtypeOut(791ea81898ca1dbe).
  ValidateMmOutInputs: '`$anonymous_namespace_csrc/ops/mm/mm_aten_kernels.cc`/ValidateMmOutInputs(1abf288658e2261b).'
  Mm: '`$anonymous_namespace_csrc/ops/mm/mm_aten_kernels.cc`/Mm(f7a73f35c2f9b04f).'
---
# Module: [`csrc/ops/mm/mm_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/mm/mm_aten_kernels.cc)

## Functions
- <a id="AtenMmDtype"></a>`AtenMmDtype(const at::Tensor& lhs, const at::Tensor& rhs, at::ScalarType out_dtype)` — [`L131`](../../../../../../../raw/code/torch_tpu/csrc/ops/mm/mm_aten_kernels.cc#L131) — PyTorch "mm" is the more restricted form of "matmul".
- <a id="AtenMmDtypeOut"></a>`AtenMmDtypeOut(const at::Tensor& lhs, const at::Tensor& rhs, at::ScalarType out_dtype, at::Tensor& out)` — [`L142`](../../../../../../../raw/code/torch_tpu/csrc/ops/mm/mm_aten_kernels.cc#L142)
- <a id="AtenMmOut"></a>`AtenMmOut(const at::Tensor& lhs, const at::Tensor& rhs, at::Tensor& out)` — [`L150`](../../../../../../../raw/code/torch_tpu/csrc/ops/mm/mm_aten_kernels.cc#L150)
- <a id="Mm"></a>`Mm(const at::Tensor& lhs, const at::Tensor& rhs, at::Tensor& out, OpParamCacheKeys param_keys, std::optional<at::ScalarType> out_dtype = std::nullopt)` — [`L94`](../../../../../../../raw/code/torch_tpu/csrc/ops/mm/mm_aten_kernels.cc#L94)
- <a id="ValidateMmOutInputs"></a>`ValidateMmOutInputs(const at::Tensor& lhs, const at::Tensor& rhs, at::Tensor& out, std::optional<at::ScalarType> out_dtype)` — [`L50`](../../../../../../../raw/code/torch_tpu/csrc/ops/mm/mm_aten_kernels.cc#L50)

