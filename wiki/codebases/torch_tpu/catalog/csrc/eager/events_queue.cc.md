---
title: 'Module: csrc/eager/events_queue.cc'
type: catalog
provenance: extracted
module: csrc/eager/events_queue.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  RecordDeferredOpCreated: RecordDeferredOpCreated(ade22ae6fe590573).
  RecordNewDataPtrCreated: RecordNewDataPtrCreated(bca6aa9c539f6ace).
  ClearAllStreams: ClearAllStreams(49f6e7a06ebc5aa8).
  PrepareSnapshotMaterializations: PrepareSnapshotMaterializations(3e733a14d0c4c199).
  EventSnapshot.Record: EventSnapshot#Record(ce57bf227c8ea4).
  EventSnapshot.ElapsedTime: EventSnapshot#ElapsedTime(faf69954c98ca7bc).
  StreamState.DeferredOpEvent.FromDeferredOp: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#DeferredOpEvent#FromDeferredOp(e12dd69c0f5fc4b2).'
  PrepareTraversals: '`$anonymous_namespace_csrc/eager/events_queue.cc`/PrepareTraversals(3dffae08ed22c57e).'
  StreamState.Clear: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#Clear(49f6e7a06ebc5aa8).'
  GetCompilationMode: GetCompilationMode(bc5df5ec6d578ca0).
  EventSnapshot.EventSnapshot: EventSnapshot#EventSnapshot(6447a03e2a33272c).
  RecordDeviceSnapshots: RecordDeviceSnapshots(9975faeba7385bd5).
  RecordAsyncDeviceToHost: RecordAsyncDeviceToHost(6447a03e2a33272c).
  ProcessDeferredOpEvent: '`$anonymous_namespace_csrc/eager/events_queue.cc`/ProcessDeferredOpEvent(3c5be55284337007).'
  StreamState.RecordDeferredOpAndDetectRepetition: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#RecordDeferredOpAndDetectRepetition(9fafde8ebd70833).'
  StreamState.RequestEventSnapshotLocked: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#RequestEventSnapshotLocked(50bd19a09392433c).'
  EventSnapshot.Synchronize: EventSnapshot#Synchronize(654e21e32f56641d).
  CreateNoOpDependency: '`$anonymous_namespace_csrc/eager/events_queue.cc`/CreateNoOpDependency(3b4821195046b4ae).'
  GetOpUsage: '`$anonymous_namespace_csrc/eager/events_queue.cc`/GetOpUsage(4772b7a28accdd5f).'
  RecordAsyncHostToDevice: RecordAsyncHostToDevice(bca6aa9c539f6ace).
  EventSnapshot.OkCallback: EventSnapshot#OkCallback(4a651ddb1401e48b).
  RecordDataPtrDestroyed: RecordDataPtrDestroyed(bca6aa9c539f6ace).
  FinishTraversal: '`$anonymous_namespace_csrc/eager/events_queue.cc`/FinishTraversal(ced7719f238d998c).'
  EventSnapshot.CompletionTime: EventSnapshot#CompletionTime(2641435ec913c0a2).
  EventSnapshot.Query: EventSnapshot#Query(917a2cf8c155f314).
  StreamState.RecordCompiledExecutionTask: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#RecordCompiledExecutionTask(2a493f864e2573ed).'
  RecordCompiledExecutionTask: RecordCompiledExecutionTask(f13630165518fa92).
  StreamState.events_queue_: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#events_queue_.'
  ResetRepeatedOpsHeuristicState: ResetRepeatedOpsHeuristicState(49f6e7a06ebc5aa8).
  RecordDeferredOpAndDetectRepetition: RecordDeferredOpAndDetectRepetition(9fafde8ebd70833).
  StreamState.CheckLastRepeatedSequence: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#CheckLastRepeatedSequence(319e7918454605be).'
  StreamState: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#'
  StreamState.FindRepeatedSequence: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#FindRepeatedSequence(f7e21917e59627ec).'
  StreamState.GetSnapshotEvents: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#GetSnapshotEvents(b126dc7c1de90089).'
  StreamState.mu_: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#mu_.'
  StreamState.futures_: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#futures_.'
  StreamState.RecordDataPtrDestroyed: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#RecordDataPtrDestroyed(bca6aa9c539f6ace).'
  StreamState.RecordNewDataPtrCreated: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#RecordNewDataPtrCreated(bca6aa9c539f6ace).'
  StreamState.RecordRepeatedHashPattern: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#RecordRepeatedHashPattern(1624ee8275b10bda).'
  StreamState.DeferredOpEvent: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#DeferredOpEvent#'
  DeviceState.GetOrCreateStreamState: '`$anonymous_namespace_csrc/eager/events_queue.cc`/DeviceState#GetOrCreateStreamState(4e07776513961dbc).'
  StreamState.RequestEventSnapshot: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#RequestEventSnapshot(4cb384e93867542).'
  StreamState.ResetRepeatedOpsHeuristicState: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#ResetRepeatedOpsHeuristicState(49f6e7a06ebc5aa8).'
  StreamState.CheckLastRepeatedSequenceResult.kPatternBreak: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#CheckLastRepeatedSequenceResult#kPatternBreak.'
  SetCorePinningMode: SetCorePinningMode(5bf44884b565e0db).
  GetOrCreateStreamState: '`$anonymous_namespace_csrc/eager/events_queue.cc`/GetOrCreateStreamState(acd48778b15ba044).'
  DeviceState.ResetRepeatedOpsHeuristicState: '`$anonymous_namespace_csrc/eager/events_queue.cc`/DeviceState#ResetRepeatedOpsHeuristicState(49f6e7a06ebc5aa8).'
  StreamState.RecordDeferredOpCreated: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#RecordDeferredOpCreated(ade22ae6fe590573).'
  DeviceState.stream_states: '`$anonymous_namespace_csrc/eager/events_queue.cc`/DeviceState#stream_states.'
  OpUsage: '`$anonymous_namespace_csrc/eager/events_queue.cc`/OpUsage#'
  GetStreamFor: '`$anonymous_namespace_csrc/eager/events_queue.cc`/GetStreamFor(6cbc45f5bc2b97b5).'
  DeviceState.GetAllStreamStates: '`$anonymous_namespace_csrc/eager/events_queue.cc`/DeviceState#GetAllStreamStates(8c2a9f4d10449bd3).'
  DeviceState.Clear: '`$anonymous_namespace_csrc/eager/events_queue.cc`/DeviceState#Clear(49f6e7a06ebc5aa8).'
  NodeMatcher.NodeMatcher: '`$anonymous_namespace_csrc/eager/events_queue.cc`/NodeMatcher#NodeMatcher(ba350244703120d6).'
  StreamState.live_nodes_: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#live_nodes_.'
  StreamState.core_pinning_mode_: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#core_pinning_mode_.'
  GetStreamStates: '`$anonymous_namespace_csrc/eager/events_queue.cc`/GetStreamStates(44ec8244686e8daf).'
  StreamStates.Clear: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamStates#Clear(49f6e7a06ebc5aa8).'
  SnapshotChainReleaser.Release: '`$anonymous_namespace_csrc/eager/events_queue.cc`/SnapshotChainReleaser#Release(ad83fc84facf9201).'
  NodeMatcher.contains: '`$anonymous_namespace_csrc/eager/events_queue.cc`/NodeMatcher#contains(3c581e08a9223ed4).'
  MarkStreamActive: '`$anonymous_namespace_csrc/eager/events_queue.cc`/MarkStreamActive(3098f2299b4ea259).'
  StreamState.repetition_i_: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#repetition_i_.'
  StreamState.repetition_hashes_: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#repetition_hashes_.'
  ReleaseNextSnapshot: '`$anonymous_namespace_csrc/eager/events_queue.cc`/ReleaseNextSnapshot(ad83fc84facf9201).'
  DefinedNodeMap: '`$anonymous_namespace_csrc/eager/events_queue.cc`/DefinedNodeMap#'
  StreamState.StreamEvent: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#StreamEvent#'
  StreamState.MarkActive: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#MarkActive(5f176e66f8d556a4).'
  NodeMatcher.small_nodes_: '`$anonymous_namespace_csrc/eager/events_queue.cc`/NodeMatcher#small_nodes_.'
  StreamState.JoinFutures: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#JoinFutures(d5c73fb4e34f1151).'
  StreamState.DeferredOpEvent.lock: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#DeferredOpEvent#lock(e2908283bbae60d1).'
  StreamStates.GetDeviceState: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamStates#GetDeviceState(e2407a42bff1172f).'
  StreamState.CheckLastRepeatedSequenceResult: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#CheckLastRepeatedSequenceResult#'
  StreamState.DeferredOpEvent.deferred_op_hash: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#DeferredOpEvent#deferred_op_hash.'
  DeviceState: '`$anonymous_namespace_csrc/eager/events_queue.cc`/DeviceState#'
  NodeMatcher.single_node_: '`$anonymous_namespace_csrc/eager/events_queue.cc`/NodeMatcher#single_node_.'
  DeviceState.mutex: '`$anonymous_namespace_csrc/eager/events_queue.cc`/DeviceState#mutex.'
  GetDeviceStreamStates: '`$anonymous_namespace_csrc/eager/events_queue.cc`/GetDeviceStreamStates(8bcc8e5e37f2ab65).'
  StreamState.EventSnapshotRequest: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#EventSnapshotRequest#'
  DeviceState.default_stream_state: '`$anonymous_namespace_csrc/eager/events_queue.cc`/DeviceState#default_stream_state.'
  StreamState.SetCorePinningMode: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#SetCorePinningMode(3895345c27d01d54).'
  OpUsage.kOutput: '`$anonymous_namespace_csrc/eager/events_queue.cc`/OpUsage#kOutput.'
  StreamState.EventSnapshotRequest.materialization_settings: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#EventSnapshotRequest#materialization_settings.'
  StreamState.EventSnapshotRequest.must_materialize: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#EventSnapshotRequest#must_materialize.'
  StreamState.DeferredOpEvent.no_side_effects: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#DeferredOpEvent#no_side_effects.'
  StreamStates.device_states: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamStates#device_states.'
  SnapshotChainReleaser.pending_: '`$anonymous_namespace_csrc/eager/events_queue.cc`/SnapshotChainReleaser#pending_.'
  SnapshotChainReleaser.releasing_: '`$anonymous_namespace_csrc/eager/events_queue.cc`/SnapshotChainReleaser#releasing_.'
  StreamStates: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamStates#'
  StreamState.EventSnapshotRequest.execution_task: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#EventSnapshotRequest#execution_task.'
  kMaxTorchDevices: '`$anonymous_namespace_csrc/eager/events_queue.cc`/kMaxTorchDevices.'
  StreamState.EventSnapshotRequest.futures: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#EventSnapshotRequest#futures.'
  NodeMatcher.large_nodes_: '`$anonymous_namespace_csrc/eager/events_queue.cc`/NodeMatcher#large_nodes_.'
  StreamState.DeferredOpEvent.side_effects: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#DeferredOpEvent#side_effects.'
  NodeMatcher: '`$anonymous_namespace_csrc/eager/events_queue.cc`/NodeMatcher#'
  SnapshotChainReleaser.mu_: '`$anonymous_namespace_csrc/eager/events_queue.cc`/SnapshotChainReleaser#mu_.'
  OpUsage.kUsed: '`$anonymous_namespace_csrc/eager/events_queue.cc`/OpUsage#kUsed.'
  StreamState.EventSnapshotRequest.live_nodes: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#EventSnapshotRequest#live_nodes.'
  StreamState.core_pinning_mode: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#core_pinning_mode(288fbb0adaf44ad9).'
  PruneCompletedFutures: '`$anonymous_namespace_csrc/eager/events_queue.cc`/PruneCompletedFutures(3e56f9cebe35d849).'
  OpUsage.kUnused: '`$anonymous_namespace_csrc/eager/events_queue.cc`/OpUsage#kUnused.'
  StreamState.CheckLastRepeatedSequenceResult.kContinueWaiting: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#CheckLastRepeatedSequenceResult#kContinueWaiting.'
  StreamState.EventSnapshotRequest.snapshot_promise: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#EventSnapshotRequest#snapshot_promise.'
  StreamState.CheckLastRepeatedSequenceResult.kRepetitionComplete: '`$anonymous_namespace_csrc/eager/events_queue.cc`/StreamState#CheckLastRepeatedSequenceResult#kRepetitionComplete.'
  SnapshotChainReleaser: '`$anonymous_namespace_csrc/eager/events_queue.cc`/SnapshotChainReleaser#'
  kMinRepeatedSubsequenceLength: '`$anonymous_namespace_csrc/eager/events_queue.cc`/kMinRepeatedSubsequenceLength.'
  kMaxRepeatedSubsequenceLength: '`$anonymous_namespace_csrc/eager/events_queue.cc`/kMaxRepeatedSubsequenceLength.'
  kMinRepetitionCount: '`$anonymous_namespace_csrc/eager/events_queue.cc`/kMinRepetitionCount.'
