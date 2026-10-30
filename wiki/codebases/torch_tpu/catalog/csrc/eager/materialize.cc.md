---
title: 'Module: csrc/eager/materialize.cc'
type: catalog
provenance: extracted
module: csrc/eager/materialize.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  MaterializeSpan.DeviceStreamId.stream_id: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializeSpan(a0adf3802245067c).DeviceStreamId#stream_id.'
  ApplySplitMode: '`$anonymous_namespace_csrc/eager/materialize.cc`/ApplySplitMode(920c63349a102936).'
  EnqueueExecutable: EnqueueExecutable(ef12c5e94b3b3da9).
  ProcessMaterializationTask: '`$anonymous_namespace_csrc/eager/materialize.cc`/ProcessMaterializationTask(17dd8c60cc54ca4b).'
  Materialize: Materialize(39220b83e86caf3a).
  MaterializeStream: MaterializeStream(abbc8cc363a8354b).
  GetUniqueDeferredNodes: '`$anonymous_namespace_csrc/eager/materialize.cc`/GetUniqueDeferredNodes(f044f1bbdf739e68).'
  VerifyMustMaterialize: '`$anonymous_namespace_csrc/eager/materialize.cc`/VerifyMustMaterialize(510097683365e48).'
  MaterializationWorker.FailRemainingExecutionTasks: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#FailRemainingExecutionTasks(49f6e7a06ebc5aa8).'
  PruneTraversalPlaceholderOutputs: '`$anonymous_namespace_csrc/eager/materialize.cc`/PruneTraversalPlaceholderOutputs(515063fe650a92aa).'
  MaterializeDevice: MaterializeDevice(6f4824d70d15e8c2).
  MaterializationWorker.MaterializeLoopStep: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#MaterializeLoopStep(98cac40c0c232ec6).'
  GetCompilationSpecForTraversal: '`$anonymous_namespace_csrc/eager/materialize.cc`/GetCompilationSpecForTraversal(1176b1c2d0afcb81).'
  MaterializationWorker.ExecuteLoop: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#ExecuteLoop(49f6e7a06ebc5aa8).'
  MarkPinnedHostOutputs: '`$anonymous_namespace_csrc/eager/materialize.cc`/MarkPinnedHostOutputs(4f04b8e939e7015a).'
  MaterializeCurrentStream: MaterializeCurrentStream(8bdb50bc92fe7f62).
  MaterializationWorker.Shutdown: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#Shutdown(49f6e7a06ebc5aa8).'
  ShutDownMaterializationState: ShutDownMaterializationState(49f6e7a06ebc5aa8).
  DependsOnPlaceholder: '`$anonymous_namespace_csrc/eager/materialize.cc`/DependsOnPlaceholder(79102fba68a55a9).'
  SplitSingleTraversal: '`$anonymous_namespace_csrc/eager/materialize.cc`/SplitSingleTraversal(aec9ba2deac1127).'
  MaterializationWorker.EnqueueStream: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#EnqueueStream(e47f6fad7fb342d).'
  HasAnyPlaceholderArgumentOrOutput: '`$anonymous_namespace_csrc/eager/materialize.cc`/HasAnyPlaceholderArgumentOrOutput(6f6b9c6fdb5063a4).'
  OutputDependsOnPlaceholder: '`$anonymous_namespace_csrc/eager/materialize.cc`/OutputDependsOnPlaceholder(f8f37cd7b4c82ac5).'
  MaterializationWorker.execute_tasks_: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#execute_tasks_.'
  FilterPlaceholderDependentTraversals: '`$anonymous_namespace_csrc/eager/materialize.cc`/FilterPlaceholderDependentTraversals(ab89b2e39be56ccb).'
  MaterializationWorker.DequeueMaterializationTask: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#DequeueMaterializationTask(bec683e1656c204c).'
  MaterializationWorker.MaterializeLoop: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#MaterializeLoop(49f6e7a06ebc5aa8).'
  GetDeviceBufferList: '`$anonymous_namespace_csrc/eager/materialize.cc`/GetDeviceBufferList(72f3b0816b25690a).'
  GetMaterializationWorker: '`$anonymous_namespace_csrc/eager/materialize.cc`/GetMaterializationWorker(a459a534209a5dbc).'
  MaterializeSpan: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializeSpan(a0adf3802245067c).'
  MaterializationStages.first_error: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationStages#first_error.'
  MaterializationWorker.DequeueExecutionTask: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#DequeueExecutionTask(1342c0bfe901fc22).'
  MaterializationWorker.StartThreads: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#StartThreads(49f6e7a06ebc5aa8).'
  MaterializationWorker.materialize_tasks_: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#materialize_tasks_.'
  MaterializationStages.execution_tasks: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationStages#execution_tasks.'
  MaterializationWorker: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#'
  MaterializationWorker.execute_mu_: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#execute_mu_.'
  ExecutionOrShutdown: '`$anonymous_namespace_csrc/eager/materialize.cc`/ExecutionOrShutdown#'
  MaterializationOrShutdown: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationOrShutdown#'
  MaterializationWorker.materialize_mu_: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#materialize_mu_.'
  ShutdownSentinel: '`$anonymous_namespace_csrc/eager/materialize.cc`/ShutdownSentinel#'
  MaterializationStages: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationStages#'
  MaterializationWorker.-MaterializationWorker: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#`~MaterializationWorker`(ced63f7c635d850d).'
  MaterializationWorker.shutdown_: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#shutdown_.'
  MaterializationTask: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationTask#'
  MaterializeSpan.DeviceStreamId: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializeSpan(a0adf3802245067c).DeviceStreamId#'
  MaterializationTask.stream_id: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationTask#stream_id.'
  MaterializationWorker.execute_thread_: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#execute_thread_.'
  MaterializationTask.device_index: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationTask#device_index.'
  MaterializationWorker.materialize_thread_: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#materialize_thread_.'
  MaterializationWorker.MaterializationWorker: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#MaterializationWorker(49f6e7a06ebc5aa8).'
  MaterializationWorker.operator: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializationWorker#`operator=`(a1b27c96d02130f7).'
  MaterializeSpan.DeviceStreamId.device_index: '`$anonymous_namespace_csrc/eager/materialize.cc`/MaterializeSpan(a0adf3802245067c).DeviceStreamId#device_index.'
