---
title: 'Module: csrc/ops/linalg/qr/linalg_qr_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/linalg/qr/linalg_qr_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenLinalgQrOut: AtenLinalgQrOut(83b16a9c5a268baa).
  AtenGeqrfA: AtenGeqrfA(2f5532e1ad90f43e).
  AtenGeqrf: AtenGeqrf(9e2535fa0f011b65).
  GeqrfOut: '`$anonymous_namespace_csrc/ops/linalg/qr/linalg_qr_kernels.cc`/GeqrfOut(cd9c95fe2084366b).'
  QrOut: '`$anonymous_namespace_csrc/ops/linalg/qr/linalg_qr_kernels.cc`/QrOut(fe910156e0ff085e).'
  DispatchGeqrf: '`$anonymous_namespace_csrc/ops/linalg/qr/linalg_qr_kernels.cc`/DispatchGeqrf(bd716ee9402a0775).'
  ComputeQrDims: '`$anonymous_namespace_csrc/ops/linalg/qr/linalg_qr_kernels.cc`/ComputeQrDims(e06367b78b37825e).'
  ValidateGeqrfInputs: '`$anonymous_namespace_csrc/ops/linalg/qr/linalg_qr_kernels.cc`/ValidateGeqrfInputs(fd0458bfc68bb174).'
  Geqrf: '`$anonymous_namespace_csrc/ops/linalg/qr/linalg_qr_kernels.cc`/Geqrf(d4a7cb8b59810a50).'
  GetOutDtype: '`$anonymous_namespace_csrc/ops/linalg/qr/linalg_qr_kernels.cc`/GetOutDtype(afbb217a7cdbf13a).'
  MaybeCastToFloat: '`$anonymous_namespace_csrc/ops/linalg/qr/linalg_qr_kernels.cc`/MaybeCastToFloat(305148ce2b3e1423).'
  kCastDtypeForIntegerInput: '`$anonymous_namespace_csrc/ops/linalg/qr/linalg_qr_kernels.cc`/kCastDtypeForIntegerInput.'
  QrDims.r_dims: '`$anonymous_namespace_csrc/ops/linalg/qr/linalg_qr_kernels.cc`/QrDims#r_dims.'
  QrDims: '`$anonymous_namespace_csrc/ops/linalg/qr/linalg_qr_kernels.cc`/QrDims#'
  QrDims.q_dims: '`$anonymous_namespace_csrc/ops/linalg/qr/linalg_qr_kernels.cc`/QrDims#q_dims.'
---
# Module: [`csrc/ops/linalg/qr/linalg_qr_kernels.cc`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/linalg_qr_kernels.cc)

## Classes
### <a id="QrDims"></a>`QrDims`
- def: [`csrc/ops/linalg/qr/linalg_qr_kernels.cc:144`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/linalg_qr_kernels.cc#L144)
- signature: `struct QrDims`
- members:
  - <a id="QrDims.q_dims"></a>`q_dims` — [`L145`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/linalg_qr_kernels.cc#L145)
  - <a id="QrDims.r_dims"></a>`r_dims` — [`L146`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/linalg_qr_kernels.cc#L146)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../../common/dimension_types.h.md#Dimensions)
- used by: [`QrOut`](linalg_qr_kernels.cc.md#QrOut), [`ComputeQrDims`](linalg_qr_kernels.cc.md#ComputeQrDims)

## Functions
- <a id="AtenGeqrf"></a>`AtenGeqrf(const at::Tensor& self)` — [`L211`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/linalg_qr_kernels.cc#L211)
- <a id="AtenGeqrfA"></a>`AtenGeqrfA(const at::Tensor& self, at::Tensor& a, at::Tensor& tau)` — [`L219`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/linalg_qr_kernels.cc#L219)
- <a id="AtenLinalgQrOut"></a>`AtenLinalgQrOut(const at::Tensor& self, c10::string_view mode, at::Tensor& q, at::Tensor& r)` — [`L228`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/linalg_qr_kernels.cc#L228)
- <a id="ComputeQrDims"></a>`ComputeQrDims(const at::Tensor& self, c10::string_view mode)` — [`L149`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/linalg_qr_kernels.cc#L149)
- <a id="DispatchGeqrf"></a>`DispatchGeqrf(const at::Tensor& self, std::array<mlir::ElementType, 2> out_dtypes, OpParamCacheKeys param_keys, DispatchFn&& dispatch_fn)` — [`L77`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/linalg_qr_kernels.cc#L77)
- <a id="Geqrf"></a>`Geqrf(const at::Tensor& self, OpParamCacheKeys param_keys)` — [`L109`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/linalg_qr_kernels.cc#L109)
- `Geqrf(const at::Tensor& self, OpParamCacheKeys param_keys)` — [`L109`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/linalg_qr_kernels.cc#L109)
- <a id="GeqrfOut"></a>`GeqrfOut(const at::Tensor& self, OpParamCacheKeys param_keys, at::Tensor& a, at::Tensor& tau)` — [`L120`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/linalg_qr_kernels.cc#L120)
- <a id="GetOutDtype"></a>`GetOutDtype(const at::Tensor& self)` — [`L54`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/linalg_qr_kernels.cc#L54)
- <a id="MaybeCastToFloat"></a>`MaybeCastToFloat(mlir::MlirOp self_op, bool input_is_integer)` — [`L64`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/linalg_qr_kernels.cc#L64)
- <a id="QrOut"></a>`QrOut(const at::Tensor& self, c10::string_view mode, OpParamCacheKeys param_keys, at::Tensor& q, at::Tensor& r)` — [`L184`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/linalg_qr_kernels.cc#L184)
- <a id="ValidateGeqrfInputs"></a>`ValidateGeqrfInputs(const at::Tensor& self)` — [`L70`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/linalg_qr_kernels.cc#L70)

## Module values
- <a id="kCastDtypeForIntegerInput"></a>`kCastDtypeForIntegerInput` — [`L52`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/linalg_qr_kernels.cc#L52)