---
# Module: [`csrc/eager/events_queue.cc`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc)

## Classes
### <a id="DefinedNodeMap"></a>`DefinedNodeMap`
- def: [`csrc/eager/events_queue.cc:752`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L752)
- signature: `using DefinedNodeMap = absl::flat_hash_map<const DeviceBufferList*, OpUsage>`
- uses (calls/refs, reference-scoped): [`DeviceBufferList`](device_buffer.h.md#DeviceBufferList), [`OpUsage`](events_queue.cc.md#OpUsage)
- used by: [`PrepareTraversals`](events_queue.cc.md#PrepareTraversals), [`ProcessDeferredOpEvent`](events_queue.cc.md#ProcessDeferredOpEvent), [`FinishTraversal`](events_queue.cc.md#FinishTraversal)

### <a id="DeviceState"></a>`DeviceState`
- def: [`csrc/eager/events_queue.cc:1033`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1033)
- signature: `struct DeviceState`
- members:
  - <a id="DeviceState.Clear"></a>`Clear()` — [`L1047`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1047)
  - `GetAllStreamStates()` — [`L1036`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1036)
  - <a id="DeviceState.GetAllStreamStates"></a>`GetAllStreamStates()` — [`L1036`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1036)
  - <a id="DeviceState.GetOrCreateStreamState"></a>`GetOrCreateStreamState(int64_t stream_id)` — [`L1085`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1085)
  - <a id="DeviceState.ResetRepeatedOpsHeuristicState"></a>`ResetRepeatedOpsHeuristicState()` — [`L1059`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1059)
  - <a id="DeviceState.default_stream_state"></a>`default_stream_state` — [`L1067`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1067)
  - <a id="DeviceState.mutex"></a>`mutex` — [`L1068`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1068)
  - <a id="DeviceState.stream_states"></a>`stream_states` — [`L1081`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1081) — TODO: currently this vector only grows and never deallocates a StreamState
- uses (calls/refs, reference-scoped): [`Clear`](events_queue.cc.md#StreamState.Clear), [`StreamState`](events_queue.cc.md#StreamState), [`ResetRepeatedOpsHeuristicState`](events_queue.cc.md#StreamState.ResetRepeatedOpsHeuristicState)
- used by: [`ResetRepeatedOpsHeuristicState`](events_queue.cc.md#ResetRepeatedOpsHeuristicState), [`GetOrCreateStreamState`](events_queue.cc.md#GetOrCreateStreamState), [`Clear`](events_queue.cc.md#StreamStates.Clear), [`GetDeviceStreamStates`](events_queue.cc.md#GetDeviceStreamStates), [`StreamStates`](events_queue.cc.md#StreamStates)

### <a id="NodeMatcher"></a>`NodeMatcher`
- def: [`csrc/eager/events_queue.cc:179`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L179)
- doc: Lightweight matcher for target DeviceBufferList pointers during
- signature: `class NodeMatcher`
- members:
  - <a id="NodeMatcher.NodeMatcher"></a>`NodeMatcher(absl::Span<const SharedDeviceBufferList> nodes)` — [`L181`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L181)
  - <a id="NodeMatcher.contains"></a>`contains(const DeviceBufferList* absl_nonnull node)` — [`L196`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L196)
  - <a id="NodeMatcher.large_nodes_"></a>`large_nodes_` — [`L210`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L210)
  - <a id="NodeMatcher.single_node_"></a>`single_node_` — [`L208`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L208)
  - <a id="NodeMatcher.small_nodes_"></a>`small_nodes_` — [`L209`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L209)
- uses (calls/refs, reference-scoped): [`DeviceBufferList`](device_buffer.h.md#DeviceBufferList), [`SharedDeviceBufferList`](device_buffer.h.md#SharedDeviceBufferList)
- used by: [`PrepareTraversals`](events_queue.cc.md#PrepareTraversals), [`PrepareSnapshotMaterializations`](events_queue.cc.md#PrepareSnapshotMaterializations), [`ProcessDeferredOpEvent`](events_queue.cc.md#ProcessDeferredOpEvent), [`GetOpUsage`](events_queue.cc.md#GetOpUsage)

### <a id="OpUsage"></a>`OpUsage`
- def: [`csrc/eager/events_queue.cc:742`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L742)
- doc: The usage of a node within an execution region.
- signature: `enum class OpUsage`
- members:
  - <a id="OpUsage.kOutput"></a>`kOutput` — [`L744`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L744) — This node is an output of the materialization.
  - <a id="OpUsage.kUnused"></a>`kUnused` — [`L749`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L749) — This node is unused, and may need to be added as an output to ensure
  - <a id="OpUsage.kUsed"></a>`kUsed` — [`L746`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L746) — This node is an input to an output.
- used by: [`PrepareTraversals`](events_queue.cc.md#PrepareTraversals), [`ProcessDeferredOpEvent`](events_queue.cc.md#ProcessDeferredOpEvent), [`GetOpUsage`](events_queue.cc.md#GetOpUsage), [`FinishTraversal`](events_queue.cc.md#FinishTraversal), [`DefinedNodeMap`](events_queue.cc.md#DefinedNodeMap)

### <a id="SnapshotChainReleaser"></a>`SnapshotChainReleaser`
- def: [`csrc/eager/events_queue.cc:133`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L133)
- doc: Sets the promises that release the next event snapshot of a stream. Setting
- signature: `class SnapshotChainReleaser`
- members:
  - <a id="SnapshotChainReleaser.Release"></a>`Release(xla::Promise<void> promise)` — [`L135`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L135)
  - <a id="SnapshotChainReleaser.mu_"></a>`mu_` — [`L163`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L163)
  - <a id="SnapshotChainReleaser.pending_"></a>`pending_` — [`L165`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L165) — Promises released while a thread was setting promises.
  - <a id="SnapshotChainReleaser.releasing_"></a>`releasing_` — [`L167`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L167) — Whether a thread is setting promises.
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ReleaseNextSnapshot`](events_queue.cc.md#ReleaseNextSnapshot)

### <a id="StreamState"></a>`StreamState`
- def: [`csrc/eager/events_queue.cc:213`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L213)
- signature: `class StreamState`
- members:
  - <a id="StreamState.CheckLastRepeatedSequence"></a>`CheckLastRepeatedSequence(size_t new_hash)` — [`L610`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L610) — Helper function for RecordDeferredOpAndDetectRepetition.
  - <a id="StreamState.Clear"></a>`Clear()` — [`L256`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L256) — Clears all tracked DeviceBufferLists from the events queue, and resets the
  - <a id="StreamState.FindRepeatedSequence"></a>`FindRepeatedSequence(size_t new_hash)` — [`L646`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L646) — Helper function for RecordDeferredOpAndDetectRepetition.
  - `GetSnapshotEvents()` — [`L443`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L443)
  - <a id="StreamState.GetSnapshotEvents"></a>`GetSnapshotEvents()` — [`L443`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L443)
  - <a id="StreamState.JoinFutures"></a>`JoinFutures()` — [`L513`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L513)
  - <a id="StreamState.MarkActive"></a>`MarkActive(std::vector<xla::Future<void>>&& new_futures)` — [`L489`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L489)
  - `MarkActive(std::vector<xla::Future<void>>&& new_futures)` — [`L489`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L489)
  - <a id="StreamState.RecordCompiledExecutionTask"></a>`RecordCompiledExecutionTask(ExecutionTask&& execution_task, EagerMode eager_mode)` — [`L502`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L502)
  - <a id="StreamState.RecordDataPtrDestroyed"></a>`RecordDataPtrDestroyed(const DeviceBufferRef& device_buffer_ref)` — [`L234`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L234) — Records on the events queue that a c10::DataPtr referencing the given
  - <a id="StreamState.RecordDeferredOpAndDetectRepetition"></a>`RecordDeferredOpAndDetectRepetition(const SharedDeviceBufferList& device_buffer_list)` — [`L387`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L387)
  - <a id="StreamState.RecordDeferredOpCreated"></a>`RecordDeferredOpCreated(const SharedDeviceBufferList& device_buffer_list)` — [`L378`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L378)
  - <a id="StreamState.RecordNewDataPtrCreated"></a>`RecordNewDataPtrCreated(const DeviceBufferRef& device_buffer_ref)` — [`L217`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L217) — Records on the events queue that a new c10::DataPtr referencing the given
  - <a id="StreamState.RecordRepeatedHashPattern"></a>`RecordRepeatedHashPattern(int64_t repetition_length)` — [`L726`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L726) — Helper function for RecordDeferredOpAndDetectRepetition.
  - <a id="StreamState.RequestEventSnapshot"></a>`RequestEventSnapshot(std::vector<SharedDeviceBufferList> must_materialize, MaterializationReason reason, MaterializationMode mode, EagerMode eager_mode)` — [`L434`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L434)
  - `RequestEventSnapshot(std::vector<SharedDeviceBufferList> must_materialize, MaterializationReason reason, MaterializationMode mode, EagerMode eager_mode)` — [`L434`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L434)
  - <a id="StreamState.RequestEventSnapshotLocked"></a>`RequestEventSnapshotLocked(std::vector<SharedDeviceBufferList> must_materialize, MaterializationReason reason, MaterializationMode mode, EagerMode eager_mode)` — [`L560`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L560) — Common helper for RequestEventSnapshot and RecordCompiledExecutionTask.
  - `RequestEventSnapshotLocked(std::vector<SharedDeviceBufferList> must_materialize, MaterializationReason reason, MaterializationMode mode, EagerMode eager_mode)` — [`L560`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L560) — Common helper for RequestEventSnapshot and RecordCompiledExecutionTask.
  - <a id="StreamState.ResetRepeatedOpsHeuristicState"></a>`ResetRepeatedOpsHeuristicState()` — [`L478`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L478)
  - <a id="StreamState.SetCorePinningMode"></a>`SetCorePinningMode(CorePinningMode core_pinning_mode)` — [`L474`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L474) — Sets the device pinning mode of this events queue.
  - <a id="StreamState.core_pinning_mode"></a>`core_pinning_mode()` — [`L472`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L472) — Returns the core pinning mode of this events queue.
  - <a id="StreamState.core_pinning_mode_"></a>`core_pinning_mode_` — [`L607`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L607)
  - <a id="StreamState.events_queue_"></a>`events_queue_` — [`L597`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L597)
  - <a id="StreamState.futures_"></a>`futures_` — [`L590`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L590)
  - <a id="StreamState.live_nodes_"></a>`live_nodes_` — [`L594`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L594) — Hold a strong pointer to the DeviceBufferList as the key; as long as there
  - <a id="StreamState.mu_"></a>`mu_` — [`L589`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L589)
  - <a id="StreamState.repetition_hashes_"></a>`repetition_hashes_` — [`L603`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L603) — If a sequence repeats twice, we anticipate that it may repeat three or
  - <a id="StreamState.repetition_i_"></a>`repetition_i_` — [`L605`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L605) — The index of the next hash in repetition_hashes_ to check.
- uses (calls/refs, reference-scoped): [`NormalizeIfInsideBuildDirectory`](../common/macro_utils.cc.md#NormalizeIfInsideBuildDirectory), [`MaybeAddCppSourceLoc`](../common/status_builder.cc.md#MaybeAddCppSourceLoc), [`GetRootOpName`](../ops/python_context.cc.md#GetRootOpName), [`SetRootOpNamePayload`](../common/status_builder.cc.md#SetRootOpNamePayload), [`StatusBuilder`](../common/status_builder.h.md#StatusBuilder), [`operator<<`](../common/status_builder.h.md#StatusBuilder.operator), [`operator<<`](../ops/op_names.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`operator<<`](../common/cache_key.cc.md#operator), [`StatusBuilder`](../common/status_builder.cc.md#StatusBuilder.StatusBuilder), [`DeviceBufferRef`](device_buffer.h.md#DeviceBufferRef), [`device_buffer_list`](device_buffer.h.md#DeviceBufferRef.device_buffer_list), [`EagerMode`](../common/context_states.h.md#EagerMode), [`is_placeholder`](device_buffer.cc.md#DeviceBufferRef.is_placeholder), [`is_materialized`](device_buffer.cc.md#DeviceBufferRef.is_materialized), [`EventSnapshot`](events_queue.h.md#EventSnapshot), [`is_constant`](device_buffer.cc.md#DeviceBufferRef.is_constant), [`SharedDeviceBufferList`](device_buffer.h.md#SharedDeviceBufferList), [`MaterializationReason`](structured_log_buffer.h.md#MaterializationReason), [`FromDeferredOp`](events_queue.cc.md#StreamState.DeferredOpEvent.FromDeferredOp), [`ExecutionTask`](execution_task.h.md#ExecutionTask), [`MaterializationMode`](events_queue.h.md#MaterializationMode), [`OkCallback`](events_queue.cc.md#EventSnapshot.OkCallback), [`kSplitGraph`](events_queue.h.md#MaterializationMode.kSplitGraph), [`CorePinningMode`](../common/cache_key.h.md#CorePinningMode), [`MaterializationSettings`](events_queue.h.md#MaterializationSettings.MaterializationSettings), [`DeferredOpEvent`](events_queue.cc.md#StreamState.DeferredOpEvent), [`kPatternBreak`](events_queue.cc.md#StreamState.CheckLastRepeatedSequenceResult.kPatternBreak), [`kUnpinned`](../common/cache_key.h.md#CorePinningMode.kUnpinned), [`ReleaseNextSnapshot`](events_queue.cc.md#ReleaseNextSnapshot), [`StreamEvent`](events_queue.cc.md#StreamState.StreamEvent), [`CheckLastRepeatedSequenceResult`](events_queue.cc.md#StreamState.CheckLastRepeatedSequenceResult), [`deferred_op_hash`](events_queue.cc.md#StreamState.DeferredOpEvent.deferred_op_hash), [`EventSnapshotRequest`](events_queue.cc.md#StreamState.EventSnapshotRequest), [`no_side_effects`](events_queue.cc.md#StreamState.DeferredOpEvent.no_side_effects), [`MaterializationSettings`](events_queue.h.md#MaterializationSettings), [`execution_task`](events_queue.cc.md#StreamState.EventSnapshotRequest.execution_task), [`kCompileModeExecution`](structured_log_buffer.h.md#MaterializationReason.kCompileModeExecution), [`side_effects`](events_queue.cc.md#StreamState.DeferredOpEvent.side_effects)  (+8 more)
- used by: [`RecordDeferredOpCreated`](events_queue.cc.md#RecordDeferredOpCreated), [`RecordNewDataPtrCreated`](events_queue.cc.md#RecordNewDataPtrCreated), [`PrepareTraversals`](events_queue.cc.md#PrepareTraversals), [`Record`](events_queue.cc.md#EventSnapshot.Record), [`PrepareSnapshotMaterializations`](events_queue.cc.md#PrepareSnapshotMaterializations), [`RecordDeviceSnapshots`](events_queue.cc.md#RecordDeviceSnapshots), [`RecordDataPtrDestroyed`](events_queue.cc.md#RecordDataPtrDestroyed), [`RecordCompiledExecutionTask`](events_queue.cc.md#RecordCompiledExecutionTask), [`RecordDeferredOpAndDetectRepetition`](events_queue.cc.md#RecordDeferredOpAndDetectRepetition), [`GetOrCreateStreamState`](events_queue.cc.md#DeviceState.GetOrCreateStreamState), [`kPatternBreak`](events_queue.cc.md#StreamState.CheckLastRepeatedSequenceResult.kPatternBreak), [`SetCorePinningMode`](events_queue.cc.md#SetCorePinningMode), [`GetOrCreateStreamState`](events_queue.cc.md#GetOrCreateStreamState), [`ResetRepeatedOpsHeuristicState`](events_queue.cc.md#DeviceState.ResetRepeatedOpsHeuristicState), [`stream_states`](events_queue.cc.md#DeviceState.stream_states), [`GetStreamFor`](events_queue.cc.md#GetStreamFor), [`Clear`](events_queue.cc.md#DeviceState.Clear), [`GetAllStreamStates`](events_queue.cc.md#DeviceState.GetAllStreamStates), [`GetStreamStates`](events_queue.cc.md#GetStreamStates), [`MarkStreamActive`](events_queue.cc.md#MarkStreamActive), [`DeviceState`](events_queue.cc.md#DeviceState), [`mutex`](events_queue.cc.md#DeviceState.mutex), [`MarkStreamActive`](events_queue.cc.md#MarkStreamActive)

### <a id="StreamState.CheckLastRepeatedSequenceResult"></a>`StreamState.CheckLastRepeatedSequenceResult`
- def: [`csrc/eager/events_queue.cc:530`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L530)
- doc: Result of CheckLastRepeatedSequence, representing the relationship of the
- signature: `enum class CheckLastRepeatedSequenceResult`
- members:
  - <a id="StreamState.CheckLastRepeatedSequenceResult.kContinueWaiting"></a>`kContinueWaiting` — [`L533`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L533) — We've seen a partial prefix of the last repeated sequence, but not the
  - <a id="StreamState.CheckLastRepeatedSequenceResult.kPatternBreak"></a>`kPatternBreak` — [`L539`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L539) — We definitely are not following the last repeated sequence. Reset and
  - <a id="StreamState.CheckLastRepeatedSequenceResult.kRepetitionComplete"></a>`kRepetitionComplete` — [`L536`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L536) — We've seen another full loop of the last repeated sequence. Materialize
- uses (calls/refs, reference-scoped): [`EventSnapshot`](events_queue.h.md#EventSnapshot), [`CheckLastRepeatedSequence`](events_queue.cc.md#StreamState.CheckLastRepeatedSequence), [`FindRepeatedSequence`](events_queue.cc.md#StreamState.FindRepeatedSequence), [`mu_`](events_queue.cc.md#StreamState.mu_), [`RecordRepeatedHashPattern`](events_queue.cc.md#StreamState.RecordRepeatedHashPattern)
- used by: [`RecordDeferredOpAndDetectRepetition`](events_queue.cc.md#StreamState.RecordDeferredOpAndDetectRepetition), [`CheckLastRepeatedSequence`](events_queue.cc.md#StreamState.CheckLastRepeatedSequence), [`core_pinning_mode_`](events_queue.cc.md#StreamState.core_pinning_mode_)

### <a id="StreamState.DeferredOpEvent"></a>`StreamState.DeferredOpEvent`
- def: [`csrc/eager/events_queue.cc:301`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L301)
- doc: If a deferred op has no side effects, then as soon as all of its DataPtrs
- signature: `struct DeferredOpEvent`
- members:
  - <a id="StreamState.DeferredOpEvent.FromDeferredOp"></a>`FromDeferredOp(const SharedDeviceBufferList& device_buffer_list, bool compute_hash = false)` — [`L302`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L302)
  - <a id="StreamState.DeferredOpEvent.lock"></a>`lock()` — [`L337`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L337)
  - <a id="StreamState.DeferredOpEvent.deferred_op_hash"></a>`deferred_op_hash` — [`L349`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L349) — If compute_hash is true, this will contain a minimal hash of the
  - <a id="StreamState.DeferredOpEvent.no_side_effects"></a>`no_side_effects` — [`L343`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L343) — At most one of these will be a valid shared pointer.
  - <a id="StreamState.DeferredOpEvent.side_effects"></a>`side_effects` — [`L344`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L344)
- uses (calls/refs, reference-scoped): [`operator<<`](../ops/op_names.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`operator<<`](../common/cache_key.cc.md#operator), [`ToString`](../ops/op_names.h.md#ToString), [`DeviceBufferList`](device_buffer.h.md#DeviceBufferList), [`ToString`](../common/to_string.h.md#ToString), [`ToString`](../common/dtype.cc.md#ToString), [`ToString`](../common/to_string.h.md#ToString), [`ToString`](../common/to_string.h.md#ToString), [`ToString`](../common/to_string.cc.md#ToString), [`ToString`](../common/to_string.h.md#ToString), [`ToString`](../common/to_string.h.md#ToString), [`ToString`](../common/to_string.h.md#ToString), [`ToString`](../common/to_string.h.md#ToString), [`ToString`](../common/to_string.h.md#ToString), [`ToString`](../common/to_string.h.md#ToString), [`ToString`](../common/to_string.cc.md#ToString), [`ToString`](../common/to_string.h.md#ToString), [`ToString`](../common/shape.cc.md#ToString), [`ToString`](structured_log_buffer.h.md#ToString), [`Hash`](device_buffer.cc.md#DeferredOp.Hash), [`SharedDeviceBufferList`](device_buffer.h.md#SharedDeviceBufferList), [`op_name`](device_buffer.h.md#DeferredOp.op_name), [`deferred_op`](device_buffer.h.md#DeviceBufferList.deferred_op), [`is_constant`](device_buffer.h.md#DeviceBufferList.is_constant), [`IsSideEffectingOp`](../ops/op_names.h.md#IsSideEffectingOp)
- used by: [`PrepareTraversals`](events_queue.cc.md#PrepareTraversals), [`Clear`](events_queue.cc.md#StreamState.Clear), [`PrepareSnapshotMaterializations`](events_queue.cc.md#PrepareSnapshotMaterializations), [`RecordDeferredOpAndDetectRepetition`](events_queue.cc.md#StreamState.RecordDeferredOpAndDetectRepetition), [`FindRepeatedSequence`](events_queue.cc.md#StreamState.FindRepeatedSequence), [`RecordRepeatedHashPattern`](events_queue.cc.md#StreamState.RecordRepeatedHashPattern), [`ResetRepeatedOpsHeuristicState`](events_queue.cc.md#StreamState.ResetRepeatedOpsHeuristicState), [`RecordDeferredOpCreated`](events_queue.cc.md#StreamState.RecordDeferredOpCreated), [`StreamEvent`](events_queue.cc.md#StreamState.StreamEvent)

### <a id="StreamState.EventSnapshotRequest"></a>`StreamState.EventSnapshotRequest`
- def: [`csrc/eager/events_queue.cc:353`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L353)
- doc: A request to create an EventSnapshot at this point in the stream.
- signature: `struct EventSnapshotRequest`
- members:
  - <a id="StreamState.EventSnapshotRequest.execution_task"></a>`execution_task` — [`L365`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L365) — If the snapshot includes a compiled mode execution task, it will be
  - <a id="StreamState.EventSnapshotRequest.futures"></a>`futures` — [`L355`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L355) — Futures that must complete before the snapshot is reached.
  - <a id="StreamState.EventSnapshotRequest.live_nodes"></a>`live_nodes` — [`L362`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L362) — Live nodes that must be materialized by the snapshot if deferred.
  - <a id="StreamState.EventSnapshotRequest.materialization_settings"></a>`materialization_settings` — [`L360`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L360) — Settings for the materialization. These are frozen when the request is
  - <a id="StreamState.EventSnapshotRequest.must_materialize"></a>`must_materialize` — [`L357`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L357) — Nodes that explicitly must be materialized by the snapshot.
  - <a id="StreamState.EventSnapshotRequest.snapshot_promise"></a>`snapshot_promise` — [`L368`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L368) — The promise which can be used to provide the snapshot once is it
- uses (calls/refs, reference-scoped): [`EventSnapshot`](events_queue.h.md#EventSnapshot), [`SharedDeviceBufferList`](device_buffer.h.md#SharedDeviceBufferList), [`ExecutionTask`](execution_task.h.md#ExecutionTask), [`MaterializationSettings`](events_queue.h.md#MaterializationSettings)
- used by: [`Clear`](events_queue.cc.md#StreamState.Clear), [`PrepareSnapshotMaterializations`](events_queue.cc.md#PrepareSnapshotMaterializations), [`RequestEventSnapshotLocked`](events_queue.cc.md#StreamState.RequestEventSnapshotLocked), [`RecordCompiledExecutionTask`](events_queue.cc.md#StreamState.RecordCompiledExecutionTask), [`GetSnapshotEvents`](events_queue.cc.md#StreamState.GetSnapshotEvents), [`StreamEvent`](events_queue.cc.md#StreamState.StreamEvent)

### <a id="StreamState.StreamEvent"></a>`StreamState.StreamEvent`
- def: [`csrc/eager/events_queue.cc:374`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L374)
- doc: The stream collects a series of DeferredOpEvents in order, with
- signature: `using StreamEvent = std::variant<DeferredOpEvent, absl_nonnull std::unique_ptr<EventSnapshotRequest>>`
- uses (calls/refs, reference-scoped): [`DeferredOpEvent`](events_queue.cc.md#StreamState.DeferredOpEvent), [`EventSnapshotRequest`](events_queue.cc.md#StreamState.EventSnapshotRequest)
- used by: [`Clear`](events_queue.cc.md#StreamState.Clear), [`PrepareSnapshotMaterializations`](events_queue.cc.md#PrepareSnapshotMaterializations), [`GetSnapshotEvents`](events_queue.cc.md#StreamState.GetSnapshotEvents), [`RequestEventSnapshot`](events_queue.cc.md#StreamState.RequestEventSnapshot), [`live_nodes_`](events_queue.cc.md#StreamState.live_nodes_)

### <a id="StreamStates"></a>`StreamStates`
- def: [`csrc/eager/events_queue.cc:1099`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1099)
- signature: `struct StreamStates`
- members:
  - <a id="StreamStates.Clear"></a>`Clear()` — [`L1106`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1106)
  - <a id="StreamStates.GetDeviceState"></a>`GetDeviceState(c10::DeviceIndex device_index)` — [`L1100`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1100)
  - <a id="StreamStates.device_states"></a>`device_states` — [`L1112`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1112)
- uses (calls/refs, reference-scoped): [`Clear`](events_queue.cc.md#DeviceState.Clear), [`DeviceState`](events_queue.cc.md#DeviceState), [`kMaxTorchDevices`](events_queue.cc.md#kMaxTorchDevices)
- used by: [`ClearAllStreams`](events_queue.cc.md#ClearAllStreams), [`ResetRepeatedOpsHeuristicState`](events_queue.cc.md#ResetRepeatedOpsHeuristicState), [`GetOrCreateStreamState`](events_queue.cc.md#GetOrCreateStreamState), [`GetStreamStates`](events_queue.cc.md#GetStreamStates), [`GetDeviceStreamStates`](events_queue.cc.md#GetDeviceStreamStates)

## Functions
- <a id="ClearAllStreams"></a>`ClearAllStreams()` — [`L1373`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1373) — Clears all references to DeviceBufferLists from the events queue, forgets all
- <a id="CreateNoOpDependency"></a>`CreateNoOpDependency` — [`L92`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L92) — Creates a new deferred DeviceBufferList which represents a data dependency
- <a id="FinishTraversal"></a>`FinishTraversal(std::vector<SharedDeviceBufferList>& execution_order, DefinedNodeMap& defined_node_map, std::vector<SharedDeviceBufferList>& output_nodes, CorePinningMode core_pinning_mode)` — [`L851`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L851) — Helper function for PrepareMaterializationTraversals.
- `FinishTraversal(std::vector<SharedDeviceBufferList>& execution_order, DefinedNodeMap& defined_node_map, std::vector<SharedDeviceBufferList>& output_nodes, CorePinningMode core_pinning_mode)` — [`L851`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L851) — Helper function for PrepareMaterializationTraversals.
- <a id="GetCompilationMode"></a>`GetCompilationMode(EagerMode eager_mode)` — [`L1400`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1400) — Returns the CompilationMode for the given EagerMode. — documented in [context-states-and-execution-modes](../../../concepts/context-states-and-execution-modes.md)
- <a id="GetDeviceStreamStates"></a>`GetDeviceStreamStates(c10::DeviceIndex device_index)` — [`L1127`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1127)
- `GetDeviceStreamStates(c10::DeviceIndex device_index)` — [`L1127`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1127)
- `GetOpUsage(const DeferredOp& deferred_op, const SharedDeviceBufferList& device_buffer_list, const absl::flat_hash_map<SharedDeviceBufferList, int64_t>& live_nodes, const NodeMatcher& nodes_to_materialize_set)` — [`L756`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L756) — Returns the OpUsage of the given device buffer list, switching between
- <a id="GetOpUsage"></a>`GetOpUsage(const DeferredOp& deferred_op, const SharedDeviceBufferList& device_buffer_list, const absl::flat_hash_map<SharedDeviceBufferList, int64_t>& live_nodes, const NodeMatcher& nodes_to_materialize_set)` — [`L756`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L756) — Returns the OpUsage of the given device buffer list, switching between
- <a id="GetOrCreateStreamState"></a>`GetOrCreateStreamState(c10::DeviceIndex device_index, int64_t stream_id)` — [`L1120`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1120)
- `GetStreamFor(const DeviceBufferRef& device_buffer_ref)` — [`L1152`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1152)
- <a id="GetStreamFor"></a>`GetStreamFor(const SharedDeviceBufferList& device_buffer_list)` — [`L1146`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1146)
- <a id="GetStreamStates"></a>`GetStreamStates()` — [`L1115`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1115)
- `MarkStreamActive(c10::DeviceIndex device_index, int64_t stream_id, std::vector<xla::Future<void>>&& new_futures)` — [`L1132`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1132)
- <a id="MarkStreamActive"></a>`MarkStreamActive(c10::DeviceIndex device_index, int64_t stream_id, xla::Future<void> future)` — [`L1138`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1138)
- `MarkStreamActive(c10::DeviceIndex device_index, int64_t stream_id, std::vector<xla::Future<void>>&& new_futures)` — [`L1132`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1132)
- `PrepareSnapshotMaterializations(c10::DeviceIndex device_index, c10::StreamId stream_id)` — [`L1197`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1197) — Returns a sequence of Traversals that, if compiled and executed, would
- <a id="PrepareSnapshotMaterializations"></a>`PrepareSnapshotMaterializations(c10::DeviceIndex device_index, c10::StreamId stream_id)` — [`L1197`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1197) — Returns a sequence of Traversals that, if compiled and executed, would
- `PrepareTraversals(absl::Span<const StreamState::DeferredOpEvent> deferred_op_events, const absl::flat_hash_map<SharedDeviceBufferList, int64_t>& live_nodes, absl::Span<const SharedDeviceBufferList> nodes_to_materialize, const NodeMatcher& nodes_to_materialize_set, CorePinningMode core_pinning_mode)` — [`L900`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L900)
- <a id="PrepareTraversals"></a>`PrepareTraversals(absl::Span<const StreamState::DeferredOpEvent> deferred_op_events, const absl::flat_hash_map<SharedDeviceBufferList, int64_t>& live_nodes, absl::Span<const SharedDeviceBufferList> nodes_to_materialize, const NodeMatcher& nodes_to_materialize_set, CorePinningMode core_pinning_mode)` — [`L900`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L900)
- `ProcessDeferredOpEvent(SharedDeviceBufferList&& device_buffer_list, const DeferredOp& deferred_op, const absl::flat_hash_map<SharedDeviceBufferList, int64_t>& live_nodes, const NodeMatcher& nodes_to_materialize_set, std::vector<SharedDeviceBufferList>& execution_order, DefinedNodeMap& defined_node_map)` — [`L801`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L801) — Helper function for PrepareMaterializationTraversals.
- <a id="ProcessDeferredOpEvent"></a>`ProcessDeferredOpEvent(SharedDeviceBufferList&& device_buffer_list, const DeferredOp& deferred_op, const absl::flat_hash_map<SharedDeviceBufferList, int64_t>& live_nodes, const NodeMatcher& nodes_to_materialize_set, std::vector<SharedDeviceBufferList>& execution_order, DefinedNodeMap& defined_node_map)` — [`L801`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L801) — Helper function for PrepareMaterializationTraversals.
- <a id="PruneCompletedFutures"></a>`PruneCompletedFutures(std::vector<xla::Future<void>>& futures)` — [`L116`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L116)
- `PruneCompletedFutures(std::vector<xla::Future<void>>& futures)` — [`L116`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L116)
- <a id="RecordAsyncDeviceToHost"></a>`RecordAsyncDeviceToHost(xla::Future<void> to_literal_future)` — [`L1244`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1244) — Tracks that an async device-to-host copy has been started.
- <a id="RecordAsyncHostToDevice"></a>`RecordAsyncHostToDevice(const DeviceBufferRef& device_buffer_ref)` — [`L1236`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1236) — Tracks that an async host-to-device copy has been started that will populate
- <a id="RecordCompiledExecutionTask"></a>`RecordCompiledExecutionTask(ExecutionTask&& execution_task, c10::DeviceIndex device_index, c10::StreamId stream_id, EagerMode eager_mode)` — [`L1187`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1187) — Tracks that a compiled mode execution task has been created.
- <a id="RecordDataPtrDestroyed"></a>`RecordDataPtrDestroyed(const DeviceBufferRef& device_buffer_ref)` — [`L1169`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1169) — Records on the events queue that a c10::DataPtr referencing the given
- <a id="RecordDeferredOpAndDetectRepetition"></a>`RecordDeferredOpAndDetectRepetition(const SharedDeviceBufferList& device_buffer_list)` — [`L1383`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1383) — Records on the events queue that a new deferred op has been created, and
- <a id="RecordDeferredOpCreated"></a>`RecordDeferredOpCreated(const SharedDeviceBufferList& device_buffer_list)` — [`L1178`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1178) — Records on the events queue that a new deferred op has been created.
- `RecordDeviceSnapshots(c10::DeviceIndex device_index, std::vector<SharedDeviceBufferList> must_materialize, MaterializationReason reason, MaterializationMode mode)` — [`L1254`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1254) — Records one PendingEventSnapshot for each stream on the given device.
- <a id="RecordDeviceSnapshots"></a>`RecordDeviceSnapshots(c10::DeviceIndex device_index, std::vector<SharedDeviceBufferList> must_materialize, MaterializationReason reason, MaterializationMode mode)` — [`L1254`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1254) — Records one PendingEventSnapshot for each stream on the given device.
- <a id="RecordNewDataPtrCreated"></a>`RecordNewDataPtrCreated(const DeviceBufferRef& device_buffer_ref)` — [`L1160`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1160) — Records on the events queue that a new c10::DataPtr referencing the given
- <a id="ReleaseNextSnapshot"></a>`ReleaseNextSnapshot(xla::Promise<void> promise)` — [`L171`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L171) — Releases the next event snapshot of a stream.
- <a id="ResetRepeatedOpsHeuristicState"></a>`ResetRepeatedOpsHeuristicState()` — [`L1394`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1394) — Resets the state of the repeated ops heuristic for all streams, but leaves
- <a id="SetCorePinningMode"></a>`SetCorePinningMode(c10::DeviceIndex device_index, c10::StreamId stream_id, CorePinningMode pinned)` — [`L1378`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1378) — Sets the core pinning mode for the given stream.

## Module values
- <a id="kMaxRepeatedSubsequenceLength"></a>`kMaxRepeatedSubsequenceLength` — [`L75`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L75)
- <a id="kMaxTorchDevices"></a>`kMaxTorchDevices` — [`L77`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L77)
- <a id="kMinRepeatedSubsequenceLength"></a>`kMinRepeatedSubsequenceLength` — [`L74`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L74)
- <a id="kMinRepetitionCount"></a>`kMinRepetitionCount` — [`L76`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L76)

## Other members
- `Record` — [`L1287`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1287)
- <a id="EventSnapshot.CompletionTime"></a>`EventSnapshot.CompletionTime` — [`L1337`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1337)
- <a id="EventSnapshot.ElapsedTime"></a>`EventSnapshot.ElapsedTime` — [`L1345`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1345)
- <a id="EventSnapshot.EventSnapshot"></a>`EventSnapshot.EventSnapshot` — [`L1302`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1302)
- <a id="EventSnapshot.OkCallback"></a>`EventSnapshot.OkCallback` — [`L1362`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1362)
- <a id="EventSnapshot.Query"></a>`EventSnapshot.Query` — [`L1332`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1332)
- <a id="EventSnapshot.Record"></a>`EventSnapshot.Record` — [`L1287`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1287)
- <a id="EventSnapshot.Synchronize"></a>`EventSnapshot.Synchronize` — [`L1320`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.cc#L1320)

