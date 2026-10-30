---
title: 'Module: csrc/eager/current_stream.cc'
type: catalog
provenance: extracted
module: csrc/eager/current_stream.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  GetCurrentDeviceStreamId: GetCurrentDeviceStreamId(fd47eaa35106cb89).
  ExchangeCurrentDeviceIndex: ExchangeCurrentDeviceIndex(f19b2f157e840411).
  ExchangeCurrentStreamId: ExchangeCurrentStreamId(7877814de101c3ae).
  kMaxDevices: '`$anonymous_namespace_csrc/eager/current_stream.cc`/kMaxDevices.'
  current_device_index_: '`$anonymous_namespace_csrc/eager/current_stream.cc`/current_device_index_.'
  NextStreamId: NextStreamId(80a83fba94cf537a).
  GetCurrentDeviceIndex: GetCurrentDeviceIndex(f1c002f0206d8350).
  current_stream_ids_: '`$anonymous_namespace_csrc/eager/current_stream.cc`/current_stream_ids_.'
  GetCurrentStreamId: GetCurrentStreamId(80a83fba94cf537a).
  ResetStreamIdCounters: ResetStreamIdCounters(49f6e7a06ebc5aa8).
  next_stream_ids_: '`$anonymous_namespace_csrc/eager/current_stream.cc`/next_stream_ids_.'
---
# Module: [`csrc/eager/current_stream.cc`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.cc)

## Functions
- <a id="ExchangeCurrentDeviceIndex"></a>`ExchangeCurrentDeviceIndex(DeviceIndex new_device_index)` — [`L48`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.cc#L48) — Sets the current device index for the calling thread and returns the previous
- <a id="ExchangeCurrentStreamId"></a>`ExchangeCurrentStreamId(DeviceIndex device_index, StreamId new_stream_id)` — [`L60`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.cc#L60) — Sets the current stream ID for the given device index on the calling thread
- <a id="GetCurrentDeviceIndex"></a>`GetCurrentDeviceIndex()` — [`L46`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.cc#L46) — Returns the current device index for the calling thread.
- <a id="GetCurrentDeviceStreamId"></a>`GetCurrentDeviceStreamId()` — [`L67`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.cc#L67) — Returns the current device and stream IDs for the calling thread. — documented in [device-streams-generators-and-rng](../../../concepts/device-streams-generators-and-rng.md)
- <a id="GetCurrentStreamId"></a>`GetCurrentStreamId(DeviceIndex device_index)` — [`L55`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.cc#L55) — Returns the current stream ID for the given device index on the calling
- <a id="NextStreamId"></a>`NextStreamId(DeviceIndex device_index)` — [`L72`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.cc#L72) — Returns the next available stream ID for the given device index.
- <a id="ResetStreamIdCounters"></a>`ResetStreamIdCounters()` — [`L77`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.cc#L77) — Resets the stream ID counters for all devices.

## Module values
- <a id="current_device_index_"></a>`current_device_index_` — [`L33`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.cc#L33) — CPP_THREAD_LOCAL_OK=State is per-C++-thread for device guard
- <a id="current_stream_ids_"></a>`current_stream_ids_` — [`L35`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.cc#L35) — CPP_THREAD_LOCAL_OK=State is per-C++-thread for device guard
- <a id="kMaxDevices"></a>`kMaxDevices` — [`L28`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.cc#L28)
- <a id="next_stream_ids_"></a>`next_stream_ids_` — [`L41`](../../../../../../raw/code/torch_tpu/csrc/eager/current_stream.cc#L41) — This is not a thread_local because all threads share the same next stream ID

