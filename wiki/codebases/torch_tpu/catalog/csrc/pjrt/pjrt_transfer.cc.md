---
title: 'Module: csrc/pjrt/pjrt_transfer.cc'
type: catalog
provenance: extracted
module: csrc/pjrt/pjrt_transfer.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  TpuMallocAndMemcpyHtoD: TpuMallocAndMemcpyHtoD(d26578bd16820a93).
  TpuMemcpyDtoH: TpuMemcpyDtoH(269d5f3fa22fa5a9).
  PrepareRawBuffer: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/PrepareRawBuffer(8435db48217be06c).'
  TpuMemcpyDtoHDirect: TpuMemcpyDtoHDirect(58c655b5c39f7e1b).
  TpuAsyncDmaCopyHtoD: TpuAsyncDmaCopyHtoD(c0f8360902571bd7).
  TpuAsyncDmaCopyDtoH: TpuAsyncDmaCopyDtoH(bd90343fb9826c45).
  TpuMemcpyDtoHFP4: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/TpuMemcpyDtoHFP4(b5e22ff1540a9fe7).'
  TpuMemcpyDtoHDirectImpl: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/TpuMemcpyDtoHDirectImpl(e661fb718245965c).'
  RawBufferHolder.RawBufferHolder: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/RawBufferHolder#RawBufferHolder(df0ac8d6f5985837).'
  RawBufferHolder.-RawBufferHolder: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/RawBufferHolder#`~RawBufferHolder`(ced63f7c635d850d).'
  RawBufferContext.hold: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/RawBufferContext#hold.'
  RawBufferHolder: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/RawBufferHolder#'
  RawBufferHolder.buffer: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/RawBufferHolder#buffer.'
  ValidateFp4Dimensions: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/ValidateFp4Dimensions(eb76a6860a5dc792).'
  RawBufferContext.raw_buffer: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/RawBufferContext#raw_buffer.'
  RawBufferHolder.extension: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/RawBufferHolder#extension.'
  RawBufferContext.extension: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/RawBufferContext#extension.'
  RawBufferContext.c_api: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/RawBufferContext#c_api.'
  PackFp4: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/PackFp4(3852baebb2523379).'
  UnpackFp4: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/UnpackFp4(aa65f8a01394c523).'
  RawBufferHolder.c_api: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/RawBufferHolder#c_api.'
  RawBufferHolder.operator: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/RawBufferHolder#`operator=`(39c33cf1a9a0c056).'
  RawBufferContext: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/RawBufferContext#'
  RawBufferHolder.device_buffer_ref: '`$anonymous_namespace_csrc/pjrt/pjrt_transfer.cc`/RawBufferHolder#device_buffer_ref.'
---
# Module: [`csrc/pjrt/pjrt_transfer.cc`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc)

## Classes
### <a id="RawBufferContext"></a>`RawBufferContext`
- def: [`csrc/pjrt/pjrt_transfer.cc:511`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L511)
- doc: Context structure bundling all components required to initiate and track a
- signature: `struct RawBufferContext`
- members:
  - <a id="RawBufferContext.c_api"></a>`c_api` — [`L513`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L513) — PjRt C API function table.
  - <a id="RawBufferContext.extension"></a>`extension` — [`L515`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L515) — PjRt RawBuffer extension function table for DMA copy calls.
  - <a id="RawBufferContext.hold"></a>`hold` — [`L519`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L519) — RAII hold object to be retained alongside the returned xla::Future<>.
  - <a id="RawBufferContext.raw_buffer"></a>`raw_buffer` — [`L517`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L517) — Raw buffer handle passed to CopyRawDeviceToHost or CopyRawHostToDevice.
