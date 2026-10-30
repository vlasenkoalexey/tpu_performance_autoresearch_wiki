---
title: 'Module: csrc/ops/histc/histc.cc'
type: catalog
provenance: extracted
module: csrc/ops/histc/histc.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildHistcShlo: BuildHistcShlo(20f53584273fe272).
  BuildScatterAdd: '`$anonymous_namespace_csrc/ops/histc/histc.cc`/BuildScatterAdd(e2a5c2a1af4e1a89).'
  BuildHistcBoundsShlo: BuildHistcBoundsShlo(8c8c3dd6e1bea642).
  BuildClampedIndices: '`$anonymous_namespace_csrc/ops/histc/histc.cc`/BuildClampedIndices(ed638056fc429976).'
  BuildIndices: '`$anonymous_namespace_csrc/ops/histc/histc.cc`/BuildIndices(5c59848f29d6c73).'
  BuildReduceMinShlo: '`$anonymous_namespace_csrc/ops/histc/histc.cc`/BuildReduceMinShlo(cf97982c188f832c).'
  AdjustMinMaxForEq: '`$anonymous_namespace_csrc/ops/histc/histc.cc`/AdjustMinMaxForEq(5ca1b8efd0d5c1e2).'
  BuildReduceMaxShlo: '`$anonymous_namespace_csrc/ops/histc/histc.cc`/BuildReduceMaxShlo(cf97982c188f832c).'
  BuildBroadcastToShape: '`$anonymous_namespace_csrc/ops/histc/histc.cc`/BuildBroadcastToShape(35caeae15ae10642).'
  BuildReduce: '`$anonymous_namespace_csrc/ops/histc/histc.cc`/BuildReduce(3c295ebfa4a270e6).'
  BuildInRange: '`$anonymous_namespace_csrc/ops/histc/histc.cc`/BuildInRange(58797ee5e7d65062).'
---
# Module: [`csrc/ops/histc/histc.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc.cc)

## Functions
- <a id="AdjustMinMaxForEq"></a>`AdjustMinMaxForEq(mlir::MlirOp& min_op, mlir::MlirOp& max_op)` — [`L83`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc.cc#L83) — Adjusts the min and max to account for the case where min == max.
- <a id="BuildBroadcastToShape"></a>`BuildBroadcastToShape(mlir::MlirOp input_op, llvm::ArrayRef<int64_t> shape)` — [`L98`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc.cc#L98) — Broadcasts the input tensor to a given shape using BroadcastInDim.
- <a id="BuildClampedIndices"></a>`BuildClampedIndices(mlir::MlirOp indices, int64_t bins, mlir::MlirBuilder& builder)` — [`L129`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc.cc#L129) — Clamps the indices to the range [0, bins - 1].
- <a id="BuildHistcBoundsShlo"></a>`BuildHistcBoundsShlo(mlir::MlirOp input_op)` — [`L205`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc.cc#L205)
- <a id="BuildHistcShlo"></a>`BuildHistcShlo(mlir::MlirOp input_op, int64_t bins, mlir::MlirOp min_op, mlir::MlirOp max_op)` — [`L219`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc.cc#L219)
- <a id="BuildInRange"></a>`BuildInRange(mlir::MlirOp input_op, mlir::MlirOp min_op, mlir::MlirOp max_op)` — [`L140`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc.cc#L140) — Returns a boolean tensor that is true for elements in [min_op, max_op].
- <a id="BuildIndices"></a>`BuildIndices(mlir::MlirOp input_op, mlir::MlirOp min_op, mlir::MlirOp max_op, int64_t bins, mlir::MlirBuilder& builder)` — [`L111`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc.cc#L111) — Computes bin indices for each element in input_op.
- <a id="BuildReduce"></a>`BuildReduce(mlir::MlirOp input_op, mlir::Attribute init_attr)` — [`L43`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc.cc#L43) — Builds a reduction over all dimensions of the input tensor, resulting in a
- <a id="BuildReduceMaxShlo"></a>`BuildReduceMaxShlo(mlir::MlirOp input_op)` — [`L73`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc.cc#L73) — Builds a reduction to compute the maximum value over all elements of
- <a id="BuildReduceMinShlo"></a>`BuildReduceMinShlo(mlir::MlirOp input_op)` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc.cc#L63) — Builds a reduction to compute the minimum value over all elements of
- <a id="BuildScatterAdd"></a>`BuildScatterAdd(mlir::MlirOp clamped_indices, mlir::MlirOp in_range, int64_t bins, mlir::Type out_dtype, mlir::MlirBuilder& builder)` — [`L154`](../../../../../../../raw/code/torch_tpu/csrc/ops/histc/histc.cc#L154) — Builds a scatter-add operation to accumulate histogram counts.

