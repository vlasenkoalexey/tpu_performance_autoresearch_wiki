---
title: 'Module: csrc/ops/op_builder_utils.h'
type: catalog
provenance: extracted
module: csrc/ops/op_builder_utils.h
status: fresh
symbol_base: 'cxx . . $ '
symbols:
  MakeConstant: torch_tpu/MakeConstant(7ff6b3e46d870de4).
  MakeScalarConstant: torch_tpu/MakeScalarConstant(a13adaa91abd4b70).
  MakeConstantLike: torch_tpu/MakeConstantLike(ffe39bf9eb7fc2d7).
  DynamicMlirOpResults: torch_tpu/DynamicMlirOpResults#
  MlirOpResults: torch_tpu/MlirOpResults#
  ApplyBroadcastIfNeeded: torch_tpu/ApplyBroadcastIfNeeded(f61962d58c48ad60).
  kDynamicSize: torch_tpu/kDynamicSize.
  ToMlirOpBuilder: absl/torch_tpu/ToMlirOpBuilder(7864480464b09eea).
  IsComplexType: torch_tpu/IsComplexType(b3276214a3243916).
  InferSize: torch_tpu/InferSize(74365378b4ba04da).
  DebugStringOptions.kDisableDebugInfo: torch_tpu/DebugStringOptions#kDisableDebugInfo.
  MlirUnaryOpBuilder: torch_tpu/MlirUnaryOpBuilder#
  NAryMlirOpBuilder: torch_tpu/NAryMlirOpBuilder#
  AsArrayRef: torch_tpu/AsArrayRef(7ad9aba464a6c125).
  MlirComputationBuilder: torch_tpu/MlirComputationBuilder#
  ReshapeReassociation.reassociation: absl/torch_tpu/ReshapeReassociation#reassociation.
  BuildFillUninitialized: absl/torch_tpu/BuildFillUninitialized.
  ReshapeType: torch_tpu/ReshapeType#
  ToResultVector: torch_tpu/ToResultVector(4a9a2ad96bb8f188).
  BroadcastIfNeeded: absl/torch_tpu/BroadcastIfNeeded.
  RngBitGeneratorLike: absl/torch_tpu/RngBitGeneratorLike.
  MlirOpBuilder: torch_tpu/MlirOpBuilder#
  MlirBinaryOpBuilder: torch_tpu/MlirBinaryOpBuilder#
  InferSizeImpl: absl/torch_tpu/internal/InferSizeImpl(21618ad741022f0e).
  MakeZeroSizedTensor: absl/torch_tpu/MakeZeroSizedTensor.
  ConvertedOps: torch_tpu/ConvertedOps#
  ReshapeReassociation: torch_tpu/ReshapeReassociation#
  AnnotateBufferDonations: absl/torch_tpu/AnnotateBufferDonations.
  ConvertedOps.op2: absl/torch_tpu/ConvertedOps#op2.
  DebugStringOptions: torch_tpu/DebugStringOptions#
  MlirOpResultsTraits: torch_tpu/internal/MlirOpResultsTraits#
  IsFloatType: torch_tpu/IsFloatType(b3276214a3243916).
  IsBooleanType: torch_tpu/IsBooleanType(b3276214a3243916).
  ReshapeReassociation.type: torch_tpu/ReshapeReassociation#type.
  MlirNullaryOpBuilder: torch_tpu/MlirNullaryOpBuilder#
  Squeeze: absl/torch_tpu/Squeeze.
  ConvertedOps.op1: torch_tpu/ConvertedOps#op1.
  NAryMlirOpBuilderTraits.type: torch_tpu/internal/NAryMlirOpBuilderTraits#type#
  DebugStringOptions.kEnableDebugInfo: torch_tpu/DebugStringOptions#kEnableDebugInfo.
  MlirTernaryOpBuilder: torch_tpu/MlirTernaryOpBuilder#
  Broadcast: absl/torch_tpu/Broadcast.
  NAryMlirOpBuilderTraits: torch_tpu/internal/NAryMlirOpBuilderTraits#
  GetDims: torch_tpu/internal/GetDims(4cde1b1beae93e7c).
  RngBitGeneratorResults.output: torch_tpu/RngBitGeneratorResults#output.
  ReshapeType.kTransposeLike: torch_tpu/ReshapeType#kTransposeLike.
  ReshapeType.kFlatten: torch_tpu/ReshapeType#kFlatten.
  ReshapeType.kCollapse: torch_tpu/ReshapeType#kCollapse.
  ReshapeType.kExpand: torch_tpu/ReshapeType#kExpand.
  IsUnsignedType: torch_tpu/IsUnsignedType(b3276214a3243916).
  RngBitGeneratorResults: absl/torch_tpu/RngBitGeneratorResults#
  MlirOpResultsTraits.type: torch_tpu/internal/MlirOpResultsTraits#type#
  RngBitGeneratorResults.output_state: torch_tpu/RngBitGeneratorResults#output_state.
  ReshapeType.kUnknown: torch_tpu/ReshapeType#kUnknown.
---
# Module: [`csrc/ops/op_builder_utils.h`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h)

