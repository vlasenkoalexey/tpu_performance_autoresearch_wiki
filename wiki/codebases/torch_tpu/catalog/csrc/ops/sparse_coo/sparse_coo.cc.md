---
title: 'Module: csrc/ops/sparse_coo/sparse_coo.cc'
type: catalog
provenance: extracted
module: csrc/ops/sparse_coo/sparse_coo.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildCoalesceAndCountShlo: BuildCoalesceAndCountShlo(d33401e4ea8828a3).
  BuildSparseToDenseShlo: BuildSparseToDenseShlo(612b36422e744ceb).
  BuildAddDenseSparseShlo: BuildAddDenseSparseShlo(9078ba194f5046ab).
  BuildMulSparseScalarShlo: BuildMulSparseScalarShlo(4e058530975e9b5a).
  BuildAddSparseSparseShlo: BuildAddSparseSparseShlo(8aca693db1b3d674).
  BuildNegSparseShlo: BuildNegSparseShlo(c116150205aa322e).
  ComputeUniqueCoordinateMask: '`$anonymous_namespace_csrc/ops/sparse_coo/sparse_coo.cc`/ComputeUniqueCoordinateMask(3312eecb330a296e).'
  BuildSliceCoalescedShlo: BuildSliceCoalescedShlo(23d29af48e568570).
  CompactUniqueIndices: '`$anonymous_namespace_csrc/ops/sparse_coo/sparse_coo.cc`/CompactUniqueIndices(950799e85e41aebf).'
  SortSparseCoordinatesAndValues: '`$anonymous_namespace_csrc/ops/sparse_coo/sparse_coo.cc`/SortSparseCoordinatesAndValues(1fcee7f1e74a8e05).'
  ScatterAddSparseToDense: '`$anonymous_namespace_csrc/ops/sparse_coo/sparse_coo.cc`/ScatterAddSparseToDense(9715a8045b971286).'
  BuildLexicographicalI64Comparator: '`$anonymous_namespace_csrc/ops/sparse_coo/sparse_coo.cc`/BuildLexicographicalI64Comparator(80b3a1bf030d9164).'
  SortedSparseCoo: '`$anonymous_namespace_csrc/ops/sparse_coo/sparse_coo.cc`/SortedSparseCoo#'
  BuildMaskDescIotaAscComparator: '`$anonymous_namespace_csrc/ops/sparse_coo/sparse_coo.cc`/BuildMaskDescIotaAscComparator(fb903c4b9d45beef).'
  SortedSparseCoo.indices: '`$anonymous_namespace_csrc/ops/sparse_coo/sparse_coo.cc`/SortedSparseCoo#indices.'
  SortedSparseCoo.values: '`$anonymous_namespace_csrc/ops/sparse_coo/sparse_coo.cc`/SortedSparseCoo#values.'
---
# Module: [`csrc/ops/sparse_coo/sparse_coo.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/sparse_coo/sparse_coo.cc)

