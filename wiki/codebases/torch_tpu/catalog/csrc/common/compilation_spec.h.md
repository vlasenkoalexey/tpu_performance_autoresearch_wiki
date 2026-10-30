---
title: 'Module: csrc/common/compilation_spec.h'
type: catalog
provenance: extracted
module: csrc/common/compilation_spec.h
status: fresh
symbol_base: 'cxx . . $ '
symbols:
  CompilationMode: torch_tpu/CompilationMode#
  CompilationMode.kFastCompile: torch_tpu/CompilationMode#kFastCompile.
  UniqueCompileOptions: torch_tpu/UniqueCompileOptions#
  CompilationSpec.xla_compile_options: torch_tpu/CompilationSpec#xla_compile_options.
  CompilationSpec: torch_tpu/CompilationSpec#
  CompilationSpec.compile_options_key: torch_tpu/CompilationSpec#compile_options_key.
  CompilationMode.kFastRuntime: torch_tpu/CompilationMode#kFastRuntime.
  CompilerOptionOverrides: torch_tpu/CompilerOptionOverrides#
  CompilationSpec.CompilationSpec: torch_tpu/CompilationSpec#CompilationSpec(8b805eb3ac27bda5).
  kCompilationModeValues: torch_tpu/kCompilationModeValues.
  CompilationSpec.Copy: torch_tpu/CompilationSpec#Copy(4472701ff372e582).
  CompilationContext: torch_tpu/CompilationContext#
  CompilationSpecsByMode: torch_tpu/CompilationSpecsByMode#
  CompilationContext.CompilationContext: torch_tpu/CompilationContext#CompilationContext(3e454b8ccf442868).
  CompilationContext.operator: absl/torch_tpu/CompilationContext#`operator=`(7c5e7bc78d84034).
  CompilationContext.compilation_specs: torch_tpu/CompilationContext#compilation_specs(c4e65b9cfc06c7a2).
  CompilationContext.compiler_option_overrides: torch_tpu/CompilationContext#compiler_option_overrides(2f7b810e606cf6de).
  CompilationSpec.operator: absl/torch_tpu/CompilationSpec#`operator=`(a1c54c5ed653fec).
  CompilationContext.compilation_specs_: absl/torch_tpu/CompilationContext#compilation_specs_.
  CompilationContext.compiler_option_overrides_: torch_tpu/CompilationContext#compiler_option_overrides_.
---
# Module: [`csrc/common/compilation_spec.h`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h)

## Classes
### `CompilationContext`
- def: [`csrc/common/compilation_spec.h:90`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L90)
- doc: Python thread-local context to manage currently effective XLA compile options
- signature: `class CompilationContext`
- members:
  - `CompilationContext(const CompilationContext&)` — [`L98`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L98) — Movable but not copyable.
  - <a id="CompilationContext.CompilationContext"></a>`CompilationContext(CompilationSpecsByMode specs, CompilerOptionOverrides overrides)` — [`L92`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L92)
  - `CompilationContext(CompilationSpecsByMode specs, CompilerOptionOverrides overrides)` — [`L92`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L92)
  - `CompilationContext(CompilationContext&&)` — [`L100`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L100)
  - `CompilationContext(CompilationSpecsByMode specs, CompilerOptionOverrides overrides)` — [`L92`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L92)
  - `CompilationContext(const CompilationContext&)` — [`L98`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L98) — Movable but not copyable.
  - `CompilationContext(CompilationContext&&)` — [`L100`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L100)
  - `compilation_specs()` — [`L103`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L103)
  - <a id="CompilationContext.compilation_specs"></a>`compilation_specs()` — [`L103`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L103)
  - `compilation_specs()` — [`L103`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L103)
  - `compiler_option_overrides()` — [`L106`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L106)
  - <a id="CompilationContext.compiler_option_overrides"></a>`compiler_option_overrides()` — [`L106`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L106)
  - `compiler_option_overrides()` — [`L106`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L106)
  - `operator=(const CompilationContext&)` — [`L99`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L99)
  - `operator=(CompilationContext&&)` — [`L101`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L101)
  - `operator=(const CompilationContext&)` — [`L99`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L99)
  - <a id="CompilationContext.operator"></a>`operator=(CompilationContext&&)` — [`L101`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L101)
  - `compilation_specs_` — [`L111`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L111)
  - <a id="CompilationContext.compilation_specs_"></a>`compilation_specs_` — [`L111`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L111)
  - <a id="CompilationContext.compiler_option_overrides_"></a>`compiler_option_overrides_` — [`L112`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L112)
  - `compiler_option_overrides_` — [`L112`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L112)
