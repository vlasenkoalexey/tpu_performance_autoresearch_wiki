---
title: 'Module: csrc/common/compilation_cache_utils.h'
type: catalog
provenance: extracted
module: csrc/common/compilation_cache_utils.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AbslStringify: AbslStringify(318473c075769085).
  CacheTier: CacheTier#
  CacheTier.kTier3: CacheTier#kTier3.
  CacheTier.kTier1: CacheTier#kTier1.
  CacheTier.kUnknown: CacheTier#kUnknown.
  CacheTier.kTier2: CacheTier#kTier2.
---
# Module: [`csrc/common/compilation_cache_utils.h`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_utils.h)

## Classes
### <a id="CacheTier"></a>`CacheTier`
- def: [`csrc/common/compilation_cache_utils.h:34`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_utils.h#L34)
- doc: The tier of the cache where an executable comes from.
- signature: `enum class CacheTier`
- members:
  - <a id="CacheTier.kTier1"></a>`kTier1` — [`L36`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_utils.h#L36)
  - <a id="CacheTier.kTier2"></a>`kTier2` — [`L37`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_utils.h#L37)
  - <a id="CacheTier.kTier3"></a>`kTier3` — [`L38`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_utils.h#L38)
  - <a id="CacheTier.kUnknown"></a>`kUnknown` — [`L35`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_utils.h#L35)
- uses (calls/refs, reference-scoped): [`operator<<`](compilation_cache_utils.cc.md#operator)
- used by: [`operator<<`](compilation_cache_utils.cc.md#operator), [`GetFromTier3OrCompile`](compilation_cache.cc.md#CompilationCache.GetFromTier3OrCompile), [`GetFromTier3Cache`](tier3_compilation_cache.cc.md#GetFromTier3Cache), [`GetFromTier2Cache`](tier2_compilation_cache.cc.md#GetFromTier2Cache), [`LoadSerializedExecutable`](compilation_cache_utils.cc.md#LoadSerializedExecutable), [`AbslStringify`](compilation_cache_utils.h.md#AbslStringify)

## Functions
- <a id="AbslStringify"></a>`AbslStringify(Sink& sink, const CacheTier tier)` — [`L44`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_cache_utils.h#L44)

