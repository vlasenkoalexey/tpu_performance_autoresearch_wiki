---
title: 'Module: csrc/internal/compile/compiled_mode.cc'
type: catalog
provenance: extracted
module: csrc/internal/compile/compiled_mode.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  TraverseAndCompile: TraverseAndCompile(82f8da09e1c914b1).
  PrepareCompiledModeArgumentsImpl: '`$anonymous_namespace_csrc/internal/compile/compiled_mode.cc`/PrepareCompiledModeArgumentsImpl(b32de324698e582d).'
  ExtractMlirFromGraph: ExtractMlirFromGraph(78f36e902a693ca6).
  GetOutputShapes: '`$anonymous_namespace_csrc/internal/compile/compiled_mode.cc`/GetOutputShapes(6a74ad31dddc379a).'
  ExecuteCompiledModelImpl: '`$anonymous_namespace_csrc/internal/compile/compiled_mode.cc`/ExecuteCompiledModelImpl(2d718f3a86e48ce6).'
  PrepareCompiledModeArgumentsNonSequentialFallback: '`$anonymous_namespace_csrc/internal/compile/compiled_mode.cc`/PrepareCompiledModeArgumentsNonSequentialFallback(ca995d5d824399ee).'
  MakePlaceholder: MakePlaceholder(9bdbba2274f5f456).
  MakeConstantTensor: MakeConstantTensor(cd958efedc17238).
  AssignConstantTensor: AssignConstantTensor(b2d6689cde60befb).
  CompileMlirExecutable: CompileMlirExecutable(6f14a52b6a9d5557).
  AsyncCompileResult.Get: AsyncCompileResult#Get(a26f2165ff7be742).
  AsyncCompileResult.AsyncCompileResult: AsyncCompileResult#AsyncCompileResult(b3fc215f521e21b).
  AsyncCompileResult.IsReady: AsyncCompileResult#IsReady(50ce9a9e25b4a850).
  ExecuteCompiledModel: ExecuteCompiledModel(ad46a11c372b8c33).
  NeedsMaterialize: '`$anonymous_namespace_csrc/internal/compile/compiled_mode.cc`/NeedsMaterialize(8182ece79fead29e).'
  DerefTensor: '`$anonymous_namespace_csrc/internal/compile/compiled_mode.cc`/DerefTensor(baf22cc3a1d700e1).'
---
# Module: [`csrc/internal/compile/compiled_mode.cc`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc)