## Classes
### `ConvertedOps`
- def: [`csrc/ops/op_builder_utils.h:601`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L601)
- doc: Result structure for `ConvertIfIntegers` containing the two operands after
- signature: `struct ConvertedOps`
- members:
  - <a id="ConvertedOps.op1"></a>`op1` — [`L604`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L604) — The first operand after applying type conversion (if it was an
  - `op1` — [`L604`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L604) — The first operand after applying type conversion (if it was an
  - `op2` — [`L607`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L607) — The second operand after applying type conversion (if it was an
  - <a id="ConvertedOps.op2"></a>`op2` — [`L607`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L607) — The second operand after applying type conversion (if it was an
- uses (calls/refs, reference-scoped): [`ConvertIfInteger`](op_builder_utils.cc.md#ConvertIfInteger), [`ConvertIfIntegers`](op_builder_utils.cc.md#ConvertIfIntegers), [`ConvertedOps`](op_builder_utils.h.md#ConvertedOps)
- used by: [`TestBody`](op_builder_utils_test.cc.md#OpBuilderUtils_ConvertIfIntegers_TwoOperands_Int_Test.TestBody), [`TestBody`](op_builder_utils_test.cc.md#OpBuilderUtils_ConvertIfIntegers_TwoIntegerOperands_Test.TestBody), [`TestBody`](op_builder_utils_test.cc.md#OpBuilderUtils_ConvertIfIntegers_TwoOperands_Float_Int_Test.TestBody), [`TestBody`](op_builder_utils_test.cc.md#OpBuilderUtils_ConvertIfIntegers_TwoOperands_Float_Test.TestBody), [`TestBody`](op_builder_utils_test.cc.md#OpBuilderUtils_ConvertIfIntegers_TwoOperands_Int_Float_Test.TestBody)

### <a id="DebugStringOptions"></a>`DebugStringOptions`
- def: [`csrc/ops/op_builder_utils.h:178`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L178)
- doc: DebugStringOptions for enabling/disabling debug info in the debug string.
- signature: `enum class DebugStringOptions`
- members:
  - `kDisableDebugInfo` — [`L180`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L180)
  - <a id="DebugStringOptions.kDisableDebugInfo"></a>`kDisableDebugInfo` — [`L180`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L180)
  - <a id="DebugStringOptions.kEnableDebugInfo"></a>`kEnableDebugInfo` — [`L179`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L179)
  - `kEnableDebugInfo` — [`L179`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L179)
- uses (calls/refs, reference-scoped): [`Dimensions`](../common/dimension_types.h.md#Dimensions), [`GetDimensions`](op_builder_utils.cc.md#GetDimensions), [`DebugString`](op_builder_utils.cc.md#DebugString), [`SerializePortableArtifact`](op_builder_utils.cc.md#SerializePortableArtifact), [`SerializeBytecode`](op_builder_utils.cc.md#SerializeBytecode), [`GetStaticShape`](op_builder_utils.cc.md#GetStaticShape), [`GetStaticShape`](op_builder_utils.cc.md#GetStaticShape), [`GetDimensions`](op_builder_utils.cc.md#GetDimensions), [`GetDimensions`](op_builder_utils.cc.md#GetDimensions), [`GetDimensions`](op_builder_utils.cc.md#GetDimensions), [`GetStaticShape`](op_builder_utils.cc.md#GetStaticShape), [`GetStaticShape`](op_builder_utils.cc.md#GetStaticShape), [`DebugStringOptions`](op_builder_utils.h.md#DebugStringOptions)
- used by: [`DebugString`](op_builder_utils.cc.md#DebugString), [`GetOrCompileImpl`](../common/compilation_cache.cc.md#CompilationCache.GetOrCompileImpl), [`PyBuildMlir`](../internal/compile/tpu_torch_compile.cc.md#PyBuildMlir), [`PyParseMlirText`](../internal/compile/tpu_torch_compile.cc.md#PyParseMlirText), [`PySerializeMlirText`](../internal/compile/tpu_torch_compile.cc.md#PySerializeMlirText)

### <a id="DynamicMlirOpResults"></a>`DynamicMlirOpResults`
- def: [`csrc/ops/op_builder_utils.h:159`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L159)
- doc: Result type of an MLIR op builder for an arbitrary number of outputs.
- signature: `using DynamicMlirOpResults = MlirOpResults<kDynamicSize>`
- uses (calls/refs, reference-scoped): [`GetTensorTypeOrDie`](op_builder_utils.cc.md#GetTensorTypeOrDie), [`GetElementTypeOrSelf`](op_builder_utils.cc.md#GetElementTypeOrSelf), [`MlirOpResults`](op_builder_utils.h.md#MlirOpResults), [`GetElementTypeOrSelf`](op_builder_utils.cc.md#GetElementTypeOrSelf), [`kDynamicSize`](op_builder_utils.h.md#kDynamicSize)
- used by: [`alltoall`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.alltoall), [`CreateViewDeviceBufferRef`](../eager/device_buffer_utils.cc.md#CreateViewDeviceBufferRef), [`allgather`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.allgather), [`Iota`](op_builder_utils.cc.md#Iota), [`PyCreateAssociativeScanOp`](../internal/compile/dispatch_scan.cc.md#PyCreateAssociativeScanOp), [`BuildMlirModule`](../eager/traversal.cc.md#Traversal.BuildMlirModule), [`AtenSparseMapRow`](experimental/sparse_map_row/sparse_map_row_aten_kernels.cc.md#AtenSparseMapRow), [`PyCreateScanOp`](../internal/compile/dispatch_scan.cc.md#PyCreateScanOp), [`CreateFlashAttentionKernelImpl`](scaled_dot_product_attention/flash_attention_kernel_builder.cc.md#CreateFlashAttentionKernelImpl), [`CreateEmptyDeviceBufferRef`](../eager/device_buffer_utils.cc.md#CreateEmptyDeviceBufferRef), [`BuildScanShlo`](scan_builder.cc.md#BuildScanShlo), [`BuildScanShlo`](scan_builder.cc.md#BuildScanShlo), [`TestBody`](../eager/materialize_test.cc.md#MaterializeTest_CompilerOptionsPropagateToMaterializeThread_Test.TestBody), [`CreateConstantDeviceBufferRefImpl`](../eager/device_buffer_utils.cc.md#CreateConstantDeviceBufferRefImpl), [`MakeAsStridedInverseBuilder`](../eager/device_buffer_utils.cc.md#MakeAsStridedInverseBuilder), [`TestBody`](../common/dynamism_utils_test.cc.md#DynamismOpsTest_GetTraversalOutputDimensionsWithBoundedInput_Test.TestBody), [`TestBody`](../eager/events_queue_test.cc.md#EventsQueueTest_ClearsBuffersAfterMaterialization_Test.TestBody), [`BuildAssociativeScan`](../internal/compile/dispatch_scan.cc.md#BuildAssociativeScan), [`DummyBuilder`](../eager/events_queue_test.cc.md#DummyBuilder), [`TestBody`](../common/dynamism_utils_test.cc.md#DynamismOpsTest_GetTraversalOutputDimensionsNoBoundedInput_Test.TestBody), [`TestBody`](../eager/op_dispatcher_test.cc.md#AutoDonateInPlaceBuffers_MultiOutputDeviceBufferListTracksPerSlotLiveDataPtrs_Test.TestBody), [`TestBody`](../eager/shutdown_test.cc.md#ShutdownTest_E2EShutdownCompletes_Test.TestBody), [`ResolveNegativeIndices`](index_utils.cc.md#ResolveNegativeIndices), [`GetPadModule`](../internal/dynamism/dynamism_ops.cc.md#GetPadModule), [`BuildAssociativeScanChlo`](scan_builder.cc.md#BuildAssociativeScanChlo), [`TestBody`](../eager/traversal_test.cc.md#TraversalTest_CompileAnnotatesArgumentLayoutsWithTilingAndCaching_Test.TestBody), [`TestBody`](../eager/traversal_test.cc.md#TraversalTest_CompilePopulatesAndResetsOutCacheKey_Test.TestBody), [`GetDynamicPadModule`](../internal/dynamism/dynamism_ops.cc.md#GetDynamicPadModule), [`ToResultVector`](op_builder_utils.cc.md#ToResultVector), [`GetSliceModule`](../internal/dynamism/dynamism_ops.cc.md#GetSliceModule), [`ToMlirOpBuilder`](op_builder_utils.h.md#ToMlirOpBuilder), [`TestBody`](../eager/op_dispatcher_test.cc.md#OpDispatcher_OutputCastingWithoutComputationDtype_Test.TestBody), [`BuildCumsumShlo`](cumsum/cumsum.cc.md#BuildCumsumShlo), [`TestBody`](../eager/traversal_test.cc.md#TraversalTest_CompileAnnotatesArgumentLayouts_Test.TestBody), [`TestBody`](scan_builder_test.cc.md#MultiScanBuilderTest_BodyBuilderError_Test.TestBody), [`TestBody`](scan_builder_test.cc.md#ScanBuilderTest_BodyBuilderError_Test.TestBody), [`TestBody`](../eager/traversal_test.cc.md#TraversalTest_BuildMlirModuleRegistersFuncInlinerExtensionAndInlinesHelpers_Test.TestBody), [`BuildCummaxShlo`](cummax/cummax.cc.md#BuildCummaxShlo), [`BuildCumminShlo`](cummin/cummin.cc.md#BuildCumminShlo), [`BuildCumprodShlo`](cumprod/cumprod.cc.md#BuildCumprodShlo)  (+53 more)

### <a id="MlirBinaryOpBuilder"></a>`MlirBinaryOpBuilder`
- def: [`csrc/ops/op_builder_utils.h:735`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L735)
- doc: An op builder with two inputs and one result, for example torch.add().
- signature: `using MlirBinaryOpBuilder = absl::AnyInvocable<absl::StatusOr<mlir::MlirOp>(mlir::MlirOp input1, mlir::MlirOp input2) const>`
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BinaryOpOut`](binary_aten_kernels.h.md#BinaryOpOut), [`DispatchBinaryOpOut`](binary_aten_kernels.cc.md#DispatchBinaryOpOut), [`BitwiseShiftScalarHelper`](binary_aten_kernels.cc.md#BitwiseShiftScalarHelper), [`DispatchBinaryOp`](binary_aten_kernels.cc.md#DispatchBinaryOp), [`AtenComparisonScalarOutHelper`](binary_aten_kernels.cc.md#AtenComparisonScalarOutHelper), [`DispatchBinaryOp`](binary_aten_kernels.cc.md#DispatchBinaryOp), [`DispatchBinaryOpOut`](binary_aten_kernels.cc.md#DispatchBinaryOpOut), [`LogicalBinaryOutImpl`](logical/logical_aten_kernels.cc.md#LogicalBinaryOutImpl), [`BinaryOp`](binary_aten_kernels.h.md#BinaryOp), [`DivOpOptions`](binary_aten_kernels.cc.md#DivOpOptions)

### <a id="MlirComputationBuilder"></a>`MlirComputationBuilder`
- def: [`csrc/ops/op_builder_utils.h:744`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L744)
- doc: Builder function for an MLIR-based computation. This is an MlirOpBuilder
- signature: `using MlirComputationBuilder = absl::AnyInvocable<absl::StatusOr<mlir::OwningOpRef<mlir::ModuleOp>>(mlir::MLIRContext& mlir_context) const>`
- uses (calls/refs, reference-scoped): [`DynamicMlirOpResults`](op_builder_utils.h.md#DynamicMlirOpResults)
- used by: [`Compile`](../eager/traversal.cc.md#Traversal.Compile), [`UnboundedDynamicCache`](../common/compilation_cache.h.md#CompilationCache.UnboundedDynamicCache), [`GetOrCompileImpl`](../common/compilation_cache.cc.md#CompilationCache.GetOrCompileImpl), [`kUnboundedDynamic`](../common/compilation_cache.h.md#CompilationCache.CacheEntryKind.kUnboundedDynamic), [`Make`](../common/compilation.cc.md#ContextedModule.Make), [`PyPrecompileSliceModule`](../internal/compile/tpu_torch_compile.cc.md#PyPrecompileSliceModule), [`PyGetOrCompileSliceModule`](../internal/compile/tpu_torch_compile.cc.md#PyGetOrCompileSliceModule), [`PyPrecompilePadModule`](../internal/compile/tpu_torch_compile.cc.md#PyPrecompilePadModule), [`CreateSlicingKernel`](../common/compilation_cache.cc.md#CompilationCache.CreateSlicingKernel), [`PyGetDynamicPadModule`](../internal/compile/tpu_torch_compile.cc.md#PyGetDynamicPadModule), [`PyGetOrCompilePadModule`](../internal/compile/tpu_torch_compile.cc.md#PyGetOrCompilePadModule), [`TestBody`](../common/compilation_cache_test.cc.md#CompilationCacheTest_PeakMemoryReported_Test.TestBody), [`CompileModuleWithCache`](../internal/compile/tpu_torch_compile.cc.md#CompileModuleWithCache), [`module_`](../common/compilation.h.md#ContextedModule.module_), [`CreatePaddingKernel`](../common/compilation_cache.cc.md#CompilationCache.CreatePaddingKernel), [`TestBody`](../common/compilation_cache_test.cc.md#CompilationCacheTest_GetOrCompileLogsOnMiss_Test.TestBody), [`MlirComputationBuilderToExecutableBuilder`](../common/compilation.cc.md#MlirComputationBuilderToExecutableBuilder), [`GetOrCompile`](../common/compilation_cache.cc.md#CompilationCache.GetOrCompile), [`GetOrCompile`](../common/compilation_cache.cc.md#CompilationCache.GetOrCompile), [`operator=`](../common/compilation.h.md#ContextedModule.operator)

### <a id="MlirNullaryOpBuilder"></a>`MlirNullaryOpBuilder`
- def: [`csrc/ops/op_builder_utils.h:727`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L727)
- doc: An op builder with zero inputs and one result, for example torch.ones().
- signature: `using MlirNullaryOpBuilder = absl::AnyInvocable<absl::StatusOr<mlir::MlirOp>(mlir::MlirBuilder& builder) const>`
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ApplyNullaryOpOut`](nullary_aten_kernels.cc.md#ApplyNullaryOpOut), [`ApplyNullaryOp`](nullary_aten_kernels.cc.md#ApplyNullaryOp)

### <a id="MlirOpBuilder"></a>`MlirOpBuilder`
- def: [`csrc/ops/op_builder_utils.h:634`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L634)
- doc: The most general op builder, with zero or more inputs and one or more
- signature: `using MlirOpBuilder = absl::AnyInvocable<absl::StatusOr<DynamicMlirOpResults>(mlir::MlirBuilder& builder, absl::Span<mlir::MlirOp> inputs) const>`
- uses (calls/refs, reference-scoped): [`DynamicMlirOpResults`](op_builder_utils.h.md#DynamicMlirOpResults)
- used by: [`CreateDeferred`](../eager/device_buffer.cc.md#DeviceBufferList.CreateDeferred), [`PyCreateAssociativeScanOp`](../internal/compile/dispatch_scan.cc.md#PyCreateAssociativeScanOp), [`PyCreateScanOp`](../internal/compile/dispatch_scan.cc.md#PyCreateScanOp), [`TestBody`](../eager/traversal_test.cc.md#TraversalTest_CompileAnnotatesArgumentLayoutsWithTilingAndCaching_Test.TestBody), [`TestBody`](../eager/traversal_test.cc.md#TraversalTest_CompilePopulatesAndResetsOutCacheKey_Test.TestBody), [`DeviceBufferList`](../eager/device_buffer.h.md#DeviceBufferList.DeviceBufferList), [`DeferredOp`](../eager/device_buffer.h.md#DeferredOp.DeferredOp), [`NAryMlirOpBuilder`](op_builder_utils.h.md#NAryMlirOpBuilder), [`op_name`](../eager/device_buffer.h.md#DeferredOp.op_name), [`op_name`](../eager/device_buffer_utils.h.md#DeferredOpParams.op_name), [`op_name_`](../eager/device_buffer.h.md#DeferredOp.op_name_), [`AsStridedInverseBuilderResult`](../eager/device_buffer_utils.cc.md#AsStridedInverseBuilderResult)

### <a id="MlirOpResults"></a>`MlirOpResults`
- def: [`csrc/ops/op_builder_utils.h:155`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L155) — documented in [stablehlo-op-builder](../../../concepts/stablehlo-op-builder.md)
- doc: Result type of an MLIR op builder for the given number of outputs. If
- signature: `template <int kNumOutputs> using MlirOpResults = internal::MlirOpResultsTraits<kNumOutputs>::type`
- uses (calls/refs, reference-scoped): [`MlirOpResultsTraits`](op_builder_utils.h.md#MlirOpResultsTraits), [`MlirOpResultsTraits`](op_builder_utils.h.md#MlirOpResultsTraits)
- used by: [`AtenPreluKernelBackward`](prelu/prelu_aten_kernels.cc.md#AtenPreluKernelBackward), [`AtenWeightNormInterface`](weight_norm/weight_norm_aten_kernels.cc.md#AtenWeightNormInterface), [`DynamicMlirOpResults`](op_builder_utils.h.md#DynamicMlirOpResults), [`AtenCtcLossTensor`](ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossTensor), [`AtenCtcLossBackwardTensor`](ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossBackwardTensor), [`AtenRmsNorm`](rms_norm/rms_norm_aten_kernels.cc.md#AtenRmsNorm), [`AtenFusedRmsNorm`](rms_norm/rms_norm_aten_kernels.cc.md#AtenFusedRmsNorm), [`AtenFusedRmsNormBackward`](rms_norm/rms_norm_aten_kernels.cc.md#AtenFusedRmsNormBackward), [`AtenNativeGroupNormBackward`](group_norm/group_norm_aten_kernels.cc.md#AtenNativeGroupNormBackward), [`AtenCummaxHelper`](cummax/cummax_aten_kernels.cc.md#AtenCummaxHelper), [`AtenCumminHelper`](cummin/cummin_aten_kernels.cc.md#AtenCumminHelper), [`AtenNativeLayerNorm`](layer_norm/layer_norm_aten_kernels.cc.md#AtenNativeLayerNorm), [`AtenLayerNormBackward`](layer_norm/layer_norm_aten_kernels.cc.md#AtenLayerNormBackward), [`AtenTopKValues`](topk/topk_aten_kernels.cc.md#AtenTopKValues), [`CreateFlashAttentionBackwardKernel`](scaled_dot_product_attention/flash_attention_kernel_builder.cc.md#CreateFlashAttentionBackwardKernel), [`AtenSortValuesStable`](sort/sort_aten_kernels.cc.md#AtenSortValuesStable), [`HistcHelperOut`](histc/histc_aten_kernels.cc.md#HistcHelperOut), [`ArgMinMax`](min_max/min_max_aten_kernels.cc.md#ArgMinMax), [`UnaryMinMax`](min_max/min_max_aten_kernels.cc.md#UnaryMinMax), [`AtenDropoutCommonImpl`](dropout/dropout_aten_kernels.cc.md#AtenDropoutCommonImpl), [`LogSigmoidForward`](sigmoid/sigmoid_aten_kernels.cc.md#LogSigmoidForward), [`AdaptiveMaxPool2dHelper`](pooling/adaptive_max_pool_aten_kernels.cc.md#AdaptiveMaxPool2dHelper), [`CtcLossForwardInternal`](ctc_loss/ctc_loss_aten_kernels.cc.md#CtcLossForwardInternal), [`CtcLossPublicInternal`](ctc_loss/ctc_loss_aten_kernels.cc.md#CtcLossPublicInternal), [`CtcLossBackwardInternal`](ctc_loss/ctc_loss_aten_kernels.cc.md#CtcLossBackwardInternal), [`BuildAdaptiveMaxPool2dShlo`](pooling/adaptive_max_pool_aten_kernels.cc.md#BuildAdaptiveMaxPool2dShlo), [`BuildEmbeddingBagShlo`](embedding/embedding.cc.md#BuildEmbeddingBagShlo), [`AtenMinMaxDim`](min_max/min_max_aten_kernels.cc.md#AtenMinMaxDim), [`ConvolutionBackward`](convolution/convolution_aten_kernels.cc.md#ConvolutionBackward), [`BuildBatchNormBackward`](native_batch_norm/native_batch_norm.cc.md#BuildBatchNormBackward), [`BuildMaxPoolWithIndicesOutNd`](pooling/max_pool_aten_kernels.cc.md#BuildMaxPoolWithIndicesOutNd), [`TpuBatchNormBackward`](native_batch_norm/native_batch_norm_aten_kernels.cc.md#TpuBatchNormBackward), [`ScaledDotProductFusedAttentionShlo`](scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc.md#ScaledDotProductFusedAttentionShlo), [`ToMlirOpBuilder`](op_builder_utils.h.md#ToMlirOpBuilder), [`MaskedSoftmaxBackwardInternalOut`](softmax/_masked_softmax_aten_kernels.cc.md#MaskedSoftmaxBackwardInternalOut), [`Svd`](linalg/linalg_svd_kernels.cc.md#Svd), [`BuildScaledDotProductFusedAttentionShloOp`](scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc.md#BuildScaledDotProductFusedAttentionShloOp), [`BuildQdwhLoopBody`](linalg/linalg_svd_kernels.cc.md#BuildQdwhLoopBody), [`BuildQrShlo`](linalg/qr/qr_lib.cc.md#BuildQrShlo), [`DispatchUnaryMinMax`](min_max/min_max_aten_kernels.cc.md#DispatchUnaryMinMax)  (+62 more)

### <a id="MlirOpResultsTraits"></a>`MlirOpResultsTraits`
- def: [`csrc/ops/op_builder_utils.h:131`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L131)
- doc: Traits for defining MlirOpResults.
- signature: `template <int kNumOutputs> struct MlirOpResultsTraits`
- uses (calls/refs, reference-scoped): [`kDynamicSize`](op_builder_utils.h.md#kDynamicSize), [`MlirOpResultsTraits`](op_builder_utils.h.md#MlirOpResultsTraits), [`kDynamicSize`](op_builder_utils.h.md#kDynamicSize)
- used by: [`MlirOpResults`](op_builder_utils.h.md#MlirOpResults)

### <a id="MlirOpResultsTraits.type"></a>`MlirOpResultsTraits.type`
- def: [`csrc/ops/op_builder_utils.h:133`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L133)
- signature: `using type = std::array<mlir::MlirOp, kNumOutputs>`
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="MlirTernaryOpBuilder"></a>`MlirTernaryOpBuilder`
- def: [`csrc/ops/op_builder_utils.h:739`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L739)
- doc: An op builder with three inputs and one result.
- signature: `using MlirTernaryOpBuilder = absl::AnyInvocable<absl::StatusOr<mlir::MlirOp>(mlir::MlirOp, mlir::MlirOp, mlir::MlirOp) const>`
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BinaryOpOut`](binary_aten_kernels.h.md#BinaryOpOut), [`TernaryOpOut`](binary_aten_kernels.cc.md#TernaryOpOut), [`DispatchTernaryOp`](binary_aten_kernels.cc.md#DispatchTernaryOp)

### <a id="MlirUnaryOpBuilder"></a>`MlirUnaryOpBuilder`
- def: [`csrc/ops/op_builder_utils.h:731`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L731)
- doc: An op builder with one input and one result, for example torch.abs().
- signature: `using MlirUnaryOpBuilder = absl::AnyInvocable<absl::StatusOr<mlir::MlirOp>(mlir::MlirOp input) const>`
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`UnaryOpOut`](unary_aten_kernels.cc.md#UnaryOpOut), [`AtenBinCount`](bincount/bincount_aten_kernels.cc.md#AtenBinCount), [`AtenAcosOut`](unary_aten_kernels.cc.md#AtenAcosOut), [`AtenAcoshOut`](unary_aten_kernels.cc.md#AtenAcoshOut), [`AtenAsinOut`](unary_aten_kernels.cc.md#AtenAsinOut), [`AtenAsinhOut`](unary_aten_kernels.cc.md#AtenAsinhOut), [`AtenAtanOut`](unary_aten_kernels.cc.md#AtenAtanOut), [`AtenAtanhOut`](unary_aten_kernels.cc.md#AtenAtanhOut), [`AtenCosOut`](unary_aten_kernels.cc.md#AtenCosOut), [`AtenCoshOut`](unary_aten_kernels.cc.md#AtenCoshOut), [`AtenExp2Out`](unary_aten_kernels.cc.md#AtenExp2Out), [`AtenExpOut`](unary_aten_kernels.cc.md#AtenExpOut), [`AtenExpm1Out`](unary_aten_kernels.cc.md#AtenExpm1Out), [`AtenLgammaOut`](unary_aten_kernels.cc.md#AtenLgammaOut), [`AtenLog10Out`](unary_aten_kernels.cc.md#AtenLog10Out), [`AtenLog1pOut`](unary_aten_kernels.cc.md#AtenLog1pOut), [`AtenLog2Out`](unary_aten_kernels.cc.md#AtenLog2Out), [`AtenLogOut`](unary_aten_kernels.cc.md#AtenLogOut), [`AtenReciprocalOut`](unary_aten_kernels.cc.md#AtenReciprocalOut), [`AtenRsqrtOut`](unary_aten_kernels.cc.md#AtenRsqrtOut), [`AtenSinOut`](unary_aten_kernels.cc.md#AtenSinOut), [`AtenSinhOut`](unary_aten_kernels.cc.md#AtenSinhOut), [`AtenSqrtOut`](unary_aten_kernels.cc.md#AtenSqrtOut), [`AtenTanOut`](unary_aten_kernels.cc.md#AtenTanOut), [`AtenTanhOut`](unary_aten_kernels.cc.md#AtenTanhOut), [`AtenCountNonzeroDimIntList`](count_nonzero/count_nonzero_aten_kernels.cc.md#AtenCountNonzeroDimIntList), [`UnaryOp`](unary_aten_kernels.cc.md#UnaryOp), [`UnaryOpInPlace`](unary_aten_kernels.cc.md#UnaryOpInPlace), [`LogicalUnaryOutImpl`](logical/logical_aten_kernels.cc.md#LogicalUnaryOutImpl), [`UnaryOpInPlace`](unary_aten_kernels.cc.md#UnaryOpInPlace), [`UnaryOpOut`](unary_aten_kernels.cc.md#UnaryOpOut), [`allow_out_dtype_cast`](unary_aten_kernels.h.md#UnaryOpOptions.allow_out_dtype_cast), [`UnaryOp`](unary_aten_kernels.cc.md#UnaryOp), [`GetAllBuilder`](all_any/all_any_aten_kernels.cc.md#GetAllBuilder)

### `NAryMlirOpBuilder`
- def: [`csrc/ops/op_builder_utils.h:684`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L684)
- doc: An op builder whose number of inputs (the arity) is known at compile time.
- signature: `template <int kArity, int kNumOutputs = 1> using NAryMlirOpBuilder = internal::NAryMlirOpBuilderTraits<kArity, kNumOutputs>::type`

### <a id="NAryMlirOpBuilderTraits"></a>`NAryMlirOpBuilderTraits`
- def: [`csrc/ops/op_builder_utils.h:643`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L643)
- doc: The primary template is for the case of kArity >= 2.
- signature: `template <int kArity, int kNumOutputs> struct NAryMlirOpBuilderTraits`
- uses (calls/refs, reference-scoped): [`kDynamicSize`](op_builder_utils.h.md#kDynamicSize), [`kDynamicSize`](op_builder_utils.h.md#kDynamicSize)
- used by: [`NAryMlirOpBuilder`](op_builder_utils.h.md#NAryMlirOpBuilder)

### <a id="NAryMlirOpBuilderTraits.type"></a>`NAryMlirOpBuilderTraits.type`
- def: [`csrc/ops/op_builder_utils.h:644`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L644)
- signature: `using type = absl::AnyInvocable<absl::StatusOr<MlirOpResults<kNumOutputs>>(FixedSizeSpan<mlir::MlirOp, kArity> inputs) const>`
- uses (calls/refs, reference-scoped): [`FixedSizeSpan`](../common/fixed_size_span.h.md#FixedSizeSpan), [`MlirOpResults`](op_builder_utils.h.md#MlirOpResults)

### <a id="ReshapeReassociation"></a>`ReshapeReassociation`
- def: [`csrc/ops/op_builder_utils.h:879`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L879)
- doc: Helper struct to hold reshape reassociation information.
- signature: `struct ReshapeReassociation`
- members:
  - <a id="ReshapeReassociation.reassociation"></a>`reassociation` — [`L881`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L881)
  - `reassociation` — [`L881`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L881)
  - <a id="ReshapeReassociation.type"></a>`type` — [`L880`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L880)
  - `type` — [`L880`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L880)
- uses (calls/refs, reference-scoped): [`Dimensions`](../common/dimension_types.h.md#Dimensions), [`ReshapeFromStaticDimensions`](op_builder_utils.cc.md#ReshapeFromStaticDimensions), [`ReassociationToString`](op_builder_utils.cc.md#ReassociationToString), [`ReshapeToStaticDimensions`](op_builder_utils.cc.md#ReshapeToStaticDimensions), [`GetReshapeReassociation`](op_builder_utils.cc.md#GetReshapeReassociation), [`GetReshapeReassociation`](op_builder_utils.cc.md#GetReshapeReassociation), [`ReshapeToStaticDimensions`](op_builder_utils.cc.md#ReshapeToStaticDimensions), [`ReshapeType`](op_builder_utils.h.md#ReshapeType), [`ReshapeFromStaticDimensions`](op_builder_utils.cc.md#ReshapeFromStaticDimensions), [`ReshapeReassociation`](op_builder_utils.h.md#ReshapeReassociation), [`ReshapeType`](op_builder_utils.h.md#ReshapeType)
- used by: [`ReshapeFromStaticDimensions`](op_builder_utils.cc.md#ReshapeFromStaticDimensions), [`ReassociationToString`](op_builder_utils.cc.md#ReassociationToString), [`GetReshapeReassociation`](op_builder_utils.cc.md#GetReshapeReassociation), [`operator()`](view_decomposition/view_sequence.cc.md#ViewCacheKeyVisitor.operator), [`HandleExpandReshape`](op_builder_utils.cc.md#HandleExpandReshape), [`GetReshapeType`](op_builder_utils.cc.md#GetReshapeType), [`HandleCollapseReshape`](op_builder_utils.cc.md#HandleCollapseReshape)

### `ReshapeType`
- def: [`csrc/ops/op_builder_utils.h:860`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L860)
- doc: The type of reshape operation, currently only handling reshapes that can be
- signature: `enum class ReshapeType`
- members:
  - <a id="ReshapeType.kCollapse"></a>`kCollapse` — [`L861`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L861)
  - `kCollapse` — [`L861`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L861)
  - `kExpand` — [`L863`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L863)
  - <a id="ReshapeType.kExpand"></a>`kExpand` — [`L863`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L863)
  - `kFlatten` — [`L862`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L862)
  - <a id="ReshapeType.kFlatten"></a>`kFlatten` — [`L862`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L862)
  - `kTransposeLike` — [`L864`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L864)
  - <a id="ReshapeType.kTransposeLike"></a>`kTransposeLike` — [`L864`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L864)
  - `kUnknown` — [`L865`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L865)
  - <a id="ReshapeType.kUnknown"></a>`kUnknown` — [`L865`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L865)
- used by: [`ReshapeFromStaticDimensions`](op_builder_utils.cc.md#ReshapeFromStaticDimensions), [`GetReshapeReassociation`](op_builder_utils.cc.md#GetReshapeReassociation), [`operator()`](view_decomposition/view_sequence.cc.md#ViewCacheKeyVisitor.operator), [`GetReshapeType`](op_builder_utils.cc.md#GetReshapeType), [`ReshapeTypeToString`](op_builder_utils.cc.md#ReshapeTypeToString), [`ReshapeReassociation`](op_builder_utils.h.md#ReshapeReassociation)

### <a id="RngBitGeneratorResults"></a>`RngBitGeneratorResults`
- def: [`csrc/ops/op_builder_utils.h:422`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L422)
- signature: `struct RngBitGeneratorResults`
- members:
  - `output` — [`L424`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L424)
  - <a id="RngBitGeneratorResults.output"></a>`output` — [`L424`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L424)
  - <a id="RngBitGeneratorResults.output_state"></a>`output_state` — [`L423`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L423)
  - `output_state` — [`L423`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L423)
- uses (calls/refs, reference-scoped): [`RngBitGeneratorResults`](op_builder_utils.h.md#RngBitGeneratorResults)

## Functions
- `ApplyBroadcastIfNeeded(Op1 op1, Op2 op2, Ops... ops)` — [`L586`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L586) — This overload takes a variable number (>= 2) of inputs, where each input is
- <a id="ApplyBroadcastIfNeeded"></a>`ApplyBroadcastIfNeeded(std::array<mlir::MlirOp, kNumInputs> ops)` — [`L554`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L554) — This overload takes a fixed number of inputs as an std::array, and returns
- <a id="AsArrayRef"></a>`AsArrayRef(absl::Span<const T> span)` — [`L171`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L171) — Convert from absl::Span to mlir::ArrayRef for interop with MLIR builder
- `GetDims(const at::IntArrayRef dims)` — [`L79`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L79)
- `GetDims(const at::Tensor& tensor)` — [`L73`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L73) — Extracts the dimensions from a Tensor or IntArrayRef.
- `GetDims(const at::IntArrayRef dims)` — [`L79`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L79)
- <a id="GetDims"></a>`GetDims(const at::Tensor& tensor)` — [`L73`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L73) — Extracts the dimensions from a Tensor or IntArrayRef.
- `GetDims(const at::Scalar& scalar)` — [`L76`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L76)
- `GetDims(const at::Scalar& scalar)` — [`L76`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L76)
- `GetDims(const at::IntArrayRef dims)` — [`L79`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L79)
- `GetDims(const at::Tensor& tensor)` — [`L73`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L73) — Extracts the dimensions from a Tensor or IntArrayRef.
- `InferSize(const Dims&... dims)` — [`L108`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L108) — Computes a mutually broadcastable shape for by applying Numpy's broadcasting
- <a id="InferSize"></a>`InferSize(const Dims&... dims)` — [`L108`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L108) — Computes a mutually broadcastable shape for by applying Numpy's broadcasting
- `InferSize(const Dims&... dims)` — [`L108`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L108) — Computes a mutually broadcastable shape for by applying Numpy's broadcasting
- <a id="InferSizeImpl"></a>`InferSizeImpl(const Dims1& a, const Dims2& b, const Dims3& c, const Dims&... rest)` — [`L93`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L93) — The recursive case:
- `InferSizeImpl(const Dims1& a, const Dims2& b)` — [`L87`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L87) — The base case:
- `InferSizeImpl(const Dims1& a, const Dims2& b, const Dims3& c, const Dims&... rest)` — [`L93`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L93) — The recursive case:
- `InferSizeImpl(const Dims1& a, const Dims2& b)` — [`L87`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L87) — The base case:
- <a id="IsBooleanType"></a>`IsBooleanType(mlir::RankedTensorType tensor_type)` — [`L208`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L208)
- `IsBooleanType(mlir::RankedTensorType tensor_type)` — [`L208`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L208)
- `IsComplexType(mlir::RankedTensorType tensor_type)` — [`L221`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L221)
- <a id="IsComplexType"></a>`IsComplexType(mlir::RankedTensorType tensor_type)` — [`L221`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L221)
- <a id="IsFloatType"></a>`IsFloatType(mlir::RankedTensorType tensor_type)` — [`L217`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L217)
- `IsFloatType(mlir::RankedTensorType tensor_type)` — [`L217`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L217)
- <a id="IsUnsignedType"></a>`IsUnsignedType(mlir::RankedTensorType tensor_type)` — [`L213`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L213)
- `IsUnsignedType(mlir::RankedTensorType tensor_type)` — [`L213`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L213)
- `MakeConstant` — [`L289`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L289) — PyTorch Specific constant builders.
- `MakeConstant(mlir::MlirBuilder& builder, T value, mlir::RankedTensorType tensor_type)` — [`L300`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L300) — Creates a constant with the tensor shape and element type.
- `MakeConstant` — [`L289`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L289) — PyTorch Specific constant builders.
- `MakeConstant(mlir::MlirBuilder& builder, T value, mlir::RankedTensorType tensor_type)` — [`L300`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L300) — Creates a constant with the tensor shape and element type.
- `MakeConstant(mlir::MlirBuilder& builder, T value, mlir::Type element_type, mlir::ArrayRef<int64_t> shape)` — [`L310`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L310) — Creates a constant with the given shape and element type.
- <a id="MakeConstant"></a>`MakeConstant(mlir::MlirBuilder& builder, T value, mlir::Type element_type, mlir::ArrayRef<int64_t> shape)` — [`L310`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L310) — Creates a constant with the given shape and element type. — documented in [stablehlo-op-builder](../../../concepts/stablehlo-op-builder.md)
- `MakeConstant(mlir::MlirBuilder& builder, T value, mlir::ElementType element_type, mlir::ArrayRef<int64_t> shape)` — [`L325`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L325) — Creates a constant with the given shape and element type.
- `MakeConstant` — [`L289`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L289)
- `MakeConstant(mlir::MlirBuilder& builder, T value, mlir::ElementType element_type, mlir::ArrayRef<int64_t> shape)` — [`L325`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L325) — Creates a constant with the given shape and element type.
- `MakeConstantLike(mlir::MlirOp input, T val, std::optional<mlir::ElementType> element_type = std::nullopt)` — [`L387`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L387)
- `MakeConstantLike(mlir::MlirOp input, T val, std::optional<mlir::Type> element_type)` — [`L366`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L366) — Creates a constant with the same shape as the input tensor.
- <a id="MakeConstantLike"></a>`MakeConstantLike(mlir::MlirOp input, T val, std::optional<mlir::Type> element_type)` — [`L366`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L366) — Creates a constant with the same shape as the input tensor. — documented in [stablehlo-op-builder](../../../concepts/stablehlo-op-builder.md)
- `MakeScalarConstant(mlir::MlirBuilder& builder, T value, mlir::Type element_type)` — [`L338`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L338) — Creates a constant with a scalar shape of the given element type.
- <a id="MakeScalarConstant"></a>`MakeScalarConstant(mlir::MlirBuilder& builder, T value, mlir::Type element_type)` — [`L338`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L338) — Creates a constant with a scalar shape of the given element type. — documented in [dynamic-shape-ops](../../../concepts/dynamic-shape-ops.md)
- `MakeScalarConstant(mlir::MlirBuilder& builder, T value, mlir::ElementType element_type)` — [`L348`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L348)
- `MakeScalarConstant(mlir::MlirBuilder& builder, T value, mlir::ElementType element_type)` — [`L348`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L348)
- `ToMlirOpBuilder(NAryMlirOpBuilder<kArity, kNumOutputs> op_builder)` — [`L690`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L690) — Converts an NAryMlirOpBuilder to an MlirOpBuilder, checking that the number
- `ToMlirOpBuilder(NAryMlirOpBuilder<kArity, kNumOutputs> op_builder)` — [`L690`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L690) — Converts an NAryMlirOpBuilder to an MlirOpBuilder, checking that the number
- <a id="ToMlirOpBuilder"></a>`ToMlirOpBuilder(NAryMlirOpBuilder<kArity, kNumOutputs> op_builder)` — [`L690`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L690) — Converts an NAryMlirOpBuilder to an MlirOpBuilder, checking that the number
- <a id="ToResultVector"></a>`ToResultVector(absl::StatusOr<std::array<mlir::MlirOp, kNumOps>> results)` — [`L750`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L750) — Converts an op that returns a tuple of outputs into a vector of outputs.
- `ToResultVector(absl::StatusOr<std::array<mlir::MlirOp, kNumOps>> results)` — [`L750`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L750) — Converts an op that returns a tuple of outputs into a vector of outputs.
- `ToResultVector(absl::StatusOr<std::array<mlir::MlirOp, kNumOps>> results)` — [`L750`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L750) — Converts an op that returns a tuple of outputs into a vector of outputs.

## Module values
- <a id="AnnotateBufferDonations"></a>`AnnotateBufferDonations` — [`L784`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L784) — Given a module name with a `main` function, annotates the donated inputs,
- `AsArrayRef` — [`L171`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L171) — Convert from absl::Span to mlir::ArrayRef for interop with MLIR builder
- <a id="Broadcast"></a>`Broadcast` — [`L595`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L595)
- <a id="BroadcastIfNeeded"></a>`BroadcastIfNeeded` — [`L499`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L499) — documented in [stablehlo-op-builder](../../../concepts/stablehlo-op-builder.md)
- <a id="BuildFillUninitialized"></a>`BuildFillUninitialized` — [`L805`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L805) — Creates a fill value used to represent "uninitialized memory".
- <a id="MakeZeroSizedTensor"></a>`MakeZeroSizedTensor` — [`L276`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L276) — Returns a tensor of shape `shape` with zero elements and the given element
- <a id="RngBitGeneratorLike"></a>`RngBitGeneratorLike` — [`L442`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L442) — Generates random bits with static or bounded dynamic shapes.
- <a id="Squeeze"></a>`Squeeze` — [`L541`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L541) — Squeezes the input tensor by removing dimensions of size 1.
- `ToResultVector` — [`L750`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L750) — Converts an op that returns a tuple of outputs into a vector of outputs.
- `kDynamicSize` — [`L124`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L124) — Sentinel value for the number of inputs/outputs when it is not known at
- <a id="kDynamicSize"></a>`kDynamicSize` — [`L124`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.h#L124) — Sentinel value for the number of inputs/outputs when it is not known at

