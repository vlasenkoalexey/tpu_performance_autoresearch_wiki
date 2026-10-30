---
title: 'Module: csrc/internal/compile/tpu_torch_compile.cc'
type: catalog
provenance: extracted
module: csrc/internal/compile/tpu_torch_compile.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  TorchTpuPyBindInitModule_tpu_torch_compile: TorchTpuPyBindInitModule_tpu_torch_compile(d5b68cea704bb038).
  PyCompileMlir: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyCompileMlir(eb315ca7e143c0ba).'
  MakePadDynamicShapes: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/MakePadDynamicShapes(1fbb64f32266009b).'
  PyBuildMlir: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyBuildMlir(68f7b009d3f2ae23).'
  UnpackSliceInputs: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/UnpackSliceInputs(7eb7d6fbc2a628a9).'
  PyParseMlirText: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyParseMlirText(f9f6eef2dcf73236).'
  PyPrecompileSliceModule: PyPrecompileSliceModule(10d48ef242235bea).
  PyGetOrCompileSliceModule: PyGetOrCompileSliceModule(eb573a88fbd22a7b).
  PyPrecompilePadModule: PyPrecompilePadModule(ed4f9cdb729e9bb5).
  ForceStrides: ForceStrides(ed65b7034535b31e).
  PyGetDynamicPadModule: PyGetDynamicPadModule(ba32f7eeb36f5fba).
  PyGetOrCompilePadModule: PyGetOrCompilePadModule(9affeb1e396383c0).
  FxOutputReconstructor.Reconstruct: FxOutputReconstructor#Reconstruct(494e704ef6a415b9).
  CompileModuleWithCache: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/CompileModuleWithCache(d2a8ed0a63896e14).'
  FxOutputReconstructor.GetReconstructedLeafNewRef: FxOutputReconstructor#GetReconstructedLeafNewRef(77045ed6507a0f19).
  FxOutputReconstructor.InitExpectedLayouts: FxOutputReconstructor#InitExpectedLayouts(49f6e7a06ebc5aa8).
  ParseCustomLayout: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/ParseCustomLayout(ed92137d084969c2).'
  PyMakeDynamicPlaceholder: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyMakeDynamicPlaceholder(615e41c50d32a8b9).'
  PyAsyncTraverseAndCompile: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyAsyncTraverseAndCompile(966e4600273b82bc).'
  PySetDeviceStateTensor: PySetDeviceStateTensor(2d56dba9b77513b0).
  PyMakePlaceholderLike: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyMakePlaceholderLike(32560beb2377088d).'
  ConvertArgumentLayouts: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/ConvertArgumentLayouts(f7a990238d58ce04).'
  RawPyObjPtr: RawPyObjPtr#
  FxOutputReconstructor.CheckInputIndex: FxOutputReconstructor#CheckInputIndex(3b75d2d14f60ac6a).
  FxOutputReconstructor.FxOutputReconstructor: FxOutputReconstructor#FxOutputReconstructor(e33398235bdf74f1).
  PyGetDeviceLayoutIfMaterialized: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyGetDeviceLayoutIfMaterialized(7eb51aa684d0c5dc).'
  PyTraverseAndCompile: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyTraverseAndCompile(10a93561c4fe506a).'
  PyGetDefaultLayout: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyGetDefaultLayout(97c166509e8b11f4).'
  PyIsDeviceShapeDynamic: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyIsDeviceShapeDynamic(b580d0b7e29ca914).'
  PyLoadSerializedExecutable: PyLoadSerializedExecutable(49fdc6b99f1d0a04).
  CompiledExecutableRunner.RunWithGenerators: CompiledExecutableRunner#RunWithGenerators(a0109920c4ca948b).
  LoadSerializedExecutableImpl: LoadSerializedExecutableImpl(da4c9752dcd3fad4).
  PySerializeExecutable: PySerializeExecutable(14f2091a16bd3701).
  PyMakePlaceholder: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyMakePlaceholder(170411de4cad48b1).'
  PyAssignConstantTensor: PyAssignConstantTensor(c0f540083bc2c76f).
  CompiledExecutableRunner.RunFast: CompiledExecutableRunner#RunFast(336d183029cacd29).
  PyExecuteCompiledModel: PyExecuteCompiledModel(6a655ea1c8101890).
  PySerializeMlirBytecode: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PySerializeMlirBytecode(bbcdbbb68a378dfa).'
  PySerializePortableArtifact: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PySerializePortableArtifact(bbcdbbb68a378dfa).'
  PyGetOutputLayouts: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyGetOutputLayouts(28d38033c9a7c2a2).'
  PyGetParameterLayouts: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyGetParameterLayouts(28d38033c9a7c2a2).'
  PyGetDeviceStateTensor: PyGetDeviceStateTensor(2382dc8283bc9a05).
  PyMakeConstantTensor: PyMakeConstantTensor(28959186f7a4bda8).
  ToPaddedShapes: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/ToPaddedShapes(b1e30c441a37ee45).'
  FxOutputReconstructor.entries_: FxOutputReconstructor#entries_.
  CompiledExecutableRunner.CompiledExecutableRunner: CompiledExecutableRunner#CompiledExecutableRunner(272f69cf4934ce05).
  FxOutputReconstructor.ExpectedTensorLayout.shape: FxOutputReconstructor#ExpectedTensorLayout#shape.
  ConvertTraverseAndCompileOptions: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/ConvertTraverseAndCompileOptions(293a608fa9e3e68b).'
  TensorBounds: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/TensorBounds#'
  FxOutputReconstructor.Entry.index: FxOutputReconstructor#Entry#index.
  PyLayout: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyLayout#'
  PyIsConstantTensor: PyIsConstantTensor(b580d0b7e29ca914).
  CompiledExecutableRunner.FormatUserOutputs: CompiledExecutableRunner#FormatUserOutputs(1e04898ec326e031).
  CompiledExecutableRunner.cached_output_shapes_: CompiledExecutableRunner#cached_output_shapes_.
  FxOutputReconstructor.SpecKind: FxOutputReconstructor#SpecKind#
  MultiGeneratorLocker.sorted_unique_mutexes_: MultiGeneratorLocker#sorted_unique_mutexes_.
  FxOutputReconstructor.ExpectedTensorLayout.stride: FxOutputReconstructor#ExpectedTensorLayout#stride.
  MultiGeneratorLocker: MultiGeneratorLocker#
  TensorInfo: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/TensorInfo#'
  FxOutputReconstructor.EntryType: FxOutputReconstructor#EntryType#
  FxOutputReconstructor.ExpectedTensorLayout.MatchesTensor: FxOutputReconstructor#ExpectedTensorLayout#MatchesTensor(f744d874a5a05b34).
  PyPushEnableTracebacks: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyPushEnableTracebacks(5690d6a5585c885c).'
  PySerializeMlirText: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PySerializeMlirText(fac0b68141b4450f).'
  UnpackInputTensorPointers: UnpackInputTensorPointers(1c78e9667411374c).
  FxOutputReconstructor: FxOutputReconstructor#
  FxOutputReconstructor.Entry: FxOutputReconstructor#Entry#
  SliceSubgraphInputs.padded_dims: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/SliceSubgraphInputs#padded_dims.'
  SliceSubgraphInputs.element_types: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/SliceSubgraphInputs#element_types.'
  FxOutputReconstructor.ParseEntry: FxOutputReconstructor#ParseEntry(3880985c92456582).
  SliceSubgraphInputs.target_dims: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/SliceSubgraphInputs#target_dims.'
  PyMakeExportModeDeviceGenerator: PyMakeExportModeDeviceGenerator(81d6a9f9a1c96416).
  CompiledExecutableRunner.reconstruct_fn_: CompiledExecutableRunner#reconstruct_fn_.
  FxOutputReconstructor.DetermineSpecKind: FxOutputReconstructor#DetermineSpecKind(9ec29e4ee1f80140).
  ToStaticShapes: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/ToStaticShapes(b1e30c441a37ee45).'
  FxOutputReconstructor.Reduce: FxOutputReconstructor#Reduce(4360aa8756bd60ab).
  ParseTupleLayout: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/ParseTupleLayout(d292dff574981cbf).'
  PyGetOutputLayoutsFromMetadata: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyGetOutputLayoutsFromMetadata(6399d57e93d95b85).'
  PyGetParameterLayoutsFromMetadata: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyGetParameterLayoutsFromMetadata(6399d57e93d95b85).'
  FxOutputReconstructor.ExpectedTensorLayout.storage_offset: FxOutputReconstructor#ExpectedTensorLayout#storage_offset.
  PyIsPinnedHost: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/PyIsPinnedHost(b580d0b7e29ca914).'
  FxOutputReconstructor.num_output_tensors_: FxOutputReconstructor#num_output_tensors_.
  FxOutputReconstructor.ExpectedTensorLayout: FxOutputReconstructor#ExpectedTensorLayout#
  SliceSubgraphInputs.input_shapes: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/SliceSubgraphInputs#input_shapes.'
  SliceSubgraphInputs: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/SliceSubgraphInputs#'
  FxOutputReconstructor.dynamic_outputs_py_: FxOutputReconstructor#dynamic_outputs_py_.
  SliceSubgraphInputs.output_shapes: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/SliceSubgraphInputs#output_shapes.'
  FxOutputReconstructor.layouts_: FxOutputReconstructor#layouts_.
  FxOutputReconstructor.Entry.type: FxOutputReconstructor#Entry#type.
  TensorBounds.dynamic_dims: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/TensorBounds#dynamic_dims.'
  MultiGeneratorLocker.Enter: MultiGeneratorLocker#Enter(49f6e7a06ebc5aa8).
  FxOutputReconstructor.Call: FxOutputReconstructor#Call(fbf40483e11cf5c3).
  FxOutputReconstructor.GetInputItemNewRef: FxOutputReconstructor#GetInputItemNewRef(b6dab3c4e84601c1).
  PyForceStrides: PyForceStrides(8e1f2eb7ff3f7593).
  ScopedGeneratorLocks.ScopedGeneratorLocks: ScopedGeneratorLocks#ScopedGeneratorLocks(2c02917a07e1e25a).
  ParseOutputShapes: ParseOutputShapes(e357b3b8f6978aba).
  IsPhysicallyContiguousLayout: IsPhysicallyContiguousLayout(24f0fb38debcab47).
  FxOutputReconstructor.ParseDimensions: FxOutputReconstructor#ParseDimensions(53218fc47e2f226).
  UnboxSingleSequenceArg: UnboxSingleSequenceArg(eb45899ec5fd5100).
  ToPyLayouts: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/ToPyLayouts(5296db8ca623c186).'
  FxOutputReconstructor.ExpectedTensorLayout.dtype: FxOutputReconstructor#ExpectedTensorLayout#dtype.
  CompiledExecutableRunner.executable_: CompiledExecutableRunner#executable_.
  ToPyLayout: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/ToPyLayout(19639261f8bf5a14).'
  pybind11_init_tpu_torch_compile: pybind11_init_tpu_torch_compile(85901dfccbeca8c6).
  pybind11_exec_tpu_torch_compile: pybind11_exec_tpu_torch_compile(6642082b04e1bfd8).
  CompiledExecutableRunner.cached_output_shapes_with_1_gen_: CompiledExecutableRunner#cached_output_shapes_with_1_gen_.
  FxOutputReconstructor.spec_kind_: FxOutputReconstructor#spec_kind_.
  MultiGeneratorLocker.locks_: MultiGeneratorLocker#locks_.
  FxOutputReconstructor.EntryType.kDedupedTensor: FxOutputReconstructor#EntryType#kDedupedTensor.
  HasSparseCoreCustomCall: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/HasSparseCoreCustomCall(5f146d1a9d83a370).'
  PySetExportModeDefaultDeviceGenerator: PySetExportModeDefaultDeviceGenerator(6fe9e9c2ce0e26ca).
  TensorInfo.shape: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/TensorInfo#shape.'
  AsFastSequence: AsFastSequence(eb45899ec5fd5100).
  FxOutputReconstructor.ExpectedTensorLayout.is_standard_contiguous: FxOutputReconstructor#ExpectedTensorLayout#is_standard_contiguous.
  FxOutputReconstructor.output_map_py_: FxOutputReconstructor#output_map_py_.
  TensorBounds.upper_bounds: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/TensorBounds#upper_bounds.'
  FxOutputReconstructor.expected_layouts_py_: FxOutputReconstructor#expected_layouts_py_.
  ScopedGeneratorLocks.locks_: ScopedGeneratorLocks#locks_.
  FxOutputReconstructor.ExpectedTensorLayout.is_dynamic: FxOutputReconstructor#ExpectedTensorLayout#is_dynamic.
  FxOutputReconstructor.Entry.can_move: FxOutputReconstructor#Entry#can_move.
  FxOutputReconstructor.spec_py_: FxOutputReconstructor#spec_py_.
  CompiledExecutableRunner.reconstructor_ptr_: CompiledExecutableRunner#reconstructor_ptr_.
  MultiGeneratorLocker.MultiGeneratorLocker: MultiGeneratorLocker#MultiGeneratorLocker(aa194155871794ae).
  MultiGeneratorLocker.Exit: MultiGeneratorLocker#Exit(f9dae42b7c5e0206).
  FxOutputReconstructor.SpecKind.kGeneral: FxOutputReconstructor#SpecKind#kGeneral.
  HasSpmdShardingInstructions: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/HasSpmdShardingInstructions(5f146d1a9d83a370).'
  FxOutputReconstructor.IsStandardContiguousLayout: FxOutputReconstructor#IsStandardContiguousLayout(3a2a3690fd5b92ed).
  PyClearExportModeDefaultDeviceGenerators: PyClearExportModeDefaultDeviceGenerators(49f6e7a06ebc5aa8).
  IsValidLayout: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/IsValidLayout(e3e6b1e89fbd0f72).'
  FxOutputReconstructor.SpecKind.kFlatTuple: FxOutputReconstructor#SpecKind#kFlatTuple.
  CompiledExecutableRunner.updates_default_generator_state_: CompiledExecutableRunner#updates_default_generator_state_.
  FxOutputReconstructor.Entry.needs_clone: FxOutputReconstructor#Entry#needs_clone.
  FxOutputReconstructor.ExpectedTensorLayout.is_physically_contiguous: FxOutputReconstructor#ExpectedTensorLayout#is_physically_contiguous.
  FxOutputReconstructor.SpecKind.kLeaf: FxOutputReconstructor#SpecKind#kLeaf.
  FxOutputReconstructor.SpecKind.kFlatList: FxOutputReconstructor#SpecKind#kFlatList.
  TensorInfo.dtype: '`$anonymous_namespace_csrc/internal/compile/tpu_torch_compile.cc`/TensorInfo#dtype.'
  FxOutputReconstructor.EntryType.kNonTensorPassthrough: FxOutputReconstructor#EntryType#kNonTensorPassthrough.
  FxOutputReconstructor.EntryType.kNone: FxOutputReconstructor#EntryType#kNone.
  FxOutputReconstructor.Entry.needs_layout_check: FxOutputReconstructor#Entry#needs_layout_check.
  MultiGeneratorLocker.operator: MultiGeneratorLocker#`operator=`(77d3e54fe11e3672).
  ScopedGeneratorLocks: ScopedGeneratorLocks#
  CompiledExecutableRunner: CompiledExecutableRunner#
