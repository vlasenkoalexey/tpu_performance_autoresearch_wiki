---
title: 'Module: csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenUpsampleBicubic2dBackwardGradInput: AtenUpsampleBicubic2dBackwardGradInput(de2dcbc79f3661c4).
  AtenUpsampleBicubic2dOut: AtenUpsampleBicubic2dOut(efa339bd3b82d173).
  BuildUpsampleBicubic2dBackwardShlo: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/BuildUpsampleBicubic2dBackwardShlo(49f9926dee955de1).'
  ComputeBicubicDimInfo: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/ComputeBicubicDimInfo(8c17f8a5abd325af).'
  CheckUpsampleDtypes: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/CheckUpsampleDtypes(45982de3b0bc1087).'
  BuildUpsampleBicubic2dShlo: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/BuildUpsampleBicubic2dShlo(24fac9bbb7bc8ccf).'
  GatherAndWeightSingleCorner: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/GatherAndWeightSingleCorner(3124009caf3d3cdd).'
  ScatterBicubic2dBackwardForSingleCorner: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/ScatterBicubic2dBackwardForSingleCorner(930977d1bcc22458).'
  ComputeBicubicSourceIndex: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/ComputeBicubicSourceIndex(c03719c730f77b23).'
  ComputeCubicWeightNear: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/ComputeCubicWeightNear(1f2e7317b5c28c4).'
  ComputeCubicWeightFar: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/ComputeCubicWeightFar(1f2e7317b5c28c4).'
  ComputeBicubicCornerIndicesAndWeight: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/ComputeBicubicCornerIndicesAndWeight(32e6befd7c4cbe3c).'
  AccumulateBicubicInterpolation: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/AccumulateBicubicInterpolation(2a382c7ffc6b64a0).'
  GetBicubicGatherConfig: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/GetBicubicGatherConfig(e2b5c8d9d87b5791).'
  ComputeTapWeight: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/ComputeTapWeight(9778f2e7142bc63d).'
  ComputeTapDistance: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/ComputeTapDistance(32088e4d0b1cb288).'
  ComputeTapOffset: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/ComputeTapOffset(32088e4d0b1cb288).'
  TapIndex: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/TapIndex#'
  GetBicubicScatterConfig: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/GetBicubicScatterConfig(e9574a50a2153f9e).'
  BicubicDimInfo: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/BicubicDimInfo#'
  BicubicDimInfo.indices: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/BicubicDimInfo#indices.'
  BicubicCornerIndicesAndWeight: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/BicubicCornerIndicesAndWeight#'
  BicubicGatherConfig: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/BicubicGatherConfig#'
  BicubicCornerIndicesAndWeight.indices: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/BicubicCornerIndicesAndWeight#indices.'
  ScaleVector: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/ScaleVector#'
  BicubicCornerIndicesAndWeight.weight: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/BicubicCornerIndicesAndWeight#weight.'
  BicubicScatterConfig: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/BicubicScatterConfig#'
  TapIndex.kTap3: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/TapIndex#kTap3.'
  TapIndex.kTap0: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/TapIndex#kTap0.'
  TapIndex.kTap2: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/TapIndex#kTap2.'
  TapIndex.kTap1: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/TapIndex#kTap1.'
  BicubicGatherConfig.gather_dimension_numbers: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/BicubicGatherConfig#gather_dimension_numbers.'
  BicubicDimInfo.weights: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/BicubicDimInfo#weights.'
  BicubicGatherConfig.slice_sizes: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/BicubicGatherConfig#slice_sizes.'
  BicubicScatterConfig.scatter_dimension_numbers: '`$anonymous_namespace_csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`/BicubicScatterConfig#scatter_dimension_numbers.'
---
# Module: [`csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc)

## Classes
### <a id="BicubicCornerIndicesAndWeight"></a>`BicubicCornerIndicesAndWeight`
- def: [`csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc:80`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L80)
- signature: `struct BicubicCornerIndicesAndWeight`
- members:
  - <a id="BicubicCornerIndicesAndWeight.indices"></a>`indices` — [`L81`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L81)
  - <a id="BicubicCornerIndicesAndWeight.weight"></a>`weight` — [`L82`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L82)
