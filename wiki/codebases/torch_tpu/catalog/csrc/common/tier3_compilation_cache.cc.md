---
title: 'Module: csrc/common/tier3_compilation_cache.cc'
type: catalog
provenance: extracted
module: csrc/common/tier3_compilation_cache.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  GetFromTier3Cache: GetFromTier3Cache(9fc7cd604995f81e).
  GetTier3CacheEntryPath: GetTier3CacheEntryPath(a8c30bde81a0886f).
  UsesTier3CompilationCache: UsesTier3CompilationCache(c9857a73d68e59ba).
  UsesLocalBackupTaskForTier3Read: UsesLocalBackupTaskForTier3Read(c9857a73d68e59ba).
  GetTier3CompilationCachePath: GetTier3CompilationCachePath(319d84e01067f75d).
  EnsureTier3CacheDirExistsOnceOrDie: EnsureTier3CacheDirExistsOnceOrDie(49f6e7a06ebc5aa8).
  kTier3CacheFileExtension: kTier3CacheFileExtension.
---
# Module: [`csrc/common/tier3_compilation_cache.cc`](../../../../../../raw/code/torch_tpu/csrc/common/tier3_compilation_cache.cc)

## Functions
- <a id="EnsureTier3CacheDirExistsOnceOrDie"></a>`EnsureTier3CacheDirExistsOnceOrDie()` — [`L93`](../../../../../../raw/code/torch_tpu/csrc/common/tier3_compilation_cache.cc#L93) — Ensures that the tier-3 cache directory exists. This function only does
- <a id="GetFromTier3Cache"></a>`GetFromTier3Cache(const CompilationCacheKey& key)` — [`L111`](../../../../../../raw/code/torch_tpu/csrc/common/tier3_compilation_cache.cc#L111) — Tries to get a loaded executable from the tier-3 compilation cache.
- <a id="GetTier3CacheEntryPath"></a>`GetTier3CacheEntryPath(const CompilationCacheKey& key)` — [`L105`](../../../../../../raw/code/torch_tpu/csrc/common/tier3_compilation_cache.cc#L105) — Returns the path to the tier-3 cache file for the given key.
- <a id="GetTier3CompilationCachePath"></a>`GetTier3CompilationCachePath()` — [`L77`](../../../../../../raw/code/torch_tpu/csrc/common/tier3_compilation_cache.cc#L77) — Returns the path to the tier-3 compilation cache directory for the current
- <a id="UsesLocalBackupTaskForTier3Read"></a>`UsesLocalBackupTaskForTier3Read()` — [`L47`](../../../../../../raw/code/torch_tpu/csrc/common/tier3_compilation_cache.cc#L47) — Returns true if a local compilation backup task should be scheduled in
- <a id="UsesTier3CompilationCache"></a>`UsesTier3CompilationCache()` — [`L40`](../../../../../../raw/code/torch_tpu/csrc/common/tier3_compilation_cache.cc#L40) — Returns true if the tier-3 compilation cache is enabled for this process.

## Module values
- <a id="kTier3CacheFileExtension"></a>`kTier3CacheFileExtension` — [`L38`](../../../../../../raw/code/torch_tpu/csrc/common/tier3_compilation_cache.cc#L38)

