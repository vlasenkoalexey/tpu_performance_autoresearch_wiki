---
title: 'Module: csrc/eager/current_stream.h'
type: catalog
provenance: extracted
module: csrc/eager/current_stream.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  StreamId: StreamId#
  DeviceIndex: DeviceIndex#
  DeviceStreamId.stream_id: DeviceStreamId#stream_id.
  DeviceStreamId: DeviceStreamId#
  DeviceStreamId.device_index: DeviceStreamId#device_index.
---
# Module: [`csrc/eager/current_stream.h`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.h)

## Classes
### <a id="DeviceIndex"></a>`DeviceIndex`
- def: [`csrc/eager/current_stream.h:29`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.h#L29)
- doc: These are the same as c10::DeviceIndex and c10::StreamId, but importing
- signature: `using DeviceIndex = int8_t`
- used by: [`StreamId`](current_stream.h.md#StreamId), [`ExchangeCurrentDeviceIndex`](current_stream.cc.md#ExchangeCurrentDeviceIndex), [`ExchangeCurrentStreamId`](current_stream.cc.md#ExchangeCurrentStreamId), [`kMaxDevices`](current_stream.cc.md#kMaxDevices), [`NextStreamId`](current_stream.cc.md#NextStreamId), [`GetCurrentDeviceIndex`](current_stream.cc.md#GetCurrentDeviceIndex), [`GetCurrentStreamId`](current_stream.cc.md#GetCurrentStreamId), [`stream_id`](current_stream.h.md#DeviceStreamId.stream_id), [`DeviceStreamId`](current_stream.h.md#DeviceStreamId), [`next_stream_ids_`](current_stream.cc.md#next_stream_ids_)

### <a id="DeviceStreamId"></a>`DeviceStreamId`
- def: [`csrc/eager/current_stream.h:51`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.h#L51)
- doc: A full stream identifier, consisting of a device index and a stream ID.
- signature: `struct DeviceStreamId`
- members:
  - <a id="DeviceStreamId.device_index"></a>`device_index` — [`L52`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.h#L52)
  - <a id="DeviceStreamId.stream_id"></a>`stream_id` — [`L53`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.h#L53)
- uses (calls/refs, reference-scoped): [`GetCurrentDeviceStreamId`](current_stream.cc.md#GetCurrentDeviceStreamId), [`StreamId`](current_stream.h.md#StreamId), [`DeviceIndex`](current_stream.h.md#DeviceIndex), [`NextStreamId`](current_stream.cc.md#NextStreamId), [`ResetStreamIdCounters`](current_stream.cc.md#ResetStreamIdCounters)
- used by: [`GetCurrentDeviceStreamId`](current_stream.cc.md#GetCurrentDeviceStreamId), [`ExchangeCurrentStreamId`](current_stream.cc.md#ExchangeCurrentStreamId)

### <a id="StreamId"></a>`StreamId`
- def: [`csrc/eager/current_stream.h:30`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.h#L30)
- signature: `using StreamId = int64_t`
- uses (calls/refs, reference-scoped): [`DeviceIndex`](current_stream.h.md#DeviceIndex), [`ExchangeCurrentDeviceIndex`](current_stream.cc.md#ExchangeCurrentDeviceIndex), [`ExchangeCurrentStreamId`](current_stream.cc.md#ExchangeCurrentStreamId), [`GetCurrentDeviceIndex`](current_stream.cc.md#GetCurrentDeviceIndex), [`GetCurrentStreamId`](current_stream.cc.md#GetCurrentStreamId)
- used by: [`GetCurrentDeviceStreamId`](current_stream.cc.md#GetCurrentDeviceStreamId), [`ExchangeCurrentDeviceIndex`](current_stream.cc.md#ExchangeCurrentDeviceIndex), [`ExchangeCurrentStreamId`](current_stream.cc.md#ExchangeCurrentStreamId), [`current_device_index_`](current_stream.cc.md#current_device_index_), [`AbslHashValue`](device_buffer.h.md#AbslHashValue), [`current_stream_ids_`](current_stream.cc.md#current_stream_ids_), [`GetCurrentStreamId`](current_stream.cc.md#GetCurrentStreamId), [`stream_id`](current_stream.h.md#DeviceStreamId.stream_id), [`device_index`](current_stream.h.md#DeviceStreamId.device_index)

