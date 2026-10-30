---
title: 'Module: csrc/distributed/process_group_tpu.cc'
type: catalog
provenance: extracted
module: csrc/distributed/process_group_tpu.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ProcessGroupTpu.alltoall: ProcessGroupTpu#alltoall(fd303876d84ed5e).
  ProcessGroupTpu.allgather: ProcessGroupTpu#allgather(9bdb1f065063b23).
  ProcessGroupTpu._allgather_base: ProcessGroupTpu#_allgather_base(d8a86914799b60f2).
  ProcessGroupTpu.allreduce: ProcessGroupTpu#allreduce(b8451028c4d3af85).
  ProcessGroupTpu.gather: ProcessGroupTpu#gather(40dbd29b985805f4).
  ProcessGroupTpu._reduce_scatter_base: ProcessGroupTpu#_reduce_scatter_base(20fb177ab3315925).
  ProcessGroupTpu.scatter: ProcessGroupTpu#scatter(5166e5ed87ff6867).
  ProcessGroupTpu.AllToAllBaseUnevenSplits: ProcessGroupTpu#AllToAllBaseUnevenSplits(9cae7e9b831b2b9f).
  ProcessGroupTpu.ProcessGroupTpu: ProcessGroupTpu#ProcessGroupTpu(885bbc13d8e829d5).
  ProcessGroupTpu.reduce_scatter: ProcessGroupTpu#reduce_scatter(31d8e60ae7730974).
  ProcessGroupTpu.broadcast: ProcessGroupTpu#broadcast(dc88ad78737fc8fe).
  ProcessGroupTpu.alltoall_base: ProcessGroupTpu#alltoall_base(abc8c5095d65c6b).
  ProcessGroupTpu.reduce_scatter_tensor_coalesced: ProcessGroupTpu#reduce_scatter_tensor_coalesced(6762cbfc988d184d).
  ProcessGroupTpu.barrier: ProcessGroupTpu#barrier(1d6036a510eddb64).
  ProcessGroupTpu.allgather_into_tensor_coalesced: ProcessGroupTpu#allgather_into_tensor_coalesced(2ed3a7927beb1b26).
  ProcessGroupTpu.AllToAllBaseEqualSplits: ProcessGroupTpu#AllToAllBaseEqualSplits(db1ef2dda4fe5e78).
  AllGatherViaNodeLocalStore: AllGatherViaNodeLocalStore(db9f2b8752f6a686).
  ProcessGroupTpu.InitializeRankToDeviceMappings: ProcessGroupTpu#InitializeRankToDeviceMappings(d9c77c711d2918ad).
  ValidateReduceScatterInputTensorShape: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/ValidateReduceScatterInputTensorShape(322904c416758605).'
  ProcessGroupTpu.experimental_recv: ProcessGroupTpu#experimental_recv(a61ad7c9e1c99b25).
  ProcessGroupTpu.GatherMemberWorldRanks: ProcessGroupTpu#GatherMemberWorldRanks(42cb28d6aa2911f6).
  ProcessGroupTpu.CrossHostReceiveBuffers: ProcessGroupTpu#CrossHostReceiveBuffers(33c4f15b1461ad4c).
  GatherSubgroupsViaNodeLocalStore: GatherSubgroupsViaNodeLocalStore(16a71fad783d15e3).
  ProcessGroupTpu.GatherAllSubgroups: ProcessGroupTpu#GatherAllSubgroups(dce6d2c18fb9a15).
  DecodeTable: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/DecodeTable(a87447c3905b868d).'
  ProcessGroupTpu.CrossHostSendBuffers: ProcessGroupTpu#CrossHostSendBuffers(348b7494abd367e4).
  DeserializeDeviceAttributes: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/DeserializeDeviceAttributes(c9844f106beeed10).'
  ProcessGroupTpu.experimental_send: ProcessGroupTpu#experimental_send(a61ad7c9e1c99b25).
  GetCrossHostTransferKey: GetCrossHostTransferKey(cfebf1f22b49f427).
  SynchronizeOutputOffsets: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/SynchronizeOutputOffsets(72ff9223ddaa46f0).'
  CallStore.R: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/CallStore(da4b2295fa017d26).R#'
  GetCollectiveSplitMode: GetCollectiveSplitMode(29d01e53e9d4eb62).
  ValidateTensorsUniformShape: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/ValidateTensorsUniformShape(4e96779e03b30f87).'
  ValidateAllToAllTensors: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/ValidateAllToAllTensors(a8a19bd5e20bf82d).'
  UnpackKeyAndValue: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/UnpackKeyAndValue(b7afd265e919db6d).'
  UnpackAllValues: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/UnpackAllValues(c52a178ac2900c88).'
  ValidateSplitSizesForAllToAllSingle: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/ValidateSplitSizesForAllToAllSingle(123181797bb34e27).'
  TpuWork.TpuWork: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/TpuWork#TpuWork(89324ea00f387dd5).'
  TpuWork.wait: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/TpuWork#wait(3e414d105f64b4eb).'
  GetNodeLocalStore: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/GetNodeLocalStore(581e8d625474bccb).'
  SetRaggedAllToAllParamKeys: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/SetRaggedAllToAllParamKeys(709108b6e4953fb8).'
  ComputeRaggedAllToAllOffsets: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/ComputeRaggedAllToAllOffsets(8527952982fca0a8).'
  ComputeRankToTopologyOrder: ComputeRankToTopologyOrder(a63ee4da3fe4146d).
  ComputeRankToTopologyOrder.TopologyKey: ComputeRankToTopologyOrder(a63ee4da3fe4146d).TopologyKey#
  ByteVector: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/ByteVector#'
  CallStore: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/CallStore(da4b2295fa017d26).'
  SerializeDeviceAttributes: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/SerializeDeviceAttributes(bc2c3f8b6a277ef7).'
  TpuWork: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/TpuWork#'
  ProcessGroupTpu.GetReplicaGroups: ProcessGroupTpu#GetReplicaGroups(117e1ce9274d5666).
  DeviceBufferRefDebugString: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/DeviceBufferRefDebugString(e48a05387d74dbbe).'
  PermuteDeviceAssignmentForSubgroups: PermuteDeviceAssignmentForSubgroups(48ac2c18b7ebd3dd).
  UnwrapPrefixStoreChain: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/UnwrapPrefixStoreChain(f87600c7d26c4f1a).'
  TpuWork.results_future_: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/TpuWork#results_future_.'
  WorldTopology: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/WorldTopology(9ebad1f2111fb61).'
  ProcessGroupTpu.shutdown: ProcessGroupTpu#shutdown(49f6e7a06ebc5aa8).
  GetGlobalRankToDeviceId: GetGlobalRankToDeviceId(a4ed58979733e8c7).
  ProcessGroupTpu.-ProcessGroupTpu: ProcessGroupTpu#`~ProcessGroupTpu`(ced63f7c635d850d).
  EncodeOkTable: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/EncodeOkTable(7864480464b09eea).'
  GetGlobalDeviceAttributes: GetGlobalDeviceAttributes(221979ca7d784ae2).
  GetGlobalRankToTopologyOrder: GetGlobalRankToTopologyOrder(221979ca7d784ae2).
  WorldTopologyState.rank_to_topo_order: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/WorldTopologyState#rank_to_topo_order.'
  WorldTopologyState.world_rank: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/WorldTopologyState#world_rank.'
  EncodeErrTable: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/EncodeErrTable(83d3572367d7e0a7).'
  NodeLocalStoreConfig: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/NodeLocalStoreConfig#'
  NodeLocalStoreConfig.local_world_size: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/NodeLocalStoreConfig#local_world_size.'
  WorldTopologyState.rank_to_device_id: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/WorldTopologyState#rank_to_device_id.'
  UnwrappedStoreChain.full_prefix: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/UnwrappedStoreChain#full_prefix.'
  IsUniformAllToAll: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/IsUniformAllToAll(adecfe2f564b2203).'
  ReduceScatterShapeMode.kStack: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/ReduceScatterShapeMode#kStack.'
  KeyAndValue.value: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/KeyAndValue#value.'
  NowMs: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/NowMs(da6335ded91d79c2).'
  PackValueList: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/PackValueList(7864480464b09eea).'
  TpuWork.getFuture: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/TpuWork#getFuture(b126dc7c1de90089).'
  RaggedAllToAllOffsets.recv_sizes: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/RaggedAllToAllOffsets#recv_sizes.'
  WorldTopologyState: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/WorldTopologyState#'
  GetCrossHostTransferDescriptorStoreKey: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/GetCrossHostTransferDescriptorStoreKey(cba8bec3477b06ab).'
  next_subgroup_gather_id: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/next_subgroup_gather_id.'
  ReduceScatterShapeMode: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/ReduceScatterShapeMode#'
  KeyAndValue.key: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/KeyAndValue#key.'
  KeyAndValue: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/KeyAndValue#'
  TpuWork.results_: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/TpuWork#results_.'
  kNodeLocalTableOkPrefix: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/kNodeLocalTableOkPrefix.'
  PrefixStoreAccessor.GetPrefix: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/PrefixStoreAccessor#GetPrefix(1540c4e286a0a988).'
  DescribeMissingKeys: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/DescribeMissingKeys(622b36d38c317e66).'
  IsEqualSplits: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/IsEqualSplits(718fc0b26c9eb689).'
  kNodeLocalTableErrPrefix: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/kNodeLocalTableErrPrefix.'
  UnwrappedStoreChain: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/UnwrappedStoreChain#'
  UnwrappedStoreChain.root_store: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/UnwrappedStoreChain#root_store.'
  RaggedAllToAllOffsets: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/RaggedAllToAllOffsets#'
  RaggedAllToAllOffsets.input_offsets: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/RaggedAllToAllOffsets#input_offsets.'
  RaggedAllToAllOffsets.output_offsets: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/RaggedAllToAllOffsets#output_offsets.'
  TpuWork.isCompleted: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/TpuWork#isCompleted(c9857a73d68e59ba).'
  TpuWork.isSuccess: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/TpuWork#isSuccess(50ce9a9e25b4a850).'
  TpuWork.operator: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/TpuWork#`operator=`(2e24b2bf30b73b39).'
  TpuWork.result: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/TpuWork#result(b126dc7c1de90089).'
  PackKeyAndValue: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/PackKeyAndValue(306a3f34aa691bd4).'
  RaggedAllToAllOffsets.send_sizes: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/RaggedAllToAllOffsets#send_sizes.'
  PrefixStoreAccessor: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/PrefixStoreAccessor#'
  NodeLocalStoreConfig.store: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/NodeLocalStoreConfig#store.'
  NodeLocalStoreConfig.local_rank: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/NodeLocalStoreConfig#local_rank.'
  ReduceScatterShapeMode.kConcat: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/ReduceScatterShapeMode#kConcat.'
  WorldTopologyState.device_attrs: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/WorldTopologyState#device_attrs.'
  TpuWork.abort: '`$anonymous_namespace_csrc/distributed/process_group_tpu.cc`/TpuWork#abort(49f6e7a06ebc5aa8).'
