---
title: 'Module: csrc/ops/op_builder_utils.cc'
type: catalog
provenance: extracted
module: csrc/ops/op_builder_utils.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  GetTensorTypeOrDie: GetTensorTypeOrDie(681e170f239ceca).
  CastIfNeeded: CastIfNeeded(c116150205aa322e).
  BroadcastIfNeeded: BroadcastIfNeeded(575d3b68656e7de8).
  MakeConstantLike: MakeConstantLike(419709da9f034888).
  Unsqueeze: Unsqueeze(32e5625f5d56765e).
  GetElementTypeOrDie: GetElementTypeOrDie(7d352280f1e9d90d).
  ReshapeFromStaticDimensions: ReshapeFromStaticDimensions(a9460c21bd6db68a).
  Broadcast: Broadcast(b3db5755db798e27).
  MakeZeroSizedTensor: MakeZeroSizedTensor(db491ac008496e15).
  ConvertIfInteger: ConvertIfInteger(c116150205aa322e).
  Squeeze: Squeeze(6696ef0d66c99f43).
  Iota: Iota(4175f2d8feeca5f8).
  PromoteFloatDtype: PromoteFloatDtype(c116150205aa322e).
  MakeConstant: MakeConstant(a0abc813c0c259b2).
  GetElementType: GetElementType(c57d1ce196dfc5e8).
  GetDimensions: GetDimensions(7d0d7c845c6a0f77).
  DebugString: DebugString(36f7f3c8911edb1d).
  BuildMaybeSlice: BuildMaybeSlice(56b54d9eb88162a7).
  Flatten: Flatten(cf97982c188f832c).
  GetMinFiniteValueAttr: GetMinFiniteValueAttr(b4a628fc4e3259e6).
  GetElementTypeOrSelf: GetElementTypeOrSelf(fd860f5e2eff5cab).
  GetAllDimensions: GetAllDimensions(6870108f518df996).
  ConvolutionLike: ConvolutionLike(8e1047356f4850eb).
  SerializePortableArtifact: SerializePortableArtifact(80803442a742f742).
  GetNumElements: GetNumElements(d40ef26ea4e60439).
  BuildReduceBody: BuildReduceBody(5070b11bb6ece266).
  GetMaxFiniteValueAttr: GetMaxFiniteValueAttr(b4a628fc4e3259e6).
  SerializeBytecode: SerializeBytecode(80803442a742f742).
  ConvertIfIntegers: ConvertIfIntegers(3cb2e1f4c40c29e).
  GetVerifiedMinFiniteValue: GetVerifiedMinFiniteValue(7b12563ba5988aa2).
  GetMlirType: GetMlirType(b223654b0022e378).
  BuildFillUninitialized: BuildFillUninitialized(9306c0e29cfed34c).
  SliceBatchDimensions: SliceBatchDimensions(e537c811d77f0d6c).
  ReassociationToString: ReassociationToString(f4558391dcccd1e9).
  GetNonzeroMask: GetNonzeroMask(cf97982c188f832c).
  BuildModuleNameFromPyContext: BuildModuleNameFromPyContext(95eed92666cb8fc8).
  GetStaticShape: GetStaticShape(6870108f518df996).
  BuildRngStateUpdateShlo: BuildRngStateUpdateShlo(1d9fc30246b9c9cd).
  GetModuleOp: GetModuleOp(38c4c50e336748f0).
  GetMaxFiniteDouble: GetMaxFiniteDouble(2d4bf6c2f5744195).
  GetBatchDimensions: GetBatchDimensions(22ee28c780cc82eb).
  AnnotateBufferDonations: AnnotateBufferDonations(38ed15182d0f8502).
  GetMinFiniteDouble: GetMinFiniteDouble(2d4bf6c2f5744195).
  ReshapeToStaticDimensions: ReshapeToStaticDimensions(8417f6002b1ef712).
  GetReshapeReassociation: GetReshapeReassociation(49155e22250c8b5c).
  ApplyBroadcastIfNeeded: ApplyBroadcastIfNeeded(a41d85da94c690fd).
  ToResultVector: ToResultVector(161e2b2ea61159aa).
  RngBitGeneratorLike: RngBitGeneratorLike(65d31b05ad949211).
  MakeConstantAttr: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/MakeConstantAttr(9abc0030f30ea225).'
  HandleExpandReshape: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/HandleExpandReshape(20019e080f2b389c).'
  ShapeTransitionToString: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/ShapeTransitionToString(a6df286996f7b5b1).'
  ValidateConvolutionBounds: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/ValidateConvolutionBounds(cb02108d7af13aed).'
  GetReshapeType: GetReshapeType(33cf24d335ee7327).
  ConvolutionResultSize: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/ConvolutionResultSize(cfd62af6320fff2a).'
  MakeStaticAtBounds: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/MakeStaticAtBounds(d7d62c269d68afab).'
  HandleCollapseReshape: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/HandleCollapseReshape(6b7987ef9abeba49).'
  HandleTransposeLikeReshape: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/HandleTransposeLikeReshape(fec1fbfef6a63c0f).'
  ZeroPastRuntimeSizes: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/ZeroPastRuntimeSizes(3d077bc631c78170).'
  ReshapeTypeToString: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/ReshapeTypeToString(757f8d6ff5a024a1).'
  InferStaticConvolutionResultShape: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/InferStaticConvolutionResultShape(2bcef12df50b8a99).'
  GetConvolutionWindows: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/GetConvolutionWindows(484972adede2ee8b).'
  BoundConvolutionResult: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/BoundConvolutionResult(4d5241cd6d4f56ea).'
  kSupportedBounds: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/kSupportedBounds.'
  GetReassociationIndicesForReshape: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/GetReassociationIndicesForReshape(f97fc88fd2389417).'
  ConvolutionWindow: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/ConvolutionWindow#'
  GetCoreShape: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/GetCoreShape(bba8512e0ebc0e78).'
  StaticAtBounds: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/StaticAtBounds#'
  StaticAtBounds.op: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/StaticAtBounds#op.'
  StaticAtBounds.runtime_sizes: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/StaticAtBounds#runtime_sizes.'
  HasBoundedDimension: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/HasBoundedDimension(807fba15d56270a7).'
  ConvolutionWindow.lhs_dilation: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/ConvolutionWindow#lhs_dilation.'
  ConvolutionWindow.stride: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/ConvolutionWindow#stride.'
  ConvolutionWindow.window_size: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/ConvolutionWindow#window_size.'
  BoundFromDimensions: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/BoundFromDimensions(21f9ff2917cccb26).'
  ConvolutionWindow.padding: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/ConvolutionWindow#padding.'
  ToStdComplex: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/ToStdComplex(a358fd9634d01384).'
  DilatedSize: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/DilatedSize(d0a0e4c270da0eca).'
  GetBasename: '`$anonymous_namespace_csrc/ops/op_builder_utils.cc`/GetBasename(6ccff4770ff7ddc3).'
