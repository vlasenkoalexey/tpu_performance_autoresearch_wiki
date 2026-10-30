---
title: 'Module: csrc/ops/addmv/addmv_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/addmv/addmv_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenAddmvOut: AtenAddmvOut(a07f23bfc1f8200e).
  Addmv: '`$anonymous_namespace_csrc/ops/addmv/addmv_aten_kernels.cc`/Addmv(5aca5006f2e20f9d).'
  ValidateAddmvInputs: '`$anonymous_namespace_csrc/ops/addmv/addmv_aten_kernels.cc`/ValidateAddmvInputs(c7a06e961a3e1ecc).'
  BuildAddmvShlo: '`$anonymous_namespace_csrc/ops/addmv/addmv_aten_kernels.cc`/BuildAddmvShlo(3df79c730fda6447).'
  BuildAddmvShloBetaZero: '`$anonymous_namespace_csrc/ops/addmv/addmv_aten_kernels.cc`/BuildAddmvShloBetaZero(9cf4131192e75483).'
  MatVecDot: '`$anonymous_namespace_csrc/ops/addmv/addmv_aten_kernels.cc`/MatVecDot(315ec7c4bc8dd31d).'
---
# Module: [`csrc/ops/addmv/addmv_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmv/addmv_aten_kernels.cc)

## Functions
- <a id="Addmv"></a>`Addmv(const at::Tensor& self, const at::Tensor& mat, const at::Tensor& vec, MaybePromotedScalar beta, const at::Tensor& alpha_tensor, at::Tensor& out, OpParamCacheKeys& param_keys)` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmv/addmv_aten_kernels.cc#L112)
- <a id="AtenAddmvOut"></a>`AtenAddmvOut(const at::Tensor& self, const at::Tensor& mat, const at::Tensor& vec, const at::Scalar& beta, const at::Scalar& alpha, at::Tensor& out)` — [`L203`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmv/addmv_aten_kernels.cc#L203)
- <a id="BuildAddmvShlo"></a>`BuildAddmvShlo(mlir::MlirOp self_op, mlir::MlirOp mat_op, mlir::MlirOp vec_op, mlir::MlirOp beta_op, mlir::MlirOp alpha_op, mlir::ElementType out_dtype, mlir::stablehlo::Precision precision)` — [`L95`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmv/addmv_aten_kernels.cc#L95)
- `BuildAddmvShlo(mlir::MlirOp self_op, mlir::MlirOp mat_op, mlir::MlirOp vec_op, mlir::MlirOp beta_op, mlir::MlirOp alpha_op, mlir::ElementType out_dtype, mlir::stablehlo::Precision precision)` — [`L95`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmv/addmv_aten_kernels.cc#L95)
- `BuildAddmvShloBetaZero(mlir::MlirOp mat_op, mlir::MlirOp vec_op, mlir::MlirOp alpha_op, mlir::ElementType out_dtype, mlir::stablehlo::Precision precision)` — [`L86`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmv/addmv_aten_kernels.cc#L86)
- <a id="BuildAddmvShloBetaZero"></a>`BuildAddmvShloBetaZero(mlir::MlirOp mat_op, mlir::MlirOp vec_op, mlir::MlirOp alpha_op, mlir::ElementType out_dtype, mlir::stablehlo::Precision precision)` — [`L86`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmv/addmv_aten_kernels.cc#L86)
- `MatVecDot(mlir::MlirOp mat_op, mlir::MlirOp vec_op, mlir::ElementType out_dtype, mlir::stablehlo::Precision precision)` — [`L51`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmv/addmv_aten_kernels.cc#L51) — Matrix-vector dot product helper.
- <a id="MatVecDot"></a>`MatVecDot(mlir::MlirOp mat_op, mlir::MlirOp vec_op, mlir::ElementType out_dtype, mlir::stablehlo::Precision precision)` — [`L51`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmv/addmv_aten_kernels.cc#L51) — Matrix-vector dot product helper.
- <a id="ValidateAddmvInputs"></a>`ValidateAddmvInputs(const at::Tensor& self, const at::Tensor& mat, const at::Tensor& vec, const at::Scalar& beta, const at::Scalar& alpha)` — [`L155`](../../../../../../../raw/code/torch_tpu/csrc/ops/addmv/addmv_aten_kernels.cc#L155)