- uses (calls/refs, reference-scoped): [`RawBufferHolder`](pjrt_transfer.cc.md#RawBufferHolder)
- used by: [`PrepareRawBuffer`](pjrt_transfer.cc.md#PrepareRawBuffer), [`TpuAsyncDmaCopyDtoH`](pjrt_transfer.cc.md#TpuAsyncDmaCopyDtoH), [`TpuAsyncDmaCopyHtoD`](pjrt_transfer.cc.md#TpuAsyncDmaCopyHtoD)

### <a id="RawBufferHolder"></a>`RawBufferHolder`
- def: [`csrc/pjrt/pjrt_transfer.cc:475`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L475)
- doc: RAII management holder for a PjRt RawBuffer alias and its underlying
- signature: `struct RawBufferHolder`
- members:
  - <a id="RawBufferHolder.RawBufferHolder"></a>`RawBufferHolder(const PJRT_Api* api, const PJRT_RawBuffer_Extension* ext, PJRT_RawBuffer* buf, DeviceBufferRef ref)` — [`L486`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L486)
  - `RawBufferHolder(const RawBufferHolder&)` — [`L493`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L493)
  - <a id="RawBufferHolder.operator"></a>`operator=(const RawBufferHolder&)` — [`L494`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L494)
  - <a id="RawBufferHolder.-RawBufferHolder"></a>`~RawBufferHolder()` — [`L496`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L496)
  - <a id="RawBufferHolder.buffer"></a>`buffer` — [`L481`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L481) — Handle to the active raw buffer alias on the TPU device.
  - <a id="RawBufferHolder.c_api"></a>`c_api` — [`L477`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L477) — Global PjRt C API function table pointer.
  - <a id="RawBufferHolder.device_buffer_ref"></a>`device_buffer_ref` — [`L484`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L484) — Reference-counted handle holding the underlying PyTorch TPU DeviceBuffer
  - <a id="RawBufferHolder.extension"></a>`extension` — [`L479`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L479) — PjRt RawBuffer extension function table pointer.
- uses (calls/refs, reference-scoped): [`DeviceBufferRef`](../eager/device_buffer.h.md#DeviceBufferRef), [`DeviceBufferRef`](../eager/device_buffer.h.md#DeviceBufferRef.DeviceBufferRef)
- used by: [`PrepareRawBuffer`](pjrt_transfer.cc.md#PrepareRawBuffer), [`raw_buffer`](pjrt_transfer.cc.md#RawBufferContext.raw_buffer)

## Functions
- <a id="PackFp4"></a>`PackFp4(const uint8_t* absl_nonnull unpacked_data, uint8_t* absl_nonnull packed_data, int64_t num_packed_elements)` — [`L103`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L103) — Packs unpacked float4_e2m1fn_x2 data (1 element per byte) from unpacked_data
- <a id="PrepareRawBuffer"></a>`PrepareRawBuffer(const DeviceBufferRef& buffer_ref)` — [`L529`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L529) — Prepares a DeviceBufferRef for zero-copy DMA by: — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="TpuAsyncDmaCopyDtoH"></a>`TpuAsyncDmaCopyDtoH(const DeviceBufferRef& src_buffer_ref, void* dst_host_ptr, int64_t copy_bytes)` — [`L587`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L587) — Performs asynchronous non-blocking Device-to-Host (D2H) DMA transfer — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="TpuAsyncDmaCopyHtoD"></a>`TpuAsyncDmaCopyHtoD(const void* src_host_ptr, const DeviceBufferRef& dst_buffer_ref, int64_t dst_byte_offset, int64_t copy_bytes)` — [`L615`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L615) — Performs asynchronous non-blocking Host-to-Device (H2D) DMA transfer — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- `TpuMallocAndMemcpyHtoD(const void* host_data, mlir::ElementType element_type, absl::Span<const int64_t> dimensions, std::optional<at::Tensor> backing_tensor, std::vector<uint8_t> backing_data)` — [`L175`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L175) — If backing tensor is present we keep it alive until the transfer completes,
- <a id="TpuMallocAndMemcpyHtoD"></a>`TpuMallocAndMemcpyHtoD(const void* host_data, mlir::ElementType element_type, absl::Span<const int64_t> dimensions, std::optional<at::Tensor> backing_tensor, std::vector<uint8_t> backing_data)` — [`L175`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L175) — If backing tensor is present we keep it alive until the transfer completes, — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="TpuMemcpyDtoH"></a>`TpuMemcpyDtoH(const DeviceBufferRef& buffer_ref, bool non_blocking)` — [`L311`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L311) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="TpuMemcpyDtoHDirect"></a>`TpuMemcpyDtoHDirect(const DeviceBufferRef& buffer_ref, void* dst_ptr, bool non_blocking)` — [`L399`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L399) — Copies the data from the device directly into the provided host buffer. — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="TpuMemcpyDtoHDirectImpl"></a>`TpuMemcpyDtoHDirectImpl(absl::Span<const int64_t> buffer_expected_dims, mlir::ElementType buffer_element_type, xla::PjRtBuffer* buffer, void* dst_ptr)` — [`L378`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L378)
- <a id="TpuMemcpyDtoHFP4"></a>`TpuMemcpyDtoHFP4(xla::PjRtBuffer* absl_nonnull buffer, absl::Span<const int64_t> buffer_expected_dims, at::Tensor& cpu_tensor_receiver)` — [`L130`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L130) — Unpacks float4_e2m1fn_x2 data from the device PjRtBuffer via a temporary — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- `UnpackFp4(const uint8_t* absl_nonnull host_data, int64_t num_elements)` — [`L77`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L77) — Unpacks packed float4_e2m1fn_x2 data from host_data into a byte vector
- <a id="UnpackFp4"></a>`UnpackFp4(const uint8_t* absl_nonnull host_data, int64_t num_elements)` — [`L77`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L77) — Unpacks packed float4_e2m1fn_x2 data from host_data into a byte vector
- <a id="ValidateFp4Dimensions"></a>`ValidateFp4Dimensions(absl::Span<const int64_t> dimensions)` — [`L116`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.cc#L116)

