---
title: 'Module: csrc/eager/tensor_to_buffer.cc'
type: catalog
provenance: extracted
module: csrc/eager/tensor_to_buffer.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  MakeTensor: MakeTensor(64e96e44dc4e9af6).
  AssignBufferToAtTensor: AssignBufferToAtTensor(22e223e7658ee4b9).
  MakeEmptyTensor: MakeEmptyTensor(7e0dac9ef1379d30).
  GetBuffer: GetBuffer(776caafdc767845a).
  GetBaseBuffer: GetBaseBuffer(776caafdc767845a).
  AssignBufferAsStorageBase: AssignBufferAsStorageBase(265f4d157ae5312b).
  MakeEmptyMemoryFormat: MakeEmptyMemoryFormat(df1f2342f1a612f8).
  MaterializeAndReturn: MaterializeAndReturn(ad353b6f65cfa47).
  TpuAllocator.allocate: TpuAllocator#allocate(d4d44b99e94cbd24).
  TpuPinnedAllocator.allocate: TpuPinnedAllocator#allocate(d4d44b99e94cbd24).
  IsFullStorageReinterpretView: IsFullStorageReinterpretView(f3c087d833018792).
  MakeStorage: MakeStorage(e33bd0564251a548).
  TpuAllocator.copy_data: TpuAllocator#copy_data(6e93f55a8a82847f).
  RegisterTpuAllocator: RegisterTpuAllocator(49f6e7a06ebc5aa8).
  MakeDataPtr: MakeDataPtr(8d89b85cc0457b8c).
  GetBuffers: GetBuffers(3b3fd1e154c71663).
  GetTpuAllocator: GetTpuAllocator(6b40f82d0487c841).
  TpuPinnedAllocator.DeleteTpuPinnedBufferStatic: TpuPinnedAllocator#DeleteTpuPinnedBufferStatic(5d22bdacc48458e8).
  TpuAllocator.getMemoryInfo: TpuAllocator#getMemoryInfo(6447bf30aca2412b).
  TpuAllocator.resetPeakStats: TpuAllocator#resetPeakStats(4af4fd0e2b26c4ac).
  TpuAllocator.getDeviceStats: TpuAllocator#getDeviceStats(c6c115545d08f94f).
  IsTpuPinnedPtr: IsTpuPinnedPtr(fa437ef3bc50daa0).
  GetTpuPinnedAllocator: GetTpuPinnedAllocator(d7373a65dc991d51).
  RemoveDataPtrAlias: '`$anonymous_namespace_csrc/eager/tensor_to_buffer.cc`/RemoveDataPtrAlias(bca6aa9c539f6ace).'
  TpuPinnedAllocator.empty_cache: TpuPinnedAllocator#empty_cache(49f6e7a06ebc5aa8).
  OverwriteDataPtr: '`$anonymous_namespace_csrc/eager/tensor_to_buffer.cc`/OverwriteDataPtr(38f7973cef221f54).'
  TpuAllocator.resetAccumulatedStats: TpuAllocator#resetAccumulatedStats(4af4fd0e2b26c4ac).
  AddDataPtrAlias: '`$anonymous_namespace_csrc/eager/tensor_to_buffer.cc`/AddDataPtrAlias(bca6aa9c539f6ace).'
  TpuPinnedAllocator.free_ptr: TpuPinnedAllocator#free_ptr(5d22bdacc48458e8).
  TpuAllocator.getDeviceStats.StatType: TpuAllocator#getDeviceStats(c6c115545d08f94f).StatType#
  TpuPinnedAllocator.is_pinned_ptr: TpuPinnedAllocator#is_pinned_ptr(fa437ef3bc50daa0).
  TpuPinnedAllocator.pinned_ptrs_: TpuPinnedAllocator#pinned_ptrs_.
  GetTpuPinnedAllocatorInternal: GetTpuPinnedAllocatorInternal(d7373a65dc991d51).
  TpuAllocator: TpuAllocator#
  DeleteDeviceBufferRef: '`$anonymous_namespace_csrc/eager/tensor_to_buffer.cc`/DeleteDeviceBufferRef(5d22bdacc48458e8).'
  TpuPinnedAllocator.mutex_: TpuPinnedAllocator#mutex_.
  TpuPinnedAllocator: TpuPinnedAllocator#
  LayoutToString: '`$anonymous_namespace_csrc/eager/tensor_to_buffer.cc`/LayoutToString(266a719af4746229).'
  TpuAllocator.raw_deleter: TpuAllocator#raw_deleter(b143708a33091e7).
  TpuAllocator.operator: TpuAllocator#`operator=`(32deabc073f66ac3).
  TpuPinnedAllocator.raw_deleter: TpuPinnedAllocator#raw_deleter(b143708a33091e7).
  TpuAllocator.TpuAllocator: TpuAllocator#TpuAllocator(20a3637976d3e73c).
  TpuPinnedAllocator.reset_accumulated_stats: TpuPinnedAllocator#reset_accumulated_stats(49f6e7a06ebc5aa8).
  TpuPinnedAllocator.copy_data: TpuPinnedAllocator#copy_data(6e93f55a8a82847f).
  TpuAllocator.emptyCache: TpuAllocator#emptyCache(49a90a789a80dcae).
  TpuPinnedAllocator.reset_peak_stats: TpuPinnedAllocator#reset_peak_stats(49f6e7a06ebc5aa8).
  TpuAllocator.recordStream: TpuAllocator#recordStream(eee58786a6655ec2).
  TpuPinnedAllocator.record_event: TpuPinnedAllocator#record_event(e8d1f34d9880fd7c).
  TpuPinnedAllocator.get_stats: TpuPinnedAllocator#get_stats(c2d8b238ee72400e).
  TpuAllocator.initialized: TpuAllocator#initialized(c9857a73d68e59ba).