- uses (calls/refs, reference-scoped): [`BicubicScatterConfig`](upsample_bicubic2d_aten_kernels.cc.md#BicubicScatterConfig)
- used by: [`ComputeBicubicDimInfo`](upsample_bicubic2d_aten_kernels.cc.md#ComputeBicubicDimInfo), [`GatherAndWeightSingleCorner`](upsample_bicubic2d_aten_kernels.cc.md#GatherAndWeightSingleCorner), [`ScatterBicubic2dBackwardForSingleCorner`](upsample_bicubic2d_aten_kernels.cc.md#ScatterBicubic2dBackwardForSingleCorner), [`ComputeBicubicCornerIndicesAndWeight`](upsample_bicubic2d_aten_kernels.cc.md#ComputeBicubicCornerIndicesAndWeight)

### <a id="BicubicDimInfo"></a>`BicubicDimInfo`
- def: [`csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc:75`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L75)
- signature: `struct BicubicDimInfo`
- members:
  - <a id="BicubicDimInfo.indices"></a>`indices` — [`L76`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L76)
  - <a id="BicubicDimInfo.weights"></a>`weights` — [`L77`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L77)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildUpsampleBicubic2dBackwardShlo`](upsample_bicubic2d_aten_kernels.cc.md#BuildUpsampleBicubic2dBackwardShlo), [`ComputeBicubicDimInfo`](upsample_bicubic2d_aten_kernels.cc.md#ComputeBicubicDimInfo), [`BuildUpsampleBicubic2dShlo`](upsample_bicubic2d_aten_kernels.cc.md#BuildUpsampleBicubic2dShlo), [`GatherAndWeightSingleCorner`](upsample_bicubic2d_aten_kernels.cc.md#GatherAndWeightSingleCorner), [`ScatterBicubic2dBackwardForSingleCorner`](upsample_bicubic2d_aten_kernels.cc.md#ScatterBicubic2dBackwardForSingleCorner), [`ComputeBicubicCornerIndicesAndWeight`](upsample_bicubic2d_aten_kernels.cc.md#ComputeBicubicCornerIndicesAndWeight), [`AccumulateBicubicInterpolation`](upsample_bicubic2d_aten_kernels.cc.md#AccumulateBicubicInterpolation), [`ComputeTapWeight`](upsample_bicubic2d_aten_kernels.cc.md#ComputeTapWeight)

### <a id="BicubicGatherConfig"></a>`BicubicGatherConfig`
- def: [`csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc:66`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L66)
- signature: `struct BicubicGatherConfig`
- members:
  - <a id="BicubicGatherConfig.gather_dimension_numbers"></a>`gather_dimension_numbers` — [`L67`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L67)
  - <a id="BicubicGatherConfig.slice_sizes"></a>`slice_sizes` — [`L68`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L68)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions)
- used by: [`BuildUpsampleBicubic2dShlo`](upsample_bicubic2d_aten_kernels.cc.md#BuildUpsampleBicubic2dShlo), [`GatherAndWeightSingleCorner`](upsample_bicubic2d_aten_kernels.cc.md#GatherAndWeightSingleCorner), [`AccumulateBicubicInterpolation`](upsample_bicubic2d_aten_kernels.cc.md#AccumulateBicubicInterpolation), [`GetBicubicScatterConfig`](upsample_bicubic2d_aten_kernels.cc.md#GetBicubicScatterConfig)

### <a id="BicubicScatterConfig"></a>`BicubicScatterConfig`
- def: [`csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc:71`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L71)
- signature: `struct BicubicScatterConfig`
- members:
  - <a id="BicubicScatterConfig.scatter_dimension_numbers"></a>`scatter_dimension_numbers` — [`L72`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L72)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ScatterBicubic2dBackwardForSingleCorner`](upsample_bicubic2d_aten_kernels.cc.md#ScatterBicubic2dBackwardForSingleCorner), [`weight`](upsample_bicubic2d_aten_kernels.cc.md#BicubicCornerIndicesAndWeight.weight)

### <a id="ScaleVector"></a>`ScaleVector`
- def: [`csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc:57`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L57)
- signature: `using ScaleVector = absl::InlinedVector<std::optional<double>, 2>`
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildUpsampleBicubic2dBackwardShlo`](upsample_bicubic2d_aten_kernels.cc.md#BuildUpsampleBicubic2dBackwardShlo), [`BuildUpsampleBicubic2dShlo`](upsample_bicubic2d_aten_kernels.cc.md#BuildUpsampleBicubic2dShlo)

### <a id="TapIndex"></a>`TapIndex`
- def: [`csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc:59`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L59)
- signature: `enum class TapIndex`
- members:
  - <a id="TapIndex.kTap0"></a>`kTap0` — [`L60`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L60)
  - <a id="TapIndex.kTap1"></a>`kTap1` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L61)
  - <a id="TapIndex.kTap2"></a>`kTap2` — [`L62`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L62)
  - <a id="TapIndex.kTap3"></a>`kTap3` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L63)
- used by: [`ComputeBicubicDimInfo`](upsample_bicubic2d_aten_kernels.cc.md#ComputeBicubicDimInfo), [`ComputeTapWeight`](upsample_bicubic2d_aten_kernels.cc.md#ComputeTapWeight), [`ComputeTapDistance`](upsample_bicubic2d_aten_kernels.cc.md#ComputeTapDistance), [`ComputeTapOffset`](upsample_bicubic2d_aten_kernels.cc.md#ComputeTapOffset)

## Functions
- <a id="AccumulateBicubicInterpolation"></a>`AccumulateBicubicInterpolation(mlir::MlirBuilder& builder, mlir::MlirOp input, const Dimensions& output_shape, absl::Span<const BicubicDimInfo> dim_infos, const BicubicGatherConfig& gather_config, int64_t offset_dim_size, mlir::RankedTensorType broadcast_type, mlir::Type calc_type)` — [`L377`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L377)
- <a id="AtenUpsampleBicubic2dBackwardGradInput"></a>`AtenUpsampleBicubic2dBackwardGradInput(const at::Tensor& grad_output, at::IntArrayRef output_size, at::IntArrayRef input_size, bool align_corners, std::optional<double> scales_h, std::optional<double> scales_w, at::Tensor& grad_input)` — [`L651`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L651)
- <a id="AtenUpsampleBicubic2dOut"></a>`AtenUpsampleBicubic2dOut(const at::Tensor& self, at::IntArrayRef output_size, bool align_corners, std::optional<double> scale_h, std::optional<double> scale_w, at::Tensor& out)` — [`L590`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L590)
- `BuildUpsampleBicubic2dBackwardShlo(mlir::MlirOp grad_output, const Dimensions& grad_input_shape, bool align_corners, const ScaleVector& scales_opt, mlir::Type calc_type)` — [`L512`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L512)
- <a id="BuildUpsampleBicubic2dBackwardShlo"></a>`BuildUpsampleBicubic2dBackwardShlo(mlir::MlirOp grad_output, const Dimensions& grad_input_shape, bool align_corners, const ScaleVector& scales_opt, mlir::Type calc_type)` — [`L512`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L512)
- `BuildUpsampleBicubic2dShlo(mlir::MlirOp input, const Dimensions& output_shape, bool align_corners, const ScaleVector& scales_opt, mlir::Type calc_type)` — [`L400`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L400)
- <a id="BuildUpsampleBicubic2dShlo"></a>`BuildUpsampleBicubic2dShlo(mlir::MlirOp input, const Dimensions& output_shape, bool align_corners, const ScaleVector& scales_opt, mlir::Type calc_type)` — [`L400`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L400)
- <a id="CheckUpsampleDtypes"></a>`CheckUpsampleDtypes(const at::Tensor& tensor)` — [`L580`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L580)
- <a id="ComputeBicubicCornerIndicesAndWeight"></a>`ComputeBicubicCornerIndicesAndWeight(int corner, absl::Span<const BicubicDimInfo> dim_infos)` — [`L326`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L326)
- <a id="ComputeBicubicDimInfo"></a>`ComputeBicubicDimInfo(mlir::MlirBuilder& builder, mlir::MlirOp src_idx, int64_t out_size, int64_t in_size, mlir::Type calc_type, mlir::RankedTensorType broadcast_type, mlir::RankedTensorType broadcast_type_calc, int spatial_dim_index)` — [`L281`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L281)
- <a id="ComputeBicubicSourceIndex"></a>`ComputeBicubicSourceIndex(mlir::MlirBuilder& builder, int64_t out_size, int64_t in_size, std::optional<double> scale_opt, bool align_corners, mlir::Type calc_type)` — [`L169`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L169)
- <a id="ComputeCubicWeightFar"></a>`ComputeCubicWeightFar(mlir::MlirBuilder& builder, mlir::MlirOp d, mlir::Type calc_type, int64_t out_size)` — [`L216`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L216)
- <a id="ComputeCubicWeightNear"></a>`ComputeCubicWeightNear(mlir::MlirBuilder& builder, mlir::MlirOp d, mlir::Type calc_type, int64_t out_size)` — [`L200`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L200)
- <a id="ComputeTapDistance"></a>`ComputeTapDistance(TapIndex tap, mlir::MlirOp lambda, mlir::MlirOp one_calc, mlir::MlirOp two_calc)` — [`L234`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L234)
- <a id="ComputeTapOffset"></a>`ComputeTapOffset(TapIndex tap, mlir::MlirOp idx_floor_calc, mlir::MlirOp one_calc, mlir::MlirOp two_calc)` — [`L250`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L250)
- <a id="ComputeTapWeight"></a>`ComputeTapWeight(mlir::MlirBuilder& builder, TapIndex tap, mlir::MlirOp distance, mlir::Type calc_type, int64_t out_size)` — [`L266`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L266)
- <a id="GatherAndWeightSingleCorner"></a>`GatherAndWeightSingleCorner(mlir::MlirBuilder& builder, mlir::MlirOp input, const Dimensions& output_shape, int corner, absl::Span<const BicubicDimInfo> dim_infos, const BicubicGatherConfig& gather_config, int64_t offset_dim_size, mlir::RankedTensorType broadcast_type, mlir::Type calc_type)` — [`L339`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L339)
- <a id="GetBicubicGatherConfig"></a>`GetBicubicGatherConfig(mlir::MlirOp input)` — [`L126`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L126)
- <a id="GetBicubicScatterConfig"></a>`GetBicubicScatterConfig(mlir::MlirOp grad_output)` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L85)
- <a id="ScatterBicubic2dBackwardForSingleCorner"></a>`ScatterBicubic2dBackwardForSingleCorner(mlir::MlirBuilder& builder, mlir::MlirOp grad_input, int offset_dim_size, int corner, absl::Span<const BicubicDimInfo> dim_infos, const BicubicScatterConfig& scatter_config, absl::FunctionRef<void(mlir::RegionBuilder&)> scatter_body, const Dimensions& grad_output_shape, mlir::MlirOp grad_output_calc, mlir::Type calc_type, mlir::Type element_type)` — [`L454`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_bicubic2d_aten_kernels.cc#L454)

