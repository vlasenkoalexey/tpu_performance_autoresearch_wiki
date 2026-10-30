---
title: 'Module: csrc/common/tier2_compilation_cache.cc'
type: catalog
provenance: extracted
module: csrc/common/tier2_compilation_cache.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  GetTier2CacheName: GetTier2CacheName(319d84e01067f75d).
  GetFromTier2Cache: GetFromTier2Cache(99d0c598dc16c4bd).
  MappedCacheEntry.Make: MappedCacheEntry#Make(3e4d8a2dbb77c668).
  GetTier2CacheEntryPath: GetTier2CacheEntryPath(a8c30bde81a0886f).
  Tier2CacheEntryLock.Tier2CacheEntryLock: Tier2CacheEntryLock#Tier2CacheEntryLock(b7e65586482a538d).
  GetTier2CompilationCachePath: GetTier2CompilationCachePath(319d84e01067f75d).
  Tier2CacheEntryLock.Release: Tier2CacheEntryLock#Release(49f6e7a06ebc5aa8).
  UsesTier2CompilationCache: UsesTier2CompilationCache(c9857a73d68e59ba).
  MappedCacheEntry: MappedCacheEntry#
  GetTier2CacheEntryLockPath: GetTier2CacheEntryLockPath(a8c30bde81a0886f).
  MappedCacheEntry.MappedCacheEntry: MappedCacheEntry#MappedCacheEntry(43fd52d4bde6eedc).
  EnsureTier2CacheDirExistsOnceOrDie: EnsureTier2CacheDirExistsOnceOrDie(49f6e7a06ebc5aa8).
  MappedCacheEntry.last_read_: MappedCacheEntry#last_read_.
  MappedCacheEntry.size_: MappedCacheEntry#size_.
  MappedCacheEntry.data: MappedCacheEntry#data(28b48b7ac385737).
  MappedCacheEntry.data_: MappedCacheEntry#data_.
  Tier2CacheEntryLock.-Tier2CacheEntryLock: Tier2CacheEntryLock#`~Tier2CacheEntryLock`(ced63f7c635d850d).
  MappedCacheEntry.-MappedCacheEntry: MappedCacheEntry#`~MappedCacheEntry`(ced63f7c635d850d).
  kDefaultCacheName: kDefaultCacheName.
  MappedCacheEntry.last_read: MappedCacheEntry#last_read(354017ff1333e0fe).
  MappedCacheEntry.operator: MappedCacheEntry#`operator=`(66ab13e2b9032883).
  kTier2CacheFileExtension: kTier2CacheFileExtension.
  kLockFileExtension: kLockFileExtension.
  kTier2CacheRootDir: kTier2CacheRootDir.
  kDisabledCacheNameInEnvVar: kDisabledCacheNameInEnvVar.
---
# Module: [`csrc/common/tier2_compilation_cache.cc`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc)

## Classes
### <a id="MappedCacheEntry"></a>`MappedCacheEntry`
- def: [`csrc/common/tier2_compilation_cache.cc:128`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L128)
- doc: RAII class for mapping a cache file into memory.
- signature: `class MappedCacheEntry`
- members:
  - <a id="MappedCacheEntry.Make"></a>`Make(const CompilationCacheKey& key)` — [`L134`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L134) — Creates a MappedCacheEntry for the given key.
  - `MappedCacheEntry(const MappedCacheEntry&)` — [`L172`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L172) — The class is movable but not copyable.
  - <a id="MappedCacheEntry.MappedCacheEntry"></a>`MappedCacheEntry(MappedCacheEntry&& other)` — [`L174`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L174)
  - `MappedCacheEntry(const char* const data, const size_t size, const absl::Time last_read)` — [`L192`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L192) — Creates a MappedCacheEntry with the given information.
  - <a id="MappedCacheEntry.data"></a>`data()` — [`L183`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L183) — Returns the mapped data, or an empty string_view if mapping failed.
  - <a id="MappedCacheEntry.last_read"></a>`last_read()` — [`L188`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L188) — Returns the last read time of the cache file.
  - <a id="MappedCacheEntry.operator"></a>`operator=(const MappedCacheEntry&)` — [`L173`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L173)
  - `operator=(MappedCacheEntry&& other)` — [`L180`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L180) — We have no need for move assignment for now.
  - <a id="MappedCacheEntry.-MappedCacheEntry"></a>`~MappedCacheEntry()` — [`L165`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L165) — Unmaps the cache file from memory.
  - <a id="MappedCacheEntry.data_"></a>`data_` — [`L196`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L196)
  - <a id="MappedCacheEntry.last_read_"></a>`last_read_` — [`L198`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L198)
  - <a id="MappedCacheEntry.size_"></a>`size_` — [`L197`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L197)
