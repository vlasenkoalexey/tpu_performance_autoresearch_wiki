---
title: 'Module: csrc/internal/profiler/xprof_callback_handler.h'
type: catalog
provenance: extracted
module: csrc/internal/profiler/xprof_callback_handler.h
status: fresh
symbol_base: cxx . . $ torch_tpu/XProfCallbackHandler#
symbols:
  XProfCallbackHandler: ''
  XProfCallbackHandler.-XProfCallbackHandler: '`~XProfCallbackHandler`(ced63f7c635d850d).'
  XProfCallbackHandler.operator: '`operator=`(b7b3ad898630b13a).'
  XProfCallbackHandler.handle_: handle_.
  XProfCallbackHandler.XProfCallbackHandler: XProfCallbackHandler(e7aebd40c066f6d8).
---
# Module: [`csrc/internal/profiler/xprof_callback_handler.h`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.h)

## Classes
### <a id="XProfCallbackHandler"></a>`XProfCallbackHandler`
- def: [`csrc/internal/profiler/xprof_callback_handler.h:33`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.h#L33) — documented in [profiler](../../../../concepts/profiler.md)
- doc: RAII class to manage the lifetime of PyTorch RecordFunction callbacks.
- signature: `class XProfCallbackHandler`
- members:
  - <a id="XProfCallbackHandler.XProfCallbackHandler"></a>`XProfCallbackHandler(const XProfCallbackHandler&)` — [`L39`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.h#L39)
  - `XProfCallbackHandler(XProfCallbackHandler&&)` — [`L41`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.h#L41)
  - `operator=(const XProfCallbackHandler&)` — [`L40`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.h#L40)
  - <a id="XProfCallbackHandler.operator"></a>`operator=(XProfCallbackHandler&&)` — [`L42`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.h#L42)
  - <a id="XProfCallbackHandler.-XProfCallbackHandler"></a>`~XProfCallbackHandler()` — [`L36`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.h#L36)
  - <a id="XProfCallbackHandler.handle_"></a>`handle_` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.h#L49)
- uses (calls/refs, reference-scoped): [`Register`](xprof_callback_handler.cc.md#XProfCallbackHandler.Register), [`XProfCallbackHandler`](xprof_callback_handler.cc.md#XProfCallbackHandler.XProfCallbackHandler)
- used by: [`start`](tpu_profiler_plugin.cc.md#TpuKinetoProfilerSession.start), [`Start`](profiler_api.cc.md#TpuProfilerServer.Start), [`Register`](xprof_callback_handler.cc.md#XProfCallbackHandler.Register), [`XProfCallbackHandler`](xprof_callback_handler.cc.md#XProfCallbackHandler.XProfCallbackHandler), [`OnFunctionExit`](xprof_callback_handler.cc.md#OnFunctionExit), [`activity_types_`](tpu_profiler_plugin.h.md#TpuKinetoProfilerSession.activity_types_)

