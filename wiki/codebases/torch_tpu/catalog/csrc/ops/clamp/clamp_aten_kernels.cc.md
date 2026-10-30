---
title: 'Module: csrc/ops/clamp/clamp_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/clamp/clamp_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenClampMinTensorOut: AtenClampMinTensorOut(dcc870e438d8791).
  AtenClampMaxTensorOut: AtenClampMaxTensorOut(dcc870e438d8791).
  AtenClampMaxOut: AtenClampMaxOut(95f92c0e0348af54).
  AtenClampMinOut: AtenClampMinOut(95f92c0e0348af54).
  AtenClampOut: AtenClampOut(8a678cd2ae06f43c).
  AtenClampTensorOut: AtenClampTensorOut(6af25556b203d1f3).
  AtenClampTensorHelper: '`$anonymous_namespace_csrc/ops/clamp/clamp_aten_kernels.cc`/AtenClampTensorHelper(cdf24adde07c2410).'
  ValidateNotBool: '`$anonymous_namespace_csrc/ops/clamp/clamp_aten_kernels.cc`/ValidateNotBool(d8359b99282c084c).'
  ClampScalarHelper: '`$anonymous_namespace_csrc/ops/clamp/clamp_aten_kernels.cc`/ClampScalarHelper(ce0c6c2b70e7672).'
  ComputeOutputShape: '`$anonymous_namespace_csrc/ops/clamp/clamp_aten_kernels.cc`/ComputeOutputShape(68b82e63cd3bbbab).'
  GetComputationType: '`$anonymous_namespace_csrc/ops/clamp/clamp_aten_kernels.cc`/GetComputationType(fc434ae5286da495).'
---
# Module: [`csrc/ops/clamp/clamp_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/clamp/clamp_aten_kernels.cc)

## Functions
- <a id="AtenClampMaxOut"></a>`AtenClampMaxOut(const at::Tensor& self, const at::Scalar& max, at::Tensor& out)` — [`L242`](../../../../../../../raw/code/torch_tpu/csrc/ops/clamp/clamp_aten_kernels.cc#L242)
- <a id="AtenClampMaxTensorOut"></a>`AtenClampMaxTensorOut(const at::Tensor& self, const at::Tensor& max, at::Tensor& out)` — [`L282`](../../../../../../../raw/code/torch_tpu/csrc/ops/clamp/clamp_aten_kernels.cc#L282)
- <a id="AtenClampMinOut"></a>`AtenClampMinOut(const at::Tensor& self, const at::Scalar& min, at::Tensor& out)` — [`L228`](../../../../../../../raw/code/torch_tpu/csrc/ops/clamp/clamp_aten_kernels.cc#L228)
- <a id="AtenClampMinTensorOut"></a>`AtenClampMinTensorOut(const at::Tensor& self, const at::Tensor& min, at::Tensor& out)` — [`L270`](../../../../../../../raw/code/torch_tpu/csrc/ops/clamp/clamp_aten_kernels.cc#L270)
- <a id="AtenClampOut"></a>`AtenClampOut(const at::Tensor& self, const c10::optional<at::Scalar>& min, const c10::optional<at::Scalar>& max, at::Tensor& out)` — [`L209`](../../../../../../../raw/code/torch_tpu/csrc/ops/clamp/clamp_aten_kernels.cc#L209)
- <a id="AtenClampTensorHelper"></a>`AtenClampTensorHelper(const at::Tensor& self, const c10::optional<at::Tensor>& min_, const c10::optional<at::Tensor>& max_, at::ScalarType computation_scalar_type, bool allow_out_dtype_cast, at::Tensor& out, OpParamCacheKeys param_keys)` — [`L99`](../../../../../../../raw/code/torch_tpu/csrc/ops/clamp/clamp_aten_kernels.cc#L99)
- <a id="AtenClampTensorOut"></a>`AtenClampTensorOut(const at::Tensor& self, const c10::optional<at::Tensor>& min, const c10::optional<at::Tensor>& max, at::Tensor& out)` — [`L256`](../../../../../../../raw/code/torch_tpu/csrc/ops/clamp/clamp_aten_kernels.cc#L256)
- <a id="ClampScalarHelper"></a>`ClampScalarHelper(const at::Tensor& self, std::optional<PromotedScalar> min, std::optional<PromotedScalar> max, at::ScalarType computation_scalar_type, bool allow_out_dtype_cast, at::Tensor& out, OpParamCacheKeys param_keys)` — [`L179`](../../../../../../../raw/code/torch_tpu/csrc/ops/clamp/clamp_aten_kernels.cc#L179) — Helper for clamping with promoted scalar bounds.
- <a id="ComputeOutputShape"></a>`ComputeOutputShape(const at::Tensor& self, const std::optional<at::Tensor>& min, const std::optional<at::Tensor>& max)` — [`L86`](../../../../../../../raw/code/torch_tpu/csrc/ops/clamp/clamp_aten_kernels.cc#L86)
- `GetComputationType(const at::Tensor& self, const c10::optional<at::Scalar>& min, const c10::optional<at::Scalar>& max)` — [`L51`](../../../../../../../raw/code/torch_tpu/csrc/ops/clamp/clamp_aten_kernels.cc#L51) — Returns the computation `at::ScalarType` for scalar bounds, following PyTorch
- <a id="GetComputationType"></a>`GetComputationType(const at::Tensor& self, const c10::optional<at::Tensor>& min, const c10::optional<at::Tensor>& max)` — [`L70`](../../../../../../../raw/code/torch_tpu/csrc/ops/clamp/clamp_aten_kernels.cc#L70) — Returns the computation `at::ScalarType` for tensor bounds.
- <a id="ValidateNotBool"></a>`ValidateNotBool(const at::Tensor& tensor, const std::string_view arg_name)` — [`L200`](../../../../../../../raw/code/torch_tpu/csrc/ops/clamp/clamp_aten_kernels.cc#L200)

