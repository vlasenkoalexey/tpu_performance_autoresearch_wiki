---
title: 'Module: csrc/common/device_type.h'
type: catalog
provenance: extracted
module: csrc/common/device_type.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  GetPrivateUse1DeviceType: GetPrivateUse1DeviceType(257f012601a17b18).
  GetPrivateUse1DeviceDebugName: GetPrivateUse1DeviceDebugName(efd28698952f529a).
  PjRtDeviceType: PjRtDeviceType#
  PjRtDeviceType.kUnknown: PjRtDeviceType#kUnknown.
  PjRtDeviceType.kTpu: PjRtDeviceType#kTpu.
---
# Module: [`csrc/common/device_type.h`](../../../../../../raw/code/torch_tpu/csrc/common/device_type.h)

## Classes
### <a id="PjRtDeviceType"></a>`PjRtDeviceType`
- def: [`csrc/common/device_type.h:31`](../../../../../../raw/code/torch_tpu/csrc/common/device_type.h#L31)
- doc: The actual physical device type used by PjRt.
- signature: `enum class PjRtDeviceType`
- members:
  - <a id="PjRtDeviceType.kTpu"></a>`kTpu` — [`L33`](../../../../../../raw/code/torch_tpu/csrc/common/device_type.h#L33)
  - <a id="PjRtDeviceType.kUnknown"></a>`kUnknown` — [`L32`](../../../../../../raw/code/torch_tpu/csrc/common/device_type.h#L32)
- used by: [`InitializeInternal`](../pjrt/pjrt_state.cc.md#PjrtBackend.InitializeInternal), [`GetGlobalDeviceId`](../pjrt/pjrt_state.cc.md#PjrtBackend.GetGlobalDeviceId), [`Shutdown`](../pjrt/pjrt_state.cc.md#PjrtBackend.Shutdown), [`operator=`](../pjrt/pjrt_state.h.md#PjrtBackend.operator), [`device_`](../pjrt/pjrt_state.h.md#PjrtBackend.device_), [`device_type_`](../pjrt/pjrt_state.h.md#PjrtBackend.device_type_)

## Functions
- <a id="GetPrivateUse1DeviceDebugName"></a>`GetPrivateUse1DeviceDebugName()` — [`L45`](../../../../../../raw/code/torch_tpu/csrc/common/device_type.h#L45) — Returns a user-friendly name for the PrivateUse1 device. Mainly useful for
- <a id="GetPrivateUse1DeviceType"></a>`GetPrivateUse1DeviceType()` — [`L37`](../../../../../../raw/code/torch_tpu/csrc/common/device_type.h#L37) — Returns the device type for TPU.

