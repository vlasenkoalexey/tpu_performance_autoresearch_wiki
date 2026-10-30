---
title: 'Module: csrc/internal/profiler/tpu_profiler_plugin.h'
type: catalog
provenance: extracted
module: csrc/internal/profiler/tpu_profiler_plugin.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  TpuKinetoProfilerSession: TpuKinetoProfilerSession#
  TpuProfiler.configure: TpuProfiler#configure(aef3f8625dd7810).
  TpuKinetoProfilerSession.errors: TpuKinetoProfilerSession#errors(c1a9bfb60daa162d).
  TpuKinetoProfilerSession.session_: TpuKinetoProfilerSession#session_.
  TpuKinetoProfilerSession.mutex_: TpuKinetoProfilerSession#mutex_.
  TpuKinetoProfilerSession.errors_: TpuKinetoProfilerSession#errors_.
  TpuKinetoProfilerSession.xspace_: TpuKinetoProfilerSession#xspace_.
  TpuKinetoProfilerSession.worker_rank_: TpuKinetoProfilerSession#worker_rank_.
  TpuKinetoProfilerSession.run_dir_: TpuKinetoProfilerSession#run_dir_.
  TpuKinetoProfilerSession.config_: TpuKinetoProfilerSession#config_.
  TpuKinetoProfilerSession.activity_types_: TpuKinetoProfilerSession#activity_types_.
  TpuProfiler.availableActivities: TpuProfiler#availableActivities(ec45a031f4e09d1e).
  TpuKinetoProfilerSession.getTraceBuffer: TpuKinetoProfilerSession#getTraceBuffer(b126dc7c1de90089).
  TpuProfiler.name: TpuProfiler#name(f4fff0029955a25f).
  TpuKinetoProfilerSession.getResourceInfos: TpuKinetoProfilerSession#getResourceInfos(9cb232b71011d867).
  TpuKinetoProfilerSession.resource_infos_: TpuKinetoProfilerSession#resource_infos_.
  TpuKinetoProfilerSession.callback_handler_: TpuKinetoProfilerSession#callback_handler_.
  TpuProfiler: TpuProfiler#
  TpuKinetoProfilerSession.start_time_ns_: TpuKinetoProfilerSession#start_time_ns_.
  TpuKinetoProfilerSession.getDeviceInfo: TpuKinetoProfilerSession#getDeviceInfo(6c02916d8585e6f4).
---
# Module: [`csrc/internal/profiler/tpu_profiler_plugin.h`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h)

## Classes
### <a id="TpuKinetoProfilerSession"></a>`TpuKinetoProfilerSession`  ·  implements/extends IActivityProfilerSession
- def: [`csrc/internal/profiler/tpu_profiler_plugin.h:42`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L42) — documented in [profiler](../../../../concepts/profiler.md)
- doc: TPU implementation of libkineto::IActivityProfilerSession.
- signature: `class TpuKinetoProfilerSession : public libkineto::IActivityProfilerSession`
- members:
  - `errors()` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L49)
  - <a id="TpuKinetoProfilerSession.errors"></a>`errors()` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L49)
  - <a id="TpuKinetoProfilerSession.getDeviceInfo"></a>`getDeviceInfo()` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L54)
  - `getDeviceInfo()` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L54)
  - `getResourceInfos()` — [`L62`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L62)
  - <a id="TpuKinetoProfilerSession.getResourceInfos"></a>`getResourceInfos()` — [`L62`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L62)
  - <a id="TpuKinetoProfilerSession.getTraceBuffer"></a>`getTraceBuffer()` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L65)
  - `getTraceBuffer()` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L65)
  - <a id="TpuKinetoProfilerSession.activity_types_"></a>`activity_types_` — [`L75`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L75)
  - <a id="TpuKinetoProfilerSession.callback_handler_"></a>`callback_handler_` — [`L76`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L76)
  - <a id="TpuKinetoProfilerSession.config_"></a>`config_` — [`L74`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L74)
  - <a id="TpuKinetoProfilerSession.errors_"></a>`errors_` — [`L73`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L73) — documented in [profiler](../../../../concepts/profiler.md)
  - <a id="TpuKinetoProfilerSession.mutex_"></a>`mutex_` — [`L70`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L70) — documented in [profiler](../../../../concepts/profiler.md)
  - <a id="TpuKinetoProfilerSession.resource_infos_"></a>`resource_infos_` — [`L80`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L80)
  - <a id="TpuKinetoProfilerSession.run_dir_"></a>`run_dir_` — [`L77`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L77) — documented in [profiler](../../../../concepts/profiler.md)
  - <a id="TpuKinetoProfilerSession.session_"></a>`session_` — [`L71`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L71) — documented in [profiler](../../../../concepts/profiler.md)
  - <a id="TpuKinetoProfilerSession.start_time_ns_"></a>`start_time_ns_` — [`L79`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L79)
  - <a id="TpuKinetoProfilerSession.worker_rank_"></a>`worker_rank_` — [`L78`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L78) — documented in [profiler](../../../../concepts/profiler.md)
  - <a id="TpuKinetoProfilerSession.xspace_"></a>`xspace_` — [`L72`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L72)
