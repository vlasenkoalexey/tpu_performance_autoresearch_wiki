---
title: 'Module: csrc/common/aten_utils.h'
type: catalog
provenance: extracted
module: csrc/common/aten_utils.h
status: fresh
symbol_base: 'cxx . . $ '
symbols:
  ValidateIsMatrix: torch_tpu/ValidateIsMatrix(d8359b99282c084c).
  ValidateOutDtype: absl/torch_tpu/ValidateOutDtype(fe57a878c6ee9afc).
  IsComplex: torch_tpu/IsComplex(fe1ba53999e710f3).
  IsFloatingPoint: torch_tpu/IsFloatingPoint(b580d0b7e29ca914).
  IsBool: torch_tpu/IsBool(fe1ba53999e710f3).
  AbslHashValue: absl/torch_tpu/AbslHashValue(c4607de3f172a947).
  IsIntegral: torch_tpu/IsIntegral(fe1ba53999e710f3).
  HashableScalar.scalar: torch_tpu/HashableScalar#scalar.
  HashableScalar.scalar_type: torch_tpu/HashableScalar#scalar_type.
  IsPrivateUse1Device: torch_tpu/IsPrivateUse1Device(b580d0b7e29ca914).
  GetScalarType: absl/torch_tpu/GetScalarType(7864480464b09eea).
  IsInteger: torch_tpu/IsInteger(b580d0b7e29ca914).
  SanitizeOptionalTensor: torch_tpu/SanitizeOptionalTensor(5d048ace904065f3).
  HashableScalar: torch_tpu/HashableScalar#
  IsFloatOrDouble: torch_tpu/IsFloatOrDouble(b580d0b7e29ca914).
  IsCpuDevice: torch_tpu/IsCpuDevice(b580d0b7e29ca914).
  IsHalf: torch_tpu/IsHalf(b580d0b7e29ca914).
  IsXlaSupportedComplex: absl/torch_tpu/IsXlaSupportedComplex(807fba15d56270a7).
  IsLong: absl/torch_tpu/IsLong(807fba15d56270a7).
---
# Module: [`csrc/common/aten_utils.h`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h)

## Classes
### <a id="HashableScalar"></a>`HashableScalar`
- def: [`csrc/common/aten_utils.h:189`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L189)
- doc: A wrapper struct to make an at::Scalar hashable by absl::Hash.
- signature: `struct HashableScalar`
- members:
  - <a id="HashableScalar.scalar"></a>`scalar` — [`L192`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L192) — The actual value of the scalar on host. Note that scalar.type() always
  - <a id="HashableScalar.scalar_type"></a>`scalar_type` — [`L194`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L194) — The desired type of the scalar.
