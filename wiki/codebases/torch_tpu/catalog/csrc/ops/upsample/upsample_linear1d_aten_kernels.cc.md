---
title: 'Module: csrc/ops/upsample/upsample_linear1d_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/upsample/upsample_linear1d_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenUpsampleLinear1dOut: AtenUpsampleLinear1dOut(e6c412cf4d4bceeb).
  BuildUpsampleLinear1dShlo: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/BuildUpsampleLinear1dShlo(77206f0959b5660a).'
  ValidateUpsampleLinear1dInputs: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/ValidateUpsampleLinear1dInputs(ac7efd68c53c7393).'
  CheckUpsampleLinear1dDtypes: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/CheckUpsampleLinear1dDtypes(45982de3b0bc1087).'
  ComputeLinear1dSourceIndex: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/ComputeLinear1dSourceIndex(b7ee11266080713).'
  ComputeLinear1dDimInfo: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/ComputeLinear1dDimInfo(515b5bfa37ebcb72).'
  GetLinear1dGatherConfig: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/GetLinear1dGatherConfig(793e7028f2eac900).'
  BroadcastInDim: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/BroadcastInDim(eca68a4ac695ada1).'
  Reshape: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/Reshape(15aeb04bfe6e5ad5).'
  Linear1dDimInfo: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/Linear1dDimInfo#'
  Clamp: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/Clamp(58797ee5e7d65062).'
  Linear1dGatherConfig: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/Linear1dGatherConfig#'
  Linear1dGatherConfig.gather_dimension_numbers: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/Linear1dGatherConfig#gather_dimension_numbers.'
  AlignCorners: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/AlignCorners#'
  Linear1dDimInfo.left_weight: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/Linear1dDimInfo#left_weight.'
  Linear1dDimInfo.right_indices: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/Linear1dDimInfo#right_indices.'
  Linear1dDimInfo.right_weight: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/Linear1dDimInfo#right_weight.'
  Linear1dDimInfo.left_indices: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/Linear1dDimInfo#left_indices.'
  Gather: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/Gather(6be30f1e52abfee5).'
  Linear1dGatherConfig.slice_sizes: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/Linear1dGatherConfig#slice_sizes.'
  AlignCorners.kYes: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/AlignCorners#kYes.'
  AlignCorners.kNo: '`$anonymous_namespace_csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`/AlignCorners#kNo.'
---
# Module: [`csrc/ops/upsample/upsample_linear1d_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc)

## Classes
### <a id="AlignCorners"></a>`AlignCorners`
- def: [`csrc/ops/upsample/upsample_linear1d_aten_kernels.cc:52`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L52)
- signature: `enum class AlignCorners : bool`
- members:
  - <a id="AlignCorners.kNo"></a>`kNo` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L53)
  - <a id="AlignCorners.kYes"></a>`kYes` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L54)
