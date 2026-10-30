---
title: 'Module: csrc/eager/tpu_hooks.cc'
type: catalog
provenance: extracted
module: csrc/eager/tpu_hooks.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  TpuHooksInterface.resizePrivateUse1Bytes: TpuHooksInterface#resizePrivateUse1Bytes(f561feded4f01501).
  TpuDeviceGuardImpl.ValidateDevice: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#ValidateDevice(9b260195f6b86e9d).'
  ValidateDeviceIndex: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/ValidateDeviceIndex(4af4fd0e2b26c4ac).'
  TpuDeviceGuardImpl.synchronizeStream: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#synchronizeStream(11b8ea42fd5f8ed5).'
  TpuDeviceGuardImpl.synchronizeDevice: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#synchronizeDevice(6b207970fb4fadd).'
  TpuDeviceGuardImpl.TpuDeviceGuardImpl: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#TpuDeviceGuardImpl(ced63f7c635d850d).'
  TpuDeviceGuardImpl.exchangeStream: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#exchangeStream(cbe94f3a756d4cf9).'
  TpuDeviceGuardImpl.record: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#record(4b63cf67dad6dcf0).'
  TpuDeviceGuardImpl.synchronizeEvent: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#synchronizeEvent(cf970aa7a2e16d63).'
  TpuHooksInterface.isAvailable: TpuHooksInterface#isAvailable(50ce9a9e25b4a850).
  TpuDeviceGuardImpl.queryEvent: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#queryEvent(e995ef3b941ef3c3).'
  TpuDeviceGuardImpl.elapsedTime: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#elapsedTime(c3d471f992f171d1).'
  TpuDeviceGuardImpl.deviceCount: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#deviceCount(f6f33044a439bb6f).'
  TpuDeviceGuardImpl.type: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#type(fcac215151cce01a).'
  TpuDeviceGuardImpl.queryStream: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#queryStream(69f97204a326261a).'
  AddTpuHooks: AddTpuHooks(c8a92d17d58c956f).
  TpuDeviceGuardImpl.block: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#block(19a5b289ad501a57).'
  TpuDeviceGuardImpl: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#'
  TpuDeviceGuardImpl.exchangeDevice: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#exchangeDevice(b6c4bbf5d51219eb).'
  TpuDeviceGuardImpl.destroyEvent: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#destroyEvent(704e02cf115ab8c7).'
  TpuDeviceGuardImpl.uncheckedSetDevice: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#uncheckedSetDevice(34bec20d488349e4).'
  TpuDeviceGuardImpl.getDevice: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#getDevice(86fed61c3d067d05).'
  TpuDeviceGuardImpl.getNewStream: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#getNewStream(4abbe546f6fdcfbb).'
  TpuDeviceGuardImpl.setDevice: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#setDevice(9b260195f6b86e9d).'
  TpuDeviceGuardImpl.getStream: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#getStream(504869b68722b4e4).'
  TpuDeviceGuardImpl.getDefaultStream: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/TpuDeviceGuardImpl#getDefaultStream(504869b68722b4e4).'
  TpuHooksInterface.hasPrimaryContext: TpuHooksInterface#hasPrimaryContext(610586bb614b2175).
  GetTpuHooks: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/GetTpuHooks(f3b3013fed0e7cd9).'
  TpuHooksInterface.-TpuHooksInterface: TpuHooksInterface#`~TpuHooksInterface`(ced63f7c635d850d).
  g_DeviceType3: g_DeviceType3.
  TpuHooksInterface.isPinnedPtr: TpuHooksInterface#isPinnedPtr(75be980956bd07bc).
  TpuHooksInterface: TpuHooksInterface#
  TpuHooksInterface.getPinnedMemoryAllocator: TpuHooksInterface#getPinnedMemoryAllocator(b7fdfcb34ac6dd1f).
  TpuHooksInterface.init: TpuHooksInterface#init(83f5f38750778ac8).
  TpuHooksArgs: TpuHooksArgs#
  TpuHooksInterface.getDefaultGenerator: TpuHooksInterface#getDefaultGenerator(df945a9c22f1ee8f).
  TpuHooksInterface.getNewGenerator: TpuHooksInterface#getNewGenerator(21806386b5f5e2e8).
  kMaxDevices: '`$anonymous_namespace_csrc/eager/tpu_hooks.cc`/kMaxDevices.'
---
# Module: [`csrc/eager/tpu_hooks.cc`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc)

