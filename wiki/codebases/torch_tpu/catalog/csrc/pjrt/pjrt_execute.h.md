---
title: 'Module: csrc/pjrt/pjrt_execute.h'
type: catalog
provenance: extracted
module: csrc/pjrt/pjrt_execute.h
status: fresh
symbol_base: cxx . . $ torch_tpu/PjRtBufferPointers#
symbols:
  PjRtBufferPointers: ''
---
# Module: [`csrc/pjrt/pjrt_execute.h`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_execute.h)

## Classes
### <a id="PjRtBufferPointers"></a>`PjRtBufferPointers`
- def: [`csrc/pjrt/pjrt_execute.h:35`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_execute.h#L35) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- doc: The result of executing a PjRtExecutable, which may produce multiple non-null
- signature: `using PjRtBufferPointers = std::vector<absl_nonnull std::unique_ptr<xla::PjRtBuffer>>`
- uses (calls/refs, reference-scoped): [`Shape`](../common/shape.h.md#Shape), [`SharedLoadedExecutableWithMetadata`](../common/compilation.h.md#SharedLoadedExecutableWithMetadata), [`Execute`](pjrt_execute.cc.md#Execute), [`Execute`](pjrt_execute.cc.md#Execute)
- used by: [`Execute`](pjrt_execute.cc.md#Execute), [`RunInternal`](../eager/execution_task.cc.md#ExecutionTask.RunInternal), [`SetOutputNodesAsMaterialized`](../eager/execution_task.cc.md#ExecutionTask.SetOutputNodesAsMaterialized), [`TestBody`](pjrt_execute_test.cc.md#PjrtExecuteTest_Execute_WithDynamicExecutionMetadata_RoutesInputsOutputsAndMetadata_Test.TestBody), [`PrepareOperands`](../experimental/precompiled_kernels/nonzero_indices_test.cc.md#NonzeroIndicesTest.PrepareOperands), [`ExecutionTask`](../eager/execution_task.h.md#ExecutionTask.ExecutionTask), [`RunSequentialExecutables`](../eager/execution_task.cc.md#RunSequentialExecutables), [`LogCompilationWait`](../eager/execution_task.cc.md#LogCompilationWait), [`HloModuleContainsCollective`](pjrt_execute.cc.md#HloModuleContainsCollective)

