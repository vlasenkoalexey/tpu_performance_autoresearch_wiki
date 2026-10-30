---
title: xprof profiling workflow (torch.profiler + TpuProfilerConfig)
type: doc-concept
provenance: doc
source: docs/markdown/performance_profiling.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# xprof profiling workflow (torch.profiler + TpuProfilerConfig)

## Definition
TorchTPU plugs the TPU into the standard `torch.profiler.profile()` context manager:
`ProfilerActivity.CPU` traces host-side dispatch and data loading, `ProfilerActivity.TPU` traces
device execution (compute, memory, interconnect), and the result is an XPlane (`.xplane.pb`) trace
viewed in TensorBoard's Profile tab or a standalone `xprof --logdir=...` server.
`torch.tpu.profiler.TpuProfilerConfig`, passed as `experimental_config=`, tunes tracer levels, the
output directory and raw libtpu profiler options such as hardware performance-counter sampling.

## In torch_tpu (grounded)
- **Config object.** [`TpuProfilerConfig`](../catalog/src/torch_tpu/_internal/profiler/profiler_config.md#TpuProfilerConfig)
  (owning module `src/torch_tpu/_internal/profiler/profiler_config.py`, experimental) subclasses
  `torch.profiler._ExperimentalConfig` and serializes its arguments into one
  `custom_profiler_config` string `key:value,key:value,...`. Stable keys: `host_tracer_level`
  (default 2), `device_tracer_level` (1), `python_tracer_level` (0), `run_dir`, `worker_rank`
  (suffixes the XPlane file name with the rank). Anything in `experimental_options` is appended
  verbatim (strings quoted/escaped, bools as `true`/`false`), followed by
  `check_experimental_options`.
- **Kineto plugin (C++).** [`TpuKinetoProfilerSession`](../catalog/csrc/internal/profiler/tpu_profiler_plugin.h.md#TpuKinetoProfilerSession "csrc/internal/profiler/tpu_profiler_plugin.h:L42")
  wraps a TSL `ProfilerSession` behind Kineto's `IActivityProfilerSession`
  ([`start`](../catalog/csrc/internal/profiler/tpu_profiler_plugin.cc.md#TpuKinetoProfilerSession.start "csrc/internal/profiler/tpu_profiler_plugin.cc:L409"),
  [`stop`](../catalog/csrc/internal/profiler/tpu_profiler_plugin.cc.md#TpuKinetoProfilerSession.stop "csrc/internal/profiler/tpu_profiler_plugin.cc:L485")).
  The config string is parsed by
  [`UpdateProfileOptions`](../catalog/csrc/internal/profiler/tpu_profiler_plugin.cc.md#UpdateProfileOptions "csrc/internal/profiler/tpu_profiler_plugin.cc:L323")
  -> [`UpdateProfileOption`](../catalog/csrc/internal/profiler/tpu_profiler_plugin.cc.md#UpdateProfileOption "csrc/internal/profiler/tpu_profiler_plugin.cc:L202"):
  the three tracer levels map to `ProfileOptions` fields, every other key goes through
  [`SetAdvancedConfigValue`](../catalog/csrc/internal/profiler/tpu_profiler_plugin.cc.md#SetAdvancedConfigValue "csrc/internal/profiler/tpu_profiler_plugin.cc:L168")
  into `advanced_configuration` (quoted -> string, `true`/`false` -> bool, else int64).
- **Output location.** [`GetProfilerBaseOutputDir`](../catalog/csrc/internal/profiler/tpu_profiler_plugin.cc.md#GetProfilerBaseOutputDir "csrc/internal/profiler/tpu_profiler_plugin.cc:L332")
  picks `TORCH_TPU_PROFILER_OUTPUT_DIR` if set, else `run_dir`, else `TMPDIR`, else `/tmp`; files
  follow the TensorBoard convention `<base>/plugins/profile/<YYYY_MM_DD_HH_MM_SS>/<host>[_<rank>].xplane.pb`.
- **Legacy entry point.** The older `torch_tpu._internal.profiler.profile()` /
  [`xprof_trace_handler`](../catalog/src/torch_tpu/_internal/profiler/_api.md#xprof_trace_handler)
  path drives the same backend through
  [`PyStartTrace`](../catalog/csrc/internal/profiler/profiler_api.cc.md#PyStartTrace "csrc/internal/profiler/profiler_api.cc:L224")
  / [`PyStopTrace`](../catalog/csrc/internal/profiler/profiler_api.cc.md#PyStopTrace "csrc/internal/profiler/profiler_api.cc:L229");
  it is forbidden inside `torch.compile` regions.

## Why it matters / when it applies
- **Capture recipe.** Wrap a representative window of the training loop (doc: 100-1000 steps; the
  profiler adds ~5-10% per-step overhead), call `torch.accelerator.synchronize()` and `prof.step()`
  each step, save with `torch.profiler.tensorboard_trace_handler(log_dir)`. TensorBoard needs
  `tensorboard-plugin-profile` and `setuptools<81` (newer setuptools drops `pkg_resources`).
- **Views.** Overview (step time, utilization, top ops), Trace Viewer (gaps = idle TPU), Op Profile
  (per-op time), Memory Profile (HBM over time). What to look for is in
  [trace-red-flags](trace-red-flags.md).
- **Hardware counters (Ironwood / TPU7x and later).** Pass
  `experimental_options={"tpu_enable_periodic_counter_sampling": True,
  "tpu_tc_perf_counter_sampling_options": "interval_us:1 scaling:0 counter_size_bits:1 indices:..."}`
  to sample TensorCore performance counters - the way to see bottlenecks inside Pallas kernels
  that event traces cannot show. Counter indices and options are documented in the OpenXLA
  kernel-profiling guide. `check_experimental_options=True` makes unknown keys fail rather than be
  ignored.
- Multi-worker jobs: launchers set `TORCH_TPU_XPROF_SESSION_ID` so all workers share one session
  (see [environment-variables](environment-variables.md)).

## Connections
- Code concepts: [profiler](../concepts/profiler.md),
  [pallas-custom-kernels](../concepts/pallas-custom-kernels.md),
  [distributed-launchers-and-spmd](../concepts/distributed-launchers-and-spmd.md)
- Module catalogs: [src/torch_tpu/_internal/profiler/profiler_config](../catalog/src/torch_tpu/_internal/profiler/profiler_config.md),
  [csrc/internal/profiler/tpu_profiler_plugin.cc](../catalog/csrc/internal/profiler/tpu_profiler_plugin.cc.md),
  [csrc/internal/profiler/tpu_profiler_plugin.h](../catalog/csrc/internal/profiler/tpu_profiler_plugin.h.md),
  [csrc/internal/profiler/profiler_api.cc](../catalog/csrc/internal/profiler/profiler_api.cc.md)
- Related doc-concepts: [pallas-register-level-fusion](pallas-register-level-fusion.md), [trace-red-flags](trace-red-flags.md),
  [hlo-and-llo-compilation-dumps](hlo-and-llo-compilation-dumps.md), [environment-variables](environment-variables.md)

## Source
Extracted from `docs/markdown/performance_profiling.md` and its byte-identical duplicate
`docs/markdown/4_debugging_and_performance_analysis_2_xprof_for_torchtpu.md` (both kept in place).
