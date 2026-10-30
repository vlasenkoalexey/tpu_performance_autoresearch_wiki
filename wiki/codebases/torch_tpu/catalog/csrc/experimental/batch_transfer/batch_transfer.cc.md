---
title: 'Module: csrc/experimental/batch_transfer/batch_transfer.cc'
type: catalog
provenance: extracted
module: csrc/experimental/batch_transfer/batch_transfer.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BatchTransferD2H: BatchTransferD2H(6c967b9c3d5dde4d).
  BatchTransferH2D: BatchTransferH2D(6c967b9c3d5dde4d).
  TransferFuture.Await: TransferFuture#Await(49f6e7a06ebc5aa8).
  GetPjrtBuffer: '`$anonymous_namespace_csrc/experimental/batch_transfer/batch_transfer.cc`/GetPjrtBuffer(5cd84d4dcb7169dc).'
  GetSizePerMajorDim: '`$anonymous_namespace_csrc/experimental/batch_transfer/batch_transfer.cc`/GetSizePerMajorDim(70486a8a4885562f).'
  ValidatePartialSpec: '`$anonymous_namespace_csrc/experimental/batch_transfer/batch_transfer.cc`/ValidatePartialSpec(1b00d4a8a1aaff80).'
  BatchTransferD2HSync: BatchTransferD2HSync(53d77337a3281dd9).
  RawBufferHolder: RawBufferHolder#
  BatchTransferH2DSync: BatchTransferH2DSync(e2955fe94444849d).
  TransferFuture.AndThen: TransferFuture#AndThen(43f9e16c316dc8ba).
  RawBufferHolder.-RawBufferHolder: RawBufferHolder#`~RawBufferHolder`(ced63f7c635d850d).
  RawBufferHolder.RawBufferHolder: RawBufferHolder#RawBufferHolder(8a8f689ac5c99b29).
  RawBufferHolder.buffer: RawBufferHolder#buffer.
  RawBufferHolder.c_api: RawBufferHolder#c_api.
  RawBufferHolder.extension: RawBufferHolder#extension.
---
# Module: [`csrc/experimental/batch_transfer/batch_transfer.cc`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc)

## Classes
### <a id="RawBufferHolder"></a>`RawBufferHolder`
- def: [`csrc/experimental/batch_transfer/batch_transfer.cc:55`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L55) — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)
- signature: `struct RawBufferHolder`
- members:
  - <a id="RawBufferHolder.RawBufferHolder"></a>`RawBufferHolder(const PJRT_Api* api, const PJRT_RawBuffer_Extension* ext, PJRT_RawBuffer* buf)` — [`L60`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L60)
  - <a id="RawBufferHolder.-RawBufferHolder"></a>`~RawBufferHolder()` — [`L64`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L64) — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)
  - <a id="RawBufferHolder.buffer"></a>`buffer` — [`L58`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L58)
  - <a id="RawBufferHolder.c_api"></a>`c_api` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L56)
  - <a id="RawBufferHolder.extension"></a>`extension` — [`L57`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L57)
- uses (calls/refs, reference-scoped): [`TransferFuture`](batch_transfer.h.md#TransferFuture)
- used by: [`BatchTransferD2H`](batch_transfer.cc.md#BatchTransferD2H), [`BatchTransferH2D`](batch_transfer.cc.md#BatchTransferH2D), [`TransferFuture`](batch_transfer.h.md#TransferFuture.TransferFuture), [`AndThen`](batch_transfer.cc.md#TransferFuture.AndThen), [`AndThen`](batch_transfer.cc.md#TransferFuture.AndThen), [`futures_`](batch_transfer.h.md#TransferFuture.futures_)

## Functions
- <a id="BatchTransferD2H"></a>`BatchTransferD2H(const std::vector<at::Tensor>& src_arrs, const std::vector<at::Tensor>& dst_arrs, const Dimensions& src_offsets_major_dim, const Dimensions& dst_offsets_major_dim, const Dimensions& copy_sizes_major_dim)` — [`L212`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L212) — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)
- `BatchTransferD2H(const std::vector<at::Tensor>& src_arrs, const std::vector<at::Tensor>& dst_arrs, const Dimensions& src_offsets_major_dim, const Dimensions& dst_offsets_major_dim, const Dimensions& copy_sizes_major_dim)` — [`L212`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L212) — Batch transfers
- <a id="BatchTransferD2HSync"></a>`BatchTransferD2HSync(const std::vector<at::Tensor>& src_arrs, const std::vector<at::Tensor>& dst_arrs, const Dimensions& src_offsets_major_dim, const Dimensions& dst_offsets_major_dim, const Dimensions& copy_sizes_major_dim)` — [`L593`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L593) — Synchronous batch transfers — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)
- `BatchTransferD2HSync(const std::vector<at::Tensor>& src_arrs, const std::vector<at::Tensor>& dst_arrs, const Dimensions& src_offsets_major_dim, const Dimensions& dst_offsets_major_dim, const Dimensions& copy_sizes_major_dim)` — [`L593`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L593)
- `BatchTransferH2D(const std::vector<at::Tensor>& src_arrs, const std::vector<at::Tensor>& dst_arrs, const Dimensions& src_offsets_major_dim, const Dimensions& dst_offsets_major_dim, const Dimensions& copy_sizes_major_dim)` — [`L425`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L425) — Asynchronous Host to Device batch transfer.
- <a id="BatchTransferH2D"></a>`BatchTransferH2D(const std::vector<at::Tensor>& src_arrs, const std::vector<at::Tensor>& dst_arrs, const Dimensions& src_offsets_major_dim, const Dimensions& dst_offsets_major_dim, const Dimensions& copy_sizes_major_dim)` — [`L425`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L425) — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)
- <a id="BatchTransferH2DSync"></a>`BatchTransferH2DSync(const std::vector<at::Tensor>& src_arrs, const std::vector<at::Tensor>& dst_arrs, const Dimensions& src_offsets_major_dim, const Dimensions& dst_offsets_major_dim, const Dimensions& copy_sizes_major_dim)` — [`L605`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L605) — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)
- `BatchTransferH2DSync(const std::vector<at::Tensor>& src_arrs, const std::vector<at::Tensor>& dst_arrs, const Dimensions& src_offsets_major_dim, const Dimensions& dst_offsets_major_dim, const Dimensions& copy_sizes_major_dim)` — [`L605`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L605)
- <a id="GetPjrtBuffer"></a>`GetPjrtBuffer(const at::Tensor& tpu_tensor, xla::PjRtBuffer*& out_buffer)` — [`L197`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L197) — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)
- <a id="GetSizePerMajorDim"></a>`GetSizePerMajorDim(const xla::Shape& shape, const xla::Layout* xla_layout, int64_t itemsize)` — [`L170`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L170) — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)
- <a id="ValidatePartialSpec"></a>`ValidatePartialSpec(const Dimensions& src_offsets_major_dim, const Dimensions& dst_offsets_major_dim, const Dimensions& copy_sizes_major_dim)` — [`L153`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L153) — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)

## Other members
- `AndThen` — [`L127`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L127)
- `AndThen` — [`L103`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L103)
- `AndThen` — [`L117`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L117)
- `AndThen` — [`L141`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L141)
- `AndThen` — [`L141`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L141)
- `AndThen` — [`L127`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L127)
- <a id="TransferFuture.AndThen"></a>`TransferFuture.AndThen` — [`L117`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L117) — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)
- <a id="TransferFuture.Await"></a>`TransferFuture.Await` — [`L71`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.cc#L71) — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)

