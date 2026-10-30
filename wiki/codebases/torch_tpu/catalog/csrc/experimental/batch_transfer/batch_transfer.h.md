---
title: 'Module: csrc/experimental/batch_transfer/batch_transfer.h'
type: catalog
provenance: extracted
module: csrc/experimental/batch_transfer/batch_transfer.h
status: fresh
symbol_base: cxx . . $ torch_tpu/TransferFuture#
symbols:
  TransferFuture.tag_: tag_.
  TransferFuture: ''
  TransferFuture.TransferFuture: TransferFuture(ced63f7c635d850d).
  TransferFuture.futures_: futures_.
  TransferFuture.holds_: holds_.
  TransferFuture.c_api_holds_: c_api_holds_.
  TransferFuture.tensors_: tensors_.
  TransferFuture.SetTag: SetTag(8d4ab0a187bf9331).
  TransferFuture.GetTag: GetTag(f4fff0029955a25f).
---
# Module: [`csrc/experimental/batch_transfer/batch_transfer.h`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.h)

## Classes
### <a id="TransferFuture"></a>`TransferFuture`
- def: [`csrc/experimental/batch_transfer/batch_transfer.h:35`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.h#L35) — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)
- signature: `class TransferFuture`
- members:
  - <a id="TransferFuture.GetTag"></a>`GetTag()` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.h#L55)
  - <a id="TransferFuture.SetTag"></a>`SetTag(std::string tag)` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.h#L54)
  - `TransferFuture()` — [`L37`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.h#L37)
  - <a id="TransferFuture.TransferFuture"></a>`TransferFuture()` — [`L37`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.h#L37) — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)
  - <a id="TransferFuture.c_api_holds_"></a>`c_api_holds_` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.h#L59) — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)
  - <a id="TransferFuture.futures_"></a>`futures_` — [`L58`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.h#L58) — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)
  - <a id="TransferFuture.holds_"></a>`holds_` — [`L60`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.h#L60) — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)
  - <a id="TransferFuture.tag_"></a>`tag_` — [`L62`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.h#L62) — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)
  - <a id="TransferFuture.tensors_"></a>`tensors_` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/experimental/batch_transfer/batch_transfer.h#L61)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions), [`Await`](batch_transfer.cc.md#TransferFuture.Await), [`BatchTransferD2HSync`](batch_transfer.cc.md#BatchTransferD2HSync), [`RawBufferHolder`](batch_transfer.cc.md#RawBufferHolder), [`AndThen`](batch_transfer.cc.md#TransferFuture.AndThen), [`AndThen`](batch_transfer.cc.md#TransferFuture.AndThen), [`AndThen`](batch_transfer.cc.md#TransferFuture.AndThen), [`AndThen`](batch_transfer.cc.md#TransferFuture.AndThen), [`BatchTransferD2H`](batch_transfer.cc.md#BatchTransferD2H), [`BatchTransferH2D`](batch_transfer.cc.md#BatchTransferH2D), [`BatchTransferH2DSync`](batch_transfer.cc.md#BatchTransferH2DSync)
- used by: [`BatchTransferD2H`](batch_transfer.cc.md#BatchTransferD2H), [`BatchTransferH2D`](batch_transfer.cc.md#BatchTransferH2D), [`Await`](batch_transfer.cc.md#TransferFuture.Await), [`GetPjrtBuffer`](batch_transfer.cc.md#GetPjrtBuffer), [`TorchTpuPyBindInitModule_batch_transfer_impl`](../../internal/batch_transfer/batch_transfer_impl.cc.md#TorchTpuPyBindInitModule_batch_transfer_impl), [`PyBatchTransferH2DSync`](../../internal/batch_transfer/batch_transfer_impl.cc.md#PyBatchTransferH2DSync), [`PyBatchTransferD2H`](../../internal/batch_transfer/batch_transfer_impl.cc.md#PyBatchTransferD2H), [`AndThen`](batch_transfer.cc.md#TransferFuture.AndThen), [`AndThen`](batch_transfer.cc.md#TransferFuture.AndThen), [`AndThen`](batch_transfer.cc.md#TransferFuture.AndThen), [`AndThen`](batch_transfer.cc.md#TransferFuture.AndThen), [`~RawBufferHolder`](batch_transfer.cc.md#RawBufferHolder.-RawBufferHolder), [`PyAwaitAll`](../../internal/batch_transfer/batch_transfer_impl.cc.md#PyAwaitAll)

