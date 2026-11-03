---
title: Server-side profiling - configured vs armed, dynamic tracer options
type: doc-concept
provenance: doc
source: docs/developers_guide/profiling/server.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Server-side profiling - configured vs armed, dynamic tracer options

## Definition
End-to-end profiling of a real serving window: start `vllm serve` with a profiler kind
and trace directory (**configured**), then bracket the traffic with
`POST /start_profile` (**armed**) and `POST /stop_profile`. Per-session tracer options
(host/device/python tracer levels, TPU trace mode, SparseCore tracing, firmware event
flags) can be passed at `/start_profile` time without restarting the server.

## In vllm-torchtpu (grounded)
- [`TPUWorker.profile`](../catalog/src/vllm_torchtpu/worker/tpu_worker.md#TPUWorker.profile)
  handles both start and stop on every worker: it resolves options, opens a
  `torch.profiler.profile` session (CPU + PrivateUse1 activities, TorchTPU
  `TpuProfilerConfig`), and on stop merges ranks via the
  [multi-rank capture protocol](multi-rank-trace-capture.md). With
  `USE_PHASED_PROFILER` set it delegates to the [phased profiler](phased-profiler.md).
- Option resolution lives in `src/vllm_torchtpu/tracing/options.py`:
  [`resolve_profile_dir_and_opts`](../catalog/src/vllm_torchtpu/tracing/options.md#resolve_profile_dir_and_opts)
  starts from [`get_default_standard_opts`](../catalog/src/vllm_torchtpu/tracing/options.md#get_default_standard_opts)
  and [`get_default_advanced_opts`](../catalog/src/vllm_torchtpu/tracing/options.md#get_default_advanced_opts),
  merges the legacy `key:value;...` string parsed by
  [`parse_profile_options`](../catalog/src/vllm_torchtpu/tracing/options.md#parse_profile_options),
  then `profiler_kwargs` (which win on collisions). Keys in
  [`_STANDARD_KEYS`](../catalog/src/vllm_torchtpu/tracing/options.md#_STANDARD_KEYS)
  become tracer levels; everything else is forwarded as TPU `experimental_options`.
  A plain `profile_prefix` (no `:` or `;`) just names a subdirectory.
- Env-var defaults:
  [`HOST_TRACER_LEVEL`](../catalog/src/vllm_torchtpu/envs.md#HOST_TRACER_LEVEL) (2),
  [`DEVICE_TRACER_LEVEL`](../catalog/src/vllm_torchtpu/envs.md#DEVICE_TRACER_LEVEL) (1),
  [`PYTHON_TRACER_LEVEL`](../catalog/src/vllm_torchtpu/envs.md#PYTHON_TRACER_LEVEL) (1),
  [`TPU_TRACE_MODE`](../catalog/src/vllm_torchtpu/envs.md#TPU_TRACE_MODE) (`TRACE_COMPUTE`),
  [`TPU_NUM_SPARSE_CORES_TO_TRACE`](../catalog/src/vllm_torchtpu/envs.md#TPU_NUM_SPARSE_CORES_TO_TRACE) and
  [`TPU_NUM_SPARSE_CORE_TILES_TO_TRACE`](../catalog/src/vllm_torchtpu/envs.md#TPU_NUM_SPARSE_CORE_TILES_TO_TRACE) (1 each).

## Usage, from the doc
```bash
vllm serve <model> --tensor-parallel-size 4 --enable-expert-parallel \
  --profiler-config.profiler torch \
  --profiler-config.torch_profiler_dir /tmp/vllm_profile \
  --profiler-config.ignore_frontend true
curl -X POST http://localhost:8000/start_profile \
  -H "Content-Type: application/json" \
  -d '{"profile_prefix": "fw_events_run", "host_tracer_level": 3,
       "tpu_trace_mode": "TRACE_COMPUTE_AND_SYNC",
       "e2e_enable_fw_throttle_event": true}'
curl -X POST http://localhost:8000/stop_profile
```
Offline equivalent: `llm.start_profile(profile_prefix=..., profiler_kwargs={...})`.
`vllm bench serve --profile` fires the two endpoints around its main run.

## Why it matters / when it applies
- **Profiling is not free**: in benchmark runs `--profile` costs roughly +11% TTFT and
  -4% throughput, so never compare profile-on numbers with a non-profile baseline.
- The standard capture spans the whole start->stop window; `delay_iterations` and
  `max_iterations` are honored **only** by the phased profiler.
- `--profiler-config.ignore_frontend true` skips the AsyncLLM CPU profiler (pure
  overhead for TPU work; it also ignores iteration limits).
- `--profiler-config.profiler torch` is mandatory - vLLM's `ProfilerConfig` rejects a
  trace directory without it.
- Most common empty-run cause: configured but never armed. Through the benchmark
  harness, `CAPTURE_PROFILE=1` adds the profiler flags and runs each cell **once more**
  with `--profile` after the measured run (sized by `PROFILE_NUM_PROMPTS`, default one
  concurrency wave), so reported numbers stay comparable to a baseline. It is inferred
  whenever `EXTRA_SERVE_ARGS` contains `--profiler-config.torch_profiler_dir`;
  `CAPTURE_PROFILE=0` opts out. Prefer one ISL/OSL cell so the trace maps to one shape.
- `TPU_TRACE_MODE=TRACE_COMPUTE_AND_SYNC` and the SparseCore tracing counts are the
  knobs to reach for when investigating collective/sync waits or SparseCore offloaded
  work (for example the SparseCore gather/scatter kernels).

## Connections
- Code concepts: [tracing-annotations](../concepts/tracing-annotations.md),
  [sparsecore-ragged-gather-scatter](../concepts/sparsecore-ragged-gather-scatter.md),
  [tpu-model-runner](../concepts/tpu-model-runner.md)
- Module catalogs: [tracing/options](../catalog/src/vllm_torchtpu/tracing/options.md),
  [tpu_worker](../catalog/src/vllm_torchtpu/worker/tpu_worker.md),
  [envs](../catalog/src/vllm_torchtpu/envs.md)
- Related doc-concepts: [phased-profiler](phased-profiler.md),
  [multi-rank-trace-capture](multi-rank-trace-capture.md),
  [offline-shape-profiling](offline-shape-profiling.md),
  [benchmark-harness-and-regression-gates](benchmark-harness-and-regression-gates.md)

## Source
Extracted from `docs/developers_guide/profiling/server.md` and
`docs/developers_guide/profiling/troubleshooting.md` (kept in place).
