---
title: 'Module: csrc/eager/device_buffer.cc'
type: catalog
provenance: extracted
module: csrc/eager/device_buffer.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  DeviceBufferList.CreateDeferred: DeviceBufferList#CreateDeferred(f047f8ac79ccb190).
  DeviceBufferList.g_creation_index_: DeviceBufferList#g_creation_index_.
  DeviceBufferList.set_is_pinned_host: DeviceBufferList#set_is_pinned_host(49f6e7a06ebc5aa8).
  DeviceBufferRef.dimensions: DeviceBufferRef#dimensions(b11922e6bc9fa98a).
  DeviceBufferList.Data.deferred_op: DeviceBufferList#Data#deferred_op(67396d37bd4c386b).
  DeviceBufferRef.element_type: DeviceBufferRef#element_type(8d8220464a956245).
  DeviceBufferRef.shape: DeviceBufferRef#shape(3778940202a43bc).
  DeviceBufferRef.is_pinned_host: DeviceBufferRef#is_pinned_host(50ce9a9e25b4a850).
  DeviceBufferList.Data.operator: DeviceBufferList#Data#`operator[]`(5b9885f6f5dcf2a6).
  IsPinnedHostBuffer: IsPinnedHostBuffer(5894924430937183).
  DeviceBufferRef.deferred_op: DeviceBufferRef#deferred_op(67396d37bd4c386b).
  DeviceBufferList.CreatePlaceholder: DeviceBufferList#CreatePlaceholder(a55f2d575c2bc750).
  DeviceBufferList.Data.SetMaterializationError: DeviceBufferList#Data#SetMaterializationError(46c269f5301026a2).
  DeviceBufferRef.DebugString: DeviceBufferRef#DebugString(219584694fe2b248).
  DeviceBufferRef.Create: DeviceBufferRef#Create(614bd02203b47355).
  DeviceBufferList.MarkDynamic: DeviceBufferList#MarkDynamic(a12e28ac4eeaa1d9).
  DeviceBufferRef.RecordChildOp: DeviceBufferRef#RecordChildOp(cf8bf0a838713cc4).
  DeviceBufferList.pjrt_buffer_size: DeviceBufferList#pjrt_buffer_size(a47dd4d300e37f51).
  DeviceBufferList.Data.SetAsPendingMaterialization: DeviceBufferList#Data#SetAsPendingMaterialization(c8a92d17d58c956f).
  DeviceBufferList.Data.ValidateMaterializedBuffers: DeviceBufferList#Data#ValidateMaterializedBuffers(32107cb1e3ffb1ae).
  DeviceBufferRef.AwaitBuffer: DeviceBufferRef#AwaitBuffer(116ac426293b144d).
  DeviceBufferList.Synchronize: DeviceBufferList#Synchronize(654e21e32f56641d).
  DeviceBufferRef.is_placeholder: DeviceBufferRef#is_placeholder(50ce9a9e25b4a850).
  DeviceBufferRef.size_bytes: DeviceBufferRef#size_bytes(fe4d2d262d4164a8).
  DeviceBufferRef.live_data_ptrs: DeviceBufferRef#live_data_ptrs(57a65ae535d7db84).
  DeviceBufferRef.is_materializing: DeviceBufferRef#is_materializing(50ce9a9e25b4a850).
  DeviceBufferList.CreatePending: DeviceBufferList#CreatePending(e2f6c218958729a2).
  DeviceBufferRef.num_elements: DeviceBufferRef#num_elements(57a65ae535d7db84).
  DeviceBufferRef.dynamic_dimensions: DeviceBufferRef#dynamic_dimensions(fb681b1517a7c90f).
  DeviceBufferRef.is_materialized: DeviceBufferRef#is_materialized(50ce9a9e25b4a850).
  DeviceBufferList.Data.PrintDebug: DeviceBufferList#Data#PrintDebug(be3b0a5ae87fb0b4).
  DeviceBufferRef.set_is_pinned_host: DeviceBufferRef#set_is_pinned_host(83f5f38750778ac8).
  DeviceBufferRef.is_deferred: DeviceBufferRef#is_deferred(50ce9a9e25b4a850).
  DeviceBufferRef.on_device_shape_is_dynamic: DeviceBufferRef#on_device_shape_is_dynamic(50ce9a9e25b4a850).
  DeferredOp.Hash: DeferredOp#Hash(fe4d2d262d4164a8).
  DeviceBufferRef.MarkDynamic: DeviceBufferRef#MarkDynamic(76b158312cefe8c7).
  DeviceBufferList.SetAsError: DeviceBufferList#SetAsError(2814731695a089b8).
  DeviceBufferRef.device_index: DeviceBufferRef#device_index(4f2304c4a29b870b).
  DeviceBufferRef.GetReadyFuture: DeviceBufferRef#GetReadyFuture(b90c656e7fa805c7).
  DeviceBufferRef.is_constant: DeviceBufferRef#is_constant(50ce9a9e25b4a850).
  DeviceBufferList.Data.Data: DeviceBufferList#Data#Data(ea7d9a1d1efde23b).
  DeviceBufferRef.stream_id: DeviceBufferRef#stream_id(57a65ae535d7db84).
  DeviceBufferList.Data.SetMaterializationStarted: DeviceBufferList#Data#SetMaterializationStarted(365121bef01be58a).
  DeviceBufferRef.Synchronize: DeviceBufferRef#Synchronize(654e21e32f56641d).
  DeviceBufferList.AwaitBuffer: DeviceBufferList#AwaitBuffer(5b9885f6f5dcf2a6).
  DeviceBufferRef.GetMaterializationFuture: DeviceBufferRef#GetMaterializationFuture(b90c656e7fa805c7).
  DeviceBufferList.size_bytes: DeviceBufferList#size_bytes(2867b430557b1c2e).
  DeviceBufferList.on_device_shape_is_dynamic: DeviceBufferList#on_device_shape_is_dynamic(b144372b1bac3642).
  DeviceBufferList.dimensions: DeviceBufferList#dimensions(8bdab20fbdb2614a).
  DeviceBufferList.dynamic_dimensions: DeviceBufferList#dynamic_dimensions(4f65a6cc92d7cd03).
  DeviceBufferList.element_type: DeviceBufferList#element_type(b6c9a07c4299eea6).
  DeviceBufferList.CreateMaterialized: DeviceBufferList#CreateMaterialized(72580923b0376f2d).
  DeviceBufferList.num_elements: DeviceBufferList#num_elements(16ae604ee302b804).
  DeviceBufferList.DebugString: DeviceBufferList#DebugString(219584694fe2b248).
  DeviceBufferRef.pjrt_buffer_size: DeviceBufferRef#pjrt_buffer_size(1f432571882563c7).
  DeviceBufferRef.is_executing: DeviceBufferRef#is_executing(50ce9a9e25b4a850).
  DeviceBufferList.SetAsPendingMaterialization: DeviceBufferList#SetAsPendingMaterialization(c8a92d17d58c956f).
  DeviceBufferList.RecordChildOp: DeviceBufferList#RecordChildOp(cf8bf0a838713cc4).
  DeviceBufferList.DebugData: DeviceBufferList#DebugData(be3b0a5ae87fb0b4).
  DeviceBufferList.is_pinned_host: DeviceBufferList#is_pinned_host(50ce9a9e25b4a850).
  DeviceBufferList.CheckMaterialization: DeviceBufferList#CheckMaterialization(da101cf9fbdcc623).
  DeviceBufferList.SetAsMaterialized: DeviceBufferList#SetAsMaterialized(19661756065552c8).
  CheckBufferShape: '`$anonymous_namespace_csrc/eager/device_buffer.cc`/CheckBufferShape(1aa1847c8ac6cd3d).'
  Fingerprint: Fingerprint(2358621048cfda63).
