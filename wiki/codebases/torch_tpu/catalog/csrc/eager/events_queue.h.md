---
title: 'Module: csrc/eager/events_queue.h'
type: catalog
provenance: extracted
module: csrc/eager/events_queue.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  EventSnapshot: EventSnapshot#
  PendingSnapshotMaterialization.traversals: PendingSnapshotMaterialization#traversals.
  MaterializationMode: MaterializationMode#
  MaterializationMode.kSplitGraph: MaterializationMode#kSplitGraph.
  PendingEventSnapshot.snapshot_future: PendingEventSnapshot#snapshot_future.
  MaterializationSettings.MaterializationSettings: MaterializationSettings#MaterializationSettings(e633f8f6d6e7747e).
  PendingSnapshotMaterialization.snapshot_promise: PendingSnapshotMaterialization#snapshot_promise.
  PendingSnapshotMaterialization.futures: PendingSnapshotMaterialization#futures.
  EventSnapshot.completion_: EventSnapshot#completion_.
  EventSnapshot.future_: EventSnapshot#future_.
  EventSnapshot.Completion.mu: EventSnapshot#Completion#mu.
  EventSnapshot.Completion.chain_promise: EventSnapshot#Completion#chain_promise.
  EventSnapshot.Completion.completed: EventSnapshot#Completion#completed.
  MaterializationSettings.compilation_mode: MaterializationSettings#compilation_mode.
  PendingSnapshotMaterialization: PendingSnapshotMaterialization#
  PendingEventSnapshot.stream_id: PendingEventSnapshot#stream_id.
  PendingSnapshotMaterialization.execution_task: PendingSnapshotMaterialization#execution_task.
  MaterializationSettings: MaterializationSettings#
  MaterializationSettings.materialization_mode: MaterializationSettings#materialization_mode.
  MaterializationSettings.reason: MaterializationSettings#reason.
  EventSnapshot.Completion: EventSnapshot#Completion#
  EventSnapshot.Completion.time: EventSnapshot#Completion#time.
  PendingSnapshotMaterialization.must_materialize: PendingSnapshotMaterialization#must_materialize.
  PendingEventSnapshot: PendingEventSnapshot#
  MaterializationMode.kFullGraph: MaterializationMode#kFullGraph.
  MaterializationSettings.compilation_context: MaterializationSettings#compilation_context.
  PendingEventSnapshot.device_index: PendingEventSnapshot#device_index.
  PendingSnapshotMaterialization.settings: PendingSnapshotMaterialization#settings.
---
# Module: [`csrc/eager/events_queue.h`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h)

## Classes
### <a id="EventSnapshot"></a>`EventSnapshot`
- def: [`csrc/eager/events_queue.h:91`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L91) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- doc: An EventSnapshot is a joined XLA future that represents the state of
- signature: `class EventSnapshot`
- members:
  - <a id="EventSnapshot.completion_"></a>`completion_` — [`L136`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L136)
  - <a id="EventSnapshot.future_"></a>`future_` — [`L135`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L135) — The future backing the event snapshot.
