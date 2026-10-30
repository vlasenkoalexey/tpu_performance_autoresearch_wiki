---
title: 'Module: csrc/common/compilation_cache.cc'
type: catalog
provenance: extracted
module: csrc/common/compilation_cache.cc
status: fresh
symbol_base: 'cxx . . $ '
symbols:
  CompilationCache.GetInstance: torch_tpu/CompilationCache#GetInstance(15e4193957bd01fd).
  CompilationCache.GetOrCreateCacheEntry: torch_tpu/CompilationCache#GetOrCreateCacheEntry(dec4fd2efbafadb4).
  CompilationCache.GetOrCompileImpl: torch_tpu/CompilationCache#GetOrCompileImpl(446291b654431f21).
  CompilationCache.EvictAll: torch_tpu/CompilationCache#EvictAll(49f6e7a06ebc5aa8).
  CompilationCache.GetFromTier3OrCompile: torch_tpu/CompilationCache#GetFromTier3OrCompile(e93260515eaa9450).
  CompilationCache.SetExecutable: torch_tpu/CompilationCache#SetExecutable(ccd8a37d7af885bf).
  CompilationCache.AddBoundedDynamicCacheEntry: torch_tpu/CompilationCache#AddBoundedDynamicCacheEntry(ef791f5b07337358).
  CompilationCache.AddUnboundedDynamicCacheEntry: torch_tpu/CompilationCache#AddUnboundedDynamicCacheEntry(e8c7e6f2e8f36a9e).
  CompilationCache.GetCacheStats: torch_tpu/CompilationCache#GetCacheStats(6b7adfe1d99d1259).
  CompilationCache.GetCacheHits: torch_tpu/CompilationCache#GetCacheHits(57a65ae535d7db84).
  CompilationCache.CreateSlicingKernel: torch_tpu/CompilationCache#CreateSlicingKernel(ef87febca74172a7).
  CompilationCache.GetOrCompile: torch_tpu/CompilationCache#GetOrCompile(d47c77059a94a130).
  AnyInducesLayoutChange: torch_tpu/`$anonymous_namespace_csrc/common/compilation_cache.cc`/AnyInducesLayoutChange(449ce7dcb191ead2).
  CompilationCache.GetCacheMisses: torch_tpu/CompilationCache#GetCacheMisses(57a65ae535d7db84).
  CompilationCache.ShutDown: torch_tpu/CompilationCache#ShutDown(49f6e7a06ebc5aa8).
  CompilationCache.Compile: torch_tpu/CompilationCache#Compile(f34680d52b6e0fde).
  CompilationCache.CreateDynamicKernelAdapter: torch_tpu/CompilationCache#CreateDynamicKernelAdapter(8bc32a1e42cfcd4e).
  CompilationCache.GetFromTier2OrCompile: torch_tpu/CompilationCache#GetFromTier2OrCompile(f34680d52b6e0fde).
  CompilationCache.GetUnboundedDynamicCacheEntry: torch_tpu/CompilationCache#GetUnboundedDynamicCacheEntry(a0e3c1004e3bf4a2).
  CompilationCache.CreatePaddingKernel: torch_tpu/CompilationCache#CreatePaddingKernel(fa7b5c2ac9b77454).
  CompilationCache.EnqueueCompilation: torch_tpu/CompilationCache#EnqueueCompilation(767a1dbc01f97b92).
  CompilationCache.cache_instance_mutex_: torch_tpu/CompilationCache#cache_instance_mutex_.
  CompilationCache.EnsureInitialized: torch_tpu/CompilationCache#EnsureInitialized(49f6e7a06ebc5aa8).
  CompilationCache.GetStaticCacheEntry: torch_tpu/CompilationCache#GetStaticCacheEntry(436758b81802fffd).
  CompilationCache.FindCacheEntryOrNull: torch_tpu/CompilationCache#FindCacheEntryOrNull(83f908947864f686).
  CompilationCache.FindUnboundedDynamicCacheEntryOrNull: torch_tpu/CompilationCache#FindUnboundedDynamicCacheEntryOrNull(b9f7e53919d69915).
  ResolvePaddingShapes: torch_tpu/`$anonymous_namespace_csrc/common/compilation_cache.cc`/ResolvePaddingShapes(469ea45c3d49e868).
  CompilationCache.AddStaticCacheEntry: torch_tpu/CompilationCache#AddStaticCacheEntry(477734b1e66557d).
  CompilationCache.SetOptions: torch_tpu/CompilationCache#SetOptions(24fc8f0a1625d4b2).
  CompilationCache.Restart: torch_tpu/CompilationCache#Restart(49f6e7a06ebc5aa8).
  CompilationCache.SetAllowCacheMode: torch_tpu/CompilationCache#SetAllowCacheMode(b45ddcbc8423892c).
  CompilationCache.GetDumpOnCacheMissMode: torch_tpu/CompilationCache#GetDumpOnCacheMissMode(50ce9a9e25b4a850).
  CompilationCache.SetDumpOnCacheMissMode: torch_tpu/CompilationCache#SetDumpOnCacheMissMode(b45ddcbc8423892c).
  CompilationCache.IsInitialized: torch_tpu/CompilationCache#IsInitialized(50ce9a9e25b4a850).
  GetNumCompilationThreads: torch_tpu/GetNumCompilationThreads(7864480464b09eea).
  CompilationCache.HbmUsageSummary: torch_tpu/CompilationCache#HbmUsageSummary(219584694fe2b248).
  CompilationCache.FindStaticCacheEntryOrNull: torch_tpu/CompilationCache#FindStaticCacheEntryOrNull(d8f16b2b31b13b95).
  CompilationCache.IsExecutableReady: torch_tpu/CompilationCache#IsExecutableReady(dd37816d3ba63f25).
  TrySetExecutablePromise: torch_tpu/TrySetExecutablePromise(88938c24c1a47d79).
  CompilationCache.ShouldUseTier2Cache: torch_tpu/CompilationCache#ShouldUseTier2Cache(50ce9a9e25b4a850).
  CompilationCache.-CompilationCache: torch_tpu/CompilationCache#`~CompilationCache`(ced63f7c635d850d).
  CompilationCache.GetCacheRequests: torch_tpu/CompilationCache#GetCacheRequests(57a65ae535d7db84).
  CompilationCache.SetCacheOnlyMode: torch_tpu/CompilationCache#SetCacheOnlyMode(b45ddcbc8423892c).
  CompilationCache.GetBoundedDynamicCacheEntries: torch_tpu/CompilationCache#GetBoundedDynamicCacheEntries(95877c4a8d9f64c3).
  CompilationCache.CompilationCache: torch_tpu/CompilationCache#CompilationCache(49f6e7a06ebc5aa8).
  CompilationCache.GetInstanceNoLock: torch_tpu/CompilationCache#GetInstanceNoLock(169592da9e7df2e0).
  IsFutureReady: torch_tpu/`$anonymous_namespace_csrc/common/compilation_cache.cc`/IsFutureReady(5b84273db97dd7ed).
  GetNumProcs: torch_tpu/`$anonymous_namespace_csrc/common/compilation_cache.cc`/GetNumProcs(b126dc7c1de90089).
  GetNumCpus: torch_tpu/`$anonymous_namespace_csrc/common/compilation_cache.cc`/GetNumCpus(b126dc7c1de90089).
  FLAGS_help_storage_torch_tpu_internal_num_compilation_threads: FLAGS_help_storage_torch_tpu_internal_num_compilation_threads.
  AbslFlagDefaultGenFortorch_tpu_internal_num_compilation_threads: AbslFlagDefaultGenFortorch_tpu_internal_num_compilation_threads#
  AbslFlagDefaultGenFortorch_tpu_internal_num_compilation_threads.value: AbslFlagDefaultGenFortorch_tpu_internal_num_compilation_threads#value.
  AbslFlagHelpGenFortorch_tpu_internal_num_compilation_threads: AbslFlagHelpGenFortorch_tpu_internal_num_compilation_threads#
  AbslFlagHelpGenFortorch_tpu_internal_num_compilation_threads.Value: AbslFlagHelpGenFortorch_tpu_internal_num_compilation_threads#Value(59d317b252f70f25).
  FLAGS_notorch_tpu_internal_num_compilation_threads: FLAGS_notorch_tpu_internal_num_compilation_threads.
  AbslFlagDefaultGenFortorch_tpu_internal_num_compilation_threads.Gen: AbslFlagDefaultGenFortorch_tpu_internal_num_compilation_threads#Gen(5d22bdacc48458e8).
  AbslFlagHelpGenFortorch_tpu_internal_num_compilation_threads.NonConst: AbslFlagHelpGenFortorch_tpu_internal_num_compilation_threads#NonConst(efd28698952f529a).
