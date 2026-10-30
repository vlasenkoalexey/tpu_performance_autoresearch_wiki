---
title: 'Module: csrc/internal/profiler/tpu_profiler_plugin.cc'
type: catalog
provenance: extracted
module: csrc/internal/profiler/tpu_profiler_plugin.cc
status: fresh
symbol_base: 'cxx . . $ '
symbols:
  UpdateProfileOptions: torch_tpu/UpdateProfileOptions(d4012e7ea7627f06).
  TpuKinetoProfilerSession.start: torch_tpu/TpuKinetoProfilerSession#start(49f6e7a06ebc5aa8).
  SplitConfigItem: torch_tpu/SplitConfigItem(db756746ae73b5a7).
  SetAdvancedConfigValue: torch_tpu/SetAdvancedConfigValue(ea8128f21314875f).
  ParseAndSetUint: torch_tpu/ParseAndSetUint(b888ffa22eaf97a7).
  UnescapeString: torch_tpu/UnescapeString(7f3ab1e6a6f5c9ea).
  TpuKinetoProfilerSession.stop: torch_tpu/TpuKinetoProfilerSession#stop(49f6e7a06ebc5aa8).
  TpuProfilerRegisterer.TpuProfilerRegisterer: torch_tpu/`$anonymous_namespace_csrc/internal/profiler/tpu_profiler_plugin.cc`/TpuProfilerRegisterer#TpuProfilerRegisterer(49f6e7a06ebc5aa8).
  TpuKinetoProfilerSession.processTrace: torch_tpu/TpuKinetoProfilerSession#processTrace(621d9360d5789134).
  GetProfilerBaseOutputDir: torch_tpu/GetProfilerBaseOutputDir(6ccff4770ff7ddc3).
  UpdateProfileOption: torch_tpu/UpdateProfileOption(ea8128f21314875f).
  SynchronizeTpuDevicesBeforeStop: torch_tpu/`$anonymous_namespace_csrc/internal/profiler/tpu_profiler_plugin.cc`/SynchronizeTpuDevicesBeforeStop(c8a92d17d58c956f).
  AddActivityStringMetadata: torch_tpu/AddActivityStringMetadata(3f9999aa564088a2).
  TpuKinetoProfilerSession.TpuKinetoProfilerSession: torch_tpu/TpuKinetoProfilerSession#TpuKinetoProfilerSession(bd6d30566586cb87).
  GetXPlaneOutputPath: torch_tpu/`$anonymous_namespace_csrc/internal/profiler/tpu_profiler_plugin.cc`/GetXPlaneOutputPath(b741151b6ea3152f).
  SplitConfig: torch_tpu/SplitConfig(47df7fe2c8915231).
  PrivateUse1ProfilerRegistry: torch/profiler/impl/PrivateUse1ProfilerRegistry#
  SanitizeStatString: torch_tpu/SanitizeStatString(6ccff4770ff7ddc3).
  ProfilerOption: torch_tpu/ProfilerOption#
  registerer: torch_tpu/`$anonymous_namespace_csrc/internal/profiler/tpu_profiler_plugin.cc`/registerer.
  ProfilerOption.value: torch_tpu/ProfilerOption#value.
  FindNextSeparator: torch_tpu/FindNextSeparator(d63a1d93027fd566).
  kRunDir: torch_tpu/kRunDir.
  PrivateUse1ProfilerFactory: torch/profiler/impl/PrivateUse1ProfilerFactory#
  kWorkerRank: torch_tpu/kWorkerRank.
  TpuProfilerRegisterer: torch_tpu/`$anonymous_namespace_csrc/internal/profiler/tpu_profiler_plugin.cc`/TpuProfilerRegisterer#
  kHostTracerLevel: torch_tpu/kHostTracerLevel.
  kDeviceTracerLevel: torch_tpu/kDeviceTracerLevel.
  GetXProfSessionStartTimeNs: torch_tpu/`$anonymous_namespace_csrc/internal/profiler/tpu_profiler_plugin.cc`/GetXProfSessionStartTimeNs(8a6a13d7d46d4ec1).
  kPythonTracerLevel: torch_tpu/kPythonTracerLevel.
  ProfilerOption.name: torch_tpu/ProfilerOption#name.
