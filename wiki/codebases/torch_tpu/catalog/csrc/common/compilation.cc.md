---
title: 'Module: csrc/common/compilation.cc'
type: catalog
provenance: extracted
module: csrc/common/compilation.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  GetCompilationSpec: GetCompilationSpec(51d86b91a6e432c0).
  ContextedModule.Make: ContextedModule#Make(e13ed184d248ee93).
  MakeCompileOptionsKey: MakeCompileOptionsKey(d015e9fb60e73a43).
  ApplyCompilerOptionOverrides: ApplyCompilerOptionOverrides(59da82648068a174).
  LoadedExecutableWithMetadata.MakeShared: LoadedExecutableWithMetadata#MakeShared(b9852ec34db12c65).
  MakeCompilationSpecs: MakeCompilationSpecs(e672d66eec3ddded).
  PushCompilerOptionOverrides: PushCompilerOptionOverrides(19661756065552c8).
  MlirComputationBuilderToExecutableBuilder: MlirComputationBuilderToExecutableBuilder(4673204227ee9f03).
  ParseEffortLevel: ParseEffortLevel(fa100936805b02c).
  GetCompilationContext: GetCompilationContext(504a16a9b2fdea94).
  PopCompilerOptionOverrides: PopCompilerOptionOverrides(49f6e7a06ebc5aa8).
  Compile: Compile(10bf2c767c34c7be).
  SetDefaultDeviceAssignment: SetDefaultDeviceAssignment(b3e7f6a2a9ab5a3d).
  MakeMlirContext: MakeMlirContext(83ad5685f0f25dcd).
  MakeCompilationContext: MakeCompilationContext(e1d3bc193bb4ee86).
  SetTpuOptions: SetTpuOptions(27a0209f68c8e798).
  Fingerprint: Fingerprint(48c65c1cd4818f59).
  Fingerprint64Impl: internal/Fingerprint64Impl#
  ContextedModule.ContextedModule: ContextedModule#ContextedModule(ff4c5bb7875d0638).
  MakeCompilerOptionOverrides: MakeCompilerOptionOverrides(7f971794e8c3a9d9).
  GetCompilerOptionOverridesFromEnvVar: GetCompilerOptionOverridesFromEnvVar(221979ca7d784ae2).
  GetDefaultCompilationContext: GetDefaultCompilationContext(3f97567903bdd2dc).
  UpdateFromXlaFlags: UpdateFromXlaFlags(d96647b1ec636972).
  UpdateMap: UpdateMap(c294a3505e7ed828).
  kMemoryFittingLevelOption: '`$anonymous_namespace_csrc/common/compilation.cc`/kMemoryFittingLevelOption.'
  Fingerprint64Impl.Compute: internal/Fingerprint64Impl#Compute(c379be352a6101c0).
  kOptimizationLevelOption: '`$anonymous_namespace_csrc/common/compilation.cc`/kOptimizationLevelOption.'
---
# Module: [`csrc/common/compilation.cc`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc)

## Classes
### <a id="Fingerprint64Impl"></a>`Fingerprint64Impl`
- def: [`csrc/common/compilation.cc:67`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L67)
- doc: Fingerprint specialization for `xla::ExecutionOptions::EffortLevel`.
- signature: `template <> struct Fingerprint64Impl<xla::ExecutionOptions::EffortLevel, /*kIsSmallIntegral=*/false>`
- members:
  - <a id="Fingerprint64Impl.Compute"></a>`Compute(const xla::ExecutionOptions::EffortLevel effort_level)` — [`L69`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L69)
