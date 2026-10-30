---
title: 'Module: csrc/ops/min_max/min_max.cc'
type: catalog
provenance: extracted
module: csrc/ops/min_max/min_max.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildMinMaxShlo: BuildMinMaxShlo(8e0deda88a5b5c00).
  RestoreReducedDims: '`$anonymous_namespace_csrc/ops/min_max/min_max.cc`/RestoreReducedDims(2bf8e380077c7cab).'
  GetMinMaxInitValue: '`$anonymous_namespace_csrc/ops/min_max/min_max.cc`/GetMinMaxInitValue(7731e13392ba92c5).'
  BuildReduceBody: '`$anonymous_namespace_csrc/ops/min_max/min_max.cc`/BuildReduceBody(71620b4e67a58245).'
  PrepareReductionInput: '`$anonymous_namespace_csrc/ops/min_max/min_max.cc`/PrepareReductionInput(dfbad5e266d586c3).'
  ReductionInput: '`$anonymous_namespace_csrc/ops/min_max/min_max.cc`/ReductionInput#'
  ReductionInput.was_flattened: '`$anonymous_namespace_csrc/ops/min_max/min_max.cc`/ReductionInput#was_flattened.'
  UpdateComparisonsForNaN: '`$anonymous_namespace_csrc/ops/min_max/min_max.cc`/UpdateComparisonsForNaN(3a33f12fbc99ae0).'
  ReductionInput.op: '`$anonymous_namespace_csrc/ops/min_max/min_max.cc`/ReductionInput#op.'
  ReductionInput.dim: '`$anonymous_namespace_csrc/ops/min_max/min_max.cc`/ReductionInput#dim.'
---
# Module: [`csrc/ops/min_max/min_max.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.cc)

## Classes
### <a id="ReductionInput"></a>`ReductionInput`
- def: [`csrc/ops/min_max/min_max.cc:107`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.cc#L107)
- signature: `struct ReductionInput`
- members:
  - <a id="ReductionInput.dim"></a>`dim` — [`L109`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.cc#L109)
  - <a id="ReductionInput.op"></a>`op` — [`L108`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.cc#L108)
  - <a id="ReductionInput.was_flattened"></a>`was_flattened` — [`L110`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.cc#L110)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildMinMaxShlo`](min_max.cc.md#BuildMinMaxShlo), [`PrepareReductionInput`](min_max.cc.md#PrepareReductionInput)

## Functions
- <a id="BuildMinMaxShlo"></a>`BuildMinMaxShlo(c10::optional<int64_t> dim, MinMaxOp op, ReductionMode mode, mlir::MlirOp input_op)` — [`L165`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.cc#L165) — Builds a StableHLO reduction for min/max operations, returning both the
- <a id="BuildReduceBody"></a>`BuildReduceBody(MinMaxOp op, mlir::Type value_type, mlir::Type index_type, mlir::RegionBuilder& rb)` — [`L68`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.cc#L68)
- <a id="GetMinMaxInitValue"></a>`GetMinMaxInitValue(mlir::MlirBuilder& builder, MinMaxOp op, mlir::Type element_type)` — [`L128`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.cc#L128) — Returns the initial value for reduction based on the MinMaxOp type
- <a id="PrepareReductionInput"></a>`PrepareReductionInput(mlir::MlirOp input_op, c10::optional<int64_t> dim)` — [`L115`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.cc#L115) — Flattens the input tensor to 1D if no reduction dimension is specified,
- <a id="RestoreReducedDims"></a>`RestoreReducedDims(mlir::MlirOp original_input, MinMaxOutputs outputs, int64_t reduction_dim, bool was_flattened)` — [`L145`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.cc#L145) — Restores the reduced dimensions to size 1 when keepdim is True.
- <a id="UpdateComparisonsForNaN"></a>`UpdateComparisonsForNaN(mlir::MlirOp& input_value0, mlir::MlirOp& input_value1, mlir::MlirOp& comparison_value, mlir::MlirOp& is_equal)` — [`L52`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.cc#L52) — For floating-point types, updates `comparison_value` and `is_equal` so that

