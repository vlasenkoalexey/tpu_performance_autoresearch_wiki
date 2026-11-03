---
title: Env-var registry, validation and compile-cache-key participation
type: doc-concept
provenance: doc
source: docs/reference/env_vars.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Env-var registry, validation and compile-cache-key participation

## Definition
The env-var reference opens with the project's rule: every environment variable the
plugin reads is declared and validated in one module, `src/vllm_torchtpu/envs.py`,
and a CI hook (`tools/check_env_reads.py`) fails on new reads elsewhere. Booleans
accept `1/true/yes/on` and `0/false/no/off` case-insensitively and an invalid value
raises `ValueError` at startup instead of silently falling back. This page covers that
mechanism and one consequence the doc does not state: the registry is also the input
to the compile cache key.

## In vllm-torchtpu (grounded)
- **Registry.** [`environment_variables`](../catalog/src/vllm_torchtpu/envs.md#environment_variables.environment_variables)
  maps each name to a zero-arg getter. Module attribute access goes through
  [`__getattr__`](../catalog/src/vllm_torchtpu/envs.md#__getattr__), so `envs.X` re-reads
  `os.environ` on every access until
  [`enable_envs_cache`](../catalog/src/vllm_torchtpu/envs.md#enable_envs_cache) wraps it in
  `functools.cache` after service init (later `os.environ` edits are then invisible).
- **Typed parsers.** [`env_bool`](../catalog/src/vllm_torchtpu/envs.md#env_bool),
  [`env_int`](../catalog/src/vllm_torchtpu/envs.md#env_int),
  [`env_nonnegative_int`](../catalog/src/vllm_torchtpu/envs.md#env_nonnegative_int),
  [`env_nonnegative_float`](../catalog/src/vllm_torchtpu/envs.md#env_nonnegative_float),
  [`env_optional_bool`](../catalog/src/vllm_torchtpu/envs.md#env_optional_bool) (tri-state),
  [`env_optional_int`](../catalog/src/vllm_torchtpu/envs.md#env_optional_int) and
  [`env_with_choices`](../catalog/src/vllm_torchtpu/envs.md#env_with_choices) (enum, raises
  on an unknown value) implement the validation the doc describes; accepted spellings
  are [`_TRUE_STRINGS`](../catalog/src/vllm_torchtpu/envs.md#_TRUE_STRINGS) /
  [`_FALSE_STRINGS`](../catalog/src/vllm_torchtpu/envs.md#_FALSE_STRINGS).
- **Doc-vs-code: not every boolean uses `env_bool`.** At this commit several older
  entries are parsed with `bool(int(...))` and so accept only integers - `true` raises
  an int-parse error rather than the friendly message:
  [`VLLM_XLA_CHECK_RECOMPILATION`](../catalog/src/vllm_torchtpu/envs.md#VLLM_XLA_CHECK_RECOMPILATION),
  [`USE_MOE_SPARSE_CORE`](../catalog/src/vllm_torchtpu/envs.md#USE_MOE_SPARSE_CORE),
  [`DP_SCHED_ENABLED`](../catalog/src/vllm_torchtpu/envs.md#DP_SCHED_ENABLED),
  [`TPU_KERNEL_ITER_MODE`](../catalog/src/vllm_torchtpu/envs.md#TPU_KERNEL_ITER_MODE).
  [`TPU_PCP_TOPOLOGY_AWARE_MESH`](../catalog/src/vllm_torchtpu/envs.md#TPU_PCP_TOPOLOGY_AWARE_MESH)
  treats anything except `0/false/off/no` as true. Several string knobs read with plain
  `os.getenv` (e.g. `REQUANTIZE_WEIGHT_DTYPE`) are not validated at all.
- **Pre-libtpu overrides.** [`env_override`](../catalog/src/vllm_torchtpu/env_override.md)
  runs at package import, before `torch_tpu`/libtpu load: it turns on the Tier-2/Tier-3
  TorchTPU compile cache when `TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT` is set, defaults
  `VLLM_CACHE_ROOT`, defaults `VLLM_USE_MEGA_AOT_ARTIFACT` to `0`, sizes the premapped DMA buffer
  for Raiden, and appends libtpu flags via
  [`set_libtpu_flag_default`](../catalog/src/vllm_torchtpu/env_override.md#set_libtpu_flag_default)
  (a user-supplied flag in `LIBTPU_INIT_ARGS` always wins). The SparseCore collective
  offload threshold comes from
  [`_resolve_sc_offload_threshold_bytes`](../catalog/src/vllm_torchtpu/env_override.md#_resolve_sc_offload_threshold_bytes).
- **Propagation to workers.** Knobs that must reach Ray workers are listed in
  [`TpuPlatform.additional_env_vars`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform.additional_env_vars).
- **Compile cache key.** [`compute_tpu_compilation_hash`](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md#compute_tpu_compilation_hash)
  hashes, among other factors,
  [`_tpu_compile_env_factors`](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md#_tpu_compile_env_factors) -
  the value of **every** registry entry not named in
  [`_TPU_COMPILE_ENV_IGNORED`](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md#_TPU_COMPILE_ENV_IGNORED)
  (ports, Raiden identity, precompile scheduling, PP handoff, tracer level for Python,
  the Tier-3 cache root, `TPU_LIBRARY_PATH`) - plus the native variables in
  [`_NATIVE_TPU_COMPILE_ENV_VARS`](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md#_NATIVE_TPU_COMPILE_ENV_VARS)
  (`LIBTPU_INIT_ARGS`, `XLA_FLAGS`, ...), the libtpu fingerprint, and the source files
  under [`_RUNTIME_CACHE_KEY_PATHS`](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md#_RUNTIME_CACHE_KEY_PATHS)
  (kernels, layer core) so a kernel edit invalidates executables Dynamo cannot see into.

## Why it matters / when it applies
- One file is the complete knob inventory: for a perf sweep, `envs.py` comments are the
  ground truth for semantics and defaults (the doc lists ~70 of ~185 entries).
- Any new knob is in the compile key by default; an experiment that flips a kernel or
  layout env var will recompile, and two arms cannot share a warm cache. Conversely,
  orchestration-only knobs can be retuned without recompiling.
- Setting env vars after import has no effect on anything `env_override` already
  consumed (libtpu flags, cache roots), and after `enable_envs_cache` no effect at all.

## Connections
- Code concepts: [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md), [tpu-platform](../concepts/tpu-platform.md), [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md)
- Module catalogs: [envs](../catalog/src/vllm_torchtpu/envs.md), [env_override](../catalog/src/vllm_torchtpu/env_override.md), [tpu_compiler](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md), [tpu_platform](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md)
- Related doc-concepts: [env-var-reference-by-subsystem](env-var-reference-by-subsystem.md), [compilation-cache-and-warmup](compilation-cache-and-warmup.md), [tpu-patch-registry](tpu-patch-registry.md)

## Source
Extracted from `docs/reference/env_vars.md` (kept in place); mechanism verified in
`src/vllm_torchtpu/envs.py`, `src/vllm_torchtpu/env_override.py`,
`src/vllm_torchtpu/compilation/tpu_compiler.py` and `tools/check_env_reads.py`.
