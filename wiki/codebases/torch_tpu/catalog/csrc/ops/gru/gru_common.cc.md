---
title: 'Module: csrc/ops/gru/gru_common.cc'
type: catalog
provenance: extracted
module: csrc/ops/gru/gru_common.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ComputeGruGateAdjoints: ComputeGruGateAdjoints(cca0cf31921a4cd4).
---
# Module: [`csrc/ops/gru/gru_common.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_common.cc)

## Functions
- <a id="ComputeGruGateAdjoints"></a>`ComputeGruGateAdjoints(mlir::MlirOp delta_h, mlir::MlirOp hx, mlir::MlirOp resetgate, mlir::MlirOp updategate, mlir::MlirOp newgate, mlir::MlirOp h_n, mlir::MlirOp one)` — [`L24`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_common.cc#L24) — Computes the pre-activation gate adjoints for a single GRU step from

