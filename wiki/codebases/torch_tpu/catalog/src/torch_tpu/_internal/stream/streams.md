---
title: 'Module: src/torch_tpu/_internal/stream/streams.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/stream/streams.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.stream.streams`/
symbols:
  experimental: experimental.
  CorePinningMode.CorePinningMode: CorePinningMode.CorePinningMode.
  TpuStream.pinned: TpuStream#pinned.
  TpuStream.wait_event: TpuStream#wait_event().
  TpuStream.record_event: TpuStream#record_event().
  TpuStream: TpuStream#
  TpuStream.wait_stream: TpuStream#wait_stream().
  TpuStream.is_sparse: TpuStream#is_sparse().
  TpuStream.is_dense: TpuStream#is_dense().
  TpuEvent: TpuEvent#
  TpuStream.__new__: TpuStream#__new__().
  TpuStream.query: TpuStream#query().
  TpuStream.priority_range: TpuStream#priority_range().
  TpuEvent.from_ipc_handle: TpuEvent#from_ipc_handle().
  TpuEvent.ipc_handle: TpuEvent#ipc_handle().
  _NOT_IMPLEMENTED_STREAMS_MSG: _NOT_IMPLEMENTED_STREAMS_MSG.
  _parse_pinned: _parse_pinned().
  TpuEvent.record: TpuEvent#record().
  TpuEvent.wait: TpuEvent#wait().
  synchronize: synchronize().
  TpuStream.__init__: TpuStream#__init__().
  TpuStream.synchronize: TpuStream#synchronize().
  TpuEvent.query: TpuEvent#query().
  TpuEvent.elapsed_time: TpuEvent#elapsed_time().
  TpuEvent.synchronize: TpuEvent#synchronize().
  _get_device_index: _get_device_index().
  TpuStream.__repr__: TpuStream#__repr__().
  TpuEvent.__new__: TpuEvent#__new__().
  TpuEvent.__repr__: TpuEvent#__repr__().
---
# Module: [`src/torch_tpu/_internal/stream/streams.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py)

## Classes
### <a id="TpuEvent"></a>`TpuEvent`
- def: [`src/torch_tpu/_internal/stream/streams.py:221`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L221)
- members:
  - <a id="TpuEvent.elapsed_time"></a>`elapsed_time(self, end_event: torch.Event)` — [`L306`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L306) — Returns the milliseconds between this event and ``end_event`` completing.
  - <a id="TpuEvent.from_ipc_handle"></a>`from_ipc_handle(cls, device, handle)` — [`L344`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L344) — Reconstructs an event from an IPC handle on the given device.
  - <a id="TpuEvent.ipc_handle"></a>`ipc_handle(self)` — [`L352`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L352) — Returns an IPC handle of this event.
  - <a id="TpuEvent.query"></a>`query(self)` — [`L298`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L298) — Checks if all work currently captured by this event has completed.
  - <a id="TpuEvent.record"></a>`record(self, stream: torch.Stream | None = None)` — [`L269`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L269) — Snapshot all pending async futures on the current device.
  - <a id="TpuEvent.synchronize"></a>`synchronize(self)` — [`L329`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L329) — Block until all snapshotted futures complete.
  - <a id="TpuEvent.wait"></a>`wait(self, stream: torch.Stream | None = None)` — [`L281`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L281) — No-op placeholder for CUDA stream-wait semantics.
- protocol/private: <a id="TpuEvent.__new__"></a>`__new__`[`L245`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L245), <a id="TpuEvent.__repr__"></a>`__repr__`[`L356`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L356)
- uses (calls/refs, reference-scoped): [`experimental`](streams.md#experimental), [`_NOT_IMPLEMENTED_STREAMS_MSG`](streams.md#_NOT_IMPLEMENTED_STREAMS_MSG)
- used by: [`record_event`](streams.md#TpuStream.record_event), [`wait_event`](streams.md#TpuStream.wait_event), [`Event`](../device/_device_module.md#_DeviceModule.Event)

### <a id="TpuStream"></a>`TpuStream`
- def: [`src/torch_tpu/_internal/stream/streams.py:86`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L86)
- doc: A stream of operations on a TPU device.
- signature: `class TpuStream(torch.Stream):`
- members:
  - <a id="TpuStream.is_dense"></a>`is_dense(self)` — [`L217`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L217)
  - <a id="TpuStream.is_sparse"></a>`is_sparse(self)` — [`L210`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L210)
  - <a id="TpuStream.priority_range"></a>`priority_range(self)` — [`L199`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L199) — Returns the priority range for streams.
  - <a id="TpuStream.query"></a>`query(self)` — [`L182`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L182) — Checks if all work submitted on this stream has been completed.
  - <a id="TpuStream.record_event"></a>`record_event(self, event: Optional[TpuEvent] = None)` — [`L172`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L172) — Records an event on this stream.
  - <a id="TpuStream.synchronize"></a>`synchronize(self)` — [`L190`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L190) — Waits for all work submitted on this stream to complete.
  - <a id="TpuStream.wait_event"></a>`wait_event(self, event: TpuEvent)` — [`L156`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L156) — Makes all future work submitted to the stream wait for an event.
  - <a id="TpuStream.wait_stream"></a>`wait_stream(self, stream: Self)` — [`L164`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L164) — Synchronizes with another stream.
  - <a id="TpuStream.pinned"></a>`pinned` — [`L144`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L144)
- protocol/private: <a id="TpuStream.__init__"></a>`__init__`[`L134`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L134), <a id="TpuStream.__new__"></a>`__new__`[`L109`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L109), <a id="TpuStream.__repr__"></a>`__repr__`[`L203`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L203)
- uses (calls/refs, reference-scoped): [`experimental`](streams.md#experimental), [`CorePinningMode`](streams.md#CorePinningMode.CorePinningMode), [`TpuEvent`](streams.md#TpuEvent), [`_NOT_IMPLEMENTED_STREAMS_MSG`](streams.md#_NOT_IMPLEMENTED_STREAMS_MSG), [`_parse_pinned`](streams.md#_parse_pinned), [`record`](streams.md#TpuEvent.record), [`wait`](streams.md#TpuEvent.wait), [`_get_device_index`](streams.md#_get_device_index)
- used by: [`current_stream`](../device/_device_module.md#_DeviceModule.current_stream), [`stream`](../device/_device_module.md#_DeviceModule.stream), [`Stream`](../device/_device_module.md#_DeviceModule.Stream), [`default_stream`](../device/_device_module.md#_DeviceModule.default_stream), [`__init__`](../device/_device_module.md#TpuStreamContext.__init__), [`set_stream`](../device/_device_module.md#_DeviceModule.set_stream)

## Functions
- <a id="_get_device_index"></a>`_get_device_index(device=None)` — [`L31`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L31) — Returns the device index of the given, or current device.
- <a id="_parse_pinned"></a>`_parse_pinned(pinned: CorePinningMode | str | None)` — [`L59`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L59) — Parses the "pinned" keyword argument using common strings.
- <a id="synchronize"></a>`synchronize(device: torch.device | str | int | None = None)` — [`L360`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L360) — Waits for all pending d2h copies on a TPU device to complete.

## Module values
- <a id="CorePinningMode.CorePinningMode"></a>`CorePinningMode` — [`L56`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L56)
- <a id="_NOT_IMPLEMENTED_STREAMS_MSG"></a>`_NOT_IMPLEMENTED_STREAMS_MSG` — [`L25`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L25)
- <a id="experimental"></a>`experimental` — [`L23`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/stream/streams.py#L23)

