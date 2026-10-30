---
title: 'Module: csrc/common/tier2_compilation_cache.h'
type: catalog
provenance: extracted
module: csrc/common/tier2_compilation_cache.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  Tier2CacheEntryLock: Tier2CacheEntryLock#
  Tier2CacheEntryStats.write_duration: Tier2CacheEntryStats#write_duration.
  Tier2CacheEntryStats: Tier2CacheEntryStats#
  Tier2CacheEntryLock.operator: Tier2CacheEntryLock#`operator=`(e28d2e87ae87917a).
  Tier2CacheEntryLock.key_: Tier2CacheEntryLock#key_.
  Tier2CacheEntryLock.lock_fd_: Tier2CacheEntryLock#lock_fd_.
  Tier2CacheEntryStats.last_read: Tier2CacheEntryStats#last_read.
  Tier2CacheEntryStats.pre_read_duration: Tier2CacheEntryStats#pre_read_duration.
  Tier2CacheEntryStats.read_duration: Tier2CacheEntryStats#read_duration.
  Tier2CacheEntryStats.pre_compile_duration: Tier2CacheEntryStats#pre_compile_duration.
  Tier2CacheEntryLock.Tier2CacheEntryLock: Tier2CacheEntryLock#Tier2CacheEntryLock(f5e8870748b1fca3).
---
# Module: [`csrc/common/tier2_compilation_cache.h`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.h)

## Classes
### <a id="Tier2CacheEntryLock"></a>`Tier2CacheEntryLock`
- def: [`csrc/common/tier2_compilation_cache.h:81`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.h#L81)
- doc: RAII class for locking and unlocking a tier-2 cache entry.
- signature: `class Tier2CacheEntryLock`
- members:
  - <a id="Tier2CacheEntryLock.Tier2CacheEntryLock"></a>`Tier2CacheEntryLock(Tier2CacheEntryLock&&)` — [`L92`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.h#L92)
  - `Tier2CacheEntryLock(const Tier2CacheEntryLock&)` — [`L90`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.h#L90) — Not copyable or movable.
  - <a id="Tier2CacheEntryLock.operator"></a>`operator=(Tier2CacheEntryLock&&)` — [`L93`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.h#L93)
  - `operator=(const Tier2CacheEntryLock&)` — [`L91`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.h#L91)
  - <a id="Tier2CacheEntryLock.key_"></a>`key_` — [`L99`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.h#L99)
  - <a id="Tier2CacheEntryLock.lock_fd_"></a>`lock_fd_` — [`L100`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.h#L100) — Descriptor of the lock file.
- uses (calls/refs, reference-scoped): [`CompilationCacheKey`](cache_key.h.md#CompilationCacheKey), [`Tier2CacheEntryLock`](tier2_compilation_cache.cc.md#Tier2CacheEntryLock.Tier2CacheEntryLock), [`Release`](tier2_compilation_cache.cc.md#Tier2CacheEntryLock.Release), [`UniqueFileDescriptor`](unique_file_descriptor.h.md#UniqueFileDescriptor), [`~Tier2CacheEntryLock`](tier2_compilation_cache.cc.md#Tier2CacheEntryLock.-Tier2CacheEntryLock)
- used by: [`UnboundedDynamicCache`](compilation_cache.h.md#CompilationCache.UnboundedDynamicCache), [`GetFromTier3OrCompile`](compilation_cache.cc.md#CompilationCache.GetFromTier3OrCompile), [`GetFromTier2OrCompile`](compilation_cache.cc.md#CompilationCache.GetFromTier2OrCompile), [`Tier2CacheEntryLock`](tier2_compilation_cache.cc.md#Tier2CacheEntryLock.Tier2CacheEntryLock), [`TestBody`](tier2_compilation_cache_test.cc.md#Tier2CacheEntryLockTest_DoesNotCreateLockFileIfItExists_Test.TestBody), [`TestBody`](tier2_compilation_cache_test.cc.md#Tier2CacheTest_GetFromTier2CacheFailsIfCacheFileIsInvalid_Test.TestBody), [`TestBody`](tier2_compilation_cache_test.cc.md#Tier2CacheTest_WriteToCacheEntryIfDoesNotExist_Test.TestBody), [`TestBody`](tier2_compilation_cache_test.cc.md#Tier2CacheTest_WriteToCacheEntryIfExists_Test.TestBody), [`TestBody`](tier2_compilation_cache_test.cc.md#Tier2CacheEntryLockTest_CreatesLockFileIfNeeded_Test.TestBody), [`Release`](tier2_compilation_cache.cc.md#Tier2CacheEntryLock.Release), [`TestBody`](tier2_compilation_cache_test.cc.md#Tier2CacheEntryLockTest_OnlyOneUserCanHoldLockAtATime_Test.TestBody), [`EnsureTier2CacheDirExistsOnceOrDie`](tier2_compilation_cache.cc.md#EnsureTier2CacheDirExistsOnceOrDie), [`~Tier2CacheEntryLock`](tier2_compilation_cache.cc.md#Tier2CacheEntryLock.-Tier2CacheEntryLock)

### <a id="Tier2CacheEntryStats"></a>`Tier2CacheEntryStats`
- def: [`csrc/common/tier2_compilation_cache.h:46`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.h#L46)
- doc: Statistics for a tier-2 cache entry.
- signature: `struct Tier2CacheEntryStats`
- members:
  - <a id="Tier2CacheEntryStats.last_read"></a>`last_read` — [`L48`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.h#L48) — When the entry's cache file was last read.
  - <a id="Tier2CacheEntryStats.pre_compile_duration"></a>`pre_compile_duration` — [`L63`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.h#L63) — These two fields are set only when the entry is compiled and written to the
  - <a id="Tier2CacheEntryStats.pre_read_duration"></a>`pre_read_duration` — [`L54`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.h#L54) — These two fields are set only when the entry is read from the tier-2 cache
  - <a id="Tier2CacheEntryStats.read_duration"></a>`read_duration` — [`L57`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.h#L57) — How long it took to read the entry, deserialize it, and load it into a
  - <a id="Tier2CacheEntryStats.write_duration"></a>`write_duration` — [`L65`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.h#L65) — How long it took to serialize and write the executable to the tier-2 cache.
- uses (calls/refs, reference-scoped): [`CompilationCacheKey`](cache_key.h.md#CompilationCacheKey), [`SharedLoadedExecutableWithMetadata`](compilation.h.md#SharedLoadedExecutableWithMetadata), [`GetFromTier2Cache`](tier2_compilation_cache.cc.md#GetFromTier2Cache), [`GetTier2CacheEntryPath`](tier2_compilation_cache.cc.md#GetTier2CacheEntryPath)
- used by: [`GetFromTier3OrCompile`](compilation_cache.cc.md#CompilationCache.GetFromTier3OrCompile), [`GetFromTier2Cache`](tier2_compilation_cache.cc.md#GetFromTier2Cache), [`GetFromTier2OrCompile`](compilation_cache.cc.md#CompilationCache.GetFromTier2OrCompile), [`TestBody`](tier2_compilation_cache_test.cc.md#Tier2CacheTest_GetFromTier2CacheFailsIfCacheFileIsInvalid_Test.TestBody), [`TestBody`](tier2_compilation_cache_test.cc.md#Tier2CacheTest_GetFromTier2CacheFailsIfCacheFileDoesNotExist_Test.TestBody), [`read_count`](compilation_cache.h.md#CacheEntryStats.read_count)