- uses (calls/refs, reference-scoped): [`NormalizeIfInsideBuildDirectory`](macro_utils.cc.md#NormalizeIfInsideBuildDirectory), [`MaybeAddCppSourceLoc`](status_builder.cc.md#MaybeAddCppSourceLoc), [`GetRootOpName`](../ops/python_context.cc.md#GetRootOpName), [`SetRootOpNamePayload`](status_builder.cc.md#SetRootOpNamePayload), [`StatusBuilder`](status_builder.h.md#StatusBuilder), [`operator<<`](status_builder.h.md#StatusBuilder.operator), [`operator<<`](../ops/op_names.h.md#operator), [`operator<<`](status_builder.h.md#operator), [`operator<<`](status_builder.h.md#operator), [`operator<<`](cache_key.cc.md#operator), [`StatusBuilder`](status_builder.cc.md#StatusBuilder.StatusBuilder), [`kInternal`](error_utils.h.md#kInternal), [`CompilationCacheKey`](cache_key.h.md#CompilationCacheKey), [`operator<<`](compilation_cache_utils.cc.md#operator), [`SharedLoadedExecutableWithMetadata`](compilation.h.md#SharedLoadedExecutableWithMetadata), [`GetTier2CacheEntryPath`](tier2_compilation_cache.cc.md#GetTier2CacheEntryPath), [`kNotFound`](error_utils.h.md#kNotFound), [`UniqueFileDescriptor`](unique_file_descriptor.h.md#UniqueFileDescriptor), [`valid`](unique_file_descriptor.h.md#UniqueFileDescriptor.valid), [`UniqueFileDescriptor`](unique_file_descriptor.h.md#UniqueFileDescriptor.UniqueFileDescriptor), [`get`](unique_file_descriptor.h.md#UniqueFileDescriptor.get)
- used by: [`GetFromTier2Cache`](tier2_compilation_cache.cc.md#GetFromTier2Cache)

## Functions
- <a id="EnsureTier2CacheDirExistsOnceOrDie"></a>`EnsureTier2CacheDirExistsOnceOrDie()` — [`L237`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L237) — Ensures that the tier-2 cache directory exists. This function only does
- <a id="GetFromTier2Cache"></a>`GetFromTier2Cache(const CompilationCacheKey& key, absl::Time request_start, Tier2CacheEntryStats& stats)` — [`L201`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L201) — Fetches a compiled executable from the tier-2 cache, where `request_start`
- <a id="GetTier2CacheEntryLockPath"></a>`GetTier2CacheEntryLockPath(const CompilationCacheKey& key)` — [`L229`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L229) — Returns the path to the lock file for the given key.
- <a id="GetTier2CacheEntryPath"></a>`GetTier2CacheEntryPath(const CompilationCacheKey& key)` — [`L119`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L119) — Returns the path to the tier-2 cache file for the given key.
- <a id="GetTier2CacheName"></a>`GetTier2CacheName()` — [`L64`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L64) — Returns the name of the tier-2 compilation cache as set by the
- <a id="GetTier2CompilationCachePath"></a>`GetTier2CompilationCachePath()` — [`L108`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L108) — Returns the path to the tier-2 compilation cache directory for this process.
- <a id="UsesTier2CompilationCache"></a>`UsesTier2CompilationCache()` — [`L106`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L106) — Returns true if the tier-2 compilation cache is enabled for this process.

## Module values
- <a id="kDefaultCacheName"></a>`kDefaultCacheName` — [`L62`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L62) — The default name of the tier-2 compilation cache, used when:
- <a id="kDisabledCacheNameInEnvVar"></a>`kDisabledCacheNameInEnvVar` — [`L56`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L56) — The value of the TORCH_TPU_TIER2_COMPILATION_CACHE environment variable that
- <a id="kLockFileExtension"></a>`kLockFileExtension` — [`L51`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L51)
- <a id="kTier2CacheFileExtension"></a>`kTier2CacheFileExtension` — [`L52`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L52)
- <a id="kTier2CacheRootDir"></a>`kTier2CacheRootDir` — [`L50`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L50)

## Other members
- <a id="Tier2CacheEntryLock.-Tier2CacheEntryLock"></a>`Tier2CacheEntryLock.-Tier2CacheEntryLock` — [`L276`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L276)
- <a id="Tier2CacheEntryLock.Release"></a>`Tier2CacheEntryLock.Release` — [`L278`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L278)
- <a id="Tier2CacheEntryLock.Tier2CacheEntryLock"></a>`Tier2CacheEntryLock.Tier2CacheEntryLock` — [`L249`](../../../../../../raw/code/torch_tpu/csrc/common/tier2_compilation_cache.cc#L249)

