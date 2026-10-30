---
title: 'Module map: torch_tpu'
type: catalog-map
provenance: extracted
---
# Module map: torch_tpu @ 005903d0ef

716 modules, 20186 documentable symbols, 15906 index rows (overloads share a row), 77410 caller edges. The index is tab-separated; grep it by anchor, never read a file whole. Columns: anchor, path, line, kind, rank, hash, callers, citing pages, then signature and doc line in the full profile. Hubs have hundreds of callers and a search tool shows about 50 lines: count first, narrow by directory, end every listing with `head`.

```
grep -P '^<path>#<Name>\t' catalog/symbols/*.tsv                            # one symbol's row
grep -P '[#.]<Name>\t' catalog/symbols/*.tsv | sort -t$'\t' -k5 -nr | head -20   # by bare name, best first
grep -P '^<dir>/.*#<Name>\t' catalog/symbols/*.tsv | head -20                    # a name within an area
awk -F'\t' '$2=="<path>"' catalog/symbols/*.tsv | cut -f1,3,4 | head -40         # everything a module defines
grep -c -P '^<path>#<Name>\t' catalog/edges/*.tsv                         # how many callers (count first)
grep -P '^<path>#<Name>\t' catalog/edges/*.tsv | cut -f2 | cut -d/ -f1-2 | sort | uniq -c   # callers by directory
grep -P '^<path>#<Name>\t<dir>/' catalog/edges/*.tsv | cut -f2 | head -20      # callers in one directory
grep -P '\t<path>#<Name>$' catalog/edges/*.tsv | cut -f1 | head -20           # what it calls
```

## Index files

| Shard | Symbols | Edges |
|---|---|---|
| `csrc/api` | [`symbols/csrc-api.tsv`](symbols/csrc-api.tsv) — 85 rows | [`edges/csrc-api.tsv`](edges/csrc-api.tsv) — 154 edges |
| `csrc/common` | [`symbols/csrc-common.tsv`](symbols/csrc-common.tsv) — 3425 rows | [`edges/csrc-common.tsv`](edges/csrc-common.tsv) — 36272 edges |
| `csrc/distributed` | [`symbols/csrc-distributed.tsv`](symbols/csrc-distributed.tsv) — 364 rows | [`edges/csrc-distributed.tsv`](edges/csrc-distributed.tsv) — 820 edges |
| `csrc/eager` | [`symbols/csrc-eager.tsv`](symbols/csrc-eager.tsv) — 1412 rows | [`edges/csrc-eager.tsv`](edges/csrc-eager.tsv) — 5604 edges |
| `csrc/experimental` | [`symbols/csrc-experimental.tsv`](symbols/csrc-experimental.tsv) — 132 rows | [`edges/csrc-experimental.tsv`](edges/csrc-experimental.tsv) — 242 edges |
| `csrc/internal` | [`symbols/csrc-internal.tsv`](symbols/csrc-internal.tsv) — 1127 rows | [`edges/csrc-internal.tsv`](edges/csrc-internal.tsv) — 2814 edges |
| `csrc/mlir` | [`symbols/csrc-mlir.tsv`](symbols/csrc-mlir.tsv) — 43 rows | [`edges/csrc-mlir.tsv`](edges/csrc-mlir.tsv) — 42 edges |
| `csrc/ops` | [`symbols/csrc-ops.tsv`](symbols/csrc-ops.tsv) — 6821 rows | [`edges/csrc-ops.tsv`](edges/csrc-ops.tsv) — 27989 edges |
| `csrc/pjrt` | [`symbols/csrc-pjrt.tsv`](symbols/csrc-pjrt.tsv) — 158 rows | [`edges/csrc-pjrt.tsv`](edges/csrc-pjrt.tsv) — 541 edges |
| `src/torch_tpu` | [`symbols/src-torch_tpu.tsv`](symbols/src-torch_tpu.tsv) — 2339 rows | [`edges/src-torch_tpu.tsv`](edges/src-torch_tpu.tsv) — 2932 edges |

Below, one row per module: entry points are the symbols with the most callers; *cited by* lists the concept pages that cite into the module.

## `csrc/api`

Index: [`symbols/csrc-api.tsv`](symbols/csrc-api.tsv) (85 rows), [`edges/csrc-api.tsv`](edges/csrc-api.tsv) (154 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`csrc/api/tensor_buffer.cc`](csrc/api/tensor_buffer.cc.md) | 21 | `GetBaseTensorBuffer`, `buffer_ref`, `TensorBufferHandle` |  |
| [`csrc/api/tensor_buffer.h`](csrc/api/tensor_buffer.h.md) | 10 | `TensorBufferHandle`, `impl_`, `DeviceBufferState` |  |
| [`csrc/api/tensor_buffer_test.cc`](csrc/api/tensor_buffer_test.cc.md) | 85 | `TensorBufferTest`, `CreateDeferredTpuTensor`, `TensorBufferTest_CpuTensorRejection_Test` |  |

## `csrc/common`

Index: [`symbols/csrc-common.tsv`](symbols/csrc-common.tsv) (3425 rows), [`edges/csrc-common.tsv`](edges/csrc-common.tsv) (36272 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`csrc/common/aten_utils.cc`](csrc/common/aten_utils.cc.md) | 5 | `operator==`, `InferComputationDtype`, `ToString` |  |
| [`csrc/common/aten_utils.h`](csrc/common/aten_utils.h.md) | 38 | `ValidateOutDtype`, `IsComplex`, `IsFloatingPoint` |  |
| [`csrc/common/cache_key.cc`](csrc/common/cache_key.cc.md) | 50 | `OpParamCacheKeys`, `operator<<`, `GetTensor` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md), [compilation-cache-key](../concepts/compilation-cache-key.md), [fused-optimizer-kernels](../concepts/fused-optimizer-kernels.md), [op-names-and-python-context](../concepts/op-names-and-python-context.md) |
| [`csrc/common/cache_key.h`](csrc/common/cache_key.h.md) | 266 | `OpParamCacheKeys`, `EnforceSetParamType`, `MakeOpParamCacheKeys` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md), [compilation-cache-key](../concepts/compilation-cache-key.md) |
| [`csrc/common/cache_key_test.cc`](csrc/common/cache_key_test.cc.md) | 284 | `Pair`, `ElementsAre`, `IsEmpty` |  |
| [`csrc/common/compilation.cc`](csrc/common/compilation.cc.md) | 39 | `GetCompilationSpec`, `Make`, `MakeCompileOptionsKey` | [compilation-pipeline](../concepts/compilation-pipeline.md) |
| [`csrc/common/compilation.h`](csrc/common/compilation.h.md) | 56 | `SharedLoadedExecutableWithMetadata`, `ContextedModule`, `CompiledKernel` | [compilation-pipeline](../concepts/compilation-pipeline.md) |
| [`csrc/common/compilation_cache.cc`](csrc/common/compilation_cache.cc.md) | 76 | `GetInstance`, `GetOrCompile`, `ShutDown` | [compilation-cache](../concepts/compilation-cache.md), [compilation-pipeline](../concepts/compilation-pipeline.md) |
| [`csrc/common/compilation_cache.h`](csrc/common/compilation_cache.h.md) | 68 | `CompilationCache`, `cache_mutex_`, `CacheEntry` | [compilation-cache](../concepts/compilation-cache.md) |
| [`csrc/common/compilation_cache_remote_filesystem_test.cc`](csrc/common/compilation_cache_remote_filesystem_test.cc.md) | 47 | `RemoteCacheTest`, `env_`, `test_dir_` |  |
| [`csrc/common/compilation_cache_test.cc`](csrc/common/compilation_cache_test.cc.md) | 154 | `CompilationCacheTest`, `DummyKey`, `CompilationCacheTestHelper` |  |
| [`csrc/common/compilation_cache_test_utils.cc`](csrc/common/compilation_cache_test_utils.cc.md) | 3 | `CreateDummyExecutable`, `MakeDummyDynamicMetadata`, `IsCompatible` |  |
| [`csrc/common/compilation_cache_tiered_test.cc`](csrc/common/compilation_cache_tiered_test.cc.md) | 21 | `TieredCompilationCacheTest_UnboundedDynamicCacheTier2Hit_Test`, `TieredCompilationCacheTest_UnboundedDynamicCacheTier3Hit_Test`, `TieredCompilationCacheTest` |  |
| [`csrc/common/compilation_cache_utils.cc`](csrc/common/compilation_cache_utils.cc.md) | 9 | `operator<<`, `AtomicWriteToCacheFile`, `GetTier3CacheRootDir` | [compilation-cache](../concepts/compilation-cache.md) |
| [`csrc/common/compilation_cache_utils.h`](csrc/common/compilation_cache_utils.h.md) | 6 | `CacheTier`, `kTier3`, `kTier1` |  |
| [`csrc/common/compilation_excess_precision_env_test.cc`](csrc/common/compilation_excess_precision_env_test.cc.md) | 9 | `CompilationExcessPrecisionEnvTest_VerifiesEnvVarInfluence_Test`, `TestBody`, `CompilationExcessPrecisionEnvTest_VerifiesEnvVarInfluence_Test` |  |
| [`csrc/common/compilation_parse_xla_options_test.cc`](csrc/common/compilation_parse_xla_options_test.cc.md) | 51 | `Pair`, `MakeCompilerOptionsTest`, `ElementsAre` |  |
| [`csrc/common/compilation_spec.h`](csrc/common/compilation_spec.h.md) | 53 | `CompilationMode`, `CompilationSpec`, `UniqueCompileOptions` | [compilation-pipeline](../concepts/compilation-pipeline.md) |
| [`csrc/common/compilation_test.cc`](csrc/common/compilation_test.cc.md) | 30 | `MakeCompilerOptionsTest`, `GetCompileOptions`, `MakeCompilerOptionsTest_CompilerOptionOverrides_Test` |  |
| [`csrc/common/compilation_test_helper.h`](csrc/common/compilation_test_helper.h.md) | 3 | `ScopedCompilerOptionOverrides`, `ScopedCompilerOptionOverrides`, `~ScopedCompilerOptionOverrides` |  |
| [`csrc/common/compilation_thread_num_test.cc`](csrc/common/compilation_thread_num_test.cc.md) | 47 | `FLAGS_torch_tpu_internal_num_compilation_threads`, `ExitedWithCode`, `TestBody` |  |
| [`csrc/common/compile_options_key.h`](csrc/common/compile_options_key.h.md) | 8 | `CompileOptionsKey`, `CompileOptionsKey`, `key` | [compilation-pipeline](../concepts/compilation-pipeline.md) |
| [`csrc/common/compile_options_key_test.cc`](csrc/common/compile_options_key_test.cc.md) | 60 | `CompileOptionsKeyTest`, `kFastCompileDefaultFingerprint`, `GetCompileOptionsKey` |  |
| [`csrc/common/constexpr_map.h`](csrc/common/constexpr_map.h.md) | 64 | `ConstexprMap`, `at`, `contains` |  |
| [`csrc/common/constexpr_map_test.cc`](csrc/common/constexpr_map_test.cc.md) | 42 | `kMap`, `kSingleMap`, `kEmptyMap` |  |
| [`csrc/common/contain.cc`](csrc/common/contain.cc.md) | 14 | `ScopedMemMeasuringContainer`, `FLAGS_torch_tpu_internal_enable_compilation_container`, `Impl` |  |
| [`csrc/common/contain.h`](csrc/common/contain.h.md) | 6 | `ScopedMemMeasuringContainer`, `impl_`, `operator=` |  |
| [`csrc/common/context_manager.cc`](csrc/common/context_manager.cc.md) | 6 | `DisallowThisThreadToAccessContextState`, `CrashIfContextStateAccessIsDisallowed`, `PopContextStateUntyped` | [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md) |
| [`csrc/common/context_manager.h`](csrc/common/context_manager.h.md) | 19 | `GetContextState`, `ContextManagerNode`, `PushContextState` | [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md) |
| [`csrc/common/context_state_access_test.cc`](csrc/common/context_state_access_test.cc.md) | 45 | `TestBody`, `TestBody`, `ContextStateAccessDeathTest_CrashOnGetContextStateIfDisallowed_Test` |  |
| [`csrc/common/context_states.h`](csrc/common/context_states.h.md) | 34 | `EagerMode`, `kInternalCompileFxGraph`, `kDeferNever` | [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md) |
| [`csrc/common/device_type.h`](csrc/common/device_type.h.md) | 5 | `GetPrivateUse1DeviceType`, `GetPrivateUse1DeviceDebugName`, `PjRtDeviceType` |  |
| [`csrc/common/device_utils.h`](csrc/common/device_utils.h.md) | 1 | `IsSingleDeviceSpecified` |  |
| [`csrc/common/dimension_types.h`](csrc/common/dimension_types.h.md) | 16 | `Dimensions`, `Indices`, `Strides` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md) |
| [`csrc/common/discovery.cc`](csrc/common/discovery.cc.md) | 1 | `GetPremappedBufferSizeFromEnvOnce` |  |
| [`csrc/common/discovery_test.cc`](csrc/common/discovery_test.cc.md) | 28 | `ExitedWithCode`, `TestBody`, `GetPremappedBufferSizeFromEnvOnceDeathTest_Returns0ByDefault_Test` |  |
| [`csrc/common/dtype.cc`](csrc/common/dtype.cc.md) | 24 | `ToString`, `ToAccumulateType`, `TorchEquivalentBitwidth` | [dtype-and-precision](../concepts/dtype-and-precision.md) |
| [`csrc/common/dtype.h`](csrc/common/dtype.h.md) | 7 | `ConvertTo`, `ConvertTo`, `ConvertTo` | [dtype-and-precision](../concepts/dtype-and-precision.md) |
| [`csrc/common/dynamism_utils.cc`](csrc/common/dynamism_utils.cc.md) | 2 | `GetTraversalOutputDimensions`, `GetTraversalOutputDimensions` |  |
| [`csrc/common/dynamism_utils.h`](csrc/common/dynamism_utils.h.md) | 3 | `DeviceRefDimensions`, `dims`, `ref` |  |
| [`csrc/common/dynamism_utils_test.cc`](csrc/common/dynamism_utils_test.cc.md) | 24 | `context_`, `DynamismOpsBuilder`, `getContext` |  |
| [`csrc/common/env_vars.h`](csrc/common/env_vars.h.md) | 128 | `GetEnvOnce`, `GetBooleanEnvOnce`, `SetEnv` |  |
| [`csrc/common/env_vars_test.cc`](csrc/common/env_vars_test.cc.md) | 118 | `WarningCapture`, `messages`, `WarningCapture` |  |
| [`csrc/common/environment.cc`](csrc/common/environment.cc.md) | 10 | `InitializeDistributedEnvironment`, `InitializeSingleDeviceEnvironment`, `AssignMegascalePorts` |  |
| [`csrc/common/environment_test.cc`](csrc/common/environment_test.cc.md) | 211 | `ExitedWithCode`, `MultisliceConfig`, `InitAndPrintMegascalePorts` |  |
| [`csrc/common/error_utils.cc`](csrc/common/error_utils.cc.md) | 46 | `TtError`, `TranslateToC10ErrorAndThrow`, `SafeWrapDim` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md), [error-handling](../concepts/error-handling.md) |
| [`csrc/common/error_utils.h`](csrc/common/error_utils.h.md) | 142 | `is_status_or_ref`, `ReturnIfErrorAdaptor`, `TtError` | [error-handling](../concepts/error-handling.md), [stablehlo-op-builder](../concepts/stablehlo-op-builder.md) |
| [`csrc/common/error_utils_cpp_context_test.cc`](csrc/common/error_utils_cpp_context_test.cc.md) | 79 | `kCppErrorTraceUrl`, `TtRetCheckFail`, `TtRetCheckFailStatusOr` |  |
| [`csrc/common/error_utils_test.cc`](csrc/common/error_utils_test.cc.md) | 1192 | `ThrowsTtError`, `HasSubstr`, `ScopedFakeProcDir` |  |
| [`csrc/common/error_utils_test_helper.h`](csrc/common/error_utils_test_helper.h.md) | 1 | `MakeErrorFromHeader` |  |
| [`csrc/common/excess_precision.cc`](csrc/common/excess_precision.cc.md) | 8 | `ExcessPrecisionState`, `GetAllowExcessPrecision`, `GetDefaultExecutableBuildOptions` | [dtype-and-precision](../concepts/dtype-and-precision.md) |
| [`csrc/common/fingerprint_utils.h`](csrc/common/fingerprint_utils.h.md) | 15 | `Fingerprint`, `FingerprintType`, `FingerprintCat` | [compilation-cache-key](../concepts/compilation-cache-key.md) |
| [`csrc/common/fingerprint_utils_test.cc`](csrc/common/fingerprint_utils_test.cc.md) | 180 | `FingerprintCat_WorksForMultipleArgs_Test`, `FingerprintCat_WorksForOneArg_Test`, `FingerprintCat_WorksForZeroArgs_Test` |  |
| [`csrc/common/fixed_size_span.h`](csrc/common/fixed_size_span.h.md) | 19 | `FixedSizeSpan`, `tuple_size`, `MoveToStdArray` |  |
| [`csrc/common/flags.h`](csrc/common/flags.h.md) | 1 | `GetFlagOnce` |  |
| [`csrc/common/flags_test.cc`](csrc/common/flags_test.cc.md) | 81 | `FLAGS_multi_test_flag_1`, `FLAGS_multi_test_flag_2`, `FLAGS_test_bool_flag` |  |
| [`csrc/common/layout_utils.cc`](csrc/common/layout_utils.cc.md) | 1 | `ResolveTpuLayout` |  |
| [`csrc/common/layout_utils.h`](csrc/common/layout_utils.h.md) | 5 | `element_type`, `sizes`, `TpuLayout` |  |
| [`csrc/common/layout_utils_test.cc`](csrc/common/layout_utils_test.cc.md) | 81 | `TestBody`, `TestBody`, `TestBody` |  |
| [`csrc/common/libtpu_version.cc`](csrc/common/libtpu_version.cc.md) | 9 | `SetLibtpuVersion`, `GetLibtpuVersion`, `GetLibtpuVersionString` |  |
| [`csrc/common/libtpu_version_test.cc`](csrc/common/libtpu_version_test.cc.md) | 93 | `LibtpuVersionTest`, `LibtpuVersionTest_CompareVersion_Test`, `LibtpuVersionTest_InitialValueIsUnsetInFreshProcess_Test` |  |
| [`csrc/common/macro_utils.cc`](csrc/common/macro_utils.cc.md) | 2 | `NormalizeIfInsideBuildDirectory`, `ArgsAsStrings` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md) |
| [`csrc/common/macro_utils.h`](csrc/common/macro_utils.h.md) | 5 | `ArgsAreIdentifiers`, `kDebugMode`, `IsWhitespace` |  |
| [`csrc/common/op_name_stack.cc`](csrc/common/op_name_stack.cc.md) | 5 | `MaybeTop`, `stack_`, `Top` | [op-names-and-python-context](../concepts/op-names-and-python-context.md) |
| [`csrc/common/op_name_stack.h`](csrc/common/op_name_stack.h.md) | 6 | `ScopedOpName`, `ScopedOpName`, `OpNameStack` | [dynamic-shape-ops](../concepts/dynamic-shape-ops.md), [op-names-and-python-context](../concepts/op-names-and-python-context.md) |
| [`csrc/common/op_name_stack_test.cc`](csrc/common/op_name_stack_test.cc.md) | 27 | `TestBody`, `TestBody`, `OpNameStackTest_EmptyStackReturnsNullopt_Test` |  |
| [`csrc/common/oss_test_main.cc`](csrc/common/oss_test_main.cc.md) | 1 | `main` |  |
| [`csrc/common/pybind_error_utils.h`](csrc/common/pybind_error_utils.h.md) | 35 | `PyBindModule`, `PyBindModule`, `def` |  |
| [`csrc/common/pybind_error_utils_test.cc`](csrc/common/pybind_error_utils_test.cc.md) | 34 | `TestHelperRaises`, `HasSubstr`, `ThrowingMember` |  |
| [`csrc/common/reroute_warnings.cc`](csrc/common/reroute_warnings.cc.md) | 10 | `SurfaceReroutedWarnings`, `RouteWarningsOnThisThreadToDispatchThread`, `mu_` |  |
| [`csrc/common/reroute_warnings_test.cc`](csrc/common/reroute_warnings_test.cc.md) | 105 | `WarningCapture`, `WarningCapture`, `ReroutedWarningsTest` |  |
| [`csrc/common/shape.cc`](csrc/common/shape.cc.md) | 2 | `ToString`, `MakeShape` |  |
| [`csrc/common/shape.h`](csrc/common/shape.h.md) | 32 | `Shape`, `Shape`, `dtype` |  |
| [`csrc/common/static_shape_check.cc`](csrc/common/static_shape_check.cc.md) | 5 | `ValidateStaticShape`, `ValidateStaticShapeImpl`, `ValidateStaticShape` |  |
| [`csrc/common/status_builder.cc`](csrc/common/status_builder.cc.md) | 18 | `MaybeAddCppSourceLoc`, `SetRootOpNamePayload`, `StatusBuilder` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md), [error-handling](../concepts/error-handling.md) |
| [`csrc/common/status_builder.h`](csrc/common/status_builder.h.md) | 36 | `operator<<`, `operator<<`, `operator<<` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md), [error-handling](../concepts/error-handling.md) |
| [`csrc/common/status_test_utils_test.cc`](csrc/common/status_test_utils_test.cc.md) | 87 | `Execute`, `Execute`, `Execute` |  |
| [`csrc/common/symbol_stage.h`](csrc/common/symbol_stage.h.md) | 23 | `SymbolStage`, `Stage`, `is_deprecated` |  |
| [`csrc/common/symbol_stage_test.cc`](csrc/common/symbol_stage_test.cc.md) | 60 | `kInternalImplementationStage`, `kExperimentalStage`, `kDeprecatedStage` |  |
| [`csrc/common/thread_pool.cc`](csrc/common/thread_pool.cc.md) | 1 | `ThreadPool` |  |
| [`csrc/common/thread_pool.h`](csrc/common/thread_pool.h.md) | 8 | `ThreadPool`, `Schedule`, `pool_` |  |
| [`csrc/common/tier2_compilation_cache.cc`](csrc/common/tier2_compilation_cache.cc.md) | 28 | `GetTier2CacheEntryPath`, `Tier2CacheEntryLock`, `MappedCacheEntry` |  |
| [`csrc/common/tier2_compilation_cache.h`](csrc/common/tier2_compilation_cache.h.md) | 13 | `Tier2CacheEntryLock`, `Tier2CacheEntryStats`, `key_` |  |
| [`csrc/common/tier2_compilation_cache_enablement_test.cc`](csrc/common/tier2_compilation_cache_enablement_test.cc.md) | 18 | `FLAGS_expected_tier2_cache_name`, `TestBody`, `Tier2CompilationCacheEnablementTest_Tier2CacheName_Test` |  |
| [`csrc/common/tier2_compilation_cache_test.cc`](csrc/common/tier2_compilation_cache_test.cc.md) | 97 | `MakeCacheKey`, `Tier2CacheTest`, `cache_path_` |  |
| [`csrc/common/tier3_compilation_cache.cc`](csrc/common/tier3_compilation_cache.cc.md) | 7 | `GetTier3CacheEntryPath`, `GetFromTier3Cache`, `UsesTier3CompilationCache` |  |
| [`csrc/common/tier3_compilation_cache_enablement_test.cc`](csrc/common/tier3_compilation_cache_enablement_test.cc.md) | 18 | `FLAGS_expected_tier3_cache_root`, `Tier3CompilationCacheEnablementTest_Tier3CacheRootDir_Test`, `TestBody` |  |
| [`csrc/common/tier3_compilation_cache_test.cc`](csrc/common/tier3_compilation_cache_test.cc.md) | 43 | `Tier3CompilationCacheTest`, `MakeCacheKey`, `Tier3CompilationCacheTest_GetFromTier3CacheFailsIfCacheFileDoesNotExist_Test` |  |
| [`csrc/common/to_string.cc`](csrc/common/to_string.cc.md) | 12 | `ToString`, `ToString`, `ToString` | [dtype-and-precision](../concepts/dtype-and-precision.md) |
| [`csrc/common/to_string.h`](csrc/common/to_string.h.md) | 23 | `ToString`, `ToString`, `ToString` |  |
| [`csrc/common/unique_file_descriptor.h`](csrc/common/unique_file_descriptor.h.md) | 13 | `UniqueFileDescriptor`, `valid`, `fd_` |  |
| [`csrc/common/utils.cc`](csrc/common/utils.cc.md) | 6 | `LosslessToString`, `TensorHasTrivialLayout`, `PercAsStr` |  |
| [`csrc/common/utils.h`](csrc/common/utils.h.md) | 19 | `CopyIntVector`, `CopyIntVector`, `CopyIntVector` |  |
| [`csrc/common/utils_test.cc`](csrc/common/utils_test.cc.md) | 27 | `LosslessToString_WorksForNegativeDoubles_Test`, `LosslessToString_WorksForPositiveDoubles_Test`, `LosslessToString_WorksForZero_Test` |  |
| [`csrc/common/version.cc`](csrc/common/version.cc.md) | 3 | `Parse`, `DieOnNegativeComponent`, `ParseOptionalComponent` |  |
| [`csrc/common/version.h`](csrc/common/version.h.md) | 10 | `Version`, `Version`, `Max` |  |
| [`csrc/common/version_test.cc`](csrc/common/version_test.cc.md) | 93 | `IsOkAndHolds`, `StatusIs`, `TestBody` |  |
| [`csrc/common/warnings.h`](csrc/common/warnings.h.md) | 12 | `WarningCategory`, `GetWarningPrefix`, `IsDeprecationWarning` |  |

