---
title: 'Module: csrc/ops/unary.cc'
type: catalog
provenance: extracted
module: csrc/ops/unary.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildAbsShlo: BuildAbsShlo(a7867b6222e713f9).
  BuildConjPhysicalShlo: BuildConjPhysicalShlo(a7867b6222e713f9).
  BuildLogShlo: BuildLogShlo(c116150205aa322e).
  BuildLog1pShlo: BuildLog1pShlo(c116150205aa322e).
  BuildReciprocalShlo: BuildReciprocalShlo(c116150205aa322e).
  BuildSgnShlo: BuildSgnShlo(a7867b6222e713f9).
  BuildSignShlo: BuildSignShlo(a7867b6222e713f9).
  BuildFracShlo: BuildFracShlo(a7867b6222e713f9).
  LogN: '`$anonymous_namespace_csrc/ops/unary.cc`/LogN(f990e9aea1567fe).'
  BuildExp2Shlo: BuildExp2Shlo(c116150205aa322e).
  BuildErfcShlo: BuildErfcShlo(c116150205aa322e).
  BuildReluShlo: BuildReluShlo(a7867b6222e713f9).
  BuildTruncShlo: BuildTruncShlo(a7867b6222e713f9).
  BuildFloorShlo: BuildFloorShlo(a7867b6222e713f9).
  BuildLog2Shlo: BuildLog2Shlo(c116150205aa322e).
  BuildCeilShlo: BuildCeilShlo(a7867b6222e713f9).
  BuildLog10Shlo: BuildLog10Shlo(c116150205aa322e).
  BuildLiftFreshShlo: BuildLiftFreshShlo(a7867b6222e713f9).
---
# Module: [`csrc/ops/unary.cc`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc)

## Functions
- <a id="BuildAbsShlo"></a>`BuildAbsShlo(mlir::MlirOp input)` — [`L72`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L72) — For functions that require more than a single-line StableHlo builder
- <a id="BuildCeilShlo"></a>`BuildCeilShlo(mlir::MlirOp input_op)` — [`L137`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L137)
- <a id="BuildConjPhysicalShlo"></a>`BuildConjPhysicalShlo(mlir::MlirOp input_op)` — [`L153`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L153)
- <a id="BuildErfcShlo"></a>`BuildErfcShlo(mlir::MlirOp input, mlir::ElementType out_mlir_type)` — [`L334`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L334)
- <a id="BuildExp2Shlo"></a>`BuildExp2Shlo(mlir::MlirOp input_op, mlir::ElementType default_mlir_type)` — [`L247`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L247)
- <a id="BuildFloorShlo"></a>`BuildFloorShlo(mlir::MlirOp input_op)` — [`L145`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L145)
- <a id="BuildFracShlo"></a>`BuildFracShlo(mlir::MlirOp input)` — [`L340`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L340)
- <a id="BuildLiftFreshShlo"></a>`BuildLiftFreshShlo(mlir::MlirOp input_op)` — [`L201`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L201) — TODO(b/442665129): Test the lift_fresh op when torch.compile is ready.
- <a id="BuildLog10Shlo"></a>`BuildLog10Shlo(mlir::MlirOp input_op, mlir::ElementType default_mlir_type)` — [`L267`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L267)
- <a id="BuildLog1pShlo"></a>`BuildLog1pShlo(mlir::MlirOp input_op, mlir::ElementType default_dtype)` — [`L226`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L226)
- <a id="BuildLog2Shlo"></a>`BuildLog2Shlo(mlir::MlirOp input_op, mlir::ElementType default_mlir_type)` — [`L262`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L262)
- <a id="BuildLogShlo"></a>`BuildLogShlo(mlir::MlirOp input_op, mlir::ElementType default_dtype)` — [`L205`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L205)
- <a id="BuildReciprocalShlo"></a>`BuildReciprocalShlo(mlir::MlirOp input_op, mlir::ElementType default_mlir_type)` — [`L166`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L166)
- <a id="BuildReluShlo"></a>`BuildReluShlo(mlir::MlirOp input_op)` — [`L175`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L175)
- <a id="BuildSgnShlo"></a>`BuildSgnShlo(mlir::MlirOp input)` — [`L278`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L278)
- <a id="BuildSignShlo"></a>`BuildSignShlo(mlir::MlirOp input)` — [`L272`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L272)
- <a id="BuildTruncShlo"></a>`BuildTruncShlo(mlir::MlirOp input_op)` — [`L181`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L181)
- <a id="LogN"></a>`LogN(mlir::MlirOp input_op, int32_t n, mlir::ElementType default_dtype)` — [`L43`](../../../../../../raw/code/torch_tpu/csrc/ops/unary.cc#L43)

