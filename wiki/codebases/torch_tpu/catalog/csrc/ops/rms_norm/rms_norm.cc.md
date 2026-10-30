---
title: 'Module: csrc/ops/rms_norm/rms_norm.cc'
type: catalog
provenance: extracted
module: csrc/ops/rms_norm/rms_norm.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildRmsNormBackwardShlo: BuildRmsNormBackwardShlo(1fb152007654dd5).
  BuildRmsNormShlo: BuildRmsNormShlo(be75869fe44c94b4).
  BuildRmsNormDx: '`$anonymous_namespace_csrc/ops/rms_norm/rms_norm.cc`/BuildRmsNormDx(afb7534f9591e617).'
  BuildRmsNormDgamma: '`$anonymous_namespace_csrc/ops/rms_norm/rms_norm.cc`/BuildRmsNormDgamma(db3620e0e7d8b97).'
---
# Module: [`csrc/ops/rms_norm/rms_norm.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm.cc)

## Functions
- <a id="BuildRmsNormBackwardShlo"></a>`BuildRmsNormBackwardShlo(mlir::MlirOp dy, mlir::MlirOp x, mlir::MlirOp rstd, std::optional<mlir::MlirOp> weight, at::IntArrayRef normalized_shape, std::array<bool, 2> output_mask)` — [`L259`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm.cc#L259)
- `BuildRmsNormDgamma(mlir::MlirBuilder& builder, mlir::MlirOp dy_f32, mlir::MlirOp x_hat, std::optional<mlir::MlirOp> weight, at::IntArrayRef normalized_shape, mlir::FloatType compute_float_type, mlir::Type orig_weight_type, const Dimensions& batch_dims, mlir::MlirOp zero)` — [`L166`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm.cc#L166) — Builds the StableHLO operations for the gradient with respect to weight
- <a id="BuildRmsNormDgamma"></a>`BuildRmsNormDgamma(mlir::MlirBuilder& builder, mlir::MlirOp dy_f32, mlir::MlirOp x_hat, std::optional<mlir::MlirOp> weight, at::IntArrayRef normalized_shape, mlir::FloatType compute_float_type, mlir::Type orig_weight_type, const Dimensions& batch_dims, mlir::MlirOp zero)` — [`L166`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm.cc#L166) — Builds the StableHLO operations for the gradient with respect to weight
- `BuildRmsNormDx(mlir::MlirBuilder& builder, mlir::MlirOp dy_f32, mlir::MlirOp x_hat, mlir::MlirOp rstd_f32_bcast, std::optional<mlir::MlirOp> weight, at::IntArrayRef normalized_shape, mlir::RankedTensorType compute_x_type, mlir::FloatType compute_float_type, mlir::Type orig_elem_type, const Dimensions& norm_dims, const Dimensions& batch_dims, mlir::MlirOp zero)` — [`L210`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm.cc#L210) — Builds the StableHLO operations for the gradient with respect to input
- <a id="BuildRmsNormDx"></a>`BuildRmsNormDx(mlir::MlirBuilder& builder, mlir::MlirOp dy_f32, mlir::MlirOp x_hat, mlir::MlirOp rstd_f32_bcast, std::optional<mlir::MlirOp> weight, at::IntArrayRef normalized_shape, mlir::RankedTensorType compute_x_type, mlir::FloatType compute_float_type, mlir::Type orig_elem_type, const Dimensions& norm_dims, const Dimensions& batch_dims, mlir::MlirOp zero)` — [`L210`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm.cc#L210) — Builds the StableHLO operations for the gradient with respect to input
- <a id="BuildRmsNormShlo"></a>`BuildRmsNormShlo(mlir::MlirOp input_op, std::optional<mlir::MlirOp> weight_op, const int normalized_num_dims, const double eps)` — [`L43`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm.cc#L43) — RMSNorm(x) = x * w / sqrt(mean(x^2) + eps)