## `csrc/distributed`

Index: [`symbols/csrc-distributed.tsv`](symbols/csrc-distributed.tsv) (364 rows), [`edges/csrc-distributed.tsv`](edges/csrc-distributed.tsv) (820 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`csrc/distributed/allgather.cc`](csrc/distributed/allgather.cc.md) | 2 | `BuildDistributedAllGatherShlo`, `BuildDistributedAllGatherShlo` |  |
| [`csrc/distributed/allgather.h`](csrc/distributed/allgather.h.md) | 4 | `AllGatherOutputMode`, `kConcat`, `kList` |  |
| [`csrc/distributed/allreduce.cc`](csrc/distributed/allreduce.cc.md) | 1 | `BuildDistributedAllReduceShlo` |  |
| [`csrc/distributed/alltoall.cc`](csrc/distributed/alltoall.cc.md) | 7 | `BuildDistributedAllToAllBaseShlo`, `BuildDistributedAllToAllBaseUnevenSplitsShlo`, `ConcatenateTensorsAlongDim0` |  |
| [`csrc/distributed/handshake.cc`](csrc/distributed/handshake.cc.md) | 1 | `GetHandshakeStageEnvVarOnce` |  |
| [`csrc/distributed/handshake.h`](csrc/distributed/handshake.h.md) | 4 | `HandshakeStage`, `kDispatchStage`, `kCompileStage` |  |
| [`csrc/distributed/handshake_test.cc`](csrc/distributed/handshake_test.cc.md) | 9 | `HandshakeDeathTest_FatalOnInvalidHandshakeStage_Test`, `TestBody`, `HandshakeDeathTest_FatalOnInvalidHandshakeStage_Test` |  |
| [`csrc/distributed/process_group_tpu.cc`](csrc/distributed/process_group_tpu.cc.md) | 148 | `TpuWork`, `GetCollectiveSplitMode`, `WorldTopology` | [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md), [op-names-and-python-context](../concepts/op-names-and-python-context.md), [process-group-and-collectives](../concepts/process-group-and-collectives.md) |
| [`csrc/distributed/process_group_tpu.h`](csrc/distributed/process_group_tpu.h.md) | 23 | `ProcessGroupTpu`, `replica_groups_`, `device_assignment` | [process-group-and-collectives](../concepts/process-group-and-collectives.md) |
| [`csrc/distributed/process_group_tpu_test.cc`](csrc/distributed/process_group_tpu_test.cc.md) | 177 | `AllGatherRankResult`, `AllGatherRankSpec`, `RunAllGather` |  |
| [`csrc/distributed/reduce_scatter.cc`](csrc/distributed/reduce_scatter.cc.md) | 1 | `BuildDistributedReduceScatterShlo` | [process-group-and-collectives](../concepts/process-group-and-collectives.md) |
| [`csrc/distributed/slicebuilder/discovery.cc`](csrc/distributed/slicebuilder/discovery.cc.md) | 2 | `GetDistributedWorkerConfiguration`, `ValidateRequiredDistributedEnvVars` | [process-group-and-collectives](../concepts/process-group-and-collectives.md) |
| [`csrc/distributed/slicebuilder/discovery.h`](csrc/distributed/slicebuilder/discovery.h.md) | 10 | `DistributedWorkerConfiguration`, `rank`, `sb_addrs` | [process-group-and-collectives](../concepts/process-group-and-collectives.md) |
| [`csrc/distributed/slicebuilder/discovery_test.cc`](csrc/distributed/slicebuilder/discovery_test.cc.md) | 28 | `ExitedWithCode`, `TestBody`, `TestBody` |  |
| [`csrc/distributed/types.cc`](csrc/distributed/types.cc.md) | 6 | `operator<<`, `DeviceGroupList`, `DeviceGroupList` | [process-group-and-collectives](../concepts/process-group-and-collectives.md) |
| [`csrc/distributed/types.h`](csrc/distributed/types.h.md) | 19 | `DeviceGroupList`, `DeviceGroup`, `groups_` | [compilation-cache-key](../concepts/compilation-cache-key.md), [process-group-and-collectives](../concepts/process-group-and-collectives.md) |
| [`csrc/distributed/types_test.cc`](csrc/distributed/types_test.cc.md) | 36 | `DeviceGroupListTest_EqualityAndInequality_Test`, `DeviceGroupListTest_Normalization_Test`, `DeviceGroupListTest_PreservesOrderWhenNormalizeIsFalse_Test` |  |
| [`csrc/distributed/utils.cc`](csrc/distributed/utils.cc.md) | 7 | `BuildReplicaGroupsAttr`, `BuildChannelHandleAttr`, `ValidateReductionOp` | [process-group-and-collectives](../concepts/process-group-and-collectives.md) |
| [`csrc/distributed/window_tpu.cc`](csrc/distributed/window_tpu.cc.md) | 9 | `PyGetWindowNumStripes`, `PyGetWindowStripeChunkMb`, `g_window_num_stripes` | [process-group-and-collectives](../concepts/process-group-and-collectives.md) |

## `csrc/eager`

Index: [`symbols/csrc-eager.tsv`](symbols/csrc-eager.tsv) (1412 rows), [`edges/csrc-eager.tsv`](edges/csrc-eager.tsv) (5604 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`csrc/eager/amp_policies.cc`](csrc/eager/amp_policies.cc.md) | 4 | `TORCH_LIBRARY_IMPL_init_aten_AutocastPrivateUse1_3`, `TORCH_LIBRARY_IMPL_init___AutocastPrivateUse1_2`, `TORCH_LIBRARY_IMPL_static_init___AutocastPrivateUse1_2` |  |
| [`csrc/eager/current_stream.cc`](csrc/eager/current_stream.cc.md) | 11 | `GetCurrentDeviceStreamId`, `kMaxDevices`, `ExchangeCurrentDeviceIndex` | [device-streams-generators-and-rng](../concepts/device-streams-generators-and-rng.md) |
| [`csrc/eager/current_stream.h`](csrc/eager/current_stream.h.md) | 5 | `StreamId`, `DeviceIndex`, `DeviceStreamId` |  |
| [`csrc/eager/defer_and_fuse_enablement_test.cc`](csrc/eager/defer_and_fuse_enablement_test.cc.md) | 18 | `FLAGS_expected_defer_and_fuse`, `DeferAndFuseEnablementTest_EagerMode_Test`, `TestBody` |  |
| [`csrc/eager/device_assignment_pipeline.cc`](csrc/eager/device_assignment_pipeline.cc.md) | 16 | `RewriteAndTileOperationForSubgroup`, `ResolveDeviceAssignment`, `ApplySubgroupTilingOrReplicaRewriting` |  |
| [`csrc/eager/device_assignment_pipeline.h`](csrc/eager/device_assignment_pipeline.h.md) | 5 | `OpDeviceAssignment`, `PallasDeviceAssignment`, `device_assignment` |  |
| [`csrc/eager/device_assignment_pipeline_test.cc`](csrc/eager/device_assignment_pipeline_test.cc.md) | 115 | `ExtractDenseIntAttrValues`, `PhysicalGroups`, `SliceOf` |  |
| [`csrc/eager/device_buffer.cc`](csrc/eager/device_buffer.cc.md) | 72 | `CreateDeferred`, `dimensions`, `element_type` | [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md), [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md) |
| [`csrc/eager/device_buffer.h`](csrc/eager/device_buffer.h.md) | 128 | `DeviceBufferRef`, `DeviceBufferRef`, `DeviceBufferList` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md), [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md), [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md) |
| [`csrc/eager/device_buffer_utils.cc`](csrc/eager/device_buffer_utils.cc.md) | 29 | `CreateZeroSizeDeviceBufferRef`, `CreateEmptyDeviceBufferRef`, `CreateDeferredDeviceBufferList` | [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md) |
| [`csrc/eager/device_buffer_utils.h`](csrc/eager/device_buffer_utils.h.md) | 10 | `DeferredOpParams`, `op_builder`, `output_shapes` |  |
| [`csrc/eager/device_buffer_utils_test.cc`](csrc/eager/device_buffer_utils_test.cc.md) | 11 | `TestBody`, `DeviceBufferUtilsTest_ComputeConstantDeviceBufferRefOpParamCacheKeysMatchesGoldenMap_Test`, `Pair` |  |
| [`csrc/eager/device_gen_impl.cc`](csrc/eager/device_gen_impl.cc.md) | 83 | `DeviceGenerators`, `GetDefaultDeviceGenerator`, `GetDefaultInstance` | [device-streams-generators-and-rng](../concepts/device-streams-generators-and-rng.md) |
| [`csrc/eager/device_gen_impl.h`](csrc/eager/device_gen_impl.h.md) | 34 | `DeviceGeneratorImplBase`, `EagerModeDeviceGeneratorImpl`, `ExportModeDeviceGeneratorImpl` | [device-streams-generators-and-rng](../concepts/device-streams-generators-and-rng.md) |
| [`csrc/eager/eager_mode.cc`](csrc/eager/eager_mode.cc.md) | 8 | `GetEagerMode`, `SetEagerMode`, `IsInplaceBufferDonationEnabled` | [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md) |
| [`csrc/eager/eager_mode.h`](csrc/eager/eager_mode.h.md) | 1 | `IsDeferNeverMode` | [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md) |
| [`csrc/eager/events_queue.cc`](csrc/eager/events_queue.cc.md) | 124 | `ClearAllStreams`, `PrepareSnapshotMaterializations`, `Record` | [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md) |
| [`csrc/eager/events_queue.h`](csrc/eager/events_queue.h.md) | 28 | `EventSnapshot`, `MaterializationMode`, `traversals` | [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md) |
| [`csrc/eager/events_queue_test.cc`](csrc/eager/events_queue_test.cc.md) | 274 | `EventsQueueTest`, `DummyBuilder`, `EventsQueueTest_ClearsBuffersAfterMaterialization_Test` |  |
| [`csrc/eager/execution_task.cc`](csrc/eager/execution_task.cc.md) | 33 | `SetOutputNodesAsError`, `RunInternal`, `FromTraversal` |  |
| [`csrc/eager/execution_task.h`](csrc/eager/execution_task.h.md) | 8 | `ExecutionTask`, `outputs_`, `compiled_kernel_` |  |
| [`csrc/eager/launch_blocking_enablement_test.cc`](csrc/eager/launch_blocking_enablement_test.cc.md) | 18 | `FLAGS_expected_launch_blocking`, `LaunchBlockingEnablementTest_EagerMode_Test`, `TestBody` |  |
| [`csrc/eager/materialization_heuristics.cc`](csrc/eager/materialization_heuristics.cc.md) | 1 | `IsFastRuntimeConvolutionCandidate` |  |
| [`csrc/eager/materialization_heuristics_test.cc`](csrc/eager/materialization_heuristics_test.cc.md) | 10 | `TestBody`, `DummyBuilder`, `MaterializeHeuristicsTest_IsFastRuntimeConvolutionCandidate_Test` |  |
| [`csrc/eager/materialize.cc`](csrc/eager/materialize.cc.md) | 69 | `Materialize`, `Materialize`, `MaterializationWorker` |  |
| [`csrc/eager/materialize.h`](csrc/eager/materialize.h.md) | 5 | `MaterializationBlockMode`, `kBlockUntilStarted`, `Materialize` | [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md) |
| [`csrc/eager/materialize_test.cc`](csrc/eager/materialize_test.cc.md) | 54 | `CreateOp`, `MaterializeTest`, `CreateView` |  |
| [`csrc/eager/op_dispatcher.cc`](csrc/eager/op_dispatcher.cc.md) | 15 | `PromoteScalar`, `MakeTensor`, `PromoteScalar` | [eager-op-dispatch](../concepts/eager-op-dispatch.md) |
| [`csrc/eager/op_dispatcher.h`](csrc/eager/op_dispatcher.h.md) | 32 | `DispatchOp`, `DispatchOp`, `DispatchOpOut` | [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md), [eager-op-dispatch](../concepts/eager-op-dispatch.md) |
| [`csrc/eager/op_dispatcher_test.cc`](csrc/eager/op_dispatcher_test.cc.md) | 109 | `AutoDonateInPlaceBuffer`, `TestBody`, `TestBody` |  |
| [`csrc/eager/shutdown_test.cc`](csrc/eager/shutdown_test.cc.md) | 9 | `TestBody`, `ShutdownTest_E2EShutdownCompletes_Test`, `ShutdownTest_E2EShutdownCompletes_Test` |  |
| [`csrc/eager/split_traversal.cc`](csrc/eager/split_traversal.cc.md) | 6 | `SplitTraversal`, `SplitTraversal`, `SplitAllMaterializationPoints` |  |
| [`csrc/eager/split_traversal_test.cc`](csrc/eager/split_traversal_test.cc.md) | 10 | `TestBody`, `SplitTraversalTest_ApplySplitPointsSorted_Test`, `DummyBuilder` |  |
| [`csrc/eager/structured_log_buffer.cc`](csrc/eager/structured_log_buffer.cc.md) | 4 | `GetInstance`, `Push`, `Drain` |  |
| [`csrc/eager/structured_log_buffer.h`](csrc/eager/structured_log_buffer.h.md) | 37 | `ToString`, `MaterializationReason`, `kExplicitSync` | [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md) |
| [`csrc/eager/structured_log_buffer_test.cc`](csrc/eager/structured_log_buffer_test.cc.md) | 49 | `StructuredLogBufferTest`, `StructuredLogBufferTest_ConcurrentPushIsSafe_Test`, `StructuredLogBufferTest_DisabledBufferDropsEvents_Test` |  |
| [`csrc/eager/tensor_to_buffer.cc`](csrc/eager/tensor_to_buffer.cc.md) | 55 | `MakeTensor`, `MakeEmptyTensor`, `AssignBufferToAtTensor` | [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md), [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md), [eager-op-dispatch](../concepts/eager-op-dispatch.md) |
| [`csrc/eager/tpu_aten_kernels.cc`](csrc/eager/tpu_aten_kernels.cc.md) | 38 | `ImplStable`, `ImplInternal`, `ImplWrapperHelper` | [host-device-copy](../concepts/host-device-copy.md), [op-names-and-python-context](../concepts/op-names-and-python-context.md) |
| [`csrc/eager/tpu_hooks.cc`](csrc/eager/tpu_hooks.cc.md) | 38 | `TpuDeviceGuardImpl`, `ValidateDevice`, `type` |  |
| [`csrc/eager/traversal.cc`](csrc/eager/traversal.cc.md) | 92 | `Create`, `GetCacheKey`, `BuildMlirModule` | [compilation-pipeline](../concepts/compilation-pipeline.md), [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md) |
| [`csrc/eager/traversal.h`](csrc/eager/traversal.h.md) | 27 | `Traversal`, `execution_order`, `outputs` |  |
| [`csrc/eager/traversal_test.cc`](csrc/eager/traversal_test.cc.md) | 142 | `TraversalTest`, `DummyBuilder`, `shape_` |  |

## `csrc/experimental`

Index: [`symbols/csrc-experimental.tsv`](symbols/csrc-experimental.tsv) (132 rows), [`edges/csrc-experimental.tsv`](edges/csrc-experimental.tsv) (242 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`csrc/experimental/batch_transfer/batch_transfer.cc`](csrc/experimental/batch_transfer/batch_transfer.cc.md) | 25 | `RawBufferHolder`, `Await`, `AndThen` | [batch-host-device-transfer](../concepts/batch-host-device-transfer.md) |
| [`csrc/experimental/batch_transfer/batch_transfer.h`](csrc/experimental/batch_transfer/batch_transfer.h.md) | 10 | `TransferFuture`, `futures_`, `holds_` | [batch-host-device-transfer](../concepts/batch-host-device-transfer.md) |
| [`csrc/experimental/precompiled_kernels/kernel_test_utils.cc`](csrc/experimental/precompiled_kernels/kernel_test_utils.cc.md) | 1 | `CreateKernelTestClient` | [batch-host-device-transfer](../concepts/batch-host-device-transfer.md) |
| [`csrc/experimental/precompiled_kernels/mosaic_custom_call.cc`](csrc/experimental/precompiled_kernels/mosaic_custom_call.cc.md) | 2 | `BuildMosaicCustomCall`, `SerializeMosaic` | [batch-host-device-transfer](../concepts/batch-host-device-transfer.md) |
| [`csrc/experimental/precompiled_kernels/mosaic_custom_call_test.cc`](csrc/experimental/precompiled_kernels/mosaic_custom_call_test.cc.md) | 9 | `TestBody`, `DynamicMosaic_CopiesDifferentShapesWithOneExecutable_Test`, `DynamicMosaic_CopiesDifferentShapesWithOneExecutable_Test` |  |
| [`csrc/experimental/precompiled_kernels/nonzero_indices.cc`](csrc/experimental/precompiled_kernels/nonzero_indices.cc.md) | 42 | `b_`, `Const`, `And` | [batch-host-device-transfer](../concepts/batch-host-device-transfer.md) |
| [`csrc/experimental/precompiled_kernels/nonzero_indices_test.cc`](csrc/experimental/precompiled_kernels/nonzero_indices_test.cc.md) | 66 | `client_`, `PrepareOperands`, `NonzeroIndicesTest` |  |

## `csrc/internal`

