---
title: 'Module: csrc/common/compilation_cache.h'
type: catalog
provenance: extracted
module: csrc/common/compilation_cache.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  CompilationCache: CompilationCache#
  CompilationCache.UnboundedDynamicCache: CompilationCache#UnboundedDynamicCache#
  CompilationCache.CacheEntryKind.kUnboundedDynamic: CompilationCache#CacheEntryKind#kUnboundedDynamic.
  CompilationCache.cache_mutex_: CompilationCache#cache_mutex_.
  CompilationCache.CacheLookupInternal.dump_on_cache_miss: CompilationCache#CacheLookupInternal#dump_on_cache_miss.
  AbslStringify: AbslStringify(8be1c544bbbc12fb).
  PerfStats.num_compilations: PerfStats#num_compilations.
  CacheEntry: CacheEntry#
  CompilationCache.CacheEntryKind: CompilationCache#CacheEntryKind#
  CacheEntry.executable_future: CacheEntry#executable_future(77ce75ff01396132).
  CompilationCache.unbounded_dynamic_cache_: CompilationCache#unbounded_dynamic_cache_.
  CompilationCache.CacheLookupInternal: CompilationCache#CacheLookupInternal#
  CacheEntryStats: CacheEntryStats#
  CompilationCache.BoundedDynamicCache: CompilationCache#BoundedDynamicCache#
  CompilationCache.executable_cache_: CompilationCache#executable_cache_.
  CacheEntry.stats: CacheEntry#stats(d6117618c67c19f3).
  PerfStats: PerfStats#
  PerfStats.per_entry_stats: PerfStats#per_entry_stats.
  CompilationCache.perf_stats_: CompilationCache#perf_stats_.
  UnboundedDynamicCacheEntry: UnboundedDynamicCacheEntry#
  CompilationCache.backup_compilation_pool_: CompilationCache#backup_compilation_pool_.
  UnboundedDynamicCacheEntry.cache_entry: UnboundedDynamicCacheEntry#cache_entry.
  PerfStats.num_cache_hits: PerfStats#num_cache_hits.
  PerfStats.peak_compilation_memory_bytes: PerfStats#peak_compilation_memory_bytes.
  CacheEntryStats.read_count: CacheEntryStats#read_count.
  CacheEntryStats.last_read: CacheEntryStats#last_read.
  CacheEntry.executable_promise: CacheEntry#executable_promise(8eb0a0fabb420e9c).
  PerfStats.num_cache_reqs: PerfStats#num_cache_reqs.
  CompilationCache.bounded_dynamic_cache_: CompilationCache#bounded_dynamic_cache_.
  CacheEntry.CacheEntry: CacheEntry#CacheEntry(49f6e7a06ebc5aa8).
  CacheEntryStats.compilation_duration: CacheEntryStats#compilation_duration.
  CompilationCache.initialized_: CompilationCache#initialized_.
  CompilationCache.dump_on_cache_miss_: CompilationCache#dump_on_cache_miss_.
  PerfStats.num_cache_misses: PerfStats#num_cache_misses(57a65ae535d7db84).
  PerfStats.EntryStats: PerfStats#EntryStats#
  UnboundedDynamicCacheEntry.key: UnboundedDynamicCacheEntry#key.
  CompilationCache.allow_cache_mode_: CompilationCache#allow_cache_mode_.
  CompilationCache.compilation_pool_: CompilationCache#compilation_pool_.
  BoundedDynamicCacheEntry: BoundedDynamicCacheEntry#
  CompilationCache.CacheLookupInternal.shape_dynamism_metadata: CompilationCache#CacheLookupInternal#shape_dynamism_metadata.
  CacheEntry.executable_promise_: CacheEntry#executable_promise_.
  CompilationCache.cache_only_mode_: CompilationCache#cache_only_mode_.
  CacheEntry.operator: CacheEntry#`operator=`(f1a0f79824a84b47).
  BoundedDynamicCacheEntry.middle_executable_key: BoundedDynamicCacheEntry#middle_executable_key.
  UnboundedDynamicCacheEntry.dynamic_meta: UnboundedDynamicCacheEntry#dynamic_meta.
  CacheEntry.executable_future_: CacheEntry#executable_future_.
  CompilationCache.CacheLookupInternal.executable_future: CompilationCache#CacheLookupInternal#executable_future.
  CompilationCache.CacheEntryKind.kStatic: CompilationCache#CacheEntryKind#kStatic.
  CompilationCache.CacheLookupInternal.executable_promise: CompilationCache#CacheLookupInternal#executable_promise.
  CompilationCache.options_: CompilationCache#options_.
  CompilationCacheInitializationOptions: CompilationCacheInitializationOptions#
  PerfStats.EntryStats.key: PerfStats#EntryStats#key.
  CompilationCache.operator: CompilationCache#`operator=`(609f85ccc2f287b6).
  CompilationCache.CompilationCache: CompilationCache#CompilationCache(86680b4dc5d9684f).
  CompilationCache.CacheLookupInternal.needs_compilation: CompilationCache#CacheLookupInternal#needs_compilation.
  BoundedDynamicCacheEntry.shape_dynamism_metadata: BoundedDynamicCacheEntry#shape_dynamism_metadata.
  CompilationCacheInitializationOptions.cache_only: CompilationCacheInitializationOptions#cache_only.
  CacheEntry.stats_: CacheEntry#stats_.
  CacheEntryStats.tier2: CacheEntryStats#tier2.