---
# Module: [`csrc/distributed/process_group_tpu.cc`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc)

## Classes
### <a id="ByteVector"></a>`ByteVector`
- def: [`csrc/distributed/process_group_tpu.cc:901`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L901)
- signature: `using ByteVector = std::vector<uint8_t>`
- used by: [`AllGatherViaNodeLocalStore`](process_group_tpu.cc.md#AllGatherViaNodeLocalStore), [`DecodeTable`](process_group_tpu.cc.md#DecodeTable), [`UnpackAllValues`](process_group_tpu.cc.md#UnpackAllValues), [`EncodeOkTable`](process_group_tpu.cc.md#EncodeOkTable), [`EncodeErrTable`](process_group_tpu.cc.md#EncodeErrTable), [`PackValueList`](process_group_tpu.cc.md#PackValueList)

### <a id="CallStore.R"></a>`CallStore.R`
- def: [`csrc/distributed/process_group_tpu.cc:874`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L874) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- signature: `using R = std::invoke_result_t<F>`
- uses (calls/refs, reference-scoped): [`NormalizeIfInsideBuildDirectory`](../common/macro_utils.cc.md#NormalizeIfInsideBuildDirectory), [`MaybeAddCppSourceLoc`](../common/status_builder.cc.md#MaybeAddCppSourceLoc), [`GetRootOpName`](../ops/python_context.cc.md#GetRootOpName), [`SetRootOpNamePayload`](../common/status_builder.cc.md#SetRootOpNamePayload), [`StatusBuilder`](../common/status_builder.h.md#StatusBuilder), [`operator<<`](../common/status_builder.h.md#StatusBuilder.operator), [`operator<<`](../ops/op_names.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`operator<<`](../common/cache_key.cc.md#operator), [`AdaptExternalErrorMessage`](../common/error_utils.cc.md#AdaptExternalErrorMessage), [`operator<<`](types.cc.md#operator), [`kUnavailable`](../common/error_utils.h.md#kUnavailable), [`kDeadlineExceeded`](../common/error_utils.h.md#kDeadlineExceeded)

### <a id="ComputeRankToTopologyOrder.TopologyKey"></a>`ComputeRankToTopologyOrder.TopologyKey`
- def: [`csrc/distributed/process_group_tpu.cc:781`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L781)
- doc: (slice_index, x, y, z, core_on_chip, id); defaults match
- signature: `using TopologyKey = std::tuple<int64_t, int64_t, int64_t, int64_t, int64_t, int64_t>`
- uses (calls/refs, reference-scoped): [`PjRtDeviceAttributes`](../pjrt/pjrt_state.h.md#PjRtDeviceAttributes), [`id`](../pjrt/pjrt_state.h.md#PjRtDeviceAttributes.id), [`coords`](../pjrt/pjrt_state.h.md#PjRtDeviceAttributes.coords), [`slice_index`](../pjrt/pjrt_state.h.md#PjRtDeviceAttributes.slice_index), [`core_on_chip`](../pjrt/pjrt_state.h.md#PjRtDeviceAttributes.core_on_chip), [`TopologyKey`](process_group_tpu.cc.md#ComputeRankToTopologyOrder.TopologyKey)

### <a id="KeyAndValue"></a>`KeyAndValue`
- def: [`csrc/distributed/process_group_tpu.cc:909`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L909)
- signature: `struct KeyAndValue`
- members:
  - <a id="KeyAndValue.key"></a>`key` — [`L910`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L910)
  - <a id="KeyAndValue.value"></a>`value` — [`L911`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L911)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`AllGatherViaNodeLocalStore`](process_group_tpu.cc.md#AllGatherViaNodeLocalStore), [`UnpackKeyAndValue`](process_group_tpu.cc.md#UnpackKeyAndValue)

### <a id="NodeLocalStoreConfig"></a>`NodeLocalStoreConfig`
- def: [`csrc/distributed/process_group_tpu.cc:1278`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1278)
- signature: `struct NodeLocalStoreConfig`
- members:
  - <a id="NodeLocalStoreConfig.local_rank"></a>`local_rank` — [`L1280`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1280)
  - <a id="NodeLocalStoreConfig.local_world_size"></a>`local_world_size` — [`L1281`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1281)
  - <a id="NodeLocalStoreConfig.store"></a>`store` — [`L1279`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1279)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ProcessGroupTpu`](process_group_tpu.cc.md#ProcessGroupTpu.ProcessGroupTpu), [`InitializeRankToDeviceMappings`](process_group_tpu.cc.md#ProcessGroupTpu.InitializeRankToDeviceMappings), [`GetNodeLocalStore`](process_group_tpu.cc.md#GetNodeLocalStore)

### <a id="PrefixStoreAccessor"></a>`PrefixStoreAccessor`  ·  implements/extends CustomClassHolder, PrefixStore, Store, intrusive_ptr_target
- def: [`csrc/distributed/process_group_tpu.cc:839`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L839)
- signature: `class PrefixStoreAccessor : public c10d::PrefixStore`
- members:
  - <a id="PrefixStoreAccessor.GetPrefix"></a>`GetPrefix(const c10d::PrefixStore* store)` — [`L841`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L841)
- used by: [`UnwrapPrefixStoreChain`](process_group_tpu.cc.md#UnwrapPrefixStoreChain)

### <a id="RaggedAllToAllOffsets"></a>`RaggedAllToAllOffsets`
- def: [`csrc/distributed/process_group_tpu.cc:355`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L355)
- doc: Offsets and slice sizes required for StableHLO ragged all-to-all custom
- signature: `struct RaggedAllToAllOffsets`
- members:
  - <a id="RaggedAllToAllOffsets.input_offsets"></a>`input_offsets` — [`L356`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L356)
  - <a id="RaggedAllToAllOffsets.output_offsets"></a>`output_offsets` — [`L358`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L358)
  - <a id="RaggedAllToAllOffsets.recv_sizes"></a>`recv_sizes` — [`L359`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L359)
  - <a id="RaggedAllToAllOffsets.send_sizes"></a>`send_sizes` — [`L357`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L357)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`AllToAllBaseUnevenSplits`](process_group_tpu.cc.md#ProcessGroupTpu.AllToAllBaseUnevenSplits), [`SynchronizeOutputOffsets`](process_group_tpu.cc.md#SynchronizeOutputOffsets), [`SetRaggedAllToAllParamKeys`](process_group_tpu.cc.md#SetRaggedAllToAllParamKeys), [`ComputeRaggedAllToAllOffsets`](process_group_tpu.cc.md#ComputeRaggedAllToAllOffsets)

### <a id="ReduceScatterShapeMode"></a>`ReduceScatterShapeMode`
- def: [`csrc/distributed/process_group_tpu.cc:207`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L207)
- signature: `enum class ReduceScatterShapeMode`
- members:
  - <a id="ReduceScatterShapeMode.kConcat"></a>`kConcat` — [`L208`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L208) — Input tensor is concatenated along dimension 0
  - <a id="ReduceScatterShapeMode.kStack"></a>`kStack` — [`L209`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L209) — Input tensor is stacked along a new dimension (at position 0)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`_reduce_scatter_base`](process_group_tpu.cc.md#ProcessGroupTpu._reduce_scatter_base), [`ValidateReduceScatterInputTensorShape`](process_group_tpu.cc.md#ValidateReduceScatterInputTensorShape)

### <a id="TpuWork"></a>`TpuWork`  ·  implements/extends CustomClassHolder, Work, intrusive_ptr_target
- def: [`csrc/distributed/process_group_tpu.cc:119`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L119)
- signature: `class TpuWork : public c10d::Work`
- members:
  - `TpuWork(std::vector<at::Tensor> result_tensors, int rank = -1, c10d::OpType op_type = c10d::OpType::UNKNOWN, c10::intrusive_ptr<c10::ivalue::Future> future = nullptr)` — [`L121`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L121)
  - `TpuWork(TpuWork&&)` — [`L149`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L149)
  - `TpuWork(const TpuWork&)` — [`L147`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L147) — This class is neither copyable nor movable.
  - <a id="TpuWork.TpuWork"></a>`TpuWork(std::vector<at::Tensor> result_tensors, int rank = -1, c10d::OpType op_type = c10d::OpType::UNKNOWN, c10::intrusive_ptr<c10::ivalue::Future> future = nullptr)` — [`L121`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L121)
  - <a id="TpuWork.abort"></a>`abort()` — [`L168`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L168)
  - <a id="TpuWork.getFuture"></a>`getFuture()` — [`L170`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L170)
  - `getFuture()` — [`L170`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L170)
  - <a id="TpuWork.isCompleted"></a>`isCompleted()` — [`L153`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L153) — NOTE: We implement TpuWork to match the PyTorch API surface.
  - <a id="TpuWork.isSuccess"></a>`isSuccess()` — [`L155`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L155)
  - <a id="TpuWork.operator"></a>`operator=(const TpuWork&)` — [`L148`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L148)
  - `operator=(TpuWork&&)` — [`L150`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L150)
  - `result()` — [`L166`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L166)
  - <a id="TpuWork.result"></a>`result()` — [`L166`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L166)
  - <a id="TpuWork.wait"></a>`wait(std::chrono::milliseconds timeout)` — [`L159`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L159)
  - <a id="TpuWork.results_"></a>`results_` — [`L175`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L175)
  - <a id="TpuWork.results_future_"></a>`results_future_` — [`L176`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L176)
- uses (calls/refs, reference-scoped): [`NormalizeIfInsideBuildDirectory`](../common/macro_utils.cc.md#NormalizeIfInsideBuildDirectory), [`MaybeAddCppSourceLoc`](../common/status_builder.cc.md#MaybeAddCppSourceLoc), [`GetRootOpName`](../ops/python_context.cc.md#GetRootOpName), [`SetRootOpNamePayload`](../common/status_builder.cc.md#SetRootOpNamePayload), [`StatusBuilder`](../common/status_builder.h.md#StatusBuilder), [`operator<<`](../common/status_builder.h.md#StatusBuilder.operator), [`TtError`](../common/error_utils.cc.md#TtError.TtError), [`ReturnIfErrorAdaptor`](../common/error_utils.h.md#ReturnIfErrorAdaptor), [`ReturnIfErrorAdaptor`](../common/error_utils.h.md#ReturnIfErrorAdaptor.ReturnIfErrorAdaptor), [`TtError`](../common/error_utils.h.md#TtError), [`StatusBuilder`](../common/status_builder.cc.md#StatusBuilder.StatusBuilder), [`operator=`](../common/error_utils.h.md#ThrowIfErrorAdapter.operator), [`ThrowIfErrorAdapter`](../common/error_utils.h.md#ThrowIfErrorAdapter.ThrowIfErrorAdapter), [`ThrowIfErrorAdapter`](../common/error_utils.h.md#ThrowIfErrorAdapter), [`ConsumeRequiringMessage`](../common/error_utils.h.md#ReturnIfErrorAdaptor.ConsumeRequiringMessage), [`kInternal`](../common/error_utils.h.md#kInternal), [`ProcessGroupTpu`](process_group_tpu.h.md#ProcessGroupTpu)
- used by: [`alltoall`](process_group_tpu.cc.md#ProcessGroupTpu.alltoall), [`allgather`](process_group_tpu.cc.md#ProcessGroupTpu.allgather), [`_allgather_base`](process_group_tpu.cc.md#ProcessGroupTpu._allgather_base), [`allreduce`](process_group_tpu.cc.md#ProcessGroupTpu.allreduce), [`gather`](process_group_tpu.cc.md#ProcessGroupTpu.gather), [`_reduce_scatter_base`](process_group_tpu.cc.md#ProcessGroupTpu._reduce_scatter_base), [`scatter`](process_group_tpu.cc.md#ProcessGroupTpu.scatter), [`reduce_scatter`](process_group_tpu.cc.md#ProcessGroupTpu.reduce_scatter), [`broadcast`](process_group_tpu.cc.md#ProcessGroupTpu.broadcast), [`alltoall_base`](process_group_tpu.cc.md#ProcessGroupTpu.alltoall_base), [`reduce_scatter_tensor_coalesced`](process_group_tpu.cc.md#ProcessGroupTpu.reduce_scatter_tensor_coalesced), [`barrier`](process_group_tpu.cc.md#ProcessGroupTpu.barrier), [`allgather_into_tensor_coalesced`](process_group_tpu.cc.md#ProcessGroupTpu.allgather_into_tensor_coalesced), [`experimental_recv`](process_group_tpu.cc.md#ProcessGroupTpu.experimental_recv), [`experimental_send`](process_group_tpu.cc.md#ProcessGroupTpu.experimental_send)

### <a id="UnwrappedStoreChain"></a>`UnwrappedStoreChain`
- def: [`csrc/distributed/process_group_tpu.cc:846`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L846)
- signature: `struct UnwrappedStoreChain`
- members:
  - <a id="UnwrappedStoreChain.full_prefix"></a>`full_prefix` — [`L848`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L848)
  - <a id="UnwrappedStoreChain.root_store"></a>`root_store` — [`L847`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L847)
- used by: [`GatherSubgroupsViaNodeLocalStore`](process_group_tpu.cc.md#GatherSubgroupsViaNodeLocalStore), [`UnwrapPrefixStoreChain`](process_group_tpu.cc.md#UnwrapPrefixStoreChain)

### <a id="WorldTopologyState"></a>`WorldTopologyState`
- def: [`csrc/distributed/process_group_tpu.cc:749`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L749)
- signature: `struct WorldTopologyState`
- members:
  - <a id="WorldTopologyState.device_attrs"></a>`device_attrs` — [`L750`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L750)
  - <a id="WorldTopologyState.rank_to_device_id"></a>`rank_to_device_id` — [`L751`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L751) — INT_VEC_OK
  - <a id="WorldTopologyState.rank_to_topo_order"></a>`rank_to_topo_order` — [`L754`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L754) — INT_VEC_OK
  - <a id="WorldTopologyState.world_rank"></a>`world_rank` — [`L755`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L755)
- uses (calls/refs, reference-scoped): [`PjRtDeviceAttributes`](../pjrt/pjrt_state.h.md#PjRtDeviceAttributes)
- used by: [`ProcessGroupTpu`](process_group_tpu.cc.md#ProcessGroupTpu.ProcessGroupTpu), [`InitializeRankToDeviceMappings`](process_group_tpu.cc.md#ProcessGroupTpu.InitializeRankToDeviceMappings), [`GatherMemberWorldRanks`](process_group_tpu.cc.md#ProcessGroupTpu.GatherMemberWorldRanks), [`GatherAllSubgroups`](process_group_tpu.cc.md#ProcessGroupTpu.GatherAllSubgroups), [`WorldTopology`](process_group_tpu.cc.md#WorldTopology), [`GetGlobalRankToDeviceId`](process_group_tpu.cc.md#GetGlobalRankToDeviceId), [`GetGlobalDeviceAttributes`](process_group_tpu.cc.md#GetGlobalDeviceAttributes), [`GetGlobalRankToTopologyOrder`](process_group_tpu.cc.md#GetGlobalRankToTopologyOrder)

## Functions
- `AllGatherViaNodeLocalStore(c10d::Store* world_store, c10d::Store* local_store, int64_t local_rank, int64_t local_world_size, std::string_view my_key, std::string_view my_value, const std::vector<std::string>& peer_keys)` — [`L1054`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1054) — Protocol. All keys are scoped by `scope_key` = "<peer_keys[0]>:<num_peers>".
- <a id="AllGatherViaNodeLocalStore"></a>`AllGatherViaNodeLocalStore(c10d::Store* world_store, c10d::Store* local_store, int64_t local_rank, int64_t local_world_size, std::string_view my_key, std::string_view my_value, const std::vector<std::string>& peer_keys)` — [`L1054`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1054) — Protocol. All keys are scoped by `scope_key` = "<peer_keys[0]>:<num_peers>". — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="CallStore"></a>`CallStore(std::string_view op, F&& f)` — [`L873`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L873) — Runs `f`, a call into c10d::Store, converting any exception it throws (e.g.
- <a id="ComputeRaggedAllToAllOffsets"></a>`ComputeRaggedAllToAllOffsets(c10d::Store* store, int rank, uint64_t seq, absl::Span<const int32_t> send_sizes, absl::Span<const int32_t> recv_sizes, int32_t input_buffer_size, int32_t output_buffer_size)` — [`L484`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L484) — Computes local input offsets via prefix sums over send_sizes, computes local
- `ComputeRankToTopologyOrder(absl::Span<const PjRtDeviceAttributes> device_attrs)` — [`L777`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L777) — Returns `order` such that `order[r]` is world rank r's position when all
- <a id="ComputeRankToTopologyOrder"></a>`ComputeRankToTopologyOrder(absl::Span<const PjRtDeviceAttributes> device_attrs)` — [`L777`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L777) — Returns `order` such that `order[r]` is world rank r's position when all
- <a id="DecodeTable"></a>`DecodeTable(absl::Span<const uint8_t> bytes, size_t expected_count)` — [`L989`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L989) — Decodes a table published by the collector. Returns an error if the
- `DecodeTable(absl::Span<const uint8_t> bytes, size_t expected_count)` — [`L989`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L989) — Decodes a table published by the collector. Returns an error if the
- <a id="DescribeMissingKeys"></a>`DescribeMissingKeys(const std::vector<std::string>& peer_keys, const std::vector<bool>& filled, size_t max_keys)` — [`L1014`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1014) — Returns up to `max_keys` of the peer keys that are not yet filled.
- `DescribeMissingKeys(const std::vector<std::string>& peer_keys, const std::vector<bool>& filled, size_t max_keys)` — [`L1014`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1014) — Returns up to `max_keys` of the peer keys that are not yet filled.
- <a id="DeserializeDeviceAttributes"></a>`DeserializeDeviceAttributes(std::string_view payload)` — [`L573`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L573)
- <a id="DeviceBufferRefDebugString"></a>`DeviceBufferRefDebugString(const at::Tensor& input)` — [`L181`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L181)
- <a id="EncodeErrTable"></a>`EncodeErrTable(std::string_view message)` — [`L982`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L982)
- `EncodeErrTable(std::string_view message)` — [`L982`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L982)
- `EncodeOkTable(absl::Span<const ByteVector> values)` — [`L974`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L974)
- <a id="EncodeOkTable"></a>`EncodeOkTable(absl::Span<const ByteVector> values)` — [`L974`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L974)
- `GatherSubgroupsViaNodeLocalStore(c10d::Store* store, c10d::Store* local_store, int64_t local_rank, int64_t local_world_size, int64_t pg_rank, int64_t pg_size, int64_t world_rank, absl::Span<const int64_t> global_rank_to_device_id, absl::Span<const int64_t> global_rank_to_topo_order, int64_t gather_id, DeviceGroup& out_member_world_ranks, DeviceGroupList& out_subgroup_member_world_ranks)` — [`L1340`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1340) — Exchanges `(subgroup_prefix, pg_rank, world_rank)` across all `world_size`
- <a id="GatherSubgroupsViaNodeLocalStore"></a>`GatherSubgroupsViaNodeLocalStore(c10d::Store* store, c10d::Store* local_store, int64_t local_rank, int64_t local_world_size, int64_t pg_rank, int64_t pg_size, int64_t world_rank, absl::Span<const int64_t> global_rank_to_device_id, absl::Span<const int64_t> global_rank_to_topo_order, int64_t gather_id, DeviceGroup& out_member_world_ranks, DeviceGroupList& out_subgroup_member_world_ranks)` — [`L1340`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1340) — Exchanges `(subgroup_prefix, pg_rank, world_rank)` across all `world_size` — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="GetCollectiveSplitMode"></a>`GetCollectiveSplitMode()` — [`L530`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L530) — Returns the OpSplitMode to use for collectives. — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="GetCrossHostTransferDescriptorStoreKey"></a>`GetCrossHostTransferDescriptorStoreKey(xla::CrossHostTransferKey key)` — [`L553`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L553)
- <a id="GetCrossHostTransferKey"></a>`GetCrossHostTransferKey(int64_t src_device_id, int64_t dst_device_id, int tag, size_t tensor_index)` — [`L542`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L542) — Returns a cross-host transfer key computed deterministically and stably — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="GetGlobalDeviceAttributes"></a>`GetGlobalDeviceAttributes()` — [`L765`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L765) — Returns global device attributes and rank-to-device-id mapping.
- `GetGlobalDeviceAttributes()` — [`L765`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L765) — Returns global device attributes and rank-to-device-id mapping.
- <a id="GetGlobalRankToDeviceId"></a>`GetGlobalRankToDeviceId()` — [`L769`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L769)
- `GetGlobalRankToDeviceId()` — [`L769`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L769)
- <a id="GetGlobalRankToTopologyOrder"></a>`GetGlobalRankToTopologyOrder()` — [`L773`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L773) — Returns, for each world rank r, its position in the physical-topology order
- `GetGlobalRankToTopologyOrder()` — [`L773`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L773) — Returns, for each world rank r, its position in the physical-topology order
- <a id="GetNodeLocalStore"></a>`GetNodeLocalStore(int64_t world_size)` — [`L1288`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1288) — Returns the node-local store used by AllGatherViaNodeLocalStore. Returns a
- <a id="IsEqualSplits"></a>`IsEqualSplits(c10::IntArrayRef split_sizes)` — [`L281`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L281)
- `IsUniformAllToAll(const std::vector<at::Tensor>& output_tensors, const std::vector<at::Tensor>& input_tensors)` — [`L341`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L341) — Returns true if all input and output tensors have identical shapes, enabling
- <a id="IsUniformAllToAll"></a>`IsUniformAllToAll(const std::vector<at::Tensor>& output_tensors, const std::vector<at::Tensor>& input_tensors)` — [`L341`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L341) — Returns true if all input and output tensors have identical shapes, enabling
- <a id="NowMs"></a>`NowMs()` — [`L833`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L833)
- `PackKeyAndValue(std::string_view key, std::string_view value)` — [`L903`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L903)
- <a id="PackKeyAndValue"></a>`PackKeyAndValue(std::string_view key, std::string_view value)` — [`L903`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L903)
- <a id="PackValueList"></a>`PackValueList(absl::Span<const ByteVector> values)` — [`L936`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L936)
- `PackValueList(absl::Span<const ByteVector> values)` — [`L936`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L936)
- `PermuteDeviceAssignmentForSubgroups(const DeviceGroupList& subgroup_member_world_ranks, absl::Span<const int64_t> rank_to_device_id, std::vector<int64_t>& device_assignment, DeviceGroupList& replica_groups)` — [`L809`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L809) — Permutes the world device_assignment to match the flattened order of
- <a id="PermuteDeviceAssignmentForSubgroups"></a>`PermuteDeviceAssignmentForSubgroups(const DeviceGroupList& subgroup_member_world_ranks, absl::Span<const int64_t> rank_to_device_id, std::vector<int64_t>& device_assignment, DeviceGroupList& replica_groups)` — [`L809`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L809) — Permutes the world device_assignment to match the flattened order of
- <a id="SerializeDeviceAttributes"></a>`SerializeDeviceAttributes(const PjRtDeviceAttributes& attrs)` — [`L560`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L560)
- <a id="SetRaggedAllToAllParamKeys"></a>`SetRaggedAllToAllParamKeys(OpParamCacheKeys& param_keys, const RaggedAllToAllOffsets& offsets)` — [`L517`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L517) — Populates kernel cache parameter keys for ragged all-to-all collectives.
- `SynchronizeOutputOffsets(c10d::Store* store, int my_rank, uint64_t seq, absl::Span<const int32_t> local_output_offsets, absl::Span<const int32_t> send_sizes, absl::Span<const int32_t> recv_sizes, int32_t input_buffer_size, int32_t output_buffer_size)` — [`L387`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L387) — Synchronizes destination output offsets across all ranks via c10d::Store.
- <a id="SynchronizeOutputOffsets"></a>`SynchronizeOutputOffsets(c10d::Store* store, int my_rank, uint64_t seq, absl::Span<const int32_t> local_output_offsets, absl::Span<const int32_t> send_sizes, absl::Span<const int32_t> recv_sizes, int32_t input_buffer_size, int32_t output_buffer_size)` — [`L387`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L387) — Synchronizes destination output offsets across all ranks via c10d::Store. — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="UnpackAllValues"></a>`UnpackAllValues(absl::Span<const uint8_t> packed)` — [`L946`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L946)
- `UnpackAllValues(absl::Span<const uint8_t> packed)` — [`L946`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L946)
- <a id="UnpackKeyAndValue"></a>`UnpackKeyAndValue(absl::Span<const uint8_t> packed)` — [`L914`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L914)
- <a id="UnwrapPrefixStoreChain"></a>`UnwrapPrefixStoreChain(c10d::Store* store)` — [`L851`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L851)
- `ValidateAllToAllTensors(const std::vector<at::Tensor>& output_tensors, const std::vector<at::Tensor>& input_tensors)` — [`L297`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L297) — Validates tensor list invariants for all-to-all: matching process group
- <a id="ValidateAllToAllTensors"></a>`ValidateAllToAllTensors(const std::vector<at::Tensor>& output_tensors, const std::vector<at::Tensor>& input_tensors)` — [`L297`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L297) — Validates tensor list invariants for all-to-all: matching process group — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ValidateReduceScatterInputTensorShape"></a>`ValidateReduceScatterInputTensorShape(at::Tensor& output, at::Tensor& input, size_t process_group_size)` — [`L214`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L214) — Helper to validate the reduce-scatter input tensor shape, and determine if — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ValidateSplitSizesForAllToAllSingle"></a>`ValidateSplitSizesForAllToAllSingle(c10::IntArrayRef split_sizes, const at::Tensor& tensor, size_t group_size)` — [`L253`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L253) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- `ValidateTensorsUniformShape(const std::vector<at::Tensor>& tensors)` — [`L189`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L189)
- <a id="ValidateTensorsUniformShape"></a>`ValidateTensorsUniformShape(const std::vector<at::Tensor>& tensors)` — [`L189`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L189) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="WorldTopology"></a>`WorldTopology()` — [`L758`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L758)

## Module values
- <a id="kNodeLocalTableErrPrefix"></a>`kNodeLocalTableErrPrefix` — [`L972`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L972)
- <a id="kNodeLocalTableOkPrefix"></a>`kNodeLocalTableOkPrefix` — [`L971`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L971) — Prefixes of the table published by the AllGatherViaNodeLocalStore collector.
- <a id="next_subgroup_gather_id"></a>`next_subgroup_gather_id` — [`L1336`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1336)

## Other members
- `allgather` — [`L1959`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1959)
- `alltoall` — [`L2652`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2652)
- `_allgather_base` — [`L2053`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2053)
- `GatherAllSubgroups` — [`L1567`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1567)
- `reduce_scatter_tensor_coalesced` — [`L2450`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2450)
- `barrier` — [`L2820`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2820)
- `reduce_scatter` — [`L2336`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2336)
- `_reduce_scatter_base` — [`L2385`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2385)
- `GatherMemberWorldRanks` — [`L1498`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1498)
- `ProcessGroupTpu` — [`L1675`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1675)
- `CrossHostSendBuffers` — [`L604`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L604)
- `CrossHostReceiveBuffers` — [`L673`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L673)
- `gather` — [`L2187`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2187)
- `allgather_into_tensor_coalesced` — [`L2161`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2161)
- `experimental_send` — [`L1886`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1886)
- `scatter` — [`L2265`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2265)
- `alltoall_base` — [`L2478`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2478)
- `broadcast` — [`L1834`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1834)
- `allreduce` — [`L1785`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1785)
- `experimental_recv` — [`L1920`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1920)
- <a id="ProcessGroupTpu.-ProcessGroupTpu"></a>`ProcessGroupTpu.-ProcessGroupTpu` — [`L1774`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1774)
- <a id="ProcessGroupTpu.AllToAllBaseEqualSplits"></a>`ProcessGroupTpu.AllToAllBaseEqualSplits` — [`L2528`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2528) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu.AllToAllBaseUnevenSplits"></a>`ProcessGroupTpu.AllToAllBaseUnevenSplits` — [`L2555`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2555) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu.CrossHostReceiveBuffers"></a>`ProcessGroupTpu.CrossHostReceiveBuffers` — [`L673`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L673)
- <a id="ProcessGroupTpu.CrossHostSendBuffers"></a>`ProcessGroupTpu.CrossHostSendBuffers` — [`L604`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L604) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu.GatherAllSubgroups"></a>`ProcessGroupTpu.GatherAllSubgroups` — [`L1567`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1567) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu.GatherMemberWorldRanks"></a>`ProcessGroupTpu.GatherMemberWorldRanks` — [`L1498`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1498) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu.GetReplicaGroups"></a>`ProcessGroupTpu.GetReplicaGroups` — [`L1781`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1781)
- <a id="ProcessGroupTpu.InitializeRankToDeviceMappings"></a>`ProcessGroupTpu.InitializeRankToDeviceMappings` — [`L1448`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1448) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu.ProcessGroupTpu"></a>`ProcessGroupTpu.ProcessGroupTpu` — [`L1675`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1675) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu._allgather_base"></a>`ProcessGroupTpu._allgather_base` — [`L2053`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2053) — documented in [op-names-and-python-context](../../../concepts/op-names-and-python-context.md)
- <a id="ProcessGroupTpu._reduce_scatter_base"></a>`ProcessGroupTpu._reduce_scatter_base` — [`L2385`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2385) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu.allgather"></a>`ProcessGroupTpu.allgather` — [`L1959`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1959) — documented in [op-names-and-python-context](../../../concepts/op-names-and-python-context.md)
- <a id="ProcessGroupTpu.allgather_into_tensor_coalesced"></a>`ProcessGroupTpu.allgather_into_tensor_coalesced` — [`L2161`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2161) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu.allreduce"></a>`ProcessGroupTpu.allreduce` — [`L1785`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1785) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu.alltoall"></a>`ProcessGroupTpu.alltoall` — [`L2652`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2652) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="ProcessGroupTpu.alltoall_base"></a>`ProcessGroupTpu.alltoall_base` — [`L2478`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2478) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu.barrier"></a>`ProcessGroupTpu.barrier` — [`L2820`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2820) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu.broadcast"></a>`ProcessGroupTpu.broadcast` — [`L1834`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1834) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu.experimental_recv"></a>`ProcessGroupTpu.experimental_recv` — [`L1920`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1920) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu.experimental_send"></a>`ProcessGroupTpu.experimental_send` — [`L1886`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1886)
- <a id="ProcessGroupTpu.gather"></a>`ProcessGroupTpu.gather` — [`L2187`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2187) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu.reduce_scatter"></a>`ProcessGroupTpu.reduce_scatter` — [`L2336`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2336) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu.reduce_scatter_tensor_coalesced"></a>`ProcessGroupTpu.reduce_scatter_tensor_coalesced` — [`L2450`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2450) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu.scatter"></a>`ProcessGroupTpu.scatter` — [`L2265`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L2265) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="ProcessGroupTpu.shutdown"></a>`ProcessGroupTpu.shutdown` — [`L1772`](../../../../../../raw/code/torch_tpu/csrc/distributed/process_group_tpu.cc#L1772)

