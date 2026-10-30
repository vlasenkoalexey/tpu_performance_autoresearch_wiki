---
title: 'Module: csrc/common/compile_options_key.h'
type: catalog
provenance: extracted
module: csrc/common/compile_options_key.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  CompileOptionsKey: CompileOptionsKey#
  CompileOptionsKey.CompileOptionsKey: CompileOptionsKey#CompileOptionsKey(2c44cd906ae4e829).
  CompileOptionsKey.key: CompileOptionsKey#key(fe4d2d262d4164a8).
  CompileOptionsKey.operator: CompileOptionsKey#`operator==`(afcf80f6d0da219).
  AbslStringify: AbslStringify(88154015c5588696).
  CompileOptionsKey.Hash.operator: CompileOptionsKey#Hash#`operator()`(ccd0acae356c692).
  CompileOptionsKey.key_: CompileOptionsKey#key_.
  CompileOptionsKey.Hash: CompileOptionsKey#Hash#
---
# Module: [`csrc/common/compile_options_key.h`](../../../../../../raw/code/torch_tpu/csrc/common/compile_options_key.h)

## Classes
### <a id="CompileOptionsKey"></a>`CompileOptionsKey`
- def: [`csrc/common/compile_options_key.h:27`](../../../../../../raw/code/torch_tpu/csrc/common/compile_options_key.h#L27) — documented in [compilation-pipeline](../../../concepts/compilation-pipeline.md)
- signature: `class CompileOptionsKey`
- members:
  - <a id="CompileOptionsKey.CompileOptionsKey"></a>`CompileOptionsKey(FingerprintType key)` — [`L29`](../../../../../../raw/code/torch_tpu/csrc/common/compile_options_key.h#L29)
  - <a id="CompileOptionsKey.key"></a>`key()` — [`L41`](../../../../../../raw/code/torch_tpu/csrc/common/compile_options_key.h#L41)
  - <a id="CompileOptionsKey.operator"></a>`operator==(const CompileOptionsKey rhs)` — [`L37`](../../../../../../raw/code/torch_tpu/csrc/common/compile_options_key.h#L37)
  - <a id="CompileOptionsKey.key_"></a>`key_` — [`L44`](../../../../../../raw/code/torch_tpu/csrc/common/compile_options_key.h#L44)
- uses (calls/refs, reference-scoped): [`FingerprintType`](fingerprint_utils.h.md#FingerprintType)
- used by: [`operator<<`](cache_key.cc.md#operator), [`CompactFormat`](cache_key.cc.md#CompilationCacheKey.CompactFormat), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_UnboundedDynamicCache_Test.TestBody), [`GetOrCreateCacheEntry`](compilation_cache.cc.md#CompilationCache.GetOrCreateCacheEntry), [`TestBody`](../eager/materialize_test.cc.md#MaterializeTest_CompilerOptionsPropagateToMaterializeThread_Test.TestBody), [`UnboundedDynamicCache`](compilation_cache.h.md#CompilationCache.UnboundedDynamicCache), [`GetCacheKey`](../eager/traversal.cc.md#Traversal.GetCacheKey), [`AddBoundedDynamicCacheEntry`](compilation_cache.cc.md#CompilationCache.AddBoundedDynamicCacheEntry), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_UnboundedDynamicCacheEvictAll_Test.TestBody), [`NonZeroCacheKey`](../experimental/precompiled_kernels/nonzero_indices.cc.md#NonZeroCacheKey), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_DynamicCacheLayoutMismatch_Test.TestBody), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_UnboundedDynamicCacheOutputShapeMismatch_Test.TestBody), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_UnboundedDynamicCacheShapeMismatch_Test.TestBody), [`MakeCompileOptionsKey`](compilation.cc.md#MakeCompileOptionsKey), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_UnboundedDynamicCacheMiss_Test.TestBody), [`CreateSlicingKernel`](compilation_cache.cc.md#CompilationCache.CreateSlicingKernel), [`shape_`](../eager/traversal_test.cc.md#TraversalTest.shape_), [`TestBody`](../eager/traversal_test.cc.md#TraversalTest_PreCompileAndCompileCacheKeyMatch_Test.TestBody), [`CompilationCacheKey`](cache_key.h.md#CompilationCacheKey.CompilationCacheKey), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_UnboundedDynamicCacheBackendNotInitialized_Test.TestBody), [`TestBody`](../eager/traversal_test.cc.md#TraversalTest_ApplyDeviceAssignmentToCompileSpecUpdatesSpec_Test.TestBody), [`CreateDynamicKernelAdapter`](compilation_cache.cc.md#CompilationCache.CreateDynamicKernelAdapter), [`TestBody`](compilation_cache_tiered_test.cc.md#TieredCompilationCacheTest_UnboundedDynamicCacheTier3Hit_Test.TestBody), [`TestBody`](../eager/traversal_test.cc.md#TraversalTest_OpWithPreExistingDeviceAssignmentParamDoesNotCrash_Test.TestBody), [`module_`](compilation.h.md#ContextedModule.module_), [`TestBody`](compilation_cache_tiered_test.cc.md#TieredCompilationCacheTest_UnboundedDynamicCacheTier2Hit_Test.TestBody), [`TestBody`](../eager/traversal_test.cc.md#TraversalTest_TopLevelDonationChangesCacheKey_Test.TestBody), [`CreatePaddingKernel`](compilation_cache.cc.md#CompilationCache.CreatePaddingKernel), [`TestBody`](../eager/traversal_test.cc.md#TraversalTest_DifferentDeviceAssignmentChangesCacheKey_Test.TestBody), [`operator=`](../eager/traversal.h.md#Traversal.operator), [`DummyKey`](compilation_cache_test.cc.md#DummyKey), [`TestBody`](compile_options_key_test.cc.md#CompileOptionsKeyTest_EnvOptionOverrides_Test.TestBody), [`TestBody`](compile_options_key_test.cc.md#CompileOptionsKeyTest_StableFingerprint_Test.TestBody), [`TestBody`](compile_options_key_test.cc.md#CompileOptionsKeyTest_ThreadLocalContextOverrides_Test.TestBody), [`TestBody`](compile_options_key_test.cc.md#CompileOptionsKeyTest_XlaExecutionEffortLevelOverrides_Test.TestBody), [`operator()`](cache_key.h.md#CompilationCacheKey.Hash.operator), [`TestBody`](compile_options_key_test.cc.md#CompileOptionsKeyDeathTest_LibtpuInitArgsAffectsFingerprint_Test.TestBody), [`graph_key`](cache_key.h.md#CompilationCacheKey.graph_key), [`Fingerprint`](compilation.cc.md#Fingerprint), [`operator==`](cache_key.h.md#operator)  (+8 more)

### <a id="CompileOptionsKey.Hash"></a>`CompileOptionsKey.Hash`
- def: [`csrc/common/compile_options_key.h:31`](../../../../../../raw/code/torch_tpu/csrc/common/compile_options_key.h#L31)
- signature: `struct Hash`
- members:
  - <a id="CompileOptionsKey.Hash.operator"></a>`operator()()` — [`L32`](../../../../../../raw/code/torch_tpu/csrc/common/compile_options_key.h#L32)
- uses (calls/refs, reference-scoped): [`CompileOptionsKey`](compile_options_key.h.md#CompileOptionsKey), [`key_`](compile_options_key.h.md#CompileOptionsKey.key_)

## Functions
- <a id="AbslStringify"></a>`AbslStringify(Sink& sink, const CompileOptionsKey key)` — [`L49`](../../../../../../raw/code/torch_tpu/csrc/common/compile_options_key.h#L49) — Formats a compile options key as a human-readable string.

