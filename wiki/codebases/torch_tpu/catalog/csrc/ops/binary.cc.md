---
title: 'Module: csrc/ops/binary.cc'
type: catalog
provenance: extracted
module: csrc/ops/binary.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildAddShlo: BuildAddShlo(9dd408ac7de815bd).
  BuildPowShlo: BuildPowShlo(9dd408ac7de815bd).
  BuildPolarShlo: BuildPolarShlo(9dd408ac7de815bd).
  BuildComplexShlo: BuildComplexShlo(9dd408ac7de815bd).
  BuildBitwiseRightShiftShlo: BuildBitwiseRightShiftShlo(9dd408ac7de815bd).
---
# Module: [`csrc/ops/binary.cc`](../../../../../../raw/code/torch_tpu/csrc/ops/binary.cc)

## Functions
- <a id="BuildAddShlo"></a>`BuildAddShlo(mlir::MlirOp lhs_op, mlir::MlirOp rhs_op)` — [`L31`](../../../../../../raw/code/torch_tpu/csrc/ops/binary.cc#L31) — Special case `Add` lowering for boolean addition. XLA has ambiguity between
- <a id="BuildBitwiseRightShiftShlo"></a>`BuildBitwiseRightShiftShlo(mlir::MlirOp lhs_op, mlir::MlirOp rhs_op)` — [`L124`](../../../../../../raw/code/torch_tpu/csrc/ops/binary.cc#L124) — PyTorch expects that signed integers will use an arithmetic right shift
- <a id="BuildComplexShlo"></a>`BuildComplexShlo(mlir::MlirOp real_op, mlir::MlirOp imag_op)` — [`L47`](../../../../../../raw/code/torch_tpu/csrc/ops/binary.cc#L47)
- <a id="BuildPolarShlo"></a>`BuildPolarShlo(mlir::MlirOp abs_op, mlir::MlirOp angle_op)` — [`L71`](../../../../../../raw/code/torch_tpu/csrc/ops/binary.cc#L71)
- <a id="BuildPowShlo"></a>`BuildPowShlo(mlir::MlirOp base_op, mlir::MlirOp exp_op)` — [`L106`](../../../../../../raw/code/torch_tpu/csrc/ops/binary.cc#L106)

