---
title: 'Module: csrc/internal/profiler/profiler_api.cc'
type: catalog
provenance: extracted
module: csrc/internal/profiler/profiler_api.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  TpuProfilerSession.Stop: TpuProfilerSession#Stop(9a836fbe81584ab8).
  TpuProfilerSession.Start: TpuProfilerSession#Start(69133efc36e4646c).
  TpuProfilerServer.Start: TpuProfilerServer#Start(19661756065552c8).
  TorchTpuPyBindInitModule__profiler_backend: TorchTpuPyBindInitModule__profiler_backend(d5b68cea704bb038).
  TpuProfilerServer.Stop: TpuProfilerServer#Stop(c8a92d17d58c956f).
  PyStopProfilerServer: PyStopProfilerServer(49f6e7a06ebc5aa8).
  PyStopTrace: PyStopTrace(9c546c94e5fcce4e).
  PyStartProfilerServer: PyStartProfilerServer(d4f767463ce0a6b3).
  PyStartTrace: PyStartTrace(eaaece8c6dadbf86).
  TpuProfilerSession: TpuProfilerSession#
  TpuProfilerServer: TpuProfilerServer#
  TpuProfilerServer.mutex_: TpuProfilerServer#mutex_.
  TpuProfilerSession.session_: TpuProfilerSession#session_.
  TpuProfilerSession.mutex_: TpuProfilerSession#mutex_.
  TpuProfilerSession.operator: TpuProfilerSession#`operator=`(be43ddea2659d027).
  TpuProfilerServer.operator: TpuProfilerServer#`operator=`(96a5369c1ef1d4df).
  TpuProfilerServer.server_: TpuProfilerServer#server_.
  TpuProfilerServer.GetInstance: TpuProfilerServer#GetInstance(ed46e903fc1a8a54).
  TpuProfilerSession.GetInstance: TpuProfilerSession#GetInstance(bdd39658dab29e59).
  pybind11_exec__profiler_backend: pybind11_exec__profiler_backend(6642082b04e1bfd8).
  pybind11_init__profiler_backend: pybind11_init__profiler_backend(85901dfccbeca8c6).
  TpuProfilerSession.TpuProfilerSession: TpuProfilerSession#TpuProfilerSession(8d42ce276d6f16de).
  TpuProfilerServer.TpuProfilerServer: TpuProfilerServer#TpuProfilerServer(b67e0ea6ad025528).
---
# Module: [`csrc/internal/profiler/profiler_api.cc`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc)

## Classes
### <a id="TpuProfilerServer"></a>`TpuProfilerServer`
- def: [`csrc/internal/profiler/profiler_api.cc:47`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L47) — documented in [profiler](../../../../concepts/profiler.md)
- doc: Thread-safe wrapper for tsl::profiler::ProfilerServer.
- signature: `class TpuProfilerServer`
- members:
  - <a id="TpuProfilerServer.GetInstance"></a>`GetInstance()` — [`L67`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L67) — Returns the global profiler server instance.
  - <a id="TpuProfilerServer.Start"></a>`Start(int port)` — [`L111`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L111) — Starts the profiler server on the given port. Fails if the server has — documented in [profiler](../../../../concepts/profiler.md)
  - <a id="TpuProfilerServer.Stop"></a>`Stop()` — [`L121`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L121) — Stops the profiler server. Fails if the server has not been started or has — documented in [profiler](../../../../concepts/profiler.md)
  - `TpuProfilerServer()` — [`L50`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L50) — Creates a server in not-started state.
  - <a id="TpuProfilerServer.TpuProfilerServer"></a>`TpuProfilerServer(const TpuProfilerServer&)` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L53) — This class is neither copyable nor movable.
  - `TpuProfilerServer(TpuProfilerServer&&)` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L55)
  - <a id="TpuProfilerServer.operator"></a>`operator=(TpuProfilerServer&&)` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L56)
  - `operator=(const TpuProfilerServer&)` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L54)
  - <a id="TpuProfilerServer.mutex_"></a>`mutex_` — [`L73`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L73) — documented in [profiler](../../../../concepts/profiler.md)
  - <a id="TpuProfilerServer.server_"></a>`server_` — [`L74`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L74) — documented in [profiler](../../../../concepts/profiler.md)