---
# Module: [`csrc/internal/compile/tpu_torch_compile.cc`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc)

## Classes
### <a id="CompiledExecutableRunner"></a>`CompiledExecutableRunner`
- def: [`csrc/internal/compile/tpu_torch_compile.cc:1888`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1888)
- doc: Pre-bound compiled executable runner that caches the unpacked C++ executable,
- signature: `class CompiledExecutableRunner`
- members:
  - <a id="CompiledExecutableRunner.CompiledExecutableRunner"></a>`CompiledExecutableRunner(SharedLoadedExecutableWithMetadata executable, std::vector<OutputShape> cached_output_shapes, py::object reconstruct_fn, bool updates_default_generator_state = false)` — [`L1890`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1890)
  - <a id="CompiledExecutableRunner.FormatUserOutputs"></a>`FormatUserOutputs(RawPyObjPtr args_ptr, std::vector<at::Tensor>& outputs, size_t user_outputs_count)` — [`L1938`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1938)
  - <a id="CompiledExecutableRunner.RunFast"></a>`RunFast(py::handle py_args)` — [`L1913`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1913)
  - <a id="CompiledExecutableRunner.RunWithGenerators"></a>`RunWithGenerators(RawPyObjPtr args_ptr, absl::InlinedVector<const at::Tensor*, 128>& argument_tensor_ptrs, absl::Span<at::Generator> generators)` — [`L1956`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1956) — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
  - <a id="CompiledExecutableRunner.cached_output_shapes_"></a>`cached_output_shapes_` — [`L2007`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L2007)
  - <a id="CompiledExecutableRunner.cached_output_shapes_with_1_gen_"></a>`cached_output_shapes_with_1_gen_` — [`L2008`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L2008)
  - <a id="CompiledExecutableRunner.executable_"></a>`executable_` — [`L2006`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L2006)
  - <a id="CompiledExecutableRunner.reconstruct_fn_"></a>`reconstruct_fn_` — [`L2009`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L2009)
  - <a id="CompiledExecutableRunner.reconstructor_ptr_"></a>`reconstructor_ptr_` — [`L2010`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L2010)
  - <a id="CompiledExecutableRunner.updates_default_generator_state_"></a>`updates_default_generator_state_` — [`L2011`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L2011)
