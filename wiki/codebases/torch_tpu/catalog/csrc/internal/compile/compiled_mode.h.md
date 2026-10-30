---
title: 'Module: csrc/internal/compile/compiled_mode.h'
type: catalog
provenance: extracted
module: csrc/internal/compile/compiled_mode.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AsyncCompileResult: AsyncCompileResult#
  OutputShape: OutputShape#
  TraverseAndCompileOptions.module_name: TraverseAndCompileOptions#module_name.
  CompileResult: CompileResult#
  OutputShape.is_dynamic: OutputShape#is_dynamic.
  AsyncCompileResult.module: AsyncCompileResult#module(612ac124052c0d04).
  TraverseAndCompileOptions: TraverseAndCompileOptions#
  AsyncCompileResult.executable_future_: AsyncCompileResult#executable_future_.
  AsyncCompileResult.argument_indices_: AsyncCompileResult#argument_indices_.
  TraverseAndCompileOptions.argument_layouts: TraverseAndCompileOptions#argument_layouts.
  AsyncCompileResult.once_: AsyncCompileResult#once_.
  AsyncCompileResult.AsyncCompileResult: AsyncCompileResult#AsyncCompileResult(c9680f28b3e5a402).
  TraverseAndCompileOptions.compilation_mode: TraverseAndCompileOptions#compilation_mode.
  AsyncCompileResult.operator: AsyncCompileResult#`operator=`(cc350a7a8a18cb6b).
  OutputShape.dimensions: OutputShape#dimensions.
  TraverseAndCompileOptions.use_stablehlo_bounds: TraverseAndCompileOptions#use_stablehlo_bounds.
  CompileResult.module: CompileResult#module.
  AsyncCompileResult.module_: AsyncCompileResult#module_.
  AsyncCompileResult.resolved_executable_: AsyncCompileResult#resolved_executable_.
  TraverseAndCompileOptions.donated_inputs: TraverseAndCompileOptions#donated_inputs.
  CompileResult.executable: CompileResult#executable.
  TraverseAndCompileOptions.build_mlir_module: TraverseAndCompileOptions#build_mlir_module.
---
# Module: [`csrc/internal/compile/compiled_mode.h`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h)

## Classes
### <a id="AsyncCompileResult"></a>`AsyncCompileResult`
- def: [`csrc/internal/compile/compiled_mode.h:101`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L101) — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- doc: Result of `TraverseAndCompile`.
- signature: `class AsyncCompileResult`
- members:
  - <a id="AsyncCompileResult.AsyncCompileResult"></a>`AsyncCompileResult(AsyncCompileResult&&)` — [`L128`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L128)
  - `AsyncCompileResult(const AsyncCompileResult&)` — [`L126`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L126)
  - `AsyncCompileResult(AsyncCompileResult&&)` — [`L128`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L128)
  - <a id="AsyncCompileResult.module"></a>`module()` — [`L131`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L131)
  - <a id="AsyncCompileResult.operator"></a>`operator=(AsyncCompileResult&&)` — [`L129`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L129)
  - `operator=(const AsyncCompileResult&)` — [`L127`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L127)
  - <a id="AsyncCompileResult.argument_indices_"></a>`argument_indices_` — [`L150`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L150)
  - <a id="AsyncCompileResult.executable_future_"></a>`executable_future_` — [`L149`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L149)
  - <a id="AsyncCompileResult.module_"></a>`module_` — [`L148`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L148)
  - <a id="AsyncCompileResult.once_"></a>`once_` — [`L147`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L147)
  - <a id="AsyncCompileResult.resolved_executable_"></a>`resolved_executable_` — [`L152`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L152)
