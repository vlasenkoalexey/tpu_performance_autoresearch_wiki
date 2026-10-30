---
title: 'Module: csrc/eager/execution_task.h'
type: catalog
provenance: extracted
module: csrc/eager/execution_task.h
status: fresh
symbol_base: cxx . . $ torch_tpu/ExecutionTask#
symbols:
  ExecutionTask: ''
  ExecutionTask.ExecutionTask: ExecutionTask(247600d4281ebfe9).
  ExecutionTask.outputs_: outputs_.
  ExecutionTask.compiled_kernel_: compiled_kernel_.
  ExecutionTask.name_: name_.
  ExecutionTask.arguments_: arguments_.
  ExecutionTask.outputs: outputs(cdca2a773587f60d).
---
# Module: [`csrc/eager/execution_task.h`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.h)

## Classes
### <a id="ExecutionTask"></a>`ExecutionTask`
- def: [`csrc/eager/execution_task.h:47`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.h#L47)
- doc: To materialize a tensor's data, we need to execute it on-device.
- signature: `class ExecutionTask`
- members:
  - <a id="ExecutionTask.ExecutionTask"></a>`ExecutionTask(std::string name, std::vector<DeviceBufferRef> arguments, std::vector<DeviceBufferRef> outputs, CompiledKernel compiled_kernel)` — [`L95`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.h#L95)
  - `ExecutionTask(std::string name, std::vector<DeviceBufferRef> arguments, std::vector<DeviceBufferRef> outputs, CompiledKernel compiled_kernel)` — [`L95`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.h#L95)
  - <a id="ExecutionTask.outputs"></a>`outputs()` — [`L92`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.h#L92)
  - <a id="ExecutionTask.arguments_"></a>`arguments_` — [`L124`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.h#L124) — The arguments to the compiled kernel.
  - <a id="ExecutionTask.compiled_kernel_"></a>`compiled_kernel_` — [`L129`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.h#L129) — The compiled kernel; or, more precisely, the futures for the compiled
  - <a id="ExecutionTask.name_"></a>`name_` — [`L122`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.h#L122) — A human-readable name for the task. Debug use only.
  - <a id="ExecutionTask.outputs_"></a>`outputs_` — [`L126`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.h#L126) — The outputs of the compiled kernel.
- uses (calls/refs, reference-scoped): [`DeviceBufferRef`](device_buffer.h.md#DeviceBufferRef), [`Traversal`](traversal.h.md#Traversal), [`SharedLoadedExecutableWithMetadata`](../common/compilation.h.md#SharedLoadedExecutableWithMetadata), [`MaterializationReason`](structured_log_buffer.h.md#MaterializationReason), [`RunInternal`](execution_task.cc.md#ExecutionTask.RunInternal), [`FromTraversal`](execution_task.cc.md#ExecutionTask.FromTraversal), [`SetOutputNodesAsMaterialized`](execution_task.cc.md#ExecutionTask.SetOutputNodesAsMaterialized), [`FromExecutable`](execution_task.cc.md#ExecutionTask.FromExecutable), [`GetArgumentBuffers`](execution_task.cc.md#ExecutionTask.GetArgumentBuffers), [`CompilationSpec`](../common/compilation_spec.h.md#CompilationSpec), [`CompiledKernel`](../common/compilation.h.md#CompiledKernel), [`GetCachedExecutables`](execution_task.cc.md#ExecutionTask.GetCachedExecutables), [`PjRtBufferPointers`](../pjrt/pjrt_execute.h.md#PjRtBufferPointers), [`FromTraversalWithLogging`](execution_task.cc.md#ExecutionTask.FromTraversalWithLogging), [`SetOutputNodesAsError`](execution_task.cc.md#ExecutionTask.SetOutputNodesAsError), [`Run`](execution_task.cc.md#ExecutionTask.Run), [`kUnknown`](structured_log_buffer.h.md#MaterializationReason.kUnknown), [`FromExecutable`](execution_task.cc.md#ExecutionTask.FromExecutable), [`FromTraversal`](execution_task.cc.md#ExecutionTask.FromTraversal), [`FromTraversalWithLogging`](execution_task.cc.md#ExecutionTask.FromTraversalWithLogging), [`GetArgumentBuffers`](execution_task.cc.md#ExecutionTask.GetArgumentBuffers), [`GetCachedExecutables`](execution_task.cc.md#ExecutionTask.GetCachedExecutables), [`SetOutputNodesAsMaterialized`](execution_task.cc.md#ExecutionTask.SetOutputNodesAsMaterialized)
- used by: [`traversals`](events_queue.h.md#PendingSnapshotMaterialization.traversals), [`RunInternal`](execution_task.cc.md#ExecutionTask.RunInternal), [`FromTraversal`](execution_task.cc.md#ExecutionTask.FromTraversal), [`ApplySplitMode`](materialize.cc.md#ApplySplitMode), [`SetOutputNodesAsMaterialized`](execution_task.cc.md#ExecutionTask.SetOutputNodesAsMaterialized), [`EnqueueExecutable`](materialize.cc.md#EnqueueExecutable), [`FromExecutable`](execution_task.cc.md#ExecutionTask.FromExecutable), [`ProcessMaterializationTask`](materialize.cc.md#ProcessMaterializationTask), [`GetArgumentBuffers`](execution_task.cc.md#ExecutionTask.GetArgumentBuffers), [`FailRemainingExecutionTasks`](materialize.cc.md#MaterializationWorker.FailRemainingExecutionTasks), [`VerifyMustMaterialize`](materialize.cc.md#VerifyMustMaterialize), [`RunSequentialExecutables`](execution_task.cc.md#RunSequentialExecutables), [`GetCachedExecutables`](execution_task.cc.md#ExecutionTask.GetCachedExecutables), [`RecordCompiledExecutionTask`](events_queue.cc.md#StreamState.RecordCompiledExecutionTask), [`RecordCompiledExecutionTask`](events_queue.cc.md#RecordCompiledExecutionTask), [`ExecuteLoop`](materialize.cc.md#MaterializationWorker.ExecuteLoop), [`FromTraversalWithLogging`](execution_task.cc.md#ExecutionTask.FromTraversalWithLogging), [`GetShapesFromDeviceBuffers`](execution_task.cc.md#GetShapesFromDeviceBuffers), [`SetOutputNodesAsError`](execution_task.cc.md#ExecutionTask.SetOutputNodesAsError), [`ExecutionOrShutdown`](materialize.cc.md#ExecutionOrShutdown), [`MaterializationStages`](materialize.cc.md#MaterializationStages), [`live_nodes`](events_queue.cc.md#StreamState.EventSnapshotRequest.live_nodes)

