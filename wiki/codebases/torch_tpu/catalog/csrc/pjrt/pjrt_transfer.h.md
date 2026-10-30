---
title: 'Module: csrc/pjrt/pjrt_transfer.h'
type: catalog
provenance: extracted
module: csrc/pjrt/pjrt_transfer.h
status: fresh
symbol_base: cxx . . $ torch_tpu/AsyncDmaResult#
symbols:
  AsyncDmaResult.buffer_hold: buffer_hold.
  AsyncDmaResult: ''
  AsyncDmaResult.future: future.
---
# Module: [`csrc/pjrt/pjrt_transfer.h`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.h)

## Classes
### <a id="AsyncDmaResult"></a>`AsyncDmaResult`
- def: [`csrc/pjrt/pjrt_transfer.h:52`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.h#L52)
- doc: Holds the completion future and RAII buffer hold for an asynchronous DMA
- signature: `struct AsyncDmaResult`
- members:
  - <a id="AsyncDmaResult.buffer_hold"></a>`buffer_hold` — [`L54`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.h#L54)
  - <a id="AsyncDmaResult.future"></a>`future` — [`L53`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_transfer.h#L53)
- uses (calls/refs, reference-scoped): [`DeviceBufferRef`](../eager/device_buffer.h.md#DeviceBufferRef), [`TpuAsyncDmaCopyDtoH`](pjrt_transfer.cc.md#TpuAsyncDmaCopyDtoH), [`TpuAsyncDmaCopyHtoD`](pjrt_transfer.cc.md#TpuAsyncDmaCopyHtoD)
- used by: [`PrepareRawBuffer`](pjrt_transfer.cc.md#PrepareRawBuffer), [`TpuAsyncDmaCopyDtoH`](pjrt_transfer.cc.md#TpuAsyncDmaCopyDtoH), [`TpuAsyncDmaCopyHtoD`](pjrt_transfer.cc.md#TpuAsyncDmaCopyHtoD)

