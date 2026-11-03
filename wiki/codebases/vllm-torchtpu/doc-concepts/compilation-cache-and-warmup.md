---
title: Compilation cache tiers, warmup precompile and recompilation detection
type: doc-concept
provenance: doc
source: docs/user_guide/compilation_cache.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Compilation cache tiers, warmup precompile and recompilation detection

## Definition
vllm-torchtpu compiles every padded token shape ahead of serving (AOT warmup), so the
first start can take minutes. The compilation-cache guide splits persistence into two
independent layers: the **native TorchTPU PJRT executable cache** (`.bin` files) rooted
at `TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT`, and the **vLLM Python-level artifacts**
(Dynamo FX bytecode, guards, AOTAutograd entries under `torch_compile_cache/`, and the
`TpuCompilerAdaptor` per-compile-range metadata) under `VLLM_CACHE_ROOT`. A separate
runtime detector, `VLLM_XLA_CHECK_RECOMPILATION`, catches shapes or code paths that
warmup never compiled.

## In vllm-torchtpu (grounded)
- **Tier-3 executable cache.** [`TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT`](../catalog/src/vllm_torchtpu/envs.md#TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT)
  is consumed at import by [`env_override`](../catalog/src/vllm_torchtpu/env_override.md),
  which also defaults the required Tier-2 in-memory cache and the
  `TORCH_TPU_INTERNAL_*` names torch_tpu actually reads; an explicitly set internal
  variable is never clobbered.
- **Python-level artifacts.** [`TpuCompilerAdaptor`](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md#TpuCompilerAdaptor)
  (`compile` / `load`) saves and replays one entry per (compile range, subgraph) under
  `VLLM_CACHE_ROOT` (defaulted to `~/.cache/vllm` by `env_override`). Its directory is
  keyed by [`compute_tpu_compilation_hash`](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md#compute_tpu_compilation_hash):
  torch / torch_tpu / jax / libtpu versions, the compile-relevant env vars, the resolved
  KV block count, `max_model_len`, `max_num_batched_tokens`, `max_num_seqs`, the
  speculative config, and the kernel source files.
- **vLLM mega AOT artifact disabled.** `env_override` defaults
  `VLLM_USE_MEGA_AOT_ARTIFACT=0`: upstream's mega artifact is inductor-only, never
  reloads on TPU, and breaks the next warm start; the per-range cache already stores the
  same bytes.
- **Warmup precompile.** [`TPUModelRunner.capture_model`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner.capture_model)
  and [`TPUModelRunner._precompile_backbone`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner._precompile_backbone)
  walk the token buckets (see [token-padding-buckets](token-padding-buckets.md)).
  Speed-ups from the env-var reference:
  [`TPU_PARALLEL_PRECOMPILE`](../catalog/src/vllm_torchtpu/envs.md#TPU_PARALLEL_PRECOMPILE)
  (ranks of a host start at different shapes, [`_rotate_precompile_sweep`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#_rotate_precompile_sweep),
  and later shapes become cache loads),
  [`TPU_PRECOMPILE_PEER_REPLAY`](../catalog/src/vllm_torchtpu/envs.md#TPU_PRECOMPILE_PEER_REPLAY)
  (one owner rank compiles each range, the others wait up to
  [`TPU_PRECOMPILE_PEER_WAIT_S`](../catalog/src/vllm_torchtpu/envs.md#TPU_PRECOMPILE_PEER_WAIT_S)
  and replay it; [`_validate_peer_replay_config`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#_validate_peer_replay_config)
  refuses `VLLM_DISABLE_COMPILE_CACHE=1`), and
  [`TPU_PRECOMPILE_TRACE_FIRST`](../catalog/src/vllm_torchtpu/envs.md#TPU_PRECOMPILE_TRACE_FIRST)
  (trace all bucket groups, then compile in one pass). The range loop itself is patched
  by [`_patch_vllm_compile_all_ranges`](../catalog/src/vllm_torchtpu/__init__.md#_patch_vllm_compile_all_ranges).
- **Recompilation detector.** With
  [`VLLM_XLA_CHECK_RECOMPILATION`](../catalog/src/vllm_torchtpu/envs.md#VLLM_XLA_CHECK_RECOMPILATION)=1,
  [`TPUModelRunner._update_num_xla_graphs`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner._update_num_xla_graphs)
  calls `torch.tpu._get_cache_stats()` at each checkpoint (every precompile bucket and
  runtime step), advances a graph-count watermark, and logs newly compiled graphs
  (sorted by compile time). It is skipped under `enforce_eager`. Note the runner reads
  the upstream `vllm.envs` copy of the variable.
- **Kernel iteration.** [`TPU_KERNEL_ITER_MODE`](../catalog/src/vllm_torchtpu/envs.md#TPU_KERNEL_ITER_MODE)
  scopes the cache key so a Pallas kernel edit reuses cached backbone executables
  ([`_iter_runtime_cache_key_files`](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md#_iter_runtime_cache_key_files)).

## Doc-vs-code disagreements
- The README tip and the env-var reference say `VLLM_XLA_CACHE_PATH` persists compiled
  artifacts (default `~/.cache/vllm/xla_cache`, `gs://` allowed). At this commit no code
  under `src/` reads that variable; the compilation-cache guide's
  `TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT` + `VLLM_CACHE_ROOT` are the knobs that work.
- The supported-models feature table also lists `VLLM_XLA_CACHE_PATH` for the
  compilation cache feature; same caveat.

## Why it matters / when it applies
- Cold starts of large MoE models are dominated by compile (the env reference quotes
  ~165 s for the biggest Qwen3.5-397B range at DP8); persist both roots across restarts
  and use parallel precompile + peer replay on multi-rank hosts.
- Any change to a hashed factor (a kernel env var, `max_num_batched_tokens`,
  `gpu_memory_utilization`, a kernel source edit) moves the cache directory: expect a
  cold compile.
- Keep the recompilation detector on in CI, off in benchmarks (it queries cache stats
  every step); a runtime recompile is a stall on the engine loop.

## Connections
- Code concepts: [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md), [tpu-model-runner](../concepts/tpu-model-runner.md), [tpu-platform](../concepts/tpu-platform.md)
- Module catalogs: [tpu_compiler](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md), [env_override](../catalog/src/vllm_torchtpu/env_override.md), [tpu_runner](../catalog/src/vllm_torchtpu/runner/tpu_runner.md), [kernel_reload](../catalog/src/vllm_torchtpu/compilation/kernel_reload.md)
- Related doc-concepts: [token-padding-buckets](token-padding-buckets.md), [env-var-registry-and-compile-key](env-var-registry-and-compile-key.md), [env-var-reference-by-subsystem](env-var-reference-by-subsystem.md), [plugin-architecture-and-kernel-bridge](plugin-architecture-and-kernel-bridge.md)

## Source
Extracted from `docs/user_guide/compilation_cache.md` (kept in place), plus section 1
of `docs/reference/env_vars.md` and the README startup tip.
