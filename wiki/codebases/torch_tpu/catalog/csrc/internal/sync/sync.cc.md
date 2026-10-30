---
title: 'Module: csrc/internal/sync/sync.cc'
type: catalog
provenance: extracted
module: csrc/internal/sync/sync.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  SynchronizeTensorsImpl: '`$anonymous_namespace_csrc/internal/sync/sync.cc`/SynchronizeTensorsImpl(8cfc6dd5f902fc0d).'
  GetTraversal: '`$anonymous_namespace_csrc/internal/sync/sync.cc`/GetTraversal(e4dc7dbb4cdb0127).'
  IsMaterializing: IsMaterializing(a1fc6b904d2bd53f).
  GetComputationMlir: GetComputationMlir(7160f5277fe6f786).
  IsMaterialized: IsMaterialized(a1fc6b904d2bd53f).
  AwaitUniqueDeviceBufferLists: '`$anonymous_namespace_csrc/internal/sync/sync.cc`/AwaitUniqueDeviceBufferLists(d6b1555679adc471).'
  GetComputationGraphviz: GetComputationGraphviz(23ea5d505932f718).
  SynchronizeTensors: SynchronizeTensors(e02acd975e563a98).
  NeedsExplicitSyncMaterialization: '`$anonymous_namespace_csrc/internal/sync/sync.cc`/NeedsExplicitSyncMaterialization(8182ece79fead29e).'
  DerefTensor: '`$anonymous_namespace_csrc/internal/sync/sync.cc`/DerefTensor(baf22cc3a1d700e1).'
---
# Module: [`csrc/internal/sync/sync.cc`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.cc)

## Functions
- <a id="AwaitUniqueDeviceBufferLists"></a>`AwaitUniqueDeviceBufferLists(absl::Span<const DeviceBufferRef> buffer_refs)` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.cc#L63) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="DerefTensor"></a>`DerefTensor(const at::Tensor& tensor)` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.cc#L49)
- `DerefTensor(const at::Tensor* tensor)` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.cc#L53) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="GetComputationGraphviz"></a>`GetComputationGraphviz(absl::Span<const DeviceBufferRef> buffer_refs, const BufferRefToVarMap& buffer_ref_to_var)` — [`L179`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.cc#L179) — Returns a graphviz compatible representation of the computation graph of the — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- `GetComputationGraphviz(absl::Span<const DeviceBufferRef> buffer_refs, const BufferRefToVarMap& buffer_ref_to_var)` — [`L179`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.cc#L179) — Returns a graphviz compatible representation of the computation graph of the
- <a id="GetComputationMlir"></a>`GetComputationMlir(absl::Span<const DeviceBufferRef> buffer_refs)` — [`L188`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.cc#L188) — Returns the MLIR representation of the computation graph of the given buffer — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="GetTraversal"></a>`GetTraversal(absl::Span<const DeviceBufferRef> buffer_refs)` — [`L156`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.cc#L156) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- `GetTraversal(absl::Span<const DeviceBufferRef> buffer_refs)` — [`L156`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.cc#L156)
- <a id="IsMaterialized"></a>`IsMaterialized(const at::Tensor& tensor)` — [`L146`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.cc#L146) — Checks the tensor is both materialized and ready, meaning that it both has — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="IsMaterializing"></a>`IsMaterializing(const at::Tensor& tensor)` — [`L138`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.cc#L138) — Checks if the tensor is materialized; that is, if it has a PjRtBuffer — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="NeedsExplicitSyncMaterialization"></a>`NeedsExplicitSyncMaterialization(const DeviceBufferRef& buffer_ref)` — [`L57`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.cc#L57) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- `SynchronizeTensors(absl::Span<const at::Tensor* const> tensors)` — [`L134`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.cc#L134)
- <a id="SynchronizeTensors"></a>`SynchronizeTensors(absl::Span<const at::Tensor> tensors)` — [`L130`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.cc#L130) — Materializes the given tensors, and then waits for their PjRtBuffers to be — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)
- <a id="SynchronizeTensorsImpl"></a>`SynchronizeTensorsImpl(TensorSpan tensors)` — [`L89`](../../../../../../../raw/code/torch_tpu/csrc/internal/sync/sync.cc#L89) — documented in [tensor-synchronization](../../../../concepts/tensor-synchronization.md)