- uses (calls/refs, reference-scoped): [`CompilerOptionOverrides`](compilation_spec.h.md#CompilerOptionOverrides), [`CompilationContext`](compilation_spec.h.md#CompilationContext), [`CompilationSpecsByMode`](compilation_spec.h.md#CompilationSpecsByMode)
- used by: [`GetCompilationSpec`](compilation.cc.md#GetCompilationSpec), [`PushCompilerOptionOverrides`](compilation.cc.md#PushCompilerOptionOverrides), [`GetCompilationSpecForTraversal`](../eager/materialize.cc.md#GetCompilationSpecForTraversal)

### <a id="CompilationMode"></a>`CompilationMode`
- def: [`csrc/common/compilation_spec.h:33`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L33) — documented in [compilation-pipeline](../../../concepts/compilation-pipeline.md)
- doc: Mode for compiling a computation graph.
- signature: `enum class CompilationMode`
- members:
  - `kFastCompile` — [`L34`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L34) — Reduces compile time, but may result in slower execution.
  - <a id="CompilationMode.kFastCompile"></a>`kFastCompile` — [`L34`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L34) — Reduces compile time, but may result in slower execution.
  - <a id="CompilationMode.kFastRuntime"></a>`kFastRuntime` — [`L35`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L35) — Produces more optimized executables, but with longer
  - `kFastRuntime` — [`L35`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L35) — Produces more optimized executables, but with longer
- uses (calls/refs, reference-scoped): [`CompilationMode`](compilation_spec.h.md#CompilationMode)
- used by: [`GetCompilationSpec`](compilation.cc.md#GetCompilationSpec), [`PyCompileMlir`](../internal/compile/tpu_torch_compile.cc.md#PyCompileMlir), [`TestBody`](../eager/materialize_test.cc.md#MaterializeTest_CompilerOptionsPropagateToMaterializeThread_Test.TestBody), [`PyPrecompileSliceModule`](../internal/compile/tpu_torch_compile.cc.md#PyPrecompileSliceModule), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_DynamicCacheLayoutMismatch_Test.TestBody), [`PyGetOrCompileSliceModule`](../internal/compile/tpu_torch_compile.cc.md#PyGetOrCompileSliceModule), [`PyPrecompilePadModule`](../internal/compile/tpu_torch_compile.cc.md#PyPrecompilePadModule), [`PyGetDynamicPadModule`](../internal/compile/tpu_torch_compile.cc.md#PyGetDynamicPadModule), [`PyGetOrCompilePadModule`](../internal/compile/tpu_torch_compile.cc.md#PyGetOrCompilePadModule), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_PeakMemoryReported_Test.TestBody), [`GetCompilationMode`](../eager/events_queue.cc.md#GetCompilationMode), [`module_`](compilation.h.md#ContextedModule.module_), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_AllowCacheModeDisabled_Test.TestBody), [`MakeCompilationSpecs`](compilation.cc.md#MakeCompilationSpecs), [`TestBody`](compilation_cache_remote_filesystem_test.cc.md#RemoteCacheTest_GetFromTier3Cache_Test.TestBody), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_GetOrCompileLogsOnMiss_Test.TestBody), [`MakeCacheKey`](tier2_compilation_cache_test.cc.md#MakeCacheKey), [`MakeCacheKey`](tier3_compilation_cache_test.cc.md#MakeCacheKey), [`TestBody`](compilation_parse_xla_options_test.cc.md#MakeCompilerOptionsTest_ParsesXlaOptions_Test.TestBody), [`TestBody`](compilation_parse_xla_options_test.cc.md#MakeCompilerOptionsTest_PythonContextManagerOverridesEnvVar_Test.TestBody), [`TestBody`](../eager/events_queue_test.cc.md#CompilationModeTest_GetCompilationMode_Test.TestBody), [`TestBody`](compile_options_key_test.cc.md#CompileOptionsKeyTest_EnvOptionOverrides_Test.TestBody), [`TestBody`](compile_options_key_test.cc.md#CompileOptionsKeyTest_StableFingerprint_Test.TestBody), [`TestBody`](compile_options_key_test.cc.md#CompileOptionsKeyTest_ThreadLocalContextOverrides_Test.TestBody), [`TestBody`](compile_options_key_test.cc.md#CompileOptionsKeyTest_XlaExecutionEffortLevelOverrides_Test.TestBody), [`GetCompilationSpecForTraversal`](../eager/materialize.cc.md#GetCompilationSpecForTraversal), [`snapshot_future`](../eager/events_queue.h.md#PendingEventSnapshot.snapshot_future), [`ResetRepeatedOpsHeuristicState`](../eager/events_queue.cc.md#ResetRepeatedOpsHeuristicState), [`TestBody`](compilation_test.cc.md#MakeCompilerOptionsTest_CompilerOptionOverrides_Test.TestBody), [`GetCompileOptionsKey`](compile_options_key_test.cc.md#GetCompileOptionsKey), [`ConvertTraverseAndCompileOptions`](../internal/compile/tpu_torch_compile.cc.md#ConvertTraverseAndCompileOptions), [`TestBody`](compilation_test.cc.md#MakeCompilerOptionsTest_DefaultToO1ForEagerMode_Test.TestBody), [`TestBody`](compilation_test.cc.md#MakeCompilerOptionsTest_DefaultToUnsetForTorchCompileMode_Test.TestBody), [`MakeCompilerOptionOverrides`](compilation.cc.md#MakeCompilerOptionOverrides), [`kCompilationModeValues`](compilation_spec.h.md#kCompilationModeValues), [`GetCompileOptions`](compilation_test.cc.md#GetCompileOptions), [`CompilationSpecsByMode`](compilation_spec.h.md#CompilationSpecsByMode), [`TraverseAndCompileOptions`](../internal/compile/compiled_mode.h.md#TraverseAndCompileOptions), [`compilation_mode`](../internal/compile/compiled_mode.h.md#TraverseAndCompileOptions.compilation_mode), [`reason`](../eager/events_queue.h.md#MaterializationSettings.reason)

### `CompilationSpec`
- def: [`csrc/common/compilation_spec.h:54`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L54)
- doc: Specifications to compile a computation graph, including
- signature: `struct CompilationSpec`
- members:
  - `CompilationSpec(const CompilationSpec&)` — [`L60`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L60) — Movable but not copyable.
  - <a id="CompilationSpec.CompilationSpec"></a>`CompilationSpec(UniqueCompileOptions options, CompileOptionsKey key)` — [`L55`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L55)
  - `CompilationSpec(UniqueCompileOptions options, CompileOptionsKey key)` — [`L55`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L55)
  - `CompilationSpec(UniqueCompileOptions options, CompileOptionsKey key)` — [`L55`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L55)
  - `CompilationSpec(CompilationSpec&&)` — [`L62`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L62)
  - `CompilationSpec(CompilationSpec&&)` — [`L62`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L62)
  - `CompilationSpec(const CompilationSpec&)` — [`L60`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L60) — Movable but not copyable.
  - `Copy()` — [`L69`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L69) — Returns a deep copy of this `CompilationSpec`.
  - <a id="CompilationSpec.Copy"></a>`Copy()` — [`L69`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L69) — Returns a deep copy of this `CompilationSpec`.
  - `operator=(const CompilationSpec&)` — [`L61`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L61)
  - <a id="CompilationSpec.operator"></a>`operator=(CompilationSpec&&)` — [`L63`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L63)
  - `operator=(CompilationSpec&&)` — [`L63`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L63)
  - `operator=(const CompilationSpec&)` — [`L61`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L61)
  - `compile_options_key` — [`L76`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L76)
  - <a id="CompilationSpec.compile_options_key"></a>`compile_options_key` — [`L76`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L76)
  - `xla_compile_options` — [`L75`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L75)
  - <a id="CompilationSpec.xla_compile_options"></a>`xla_compile_options` — [`L75`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L75)
- uses (calls/refs, reference-scoped): [`CompileOptionsKey`](compile_options_key.h.md#CompileOptionsKey), [`UniqueCompileOptions`](compilation_spec.h.md#UniqueCompileOptions), [`CompilationSpec`](compilation_spec.h.md#CompilationSpec)
- used by: [`GetCompilationSpec`](compilation.cc.md#GetCompilationSpec), [`VerifyAndCompileTraversal`](../eager/execution_task.cc.md#VerifyAndCompileTraversal), [`Compile`](../eager/traversal.cc.md#Traversal.Compile), [`PyCompileMlir`](../internal/compile/tpu_torch_compile.cc.md#PyCompileMlir), [`TestBody`](../eager/materialize_test.cc.md#MaterializeTest_CompilerOptionsPropagateToMaterializeThread_Test.TestBody), [`PyPrecompileSliceModule`](../internal/compile/tpu_torch_compile.cc.md#PyPrecompileSliceModule), [`TestBody`](../eager/traversal_test.cc.md#TraversalTest_CompileAnnotatesArgumentLayoutsWithTilingAndCaching_Test.TestBody), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_DynamicCacheLayoutMismatch_Test.TestBody), [`TestBody`](../eager/traversal_test.cc.md#TraversalTest_CompilePopulatesAndResetsOutCacheKey_Test.TestBody), [`PyGetOrCompileSliceModule`](../internal/compile/tpu_torch_compile.cc.md#PyGetOrCompileSliceModule), [`PyPrecompilePadModule`](../internal/compile/tpu_torch_compile.cc.md#PyPrecompilePadModule), [`PyGetDynamicPadModule`](../internal/compile/tpu_torch_compile.cc.md#PyGetDynamicPadModule), [`PyGetOrCompilePadModule`](../internal/compile/tpu_torch_compile.cc.md#PyGetOrCompilePadModule), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_PeakMemoryReported_Test.TestBody), [`TestBody`](../eager/traversal_test.cc.md#TraversalTest_CompileAnnotatesArgumentLayouts_Test.TestBody), [`TestBody`](../eager/traversal_test.cc.md#TraversalTest_PreCompileAndCompileCacheKeyMatch_Test.TestBody), [`TestBody`](../eager/traversal_test.cc.md#TraversalTest_ApplyDeviceAssignmentToCompileSpecUpdatesSpec_Test.TestBody), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_AllowCacheModeDisabled_Test.TestBody), [`TestBody`](compilation_cache_remote_filesystem_test.cc.md#RemoteCacheTest_GetFromTier3Cache_Test.TestBody), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_GetOrCompileLogsOnMiss_Test.TestBody), [`MakeCacheKey`](tier2_compilation_cache_test.cc.md#MakeCacheKey), [`MakeCacheKey`](tier3_compilation_cache_test.cc.md#MakeCacheKey), [`MaybeUpdateSpecWithLayout`](../eager/traversal.cc.md#Traversal.MaybeUpdateSpecWithLayout), [`ApplyDeviceAssignmentToCompileSpec`](../eager/traversal.cc.md#Traversal.ApplyDeviceAssignmentToCompileSpec), [`TestBody`](compilation_parse_xla_options_test.cc.md#MakeCompilerOptionsTest_ParsesXlaOptions_Test.TestBody), [`TestBody`](compilation_parse_xla_options_test.cc.md#MakeCompilerOptionsTest_PythonContextManagerOverridesEnvVar_Test.TestBody), [`ApplyPlacementsToCompileSpec`](../eager/traversal.cc.md#ApplyPlacementsToCompileSpec), [`GetCompileOptionsKey`](compile_options_key_test.cc.md#GetCompileOptionsKey), [`GetCompileOptions`](compilation_test.cc.md#GetCompileOptions)

### <a id="CompilationSpecsByMode"></a>`CompilationSpecsByMode`
- def: [`csrc/common/compilation_spec.h:79`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L79)
- signature: `using CompilationSpecsByMode = std::map<CompilationMode, CompilationSpec>`
- uses (calls/refs, reference-scoped): [`CompilationMode`](compilation_spec.h.md#CompilationMode), [`CompilationSpec`](compilation_spec.h.md#CompilationSpec)
- used by: [`MakeCompileOptionsKey`](compilation.cc.md#MakeCompileOptionsKey), [`MakeCompilationSpecs`](compilation.cc.md#MakeCompilationSpecs), [`MakeCompilationContext`](compilation.cc.md#MakeCompilationContext), [`CompilationContext`](compilation_spec.h.md#CompilationContext.CompilationContext), [`operator=`](compilation_spec.h.md#CompilationContext.operator), [`compiler_option_overrides`](compilation_spec.h.md#CompilationContext.compiler_option_overrides)

### <a id="CompilerOptionOverrides"></a>`CompilerOptionOverrides`
- def: [`csrc/common/compilation_spec.h:83`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L83)
- doc: Maps an XLA compiler option name to its string value. We pick this
- signature: `using CompilerOptionOverrides = std::map<std::string, std::string>`
- used by: [`TestBody`](../eager/materialize_test.cc.md#MaterializeTest_CompilerOptionsPropagateToMaterializeThread_Test.TestBody), [`ApplyCompilerOptionOverrides`](compilation.cc.md#ApplyCompilerOptionOverrides), [`module_`](compilation.h.md#ContextedModule.module_), [`MakeCompilationSpecs`](compilation.cc.md#MakeCompilationSpecs), [`PushCompilerOptionOverrides`](compilation.cc.md#PushCompilerOptionOverrides), [`ParseEffortLevel`](compilation.cc.md#ParseEffortLevel), [`PushCompilerOptions`](../internal/compiler_options/compiler_options_impl.cc.md#PushCompilerOptions), [`MakeCompilationContext`](compilation.cc.md#MakeCompilationContext), [`SetTpuOptions`](compilation.cc.md#SetTpuOptions), [`ScopedCompilerOptionOverrides`](compilation_test_helper.h.md#ScopedCompilerOptionOverrides.ScopedCompilerOptionOverrides), [`TestBody`](compilation_parse_xla_options_test.cc.md#ApplyCompilerOptionOverrides_AppendsNonExistingOptions_Test.TestBody), [`TestBody`](compilation_parse_xla_options_test.cc.md#ApplyCompilerOptionOverrides_HandlesExistingAndNewOptions_Test.TestBody), [`TestBody`](compilation_parse_xla_options_test.cc.md#ApplyCompilerOptionOverrides_ReplacesExistingOptions_Test.TestBody), [`MakeCompilerOptionOverrides`](compilation.cc.md#MakeCompilerOptionOverrides), [`CompilationContext`](compilation_spec.h.md#CompilationContext.CompilationContext), [`GetCompilerOptionOverridesFromEnvVar`](compilation.cc.md#GetCompilerOptionOverridesFromEnvVar), [`compilation_specs`](compilation_spec.h.md#CompilationContext.compilation_specs), [`compilation_specs_`](compilation_spec.h.md#CompilationContext.compilation_specs_)

### <a id="UniqueCompileOptions"></a>`UniqueCompileOptions`
- def: [`csrc/common/compilation_spec.h:49`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L49)
- doc: `xla::CompileOptions` is a complex object with many fields. Even moving it
- signature: `using UniqueCompileOptions = absl_nonnull std::unique_ptr<xla::CompileOptions>`
- used by: [`UnboundedDynamicCache`](compilation_cache.h.md#CompilationCache.UnboundedDynamicCache), [`GetOrCompileImpl`](compilation_cache.cc.md#CompilationCache.GetOrCompileImpl), [`kUnboundedDynamic`](compilation_cache.h.md#CompilationCache.CacheEntryKind.kUnboundedDynamic), [`GetFromTier3OrCompile`](compilation_cache.cc.md#CompilationCache.GetFromTier3OrCompile), [`CreateSlicingKernel`](compilation_cache.cc.md#CompilationCache.CreateSlicingKernel), [`BuildNonzeroIndicesExecutable`](../experimental/precompiled_kernels/nonzero_indices.cc.md#BuildNonzeroIndicesExecutable), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_PeakMemoryReported_Test.TestBody), [`CompileModuleWithCache`](../internal/compile/tpu_torch_compile.cc.md#CompileModuleWithCache), [`Compile`](compilation_cache.cc.md#CompilationCache.Compile), [`CreateDynamicKernelAdapter`](compilation_cache.cc.md#CompilationCache.CreateDynamicKernelAdapter), [`module_`](compilation.h.md#ContextedModule.module_), [`CreateDummyExecutable`](compilation_cache_test_utils.cc.md#CreateDummyExecutable), [`GetFromTier2OrCompile`](compilation_cache.cc.md#CompilationCache.GetFromTier2OrCompile), [`CreatePaddingKernel`](compilation_cache.cc.md#CompilationCache.CreatePaddingKernel), [`EnqueueCompilation`](compilation_cache.cc.md#CompilationCache.EnqueueCompilation), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_GetOrCompileLogsOnMiss_Test.TestBody), [`CompileMlirExecutable`](../internal/compile/compiled_mode.cc.md#CompileMlirExecutable), [`MlirComputationBuilderToExecutableBuilder`](compilation.cc.md#MlirComputationBuilderToExecutableBuilder), [`CompileMlirExecutable`](../internal/compile/compiled_mode.cc.md#CompileMlirExecutable), [`Compile`](compilation.cc.md#Compile), [`TestBody`](compilation_parse_xla_options_test.cc.md#MakeCompilerOptionsTest_ParsesXlaOptions_Test.TestBody), [`TestBody`](compilation_parse_xla_options_test.cc.md#MakeCompilerOptionsTest_PythonContextManagerOverridesEnvVar_Test.TestBody), [`module_name`](../internal/compile/compiled_mode.h.md#TraverseAndCompileOptions.module_name), [`TestBody`](compilation_test.cc.md#MakeCompilerOptionsTest_CompilerOptionOverrides_Test.TestBody), [`TestBody`](compilation_test.cc.md#MakeCompilerOptionsTest_DefaultToO1ForEagerMode_Test.TestBody), [`TestBody`](compilation_test.cc.md#MakeCompilerOptionsTest_DefaultToUnsetForTorchCompileMode_Test.TestBody), [`CompilationSpec`](compilation_spec.h.md#CompilationSpec.CompilationSpec), [`LoadedExecutableBuilder`](compilation.h.md#LoadedExecutableBuilder), [`GetOrCompile`](compilation_cache.cc.md#CompilationCache.GetOrCompile), [`SetUpTestSuite`](compilation_test.cc.md#MakeCompilerOptionsTest.SetUpTestSuite), [`Copy`](compilation_spec.h.md#CompilationSpec.Copy)

## Module values
- <a id="kCompilationModeValues"></a>`kCompilationModeValues` — [`L41`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L41) — LINT.IfChange(compilation_mode_values)
- `kCompilationModeValues` — [`L41`](../../../../../../raw/code/torch_tpu/csrc/common/compilation_spec.h#L41) — LINT.IfChange(compilation_mode_values)

