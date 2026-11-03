---
title: Phased profiler (one bounded trace per inference phase)
type: doc-concept
provenance: doc
source: docs/developers_guide/profiling/phased.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Phased profiler (one bounded trace per inference phase)

## Definition
A serving benchmark interleaves prefill and decode, so a continuous trace blends both
regimes. The phased profiler classifies every engine step by its batch composition
(`prefill_tokens / total_scheduled_tokens`) and opens a **separate, bounded capture the
first time each phase appears** in a profiling session, for `max_iterations` steps.
It is selected by the env var `USE_PHASED_PROFILER=true` and armed by the same
`/start_profile` / `/stop_profile` trigger as the standard profiler.

## In vllm-torchtpu (grounded)
- Switch: [`USE_PHASED_PROFILER`](../catalog/src/vllm_torchtpu/envs.md#USE_PHASED_PROFILER)
  (read by the TPU workers, so it must be in the **server's** environment).
- Trigger: [`TPUWorker.profile`](../catalog/src/vllm_torchtpu/worker/tpu_worker.md#TPUWorker.profile)
  routes to [`TPUModelRunner.start_phased_profiling`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner.start_phased_profiling)
  / [`stop_phased_profiling`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner.stop_phased_profiling)
  when the env var is set; [`_init_phased_profiling`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner._init_phased_profiling)
  takes the trace dir from `profiler_config.torch_profiler_dir`.
- Engine: [`PhaseBasedProfiler`](../catalog/src/vllm_torchtpu/runner/utils.md#PhaseBasedProfiler)
  (`step`, `finish`) in `runner/utils.py`, fed per step from `execute_model` with stats
  from [`get_batch_composition_stats`](../catalog/src/vllm_torchtpu/runner/utils.md#get_batch_composition_stats)
  and classified by
  [`determine_phase_from_batch_composition_stats`](../catalog/src/vllm_torchtpu/runner/utils.md#determine_phase_from_batch_composition_stats)
  into [`InferencePhase`](../catalog/src/vllm_torchtpu/runner/utils.md#InferencePhase).
- Startup validation: [`_validate_phased_profiling_config`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#_validate_phased_profiling_config)
  rejects the legacy `additional_config['phased_profiling_dir']` and refuses to start
  when `USE_PHASED_PROFILER` is set without a `torch_profiler_dir`.
- Each phase capture uses `torch.profiler.profile` with CPU + PrivateUse1 (TPU)
  activities and TorchTPU's `TpuProfilerConfig`, then goes through the shared
  rank-merge protocol ([multi-rank-trace-capture](multi-rank-trace-capture.md)).

## Phase classification

| Phase | prefill ratio | Meaning |
|---|---|---|
| `prefill_only` | `1.0` | Pure prompt ingestion |
| `prefill_heavy` | `>= 0.9` | Mostly prefill, a few decodes riding along |
| `balanced` | `0.4` - `0.6` | Chunked prefill and decode mixed evenly |
| `decode_heavy` | `<= 0.2` | Steady-state decode with a little chunked prefill |
| `decode_only` | `0.0` | Pure generation |
| `ambiguous` | `(0.2, 0.4)` and `(0.6, 0.9)` | Never captured (transitional) |

Token accounting: a request with zero computed tokens is prefill; an ongoing request
scheduled for more than one token is chunked prefill; one token is decode; and
**speculative-decode draft tokens count as decode**, not chunked prefill.

## Configuration

| Setting | Effect |
|---|---|
| `USE_PHASED_PROFILER=true` | Only on/off switch |
| `--profiler-config.profiler torch` | Required; `ProfilerConfig` rejects a trace dir without it |
| `--profiler-config.torch_profiler_dir <dir>` | Root; per-phase subdirectories beneath it |
| `--profiler-config.max_iterations N` | Steps per phase; upstream's `0` ("no limit") falls back to `PHASED_PROFILER_NUM_STEPS_TO_PROFILE_FOR` = 15 |
| `--profiler-config.delay_iterations N` | Skip N `decode_heavy` steps before capturing that phase (only affects `decode_heavy`) |
| `--additional-config` `phased_profiler_decode_only_kv_len_threshold` / `..._prefill_only_kv_len_threshold` | Skip `decode_only` / `prefill_only` steps until the batch's minimum KV length reaches the threshold (default `-1`, off) |

The two KV-length thresholds are listed in
[`HASH_IGNORED_ADDITIONAL_CONFIG_KEYS`](../catalog/src/vllm_torchtpu/runner/utils.md#HASH_IGNORED_ADDITIONAL_CONFIG_KEYS),
which [`_patch_vllm_config_hash_ignore_diagnostics`](../catalog/src/vllm_torchtpu/__init__.md#_patch_vllm_config_hash_ignore_diagnostics)
keeps out of the TPU compile cache key - setting them does not force a recompile.

## Why it matters / when it applies
- Gives one clean trace per regime (prefill vs decode vs mixed) from a single realistic
  benchmark run - the right unit for attributing step time to attention, MoE, sampling
  or collectives per mode, which is how this repo's perf PRs are expected to report
  (per-mode speedups; see [perf-evidence-standard](perf-evidence-standard.md)).
- The KV-length thresholds make the decode trace reflect steady-state context lengths
  (and the prefill trace a mid-sequence chunk), which matters for attention kernels
  whose cost scales with KV length.
- Phases appear only if the traffic produces them: one request at a time gives
  `prefill_only` + `decode_only` only; mixed phases need concurrency. A heavily
  overlapped run may never schedule a pure-prefill or pure-decode batch. Check the
  per-step `batch_composition_stats_*.json` files to see what the scheduler produced.
- Each phase is captured once per session; a new `/start_profile` session (for
  example the next benchmark cell with `--profile`) re-arms every phase.
- Always pass `--attention-backend CUSTOM` (batched RPA) when profiling, otherwise vLLM
  falls back to `FLASH_ATTN` with `block_size=16` and you profile a backend you do not
  serve with. Clear the trace directory between runs - phases accumulate.

## Doc vs code at this commit
- The doc and the module docstrings call the capture the "PyTorch/XLA profiler"; the
  code actually drives `torch.profiler` with TorchTPU's `TpuProfilerConfig`
  (`torch_tpu._internal.profiler`), i.e. the TorchTPU profiler, not PyTorch/XLA.
- A batch-size-1 run can capture `decode_only`: `step` guards on
  `total_num_scheduled_tokens > 0` (a code comment records that an earlier `> 1`
  guard made decode-only uncapturable).

## Connections
- Code concepts: [tracing-annotations](../concepts/tracing-annotations.md),
  [tpu-model-runner](../concepts/tpu-model-runner.md),
  [speculative-decoding](../concepts/speculative-decoding.md),
  [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md)
- Module catalogs: [runner/utils](../catalog/src/vllm_torchtpu/runner/utils.md),
  [tpu_runner](../catalog/src/vllm_torchtpu/runner/tpu_runner.md),
  [tpu_worker](../catalog/src/vllm_torchtpu/worker/tpu_worker.md),
  [envs](../catalog/src/vllm_torchtpu/envs.md)
- Related doc-concepts: [multi-rank-trace-capture](multi-rank-trace-capture.md),
  [server-side-profiling-and-trace-options](server-side-profiling-and-trace-options.md),
  [disaggregated-pd-trace-correlation](disaggregated-pd-trace-correlation.md),
  [benchmark-harness-and-regression-gates](benchmark-harness-and-regression-gates.md)

## Source
Extracted from `docs/developers_guide/profiling/phased.md`, with the missing-phase and
startup-assertion items from `docs/developers_guide/profiling/troubleshooting.md`
(kept in place).
