---
title: 'Module: csrc/common/context_states.h'
type: catalog
provenance: extracted
module: csrc/common/context_states.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  EagerMode: EagerMode#
  EagerMode.kDeferNever: EagerMode#kDeferNever.
  EagerMode.kDeferAndFuse: EagerMode#kDeferAndFuse.
  EagerMode.kInternalCompileFxGraph: EagerMode#kInternalCompileFxGraph.
  EagerMode.kDeferNeverAndLaunchBlocking: EagerMode#kDeferNeverAndLaunchBlocking.
  EagerModeContextState: EagerModeContextState#
  TracebackMode: TracebackMode#
  EnableTracebacksContextState: EnableTracebacksContextState#
  EagerMode.kInternalDeferAll: EagerMode#kInternalDeferAll.
  CustomCompilerOptionsContextState: CustomCompilerOptionsContextState#
  ProfileContextState: ProfileContextState#
  TracebackMode.kEnabled: TracebackMode#kEnabled.
  PrecisionContextState: PrecisionContextState#
  ProfilerStatus: ProfilerStatus#
  TracebackMode.kDisabled: TracebackMode#kDisabled.
  ProfilerStatus.kEnabled: ProfilerStatus#kEnabled.
  IsSpmdSafeContextState: IsSpmdSafeContextState#
  LayoutContextState: LayoutContextState#
  ProfilerStatus.kDisabled: ProfilerStatus#kDisabled.
---
# Module: [`csrc/common/context_states.h`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h)