- uses (calls/refs, reference-scoped): [`SharedLoadedExecutableWithMetadata`](../../common/compilation.h.md#SharedLoadedExecutableWithMetadata), [`GetDefaultDeviceGenerator`](../../eager/device_gen_impl.cc.md#GetDefaultDeviceGenerator), [`Reconstruct`](tpu_torch_compile.cc.md#FxOutputReconstructor.Reconstruct), [`PySetDeviceStateTensor`](tpu_torch_compile.cc.md#PySetDeviceStateTensor), [`RawPyObjPtr`](tpu_torch_compile.cc.md#RawPyObjPtr), [`OutputShape`](compiled_mode.h.md#OutputShape), [`PyGetDeviceStateTensor`](tpu_torch_compile.cc.md#PyGetDeviceStateTensor), [`UnpackInputTensorPointers`](tpu_torch_compile.cc.md#UnpackInputTensorPointers), [`FxOutputReconstructor`](tpu_torch_compile.cc.md#FxOutputReconstructor), [`ExecuteCompiledModel`](compiled_mode.cc.md#ExecuteCompiledModel), [`ScopedGeneratorLocks`](tpu_torch_compile.cc.md#ScopedGeneratorLocks.ScopedGeneratorLocks), [`UnboxSingleSequenceArg`](tpu_torch_compile.cc.md#UnboxSingleSequenceArg), [`ScopedGeneratorLocks`](tpu_torch_compile.cc.md#ScopedGeneratorLocks)
- used by: [`TorchTpuPyBindInitModule_tpu_torch_compile`](tpu_torch_compile.cc.md#TorchTpuPyBindInitModule_tpu_torch_compile)

### <a id="FxOutputReconstructor"></a>`FxOutputReconstructor`
- def: [`csrc/internal/compile/tpu_torch_compile.cc:1400`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1400)
- signature: `class FxOutputReconstructor`
- members:
  - <a id="FxOutputReconstructor.Call"></a>`Call(py::handle inputs, std::vector<at::Tensor> deduped_outputs)` — [`L1645`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1645)
  - <a id="FxOutputReconstructor.CheckInputIndex"></a>`CheckInputIndex(const Py_ssize_t size, const int index)` — [`L1662`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1662)
  - <a id="FxOutputReconstructor.DetermineSpecKind"></a>`DetermineSpecKind(const py::object& spec_py)` — [`L1487`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1487)
  - <a id="FxOutputReconstructor.FxOutputReconstructor"></a>`FxOutputReconstructor(py::object output_map, py::object expected_layouts, py::object spec, py::object dynamic_outputs = py::none())` — [`L1508`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1508)
  - <a id="FxOutputReconstructor.GetInputItemNewRef"></a>`GetInputItemNewRef(RawPyObjPtr inputs_ptr, const int index)` — [`L1669`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1669) — Returns a new reference to `inputs_ptr[index]`, or throws a Python
  - <a id="FxOutputReconstructor.GetReconstructedLeafNewRef"></a>`GetReconstructedLeafNewRef(size_t i, RawPyObjPtr inputs_ptr, absl::Span<at::Tensor> deduped_outputs, bool outputs_are_fresh_pjrt)` — [`L1679`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1679) — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
  - <a id="FxOutputReconstructor.InitExpectedLayouts"></a>`InitExpectedLayouts()` — [`L1538`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1538) — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
  - <a id="FxOutputReconstructor.IsStandardContiguousLayout"></a>`IsStandardContiguousLayout(const Dimensions& shape, const Dimensions& stride, int64_t storage_offset)` — [`L1441`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1441)
  - <a id="FxOutputReconstructor.ParseDimensions"></a>`ParseDimensions(py::handle seq)` — [`L1465`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1465)
  - <a id="FxOutputReconstructor.ParseEntry"></a>`ParseEntry(py::handle item)` — [`L1473`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1473)
  - <a id="FxOutputReconstructor.Reconstruct"></a>`Reconstruct(py::handle inputs_handle, absl::Span<at::Tensor> deduped_outputs, bool outputs_are_fresh_pjrt = false)` — [`L1598`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1598) — Reconstructs the FX graph output structure from runtime `inputs_handle` and — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
  - <a id="FxOutputReconstructor.Reduce"></a>`Reduce()` — [`L1652`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1652) — Enables pickle serialization (`__reduce__`) for compiled artifact caching.
  - <a id="FxOutputReconstructor.dynamic_outputs_py_"></a>`dynamic_outputs_py_` — [`L1724`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1724)
  - <a id="FxOutputReconstructor.entries_"></a>`entries_` — [`L1716`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1716)
  - <a id="FxOutputReconstructor.expected_layouts_py_"></a>`expected_layouts_py_` — [`L1722`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1722)
  - <a id="FxOutputReconstructor.layouts_"></a>`layouts_` — [`L1717`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1717)
  - <a id="FxOutputReconstructor.num_output_tensors_"></a>`num_output_tensors_` — [`L1719`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1719) — The number of deduplicated outputs that `entries_` read.
  - <a id="FxOutputReconstructor.output_map_py_"></a>`output_map_py_` — [`L1721`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1721)
  - <a id="FxOutputReconstructor.spec_kind_"></a>`spec_kind_` — [`L1720`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1720)
  - <a id="FxOutputReconstructor.spec_py_"></a>`spec_py_` — [`L1723`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1723)
- uses (calls/refs, reference-scoped): [`NormalizeIfInsideBuildDirectory`](../../common/macro_utils.cc.md#NormalizeIfInsideBuildDirectory), [`GetRootOpName`](../../ops/python_context.cc.md#GetRootOpName), [`SetRootOpNamePayload`](../../common/status_builder.cc.md#SetRootOpNamePayload), [`operator<<`](../../common/status_builder.h.md#StatusBuilder.operator), [`Dimensions`](../../common/dimension_types.h.md#Dimensions), [`ReturnIfErrorAdaptor`](../../common/error_utils.h.md#ReturnIfErrorAdaptor), [`ReturnIfErrorAdaptor`](../../common/error_utils.h.md#ReturnIfErrorAdaptor.ReturnIfErrorAdaptor), [`operator=`](../../common/error_utils.h.md#ThrowIfErrorAdapter.operator), [`ThrowIfErrorAdapter`](../../common/error_utils.h.md#ThrowIfErrorAdapter.ThrowIfErrorAdapter), [`ThrowIfErrorAdapter`](../../common/error_utils.h.md#ThrowIfErrorAdapter), [`ConsumeRequiringMessage`](../../common/error_utils.h.md#ReturnIfErrorAdaptor.ConsumeRequiringMessage), [`ForceStrides`](tpu_torch_compile.cc.md#ForceStrides), [`RawPyObjPtr`](tpu_torch_compile.cc.md#RawPyObjPtr), [`kPythonIndexError`](../../common/error_utils.h.md#kPythonIndexError), [`shape`](tpu_torch_compile.cc.md#FxOutputReconstructor.ExpectedTensorLayout.shape), [`index`](tpu_torch_compile.cc.md#FxOutputReconstructor.Entry.index), [`EntryType`](tpu_torch_compile.cc.md#FxOutputReconstructor.EntryType), [`SpecKind`](tpu_torch_compile.cc.md#FxOutputReconstructor.SpecKind), [`stride`](tpu_torch_compile.cc.md#FxOutputReconstructor.ExpectedTensorLayout.stride), [`MatchesTensor`](tpu_torch_compile.cc.md#FxOutputReconstructor.ExpectedTensorLayout.MatchesTensor), [`Entry`](tpu_torch_compile.cc.md#FxOutputReconstructor.Entry), [`storage_offset`](tpu_torch_compile.cc.md#FxOutputReconstructor.ExpectedTensorLayout.storage_offset), [`ExpectedTensorLayout`](tpu_torch_compile.cc.md#FxOutputReconstructor.ExpectedTensorLayout), [`type`](tpu_torch_compile.cc.md#FxOutputReconstructor.Entry.type), [`IsPhysicallyContiguousLayout`](tpu_torch_compile.cc.md#IsPhysicallyContiguousLayout), [`dtype`](tpu_torch_compile.cc.md#FxOutputReconstructor.ExpectedTensorLayout.dtype), [`kDedupedTensor`](tpu_torch_compile.cc.md#FxOutputReconstructor.EntryType.kDedupedTensor), [`AsFastSequence`](tpu_torch_compile.cc.md#AsFastSequence), [`can_move`](tpu_torch_compile.cc.md#FxOutputReconstructor.Entry.can_move), [`is_dynamic`](tpu_torch_compile.cc.md#FxOutputReconstructor.ExpectedTensorLayout.is_dynamic), [`is_standard_contiguous`](tpu_torch_compile.cc.md#FxOutputReconstructor.ExpectedTensorLayout.is_standard_contiguous), [`kGeneral`](tpu_torch_compile.cc.md#FxOutputReconstructor.SpecKind.kGeneral), [`is_physically_contiguous`](tpu_torch_compile.cc.md#FxOutputReconstructor.ExpectedTensorLayout.is_physically_contiguous), [`kFlatList`](tpu_torch_compile.cc.md#FxOutputReconstructor.SpecKind.kFlatList), [`kFlatTuple`](tpu_torch_compile.cc.md#FxOutputReconstructor.SpecKind.kFlatTuple), [`kLeaf`](tpu_torch_compile.cc.md#FxOutputReconstructor.SpecKind.kLeaf), [`kNonTensorPassthrough`](tpu_torch_compile.cc.md#FxOutputReconstructor.EntryType.kNonTensorPassthrough), [`kNone`](tpu_torch_compile.cc.md#FxOutputReconstructor.EntryType.kNone), [`needs_clone`](tpu_torch_compile.cc.md#FxOutputReconstructor.Entry.needs_clone), [`needs_layout_check`](tpu_torch_compile.cc.md#FxOutputReconstructor.Entry.needs_layout_check)
- used by: [`TorchTpuPyBindInitModule_tpu_torch_compile`](tpu_torch_compile.cc.md#TorchTpuPyBindInitModule_tpu_torch_compile), [`PyExecuteCompiledModel`](tpu_torch_compile.cc.md#PyExecuteCompiledModel), [`CompiledExecutableRunner`](tpu_torch_compile.cc.md#CompiledExecutableRunner.CompiledExecutableRunner), [`FormatUserOutputs`](tpu_torch_compile.cc.md#CompiledExecutableRunner.FormatUserOutputs), [`reconstruct_fn_`](tpu_torch_compile.cc.md#CompiledExecutableRunner.reconstruct_fn_)

### <a id="FxOutputReconstructor.Entry"></a>`FxOutputReconstructor.Entry`
- def: [`csrc/internal/compile/tpu_torch_compile.cc:1410`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1410)
- signature: `struct Entry`
- members:
  - <a id="FxOutputReconstructor.Entry.can_move"></a>`can_move` — [`L1414`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1414)
  - <a id="FxOutputReconstructor.Entry.index"></a>`index` — [`L1412`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1412)
  - <a id="FxOutputReconstructor.Entry.needs_clone"></a>`needs_clone` — [`L1413`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1413)
  - <a id="FxOutputReconstructor.Entry.needs_layout_check"></a>`needs_layout_check` — [`L1415`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1415)
  - <a id="FxOutputReconstructor.Entry.type"></a>`type` — [`L1411`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1411)
- uses (calls/refs, reference-scoped): [`EntryType`](tpu_torch_compile.cc.md#FxOutputReconstructor.EntryType)
- used by: [`GetReconstructedLeafNewRef`](tpu_torch_compile.cc.md#FxOutputReconstructor.GetReconstructedLeafNewRef), [`InitExpectedLayouts`](tpu_torch_compile.cc.md#FxOutputReconstructor.InitExpectedLayouts), [`FxOutputReconstructor`](tpu_torch_compile.cc.md#FxOutputReconstructor.FxOutputReconstructor), [`ParseDimensions`](tpu_torch_compile.cc.md#FxOutputReconstructor.ParseDimensions)

### <a id="FxOutputReconstructor.EntryType"></a>`FxOutputReconstructor.EntryType`
- def: [`csrc/internal/compile/tpu_torch_compile.cc:1404`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1404)
- doc: Specifies how a single leaf in the flattened FX output maps to runtime
- signature: `enum class EntryType : uint8_t`
- members:
  - <a id="FxOutputReconstructor.EntryType.kDedupedTensor"></a>`kDedupedTensor` — [`L1405`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1405) — Indexes into `deduped_outputs`.
  - <a id="FxOutputReconstructor.EntryType.kNonTensorPassthrough"></a>`kNonTensorPassthrough` — [`L1406`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1406) — Indexes into runtime `inputs` sequence.
  - <a id="FxOutputReconstructor.EntryType.kNone"></a>`kNone` — [`L1407`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1407) — Evaluates to Python `None`.
- used by: [`GetReconstructedLeafNewRef`](tpu_torch_compile.cc.md#FxOutputReconstructor.GetReconstructedLeafNewRef), [`InitExpectedLayouts`](tpu_torch_compile.cc.md#FxOutputReconstructor.InitExpectedLayouts), [`FxOutputReconstructor`](tpu_torch_compile.cc.md#FxOutputReconstructor.FxOutputReconstructor), [`Entry`](tpu_torch_compile.cc.md#FxOutputReconstructor.Entry), [`ParseEntry`](tpu_torch_compile.cc.md#FxOutputReconstructor.ParseEntry)

### <a id="FxOutputReconstructor.ExpectedTensorLayout"></a>`FxOutputReconstructor.ExpectedTensorLayout`
- def: [`csrc/internal/compile/tpu_torch_compile.cc:1419`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1419)
- doc: Expected tensor layout metadata for each deduplicated output tensor.
- signature: `struct ExpectedTensorLayout`
- members:
  - <a id="FxOutputReconstructor.ExpectedTensorLayout.MatchesTensor"></a>`MatchesTensor(const at::Tensor& tensor)` — [`L1428`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1428)
  - <a id="FxOutputReconstructor.ExpectedTensorLayout.dtype"></a>`dtype` — [`L1420`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1420)
  - <a id="FxOutputReconstructor.ExpectedTensorLayout.is_dynamic"></a>`is_dynamic` — [`L1424`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1424)
  - <a id="FxOutputReconstructor.ExpectedTensorLayout.is_physically_contiguous"></a>`is_physically_contiguous` — [`L1426`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1426)
  - <a id="FxOutputReconstructor.ExpectedTensorLayout.is_standard_contiguous"></a>`is_standard_contiguous` — [`L1425`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1425)
  - <a id="FxOutputReconstructor.ExpectedTensorLayout.shape"></a>`shape` — [`L1421`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1421)
  - <a id="FxOutputReconstructor.ExpectedTensorLayout.storage_offset"></a>`storage_offset` — [`L1423`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1423)
  - <a id="FxOutputReconstructor.ExpectedTensorLayout.stride"></a>`stride` — [`L1422`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1422)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions)
- used by: [`GetReconstructedLeafNewRef`](tpu_torch_compile.cc.md#FxOutputReconstructor.GetReconstructedLeafNewRef), [`InitExpectedLayouts`](tpu_torch_compile.cc.md#FxOutputReconstructor.InitExpectedLayouts), [`entries_`](tpu_torch_compile.cc.md#FxOutputReconstructor.entries_)

### <a id="FxOutputReconstructor.SpecKind"></a>`FxOutputReconstructor.SpecKind`
- def: [`csrc/internal/compile/tpu_torch_compile.cc:1458`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1458)
- doc: Fast-path categories for PyTree unflattening.
- signature: `enum class SpecKind : uint8_t`
- members:
  - <a id="FxOutputReconstructor.SpecKind.kFlatList"></a>`kFlatList` — [`L1461`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1461) — 1-level flat list of leaves (constructed via PyList_New).
  - <a id="FxOutputReconstructor.SpecKind.kFlatTuple"></a>`kFlatTuple` — [`L1460`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1460) — 1-level flat tuple of leaves (constructed via PyTuple_New).
  - <a id="FxOutputReconstructor.SpecKind.kGeneral"></a>`kGeneral` — [`L1462`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1462) — Arbitrary nested PyTree (delegates to spec.unflatten()).
  - <a id="FxOutputReconstructor.SpecKind.kLeaf"></a>`kLeaf` — [`L1459`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1459) — Single leaf output (returns the leaf object directly).
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions)
- used by: [`Reconstruct`](tpu_torch_compile.cc.md#FxOutputReconstructor.Reconstruct), [`DetermineSpecKind`](tpu_torch_compile.cc.md#FxOutputReconstructor.DetermineSpecKind), [`ParseEntry`](tpu_torch_compile.cc.md#FxOutputReconstructor.ParseEntry), [`num_output_tensors_`](tpu_torch_compile.cc.md#FxOutputReconstructor.num_output_tensors_)

### <a id="MultiGeneratorLocker"></a>`MultiGeneratorLocker`
- def: [`csrc/internal/compile/tpu_torch_compile.cc:1313`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1313)
- doc: A context manager for locking multiple generators' mutexes.
- signature: `class MultiGeneratorLocker`
- members:
  - <a id="MultiGeneratorLocker.Enter"></a>`Enter()` — [`L1346`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1346) — Enters the context.
  - <a id="MultiGeneratorLocker.Exit"></a>`Exit(pybind11::handle exc_type, pybind11::handle exc_val, pybind11::handle exc_tb)` — [`L1361`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1361) — Exits the context.
  - `MultiGeneratorLocker(MultiGeneratorLocker&&)` — [`L1339`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1339)
  - <a id="MultiGeneratorLocker.MultiGeneratorLocker"></a>`MultiGeneratorLocker(std::vector<at::Generator>& generators)` — [`L1318`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1318) — Constructs a MultiGeneratorLocker.
  - `MultiGeneratorLocker(const MultiGeneratorLocker&)` — [`L1337`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1337)
  - <a id="MultiGeneratorLocker.operator"></a>`operator=(const MultiGeneratorLocker&)` — [`L1338`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1338)
  - `operator=(MultiGeneratorLocker&&)` — [`L1340`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1340)
  - <a id="MultiGeneratorLocker.locks_"></a>`locks_` — [`L1371`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1371) — NOLINT
  - <a id="MultiGeneratorLocker.sorted_unique_mutexes_"></a>`sorted_unique_mutexes_` — [`L1370`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1370) — NOLINT
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`TorchTpuPyBindInitModule_tpu_torch_compile`](tpu_torch_compile.cc.md#TorchTpuPyBindInitModule_tpu_torch_compile)

### <a id="PyLayout"></a>`PyLayout`
- def: [`csrc/internal/compile/tpu_torch_compile.cc:124`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L124)
- signature: `using PyLayout = std::tuple<std::vector<int64_t>, std::vector<std::vector<int64_t>>, int64_t>`
- used by: [`PyMakePlaceholderLike`](tpu_torch_compile.cc.md#PyMakePlaceholderLike), [`PyGetDeviceLayoutIfMaterialized`](tpu_torch_compile.cc.md#PyGetDeviceLayoutIfMaterialized), [`PyGetDefaultLayout`](tpu_torch_compile.cc.md#PyGetDefaultLayout), [`PyIsDeviceShapeDynamic`](tpu_torch_compile.cc.md#PyIsDeviceShapeDynamic), [`PyGetOutputLayouts`](tpu_torch_compile.cc.md#PyGetOutputLayouts), [`PyGetParameterLayouts`](tpu_torch_compile.cc.md#PyGetParameterLayouts), [`PyGetParameterLayoutsFromMetadata`](tpu_torch_compile.cc.md#PyGetParameterLayoutsFromMetadata), [`ToPyLayouts`](tpu_torch_compile.cc.md#ToPyLayouts), [`ToPyLayout`](tpu_torch_compile.cc.md#ToPyLayout)

### <a id="RawPyObjPtr"></a>`RawPyObjPtr`
- def: [`csrc/internal/compile/tpu_torch_compile.cc:1383`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1383)
- doc: Reconstructs the original FX graph output structure from flattened MLIR
- signature: `using RawPyObjPtr = std::decay_t<decltype(py::handle().ptr())>`
- used by: [`Reconstruct`](tpu_torch_compile.cc.md#FxOutputReconstructor.Reconstruct), [`GetReconstructedLeafNewRef`](tpu_torch_compile.cc.md#FxOutputReconstructor.GetReconstructedLeafNewRef), [`CheckInputIndex`](tpu_torch_compile.cc.md#FxOutputReconstructor.CheckInputIndex), [`RunWithGenerators`](tpu_torch_compile.cc.md#CompiledExecutableRunner.RunWithGenerators), [`RunFast`](tpu_torch_compile.cc.md#CompiledExecutableRunner.RunFast), [`PyExecuteCompiledModel`](tpu_torch_compile.cc.md#PyExecuteCompiledModel), [`FormatUserOutputs`](tpu_torch_compile.cc.md#CompiledExecutableRunner.FormatUserOutputs), [`UnpackInputTensorPointers`](tpu_torch_compile.cc.md#UnpackInputTensorPointers), [`dynamic_outputs_py_`](tpu_torch_compile.cc.md#FxOutputReconstructor.dynamic_outputs_py_), [`GetInputItemNewRef`](tpu_torch_compile.cc.md#FxOutputReconstructor.GetInputItemNewRef), [`ParseOutputShapes`](tpu_torch_compile.cc.md#ParseOutputShapes), [`UnboxSingleSequenceArg`](tpu_torch_compile.cc.md#UnboxSingleSequenceArg), [`AsFastSequence`](tpu_torch_compile.cc.md#AsFastSequence)

### <a id="ScopedGeneratorLocks"></a>`ScopedGeneratorLocks`
- def: [`csrc/internal/compile/tpu_torch_compile.cc:1838`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1838)
- doc: RAII lock guard for one or more PyTorch RNG generators.
- signature: `class ScopedGeneratorLocks`
- members:
  - <a id="ScopedGeneratorLocks.ScopedGeneratorLocks"></a>`ScopedGeneratorLocks(absl::Span<at::Generator> generators)` — [`L1840`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1840)
  - <a id="ScopedGeneratorLocks.locks_"></a>`locks_` — [`L1866`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1866)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`RunWithGenerators`](tpu_torch_compile.cc.md#CompiledExecutableRunner.RunWithGenerators)

### <a id="SliceSubgraphInputs"></a>`SliceSubgraphInputs`
- def: [`csrc/internal/compile/tpu_torch_compile.cc:798`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L798)
- signature: `struct SliceSubgraphInputs`
- members:
  - <a id="SliceSubgraphInputs.element_types"></a>`element_types` — [`L803`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L803)
  - <a id="SliceSubgraphInputs.input_shapes"></a>`input_shapes` — [`L804`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L804)
  - <a id="SliceSubgraphInputs.output_shapes"></a>`output_shapes` — [`L805`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L805)
  - <a id="SliceSubgraphInputs.padded_dims"></a>`padded_dims` — [`L802`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L802)
  - <a id="SliceSubgraphInputs.target_dims"></a>`target_dims` — [`L801`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L801) — TODO: unda - Remove target_dims and padded_dims by reworking the
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions), [`Shape`](../../common/shape.h.md#Shape)
- used by: [`UnpackSliceInputs`](tpu_torch_compile.cc.md#UnpackSliceInputs), [`PyPrecompileSliceModule`](tpu_torch_compile.cc.md#PyPrecompileSliceModule), [`PyGetOrCompileSliceModule`](tpu_torch_compile.cc.md#PyGetOrCompileSliceModule)

### <a id="TensorBounds"></a>`TensorBounds`
- def: [`csrc/internal/compile/tpu_torch_compile.cc:119`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L119)
- signature: `struct TensorBounds`
- members:
  - <a id="TensorBounds.dynamic_dims"></a>`dynamic_dims` — [`L120`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L120) — INT_VEC_OK
  - <a id="TensorBounds.upper_bounds"></a>`upper_bounds` — [`L121`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L121) — INT_VEC_OK
- used by: [`TorchTpuPyBindInitModule_tpu_torch_compile`](tpu_torch_compile.cc.md#TorchTpuPyBindInitModule_tpu_torch_compile), [`MakePadDynamicShapes`](tpu_torch_compile.cc.md#MakePadDynamicShapes), [`PyPrecompilePadModule`](tpu_torch_compile.cc.md#PyPrecompilePadModule), [`PyGetDynamicPadModule`](tpu_torch_compile.cc.md#PyGetDynamicPadModule), [`PyGetOrCompilePadModule`](tpu_torch_compile.cc.md#PyGetOrCompilePadModule), [`PyMakeDynamicPlaceholder`](tpu_torch_compile.cc.md#PyMakeDynamicPlaceholder)

### <a id="TensorInfo"></a>`TensorInfo`
- def: [`csrc/internal/compile/tpu_torch_compile.cc:114`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L114)
- signature: `struct TensorInfo`
- members:
  - <a id="TensorInfo.dtype"></a>`dtype` — [`L116`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L116)
  - <a id="TensorInfo.shape"></a>`shape` — [`L115`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L115) — INT_VEC_OK
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`TorchTpuPyBindInitModule_tpu_torch_compile`](tpu_torch_compile.cc.md#TorchTpuPyBindInitModule_tpu_torch_compile), [`MakePadDynamicShapes`](tpu_torch_compile.cc.md#MakePadDynamicShapes), [`PyPrecompilePadModule`](tpu_torch_compile.cc.md#PyPrecompilePadModule), [`PyGetDynamicPadModule`](tpu_torch_compile.cc.md#PyGetDynamicPadModule), [`PyGetOrCompilePadModule`](tpu_torch_compile.cc.md#PyGetOrCompilePadModule)

## Functions
- <a id="AsFastSequence"></a>`AsFastSequence(RawPyObjPtr seq_ptr, py::object* fast_holder)` — [`L1388`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1388) — Returns `seq_ptr` directly when it is already an exact `tuple` or `list`, or
- <a id="CompileModuleWithCache"></a>`CompileModuleWithCache(MlirComputationBuilder builder, const CompilationCacheKey& cache_key, const std::vector<Shape>& input_shapes, const std::vector<Shape>& output_shapes, UniqueCompileOptions compile_options, bool build_mlir_module, bool is_caching_disabled, bool compile_dynamic_adapter = false)` — [`L868`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L868) — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="ConvertArgumentLayouts"></a>`ConvertArgumentLayouts(const std::vector<at::Tensor>& argument_tensors, std::optional<std::vector<py::object>> argument_layouts_opt)` — [`L582`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L582)
- <a id="ConvertTraverseAndCompileOptions"></a>`ConvertTraverseAndCompileOptions(const std::vector<at::Tensor>& argument_tensors, bool fast_compile, bool build_mlir_module, bool use_stablehlo_bounds, std::optional<std::vector<py::object>> argument_layouts_opt = std::nullopt, const std::vector<int64_t>& donated_inputs = {}, const std::optional<std::string>& module_name = std::nullopt)` — [`L605`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L605)
- <a id="ForceStrides"></a>`ForceStrides(const at::Tensor& tensor, const Dimensions& target_strides, int64_t target_storage_offset)` — [`L1256`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1256) — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="HasSparseCoreCustomCall"></a>`HasSparseCoreCustomCall(mlir::ModuleOp module)` — [`L424`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L424)
- <a id="HasSpmdShardingInstructions"></a>`HasSpmdShardingInstructions(mlir::ModuleOp module)` — [`L404`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L404) — Check if the MLIR module contains SparseCore custom call operations.
- <a id="IsPhysicallyContiguousLayout"></a>`IsPhysicallyContiguousLayout(at::IntArrayRef shape, at::IntArrayRef stride, int64_t storage_offset)` — [`L1238`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1238) — Returns whether `storage_offset` is zero and every element of a tensor with
- <a id="IsValidLayout"></a>`IsValidLayout(const std::vector<int64_t>& layout, int64_t rank)` — [`L129`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L129)
- <a id="LoadSerializedExecutableImpl"></a>`LoadSerializedExecutableImpl(std::string_view data)` — [`L1189`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1189)
- <a id="MakePadDynamicShapes"></a>`MakePadDynamicShapes(const std::vector<TensorInfo>& tensor_info, const std::vector<TensorBounds>& bounds_list)` — [`L730`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L730) — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="ParseCustomLayout"></a>`ParseCustomLayout(const py::object& obj, const at::Tensor& tensor, size_t arg_index)` — [`L556`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L556) — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="ParseOutputShapes"></a>`ParseOutputShapes(py::handle output_shapes_obj)` — [`L1776`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1776)
- <a id="ParseTupleLayout"></a>`ParseTupleLayout(const py::tuple& t, CustomLayout& cl, std::vector<int64_t>& minor_to_major)` — [`L540`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L540)
- <a id="PyAssignConstantTensor"></a>`PyAssignConstantTensor(const at::Tensor& cpu_src_tensor, const at::Tensor& tpu_dst_tensor)` — [`L1215`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1215)
- <a id="PyAsyncTraverseAndCompile"></a>`PyAsyncTraverseAndCompile(const std::vector<at::Tensor>& result_tensors, const std::vector<at::Tensor>& argument_tensors, bool fast_compile = false, bool build_mlir_module = false, bool use_stablehlo_bounds = false, std::optional<std::vector<py::object>> argument_layouts_opt = std::nullopt, const std::vector<int64_t>& donated_inputs = {}, const std::optional<std::string>& module_name = std::nullopt)` — [`L623`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L623) — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="PyBuildMlir"></a>`PyBuildMlir(const std::vector<at::Tensor>& result_tensors, const std::vector<at::Tensor>& argument_tensors, bool use_stablehlo_bounds)` — [`L334`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L334) — Returns a ContextedModule corresponding to the graph terminating at — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="PyClearExportModeDefaultDeviceGenerators"></a>`PyClearExportModeDefaultDeviceGenerators()` — [`L725`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L725) — Clears all registered export-mode default generator overrides.
- <a id="PyCompileMlir"></a>`PyCompileMlir(std::shared_ptr<ContextedModule> module, const bool fast_compile, const std::vector<std::vector<int64_t>>& argument_layouts)` — [`L450`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L450) — Compiles an MLIR module. — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="PyExecuteCompiledModel"></a>`PyExecuteCompiledModel(const SharedLoadedExecutableWithMetadata& executable, py::handle py_args, py::handle output_shapes_obj = py::none(), py::handle reconstruct_fn = py::none())` — [`L1791`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1791) — Executes a compiled PJRT executable with the given arguments.
- <a id="PyForceStrides"></a>`PyForceStrides(const at::Tensor& tensor, const std::vector<int64_t>& target_strides, int64_t target_storage_offset)` — [`L1298`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1298)
- <a id="PyGetDefaultLayout"></a>`PyGetDefaultLayout(at::ScalarType dtype, const std::vector<int64_t>& shape)` — [`L283`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L283)
- <a id="PyGetDeviceLayoutIfMaterialized"></a>`PyGetDeviceLayoutIfMaterialized(const at::Tensor& tensor)` — [`L259`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L259)
- <a id="PyGetDeviceStateTensor"></a>`PyGetDeviceStateTensor(const at::Generator& gen)` — [`L689`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L689) — Returns the internal TPU RNG state tensor {seed, offset} from a generator. — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="PyGetDynamicPadModule"></a>`PyGetDynamicPadModule(const std::vector<TensorInfo>& tensor_info, const std::vector<TensorBounds>& bounds_list, const bool fast_compile)` — [`L1044`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1044) — Returns a CompileResult containing the executable and the MLIR — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="PyGetOrCompilePadModule"></a>`PyGetOrCompilePadModule(const std::vector<TensorInfo>& tensor_info, const std::vector<TensorBounds>& bounds_list, const bool fast_compile, const bool build_mlir_module, const bool is_caching_disabled)` — [`L982`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L982) — Returns a CompileResult containing the executable and optionally the MLIR — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="PyGetOrCompileSliceModule"></a>`PyGetOrCompileSliceModule(const std::vector<std::vector<int64_t>>& target_shapes, const std::vector<std::vector<int64_t>>& padded_shapes, const std::vector<at::ScalarType>& input_scalar_types, const bool fast_compile, const bool build_mlir_module, const bool is_caching_disabled)` — [`L1144`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1144) — Returns a CompileResult containing the executable and optionally the MLIR — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="PyGetOutputLayouts"></a>`PyGetOutputLayouts(const xla::PjRtLoadedExecutable& executable)` — [`L312`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L312)
- <a id="PyGetOutputLayoutsFromMetadata"></a>`PyGetOutputLayoutsFromMetadata(const LoadedExecutableWithMetadata& executable_metadata)` — [`L325`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L325)
- <a id="PyGetParameterLayouts"></a>`PyGetParameterLayouts(const xla::PjRtLoadedExecutable& executable)` — [`L306`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L306)
- <a id="PyGetParameterLayoutsFromMetadata"></a>`PyGetParameterLayoutsFromMetadata(const LoadedExecutableWithMetadata& executable_metadata)` — [`L318`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L318)
- <a id="PyIsConstantTensor"></a>`PyIsConstantTensor(const at::Tensor& tensor)` — [`L1220`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1220)
- <a id="PyIsDeviceShapeDynamic"></a>`PyIsDeviceShapeDynamic(const at::Tensor& tensor)` — [`L301`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L301)
- <a id="PyIsPinnedHost"></a>`PyIsPinnedHost(const at::Tensor& tensor)` — [`L147`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L147)
- <a id="PyLoadSerializedExecutable"></a>`PyLoadSerializedExecutable(py::bytes& serialized_bytes)` — [`L1201`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1201)
- <a id="PyMakeConstantTensor"></a>`PyMakeConstantTensor(const at::Tensor& cpu_tensor)` — [`L1210`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1210)
- <a id="PyMakeDynamicPlaceholder"></a>`PyMakeDynamicPlaceholder(const std::vector<int64_t>& sizes, at::ScalarType dtype, const TensorBounds& bounds, bool requires_grad, bool is_pinned_host)` — [`L165`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L165) — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="PyMakeExportModeDeviceGenerator"></a>`PyMakeExportModeDeviceGenerator(const at::Generator& orig_gen)` — [`L702`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L702) — Creates a new export-mode generator by cloning the state of an eager
- <a id="PyMakePlaceholder"></a>`PyMakePlaceholder(const std::vector<int64_t>& sizes, at::ScalarType dtype, bool requires_grad, bool is_pinned_host)` — [`L155`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L155) — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="PyMakePlaceholderLike"></a>`PyMakePlaceholderLike(const at::Tensor& arg_tensor, bool is_pinned_host)` — [`L186`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L186) — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="PyParseMlirText"></a>`PyParseMlirText(const std::string& mlir_text)` — [`L357`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L357) — Parses MLIR text, verifies it, and returns a ContextedModule. — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="PyPrecompilePadModule"></a>`PyPrecompilePadModule(const std::vector<TensorInfo>& tensor_info, const std::vector<TensorBounds>& bounds_list, const bool fast_compile)` — [`L926`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L926) — Precompiles the pad subgraph for the given shapes. Doesn't wait for the — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="PyPrecompileSliceModule"></a>`PyPrecompileSliceModule(const std::vector<std::vector<int64_t>>& target_shapes, const std::vector<std::vector<int64_t>>& padded_shapes, const std::vector<at::ScalarType>& input_scalar_types, const bool fast_compile)` — [`L1083`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1083) — Precompiles the slice subgraph for the given shapes. Doesn't wait for the — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="PyPushEnableTracebacks"></a>`PyPushEnableTracebacks(std::optional<bool> enabled)` — [`L677`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L677)
- <a id="PySerializeExecutable"></a>`PySerializeExecutable(const SharedLoadedExecutableWithMetadata& executable)` — [`L1181`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1181)
- <a id="PySerializeMlirBytecode"></a>`PySerializeMlirBytecode(std::shared_ptr<ContextedModule> module)` — [`L390`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L390) — Serializes a ContextedModule to bytecode.
- <a id="PySerializeMlirText"></a>`PySerializeMlirText(std::shared_ptr<ContextedModule> module, bool enable_debug_info)` — [`L382`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L382) — Serializes a ContextedModule to MLIR text.
- <a id="PySerializePortableArtifact"></a>`PySerializePortableArtifact(std::shared_ptr<ContextedModule> module)` — [`L396`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L396) — Serializes a ContextedModule to a versioned portable artifact.
- <a id="PySetDeviceStateTensor"></a>`PySetDeviceStateTensor(const at::Generator& gen, at::Tensor rng_state)` — [`L695`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L695) — Sets the internal TPU RNG state tensor {seed, offset} on a generator. — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="PySetExportModeDefaultDeviceGenerator"></a>`PySetExportModeDefaultDeviceGenerator(c10::optional<at::Generator> gen, const c10::DeviceIndex idx)` — [`L719`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L719) — Registers an export-mode generator override for GetDefaultDeviceGenerator().
- <a id="PyTraverseAndCompile"></a>`PyTraverseAndCompile(const std::vector<at::Tensor>& result_tensors, const std::vector<at::Tensor>& argument_tensors, bool fast_compile = false, bool build_mlir_module = false, bool use_stablehlo_bounds = false, std::optional<std::vector<py::object>> argument_layouts_opt = std::nullopt, const std::vector<int64_t>& donated_inputs = {}, const std::optional<std::string>& module_name = std::nullopt)` — [`L653`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L653)
- <a id="ToPaddedShapes"></a>`ToPaddedShapes(const std::vector<Shape>& shapes)` — [`L785`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L785)
- <a id="ToPyLayout"></a>`ToPyLayout(const xla::Layout& layout)` — [`L232`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L232)
- <a id="ToPyLayouts"></a>`ToPyLayouts(const std::vector<std::shared_ptr<const xla::PjRtLayout>>& layouts)` — [`L245`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L245)
- <a id="ToStaticShapes"></a>`ToStaticShapes(const std::vector<Shape>& shapes)` — [`L776`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L776)
- <a id="TorchTpuPyBindInitModule_tpu_torch_compile"></a>`TorchTpuPyBindInitModule_tpu_torch_compile(tpu_torch_compile, m)` — [`L2014`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L2014) — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="UnboxSingleSequenceArg"></a>`UnboxSingleSequenceArg(RawPyObjPtr args_ptr, py::object* fast_holder)` — [`L1733`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1733) — Dynamo's boxed calling convention passes compiled graph inputs as either
- <a id="UnpackInputTensorPointers"></a>`UnpackInputTensorPointers(RawPyObjPtr fast_args_ptr, absl::InlinedVector<const at::Tensor*, 128>* argument_tensor_ptrs, absl::InlinedVector<at::Generator, 2>* generators = nullptr)` — [`L1758`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L1758) — Fast-path argument unpacker that traverses the contiguous internal
- <a id="UnpackSliceInputs"></a>`UnpackSliceInputs(const std::vector<std::vector<int64_t>>& target_shapes, const std::vector<std::vector<int64_t>>& padded_shapes, const std::vector<at::ScalarType>& input_scalar_types)` — [`L808`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L808) — documented in [compiled-mode](../../../../concepts/compiled-mode.md)
- <a id="pybind11_exec_tpu_torch_compile"></a>`pybind11_exec_tpu_torch_compile(tpu_torch_compile, m)` — [`L2014`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L2014)
- <a id="pybind11_init_tpu_torch_compile"></a>`pybind11_init_tpu_torch_compile(tpu_torch_compile, m)` — [`L2014`](../../../../../../../raw/code/torch_tpu/csrc/internal/compile/tpu_torch_compile.cc#L2014)