- uses (calls/refs, reference-scoped): [`Indices`](../../common/dimension_types.h.md#Indices), [`ContextedModule`](../../common/compilation.h.md#ContextedModule), [`SharedLoadedExecutableWithMetadata`](../../common/compilation.h.md#SharedLoadedExecutableWithMetadata), [`Get`](compiled_mode.cc.md#AsyncCompileResult.Get), [`SharedLoadedExecutableWithMetadataFuture`](../../common/compilation.h.md#SharedLoadedExecutableWithMetadataFuture), [`AsyncCompileResult`](compiled_mode.cc.md#AsyncCompileResult.AsyncCompileResult), [`IsReady`](compiled_mode.cc.md#AsyncCompileResult.IsReady), [`AsyncCompileResult`](compiled_mode.cc.md#AsyncCompileResult.AsyncCompileResult)
- used by: [`TorchTpuPyBindInitModule_tpu_torch_compile`](tpu_torch_compile.cc.md#TorchTpuPyBindInitModule_tpu_torch_compile), [`TraverseAndCompile`](compiled_mode.cc.md#TraverseAndCompile), [`ExtractMlirFromGraph`](compiled_mode.cc.md#ExtractMlirFromGraph), [`PyAsyncTraverseAndCompile`](tpu_torch_compile.cc.md#PyAsyncTraverseAndCompile), [`PyTraverseAndCompile`](tpu_torch_compile.cc.md#PyTraverseAndCompile), [`module_name`](compiled_mode.h.md#TraverseAndCompileOptions.module_name), [`Get`](compiled_mode.cc.md#AsyncCompileResult.Get), [`ConvertTraverseAndCompileOptions`](tpu_torch_compile.cc.md#ConvertTraverseAndCompileOptions), [`AsyncCompileResult`](compiled_mode.cc.md#AsyncCompileResult.AsyncCompileResult), [`IsReady`](compiled_mode.cc.md#AsyncCompileResult.IsReady)

### <a id="CompileResult"></a>`CompileResult`
- def: [`csrc/internal/compile/compiled_mode.h:91`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L91)
- doc: Result of `TraverseAndCompile`, containing the compiled executable and
- signature: `struct CompileResult`
- members:
  - <a id="CompileResult.executable"></a>`executable` — [`L93`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L93)
  - <a id="CompileResult.module"></a>`module` — [`L92`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L92)
- uses (calls/refs, reference-scoped): [`ContextedModule`](../../common/compilation.h.md#ContextedModule), [`SharedLoadedExecutableWithMetadata`](../../common/compilation.h.md#SharedLoadedExecutableWithMetadata)
- used by: [`TorchTpuPyBindInitModule_tpu_torch_compile`](tpu_torch_compile.cc.md#TorchTpuPyBindInitModule_tpu_torch_compile), [`UnpackSliceInputs`](tpu_torch_compile.cc.md#UnpackSliceInputs), [`PyPrecompileSliceModule`](tpu_torch_compile.cc.md#PyPrecompileSliceModule), [`PyGetOrCompileSliceModule`](tpu_torch_compile.cc.md#PyGetOrCompileSliceModule), [`PyPrecompilePadModule`](tpu_torch_compile.cc.md#PyPrecompilePadModule), [`PyGetDynamicPadModule`](tpu_torch_compile.cc.md#PyGetDynamicPadModule), [`PyGetOrCompilePadModule`](tpu_torch_compile.cc.md#PyGetOrCompilePadModule), [`CompileModuleWithCache`](tpu_torch_compile.cc.md#CompileModuleWithCache), [`PyAsyncTraverseAndCompile`](tpu_torch_compile.cc.md#PyAsyncTraverseAndCompile), [`PyTraverseAndCompile`](tpu_torch_compile.cc.md#PyTraverseAndCompile)

### <a id="OutputShape"></a>`OutputShape`
- def: [`csrc/internal/compile/compiled_mode.h:247`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L247)
- signature: `struct OutputShape`
- members:
  - <a id="OutputShape.dimensions"></a>`dimensions` — [`L248`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L248) — INT_VEC_OK
  - <a id="OutputShape.is_dynamic"></a>`is_dynamic` — [`L249`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L249)
- uses (calls/refs, reference-scoped): [`SharedLoadedExecutableWithMetadata`](../../common/compilation.h.md#SharedLoadedExecutableWithMetadata), [`MakeConstantTensor`](compiled_mode.cc.md#MakeConstantTensor), [`AssignConstantTensor`](compiled_mode.cc.md#AssignConstantTensor), [`ExecuteCompiledModel`](compiled_mode.cc.md#ExecuteCompiledModel), [`ExecuteCompiledModel`](compiled_mode.cc.md#ExecuteCompiledModel), [`ExecuteCompiledModel`](compiled_mode.cc.md#ExecuteCompiledModel), [`ExecuteCompiledModel`](compiled_mode.cc.md#ExecuteCompiledModel)
- used by: [`TorchTpuPyBindInitModule_tpu_torch_compile`](tpu_torch_compile.cc.md#TorchTpuPyBindInitModule_tpu_torch_compile), [`GetOutputShapes`](compiled_mode.cc.md#GetOutputShapes), [`ExecuteCompiledModelImpl`](compiled_mode.cc.md#ExecuteCompiledModelImpl), [`RunWithGenerators`](tpu_torch_compile.cc.md#CompiledExecutableRunner.RunWithGenerators), [`PyExecuteCompiledModel`](tpu_torch_compile.cc.md#PyExecuteCompiledModel), [`CompiledExecutableRunner`](tpu_torch_compile.cc.md#CompiledExecutableRunner.CompiledExecutableRunner), [`cached_output_shapes_`](tpu_torch_compile.cc.md#CompiledExecutableRunner.cached_output_shapes_), [`ExecuteCompiledModel`](compiled_mode.cc.md#ExecuteCompiledModel), [`UnpackInputTensorPointers`](tpu_torch_compile.cc.md#UnpackInputTensorPointers), [`ExecuteCompiledModel`](compiled_mode.cc.md#ExecuteCompiledModel), [`ParseOutputShapes`](tpu_torch_compile.cc.md#ParseOutputShapes), [`executable_`](tpu_torch_compile.cc.md#CompiledExecutableRunner.executable_)

### <a id="TraverseAndCompileOptions"></a>`TraverseAndCompileOptions`
- def: [`csrc/internal/compile/compiled_mode.h:155`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L155)
- signature: `struct TraverseAndCompileOptions`
- members:
  - <a id="TraverseAndCompileOptions.argument_layouts"></a>`argument_layouts` — [`L164`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L164) — Forced layouts for arguments.
  - <a id="TraverseAndCompileOptions.build_mlir_module"></a>`build_mlir_module` — [`L159`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L159) — If true, build the MLIR module and return it in the `CompileResult`.
  - <a id="TraverseAndCompileOptions.compilation_mode"></a>`compilation_mode` — [`L157`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L157) — The compilation mode to use.
  - <a id="TraverseAndCompileOptions.donated_inputs"></a>`donated_inputs` — [`L166`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L166) — Indices of arguments to donate.
  - <a id="TraverseAndCompileOptions.module_name"></a>`module_name` — [`L168`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L168) — Optional custom module name.
  - <a id="TraverseAndCompileOptions.use_stablehlo_bounds"></a>`use_stablehlo_bounds` — [`L162`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.h#L162) — If true, use StableHLO style bounds in the generated MLIR for dynamic
- uses (calls/refs, reference-scoped): [`Indices`](../../common/dimension_types.h.md#Indices), [`TraverseAndCompile`](compiled_mode.cc.md#TraverseAndCompile), [`CompilationMode`](../../common/compilation_spec.h.md#CompilationMode), [`SharedLoadedExecutableWithMetadata`](../../common/compilation.h.md#SharedLoadedExecutableWithMetadata), [`CustomLayout`](../../common/dimension_types.h.md#CustomLayout), [`UniqueCompileOptions`](../../common/compilation_spec.h.md#UniqueCompileOptions), [`CompileMlirExecutable`](compiled_mode.cc.md#CompileMlirExecutable), [`AsyncCompileResult`](compiled_mode.h.md#AsyncCompileResult), [`CompileMlirExecutable`](compiled_mode.cc.md#CompileMlirExecutable), [`kFastRuntime`](../../common/compilation_spec.h.md#CompilationMode.kFastRuntime), [`CompileMlirExecutable`](compiled_mode.cc.md#CompileMlirExecutable), [`CompileMlirExecutable`](compiled_mode.cc.md#CompileMlirExecutable), [`TraverseAndCompile`](compiled_mode.cc.md#TraverseAndCompile)
- used by: [`TraverseAndCompile`](compiled_mode.cc.md#TraverseAndCompile), [`ConvertArgumentLayouts`](tpu_torch_compile.cc.md#ConvertArgumentLayouts), [`ConvertTraverseAndCompileOptions`](tpu_torch_compile.cc.md#ConvertTraverseAndCompileOptions)