- uses (calls/refs, reference-scoped): [`start`](tpu_profiler_plugin.cc.md#TpuKinetoProfilerSession.start), [`stop`](tpu_profiler_plugin.cc.md#TpuKinetoProfilerSession.stop), [`XProfCallbackHandler`](xprof_callback_handler.h.md#XProfCallbackHandler), [`processTrace`](tpu_profiler_plugin.cc.md#TpuKinetoProfilerSession.processTrace), [`TpuKinetoProfilerSession`](tpu_profiler_plugin.cc.md#TpuKinetoProfilerSession.TpuKinetoProfilerSession), [`TpuKinetoProfilerSession`](tpu_profiler_plugin.cc.md#TpuKinetoProfilerSession.TpuKinetoProfilerSession)
- used by: [`start`](tpu_profiler_plugin.cc.md#TpuKinetoProfilerSession.start), [`stop`](tpu_profiler_plugin.cc.md#TpuKinetoProfilerSession.stop), [`processTrace`](tpu_profiler_plugin.cc.md#TpuKinetoProfilerSession.processTrace), [`AddActivityStringMetadata`](tpu_profiler_plugin.cc.md#AddActivityStringMetadata), [`SynchronizeTpuDevicesBeforeStop`](tpu_profiler_plugin.cc.md#SynchronizeTpuDevicesBeforeStop), [`GetXPlaneOutputPath`](tpu_profiler_plugin.cc.md#GetXPlaneOutputPath), [`TpuKinetoProfilerSession`](tpu_profiler_plugin.cc.md#TpuKinetoProfilerSession.TpuKinetoProfilerSession), [`configure`](tpu_profiler_plugin.h.md#TpuProfiler.configure)

### <a id="TpuProfiler"></a>`TpuProfiler`  ·  implements/extends IActivityProfiler
- def: [`csrc/internal/profiler/tpu_profiler_plugin.h:85`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L85)
- doc: TPU implementation of libkineto::IActivityProfiler.
- signature: `class TpuProfiler : public libkineto::IActivityProfiler`
- members:
  - <a id="TpuProfiler.availableActivities"></a>`availableActivities()` — [`L91`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L91)
  - `availableActivities()` — [`L91`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L91)
  - `configure(int64_t /*ts_ms*/, int64_t /*duration_ms*/, const std::set<libkineto::ActivityType>& activity_types, const libkineto::Config& config)` — [`L104`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L104)
  - `configure(const std::set<libkineto::ActivityType>& activity_types, const libkineto::Config& config)` — [`L99`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L99)
  - <a id="TpuProfiler.configure"></a>`configure(int64_t /*ts_ms*/, int64_t /*duration_ms*/, const std::set<libkineto::ActivityType>& activity_types, const libkineto::Config& config)` — [`L104`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L104) — documented in [profiler](../../../../concepts/profiler.md)
  - `configure(const std::set<libkineto::ActivityType>& activity_types, const libkineto::Config& config)` — [`L99`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L99)
  - <a id="TpuProfiler.name"></a>`name()` — [`L87`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.h#L87)
- uses (calls/refs, reference-scoped): [`UpdateProfileOptions`](tpu_profiler_plugin.cc.md#UpdateProfileOptions), [`TpuKinetoProfilerSession`](tpu_profiler_plugin.h.md#TpuKinetoProfilerSession), [`GetProfilerBaseOutputDir`](tpu_profiler_plugin.cc.md#GetProfilerBaseOutputDir), [`AddActivityStringMetadata`](tpu_profiler_plugin.cc.md#AddActivityStringMetadata), [`SanitizeStatString`](tpu_profiler_plugin.cc.md#SanitizeStatString), [`UpdateProfileOptions`](tpu_profiler_plugin.cc.md#UpdateProfileOptions)
- used by: [`TpuProfilerRegisterer`](tpu_profiler_plugin.cc.md#TpuProfilerRegisterer.TpuProfilerRegisterer)