---
# Module: [`csrc/eager/tensor_to_buffer.cc`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc)

## Classes
### <a id="TpuAllocator"></a>`TpuAllocator`  ·  implements/extends Allocator, DeviceAllocator
- def: [`csrc/eager/tensor_to_buffer.cc:427`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L427)
- signature: `class TpuAllocator final : public c10::DeviceAllocator`
- members:
  - `TpuAllocator()` — [`L429`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L429)
  - <a id="TpuAllocator.TpuAllocator"></a>`TpuAllocator(const TpuAllocator&)` — [`L434`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L434)
  - `TpuAllocator(TpuAllocator&& other)` — [`L432`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L432) — This class is move-only.
  - <a id="TpuAllocator.allocate"></a>`allocate(size_t nbytes)` — [`L437`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L437) — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
  - <a id="TpuAllocator.copy_data"></a>`copy_data(void* dest, const void* src, std::size_t count)` — [`L463`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L463) — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
  - <a id="TpuAllocator.emptyCache"></a>`emptyCache(c10::MempoolId_t mempool_id)` — [`L476`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L476)
  - <a id="TpuAllocator.getDeviceStats"></a>`getDeviceStats(c10::DeviceIndex device)` — [`L484`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L484)
  - <a id="TpuAllocator.getMemoryInfo"></a>`getMemoryInfo(c10::DeviceIndex device)` — [`L537`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L537)
  - <a id="TpuAllocator.initialized"></a>`initialized()` — [`L474`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L474)
  - <a id="TpuAllocator.operator"></a>`operator=(TpuAllocator&& other)` — [`L433`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L433)
  - `operator=(const TpuAllocator&)` — [`L435`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L435)
  - <a id="TpuAllocator.raw_deleter"></a>`raw_deleter()` — [`L470`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L470)
  - <a id="TpuAllocator.recordStream"></a>`recordStream(const c10::DataPtr& ptr, c10::Stream stream)` — [`L480`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L480)
  - <a id="TpuAllocator.resetAccumulatedStats"></a>`resetAccumulatedStats(c10::DeviceIndex device)` — [`L521`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L521)
  - <a id="TpuAllocator.resetPeakStats"></a>`resetPeakStats(c10::DeviceIndex device)` — [`L528`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L528)
