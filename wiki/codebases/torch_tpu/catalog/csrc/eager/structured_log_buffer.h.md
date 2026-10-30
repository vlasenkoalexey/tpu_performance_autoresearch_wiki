---
title: 'Module: csrc/eager/structured_log_buffer.h'
type: catalog
provenance: extracted
module: csrc/eager/structured_log_buffer.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ToString: ToString(a4dcaf028cebc441).
  MaterializationReason: MaterializationReason#
  StructuredLogBuffer: StructuredLogBuffer#
  MaterializationReason.kExplicitSync: MaterializationReason#kExplicitSync.
  StructuredLogEvent: StructuredLogEvent#
  StructuredLogBuffer.DrainResult.events: StructuredLogBuffer#DrainResult#events.
  StructuredLogBuffer.SetEnabledForTest: StructuredLogBuffer#SetEnabledForTest(b45ddcbc8423892c).
  StructuredLogEvent.timestamp: StructuredLogEvent#timestamp.
  StructuredLogBuffer.events_: StructuredLogBuffer#events_.
  StructuredLogBuffer.enabled_: StructuredLogBuffer#enabled_.
  StructuredLogBuffer.dropped_since_last_drain_: StructuredLogBuffer#dropped_since_last_drain_.
  StructuredLogEvent.name: StructuredLogEvent#name.
  MaterializationReason.kUnknown: MaterializationReason#kUnknown.
  StructuredLogBuffer.DrainResult.dropped_since_last_drain: StructuredLogBuffer#DrainResult#dropped_since_last_drain.
  StructuredLogBuffer.mu_: StructuredLogBuffer#mu_.
  StructuredLogBuffer.enabled: StructuredLogBuffer#enabled(50ce9a9e25b4a850).
  StructuredLogBuffer.DrainResult: StructuredLogBuffer#DrainResult#
  MaterializationReason.kCpuTransfer: MaterializationReason#kCpuTransfer.
  StructuredLogEvent.reason: StructuredLogEvent#reason.
  StructuredLogEvent.duration: StructuredLogEvent#duration.
  StructuredLogBuffer.kMaxEvents: StructuredLogBuffer#kMaxEvents.
  MaterializationReason.kDistributedOp: MaterializationReason#kDistributedOp.
  MaterializationReason.kCompileModeExecution: MaterializationReason#kCompileModeExecution.
  MaterializationReason.kDebugMode: MaterializationReason#kDebugMode.
  StructuredLogEvent.mlir_payload: StructuredLogEvent#mlir_payload.
  MaterializationReason.kScalarConversion: MaterializationReason#kScalarConversion.
  StructuredLogEvent.cache_hit: StructuredLogEvent#cache_hit.
  StructuredLogEvent.StructuredLogEvent: StructuredLogEvent#StructuredLogEvent(4ee15765baab6439).
  StructuredLogEvent.operator: StructuredLogEvent#`operator=`(10d86b8ec3f9fe78).
  StructuredLogEvent.compile_failed: StructuredLogEvent#compile_failed.
  MaterializationReason.kRepeatedOpDetection: MaterializationReason#kRepeatedOpDetection.
  StructuredLogEvent.aten_graph_payload: StructuredLogEvent#aten_graph_payload.
  MaterializationReason.kAutogradSync: MaterializationReason#kAutogradSync.
  StructuredLogEvent.chromium_payload: StructuredLogEvent#chromium_payload.
---
# Module: [`csrc/eager/structured_log_buffer.h`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h)

## Classes
### <a id="MaterializationReason"></a>`MaterializationReason`
- def: [`csrc/eager/structured_log_buffer.h:36`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L36) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- doc: Represents the reason for an op materialization event.
- signature: `enum class MaterializationReason`
- members:
  - <a id="MaterializationReason.kAutogradSync"></a>`kAutogradSync` — [`L41`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L41)
  - <a id="MaterializationReason.kCompileModeExecution"></a>`kCompileModeExecution` — [`L45`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L45)
  - <a id="MaterializationReason.kCpuTransfer"></a>`kCpuTransfer` — [`L38`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L38)
  - <a id="MaterializationReason.kDebugMode"></a>`kDebugMode` — [`L43`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L43)
  - <a id="MaterializationReason.kDistributedOp"></a>`kDistributedOp` — [`L44`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L44)
  - <a id="MaterializationReason.kExplicitSync"></a>`kExplicitSync` — [`L40`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L40)
  - <a id="MaterializationReason.kRepeatedOpDetection"></a>`kRepeatedOpDetection` — [`L42`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L42)
  - <a id="MaterializationReason.kScalarConversion"></a>`kScalarConversion` — [`L39`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L39)
  - <a id="MaterializationReason.kUnknown"></a>`kUnknown` — [`L37`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L37)