## Classes
### <a id="TpuDeviceGuardImpl"></a>`TpuDeviceGuardImpl`  ·  implements/extends DeviceGuardImplInterface
- def: [`csrc/eager/tpu_hooks.cc:99`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L99)
- signature: `class TpuDeviceGuardImpl final : public c10::impl::DeviceGuardImplInterface`
- members:
  - <a id="TpuDeviceGuardImpl.TpuDeviceGuardImpl"></a>`TpuDeviceGuardImpl()` — [`L101`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L101)
  - <a id="TpuDeviceGuardImpl.ValidateDevice"></a>`ValidateDevice(c10::Device d)` — [`L144`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L144) — Not implemented: getStreamFromGlobalPool
  - <a id="TpuDeviceGuardImpl.block"></a>`block(void* event, const c10::Stream& stream)` — [`L259`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L259)
  - <a id="TpuDeviceGuardImpl.destroyEvent"></a>`destroyEvent(void* event, const c10::DeviceIndex device_index)` — [`L291`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L291) — All `void* event` values are actually `std::shared_ptr<EventSnapshot>*`;
  - <a id="TpuDeviceGuardImpl.deviceCount"></a>`deviceCount()` — [`L228`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L228)
  - <a id="TpuDeviceGuardImpl.elapsedTime"></a>`elapsedTime(void* event1, void* event2, const c10::DeviceIndex device_index)` — [`L306`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L306)
  - <a id="TpuDeviceGuardImpl.exchangeDevice"></a>`exchangeDevice(c10::Device d)` — [`L153`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L153)
  - <a id="TpuDeviceGuardImpl.exchangeStream"></a>`exchangeStream(c10::Stream s)` — [`L187`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L187)
  - <a id="TpuDeviceGuardImpl.getDefaultStream"></a>`getDefaultStream(c10::Device d)` — [`L242`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L242)
  - <a id="TpuDeviceGuardImpl.getDevice"></a>`getDevice()` — [`L159`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L159)
  - <a id="TpuDeviceGuardImpl.getNewStream"></a>`getNewStream(c10::Device d, int priority)` — [`L180`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L180)
  - <a id="TpuDeviceGuardImpl.getStream"></a>`getStream(c10::Device d)` — [`L174`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L174)
  - <a id="TpuDeviceGuardImpl.queryEvent"></a>`queryEvent(void* event)` — [`L263`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L263)
  - <a id="TpuDeviceGuardImpl.queryStream"></a>`queryStream(const c10::Stream& stream)` — [`L269`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L269)
  - <a id="TpuDeviceGuardImpl.record"></a>`record(void** event, const c10::Stream& stream, const c10::DeviceIndex device_index, const c10::EventFlag flag)` — [`L247`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L247)
  - <a id="TpuDeviceGuardImpl.setDevice"></a>`setDevice(c10::Device d)` — [`L163`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L163)
  - <a id="TpuDeviceGuardImpl.synchronizeDevice"></a>`synchronizeDevice(c10::DeviceIndex device_index)` — [`L281`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L281)
  - <a id="TpuDeviceGuardImpl.synchronizeEvent"></a>`synchronizeEvent(void* event)` — [`L298`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L298)
  - <a id="TpuDeviceGuardImpl.synchronizeStream"></a>`synchronizeStream(const c10::Stream& stream)` — [`L273`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L273)
  - <a id="TpuDeviceGuardImpl.type"></a>`type()` — [`L140`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L140)
  - <a id="TpuDeviceGuardImpl.uncheckedSetDevice"></a>`uncheckedSetDevice(c10::Device d)` — [`L168`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L168)
