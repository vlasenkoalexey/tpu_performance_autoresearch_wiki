---
title: 'Module: csrc/common/reroute_warnings.cc'
type: catalog
provenance: extracted
module: csrc/common/reroute_warnings.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  SurfaceReroutedWarnings: SurfaceReroutedWarnings(49f6e7a06ebc5aa8).
  RouteWarningsOnThisThreadToDispatchThread: RouteWarningsOnThisThreadToDispatchThread(49f6e7a06ebc5aa8).
  DelayedWarningHandler.mu_: '`$anonymous_namespace_csrc/common/reroute_warnings.cc`/DelayedWarningHandler#mu_.'
  DelayedWarningHandler.GetAll: '`$anonymous_namespace_csrc/common/reroute_warnings.cc`/DelayedWarningHandler#GetAll(878f6bfbdbd0b2ce).'
  DelayedWarningHandler.warnings_: '`$anonymous_namespace_csrc/common/reroute_warnings.cc`/DelayedWarningHandler#warnings_.'
  GetDelayedWarningHandler: '`$anonymous_namespace_csrc/common/reroute_warnings.cc`/GetDelayedWarningHandler(f8e62dc096951422).'
  DelayedWarningHandler: '`$anonymous_namespace_csrc/common/reroute_warnings.cc`/DelayedWarningHandler#'
  DelayedWarningHandler.has_warnings_: '`$anonymous_namespace_csrc/common/reroute_warnings.cc`/DelayedWarningHandler#has_warnings_.'
  DelayedWarningHandler.process: '`$anonymous_namespace_csrc/common/reroute_warnings.cc`/DelayedWarningHandler#process(af73b66e32ab7449).'
  DelayedWarningHandler.has_warnings: '`$anonymous_namespace_csrc/common/reroute_warnings.cc`/DelayedWarningHandler#has_warnings(50ce9a9e25b4a850).'
---
# Module: [`csrc/common/reroute_warnings.cc`](../../../../../../raw/code/torch_tpu/csrc/common/reroute_warnings.cc)

## Classes
### <a id="DelayedWarningHandler"></a>`DelayedWarningHandler`  ·  implements/extends WarningHandler
- def: [`csrc/common/reroute_warnings.cc:33`](../../../../../../raw/code/torch_tpu/csrc/common/reroute_warnings.cc#L33)
- doc: Buffers the warnings of every thread installing it as warning handler.
- signature: `class DelayedWarningHandler final : public c10::WarningHandler`
- members:
  - <a id="DelayedWarningHandler.GetAll"></a>`GetAll()` — [`L47`](../../../../../../raw/code/torch_tpu/csrc/common/reroute_warnings.cc#L47) — Returns all buffered warnings and empties the buffer.
  - <a id="DelayedWarningHandler.has_warnings"></a>`has_warnings()` — [`L42`](../../../../../../raw/code/torch_tpu/csrc/common/reroute_warnings.cc#L42) — Returns whether there may be buffered warnings, without locking.
  - <a id="DelayedWarningHandler.process"></a>`process(const c10::Warning& warning)` — [`L35`](../../../../../../raw/code/torch_tpu/csrc/common/reroute_warnings.cc#L35)
  - <a id="DelayedWarningHandler.has_warnings_"></a>`has_warnings_` — [`L59`](../../../../../../raw/code/torch_tpu/csrc/common/reroute_warnings.cc#L59) — Mirroring emptiness check so `SurfaceReroutedWarnings` can skip locking in
  - <a id="DelayedWarningHandler.mu_"></a>`mu_` — [`L62`](../../../../../../raw/code/torch_tpu/csrc/common/reroute_warnings.cc#L62) — Protects `warnings_`.
  - <a id="DelayedWarningHandler.warnings_"></a>`warnings_` — [`L61`](../../../../../../raw/code/torch_tpu/csrc/common/reroute_warnings.cc#L61)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`SurfaceReroutedWarnings`](reroute_warnings.cc.md#SurfaceReroutedWarnings), [`GetDelayedWarningHandler`](reroute_warnings.cc.md#GetDelayedWarningHandler)

## Functions
- <a id="GetDelayedWarningHandler"></a>`GetDelayedWarningHandler()` — [`L66`](../../../../../../raw/code/torch_tpu/csrc/common/reroute_warnings.cc#L66) — Returns the process-wide rerouted warning handler singleton.
- <a id="RouteWarningsOnThisThreadToDispatchThread"></a>`RouteWarningsOnThisThreadToDispatchThread()` — [`L73`](../../../../../../raw/code/torch_tpu/csrc/common/reroute_warnings.cc#L73) — Makes the calling thread reroute its c10 warnings to dispatch threads, i.e.
- <a id="SurfaceReroutedWarnings"></a>`SurfaceReroutedWarnings()` — [`L77`](../../../../../../raw/code/torch_tpu/csrc/common/reroute_warnings.cc#L77) — Raises all rerouted warnings, from every background thread, through the

