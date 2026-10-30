---
title: Graph fingerprint and recompilation storms (shape churn, drop_last, warmup)
type: doc-concept
provenance: doc
source: docs/markdown/compilation_cache.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Graph fingerprint and recompilation storms (shape churn, drop_last, warmup)

## Definition
Every recorded computation graph gets a **fingerprint** that indexes the [compilation cache](multi-tier-compilation-cache.md). Per the doc it is built from (1) **input shapes** - and also **input scalar values**, (2) **input dtypes**, and (3) **the exact sequence of ATen ops**. If any of these changes the fingerprint (most likely) changes, the cache misses, and a full compile runs. A workload whose fingerprints never stabilize - variable sequence lengths without padding, data-dependent ops such as `nonzero()`, a ragged last batch - recompiles repeatedly: a **compilation storm**.

The doc's scenario table:

| Input pattern | Distinct graphs | Outcome |
|---|---|---|
| fixed batch 32, fixed seq 128 | 1 | always warm hits |
| fixed batch 32, 3 sequence buckets (128 / 512 / 1024) | 3 | 3 cold starts, then all hits |
| every batch a different length | N | recompiles every step |

## In torch_tpu (grounded)
- The key is a [`CompilationCacheKey`](../catalog/csrc/common/cache_key.h.md#CompilationCacheKey) built around a [`GraphKey`](../catalog/csrc/common/cache_key.h.md#GraphKey), which deliberately splits into a structural [`ShapelessKey`](../catalog/csrc/common/cache_key.h.md#ShapelessKey) (op sequence, dtypes, op params) and a [`DimensionsKey`](../catalog/csrc/common/cache_key.h.md#DimensionsKey) (the concrete sizes). Both come from an ephemeral [`GraphSignature`](../catalog/csrc/common/cache_key.h.md#GraphSignature): tensor dimensions, element types, op names, op inputs/outputs and per-op parameter keys.
- "Sequence of operations" includes non-tensor op parameters: each kernel declares the parameters that change its compilation via [`OpParamCacheKeys`](../catalog/csrc/common/cache_key.h.md#OpParamCacheKeys) / [`MakeOpParamCacheKeys`](../catalog/csrc/common/cache_key.h.md#MakeOpParamCacheKeys) (e.g. `gelu(approximate=...)`), filtered by [`IncludeInCacheKey`](../catalog/csrc/common/cache_key.h.md#IncludeInCacheKey).
- The doc's "scalar values affect the fingerprint" is true only for scalars kept as constants. Many kernels wrap Python scalars in [`PromotedScalar`](../catalog/csrc/common/cache_key.h.md#PromotedScalar), which is lazily promoted to a device tensor and therefore **ignored** in the key; `MaybePromotedScalar` keeps a value in the key only when it matches a special-cased constant (e.g. `alpha == 1` in `add`, so the common case compiles without the extra multiply). So `x * lr` with a changing Python float typically does not recompile, but a scalar baked as an op parameter does.
- Separating `ShapelessKey` from `DimensionsKey` is what enables bounded dynamism in the cache: a [`BoundedDynamicCacheEntry`](../catalog/csrc/common/compilation_cache.h.md#BoundedDynamicCacheEntry) is a `[preamble, middle, postamble]` triplet keyed by shapeless key, where [`CompilationCache.CreatePaddingKernel`](../catalog/csrc/common/compilation_cache.cc.md#CompilationCache.CreatePaddingKernel) pads inputs up to a bound so differing sizes reuse one middle executable ([`CompilationCache.AddBoundedDynamicCacheEntry`](../catalog/csrc/common/compilation_cache.cc.md#CompilationCache.AddBoundedDynamicCacheEntry), metadata in [`ShapeDynamismMetadata`](../catalog/csrc/common/cache_key.h.md#ShapeDynamismMetadata)). The doc does not cover this; it is the runtime side of the bounded-dynamism feature named in the intro ([torch-compile-static-shapes-and-bounded-dynamism.md](torch-compile-static-shapes-and-bounded-dynamism.md)).

## Why it matters / when it applies
- **Pad or bucket outside the compiled region.** Fixed shapes (or a small set of buckets) bound the number of cold compiles; arbitrary lengths make every step a miss.
- **`drop_last=True`.** The doc's production example: batch 32 over 100 samples gives a final batch of 4, which recompiles on the last step of every epoch. Dropping the ragged batch removes it.
- **`num_workers=0` for `DataLoader`.** Not a cache issue but called out on the same page: forking DataLoader workers after the PjRt runtime has started threads and taken `/tmp/libtpu_lockfile` deadlocks silently before step 0; load in-process or use Grain for async input.
- **Data-dependent ops** (`nonzero()`, boolean masking) produce output shapes that depend on values, so downstream graphs re-fingerprint; see [dynamic-shape-ops](../concepts/dynamic-shape-ops.md).
- **Warm up before timing.** Run 2-3 iterations (forcing materialization with `.cpu()`) before starting the timer so compile time is not counted as step time.
- **Catching storms (not in the doc).** The private device-module hooks expose the cache's own view: counters [`_DeviceModule._get_cache_requests`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModule._get_cache_requests) / [`_DeviceModule._get_cache_hits`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModule._get_cache_hits) / [`_DeviceModule._get_cache_misses`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModule._get_cache_misses) (a miss count that keeps rising after warmup is a storm), [`_DeviceModule._set_cache_only`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModule._set_cache_only) (lookup-only, never compile - turns a steady-state miss into a visible failure), and [`_DeviceModule._set_dump_on_cache_miss`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModule._set_dump_on_cache_miss) (dump the StableHLO of every missing graph, so two dumps can be diffed to see what changed). These are underscore APIs - treat them as debugging aids.
- In DeferAndFuse mode, where a materialization trigger falls also decides the op sequence - moving a stray `.item()` changes the fingerprint ([defer-and-fuse-materialization.md](defer-and-fuse-materialization.md)).

## Connections
- Code concepts: [compilation-cache-key](../concepts/compilation-cache-key.md), [compilation-cache](../concepts/compilation-cache.md), [dynamic-shape-ops](../concepts/dynamic-shape-ops.md), [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md), [aten-kernel-authoring](../concepts/aten-kernel-authoring.md), [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md)
- Module catalogs: [csrc/common/cache_key.h](../catalog/csrc/common/cache_key.h.md), [csrc/common/compilation_cache.h](../catalog/csrc/common/compilation_cache.h.md), [csrc/common/compilation_cache.cc](../catalog/csrc/common/compilation_cache.cc.md)
- Related doc-concepts: [multi-tier-compilation-cache.md](multi-tier-compilation-cache.md), [torch-compile-static-shapes-and-bounded-dynamism.md](torch-compile-static-shapes-and-bounded-dynamism.md), [defer-and-fuse-materialization.md](defer-and-fuse-materialization.md), [host-sync-avoidance-in-training-loops.md](host-sync-avoidance-in-training-loops.md)

## Source
Extracted from `docs/markdown/compilation_cache.md` ("Graph Fingerprinting", "Avoiding Unnecessary Recompilations", "Warmup Runs") (kept in place).
