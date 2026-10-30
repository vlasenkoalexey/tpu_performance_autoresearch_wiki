---
title: 'Module: csrc/ops/scan_builder.cc'
type: catalog
provenance: extracted
module: csrc/ops/scan_builder.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildScanShlo: BuildScanShlo(1c1b8d3cb504181b).
  BuildAssociativeScanChlo: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/BuildAssociativeScanChlo(ee91d85e6db6392d).'
  PopulateScanBody: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/PopulateScanBody(6aa49c7b86bc8e8f).'
  CreateRankReducedConstantLike: CreateRankReducedConstantLike(9c2c7aa80a22f9ef).
  VerifyScanDimSizes: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/VerifyScanDimSizes(56da269292df5947).'
  PrepareScanLoop: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/PrepareScanLoop(bfa255871f5bc86).'
  UpdateAccumulatorSlice: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/UpdateAccumulatorSlice(b468e0bf05cfacaa).'
  SqueezeScanOutputs: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/SqueezeScanOutputs(abed769ca734e091).'
  BuildScanBodyInputs: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/BuildScanBodyInputs(186177b40ddfe191).'
  SliceInput: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/SliceInput(180911fad54857be).'
  GetScanDimSize: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/GetScanDimSize(1b0b2c9a99962010).'
  ScanLoopState.loc: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/ScanLoopState#loc.'
  GetSequenceIndex: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/GetSequenceIndex(3df4424735895ab1).'
  PopulateScanCondition: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/PopulateScanCondition(8d012d04c838e554).'
  IncrementLoopIndex: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/IncrementLoopIndex(7c42a94bd496cdec).'
  ScanLoopState.loop_types: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/ScanLoopState#loop_types.'
  CreateStartIndices: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/CreateStartIndices(230bfaa00db9923d).'
  ScanLoopState.scan_dim: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/ScanLoopState#scan_dim.'
  RankReduceType: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/RankReduceType(b6c55992c0ff5a47).'
  ScanLoopState.loop_inits: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/ScanLoopState#loop_inits.'
  ScanLoopState: '`$anonymous_namespace_csrc/ops/scan_builder.cc`/ScanLoopState#'
---
# Module: [`csrc/ops/scan_builder.cc`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc)

