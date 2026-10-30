---
title: 'Module: csrc/eager/materialize.h'
type: catalog
provenance: extracted
module: csrc/eager/materialize.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  Materialize: Materialize(a39d34bd049e5a35).
  MaterializationBlockMode: MaterializationBlockMode#
  MaterializationBlockMode.kNonBlocking: MaterializationBlockMode#kNonBlocking.
  MaterializationBlockMode.kBlockUntilStarted: MaterializationBlockMode#kBlockUntilStarted.
---
# Module: [`csrc/eager/materialize.h`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.h)

## Classes
### <a id="MaterializationBlockMode"></a>`MaterializationBlockMode`
- def: [`csrc/eager/materialize.h:54`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.h#L54) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- doc: Controls how long a materialization operation will block the calling thread.
- signature: `enum class MaterializationBlockMode`
- members:
  - <a id="MaterializationBlockMode.kBlockUntilStarted"></a>`kBlockUntilStarted` — [`L60`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.h#L60) — The calling thread will block until the materialization graph has been
  - <a id="MaterializationBlockMode.kNonBlocking"></a>`kNonBlocking` — [`L65`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.h#L65) — The calling thread will return immediately after scheduling the
- uses (calls/refs, reference-scoped): [`DeviceBufferRef`](device_buffer.h.md#DeviceBufferRef), [`SharedDeviceBufferList`](device_buffer.h.md#SharedDeviceBufferList), [`MaterializationReason`](structured_log_buffer.h.md#MaterializationReason), [`MaterializationMode`](events_queue.h.md#MaterializationMode), [`Materialize`](materialize.cc.md#Materialize), [`Materialize`](materialize.cc.md#Materialize), [`kSplitGraph`](events_queue.h.md#MaterializationMode.kSplitGraph), [`Materialize`](materialize.cc.md#Materialize)
- used by: [`gather`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.gather), [`PrepareCompiledModeArgumentsImpl`](../internal/compile/compiled_mode.cc.md#PrepareCompiledModeArgumentsImpl), [`PrepareCompiledModeArgumentsImpl`](../internal/compile/compiled_mode.cc.md#PrepareCompiledModeArgumentsImpl), [`MarkDynamic`](../internal/dynamism/dynamism.cc.md#MarkDynamic), [`CopyTpuToCpu`](../ops/copy_from/tpu_to_cpu.cc.md#CopyTpuToCpu), [`MaterializeAndReturn`](tensor_to_buffer.cc.md#MaterializeAndReturn), [`stream_id`](materialize.cc.md#MaterializeSpan.DeviceStreamId.stream_id), [`MaybeMaterializeDeviceStateTensor`](device_gen_impl.cc.md#DeviceGeneratorState.MaybeMaterializeDeviceStateTensor), [`TestBody`](shutdown_test.cc.md#ShutdownTest_E2EShutdownCompletes_Test.TestBody), [`TrySyncSingleTensorFast`](../internal/sync/sync_py.cc.md#TrySyncSingleTensorFast), [`TrySyncTensorArrayFast`](../internal/sync/sync_py.cc.md#TrySyncTensorArrayFast), [`GetDynamismInfo`](../internal/dynamism/dynamism.cc.md#GetDynamismInfo), [`SynchronizeTensorsImpl`](../internal/sync/sync.cc.md#SynchronizeTensorsImpl), [`PySyncSpanNoWait`](../internal/sync/sync_py.cc.md#PySyncSpanNoWait), [`Materialize`](materialize.h.md#Materialize), [`DeferNeverDispatch`](device_buffer_utils.cc.md#DeferNeverDispatch), [`Materialize`](materialize.cc.md#Materialize), [`Materialize`](materialize.cc.md#Materialize), [`Materialize`](../api/tensor_buffer.cc.md#TensorBufferHandle.Materialize), [`Materialize`](materialize.h.md#Materialize), [`Materialize`](materialize.cc.md#Materialize), [`MaterializeSpan`](materialize.cc.md#MaterializeSpan)

## Functions
- <a id="Materialize"></a>`Materialize(const DeviceBufferRef& buffer_ref, MaterializationReason reason, MaterializationMode mode = MaterializationMode::kSplitGraph, MaterializationBlockMode block_mode = MaterializationBlockMode::kBlockUntilStarted)` — [`L106`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.h#L106) — Materializes the given buffer in-place. Delegates to the span overload.
- `Materialize(const SharedDeviceBufferList& node, MaterializationReason reason, MaterializationMode mode = MaterializationMode::kSplitGraph, MaterializationBlockMode block_mode = MaterializationBlockMode::kBlockUntilStarted)` — [`L96`](../../../../../../raw/code/torch_tpu/csrc/eager/materialize.h#L96) — Materializes the given node in-place. Delegates to the span overload.

