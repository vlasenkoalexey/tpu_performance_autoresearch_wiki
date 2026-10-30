---
title: 'Module: csrc/ops/lstm/lstm_common.cc'
type: catalog
provenance: extracted
module: csrc/ops/lstm/lstm_common.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ComputeLstmGateAdjoints: ComputeLstmGateAdjoints(4ec1d2ef5db79eff).
---
# Module: [`csrc/ops/lstm/lstm_common.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_common.cc)

## Functions
- <a id="ComputeLstmGateAdjoints"></a>`ComputeLstmGateAdjoints(mlir::MlirOp delta_h, mlir::MlirOp delta_c_next, mlir::MlirOp tanh_c, mlir::MlirOp c_prev, mlir::MlirOp i, mlir::MlirOp f, mlir::MlirOp g, mlir::MlirOp o, mlir::MlirOp one)` — [`L24`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_common.cc#L24) — Computes the pre-activation gate adjoints and cell state adjoint for a single