## Functions
- <a id="AssignConstantTensor"></a>`AssignConstantTensor(const at::Tensor& cpu_src_tensor, const at::Tensor& tpu_dst_tensor)` — [`L741`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L741) — Updates tpu_dst_tensor to be a tensor with the constant value of the CPU — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- `CompileMlirExecutable(const std::string_view mlir_module_bytecode, UniqueCompileOptions compile_options)` — [`L548`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L548) — torch.compile integration: this is called by torch.compile() to compile the
- `CompileMlirExecutable(const std::string_view mlir_module_bytecode, UniqueCompileOptions compile_options)` — [`L548`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L548) — torch.compile integration: this is called by torch.compile() to compile the
- `CompileMlirExecutable(xla::MaybeOwningMlirModule module, UniqueCompileOptions compile_options)` — [`L564`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L564) — torch.compile integration: this is called by torch.compile() to compile the
- <a id="CompileMlirExecutable"></a>`CompileMlirExecutable(xla::MaybeOwningMlirModule module, UniqueCompileOptions compile_options)` — [`L564`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L564) — torch.compile integration: this is called by torch.compile() to compile the
- <a id="DerefTensor"></a>`DerefTensor(const at::Tensor& t)` — [`L83`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L83)
- `DerefTensor(const at::Tensor* t)` — [`L84`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L84)
- `ExecuteCompiledModel(const SharedLoadedExecutableWithMetadata& executable, absl::Span<const at::Tensor> argument_tensors, absl::Span<const OutputShape> output_shapes)` — [`L691`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L691) — This is bound to Python function tpu_torch_compile.execute(), and thus
- `ExecuteCompiledModel(const SharedLoadedExecutableWithMetadata& executable, absl::Span<const at::Tensor* const> argument_tensors, absl::Span<const OutputShape> output_shapes)` — [`L698`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L698)
- <a id="ExecuteCompiledModel"></a>`ExecuteCompiledModel(const SharedLoadedExecutableWithMetadata& executable, absl::Span<const at::Tensor> argument_tensors, absl::Span<const OutputShape> output_shapes)` — [`L691`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L691) — This is bound to Python function tpu_torch_compile.execute(), and thus
- `ExecuteCompiledModel(const SharedLoadedExecutableWithMetadata& executable, absl::Span<const at::Tensor* const> argument_tensors, absl::Span<const OutputShape> output_shapes)` — [`L698`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L698)
- <a id="ExecuteCompiledModelImpl"></a>`ExecuteCompiledModelImpl(const SharedLoadedExecutableWithMetadata& executable, TensorSpan argument_tensors, absl::Span<const OutputShape> output_shapes)` — [`L650`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L650) — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- `ExecuteCompiledModelImpl(const SharedLoadedExecutableWithMetadata& executable, TensorSpan argument_tensors, absl::Span<const OutputShape> output_shapes)` — [`L650`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L650)
- <a id="ExtractMlirFromGraph"></a>`ExtractMlirFromGraph(mlir::MLIRContext& mlir_context, const std::vector<at::Tensor>& arg_tensors, const std::vector<at::Tensor>& result_tensors, bool use_stablehlo_bounds)` — [`L299`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L299) — Extracts the MLIR module from the given graph without compiling or — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- `ExtractMlirFromGraph(mlir::MLIRContext& mlir_context, const std::vector<at::Tensor>& arg_tensors, const std::vector<at::Tensor>& result_tensors, bool use_stablehlo_bounds)` — [`L299`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L299) — Extracts the MLIR module from the given graph without compiling or
- <a id="GetOutputShapes"></a>`GetOutputShapes(const SharedLoadedExecutableWithMetadata& executable, absl::Span<const OutputShape> output_shapes)` — [`L598`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L598) — Returns the output shapes for executing the given executable. — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- `GetOutputShapes(const SharedLoadedExecutableWithMetadata& executable, absl::Span<const OutputShape> output_shapes)` — [`L598`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L598) — Returns the output shapes for executing the given executable.
- <a id="MakeConstantTensor"></a>`MakeConstantTensor(const at::Tensor& cpu_tensor)` — [`L705`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L705) — Creates a TPU tensor that represents the constant value of the CPU tensor. — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- `MakePlaceholder(Shape shape, bool requires_grad, bool is_pinned_host)` — [`L284`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L284)
- <a id="MakePlaceholder"></a>`MakePlaceholder(absl::Span<const int64_t> sizes, at::ScalarType dtype, bool requires_grad, bool is_pinned_host)` — [`L263`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L263) — Creates a contiguous tensor with a new, unshared c10::Storage and a — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="NeedsMaterialize"></a>`NeedsMaterialize(const DeviceBufferRef& buffer_ref)` — [`L94`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L94) — Checks whether a base DeviceBufferRef requires explicit materialization
- `PrepareCompiledModeArgumentsImpl(TensorSpan argument_tensors)` — [`L103`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L103) — To call a compiled PjRtExecutable, we need to get materialized base buffers
- `PrepareCompiledModeArgumentsImpl(TensorSpan argument_tensors)` — [`L103`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L103) — To call a compiled PjRtExecutable, we need to get materialized base buffers
- `PrepareCompiledModeArgumentsImpl(TensorSpan argument_tensors, const Indices& argument_indices)` — [`L211`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L211)
- <a id="PrepareCompiledModeArgumentsImpl"></a>`PrepareCompiledModeArgumentsImpl(TensorSpan argument_tensors, const Indices& argument_indices)` — [`L211`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L211) — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- `PrepareCompiledModeArgumentsNonSequentialFallback(TensorSpan argument_tensors, const Indices& argument_indices, bool* has_deferred_or_placeholder)` — [`L180`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L180) — Deduplicated Path: If we have argument_indices, populate only the unique
- <a id="PrepareCompiledModeArgumentsNonSequentialFallback"></a>`PrepareCompiledModeArgumentsNonSequentialFallback(TensorSpan argument_tensors, const Indices& argument_indices, bool* has_deferred_or_placeholder)` — [`L180`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L180) — Deduplicated Path: If we have argument_indices, populate only the unique — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- `TraverseAndCompile(const std::vector<at::Tensor>& result_tensors, const std::vector<at::Tensor>& argument_tensors, const TraverseAndCompileOptions& options)` — [`L357`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L357) — Traverses the graph from `result_tensors` back to `argument_tensors`,
- <a id="TraverseAndCompile"></a>`TraverseAndCompile(const std::vector<at::Tensor>& result_tensors, const std::vector<at::Tensor>& argument_tensors, const TraverseAndCompileOptions& options)` — [`L357`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L357) — Traverses the graph from `result_tensors` back to `argument_tensors`, — documented in [compiled-mode](../../../../concepts/compiled-mode.md)

## Other members
- `AsyncCompileResult` — [`L508`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L508)
- <a id="AsyncCompileResult.AsyncCompileResult"></a>`AsyncCompileResult.AsyncCompileResult` — [`L508`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L508)
- <a id="AsyncCompileResult.Get"></a>`AsyncCompileResult.Get` — [`L524`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L524)
- <a id="AsyncCompileResult.IsReady"></a>`AsyncCompileResult.IsReady` — [`L518`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/compiled_mode.cc#L518)

