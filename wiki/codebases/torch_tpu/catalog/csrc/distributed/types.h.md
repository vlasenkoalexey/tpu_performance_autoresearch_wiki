---
title: 'Module: csrc/distributed/types.h'
type: catalog
provenance: extracted
module: csrc/distributed/types.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  DeviceGroupList: DeviceGroupList#
  DeviceGroup: DeviceGroup#
  DeviceGroupList.DeviceGroupList: DeviceGroupList#DeviceGroupList(ced63f7c635d850d).
  DeviceGroupList.operator: DeviceGroupList#`operator[]`(fa5b381ed6d106f9).
  DeviceGroupList.groups_: DeviceGroupList#groups_.
  DeviceGroupList.groups: DeviceGroupList#groups(e47d417e9239fcf3).
  DeviceGroupList.fingerprint_: DeviceGroupList#fingerprint_.
  DeviceGroupList.empty: DeviceGroupList#empty(50ce9a9e25b4a850).
  DeviceGroupList.size: DeviceGroupList#size(fe4d2d262d4164a8).
  EncodeParamCacheKey: EncodeParamCacheKey(323e51b19105d354).
  Fingerprint64Impl.Compute: internal/Fingerprint64Impl#Compute(323e51b19105d354).
  DeviceGroupList.fingerprint: DeviceGroupList#fingerprint(fe4d2d262d4164a8).
  DeviceGroupList.at: DeviceGroupList#at(fa5b381ed6d106f9).
  DeviceGroupList.cend: DeviceGroupList#cend(a2b22adafb4c9f54).
  DeviceGroupList.cbegin: DeviceGroupList#cbegin(a2b22adafb4c9f54).
  DeviceGroupList.end: DeviceGroupList#end(a2b22adafb4c9f54).
  DeviceGroupList.begin: DeviceGroupList#begin(a2b22adafb4c9f54).
---
# Module: [`csrc/distributed/types.h`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h)