---
# Module: [`csrc/common/compilation_cache.h`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h)

## Classes
### <a id="BoundedDynamicCacheEntry"></a>`BoundedDynamicCacheEntry`
- def: [`csrc/common/compilation_cache.h:116`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L116) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- signature: `struct BoundedDynamicCacheEntry`
- members:
  - <a id="BoundedDynamicCacheEntry.middle_executable_key"></a>`middle_executable_key` — [`L121`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L121) — The key for the cache entry corresponding to the middle part of the
  - <a id="BoundedDynamicCacheEntry.shape_dynamism_metadata"></a>`shape_dynamism_metadata` — [`L124`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L124) — The shape dynamism metadata required to generate the adapters around the
- uses (calls/refs, reference-scoped): [`ShapeDynamismMetadata`](cache_key.h.md#ShapeDynamismMetadata), [`CompilationCacheKey`](cache_key.h.md#CompilationCacheKey)
- used by: [`GetOrCreateCacheEntry`](compilation_cache.cc.md#CompilationCache.GetOrCreateCacheEntry), [`AddBoundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.AddBoundedDynamicCacheEntry), [`BoundedDynamicCache`](compilation_cache.h.md#CompilationCache.BoundedDynamicCache)

### <a id="CacheEntry"></a>`CacheEntry`
- def: [`csrc/common/compilation_cache.h:84`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L84) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- doc: A cache entry, which is a future executable with its metadata.
- signature: `class CacheEntry`
- members:
  - <a id="CacheEntry.CacheEntry"></a>`CacheEntry()` — [`L86`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L86)
  - `CacheEntry(const CacheEntry&)` — [`L93`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L93)
  - `CacheEntry(CacheEntry&&)` — [`L91`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L91) — This class is movable but not copyable.
  - `CacheEntry(CacheEntry&&)` — [`L91`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L91) — This class is movable but not copyable.
  - <a id="CacheEntry.executable_future"></a>`executable_future()` — [`L97`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L97)
  - <a id="CacheEntry.executable_promise"></a>`executable_promise()` — [`L102`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L102)
  - <a id="CacheEntry.operator"></a>`operator=(const CacheEntry&)` — [`L94`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L94)
  - `operator=(CacheEntry&&)` — [`L92`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L92)
  - `operator=(CacheEntry&&)` — [`L92`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L92)
  - <a id="CacheEntry.stats"></a>`stats()` — [`L106`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L106)
  - <a id="CacheEntry.executable_future_"></a>`executable_future_` — [`L112`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L112)
  - <a id="CacheEntry.executable_promise_"></a>`executable_promise_` — [`L111`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L111) — Order the fields so that the promise is constructed before the future
  - <a id="CacheEntry.stats_"></a>`stats_` — [`L113`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L113)
- uses (calls/refs, reference-scoped): [`SharedLoadedExecutableWithMetadataFuture`](compilation.h.md#SharedLoadedExecutableWithMetadataFuture), [`CacheEntryStats`](compilation_cache.h.md#CacheEntryStats), [`LoadedExecutablePromise`](compilation.h.md#LoadedExecutablePromise)
- used by: [`EvictAll`](compilation_cache.cc.md#CompilationCache.EvictAll), [`GetFromTier3OrCompile`](compilation_cache.cc.md#CompilationCache.GetFromTier3OrCompile), [`SetExecutable`](compilation_cache.cc.md#CompilationCache.SetExecutable), [`AddUnboundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.AddUnboundedDynamicCacheEntry), [`GetCacheStats`](compilation_cache.cc.md#CompilationCache.GetCacheStats), [`GetUnboundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.GetUnboundedDynamicCacheEntry), [`GetStaticCacheEntry`](compilation_cache.cc.md#CompilationCache.GetStaticCacheEntry), [`FindUnboundedDynamicCacheEntryOrNull`](compilation_cache.cc.md#CompilationCache.FindUnboundedDynamicCacheEntryOrNull), [`AddStaticCacheEntry`](compilation_cache.cc.md#CompilationCache.AddStaticCacheEntry), [`GetUnboundedDynamicCacheEntryStats`](compilation_cache_test.cc.md#CompilationCacheTestHelper.GetUnboundedDynamicCacheEntryStats), [`HbmUsageSummary`](compilation_cache.cc.md#CompilationCache.HbmUsageSummary), [`IsExecutableReady`](compilation_cache.cc.md#CompilationCache.IsExecutableReady), [`dump_on_cache_miss`](compilation_cache.h.md#CompilationCache.CacheLookupInternal.dump_on_cache_miss), [`backup_compilation_pool_`](compilation_cache.h.md#CompilationCache.backup_compilation_pool_), [`dynamic_meta`](compilation_cache.h.md#UnboundedDynamicCacheEntry.dynamic_meta)

### <a id="CacheEntryStats"></a>`CacheEntryStats`
- def: [`csrc/common/compilation_cache.h:56`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L56) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- doc: Statistics for a single entry in the tier-1 compilation cache.
- signature: `struct CacheEntryStats`
- members:
  - <a id="CacheEntryStats.compilation_duration"></a>`compilation_duration` — [`L60`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L60) — If the entry was successfully compiled by this process, this is the time it
  - <a id="CacheEntryStats.last_read"></a>`last_read` — [`L63`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L63) — The last time this entry was read. The initial compilation counts as one
  - <a id="CacheEntryStats.read_count"></a>`read_count` — [`L67`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L67) — How many times this entry has been read. The initial compilation counts as
  - <a id="CacheEntryStats.tier2"></a>`tier2` — [`L70`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L70) — Set only when the entry is populated from the tier-2 cache as opposed to
- uses (calls/refs, reference-scoped): [`Tier2CacheEntryStats`](tier2_compilation_cache.h.md#Tier2CacheEntryStats), [`EntryStats`](compilation_cache.h.md#PerfStats.EntryStats)
- used by: [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_UnboundedDynamicCache_Test.TestBody), [`UnboundedDynamicCache`](compilation_cache.h.md#CompilationCache.UnboundedDynamicCache), [`GetFromTier3OrCompile`](compilation_cache.cc.md#CompilationCache.GetFromTier3OrCompile), [`SetExecutable`](compilation_cache.cc.md#CompilationCache.SetExecutable), [`GetUnboundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.GetUnboundedDynamicCacheEntry), [`GetStaticCacheEntry`](compilation_cache.cc.md#CompilationCache.GetStaticCacheEntry), [`TestBody`](compilation_cache_test.cc.md#CacheEntryStatsPrinterTest_Works_Test.TestBody), [`AbslStringify`](compilation_cache.h.md#AbslStringify), [`AbslStringify`](compilation_cache.h.md#AbslStringify), [`AbslStringify`](compilation_cache.h.md#AbslStringify), [`RestartCompilationCache`](compilation_cache_test.cc.md#CompilationCacheTestHelper.RestartCompilationCache), [`executable_promise`](compilation_cache.h.md#CacheEntry.executable_promise), [`EntryStats`](compilation_cache.h.md#PerfStats.EntryStats), [`executable_future_`](compilation_cache.h.md#CacheEntry.executable_future_)

### <a id="CompilationCache"></a>`CompilationCache`
- def: [`csrc/common/compilation_cache.h:201`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L201) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- doc: An in-memory cache for compiled XLA programs. The ownership of cached
- signature: `class CompilationCache`
- members:
  - <a id="CompilationCache.CompilationCache"></a>`CompilationCache(CompilationCache&&)` — [`L206`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L206)
  - `CompilationCache(const CompilationCache&)` — [`L204`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L204) — CompilationCache is neither copyable nor movable.
  - <a id="CompilationCache.operator"></a>`operator=(const CompilationCache&)` — [`L205`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L205)
  - `operator=(CompilationCache&&)` — [`L207`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L207)
  - <a id="CompilationCache.allow_cache_mode_"></a>`allow_cache_mode_` — [`L598`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L598) — If true, the cache will be enabled. If false, the cache will be disabled
  - <a id="CompilationCache.backup_compilation_pool_"></a>`backup_compilation_pool_` — [`L578`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L578) — Lower-priority thread pool for running backup compilations.
  - <a id="CompilationCache.bounded_dynamic_cache_"></a>`bounded_dynamic_cache_` — [`L587`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L587) — The cache of successfully compiled and in flight executables with bounded
  - <a id="CompilationCache.cache_mutex_"></a>`cache_mutex_` — [`L571`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L571) — Main mutex for protecting cache statistics and cache-only mode.
  - <a id="CompilationCache.cache_only_mode_"></a>`cache_only_mode_` — [`L601`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L601) — If true, the cache will only lookup and not compile. Any cache miss will
  - <a id="CompilationCache.compilation_pool_"></a>`compilation_pool_` — [`L574`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L574) — Thread pool for running compilations concurrently.
  - <a id="CompilationCache.dump_on_cache_miss_"></a>`dump_on_cache_miss_` — [`L604`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L604) — If true, the cache will dump the input StableHLO module for any cache
  - <a id="CompilationCache.executable_cache_"></a>`executable_cache_` — [`L583`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L583) — The cache of successfully compiled and in flight executables.
  - <a id="CompilationCache.initialized_"></a>`initialized_` — [`L610`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L610) — Whether the cache has been fully initialized (thread pools started).
  - <a id="CompilationCache.options_"></a>`options_` — [`L607`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L607) — The current initialization options.
  - <a id="CompilationCache.perf_stats_"></a>`perf_stats_` — [`L594`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L594) — Cache statistics.
  - <a id="CompilationCache.unbounded_dynamic_cache_"></a>`unbounded_dynamic_cache_` — [`L591`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L591) — The cache of successfully compiled executables with unbounded dynamic
- uses (calls/refs, reference-scoped): [`CompilationCacheKey`](cache_key.h.md#CompilationCacheKey), [`UnboundedDynamicCache`](compilation_cache.h.md#CompilationCache.UnboundedDynamicCache), [`GetNumCompilationThreads`](compilation_cache.cc.md#GetNumCompilationThreads), [`CacheEntry`](compilation_cache.h.md#CacheEntry), [`BoundedDynamicCache`](compilation_cache.h.md#CompilationCache.BoundedDynamicCache), [`ThreadPool`](thread_pool.h.md#ThreadPool), [`PerfStats`](compilation_cache.h.md#PerfStats), [`CompilationCacheInitializationOptions`](compilation_cache.h.md#CompilationCacheInitializationOptions), [`Hash`](cache_key.h.md#CompilationCacheKey.Hash)
- used by: [`GetInstance`](compilation_cache.cc.md#CompilationCache.GetInstance), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_UnboundedDynamicCache_Test.TestBody), [`GetOrCreateCacheEntry`](compilation_cache.cc.md#CompilationCache.GetOrCreateCacheEntry), [`Compile`](../eager/traversal.cc.md#Traversal.Compile), [`TestBody`](../experimental/precompiled_kernels/nonzero_indices_test.cc.md#NonzeroIndicesTest_UnboundedDynamicCacheServesKernel_Test.TestBody), [`TestBody`](../eager/materialize_test.cc.md#MaterializeTest_CompilerOptionsPropagateToMaterializeThread_Test.TestBody), [`UnboundedDynamicCache`](compilation_cache.h.md#CompilationCache.UnboundedDynamicCache), [`GetOrCompileImpl`](compilation_cache.cc.md#CompilationCache.GetOrCompileImpl), [`kUnboundedDynamic`](compilation_cache.h.md#CompilationCache.CacheEntryKind.kUnboundedDynamic), [`EvictAll`](compilation_cache.cc.md#CompilationCache.EvictAll), [`GetFromTier3OrCompile`](compilation_cache.cc.md#CompilationCache.GetFromTier3OrCompile), [`SetExecutable`](compilation_cache.cc.md#CompilationCache.SetExecutable), [`AddBoundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.AddBoundedDynamicCacheEntry), [`AddUnboundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.AddUnboundedDynamicCacheEntry), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_UnboundedDynamicCacheEvictAll_Test.TestBody), [`PyPrecompileSliceModule`](../internal/compile/tpu_torch_compile.cc.md#PyPrecompileSliceModule), [`GetCacheStats`](compilation_cache.cc.md#CompilationCache.GetCacheStats), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_DynamicCacheLayoutMismatch_Test.TestBody), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_UnboundedDynamicCacheOutputShapeMismatch_Test.TestBody), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_UnboundedDynamicCacheShapeMismatch_Test.TestBody), [`PyPrecompilePadModule`](../internal/compile/tpu_torch_compile.cc.md#PyPrecompilePadModule), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_UnboundedDynamicCacheMiss_Test.TestBody), [`CreateSlicingKernel`](compilation_cache.cc.md#CompilationCache.CreateSlicingKernel), [`GetCacheHits`](compilation_cache.cc.md#CompilationCache.GetCacheHits), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_PeakMemoryReported_Test.TestBody), [`GetCacheMisses`](compilation_cache.cc.md#CompilationCache.GetCacheMisses), [`ShutDown`](compilation_cache.cc.md#CompilationCache.ShutDown), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_UnboundedDynamicCacheBackendNotInitialized_Test.TestBody), [`CompileModuleWithCache`](../internal/compile/tpu_torch_compile.cc.md#CompileModuleWithCache), [`Compile`](compilation_cache.cc.md#CompilationCache.Compile), [`CreateDynamicKernelAdapter`](compilation_cache.cc.md#CompilationCache.CreateDynamicKernelAdapter), [`TestBody`](compilation_cache_tiered_test.cc.md#TieredCompilationCacheTest_UnboundedDynamicCacheTier3Hit_Test.TestBody), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_AllowCacheModeDisabled_Test.TestBody), [`TestBody`](compilation_cache_tiered_test.cc.md#TieredCompilationCacheTest_UnboundedDynamicCacheTier2Hit_Test.TestBody), [`GetFromTier2OrCompile`](compilation_cache.cc.md#CompilationCache.GetFromTier2OrCompile), [`GetUnboundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.GetUnboundedDynamicCacheEntry), [`CreatePaddingKernel`](compilation_cache.cc.md#CompilationCache.CreatePaddingKernel), [`EnqueueCompilation`](compilation_cache.cc.md#CompilationCache.EnqueueCompilation), [`cache_instance_mutex_`](compilation_cache.cc.md#CompilationCache.cache_instance_mutex_), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_GetOrCompileLogsOnMiss_Test.TestBody)  (+40 more)

### <a id="CompilationCache.BoundedDynamicCache"></a>`CompilationCache.BoundedDynamicCache`
- def: [`csrc/common/compilation_cache.h:409`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L409)
- signature: `using BoundedDynamicCache = absl::flat_hash_map<ShapelessKey, std::vector<BoundedDynamicCacheEntry>, ShapelessKey::Hash>`
- uses (calls/refs, reference-scoped): [`ShapelessKey`](cache_key.h.md#ShapelessKey), [`BoundedDynamicCacheEntry`](compilation_cache.h.md#BoundedDynamicCacheEntry), [`Hash`](cache_key.h.md#ShapelessKey.Hash)
- used by: [`GetOrCreateCacheEntry`](compilation_cache.cc.md#CompilationCache.GetOrCreateCacheEntry), [`UnboundedDynamicCache`](compilation_cache.h.md#CompilationCache.UnboundedDynamicCache), [`AddBoundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.AddBoundedDynamicCacheEntry), [`GetStaticCacheEntry`](compilation_cache.cc.md#CompilationCache.GetStaticCacheEntry), [`executable_cache_`](compilation_cache.h.md#CompilationCache.executable_cache_)

### <a id="CompilationCache.CacheEntryKind"></a>`CompilationCache.CacheEntryKind`
- def: [`csrc/common/compilation_cache.h:211`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L211)
- doc: Which tier-1 cache a key lives in. The tiered lookup/compile path is shared
- signature: `enum class CacheEntryKind`
- members:
  - <a id="CompilationCache.CacheEntryKind.kStatic"></a>`kStatic` — [`L212`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L212)
  - <a id="CompilationCache.CacheEntryKind.kUnboundedDynamic"></a>`kUnboundedDynamic` — [`L213`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L213)
- uses (calls/refs, reference-scoped): [`CompilationCache`](compilation_cache.h.md#CompilationCache), [`Shape`](shape.h.md#Shape), [`CompilationCacheKey`](cache_key.h.md#CompilationCacheKey), [`GetInstance`](compilation_cache.cc.md#CompilationCache.GetInstance), [`ContextedModule`](compilation.h.md#ContextedModule), [`EvictAll`](compilation_cache.cc.md#CompilationCache.EvictAll), [`AddUnboundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.AddUnboundedDynamicCacheEntry), [`GetCacheStats`](compilation_cache.cc.md#CompilationCache.GetCacheStats), [`GetCacheHits`](compilation_cache.cc.md#CompilationCache.GetCacheHits), [`GetOrCompile`](compilation_cache.cc.md#CompilationCache.GetOrCompile), [`cache_mutex_`](compilation_cache.h.md#CompilationCache.cache_mutex_), [`GetCacheMisses`](compilation_cache.cc.md#CompilationCache.GetCacheMisses), [`ShutDown`](compilation_cache.cc.md#CompilationCache.ShutDown), [`AddUnboundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.AddUnboundedDynamicCacheEntry), [`UniqueCompileOptions`](compilation_spec.h.md#UniqueCompileOptions), [`EnqueueCompilation`](compilation_cache.cc.md#CompilationCache.EnqueueCompilation), [`cache_instance_mutex_`](compilation_cache.cc.md#CompilationCache.cache_instance_mutex_), [`CompiledKernel`](compilation.h.md#CompiledKernel), [`GetOrCompile`](compilation_cache.cc.md#CompilationCache.GetOrCompile), [`SetOptions`](compilation_cache.cc.md#CompilationCache.SetOptions), [`MlirComputationBuilder`](../ops/op_builder_utils.h.md#MlirComputationBuilder), [`UnboundedDynamicExecutionMetadata`](compilation.h.md#UnboundedDynamicExecutionMetadata), [`Restart`](compilation_cache.cc.md#CompilationCache.Restart), [`GetDumpOnCacheMissMode`](compilation_cache.cc.md#CompilationCache.GetDumpOnCacheMissMode), [`IsInitialized`](compilation_cache.cc.md#CompilationCache.IsInitialized), [`SetAllowCacheMode`](compilation_cache.cc.md#CompilationCache.SetAllowCacheMode), [`SetDumpOnCacheMissMode`](compilation_cache.cc.md#CompilationCache.SetDumpOnCacheMissMode), [`HbmUsageSummary`](compilation_cache.cc.md#CompilationCache.HbmUsageSummary), [`CompilationCacheTestHelper`](compilation_cache_test.cc.md#CompilationCacheTestHelper), [`IsExecutableReady`](compilation_cache.cc.md#CompilationCache.IsExecutableReady), [`~CompilationCache`](compilation_cache.cc.md#CompilationCache.-CompilationCache), [`GetCacheRequests`](compilation_cache.cc.md#CompilationCache.GetCacheRequests), [`LoadedExecutableBuilder`](compilation.h.md#LoadedExecutableBuilder), [`GetOrCompile`](compilation_cache.cc.md#CompilationCache.GetOrCompile), [`SetCacheOnlyMode`](compilation_cache.cc.md#CompilationCache.SetCacheOnlyMode), [`PerfStats`](compilation_cache.h.md#PerfStats), [`CompilationCacheInitializationOptions`](compilation_cache.h.md#CompilationCacheInitializationOptions), [`EnqueueCompilation`](compilation_cache.cc.md#CompilationCache.EnqueueCompilation), [`GetOrCompile`](compilation_cache.cc.md#CompilationCache.GetOrCompile)
- used by: [`UnboundedDynamicCache`](compilation_cache.h.md#CompilationCache.UnboundedDynamicCache), [`GetFromTier3OrCompile`](compilation_cache.cc.md#CompilationCache.GetFromTier3OrCompile), [`SetExecutable`](compilation_cache.cc.md#CompilationCache.SetExecutable), [`AddUnboundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.AddUnboundedDynamicCacheEntry), [`Compile`](compilation_cache.cc.md#CompilationCache.Compile), [`GetFromTier2OrCompile`](compilation_cache.cc.md#CompilationCache.GetFromTier2OrCompile), [`EnqueueCompilation`](compilation_cache.cc.md#CompilationCache.EnqueueCompilation), [`FindCacheEntryOrNull`](compilation_cache.cc.md#CompilationCache.FindCacheEntryOrNull), [`IsExecutableReady`](compilation_cache.cc.md#CompilationCache.IsExecutableReady), [`dump_on_cache_miss`](compilation_cache.h.md#CompilationCache.CacheLookupInternal.dump_on_cache_miss)

### <a id="CompilationCache.CacheLookupInternal"></a>`CompilationCache.CacheLookupInternal`
- def: [`csrc/common/compilation_cache.h:377`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L377)
- doc: The internal variant type for GetOrCreateCacheEntry, which returns
- signature: `struct CacheLookupInternal`
- members:
  - <a id="CompilationCache.CacheLookupInternal.dump_on_cache_miss"></a>`dump_on_cache_miss` — [`L382`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L382)
  - <a id="CompilationCache.CacheLookupInternal.executable_future"></a>`executable_future` — [`L379`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L379)
  - <a id="CompilationCache.CacheLookupInternal.executable_promise"></a>`executable_promise` — [`L378`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L378)
  - <a id="CompilationCache.CacheLookupInternal.needs_compilation"></a>`needs_compilation` — [`L381`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L381)
  - <a id="CompilationCache.CacheLookupInternal.shape_dynamism_metadata"></a>`shape_dynamism_metadata` — [`L380`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L380)
- uses (calls/refs, reference-scoped): [`ShapeDynamismMetadata`](cache_key.h.md#ShapeDynamismMetadata), [`CompilationCacheKey`](cache_key.h.md#CompilationCacheKey), [`cache_mutex_`](compilation_cache.h.md#CompilationCache.cache_mutex_), [`GetStaticCacheEntry`](compilation_cache.cc.md#CompilationCache.GetStaticCacheEntry), [`FindCacheEntryOrNull`](compilation_cache.cc.md#CompilationCache.FindCacheEntryOrNull), [`FindUnboundedDynamicCacheEntryOrNull`](compilation_cache.cc.md#CompilationCache.FindUnboundedDynamicCacheEntryOrNull), [`FindStaticCacheEntryOrNull`](compilation_cache.cc.md#CompilationCache.FindStaticCacheEntryOrNull), [`SharedLoadedExecutableWithMetadataFuture`](compilation.h.md#SharedLoadedExecutableWithMetadataFuture), [`CacheEntry`](compilation_cache.h.md#CacheEntry), [`CacheEntryKind`](compilation_cache.h.md#CompilationCache.CacheEntryKind), [`UnboundedDynamicCacheEntry`](compilation_cache.h.md#UnboundedDynamicCacheEntry), [`LoadedExecutablePromise`](compilation.h.md#LoadedExecutablePromise)
- used by: [`GetOrCreateCacheEntry`](compilation_cache.cc.md#CompilationCache.GetOrCreateCacheEntry), [`UnboundedDynamicCache`](compilation_cache.h.md#CompilationCache.UnboundedDynamicCache), [`GetOrCompileImpl`](compilation_cache.cc.md#CompilationCache.GetOrCompileImpl), [`AddBoundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.AddBoundedDynamicCacheEntry), [`AddUnboundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.AddUnboundedDynamicCacheEntry), [`GetUnboundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.GetUnboundedDynamicCacheEntry), [`GetStaticCacheEntry`](compilation_cache.cc.md#CompilationCache.GetStaticCacheEntry), [`FindCacheEntryOrNull`](compilation_cache.cc.md#CompilationCache.FindCacheEntryOrNull), [`AddStaticCacheEntry`](compilation_cache.cc.md#CompilationCache.AddStaticCacheEntry), [`GetBoundedDynamicCacheEntries`](compilation_cache.cc.md#CompilationCache.GetBoundedDynamicCacheEntries)

### <a id="CompilationCache.UnboundedDynamicCache"></a>`CompilationCache.UnboundedDynamicCache`
- def: [`csrc/common/compilation_cache.h:412`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L412)
- signature: `using UnboundedDynamicCache = absl::flat_hash_map<ShapelessKey, std::vector<UnboundedDynamicCacheEntry>, ShapelessKey::Hash>`
- uses (calls/refs, reference-scoped): [`Shape`](shape.h.md#Shape), [`ShapeDynamismMetadata`](cache_key.h.md#ShapeDynamismMetadata), [`CompilationCacheKey`](cache_key.h.md#CompilationCacheKey), [`GetOrCreateCacheEntry`](compilation_cache.cc.md#CompilationCache.GetOrCreateCacheEntry), [`GetOrCompileImpl`](compilation_cache.cc.md#CompilationCache.GetOrCompileImpl), [`SharedLoadedExecutableWithMetadata`](compilation.h.md#SharedLoadedExecutableWithMetadata), [`GetFromTier3OrCompile`](compilation_cache.cc.md#CompilationCache.GetFromTier3OrCompile), [`SetExecutable`](compilation_cache.cc.md#CompilationCache.SetExecutable), [`AddBoundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.AddBoundedDynamicCacheEntry), [`CompileOptionsKey`](compile_options_key.h.md#CompileOptionsKey), [`CreateSlicingKernel`](compilation_cache.cc.md#CompilationCache.CreateSlicingKernel), [`cache_mutex_`](compilation_cache.h.md#CompilationCache.cache_mutex_), [`Compile`](compilation_cache.cc.md#CompilationCache.Compile), [`CreateDynamicKernelAdapter`](compilation_cache.cc.md#CompilationCache.CreateDynamicKernelAdapter), [`GetFromTier2OrCompile`](compilation_cache.cc.md#CompilationCache.GetFromTier2OrCompile), [`GetUnboundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.GetUnboundedDynamicCacheEntry), [`CreatePaddingKernel`](compilation_cache.cc.md#CompilationCache.CreatePaddingKernel), [`UniqueCompileOptions`](compilation_spec.h.md#UniqueCompileOptions), [`CompiledKernel`](compilation.h.md#CompiledKernel), [`ShapelessKey`](cache_key.h.md#ShapelessKey), [`AddStaticCacheEntry`](compilation_cache.cc.md#CompilationCache.AddStaticCacheEntry), [`MlirComputationBuilder`](../ops/op_builder_utils.h.md#MlirComputationBuilder), [`Tier2CacheEntryLock`](tier2_compilation_cache.h.md#Tier2CacheEntryLock), [`SharedLoadedExecutableWithMetadataFuture`](compilation.h.md#SharedLoadedExecutableWithMetadataFuture), [`ShouldUseTier2Cache`](compilation_cache.cc.md#CompilationCache.ShouldUseTier2Cache), [`CacheEntryKind`](compilation_cache.h.md#CompilationCache.CacheEntryKind), [`LoadedExecutableBuilder`](compilation.h.md#LoadedExecutableBuilder), [`CacheLookupInternal`](compilation_cache.h.md#CompilationCache.CacheLookupInternal), [`BoundedDynamicCache`](compilation_cache.h.md#CompilationCache.BoundedDynamicCache), [`CacheEntryStats`](compilation_cache.h.md#CacheEntryStats), [`UnboundedDynamicCacheEntry`](compilation_cache.h.md#UnboundedDynamicCacheEntry), [`GetBoundedDynamicCacheEntries`](compilation_cache.cc.md#CompilationCache.GetBoundedDynamicCacheEntries), [`GetOrCompileImpl`](compilation_cache.cc.md#CompilationCache.GetOrCompileImpl), [`DynamicKernelAdapter`](compilation.h.md#DynamicKernelAdapter), [`CreateDynamicKernelAdapter`](compilation_cache.cc.md#CompilationCache.CreateDynamicKernelAdapter), [`CreatePaddingKernel`](compilation_cache.cc.md#CompilationCache.CreatePaddingKernel), [`CreateSlicingKernel`](compilation_cache.cc.md#CompilationCache.CreateSlicingKernel), [`GetBoundedDynamicCacheEntries`](compilation_cache.cc.md#CompilationCache.GetBoundedDynamicCacheEntries), [`GetFromTier3OrCompile`](compilation_cache.cc.md#CompilationCache.GetFromTier3OrCompile), [`Hash`](cache_key.h.md#ShapelessKey.Hash)  (+4 more)
- used by: [`bounded_dynamic_cache_`](compilation_cache.h.md#CompilationCache.bounded_dynamic_cache_)

### <a id="CompilationCacheInitializationOptions"></a>`CompilationCacheInitializationOptions`
- def: [`csrc/common/compilation_cache.h:51`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L51) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- signature: `struct CompilationCacheInitializationOptions`
- members:
  - <a id="CompilationCacheInitializationOptions.cache_only"></a>`cache_only` — [`L52`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L52)
- used by: [`kUnboundedDynamic`](compilation_cache.h.md#CompilationCache.CacheEntryKind.kUnboundedDynamic), [`SetOptions`](compilation_cache.cc.md#CompilationCache.SetOptions), [`dump_on_cache_miss_`](compilation_cache.h.md#CompilationCache.dump_on_cache_miss_)

### <a id="PerfStats"></a>`PerfStats`
- def: [`csrc/common/compilation_cache.h:137`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L137) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- doc: Aggregated statistics for the compilation cache.
- signature: `struct PerfStats`
- members:
  - <a id="PerfStats.num_cache_misses"></a>`num_cache_misses()` — [`L153`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L153) — These fields refer to the tier-1 cache. E.g. a hit here means the entry was
  - <a id="PerfStats.num_cache_hits"></a>`num_cache_hits` — [`L155`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L155)
  - <a id="PerfStats.num_cache_reqs"></a>`num_cache_reqs` — [`L154`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L154)
  - <a id="PerfStats.num_compilations"></a>`num_compilations` — [`L156`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L156)
  - <a id="PerfStats.peak_compilation_memory_bytes"></a>`peak_compilation_memory_bytes` — [`L159`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L159) — Peak memory usage (host) during compilation in bytes across all concurrent
  - <a id="PerfStats.per_entry_stats"></a>`per_entry_stats` — [`L161`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L161)
- uses (calls/refs, reference-scoped): [`EntryStats`](compilation_cache.h.md#PerfStats.EntryStats)
- used by: [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_UnboundedDynamicCache_Test.TestBody), [`GetOrCreateCacheEntry`](compilation_cache.cc.md#CompilationCache.GetOrCreateCacheEntry), [`TestBody`](../eager/materialize_test.cc.md#MaterializeTest_CompilerOptionsPropagateToMaterializeThread_Test.TestBody), [`GetOrCompileImpl`](compilation_cache.cc.md#CompilationCache.GetOrCompileImpl), [`kUnboundedDynamic`](compilation_cache.h.md#CompilationCache.CacheEntryKind.kUnboundedDynamic), [`EvictAll`](compilation_cache.cc.md#CompilationCache.EvictAll), [`GetCacheStats`](compilation_cache.cc.md#CompilationCache.GetCacheStats), [`GetCacheHits`](compilation_cache.cc.md#CompilationCache.GetCacheHits), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_PeakMemoryReported_Test.TestBody), [`GetCacheMisses`](compilation_cache.cc.md#CompilationCache.GetCacheMisses), [`Compile`](compilation_cache.cc.md#CompilationCache.Compile), [`TestBody`](compilation_cache_tiered_test.cc.md#TieredCompilationCacheTest_UnboundedDynamicCacheTier3Hit_Test.TestBody), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_AllowCacheModeDisabled_Test.TestBody), [`TestBody`](compilation_cache_tiered_test.cc.md#TieredCompilationCacheTest_UnboundedDynamicCacheTier2Hit_Test.TestBody), [`GetUnboundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.GetUnboundedDynamicCacheEntry), [`GetStaticCacheEntry`](compilation_cache.cc.md#CompilationCache.GetStaticCacheEntry), [`TestBody`](compilation_cache_test.cc.md#PerfStatsPrinterTest_WithPerEntry_Test.TestBody), [`AbslStringify`](compilation_cache.h.md#AbslStringify), [`TestBody`](compilation_cache_test.cc.md#PerfStatsPrinterTest_EmptyPerEntry_Test.TestBody), [`GetCacheRequests`](compilation_cache.cc.md#CompilationCache.GetCacheRequests), [`unbounded_dynamic_cache_`](compilation_cache.h.md#CompilationCache.unbounded_dynamic_cache_)

### <a id="PerfStats.EntryStats"></a>`PerfStats.EntryStats`  ·  implements/extends CacheEntryStats
- def: [`csrc/common/compilation_cache.h:139`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L139)
- doc: Statistics for a single entry in the compilation cache.
- signature: `struct EntryStats : public CacheEntryStats`
- members:
  - <a id="PerfStats.EntryStats.key"></a>`key` — [`L140`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L140)
- uses (calls/refs, reference-scoped): [`CompilationCacheKey`](cache_key.h.md#CompilationCacheKey), [`CacheEntryStats`](compilation_cache.h.md#CacheEntryStats)
- used by: [`TestBody`](../eager/materialize_test.cc.md#MaterializeTest_CompilerOptionsPropagateToMaterializeThread_Test.TestBody), [`CacheEntryStats`](compilation_cache.h.md#CacheEntryStats), [`peak_compilation_memory_bytes`](compilation_cache.h.md#PerfStats.peak_compilation_memory_bytes), [`AbslStringify`](compilation_cache.h.md#AbslStringify)

### <a id="UnboundedDynamicCacheEntry"></a>`UnboundedDynamicCacheEntry`
- def: [`csrc/common/compilation_cache.h:127`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L127)
- signature: `struct UnboundedDynamicCacheEntry`
- members:
  - <a id="UnboundedDynamicCacheEntry.cache_entry"></a>`cache_entry` — [`L133`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L133)
  - <a id="UnboundedDynamicCacheEntry.dynamic_meta"></a>`dynamic_meta` — [`L132`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L132) — Consulted for compatibility checks while the executable is still in
  - <a id="UnboundedDynamicCacheEntry.key"></a>`key` — [`L128`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L128)
- uses (calls/refs, reference-scoped): [`CompilationCacheKey`](cache_key.h.md#CompilationCacheKey), [`UnboundedDynamicExecutionMetadata`](compilation.h.md#UnboundedDynamicExecutionMetadata), [`CacheEntry`](compilation_cache.h.md#CacheEntry)
- used by: [`UnboundedDynamicCache`](compilation_cache.h.md#CompilationCache.UnboundedDynamicCache), [`EvictAll`](compilation_cache.cc.md#CompilationCache.EvictAll), [`SetExecutable`](compilation_cache.cc.md#CompilationCache.SetExecutable), [`AddUnboundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.AddUnboundedDynamicCacheEntry), [`GetUnboundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.GetUnboundedDynamicCacheEntry), [`FindCacheEntryOrNull`](compilation_cache.cc.md#CompilationCache.FindCacheEntryOrNull), [`FindUnboundedDynamicCacheEntryOrNull`](compilation_cache.cc.md#CompilationCache.FindUnboundedDynamicCacheEntryOrNull), [`GetUnboundedDynamicCacheEntryStats`](compilation_cache_test.cc.md#CompilationCacheTestHelper.GetUnboundedDynamicCacheEntryStats), [`HbmUsageSummary`](compilation_cache.cc.md#CompilationCache.HbmUsageSummary), [`FindStaticCacheEntryOrNull`](compilation_cache.cc.md#CompilationCache.FindStaticCacheEntryOrNull), [`dump_on_cache_miss`](compilation_cache.h.md#CompilationCache.CacheLookupInternal.dump_on_cache_miss)

## Functions
- `AbslStringify(Sink& sink, const EntryStats& stats)` — [`L143`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L143)
- `AbslStringify(Sink& sink, const CacheEntryStats& stats)` — [`L73`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L73)
- <a id="AbslStringify"></a>`AbslStringify(Sink& sink, const PerfStats& stats)` — [`L164`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.h#L164)