- uses (calls/refs, reference-scoped): [`operator==`](aten_utils.cc.md#operator), [`CanCastScalarWithoutOverflow`](aten_utils.cc.md#CanCastScalarWithoutOverflow)
- used by: [`operator==`](aten_utils.cc.md#operator), [`MakeBuffer`](../eager/op_dispatcher.cc.md#MakeBuffer), [`AbslHashValue`](aten_utils.h.md#AbslHashValue)

## Functions
- <a id="AbslHashValue"></a>`AbslHashValue(H h, const HashableScalar& hashable_scalar)` — [`L215`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L215) — Make c10::Scalar hashable for absl containers. This encodes both the target
- `AbslHashValue(H h, const HashableScalar& hashable_scalar)` — [`L215`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L215) — Make c10::Scalar hashable for absl containers. This encodes both the target
- `GetScalarType(const at::Tensor& tensor)` — [`L47`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L47) — Returns the scalar type of the given tensor.
- `GetScalarType(const at::Tensor& tensor)` — [`L47`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L47) — Returns the scalar type of the given tensor.
- `GetScalarType(at::ScalarType scalar_type)` — [`L56`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L56)
- <a id="GetScalarType"></a>`GetScalarType(at::ScalarType scalar_type)` — [`L56`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L56)
- `GetScalarType(const at::Scalar& scalar)` — [`L52`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L52) — Returns the scalar type of the given scalar.
- <a id="IsBool"></a>`IsBool(const T& thing)` — [`L109`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L109) — Returns whether `thing` holds boolean data.
- `IsBool(const T& thing)` — [`L109`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L109) — Returns whether `thing` holds boolean data.
- <a id="IsComplex"></a>`IsComplex(const T& thing)` — [`L121`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L121) — Returns whether `thing` holds complex data.
- `IsComplex(const T& thing)` — [`L121`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L121) — Returns whether `thing` holds complex data.
- `IsCpuDevice(const at::Tensor& tensor)` — [`L176`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L176) — Returns whether `tensor` device is CPU.
- <a id="IsCpuDevice"></a>`IsCpuDevice(const at::Tensor& tensor)` — [`L176`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L176) — Returns whether `tensor` device is CPU.
- `IsFloatOrDouble(const at::Tensor& tensor)` — [`L131`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L131) — Returns whether `tensor` holds `float32` (float) or `float64` (double) data.
- <a id="IsFloatOrDouble"></a>`IsFloatOrDouble(const at::Tensor& tensor)` — [`L131`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L131) — Returns whether `tensor` holds `float32` (float) or `float64` (double) data.
- <a id="IsFloatingPoint"></a>`IsFloatingPoint(const at::Tensor& tensor)` — [`L126`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L126) — Returns whether `tensor` holds floating-point data.
- `IsFloatingPoint(const at::Tensor& tensor)` — [`L126`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L126) — Returns whether `tensor` holds floating-point data.
- `IsHalf(const at::Tensor& tensor)` — [`L137`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L137) — Returns whether `tensor` holds `float16` (half) data.
- <a id="IsHalf"></a>`IsHalf(const at::Tensor& tensor)` — [`L137`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L137) — Returns whether `tensor` holds `float16` (half) data.
- <a id="IsInteger"></a>`IsInteger(const at::Tensor& tensor)` — [`L142`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L142) — Returns whether `tensor` holds integer data.
- `IsInteger(const at::Tensor& tensor)` — [`L142`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L142) — Returns whether `tensor` holds integer data.
- `IsIntegral(const T& thing)` — [`L154`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L154) — Returns whether `thing` holds integral data.
- <a id="IsIntegral"></a>`IsIntegral(const T& thing)` — [`L154`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L154) — Returns whether `thing` holds integral data.
- <a id="IsLong"></a>`IsLong(const at::Tensor& tensor)` — [`L159`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L159) — Returns whether `tensor` holds Long typed data.
- `IsLong(const at::Tensor& tensor)` — [`L159`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L159) — Returns whether `tensor` holds Long typed data.
- `IsPrivateUse1Device(const at::Tensor& tensor)` — [`L171`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L171) — Returns whether `tensor` device is PrivateUse1.
- <a id="IsPrivateUse1Device"></a>`IsPrivateUse1Device(const at::Tensor& tensor)` — [`L171`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L171) — Returns whether `tensor` device is PrivateUse1.
- <a id="IsXlaSupportedComplex"></a>`IsXlaSupportedComplex(const at::Tensor& tensor)` — [`L165`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L165) — Returns whether `tensor` holds complex data that is supported by OpenXLA:
- `IsXlaSupportedComplex(const at::Tensor& tensor)` — [`L165`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L165) — Returns whether `tensor` holds complex data that is supported by OpenXLA:
- <a id="SanitizeOptionalTensor"></a>`SanitizeOptionalTensor(std::optional<at::Tensor> t)` — [`L183`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L183) — Unfortunately, the PyTorch dispatcher can call us by passing an optional
- <a id="ValidateIsMatrix"></a>`ValidateIsMatrix(const at::Tensor& tensor, std::string_view arg_name)` — [`L68`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L68)
- `ValidateIsMatrix(const at::Tensor& tensor, std::string_view arg_name)` — [`L68`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L68)
- `ValidateOutDtype(const at::Tensor& out, const at::ScalarType result_dtype, const bool allow_out_dtype_cast = true)` — [`L84`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L84) — Verifies that result_dtype matches or can be safely cast to the out tensor's
- <a id="ValidateOutDtype"></a>`ValidateOutDtype(const at::Tensor& out, const at::ScalarType result_dtype, const bool allow_out_dtype_cast = true)` — [`L84`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L84) — Verifies that result_dtype matches or can be safely cast to the out tensor's

## Module values
- `SanitizeOptionalTensor` — [`L183`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.h#L183) — Unfortunately, the PyTorch dispatcher can call us by passing an optional