Index: [`symbols/csrc-internal.tsv`](symbols/csrc-internal.tsv) (1127 rows), [`edges/csrc-internal.tsv`](edges/csrc-internal.tsv) (2814 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`csrc/internal/batch_transfer/batch_transfer_impl.cc`](csrc/internal/batch_transfer/batch_transfer_impl.cc.md) | 8 | `TorchTpuPyBindInitModule_batch_transfer_impl`, `PyBatchTransferH2DSync`, `PyBatchTransferD2HSync` |  |
| [`csrc/internal/compile/compiled_mode.cc`](csrc/internal/compile/compiled_mode.cc.md) | 33 | `CompileMlirExecutable`, `ExecuteCompiledModel`, `MakePlaceholder` | [compiled-mode](../concepts/compiled-mode.md) |
| [`csrc/internal/compile/compiled_mode.h`](csrc/internal/compile/compiled_mode.h.md) | 25 | `AsyncCompileResult`, `OutputShape`, `CompileResult` | [compiled-mode](../concepts/compiled-mode.md) |
| [`csrc/internal/compile/dispatch_scan.cc`](csrc/internal/compile/dispatch_scan.cc.md) | 91 | `SymVal`, `PyCreateScanOp`, `Tag` | [compiled-mode](../concepts/compiled-mode.md) |
| [`csrc/internal/compile/dispatch_scan_test.cc`](csrc/internal/compile/dispatch_scan_test.cc.md) | 305 | `DispatchScanTest`, `HasSubstr`, `MakePlaceholderI32` |  |
| [`csrc/internal/compile/tpu_torch_compile.cc`](csrc/internal/compile/tpu_torch_compile.cc.md) | 144 | `RawPyObjPtr`, `PyLayout`, `PySetDeviceStateTensor` | [compiled-mode](../concepts/compiled-mode.md) |
| [`csrc/internal/compiler_options/compiler_options_impl.cc`](csrc/internal/compiler_options/compiler_options_impl.cc.md) | 4 | `PushCompilerOptions`, `TorchTpuPyBindInitModule_compiler_options_impl`, `pybind11_exec_compiler_options_impl` |  |
| [`csrc/internal/distributed/tpu_distributed.cc`](csrc/internal/distributed/tpu_distributed.cc.md) | 9 | `TorchTpuPyBindInitModule_tpu_distributed`, `GetGlobalDeviceId`, `DeviceDebugString` |  |
| [`csrc/internal/dynamism/dynamism.cc`](csrc/internal/dynamism/dynamism.cc.md) | 2 | `MarkDynamic`, `GetDynamismInfo` |  |
| [`csrc/internal/dynamism/dynamism_ops.cc`](csrc/internal/dynamism/dynamism_ops.cc.md) | 6 | `GetPadModule`, `GetSliceModule`, `Pad` |  |
| [`csrc/internal/dynamism/dynamism_ops_test.cc`](csrc/internal/dynamism/dynamism_ops_test.cc.md) | 22 | `DynamismOpsBuilder`, `getContext`, `context_` |  |
| [`csrc/internal/dynamism/dynamism_py.cc`](csrc/internal/dynamism/dynamism_py.cc.md) | 5 | `PyMarkDynamic`, `PyGetDynamismInfo`, `TorchTpuPyBindInitModule__tpu_torch_dynamism` |  |
| [`csrc/internal/env.cc`](csrc/internal/env.cc.md) | 6 | `TorchTpuPyBindInitModule_env`, `PyGetIntegerEnvOnce`, `PyGetStringEnvOnce` |  |
| [`csrc/internal/execution_mode/execution_mode_impl.cc`](csrc/internal/execution_mode/execution_mode_impl.cc.md) | 3 | `TorchTpuPyBindInitModule_execution_mode_impl`, `pybind11_exec_execution_mode_impl`, `pybind11_init_execution_mode_impl` |  |
| [`csrc/internal/mosaic/dialect/torch_tpu_mosaic_dialect.cc`](csrc/internal/mosaic/dialect/torch_tpu_mosaic_dialect.cc.md) | 1 | `initialize` |  |
| [`csrc/internal/mosaic/kiln/core/cond.cc`](csrc/internal/mosaic/kiln/core/cond.cc.md) | 4 | `Cond`, `operator!`, `operator&&` |  |
| [`csrc/internal/mosaic/kiln/core/cond.h`](csrc/internal/mosaic/kiln/core/cond.h.md) | 1 | `Cond` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md) |
| [`csrc/internal/mosaic/kiln/core/context.cc`](csrc/internal/mosaic/kiln/core/context.cc.md) | 11 | `CurrentBuilder`, `ToMlirType`, `ToMlirType` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md) |
| [`csrc/internal/mosaic/kiln/core/context.h`](csrc/internal/mosaic/kiln/core/context.h.md) | 9 | `unwrap`, `wrap`, `ValueAccess` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md) |
| [`csrc/internal/mosaic/kiln/core/control_flow.cc`](csrc/internal/mosaic/kiln/core/control_flow.cc.md) | 4 | `If`, `For`, `If` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md) |
| [`csrc/internal/mosaic/kiln/core/control_flow.h`](csrc/internal/mosaic/kiln/core/control_flow.h.md) | 1 | `For` |  |
| [`csrc/internal/mosaic/kiln/core/dtype.h`](csrc/internal/mosaic/kiln/core/dtype.h.md) | 45 | `DType`, `Kind`, `Float32Type` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md) |
| [`csrc/internal/mosaic/kiln/core/elementwise.h`](csrc/internal/mosaic/kiln/core/elementwise.h.md) | 42 | `ElementwiseOps`, `Ops`, `AsType` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md) |
| [`csrc/internal/mosaic/kiln/core/elementwise_impl.cc`](csrc/internal/mosaic/kiln/core/elementwise_impl.cc.md) | 4 | `EmitBroadcast`, `AlignShapes`, `BroadcastShapes` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md) |
| [`csrc/internal/mosaic/kiln/core/elementwise_impl.h`](csrc/internal/mosaic/kiln/core/elementwise_impl.h.md) | 38 | `Compare`, `UnaryFloat`, `Compare` |  |
| [`csrc/internal/mosaic/kiln/core/index_arg.h`](csrc/internal/mosaic/kiln/core/index_arg.h.md) | 7 | `IndexArg`, `IndexArg`, `val_` |  |
| [`csrc/internal/mosaic/kiln/core/index_map.h`](csrc/internal/mosaic/kiln/core/index_map.h.md) | 8 | `IndexMap`, `IndexIndices`, `mapping_` |  |
| [`csrc/internal/mosaic/kiln/core/kernel.cc`](csrc/internal/mosaic/kiln/core/kernel.cc.md) | 39 | `ProgramId`, `CurrentScope`, `KernelScope` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md), [mosaic-matmul](../concepts/mosaic-matmul.md) |
| [`csrc/internal/mosaic/kiln/core/kernel.h`](csrc/internal/mosaic/kiln/core/kernel.h.md) | 12 | `Kernel`, `CreateKernel`, `impl_` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md) |
| [`csrc/internal/mosaic/kiln/core/literal.h`](csrc/internal/mosaic/kiln/core/literal.h.md) | 46 | `Literal`, `Literal`, `Select` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md) |
| [`csrc/internal/mosaic/kiln/core/ref.cc`](csrc/internal/mosaic/kiln/core/ref.cc.md) | 14 | `operator=`, `rank`, `MemRefTypeOf` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md) |
| [`csrc/internal/mosaic/kiln/core/ref.h`](csrc/internal/mosaic/kiln/core/ref.h.md) | 20 | `Ref`, `DimDesc`, `operator()` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md) |
| [`csrc/internal/mosaic/kiln/core/scalar.cc`](csrc/internal/mosaic/kiln/core/scalar.cc.md) | 8 | `I32`, `MakeScalarConstant`, `F32` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md), [stablehlo-op-builder](../concepts/stablehlo-op-builder.md) |
| [`csrc/internal/mosaic/kiln/core/scalar.h`](csrc/internal/mosaic/kiln/core/scalar.h.md) | 1 | `Scalar` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md) |
| [`csrc/internal/mosaic/kiln/core/specs.h`](csrc/internal/mosaic/kiln/core/specs.h.md) | 35 | `GridSpec`, `InSpec`, `OutSpec` | [mosaic-matmul](../concepts/mosaic-matmul.md) |
| [`csrc/internal/mosaic/kiln/core/tile.cc`](csrc/internal/mosaic/kiln/core/tile.cc.md) | 29 | `shape`, `rank`, `Zeros` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md) |
| [`csrc/internal/mosaic/kiln/core/tile.h`](csrc/internal/mosaic/kiln/core/tile.h.md) | 15 | `Tile`, `ContractPrecision`, `DotOptions` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md) |
| [`csrc/internal/mosaic/kiln/core/value_base.h`](csrc/internal/mosaic/kiln/core/value_base.h.md) | 6 | `dtype`, `ValueBase`, `ValueBase` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md) |
| [`csrc/internal/mosaic/kiln/kiln_test.cc`](csrc/internal/mosaic/kiln/kiln_test.cc.md) | 149 | `KilnTest`, `IsOk`, `ExpectKernelMatches` | [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md), [mosaic-matmul](../concepts/mosaic-matmul.md) |
| [`csrc/internal/mosaic/op_builders.cc`](csrc/internal/mosaic/op_builders.cc.md) | 14 | `CreateMatmul`, `CreateMlirContextWithDialects`, `GetVmemMemRefType` | [mosaic-matmul](../concepts/mosaic-matmul.md) |
| [`csrc/internal/mosaic/op_builders.h`](csrc/internal/mosaic/op_builders.h.md) | 16 | `DimensionSemantics`, `MatmulOptions`, `kArbitrary` | [mosaic-matmul](../concepts/mosaic-matmul.md) |
| [`csrc/internal/pallas/pallas_py.cc`](csrc/internal/pallas/pallas_py.cc.md) | 6 | `PyCallCustomKernel`, `TorchTpuPyBindInitModule_tpu_torch_pallas`, `pybind11_exec_tpu_torch_pallas` |  |
| [`csrc/internal/precision/precision_impl.cc`](csrc/internal/precision/precision_impl.cc.md) | 4 | `TorchTpuPyBindInitModule_precision_impl`, `Precision`, `pybind11_exec_precision_impl` |  |
| [`csrc/internal/profiler/profiler_api.cc`](csrc/internal/profiler/profiler_api.cc.md) | 29 | `TpuProfilerServer`, `TpuProfilerSession`, `mutex_` | [profiler](../concepts/profiler.md) |
| [`csrc/internal/profiler/tpu_profiler_plugin.cc`](csrc/internal/profiler/tpu_profiler_plugin.cc.md) | 34 | `UpdateProfileOptions`, `ProfilerOption`, `UnescapeString` | [profiler](../concepts/profiler.md) |
| [`csrc/internal/profiler/tpu_profiler_plugin.h`](csrc/internal/profiler/tpu_profiler_plugin.h.md) | 28 | `mutex_`, `TpuKinetoProfilerSession`, `errors_` | [profiler](../concepts/profiler.md) |
| [`csrc/internal/profiler/xprof_callback_handler.cc`](csrc/internal/profiler/xprof_callback_handler.cc.md) | 9 | `Register`, `IsProfilerEnabled`, `XProfCallbackHandler` | [profiler](../concepts/profiler.md) |
| [`csrc/internal/profiler/xprof_callback_handler.h`](csrc/internal/profiler/xprof_callback_handler.h.md) | 7 | `XProfCallbackHandler`, `handle_`, `operator=` | [profiler](../concepts/profiler.md) |
| [`csrc/internal/sync/sync.cc`](csrc/internal/sync/sync.cc.md) | 14 | `IsMaterializing`, `SynchronizeTensors`, `SynchronizeTensorsImpl` | [tensor-synchronization](../concepts/tensor-synchronization.md) |
| [`csrc/internal/sync/sync.h`](csrc/internal/sync/sync.h.md) | 3 | `kYes`, `WaitOnExecution`, `kNo` | [tensor-synchronization](../concepts/tensor-synchronization.md) |
| [`csrc/internal/sync/sync_py.cc`](csrc/internal/sync/sync_py.cc.md) | 20 | `UnwrapTensor`, `PySyncSpan`, `TrySyncSingleTensorFast` | [tensor-synchronization](../concepts/tensor-synchronization.md) |
| [`csrc/internal/testing.cc`](csrc/internal/testing.cc.md) | 18 | `TorchTpuPyBindInitModule_testing`, `ThrowTtErrorInFreeFunction`, `ThrowTtErrorInMemberFunction` |  |
| [`csrc/internal/warnings_impl.cc`](csrc/internal/warnings_impl.cc.md) | 3 | `TorchTpuPyBindInitModule_warnings_impl`, `pybind11_exec_warnings_impl`, `pybind11_init_warnings_impl` |  |

## `csrc/mlir`

Index: [`symbols/csrc-mlir.tsv`](symbols/csrc-mlir.tsv) (43 rows), [`edges/csrc-mlir.tsv`](edges/csrc-mlir.tsv) (42 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`csrc/mlir/instrumentation.cc`](csrc/mlir/instrumentation.cc.md) | 7 | `Apply`, `ConfigureInstrumentation`, `NextModuleId` | [mlir-optimization-passes](../concepts/mlir-optimization-passes.md) |
| [`csrc/mlir/instrumentation.h`](csrc/mlir/instrumentation.h.md) | 4 | `InstrumentationState`, `dump_to_print`, `ir_os` | [mlir-optimization-passes](../concepts/mlir-optimization-passes.md) |
| [`csrc/mlir/passes/dummy_pass.cc`](csrc/mlir/passes/dummy_pass.cc.md) | 6 | `DummyPass`, `createDummyPass`, `resolveTypeID` | [mlir-optimization-passes](../concepts/mlir-optimization-passes.md) |
| [`csrc/mlir/passes/reassociate_norm_weights.cc`](csrc/mlir/passes/reassociate_norm_weights.cc.md) | 19 | `createReassociateNormWeightsPass`, `MatchedWeight`, `ReassociateNormWeightsPass` | [mlir-optimization-passes](../concepts/mlir-optimization-passes.md) |
| [`csrc/mlir/pipeline.cc`](csrc/mlir/pipeline.cc.md) | 4 | `RunTorchTpuOptimizationPasses`, `AddTorchTpuOptimizationPasses`, `AddShloPasses` | [mlir-optimization-passes](../concepts/mlir-optimization-passes.md) |
| [`csrc/mlir/pipeline_test.cc`](csrc/mlir/pipeline_test.cc.md) | 13 | `TestBody`, `PipelineTest_RunOptimizationPassesFailsOnInvalidModule_Test`, `HasSubstr` |  |
| [`csrc/mlir/registration.cc`](csrc/mlir/registration.cc.md) | 2 | `RegisterTorchTpuPasses`, `RegisterTorchTpuDialects` | [mlir-optimization-passes](../concepts/mlir-optimization-passes.md) |

## `csrc/ops`

