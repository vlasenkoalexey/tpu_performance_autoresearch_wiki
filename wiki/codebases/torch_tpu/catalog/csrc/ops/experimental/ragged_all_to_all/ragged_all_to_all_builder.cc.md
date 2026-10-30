---
title: 'Module: csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_builder.cc'
type: catalog
provenance: extracted
module: csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_builder.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildRaggedAllToAllShlo: BuildRaggedAllToAllShlo(1d4e95ca7ef9e45d).
---
# Module: [`csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_builder.cc`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_builder.cc)

## Functions
- <a id="BuildRaggedAllToAllShlo"></a>`BuildRaggedAllToAllShlo(mlir::MlirOp operand, mlir::MlirOp output, mlir::MlirOp input_offsets, mlir::MlirOp send_sizes, mlir::MlirOp output_offsets, mlir::MlirOp recv_sizes, mlir::DenseIntElementsAttr replica_groups_attr, int64_t channel_id)` — [`L34`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_builder.cc#L34) — Builds and emits a StableHLO custom call for the TPU `ragged_all_to_all`

