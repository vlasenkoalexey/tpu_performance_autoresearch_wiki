---
slug: torch_tpu
repo: raw/code/torch_tpu
acquire: submodule
# Release v0.2.0 (tag v0.2.0 -> 005903d0e, 2026-10-17). Fresh ingest: the 0.2.0 tree moved the
# Python package to src/torch_tpu/ and the C++ core to csrc/ (the old torch_tpu/ dir is gone).
ref: 005903d0ef0dde919b832530451e568912c6f464
wiki_subdir: codebases
source_type: code
languages: [cpp, python]
# The C++ core is indexed via a bazel-derived compile DB: `prepare` runs `bazel build` + `aquery`
# on these targets, converts to compile_commands.json and runs scip-clang (slow on a cold cache).
bazel_targets: "//csrc/..."
index_shards: ["src/torch_tpu/*"]
catalog: full   # per-module catalog pages, like the other silos in this wiki (citations link to them)
agenda: subsystems
# The flat csrc/common, csrc/ops and csrc/eager dirs split into reference communities named after
# utility hubs (error macros, op names) that mix unrelated kernels; those planner units are dropped
# and replaced by the topic-named units under ## Concepts. Every module still gets a catalog page.
agenda_exclude:
  - csrc/common
  - csrc/ops
  - csrc/eager
  - csrc/internal
  - csrc/ops/pooling
  - csrc/ops/linalg
  - src/torch_tpu/_internal
  - src/torch_tpu
  - csrc/api
coverage_collapse: ["tests/**", "**/*_test.*", "third_party/**"]
docs: ["README.md", "docs/**/*.md"]
synthesis_focus: "TPU performance - how an ATen op is dispatched and lowered to StableHLO, eager deferred execution and materialization, the compilation pipeline and its cache tiers, dynamic shapes, the torch.compile backend, distributed collectives and sharding, precision/dtype handling, attention and Pallas custom kernels, and the env vars and APIs that control them"
---

