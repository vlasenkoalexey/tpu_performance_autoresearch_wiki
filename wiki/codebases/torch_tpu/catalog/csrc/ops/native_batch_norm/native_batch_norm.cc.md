---
title: 'Module: csrc/ops/native_batch_norm/native_batch_norm.cc'
type: catalog
provenance: extracted
module: csrc/ops/native_batch_norm/native_batch_norm.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildBatchNormBackward: BuildBatchNormBackward(17074246f634ffa0).
  BuildBatchNorm: BuildBatchNorm(5a799bd3f8b283c8).
  ComputeInvStd: '`$anonymous_namespace_csrc/ops/native_batch_norm/native_batch_norm.cc`/ComputeInvStd(bc9f3c11c029dd2d).'
---
# Module: [`csrc/ops/native_batch_norm/native_batch_norm.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm.cc)

## Functions
- <a id="BuildBatchNorm"></a>`BuildBatchNorm(mlir::MlirOp input, std::optional<mlir::MlirOp> weight_opt, std::optional<mlir::MlirOp> bias_opt, std::optional<mlir::MlirOp> running_mean_opt, std::optional<mlir::MlirOp> running_variance_opt, bool training, double momentum, double eps, mlir::ElementType acc_dtype)` — [`L219`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm.cc#L219)
- `BuildBatchNorm(mlir::MlirOp input, std::optional<mlir::MlirOp> weight_opt, std::optional<mlir::MlirOp> bias_opt, std::optional<mlir::MlirOp> running_mean_opt, std::optional<mlir::MlirOp> running_variance_opt, bool training, double momentum, double eps, mlir::ElementType acc_dtype)` — [`L219`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm.cc#L219)
- `BuildBatchNormBackward(mlir::MlirOp grad_out, mlir::MlirOp input, std::optional<mlir::MlirOp> weight_opt, std::optional<mlir::MlirOp> running_mean_opt, std::optional<mlir::MlirOp> running_variance_opt, std::optional<mlir::MlirOp> save_mean_opt, std::optional<mlir::MlirOp> save_invstd_opt, bool training, double eps, std::array<bool, 3> output_mask, mlir::ElementType acc_dtype)` — [`L50`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm.cc#L50)
- <a id="BuildBatchNormBackward"></a>`BuildBatchNormBackward(mlir::MlirOp grad_out, mlir::MlirOp input, std::optional<mlir::MlirOp> weight_opt, std::optional<mlir::MlirOp> running_mean_opt, std::optional<mlir::MlirOp> running_variance_opt, std::optional<mlir::MlirOp> save_mean_opt, std::optional<mlir::MlirOp> save_invstd_opt, bool training, double eps, std::array<bool, 3> output_mask, mlir::ElementType acc_dtype)` — [`L50`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm.cc#L50)
- <a id="ComputeInvStd"></a>`ComputeInvStd(mlir::MlirOp variance, double eps)` — [`L41`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm.cc#L41) — Computes the batch-norm inverse standard deviation: 1 / sqrt(variance + eps).