- uses (calls/refs, reference-scoped): [`NormalizeIfInsideBuildDirectory`](../common/macro_utils.cc.md#NormalizeIfInsideBuildDirectory), [`GetRootOpName`](../ops/python_context.cc.md#GetRootOpName), [`SetRootOpNamePayload`](../common/status_builder.cc.md#SetRootOpNamePayload), [`operator<<`](../common/status_builder.h.md#StatusBuilder.operator), [`is_status_or_ref`](../common/error_utils.h.md#is_status_or_ref), [`operator<<`](../ops/op_names.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`operator<<`](../common/cache_key.cc.md#operator), [`TtError`](../common/error_utils.cc.md#TtError.TtError), [`ReturnIfErrorAdaptor`](../common/error_utils.h.md#ReturnIfErrorAdaptor), [`ReturnIfErrorAdaptor`](../common/error_utils.h.md#ReturnIfErrorAdaptor.ReturnIfErrorAdaptor), [`TtError`](../common/error_utils.h.md#TtError), [`kInvalidArgument`](../common/error_utils.h.md#kInvalidArgument), [`GetStatus`](../common/error_utils.h.md#GetStatus), [`operator=`](../common/error_utils.h.md#ThrowIfErrorAdapter.operator), [`ThrowIfErrorAdapter`](../common/error_utils.h.md#ThrowIfErrorAdapter.ThrowIfErrorAdapter), [`ThrowIfErrorAdapter`](../common/error_utils.h.md#ThrowIfErrorAdapter), [`Consume`](../common/error_utils.h.md#ReturnIfErrorAdaptor.Consume), [`GetInstance`](../pjrt/pjrt_state.cc.md#PjrtBackend.GetInstance), [`ConsumeRequiringMessage`](../common/error_utils.h.md#ReturnIfErrorAdaptor.ConsumeRequiringMessage), [`SyncAndCheckStickyError`](../common/error_utils.cc.md#SyncAndCheckStickyError), [`PjrtBackend`](../pjrt/pjrt_state.h.md#PjrtBackend), [`GetClient`](../pjrt/pjrt_state.cc.md#PjrtBackend.GetClient), [`EventSnapshot`](events_queue.h.md#EventSnapshot), [`MaterializationReason`](structured_log_buffer.h.md#MaterializationReason), [`ElapsedTime`](events_queue.cc.md#EventSnapshot.ElapsedTime), [`ValidateDeviceIndex`](tpu_hooks.cc.md#ValidateDeviceIndex), [`GetWarningPrefix`](../common/warnings.h.md#GetWarningPrefix), [`WarningCategory`](../common/warnings.h.md#WarningCategory), [`MaterializeStream`](materialize.cc.md#MaterializeStream), [`GetPrivateUse1DeviceType`](../common/device_type.h.md#GetPrivateUse1DeviceType), [`MaterializeDevice`](materialize.cc.md#MaterializeDevice), [`Synchronize`](events_queue.cc.md#EventSnapshot.Synchronize), [`IsDeprecationWarning`](../common/warnings.h.md#IsDeprecationWarning), [`ExchangeCurrentDeviceIndex`](current_stream.cc.md#ExchangeCurrentDeviceIndex), [`Query`](events_queue.cc.md#EventSnapshot.Query), [`kExplicitSync`](structured_log_buffer.h.md#MaterializationReason.kExplicitSync), [`ExchangeCurrentStreamId`](current_stream.cc.md#ExchangeCurrentStreamId), [`GetStatus`](../common/error_utils.h.md#GetStatus)  (+4 more)
- used by: [`g_DeviceType3`](tpu_hooks.cc.md#g_DeviceType3)

### <a id="TpuHooksArgs"></a>`TpuHooksArgs`  ·  implements/extends PrivateUse1HooksArgs
- def: [`csrc/eager/tpu_hooks.cc:417`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L417)
- signature: `struct TORCH_API TpuHooksArgs : public at::PrivateUse1HooksArgs`
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="TpuHooksInterface"></a>`TpuHooksInterface`  ·  implements/extends AcceleratorHooksInterface, PrivateUse1HooksInterface
- def: [`csrc/eager/tpu_hooks.cc:318`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L318)
- signature: `struct TORCH_API TpuHooksInterface : public at::PrivateUse1HooksInterface`
- members:
  - <a id="TpuHooksInterface.getDefaultGenerator"></a>`getDefaultGenerator(c10::DeviceIndex device_index)` — [`L321`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L321)
  - <a id="TpuHooksInterface.getNewGenerator"></a>`getNewGenerator(c10::DeviceIndex device_index)` — [`L328`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L328)
  - <a id="TpuHooksInterface.getPinnedMemoryAllocator"></a>`getPinnedMemoryAllocator()` — [`L340`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L340)
  - <a id="TpuHooksInterface.hasPrimaryContext"></a>`hasPrimaryContext(c10::DeviceIndex device_index)` — [`L332`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L332)
  - <a id="TpuHooksInterface.init"></a>`init()` — [`L326`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L326)
  - <a id="TpuHooksInterface.isAvailable"></a>`isAvailable()` — [`L411`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L411)
  - <a id="TpuHooksInterface.isPinnedPtr"></a>`isPinnedPtr(const void* data)` — [`L336`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L336)
  - <a id="TpuHooksInterface.resizePrivateUse1Bytes"></a>`resizePrivateUse1Bytes(const c10::Storage& storage, size_t new_bytes)` — [`L346`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L346) — TODO: b/449801230 - once TPU is upstreamed, invoke this logic from
  - <a id="TpuHooksInterface.-TpuHooksInterface"></a>`~TpuHooksInterface()` — [`L319`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L319)
- uses (calls/refs, reference-scoped): [`NormalizeIfInsideBuildDirectory`](../common/macro_utils.cc.md#NormalizeIfInsideBuildDirectory), [`TranslateToC10ErrorAndThrow`](../common/error_utils.cc.md#TranslateToC10ErrorAndThrow), [`ArgsAsStrings`](../common/macro_utils.cc.md#ArgsAsStrings), [`OpName`](../ops/op_names.h.md#OpName), [`is_status_or_ref`](../common/error_utils.h.md#is_status_or_ref), [`ParseArgTypesOrEmpty`](../ops/macros/logging.cc.md#ParseArgTypesOrEmpty), [`TtError`](../common/error_utils.cc.md#TtError.TtError), [`MakeTensor`](tensor_to_buffer.cc.md#MakeTensor), [`OpParamCacheKeys`](../common/cache_key.h.md#OpParamCacheKeys), [`ReturnIfErrorAdaptor`](../common/error_utils.h.md#ReturnIfErrorAdaptor), [`ReturnIfErrorAdaptor`](../common/error_utils.h.md#ReturnIfErrorAdaptor.ReturnIfErrorAdaptor), [`TtError`](../common/error_utils.h.md#TtError), [`OpParamCacheKeys`](../common/cache_key.cc.md#OpParamCacheKeys.OpParamCacheKeys), [`GetStatus`](../common/error_utils.h.md#GetStatus), [`ScopedPythonContextCapturer`](../ops/python_context.h.md#ScopedPythonContextCapturer), [`ScopedPythonContextCapturer`](../ops/python_context.cc.md#ScopedPythonContextCapturer.ScopedPythonContextCapturer), [`operator=`](../common/error_utils.h.md#ThrowIfErrorAdapter.operator), [`ThrowIfErrorAdapter`](../common/error_utils.h.md#ThrowIfErrorAdapter.ThrowIfErrorAdapter), [`ThrowIfErrorAdapter`](../common/error_utils.h.md#ThrowIfErrorAdapter), [`DeviceBufferRef`](device_buffer.h.md#DeviceBufferRef), [`LogKernelArgs`](../ops/macros/logging.h.md#LogKernelArgs), [`MakeOpParamCacheKeys`](../common/cache_key.h.md#MakeOpParamCacheKeys), [`ArgsAreIdentifiers`](../common/macro_utils.h.md#ArgsAreIdentifiers), [`EnforceSetParamType`](../common/cache_key.h.md#EnforceSetParamType), [`CheckTtKernelArgList`](../ops/macros/logging.h.md#CheckTtKernelArgList), [`ScopedOpName`](../common/op_name_stack.h.md#ScopedOpName.ScopedOpName), [`ScopedOpName`](../common/op_name_stack.h.md#ScopedOpName), [`LogKernelName`](../ops/macros/logging.h.md#LogKernelName), [`KernelArgCheckerContext`](../ops/macros/logging.h.md#KernelArgCheckerContext), [`CountFunctionParams`](../ops/macros/logging.h.md#CountFunctionParams), [`kDebugMode`](../common/macro_utils.h.md#kDebugMode), [`InvalidOpParamCacheKeys`](../ops/macros/kernel.h.md#InvalidOpParamCacheKeys), [`ConditionalStaticAssert`](../ops/macros/kernel.h.md#ConditionalStaticAssert), [`InvalidOpParamCacheKeys`](../ops/macros/kernel.h.md#InvalidOpParamCacheKeys.InvalidOpParamCacheKeys), [`kNo`](../common/cache_key.h.md#EnforceSetParamType.kNo), [`LogKernelArgs`](../ops/macros/logging.h.md#LogKernelArgs), [`Consume`](../common/error_utils.h.md#ReturnIfErrorAdaptor.Consume), [`ConvertTo`](../common/dtype.h.md#ConvertTo), [`ConvertTo`](../common/dtype.h.md#ConvertTo), [`ConvertTo`](../common/dtype.h.md#ConvertTo)  (+18 more)
- used by: [`GetTpuHooks`](tpu_hooks.cc.md#GetTpuHooks)

## Functions
- <a id="AddTpuHooks"></a>`AddTpuHooks()` — [`L429`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L429)
- <a id="GetTpuHooks"></a>`GetTpuHooks()` — [`L422`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L422) — register to PrivateUse1HooksInterface
- <a id="ValidateDeviceIndex"></a>`ValidateDeviceIndex(c10::DeviceIndex device_index)` — [`L67`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L67)

## Module values
- <a id="g_DeviceType3"></a>`g_DeviceType3` — [`L316`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L316)
- <a id="kMaxDevices"></a>`kMaxDevices` — [`L65`](../../../../../../raw/code/torch_tpu/csrc/eager/tpu_hooks.cc#L65)

