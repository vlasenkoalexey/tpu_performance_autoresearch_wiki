---
title: 'Module: csrc/ops/scatter/scatter.cc'
type: catalog
provenance: extracted
module: csrc/ops/scatter/scatter.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildScatterShlo: BuildScatterShlo(58dfb6e698f40b60).
  GetIdentityValue: '`$anonymous_namespace_csrc/ops/scatter/scatter.cc`/GetIdentityValue(d96c3ec0da936618).'
  GetRowBroadcastIndex: '`$anonymous_namespace_csrc/ops/scatter/scatter.cc`/GetRowBroadcastIndex(e5012d46f551c798).'
---
# Module: [`csrc/ops/scatter/scatter.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.cc)

## Functions
- <a id="BuildScatterShlo"></a>`BuildScatterShlo(mlir::MlirOp self, int64_t dim, mlir::MlirOp index, mlir::MlirOp src, ScatterOp scatter_op, mlir::ElementType computation_element_type, ScatterIncludeSelf include_self)` — [`L109`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.cc#L109)
- <a id="GetIdentityValue"></a>`GetIdentityValue(mlir::MlirBuilder& builder, mlir::Type type, ScatterOp op)` — [`L51`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.cc#L51) — Returns the identity value for the given scatter op and computation type
- <a id="GetRowBroadcastIndex"></a>`GetRowBroadcastIndex(mlir::MlirOp index, int64_t dim)` — [`L84`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.cc#L84) — If `index` is a broadcast of a 1-D tensor that is constant along every

