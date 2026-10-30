---
title: 'Module: csrc/eager/device_assignment_pipeline.h'
type: catalog
provenance: extracted
module: csrc/eager/device_assignment_pipeline.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  OpDeviceAssignment: OpDeviceAssignment#
  PallasDeviceAssignment.device_assignment: PallasDeviceAssignment#device_assignment.
  PallasDeviceAssignment: PallasDeviceAssignment#
  OpDeviceAssignment.device_assignment: OpDeviceAssignment#device_assignment.
  OpDeviceAssignment.op_name: OpDeviceAssignment#op_name.
---
# Module: [`csrc/eager/device_assignment_pipeline.h`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.h)

## Classes
### <a id="OpDeviceAssignment"></a>`OpDeviceAssignment`
- def: [`csrc/eager/device_assignment_pipeline.h:34`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.h#L34)
- signature: `struct OpDeviceAssignment`
- members:
  - <a id="OpDeviceAssignment.device_assignment"></a>`device_assignment` — [`L36`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.h#L36)
  - <a id="OpDeviceAssignment.op_name"></a>`op_name` — [`L35`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.h#L35)
- uses (calls/refs, reference-scoped): [`OpName`](../ops/op_names.h.md#OpName)
- used by: [`VerifySameDeviceSet`](device_assignment_pipeline.cc.md#VerifySameDeviceSet), [`TestBody`](device_assignment_pipeline_test.cc.md#DeviceAssignmentPipelineTest_MultiSliceRewritePreservesRankOrderAndPerSliceSymmetryForMegascale_Test.TestBody), [`device_assignment`](device_assignment_pipeline.h.md#PallasDeviceAssignment.device_assignment), [`ResolveDeviceAssignment`](device_assignment_pipeline.cc.md#ResolveDeviceAssignment), [`TestBody`](device_assignment_pipeline_test.cc.md#DeviceAssignmentPipelineTest_MultiSlicePermutedLauncherRanksShardIotaAndReplicateRewrite_Test.TestBody), [`TestBody`](device_assignment_pipeline_test.cc.md#DeviceAssignmentPipelineTest_ResolveDeviceAssignmentPermutationRemapsWithWarning_Test.TestBody), [`ResolveDeviceAssignmentForTraversal`](device_assignment_pipeline.cc.md#ResolveDeviceAssignmentForTraversal), [`TestBody`](device_assignment_pipeline_test.cc.md#DeviceAssignmentPipelineTest_ResolveDeviceAssignmentLogsWarningAndFailsOnDifferingDAs_Test.TestBody), [`TestBody`](device_assignment_pipeline_test.cc.md#DeviceAssignmentPipelineTest_ResolveDeviceAssignmentHsdpSymmetricAcrossRanks_Test.TestBody), [`TestBody`](device_assignment_pipeline_test.cc.md#DeviceAssignmentPipelineTest_ResolveDeviceAssignmentPreservesSyntheticNonZeroDeviceIds_Test.TestBody)

### <a id="PallasDeviceAssignment"></a>`PallasDeviceAssignment`
- def: [`csrc/eager/device_assignment_pipeline.h:39`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.h#L39)
- signature: `struct PallasDeviceAssignment`
- members:
  - <a id="PallasDeviceAssignment.device_assignment"></a>`device_assignment` — [`L40`](../../../../../../raw/code/torch_tpu/csrc/eager/device_assignment_pipeline.h#L40)
- uses (calls/refs, reference-scoped): [`DeferredOp`](device_buffer.h.md#DeferredOp), [`SharedDeviceBufferList`](device_buffer.h.md#SharedDeviceBufferList), [`RewriteAndTileOperationForSubgroup`](device_assignment_pipeline.cc.md#RewriteAndTileOperationForSubgroup), [`ResolveDeviceAssignment`](device_assignment_pipeline.cc.md#ResolveDeviceAssignment), [`OpDeviceAssignment`](device_assignment_pipeline.h.md#OpDeviceAssignment), [`ResolveDeviceAssignment`](device_assignment_pipeline.cc.md#ResolveDeviceAssignment), [`ApplySubgroupTilingOrReplicaRewriting`](device_assignment_pipeline.cc.md#ApplySubgroupTilingOrReplicaRewriting), [`ResolveDeviceAssignmentForTraversal`](device_assignment_pipeline.cc.md#ResolveDeviceAssignmentForTraversal), [`ApplySubgroupTilingOrReplicaRewriting`](device_assignment_pipeline.cc.md#ApplySubgroupTilingOrReplicaRewriting), [`ResolveDeviceAssignmentForTraversal`](device_assignment_pipeline.cc.md#ResolveDeviceAssignmentForTraversal)
- used by: [`ResolvePallasDeviceAssignment`](device_assignment_pipeline.cc.md#ResolvePallasDeviceAssignment), [`ResolveDeviceAssignment`](device_assignment_pipeline.cc.md#ResolveDeviceAssignment), [`TestBody`](device_assignment_pipeline_test.cc.md#DeviceAssignmentPipelineTest_ResolveDeviceAssignmentPermutationRemapsWithWarning_Test.TestBody), [`ResolveDeviceAssignmentForTraversal`](device_assignment_pipeline.cc.md#ResolveDeviceAssignmentForTraversal), [`TestBody`](device_assignment_pipeline_test.cc.md#DeviceAssignmentPipelineTest_ResolveDeviceAssignmentLogsWarningAndFailsOnDifferingDAs_Test.TestBody), [`TestBody`](device_assignment_pipeline_test.cc.md#DeviceAssignmentPipelineTest_ResolveDeviceAssignmentThrowsOnDifferingPallasMeshes_Test.TestBody)