---
# Module: [`csrc/ops/op_builder_utils.cc`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc)

## Classes
### <a id="ConvolutionWindow"></a>`ConvolutionWindow`
- def: [`csrc/ops/op_builder_utils.cc:123`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L123)
- doc: Window of a convolution spatial dimension.
- signature: `struct ConvolutionWindow`
- members:
  - <a id="ConvolutionWindow.lhs_dilation"></a>`lhs_dilation` — [`L124`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L124)
  - <a id="ConvolutionWindow.padding"></a>`padding` — [`L126`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L126) — Sum of the low and high padding.
  - <a id="ConvolutionWindow.stride"></a>`stride` — [`L129`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L129)
  - <a id="ConvolutionWindow.window_size"></a>`window_size` — [`L128`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L128) — Kernel size after rhs dilation.
- used by: [`ConvolutionLike`](op_builder_utils.cc.md#ConvolutionLike), [`ConvolutionResultSize`](op_builder_utils.cc.md#ConvolutionResultSize), [`ConvolutionResultSize`](op_builder_utils.cc.md#ConvolutionResultSize), [`ZeroPastRuntimeSizes`](op_builder_utils.cc.md#ZeroPastRuntimeSizes), [`InferStaticConvolutionResultShape`](op_builder_utils.cc.md#InferStaticConvolutionResultShape), [`BoundConvolutionResult`](op_builder_utils.cc.md#BoundConvolutionResult), [`GetConvolutionWindows`](op_builder_utils.cc.md#GetConvolutionWindows)

### <a id="StaticAtBounds"></a>`StaticAtBounds`
- def: [`csrc/ops/op_builder_utils.cc:174`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L174)
- doc: An operand made static at its upper bounds.
- signature: `struct StaticAtBounds`
- members:
  - <a id="StaticAtBounds.op"></a>`op` — [`L175`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L175)
  - <a id="StaticAtBounds.runtime_sizes"></a>`runtime_sizes` — [`L177`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L177) — Runtime size of each bounded dimension, nullopt for static dimensions.
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ConvolutionLike`](op_builder_utils.cc.md#ConvolutionLike), [`MakeStaticAtBounds`](op_builder_utils.cc.md#MakeStaticAtBounds)

## Functions
- <a id="AnnotateBufferDonations"></a>`AnnotateBufferDonations(mlir::ModuleOp module, mlir::ArrayRef<int64_t> donated_inputs)` — [`L1224`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1224) — Given a module name with a `main` function, annotates the donated inputs,
- `ApplyBroadcastIfNeeded(absl::Span<const mlir::MlirOp> ops)` — [`L970`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L970) — Applies Numpy's broadcasting rules to a dynamic span of ops, if needed.
- <a id="ApplyBroadcastIfNeeded"></a>`ApplyBroadcastIfNeeded(absl::Span<const mlir::MlirOp> ops)` — [`L970`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L970) — Applies Numpy's broadcasting rules to a dynamic span of ops, if needed.
- <a id="BoundConvolutionResult"></a>`BoundConvolutionResult(mlir::MlirOp result, const stablehlo::ConvDimensionNumbersAttr dimension_numbers, const mlir::ArrayRef<ConvolutionWindow> windows, const std::vector<std::optional<mlir::MlirOp>>& runtime_sizes)` — [`L308`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L308) — Bounds the dimensions of the static convolution `result` that depend on the
- `BoundConvolutionResult(mlir::MlirOp result, const stablehlo::ConvDimensionNumbersAttr dimension_numbers, const mlir::ArrayRef<ConvolutionWindow> windows, const std::vector<std::optional<mlir::MlirOp>>& runtime_sizes)` — [`L308`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L308) — Bounds the dimensions of the static convolution `result` that depend on the
- `BoundFromDimensions(mlir::MlirOp input, const stablehlo::Dimensions& dims)` — [`L209`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L209) — Bounds the dimensions of the static `input` that have a boundOp in `dims`.
- <a id="BoundFromDimensions"></a>`BoundFromDimensions(mlir::MlirOp input, const stablehlo::Dimensions& dims)` — [`L209`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L209) — Bounds the dimensions of the static `input` that have a boundOp in `dims`.
- <a id="Broadcast"></a>`Broadcast(mlir::MlirOp input, absl::Span<const int64_t> output_dims, absl::Span<const int64_t> bcast_dims)` — [`L1004`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1004)
- `BroadcastIfNeeded(mlir::MlirOp input, mlir::stablehlo::Dimensions shape, absl::Span<const int64_t> broadcast_dimensions)` — [`L926`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L926) — Returns a broadcasted version of the input tensor to the target shape.
- <a id="BroadcastIfNeeded"></a>`BroadcastIfNeeded(mlir::MlirOp input, mlir::MlirOp target, absl::Span<const int64_t> broadcast_dimensions)` — [`L946`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L946) — Broadcasts input to target shape, returning an error if the shapes are — documented in [stablehlo-op-builder](../../../concepts/stablehlo-op-builder.md)
- `BroadcastIfNeeded(mlir::MlirOp input, absl::Span<const int64_t> shape)` — [`L896`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L896)
- `BroadcastIfNeeded(mlir::MlirOp input, mlir::stablehlo::Dimensions shape, absl::Span<const int64_t> broadcast_dimensions)` — [`L926`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L926) — Returns a broadcasted version of the input tensor to the target shape.
- <a id="BuildFillUninitialized"></a>`BuildFillUninitialized(mlir::MlirBuilder& builder, mlir::ElementType tensor_element_type, absl::Span<const int64_t> shape)` — [`L1318`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1318) — Creates a fill value used to represent "uninitialized memory".
- <a id="BuildMaybeSlice"></a>`BuildMaybeSlice(mlir::MlirOp op, int64_t dimension, int64_t left_pad, int64_t right_pad)` — [`L1511`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1511) — Slice if left_pad or right_pad is negative to truncate the vector,
- <a id="BuildModuleNameFromPyContext"></a>`BuildModuleNameFromPyContext(mlir::MLIRContext& mlir_context, const PythonContext* absl_nullable python_context)` — [`L1175`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1175) — Builds a module name from the current Python stack frame.
- <a id="BuildReduceBody"></a>`BuildReduceBody(mlir::RegionBuilder& rb, mlir::Type element_type, c10d::ReduceOp::RedOpType reduce_op_type)` — [`L1272`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1272) — Generates the body of a reduce operation for a given reduce type.
- <a id="BuildRngStateUpdateShlo"></a>`BuildRngStateUpdateShlo(mlir::MlirOp state, int64_t num_elements, int64_t bit_width)` — [`L1606`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1606) — Builds an MLIR op that updates the RNG state (Philox offset) based on the
- <a id="CastIfNeeded"></a>`CastIfNeeded(mlir::MlirOp op, mlir::ElementType expected_output_type)` — [`L1243`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1243) — Casts a given op to the expected type if necessary, preserving the values. — documented in [dynamic-shape-ops](../../../concepts/dynamic-shape-ops.md)
- <a id="ConvertIfInteger"></a>`ConvertIfInteger(mlir::MlirOp op, mlir::ElementType target_dtype)` — [`L1111`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1111) — Conditionally converts the element type of an input tensor to the
- <a id="ConvertIfIntegers"></a>`ConvertIfIntegers(mlir::MlirOp op1, mlir::MlirOp op2, mlir::ElementType target_dtype)` — [`L1094`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1094) — Conditionally converts the element types of two input tensors to the
- <a id="ConvolutionLike"></a>`ConvolutionLike(const mlir::RankedTensorType result_type, mlir::MlirOp lhs, mlir::MlirOp rhs, const stablehlo::ConvDimensionNumbersAttr dimension_numbers, const int64_t feature_group_count, const int64_t batch_group_count, const mlir::DenseI64ArrayAttr window_strides, const mlir::DenseIntElementsAttr padding, const mlir::DenseI64ArrayAttr lhs_dilation, const mlir::DenseI64ArrayAttr rhs_dilation, const mlir::DenseBoolArrayAttr window_reversal, const mlir::ArrayAttr precision_config, const std::optional<stablehlo::Dimensions>& result_dims)` — [`L814`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L814) — Builds a stablehlo.convolution that also supports bounded dynamic dimensions.
- `ConvolutionLike(const mlir::RankedTensorType result_type, mlir::MlirOp lhs, mlir::MlirOp rhs, const stablehlo::ConvDimensionNumbersAttr dimension_numbers, const int64_t feature_group_count, const int64_t batch_group_count, const mlir::DenseI64ArrayAttr window_strides, const mlir::DenseIntElementsAttr padding, const mlir::DenseI64ArrayAttr lhs_dilation, const mlir::DenseI64ArrayAttr rhs_dilation, const mlir::DenseBoolArrayAttr window_reversal, const mlir::ArrayAttr precision_config, const std::optional<stablehlo::Dimensions>& result_dims)` — [`L814`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L814) — Builds a stablehlo.convolution that also supports bounded dynamic dimensions.
- <a id="ConvolutionResultSize"></a>`ConvolutionResultSize(const ConvolutionWindow& window, mlir::MlirOp size)` — [`L145`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L145) — In-graph version of the above for the runtime size of a bounded dimension,
- `ConvolutionResultSize(const ConvolutionWindow& window, const int64_t size)` — [`L134`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L134) — Returns the convolution result size for an lhs size. Matches the StableHLO
- <a id="DebugString"></a>`DebugString(mlir::Operation* absl_nonnull op, DebugStringOptions opts)` — [`L437`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L437) — Returns a debugstring of the current operation or module
- <a id="DilatedSize"></a>`DilatedSize(const int64_t size, const int64_t dilation)` — [`L118`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L118) — Returns the size of `size` elements with `dilation - 1` holes inserted
- <a id="Flatten"></a>`Flatten(mlir::MlirOp input)` — [`L1488`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1488) — Flattens the input tensor to a single dimension.
- <a id="GetAllDimensions"></a>`GetAllDimensions(mlir::MlirOp op)` — [`L1548`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1548) — Returns a vector containing all dimensions of the given MlirOp.
- `GetAllDimensions(mlir::MlirOp op)` — [`L1548`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1548) — Returns a vector containing all dimensions of the given MlirOp.
- <a id="GetBasename"></a>`GetBasename(std::string_view filename)` — [`L104`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L104) — Given a potential filename, extract the filename without extension and path.
- `GetBatchDimensions(int64_t rank, int64_t dim)` — [`L1554`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1554) — Returns the batching dimensions for a tensor of rank `rank` excluding `dim`.
- <a id="GetBatchDimensions"></a>`GetBatchDimensions(int64_t rank, int64_t dim)` — [`L1554`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1554) — Returns the batching dimensions for a tensor of rank `rank` excluding `dim`.
- <a id="GetConvolutionWindows"></a>`GetConvolutionWindows(const stablehlo::ConvDimensionNumbersAttr dimension_numbers, const stablehlo::Dimensions& rhs_dims, const mlir::DenseI64ArrayAttr window_strides, const mlir::DenseIntElementsAttr padding, const mlir::DenseI64ArrayAttr lhs_dilation, const mlir::DenseI64ArrayAttr rhs_dilation)` — [`L251`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L251) — Returns the windows of the convolution spatial dimensions. Absent window
- `GetConvolutionWindows(const stablehlo::ConvDimensionNumbersAttr dimension_numbers, const stablehlo::Dimensions& rhs_dims, const mlir::DenseI64ArrayAttr window_strides, const mlir::DenseIntElementsAttr padding, const mlir::DenseI64ArrayAttr lhs_dilation, const mlir::DenseI64ArrayAttr rhs_dilation)` — [`L251`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L251) — Returns the windows of the convolution spatial dimensions. Absent window
- `GetCoreShape(const Dimensions& shape)` — [`L1783`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1783)
- <a id="GetCoreShape"></a>`GetCoreShape(const Dimensions& shape)` — [`L1783`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1783)
- `GetDimensions(mlir::Value value)` — [`L412`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L412) — Returns the dimensions of the value with bounded information if present.
- `GetDimensions(mlir::Value value)` — [`L412`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L412) — Returns the dimensions of the value with bounded information if present.
- <a id="GetDimensions"></a>`GetDimensions(mlir::MlirOp input)` — [`L420`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L420) — Returns the dimensions of the input op with bounded information if present.
- `GetDimensions(mlir::MlirOp input)` — [`L420`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L420) — Returns the dimensions of the input op with bounded information if present.
- <a id="GetElementType"></a>`GetElementType(mlir::MlirOp op)` — [`L495`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L495) — Returns the element type of the input op. Requires that the input op is a
- <a id="GetElementTypeOrDie"></a>`GetElementTypeOrDie(mlir::MlirOp op)` — [`L500`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L500)
- <a id="GetElementTypeOrSelf"></a>`GetElementTypeOrSelf(mlir::Type type)` — [`L484`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L484) — Gets the element type if ranked type, otherwise returns self. — documented in [stablehlo-op-builder](../../../concepts/stablehlo-op-builder.md)
- `GetElementTypeOrSelf(mlir::MlirOp type)` — [`L491`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L491)
- <a id="GetMaxFiniteDouble"></a>`GetMaxFiniteDouble(mlir::Type element_type)` — [`L583`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L583) — Returns the maximum representable finite value for a given floating-point
- <a id="GetMaxFiniteValueAttr"></a>`GetMaxFiniteValueAttr(mlir::Type element_type, mlir::OpBuilder& builder)` — [`L558`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L558) — Returns an attribute for the maximum finite value for a given type. This is
- <a id="GetMinFiniteDouble"></a>`GetMinFiniteDouble(mlir::Type element_type)` — [`L592`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L592) — Returns the minimum representable finite value for a given floating-point
- <a id="GetMinFiniteValueAttr"></a>`GetMinFiniteValueAttr(mlir::Type element_type, mlir::OpBuilder& builder)` — [`L533`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L533) — Returns an attribute for the minimum finite value for a given type. This is
- <a id="GetMlirType"></a>`GetMlirType(mlir::MLIRContext& ctx, const mlir::ElementType element_type)` — [`L509`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L509) — Shorthand for `ToElementType -> getElementType`. — documented in [stablehlo-op-builder](../../../concepts/stablehlo-op-builder.md)
- <a id="GetModuleOp"></a>`GetModuleOp(mlir::MlirBuilder& builder)` — [`L1424`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1424) — Returns the current ModuleOp a builder is operating in.
- <a id="GetNonzeroMask"></a>`GetNonzeroMask(mlir::MlirOp input)` — [`L746`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L746) — Returns an i1 mask of the elements that are not zero.
- <a id="GetNumElements"></a>`GetNumElements(mlir::MlirOp input, mlir::Type element_type, mlir::ArrayRef<int64_t> dims)` — [`L1383`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1383) — Returns an mlir::MlirOp representing the number of elements in the input
- `GetReassociationIndicesForReshape(const Dimensions& static_shape_before, const Dimensions& static_shape_after)` — [`L1668`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1668)
- <a id="GetReassociationIndicesForReshape"></a>`GetReassociationIndicesForReshape(const Dimensions& static_shape_before, const Dimensions& static_shape_after)` — [`L1668`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1668)
- `GetReshapeReassociation(const Dimensions& static_shape_before, const Dimensions& static_shape_after)` — [`L1880`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1880) — Returns the reassociation indices for the given input and output shapes.
- <a id="GetReshapeReassociation"></a>`GetReshapeReassociation(const Dimensions& static_shape_before, const Dimensions& static_shape_after)` — [`L1880`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1880) — Returns the reassociation indices for the given input and output shapes.
- `GetReshapeType(const Dimensions& static_shape_before, const Dimensions& static_shape_after)` — [`L1862`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1862) — Determines the reshape type for the given input and output shapes.
- <a id="GetReshapeType"></a>`GetReshapeType(const Dimensions& static_shape_before, const Dimensions& static_shape_after)` — [`L1862`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1862) — Determines the reshape type for the given input and output shapes.
- <a id="GetStaticShape"></a>`GetStaticShape(mlir::MlirOp input)` — [`L433`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L433) — Returns the static shape of the input op. For bounded dynamic dimensions, the
- `GetStaticShape(mlir::MlirOp input)` — [`L433`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L433) — Returns the static shape of the input op. For bounded dynamic dimensions, the
- `GetStaticShape(const mlir::stablehlo::Dimensions& dims)` — [`L424`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L424) — Returns the static shape of `dims`, with its bounded dynamic dimensions at
- `GetStaticShape(const mlir::stablehlo::Dimensions& dims)` — [`L424`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L424) — Returns the static shape of `dims`, with its bounded dynamic dimensions at
- <a id="GetTensorTypeOrDie"></a>`GetTensorTypeOrDie(const mlir::MlirOp& input)` — [`L475`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L475) — Gets the tensor type of the input op. Crashes if the input is not a tensor. — documented in [dtype-and-precision](../../../concepts/dtype-and-precision.md)
- <a id="GetVerifiedMinFiniteValue"></a>`GetVerifiedMinFiniteValue(mlir::MlirBuilder& builder, mlir::RankedTensorType constant_tensor_type)` — [`L519`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L519) — REMOVE STATUS RESULT ONCE TESTED
- <a id="HandleCollapseReshape"></a>`HandleCollapseReshape(mlir::MlirOp op, const ReshapeReassociation& reassociation, const mlir::stablehlo::Dimensions& op_dims, const Dimensions& static_shape_after, mlir::SmallVector<mlir::stablehlo::DimensionInfo>& output_dims)` — [`L1679`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1679)
- `HandleCollapseReshape(mlir::MlirOp op, const ReshapeReassociation& reassociation, const mlir::stablehlo::Dimensions& op_dims, const Dimensions& static_shape_after, mlir::SmallVector<mlir::stablehlo::DimensionInfo>& output_dims)` — [`L1679`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1679)
- <a id="HandleExpandReshape"></a>`HandleExpandReshape(mlir::MlirOp op, const ReshapeReassociation& reassociation, const mlir::stablehlo::Dimensions& op_dims, const Dimensions& static_shape_before, const Dimensions& static_shape_after, mlir::SmallVector<mlir::stablehlo::DimensionInfo>& output_dims)` — [`L1723`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1723)
- `HandleExpandReshape(mlir::MlirOp op, const ReshapeReassociation& reassociation, const mlir::stablehlo::Dimensions& op_dims, const Dimensions& static_shape_before, const Dimensions& static_shape_after, mlir::SmallVector<mlir::stablehlo::DimensionInfo>& output_dims)` — [`L1723`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1723)
- <a id="HandleTransposeLikeReshape"></a>`HandleTransposeLikeReshape(mlir::MlirOp op, const mlir::stablehlo::Dimensions& op_dims, const Dimensions& shape_before, const Dimensions& shape_after, mlir::SmallVector<mlir::stablehlo::DimensionInfo>& output_dims)` — [`L1793`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1793)
- `HandleTransposeLikeReshape(mlir::MlirOp op, const mlir::stablehlo::Dimensions& op_dims, const Dimensions& shape_before, const Dimensions& shape_after, mlir::SmallVector<mlir::stablehlo::DimensionInfo>& output_dims)` — [`L1793`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1793)
- `HasBoundedDimension(const std::optional<stablehlo::Dimensions>& dims)` — [`L201`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L201) — Returns whether `dims` has any bounded dynamic dimension.
- <a id="HasBoundedDimension"></a>`HasBoundedDimension(const std::optional<stablehlo::Dimensions>& dims)` — [`L201`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L201) — Returns whether `dims` has any bounded dynamic dimension.
- `InferStaticConvolutionResultShape(const stablehlo::ConvDimensionNumbersAttr dimension_numbers, const stablehlo::Dimensions& lhs_dims, const stablehlo::Dimensions& rhs_dims, const int64_t batch_group_count, const mlir::ArrayRef<ConvolutionWindow> windows)` — [`L284`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L284) — Infers the static result shape of a convolution at the upper bounds of `lhs`
- <a id="InferStaticConvolutionResultShape"></a>`InferStaticConvolutionResultShape(const stablehlo::ConvDimensionNumbersAttr dimension_numbers, const stablehlo::Dimensions& lhs_dims, const stablehlo::Dimensions& rhs_dims, const int64_t batch_group_count, const mlir::ArrayRef<ConvolutionWindow> windows)` — [`L284`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L284) — Infers the static result shape of a convolution at the upper bounds of `lhs`
- <a id="Iota"></a>`Iota(mlir::MlirOp reference_op, int64_t iota_dimension, mlir::Type element_type)` — [`L1121`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1121) — Generates an Iota tensor with the same shape as the reference op,
- <a id="MakeConstant"></a>`MakeConstant(mlir::MlirBuilder& builder, const at::Scalar& value, c10::optional<mlir::ElementType> element_type_opt, mlir::ArrayRef<int64_t> shape)` — [`L716`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L716) — PyTorch Specific constant builders. — documented in [stablehlo-op-builder](../../../concepts/stablehlo-op-builder.md)
- `MakeConstantAttr(mlir::MLIRContext& ctx, const T value, mlir::ArrayRef<int64_t> shape, const mlir::ElementType element_type)` — [`L623`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L623)
- <a id="MakeConstantAttr"></a>`MakeConstantAttr(mlir::MLIRContext& ctx, const at::Scalar& scalar_value, mlir::ArrayRef<int64_t> shape, c10::optional<mlir::ElementType> element_type_opt = std::nullopt)` — [`L630`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L630)
- <a id="MakeConstantLike"></a>`MakeConstantLike(mlir::MlirOp input, const at::Scalar& value)` — [`L726`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L726) — Returns a constant with the same shape as the input tensor. — documented in [stablehlo-op-builder](../../../concepts/stablehlo-op-builder.md)
- <a id="MakeStaticAtBounds"></a>`MakeStaticAtBounds(mlir::MlirOp input)` — [`L182`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L182) — Makes `input` static at its upper bounds, keeping the runtime sizes of its
- `MakeZeroSizedTensor(mlir::MlirBuilder& builder, mlir::Type element_type, mlir::ArrayRef<int64_t> shape)` — [`L596`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L596) — Returns a tensor of shape `shape` with zero elements and the given element
- <a id="MakeZeroSizedTensor"></a>`MakeZeroSizedTensor(mlir::MlirBuilder& builder, mlir::ElementType element_type, mlir::ArrayRef<int64_t> shape)` — [`L608`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L608) — Returns a tensor of shape `shape` with zero elements and the given element
- <a id="PromoteFloatDtype"></a>`PromoteFloatDtype(mlir::MlirOp op, mlir::ElementType min_precision)` — [`L1588`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1588) — Converts the data type of given float op to the given type if it has a lower
- <a id="ReassociationToString"></a>`ReassociationToString(const ReshapeReassociation& reassociation)` — [`L1843`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1843) — Returns a string representation of the reassociation indices for debugging.
- `ReshapeFromStaticDimensions(mlir::MlirOp op, const Dimensions& static_shape_before, const Dimensions& static_shape_after)` — [`L1909`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1909) — Reshapes the input op to the output shape.
- <a id="ReshapeFromStaticDimensions"></a>`ReshapeFromStaticDimensions(mlir::MlirOp op, const Dimensions& static_shape_before, const Dimensions& static_shape_after)` — [`L1909`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1909) — Reshapes the input op to the output shape.
- <a id="ReshapeToStaticDimensions"></a>`ReshapeToStaticDimensions(mlir::MlirOp op, const Dimensions& static_shape_after)` — [`L1972`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1972) — Reshapes the input op to `static_shape_after` (static sizes, or upper bounds
- `ReshapeToStaticDimensions(mlir::MlirOp op, const Dimensions& static_shape_after)` — [`L1972`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1972) — Reshapes the input op to `static_shape_after` (static sizes, or upper bounds
- <a id="ReshapeTypeToString"></a>`ReshapeTypeToString(ReshapeType type)` — [`L1645`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1645)
- <a id="RngBitGeneratorLike"></a>`RngBitGeneratorLike(mlir::MlirOp rng_input_state, mlir::RankedTensorType output_type, mlir::stablehlo::RngAlgorithmAttr rng_alg, std::optional<mlir::MlirOp> shape_reference)` — [`L770`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L770) — Generates random bits with static or bounded dynamic shapes.
- `RngBitGeneratorLike(mlir::MlirOp rng_input_state, mlir::RankedTensorType output_type, mlir::stablehlo::RngAlgorithmAttr rng_alg, std::optional<mlir::MlirOp> shape_reference)` — [`L770`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L770) — Generates random bits with static or bounded dynamic shapes.
- <a id="SerializeBytecode"></a>`SerializeBytecode(mlir::ModuleOp module)` — [`L447`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L447) — Returns the bytecode of the module.
- <a id="SerializePortableArtifact"></a>`SerializePortableArtifact(mlir::ModuleOp module)` — [`L456`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L456) — Returns the portable artifact (serialized Versioned StableHLO) of the module.
- <a id="ShapeTransitionToString"></a>`ShapeTransitionToString(absl::Span<const int64_t> shape_before, absl::Span<const int64_t> shape_after)` — [`L1661`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1661) — Returns a debug string for shape transitions of form: `from [1,2] to [3,4]`.
- <a id="SliceBatchDimensions"></a>`SliceBatchDimensions(mlir::MlirOp self, int64_t dim, const mlir::RankedTensorType& index_type)` — [`L1566`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1566) — Slices batch dimensions of `self` (dimensions other than `dim`) to match the
- <a id="Squeeze"></a>`Squeeze(mlir::MlirOp input, absl::Span<const int64_t> dims)` — [`L1451`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1451) — Squeezes the input tensor by removing dimensions of size 1.
- <a id="ToResultVector"></a>`ToResultVector(absl::StatusOr<mlir::MlirOp> results)` — [`L1169`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1169) — Converts a single-output op return value into a vector of outputs,
- `ToResultVector(absl::StatusOr<mlir::MlirOp> results)` — [`L1169`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1169) — Converts a single-output op return value into a vector of outputs,
- <a id="ToStdComplex"></a>`ToStdComplex(const c10::complex<T>& complex_value)` — [`L95`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L95)
- <a id="Unsqueeze"></a>`Unsqueeze(mlir::MlirOp input, int64_t dim)` — [`L1434`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L1434) — Unsqueezes the input tensor by inserting a dimension of size 1 at the
- `ValidateConvolutionBounds(const mlir::RankedTensorType lhs_type, const stablehlo::Dimensions& lhs_dims, const mlir::RankedTensorType rhs_type, const stablehlo::Dimensions& rhs_dims, const stablehlo::ConvDimensionNumbersAttr dimension_numbers, const int64_t feature_group_count, const int64_t batch_group_count, const bool has_result_dims)` — [`L342`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L342) — Returns a kPythonNotImplementedError if the bounded dynamic dimensions of
- <a id="ValidateConvolutionBounds"></a>`ValidateConvolutionBounds(const mlir::RankedTensorType lhs_type, const stablehlo::Dimensions& lhs_dims, const mlir::RankedTensorType rhs_type, const stablehlo::Dimensions& rhs_dims, const stablehlo::ConvDimensionNumbersAttr dimension_numbers, const int64_t feature_group_count, const int64_t batch_group_count, const bool has_result_dims)` — [`L342`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L342) — Returns a kPythonNotImplementedError if the bounded dynamic dimensions of
- <a id="ZeroPastRuntimeSizes"></a>`ZeroPastRuntimeSizes(mlir::MlirOp input, const std::vector<std::optional<mlir::MlirOp>>& runtime_sizes, const std::optional<int64_t> unzeroed_dim = std::nullopt)` — [`L224`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L224) — Zeroes the elements of the static `input` past the runtime sizes in
- `ZeroPastRuntimeSizes(mlir::MlirOp input, const std::vector<std::optional<mlir::MlirOp>>& runtime_sizes, const std::optional<int64_t> unzeroed_dim = std::nullopt)` — [`L224`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L224) — Zeroes the elements of the static `input` past the runtime sizes in

## Module values
- <a id="kSupportedBounds"></a>`kSupportedBounds` — [`L335`](../../../../../../raw/code/torch_tpu/csrc/ops/op_builder_utils.cc#L335) — Suffix of the error messages about unsupported bounded dynamic dimensions.