## Classes
### <a id="SortedSparseCoo"></a>`SortedSparseCoo`
- def: [`csrc/ops/sparse_coo/sparse_coo.cc:135`](../../../../../../../raw/code/torch_tpu/csrc/ops/sparse_coo/sparse_coo.cc#L135)
- signature: `struct SortedSparseCoo`
- members:
  - <a id="SortedSparseCoo.indices"></a>`indices` — [`L136`](../../../../../../../raw/code/torch_tpu/csrc/ops/sparse_coo/sparse_coo.cc#L136)
  - <a id="SortedSparseCoo.values"></a>`values` — [`L137`](../../../../../../../raw/code/torch_tpu/csrc/ops/sparse_coo/sparse_coo.cc#L137)
- uses (calls/refs, reference-scoped): (none in-repo)

## Functions
- <a id="BuildAddDenseSparseShlo"></a>`BuildAddDenseSparseShlo(mlir::MlirOp dense_self_op, mlir::MlirOp sparse_indices_op, mlir::MlirOp sparse_values_op, std::optional<mlir::MlirOp> alpha_op, mlir::ElementType out_dtype)` — [`L242`](../../../../../../../raw/code/torch_tpu/csrc/ops/sparse_coo/sparse_coo.cc#L242) — Lowers dense + alpha * sparse -> dense to StableHLO using ScatterOp with
- <a id="BuildAddSparseSparseShlo"></a>`BuildAddSparseSparseShlo(mlir::MlirOp indices1_op, mlir::MlirOp values1_op, mlir::MlirOp indices2_op, mlir::MlirOp values2_op, std::optional<mlir::MlirOp> alpha_op, mlir::ElementType out_dtype)` — [`L264`](../../../../../../../raw/code/torch_tpu/csrc/ops/sparse_coo/sparse_coo.cc#L264) — Lowers sparse + alpha * sparse -> uncoalesced sparse (indices, values) to
- <a id="BuildCoalesceAndCountShlo"></a>`BuildCoalesceAndCountShlo(mlir::MlirOp indices_op, mlir::MlirOp values_op)` — [`L306`](../../../../../../../raw/code/torch_tpu/csrc/ops/sparse_coo/sparse_coo.cc#L306) — Coalesces a sparse COO tensor in StableHLO by lexicographically sorting
- <a id="BuildLexicographicalI64Comparator"></a>`BuildLexicographicalI64Comparator(const int64_t num_keys, mlir::RegionBuilder& rb)` — [`L74`](../../../../../../../raw/code/torch_tpu/csrc/ops/sparse_coo/sparse_coo.cc#L74)
- <a id="BuildMaskDescIotaAscComparator"></a>`BuildMaskDescIotaAscComparator(mlir::RegionBuilder& rb)` — [`L105`](../../../../../../../raw/code/torch_tpu/csrc/ops/sparse_coo/sparse_coo.cc#L105)
- <a id="BuildMulSparseScalarShlo"></a>`BuildMulSparseScalarShlo(mlir::MlirOp values_op, mlir::MlirOp scalar_op, mlir::ElementType out_dtype)` — [`L287`](../../../../../../../raw/code/torch_tpu/csrc/ops/sparse_coo/sparse_coo.cc#L287) — Multiplies sparse values by a 0-D scalar tensor in StableHLO.
- <a id="BuildNegSparseShlo"></a>`BuildNegSparseShlo(mlir::MlirOp values_op, mlir::ElementType out_dtype)` — [`L299`](../../../../../../../raw/code/torch_tpu/csrc/ops/sparse_coo/sparse_coo.cc#L299) — Negates sparse values in StableHLO.
- <a id="BuildSliceCoalescedShlo"></a>`BuildSliceCoalescedShlo(mlir::MlirOp compacted_indices_op, mlir::MlirOp compacted_values_op, const int64_t output_size)` — [`L348`](../../../../../../../raw/code/torch_tpu/csrc/ops/sparse_coo/sparse_coo.cc#L348) — Slices compacted coalesced indices [k, nnz] and values [nnz, ...] to their
- <a id="BuildSparseToDenseShlo"></a>`BuildSparseToDenseShlo(mlir::MlirOp indices_op, mlir::MlirOp values_op, absl::Span<const int64_t> out_sizes, mlir::ElementType out_dtype)` — [`L224`](../../../../../../../raw/code/torch_tpu/csrc/ops/sparse_coo/sparse_coo.cc#L224) — Lowers sparse-to-dense conversion to StableHLO using ScatterOp with AddOp.
- <a id="CompactUniqueIndices"></a>`CompactUniqueIndices(mlir::MlirBuilder& builder, mlir::MlirOp sorted_indices, mlir::MlirOp is_unique_mask)` — [`L208`](../../../../../../../raw/code/torch_tpu/csrc/ops/sparse_coo/sparse_coo.cc#L208)
- <a id="ComputeUniqueCoordinateMask"></a>`ComputeUniqueCoordinateMask(mlir::MlirBuilder& builder, mlir::MlirOp sorted_indices)` — [`L180`](../../../../../../../raw/code/torch_tpu/csrc/ops/sparse_coo/sparse_coo.cc#L180)
- <a id="ScatterAddSparseToDense"></a>`ScatterAddSparseToDense(mlir::MlirBuilder& builder, mlir::MlirOp operand, mlir::MlirOp scatter_indices_2d, mlir::MlirOp updates)` — [`L44`](../../../../../../../raw/code/torch_tpu/csrc/ops/sparse_coo/sparse_coo.cc#L44)
- <a id="SortSparseCoordinatesAndValues"></a>`SortSparseCoordinatesAndValues(mlir::MlirBuilder& builder, mlir::MlirOp indices_op, mlir::MlirOp values_op)` — [`L140`](../../../../../../../raw/code/torch_tpu/csrc/ops/sparse_coo/sparse_coo.cc#L140)