---
# Module: [`csrc/internal/profiler/tpu_profiler_plugin.cc`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc)

## Classes
### <a id="PrivateUse1ProfilerFactory"></a>`PrivateUse1ProfilerFactory`
- def: [`csrc/internal/profiler/tpu_profiler_plugin.cc:75`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L75)
- signature: `using PrivateUse1ProfilerFactory = std::function< std::unique_ptr<libkineto::IActivityProfiler>()>`
- used by: [`PrivateUse1ProfilerRegistry`](tpu_profiler_plugin.cc.md#PrivateUse1ProfilerRegistry)

### <a id="PrivateUse1ProfilerRegistry"></a>`PrivateUse1ProfilerRegistry`
- def: [`csrc/internal/profiler/tpu_profiler_plugin.cc:78`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L78)
- signature: `class PrivateUse1ProfilerRegistry`
- uses (calls/refs, reference-scoped): [`PrivateUse1ProfilerFactory`](tpu_profiler_plugin.cc.md#PrivateUse1ProfilerFactory)
- used by: [`TpuProfilerRegisterer`](tpu_profiler_plugin.cc.md#TpuProfilerRegisterer.TpuProfilerRegisterer)

### <a id="ProfilerOption"></a>`ProfilerOption`
- def: [`csrc/internal/profiler/tpu_profiler_plugin.cc:96`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L96)
- doc: Represents a parsed custom configuration option.
- signature: `struct ProfilerOption`
- members:
  - <a id="ProfilerOption.name"></a>`name` — [`L97`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L97)
  - <a id="ProfilerOption.value"></a>`value` — [`L98`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L98)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`UpdateProfileOptions`](tpu_profiler_plugin.cc.md#UpdateProfileOptions), [`SplitConfigItem`](tpu_profiler_plugin.cc.md#SplitConfigItem), [`SplitConfig`](tpu_profiler_plugin.cc.md#SplitConfig)

### <a id="TpuProfilerRegisterer"></a>`TpuProfilerRegisterer`
- def: [`csrc/internal/profiler/tpu_profiler_plugin.cc:790`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L790)
- signature: `struct TpuProfilerRegisterer`
- members:
  - <a id="TpuProfilerRegisterer.TpuProfilerRegisterer"></a>`TpuProfilerRegisterer()` — [`L791`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L791) — documented in [profiler](../../../../concepts/profiler.md)
- uses (calls/refs, reference-scoped): [`PrivateUse1ProfilerRegistry`](tpu_profiler_plugin.cc.md#PrivateUse1ProfilerRegistry), [`TpuProfiler`](tpu_profiler_plugin.h.md#TpuProfiler)
- used by: [`registerer`](tpu_profiler_plugin.cc.md#registerer)

## Functions
- <a id="AddActivityStringMetadata"></a>`AddActivityStringMetadata(libkineto::GenericTraceActivity& activity, const std::string& key, std::string_view value)` — [`L589`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L589) — Adds a string metadata entry to a Kineto trace activity, ensuring that the
- <a id="FindNextSeparator"></a>`FindNextSeparator(std::string_view custom_config, char sep, size_t start = 0)` — [`L221`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L221) — Helper to find the next comma or colon separator while ignoring delimiters
- <a id="GetProfilerBaseOutputDir"></a>`GetProfilerBaseOutputDir(std::string_view run_dir)` — [`L332`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L332) — Resolves the base output directory for profiling artifacts. — documented in [profiler](../../../../concepts/profiler.md)
- <a id="GetXPlaneOutputPath"></a>`GetXPlaneOutputPath(std::string_view run_dir, std::optional<std::string_view> worker_rank)` — [`L365`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L365) — Helper to determine the output path for the XPlane file.
- <a id="GetXProfSessionStartTimeNs"></a>`GetXProfSessionStartTimeNs(const tensorflow::profiler::XSpace& space)` — [`L551`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L551)
- <a id="ParseAndSetUint"></a>`ParseAndSetUint(tensorflow::ProfileOptions& opts, std::string_view key, std::string_view val, void (tensorflow::ProfileOptions::*setter)(uint32_t))` — [`L102`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L102) — Helper to parse uint32_t and apply to a setter method of ProfileOptions. — documented in [profiler](../../../../concepts/profiler.md)
- <a id="SanitizeStatString"></a>`SanitizeStatString(std::string_view s)` — [`L581`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L581) — Sanitizes a string stat value for Kineto activity metadata. Kineto's
- <a id="SetAdvancedConfigValue"></a>`SetAdvancedConfigValue(tensorflow::ProfileOptions& opts, std::string_view key, std::string_view val)` — [`L168`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L168) — Parses the value and sets it in the advanced_configuration map. — documented in [profiler](../../../../concepts/profiler.md)
- `SplitConfig(std::string_view custom_config, char sep)` — [`L243`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L243) — Helper to split a string by an escape-aware separator, ignoring delimiters
- <a id="SplitConfig"></a>`SplitConfig(std::string_view custom_config, char sep)` — [`L243`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L243) — Helper to split a string by an escape-aware separator, ignoring delimiters
- <a id="SplitConfigItem"></a>`SplitConfigItem(std::string_view item)` — [`L262`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L262) — Splits a single custom config item (e.g., "key:value") by the first — documented in [profiler](../../../../concepts/profiler.md)
- <a id="SynchronizeTpuDevicesBeforeStop"></a>`SynchronizeTpuDevicesBeforeStop()` — [`L464`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L464) — Synchronizes all TPU devices and deferred operations before stopping trace
- <a id="UnescapeString"></a>`UnescapeString(std::string_view s)` — [`L140`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L140) — Unescapes a string value by removing backslashes that escape other — documented in [profiler](../../../../concepts/profiler.md)
- <a id="UpdateProfileOption"></a>`UpdateProfileOption(tensorflow::ProfileOptions& opts, std::string_view key, std::string_view val)` — [`L202`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L202) — Updates a single key-value option in the ProfileOptions. — documented in [profiler](../../../../concepts/profiler.md)
- <a id="UpdateProfileOptions"></a>`UpdateProfileOptions(std::string_view custom_config, tensorflow::ProfileOptions& opts, std::string& out_run_dir, std::optional<std::string>& out_worker_rank)` — [`L280`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L280) — Parses the custom configuration string from Kineto. Leading and trailing — documented in [profiler](../../../../concepts/profiler.md)
- `UpdateProfileOptions(std::string_view custom_config, tensorflow::ProfileOptions& opts, std::string& out_run_dir)` — [`L323`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L323)

## Module values
- <a id="kDeviceTracerLevel"></a>`kDeviceTracerLevel` — [`L89`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L89) — The set of valid parameter names for configuring the TPU profiler.
- <a id="kHostTracerLevel"></a>`kHostTracerLevel` — [`L90`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L90)
- <a id="kPythonTracerLevel"></a>`kPythonTracerLevel` — [`L91`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L91)
- <a id="kRunDir"></a>`kRunDir` — [`L92`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L92)
- <a id="kWorkerRank"></a>`kWorkerRank` — [`L93`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L93)
- <a id="registerer"></a>`registerer` — [`L807`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L807)

## Other members
- `TpuKinetoProfilerSession` — [`L404`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L404)
- <a id="TpuKinetoProfilerSession.TpuKinetoProfilerSession"></a>`TpuKinetoProfilerSession.TpuKinetoProfilerSession` — [`L404`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L404)
- <a id="TpuKinetoProfilerSession.processTrace"></a>`TpuKinetoProfilerSession.processTrace` — [`L594`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L594) — documented in [profiler](../../../../concepts/profiler.md)
- <a id="TpuKinetoProfilerSession.start"></a>`TpuKinetoProfilerSession.start` — [`L409`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L409) — documented in [profiler](../../../../concepts/profiler.md)
- <a id="TpuKinetoProfilerSession.stop"></a>`TpuKinetoProfilerSession.stop` — [`L485`](../../../../../../../raw/code/torch_tpu/csrc/internal/profiler/tpu_profiler_plugin.cc#L485) — documented in [profiler](../../../../concepts/profiler.md)

