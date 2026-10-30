---
title: 'Module: csrc/ops/view_decomposition/contiguous_to_view.cc'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/contiguous_to_view.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ContiguousToView: ContiguousToView(c226eaa2e57cabf).
  GetNonOverlappingWindows: '`$anonymous_namespace_csrc/ops/view_decomposition/contiguous_to_view.cc`/GetNonOverlappingWindows(91e353b8e41f9695).'
  GetOverlappingAxes: '`$anonymous_namespace_csrc/ops/view_decomposition/contiguous_to_view.cc`/GetOverlappingAxes(cfa8ab60dd590038).'
  GetNonOverlappingWindowShape: '`$anonymous_namespace_csrc/ops/view_decomposition/contiguous_to_view.cc`/GetNonOverlappingWindowShape(83657c5c996a6093).'
  WriteWindowsToTensor: '`$anonymous_namespace_csrc/ops/view_decomposition/contiguous_to_view.cc`/WriteWindowsToTensor(ef92db96dd6c7563).'
  IndexedStridedDim.stride: '`$anonymous_namespace_csrc/ops/view_decomposition/contiguous_to_view.cc`/IndexedStridedDim#stride.'
  NonOverlappingWindow: '`$anonymous_namespace_csrc/ops/view_decomposition/contiguous_to_view.cc`/NonOverlappingWindow#'
  NonOverlappingWindow.write_storage_offset: '`$anonymous_namespace_csrc/ops/view_decomposition/contiguous_to_view.cc`/NonOverlappingWindow#write_storage_offset.'
  NonOverlappingWindow.window_value: '`$anonymous_namespace_csrc/ops/view_decomposition/contiguous_to_view.cc`/NonOverlappingWindow#window_value.'
  IndexedStridedDim: '`$anonymous_namespace_csrc/ops/view_decomposition/contiguous_to_view.cc`/IndexedStridedDim#'
  IndexedStridedDim.size: '`$anonymous_namespace_csrc/ops/view_decomposition/contiguous_to_view.cc`/IndexedStridedDim#size.'
  IndexedStridedDim.index: '`$anonymous_namespace_csrc/ops/view_decomposition/contiguous_to_view.cc`/IndexedStridedDim#index.'
---
# Module: [`csrc/ops/view_decomposition/contiguous_to_view.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/contiguous_to_view.cc)

## Classes
### <a id="IndexedStridedDim"></a>`IndexedStridedDim`
- def: [`csrc/ops/view_decomposition/contiguous_to_view.cc:46`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/contiguous_to_view.cc#L46)
- doc: Helper struct to sort dimensions by stride while preserving the original
- signature: `struct IndexedStridedDim`
- members:
  - <a id="IndexedStridedDim.index"></a>`index` — [`L47`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/contiguous_to_view.cc#L47)
  - <a id="IndexedStridedDim.size"></a>`size` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/contiguous_to_view.cc#L48)
  - <a id="IndexedStridedDim.stride"></a>`stride` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/contiguous_to_view.cc#L49)
- uses (calls/refs, reference-scoped): [`Indices`](../../common/dimension_types.h.md#Indices)
- used by: [`GetOverlappingAxes`](contiguous_to_view.cc.md#GetOverlappingAxes)

### <a id="NonOverlappingWindow"></a>`NonOverlappingWindow`
- def: [`csrc/ops/view_decomposition/contiguous_to_view.cc:144`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/contiguous_to_view.cc#L144)
- doc: One window of data that needs to be written to the output tensor.
- signature: `struct NonOverlappingWindow`
- members:
  - <a id="NonOverlappingWindow.window_value"></a>`window_value` — [`L146`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/contiguous_to_view.cc#L146) — The logical values that will be written into the output tensor.
  - <a id="NonOverlappingWindow.write_storage_offset"></a>`write_storage_offset` — [`L150`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/contiguous_to_view.cc#L150) — The storage offset in the output tensor to write this window to.
- uses (calls/refs, reference-scoped): [`DeviceBufferRef`](../../eager/device_buffer.h.md#DeviceBufferRef)
- used by: [`ContiguousToView`](contiguous_to_view.cc.md#ContiguousToView), [`GetNonOverlappingWindows`](contiguous_to_view.cc.md#GetNonOverlappingWindows), [`WriteWindowsToTensor`](contiguous_to_view.cc.md#WriteWindowsToTensor)

## Functions
- <a id="ContiguousToView"></a>`ContiguousToView(DeviceBufferRef contiguous_buffer, absl::Span<const int64_t> target_strides, int64_t target_storage_offset)` — [`L261`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/contiguous_to_view.cc#L261) — Converts a contiguous tensor to a view tensor with equivalent logical values — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- <a id="GetNonOverlappingWindowShape"></a>`GetNonOverlappingWindowShape(absl::Span<const int64_t> dimensions, absl::Span<const int64_t> target_strides, const Indices& overlapping_axes)` — [`L121`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/contiguous_to_view.cc#L121) — Returns the shape of the largest non-overlapping window that can be read from — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- `GetNonOverlappingWindows(DeviceBufferRef contiguous_buffer, absl::Span<const int64_t> target_strides, int64_t target_storage_offset)` — [`L166`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/contiguous_to_view.cc#L166) — Returns the full set of non-overlapping windows that can be read from the
- <a id="GetNonOverlappingWindows"></a>`GetNonOverlappingWindows(DeviceBufferRef contiguous_buffer, absl::Span<const int64_t> target_strides, int64_t target_storage_offset)` — [`L166`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/contiguous_to_view.cc#L166) — Returns the full set of non-overlapping windows that can be read from the — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- <a id="GetOverlappingAxes"></a>`GetOverlappingAxes(absl::Span<const int64_t> dimensions, absl::Span<const int64_t> target_strides)` — [`L62`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/contiguous_to_view.cc#L62) — Identifies which dimensions (axes) of a tensor are overlapping, given its — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- `WriteWindowsToTensor(const at::Tensor& output_tensor, absl::Span<const int64_t> target_strides, std::vector<NonOverlappingWindow> non_overlapping_windows)` — [`L238`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/contiguous_to_view.cc#L238) — Repeatedly writes the values of each non-overlapping window to the output
- <a id="WriteWindowsToTensor"></a>`WriteWindowsToTensor(const at::Tensor& output_tensor, absl::Span<const int64_t> target_strides, std::vector<NonOverlappingWindow> non_overlapping_windows)` — [`L238`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/contiguous_to_view.cc#L238) — Repeatedly writes the values of each non-overlapping window to the output