Index: [`symbols/csrc-ops.tsv`](symbols/csrc-ops.tsv) (6821 rows), [`edges/csrc-ops.tsv`](edges/csrc-ops.tsv) (27989 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`csrc/ops/a_min_max/a_min_max.cc`](csrc/ops/a_min_max/a_min_max.cc.md) | 3 | `BuildFusedAMinMaxShlo`, `BuildAMinMaxShlo`, `BuildFusedAMinMaxShlo` |  |
| [`csrc/ops/a_min_max/a_min_max.h`](csrc/ops/a_min_max/a_min_max.h.md) | 3 | `AMinMaxOp`, `kAmax`, `kAmin` |  |
| [`csrc/ops/a_min_max/a_min_max_aten_kernels.cc`](csrc/ops/a_min_max/a_min_max_aten_kernels.cc.md) | 6 | `AtenAminmaxOut`, `AtenAmaxOut`, `AtenAminOut` |  |
| [`csrc/ops/addcdiv/addcdiv_aten_kernels.cc`](csrc/ops/addcdiv/addcdiv_aten_kernels.cc.md) | 2 | `AtenAddcdivOut`, `BuildAddcdivShlo` |  |
| [`csrc/ops/addcmul/addcmul_aten_kernels.cc`](csrc/ops/addcmul/addcmul_aten_kernels.cc.md) | 2 | `AtenAddcmulOut`, `BuildAddcmulShlo` |  |
| [`csrc/ops/addmm/addmm_aten_kernels.cc`](csrc/ops/addmm/addmm_aten_kernels.cc.md) | 12 | `DispatchAddmm`, `AtenAddmmActivationOut`, `AtenAddmmDtypeOut` |  |
| [`csrc/ops/addmv/addmv_aten_kernels.cc`](csrc/ops/addmv/addmv_aten_kernels.cc.md) | 9 | `AtenAddmvOut`, `MatVecDot`, `Addmv` |  |
| [`csrc/ops/all_any/all_any.cc`](csrc/ops/all_any/all_any.cc.md) | 2 | `BuildAnyShlo`, `BuildAllShlo` |  |
| [`csrc/ops/all_any/all_any_aten_kernels.cc`](csrc/ops/all_any/all_any_aten_kernels.cc.md) | 13 | `ValidateAllAnyOut`, `GetAllAnyReductionParams`, `reduced_shape` |  |
| [`csrc/ops/angle/angle_aten_kernels.cc`](csrc/ops/angle/angle_aten_kernels.cc.md) | 3 | `AtenAngleOut`, `AtenAngle`, `BuildAngleShlo` |  |
| [`csrc/ops/ao/ao_offload_kernels.cc`](csrc/ops/ao/ao_offload_kernels.cc.md) | 8 | `AtenAoReload`, `AtenAoOffload`, `AtenAoWaitTensor` |  |
| [`csrc/ops/arange/arange.cc`](csrc/ops/arange/arange.cc.md) | 2 | `BuildArangeOp`, `PrepareScalar` |  |
| [`csrc/ops/arange/arange_aten_kernels.cc`](csrc/ops/arange/arange_aten_kernels.cc.md) | 4 | `AtenArangeStartOut`, `ValidateArangeInputs`, `GetArangeNumElements` |  |
| [`csrc/ops/as_strided/as_strided_aten_kernels.cc`](csrc/ops/as_strided/as_strided_aten_kernels.cc.md) | 2 | `AtenAsStrided`, `AsStrided` |  |
| [`csrc/ops/assertion_aten_kernels.cc`](csrc/ops/assertion_aten_kernels.cc.md) | 6 | `AtenAssertAsyncMsg`, `AtenAssertAsync`, `ScheduleAsyncAssertionCheck` |  |
| [`csrc/ops/baddbmm/baddbmm_aten_kernels.cc`](csrc/ops/baddbmm/baddbmm_aten_kernels.cc.md) | 16 | `ValidateBaddbmmInputs`, `AtenBaddbmmDtype`, `AtenBaddbmmDtypeOut` |  |
| [`csrc/ops/bernoulli/bernoulli_aten_kernels.cc`](csrc/ops/bernoulli/bernoulli_aten_kernels.cc.md) | 10 | `AtenBernoulli_Float`, `AtenBernoulliOut`, `AtenBernoulli_Tensor` |  |
| [`csrc/ops/binary.cc`](csrc/ops/binary.cc.md) | 5 | `BuildAddShlo`, `BuildPowShlo`, `BuildPolarShlo` |  |
| [`csrc/ops/binary.h`](csrc/ops/binary.h.md) | 17 | `BuildMulShlo`, `BuildSubShlo`, `BuildDivShlo` |  |
| [`csrc/ops/binary_aten_kernels.cc`](csrc/ops/binary_aten_kernels.cc.md) | 104 | `TernaryOpOut`, `ValidateAlphaTypeSupported`, `AtenMaximumOut` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md) |
| [`csrc/ops/binary_aten_kernels.h`](csrc/ops/binary_aten_kernels.h.md) | 19 | `BinaryOpOut`, `BinaryOpOptions`, `BinaryOp` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md) |
| [`csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc`](csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc.md) | 9 | `AtenBinaryCrossEntropyBackwardGradInput`, `AtenBinaryCrossEntropy`, `AtenBinaryCrossEntropyBackward` |  |
| [`csrc/ops/bincount/bincount_aten_kernels.cc`](csrc/ops/bincount/bincount_aten_kernels.cc.md) | 2 | `AtenBinCount`, `BuildBinCount` |  |
| [`csrc/ops/bmm/bmm.cc`](csrc/ops/bmm/bmm.cc.md) | 2 | `BuildBmmShlo`, `BuildBmmShlo` |  |
| [`csrc/ops/bmm/bmm_aten_kernels.cc`](csrc/ops/bmm/bmm_aten_kernels.cc.md) | 8 | `AtenBmmDtypeOut`, `AtenBmmOut`, `AtenBmmDtype` |  |
| [`csrc/ops/bucketize/bucketize_aten_kernels.cc`](csrc/ops/bucketize/bucketize_aten_kernels.cc.md) | 13 | `BroadcastResult`, `AtenBucketizeTensorOut`, `AtenBucketizeScalar` |  |
| [`csrc/ops/cat/cat.cc`](csrc/ops/cat/cat.cc.md) | 2 | `BuildCatShlo`, `BuildStackShlo` |  |
| [`csrc/ops/cat/cat_aten_kernels.cc`](csrc/ops/cat/cat_aten_kernels.cc.md) | 20 | `StackDispatchParams`, `CatComputationResult`, `CatShapeInfo` |  |
| [`csrc/ops/channel_shuffle/channel_shuffle_aten_kernels.cc`](csrc/ops/channel_shuffle/channel_shuffle_aten_kernels.cc.md) | 2 | `AtenChannelShuffle`, `BuildChannelShuffleShlo` |  |
| [`csrc/ops/clamp/clamp.cc`](csrc/ops/clamp/clamp.cc.md) | 1 | `BuildClampShlo` |  |
| [`csrc/ops/clamp/clamp_aten_kernels.cc`](csrc/ops/clamp/clamp_aten_kernels.cc.md) | 12 | `AtenClampMaxTensorOut`, `AtenClampMinTensorOut`, `GetComputationType` |  |
| [`csrc/ops/col2im/col2im.cc`](csrc/ops/col2im/col2im.cc.md) | 1 | `BuildCol2ImShlo` |  |
| [`csrc/ops/col2im/col2im_aten_kernels.cc`](csrc/ops/col2im/col2im_aten_kernels.cc.md) | 5 | `AtenCol2Im`, `AtenCol2ImOut`, `ComputeOutputSize` |  |
| [`csrc/ops/constant_pad/constant_pad_aten_kernels.cc`](csrc/ops/constant_pad/constant_pad_aten_kernels.cc.md) | 3 | `AtenConstantPadNd`, `BuildConstantPadNdShlo`, `PadSingleDimensionShlo` |  |
| [`csrc/ops/convolution/convolution.cc`](csrc/ops/convolution/convolution.cc.md) | 16 | `BuildConvolution`, `BuildConvolutionBackwardBias`, `CalculateWindowAlignedPadding` |  |
| [`csrc/ops/convolution/convolution_aten_kernels.cc`](csrc/ops/convolution/convolution_aten_kernels.cc.md) | 24 | `ConvolutionDispatchParams`, `AtenConvolution`, `AtenConvolutionOut` |  |
| [`csrc/ops/convolution/convolution_checks.cc`](csrc/ops/convolution/convolution_checks.cc.md) | 4 | `ValidateConvolutionSpatialDimensionsMatch`, `ValidateConvolutionBias`, `ValidateConvolutionInput` |  |
| [`csrc/ops/copy_from/copy_from_aten_kernels.cc`](csrc/ops/copy_from/copy_from_aten_kernels.cc.md) | 18 | `CopyTensor`, `CopyType`, `AtenCopy_` | [host-device-copy](../concepts/host-device-copy.md) |
| [`csrc/ops/copy_from/cpu_to_tpu.cc`](csrc/ops/copy_from/cpu_to_tpu.cc.md) | 2 | `CopyCpuToTpuBuffer`, `CopyCpuToTpu` | [host-device-copy](../concepts/host-device-copy.md) |
| [`csrc/ops/copy_from/tpu_to_cpu.cc`](csrc/ops/copy_from/tpu_to_cpu.cc.md) | 2 | `CopyTpuToCpu`, `TranslateXlaTensorOomError` | [host-device-copy](../concepts/host-device-copy.md) |
| [`csrc/ops/copy_from/tpu_to_tpu.cc`](csrc/ops/copy_from/tpu_to_tpu.cc.md) | 3 | `CopyTpuToTpu`, `SliceFP4`, `PadFP4` | [host-device-copy](../concepts/host-device-copy.md) |
| [`csrc/ops/count_nonzero/count_nonzero_aten_kernels.cc`](csrc/ops/count_nonzero/count_nonzero_aten_kernels.cc.md) | 2 | `AtenCountNonzeroDimIntList`, `BuildCountNonzeroShlo` |  |
| [`csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`](csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc.md) | 24 | `AtenCrossEntropyLoss`, `RoundThroughOrigDtype`, `kProbabilities` |  |
| [`csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`](csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc.md) | 59 | `ZeroInfinity`, `ValidateLogProbsDtype`, `kYes` |  |
| [`csrc/ops/ctc_loss/ctc_loss_aten_kernels.h`](csrc/ops/ctc_loss/ctc_loss_aten_kernels.h.md) | 2 | `AtenCtcLossTensorAutograd`, `AtenCtcLossAutograd` |  |
| [`csrc/ops/cummax/cummax.cc`](csrc/ops/cummax/cummax.cc.md) | 1 | `BuildCummaxShlo` |  |
| [`csrc/ops/cummax/cummax.h`](csrc/ops/cummax/cummax.h.md) | 3 | `CummaxOutputs`, `indices`, `values` |  |
| [`csrc/ops/cummax/cummax_aten_kernels.cc`](csrc/ops/cummax/cummax_aten_kernels.cc.md) | 1 | `AtenCummaxHelper` |  |
| [`csrc/ops/cummin/cummin.cc`](csrc/ops/cummin/cummin.cc.md) | 1 | `BuildCumminShlo` |  |
| [`csrc/ops/cummin/cummin.h`](csrc/ops/cummin/cummin.h.md) | 3 | `CumminOutputs`, `indices`, `values` |  |
| [`csrc/ops/cummin/cummin_aten_kernels.cc`](csrc/ops/cummin/cummin_aten_kernels.cc.md) | 1 | `AtenCumminHelper` |  |
| [`csrc/ops/cumprod/cumprod.cc`](csrc/ops/cumprod/cumprod.cc.md) | 1 | `BuildCumprodShlo` |  |
| [`csrc/ops/cumprod/cumprod_aten_kernels.cc`](csrc/ops/cumprod/cumprod_aten_kernels.cc.md) | 1 | `AtenCumprodOut` |  |
| [`csrc/ops/cumsum/cumsum.cc`](csrc/ops/cumsum/cumsum.cc.md) | 1 | `BuildCumsumShlo` |  |
| [`csrc/ops/cumsum/cumsum_aten_kernels.cc`](csrc/ops/cumsum/cumsum_aten_kernels.cc.md) | 1 | `AtenCumsumOut` |  |
| [`csrc/ops/custom_kernels.cc`](csrc/ops/custom_kernels.cc.md) | 40 | `RegisterCustomKernel`, `CustomKernelRegistry`, `CallCustomKernel` |  |
| [`csrc/ops/custom_kernels_test.cc`](csrc/ops/custom_kernels_test.cc.md) | 71 | `CustomKernelRegistryTest`, `kUnrefinedRank1AddMlirKernel`, `HasSubstr` |  |
| [`csrc/ops/digamma/digamma_aten_kernels.cc`](csrc/ops/digamma/digamma_aten_kernels.cc.md) | 2 | `BuildDigammaShlo`, `AtenDigammaOut` |  |
| [`csrc/ops/distance/dist_aten_kernels.cc`](csrc/ops/distance/dist_aten_kernels.cc.md) | 16 | `ValidateNotBFloatOrHalf`, `ValidateIsFloatingPoint`, `AtenCdistBackward` |  |
| [`csrc/ops/dot/dot.cc`](csrc/ops/dot/dot.cc.md) | 2 | `BuildDotShlo`, `BuildDotShlo` |  |
| [`csrc/ops/dot/dot_aten_kernels.cc`](csrc/ops/dot/dot_aten_kernels.cc.md) | 2 | `AtenDot`, `Dot` |  |
| [`csrc/ops/dot/dot_checks.cc`](csrc/ops/dot/dot_checks.cc.md) | 2 | `ValidateIsVector`, `ValidateAndGetDotOutputType` |  |
| [`csrc/ops/dot/vdot_aten_kernels.cc`](csrc/ops/dot/vdot_aten_kernels.cc.md) | 5 | `AtenVdot`, `ValidateInputs`, `Vdot` |  |
| [`csrc/ops/dropout/dropout.cc`](csrc/ops/dropout/dropout.cc.md) | 4 | `BuildDropoutBackwardShlo`, `BuildDropoutTrainShlo`, `BuildDropoutBackwardShlo` |  |
| [`csrc/ops/dropout/dropout_aten_kernels.cc`](csrc/ops/dropout/dropout_aten_kernels.cc.md) | 8 | `AtenNativeDropoutBackward`, `AtenDropoutCommonImpl`, `AtenDropout` |  |
| [`csrc/ops/dynamic/dynamic_arange/dynamic_arange.cc`](csrc/ops/dynamic/dynamic_arange/dynamic_arange.cc.md) | 2 | `DynamicArange`, `BuildDynamicArange` | [dynamic-shape-ops](../concepts/dynamic-shape-ops.md) |
| [`csrc/ops/dynamic/dynamic_broadcast/dynamic_broadcast.cc`](csrc/ops/dynamic/dynamic_broadcast/dynamic_broadcast.cc.md) | 1 | `DynamicBroadcast` | [dynamic-shape-ops](../concepts/dynamic-shape-ops.md) |
| [`csrc/ops/dynamic/dynamic_reshape/dynamic_reshape.cc`](csrc/ops/dynamic/dynamic_reshape/dynamic_reshape.cc.md) | 1 | `DynamicReshape` | [dynamic-shape-ops](../concepts/dynamic-shape-ops.md) |
| [`csrc/ops/dynamic/dynamic_slice/dynamic_slice.cc`](csrc/ops/dynamic/dynamic_slice/dynamic_slice.cc.md) | 1 | `DynamicSlice` | [dynamic-shape-ops](../concepts/dynamic-shape-ops.md) |
| [`csrc/ops/dynamic/pad_real_to_static/pad_real_to_static.cc`](csrc/ops/dynamic/pad_real_to_static/pad_real_to_static.cc.md) | 3 | `PadRealToStatic`, `BuildPadRealToStaticCustomCall`, `BuildPadRealToStaticCustomCall` | [dynamic-shape-ops](../concepts/dynamic-shape-ops.md) |
| [`csrc/ops/dynamic/set_dimension_logical_size/set_dimension_logical_size.cc`](csrc/ops/dynamic/set_dimension_logical_size/set_dimension_logical_size.cc.md) | 1 | `SetDimensionLogicalSize` | [dynamic-shape-ops](../concepts/dynamic-shape-ops.md) |
| [`csrc/ops/elu/elu_aten_kernels.cc`](csrc/ops/elu/elu_aten_kernels.cc.md) | 5 | `AtenEluBackwardGradInput`, `AtenEluOut`, `ValidateIsFloatingPoint` |  |
| [`csrc/ops/embedding/embedding.cc`](csrc/ops/embedding/embedding.cc.md) | 33 | `BuildEmbeddingGather`, `HasWindow`, `BuildSimpleScatter` |  |
| [`csrc/ops/embedding/embedding.h`](csrc/ops/embedding/embedding.h.md) | 4 | `EmbeddingBagMode`, `kMean`, `kMax` |  |
| [`csrc/ops/embedding/embedding_aten_kernels.cc`](csrc/ops/embedding/embedding_aten_kernels.cc.md) | 18 | `AtenEmbeddingBag`, `AtenEmbeddingSparseBackward`, `AtenEmbeddingDenseBackward` |  |
| [`csrc/ops/equal/equal_aten_kernels.cc`](csrc/ops/equal/equal_aten_kernels.cc.md) | 2 | `AtenEqual`, `BuildEqualShlo` |  |
| [`csrc/ops/experimental/collectives/collectives_aten_kernels.cc`](csrc/ops/experimental/collectives/collectives_aten_kernels.cc.md) | 14 | `output_shape`, `dim`, `CollectiveShape` | [ragged-collectives-and-sparse-ops](../concepts/ragged-collectives-and-sparse-ops.md) |
| [`csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.cc`](csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.cc.md) | 6 | `AtenRaggedAllToAllOut`, `AtenRaggedAllToAll`, `RaggedAllToAllCommon` | [ragged-collectives-and-sparse-ops](../concepts/ragged-collectives-and-sparse-ops.md) |
| [`csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.h`](csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.h.md) | 1 | `AtenRaggedAllToAllAutograd` | [ragged-collectives-and-sparse-ops](../concepts/ragged-collectives-and-sparse-ops.md) |
| [`csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_builder.cc`](csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_builder.cc.md) | 1 | `BuildRaggedAllToAllShlo` |  |
| [`csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc`](csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc.md) | 11 | `AtenRaggedDotOut`, `AtenRaggedDotWeightGrad`, `AtenRaggedDot` | [ragged-collectives-and-sparse-ops](../concepts/ragged-collectives-and-sparse-ops.md) |
| [`csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.h`](csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.h.md) | 1 | `AtenRaggedDotAutograd` |  |
| [`csrc/ops/experimental/send_recv/send_recv_kernels.cc`](csrc/ops/experimental/send_recv/send_recv_kernels.cc.md) | 3 | `TorchTpuRecv`, `TorchTpuSend`, `GetProcessGroupTpu` | [ragged-collectives-and-sparse-ops](../concepts/ragged-collectives-and-sparse-ops.md) |
| [`csrc/ops/experimental/sparse_dense_matmul/compute_stats_aten_kernels.cc`](csrc/ops/experimental/sparse_dense_matmul/compute_stats_aten_kernels.cc.md) | 2 | `TORCH_LIBRARY_FRAGMENT_init_tpu_1`, `TORCH_LIBRARY_FRAGMENT_static_init_tpu_1` | [ragged-collectives-and-sparse-ops](../concepts/ragged-collectives-and-sparse-ops.md) |
| [`csrc/ops/experimental/sparse_dense_matmul/input_preprocessing_aten_kernels.cc`](csrc/ops/experimental/sparse_dense_matmul/input_preprocessing_aten_kernels.cc.md) | 2 | `TORCH_LIBRARY_FRAGMENT_init_tpu_2`, `TORCH_LIBRARY_FRAGMENT_static_init_tpu_2` |  |
| [`csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc`](csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc.md) | 10 | `ValidateSparseDenseMatmulActivationUnstackInputs`, `AtenSparseDenseMatmulActivationUnstack`, `AtenSparseDenseMatmulActivationUnstack` | [ragged-collectives-and-sparse-ops](../concepts/ragged-collectives-and-sparse-ops.md) |
| [`csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.h`](csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.h.md) | 1 | `AtenSparseDenseMatmulActivationUnstackAutograd` |  |
| [`csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_aten_kernels.cc`](csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_aten_kernels.cc.md) | 2 | `AtenSparseDenseMatmul`, `SparseDenseMatmulBuilder` | [ragged-collectives-and-sparse-ops](../concepts/ragged-collectives-and-sparse-ops.md) |
| [`csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adagrad_aten_kernels.cc`](csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adagrad_aten_kernels.cc.md) | 4 | `AtenSparseDenseMatmulGradWithAdagrad`, `SparseDenseMatmulGradWithAdagradBuilder`, `SparseDenseMatmulGradWithAdagradBuilder` | [ragged-collectives-and-sparse-ops](../concepts/ragged-collectives-and-sparse-ops.md) |
| [`csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adam_aten_kernels.cc`](csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adam_aten_kernels.cc.md) | 3 | `AtenSparseDenseMatmulGradWithAdam`, `SparseDenseMatmulGradWithAdamBuilder`, `SparseDenseMatmulGradWithAdamBuilder` | [ragged-collectives-and-sparse-ops](../concepts/ragged-collectives-and-sparse-ops.md) |
| [`csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_sgd_aten_kernels.cc`](csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_sgd_aten_kernels.cc.md) | 2 | `AtenSparseDenseMatmulGradWithSgd`, `SparseDenseMatmulGradWithSgdBuilder` | [ragged-collectives-and-sparse-ops](../concepts/ragged-collectives-and-sparse-ops.md) |
| [`csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_gradient_stack_aten_kernels.cc`](csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_gradient_stack_aten_kernels.cc.md) | 3 | `ValidateSparseDenseMatmulGradientStackInputs`, `AtenSparseDenseMatmulGradientStack`, `SparseDenseMatmulGradientStackBuilder` | [ragged-collectives-and-sparse-ops](../concepts/ragged-collectives-and-sparse-ops.md) |
| [`csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc`](csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc.md) | 8 | `ValidateSparseGatherInputs`, `AtenSparseGatherBackward`, `AtenSparseGather` | [ragged-collectives-and-sparse-ops](../concepts/ragged-collectives-and-sparse-ops.md) |
| [`csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.h`](csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.h.md) | 1 | `AtenSparseGatherAutograd` |  |
| [`csrc/ops/experimental/sparse_iota/sparse_iota_aten_kernels.cc`](csrc/ops/experimental/sparse_iota/sparse_iota_aten_kernels.cc.md) | 6 | `ValidateSparseIotaInputs`, `AtenSparseIota`, `SparseIotaBuilder` | [ragged-collectives-and-sparse-ops](../concepts/ragged-collectives-and-sparse-ops.md) |
| [`csrc/ops/experimental/sparse_map_row/sparse_map_row_aten_kernels.cc`](csrc/ops/experimental/sparse_map_row/sparse_map_row_aten_kernels.cc.md) | 10 | `ValidateSparseMapRowInputs`, `AtenSparseMapRow`, `AtenSparseMapRow` | [ragged-collectives-and-sparse-ops](../concepts/ragged-collectives-and-sparse-ops.md) |
| [`csrc/ops/exponential/exponential_aten_kernels.cc`](csrc/ops/exponential/exponential_aten_kernels.cc.md) | 5 | `AtenExponential_`, `GetExponentialFunctional`, `BuildExponentialShlo` |  |
| [`csrc/ops/eye/eye_aten_kernels.cc`](csrc/ops/eye/eye_aten_kernels.cc.md) | 3 | `AtenEyeMOut`, `AtenEyeOut`, `GetEyeOpBuilder` |  |
| [`csrc/ops/eye/eye_lib.cc`](csrc/ops/eye/eye_lib.cc.md) | 1 | `BuildEyeShlo` |  |
| [`csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc`](csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc.md) | 6 | `FakeQuantizePerTensorAffineCachemask`, `FakeQuantizePerTensorAffineCachemaskResult`, `FakeQuantizePerTensorAffineCachemaskHelper` |  |
| [`csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc`](csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc.md) | 8 | `FusedMovingAvgObsFqHelper`, `FusedMovingAvgObsFqHelperImpl`, `ValidateFusedMovingAvgObsFqInputs` |  |
| [`csrc/ops/fft/fft_aten_kernels.cc`](csrc/ops/fft/fft_aten_kernels.cc.md) | 41 | `FftNormalization`, `PromoteToFloatIfBFloat16`, `FFTValidateStaticShape` |  |
| [`csrc/ops/fill/fill_aten_kernels.cc`](csrc/ops/fill/fill_aten_kernels.cc.md) | 4 | `AtenZero_`, `AtenFillScalar_`, `AtenFillTensor_` |  |
| [`csrc/ops/flip/flip_aten_kernels.cc`](csrc/ops/flip/flip_aten_kernels.cc.md) | 2 | `AtenFlip`, `BuildFlipShlo` |  |
| [`csrc/ops/fmax/fmax_aten_kernels.cc`](csrc/ops/fmax/fmax_aten_kernels.cc.md) | 2 | `AtenFmaxOut`, `BuildFmaxShlo` |  |
| [`csrc/ops/fmin/fmin_aten_kernels.cc`](csrc/ops/fmin/fmin_aten_kernels.cc.md) | 2 | `AtenFminOut`, `BuildFminShlo` |  |
| [`csrc/ops/foreach_aten_kernels.cc`](csrc/ops/foreach_aten_kernels.cc.md) | 288 | `GetOutputDtypes`, `GetOutputDtypes`, `ForeachUnaryOp` |  |
| [`csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`](csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc.md) | 62 | `GradScaleMode`, `kEnabled`, `FoundInfMode` | [fused-optimizer-kernels](../concepts/fused-optimizer-kernels.md) |
| [`csrc/ops/fused_adam/fused_adam_aten_kernels.cc`](csrc/ops/fused_adam/fused_adam_aten_kernels.cc.md) | 54 | `OneParamResult`, `grad`, `max_exp_avg_sq` | [fused-optimizer-kernels](../concepts/fused-optimizer-kernels.md) |
| [`csrc/ops/fused_adam/fused_adam_aten_kernels.h`](csrc/ops/fused_adam/fused_adam_aten_kernels.h.md) | 13 | `AdamAmsgradMode`, `AdamObjectiveMode`, `kEnabled` |  |
| [`csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`](csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc.md) | 48 | `OneParamResult`, `max_exp_avg_sq`, `grad` | [fused-optimizer-kernels](../concepts/fused-optimizer-kernels.md) |
| [`csrc/ops/fused_adamw/fused_adamw_aten_kernels.h`](csrc/ops/fused_adamw/fused_adamw_aten_kernels.h.md) | 6 | `AmsgradMode`, `ObjectiveMode`, `kEnabled` |  |
| [`csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`](csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc.md) | 71 | `MomentumMode`, `kEnabled`, `GradScaleMode` | [fused-optimizer-kernels](../concepts/fused-optimizer-kernels.md) |
| [`csrc/ops/gather/gather.cc`](csrc/ops/gather/gather.cc.md) | 2 | `BuildGatherShlo`, `ValidateGatherInputs` |  |
| [`csrc/ops/gather/gather_aten_kernels.cc`](csrc/ops/gather/gather_aten_kernels.cc.md) | 4 | `AtenGatherOut`, `AtenGather`, `GatherOut` |  |
| [`csrc/ops/gelu/gelu.cc`](csrc/ops/gelu/gelu.cc.md) | 6 | `BuildGeluShlo`, `BuildGeluBackwardGradInputShlo`, `BuildGeluApproximateShlo` |  |
| [`csrc/ops/gelu/gelu_aten_kernels.cc`](csrc/ops/gelu/gelu_aten_kernels.cc.md) | 4 | `AtenGeluBackwardGradInput`, `AtenGeluOut`, `AtenGelu` |  |
| [`csrc/ops/glu/glu_aten_kernels.cc`](csrc/ops/glu/glu_aten_kernels.cc.md) | 7 | `ValidateIsFloatingPoint`, `AtenGluOut`, `AtenGluBackwardGradInput` |  |
| [`csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`](csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc.md) | 92 | `PaddingMode`, `GridSamplerGatherConfig`, `DimensionInfoToOp` |  |
| [`csrc/ops/group_norm/group_norm_aten_kernels.cc`](csrc/ops/group_norm/group_norm_aten_kernels.cc.md) | 6 | `GroupNormBackwardShloResults`, `AtenNativeGroupNormBackward`, `BuildGroupNormBackwardShlo` |  |
| [`csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc`](csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc.md) | 11 | `AtenGroupedMm`, `AtenScaledGroupedMm`, `GetGroupedMmOutputSize` |  |
| [`csrc/ops/gru/gru_aten_kernels.cc`](csrc/ops/gru/gru_aten_kernels.cc.md) | 273 | `ConcatDim`, `kGruUnrollFactor`, `ExpandStep3D` |  |
| [`csrc/ops/gru/gru_common.cc`](csrc/ops/gru/gru_common.cc.md) | 1 | `ComputeGruGateAdjoints` |  |
| [`csrc/ops/gru/gru_common.h`](csrc/ops/gru/gru_common.h.md) | 6 | `GruGateAdjoints`, `delta_hx_skip`, `delta_pre_r` |  |
| [`csrc/ops/hardsigmoid/hardsigmoid_aten_kernels.cc`](csrc/ops/hardsigmoid/hardsigmoid_aten_kernels.cc.md) | 4 | `AtenHardsigmoidBackwardGradInput`, `AtenHardsigmoidOut`, `BuildHardsigmoidBackwardShlo` |  |
| [`csrc/ops/hardswish/hardswish_aten_kernels.cc`](csrc/ops/hardswish/hardswish_aten_kernels.cc.md) | 6 | `BuildHardswishShlo`, `AtenHardswishBackward`, `AtenHardswishOut` |  |
| [`csrc/ops/hardtanh/hardtanh_aten_kernels.cc`](csrc/ops/hardtanh/hardtanh_aten_kernels.cc.md) | 20 | `HardtanhBounds`, `AtenHardtanhOut`, `AtenHardtanhBackwardGradInput` |  |
| [`csrc/ops/histc/histc.cc`](csrc/ops/histc/histc.cc.md) | 11 | `BuildHistcShlo`, `BuildHistcBoundsShlo`, `BuildReduce` |  |
| [`csrc/ops/histc/histc.h`](csrc/ops/histc/histc.h.md) | 3 | `HistcBounds`, `max`, `min` |  |
| [`csrc/ops/histc/histc_aten_kernels.cc`](csrc/ops/histc/histc_aten_kernels.cc.md) | 6 | `HistcHelperOut`, `AtenHistc`, `AtenHistcOut` |  |
| [`csrc/ops/im2col/im2col.cc`](csrc/ops/im2col/im2col.cc.md) | 1 | `BuildIm2ColShlo` |  |
| [`csrc/ops/im2col/im2col_aten_kernels.cc`](csrc/ops/im2col/im2col_aten_kernels.cc.md) | 3 | `AtenIm2Col`, `AtenIm2ColOut`, `AtenIm2Col` |  |
| [`csrc/ops/index/index.cc`](csrc/ops/index/index.cc.md) | 6 | `BuildIndexShlo`, `BuildBooleanMaskIndexShlo`, `AreConsecutive` |  |
| [`csrc/ops/index/index_aten_kernels.cc`](csrc/ops/index/index_aten_kernels.cc.md) | 8 | `IndicesInfo`, `indices`, `dimensions` | [op-names-and-python-context](../concepts/op-names-and-python-context.md) |
| [`csrc/ops/index_add/index_add.cc`](csrc/ops/index_add/index_add.cc.md) | 1 | `BuildIndexAddShlo` |  |
| [`csrc/ops/index_add/index_add_aten_kernels.cc`](csrc/ops/index_add/index_add_aten_kernels.cc.md) | 2 | `TpuAtenIndexAddOut`, `IndexAdd` |  |
| [`csrc/ops/index_copy/index_copy.cc`](csrc/ops/index_copy/index_copy.cc.md) | 2 | `BuildIndexCopyShlo`, `BuildIndexCopyShlo` |  |
| [`csrc/ops/index_copy/index_copy_aten_kernels.cc`](csrc/ops/index_copy/index_copy_aten_kernels.cc.md) | 2 | `AtenIndexCopyOut`, `IndexCopy` |  |
| [`csrc/ops/index_fill/index_fill_aten_kernels.cc`](csrc/ops/index_fill/index_fill_aten_kernels.cc.md) | 4 | `AtenIndexFillIntTensor_`, `AtenIndexFillIntScalar_`, `ValidateIndexFillInputs` |  |
| [`csrc/ops/index_put/index_put.cc`](csrc/ops/index_put/index_put.cc.md) | 4 | `BuildIndexPutShlo`, `BuildIndexPutSelectShlo`, `ApplyScatter` |  |
| [`csrc/ops/index_put/index_put_aten_kernels.cc`](csrc/ops/index_put/index_put_aten_kernels.cc.md) | 18 | `TpuAtenIndexPutImpl_`, `BooleanMaskInfo`, `IndexPut` |  |
| [`csrc/ops/index_reduce/index_reduce_aten_kernels.cc`](csrc/ops/index_reduce/index_reduce_aten_kernels.cc.md) | 3 | `TpuAtenIndexReduceOut`, `IndexReduce`, `GetReduceOp` |  |
| [`csrc/ops/index_select/index_select.cc`](csrc/ops/index_select/index_select.cc.md) | 2 | `BuildIndexSelectShlo`, `BuildIndexSelectShlo` |  |
| [`csrc/ops/index_select/index_select_aten_kernels.cc`](csrc/ops/index_select/index_select_aten_kernels.cc.md) | 2 | `TpuAtenIndexSelect`, `IndexSelect` |  |
| [`csrc/ops/index_utils.cc`](csrc/ops/index_utils.cc.md) | 4 | `ValidateIndexInputsAndGetDim`, `ResolveNegativeIndices`, `ResolveAuxiliaryTensorDevice` |  |
| [`csrc/ops/is/is.cc`](csrc/ops/is/is.cc.md) | 5 | `BuildIsNanShlo`, `MakeBoolLike`, `BuildIsNegInfShlo` |  |
| [`csrc/ops/is/is_aten_kernels.cc`](csrc/ops/is/is_aten_kernels.cc.md) | 3 | `AtenIsNegInfOut`, `AtenIsPosInfOut`, `AtenIsNan` |  |
| [`csrc/ops/isin/isin.cc`](csrc/ops/isin/isin.cc.md) | 1 | `BuildIsInShlo` |  |
| [`csrc/ops/isin/isin.h`](csrc/ops/isin/isin.h.md) | 6 | `IsInverted`, `IsUnique`, `kYes` |  |
| [`csrc/ops/isin/isin_aten_kernels.cc`](csrc/ops/isin/isin_aten_kernels.cc.md) | 6 | `AtenIsInHelper`, `ToIsInverted`, `ToIsUnique` |  |
| [`csrc/ops/jagged/jagged_aten_kernels.cc`](csrc/ops/jagged/jagged_aten_kernels.cc.md) | 27 | `JaggedToPaddedIndices`, `AtenPaddedDenseToJaggedForward`, `AtenNestedViewFromJagged` |  |
| [`csrc/ops/layer_norm/layer_norm.cc`](csrc/ops/layer_norm/layer_norm.cc.md) | 7 | `BuildLayerNormShlo`, `BuildLayerNormBackwardShlo`, `TwoMoments` |  |
| [`csrc/ops/layer_norm/layer_norm.h`](csrc/ops/layer_norm/layer_norm.h.md) | 8 | `LayerNormShloResults`, `LayerNormBackwardShloResults`, `normalized_values` |  |
| [`csrc/ops/layer_norm/layer_norm_aten_kernels.cc`](csrc/ops/layer_norm/layer_norm_aten_kernels.cc.md) | 3 | `AtenNativeLayerNorm`, `AtenLayerNormBackward`, `ValidateInputs` |  |
| [`csrc/ops/lcm/lcm_aten_kernels.cc`](csrc/ops/lcm/lcm_aten_kernels.cc.md) | 6 | `AtenLcmOut`, `ValidateLcmInputs`, `BuildLcmShlo` |  |
| [`csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc`](csrc/ops/leaky_relu/leaky_relu_aten_kernels.cc.md) | 8 | `AtenLeakyReluBackwardGradInput`, `AtenLeakyReluOut`, `AtenLeakyReluBackwardTensorHelper` |  |
| [`csrc/ops/lerp/lerp_aten_kernels.cc`](csrc/ops/lerp/lerp_aten_kernels.cc.md) | 7 | `AtenLerpTensorOut`, `AtenLerpScalarOut`, `ValidateLerpSelfInput` |  |
| [`csrc/ops/linalg/linalg_kernels.cc`](csrc/ops/linalg/linalg_kernels.cc.md) | 2 | `AtenLinalgSolveExOut`, `AtenLinalgInvExInverse` |  |
| [`csrc/ops/linalg/linalg_svd_kernels.cc`](csrc/ops/linalg/linalg_svd_kernels.cc.md) | 97 | `BuildConjugateTransposeShlo`, `BuildMatMulShlo`, `BuildScaleTensor` |  |
| [`csrc/ops/linalg/lu/linalg_lu_kernels.cc`](csrc/ops/linalg/lu/linalg_lu_kernels.cc.md) | 8 | `AtenLinalgLuFactorExOut`, `AtenLinalgLuSolveOut`, `AtenLuUnpackOut` |  |
| [`csrc/ops/linalg/qr/linalg_qr_kernels.cc`](csrc/ops/linalg/qr/linalg_qr_kernels.cc.md) | 16 | `GetOutDtype`, `QrDims`, `AtenGeqrfA` |  |
| [`csrc/ops/linalg/qr/qr_lib.cc`](csrc/ops/linalg/qr/qr_lib.cc.md) | 15 | `BuildQrShlo`, `BuildQrShlo`, `BuildGeqrfShlo` |  |
| [`csrc/ops/linalg/solve_triangular/linalg_solve_triangular_kernels.cc`](csrc/ops/linalg/solve_triangular/linalg_solve_triangular_kernels.cc.md) | 5 | `LinalgSolveTriangularBuilder`, `AtenLinalgSolveTriangular`, `AtenLinalgSolveTriangularOut` |  |
| [`csrc/ops/linalg/solve_triangular/linalg_solve_triangular_kernels.h`](csrc/ops/linalg/solve_triangular/linalg_solve_triangular_kernels.h.md) | 5 | `SolveTriangularOptions`, `adjoint`, `left` |  |
| [`csrc/ops/linalg/vector_norm/aten_vector_norm_kernels.cc`](csrc/ops/linalg/vector_norm/aten_vector_norm_kernels.cc.md) | 2 | `AtenLinalgVectorNormOut`, `PNormOut` |  |
| [`csrc/ops/linalg/vector_norm/pnorm.cc`](csrc/ops/linalg/vector_norm/pnorm.cc.md) | 2 | `BuildPNormShlo`, `BuildPNormShlo` |  |
| [`csrc/ops/linear/linear_aten_kernels.cc`](csrc/ops/linear/linear_aten_kernels.cc.md) | 23 | `ValidateLinearInputs`, `BuildDotGeneral`, `AtenLinearBackward` |  |
| [`csrc/ops/linspace/linspace_aten_kernels.cc`](csrc/ops/linspace/linspace_aten_kernels.cc.md) | 5 | `AtenLinspaceOut`, `PrepareScalar`, `BuildLinspaceInterpolation` |  |
| [`csrc/ops/logcumsumexp/logcumsumexp_aten_kernels.cc`](csrc/ops/logcumsumexp/logcumsumexp_aten_kernels.cc.md) | 4 | `AtenLogcumsumexpOut`, `AtenLogcumsumexp`, `BuildLogcumsumexpShlo` |  |
| [`csrc/ops/logical/logical.cc`](csrc/ops/logical/logical.cc.md) | 9 | `BroadcastLogicalOperands`, `other`, `self` |  |
| [`csrc/ops/logical/logical_aten_kernels.cc`](csrc/ops/logical/logical_aten_kernels.cc.md) | 6 | `LogicalBinaryOutImpl`, `AtenLogicalAndOut`, `AtenLogicalNotOut` |  |
| [`csrc/ops/logit/logit_aten_kernels.cc`](csrc/ops/logit/logit_aten_kernels.cc.md) | 10 | `AtenLogitBackwardGradInput`, `AtenLogitOut`, `AtenLogit_` |  |
| [`csrc/ops/lstm/lstm_aten_kernels.cc`](csrc/ops/lstm/lstm_aten_kernels.cc.md) | 172 | `ConcatDim`, `kLstmUnrollFactor`, `SliceStep2D` |  |
| [`csrc/ops/lstm/lstm_common.cc`](csrc/ops/lstm/lstm_common.cc.md) | 1 | `ComputeLstmGateAdjoints` |  |
| [`csrc/ops/lstm/lstm_common.h`](csrc/ops/lstm/lstm_common.h.md) | 8 | `LstmGateAdjoints`, `delta_c_prev`, `SigmoidBackward` |  |
| [`csrc/ops/macros/kernel.cc`](csrc/ops/macros/kernel.cc.md) | 4 | `AppendPromotedScalarPointers`, `AppendPromotedScalarPointers`, `CheckTensorsUsed` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md) |
| [`csrc/ops/macros/kernel.h`](csrc/ops/macros/kernel.h.md) | 21 | `ConditionalStaticAssert`, `InvalidOpParamCacheKeys`, `InvalidOpParamCacheKeys` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md) |
| [`csrc/ops/macros/kernel_test.cc`](csrc/ops/macros/kernel_test.cc.md) | 76 | `Pair`, `ElementsAre`, `StartsWith` |  |
| [`csrc/ops/macros/logging.cc`](csrc/ops/macros/logging.cc.md) | 5 | `ParseArgTypesOrEmpty`, `Regex`, `ParseArgTypesOrEmpty` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md) |
| [`csrc/ops/macros/logging.h`](csrc/ops/macros/logging.h.md) | 23 | `KernelArgCheckerContext`, `LogKernelArgs`, `CheckTtKernelArgList` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md) |
| [`csrc/ops/macros/logging_test.cc`](csrc/ops/macros/logging_test.cc.md) | 214 | `LogKernelArgs`, `StartsWith`, `ElementsAre` |  |
| [`csrc/ops/masked_fill/masked_fill_aten_kernels.cc`](csrc/ops/masked_fill/masked_fill_aten_kernels.cc.md) | 12 | `ResolveScalarValueAndDispatch`, `AtenMaskedFill_Scalar`, `AtenMaskedFill_Tensor` |  |
| [`csrc/ops/masked_scatter/masked_scatter.cc`](csrc/ops/masked_scatter/masked_scatter.cc.md) | 6 | `RowPartition`, `BuildMaskedScatterShlo`, `ComputeRowPartition` |  |
| [`csrc/ops/masked_scatter/masked_scatter_aten_kernels.cc`](csrc/ops/masked_scatter/masked_scatter_aten_kernels.cc.md) | 2 | `AtenMaskedScatter_`, `NarrowBroadcastTrailingDims` | [op-names-and-python-context](../concepts/op-names-and-python-context.md) |
| [`csrc/ops/masked_select/masked_select_aten_kernels.cc`](csrc/ops/masked_select/masked_select_aten_kernels.cc.md) | 5 | `AtenMaskedSelect`, `AtenMaskedSelectOut`, `ValidateMaskTensorIsBool` |  |
| [`csrc/ops/min_max/min_max.cc`](csrc/ops/min_max/min_max.cc.md) | 10 | `BuildMinMaxShlo`, `ReductionInput`, `GetMinMaxInitValue` |  |
| [`csrc/ops/min_max/min_max.h`](csrc/ops/min_max/min_max.h.md) | 6 | `MinMaxOp`, `kMax`, `kMin` |  |
| [`csrc/ops/min_max/min_max_aten_kernels.cc`](csrc/ops/min_max/min_max_aten_kernels.cc.md) | 13 | `UnaryMinMax`, `ValidateNotZeroElementTensor`, `AtenMax` |  |
| [`csrc/ops/mm/mm.cc`](csrc/ops/mm/mm.cc.md) | 2 | `BuildMmShlo`, `BuildMmShlo` |  |
| [`csrc/ops/mm/mm_aten_kernels.cc`](csrc/ops/mm/mm_aten_kernels.cc.md) | 5 | `Mm`, `AtenMmDtype`, `AtenMmDtypeOut` |  |
| [`csrc/ops/mse_loss/mse_loss_aten_kernels.cc`](csrc/ops/mse_loss/mse_loss_aten_kernels.cc.md) | 4 | `AtenMseLossBackward`, `AtenMseLossOut`, `BuildMseLossShlo` |  |
| [`csrc/ops/multinomial/multinomial.cc`](csrc/ops/multinomial/multinomial.cc.md) | 2 | `BuildMultinomialShlo`, `BuildGumbelNoise` |  |
| [`csrc/ops/multinomial/multinomial_aten_kernels.cc`](csrc/ops/multinomial/multinomial_aten_kernels.cc.md) | 7 | `AtenMultinomial`, `AtenMultinomialOut`, `ValidateInputs` |  |
| [`csrc/ops/nan_to_num/nan_to_num_aten_kernels.cc`](csrc/ops/nan_to_num/nan_to_num_aten_kernels.cc.md) | 2 | `AtenNanToNumOut`, `BuildNanToNumShlo` |  |
| [`csrc/ops/native_batch_norm/native_batch_norm.cc`](csrc/ops/native_batch_norm/native_batch_norm.cc.md) | 5 | `BuildBatchNorm`, `ComputeInvStd`, `BuildBatchNormBackward` |  |
| [`csrc/ops/native_batch_norm/native_batch_norm.h`](csrc/ops/native_batch_norm/native_batch_norm.h.md) | 1 | `kTorchFeaturesDimensionIndex` |  |
| [`csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc`](csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc.md) | 20 | `AtenNativeBatchNorm`, `TpuBatchNormOut`, `AtenNativeBatchNormLegitNoStatsOut` |  |
| [`csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc`](csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc.md) | 18 | `AtenNativeMultiHeadAttention`, `BuildMhaCore`, `BuildDotGeneral` |  |
| [`csrc/ops/native_norm/native_norm_aten_kernels.cc`](csrc/ops/native_norm/native_norm_aten_kernels.cc.md) | 3 | `AtenNativeNormScalarOptDimDtype`, `AtenNativeNormScalar`, `PNorm` |  |
| [`csrc/ops/nll_loss/nll_loss.cc`](csrc/ops/nll_loss/nll_loss.cc.md) | 4 | `GatherWeightsShlo`, `BuildNllLossForwardOutShlo`, `BuildNllLossBackwardGradInputShlo` |  |
| [`csrc/ops/nll_loss/nll_loss_aten_kernels.cc`](csrc/ops/nll_loss/nll_loss_aten_kernels.cc.md) | 27 | `ValidateNllLossCommon`, `IsFakeOrFunctorchLossInputs`, `ValidateNllLoss2dForwardShapes` |  |
| [`csrc/ops/nonzero/nonzero.cc`](csrc/ops/nonzero/nonzero.cc.md) | 4 | `BuildNonzeroShlo`, `BuildNonzeroGetOutputSizeShlo`, `UnravelIndices` |  |
| [`csrc/ops/nonzero/nonzero_aten_kernels.cc`](csrc/ops/nonzero/nonzero_aten_kernels.cc.md) | 7 | `AtenNonzero`, `AtenNonzeroOut`, `GetNumNonZeroElements` |  |
| [`csrc/ops/norm/norm_aten_kernels.cc`](csrc/ops/norm/norm_aten_kernels.cc.md) | 5 | `AtenNormDtypeOut`, `AtenNormOut`, `PNormOut` |  |
| [`csrc/ops/normal/normal_aten_kernels.cc`](csrc/ops/normal/normal_aten_kernels.cc.md) | 36 | `ValidateNormalPreconditions`, `ValidateNormalStdPreconditions`, `BuildNormalShlo` |  |
| [`csrc/ops/nullary_aten_kernels.cc`](csrc/ops/nullary_aten_kernels.cc.md) | 5 | `AtenEfficientZeroTensor`, `ApplyNullaryOp`, `ApplyNullaryOpOut` |  |
| [`csrc/ops/op_builder_utils.cc`](csrc/ops/op_builder_utils.cc.md) | 113 | `GetTensorTypeOrDie`, `MakeConstantLike`, `BroadcastIfNeeded` | [dtype-and-precision](../concepts/dtype-and-precision.md), [dynamic-shape-ops](../concepts/dynamic-shape-ops.md), [stablehlo-op-builder](../concepts/stablehlo-op-builder.md) |
| [`csrc/ops/op_builder_utils.h`](csrc/ops/op_builder_utils.h.md) | 112 | `MakeScalarConstant`, `MakeScalarConstant`, `MakeConstantLike` | [dynamic-shape-ops](../concepts/dynamic-shape-ops.md), [stablehlo-op-builder](../concepts/stablehlo-op-builder.md) |
| [`csrc/ops/op_builder_utils_test.cc`](csrc/ops/op_builder_utils_test.cc.md) | 789 | `OpBuilderUtilsBuilder`, `OpBuilderUtilsBuilder`, `get` |  |
| [`csrc/ops/op_names.cc`](csrc/ops/op_names.cc.md) | 1 | `ToBaseName` |  |
| [`csrc/ops/op_names.h`](csrc/ops/op_names.h.md) | 857 | `OpName`, `operator<<`, `ToString` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md), [op-names-and-python-context](../concepts/op-names-and-python-context.md) |
| [`csrc/ops/op_names_test.cc`](csrc/ops/op_names_test.cc.md) | 9 | `OpNamesTest_AllToStringResultsAreUnique_Test`, `TestBody`, `OpNamesTest_AllToStringResultsAreUnique_Test` |  |
| [`csrc/ops/optimization_barrier/optimization_barrier_kernels.cc`](csrc/ops/optimization_barrier/optimization_barrier_kernels.cc.md) | 2 | `TorchTpuOptimizationBarrier`, `TorchTpuOptimizationBarrier` |  |
| [`csrc/ops/polygamma/polygamma_aten_kernels.cc`](csrc/ops/polygamma/polygamma_aten_kernels.cc.md) | 9 | `AtenPolygammaOut`, `ComputeCotDerivativeCoeffs`, `BuildPolygammaShlo` |  |
| [`csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc`](csrc/ops/pooling/adaptive_avg_pool_aten_kernels.cc.md) | 17 | `AtenAdaptiveAvgPool3dOut`, `AtenAdaptiveAvgPool3dBackwardGradInput`, `AtenAdaptiveAvgPool2dBackward` |  |
| [`csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`](csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc.md) | 18 | `AdaptiveIntervals`, `AtenAdaptiveMaxPool2dOut`, `AdaptiveMaxPoolBuffers` |  |
| [`csrc/ops/pooling/avg_pool_aten_kernels.cc`](csrc/ops/pooling/avg_pool_aten_kernels.cc.md) | 17 | `BuildAvgPoolOutNd`, `BuildAvgPoolBackwardGradInputNd`, `k3dSpatialDimCount` |  |
| [`csrc/ops/pooling/max_pool_aten_kernels.cc`](csrc/ops/pooling/max_pool_aten_kernels.cc.md) | 35 | `CheckMaxPoolDtypes`, `AtenMaxPool3dWithIndicesOut`, `AtenMaxPool3dWithIndicesBackwardGradInput` |  |
| [`csrc/ops/pooling/max_pool_aten_kernels.h`](csrc/ops/pooling/max_pool_aten_kernels.h.md) | 3 | `TpuMaxPool1dAutograd`, `TpuMaxPool2dAutograd`, `TpuMaxPool3dAutograd` |  |
| [`csrc/ops/pooling/pooling.cc`](csrc/ops/pooling/pooling.cc.md) | 9 | `CreateBatchInput`, `RemoveTrivialBatch`, `GetPoolingOutputSize` |  |
| [`csrc/ops/pooling/pooling.h`](csrc/ops/pooling/pooling.h.md) | 12 | `batch_input`, `ReduceWindowAttributes`, `original_dim_size` |  |
| [`csrc/ops/precision_context.cc`](csrc/ops/precision_context.cc.md) | 12 | `GetAndAddPrecisionTo`, `PyUnsafeGetPrecision`, `PyGetGlobalPrecision` | [dtype-and-precision](../concepts/dtype-and-precision.md) |
| [`csrc/ops/prelu/prelu_aten_kernels.cc`](csrc/ops/prelu/prelu_aten_kernels.cc.md) | 6 | `AtenPreluKernelBackward`, `AtenPreluKernel`, `ValidateIsFloatingPoint` |  |
| [`csrc/ops/prod/prod.cc`](csrc/ops/prod/prod.cc.md) | 4 | `BuildProdShlo`, `GetProdInitValue`, `BuildProdShlo` |  |
| [`csrc/ops/prod/prod_aten_kernels.cc`](csrc/ops/prod/prod_aten_kernels.cc.md) | 6 | `AtenProdDimOut`, `AtenProd`, `AtenProdHelper` |  |
| [`csrc/ops/put/put_aten_kernels.cc`](csrc/ops/put/put_aten_kernels.cc.md) | 3 | `AtenPut_`, `ValidateInputs`, `BuildPutShlo` |  |
| [`csrc/ops/python_context.cc`](csrc/ops/python_context.cc.md) | 33 | `ScopedPythonContextCapturer`, `GetRootOpName`, `GetContext` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md), [op-names-and-python-context](../concepts/op-names-and-python-context.md) |
| [`csrc/ops/python_context.h`](csrc/ops/python_context.h.md) | 44 | `ScopedPythonContextCapturer`, `PythonContext`, `ScopedPythonContextProvider` | [dynamic-shape-ops](../concepts/dynamic-shape-ops.md), [op-names-and-python-context](../concepts/op-names-and-python-context.md) |
| [`csrc/ops/python_context_test.cc`](csrc/ops/python_context_test.cc.md) | 123 | `ElementsAre`, `ScopedPythonContextCapturerTrackebackTest`, `ScopedPythonContextCapturerTrackebackTest_CapturesTracebackWhenEnabled_Test` |  |
| [`csrc/ops/random/random.cc`](csrc/ops/random/random.cc.md) | 4 | `BuildRandomShlo`, `BitsToRandomIntegersInRange`, `AddLowerBound` |  |
| [`csrc/ops/random/random_aten_kernels.cc`](csrc/ops/random/random_aten_kernels.cc.md) | 10 | `Random`, `AtenRandom_`, `AtenRandom_From` |  |
| [`csrc/ops/randperm/randperm_aten_kernels.cc`](csrc/ops/randperm/randperm_aten_kernels.cc.md) | 2 | `AtenRandpermGeneratorOut`, `BuildRandpermShlo` |  |
| [`csrc/ops/reductions/mean_aten_kernels.cc`](csrc/ops/reductions/mean_aten_kernels.cc.md) | 3 | `BuildMeanShlo`, `AtenMeanOut`, `GetOutputScalarType` | [reductions](../concepts/reductions.md) |
| [`csrc/ops/reductions/reduction_utils.cc`](csrc/ops/reductions/reduction_utils.cc.md) | 10 | `CanonicalizeDims`, `GetSizesAfterReduction`, `ValidateFloatOrComplex` | [reductions](../concepts/reductions.md) |
| [`csrc/ops/reductions/reductions.cc`](csrc/ops/reductions/reductions.cc.md) | 3 | `BuildReductionShlo`, `BuildKeepDimsShlo`, `BuildReductionShlo` | [reductions](../concepts/reductions.md) |
| [`csrc/ops/reductions/reductions.h`](csrc/ops/reductions/reductions.h.md) | 3 | `ReductionMode`, `kDropDims`, `kKeepDims` | [reductions](../concepts/reductions.md) |
| [`csrc/ops/reductions/std_aten_kernels.cc`](csrc/ops/reductions/std_aten_kernels.cc.md) | 5 | `AtenStd`, `AtenStdOut`, `CreateStdBuilder` | [reductions](../concepts/reductions.md) |
| [`csrc/ops/reductions/sum.cc`](csrc/ops/reductions/sum.cc.md) | 1 | `BuildSumShlo` | [reductions](../concepts/reductions.md) |
| [`csrc/ops/reductions/sum_aten_kernels.cc`](csrc/ops/reductions/sum_aten_kernels.cc.md) | 1 | `AtenSumIntListOut` | [reductions](../concepts/reductions.md) |
| [`csrc/ops/reductions/var_aten_kernels.cc`](csrc/ops/reductions/var_aten_kernels.cc.md) | 6 | `WarnIfInvalidCorrection`, `AtenVarMeanCorrection`, `AtenVar` | [reductions](../concepts/reductions.md) |
| [`csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc`](csrc/ops/reflection_pad/reflection_pad_aten_kernels.cc.md) | 16 | `ReflectionPadHelper`, `AtenReflectionPad2dBackwardGradInput`, `AtenReflectionPad2dOut` |  |
| [`csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`](csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc.md) | 29 | `AtenRepeatInterleaveSelfInt`, `IsFakeOrFunctorchTensor`, `RepeatsStats` |  |
| [`csrc/ops/replication_pad/replication_pad_aten_kernels.cc`](csrc/ops/replication_pad/replication_pad_aten_kernels.cc.md) | 13 | `ReplicationPadHelper`, `AtenReplicationPad2dBackwardGradInput`, `AtenReplicationPad3dBackwardGradInput` |  |
| [`csrc/ops/resize/resize_aten_kernels.cc`](csrc/ops/resize/resize_aten_kernels.cc.md) | 2 | `ResizeTensor`, `AtenResize_` |  |
| [`csrc/ops/resize/resize_aten_kernels.h`](csrc/ops/resize/resize_aten_kernels.h.md) | 1 | `ResizeTensorIfShapeDiffers` |  |
| [`csrc/ops/rms_norm/rms_norm.cc`](csrc/ops/rms_norm/rms_norm.cc.md) | 6 | `BuildRmsNormShlo`, `BuildRmsNormBackwardShlo`, `BuildRmsNormDx` |  |
| [`csrc/ops/rms_norm/rms_norm.h`](csrc/ops/rms_norm/rms_norm.h.md) | 3 | `RmsNormBackwardShloResults`, `grad_weight`, `grad_input` |  |
| [`csrc/ops/rms_norm/rms_norm_aten_kernels.cc`](csrc/ops/rms_norm/rms_norm_aten_kernels.cc.md) | 10 | `ValidateRmsNormInputs`, `AtenRmsNorm`, `GetRmsNormEpsilon` |  |
| [`csrc/ops/rng_utils.h`](csrc/ops/rng_utils.h.md) | 7 | `RngUsage`, `DispatchRngOpGeneral`, `DispatchRngOp` | [device-streams-generators-and-rng](../concepts/device-streams-generators-and-rng.md) |
| [`csrc/ops/roll/roll_aten_kernels.cc`](csrc/ops/roll/roll_aten_kernels.cc.md) | 2 | `AtenRoll`, `BuildRollShlo` |  |
| [`csrc/ops/round/round.cc`](csrc/ops/round/round.cc.md) | 1 | `BuildRoundShlo` |  |
| [`csrc/ops/round/round_aten_kernels.cc`](csrc/ops/round/round_aten_kernels.cc.md) | 4 | `AtenRoundDecimalsOut`, `AtenRoundOut`, `ValidateNumericDtype` |  |
| [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc`](csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc.md) | 51 | `BwdArgIndices`, `LoadedTiles`, `do_2d` | [mosaic-matmul](../concepts/mosaic-matmul.md), [scaled-dot-product-attention](../concepts/scaled-dot-product-attention.md) |
| [`csrc/ops/scaled_dot_product_attention/flash_attention_config.h`](csrc/ops/scaled_dot_product_attention/flash_attention_config.h.md) | 50 | `FlashAttnConfig`, `Tiling`, `qt` | [scaled-dot-product-attention](../concepts/scaled-dot-product-attention.md) |
| [`csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`](csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc.md) | 30 | `SoftmaxState`, `KernelArgs`, `m` | [mosaic-matmul](../concepts/mosaic-matmul.md), [scaled-dot-product-attention](../concepts/scaled-dot-product-attention.md) |
| [`csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`](csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc.md) | 24 | `PadSequenceDim`, `kMinHeuristicTileSize`, `RoundUpToTileSize` | [scaled-dot-product-attention](../concepts/scaled-dot-product-attention.md) |
| [`csrc/ops/scaled_dot_product_attention/helpers.cc`](csrc/ops/scaled_dot_product_attention/helpers.cc.md) | 8 | `flatten_batch_dims`, `get_batch_size`, `EmptyLikeStrides` | [scaled-dot-product-attention](../concepts/scaled-dot-product-attention.md) |
| [`csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc`](csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc.md) | 13 | `AtenFusedSdpChoice`, `AtenScaledDotProductFusedAttentionOverrideable`, `AtenScaledDotProductFusedAttentionOverrideableBackward` | [scaled-dot-product-attention](../concepts/scaled-dot-product-attention.md) |
| [`csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`](csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc.md) | 39 | `ConvertElementTypeIfNeeded`, `SdpaPromotionType`, `BackwardGradients4D` | [scaled-dot-product-attention](../concepts/scaled-dot-product-attention.md) |
| [`csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.h`](csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.h.md) | 3 | `FusedAttentionResults`, `logsumexp`, `output` |  |
| [`csrc/ops/scaled_dot_product_attention/util.cc`](csrc/ops/scaled_dot_product_attention/util.cc.md) | 39 | `SplatConstant`, `ScaleValue`, `AppendScalarPrefetchTypes` | [scaled-dot-product-attention](../concepts/scaled-dot-product-attention.md) |
| [`csrc/ops/scaled_dot_product_attention/util.h`](csrc/ops/scaled_dot_product_attention/util.h.md) | 3 | `KVWindowMaps`, `v_map`, `k_map` | [scaled-dot-product-attention](../concepts/scaled-dot-product-attention.md) |
| [`csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`](csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc.md) | 26 | `Operand`, `AtenScaledMmV2`, `AtenScaledMm` |  |
| [`csrc/ops/scan_builder.cc`](csrc/ops/scan_builder.cc.md) | 29 | `BuildScanShlo`, `BuildScanShlo`, `CreateRankReducedConstantLike` |  |
| [`csrc/ops/scan_builder.h`](csrc/ops/scan_builder.h.md) | 13 | `ScanDirection`, `kForward`, `ScanBodyResults` |  |
| [`csrc/ops/scan_builder_test.cc`](csrc/ops/scan_builder_test.cc.md) | 237 | `op_builder`, `builder`, `MultiScanBuilderTest` |  |
| [`csrc/ops/scatter/scatter.cc`](csrc/ops/scatter/scatter.cc.md) | 3 | `BuildScatterShlo`, `GetIdentityValue`, `GetRowBroadcastIndex` |  |
| [`csrc/ops/scatter/scatter.h`](csrc/ops/scatter/scatter.h.md) | 17 | `ScatterOp`, `ScatterIncludeSelf`, `kYes` |  |
| [`csrc/ops/scatter/scatter_aten_kernels.cc`](csrc/ops/scatter/scatter_aten_kernels.cc.md) | 8 | `Scatter`, `AtenScatterReduceOut`, `ParseScatterOp` |  |
| [`csrc/ops/searchsorted_aten_kernels.cc`](csrc/ops/searchsorted_aten_kernels.cc.md) | 14 | `AtenSearchsortedScalarOut`, `AtenSearchsortedTensorOut`, `AtenSearchsortedScalar` |  |
| [`csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc`](csrc/ops/segment_reduce/segment_reduce_aten_kernels.cc.md) | 23 | `SegmentReduceOp`, `kMean`, `kProd` |  |
| [`csrc/ops/select_scatter/select_scatter_aten_kernels.cc`](csrc/ops/select_scatter/select_scatter_aten_kernels.cc.md) | 3 | `AtenSelectScatterOut`, `AtenSelectScatter`, `BuildSelectScatterShlo` |  |
| [`csrc/ops/set/set_aten_kernels.cc`](csrc/ops/set/set_aten_kernels.cc.md) | 4 | `AtenSet_SourceStorageOffset`, `AtenSet_`, `AtenSet_SourceStorage` |  |
| [`csrc/ops/sigmoid/sigmoid_aten_kernels.cc`](csrc/ops/sigmoid/sigmoid_aten_kernels.cc.md) | 10 | `BuildSigmoidShlo`, `AtenSigmoidOut`, `AtenSigmoidBackwardGradInput` |  |
| [`csrc/ops/silu/silu_aten_kernels.cc`](csrc/ops/silu/silu_aten_kernels.cc.md) | 11 | `ValidateSiluBackwardInputs`, `ValidateSiluBackwardInputsOrThrow`, `SiluBackwardComposite` |  |
| [`csrc/ops/slice_backward/slice_backward_aten_kernels.cc`](csrc/ops/slice_backward/slice_backward_aten_kernels.cc.md) | 6 | `AtenSelectBackward`, `AtenSliceBackward`, `BuildUnitStrideSliceBackwardShlo` |  |
| [`csrc/ops/slice_scatter/slice_scatter_aten_kernels.cc`](csrc/ops/slice_scatter/slice_scatter_aten_kernels.cc.md) | 5 | `AtenSliceScatterOut`, `AtenSliceScatter`, `BuildSliceScatterShlo` |  |
| [`csrc/ops/softmax/_masked_softmax_aten_kernels.cc`](csrc/ops/softmax/_masked_softmax_aten_kernels.cc.md) | 8 | `AtenMaskedSoftmax`, `AtenMaskedSoftmaxBackward`, `AtenMaskedSoftmaxBackwardOut` |  |
| [`csrc/ops/softmax/softmax.cc`](csrc/ops/softmax/softmax.cc.md) | 8 | `BuildSoftmaxShlo`, `BuildSoftmaxBackwardDataShlo`, `BuildSoftmaxBackwardDataShlo` |  |
| [`csrc/ops/softmax/softmax.h`](csrc/ops/softmax/softmax.h.md) | 4 | `SoftmaxMode`, `kSoftmax`, `kLogSoftmax` | [compilation-cache-key](../concepts/compilation-cache-key.md) |
| [`csrc/ops/softmax/softmax_aten_kernels.cc`](csrc/ops/softmax/softmax_aten_kernels.cc.md) | 10 | `SoftmaxBackwardDataInternalOut`, `AtenLogSoftmaxBackwardDataOut`, `AtenLogSoftmaxOut` |  |
| [`csrc/ops/softplus/softplus_aten_kernels.cc`](csrc/ops/softplus/softplus_aten_kernels.cc.md) | 4 | `AtenSoftplusBackwardGradInput`, `AtenSoftplusOut`, `BuildSoftplusBackwardShlo` |  |
| [`csrc/ops/sort/sort.cc`](csrc/ops/sort/sort.cc.md) | 2 | `BuildSortShlo`, `BuildSortShlo` |  |
| [`csrc/ops/sort/sort.h`](csrc/ops/sort/sort.h.md) | 3 | `SortShloOutputs`, `values`, `indices` |  |
| [`csrc/ops/sort/sort_aten_kernels.cc`](csrc/ops/sort/sort_aten_kernels.cc.md) | 1 | `AtenSortValuesStable` |  |
| [`csrc/ops/sparse_coo/sparse_coo.cc`](csrc/ops/sparse_coo/sparse_coo.cc.md) | 16 | `BuildMulSparseScalarShlo`, `BuildSliceCoalescedShlo`, `ScatterAddSparseToDense` |  |
| [`csrc/ops/sparse_coo/sparse_coo_aten_kernels.cc`](csrc/ops/sparse_coo/sparse_coo_aten_kernels.cc.md) | 58 | `MakeSparseCooTensor`, `CopyOrCastValuesTensor`, `CopyIndicesTensor` |  |
| [`csrc/ops/split_with_sizes_copy/split_with_sizes_copy_aten_kernels.cc`](csrc/ops/split_with_sizes_copy/split_with_sizes_copy_aten_kernels.cc.md) | 1 | `AtenSplitWithSizesCopyOut` |  |
| [`csrc/ops/stride/stride_helper.cc`](csrc/ops/stride/stride_helper.cc.md) | 6 | `ValidateProvidedLayoutDataFitsInStorage`, `CalculateStridesContiguous`, `IsOverlapping` |  |
| [`csrc/ops/take/take_aten_kernels.cc`](csrc/ops/take/take_aten_kernels.cc.md) | 5 | `AtenTake`, `AtenTakeOut`, `ValidateTakeInputs` |  |
| [`csrc/ops/tanh/tanh_aten_kernels.cc`](csrc/ops/tanh/tanh_aten_kernels.cc.md) | 2 | `AtenTanhBackwardGradInput`, `BuildTanhBackwardGradInputShlo` |  |
| [`csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc`](csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc.md) | 15 | `CreateConstantFilledTensor`, `CreateScalarFilledTensor`, `ValidateLikeMemoryFormat` |  |
| [`csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc`](csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc.md) | 12 | `AtenThnnFusedGruCellBackward`, `AtenThnnFusedGruCellOut`, `AtenThnnFusedGruCell` |  |
| [`csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc`](csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc.md) | 12 | `AtenThnnFusedLstmCellBackwardImpl`, `AtenThnnFusedLstmCellOut`, `AtenThnnFusedLstmCell` |  |
| [`csrc/ops/threshold/threshold_aten_kernels.cc`](csrc/ops/threshold/threshold_aten_kernels.cc.md) | 5 | `AtenThresholdBackwardGradInput`, `AtenThresholdOut`, `ValidateThresholdInputs` |  |
| [`csrc/ops/to_copy/to_copy_aten_kernels.cc`](csrc/ops/to_copy/to_copy_aten_kernels.cc.md) | 1 | `AtenToCopy` |  |
| [`csrc/ops/topk/topk.cc`](csrc/ops/topk/topk.cc.md) | 1 | `BuildTopKShlo` |  |
| [`csrc/ops/topk/topk.h`](csrc/ops/topk/topk.h.md) | 9 | `TopKOutputs`, `TopKMode`, `TopKStableMode` |  |
| [`csrc/ops/topk/topk_aten_kernels.cc`](csrc/ops/topk/topk_aten_kernels.cc.md) | 1 | `AtenTopKValues` |  |
| [`csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc`](csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc.md) | 11 | `AtenTransformerEncoderLayerFwd`, `kGelu`, `Activation` |  |
| [`csrc/ops/triangular/triangular.cc`](csrc/ops/triangular/triangular.cc.md) | 3 | `BuildTriangularShlo`, `TriangularMask`, `TriangularMask` |  |
| [`csrc/ops/triangular/triangular.h`](csrc/ops/triangular/triangular.h.md) | 3 | `TriangleType`, `kUpper`, `kLower` |  |
| [`csrc/ops/triangular/triangular_aten_kernels.cc`](csrc/ops/triangular/triangular_aten_kernels.cc.md) | 2 | `AtenTrilOut`, `AtenTriuOut` |  |
| [`csrc/ops/tril_indices/tril_indices.cc`](csrc/ops/tril_indices/tril_indices.cc.md) | 1 | `BuildTrilIndicesShlo` |  |
| [`csrc/ops/tril_indices/tril_indices_aten_kernels.cc`](csrc/ops/tril_indices/tril_indices_aten_kernels.cc.md) | 2 | `AtenTrilIndices`, `GetTrilIndicesFunctional` |  |
| [`csrc/ops/unary.cc`](csrc/ops/unary.cc.md) | 18 | `BuildConjPhysicalShlo`, `BuildAbsShlo`, `BuildLogShlo` |  |
| [`csrc/ops/unary.h`](csrc/ops/unary.h.md) | 21 | `BuildSqrtShlo`, `BuildNegShlo`, `BuildTanhShlo` |  |
| [`csrc/ops/unary_aten_kernels.cc`](csrc/ops/unary_aten_kernels.cc.md) | 46 | `UnaryOpOut`, `UnaryOp`, `UnaryOpInPlace` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md) |
| [`csrc/ops/unary_aten_kernels.h`](csrc/ops/unary_aten_kernels.h.md) | 7 | `UnaryOpOptions`, `op_name`, `op_param_cache_keys` | [aten-kernel-authoring](../concepts/aten-kernel-authoring.md) |
| [`csrc/ops/unfold/unfold_aten_kernels.cc`](csrc/ops/unfold/unfold_aten_kernels.cc.md) | 3 | `AtenUnfold`, `AtenUnfoldBackward`, `BuildUnfoldBackwardShlo` |  |
| [`csrc/ops/uniform/uniform.cc`](csrc/ops/uniform/uniform.cc.md) | 5 | `BuildUniformShlo`, `BuildUniformShlo`, `BuildUniformShlo` |  |
| [`csrc/ops/uniform/uniform_aten_kernels.cc`](csrc/ops/uniform/uniform_aten_kernels.cc.md) | 4 | `AtenUniform_`, `ValidateUniformPreconditions`, `GetUniformFunctional` |  |
| [`csrc/ops/unique/unique.cc`](csrc/ops/unique/unique.cc.md) | 5 | `BuildUnique2Shlo`, `BuildUniqueGetOutputSizeShlo`, `BuildUniqueMask` |  |
| [`csrc/ops/unique/unique.h`](csrc/ops/unique/unique.h.md) | 4 | `BuildUniqueShloOutputs`, `counts`, `inverse_indices` |  |
| [`csrc/ops/unique/unique_aten_kernels.cc`](csrc/ops/unique/unique_aten_kernels.cc.md) | 3 | `AtenUnique2`, `Unique2`, `GetUniqueCount` |  |
| [`csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc`](csrc/ops/unique_consecutive/unique_consecutive_aten_kernels.cc.md) | 27 | `inverse_indices`, `BuildUniqueConsecutiveShloOutputs`, `counts` |  |
| [`csrc/ops/upsample/upsample_aten_kernels.cc`](csrc/ops/upsample/upsample_aten_kernels.cc.md) | 62 | `UpsampleMode`, `ConstructScaleFactorArray`, `ConstructScaleFactorArray` |  |
| [`csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`](csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc.md) | 37 | `BicubicDimInfo`, `TapIndex`, `BicubicGatherConfig` |  |
| [`csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`](csrc/ops/upsample/upsample_linear1d_aten_kernels.cc.md) | 23 | `AlignCorners`, `AtenUpsampleLinear1dOut`, `Linear1dDimInfo` |  |
| [`csrc/ops/view/view_aten_kernels.cc`](csrc/ops/view/view_aten_kernels.cc.md) | 9 | `AtenViewAsReal`, `AtenViewAsComplex`, `AtenView` |  |
| [`csrc/ops/view_decomposition/bitcast_primitive.cc`](csrc/ops/view_decomposition/bitcast_primitive.cc.md) | 27 | `operator<<`, `operator<<`, `operator<<` | [view-decomposition](../concepts/view-decomposition.md) |
| [`csrc/ops/view_decomposition/bitcast_primitive.h`](csrc/ops/view_decomposition/bitcast_primitive.h.md) | 15 | `RealToRealBitcast`, `ComplexToRealBitcast`, `ComplexElementType` | [view-decomposition](../concepts/view-decomposition.md) |
| [`csrc/ops/view_decomposition/bitcast_primitive_test.cc`](csrc/ops/view_decomposition/bitcast_primitive_test.cc.md) | 135 | `TestBody`, `TestBody`, `TestBody` |  |
| [`csrc/ops/view_decomposition/broadcast_primitive.cc`](csrc/ops/view_decomposition/broadcast_primitive.cc.md) | 6 | `operator<<`, `UpdateLayout`, `ViewPrimitiveShlo` |  |
| [`csrc/ops/view_decomposition/broadcast_primitive.h`](csrc/ops/view_decomposition/broadcast_primitive.h.md) | 4 | `BroadcastPrimitive`, `broadcast_dimensions`, `new_sizes` |  |
| [`csrc/ops/view_decomposition/broadcast_primitive_test.cc`](csrc/ops/view_decomposition/broadcast_primitive_test.cc.md) | 36 | `UpdateLayoutBroadcast_ScalarNoOp_Test`, `UpdateLayoutBroadcast_ScalarToTensor_Test`, `UpdateLayoutBroadcast_TensorNoOp_Test` |  |
| [`csrc/ops/view_decomposition/conj_primitive.h`](csrc/ops/view_decomposition/conj_primitive.h.md) | 3 | `ConjPrimitive`, `UpdateLayout`, `is_set` |  |
| [`csrc/ops/view_decomposition/contiguous_to_view.cc`](csrc/ops/view_decomposition/contiguous_to_view.cc.md) | 14 | `ContiguousToView`, `NonOverlappingWindow`, `GetNonOverlappingWindows` | [view-decomposition](../concepts/view-decomposition.md) |
| [`csrc/ops/view_decomposition/decomposition.cc`](csrc/ops/view_decomposition/decomposition.cc.md) | 46 | `DecomposeIntoViewSequence`, `GetContiguousBaseShape`, `DecomposeIntoViewSequence` | [view-decomposition](../concepts/view-decomposition.md) |
| [`csrc/ops/view_decomposition/decomposition_test.cc`](csrc/ops/view_decomposition/decomposition_test.cc.md) | 480 | `DecompositionTest`, `GetContiguousBaseShapeTest`, `ValidateViewSequence` |  |
| [`csrc/ops/view_decomposition/inversion.cc`](csrc/ops/view_decomposition/inversion.cc.md) | 43 | `ComputeInverseViewOperation`, `operator==`, `operator==` | [view-decomposition](../concepts/view-decomposition.md) |
| [`csrc/ops/view_decomposition/inversion.h`](csrc/ops/view_decomposition/inversion.h.md) | 12 | `InverseViewStage`, `InverseViewOperation`, `stages` | [view-decomposition](../concepts/view-decomposition.md) |
| [`csrc/ops/view_decomposition/inversion_test.cc`](csrc/ops/view_decomposition/inversion_test.cc.md) | 432 | `TestBody`, `TestBody`, `TestBody` |  |
| [`csrc/ops/view_decomposition/pad_primitive.cc`](csrc/ops/view_decomposition/pad_primitive.cc.md) | 7 | `operator<<`, `operator<<`, `operator==` |  |
| [`csrc/ops/view_decomposition/pad_primitive.h`](csrc/ops/view_decomposition/pad_primitive.h.md) | 6 | `PadPrimitive`, `pad_dims`, `PadDimension` |  |
| [`csrc/ops/view_decomposition/pad_primitive_test.cc`](csrc/ops/view_decomposition/pad_primitive_test.cc.md) | 27 | `UpdateLayoutPad_ScalarNoOp_Test`, `UpdateLayoutPad_TensorNoOp_Test`, `UpdateLayoutPad_TensorToTensor_Test` |  |
| [`csrc/ops/view_decomposition/reshape_primitive.cc`](csrc/ops/view_decomposition/reshape_primitive.cc.md) | 11 | `operator<<`, `UpdateLayout`, `ViewPrimitiveShlo` | [view-decomposition](../concepts/view-decomposition.md) |
| [`csrc/ops/view_decomposition/reshape_primitive.h`](csrc/ops/view_decomposition/reshape_primitive.h.md) | 3 | `ReshapePrimitive`, `new_sizes`, `base_sizes` | [view-decomposition](../concepts/view-decomposition.md) |
| [`csrc/ops/view_decomposition/reshape_primitive_test.cc`](csrc/ops/view_decomposition/reshape_primitive_test.cc.md) | 72 | `TestBody`, `MergeSequentialReshape_ValidMerge_Test`, `UpdateLayoutReshape_ScalarNoOp_Test` |  |
| [`csrc/ops/view_decomposition/slice_primitive.cc`](csrc/ops/view_decomposition/slice_primitive.cc.md) | 9 | `operator<<`, `operator<<`, `operator==` | [view-decomposition](../concepts/view-decomposition.md) |
| [`csrc/ops/view_decomposition/slice_primitive.h`](csrc/ops/view_decomposition/slice_primitive.h.md) | 6 | `SlicePrimitive`, `slice_dims`, `SliceDimension` | [view-decomposition](../concepts/view-decomposition.md) |
| [`csrc/ops/view_decomposition/slice_primitive_test.cc`](csrc/ops/view_decomposition/slice_primitive_test.cc.md) | 36 | `TestBody`, `MergeSlice_ValidMerge_Test`, `UpdateLayoutSlice_ScalarNoOp_Test` |  |
| [`csrc/ops/view_decomposition/strided_layout.cc`](csrc/ops/view_decomposition/strided_layout.cc.md) | 7 | `MakeContiguousBaseLayout`, `operator<<`, `operator==` | [view-decomposition](../concepts/view-decomposition.md) |
| [`csrc/ops/view_decomposition/strided_layout.h`](csrc/ops/view_decomposition/strided_layout.h.md) | 7 | `StridedLayout`, `strided_dims`, `size` | [view-decomposition](../concepts/view-decomposition.md) |
| [`csrc/ops/view_decomposition/strided_layout_test.cc`](csrc/ops/view_decomposition/strided_layout_test.cc.md) | 117 | `GetSizes_EmptyLayout_Test`, `GetSizes_ReturnsDimensionSizes_Test`, `GetStrides_EmptyLayout_Test` |  |
| [`csrc/ops/view_decomposition/transpose_primitive.cc`](csrc/ops/view_decomposition/transpose_primitive.cc.md) | 4 | `operator<<`, `UpdateLayout`, `ViewPrimitiveShlo` |  |
| [`csrc/ops/view_decomposition/transpose_primitive.h`](csrc/ops/view_decomposition/transpose_primitive.h.md) | 2 | `TransposePrimitive`, `permutation` |  |
| [`csrc/ops/view_decomposition/transpose_primitive_test.cc`](csrc/ops/view_decomposition/transpose_primitive_test.cc.md) | 27 | `UpdateLayoutPermute_ScalarNoOp_Test`, `UpdateLayoutPermute_TensorNoOp_Test`, `UpdateLayoutPermute_TensorToTensor_Test` |  |
| [`csrc/ops/view_decomposition/unfold_primitive.cc`](csrc/ops/view_decomposition/unfold_primitive.cc.md) | 6 | `UpdateLayout`, `operator<<`, `ViewPrimitiveShlo` |  |
| [`csrc/ops/view_decomposition/unfold_primitive.h`](csrc/ops/view_decomposition/unfold_primitive.h.md) | 5 | `UnfoldPrimitive`, `start_index`, `limit_index` |  |
| [`csrc/ops/view_decomposition/unfold_primitive_test.cc`](csrc/ops/view_decomposition/unfold_primitive_test.cc.md) | 27 | `UpdateLayoutUnfold_TensorNoOp_Test`, `UpdateLayoutUnfold_TensorValidUnfold_Test`, `UpdateLayoutUnfold_UnfoldWithStrideOnLastDimension_Test` |  |
| [`csrc/ops/view_decomposition/view_primitive_error_utils.h`](csrc/ops/view_decomposition/view_primitive_error_utils.h.md) | 10 | `GetUpdateLayoutBugSuffix`, `GetViewPrimitiveErrorSuffix`, `GetViewPrimitiveShloErrorSuffix` |  |
| [`csrc/ops/view_decomposition/view_primitive_error_utils_test.cc`](csrc/ops/view_decomposition/view_primitive_error_utils_test.cc.md) | 36 | `TestBody`, `TestBody`, `TestBody` |  |
| [`csrc/ops/view_decomposition/view_sequence.cc`](csrc/ops/view_decomposition/view_sequence.cc.md) | 37 | `operator==`, `UpdateLayout`, `UpdateLayout` | [view-decomposition](../concepts/view-decomposition.md) |
| [`csrc/ops/view_decomposition/view_sequence.h`](csrc/ops/view_decomposition/view_sequence.h.md) | 3 | `ViewSequence`, `ViewPrimitive`, `ViewSequenceSpan` |  |
| [`csrc/ops/view_decomposition/view_sequence_test.cc`](csrc/ops/view_decomposition/view_sequence_test.cc.md) | 246 | `SimplifyTest`, `Pair`, `ElementsAre` |  |
| [`csrc/ops/weight_norm/weight_norm_aten_kernels.cc`](csrc/ops/weight_norm/weight_norm_aten_kernels.cc.md) | 3 | `AtenWeightNormInterface`, `BuildWeightNormShlo`, `BuildWeightNormShlo` |  |
| [`csrc/ops/where/where.cc`](csrc/ops/where/where.cc.md) | 1 | `BuildWhereShlo` |  |
| [`csrc/ops/where/where_aten_kernels.cc`](csrc/ops/where/where_aten_kernels.cc.md) | 3 | `AtenWhereSelfOut`, `AtenWhereSelf`, `DispatchWhere` |  |
| [`csrc/ops/xla_utils.h`](csrc/ops/xla_utils.h.md) | 4 | `ToXlaBFloat16`, `ToXlaHalf`, `ToXlaComplex128` |  |
| [`csrc/ops/xlogy/xlogy_aten_kernels.cc`](csrc/ops/xlogy/xlogy_aten_kernels.cc.md) | 2 | `AtenXlogyOutTensor`, `BuildXlogyShlo` |  |

## `csrc/pjrt`

Index: [`symbols/csrc-pjrt.tsv`](symbols/csrc-pjrt.tsv) (158 rows), [`edges/csrc-pjrt.tsv`](edges/csrc-pjrt.tsv) (541 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`csrc/pjrt/pjrt_client.cc`](csrc/pjrt/pjrt_client.cc.md) | 2 | `GetPjRtClient`, `GetPjRtClient` | [pjrt-client](../concepts/pjrt-client.md) |
| [`csrc/pjrt/pjrt_execute.cc`](csrc/pjrt/pjrt_execute.cc.md) | 10 | `Execute`, `DynamicExecutionArguments`, `ephemeral_buffers` | [pjrt-client](../concepts/pjrt-client.md) |
| [`csrc/pjrt/pjrt_execute.h`](csrc/pjrt/pjrt_execute.h.md) | 1 | `PjRtBufferPointers` | [pjrt-client](../concepts/pjrt-client.md) |
| [`csrc/pjrt/pjrt_execute_test.cc`](csrc/pjrt/pjrt_execute_test.cc.md) | 15 | `PjrtExecuteTest_Execute_WithDynamicExecutionMetadata_RoutesInputsOutputsAndMetadata_Test`, `client_`, `memory_space_` |  |
| [`csrc/pjrt/pjrt_init_test.cc`](csrc/pjrt/pjrt_init_test.cc.md) | 78 | `PjRtInitTest`, `PjRtInitTest_BadForkCheckerPreventsAccessAfterInit_Test`, `PjRtInitTest_GetClientAndGetDeviceFailForUnsupportedDeviceType_Test` |  |
| [`csrc/pjrt/pjrt_state.cc`](csrc/pjrt/pjrt_state.cc.md) | 26 | `GetInstance`, `GetClient`, `SetPjRtInitializationOptions` | [compilation-cache](../concepts/compilation-cache.md), [pjrt-client](../concepts/pjrt-client.md) |
| [`csrc/pjrt/pjrt_state.h`](csrc/pjrt/pjrt_state.h.md) | 33 | `PjrtBackend`, `mutex_`, `PjRtDeviceAttributes` | [pjrt-client](../concepts/pjrt-client.md) |
| [`csrc/pjrt/pjrt_transfer.cc`](csrc/pjrt/pjrt_transfer.cc.md) | 27 | `TpuMallocAndMemcpyHtoD`, `RawBufferHolder`, `TpuMemcpyDtoH` | [pjrt-client](../concepts/pjrt-client.md) |
| [`csrc/pjrt/pjrt_transfer.h`](csrc/pjrt/pjrt_transfer.h.md) | 3 | `AsyncDmaResult`, `buffer_hold`, `future` |  |
| [`csrc/pjrt/pjrt_utils.cc`](csrc/pjrt/pjrt_utils.cc.md) | 5 | `TpuDeviceSupportsSparseCore`, `ToString`, `GetDefaultMemorySpace` | [pjrt-client](../concepts/pjrt-client.md) |

## `src/torch_tpu`

Index: [`symbols/src-torch_tpu.tsv`](symbols/src-torch_tpu.tsv) (2339 rows), [`edges/src-torch_tpu.tsv`](edges/src-torch_tpu.tsv) (2932 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`src/torch_tpu/_internal/batch_transfer/__init__.py`](src/torch_tpu/_internal/batch_transfer/__init__.md) | 7 | `TransferFuture`, `await_all`, `batch_transfer_d2h` |  |
| [`src/torch_tpu/_internal/benchmarks/export_adapter.py`](src/torch_tpu/_internal/benchmarks/export_adapter.md) | 3 | `_TEAM_NAME`, `_TENSORBOARD_OUTPUT_ENV_VAR`, `export_benchmark_results` |  |
| [`src/torch_tpu/_internal/benchmarks/xprof_adapter.py`](src/torch_tpu/_internal/benchmarks/xprof_adapter.md) | 17 | `TraceMe`, `__enter__`, `__exit__` |  |
| [`src/torch_tpu/_internal/compile/__init__.py`](src/torch_tpu/_internal/compile/__init__.md) | 9 | `_flex_attention_tpu`, `fold`, `_get_sdpa_attn_bias` |  |
| [`src/torch_tpu/_internal/compile/_backend.py`](src/torch_tpu/_internal/compile/_backend.md) | 55 | `_cache_save_lock`, `_pending_cache_saves`, `_cache_saves_manager` | [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md), [torch-compile-backend](../concepts/torch-compile-backend.md) |
| [`src/torch_tpu/_internal/compile/compiler.py`](src/torch_tpu/_internal/compile/compiler.md) | 20 | `StaticCompiler`, `CompilationContext`, `_is_tracing_enabled` | [compilation-pipeline](../concepts/compilation-pipeline.md), [fx-graph-passes](../concepts/fx-graph-passes.md), [torch-compile-backend](../concepts/torch-compile-backend.md) |
| [`src/torch_tpu/_internal/compile/debug.py`](src/torch_tpu/_internal/compile/debug.md) | 12 | `TpuCompileDebug`, `post_autograd_fx_backward_code`, `post_autograd_fx_forward_code` | [torch-compile-backend](../concepts/torch-compile-backend.md) |
| [`src/torch_tpu/_internal/compile/dynamic/convert_constant_symints_pass.py`](src/torch_tpu/_internal/compile/dynamic/convert_constant_symints_pass.md) | 7 | `_example_inputs`, `updated_example_inputs`, `_replace_node_with_value` |  |
| [`src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.py`](src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.md) | 11 | `static_compiler`, `_prepare_bucket_spec`, `_create_bounded_model_inputs` | [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md) |
| [`src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py`](src/torch_tpu/_internal/compile/dynamic/dynamic_executable.md) | 49 | `_bucket_specs`, `symbol_bounds`, `_symbol_to_input_loc` | [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md) |
| [`src/torch_tpu/_internal/compile/dynamic/dynamic_view_pass.py`](src/torch_tpu/_internal/compile/dynamic/dynamic_view_pass.md) | 7 | `_example_inputs`, `view_arg_indices`, `updated_example_inputs` |  |
| [`src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.py`](src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.md) | 11 | `_transform_context`, `_insert_set_dimension_logical_size`, `_process_bounded_size_op` | [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md) |
| [`src/torch_tpu/_internal/compile/dynamic/graph_transform_context.py`](src/torch_tpu/_internal/compile/dynamic/graph_transform_context.md) | 14 | `ensure_tensor`, `GraphTransformContext`, `get_upper_bound` | [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md) |
| [`src/torch_tpu/_internal/compile/dynamic/graph_transformations.py`](src/torch_tpu/_internal/compile/dynamic/graph_transformations.md) | 31 | `GraphTransformObserver`, `_transform_context`, `apply_dynamism_transformations` | [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md) |
| [`src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py`](src/torch_tpu/_internal/compile/dynamic/output_sym_shape.md) | 12 | `OutputSymShape`, `is_dynamic`, `output_sym_shape` | [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md) |
| [`src/torch_tpu/_internal/compile/dynamic/sym_bounds_manager.py`](src/torch_tpu/_internal/compile/dynamic/sym_bounds_manager.md) | 7 | `_atomic_symints`, `get_bucketed_symbol_bounds`, `get_fallback_symbol_bounds` | [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md) |
| [`src/torch_tpu/_internal/compile/dynamic/sym_utils.py`](src/torch_tpu/_internal/compile/dynamic/sym_utils.md) | 19 | `is_symint`, `is_symint_node`, `has_dynamic_shape` | [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md) |
| [`src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py`](src/torch_tpu/_internal/compile/dynamic/symbol_bounds.md) | 14 | `SymbolBounds`, `_symbol_ranges`, `get_symint_bounds` | [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md) |
| [`src/torch_tpu/_internal/compile/dynamic/view_decomposition.py`](src/torch_tpu/_internal/compile/dynamic/view_decomposition.md) | 20 | `_fmt_sym`, `_is_contiguous_tensor`, `_decompose_layout` | [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md) |
| [`src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py`](src/torch_tpu/_internal/compile/dynamic/view_ops_passes.md) | 36 | `_transform_context`, `_get_node_val`, `_replace_node_with_set_logical_sizes` | [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md) |
| [`src/torch_tpu/_internal/compile/fx_passes/clone_mutated_returned_placeholders.py`](src/torch_tpu/_internal/compile/fx_passes/clone_mutated_returned_placeholders.md) | 7 | `apply`, `_find_placeholders_to_clone`, `_clone_and_replace_placeholder` | [fx-graph-passes](../concepts/fx-graph-passes.md) |
| [`src/torch_tpu/_internal/compile/fx_passes/detect_causal_mask.py`](src/torch_tpu/_internal/compile/fx_passes/detect_causal_mask.md) | 8 | `_evaluate_node_on_inputs`, `_try_eliminate_causal_mask`, `apply` | [fx-graph-passes](../concepts/fx-graph-passes.md) |
| [`src/torch_tpu/_internal/compile/fx_passes/fold_gqa.py`](src/torch_tpu/_internal/compile/fx_passes/fold_gqa.md) | 11 | `apply`, `_RESHAPE_TARGETS`, `_extract_repeat_kv_source` | [fx-graph-passes](../concepts/fx-graph-passes.md) |
| [`src/torch_tpu/_internal/compile/fx_passes/force_collectives_output.py`](src/torch_tpu/_internal/compile/fx_passes/force_collectives_output.md) | 3 | `apply`, `_mark_live`, `_is_collective_or_wait` | [fx-graph-passes](../concepts/fx-graph-passes.md) |
| [`src/torch_tpu/_internal/compile/fx_passes/mark_activation_checkpoints.py`](src/torch_tpu/_internal/compile/fx_passes/mark_activation_checkpoints.md) | 1 | `apply` | [fx-graph-passes](../concepts/fx-graph-passes.md) |
| [`src/torch_tpu/_internal/compile/fx_passes/mark_embedded_constants.py`](src/torch_tpu/_internal/compile/fx_passes/mark_embedded_constants.md) | 1 | `apply` | [fx-graph-passes](../concepts/fx-graph-passes.md) |
| [`src/torch_tpu/_internal/compile/fx_passes/propagate_symints.py`](src/torch_tpu/_internal/compile/fx_passes/propagate_symints.md) | 2 | `_collect_free_symbols`, `apply` | [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md), [fx-graph-passes](../concepts/fx-graph-passes.md) |
| [`src/torch_tpu/_internal/compile/fx_passes/reorder_symints.py`](src/torch_tpu/_internal/compile/fx_passes/reorder_symints.md) | 1 | `apply` | [fx-graph-passes](../concepts/fx-graph-passes.md) |
| [`src/torch_tpu/_internal/compile/fx_passes/sink_get_attr_constants.py`](src/torch_tpu/_internal/compile/fx_passes/sink_get_attr_constants.md) | 7 | `_sink_constants_for_submodule`, `apply`, `_get_sinkable_constant` | [fx-graph-passes](../concepts/fx-graph-passes.md) |
| [`src/torch_tpu/_internal/compile/grouped_mm_meta.py`](src/torch_tpu/_internal/compile/grouped_mm_meta.md) | 6 | `_check`, `_name`, `_tpu_grouped_mm_meta` |  |
| [`src/torch_tpu/_internal/compile/scan.py`](src/torch_tpu/_internal/compile/scan.md) | 27 | `_callable_cache_key`, `_to_placeholder`, `_tpu_associative_scan` |  |
| [`src/torch_tpu/_internal/compile/split_compiler.py`](src/torch_tpu/_internal/compile/split_compiler.md) | 52 | `compiled_executables`, `_SplitCompiledExecutable`, `ProcessGroupId` | [fx-graph-passes](../concepts/fx-graph-passes.md), [torch-compile-backend](../concepts/torch-compile-backend.md) |
| [`src/torch_tpu/_internal/compile/torch_tpu_compiled_executable.py`](src/torch_tpu/_internal/compile/torch_tpu_compiled_executable.md) | 75 | `CompiledArtifact`, `_executable`, `_resolve` | [torch-compile-backend](../concepts/torch-compile-backend.md) |
| [`src/torch_tpu/_internal/compiler_options/__init__.py`](src/torch_tpu/_internal/compiler_options/__init__.md) | 2 | `__all__`, `custom_compiler_options` |  |
| [`src/torch_tpu/_internal/device/_device_module.py`](src/torch_tpu/_internal/device/_device_module.md) | 105 | `_public_module`, `experimental`, `_STRICT_INTERNAL_DEVICE_APIS` |  |
| [`src/torch_tpu/_internal/device_utils/annotations.py`](src/torch_tpu/_internal/device_utils/annotations.md) | 11 | `TpuLayout`, `tiles`, `minor_to_major` |  |
| [`src/torch_tpu/_internal/device_utils/annotations_test.py`](src/torch_tpu/_internal/device_utils/annotations_test.md) | 5 | `test_layout_context_1d_tiling`, `test_layout_context_device_arg`, `test_layout_context_nested` |  |
| [`src/torch_tpu/_internal/distributed/_distributed_module.py`](src/torch_tpu/_internal/distributed/_distributed_module.md) | 5 | `_get_backend_fn`, `window_num_stripes`, `window_stripe_chunk_mb` |  |
| [`src/torch_tpu/_internal/distributed/collective_ops.py`](src/torch_tpu/_internal/distributed/collective_ops.md) | 3 | `COLLECTIVE_OPS`, `_TPU_COLLECTIVE_NAMES`, `is_collective_op` |  |
| [`src/torch_tpu/_internal/distributed/device_mesh.py`](src/torch_tpu/_internal/distributed/device_mesh.md) | 15 | `slice_index`, `id`, `_DeviceStub` | [distributed-launchers-and-spmd](../concepts/distributed-launchers-and-spmd.md) |
| [`src/torch_tpu/_internal/distributed/device_utils.py`](src/torch_tpu/_internal/distributed/device_utils.md) | 37 | `_get_physical_tpu_mesh`, `_TPU_7`, `_TPU_7X` | [distributed-launchers-and-spmd](../concepts/distributed-launchers-and-spmd.md) |
| [`src/torch_tpu/_internal/distributed/distributed.py`](src/torch_tpu/_internal/distributed/distributed.md) | 18 | `require_worker_hostnames`, `_LOCAL_DEVICE_COORDS_PREFIX`, `_CHIPS_PER_HOST` |  |
| [`src/torch_tpu/_internal/distributed/distributed_test.py`](src/torch_tpu/_internal/distributed/distributed_test.md) | 48 | `_mock_env`, `_coords_process`, `get_int_env_once` |  |
| [`src/torch_tpu/_internal/distributed/from_local.py`](src/torch_tpu/_internal/distributed/from_local.md) | 5 | `from_local`, `_UNEVEN_SHARDING_WARNING`, `_is_debug_eager_mode` |  |
| [`src/torch_tpu/_internal/distributed/gpu_env.py`](src/torch_tpu/_internal/distributed/gpu_env.md) | 1 | `run_in_workers` |  |
| [`src/torch_tpu/_internal/distributed/handshake.py`](src/torch_tpu/_internal/distributed/handshake.md) | 140 | `_pg_to_count`, `ProcessGroupId`, `CollectiveHandshakeResponse` | [distributed-launchers-and-spmd](../concepts/distributed-launchers-and-spmd.md) |
| [`src/torch_tpu/_internal/distributed/multiprocessing.py`](src/torch_tpu/_internal/distributed/multiprocessing.md) | 5 | `parse_absl_flags`, `init_spawn`, `get_context` |  |
| [`src/torch_tpu/_internal/distributed/process_group_utils.py`](src/torch_tpu/_internal/distributed/process_group_utils.md) | 12 | `ranks`, `ProcessGroupId`, `_get_collective_op` |  |
| [`src/torch_tpu/_internal/distributed/spmd_util.py`](src/torch_tpu/_internal/distributed/spmd_util.md) | 5 | `wrapper`, `_synchronize_tensors`, `_F` |  |
| [`src/torch_tpu/_internal/distributed/torchcomm_tpu.py`](src/torch_tpu/_internal/distributed/torchcomm_tpu.md) | 81 | `_check_not_finalized`, `_pg`, `_device` | [distributed-launchers-and-spmd](../concepts/distributed-launchers-and-spmd.md) |
| [`src/torch_tpu/_internal/dynamism/__init__.py`](src/torch_tpu/_internal/dynamism/__init__.md) | 1 | `__all__` |  |
| [`src/torch_tpu/_internal/env_utils.py`](src/torch_tpu/_internal/env_utils.md) | 3 | `_resolved_values`, `set_str_env`, `get_and_set_str_env_once` |  |
| [`src/torch_tpu/_internal/execution_mode/__init__.py`](src/torch_tpu/_internal/execution_mode/__init__.md) | 19 | `_EagerMode`, `EagerMode`, `_unwrap_eager_mode` | [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md) |
| [`src/torch_tpu/_internal/export/__init__.py`](src/torch_tpu/_internal/export/__init__.md) | 3 | `__all__`, `exported_to_mlir`, `fx_to_mlir` |  |
| [`src/torch_tpu/_internal/export/export.py`](src/torch_tpu/_internal/export/export.md) | 44 | `module`, `_TensorLayout`, `ExportedMlir` | [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md) |
| [`src/torch_tpu/_internal/ops/__init__.py`](src/torch_tpu/_internal/ops/__init__.md) | 1 | `__all__` |  |
| [`src/torch_tpu/_internal/ops/collectives.py`](src/torch_tpu/_internal/ops/collectives.md) | 4 | `_resolve_group`, `all_gather_dim`, `reduce_scatter_dim` |  |
| [`src/torch_tpu/_internal/ops/jagged.py`](src/torch_tpu/_internal/ops/jagged.md) | 3 | `align_jagged_to_multiple`, `strip_jagged_padding`, `__all__` |  |
| [`src/torch_tpu/_internal/ops/ops.py`](src/torch_tpu/_internal/ops/ops.md) | 23 | `__all__`, `max_pool1d`, `max_pool1d_backward` |  |
| [`src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py`](src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.md) | 16 | `_expand_scale_axis`, `_BLOCK_SIZE`, `_ceil_div` | [python-ops](../concepts/python-ops.md) |
| [`src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py`](src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.md) | 21 | `_TestCase`, `_BLOCK_SIZE`, `test_pad_shapes_and_fill` | [python-ops](../concepts/python-ops.md) |
| [`src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py`](src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.md) | 37 | `_run_kernel`, `_FP8_E4M3`, `_BLOCK_SIZE` | [python-ops](../concepts/python-ops.md) |
| [`src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py`](src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.md) | 14 | `blockwise_scaled_mm`, `export_mlir_module`, `_pad_to_tiles` | [python-ops](../concepts/python-ops.md) |
| [`src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py`](src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.md) | 29 | `block_size`, `k`, `n` | [python-ops](../concepts/python-ops.md) |
| [`src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py`](src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.md) | 32 | `_BLOCK_SIZE`, `_FP8_E4M3`, `_run_kernel` | [python-ops](../concepts/python-ops.md) |
| [`src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py`](src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.md) | 20 | `generate_kernel_module`, `_RECIPE_GENERATORS`, `get_supported_recipes` | [pallas-custom-kernels](../concepts/pallas-custom-kernels.md), [python-ops](../concepts/python-ops.md) |
| [`src/torch_tpu/_internal/ops/splash_attention.py`](src/torch_tpu/_internal/ops/splash_attention.md) | 16 | `_single_bwd`, `_make_splash_attention_fn`, `_get_splash_op_names` | [python-ops](../concepts/python-ops.md) |
| [`src/torch_tpu/_internal/optim/__init__.py`](src/torch_tpu/_internal/optim/__init__.md) | 4 | `AdamW`, `patch_optimizer_graph_breaks`, `unpatch_optimizer_graph_breaks` |  |
| [`src/torch_tpu/_internal/optim/adamw.py`](src/torch_tpu/_internal/optim/adamw.md) | 5 | `AdamW`, `_eager_init_state`, `_my_init_group` |  |
| [`src/torch_tpu/_internal/optim/patch.py`](src/torch_tpu/_internal/optim/patch.md) | 10 | `_patch_closure_chain`, `_original_use_grad_for_differentiable`, `use_grad_for_differentiable` |  |
| [`src/torch_tpu/_internal/optimizers/adamw.py`](src/torch_tpu/_internal/optimizers/adamw.md) | 32 | `_AdamWBase`, `ParamGroup`, `params` | [python-optimizers](../concepts/python-optimizers.md) |
| [`src/torch_tpu/_internal/optimizers/muon.py`](src/torch_tpu/_internal/optimizers/muon.md) | 35 | `_MuonBase`, `ParamGroup`, `params` | [python-optimizers](../concepts/python-optimizers.md) |
| [`src/torch_tpu/_internal/optimizers/optim.py`](src/torch_tpu/_internal/optimizers/optim.md) | 11 | `_lr`, `_weight_decay`, `Optimizer` | [python-optimizers](../concepts/python-optimizers.md) |
| [`src/torch_tpu/_internal/optimizers/sgd.py`](src/torch_tpu/_internal/optimizers/sgd.md) | 28 | `_SgdBase`, `ParamGroup`, `params` | [python-optimizers](../concepts/python-optimizers.md) |
| [`src/torch_tpu/_internal/optimizers/single_trace_trainer.py`](src/torch_tpu/_internal/optimizers/single_trace_trainer.md) | 38 | `_param_group`, `_buffers`, `_key_map` | [python-optimizers](../concepts/python-optimizers.md) |
| [`src/torch_tpu/_internal/pallas/__init__.py`](src/torch_tpu/_internal/pallas/__init__.md) | 3 | `__all__`, `__dir__`, `__getattr__` |  |
| [`src/torch_tpu/_internal/pallas/_compat.py`](src/torch_tpu/_internal/pallas/_compat.md) | 1 | `warn_deprecation_with_skip` |  |
| [`src/torch_tpu/_internal/pallas/_mock_device.py`](src/torch_tpu/_internal/pallas/_mock_device.md) | 20 | `device_kind`, `id`, `platform` | [pallas-custom-kernels](../concepts/pallas-custom-kernels.md) |
| [`src/torch_tpu/_internal/pallas/mesh.py`](src/torch_tpu/_internal/pallas/mesh.md) | 1 | `get_pallas_mesh` |  |
| [`src/torch_tpu/_internal/pallas/pallas.py`](src/torch_tpu/_internal/pallas/pallas.md) | 82 | `_strip_optional`, `static_argnums`, `_get_sequence_element_type` | [pallas-custom-kernels](../concepts/pallas-custom-kernels.md) |
| [`src/torch_tpu/_internal/pallas/pallas_kernel_generate_utils.py`](src/torch_tpu/_internal/pallas/pallas_kernel_generate_utils.md) | 1 | `generate_embedded_file` | [pallas-custom-kernels](../concepts/pallas-custom-kernels.md) |
| [`src/torch_tpu/_internal/performance/micro/qwen3_explore.py`](src/torch_tpu/_internal/performance/micro/qwen3_explore.md) | 10 | `configs`, `FeedForward`, `fc1` |  |
| [`src/torch_tpu/_internal/performance/micro/utils.py`](src/torch_tpu/_internal/performance/micro/utils.md) | 4 | `run_model_cpu_acc`, `_get_device`, `_ACC` |  |
| [`src/torch_tpu/_internal/pooling/patch.py`](src/torch_tpu/_internal/pooling/patch.md) | 22 | `patched_max_pool2d`, `_is_tpu_tensor`, `patched_max_pool1d` |  |
| [`src/torch_tpu/_internal/pooling/patch_test.py`](src/torch_tpu/_internal/pooling/patch_test.md) | 11 | `_create_mock_tensor`, `test_patch_and_unpatch_lifecycle`, `test_patched_max_pool2d_tpu_train_routes_to_autograd_function` |  |
| [`src/torch_tpu/_internal/precision/__init__.py`](src/torch_tpu/_internal/precision/__init__.md) | 3 | `precision`, `Precision`, `__all__` |  |
| [`src/torch_tpu/_internal/precision/precision.py`](src/torch_tpu/_internal/precision/precision.md) | 5 | `Precision`, `experimental`, `_VALID_PRECISIONS` |  |
| [`src/torch_tpu/_internal/profiler/__init__.py`](src/torch_tpu/_internal/profiler/__init__.md) | 1 | `__all__` |  |
| [`src/torch_tpu/_internal/profiler/_api.py`](src/torch_tpu/_internal/profiler/_api.md) | 9 | `ProfilerActivity`, `CPU`, `TPU` |  |
| [`src/torch_tpu/_internal/profiler/_impl.py`](src/torch_tpu/_internal/profiler/_impl.md) | 17 | `profile_session`, `worker_rank`, `log_dir` |  |
| [`src/torch_tpu/_internal/profiler/profiler_config.py`](src/torch_tpu/_internal/profiler/profiler_config.md) | 12 | `_ExperimentalValue`, `_PK_CHECK_EXPERIMENTAL_OPTIONS`, `_PK_DEVICE_TRACER_LEVEL` |  |
| [`src/torch_tpu/_internal/public_api.py`](src/torch_tpu/_internal/public_api.md) | 50 | `ModuleSpec`, `_module_name`, `_target_module` |  |
| [`src/torch_tpu/_internal/public_api_test.py`](src/torch_tpu/_internal/public_api_test.md) | 27 | `_sample_table`, `_FakeMeta`, `impl_mod` |  |
| [`src/torch_tpu/_internal/stream/streams.py`](src/torch_tpu/_internal/stream/streams.md) | 29 | `experimental`, `CorePinningMode`, `TpuStream` |  |
| [`src/torch_tpu/_internal/sync/__init__.py`](src/torch_tpu/_internal/sync/__init__.md) | 7 | `computation_graphviz`, `computation_mlir`, `dump_computation_graphviz` |  |
| [`src/torch_tpu/_internal/sync/sync.py`](src/torch_tpu/_internal/sync/sync.md) | 8 | `_dump_computation`, `computation_graphviz`, `computation_mlir` |  |
| [`src/torch_tpu/_internal/tracing/__init__.py`](src/torch_tpu/_internal/tracing/__init__.md) | 14 | `_daemon`, `_FLUSH_INTERVAL_SECONDS`, `_const_thunk` |  |
| [`src/torch_tpu/_internal/utils/annotations.py`](src/torch_tpu/_internal/utils/annotations.md) | 35 | `Stage`, `_T`, `_annotate_target` | [hardware-introspection](../concepts/hardware-introspection.md) |
| [`src/torch_tpu/_internal/utils/annotations_test.py`](src/torch_tpu/_internal/utils/annotations_test.md) | 92 | `sample_func`, `experimental`, `deprecated` |  |
| [`src/torch_tpu/_internal/utils/hardware.py`](src/torch_tpu/_internal/utils/hardware.md) | 30 | `TpuVersion`, `get_tpu_version`, `_DEVICES_PER_CHIP` | [hardware-introspection](../concepts/hardware-introspection.md) |
| [`src/torch_tpu/_internal/utils/hardware_test.py`](src/torch_tpu/_internal/utils/hardware_test.md) | 12 | `_run_mock_test`, `get_path_mock`, `test_v5e_8_chips` |  |
| [`src/torch_tpu/_internal/utils/log_utils.py`](src/torch_tpu/_internal/utils/log_utils.md) | 2 | `__all__`, `log_to_stderr` |  |
| [`src/torch_tpu/_internal/utils/test_fixtures.py`](src/torch_tpu/_internal/utils/test_fixtures.md) | 60 | `IntWeightInitMixin`, `_init_linear`, `_T` |  |
| [`src/torch_tpu/_internal/utils/test_fixtures_test.py`](src/torch_tpu/_internal/utils/test_fixtures_test.md) | 12 | `_assert_linear_has_int_weights`, `test_int_weight_init_mixin_on_container_module`, `test_int_weight_init_mixin_on_module_list_module` |  |
| [`src/torch_tpu/_internal/utils/test_utils.py`](src/torch_tpu/_internal/utils/test_utils.md) | 27 | `CheckValueMode`, `LOOSE`, `STRICT` |  |
| [`src/torch_tpu/_internal/utils/tracer_utils.py`](src/torch_tpu/_internal/utils/tracer_utils.md) | 12 | `_pformat_value`, `link_events`, `_helper_render_delta` | [hardware-introspection](../concepts/hardware-introspection.md) |
| [`src/torch_tpu/_internal/utils/tracer_utils_test.py`](src/torch_tpu/_internal/utils/tracer_utils_test.md) | 13 | `AllTest`, `test_pformat_activation_tracer_module_list`, `test_pformat_activation_tracer_nested_children` |  |
| [`src/torch_tpu/_internal/utils/tracer_utils_tpu_test.py`](src/torch_tpu/_internal/utils/tracer_utils_tpu_test.md) | 4 | `device`, `test_replay_on_linear_no_change`, `TpuTest` |  |
| [`src/torch_tpu/_internal/utils/tt_warnings.py`](src/torch_tpu/_internal/utils/tt_warnings.md) | 1 | `warn` |  |
| [`src/torch_tpu/_internal/utils/tt_warnings_test.py`](src/torch_tpu/_internal/utils/tt_warnings_test.md) | 9 | `fn`, `_warn_from_library`, `test_compile_fullgraph_does_not_warn` |  |
| [`src/torch_tpu/_internal/utils/utils.py`](src/torch_tpu/_internal/utils/utils.md) | 42 | `Event`, `_idx`, `ops_log` | [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md), [hardware-introspection](../concepts/hardware-introspection.md) |
| [`src/torch_tpu/_internal/utils/utils_test.py`](src/torch_tpu/_internal/utils/utils_test.md) | 79 | `assert_logs_equal`, `device`, `bwd` |  |
| [`src/torch_tpu/_internal/warnings.py`](src/torch_tpu/_internal/warnings.md) | 13 | `WarningCategory`, `get_prefix`, `format_message` |  |
| [`src/torch_tpu/_loader.py`](src/torch_tpu/_loader.md) | 24 | `_default_backend_selector`, `_AUTOLOAD_ENV_VAR`, `_InductorWrapper` |  |
| [`src/torch_tpu/_tcmalloc_check.py`](src/torch_tpu/_tcmalloc_check.md) | 5 | `TCMALLOC_WARNING_PREFIX`, `_TCMALLOC_OR_SANITIZER_RE`, `_has_sanitizer_init` |  |
| [`src/torch_tpu/_versioned_so_loader.py`](src/torch_tpu/_versioned_so_loader.md) | 21 | `_real_loader`, `_VERSION_SUFFIX`, `torch_version_suffix` |  |

