---
title: 'Module: csrc/ops/is/is.cc'
type: catalog
provenance: extracted
module: csrc/ops/is/is.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildIsNanShlo: BuildIsNanShlo(a7867b6222e713f9).
  BuildIsPosInfShlo: BuildIsPosInfShlo(a7867b6222e713f9).
  BuildIsNegInfShlo: BuildIsNegInfShlo(a7867b6222e713f9).
  MakeBoolLike: '`$anonymous_namespace_csrc/ops/is/is.cc`/MakeBoolLike(cf250d01414c83ef).'
  IsNanImpl: '`$anonymous_namespace_csrc/ops/is/is.cc`/IsNanImpl(cf97982c188f832c).'
---
# Module: [`csrc/ops/is/is.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/is/is.cc)

## Functions
- <a id="BuildIsNanShlo"></a>`BuildIsNanShlo(BuildIsNanShlo, IsNanImpl, false)` — [`L64`](../../../../../../../raw/code/torch_tpu/csrc/ops/is/is.cc#L64) — go/keep-sorted start
- <a id="BuildIsNegInfShlo"></a>`BuildIsNegInfShlo(BuildIsNegInfShlo, mlir::chlo::IsNegInf, false)` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/ops/is/is.cc#L65)
- <a id="BuildIsPosInfShlo"></a>`BuildIsPosInfShlo(BuildIsPosInfShlo, mlir::chlo::IsPosInf, false)` — [`L66`](../../../../../../../raw/code/torch_tpu/csrc/ops/is/is.cc#L66)
- <a id="IsNanImpl"></a>`IsNanImpl(mlir::MlirOp input_op)` — [`L39`](../../../../../../../raw/code/torch_tpu/csrc/ops/is/is.cc#L39)
- <a id="MakeBoolLike"></a>`MakeBoolLike(mlir::MlirOp input_op, mlir::MlirBuilder& builder, bool value)` — [`L34`](../../../../../../../raw/code/torch_tpu/csrc/ops/is/is.cc#L34) — Returns a Boolean tensor with the same shape as input_type and each

