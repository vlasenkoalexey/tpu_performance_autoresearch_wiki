---
title: 'Module: csrc/ops/index_put/index_put.cc'
type: catalog
provenance: extracted
module: csrc/ops/index_put/index_put.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ApplyScatter: '`$anonymous_namespace_csrc/ops/index_put/index_put.cc`/ApplyScatter(fea959f79a26162c).'
  ApplySelect: '`$anonymous_namespace_csrc/ops/index_put/index_put.cc`/ApplySelect(607c9e45d110e5c1).'
  BuildIndexPutShlo: BuildIndexPutShlo(fea959f79a26162c).
  BuildIndexPutSelectShlo: BuildIndexPutSelectShlo(607c9e45d110e5c1).
---
# Module: [`csrc/ops/index_put/index_put.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put.cc)

## Functions
- <a id="ApplyScatter"></a>`ApplyScatter(mlir::MlirOp self, mlir::ArrayRef<mlir::MlirOp> indices, const int64_t index_start_dim, const int64_t index_end_dim, const Dimensions& index_broadcast_shape, mlir::MlirOp values, const Dimensions& values_broadcast_shape, const bool accumulate)` — [`L42`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put.cc#L42)
- <a id="ApplySelect"></a>`ApplySelect(mlir::MlirOp self, mlir::MlirOp mask, const int64_t index_start_dim, mlir::MlirOp values, bool accumulate)` — [`L196`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put.cc#L196)
- <a id="BuildIndexPutSelectShlo"></a>`BuildIndexPutSelectShlo(mlir::MlirOp self, mlir::MlirOp mask, const int64_t index_start_dim, mlir::MlirOp values, const bool accumulate)` — [`L272`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put.cc#L272) — Builds StableHLO operations to implement the semantics of index_put operation
- <a id="BuildIndexPutShlo"></a>`BuildIndexPutShlo(mlir::MlirOp self, mlir::ArrayRef<mlir::MlirOp> indices, const int64_t index_start_dim, const int64_t index_end_dim, const Dimensions& index_broadcast_shape, mlir::MlirOp values, const Dimensions& values_broadcast_shape, const bool accumulate)` — [`L262`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_put/index_put.cc#L262) — Builds StableHLO operations to implement the semantics of index_put operation