- uses (calls/refs, reference-scoped): [`NormalizeIfInsideBuildDirectory`](../../common/macro_utils.cc.md#NormalizeIfInsideBuildDirectory), [`MaybeAddCppSourceLoc`](../../common/status_builder.cc.md#MaybeAddCppSourceLoc), [`GetRootOpName`](../../ops/python_context.cc.md#GetRootOpName), [`SetRootOpNamePayload`](../../common/status_builder.cc.md#SetRootOpNamePayload), [`StatusBuilder`](../../common/status_builder.h.md#StatusBuilder), [`operator<<`](../../common/status_builder.h.md#StatusBuilder.operator), [`StatusBuilder`](../../common/status_builder.cc.md#StatusBuilder.StatusBuilder), [`kFailedPrecondition`](../../common/error_utils.h.md#kFailedPrecondition), [`TpuProfilerSession`](profiler_api.cc.md#TpuProfilerSession), [`XProfCallbackHandler`](xprof_callback_handler.h.md#XProfCallbackHandler), [`Register`](xprof_callback_handler.cc.md#XProfCallbackHandler.Register)
- used by: [`PyStartProfilerServer`](profiler_api.cc.md#PyStartProfilerServer), [`PyStopProfilerServer`](profiler_api.cc.md#PyStopProfilerServer), [`session_`](profiler_api.cc.md#TpuProfilerSession.session_)

### <a id="TpuProfilerSession"></a>`TpuProfilerSession`
- def: [`csrc/internal/profiler/profiler_api.cc:79`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L79) — documented in [profiler](../../../../concepts/profiler.md)
- doc: Thread-safe wrapper for tsl::ProfilerSession.
- signature: `class TpuProfilerSession`
- members:
  - <a id="TpuProfilerSession.GetInstance"></a>`GetInstance()` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L100) — Returns the global profiler session instance. — documented in [profiler](../../../../concepts/profiler.md)
  - <a id="TpuProfilerSession.Start"></a>`Start(const std::string& logdir, py::object options_obj)` — [`L130`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L130) — Starts the profiler session on the given log directory with the given — documented in [profiler](../../../../concepts/profiler.md)
  - <a id="TpuProfilerSession.Stop"></a>`Stop(const std::string& filename)` — [`L166`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L166) — Stops the profiler session and writes the trace data to the given file. — documented in [profiler](../../../../concepts/profiler.md)
  - `TpuProfilerSession()` — [`L82`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L82) — Creates a session in not-started state.
  - <a id="TpuProfilerSession.TpuProfilerSession"></a>`TpuProfilerSession(const TpuProfilerSession&)` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L85) — This class is neither copyable nor movable.
  - `TpuProfilerSession(TpuProfilerSession&&)` — [`L87`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L87)
  - <a id="TpuProfilerSession.operator"></a>`operator=(TpuProfilerSession&&)` — [`L88`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L88) — documented in [profiler](../../../../concepts/profiler.md)
  - `operator=(const TpuProfilerSession&)` — [`L86`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L86)
  - <a id="TpuProfilerSession.mutex_"></a>`mutex_` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L106) — documented in [profiler](../../../../concepts/profiler.md)
  - <a id="TpuProfilerSession.session_"></a>`session_` — [`L107`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L107) — documented in [profiler](../../../../concepts/profiler.md)
- uses (calls/refs, reference-scoped): [`NormalizeIfInsideBuildDirectory`](../../common/macro_utils.cc.md#NormalizeIfInsideBuildDirectory), [`MaybeAddCppSourceLoc`](../../common/status_builder.cc.md#MaybeAddCppSourceLoc), [`GetRootOpName`](../../ops/python_context.cc.md#GetRootOpName), [`SetRootOpNamePayload`](../../common/status_builder.cc.md#SetRootOpNamePayload), [`StatusBuilder`](../../common/status_builder.h.md#StatusBuilder), [`operator<<`](../../common/status_builder.h.md#StatusBuilder.operator), [`ReturnIfErrorAdaptor`](../../common/error_utils.h.md#ReturnIfErrorAdaptor), [`ReturnIfErrorAdaptor`](../../common/error_utils.h.md#ReturnIfErrorAdaptor.ReturnIfErrorAdaptor), [`StatusBuilder`](../../common/status_builder.cc.md#StatusBuilder.StatusBuilder), [`GetStatus`](../../common/error_utils.h.md#GetStatus), [`Consume`](../../common/error_utils.h.md#ReturnIfErrorAdaptor.Consume), [`kInternal`](../../common/error_utils.h.md#kInternal), [`SetPrepend`](../../common/status_builder.h.md#StatusBuilder.SetPrepend), [`kFailedPrecondition`](../../common/error_utils.h.md#kFailedPrecondition), [`TpuProfilerServer`](profiler_api.cc.md#TpuProfilerServer)
- used by: [`Stop`](profiler_api.cc.md#TpuProfilerServer.Stop), [`PyStartTrace`](profiler_api.cc.md#PyStartTrace), [`PyStopTrace`](profiler_api.cc.md#PyStopTrace)

## Functions
- <a id="PyStartProfilerServer"></a>`PyStartProfilerServer(int port)` — [`L216`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L216) — documented in [profiler](../../../../concepts/profiler.md)
- <a id="PyStartTrace"></a>`PyStartTrace(const std::string& logdir, py::object options_obj)` — [`L224`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L224) — documented in [profiler](../../../../concepts/profiler.md)
- <a id="PyStopProfilerServer"></a>`PyStopProfilerServer()` — [`L220`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L220) — documented in [profiler](../../../../concepts/profiler.md)
- <a id="PyStopTrace"></a>`PyStopTrace(const std::string& filename)` — [`L229`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L229) — documented in [profiler](../../../../concepts/profiler.md)
- <a id="TorchTpuPyBindInitModule__profiler_backend"></a>`TorchTpuPyBindInitModule__profiler_backend(_profiler_backend, m)` — [`L233`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L233) — documented in [profiler](../../../../concepts/profiler.md)
- <a id="pybind11_exec__profiler_backend"></a>`pybind11_exec__profiler_backend(_profiler_backend, m)` — [`L233`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L233) — documented in [profiler](../../../../concepts/profiler.md)
- <a id="pybind11_init__profiler_backend"></a>`pybind11_init__profiler_backend(_profiler_backend, m)` — [`L233`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/profiler_api.cc#L233) — documented in [profiler](../../../../concepts/profiler.md)