## Classes
### <a id="CustomCompilerOptionsContextState"></a>`CustomCompilerOptionsContextState`
- def: [`csrc/common/context_states.h:102`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L102)
- doc: The state of the `custom_compiler_options` context manager.
- signature: `using CustomCompilerOptionsContextState = absl_nonnull std::shared_ptr<const CompilationContext>`
- uses (calls/refs, reference-scoped): [`CompilationContext`](compilation_spec.h.md#CompilationContext)
- used by: [`MakeCompilationSpecs`](compilation.cc.md#MakeCompilationSpecs), [`PushCompilerOptionOverrides`](compilation.cc.md#PushCompilerOptionOverrides), [`GetCompilationContext`](compilation.cc.md#GetCompilationContext), [`PopCompilerOptionOverrides`](compilation.cc.md#PopCompilerOptionOverrides), [`MakeCompilationContext`](compilation.cc.md#MakeCompilationContext), [`ContextManagerState`](context_manager.h.md#ContextManagerState), [`GetDefaultCompilationContext`](compilation.cc.md#GetDefaultCompilationContext)

### <a id="EagerMode"></a>`EagerMode`
- def: [`csrc/common/context_states.h:35`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L35) — documented in [context-states-and-execution-modes](../../../concepts/context-states-and-execution-modes.md)
- doc: The op defer mode.
- signature: `enum class EagerMode`
- members:
  - `kDeferAndFuse` — [`L38`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L38) — kDeferAndFuse defers all ops except those that cannot be deferred.  This
  - <a id="EagerMode.kDeferAndFuse"></a>`kDeferAndFuse` — [`L38`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L38) — kDeferAndFuse defers all ops except those that cannot be deferred.  This
  - <a id="EagerMode.kDeferNever"></a>`kDeferNever` — [`L42`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L42) — kDeferNever marks all ops to be executed immediately, similarly to PyTorch
  - `kDeferNever` — [`L42`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L42) — kDeferNever marks all ops to be executed immediately, similarly to PyTorch
  - <a id="EagerMode.kDeferNeverAndLaunchBlocking"></a>`kDeferNeverAndLaunchBlocking` — [`L48`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L48) — kDeferNeverAndLaunchBlocking marks all ops to be executed immediately and
  - `kDeferNeverAndLaunchBlocking` — [`L48`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L48) — kDeferNeverAndLaunchBlocking marks all ops to be executed immediately and
  - <a id="EagerMode.kInternalCompileFxGraph"></a>`kInternalCompileFxGraph` — [`L58`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L58) — kInternalCompileFxGraph fully prevents all eager mode operations from
  - `kInternalCompileFxGraph` — [`L58`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L58) — kInternalCompileFxGraph fully prevents all eager mode operations from
  - `kInternalDeferAll` — [`L54`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L54) — kInternalDeferAll attempts to defer all ops. If an op cannot be deferred,
  - <a id="EagerMode.kInternalDeferAll"></a>`kInternalDeferAll` — [`L54`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L54) — kInternalDeferAll attempts to defer all ops. If an op cannot be deferred,
- used by: [`GetEnableDebugChecks`](error_utils.cc.md#GetEnableDebugChecks), [`RecordDeferredOpCreated`](../eager/events_queue.cc.md#RecordDeferredOpCreated), [`CreateDeferredDeviceBufferList`](../eager/device_buffer_utils.cc.md#CreateDeferredDeviceBufferList), [`RecordNewDataPtrCreated`](../eager/events_queue.cc.md#RecordNewDataPtrCreated), [`MarkDynamic`](../internal/dynamism/dynamism.cc.md#MarkDynamic), [`SetEagerMode`](../eager/eager_mode.cc.md#SetEagerMode), [`MakeBuffer`](../eager/op_dispatcher.cc.md#MakeBuffer), [`TestBody`](../eager/op_dispatcher_test.cc.md#AutoDonateInPlaceBuffers_MultiOutputDeviceBufferListTracksPerSlotLiveDataPtrs_Test.TestBody), [`MaybeMaterializeDeviceStateTensor`](../eager/device_gen_impl.cc.md#DeviceGeneratorState.MaybeMaterializeDeviceStateTensor), [`GetDynamismInfo`](../internal/dynamism/dynamism.cc.md#GetDynamismInfo), [`GetDefaultGenerator`](../eager/device_gen_impl.cc.md#DeviceGenerators.GetDefaultGenerator), [`GetTracebackMode`](../ops/python_context.cc.md#GetTracebackMode), [`TestBody`](../eager/op_dispatcher_test.cc.md#OpDispatcher_OutputCastingWithoutComputationDtype_Test.TestBody), [`LowerAndVerify`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest.LowerAndVerify), [`TorchTpuPyBindInitModule_execution_mode_impl`](../internal/execution_mode/execution_mode_impl.cc.md#TorchTpuPyBindInitModule_execution_mode_impl), [`GetCompilationMode`](../eager/events_queue.cc.md#GetCompilationMode), [`TestBody`](../eager/op_dispatcher_test.cc.md#AutoDonateInPlaceBuffers_DoesNotDonateSharedBufferWithMultipleLiveDataPtrs_Test.TestBody), [`Record`](../eager/events_queue.cc.md#EventSnapshot.Record), [`RecordDeviceSnapshots`](../eager/events_queue.cc.md#RecordDeviceSnapshots), [`RecordAsyncDeviceToHost`](../eager/events_queue.cc.md#RecordAsyncDeviceToHost), [`RequestEventSnapshotLocked`](../eager/events_queue.cc.md#StreamState.RequestEventSnapshotLocked), [`TestBody`](../eager/defer_and_fuse_enablement_test.cc.md#DeferAndFuseEnablementTest_EagerMode_Test.TestBody), [`TestBody`](../eager/launch_blocking_enablement_test.cc.md#LaunchBlockingEnablementTest_EagerMode_Test.TestBody), [`RecordAsyncHostToDevice`](../eager/events_queue.cc.md#RecordAsyncHostToDevice), [`RecordDataPtrDestroyed`](../eager/events_queue.cc.md#RecordDataPtrDestroyed), [`TestBody`](../eager/events_queue_test.cc.md#CompilationModeTest_GetCompilationMode_Test.TestBody), [`TestBody`](../eager/op_dispatcher_test.cc.md#AutoDonateInPlaceBuffer_EligibilityAndAliasingTests_Test.TestBody), [`TestBody`](../eager/op_dispatcher_test.cc.md#AutoDonateInPlaceBuffers_CannotDonateBufferMultipleTimes_Test.TestBody), [`TestBody`](../eager/op_dispatcher_test.cc.md#AutoDonateInPlaceBuffers_MultiOutputDonation_Test.TestBody), [`RecordCompiledExecutionTask`](../eager/events_queue.cc.md#StreamState.RecordCompiledExecutionTask), [`RecordCompiledExecutionTask`](../eager/events_queue.cc.md#RecordCompiledExecutionTask), [`TestBody`](../eager/op_dispatcher_test.cc.md#AutoDonateInPlaceBuffer_DetectsDonation_Test.TestBody), [`snapshot_future`](../eager/events_queue.h.md#PendingEventSnapshot.snapshot_future), [`RecordDeferredOpAndDetectRepetition`](../eager/events_queue.cc.md#RecordDeferredOpAndDetectRepetition), [`TestBody`](context_state_access_test.cc.md#ContextStateMutation_IsAllowedByDefault_Test.TestBody), [`TestBody`](../ops/op_builder_utils_test.cc.md#EagerModeTest_IsDeferNeverMode_Test.TestBody), [`IsDeferNeverMode`](../eager/eager_mode.h.md#IsDeferNeverMode), [`TestBody`](context_state_access_test.cc.md#ContextStateMutationDeathTest_CrashOnPushAndPopContextStateIfDisallowed_Test.TestBody), [`TestBody`](error_utils_test.cc.md#GetEnableDebugChecksDeathTest_CanBeDisabledByEnvVarInDebugMode_Test.TestBody), [`TestBody`](error_utils_test.cc.md#GetEnableDebugChecksDeathTest_CanBeEnabledByEnvVarInDebugMode_Test.TestBody)  (+10 more)

### `EagerModeContextState`
- def: [`csrc/common/context_states.h:62`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L62)
- doc: The state of the `eager_mode` context manager.
- signature: `using EagerModeContextState = EagerMode`
- uses (calls/refs, reference-scoped): [`EagerMode`](context_states.h.md#EagerMode), [`EagerMode`](context_states.h.md#EagerMode)

### <a id="EnableTracebacksContextState"></a>`EnableTracebacksContextState`
- def: [`csrc/common/context_states.h:96`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L96)
- doc: The state of the `enable_tracebacks` context manager.
- signature: `using EnableTracebacksContextState = std::optional<TracebackMode>`
- uses (calls/refs, reference-scoped): [`TracebackMode`](context_states.h.md#TracebackMode)
- used by: [`TorchTpuPyBindInitModule_tpu_torch_compile`](../internal/compile/tpu_torch_compile.cc.md#TorchTpuPyBindInitModule_tpu_torch_compile), [`GetTracebackMode`](../ops/python_context.cc.md#GetTracebackMode), [`TestBody`](../ops/python_context_test.cc.md#ScopedPythonContextCapturerTrackebackTest_CapturesTracebackWhenEnabled_Test.TestBody), [`TestBody`](../ops/python_context_test.cc.md#ScopedPythonContextCapturerTrackebackTest_DoesNotCaptureTracebackWhenDisabled_Test.TestBody), [`ContextManagerState`](context_manager.h.md#ContextManagerState), [`PyPushEnableTracebacks`](../internal/compile/tpu_torch_compile.cc.md#PyPushEnableTracebacks), [`~ScopedPythonContextCapturerTrackebackTest`](../ops/python_context_test.cc.md#ScopedPythonContextCapturerTrackebackTest.-ScopedPythonContextCapturerTrackebackTest)

### <a id="IsSpmdSafeContextState"></a>`IsSpmdSafeContextState`
- def: [`csrc/common/context_states.h:99`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L99)
- doc: The state of the `spmd_safe` context manager.
- signature: `using IsSpmdSafeContextState = bool`
- used by: [`ContextManagerState`](context_manager.h.md#ContextManagerState), [`EnterSpmdSafeRegion`](../distributed/utils.cc.md#EnterSpmdSafeRegion), [`IsSpmdSafe`](../distributed/utils.cc.md#IsSpmdSafe), [`ExitSpmdSafeRegion`](../distributed/utils.cc.md#ExitSpmdSafeRegion)

### <a id="LayoutContextState"></a>`LayoutContextState`
- def: [`csrc/common/context_states.h:106`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L106)
- doc: The state of the `layout` context manager.
- signature: `using LayoutContextState = absl_nonnull std::shared_ptr<const xla::Layout>`
- used by: [`TpuMallocAndMemcpyHtoD`](../pjrt/pjrt_transfer.cc.md#TpuMallocAndMemcpyHtoD), [`ContextManagerState`](context_manager.h.md#ContextManagerState)

### <a id="PrecisionContextState"></a>`PrecisionContextState`
- def: [`csrc/common/context_states.h:70`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L70)
- doc: The state of the `precision` context manager. If the state is empty
- signature: `using PrecisionContextState = mlir::stablehlo::Precision`
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`PyUnsafeGetPrecision`](../ops/precision_context.cc.md#PyUnsafeGetPrecision), [`ContextManagerState`](context_manager.h.md#ContextManagerState), [`PyPopPrecision`](../ops/precision_context.cc.md#PyPopPrecision), [`PyPushPrecision`](../ops/precision_context.cc.md#PyPushPrecision)

### `ProfileContextState`
- def: [`csrc/common/context_states.h:83`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L83)
- doc: The state of the `profile` context manager.
- signature: `using ProfileContextState = ProfilerStatus`

### `ProfilerStatus`
- def: [`csrc/common/context_states.h:72`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L72)
- signature: `enum class ProfilerStatus`
- members:
  - <a id="ProfilerStatus.kDisabled"></a>`kDisabled` — [`L74`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L74) — By default, profiling is disabled.
  - `kDisabled` — [`L74`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L74) — By default, profiling is disabled.
  - <a id="ProfilerStatus.kEnabled"></a>`kEnabled` — [`L77`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L77) — Enables the collection of performance metrics by scoping the code region
  - `kEnabled` — [`L77`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L77) — Enables the collection of performance metrics by scoping the code region
- used by: [`TorchTpuPyBindInitModule__profiler_backend`](../internal/profiler/profiler_api.cc.md#TorchTpuPyBindInitModule__profiler_backend), [`IsProfilerEnabled`](../internal/profiler/xprof_callback_handler.cc.md#IsProfilerEnabled), [`ProfileContextState`](context_states.h.md#ProfileContextState)

### `TracebackMode`
- def: [`csrc/common/context_states.h:86`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L86)
- doc: Whether to capture tracebacks for each dispatched op.
- signature: `enum class TracebackMode`
- members:
  - <a id="TracebackMode.kDisabled"></a>`kDisabled` — [`L89`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L89) — Tracebacks are not captured. This is the default for eager mode, where MLIR
  - `kDisabled` — [`L89`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L89) — Tracebacks are not captured. This is the default for eager mode, where MLIR
  - <a id="TracebackMode.kEnabled"></a>`kEnabled` — [`L92`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L92) — Tracebacks are captured for each dispatched op. This is the default for
  - `kEnabled` — [`L92`](../../../../../../raw/code/torch_tpu/csrc/common/context_states.h#L92) — Tracebacks are captured for each dispatched op. This is the default for
- used by: [`GetTracebackMode`](../ops/python_context.cc.md#GetTracebackMode), [`ScopedPythonContextCapturer`](../ops/python_context.cc.md#ScopedPythonContextCapturer.ScopedPythonContextCapturer), [`TestBody`](../ops/python_context_test.cc.md#ScopedPythonContextCapturerTrackebackTest_CapturesTracebackWhenEnabled_Test.TestBody), [`TestBody`](../ops/python_context_test.cc.md#ScopedPythonContextCapturerTrackebackTest_DoesNotCaptureTracebackWhenDisabled_Test.TestBody), [`PyPushEnableTracebacks`](../internal/compile/tpu_torch_compile.cc.md#PyPushEnableTracebacks)

