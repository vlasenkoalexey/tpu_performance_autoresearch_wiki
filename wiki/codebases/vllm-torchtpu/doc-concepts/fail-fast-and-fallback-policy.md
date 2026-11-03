---
title: Fail fast - fallback policy, asserts and recompilation guards
type: doc-concept
provenance: doc
source: docs/developers_guide/coding_guidance.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Fail fast - fallback policy, asserts and recompilation guards

## Definition
Section 5 of the coding guidance: no silent failure. No defensive `try/except`, assert
untested assumptions (especially in quantization and kernels, where the failure mode is
wrong numbers rather than a crash), raise `NotImplementedError` for unsupported options,
and write error messages that state the fix. Its perf-relevant core is the **fallback
discriminator** (R-5.3) and the **recompilation rule** (R-5.6).

## The rules that touch performance
- **R-5.3 fallback discriminator.** When widening a default (e.g. enabling a kernel for
  more models), an automatic fallback is acceptable only if it preserves correctness at
  a *known* perf cost **and** logs `warning_once`. If the result would be wrong or the
  config is unsupported, raise an actionable error - never fall back.
- **R-5.6 recompilation.** Guard recompilation with official APIs, wrapped so the error
  is actionable; never override private JAX internals. A kernel-backend switch must not
  change a compiled function's traced signature - it must error instead.
- **R-5.5.** Do not hide a dtype mismatch with a cast (`v.astype(k.dtype)`); find the
  source. Silent casts are also silent extra HBM traffic and MXU dtype changes.
- **R-1.7 logging.** Log lines are self-contained: subsystem tag, shapes/values, failure
  mode; `warning_once` / `info_once` for unexpected fallback paths and tuned-table misses
  ([tuned-block-size-tables](tuned-block-size-tables.md)).

## In vllm-torchtpu (grounded)
- Logging goes through [`init_logger`](../catalog/src/vllm_torchtpu/logger.md#init_logger)
  (no `print` in library code); kernels' tuned-table lookups use `warning_once` on a
  miss.
- Envelope gating instead of silent fallback: kernel eligibility predicates such as
  [`adaptive_fused_moe_supported`](../catalog/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.md#adaptive_fused_moe_supported)
  decide up front whether a fast path applies.
- Startup validation refuses to run in configurations that would silently do nothing,
  e.g. [`_validate_phased_profiling_config`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#_validate_phased_profiling_config)
  rejects `USE_PHASED_PROFILER` without a trace directory (see
  [phased-profiler](phased-profiler.md)), and the MoE routing-simulation module raises on
  an unknown `VLLM_MOE_ROUTING_SIMULATION_STRATEGY`.
- Recompilation detection at runtime is upstream vLLM's `VLLM_XLA_CHECK_RECOMPILATION`,
  read by the runner (see [compilation-cache-and-warmup](compilation-cache-and-warmup.md)).

## Why it matters / when it applies
For an optimizer, the discriminator draws a hard line: a change that silently routes some
shapes to a slow path is acceptable only with a logged warning and preserved
correctness, and a speedup that depends on a path producing different numbers is not a
speedup. A traced-signature change on a backend switch means a recompile (minutes on
large models), which is why it must error rather than happen implicitly. `gc.collect()`
and `atexit` workarounds are treated as symptoms of a real bug elsewhere (R-5.1).

## Connections
- Code concepts: [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md),
  [tpu-model-runner](../concepts/tpu-model-runner.md),
  [adaptive-fused-moe-kernel](../concepts/adaptive-fused-moe-kernel.md),
  [quantization-methods](../concepts/quantization-methods.md)
- Module catalogs: [logger](../catalog/src/vllm_torchtpu/logger.md),
  [tpu_platform](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md)
- Related doc-concepts: [derive-dont-declare](derive-dont-declare.md),
  [plugin-architecture-and-kernel-bridge](plugin-architecture-and-kernel-bridge.md),
  [compilation-cache-and-warmup](compilation-cache-and-warmup.md),
  [tuned-block-size-tables](tuned-block-size-tables.md)

## Source
Extracted from `docs/developers_guide/coding_guidance.md` sections 1 and 5
(kept in place).
