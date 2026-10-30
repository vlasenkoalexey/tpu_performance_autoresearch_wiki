---
title: 'Module: csrc/ops/scan_builder.h'
type: catalog
provenance: extracted
module: csrc/ops/scan_builder.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ScanDirection: ScanDirection#
  ScanDirection.kForward: ScanDirection#kForward.
  ScanBodyResults: ScanBodyResults#
  MultiInputScanBodyBuilder: MultiInputScanBodyBuilder#
  ScanOptions: ScanOptions#
  ScanBodyBuilder: ScanBodyBuilder#
  ScanBodyResults.new_carries: ScanBodyResults#new_carries.
  ScanDirection.kReverse: ScanDirection#kReverse.
  ScanOptions.direction: ScanOptions#direction.
  ScanBodyResults.new_outputs: ScanBodyResults#new_outputs.
  ScanOptions.is_associative: ScanOptions#is_associative.
  EncodeParamCacheKey: EncodeParamCacheKey(cbedb086fa928b96).
  ScanOptions.should_squeeze: ScanOptions#should_squeeze.
---
# Module: [`csrc/ops/scan_builder.h`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.h)

## Classes
### <a id="MultiInputScanBodyBuilder"></a>`MultiInputScanBodyBuilder`
- def: [`csrc/ops/scan_builder.h:79`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.h#L79)
- doc: (op_builder, loc, input_slices, index_0d, carries) -> (new_carries,
- signature: `using MultiInputScanBodyBuilder = absl::AnyInvocable<absl::StatusOr<ScanBodyResults>(mlir::OpBuilder&, mlir::Location, mlir::ValueRange, mlir::Value, mlir::ValueRange) const>`
- uses (calls/refs, reference-scoped): [`DynamicMlirOpResults`](op_builder_utils.h.md#DynamicMlirOpResults), [`BuildScanShlo`](scan_builder.cc.md#BuildScanShlo), [`CreateRankReducedConstantLike`](scan_builder.cc.md#CreateRankReducedConstantLike), [`ScanBodyResults`](scan_builder.h.md#ScanBodyResults), [`ScanOptions`](scan_builder.h.md#ScanOptions), [`BuildScanShlo`](scan_builder.cc.md#BuildScanShlo)
- used by: [`BuildScanShlo`](scan_builder.cc.md#BuildScanShlo), [`BuildScanShlo`](scan_builder.cc.md#BuildScanShlo), [`BuildAssociativeScanChlo`](scan_builder.cc.md#BuildAssociativeScanChlo), [`PopulateScanBody`](scan_builder.cc.md#PopulateScanBody), [`BuildCumsumShlo`](cumsum/cumsum.cc.md#BuildCumsumShlo), [`BuildCummaxShlo`](cummax/cummax.cc.md#BuildCummaxShlo), [`BuildCumminShlo`](cummin/cummin.cc.md#BuildCumminShlo), [`BuildCumprodShlo`](cumprod/cumprod.cc.md#BuildCumprodShlo), [`EmitSliceInitScan`](../internal/compile/dispatch_scan.cc.md#EmitSliceInitScan), [`Scan`](scan_builder_test.cc.md#ScanBuilderTest.Scan), [`CreateAddBodyBuilder`](scan_builder_test.cc.md#ScanBuilderTest.CreateAddBodyBuilder), [`EmitIdentityInitChloScan`](../internal/compile/dispatch_scan.cc.md#EmitIdentityInitChloScan), [`CreateMultiAddBodyBuilder`](scan_builder_test.cc.md#ScanBuilderTest.CreateMultiAddBodyBuilder)

### <a id="ScanBodyBuilder"></a>`ScanBodyBuilder`
- def: [`csrc/ops/scan_builder.h:58`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.h#L58)
- doc: (op_builder, loc, input_slice, index_0d, carries) -> new_carries.
- signature: `using ScanBodyBuilder = absl::AnyInvocable<absl::StatusOr<llvm::SmallVector<mlir::Value>>(mlir::OpBuilder&, mlir::Location, mlir::Value, mlir::Value, mlir::ValueRange) const>`
- uses (calls/refs, reference-scoped): [`DynamicMlirOpResults`](op_builder_utils.h.md#DynamicMlirOpResults), [`BuildScanShlo`](scan_builder.cc.md#BuildScanShlo), [`ScanOptions`](scan_builder.h.md#ScanOptions), [`BuildScanShlo`](scan_builder.cc.md#BuildScanShlo)
- used by: [`BuildScanShlo`](scan_builder.cc.md#BuildScanShlo), [`Scan`](scan_builder_test.cc.md#ScanBuilderTest.Scan), [`CreateBoundedTensorArg`](scan_builder_test.cc.md#ScanBuilderTest.CreateBoundedTensorArg)

### <a id="ScanBodyResults"></a>`ScanBodyResults`
- def: [`csrc/ops/scan_builder.h:72`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.h#L72)
- signature: `struct ScanBodyResults`
- members:
  - <a id="ScanBodyResults.new_carries"></a>`new_carries` — [`L73`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.h#L73)
  - <a id="ScanBodyResults.new_outputs"></a>`new_outputs` — [`L74`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.h#L74)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`PyCreateScanOp`](../internal/compile/dispatch_scan.cc.md#PyCreateScanOp), [`BuildScanShlo`](scan_builder.cc.md#BuildScanShlo), [`BuildAssociativeScan`](../internal/compile/dispatch_scan.cc.md#BuildAssociativeScan), [`BuildAssociativeScanChlo`](scan_builder.cc.md#BuildAssociativeScanChlo), [`PopulateScanBody`](scan_builder.cc.md#PopulateScanBody), [`BuildCumsumShlo`](cumsum/cumsum.cc.md#BuildCumsumShlo), [`TestBody`](scan_builder_test.cc.md#MultiScanBuilderTest_BodyBuilderError_Test.TestBody), [`BuildCummaxShlo`](cummax/cummax.cc.md#BuildCummaxShlo), [`BuildCumminShlo`](cummin/cummin.cc.md#BuildCumminShlo), [`BuildCumprodShlo`](cumprod/cumprod.cc.md#BuildCumprodShlo), [`CreateAddBodyBuilder`](scan_builder_test.cc.md#ScanBuilderTest.CreateAddBodyBuilder), [`MultiInputScanBodyBuilder`](scan_builder.h.md#MultiInputScanBodyBuilder), [`TestBody`](scan_builder_test.cc.md#MultiScanBuilderTest_MismatchedCarriesError_Test.TestBody), [`TestBody`](scan_builder_test.cc.md#MultiScanBuilderTest_MismatchedOutputsError_Test.TestBody), [`TestBody`](scan_builder_test.cc.md#MultiScanBuilderTest_WithStaticInput_Test.TestBody), [`ImportStepFunctionCallees`](../internal/compile/dispatch_scan.cc.md#ImportStepFunctionCallees), [`TestBody`](scan_builder_test.cc.md#MultiScanBuilderTest_MismatchedInitsAllowed_Test.TestBody), [`BuildAssociativeLoopBody`](../internal/compile/dispatch_scan.cc.md#BuildAssociativeLoopBody), [`CreateMultiAddBodyBuilder`](scan_builder_test.cc.md#ScanBuilderTest.CreateMultiAddBodyBuilder), [`CreateIdentityBodyBuilder`](scan_builder_test.cc.md#ScanBuilderTest.CreateIdentityBodyBuilder), [`BuildLoopBody`](../internal/compile/dispatch_scan.cc.md#BuildLoopBody), [`LogaddexpScanBody`](logcumsumexp/logcumsumexp_aten_kernels.cc.md#LogaddexpScanBody)

### <a id="ScanDirection"></a>`ScanDirection`
- def: [`csrc/ops/scan_builder.h:37`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.h#L37)
- signature: `enum class ScanDirection`
- members:
  - <a id="ScanDirection.kForward"></a>`kForward` — [`L37`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.h#L37)
  - <a id="ScanDirection.kReverse"></a>`kReverse` — [`L37`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.h#L37)
- used by: [`TorchTpuPyBindInitModule_tpu_torch_compile`](../internal/compile/tpu_torch_compile.cc.md#TorchTpuPyBindInitModule_tpu_torch_compile), [`PyCreateAssociativeScanOp`](../internal/compile/dispatch_scan.cc.md#PyCreateAssociativeScanOp), [`PyCreateScanOp`](../internal/compile/dispatch_scan.cc.md#PyCreateScanOp), [`BuildScanShlo`](scan_builder.cc.md#BuildScanShlo), [`BuildAssociativeScan`](../internal/compile/dispatch_scan.cc.md#BuildAssociativeScan), [`BuildAssociativeScanChlo`](scan_builder.cc.md#BuildAssociativeScanChlo), [`PopulateScanBody`](scan_builder.cc.md#PopulateScanBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_DtypeMismatchError_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_AssociativeScanUnwrapsMovedimView_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_AssociativeScanInfersIdentityAndEmitsChloScan_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_MismatchedInputsDuringLowering_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_With2D_Test.TestBody), [`TestBody`](scan_builder_test.cc.md#MultiScanBuilderTest_ReverseScan_Test.TestBody), [`EmitSliceInitScan`](../internal/compile/dispatch_scan.cc.md#EmitSliceInitScan), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_VerifyCacheKeys_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_With1D_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanNumScanInputsTest_InvalidNumScanInputs_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_AssociativeScanErrorValidation_Test.TestBody), [`EmitIdentityInitChloScan`](../internal/compile/dispatch_scan.cc.md#EmitIdentityInitChloScan), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_AssociativeScanTier2SliceInitFallback_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_InvalidMlirModuleError_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_AssociativeScanBitwiseAndUsesSliceInit_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_AssociativeScanHighRankScansOriginalDim_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_AssociativeScanMambaSsmTupleInfersIdentity_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_AssociativeScanSeqLenOneShortCircuits_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_AssociativeScanTier2WhileFallbackWithConstants_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_AssociativeScanWithStaticInputsUsesWhile_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_CpuTensorInputsError_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_MismatchedDummyOutputsError_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_TooFewResultsError_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_EmptyInputsError_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_MissingMainError_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_NestedStepFunctionCalleesAreImported_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_StepFunctionCalleeIsImported_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_WithMultiCarries_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_WithMultiScannedInputs_Test.TestBody), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_WithStaticInputs_Test.TestBody), [`ScanOptions`](scan_builder.h.md#ScanOptions), [`TestBody`](../internal/compile/dispatch_scan_test.cc.md#DispatchScanTest_WithReverse_Test.TestBody), [`direction`](scan_builder.h.md#ScanOptions.direction)  (+1 more)

### <a id="ScanOptions"></a>`ScanOptions`
- def: [`csrc/ops/scan_builder.h:44`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.h#L44)
- signature: `struct ScanOptions`
- members:
  - <a id="ScanOptions.direction"></a>`direction` — [`L45`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.h#L45)
  - <a id="ScanOptions.is_associative"></a>`is_associative` — [`L55`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.h#L55) — When true, the scan body is asserted to be associative and the scan is
  - <a id="ScanOptions.should_squeeze"></a>`should_squeeze` — [`L46`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.h#L46)
- uses (calls/refs, reference-scoped): [`ScanDirection`](scan_builder.h.md#ScanDirection), [`kForward`](scan_builder.h.md#ScanDirection.kForward)
- used by: [`PyCreateScanOp`](../internal/compile/dispatch_scan.cc.md#PyCreateScanOp), [`BuildScanShlo`](scan_builder.cc.md#BuildScanShlo), [`BuildScanShlo`](scan_builder.cc.md#BuildScanShlo), [`BuildAssociativeScan`](../internal/compile/dispatch_scan.cc.md#BuildAssociativeScan), [`BuildAssociativeScanChlo`](scan_builder.cc.md#BuildAssociativeScanChlo), [`BuildCumsumShlo`](cumsum/cumsum.cc.md#BuildCumsumShlo), [`BuildCummaxShlo`](cummax/cummax.cc.md#BuildCummaxShlo), [`BuildCumminShlo`](cummin/cummin.cc.md#BuildCumminShlo), [`BuildCumprodShlo`](cumprod/cumprod.cc.md#BuildCumprodShlo), [`TestBody`](scan_builder_test.cc.md#MultiScanBuilderTest_ReverseScan_Test.TestBody), [`EmitSliceInitScan`](../internal/compile/dispatch_scan.cc.md#EmitSliceInitScan), [`Scan`](scan_builder_test.cc.md#ScanBuilderTest.Scan), [`BuildLogcumsumexpShlo`](logcumsumexp/logcumsumexp_aten_kernels.cc.md#BuildLogcumsumexpShlo), [`MultiInputScanBodyBuilder`](scan_builder.h.md#MultiInputScanBodyBuilder), [`TestBody`](scan_builder_test.cc.md#MultiScanBuilderTest_Squeeze1DTo0DTensor_Test.TestBody), [`TestBody`](scan_builder_test.cc.md#MultiScanBuilderTest_SqueezeScan_Test.TestBody), [`Scan`](scan_builder_test.cc.md#ScanBuilderTest.Scan), [`EmitIdentityInitChloScan`](../internal/compile/dispatch_scan.cc.md#EmitIdentityInitChloScan), [`ScanBodyBuilder`](scan_builder.h.md#ScanBodyBuilder)

## Functions
- <a id="EncodeParamCacheKey"></a>`EncodeParamCacheKey(const ScanDirection value)` — [`L39`](../../../../../../raw/code/torch_tpu/csrc/ops/scan_builder.h#L39)

