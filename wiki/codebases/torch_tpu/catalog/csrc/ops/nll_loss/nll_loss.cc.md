---
title: 'Module: csrc/ops/nll_loss/nll_loss.cc'
type: catalog
provenance: extracted
module: csrc/ops/nll_loss/nll_loss.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildNllLossForwardOutShlo: BuildNllLossForwardOutShlo(7664ab803088e611).
  BuildNllLossBackwardGradInputShlo: BuildNllLossBackwardGradInputShlo(67596fed33ceb706).
  GatherWeightsShlo: GatherWeightsShlo(3bc34110f3947668).
---
# Module: [`csrc/ops/nll_loss/nll_loss.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss.cc)

## Functions
- <a id="BuildNllLossBackwardGradInputShlo"></a>`BuildNllLossBackwardGradInputShlo(mlir::MlirOp grad_output, mlir::MlirOp self, mlir::MlirOp target, std::optional<mlir::MlirOp> weight, int64_t reduction, int64_t ignore_index, mlir::MlirOp total_weight, mlir::MlirBuilder& /*builder*/)` — [`L195`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss.cc#L195)
- `BuildNllLossForwardOutShlo(mlir::MlirOp self, mlir::MlirOp target, std::optional<mlir::MlirOp> weight, int64_t reduction, int64_t ignore_index, mlir::MlirBuilder& builder)` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss.cc#L54)
- <a id="BuildNllLossForwardOutShlo"></a>`BuildNllLossForwardOutShlo(mlir::MlirOp self, mlir::MlirOp target, std::optional<mlir::MlirOp> weight, int64_t reduction, int64_t ignore_index, mlir::MlirBuilder& builder)` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss.cc#L54)
- <a id="GatherWeightsShlo"></a>`GatherWeightsShlo(mlir::MlirOp weight, mlir::MlirOp safe_target)` — [`L39`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss.cc#L39) — Gathers class weights from 1D `weight` ([C]) using `safe_target` of arbitrary

