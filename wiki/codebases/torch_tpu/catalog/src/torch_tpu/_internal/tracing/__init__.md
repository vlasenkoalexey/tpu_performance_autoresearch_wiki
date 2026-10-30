---
title: 'Module: src/torch_tpu/_internal/tracing/__init__.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/tracing/__init__.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.tracing`/
symbols:
  _atexit_flush: _atexit_flush().
  enable_if_requested: enable_if_requested().
  _daemon._daemon: _daemon._daemon.
  _FlushDaemon.run: _FlushDaemon#run().
  _flush: _flush().
  _emit_chromium: _emit_chromium().
  _emit_event_artifacts: _emit_event_artifacts().
  _FlushDaemon.stop: _FlushDaemon#stop().
  _FLUSH_INTERVAL_SECONDS: _FLUSH_INTERVAL_SECONDS.
  _const_thunk: _const_thunk().
  _FlushDaemon: _FlushDaemon#
  _FlushDaemon._stop_event: _FlushDaemon#_stop_event.
  _lock: _lock.
  _FlushDaemon.__init__: _FlushDaemon#__init__().
---
# Module: [`src/torch_tpu/_internal/tracing/__init__.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/tracing/__init__.py)

## Classes
### <a id="_FlushDaemon"></a>`_FlushDaemon`  ·  implements/extends Thread
- def: [`src/torch_tpu/_internal/tracing/__init__.py:109`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/tracing/__init__.py#L109)
- doc: Background thread that drains the buffer every _FLUSH_INTERVAL_SECONDS.
- signature: `class _FlushDaemon(threading.Thread):`
- members:
  - <a id="_FlushDaemon.run"></a>`run(self)` — [`L116`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/tracing/__init__.py#L116)
  - <a id="_FlushDaemon.stop"></a>`stop(self)` — [`L122`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/tracing/__init__.py#L122)
- protocol/private: <a id="_FlushDaemon.__init__"></a>`__init__`[`L112`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/tracing/__init__.py#L112), <a id="_FlushDaemon._stop_event"></a>`_stop_event`[`L114`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/tracing/__init__.py#L114)
- uses (calls/refs, reference-scoped): [`_flush`](__init__.md#_flush), [`_FLUSH_INTERVAL_SECONDS`](__init__.md#_FLUSH_INTERVAL_SECONDS)
- used by: [`_atexit_flush`](__init__.md#_atexit_flush), [`enable_if_requested`](__init__.md#enable_if_requested), [`_daemon`](__init__.md#_daemon._daemon)

## Functions
- <a id="_atexit_flush"></a>`_atexit_flush()` — [`L131`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/tracing/__init__.py#L131) — Stop the daemon and let its run() loop do the final flush.
- <a id="_const_thunk"></a>`_const_thunk(value: Any)` — [`L39`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/tracing/__init__.py#L39) — Create a closure capturing the value.
- <a id="_emit_chromium"></a>`_emit_chromium(event: Mapping[str, Any])` — [`L44`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/tracing/__init__.py#L44) — Thread-safe: emit one chromium_event for an eager batch.
- <a id="_emit_event_artifacts"></a>`_emit_event_artifacts(event: Mapping[str, Any])` — [`L62`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/tracing/__init__.py#L62) — Thread-safe: emit aten_graph and stablehlo artifacts for one batch.
- <a id="_flush"></a>`_flush()` — [`L91`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/tracing/__init__.py#L91) — Drain the C++ buffer and emit artifacts. Safe from any thread.
- <a id="enable_if_requested"></a>`enable_if_requested()` — [`L153`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/tracing/__init__.py#L153) — Initialize the tracing daemon if TORCH_TRACE was set at startup.

## Module values
- <a id="_FLUSH_INTERVAL_SECONDS"></a>`_FLUSH_INTERVAL_SECONDS` — [`L36`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/tracing/__init__.py#L36)
- <a id="_daemon._daemon"></a>`_daemon` — [`L126`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/tracing/__init__.py#L126)
- <a id="_lock"></a>`_lock` — [`L128`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/tracing/__init__.py#L128)

