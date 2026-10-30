---
title: 'Module: csrc/ops/addmm/addmm_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/addmm/addmm_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenAddmmDtypeOut: AtenAddmmDtypeOut(d26884d764022210).
  AtenAddmmActivationOut: AtenAddmmActivationOut(28109afc6aac1159).
  AtenAddmmOut: AtenAddmmOut(a07f23bfc1f8200e).
  AtenAddmmDtype: AtenAddmmDtype(6b83f4dd57f2f3b3).
  ValidateAddmmInputsAndGetOutputDtype: '`$anonymous_namespace_csrc/ops/addmm/addmm_aten_kernels.cc`/ValidateAddmmInputsAndGetOutputDtype(366fcc2ba53f78d3).'
  DispatchAddmm: '`$anonymous_namespace_csrc/ops/addmm/addmm_aten_kernels.cc`/DispatchAddmm(6cd26904d3fb8d5a).'
  ValidateInputBroadcast: '`$anonymous_namespace_csrc/ops/addmm/addmm_aten_kernels.cc`/ValidateInputBroadcast(ee17b71def4d9c7f).'
  BuildAddmmShlo: '`$anonymous_namespace_csrc/ops/addmm/addmm_aten_kernels.cc`/BuildAddmmShlo(7521a128e240c5e9).'
  AddMm: '`$anonymous_namespace_csrc/ops/addmm/addmm_aten_kernels.cc`/AddMm(7843cd938bd9110c).'
  AddMmOut: '`$anonymous_namespace_csrc/ops/addmm/addmm_aten_kernels.cc`/AddMmOut(afbf01f3d3c990ee).'
  AddMmActivationOut: '`$anonymous_namespace_csrc/ops/addmm/addmm_aten_kernels.cc`/AddMmActivationOut(a9f070ac0cd7a899).'
---
# Module: [`csrc/ops/addmm/addmm_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmm/addmm_aten_kernels.cc)

## Functions
- <a id="AddMm"></a>`AddMm(const at::Tensor& self, const at::Tensor& mat1, const at::Tensor& mat2, MaybePromotedScalar beta, PromotedScalar alpha, at::ScalarType out_scalar_type, OpParamCacheKeys& param_keys)` — [`L231`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmm/addmm_aten_kernels.cc#L231)
- <a id="AddMmActivationOut"></a>`AddMmActivationOut(const at::Tensor& self, const at::Tensor& mat1, const at::Tensor& mat2, MaybePromotedScalar beta, PromotedScalar alpha, bool use_gelu, at::ScalarType out_scalar_type, OpParamCacheKeys& param_keys, at::Tensor& out)` — [`L271`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmm/addmm_aten_kernels.cc#L271)
- <a id="AddMmOut"></a>`AddMmOut(const at::Tensor& self, const at::Tensor& mat1, const at::Tensor& mat2, MaybePromotedScalar beta, PromotedScalar alpha, at::ScalarType out_scalar_type, OpParamCacheKeys& param_keys, at::Tensor& out)` — [`L251`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmm/addmm_aten_kernels.cc#L251)
- <a id="AtenAddmmActivationOut"></a>`AtenAddmmActivationOut(const at::Tensor& self, const at::Tensor& mat1, const at::Tensor& mat2, const at::Scalar& beta, const at::Scalar& alpha, bool use_gelu, at::Tensor& out)` — [`L315`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmm/addmm_aten_kernels.cc#L315)
- <a id="AtenAddmmDtype"></a>`AtenAddmmDtype(const at::Tensor& self, const at::Tensor& mat1, const at::Tensor& mat2, at::ScalarType out_dtype, const at::Scalar& beta, const at::Scalar& alpha)` — [`L340`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmm/addmm_aten_kernels.cc#L340)
- <a id="AtenAddmmDtypeOut"></a>`AtenAddmmDtypeOut(const at::Tensor& self, const at::Tensor& mat1, const at::Tensor& mat2, at::ScalarType out_dtype, const at::Scalar& beta, const at::Scalar& alpha, at::Tensor& out)` — [`L356`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmm/addmm_aten_kernels.cc#L356)
- <a id="AtenAddmmOut"></a>`AtenAddmmOut(const at::Tensor& self, const at::Tensor& mat1, const at::Tensor& mat2, const at::Scalar& beta, const at::Scalar& alpha, at::Tensor& out)` — [`L294`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmm/addmm_aten_kernels.cc#L294)
- <a id="BuildAddmmShlo"></a>`BuildAddmmShlo(mlir::MlirOp self_op, mlir::MlirOp mat1_op, mlir::MlirOp mat2_op, std::optional<mlir::MlirOp> beta_op, mlir::MlirOp alpha_op, mlir::ElementType out_dtype, mlir::stablehlo::Precision precision)` — [`L58`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmm/addmm_aten_kernels.cc#L58)
- `BuildAddmmShlo(mlir::MlirOp self_op, mlir::MlirOp mat1_op, mlir::MlirOp mat2_op, std::optional<mlir::MlirOp> beta_op, mlir::MlirOp alpha_op, mlir::ElementType out_dtype, mlir::stablehlo::Precision precision)` — [`L58`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmm/addmm_aten_kernels.cc#L58)
- <a id="DispatchAddmm"></a>`DispatchAddmm(const at::Tensor& self, const at::Tensor& mat1, const at::Tensor& mat2, MaybePromotedScalar beta, PromotedScalar alpha, at::ScalarType out_scalar_type, OpParamCacheKeys& param_keys, std::optional<bool> use_gelu, Dispatch4&& dispatch4, Dispatch5&& dispatch5)` — [`L166`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmm/addmm_aten_kernels.cc#L166)
- <a id="ValidateAddmmInputsAndGetOutputDtype"></a>`ValidateAddmmInputsAndGetOutputDtype(const at::Tensor& self, const at::Tensor& mat1, const at::Tensor& mat2, const MaybePromotedScalar& beta, const PromotedScalar& alpha, at::ScalarType out_scalar_type)` — [`L121`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmm/addmm_aten_kernels.cc#L121) — Validates input dtypes, matrix dimensions, and broadcastability for addmm
- <a id="ValidateInputBroadcast"></a>`ValidateInputBroadcast(const at::Tensor& self, const Dimensions& output_dims_vec)` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmm/addmm_aten_kernels.cc#L100)

