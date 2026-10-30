---
title: 'Module: csrc/ops/bmm/bmm_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/bmm/bmm_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenBmmDtypeOut: AtenBmmDtypeOut(791ea81898ca1dbe).
  AtenBmmOut: AtenBmmOut(dcc870e438d8791).
  AtenBmmDtype: AtenBmmDtype(f2aa9cd43ebdcffe).
  ValidateBmmInputs: '`$anonymous_namespace_csrc/ops/bmm/bmm_aten_kernels.cc`/ValidateBmmInputs(b2d6689cde60befb).'
  DispatchBmm: '`$anonymous_namespace_csrc/ops/bmm/bmm_aten_kernels.cc`/DispatchBmm(fd35c44487b8de49).'
  ValidateBmmOut: '`$anonymous_namespace_csrc/ops/bmm/bmm_aten_kernels.cc`/ValidateBmmOut(acb502079e74052e).'
  BmmOut: '`$anonymous_namespace_csrc/ops/bmm/bmm_aten_kernels.cc`/BmmOut(6180c64f3fef3b0d).'
  Bmm: '`$anonymous_namespace_csrc/ops/bmm/bmm_aten_kernels.cc`/Bmm(fe248e49fbbd4f32).'
---
# Module: [`csrc/ops/bmm/bmm_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/bmm/bmm_aten_kernels.cc)

## Functions
- <a id="AtenBmmDtype"></a>`AtenBmmDtype(const at::Tensor& self, const at::Tensor& mat2, at::ScalarType out_dtype)` — [`L147`](../../../../../../../raw/code/torch_tpu/csrc/ops/bmm/bmm_aten_kernels.cc#L147)
- <a id="AtenBmmDtypeOut"></a>`AtenBmmDtypeOut(const at::Tensor& self, const at::Tensor& mat2, at::ScalarType out_dtype, at::Tensor& out)` — [`L156`](../../../../../../../raw/code/torch_tpu/csrc/ops/bmm/bmm_aten_kernels.cc#L156)
- <a id="AtenBmmOut"></a>`AtenBmmOut(const at::Tensor& self, const at::Tensor& mat2, at::Tensor& out)` — [`L165`](../../../../../../../raw/code/torch_tpu/csrc/ops/bmm/bmm_aten_kernels.cc#L165)
- <a id="Bmm"></a>`Bmm(const at::Tensor& self, const at::Tensor& mat2, at::ScalarType out_dtype, OpParamCacheKeys param_keys)` — [`L120`](../../../../../../../raw/code/torch_tpu/csrc/ops/bmm/bmm_aten_kernels.cc#L120)
- <a id="BmmOut"></a>`BmmOut(const at::Tensor& self, const at::Tensor& mat2, at::ScalarType out_dtype, at::Tensor& out, OpParamCacheKeys param_keys)` — [`L132`](../../../../../../../raw/code/torch_tpu/csrc/ops/bmm/bmm_aten_kernels.cc#L132)
- <a id="DispatchBmm"></a>`DispatchBmm(const at::Tensor& self, const at::Tensor& mat2, at::ScalarType out_dtype, OpParamCacheKeys param_keys, DispatchFn&& dispatch_fn)` — [`L97`](../../../../../../../raw/code/torch_tpu/csrc/ops/bmm/bmm_aten_kernels.cc#L97)
- <a id="ValidateBmmInputs"></a>`ValidateBmmInputs(const at::Tensor& self, const at::Tensor& mat2)` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/bmm/bmm_aten_kernels.cc#L55)
- <a id="ValidateBmmOut"></a>`ValidateBmmOut(const at::Tensor& out, at::ScalarType out_dtype)` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/ops/bmm/bmm_aten_kernels.cc#L48)

