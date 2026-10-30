---
title: 'Module: csrc/eager/device_assignment_pipeline.cc'
type: catalog
provenance: extracted
module: csrc/eager/device_assignment_pipeline.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  RewriteAndTileOperationForSubgroup: RewriteAndTileOperationForSubgroup(3a79750e118bc262).
  ResolvePallasDeviceAssignment: '`$anonymous_namespace_csrc/eager/device_assignment_pipeline.cc`/ResolvePallasDeviceAssignment(10d62f0529a01878).'
  VerifySameDeviceSet: '`$anonymous_namespace_csrc/eager/device_assignment_pipeline.cc`/VerifySameDeviceSet(72e4ee3a6a15305).'
  ResolveDeviceAssignment: ResolveDeviceAssignment(f84415437ea7b0a1).
  ApplySubgroupTilingOrReplicaRewriting: ApplySubgroupTilingOrReplicaRewriting(fc780b3990d88f71).
  ResolveDeviceAssignmentForTraversal: ResolveDeviceAssignmentForTraversal(4cd52f386d0ace4c).
  RewriteCustomCallBackendConfig: '`$anonymous_namespace_csrc/eager/device_assignment_pipeline.cc`/RewriteCustomCallBackendConfig(5d00bf74438e004a).'
  RewriteReplicaGroupsAttr: '`$anonymous_namespace_csrc/eager/device_assignment_pipeline.cc`/RewriteReplicaGroupsAttr(e3fc86864cfc3427).'
  VectorToString: '`$anonymous_namespace_csrc/eager/device_assignment_pipeline.cc`/VectorToString(51b83c67fbc9a836).'
  RewriteSourceTargetPairsAttr: '`$anonymous_namespace_csrc/eager/device_assignment_pipeline.cc`/RewriteSourceTargetPairsAttr(e3fc86864cfc3427).'
  BuildRankToPartition: '`$anonymous_namespace_csrc/eager/device_assignment_pipeline.cc`/BuildRankToPartition(297462f883590073).'
---
# Module: [`csrc/eager/device_assignment_pipeline.cc`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.cc)

## Functions
- `ApplySubgroupTilingOrReplicaRewriting(mlir::Operation* absl_nullable first_new_op, absl::Span<const mlir::func::FuncOp> new_func_ops, const DeferredOp& deferred_op, absl::Span<const int64_t> resolved_da)` — [`L286`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.cc#L286) — Applies partition-index replica rewriting to all MLIR operations emitted for
- <a id="ApplySubgroupTilingOrReplicaRewriting"></a>`ApplySubgroupTilingOrReplicaRewriting(mlir::Operation* absl_nullable first_new_op, absl::Span<const mlir::func::FuncOp> new_func_ops, const DeferredOp& deferred_op, absl::Span<const int64_t> resolved_da)` — [`L286`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.cc#L286) — Applies partition-index replica rewriting to all MLIR operations emitted for
- `BuildRankToPartition(absl::Span<const int64_t> op_da, absl::Span<const int64_t> resolved_da)` — [`L56`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.cc#L56)
- <a id="BuildRankToPartition"></a>`BuildRankToPartition(absl::Span<const int64_t> op_da, absl::Span<const int64_t> resolved_da)` — [`L56`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.cc#L56)
- `ResolveDeviceAssignment(absl::Span<const OpDeviceAssignment> ops, absl::Span<const PallasDeviceAssignment> pallas_ops)` — [`L210`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.cc#L210)
- <a id="ResolveDeviceAssignment"></a>`ResolveDeviceAssignment(absl::Span<const OpDeviceAssignment> ops, absl::Span<const PallasDeviceAssignment> pallas_ops)` — [`L210`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.cc#L210)
- <a id="ResolveDeviceAssignmentForTraversal"></a>`ResolveDeviceAssignmentForTraversal(absl::Span<const SharedDeviceBufferList> execution_order, absl::Span<const int64_t> pallas_device_assignment)` — [`L232`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.cc#L232)
- `ResolveDeviceAssignmentForTraversal(absl::Span<const SharedDeviceBufferList> execution_order, absl::Span<const int64_t> pallas_device_assignment)` — [`L232`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.cc#L232)
- <a id="ResolvePallasDeviceAssignment"></a>`ResolvePallasDeviceAssignment(absl::Span<const PallasDeviceAssignment> pallas_ops)` — [`L134`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.cc#L134)
- `ResolvePallasDeviceAssignment(absl::Span<const PallasDeviceAssignment> pallas_ops)` — [`L134`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.cc#L134)
- <a id="RewriteAndTileOperationForSubgroup"></a>`RewriteAndTileOperationForSubgroup(mlir::Operation* absl_nonnull root_op, absl::Span<const int64_t> op_da, absl::Span<const int64_t> resolved_da)` — [`L257`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.cc#L257) — Rewrites rank-local collective attributes (`replica_groups`,
- <a id="RewriteCustomCallBackendConfig"></a>`RewriteCustomCallBackendConfig(mlir::Operation* op, absl::Span<const int64_t> rank_to_partition)` — [`L179`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.cc#L179)
- <a id="RewriteReplicaGroupsAttr"></a>`RewriteReplicaGroupsAttr(mlir::DenseIntElementsAttr attr, absl::Span<const int64_t> rank_to_partition)` — [`L73`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.cc#L73)
- <a id="RewriteSourceTargetPairsAttr"></a>`RewriteSourceTargetPairsAttr(mlir::DenseIntElementsAttr attr, absl::Span<const int64_t> rank_to_partition)` — [`L113`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.cc#L113)
- <a id="VectorToString"></a>`VectorToString(absl::Span<const int64_t> vec)` — [`L51`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.cc#L51)
- <a id="VerifySameDeviceSet"></a>`VerifySameDeviceSet(absl::Span<const int64_t> resolved_da, const OpDeviceAssignment& op, size_t index)` — [`L158`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.cc#L158)

