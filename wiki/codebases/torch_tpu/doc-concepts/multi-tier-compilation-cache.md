---
title: Multi-tier compilation cache (cold starts vs warm hits)
type: doc-concept
provenance: doc
source: docs/markdown/compilation_cache.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Multi-tier compilation cache (cold starts vs warm hits)

## Definition
The first time a given sequence of ops runs, TorchTPU must compile it to TPU machine code - a **cold start** that can take seconds to minutes for a large model. The executable is then stored in the **compilation cache**, and later runs of the same graph are **warm hits** that start executing immediately (`record graph -> fingerprint -> HIT -> execute`). The intro doc describes three tiers:

| Tier | Scope | Doc's description |
|---|---|---|
| 1 | process | in-memory cache, always on |
| 2 | host | host-local shared memory, reused across the processes of a multi-device job |
| 3 | fleet | persistent remote cache (e.g. Cloud Storage), reused across hosts and job restarts |

## In torch_tpu (grounded)
- Tier 1 is the [`CompilationCache`](../catalog/csrc/common/compilation_cache.h.md#CompilationCache) object. [`CompilationCache.GetOrCompile`](../catalog/csrc/common/compilation_cache.cc.md#CompilationCache.GetOrCompile) / [`CompilationCache.GetOrCompileImpl`](../catalog/csrc/common/compilation_cache.cc.md#CompilationCache.GetOrCompileImpl) look the key up in memory and, on a miss, [`CompilationCache.EnqueueCompilation`](../catalog/csrc/common/compilation_cache.cc.md#CompilationCache.EnqueueCompilation) schedules the lower tiers; the result lands via [`CompilationCache.SetExecutable`](../catalog/csrc/common/compilation_cache.cc.md#CompilationCache.SetExecutable). Tiers are enumerated by [`CacheTier`](../catalog/csrc/common/compilation_cache_utils.h.md#CacheTier).
- Tier 2 ([`CompilationCache.GetFromTier2OrCompile`](../catalog/csrc/common/compilation_cache.cc.md#CompilationCache.GetFromTier2OrCompile), [`GetFromTier2Cache`](../catalog/csrc/common/tier2_compilation_cache.cc.md#GetFromTier2Cache)) is a file per key under [`kTier2CacheRootDir`](../catalog/csrc/common/tier2_compilation_cache.cc.md#kTier2CacheRootDir) = `/dev/shm/torch_tpu_cache/<name>/<binary-fingerprint>/`, memory-mapped on read ([`MappedCacheEntry`](../catalog/csrc/common/tier2_compilation_cache.cc.md#MappedCacheEntry)). On a miss the process takes a per-key file lock ([`Tier2CacheEntryLock`](../catalog/csrc/common/tier2_compilation_cache.h.md#Tier2CacheEntryLock)), re-checks, and only then compiles - so the N processes on a host compile each graph **once**, not N times.
- Tier-2 enablement ([`GetTier2CacheName`](../catalog/csrc/common/tier2_compilation_cache.cc.md#GetTier2CacheName), [`UsesTier2CompilationCache`](../catalog/csrc/common/tier2_compilation_cache.cc.md#UsesTier2CompilationCache)) is driven by [`kTorchTpuTier2CompilationCacheEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuTier2CompilationCacheEnvVar) (`TORCH_TPU_TIER2_COMPILATION_CACHE`): a name enables it, `"disabled"` turns it off, and when unset it is **on iff world size > 1** (or tier 3 is configured).
- Tier 3 ([`CompilationCache.GetFromTier3OrCompile`](../catalog/csrc/common/compilation_cache.cc.md#CompilationCache.GetFromTier3OrCompile), [`GetFromTier3Cache`](../catalog/csrc/common/tier3_compilation_cache.cc.md#GetFromTier3Cache)) is enabled by setting [`kTorchTpuTier3CompilationCacheRootEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuTier3CompilationCacheRootEnvVar) (`TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT`, read by [`GetTier3CacheRootDir`](../catalog/csrc/common/compilation_cache_utils.cc.md#GetTier3CacheRootDir)); [`UsesTier3CompilationCache`](../catalog/csrc/common/tier3_compilation_cache.cc.md#UsesTier3CompilationCache) requires tier 2 as well, and tier 3 is consulted inside the tier-2 lock. By default a local "backup" compilation races the remote read and whichever finishes first unblocks execution ([`UsesLocalBackupTaskForTier3Read`](../catalog/csrc/common/tier3_compilation_cache.cc.md#UsesLocalBackupTaskForTier3Read), toggled by [`kTorchTpuInternalTier3CompilationCacheLocalBackupTaskEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuInternalTier3CompilationCacheLocalBackupTaskEnvVar)).
- The tier-2/3 directory is keyed by [`GetTorchTpuBinaryFingerprint`](../catalog/csrc/common/compilation_cache_utils.cc.md#GetTorchTpuBinaryFingerprint) = a hand-bumped TorchTPU binary-format version + the PjRt/libtpu version string, so upgrading libtpu (or a torch_tpu release that bumps the version) invalidates persisted executables.
- `torch.compile` adds a PyTorch-level layer on top: [`TpuBackend`](../catalog/src/torch_tpu/_internal/compile/_backend.md#TpuBackend) defaults `enable_serialization=True` so AOTAutogradCache can save/load compiled artifacts (static-shape graphs only).
- What the key contains is the subject of [graph-fingerprint-and-recompilation.md](graph-fingerprint-and-recompilation.md).

## Why it matters / when it applies
- Steady-state step time assumes every graph is a warm hit; any step that misses pays a full XLA compile on the critical path. Exclude the first 2-3 iterations from timing (the doc's warmup rule).
- Multi-chip jobs on one host: tier 2 removes duplicated compile work across ranks automatically. Single-process runs get no tier-2 benefit unless the env var names a cache.
- Restarted / preempted / multi-host jobs: only tier 3 avoids recompiling from scratch; set the root to shared storage.
- `/dev/shm` consumption grows with the number of distinct graphs; shape churn therefore costs host RAM as well as compile time.

## Connections
- Code concepts: [compilation-cache](../concepts/compilation-cache.md), [compilation-cache-key](../concepts/compilation-cache-key.md), [compilation-pipeline](../concepts/compilation-pipeline.md), [torch-compile-backend](../concepts/torch-compile-backend.md), [pjrt-client](../concepts/pjrt-client.md)
- Module catalogs: [csrc/common/compilation_cache.h](../catalog/csrc/common/compilation_cache.h.md), [csrc/common/compilation_cache.cc](../catalog/csrc/common/compilation_cache.cc.md), [csrc/common/tier2_compilation_cache.cc](../catalog/csrc/common/tier2_compilation_cache.cc.md), [csrc/common/tier3_compilation_cache.cc](../catalog/csrc/common/tier3_compilation_cache.cc.md), [csrc/common/compilation_cache_utils.cc](../catalog/csrc/common/compilation_cache_utils.cc.md), [csrc/common/env_vars.h](../catalog/csrc/common/env_vars.h.md)
- Related doc-concepts: [graph-fingerprint-and-recompilation.md](graph-fingerprint-and-recompilation.md), [defer-and-fuse-materialization.md](defer-and-fuse-materialization.md), [torch-compile-static-shapes-and-bounded-dynamism.md](torch-compile-static-shapes-and-bounded-dynamism.md), [torch-tpu-architecture-and-lowering-stack.md](torch-tpu-architecture-and-lowering-stack.md)

## Source
Extracted from `docs/markdown/compilation_cache.md` ("How the Cache Works", "Warmup Runs") and the "Multi-tier compilation cache" bullet of `docs/markdown/intro_to_torchtpu.md` (= `docs/markdown/1_basics_1_intro_to_torchtpu.md`) (kept in place).