- used by: [`AtenUpsampleLinear1dOut`](upsample_linear1d_aten_kernels.cc.md#AtenUpsampleLinear1dOut), [`BuildUpsampleLinear1dShlo`](upsample_linear1d_aten_kernels.cc.md#BuildUpsampleLinear1dShlo), [`ComputeLinear1dSourceIndex`](upsample_linear1d_aten_kernels.cc.md#ComputeLinear1dSourceIndex)

### <a id="Linear1dDimInfo"></a>`Linear1dDimInfo`
- def: [`csrc/ops/upsample/upsample_linear1d_aten_kernels.cc:62`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L62)
- signature: `struct Linear1dDimInfo`
- members:
  - <a id="Linear1dDimInfo.left_indices"></a>`left_indices` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L63)
  - <a id="Linear1dDimInfo.left_weight"></a>`left_weight` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L65)
  - <a id="Linear1dDimInfo.right_indices"></a>`right_indices` — [`L64`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L64)
  - <a id="Linear1dDimInfo.right_weight"></a>`right_weight` — [`L66`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L66)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildUpsampleLinear1dShlo`](upsample_linear1d_aten_kernels.cc.md#BuildUpsampleLinear1dShlo), [`ComputeLinear1dSourceIndex`](upsample_linear1d_aten_kernels.cc.md#ComputeLinear1dSourceIndex), [`ComputeLinear1dDimInfo`](upsample_linear1d_aten_kernels.cc.md#ComputeLinear1dDimInfo)

### <a id="Linear1dGatherConfig"></a>`Linear1dGatherConfig`
- def: [`csrc/ops/upsample/upsample_linear1d_aten_kernels.cc:57`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L57)
- signature: `struct Linear1dGatherConfig`
- members:
  - <a id="Linear1dGatherConfig.gather_dimension_numbers"></a>`gather_dimension_numbers` — [`L58`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L58)
  - <a id="Linear1dGatherConfig.slice_sizes"></a>`slice_sizes` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L59)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions)
- used by: [`BuildUpsampleLinear1dShlo`](upsample_linear1d_aten_kernels.cc.md#BuildUpsampleLinear1dShlo), [`BroadcastInDim`](upsample_linear1d_aten_kernels.cc.md#BroadcastInDim)

## Functions
- <a id="AtenUpsampleLinear1dOut"></a>`AtenUpsampleLinear1dOut(const at::Tensor& self, at::IntArrayRef output_size, bool align_corners, std::optional<double> scales, at::Tensor& out)` — [`L277`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L277)
- <a id="BroadcastInDim"></a>`BroadcastInDim(mlir::Type result_type, mlir::MlirOp operand, llvm::ArrayRef<int64_t> broadcast_dimensions)` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L85)
- <a id="BuildUpsampleLinear1dShlo"></a>`BuildUpsampleLinear1dShlo(mlir::MlirOp input, const Dimensions& output_shape, AlignCorners align_corners, std::optional<double> scales, mlir::Type calc_type)` — [`L184`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L184)
- <a id="CheckUpsampleLinear1dDtypes"></a>`CheckUpsampleLinear1dDtypes(const at::Tensor& tensor)` — [`L243`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L243)
- <a id="Clamp"></a>`Clamp(mlir::MlirOp min, mlir::MlirOp operand, mlir::MlirOp max)` — [`L69`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L69)
- <a id="ComputeLinear1dDimInfo"></a>`ComputeLinear1dDimInfo(mlir::MlirBuilder& builder, mlir::MlirOp src_idx, int64_t out_size, int64_t in_size, mlir::Type calc_type)` — [`L146`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L146)
- <a id="ComputeLinear1dSourceIndex"></a>`ComputeLinear1dSourceIndex(mlir::MlirBuilder& builder, int64_t out_size, int64_t in_size, std::optional<double> scale_opt, AlignCorners align_corners, mlir::Type calc_type)` — [`L114`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L114)
- `Gather(mlir::MlirOp operand, mlir::MlirOp start_indices, mlir::stablehlo::GatherDimensionNumbersAttr dimension_numbers, llvm::ArrayRef<int64_t> slice_sizes, bool indices_are_sorted = false)` — [`L73`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L73)
- <a id="Gather"></a>`Gather(mlir::MlirOp operand, mlir::MlirOp start_indices, mlir::stablehlo::GatherDimensionNumbersAttr dimension_numbers, llvm::ArrayRef<int64_t> slice_sizes, bool indices_are_sorted = false)` — [`L73`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L73)
- <a id="GetLinear1dGatherConfig"></a>`GetLinear1dGatherConfig(mlir::MlirOp input)` — [`L91`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L91)
- <a id="Reshape"></a>`Reshape(mlir::Type result_type, mlir::MlirOp operand)` — [`L81`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L81)
- <a id="ValidateUpsampleLinear1dInputs"></a>`ValidateUpsampleLinear1dInputs(const at::Tensor& self, at::IntArrayRef output_size, const at::Tensor& out)` — [`L249`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_linear1d_aten_kernels.cc#L249)