- uses (calls/refs, reference-scoped): [`Record`](events_queue.cc.md#EventSnapshot.Record), [`SharedDeviceBufferList`](device_buffer.h.md#SharedDeviceBufferList), [`MaterializationReason`](structured_log_buffer.h.md#MaterializationReason), [`ElapsedTime`](events_queue.cc.md#EventSnapshot.ElapsedTime), [`Record`](events_queue.cc.md#EventSnapshot.Record), [`MaterializationMode`](events_queue.h.md#MaterializationMode), [`EventSnapshot`](events_queue.cc.md#EventSnapshot.EventSnapshot), [`Synchronize`](events_queue.cc.md#EventSnapshot.Synchronize), [`OkCallback`](events_queue.cc.md#EventSnapshot.OkCallback), [`Query`](events_queue.cc.md#EventSnapshot.Query), [`kSplitGraph`](events_queue.h.md#MaterializationMode.kSplitGraph), [`kUnknown`](structured_log_buffer.h.md#MaterializationReason.kUnknown), [`Completion`](events_queue.h.md#EventSnapshot.Completion)
- used by: [`TestBody`](events_queue_test.cc.md#EventsQueueTest_ClearsBuffersAfterMaterialization_Test.TestBody), [`stream_id`](materialize.cc.md#MaterializeSpan.DeviceStreamId.stream_id), [`ElapsedTime`](events_queue.cc.md#EventSnapshot.ElapsedTime), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_PrepareStreamTraversals_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_StreamsMaterializeSeparately_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_DeadSideEffectsRetained_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_GetsLiveDeferredBuffers_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_MaterializationAppendsExplicitEmptyOps_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_MaterializationIgnoresUnusedEmptyOps_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_SingleTraversalIfPossible_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_SplitModeRespected_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_UsedEmptyOpsMaterializedOnFirstUse_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_DeadCodeEliminated_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_StreamMustMaterializeEmptyTensors_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_MultipleSnapshotsPulled_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_NodeMatcherAcrossSmallAndLargeSpans_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_NotPulledAfterLastSnapshot_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_SingleOpFastPathAndExtraConstantFallback_Test.TestBody), [`EnqueueExecutable`](materialize.cc.md#EnqueueExecutable), [`Materialize`](materialize.h.md#Materialize), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_StopsTrackingAfterClearEventsQueue_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_IgnoresPlaceholderBuffers_Test.TestBody), [`ProcessMaterializationTask`](materialize.cc.md#ProcessMaterializationTask), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_RetainsFailedCompletedFutures_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_SyncIgnoresEmptyBuffers_Test.TestBody), [`Record`](events_queue.cc.md#EventSnapshot.Record), [`MaterializeStream`](materialize.cc.md#MaterializeStream), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_IgnoresAlreadyMaterializedBuffers_Test.TestBody), [`EventSnapshot`](events_queue.cc.md#EventSnapshot.EventSnapshot), [`RecordDeviceSnapshots`](events_queue.cc.md#RecordDeviceSnapshots), [`TestBody`](events_queue_test.cc.md#EventSnapshotTest_ElapsedTimeReturnsEventError_Test.TestBody), [`RecordDeferredOpAndDetectRepetition`](events_queue.cc.md#StreamState.RecordDeferredOpAndDetectRepetition), [`MaterializeDevice`](materialize.cc.md#MaterializeDevice), [`RequestEventSnapshotLocked`](events_queue.cc.md#StreamState.RequestEventSnapshotLocked), [`record`](tpu_hooks.cc.md#TpuDeviceGuardImpl.record), [`synchronizeEvent`](tpu_hooks.cc.md#TpuDeviceGuardImpl.synchronizeEvent), [`Synchronize`](events_queue.cc.md#EventSnapshot.Synchronize), [`OkCallback`](events_queue.cc.md#EventSnapshot.OkCallback), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_CompletesLongSnapshotChainOnSmallStack_Test.TestBody), [`CompletionTime`](events_queue.cc.md#EventSnapshot.CompletionTime)  (+12 more)

### <a id="EventSnapshot.Completion"></a>`EventSnapshot.Completion`
- def: [`csrc/eager/events_queue.h:121`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L121)
- doc: The completion of an event snapshot, shared with the callback on its future
- signature: `struct Completion`
- members:
  - <a id="EventSnapshot.Completion.chain_promise"></a>`chain_promise` — [`L128`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L128) — The promise passed to OkCallback before the snapshot completed.
  - <a id="EventSnapshot.Completion.completed"></a>`completed` — [`L124`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L124) — Whether the snapshot has completed and `time` is set.
  - <a id="EventSnapshot.Completion.mu"></a>`mu` — [`L122`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L122)
  - <a id="EventSnapshot.Completion.time"></a>`time` — [`L126`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L126) — The host time at which the snapshot completed.
- uses (calls/refs, reference-scoped): [`CompletionTime`](events_queue.cc.md#EventSnapshot.CompletionTime)
- used by: [`EventSnapshot`](events_queue.cc.md#EventSnapshot.EventSnapshot), [`Synchronize`](events_queue.cc.md#EventSnapshot.Synchronize), [`OkCallback`](events_queue.cc.md#EventSnapshot.OkCallback), [`CompletionTime`](events_queue.cc.md#EventSnapshot.CompletionTime), [`future_`](events_queue.h.md#EventSnapshot.future_)

### <a id="MaterializationMode"></a>`MaterializationMode`
- def: [`csrc/eager/events_queue.h:87`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L87) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- signature: `enum class MaterializationMode`
- members:
  - <a id="MaterializationMode.kFullGraph"></a>`kFullGraph` — [`L87`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L87)
  - <a id="MaterializationMode.kSplitGraph"></a>`kSplitGraph` — [`L87`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L87)
- used by: [`gather`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.gather), [`PrepareCompiledModeArgumentsImpl`](../internal/compile/compiled_mode.cc.md#PrepareCompiledModeArgumentsImpl), [`EventSnapshot`](events_queue.h.md#EventSnapshot), [`PrepareCompiledModeArgumentsImpl`](../internal/compile/compiled_mode.cc.md#PrepareCompiledModeArgumentsImpl), [`MarkDynamic`](../internal/dynamism/dynamism.cc.md#MarkDynamic), [`CopyTpuToCpu`](../ops/copy_from/tpu_to_cpu.cc.md#CopyTpuToCpu), [`MaterializeAndReturn`](tensor_to_buffer.cc.md#MaterializeAndReturn), [`MaybeMaterializeDeviceStateTensor`](device_gen_impl.cc.md#DeviceGeneratorState.MaybeMaterializeDeviceStateTensor), [`TestBody`](shutdown_test.cc.md#ShutdownTest_E2EShutdownCompletes_Test.TestBody), [`TrySyncSingleTensorFast`](../internal/sync/sync_py.cc.md#TrySyncSingleTensorFast), [`TrySyncTensorArrayFast`](../internal/sync/sync_py.cc.md#TrySyncTensorArrayFast), [`GetDynamismInfo`](../internal/dynamism/dynamism.cc.md#GetDynamismInfo), [`SynchronizeTensorsImpl`](../internal/sync/sync.cc.md#SynchronizeTensorsImpl), [`PySyncSpanNoWait`](../internal/sync/sync_py.cc.md#PySyncSpanNoWait), [`ApplySplitMode`](materialize.cc.md#ApplySplitMode), [`Materialize`](materialize.h.md#Materialize), [`Record`](events_queue.cc.md#EventSnapshot.Record), [`DeferNeverDispatch`](device_buffer_utils.cc.md#DeferNeverDispatch), [`Materialize`](materialize.cc.md#Materialize), [`MaterializeStream`](materialize.cc.md#MaterializeStream), [`RecordDeviceSnapshots`](events_queue.cc.md#RecordDeviceSnapshots), [`Materialize`](materialize.cc.md#Materialize), [`MaterializeDevice`](materialize.cc.md#MaterializeDevice), [`Materialize`](../api/tensor_buffer.cc.md#TensorBufferHandle.Materialize), [`RequestEventSnapshotLocked`](events_queue.cc.md#StreamState.RequestEventSnapshotLocked), [`kNonBlocking`](materialize.h.md#MaterializationBlockMode.kNonBlocking), [`Materialize`](materialize.h.md#Materialize), [`RecordCompiledExecutionTask`](events_queue.cc.md#StreamState.RecordCompiledExecutionTask), [`Materialize`](materialize.cc.md#Materialize), [`snapshot_future`](events_queue.h.md#PendingEventSnapshot.snapshot_future), [`MaterializeCurrentStream`](materialize.cc.md#MaterializeCurrentStream), [`MaterializationSettings`](events_queue.h.md#MaterializationSettings.MaterializationSettings), [`GetRepeatedOpsMaterializationMode`](device_buffer_utils.cc.md#GetRepeatedOpsMaterializationMode), [`RequestEventSnapshot`](events_queue.cc.md#StreamState.RequestEventSnapshot), [`MustApplyRepeatedOpsHeuristic`](device_buffer_utils.cc.md#MustApplyRepeatedOpsHeuristic), [`MaterializeSpan`](materialize.cc.md#MaterializeSpan)

### <a id="MaterializationSettings"></a>`MaterializationSettings`
- def: [`csrc/eager/events_queue.h:163`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L163)
- doc: Settings for how to compile a set of traversals to reach a snapshot.
- signature: `struct MaterializationSettings`
- members:
  - <a id="MaterializationSettings.MaterializationSettings"></a>`MaterializationSettings(MaterializationReason reason, MaterializationMode materialization_mode, EagerMode eager_mode)` — [`L164`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L164)
  - <a id="MaterializationSettings.compilation_context"></a>`compilation_context` — [`L178`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L178) — Immutable, shared set of pre-resolved CompilationSpecs for every
  - <a id="MaterializationSettings.compilation_mode"></a>`compilation_mode` — [`L173`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L173)
  - <a id="MaterializationSettings.materialization_mode"></a>`materialization_mode` — [`L171`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L171)
  - <a id="MaterializationSettings.reason"></a>`reason` — [`L172`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L172)
- uses (calls/refs, reference-scoped): [`EagerMode`](../common/context_states.h.md#EagerMode), [`CompilationMode`](../common/compilation_spec.h.md#CompilationMode), [`MaterializationReason`](structured_log_buffer.h.md#MaterializationReason), [`GetCompilationMode`](events_queue.cc.md#GetCompilationMode), [`MaterializationMode`](events_queue.h.md#MaterializationMode), [`GetCompilationContext`](../common/compilation.cc.md#GetCompilationContext), [`CompilationContext`](../common/compilation_spec.h.md#CompilationContext)
- used by: [`ApplySplitMode`](materialize.cc.md#ApplySplitMode), [`RequestEventSnapshotLocked`](events_queue.cc.md#StreamState.RequestEventSnapshotLocked), [`GetCompilationSpecForTraversal`](materialize.cc.md#GetCompilationSpecForTraversal), [`must_materialize`](events_queue.cc.md#StreamState.EventSnapshotRequest.must_materialize), [`must_materialize`](events_queue.h.md#PendingSnapshotMaterialization.must_materialize)

### <a id="PendingEventSnapshot"></a>`PendingEventSnapshot`
- def: [`csrc/eager/events_queue.h:142`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L142)
- doc: A future that will resolve to an EventSnapshot during the materialization
- signature: `struct PendingEventSnapshot`
- members:
  - <a id="PendingEventSnapshot.device_index"></a>`device_index` — [`L144`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L144) — The device and stream that the snapshot is for.
  - <a id="PendingEventSnapshot.snapshot_future"></a>`snapshot_future` — [`L147`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L147) — The future that will resolve to the EventSnapshot.
  - <a id="PendingEventSnapshot.stream_id"></a>`stream_id` — [`L145`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L145)
- uses (calls/refs, reference-scoped): [`EagerMode`](../common/context_states.h.md#EagerMode), [`EventSnapshot`](events_queue.h.md#EventSnapshot), [`SharedDeviceBufferList`](device_buffer.h.md#SharedDeviceBufferList), [`CompilationMode`](../common/compilation_spec.h.md#CompilationMode), [`MaterializationReason`](structured_log_buffer.h.md#MaterializationReason), [`GetCompilationMode`](events_queue.cc.md#GetCompilationMode), [`MaterializationMode`](events_queue.h.md#MaterializationMode), [`RecordDeviceSnapshots`](events_queue.cc.md#RecordDeviceSnapshots), [`kSplitGraph`](events_queue.h.md#MaterializationMode.kSplitGraph), [`kUnknown`](structured_log_buffer.h.md#MaterializationReason.kUnknown), [`RecordDeviceSnapshots`](events_queue.cc.md#RecordDeviceSnapshots)
- used by: [`TestBody`](events_queue_test.cc.md#EventsQueueTest_PrepareDeviceTraversals_Test.TestBody), [`RecordDeviceSnapshots`](events_queue.cc.md#RecordDeviceSnapshots), [`RecordAsyncDeviceToHost`](events_queue.cc.md#RecordAsyncDeviceToHost), [`MaterializeDevice`](materialize.cc.md#MaterializeDevice)

### <a id="PendingSnapshotMaterialization"></a>`PendingSnapshotMaterialization`
- def: [`csrc/eager/events_queue.h:182`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L182)
- doc: A snapshot to be materialized.
- signature: `struct PendingSnapshotMaterialization`
- members:
  - <a id="PendingSnapshotMaterialization.execution_task"></a>`execution_task` — [`L189`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L189) — If the snapshot includes a compiled mode execution task, it will be stored
  - <a id="PendingSnapshotMaterialization.futures"></a>`futures` — [`L195`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L195) — Futures that must be completed before the snapshot is reached.
  - <a id="PendingSnapshotMaterialization.must_materialize"></a>`must_materialize` — [`L191`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L191) — The nodes that were expected to be materialized by the traversals.
  - <a id="PendingSnapshotMaterialization.settings"></a>`settings` — [`L193`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L193) — Settings for the materialization.
  - <a id="PendingSnapshotMaterialization.snapshot_promise"></a>`snapshot_promise` — [`L198`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L198) — When the execution for the traversals has started, an EventSnapshot will be
  - <a id="PendingSnapshotMaterialization.traversals"></a>`traversals` — [`L186`](../../../../../../raw/code/torch_tpu/csrc/eager/events_queue.h#L186) — The traversals that must be executed to materialize the snapshot.
- uses (calls/refs, reference-scoped): [`Traversal`](traversal.h.md#Traversal), [`EventSnapshot`](events_queue.h.md#EventSnapshot), [`PrepareSnapshotMaterializations`](events_queue.cc.md#PrepareSnapshotMaterializations), [`SharedDeviceBufferList`](device_buffer.h.md#SharedDeviceBufferList), [`ExecutionTask`](execution_task.h.md#ExecutionTask), [`PrepareSnapshotMaterializations`](events_queue.cc.md#PrepareSnapshotMaterializations), [`CorePinningMode`](../common/cache_key.h.md#CorePinningMode), [`SetCorePinningMode`](events_queue.cc.md#SetCorePinningMode), [`MaterializationSettings`](events_queue.h.md#MaterializationSettings)
- used by: [`TestBody`](events_queue_test.cc.md#EventsQueueTest_ClearsBuffersAfterMaterialization_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_PrepareStreamTraversals_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_StreamsMaterializeSeparately_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_PrepareDeviceTraversals_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_DeadSideEffectsRetained_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_GetsLiveDeferredBuffers_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_MaterializationAppendsExplicitEmptyOps_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_MaterializationIgnoresUnusedEmptyOps_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_SingleTraversalIfPossible_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_SplitModeRespected_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_UsedEmptyOpsMaterializedOnFirstUse_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_DeadCodeEliminated_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_StreamMustMaterializeEmptyTensors_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_DeviceMustMaterializeEmptyTensors_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_MultipleSnapshotsPulled_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_NodeMatcherAcrossSmallAndLargeSpans_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_NotPulledAfterLastSnapshot_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_SingleOpFastPathAndExtraConstantFallback_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_StopsTrackingAfterClearEventsQueue_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_IgnoresPlaceholderBuffers_Test.TestBody), [`ProcessMaterializationTask`](materialize.cc.md#ProcessMaterializationTask), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_RetainsFailedCompletedFutures_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_SyncIgnoresEmptyBuffers_Test.TestBody), [`PrepareSnapshotMaterializations`](events_queue.cc.md#PrepareSnapshotMaterializations), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_IgnoresAlreadyMaterializedBuffers_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_PrunesSuccessfulCompletedFutures_Test.TestBody), [`RecordCompiledExecutionTask`](events_queue.cc.md#RecordCompiledExecutionTask)