---
# Module: [`csrc/eager/materialize.cc`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc)

## Classes
### <a id="ExecutionOrShutdown"></a>`ExecutionOrShutdown`
- def: [`csrc/eager/materialize.cc:445`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L445)
- signature: `using ExecutionOrShutdown = std::variant<ShutdownSentinel, ExecutionTask>`
- uses (calls/refs, reference-scoped): [`ExecutionTask`](execution_task.h.md#ExecutionTask), [`ShutdownSentinel`](materialize.cc.md#ShutdownSentinel)
- used by: [`DequeueMaterializationTask`](materialize.cc.md#MaterializationWorker.DequeueMaterializationTask), [`DequeueExecutionTask`](materialize.cc.md#MaterializationWorker.DequeueExecutionTask), [`execute_mu_`](materialize.cc.md#MaterializationWorker.execute_mu_)

### <a id="MaterializationOrShutdown"></a>`MaterializationOrShutdown`
- def: [`csrc/eager/materialize.cc:443`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L443)
- signature: `using MaterializationOrShutdown = std::variant<ShutdownSentinel, MaterializationTask>`
- uses (calls/refs, reference-scoped): [`ShutdownSentinel`](materialize.cc.md#ShutdownSentinel), [`MaterializationTask`](materialize.cc.md#MaterializationTask)
- used by: [`EnqueueStream`](materialize.cc.md#MaterializationWorker.EnqueueStream), [`DequeueMaterializationTask`](materialize.cc.md#MaterializationWorker.DequeueMaterializationTask), [`materialize_mu_`](materialize.cc.md#MaterializationWorker.materialize_mu_)

### <a id="MaterializationStages"></a>`MaterializationStages`
- def: [`csrc/eager/materialize.cc:103`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L103)
- doc: When preparing a list of Traversals into a sequence of ExecutionTasks,
- signature: `struct MaterializationStages`
- members:
  - <a id="MaterializationStages.execution_tasks"></a>`execution_tasks` — [`L104`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L104)
  - <a id="MaterializationStages.first_error"></a>`first_error` — [`L105`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L105)
- uses (calls/refs, reference-scoped): [`ExecutionTask`](execution_task.h.md#ExecutionTask), [`CompilationSpec`](../common/compilation_spec.h.md#CompilationSpec)
- used by: [`ApplySplitMode`](materialize.cc.md#ApplySplitMode), [`ProcessMaterializationTask`](materialize.cc.md#ProcessMaterializationTask), [`FilterPlaceholderDependentTraversals`](materialize.cc.md#FilterPlaceholderDependentTraversals)

### <a id="MaterializationTask"></a>`MaterializationTask`
- def: [`csrc/eager/materialize.cc:80`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L80)
- doc: A task to materialize a stream.
- signature: `struct MaterializationTask`
- members:
  - <a id="MaterializationTask.device_index"></a>`device_index` — [`L81`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L81)
  - <a id="MaterializationTask.stream_id"></a>`stream_id` — [`L82`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L82)
- used by: [`ProcessMaterializationTask`](materialize.cc.md#ProcessMaterializationTask), [`MaterializeLoopStep`](materialize.cc.md#MaterializationWorker.MaterializeLoopStep), [`EnqueueStream`](materialize.cc.md#MaterializationWorker.EnqueueStream), [`MaterializationOrShutdown`](materialize.cc.md#MaterializationOrShutdown)

### <a id="MaterializationWorker"></a>`MaterializationWorker`
- def: [`csrc/eager/materialize.cc:447`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L447)
- signature: `class MaterializationWorker`
- members:
  - <a id="MaterializationWorker.DequeueExecutionTask"></a>`DequeueExecutionTask()` — [`L510`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L510) — Dequeues an execution task or a shutdown signal.
  - <a id="MaterializationWorker.DequeueMaterializationTask"></a>`DequeueMaterializationTask()` — [`L497`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L497) — Dequeues a materialization task or a shutdown signal.
  - <a id="MaterializationWorker.EnqueueStream"></a>`EnqueueStream(const c10::DeviceIndex device_index, const c10::StreamId stream_id)` — [`L485`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L485)
  - <a id="MaterializationWorker.ExecuteLoop"></a>`ExecuteLoop()` — [`L566`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L566)
  - <a id="MaterializationWorker.FailRemainingExecutionTasks"></a>`FailRemainingExecutionTasks()` — [`L589`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L589)
  - <a id="MaterializationWorker.MaterializationWorker"></a>`MaterializationWorker()` — [`L455`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L455)
  - `MaterializationWorker(const MaterializationWorker&)` — [`L452`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L452)
  - `MaterializationWorker(MaterializationWorker&& other)` — [`L450`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L450) — This class is move-only.
  - <a id="MaterializationWorker.MaterializeLoop"></a>`MaterializeLoop()` — [`L548`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L548)
  - <a id="MaterializationWorker.MaterializeLoopStep"></a>`MaterializeLoopStep(mlir::MLIRContext& mlir_context)` — [`L529`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L529) — Processes a single materialization task.
  - <a id="MaterializationWorker.Shutdown"></a>`Shutdown()` — [`L462`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L462) — Shuts down the worker threads. Reordering the shutdown sequence ensures
  - <a id="MaterializationWorker.StartThreads"></a>`StartThreads()` — [`L520`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L520)
  - <a id="MaterializationWorker.operator"></a>`operator=(const MaterializationWorker&)` — [`L453`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L453)
  - `operator=(MaterializationWorker&& other)` — [`L451`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L451)
  - <a id="MaterializationWorker.-MaterializationWorker"></a>`~MaterializationWorker()` — [`L457`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L457)
  - <a id="MaterializationWorker.execute_mu_"></a>`execute_mu_` — [`L624`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L624)
  - <a id="MaterializationWorker.execute_tasks_"></a>`execute_tasks_` — [`L627`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L627) — Queue of execution tasks. Storing std::variant allows enqueuing
  - <a id="MaterializationWorker.execute_thread_"></a>`execute_thread_` — [`L612`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L612)
  - <a id="MaterializationWorker.materialize_mu_"></a>`materialize_mu_` — [`L618`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L618)
  - <a id="MaterializationWorker.materialize_tasks_"></a>`materialize_tasks_` — [`L621`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L621) — Queue of materialization tasks. Storing std::variant allows enqueuing
  - <a id="MaterializationWorker.materialize_thread_"></a>`materialize_thread_` — [`L611`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L611)
  - <a id="MaterializationWorker.shutdown_"></a>`shutdown_` — [`L616`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L616) — Set to true when the MaterializationWorker is undergoing shutdown,
- uses (calls/refs, reference-scoped): [`NormalizeIfInsideBuildDirectory`](../common/macro_utils.cc.md#NormalizeIfInsideBuildDirectory), [`MaybeAddCppSourceLoc`](../common/status_builder.cc.md#MaybeAddCppSourceLoc), [`GetRootOpName`](../ops/python_context.cc.md#GetRootOpName), [`SetRootOpNamePayload`](../common/status_builder.cc.md#SetRootOpNamePayload), [`StatusBuilder`](../common/status_builder.h.md#StatusBuilder), [`operator<<`](../common/status_builder.h.md#StatusBuilder.operator), [`operator<<`](../ops/op_names.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`operator<<`](../common/cache_key.cc.md#operator), [`StatusBuilder`](../common/status_builder.cc.md#StatusBuilder.StatusBuilder), [`ExecutionTask`](execution_task.h.md#ExecutionTask), [`DisallowThisThreadToAccessContextState`](../common/context_manager.cc.md#DisallowThisThreadToAccessContextState), [`MakeMlirContext`](../common/compilation.cc.md#MakeMlirContext), [`RouteWarningsOnThisThreadToDispatchThread`](../common/reroute_warnings.cc.md#RouteWarningsOnThisThreadToDispatchThread), [`SetOutputNodesAsError`](execution_task.cc.md#ExecutionTask.SetOutputNodesAsError), [`Run`](execution_task.cc.md#ExecutionTask.Run), [`ExecutionOrShutdown`](materialize.cc.md#ExecutionOrShutdown), [`MaterializationOrShutdown`](materialize.cc.md#MaterializationOrShutdown), [`ShutdownSentinel`](materialize.cc.md#ShutdownSentinel), [`MaterializationTask`](materialize.cc.md#MaterializationTask), [`kCancelled`](../common/error_utils.h.md#kCancelled), [`ProcessMaterializationTask`](materialize.cc.md#ProcessMaterializationTask)
- used by: [`stream_id`](materialize.cc.md#MaterializeSpan.DeviceStreamId.stream_id), [`EnqueueExecutable`](materialize.cc.md#EnqueueExecutable), [`MaterializeStream`](materialize.cc.md#MaterializeStream), [`MaterializeDevice`](materialize.cc.md#MaterializeDevice), [`ShutDownMaterializationState`](materialize.cc.md#ShutDownMaterializationState), [`GetMaterializationWorker`](materialize.cc.md#GetMaterializationWorker)

### <a id="MaterializeSpan.DeviceStreamId"></a>`MaterializeSpan.DeviceStreamId`
- def: [`csrc/eager/materialize.cc:739`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L739)
- doc: In the majority of cases, we expect that there will very few distinct
- signature: `struct DeviceStreamId`
- members:
  - <a id="MaterializeSpan.DeviceStreamId.device_index"></a>`device_index` — [`L740`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L740)
  - <a id="MaterializeSpan.DeviceStreamId.stream_id"></a>`stream_id` — [`L741`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L741)
- uses (calls/refs, reference-scoped): [`NormalizeIfInsideBuildDirectory`](../common/macro_utils.cc.md#NormalizeIfInsideBuildDirectory), [`MaybeAddCppSourceLoc`](../common/status_builder.cc.md#MaybeAddCppSourceLoc), [`GetRootOpName`](../ops/python_context.cc.md#GetRootOpName), [`SetRootOpNamePayload`](../common/status_builder.cc.md#SetRootOpNamePayload), [`StatusBuilder`](../common/status_builder.h.md#StatusBuilder), [`operator<<`](../common/status_builder.h.md#StatusBuilder.operator), [`is_status_or_ref`](../common/error_utils.h.md#is_status_or_ref), [`ReturnIfErrorAdaptor`](../common/error_utils.h.md#ReturnIfErrorAdaptor), [`ReturnIfErrorAdaptor`](../common/error_utils.h.md#ReturnIfErrorAdaptor.ReturnIfErrorAdaptor), [`Consume`](../common/error_utils.h.md#ReturnIfErrorAdaptor.Consume), [`Consume`](../common/error_utils.h.md#ReturnIfErrorAdaptor.Consume), [`kInternal`](../common/error_utils.h.md#kInternal), [`EventSnapshot`](events_queue.h.md#EventSnapshot), [`Record`](events_queue.cc.md#EventSnapshot.Record), [`SharedDeviceBufferList`](device_buffer.h.md#SharedDeviceBufferList), [`device_index`](device_buffer.h.md#DeviceBufferList.device_index), [`stream_id`](device_buffer.h.md#DeviceBufferList.stream_id), [`MaterializationBlockMode`](materialize.h.md#MaterializationBlockMode), [`GetStatus`](../common/error_utils.h.md#GetStatus), [`is_deferred`](device_buffer.h.md#DeviceBufferList.is_deferred), [`kBlockUntilStarted`](materialize.h.md#MaterializationBlockMode.kBlockUntilStarted), [`is_placeholder`](device_buffer.h.md#DeviceBufferList.is_placeholder), [`EnqueueStream`](materialize.cc.md#MaterializationWorker.EnqueueStream), [`GetDeviceBufferList`](materialize.cc.md#GetDeviceBufferList), [`GetMaterializationWorker`](materialize.cc.md#GetMaterializationWorker), [`GetDeviceBufferList`](materialize.cc.md#GetDeviceBufferList), [`GetUniqueDeferredNodes`](materialize.cc.md#GetUniqueDeferredNodes)

### <a id="ShutdownSentinel"></a>`ShutdownSentinel`
- def: [`csrc/eager/materialize.cc:441`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L441)
- doc: Signals that a shutdown has been initiated.
- signature: `enum class ShutdownSentinel`
- used by: [`MaterializeLoopStep`](materialize.cc.md#MaterializationWorker.MaterializeLoopStep), [`ExecuteLoop`](materialize.cc.md#MaterializationWorker.ExecuteLoop), [`Shutdown`](materialize.cc.md#MaterializationWorker.Shutdown), [`ExecutionOrShutdown`](materialize.cc.md#ExecutionOrShutdown), [`MaterializationOrShutdown`](materialize.cc.md#MaterializationOrShutdown)

## Functions
- <a id="ApplySplitMode"></a>`ApplySplitMode(std::vector<absl_nonnull std::unique_ptr<Traversal>>&& traversals, const MaterializationSettings& settings, mlir::MLIRContext& mlir_context)` — [`L292`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L292) — Converts a sequence of Traversals to a sequence of ExecutionTasks.
- `ApplySplitMode(std::vector<absl_nonnull std::unique_ptr<Traversal>>&& traversals, const MaterializationSettings& settings, mlir::MLIRContext& mlir_context)` — [`L292`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L292) — Converts a sequence of Traversals to a sequence of ExecutionTasks.
- `DependsOnPlaceholder(const SharedDeviceBufferList& node, absl::flat_hash_map<const DeviceBufferList*, bool>& memo)` — [`L158`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L158)
- <a id="DependsOnPlaceholder"></a>`DependsOnPlaceholder(const SharedDeviceBufferList& node, absl::flat_hash_map<const DeviceBufferList*, bool>& memo)` — [`L158`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L158)
- <a id="EnqueueExecutable"></a>`EnqueueExecutable(SharedLoadedExecutableWithMetadata executable, std::vector<DeviceBufferRef> arguments, absl::Span<const Shape> output_shapes, std::string_view task_name)` — [`L819`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L819) — Enqueues an executable for materialization.
- `EnqueueExecutable(SharedLoadedExecutableWithMetadata executable, std::vector<DeviceBufferRef> arguments, absl::Span<const Shape> output_shapes, std::string_view task_name)` — [`L819`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L819) — Enqueues an executable for materialization.
- <a id="FilterPlaceholderDependentTraversals"></a>`FilterPlaceholderDependentTraversals(std::vector<absl_nonnull std::unique_ptr<Traversal>>&& traversals, absl::Status& first_error)` — [`L261`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L261) — Eager ops traced over placeholder tensors (e.g. aten::clone during
- `FilterPlaceholderDependentTraversals(std::vector<absl_nonnull std::unique_ptr<Traversal>>&& traversals, absl::Status& first_error)` — [`L261`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L261) — Eager ops traced over placeholder tensors (e.g. aten::clone during
- <a id="GetCompilationSpecForTraversal"></a>`GetCompilationSpecForTraversal(const MaterializationSettings& materialization_settings, const Traversal& traversal)` — [`L112`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L112) — Returns the appropriate CompilationSpec for a split traversal.
- <a id="GetDeviceBufferList"></a>`GetDeviceBufferList(const DeviceBufferRef& buffer_ref)` — [`L640`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L640)
- `GetDeviceBufferList(const SharedDeviceBufferList& node)` — [`L635`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L635)
- <a id="GetMaterializationWorker"></a>`GetMaterializationWorker()` — [`L630`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L630)
- `GetUniqueDeferredNodes(absl::Span<const T> items, c10::DeviceIndex device_index, std::optional<c10::StreamId> stream_id)` — [`L649`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L649) — Makes a copy of all SharedDeviceBufferLists in `items` that are deferred and
- <a id="GetUniqueDeferredNodes"></a>`GetUniqueDeferredNodes(absl::Span<const T> items, c10::DeviceIndex device_index, std::optional<c10::StreamId> stream_id)` — [`L649`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L649) — Makes a copy of all SharedDeviceBufferLists in `items` that are deferred and
- <a id="HasAnyPlaceholderArgumentOrOutput"></a>`HasAnyPlaceholderArgumentOrOutput(const Traversal& traversal)` — [`L233`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L233)
- <a id="MarkPinnedHostOutputs"></a>`MarkPinnedHostOutputs(absl::Span<const DeviceBufferRef> outputs, const SharedLoadedExecutableWithMetadata& executable)` — [`L418`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L418)
- `Materialize(absl::Span<const DeviceBufferRef> buffer_refs, MaterializationReason reason, MaterializationMode materialization_mode)` — [`L805`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L805) — Materializes all of the buffers and connected leaf nodes in-place.
- <a id="Materialize"></a>`Materialize(absl::Span<const DeviceBufferRef> buffer_refs, MaterializationReason reason, MaterializationMode materialization_mode, MaterializationBlockMode block_mode)` — [`L812`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L812)
- `Materialize(absl::Span<const SharedDeviceBufferList> nodes, MaterializationReason reason, MaterializationMode materialization_mode, MaterializationBlockMode block_mode)` — [`L798`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L798) — Executes all deferred nodes in the list, and updates them in place.  No-op
- <a id="MaterializeCurrentStream"></a>`MaterializeCurrentStream(MaterializationReason reason, MaterializationMode mode, absl::Span<const SharedDeviceBufferList> must_materialize)` — [`L916`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L916) — Materializes all live tensors on the current stream.
- `MaterializeDevice(c10::DeviceIndex device_index, MaterializationReason reason, MaterializationMode mode, absl::Span<const SharedDeviceBufferList> must_materialize)` — [`L882`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L882) — Materializes all live tensors on the given device.
- <a id="MaterializeDevice"></a>`MaterializeDevice(c10::DeviceIndex device_index, MaterializationReason reason, MaterializationMode mode, absl::Span<const SharedDeviceBufferList> must_materialize)` — [`L882`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L882) — Materializes all live tensors on the given device.
- <a id="MaterializeSpan"></a>`MaterializeSpan(absl::Span<const T> items, MaterializationReason reason, MaterializationMode materialization_mode, MaterializationBlockMode block_mode)` — [`L729`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L729) — Dispatches only as many stream materialization tasks as necessary to ensure
- <a id="MaterializeStream"></a>`MaterializeStream(c10::DeviceIndex device_index, c10::StreamId stream_id, MaterializationReason reason, MaterializationMode mode, absl::Span<const SharedDeviceBufferList> must_materialize)` — [`L861`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L861) — Materializes all live tensors on the given stream.
- <a id="OutputDependsOnPlaceholder"></a>`OutputDependsOnPlaceholder(const DeviceBufferRef& ref, absl::flat_hash_map<const DeviceBufferList*, bool>& memo)` — [`L183`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L183)
- `OutputDependsOnPlaceholder(const DeviceBufferRef& ref, absl::flat_hash_map<const DeviceBufferList*, bool>& memo)` — [`L183`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L183)
- `ProcessMaterializationTask(MaterializationTask& task, mlir::MLIRContext& mlir_context)` — [`L361`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L361) — Processes a MaterializationTask, converting it into a sequence of
- <a id="ProcessMaterializationTask"></a>`ProcessMaterializationTask(MaterializationTask& task, mlir::MLIRContext& mlir_context)` — [`L361`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L361) — Processes a MaterializationTask, converting it into a sequence of
- `PruneTraversalPlaceholderOutputs(absl_nonnull std::unique_ptr<Traversal> traversal, absl::flat_hash_map<const DeviceBufferList*, bool>& memo, std::vector<absl_nonnull std::unique_ptr<Traversal>>& clean_traversals, absl::Status& first_error)` — [`L190`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L190)
- <a id="PruneTraversalPlaceholderOutputs"></a>`PruneTraversalPlaceholderOutputs(absl_nonnull std::unique_ptr<Traversal> traversal, absl::flat_hash_map<const DeviceBufferList*, bool>& memo, std::vector<absl_nonnull std::unique_ptr<Traversal>>& clean_traversals, absl::Status& first_error)` — [`L190`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L190)
- <a id="ShutDownMaterializationState"></a>`ShutDownMaterializationState()` — [`L796`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L796) — Shuts down the materialization worker and joins its threads.
- <a id="SplitSingleTraversal"></a>`SplitSingleTraversal(absl_nonnull std::unique_ptr<Traversal> pre_split_traversal, absl::flat_hash_set<const DeviceBufferList*>& scratch_set, std::vector<absl_nonnull std::unique_ptr<Traversal>>& post_split_traversals)` — [`L137`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L137)
- `SplitSingleTraversal(absl_nonnull std::unique_ptr<Traversal> pre_split_traversal, absl::flat_hash_set<const DeviceBufferList*>& scratch_set, std::vector<absl_nonnull std::unique_ptr<Traversal>>& post_split_traversals)` — [`L137`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L137)
- <a id="VerifyMustMaterialize"></a>`VerifyMustMaterialize(absl::Span<const SharedDeviceBufferList> must_materialize)` — [`L343`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.cc#L343) — Checks that all must_materialize nodes in the task have started