## Classes
### <a id="ScanLoopState"></a>`ScanLoopState`
- def: [`csrc/ops/scan_builder.cc:83`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L83)
- signature: `struct ScanLoopState`
- members:
  - <a id="ScanLoopState.loc"></a>`loc` — [`L87`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L87)
  - <a id="ScanLoopState.loop_inits"></a>`loop_inits` — [`L86`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L86)
  - <a id="ScanLoopState.loop_types"></a>`loop_types` — [`L85`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L85)
  - <a id="ScanLoopState.scan_dim"></a>`scan_dim` — [`L84`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L84)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildScanShlo`](scan_builder.cc.md#BuildScanShlo), [`BuildScanShlo`](scan_builder.cc.md#BuildScanShlo), [`PrepareScanLoop`](scan_builder.cc.md#PrepareScanLoop)

## Functions
- <a id="BuildAssociativeScanChlo"></a>`BuildAssociativeScanChlo(mlir::MlirBuilder& builder, const llvm::ArrayRef<mlir::MlirOp> scan_inputs, const int64_t scan_dim, const int64_t num_scan_inputs, const llvm::ArrayRef<mlir::MlirOp> carry_inits, const llvm::ArrayRef<mlir::MlirOp> output_inits, const MultiInputScanBodyBuilder& body_builder, const ScanOptions& options)` — [`L360`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L360) — Lowers an associative prefix scan to chlo.ScanOp, which the TPU compiler's
- `BuildAssociativeScanChlo(mlir::MlirBuilder& builder, const llvm::ArrayRef<mlir::MlirOp> scan_inputs, const int64_t scan_dim, const int64_t num_scan_inputs, const llvm::ArrayRef<mlir::MlirOp> carry_inits, const llvm::ArrayRef<mlir::MlirOp> output_inits, const MultiInputScanBodyBuilder& body_builder, const ScanOptions& options)` — [`L360`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L360) — Lowers an associative prefix scan to chlo.ScanOp, which the TPU compiler's
- <a id="BuildScanBodyInputs"></a>`BuildScanBodyInputs(mlir::MlirBuilder& builder, mlir::Block* body, const llvm::ArrayRef<mlir::MlirOp> scan_inputs, const int64_t num_scan_inputs, const int64_t scan_dim, const bool should_squeeze)` — [`L305`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L305) — Assembles the body's inputs: the scanned slices (unsqueezed back to size-1
- `BuildScanBodyInputs(mlir::MlirBuilder& builder, mlir::Block* body, const llvm::ArrayRef<mlir::MlirOp> scan_inputs, const int64_t num_scan_inputs, const int64_t scan_dim, const bool should_squeeze)` — [`L305`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L305) — Assembles the body's inputs: the scanned slices (unsqueezed back to size-1
- <a id="BuildScanShlo"></a>`BuildScanShlo(mlir::MlirBuilder& builder, mlir::MlirOp input, const int64_t dim, const llvm::ArrayRef<mlir::MlirOp> carry_inits, const llvm::ArrayRef<mlir::MlirOp> output_inits, const ScanBodyBuilder body_builder, const ScanOptions& options)` — [`L466`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L466) — Lowers a prefix scan along 'dim'. By default uses a StableHLO while loop; if
- `BuildScanShlo(mlir::MlirBuilder& builder, mlir::MlirOp input, const int64_t dim, const llvm::ArrayRef<mlir::MlirOp> carry_inits, const llvm::ArrayRef<mlir::MlirOp> output_inits, const ScanBodyBuilder body_builder, const ScanOptions& options)` — [`L466`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L466) — Lowers a prefix scan along 'dim'. By default uses a StableHLO while loop; if
- `BuildScanShlo(mlir::MlirBuilder& builder, llvm::ArrayRef<mlir::MlirOp> scan_inputs, int64_t dim, int64_t num_scan_inputs, llvm::ArrayRef<mlir::MlirOp> carry_inits, llvm::ArrayRef<mlir::MlirOp> output_inits, MultiInputScanBodyBuilder body_builder, const ScanOptions& options)` — [`L543`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L543) — Generalized version of BuildScanShlo supporting multiple inputs, separate
- `BuildScanShlo(mlir::MlirBuilder& builder, llvm::ArrayRef<mlir::MlirOp> scan_inputs, int64_t dim, int64_t num_scan_inputs, llvm::ArrayRef<mlir::MlirOp> carry_inits, llvm::ArrayRef<mlir::MlirOp> output_inits, MultiInputScanBodyBuilder body_builder, const ScanOptions& options)` — [`L543`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L543) — Generalized version of BuildScanShlo supporting multiple inputs, separate
- <a id="CreateRankReducedConstantLike"></a>`CreateRankReducedConstantLike(mlir::MlirOp input, int64_t scan_dim, const at::Scalar& value)` — [`L608`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L608) — Creates a constant tensor filled with 'value' matching the shape and bounds
- <a id="CreateStartIndices"></a>`CreateStartIndices(mlir::MlirBuilder& builder, const mlir::Value index, const int64_t rank, const int64_t scan_dim)` — [`L64`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L64)
- <a id="GetScanDimSize"></a>`GetScanDimSize(mlir::MlirBuilder& builder, mlir::MlirOp input, const int64_t scan_dim)` — [`L49`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L49)
- <a id="GetSequenceIndex"></a>`GetSequenceIndex(mlir::MlirBuilder& builder, const mlir::Location loc, const mlir::Value index, const mlir::Value seq_len, bool reverse)` — [`L121`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L121)
- <a id="IncrementLoopIndex"></a>`IncrementLoopIndex(mlir::MlirBuilder& builder, const mlir::Location loc, const mlir::Value index)` — [`L74`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L74)
- <a id="PopulateScanBody"></a>`PopulateScanBody(mlir::stablehlo::WhileOp& while_op, mlir::MlirBuilder& builder, llvm::ArrayRef<mlir::MlirOp> scan_inputs, const int64_t scan_dim, const llvm::SmallVector<mlir::Type>& loop_types, const mlir::Location loc, const int num_scan_inputs, const int num_carries, const MultiInputScanBodyBuilder& body_builder, ScanDirection scan_direction, bool should_squeeze)` — [`L197`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L197)
- `PopulateScanBody(mlir::stablehlo::WhileOp& while_op, mlir::MlirBuilder& builder, llvm::ArrayRef<mlir::MlirOp> scan_inputs, const int64_t scan_dim, const llvm::SmallVector<mlir::Type>& loop_types, const mlir::Location loc, const int num_scan_inputs, const int num_carries, const MultiInputScanBodyBuilder& body_builder, ScanDirection scan_direction, bool should_squeeze)` — [`L197`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L197)
- `PopulateScanCondition(mlir::stablehlo::WhileOp& while_op, mlir::MlirBuilder& builder, mlir::MlirOp input, const int64_t scan_dim, const llvm::SmallVector<mlir::Type>& loop_types, const mlir::Location loc)` — [`L178`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L178)
- <a id="PopulateScanCondition"></a>`PopulateScanCondition(mlir::stablehlo::WhileOp& while_op, mlir::MlirBuilder& builder, mlir::MlirOp input, const int64_t scan_dim, const llvm::SmallVector<mlir::Type>& loop_types, const mlir::Location loc)` — [`L178`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L178)
- <a id="PrepareScanLoop"></a>`PrepareScanLoop(mlir::MlirBuilder& builder, mlir::MlirOp input, const int64_t dim, const llvm::ArrayRef<mlir::MlirOp> carry_inits, const llvm::ArrayRef<mlir::MlirOp> output_inits)` — [`L90`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L90)
- <a id="RankReduceType"></a>`RankReduceType(const mlir::RankedTensorType type, const int64_t scan_dim)` — [`L294`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L294) — The type of one position's slice along the scan dimension: the input type
- <a id="SliceInput"></a>`SliceInput(mlir::MlirBuilder& builder, const mlir::Location loc, mlir::MlirOp input, const mlir::Value seq_idx, const int64_t scan_dim, bool should_squeeze)` — [`L137`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L137)
- <a id="SqueezeScanOutputs"></a>`SqueezeScanOutputs(mlir::MlirBuilder& builder, const llvm::ArrayRef<mlir::Value> new_outputs, const int64_t scan_dim, const bool should_squeeze)` — [`L332`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L332) — Squeezes the body's per-position outputs back to rank-reduced form (when the
- `SqueezeScanOutputs(mlir::MlirBuilder& builder, const llvm::ArrayRef<mlir::Value> new_outputs, const int64_t scan_dim, const bool should_squeeze)` — [`L332`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L332) — Squeezes the body's per-position outputs back to rank-reduced form (when the
- <a id="UpdateAccumulatorSlice"></a>`UpdateAccumulatorSlice(mlir::MlirBuilder& builder, const mlir::Location loc, const mlir::Value accumulator, const mlir::Value slice, const mlir::Value seq_idx, const int64_t scan_dim, bool was_squeezed)` — [`L161`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L161)
- <a id="VerifyScanDimSizes"></a>`VerifyScanDimSizes(llvm::ArrayRef<mlir::MlirOp> scan_inputs, int64_t dim, int64_t num_scan_inputs)` — [`L260`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.cc#L260)