- uses (calls/refs, reference-scoped): [`OpName`](../ops/op_names.h.md#OpName), [`Fingerprint`](fingerprint_utils.h.md#Fingerprint), [`FingerprintType`](fingerprint_utils.h.md#FingerprintType), [`DeviceGroupList`](../distributed/types.h.md#DeviceGroupList)
- used by: [`Fingerprint`](fingerprint_utils.h.md#Fingerprint)

## Functions
- <a id="ApplyCompilerOptionOverrides"></a>`ApplyCompilerOptionOverrides(CompilerOptionOverrides overrides, xla::CompileOptions& compile_options)` — [`L354`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L354) — Updates `compile_options.env_option_overrides` with the given overrides.
- `ApplyCompilerOptionOverrides(CompilerOptionOverrides overrides, xla::CompileOptions& compile_options)` — [`L354`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L354) — Updates `compile_options.env_option_overrides` with the given overrides.
- `Compile(xla::PjRtClient& client, LoadedExecutableBuilder executable_builder, UniqueCompileOptions compile_options)` — [`L141`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L141) — Synchronously compiles a program, without any cache behavior.
- <a id="Compile"></a>`Compile(xla::PjRtClient& client, LoadedExecutableBuilder executable_builder, UniqueCompileOptions compile_options)` — [`L141`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L141) — Synchronously compiles a program, without any cache behavior. — documented in [compilation-pipeline](../../../concepts/compilation-pipeline.md)
- `Fingerprint(const xla::ExecutableBuildOptions& options)` — [`L276`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L276) — Returns fingerprint of `xla::ExecutableBuildOptions` fields that are used
- <a id="Fingerprint"></a>`Fingerprint(const xla::CompileOptions& options)` — [`L422`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L422) — Returns fingerprint of `xla::CompileOptions` to be used as part of
- <a id="GetCompilationContext"></a>`GetCompilationContext()` — [`L561`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L561) — Returns a shared pointer to the active thread-local immutable
- <a id="GetCompilationSpec"></a>`GetCompilationSpec(const CompilationMode mode)` — [`L566`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L566) — Returns resolved compilation settings for the given compilation mode.
- `GetCompilerOptionOverridesFromEnvVar()` — [`L197`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L197) — Returns the compile option overrides from the environment variable
- <a id="GetCompilerOptionOverridesFromEnvVar"></a>`GetCompilerOptionOverridesFromEnvVar()` — [`L197`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L197) — Returns the compile option overrides from the environment variable
- <a id="GetDefaultCompilationContext"></a>`GetDefaultCompilationContext()` — [`L529`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L529) — Returns the default `CompilationContext` when no overrides are applied. This
- `MakeCompilationContext(CompilerOptionOverrides overrides)` — [`L518`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L518) — LINT.ThenChange(:compile_options_key)
- <a id="MakeCompilationContext"></a>`MakeCompilationContext(CompilerOptionOverrides overrides)` — [`L518`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L518) — LINT.ThenChange(:compile_options_key)
- `MakeCompilationSpecs(const CompilerOptionOverrides& overrides)` — [`L487`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L487) — On success, returns compilation specs for all compilation modes. Each
- <a id="MakeCompilationSpecs"></a>`MakeCompilationSpecs(const CompilerOptionOverrides& overrides)` — [`L487`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L487) — On success, returns compilation specs for all compilation modes. Each
- <a id="MakeCompileOptionsKey"></a>`MakeCompileOptionsKey(const xla::CompileOptions& options)` — [`L441`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L441) — Returns the compile options key for the given compile options. — documented in [compilation-pipeline](../../../concepts/compilation-pipeline.md)
- <a id="MakeCompilerOptionOverrides"></a>`MakeCompilerOptionOverrides(const bool is_tpu, const CompilationMode mode, const CompilerOptionOverrides& context_overrides)` — [`L325`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L325) — Returns compiler option overrides (a string-string map) for the given
- `MakeCompilerOptionOverrides(const bool is_tpu, const CompilationMode mode, const CompilerOptionOverrides& context_overrides)` — [`L325`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L325) — Returns compiler option overrides (a string-string map) for the given
- <a id="MakeMlirContext"></a>`MakeMlirContext()` — [`L88`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L88) — Creates an MLIR context and registers all required TPU dialects. — documented in [compilation-pipeline](../../../concepts/compilation-pipeline.md)
- `MakeMlirContext()` — [`L88`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L88) — Creates an MLIR context and registers all required TPU dialects.
- <a id="MlirComputationBuilderToExecutableBuilder"></a>`MlirComputationBuilderToExecutableBuilder(const MlirComputationBuilder& computation_builder)` — [`L151`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L151) — Lifts a MlirComputationBuilder into an ExecutableBuilder.
- `MlirComputationBuilderToExecutableBuilder(const MlirComputationBuilder& computation_builder)` — [`L151`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L151) — Lifts a MlirComputationBuilder into an ExecutableBuilder.
- <a id="ParseEffortLevel"></a>`ParseEffortLevel(std::string_view level)` — [`L174`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L174)
- <a id="PopCompilerOptionOverrides"></a>`PopCompilerOptionOverrides()` — [`L557`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L557) — Pops the compile option overrides for the current thread from the — documented in [compilation-pipeline](../../../concepts/compilation-pipeline.md)
- <a id="PushCompilerOptionOverrides"></a>`PushCompilerOptionOverrides(CompilerOptionOverrides overrides)` — [`L541`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L541) — Pushes the compile option overrides for the current thread on to the — documented in [compilation-pipeline](../../../concepts/compilation-pipeline.md)
- `PushCompilerOptionOverrides(CompilerOptionOverrides overrides)` — [`L541`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L541) — Pushes the compile option overrides for the current thread on to the
- <a id="SetDefaultDeviceAssignment"></a>`SetDefaultDeviceAssignment(xla::ExecutableBuildOptions& options)` — [`L232`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L232)
- <a id="SetTpuOptions"></a>`SetTpuOptions(xla::CompileOptions& options)` — [`L299`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L299) — Sets `options.env_option_overrides` to TPU-specific options, sorted by key
- <a id="UpdateFromXlaFlags"></a>`UpdateFromXlaFlags(xla::CompileOptions& options)` — [`L218`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L218) — Updates the `executable_build_options.debug_options` field of the given
- <a id="UpdateMap"></a>`UpdateMap(Map& map, Map updates)` — [`L168`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L168) — Updates `map` with the contents of `updates`. If a key appears in both `map`

## Module values
- <a id="kMemoryFittingLevelOption"></a>`kMemoryFittingLevelOption` — [`L83`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L83)
- <a id="kOptimizationLevelOption"></a>`kOptimizationLevelOption` — [`L82`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L82) — Names of special XLA compiler options.

## Other members
- `MakeShared` — [`L110`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L110)
- `ContextedModule` — [`L97`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L97)
- <a id="ContextedModule.ContextedModule"></a>`ContextedModule.ContextedModule` — [`L97`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L97)
- <a id="ContextedModule.Make"></a>`ContextedModule.Make` — [`L101`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L101)
- <a id="LoadedExecutableWithMetadata.MakeShared"></a>`LoadedExecutableWithMetadata.MakeShared` — [`L110`](../../../../../../raw/code/torch_tpu/csrc/common/compilation.cc#L110)