---
# Module: [`csrc/eager/device_buffer.cc`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc)

## Functions
- <a id="CheckBufferShape"></a>`CheckBufferShape(const Shape& at_shape, const xla::Shape& buffer_shape)` — [`L502`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L502) — Checks that the requested `at_shape` that a deferred op expects is valid for
- <a id="Fingerprint"></a>`Fingerprint(const Shape& shape)` — [`L825`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L825)
- <a id="IsPinnedHostBuffer"></a>`IsPinnedHostBuffer(const xla::PjRtBuffer* absl_nullable buffer)` — [`L63`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L63) — Returns true if the PjRtBuffer is host offloaded.

## Other members
- `CheckMaterialization` — [`L536`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L536)
- `CreateMaterialized` — [`L344`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L344)
- `CreateDeferred` — [`L357`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L357)
- `SetAsMaterialized` — [`L567`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L567)
- `SetMaterializationStarted` — [`L151`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L151)
- `Data` — [`L70`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L70)
- `Data` — [`L88`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L88)
- `Data` — [`L88`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L88)
- <a id="DeferredOp.Hash"></a>`DeferredOp.Hash` — [`L829`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L829)
- <a id="DeviceBufferList.AwaitBuffer"></a>`DeviceBufferList.AwaitBuffer` — [`L337`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L337)
- <a id="DeviceBufferList.CheckMaterialization"></a>`DeviceBufferList.CheckMaterialization` — [`L536`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L536)
- <a id="DeviceBufferList.CreateDeferred"></a>`DeviceBufferList.CreateDeferred` — [`L357`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L357) — documented in [context-states-and-execution-modes](../../../concepts/context-states-and-execution-modes.md)
- <a id="DeviceBufferList.CreateMaterialized"></a>`DeviceBufferList.CreateMaterialized` — [`L344`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L344)
- <a id="DeviceBufferList.CreatePending"></a>`DeviceBufferList.CreatePending` — [`L472`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L472) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferList.CreatePlaceholder"></a>`DeviceBufferList.CreatePlaceholder` — [`L459`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L459) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferList.Data.Data"></a>`DeviceBufferList.Data.Data` — [`L79`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L79)
- <a id="DeviceBufferList.Data.PrintDebug"></a>`DeviceBufferList.Data.PrintDebug` — [`L199`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L199)
- <a id="DeviceBufferList.Data.SetAsPendingMaterialization"></a>`DeviceBufferList.Data.SetAsPendingMaterialization` — [`L115`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L115)
- <a id="DeviceBufferList.Data.SetMaterializationError"></a>`DeviceBufferList.Data.SetMaterializationError` — [`L132`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L132)
- <a id="DeviceBufferList.Data.SetMaterializationStarted"></a>`DeviceBufferList.Data.SetMaterializationStarted` — [`L151`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L151)
- <a id="DeviceBufferList.Data.ValidateMaterializedBuffers"></a>`DeviceBufferList.Data.ValidateMaterializedBuffers` — [`L170`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L170)
- <a id="DeviceBufferList.Data.deferred_op"></a>`DeviceBufferList.Data.deferred_op` — [`L103`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L103)
- <a id="DeviceBufferList.Data.operator"></a>`DeviceBufferList.Data.operator` — [`L182`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L182)
- <a id="DeviceBufferList.DebugData"></a>`DeviceBufferList.DebugData` — [`L283`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L283)
- <a id="DeviceBufferList.DebugString"></a>`DeviceBufferList.DebugString` — [`L275`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L275)
- <a id="DeviceBufferList.MarkDynamic"></a>`DeviceBufferList.MarkDynamic` — [`L582`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L582)
- <a id="DeviceBufferList.RecordChildOp"></a>`DeviceBufferList.RecordChildOp` — [`L731`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L731)
- <a id="DeviceBufferList.SetAsError"></a>`DeviceBufferList.SetAsError` — [`L574`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L574)
- <a id="DeviceBufferList.SetAsMaterialized"></a>`DeviceBufferList.SetAsMaterialized` — [`L567`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L567)
- <a id="DeviceBufferList.SetAsPendingMaterialization"></a>`DeviceBufferList.SetAsPendingMaterialization` — [`L484`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L484)
- <a id="DeviceBufferList.Synchronize"></a>`DeviceBufferList.Synchronize` — [`L315`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L315)
- <a id="DeviceBufferList.dimensions"></a>`DeviceBufferList.dimensions` — [`L299`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L299)
- <a id="DeviceBufferList.dynamic_dimensions"></a>`DeviceBufferList.dynamic_dimensions` — [`L634`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L634)
- <a id="DeviceBufferList.element_type"></a>`DeviceBufferList.element_type` — [`L304`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L304)
- <a id="DeviceBufferList.g_creation_index_"></a>`DeviceBufferList.g_creation_index_` — [`L342`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L342) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferList.is_pinned_host"></a>`DeviceBufferList.is_pinned_host` — [`L640`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L640)
- <a id="DeviceBufferList.num_elements"></a>`DeviceBufferList.num_elements` — [`L309`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L309)
- <a id="DeviceBufferList.on_device_shape_is_dynamic"></a>`DeviceBufferList.on_device_shape_is_dynamic` — [`L629`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L629)
- <a id="DeviceBufferList.pjrt_buffer_size"></a>`DeviceBufferList.pjrt_buffer_size` — [`L255`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L255)
- <a id="DeviceBufferList.set_is_pinned_host"></a>`DeviceBufferList.set_is_pinned_host` — [`L644`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L644)
- <a id="DeviceBufferList.size_bytes"></a>`DeviceBufferList.size_bytes` — [`L237`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L237)
- <a id="DeviceBufferRef.AwaitBuffer"></a>`DeviceBufferRef.AwaitBuffer` — [`L722`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L722) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.Create"></a>`DeviceBufferRef.Create` — [`L646`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L646)
- <a id="DeviceBufferRef.DebugString"></a>`DeviceBufferRef.DebugString` — [`L287`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L287) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.GetMaterializationFuture"></a>`DeviceBufferRef.GetMaterializationFuture` — [`L727`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L727)
- <a id="DeviceBufferRef.GetReadyFuture"></a>`DeviceBufferRef.GetReadyFuture` — [`L747`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L747) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.MarkDynamic"></a>`DeviceBufferRef.MarkDynamic` — [`L793`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L793) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.RecordChildOp"></a>`DeviceBufferRef.RecordChildOp` — [`L809`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L809) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.Synchronize"></a>`DeviceBufferRef.Synchronize` — [`L718`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L718) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.deferred_op"></a>`DeviceBufferRef.deferred_op` — [`L714`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L714) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.device_index"></a>`DeviceBufferRef.device_index` — [`L813`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L813) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.dimensions"></a>`DeviceBufferRef.dimensions` — [`L701`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L701) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.dynamic_dimensions"></a>`DeviceBufferRef.dynamic_dimensions` — [`L804`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L804) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.element_type"></a>`DeviceBufferRef.element_type` — [`L709`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L709) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.is_constant"></a>`DeviceBufferRef.is_constant` — [`L693`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L693) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.is_deferred"></a>`DeviceBufferRef.is_deferred` — [`L669`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L669) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.is_executing"></a>`DeviceBufferRef.is_executing` — [`L677`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L677)
- <a id="DeviceBufferRef.is_materialized"></a>`DeviceBufferRef.is_materialized` — [`L681`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L681) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.is_materializing"></a>`DeviceBufferRef.is_materializing` — [`L673`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L673) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.is_pinned_host"></a>`DeviceBufferRef.is_pinned_host` — [`L685`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L685) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.is_placeholder"></a>`DeviceBufferRef.is_placeholder` — [`L665`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L665) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.live_data_ptrs"></a>`DeviceBufferRef.live_data_ptrs` — [`L821`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L821)
- <a id="DeviceBufferRef.num_elements"></a>`DeviceBufferRef.num_elements` — [`L705`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L705) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.on_device_shape_is_dynamic"></a>`DeviceBufferRef.on_device_shape_is_dynamic` — [`L800`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L800) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.pjrt_buffer_size"></a>`DeviceBufferRef.pjrt_buffer_size` — [`L661`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L661)
- <a id="DeviceBufferRef.set_is_pinned_host"></a>`DeviceBufferRef.set_is_pinned_host` — [`L689`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L689) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.shape"></a>`DeviceBufferRef.shape` — [`L697`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L697) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.size_bytes"></a>`DeviceBufferRef.size_bytes` — [`L657`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L657) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="DeviceBufferRef.stream_id"></a>`DeviceBufferRef.stream_id` — [`L817`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer.cc#L817) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)