## Concepts
<!-- Discovery-driven: the subsystem planner proposes the units; entries here pin, rename and add. -->
- **eager-op-dispatch** - seeds: (subsystem: csrc/eager::tensor_to_buffer)
- **deferred-execution-and-materialization** - seeds: (subsystem: csrc/eager::device_buffer)
- **compilation-pipeline** - seeds: `compilation#Compile`, `CompiledKernel`, `ContextedModule`, `DynamicKernelAdapter`, `LoadedExecutableWithMetadata`, `MakeMlirContext`, `PushCompilerOptionOverrides`, `PopCompilerOptionOverrides`, `UnboundedDynamicExecutionMetadata`, `WithDynamicExecutionMetadata`, `CompilationSpec`, `CompilationContext`, `CompilationMode`, `CompileOptionsKey`, `MakeCompileOptionsKey`
- **compilation-cache** - seeds: `compilation_cache#CompilationCache`, `GetOrCompile`, `GetOrCompileImpl`, `EnqueueCompilation`, `GetOrCreateCacheEntry`, `GetFromTier2OrCompile`, `GetFromTier3OrCompile`, `CacheEntry`, `CacheEntryStats`, `BoundedDynamicCacheEntry`, `AddStaticCacheEntry`, `AddBoundedDynamicCacheEntry`, `AddUnboundedDynamicCacheEntry`, `CreateDynamicKernelAdapter`, `CreatePaddingKernel`, `CreateSlicingKernel`, `PerfStats`, `CompilationCacheInitializationOptions`, `EvictAll`, `EnsureInitialized`, `IsExecutableReady`, `HbmUsageSummary`, `GetDumpOnCacheMissMode`, `GetTorchTpuBinaryFingerprint`
- **compilation-cache-key** - seeds: `OpParamCacheKeys`, `MakeOpParamCacheKeys`, `EnforceSetParamType`, `PromotedScalar`, `MaybePromotedScalar`, `CompilationCacheKey`, `GraphKey`, `ShapelessKey`, `DimensionsKey`, `GraphSignature`, `OpSignatureBuilder`, `EncodeParamCacheKey`, `IncludeInCacheKey`, `IgnoredInCacheKey`, `ShapeDynamismMetadata`, `IsStaticShapeCompatible`, `CorePinningMode`, `FingerprintCat`, `PadModuleCacheKey`, `GetSliceModuleCacheKey`
- **dtype-and-precision** - seeds: `ToElementType`, `ConvertTo`, `RealComponentOf`, `IsValidElemType`, `SetAllowExcessPrecision`, `GetAndAddPrecisionTo`, `PyGetGlobalPrecision`, `PySetGlobalPrecision`, `PyPushPrecision`, `PyPopPrecision`
- **context-states-and-execution-modes** - seeds: `EagerMode`, `TracebackMode`, `ProfilerStatus`, `ContextManagerNode`, `GetContextState`, `PushContextState`, `PopContextState`, `PushContextStateUntyped`, `PopContextStateUntyped`, `CrashIfContextStateAccessIsDisallowed`, `DisallowThisThreadToAccessContextState`, `GetEagerMode`, `SetEagerMode`, `IsDeferNeverMode`, `EnableInplaceBufferDonation`, `IsInplaceBufferDonationEnabled`, `GetCompilationMode`
- **error-handling** - seeds: `StatusBuilder`, `StatusBuilderWithMessage`, `MaybeAddCppSourceLoc`, `SetRootOpNamePayload`, `ReturnIfErrorAdaptor`, `GetStatus`, `AdaptXlaError`, `CheckDeviceIsTpu`, `SetStickyError`, `GetStickyError`, `ClearStickyError`, `SyncAndCheckStickyError`, `TtError`, `TranslateToC10ErrorAndThrow`
- **op-names-and-python-context** - seeds: `OpName`, `IsDistributedOp`, `OpNameStack`, `ScopedOpName`, `PythonContext`, `PythonTraceback`, `PythonStackFrame`, `ScopedPythonContextCapturer`, `ScopedPythonContextProvider`, `PythonApiName`
- **aten-kernel-authoring** - seeds: `UnaryOp`, `UnaryOpOut`, `UnaryOpInPlace`, `UnaryOpOptions`, `BinaryOp`, `BinaryOpOut`, `BinaryOpOptions`, `DispatchBinaryOp`, `DispatchBinaryOpOut`, `DispatchTernaryOp`, `TernaryOpOut`, `CheckTensorsUsed`, `CollectPromotedScalarPointers`, `InvalidOpParamCacheKeys`, `CheckTtKernelArgList`, `LogKernelArgs`, `LogKernelName`, `ParseArgTypesOrEmpty`
- **stablehlo-op-builder** - seeds: `GetTensorTypeOrDie`, `MakeScalarConstant`, `MakeConstantLike`, `MakeConstant`, `MlirOpResults`, `BroadcastIfNeeded`, `GetElementTypeOrSelf`, `GetMlirType`
- **device-streams-generators-and-rng** - seeds: `GetDefaultDeviceGenerator`, `GetCurrentDeviceStreamId`, `DeviceGeneratorImplBase`, `DeviceStateTensor`, `DispatchRngOp`, `DispatchRngOpGeneral`, `DispatchRngOpAndReturnBuffer`, `RngUsage`
- **view-decomposition** - seeds: (subsystem: csrc/ops/view_decomposition)
- **scaled-dot-product-attention** - seeds: (subsystem: csrc/ops/scaled_dot_product_attention)
- **reductions** - seeds: (subsystem: csrc/ops/reductions)
- **ragged-collectives-and-sparse-ops** - seeds: (subsystem: csrc/ops/experimental)
- **host-device-copy** - seeds: (subsystem: csrc/ops/copy_from)
- **batch-host-device-transfer** - seeds: (subsystem: csrc/experimental)
- **dynamic-shape-ops** - seeds: (subsystem: csrc/ops/dynamic)
- **fused-optimizer-kernels** - seeds: `AtenFusedAdam`, `AtenFusedAdamw`, `AtenFusedSgd`, `AtenFusedAdagrad`, `AtenFusedAdamTensorLr`, `AtenFusedAdamwTensorLr`
- **process-group-and-collectives** - seeds: (subsystem: csrc/distributed)
- **pjrt-client** - seeds: (subsystem: csrc/pjrt)
- **kiln-kernel-dsl** - seeds: (subsystem: csrc/internal/mosaic/kiln)
- **mosaic-matmul** - seeds: `CreateMatmul`, `MatmulOptions`, `DimensionSemantics`, `GetVmemMemRefType`
- **mlir-optimization-passes** - seeds: (subsystem: csrc/mlir)
- **profiler** - seeds: (subsystem: csrc/internal/profiler)
- **compiled-mode** - seeds: (subsystem: csrc/internal/compile)
- **tensor-synchronization** - seeds: (subsystem: csrc/internal/sync)
- **torch-compile-backend** - seeds: (subsystem: src/torch_tpu/_internal/compile)
- **dynamic-shapes-compiler** - seeds: (subsystem: src/torch_tpu/_internal/compile/dynamic)
- **fx-graph-passes** - seeds: (subsystem: src/torch_tpu/_internal/compile/fx_passes)
- **distributed-launchers-and-spmd** - seeds: (subsystem: src/torch_tpu/_internal/distributed)
- **pallas-custom-kernels** - seeds: (subsystem: src/torch_tpu/_internal/pallas)
- **python-optimizers** - seeds: (subsystem: src/torch_tpu/_internal/optimizers)
- **hardware-introspection** - seeds: (subsystem: src/torch_tpu/_internal/utils)
- **python-ops** - seeds: (subsystem: src/torch_tpu/_internal/ops)
