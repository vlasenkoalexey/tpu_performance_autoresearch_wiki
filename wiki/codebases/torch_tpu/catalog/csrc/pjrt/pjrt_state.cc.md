---
title: 'Module: csrc/pjrt/pjrt_state.cc'
type: catalog
provenance: extracted
module: csrc/pjrt/pjrt_state.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  PjrtBackend.GetInstance: PjrtBackend#GetInstance(bee92f14968c483b).
  PjrtBackend.GetClient: PjrtBackend#GetClient(bd9011293b413159).
  PjrtBackend.EnsureInitialized: PjrtBackend#EnsureInitialized(c8a92d17d58c956f).
  PjrtBackend.InitializeInternal: PjrtBackend#InitializeInternal(c8a92d17d58c956f).
  PjrtBackend.SetPjRtInitializationOptions: PjrtBackend#SetPjRtInitializationOptions(2c78ad74ad3472b8).
  PjrtBackend.GetDevice: PjrtBackend#GetDevice(845b845cdfe8e8b).
  PjrtBackend.GetDeviceAttributes: PjrtBackend#GetDeviceAttributes(fae9dac868590d1b).
  PjrtBackend.GetGlobalDeviceCount: PjrtBackend#GetGlobalDeviceCount(f1bb9610c0ed55db).
  PjrtBackend.GetGlobalDeviceId: PjrtBackend#GetGlobalDeviceId(f1bb9610c0ed55db).
  PjrtBackend.IsInitialized: PjrtBackend#IsInitialized(50ce9a9e25b4a850).
  PjrtBackend.Shutdown: PjrtBackend#Shutdown(49f6e7a06ebc5aa8).
  PjrtBackend.GetHostAllocator: PjrtBackend#GetHostAllocator(26f08a07f7dc4741).
  PjrtBackend.GetSharedClient: PjrtBackend#GetSharedClient(26d35c9b5f35d4b6).
  PjrtBackend.GetAllocatorStats: PjrtBackend#GetAllocatorStats(c05f45b05459021e).
  PjrtBackend.ClearAllocatorStats: PjrtBackend#ClearAllocatorStats(c8a92d17d58c956f).
  PjrtBackend.IsInBadFork: PjrtBackend#IsInBadFork(50ce9a9e25b4a850).
  PjrtBackend.GetDeviceType: PjrtBackend#GetDeviceType(e1ae45ce462af988).
  MaybeSkipMegascaleForLaterClients: '`$anonymous_namespace_csrc/pjrt/pjrt_state.cc`/MaybeSkipMegascaleForLaterClients(794bbbca577513a2).'
  TryExpandRankInEnvVar: '`$anonymous_namespace_csrc/pjrt/pjrt_state.cc`/TryExpandRankInEnvVar(c8024318075daf50).'
  MaybeRegisterProfiler: '`$anonymous_namespace_csrc/pjrt/pjrt_state.cc`/MaybeRegisterProfiler(c8024318075daf50).'
  CreateTpuProfiler: '`$anonymous_namespace_csrc/pjrt/pjrt_state.cc`/CreateTpuProfiler(938757c242be677c).'
  GetIntAttribute: '`$anonymous_namespace_csrc/pjrt/pjrt_state.cc`/GetIntAttribute(52748d61f94e7edc).'
  GetIntVecAttribute: '`$anonymous_namespace_csrc/pjrt/pjrt_state.cc`/GetIntVecAttribute(269bb3f5b80e34ae).'
---
# Module: [`csrc/pjrt/pjrt_state.cc`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc)

## Functions
- <a id="CreateTpuProfiler"></a>`CreateTpuProfiler(const PLUGIN_Profiler_Api* absl_nonnull profiler_api, const tensorflow::ProfileOptions& opts)` — [`L78`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L78) — Creates a PluginTracer instance to collect TPU profile metrics.
- `CreateTpuProfiler(const PLUGIN_Profiler_Api* absl_nonnull profiler_api, const tensorflow::ProfileOptions& opts)` — [`L78`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L78) — Creates a PluginTracer instance to collect TPU profile metrics.
- <a id="GetIntAttribute"></a>`GetIntAttribute(const xla::PjRtDevice* device, std::string_view key)` — [`L143`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L143)
- `GetIntVecAttribute(const xla::PjRtDevice* device, std::string_view key)` — [`L155`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L155)
- <a id="GetIntVecAttribute"></a>`GetIntVecAttribute(const xla::PjRtDevice* device, std::string_view key)` — [`L155`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L155)
- <a id="MaybeRegisterProfiler"></a>`MaybeRegisterProfiler(std::string_view plugin_name)` — [`L114`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L114) — Dynamically discovers the PJRT Profiler Extension within the given plugin
- <a id="MaybeSkipMegascaleForLaterClients"></a>`MaybeSkipMegascaleForLaterClients(const absl::flat_hash_map<std::string, xla::PjRtDeviceAttribute>& device_attributes)` — [`L173`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L173) — Sets SKIP_MEGASCALE_PJRT_CLIENT if the device belongs to a MegaScale client
- `MaybeSkipMegascaleForLaterClients(const absl::flat_hash_map<std::string, xla::PjRtDeviceAttribute>& device_attributes)` — [`L173`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L173) — Sets SKIP_MEGASCALE_PJRT_CLIENT if the device belongs to a MegaScale client
- <a id="TryExpandRankInEnvVar"></a>`TryExpandRankInEnvVar(std::string_view rank)` — [`L66`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L66)

## Other members
- <a id="PjrtBackend.ClearAllocatorStats"></a>`PjrtBackend.ClearAllocatorStats` — [`L411`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L411) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="PjrtBackend.EnsureInitialized"></a>`PjrtBackend.EnsureInitialized` — [`L202`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L202) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="PjrtBackend.GetAllocatorStats"></a>`PjrtBackend.GetAllocatorStats` — [`L406`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L406) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="PjrtBackend.GetClient"></a>`PjrtBackend.GetClient` — [`L337`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L337) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="PjrtBackend.GetDevice"></a>`PjrtBackend.GetDevice` — [`L354`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L354) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="PjrtBackend.GetDeviceAttributes"></a>`PjrtBackend.GetDeviceAttributes` — [`L387`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L387) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="PjrtBackend.GetDeviceType"></a>`PjrtBackend.GetDeviceType` — [`L382`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L382) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="PjrtBackend.GetGlobalDeviceCount"></a>`PjrtBackend.GetGlobalDeviceCount` — [`L364`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L364) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="PjrtBackend.GetGlobalDeviceId"></a>`PjrtBackend.GetGlobalDeviceId` — [`L373`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L373) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="PjrtBackend.GetHostAllocator"></a>`PjrtBackend.GetHostAllocator` — [`L416`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L416) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="PjrtBackend.GetInstance"></a>`PjrtBackend.GetInstance` — [`L188`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L188) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="PjrtBackend.GetSharedClient"></a>`PjrtBackend.GetSharedClient` — [`L348`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L348) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="PjrtBackend.InitializeInternal"></a>`PjrtBackend.InitializeInternal` — [`L235`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L235) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="PjrtBackend.IsInBadFork"></a>`PjrtBackend.IsInBadFork` — [`L332`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L332) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="PjrtBackend.IsInitialized"></a>`PjrtBackend.IsInitialized` — [`L324`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L324) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="PjrtBackend.SetPjRtInitializationOptions"></a>`PjrtBackend.SetPjRtInitializationOptions` — [`L193`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L193) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="PjrtBackend.Shutdown"></a>`PjrtBackend.Shutdown` — [`L426`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.cc#L426) — documented in [pjrt-client](../../../concepts/pjrt-client.md)

