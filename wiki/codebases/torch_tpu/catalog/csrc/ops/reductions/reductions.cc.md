---
title: 'Module: csrc/ops/reductions/reductions.cc'
type: catalog
provenance: extracted
module: csrc/ops/reductions/reductions.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildReductionShlo: BuildReductionShlo(41371e6da3840cf7).
  BuildKeepDimsShlo: BuildKeepDimsShlo(bd24e232362501d5).
---
# Module: [`csrc/ops/reductions/reductions.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reductions.cc)

## Functions
- <a id="BuildKeepDimsShlo"></a>`BuildKeepDimsShlo(mlir::MlirOp reduction_input, mlir::MlirOp reduction_output, absl::Span<const int64_t> dims)` — [`L73`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reductions.cc#L73) — Builds the output unsqueeze for reduction ops that keep dimensions. — documented in [reductions](../../../../concepts/reductions.md)
- <a id="BuildReductionShlo"></a>`BuildReductionShlo(mlir::MlirOp input_op, absl::Span<const int64_t> dims, mlir::Type mlir_type, mlir::MlirOp init_val, absl::AnyInvocable<void(mlir::RegionBuilder&) const> reduce_fn, ReductionMode reduction_mode)` — [`L37`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reductions.cc#L37) — documented in [reductions](../../../../concepts/reductions.md)

## Module values
- `BuildReductionShlo` — [`L37`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reductions.cc#L37)