---
# Module: [`csrc/common/compilation_cache.cc`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc)

## Classes
### <a id="AbslFlagDefaultGenFortorch_tpu_internal_num_compilation_threads"></a>`AbslFlagDefaultGenFortorch_tpu_internal_num_compilation_threads`
- def: [`csrc/common/compilation_cache.cc:82`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L82)
- signature: `ABSL_FLAG(int32_t, torch_tpu_internal_num_compilation_threads, 0, "The number of threads to use for compilation. If 0, use the default " "number of threads based on the number of logical CPUs.")`
- members:
  - <a id="AbslFlagDefaultGenFortorch_tpu_internal_num_compilation_threads.Gen"></a>`Gen(int32_t, torch_tpu_internal_num_compilation_threads, 0, "The number of threads to use for compilation. If 0, use the default " "number of threads based on the number of logical CPUs.")` — [`L82`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L82)
  - <a id="AbslFlagDefaultGenFortorch_tpu_internal_num_compilation_threads.value"></a>`value` — [`L82`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L82)
- used by: [`FLAGS_torch_tpu_internal_num_compilation_threads`](compilation_thread_num_test.cc.md#FLAGS_torch_tpu_internal_num_compilation_threads)

### <a id="AbslFlagHelpGenFortorch_tpu_internal_num_compilation_threads"></a>`AbslFlagHelpGenFortorch_tpu_internal_num_compilation_threads`
- def: [`csrc/common/compilation_cache.cc:82`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L82)
- signature: `ABSL_FLAG(int32_t, torch_tpu_internal_num_compilation_threads, 0, "The number of threads to use for compilation. If 0, use the default " "number of threads based on the number of logical CPUs.")`
- members:
  - <a id="AbslFlagHelpGenFortorch_tpu_internal_num_compilation_threads.NonConst"></a>`NonConst(int32_t, torch_tpu_internal_num_compilation_threads, 0, "The number of threads to use for compilation. If 0, use the default " "number of threads based on the number of logical CPUs.")` — [`L82`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L82)
  - <a id="AbslFlagHelpGenFortorch_tpu_internal_num_compilation_threads.Value"></a>`Value(int32_t, torch_tpu_internal_num_compilation_threads, 0, "The number of threads to use for compilation. If 0, use the default " "number of threads based on the number of logical CPUs.")` — [`L82`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L82) — long enough for NonConst to work correctly.
- used by: [`FLAGS_torch_tpu_internal_num_compilation_threads`](compilation_thread_num_test.cc.md#FLAGS_torch_tpu_internal_num_compilation_threads)

## Functions
- <a id="AnyInducesLayoutChange"></a>`AnyInducesLayoutChange(const std::vector<Shape>& input_shapes, const std::vector<Shape>& output_shapes, xla::PjRtClient* client)` — [`L708`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L708) — Returns true if the default layout is different between any input / output
- `AnyInducesLayoutChange(const std::vector<Shape>& input_shapes, const std::vector<Shape>& output_shapes, xla::PjRtClient* client)` — [`L708`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L708) — Returns true if the default layout is different between any input / output
- `GetNumCompilationThreads()` — [`L158`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L158) — Returns the number of threads to use for compilation based on the flag value,
- <a id="GetNumCompilationThreads"></a>`GetNumCompilationThreads(const int num_procs)` — [`L114`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L114) — Returns the number of threads to use for compilation.
- <a id="GetNumCpus"></a>`GetNumCpus()` — [`L106`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L106)
- <a id="GetNumProcs"></a>`GetNumProcs()` — [`L98`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L98) — Returns the value of the NPROC environment variable (a positive integer), or
- <a id="IsFutureReady"></a>`IsFutureReady(const SharedLoadedExecutableWithMetadataFuture& future)` — [`L91`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L91) — Returns true if the future is ready.
- `ResolvePaddingShapes(const ShapeDynamismMetadata& shape_dynamism_metadata, const std::vector<Shape>& input_shapes, std::vector<Shape>& static_runtime_input_shapes, std::vector<Shape>& static_padded_input_shapes, std::vector<Shape>& input_shapes_with_updated_dynamism)` — [`L740`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L740) — Resolves runtime dynamic input shapes, static padded input shapes and updated
- <a id="ResolvePaddingShapes"></a>`ResolvePaddingShapes(const ShapeDynamismMetadata& shape_dynamism_metadata, const std::vector<Shape>& input_shapes, std::vector<Shape>& static_runtime_input_shapes, std::vector<Shape>& static_padded_input_shapes, std::vector<Shape>& input_shapes_with_updated_dynamism)` — [`L740`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L740) — Resolves runtime dynamic input shapes, static padded input shapes and updated
- <a id="TrySetExecutablePromise"></a>`TrySetExecutablePromise(const CompilationCacheKey& key, LoadedExecutablePromise& promise, const absl::StatusOr<SharedLoadedExecutableWithMetadata>& executable)` — [`L255`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L255) — Sets the executable promise for the given key. If the promise is already

## Module values
- <a id="FLAGS_help_storage_torch_tpu_internal_num_compilation_threads"></a>`FLAGS_help_storage_torch_tpu_internal_num_compilation_threads` — [`L82`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L82)
- <a id="FLAGS_notorch_tpu_internal_num_compilation_threads"></a>`FLAGS_notorch_tpu_internal_num_compilation_threads` — [`L82`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L82)

## Other members
- `CreatePaddingKernel` — [`L776`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L776)
- `GetBoundedDynamicCacheEntries` — [`L474`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L474)
- `GetOrCompile` — [`L1004`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L1004)
- `EnqueueCompilation` — [`L1026`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L1026)
- `GetOrCompile` — [`L1004`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L1004)
- `GetFromTier2OrCompile` — [`L1127`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L1127)
- `AddBoundedDynamicCacheEntry` — [`L535`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L535)
- `CreateSlicingKernel` — [`L805`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L805)
- `GetInstanceNoLock` — [`L209`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L209)
- `GetOrCompileImpl` — [`L920`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L920)
- `AddUnboundedDynamicCacheEntry` — [`L568`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L568)
- `CreateDynamicKernelAdapter` — [`L870`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L870)
- `GetOrCreateCacheEntry` — [`L607`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L607)
- `GetFromTier3OrCompile` — [`L1180`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L1180)
- `GetOrCompile` — [`L1015`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L1015)
- `Compile` — [`L1316`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L1316)
- <a id="CompilationCache.-CompilationCache"></a>`CompilationCache.-CompilationCache` — [`L197`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L197)
- <a id="CompilationCache.AddBoundedDynamicCacheEntry"></a>`CompilationCache.AddBoundedDynamicCacheEntry` — [`L535`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L535) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="CompilationCache.AddStaticCacheEntry"></a>`CompilationCache.AddStaticCacheEntry` — [`L522`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L522) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="CompilationCache.AddUnboundedDynamicCacheEntry"></a>`CompilationCache.AddUnboundedDynamicCacheEntry` — [`L568`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L568) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="CompilationCache.CompilationCache"></a>`CompilationCache.CompilationCache` — [`L195`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L195)
- <a id="CompilationCache.Compile"></a>`CompilationCache.Compile` — [`L1316`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L1316) — documented in [compilation-pipeline](../../../concepts/compilation-pipeline.md)
- <a id="CompilationCache.CreateDynamicKernelAdapter"></a>`CompilationCache.CreateDynamicKernelAdapter` — [`L870`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L870) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="CompilationCache.CreatePaddingKernel"></a>`CompilationCache.CreatePaddingKernel` — [`L776`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L776) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="CompilationCache.CreateSlicingKernel"></a>`CompilationCache.CreateSlicingKernel` — [`L805`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L805) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="CompilationCache.EnqueueCompilation"></a>`CompilationCache.EnqueueCompilation` — [`L1026`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L1026) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="CompilationCache.EnsureInitialized"></a>`CompilationCache.EnsureInitialized` — [`L162`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L162) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="CompilationCache.EvictAll"></a>`CompilationCache.EvictAll` — [`L280`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L280) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="CompilationCache.FindCacheEntryOrNull"></a>`CompilationCache.FindCacheEntryOrNull` — [`L441`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L441)
- <a id="CompilationCache.FindStaticCacheEntryOrNull"></a>`CompilationCache.FindStaticCacheEntryOrNull` — [`L419`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L419)
- <a id="CompilationCache.FindUnboundedDynamicCacheEntryOrNull"></a>`CompilationCache.FindUnboundedDynamicCacheEntryOrNull` — [`L426`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L426)
- <a id="CompilationCache.GetBoundedDynamicCacheEntries"></a>`CompilationCache.GetBoundedDynamicCacheEntries` — [`L474`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L474)
- <a id="CompilationCache.GetCacheHits"></a>`CompilationCache.GetCacheHits` — [`L387`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L387)
- <a id="CompilationCache.GetCacheMisses"></a>`CompilationCache.GetCacheMisses` — [`L392`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L392)
- <a id="CompilationCache.GetCacheRequests"></a>`CompilationCache.GetCacheRequests` — [`L382`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L382)
- <a id="CompilationCache.GetCacheStats"></a>`CompilationCache.GetCacheStats` — [`L397`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L397)
- <a id="CompilationCache.GetDumpOnCacheMissMode"></a>`CompilationCache.GetDumpOnCacheMissMode` — [`L377`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L377) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="CompilationCache.GetFromTier2OrCompile"></a>`CompilationCache.GetFromTier2OrCompile` — [`L1127`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L1127) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="CompilationCache.GetFromTier3OrCompile"></a>`CompilationCache.GetFromTier3OrCompile` — [`L1180`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L1180) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="CompilationCache.GetInstance"></a>`CompilationCache.GetInstance` — [`L216`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L216)
- <a id="CompilationCache.GetInstanceNoLock"></a>`CompilationCache.GetInstanceNoLock` — [`L209`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L209)
- <a id="CompilationCache.GetOrCompile"></a>`CompilationCache.GetOrCompile` — [`L1015`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L1015) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="CompilationCache.GetOrCompileImpl"></a>`CompilationCache.GetOrCompileImpl` — [`L920`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L920) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="CompilationCache.GetOrCreateCacheEntry"></a>`CompilationCache.GetOrCreateCacheEntry` — [`L607`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L607) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="CompilationCache.GetStaticCacheEntry"></a>`CompilationCache.GetStaticCacheEntry` — [`L455`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L455)
- <a id="CompilationCache.GetUnboundedDynamicCacheEntry"></a>`CompilationCache.GetUnboundedDynamicCacheEntry` — [`L483`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L483)
- <a id="CompilationCache.HbmUsageSummary"></a>`CompilationCache.HbmUsageSummary` — [`L1346`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L1346) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="CompilationCache.IsExecutableReady"></a>`CompilationCache.IsExecutableReady` — [`L693`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L693) — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="CompilationCache.IsInitialized"></a>`CompilationCache.IsInitialized` — [`L240`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L240)
- <a id="CompilationCache.Restart"></a>`CompilationCache.Restart` — [`L233`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L233)
- <a id="CompilationCache.SetAllowCacheMode"></a>`CompilationCache.SetAllowCacheMode` — [`L359`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L359)
- <a id="CompilationCache.SetCacheOnlyMode"></a>`CompilationCache.SetCacheOnlyMode` — [`L365`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L365)
- <a id="CompilationCache.SetDumpOnCacheMissMode"></a>`CompilationCache.SetDumpOnCacheMissMode` — [`L371`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L371)
- <a id="CompilationCache.SetExecutable"></a>`CompilationCache.SetExecutable` — [`L1056`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L1056)
- <a id="CompilationCache.SetOptions"></a>`CompilationCache.SetOptions` — [`L245`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L245)
- <a id="CompilationCache.ShouldUseTier2Cache"></a>`CompilationCache.ShouldUseTier2Cache` — [`L1118`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L1118)
- <a id="CompilationCache.ShutDown"></a>`CompilationCache.ShutDown` — [`L224`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L224)
- <a id="CompilationCache.cache_instance_mutex_"></a>`CompilationCache.cache_instance_mutex_` — [`L206`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache.cc#L206)

