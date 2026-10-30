---
title: 'Module: csrc/common/compilation_cache_utils.cc'
type: catalog
provenance: extracted
module: csrc/common/compilation_cache_utils.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtomicWriteToCacheFile: AtomicWriteToCacheFile(6c5d665b525200aa).
  operator: '`operator<<`(3c908a83df6cf216).'
  LoadSerializedExecutable: LoadSerializedExecutable(1129cd44f0411d7f).
  GetTorchTpuBinaryFingerprint: GetTorchTpuBinaryFingerprint(f708dce9a8856c70).
  GetPjRtVersion: GetPjRtVersion(efd28698952f529a).
  GetTier3CacheRootDir: GetTier3CacheRootDir(319d84e01067f75d).
  EnsureDirExistsRecursively: EnsureDirExistsRecursively(9a836fbe81584ab8).
  kTorchTpuBinaryVersion: kTorchTpuBinaryVersion.
---
# Module: [`csrc/common/compilation_cache_utils.cc`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_utils.cc)

## Functions
- <a id="AtomicWriteToCacheFile"></a>`AtomicWriteToCacheFile(const std::string& cache_entry_path, const std::string& serialized_data)` — [`L129`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_utils.cc#L129)
- `AtomicWriteToCacheFile(const std::string& cache_entry_path, const SharedLoadedExecutableWithMetadata& executable)` — [`L195`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_utils.cc#L195) — Writes a compiled executable to the given tier-2 or tier-3 cache file. This
- <a id="EnsureDirExistsRecursively"></a>`EnsureDirExistsRecursively(const std::string& path)` — [`L208`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_utils.cc#L208) — Creates the directory recursively as needed, and sets the permissions to
- <a id="GetPjRtVersion"></a>`GetPjRtVersion()` — [`L71`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_utils.cc#L71) — Returns the PjRt version string.
- <a id="GetTier3CacheRootDir"></a>`GetTier3CacheRootDir()` — [`L213`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_utils.cc#L213) — Returns the root directory of the tier-3 compilation cache, as set by the
- <a id="GetTorchTpuBinaryFingerprint"></a>`GetTorchTpuBinaryFingerprint()` — [`L91`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_utils.cc#L91) — Returns the fingerprint of the TorchTPU binary version. The intent is to — documented in [compilation-cache](../../../concepts/compilation-cache.md)
- <a id="LoadSerializedExecutable"></a>`LoadSerializedExecutable(CacheTier tier, const CompilationCacheKey& key, const std::string_view data)` — [`L109`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_utils.cc#L109) — Loads a serialized executable read from the given cache.
- <a id="operator"></a>`operator<<(std::ostream& os, const CacheTier tier)` — [`L55`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_utils.cc#L55) — Formats a cache tier as a human-readable string.

## Module values
- <a id="kTorchTpuBinaryVersion"></a>`kTorchTpuBinaryVersion` — [`L53`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_utils.cc#L53) — Remember to increment this whenever TorchTPU's behavior changes enough to

