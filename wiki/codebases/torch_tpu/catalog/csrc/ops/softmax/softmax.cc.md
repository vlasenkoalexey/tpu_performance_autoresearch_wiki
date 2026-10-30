---
title: 'Module: csrc/ops/softmax/softmax.cc'
type: catalog
provenance: extracted
module: csrc/ops/softmax/softmax.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildSoftmaxBackwardDataShlo: BuildSoftmaxBackwardDataShlo(476806f02d2eb95).
  BuildSoftmaxShlo: BuildSoftmaxShlo(2c0acbf30a0afe0e).
  BuildBroadcastedMaxShlo: '`$anonymous_namespace_csrc/ops/softmax/softmax.cc`/BuildBroadcastedMaxShlo(32e5625f5d56765e).'
  BuildMaskedSoftmaxShlo: BuildMaskedSoftmaxShlo(6fd1d6b73280415e).
  BuildMaskedSoftmaxBackwardDataShlo: BuildMaskedSoftmaxBackwardDataShlo(724db6f770f20e2).
  PrepareMaskOp: '`$anonymous_namespace_csrc/ops/softmax/softmax.cc`/PrepareMaskOp(f31d1d7463e61418).'
---
# Module: [`csrc/ops/softmax/softmax.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax.cc)

## Functions
- <a id="BuildBroadcastedMaxShlo"></a>`BuildBroadcastedMaxShlo(mlir::MlirOp input_op, int64_t dim)` — [`L46`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax.cc#L46)
- <a id="BuildMaskedSoftmaxBackwardDataShlo"></a>`BuildMaskedSoftmaxBackwardDataShlo(mlir::MlirOp grad_output_op, mlir::MlirOp output_op, mlir::MlirOp mask_op, int64_t dim, mlir::stablehlo::Precision precision)` — [`L293`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax.cc#L293)
- `BuildMaskedSoftmaxBackwardDataShlo(mlir::MlirOp grad_output_op, mlir::MlirOp output_op, mlir::MlirOp mask_op, int64_t dim, mlir::stablehlo::Precision precision)` — [`L293`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax.cc#L293)
- <a id="BuildMaskedSoftmaxShlo"></a>`BuildMaskedSoftmaxShlo(mlir::MlirOp input_op, mlir::MlirOp mask_op, int64_t dim, std::optional<int64_t> mask_type)` — [`L268`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax.cc#L268)
- `BuildSoftmaxBackwardDataShlo(mlir::MlirOp grad_output_op, mlir::MlirOp output_op, int64_t dim, mlir::stablehlo::Precision precision, SoftmaxMode softmax_mode)` — [`L135`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax.cc#L135)
- <a id="BuildSoftmaxBackwardDataShlo"></a>`BuildSoftmaxBackwardDataShlo(mlir::MlirOp grad_output_op, mlir::MlirOp output_op, int64_t dim, mlir::stablehlo::Precision precision, SoftmaxMode softmax_mode)` — [`L135`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax.cc#L135)
- <a id="BuildSoftmaxShlo"></a>`BuildSoftmaxShlo(mlir::MlirOp input_op, int64_t dim, SoftmaxMode softmax_mode)` — [`L75`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax.cc#L75)
- <a id="PrepareMaskOp"></a>`PrepareMaskOp(mlir::MlirOp mask_op, mlir::MlirOp input_op, std::optional<int64_t> mask_type)` — [`L227`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax.cc#L227)

