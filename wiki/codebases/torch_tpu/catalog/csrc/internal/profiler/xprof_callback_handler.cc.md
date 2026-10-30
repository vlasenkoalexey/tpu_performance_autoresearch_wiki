---
title: 'Module: csrc/internal/profiler/xprof_callback_handler.cc'
type: catalog
provenance: extracted
module: csrc/internal/profiler/xprof_callback_handler.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  IsProfilerEnabled: '`$anonymous_namespace_csrc/internal/profiler/xprof_callback_handler.cc`/IsProfilerEnabled(c9857a73d68e59ba).'
  XProfCallbackHandler.Register: XProfCallbackHandler#Register(49f6e7a06ebc5aa8).
  XProfCallbackHandler.XProfCallbackHandler: XProfCallbackHandler#XProfCallbackHandler(49f6e7a06ebc5aa8).
  OnFunctionEnter: '`$anonymous_namespace_csrc/internal/profiler/xprof_callback_handler.cc`/OnFunctionEnter(9dd6ef9c714b06a9).'
  OnFunctionExit: '`$anonymous_namespace_csrc/internal/profiler/xprof_callback_handler.cc`/OnFunctionExit(3c1fd3fa39db8b75).'
  XProfObserverContext: '`$anonymous_namespace_csrc/internal/profiler/xprof_callback_handler.cc`/XProfObserverContext#'
  XProfObserverContext.XProfObserverContext: '`$anonymous_namespace_csrc/internal/profiler/xprof_callback_handler.cc`/XProfObserverContext#XProfObserverContext(32511cafd53c7696).'
  XProfObserverContext.traceme_: '`$anonymous_namespace_csrc/internal/profiler/xprof_callback_handler.cc`/XProfObserverContext#traceme_.'
---
# Module: [`csrc/internal/profiler/xprof_callback_handler.cc`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.cc)

## Classes
### <a id="XProfObserverContext"></a>`XProfObserverContext`  ·  implements/extends ObserverContext
- def: [`csrc/internal/profiler/xprof_callback_handler.cc:40`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.cc#L40)
- doc: Observer context for RecordFunction callbacks.
- signature: `class XProfObserverContext : public at::ObserverContext`
- members:
  - <a id="XProfObserverContext.XProfObserverContext"></a>`XProfObserverContext(tsl::profiler::TraceMe tm)` — [`L42`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.cc#L42)
  - <a id="XProfObserverContext.traceme_"></a>`traceme_` — [`L46`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.cc#L46)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`OnFunctionEnter`](xprof_callback_handler.cc.md#OnFunctionEnter)

## Functions
- <a id="IsProfilerEnabled"></a>`IsProfilerEnabled()` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.cc#L59) — Returns true if profiling is enabled for the current thread, otherwise — documented in [profiler](../../../../concepts/profiler.md)
- <a id="OnFunctionEnter"></a>`OnFunctionEnter(const at::RecordFunction& fn)` — [`L79`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.cc#L79) — The callback function that is called when a RecordFunction is pushed.
- `OnFunctionEnter(const at::RecordFunction& fn)` — [`L79`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.cc#L79) — The callback function that is called when a RecordFunction is pushed.
- <a id="OnFunctionExit"></a>`OnFunctionExit(const at::RecordFunction& /*fn*/, at::ObserverContext* /*context_ptr*/)` — [`L95`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.cc#L95) — The callback function that is called when a RecordFunction is popped.

## Other members
- <a id="XProfCallbackHandler.Register"></a>`XProfCallbackHandler.Register` — [`L111`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.cc#L111) — documented in [profiler](../../../../concepts/profiler.md)
- <a id="XProfCallbackHandler.XProfCallbackHandler"></a>`XProfCallbackHandler.XProfCallbackHandler` — [`L102`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/xprof_callback_handler.cc#L102) — documented in [profiler](../../../../concepts/profiler.md)