## Classes
### <a id="DeviceGroup"></a>`DeviceGroup`
- def: [`csrc/distributed/types.h:31`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L31) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- doc: TODO(b/445264222) Create a more purpose-specific type for device groups
- signature: `using DeviceGroup = std::vector<int64_t>`
- used by: [`ProcessGroupTpu`](process_group_tpu.cc.md#ProcessGroupTpu.ProcessGroupTpu), [`InitializeRankToDeviceMappings`](process_group_tpu.cc.md#ProcessGroupTpu.InitializeRankToDeviceMappings), [`GatherMemberWorldRanks`](process_group_tpu.cc.md#ProcessGroupTpu.GatherMemberWorldRanks), [`GatherSubgroupsViaNodeLocalStore`](process_group_tpu.cc.md#GatherSubgroupsViaNodeLocalStore), [`GatherAllSubgroups`](process_group_tpu.cc.md#ProcessGroupTpu.GatherAllSubgroups), [`OpDebugString`](process_group_tpu.h.md#ProcessGroupTpu.OpDebugString), [`BuildReplicaGroupsAttr`](utils.cc.md#BuildReplicaGroupsAttr), [`DeviceGroupList`](types.cc.md#DeviceGroupList.DeviceGroupList), [`expected_local_subgroup`](process_group_tpu_test.cc.md#ProcessGroupTpuTest_GatherSubgroupsViaNodeLocalStoreCrossNodeSubgroups_Test.TestBody.RankSubgroupSpec.expected_local_subgroup), [`TestBody`](process_group_tpu_test.cc.md#ProcessGroupTpuTest_GatherSubgroupsViaNodeLocalStoreWorldSizedPreservesOrder_Test.TestBody), [`TestBody`](types_test.cc.md#DeviceGroupListTest_PreservesOrderWhenNormalizeIsFalse_Test.TestBody), [`PermuteDeviceAssignmentForSubgroups`](process_group_tpu.cc.md#PermuteDeviceAssignmentForSubgroups), [`DeviceGroupList`](types.cc.md#DeviceGroupList.DeviceGroupList), [`DeviceGroupList`](types.h.md#DeviceGroupList.DeviceGroupList), [`operator[]`](types.h.md#DeviceGroupList.operator), [`member_world_ranks_`](process_group_tpu.h.md#ProcessGroupTpu.member_world_ranks_), [`addressable_device_id_`](process_group_tpu.h.md#ProcessGroupTpu.addressable_device_id_), [`empty`](types.h.md#DeviceGroupList.empty), [`Normalize`](types.cc.md#Normalize), [`operator<=>`](types.h.md#DeviceGroupList.operator), [`pg_rank`](process_group_tpu_test.cc.md#ProcessGroupTpuTest_GatherSubgroupsViaNodeLocalStoreCrossNodeSubgroups_Test.TestBody.RankSubgroupSpec.pg_rank)

### <a id="DeviceGroupList"></a>`DeviceGroupList`
- def: [`csrc/distributed/types.h:49`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L49) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- doc: Represents a normalized list of TPU device groups for distributed collective
- signature: `class DeviceGroupList`
- members:
  - <a id="DeviceGroupList.DeviceGroupList"></a>`DeviceGroupList()` — [`L51`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L51)
  - `DeviceGroupList()` — [`L51`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L51)
  - <a id="DeviceGroupList.at"></a>`at(size_t index)` — [`L67`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L67)
  - <a id="DeviceGroupList.begin"></a>`begin()` — [`L69`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L69)
  - <a id="DeviceGroupList.cbegin"></a>`cbegin()` — [`L71`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L71)
  - <a id="DeviceGroupList.cend"></a>`cend()` — [`L72`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L72)
  - <a id="DeviceGroupList.empty"></a>`empty()` — [`L64`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L64)
  - <a id="DeviceGroupList.end"></a>`end()` — [`L70`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L70)
  - <a id="DeviceGroupList.fingerprint"></a>`fingerprint()` — [`L61`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L61)
  - <a id="DeviceGroupList.groups"></a>`groups()` — [`L59`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L59)
  - `operator<=>(const DeviceGroupList&)` — [`L74`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L74)
  - <a id="DeviceGroupList.operator"></a>`operator[](size_t index)` — [`L66`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L66)
  - <a id="DeviceGroupList.size"></a>`size()` — [`L63`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L63)
  - <a id="DeviceGroupList.fingerprint_"></a>`fingerprint_` — [`L83`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L83) — Fingerprint of `groups_`.
  - <a id="DeviceGroupList.groups_"></a>`groups_` — [`L81`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L81) — Invariant:
- uses (calls/refs, reference-scoped): [`operator<<`](types.cc.md#operator), [`FingerprintType`](../common/fingerprint_utils.h.md#FingerprintType), [`DeviceGroup`](types.h.md#DeviceGroup), [`DeviceGroupList`](types.cc.md#DeviceGroupList.DeviceGroupList), [`DeviceGroupList`](types.cc.md#DeviceGroupList.DeviceGroupList)
- used by: [`operator<<`](types.cc.md#operator), [`_reduce_scatter_base`](process_group_tpu.cc.md#ProcessGroupTpu._reduce_scatter_base), [`AllToAllBaseUnevenSplits`](process_group_tpu.cc.md#ProcessGroupTpu.AllToAllBaseUnevenSplits), [`ProcessGroupTpu`](process_group_tpu.cc.md#ProcessGroupTpu.ProcessGroupTpu), [`alltoall_base`](process_group_tpu.cc.md#ProcessGroupTpu.alltoall_base), [`AllGatherDim`](../ops/experimental/collectives/collectives_aten_kernels.cc.md#AllGatherDim), [`ReduceScatterDim`](../ops/experimental/collectives/collectives_aten_kernels.cc.md#ReduceScatterDim), [`GatherMemberWorldRanks`](process_group_tpu.cc.md#ProcessGroupTpu.GatherMemberWorldRanks), [`GatherSubgroupsViaNodeLocalStore`](process_group_tpu.cc.md#GatherSubgroupsViaNodeLocalStore), [`GatherAllSubgroups`](process_group_tpu.cc.md#ProcessGroupTpu.GatherAllSubgroups), [`device_assignment`](process_group_tpu.h.md#ProcessGroupTpu.device_assignment), [`DispatchCollectiveWithDim`](../ops/experimental/collectives/collectives_aten_kernels.cc.md#DispatchCollectiveWithDim), [`BuildDistributedReduceScatterShlo`](reduce_scatter.cc.md#BuildDistributedReduceScatterShlo), [`BuildDistributedAllGatherShlo`](allgather.cc.md#BuildDistributedAllGatherShlo), [`BuildDistributedAllReduceShlo`](allreduce.cc.md#BuildDistributedAllReduceShlo), [`OpDebugString`](process_group_tpu.h.md#ProcessGroupTpu.OpDebugString), [`BuildDistributedAllToAllShlo`](alltoall.cc.md#BuildDistributedAllToAllShlo), [`BuildReplicaGroupsAttr`](utils.cc.md#BuildReplicaGroupsAttr), [`DeviceGroupList`](types.cc.md#DeviceGroupList.DeviceGroupList), [`expected_local_subgroup`](process_group_tpu_test.cc.md#ProcessGroupTpuTest_GatherSubgroupsViaNodeLocalStoreCrossNodeSubgroups_Test.TestBody.RankSubgroupSpec.expected_local_subgroup), [`BuildDistributedAllToAllBaseShlo`](alltoall.cc.md#BuildDistributedAllToAllBaseShlo), [`Fingerprint64Impl`](../common/compilation.cc.md#Fingerprint64Impl), [`TestBody`](process_group_tpu_test.cc.md#ProcessGroupTpuTest_GatherSubgroupsViaNodeLocalStoreWorldSizedPreservesOrder_Test.TestBody), [`kStack`](allgather.h.md#AllGatherOutputMode.kStack), [`TestBody`](process_group_tpu_test.cc.md#ProcessGroupTpuTest_PermuteDeviceAssignmentForSubgroupsMultiSlicePermutedLauncherRanks_Test.TestBody), [`TestBody`](types_test.cc.md#DeviceGroupListTest_PreservesOrderWhenNormalizeIsFalse_Test.TestBody), [`TestBody`](types_test.cc.md#DeviceGroupListTest_SubgroupsFingerprintGoldenValues_Test.TestBody), [`BuildDistributedAllToAllBaseUnevenSplitsShlo`](alltoall.cc.md#BuildDistributedAllToAllBaseUnevenSplitsShlo), [`PermuteDeviceAssignmentForSubgroups`](process_group_tpu.cc.md#PermuteDeviceAssignmentForSubgroups), [`TestBody`](types_test.cc.md#DeviceGroupListTest_Normalization_Test.TestBody), [`DeviceGroupList`](types.cc.md#DeviceGroupList.DeviceGroupList), [`TestBody`](types_test.cc.md#DeviceGroupListTest_EqualityAndInequality_Test.TestBody), [`Normalize`](types.cc.md#Normalize), [`Compute`](types.h.md#Fingerprint64Impl.Compute), [`EncodeParamCacheKey`](types.h.md#EncodeParamCacheKey), [`device_assignment_`](process_group_tpu.h.md#ProcessGroupTpu.device_assignment_)

## Functions
- <a id="EncodeParamCacheKey"></a>`EncodeParamCacheKey(const DeviceGroupList& list)` — [`L88`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L88) — documented in [compilation-cache-key](../../../concepts/compilation-cache-key.md)

## Other members
- <a id="Fingerprint64Impl.Compute"></a>`Fingerprint64Impl.Compute` — [`L96`](../../../../../../raw/code/torch_tpu/csrc/distributed/types.h#L96)