- used by: [`ToString`](structured_log_buffer.h.md#ToString), [`gather`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.gather), [`PrepareCompiledModeArgumentsImpl`](../internal/compile/compiled_mode.cc.md#PrepareCompiledModeArgumentsImpl), [`AllToAllBaseUnevenSplits`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.AllToAllBaseUnevenSplits), [`AtenEqual`](../ops/equal/equal_aten_kernels.cc.md#AtenEqual), [`EventSnapshot`](events_queue.h.md#EventSnapshot), [`PrepareCompiledModeArgumentsImpl`](../internal/compile/compiled_mode.cc.md#PrepareCompiledModeArgumentsImpl), [`MarkDynamic`](../internal/dynamism/dynamism.cc.md#MarkDynamic), [`outputs`](traversal.h.md#Traversal.outputs), [`TestBody`](materialize_test.cc.md#MaterializeTest_CompilerOptionsPropagateToMaterializeThread_Test.TestBody), [`CopyTpuToCpu`](../ops/copy_from/tpu_to_cpu.cc.md#CopyTpuToCpu), [`MaterializeAndReturn`](tensor_to_buffer.cc.md#MaterializeAndReturn), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_ClearsBuffersAfterMaterialization_Test.TestBody), [`MaybeMaterializeDeviceStateTensor`](device_gen_impl.cc.md#DeviceGeneratorState.MaybeMaterializeDeviceStateTensor), [`TestBody`](shutdown_test.cc.md#ShutdownTest_E2EShutdownCompletes_Test.TestBody), [`TrySyncSingleTensorFast`](../internal/sync/sync_py.cc.md#TrySyncSingleTensorFast), [`TrySyncTensorArrayFast`](../internal/sync/sync_py.cc.md#TrySyncTensorArrayFast), [`GetDynamismInfo`](../internal/dynamism/dynamism.cc.md#GetDynamismInfo), [`SynchronizeTensorsImpl`](../internal/sync/sync.cc.md#SynchronizeTensorsImpl), [`PySyncSpanNoWait`](../internal/sync/sync_py.cc.md#PySyncSpanNoWait), [`ExecutionTask`](execution_task.h.md#ExecutionTask), [`Materialize`](materialize.h.md#Materialize), [`ScheduleAsyncAssertionCheck`](../ops/assertion_aten_kernels.cc.md#ScheduleAsyncAssertionCheck), [`experimental_send`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.experimental_send), [`GetPjrtBuffer`](../experimental/batch_transfer/batch_transfer.cc.md#GetPjrtBuffer), [`Record`](events_queue.cc.md#EventSnapshot.Record), [`synchronizeDevice`](tpu_hooks.cc.md#TpuDeviceGuardImpl.synchronizeDevice), [`synchronizeStream`](tpu_hooks.cc.md#TpuDeviceGuardImpl.synchronizeStream), [`ReadableString`](traversal.cc.md#Traversal.ReadableString), [`DeferNeverDispatch`](device_buffer_utils.cc.md#DeferNeverDispatch), [`TestBody`](traversal_test.cc.md#TraversalTest_ReadableStringWithTraceback_Test.TestBody), [`Materialize`](materialize.cc.md#Materialize), [`MaterializeStream`](materialize.cc.md#MaterializeStream), [`TestBody`](traversal_test.cc.md#TraversalTest_ReadableStringComplexGraph_Test.TestBody), [`TestBody`](traversal_test.cc.md#TraversalTest_ReadableString_Test.TestBody), [`RecordDeviceSnapshots`](events_queue.cc.md#RecordDeviceSnapshots), [`TestBody`](traversal_test.cc.md#TraversalTest_ReadableStringMultiOutput_Test.TestBody), [`TestBody`](traversal_test.cc.md#TraversalTest_ReadableStringReasons_Test.TestBody), [`GetCpuOffsets`](../ops/jagged/jagged_aten_kernels.cc.md#GetCpuOffsets), [`exchangeStream`](tpu_hooks.cc.md#TpuDeviceGuardImpl.exchangeStream)  (+25 more)

### <a id="StructuredLogBuffer"></a>`StructuredLogBuffer`
- def: [`csrc/eager/structured_log_buffer.h:107`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L107)
- doc: A global thread-safe buffer for collecting structured log events.
- signature: `class StructuredLogBuffer`
- members:
  - <a id="StructuredLogBuffer.SetEnabledForTest"></a>`SetEnabledForTest(bool enabled)` — [`L132`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L132) — Overrides the enable state for testing.
  - <a id="StructuredLogBuffer.enabled"></a>`enabled()` — [`L113`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L113) — Returns whether logging is currently enabled.
  - <a id="StructuredLogBuffer.dropped_since_last_drain_"></a>`dropped_since_last_drain_` — [`L142`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L142)
  - <a id="StructuredLogBuffer.enabled_"></a>`enabled_` — [`L138`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L138)
  - <a id="StructuredLogBuffer.events_"></a>`events_` — [`L140`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L140)
  - <a id="StructuredLogBuffer.kMaxEvents"></a>`kMaxEvents` — [`L143`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L143)
  - <a id="StructuredLogBuffer.mu_"></a>`mu_` — [`L139`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L139)
- uses (calls/refs, reference-scoped): [`Push`](structured_log_buffer.cc.md#StructuredLogBuffer.Push), [`GetInstance`](structured_log_buffer.cc.md#StructuredLogBuffer.GetInstance), [`StructuredLogEvent`](structured_log_buffer.h.md#StructuredLogEvent), [`StructuredLogBuffer`](structured_log_buffer.cc.md#StructuredLogBuffer.StructuredLogBuffer)
- used by: [`FinalizePushTraceEvent`](execution_task.cc.md#FinalizePushTraceEvent), [`Push`](structured_log_buffer.cc.md#StructuredLogBuffer.Push), [`Drain`](structured_log_buffer.cc.md#StructuredLogBuffer.Drain), [`GetInstance`](structured_log_buffer.cc.md#StructuredLogBuffer.GetInstance), [`MaybeStartTraceEvent`](execution_task.cc.md#MaybeStartTraceEvent), [`TestBody`](structured_log_buffer_test.cc.md#StructuredLogBufferTest_PushDrainRoundtrip_Test.TestBody), [`TestBody`](structured_log_buffer_test.cc.md#StructuredLogBufferTest_ConcurrentPushIsSafe_Test.TestBody), [`TestBody`](structured_log_buffer_test.cc.md#StructuredLogBufferTest_DrainWhileDisabledReturnsEmpty_Test.TestBody), [`TestBody`](structured_log_buffer_test.cc.md#StructuredLogBufferTest_FifoEviction_Test.TestBody), [`TestBody`](structured_log_buffer_test.cc.md#StructuredLogBufferTest_DisabledBufferDropsEvents_Test.TestBody), [`~StructuredLogBufferTest`](structured_log_buffer_test.cc.md#StructuredLogBufferTest.-StructuredLogBufferTest), [`StructuredLogBufferTest`](structured_log_buffer_test.cc.md#StructuredLogBufferTest.StructuredLogBufferTest), [`StructuredLogBuffer`](structured_log_buffer.cc.md#StructuredLogBuffer.StructuredLogBuffer)

### <a id="StructuredLogBuffer.DrainResult"></a>`StructuredLogBuffer.DrainResult`
- def: [`csrc/eager/structured_log_buffer.h:121`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L121)
- signature: `struct DrainResult`
- members:
  - <a id="StructuredLogBuffer.DrainResult.dropped_since_last_drain"></a>`dropped_since_last_drain` — [`L123`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L123)
  - <a id="StructuredLogBuffer.DrainResult.events"></a>`events` — [`L122`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L122)
- uses (calls/refs, reference-scoped): [`Drain`](structured_log_buffer.cc.md#StructuredLogBuffer.Drain), [`StructuredLogEvent`](structured_log_buffer.h.md#StructuredLogEvent)
- used by: [`Push`](structured_log_buffer.cc.md#StructuredLogBuffer.Push), [`TestBody`](structured_log_buffer_test.cc.md#StructuredLogBufferTest_PushDrainRoundtrip_Test.TestBody), [`TestBody`](structured_log_buffer_test.cc.md#StructuredLogBufferTest_ConcurrentPushIsSafe_Test.TestBody), [`TestBody`](structured_log_buffer_test.cc.md#StructuredLogBufferTest_DrainWhileDisabledReturnsEmpty_Test.TestBody), [`TestBody`](structured_log_buffer_test.cc.md#StructuredLogBufferTest_FifoEviction_Test.TestBody), [`TestBody`](structured_log_buffer_test.cc.md#StructuredLogBufferTest_DisabledBufferDropsEvents_Test.TestBody)

### <a id="StructuredLogEvent"></a>`StructuredLogEvent`
- def: [`csrc/eager/structured_log_buffer.h:74`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L74)
- doc: A structured log event representing a materialization event or other eager
- signature: `struct StructuredLogEvent`
- members:
  - `StructuredLogEvent()` — [`L75`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L75)
  - <a id="StructuredLogEvent.StructuredLogEvent"></a>`StructuredLogEvent(const StructuredLogEvent&)` — [`L79`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L79) — Disable move and copy to force storing unique_ptr in containers and to
  - `StructuredLogEvent(StructuredLogEvent&&)` — [`L81`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L81)
  - <a id="StructuredLogEvent.operator"></a>`operator=(StructuredLogEvent&&)` — [`L82`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L82)
  - `operator=(const StructuredLogEvent&)` — [`L80`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L80)
  - <a id="StructuredLogEvent.aten_graph_payload"></a>`aten_graph_payload` — [`L94`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L94) — FX-style ATen graph with inline source locations. Populated on cache
  - <a id="StructuredLogEvent.cache_hit"></a>`cache_hit` — [`L91`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L91) — Whether the PJRT executable was already in the compilation cache.
  - <a id="StructuredLogEvent.chromium_payload"></a>`chromium_payload` — [`L101`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L101) — Pre-serialized JSON for the chromium_event payload.
  - <a id="StructuredLogEvent.compile_failed"></a>`compile_failed` — [`L103`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L103) — True if compilation failed.
  - <a id="StructuredLogEvent.duration"></a>`duration` — [`L89`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L89) — Duration from event start to event end.
  - <a id="StructuredLogEvent.mlir_payload"></a>`mlir_payload` — [`L97`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L97) — StableHLO MLIR text with #loc debug info. Populated on cache miss;
  - <a id="StructuredLogEvent.name"></a>`name` — [`L85`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L85) — Event name, e.g. "torchtpu_eager/kMm+kAdd".
  - <a id="StructuredLogEvent.reason"></a>`reason` — [`L99`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L99) — Why this materialization was triggered.
  - <a id="StructuredLogEvent.timestamp"></a>`timestamp` — [`L87`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L87) — Wall-clock time the event started.
- uses (calls/refs, reference-scoped): [`MaterializationReason`](structured_log_buffer.h.md#MaterializationReason), [`kUnknown`](structured_log_buffer.h.md#MaterializationReason.kUnknown)
- used by: [`FinalizePushTraceEvent`](execution_task.cc.md#FinalizePushTraceEvent), [`PropagateBoundedDynamism`](execution_task.cc.md#PropagateBoundedDynamism), [`Push`](structured_log_buffer.cc.md#StructuredLogBuffer.Push), [`MaybeStartTraceEvent`](execution_task.cc.md#MaybeStartTraceEvent), [`TestBody`](structured_log_buffer_test.cc.md#StructuredLogBufferTest_PushDrainRoundtrip_Test.TestBody), [`TestBody`](structured_log_buffer_test.cc.md#StructuredLogBufferTest_ConcurrentPushIsSafe_Test.TestBody), [`TestBody`](structured_log_buffer_test.cc.md#StructuredLogBufferTest_DrainWhileDisabledReturnsEmpty_Test.TestBody), [`TestBody`](structured_log_buffer_test.cc.md#StructuredLogBufferTest_FifoEviction_Test.TestBody), [`TestBody`](structured_log_buffer_test.cc.md#StructuredLogBufferTest_DisabledBufferDropsEvents_Test.TestBody), [`mu_`](structured_log_buffer.h.md#StructuredLogBuffer.mu_), [`enabled`](structured_log_buffer.h.md#StructuredLogBuffer.enabled), [`DrainResult`](structured_log_buffer.h.md#StructuredLogBuffer.DrainResult)

## Functions
- <a id="ToString"></a>`ToString(MaterializationReason reason)` — [`L48`](../../../../../../raw/code/torch_tpu/csrc/eager/structured_log_buffer.h#L48) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)