- uses (calls/refs, reference-scoped): [`NormalizeIfInsideBuildDirectory`](../common/macro_utils.cc.md#NormalizeIfInsideBuildDirectory), [`GetRootOpName`](../ops/python_context.cc.md#GetRootOpName), [`SetRootOpNamePayload`](../common/status_builder.cc.md#SetRootOpNamePayload), [`operator<<`](../common/status_builder.h.md#StatusBuilder.operator), [`OpName`](../ops/op_names.h.md#OpName), [`is_status_or_ref`](../common/error_utils.h.md#is_status_or_ref), [`operator<<`](../ops/op_names.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`operator<<`](../common/cache_key.cc.md#operator), [`TtError`](../common/error_utils.cc.md#TtError.TtError), [`ReturnIfErrorAdaptor`](../common/error_utils.h.md#ReturnIfErrorAdaptor), [`ReturnIfErrorAdaptor`](../common/error_utils.h.md#ReturnIfErrorAdaptor.ReturnIfErrorAdaptor), [`TtError`](../common/error_utils.h.md#TtError), [`ScopedPythonContextCapturer`](../ops/python_context.h.md#ScopedPythonContextCapturer), [`ScopedPythonContextCapturer`](../ops/python_context.cc.md#ScopedPythonContextCapturer.ScopedPythonContextCapturer), [`operator=`](../common/error_utils.h.md#ThrowIfErrorAdapter.operator), [`ThrowIfErrorAdapter`](../common/error_utils.h.md#ThrowIfErrorAdapter.ThrowIfErrorAdapter), [`ThrowIfErrorAdapter`](../common/error_utils.h.md#ThrowIfErrorAdapter), [`GetInstance`](../pjrt/pjrt_state.cc.md#PjrtBackend.GetInstance), [`DeviceBufferRef`](device_buffer.h.md#DeviceBufferRef.DeviceBufferRef), [`ConsumeRequiringMessage`](../common/error_utils.h.md#ReturnIfErrorAdaptor.ConsumeRequiringMessage), [`PjrtBackend`](../pjrt/pjrt_state.h.md#PjrtBackend), [`CreateEmptyDeviceBufferRef`](device_buffer_utils.cc.md#CreateEmptyDeviceBufferRef), [`kPythonNotImplementedError`](../common/error_utils.h.md#kPythonNotImplementedError), [`GetDevice`](../pjrt/pjrt_state.cc.md#PjrtBackend.GetDevice), [`GetWarningPrefix`](../common/warnings.h.md#GetWarningPrefix), [`WarningCategory`](../common/warnings.h.md#WarningCategory), [`MakeDataPtr`](tensor_to_buffer.cc.md#MakeDataPtr), [`GetAllocatorStats`](../pjrt/pjrt_state.cc.md#PjrtBackend.GetAllocatorStats), [`IsDeprecationWarning`](../common/warnings.h.md#IsDeprecationWarning), [`ClearAllocatorStats`](../pjrt/pjrt_state.cc.md#PjrtBackend.ClearAllocatorStats), [`kPerformance`](../common/warnings.h.md#WarningCategory.kPerformance), [`kTorchTpu`](../common/warnings.h.md#WarningCategory.kTorchTpu), [`DeleteDeviceBufferRef`](tensor_to_buffer.cc.md#DeleteDeviceBufferRef), [`kResourceExhausted`](../common/error_utils.h.md#kResourceExhausted), [`kTorchTpuStorageAllocate`](../ops/op_names.h.md#OpName.kTorchTpuStorageAllocate)
- used by: [`GetTpuAllocator`](tensor_to_buffer.cc.md#GetTpuAllocator)

### <a id="TpuAllocator.getDeviceStats.StatType"></a>`TpuAllocator.getDeviceStats.StatType`
- def: [`csrc/eager/tensor_to_buffer.cc:496`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L496)
- doc: Map available stats
- signature: `using StatType = c10::CachingAllocator::StatType`

### <a id="TpuPinnedAllocator"></a>`TpuPinnedAllocator`  ·  implements/extends Allocator, HostAllocator
- def: [`csrc/eager/tensor_to_buffer.cc:551`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L551)
- signature: `class TpuPinnedAllocator final : public at::HostAllocator`
- members:
  - <a id="TpuPinnedAllocator.DeleteTpuPinnedBufferStatic"></a>`DeleteTpuPinnedBufferStatic(void* ptr)` — [`L631`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L631)
  - <a id="TpuPinnedAllocator.allocate"></a>`allocate(size_t nbytes)` — [`L553`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L553) — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
  - <a id="TpuPinnedAllocator.copy_data"></a>`copy_data(void* dest, const void* src, std::size_t count)` — [`L575`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L575)
  - <a id="TpuPinnedAllocator.empty_cache"></a>`empty_cache()` — [`L592`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L592) — This allocator does not cache allocations, so there is nothing to do here.
  - <a id="TpuPinnedAllocator.free_ptr"></a>`free_ptr(void* ptr)` — [`L608`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L608)
  - <a id="TpuPinnedAllocator.get_stats"></a>`get_stats()` — [`L597`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L597)
  - <a id="TpuPinnedAllocator.is_pinned_ptr"></a>`is_pinned_ptr(const void* ptr)` — [`L603`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L603)
  - <a id="TpuPinnedAllocator.raw_deleter"></a>`raw_deleter()` — [`L580`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L580)
  - <a id="TpuPinnedAllocator.record_event"></a>`record_event(void* ptr, void* ctx, c10::Stream stream)` — [`L584`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L584)
  - <a id="TpuPinnedAllocator.reset_accumulated_stats"></a>`reset_accumulated_stats()` — [`L599`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L599)
  - <a id="TpuPinnedAllocator.reset_peak_stats"></a>`reset_peak_stats()` — [`L601`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L601)
  - <a id="TpuPinnedAllocator.mutex_"></a>`mutex_` — [`L621`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L621)
  - <a id="TpuPinnedAllocator.pinned_ptrs_"></a>`pinned_ptrs_` — [`L623`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L623)
- uses (calls/refs, reference-scoped): [`NormalizeIfInsideBuildDirectory`](../common/macro_utils.cc.md#NormalizeIfInsideBuildDirectory), [`GetRootOpName`](../ops/python_context.cc.md#GetRootOpName), [`SetRootOpNamePayload`](../common/status_builder.cc.md#SetRootOpNamePayload), [`operator<<`](../common/status_builder.h.md#StatusBuilder.operator), [`is_status_or_ref`](../common/error_utils.h.md#is_status_or_ref), [`operator<<`](../ops/op_names.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`operator<<`](../common/cache_key.cc.md#operator), [`TtError`](../common/error_utils.cc.md#TtError.TtError), [`ReturnIfErrorAdaptor`](../common/error_utils.h.md#ReturnIfErrorAdaptor), [`ReturnIfErrorAdaptor`](../common/error_utils.h.md#ReturnIfErrorAdaptor.ReturnIfErrorAdaptor), [`StatusBuilderWithMessage`](../common/status_builder.h.md#StatusBuilderWithMessage), [`TtError`](../common/error_utils.h.md#TtError), [`operator=`](../common/error_utils.h.md#ThrowIfErrorAdapter.operator), [`ThrowIfErrorAdapter`](../common/error_utils.h.md#ThrowIfErrorAdapter.ThrowIfErrorAdapter), [`ThrowIfErrorAdapter`](../common/error_utils.h.md#ThrowIfErrorAdapter), [`GetInstance`](../pjrt/pjrt_state.cc.md#PjrtBackend.GetInstance), [`ConsumeRequiringMessage`](../common/error_utils.h.md#ReturnIfErrorAdaptor.ConsumeRequiringMessage), [`PjrtBackend`](../pjrt/pjrt_state.h.md#PjrtBackend), [`operator<<`](../common/status_builder.h.md#StatusBuilder.operator), [`GetWarningPrefix`](../common/warnings.h.md#GetWarningPrefix), [`WarningCategory`](../common/warnings.h.md#WarningCategory), [`GetHostAllocator`](../pjrt/pjrt_state.cc.md#PjrtBackend.GetHostAllocator), [`IsDeprecationWarning`](../common/warnings.h.md#IsDeprecationWarning), [`kTorchTpu`](../common/warnings.h.md#WarningCategory.kTorchTpu), [`GetTpuPinnedAllocatorInternal`](tensor_to_buffer.cc.md#GetTpuPinnedAllocatorInternal), [`kResourceExhausted`](../common/error_utils.h.md#kResourceExhausted)
- used by: [`IsTpuPinnedPtr`](tensor_to_buffer.cc.md#IsTpuPinnedPtr), [`GetTpuPinnedAllocatorInternal`](tensor_to_buffer.cc.md#GetTpuPinnedAllocatorInternal)

## Functions
- <a id="AddDataPtrAlias"></a>`AddDataPtrAlias(const DeviceBufferRef& buffer_ref)` — [`L85`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L85) — Records that a DeviceBufferRef has one more c10::DataPtr using it.
- <a id="AssignBufferAsStorageBase"></a>`AssignBufferAsStorageBase(DeviceBufferRef new_base, const at::Tensor& tensor)` — [`L294`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L294) — Replaces the base DeviceBufferRef of `tensor`'s storage with `new_base`, — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="AssignBufferToAtTensor"></a>`AssignBufferToAtTensor(DeviceBufferRef result_buf, const at::Tensor& tensor, bool enable_autodonation)` — [`L134`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L134) — Assigns the given DeviceBufferRef to the given ATen tensor. — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeleteDeviceBufferRef"></a>`DeleteDeviceBufferRef(void* ctx_ptr)` — [`L102`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L102) — Delegate responsibility for deleting the DeviceBufferRef to the
- <a id="GetBaseBuffer"></a>`GetBaseBuffer(const at::Tensor& tensor)` — [`L317`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L317) — Returns the device buffer for the given tensor's base tensor. — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- `GetBaseBuffer(const c10::Storage& storage)` — [`L338`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L338)
- <a id="GetBuffer"></a>`GetBuffer(const at::Tensor& tensor)` — [`L350`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L350) — Extracts the DeviceBufferRef from the given ATen tensor. — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="GetBuffers"></a>`GetBuffers(absl::Span<const at::Tensor> tensors)` — [`L369`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L369) — Extracts all DeviceBufferRefs from the list of AtenTensors. — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- `GetBuffers(absl::Span<const at::Tensor> tensors)` — [`L369`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L369) — Extracts all DeviceBufferRefs from the list of AtenTensors.
- <a id="GetTpuAllocator"></a>`GetTpuAllocator()` — [`L636`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L636) — Returns the C10 allocator singleton for TPU. — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="GetTpuPinnedAllocator"></a>`GetTpuPinnedAllocator()` — [`L641`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L641) — Returns the Tpu pinned memory allocator. — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="GetTpuPinnedAllocatorInternal"></a>`GetTpuPinnedAllocatorInternal()` — [`L626`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L626)
- <a id="IsFullStorageReinterpretView"></a>`IsFullStorageReinterpretView(const at::Tensor& tensor, const DeviceBufferRef& base)` — [`L268`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L268) — Returns true if `tensor` is a pure reinterpretation of all the bytes of — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="IsTpuPinnedPtr"></a>`IsTpuPinnedPtr(const void* ptr)` — [`L645`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L645) — Returns true if the given pointer was allocated by the Tpu pinned memory — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="LayoutToString"></a>`LayoutToString(c10::optional<at::Layout> layout_opt)` — [`L706`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L706)
- <a id="MakeDataPtr"></a>`MakeDataPtr(DeviceBufferRef buffer_ref, const int device_idx)` — [`L655`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L655) — Creates a c10::DataPtr to hold the given DeviceBufferRef on the given — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="MakeEmptyMemoryFormat"></a>`MakeEmptyMemoryFormat(at::IntArrayRef size, c10::optional<at::ScalarType> dtype_opt, c10::optional<at::Layout> layout_opt, c10::optional<at::Device> device_opt, c10::optional<bool> pin_memory_opt, c10::optional<at::MemoryFormat> memory_format_opt)` — [`L720`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L720) — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="MakeEmptyTensor"></a>`MakeEmptyTensor(at::IntArrayRef size, c10::ScalarType dtype, c10::optional<at::Device> device_opt)` — [`L775`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L775) — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="MakeStorage"></a>`MakeStorage(DeviceBufferRef buffer_ref, int device_idx)` — [`L380`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L380) — Creates a c10::Storage pointer to a new c10::StorageImpl, which holds a — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="MakeTensor"></a>`MakeTensor(DeviceBufferRef buffer_ref, int device_idx)` — [`L392`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L392) — Returns an ATen tensor with the given DeviceBufferRef. — documented in [context-states-and-execution-modes](../../../concepts/context-states-and-execution-modes.md)
- <a id="MaterializeAndReturn"></a>`MaterializeAndReturn(const at::Tensor& tensor, MaterializationReason reason, MaterializationBlockMode block_mode)` — [`L663`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L663) — Returns a materialized DeviceBufferRef for the logical data in the tensor. — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="OverwriteDataPtr"></a>`OverwriteDataPtr(const c10::DataPtr& data_ptr, DeviceBufferRef&& buffer_ref)` — [`L120`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L120) — Overwrites the referent of the data_ptr to be the new buffer_ref. — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="RegisterTpuAllocator"></a>`RegisterTpuAllocator()` — [`L650`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L650) — Registers the TpuAllocator as the allocator for the PrivateUse1 device. — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="RemoveDataPtrAlias"></a>`RemoveDataPtrAlias(const DeviceBufferRef& ref)` — [`L91`](../../../../../../raw/code/torch_tpu/csrc/eager/tensor_to_buffer.cc#L91) — Records that a ref_ptr has one fewer DataPtr using it. — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)

