---
title: 'Module: csrc/ops/logical/logical.cc'
type: catalog
provenance: extracted
module: csrc/ops/logical/logical.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildLogicalOrShlo: BuildLogicalOrShlo(9dd408ac7de815bd).
  BuildLogicalAndShlo: BuildLogicalAndShlo(9dd408ac7de815bd).
  BuildLogicalXorShlo: BuildLogicalXorShlo(9dd408ac7de815bd).
  BroadcastLogicalOperands: '`$anonymous_namespace_csrc/ops/logical/logical.cc`/BroadcastLogicalOperands(28eb7d3c534bfedb).'
  BuildLogicalNotShlo: BuildLogicalNotShlo(a7867b6222e713f9).
  CastToBooleanIfNeeded: '`$anonymous_namespace_csrc/ops/logical/logical.cc`/CastToBooleanIfNeeded(a7867b6222e713f9).'
  BroadcastedOperands.other: '`$anonymous_namespace_csrc/ops/logical/logical.cc`/BroadcastedOperands#other.'
  BroadcastedOperands.self: '`$anonymous_namespace_csrc/ops/logical/logical.cc`/BroadcastedOperands#self.'
  BroadcastedOperands: '`$anonymous_namespace_csrc/ops/logical/logical.cc`/BroadcastedOperands#'
---
# Module: [`csrc/ops/logical/logical.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/logical/logical.cc)

## Classes
### <a id="BroadcastedOperands"></a>`BroadcastedOperands`
- def: [`csrc/ops/logical/logical.cc:43`](../../../../../../../raw/code/torch_tpu/csrc/ops/logical/logical.cc#L43)
- signature: `struct BroadcastedOperands`
- members:
  - <a id="BroadcastedOperands.other"></a>`other` — [`L45`](../../../../../../../raw/code/torch_tpu/csrc/ops/logical/logical.cc#L45)
  - <a id="BroadcastedOperands.self"></a>`self` — [`L44`](../../../../../../../raw/code/torch_tpu/csrc/ops/logical/logical.cc#L44)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildLogicalAndShlo`](logical.cc.md#BuildLogicalAndShlo), [`BuildLogicalOrShlo`](logical.cc.md#BuildLogicalOrShlo), [`BuildLogicalXorShlo`](logical.cc.md#BuildLogicalXorShlo), [`BroadcastLogicalOperands`](logical.cc.md#BroadcastLogicalOperands)

## Functions
- <a id="BroadcastLogicalOperands"></a>`BroadcastLogicalOperands(mlir::MlirOp self, mlir::MlirOp other)` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/ops/logical/logical.cc#L48)
- <a id="BuildLogicalAndShlo"></a>`BuildLogicalAndShlo(mlir::MlirOp self, mlir::MlirOp other)` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/logical/logical.cc#L59)
- <a id="BuildLogicalNotShlo"></a>`BuildLogicalNotShlo(mlir::MlirOp self)` — [`L77`](../../../../../../../raw/code/torch_tpu/csrc/ops/logical/logical.cc#L77)
- <a id="BuildLogicalOrShlo"></a>`BuildLogicalOrShlo(mlir::MlirOp self, mlir::MlirOp other)` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/ops/logical/logical.cc#L65)
- <a id="BuildLogicalXorShlo"></a>`BuildLogicalXorShlo(mlir::MlirOp self, mlir::MlirOp other)` — [`L71`](../../../../../../../raw/code/torch_tpu/csrc/ops/logical/logical.cc#L71)
- <a id="CastToBooleanIfNeeded"></a>`CastToBooleanIfNeeded(mlir::MlirOp op)` — [`L35`](../../../../../../../raw/code/torch_tpu/csrc/ops/logical/logical.cc#L35)

