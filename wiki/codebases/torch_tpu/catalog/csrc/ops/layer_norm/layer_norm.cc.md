---
title: 'Module: csrc/ops/layer_norm/layer_norm.cc'
type: catalog
provenance: extracted
module: csrc/ops/layer_norm/layer_norm.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildLayerNormShlo: BuildLayerNormShlo(72a47bbf775e937c).
  BuildLayerNormBackwardShlo: BuildLayerNormBackwardShlo(8e17292c415461c8).
  ComputeTwoMoments: '`$anonymous_namespace_csrc/ops/layer_norm/layer_norm.cc`/ComputeTwoMoments(271016dc718aa87f).'
  TwoMoments.mean_squared: '`$anonymous_namespace_csrc/ops/layer_norm/layer_norm.cc`/TwoMoments#mean_squared.'
  TwoMoments: '`$anonymous_namespace_csrc/ops/layer_norm/layer_norm.cc`/TwoMoments#'
  TwoMoments.mean: '`$anonymous_namespace_csrc/ops/layer_norm/layer_norm.cc`/TwoMoments#mean.'
---
# Module: [`csrc/ops/layer_norm/layer_norm.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm.cc)

## Classes
### <a id="TwoMoments"></a>`TwoMoments`
- def: [`csrc/ops/layer_norm/layer_norm.cc:42`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm.cc#L42)
- signature: `struct TwoMoments`
- members:
  - <a id="TwoMoments.mean"></a>`mean` — [`L43`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm.cc#L43)
  - <a id="TwoMoments.mean_squared"></a>`mean_squared` — [`L44`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm.cc#L44)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildLayerNormShlo`](layer_norm.cc.md#BuildLayerNormShlo), [`ComputeTwoMoments`](layer_norm.cc.md#ComputeTwoMoments)

## Functions
- <a id="BuildLayerNormBackwardShlo"></a>`BuildLayerNormBackwardShlo(mlir::MlirOp dy, mlir::MlirOp x, mlir::MlirOp mean, mlir::MlirOp rstd, std::optional<mlir::MlirOp> weight, at::IntArrayRef normalized_shape, bool compute_dbeta)` — [`L233`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm.cc#L233)
- <a id="BuildLayerNormShlo"></a>`BuildLayerNormShlo(mlir::MlirOp input_op, std::optional<mlir::MlirOp> weight_op, std::optional<mlir::MlirOp> bias_op, const int normalized_num_dims, const double eps)` — [`L107`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm.cc#L107) — This layer implements the operation as described:
- `ComputeTwoMoments(const mlir::RankedTensorType& input_type, mlir::MlirOp input_casted, mlir::MlirOp sum_x, mlir::MlirOp sum_x_squared, const Dimensions& reduction_axes, mlir::Type stats_type)` — [`L47`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm.cc#L47)
- <a id="ComputeTwoMoments"></a>`ComputeTwoMoments(const mlir::RankedTensorType& input_type, mlir::MlirOp input_casted, mlir::MlirOp sum_x, mlir::MlirOp sum_x_squared, const Dimensions& reduction_axes, mlir::Type stats_type)` — [`L47`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm.cc#L47)

