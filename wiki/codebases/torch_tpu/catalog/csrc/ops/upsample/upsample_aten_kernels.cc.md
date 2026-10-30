---
title: 'Module: csrc/ops/upsample/upsample_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/upsample/upsample_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenUpsampleNearest1dOut: AtenUpsampleNearest1dOut(b259a44a9c1a1fd7).
  AtenUpsampleNearestExact3dOut: AtenUpsampleNearestExact3dOut(5f45602fc47c117e).
  AtenUpsampleNearestExact1dOut: AtenUpsampleNearestExact1dOut(b259a44a9c1a1fd7).
  AtenUpsampleNearest2dOut: AtenUpsampleNearest2dOut(fc60edb1aa34ff0a).
  AtenUpsampleNearestExact2dOut: AtenUpsampleNearestExact2dOut(fc60edb1aa34ff0a).
  AtenUpsampleNearest3dOut: AtenUpsampleNearest3dOut(5f45602fc47c117e).
  AtenUpsampleNearest1dBackwardGradInput: AtenUpsampleNearest1dBackwardGradInput(73d417c93c6c8ac9).
  AtenUpsampleNearestExact3dBackwardGradInput: AtenUpsampleNearestExact3dBackwardGradInput(9175134e47f5e365).
  AtenUpsampleNearest3dBackwardGradInput: AtenUpsampleNearest3dBackwardGradInput(9175134e47f5e365).
  AtenUpsampleNearestExact2dBackwardGradInput: AtenUpsampleNearestExact2dBackwardGradInput(8bd706b2f2621696).
  AtenUpsampleNearest2dBackwardGradInput: AtenUpsampleNearest2dBackwardGradInput(8bd706b2f2621696).
  AtenUpsampleNearestExact1dBackwardGradInput: AtenUpsampleNearestExact1dBackwardGradInput(73d417c93c6c8ac9).
  AtenUpsampleBilinear2dOut: AtenUpsampleBilinear2dOut(efa339bd3b82d173).
  AtenUpsampleBilinear2dBackwardGradInput: AtenUpsampleBilinear2dBackwardGradInput(de2dcbc79f3661c4).
  BuildUpsampleBilinearBackwardShlo: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/BuildUpsampleBilinearBackwardShlo(f19ac7e28e40b7b3).'
  CheckUpsampleDtypes: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/CheckUpsampleDtypes(45982de3b0bc1087).'
  BuildUpsampleBilinearShlo: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/BuildUpsampleBilinearShlo(f19ac7e28e40b7b3).'
  BuildUpsampleNearestBackwardIndexTensor: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/BuildUpsampleNearestBackwardIndexTensor(b2e9640799b4c39b).'
  AccumulateBilinearInterpolation: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/AccumulateBilinearInterpolation(28151c689093b8cd).'
  BuildUpsampleNearestBackwardShlo: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/BuildUpsampleNearestBackwardShlo(e1af406027a4b4b3).'
  ScatterBilinearBackwardForSingleCorner: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/ScatterBilinearBackwardForSingleCorner(1f5c6e0387fe5688).'
  BuildUpsampleNearestShlo: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/BuildUpsampleNearestShlo(1c76d98f49e4ef38).'
  BuildUpsampleNearestSingleDimIndexTensor: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/BuildUpsampleNearestSingleDimIndexTensor(9dc3c1381d104756).'
  ConstructScaleFactorArray: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/ConstructScaleFactorArray(ddb3ac8358eaf668).'
  ComputeSourceIndex: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/ComputeSourceIndex(c03719c730f77b23).'
  ComputeCornerIndicesAndWeight: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/ComputeCornerIndicesAndWeight(95af7d5e2ba04f4a).'
  BuildUpsampleNearestIndexTensor: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/BuildUpsampleNearestIndexTensor(b2e9640799b4c39b).'
  ComputeDimInfo: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/ComputeDimInfo(20702524af34adc1).'
  GetUpsampleGatherConfig: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/GetUpsampleGatherConfig(8d95ca40f340fc84).'
  UpsampleMode: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/UpsampleMode#'
  GetUpsampleScatterConfig: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/GetUpsampleScatterConfig(89bdcf7607ca97e8).'
  StandardizeScaleFactors: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/StandardizeScaleFactors(2c9f1b2a67a58881).'
  MlirOpVector: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/MlirOpVector#'
  DimInfo: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/DimInfo#'
  DimInfo.weight_ceil: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/DimInfo#weight_ceil.'
  TensorVector: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/TensorVector#'
  UpsampleMode.kNearestExact: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/UpsampleMode#kNearestExact.'
  UpsampleGatherConfig: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/UpsampleGatherConfig#'
  CornerIndicesAndWeight.weight: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/CornerIndicesAndWeight#weight.'
  UpsampleMode.kNearest: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/UpsampleMode#kNearest.'
  UpsampleScatterConfig.scatter_dimension_numbers: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/UpsampleScatterConfig#scatter_dimension_numbers.'
  DimInfo.idx_floor: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/DimInfo#idx_floor.'
  DimInfo.idx_ceil: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/DimInfo#idx_ceil.'
  ScaleVector: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/ScaleVector#'
  CornerIndicesAndWeight: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/CornerIndicesAndWeight#'
  DimInfo.weight_floor: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/DimInfo#weight_floor.'
  UpsampleScatterConfig: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/UpsampleScatterConfig#'
  UpsampleGatherConfig.gather_dimension_numbers: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/UpsampleGatherConfig#gather_dimension_numbers.'
  CornerIndicesAndWeight.indices: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/CornerIndicesAndWeight#indices.'
  UpsampleGatherConfig.slice_sizes: '`$anonymous_namespace_csrc/ops/upsample/upsample_aten_kernels.cc`/UpsampleGatherConfig#slice_sizes.'
---
# Module: [`csrc/ops/upsample/upsample_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc)

## Classes
### <a id="CornerIndicesAndWeight"></a>`CornerIndicesAndWeight`
- def: [`csrc/ops/upsample/upsample_aten_kernels.cc:280`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L280)
- doc: Represents the gathered spatial indices and the precomputed interpolation
- signature: `struct CornerIndicesAndWeight`
- members:
  - <a id="CornerIndicesAndWeight.indices"></a>`indices` — [`L284`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L284) — The gathered coordinates (idx_floor or idx_ceil) for each spatial dimension
  - <a id="CornerIndicesAndWeight.weight"></a>`weight` — [`L287`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L287) — The cumulative interpolation weight (e.g., lambda * (1 - lambda))
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`AccumulateBilinearInterpolation`](upsample_aten_kernels.cc.md#AccumulateBilinearInterpolation), [`ComputeCornerIndicesAndWeight`](upsample_aten_kernels.cc.md#ComputeCornerIndicesAndWeight)

### <a id="DimInfo"></a>`DimInfo`
- def: [`csrc/ops/upsample/upsample_aten_kernels.cc:161`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L161)
- doc: Stores the floor and ceil indices and their corresponding weights (lambda)
- signature: `struct DimInfo`
- members:
  - <a id="DimInfo.idx_ceil"></a>`idx_ceil` — [`L165`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L165) — Upper bound index (ceil(source_index))
  - <a id="DimInfo.idx_floor"></a>`idx_floor` — [`L163`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L163) — Lower bound index (floor(source_index))
  - <a id="DimInfo.weight_ceil"></a>`weight_ceil` — [`L169`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L169) — Weight for the upper bound index (lambda)
  - <a id="DimInfo.weight_floor"></a>`weight_floor` — [`L167`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L167) — Weight for the lower bound index (1 - lambda)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildUpsampleBilinearBackwardShlo`](upsample_aten_kernels.cc.md#BuildUpsampleBilinearBackwardShlo), [`BuildUpsampleBilinearShlo`](upsample_aten_kernels.cc.md#BuildUpsampleBilinearShlo), [`AccumulateBilinearInterpolation`](upsample_aten_kernels.cc.md#AccumulateBilinearInterpolation), [`ScatterBilinearBackwardForSingleCorner`](upsample_aten_kernels.cc.md#ScatterBilinearBackwardForSingleCorner), [`ComputeSourceIndex`](upsample_aten_kernels.cc.md#ComputeSourceIndex), [`ComputeCornerIndicesAndWeight`](upsample_aten_kernels.cc.md#ComputeCornerIndicesAndWeight), [`ComputeDimInfo`](upsample_aten_kernels.cc.md#ComputeDimInfo)

### <a id="MlirOpVector"></a>`MlirOpVector`
- def: [`csrc/ops/upsample/upsample_aten_kernels.cc:70`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L70)
- signature: `using MlirOpVector = absl::InlinedVector<mlir::MlirOp, 6>`
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildUpsampleNearestBackwardIndexTensor`](upsample_aten_kernels.cc.md#BuildUpsampleNearestBackwardIndexTensor), [`BuildUpsampleNearestBackwardShlo`](upsample_aten_kernels.cc.md#BuildUpsampleNearestBackwardShlo), [`BuildUpsampleNearestShlo`](upsample_aten_kernels.cc.md#BuildUpsampleNearestShlo), [`BuildUpsampleNearestSingleDimIndexTensor`](upsample_aten_kernels.cc.md#BuildUpsampleNearestSingleDimIndexTensor), [`BuildUpsampleNearestIndexTensor`](upsample_aten_kernels.cc.md#BuildUpsampleNearestIndexTensor)

### <a id="ScaleVector"></a>`ScaleVector`
- def: [`csrc/ops/upsample/upsample_aten_kernels.cc:69`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L69)
- signature: `using ScaleVector = absl::InlinedVector<std::optional<double>, 6>`
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildUpsampleBilinearBackwardShlo`](upsample_aten_kernels.cc.md#BuildUpsampleBilinearBackwardShlo), [`BuildUpsampleBilinearShlo`](upsample_aten_kernels.cc.md#BuildUpsampleBilinearShlo)

### <a id="TensorVector"></a>`TensorVector`
- def: [`csrc/ops/upsample/upsample_aten_kernels.cc:71`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L71)
- signature: `using TensorVector = absl::InlinedVector<at::Tensor, 6>`
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ConstructScaleFactorArray`](upsample_aten_kernels.cc.md#ConstructScaleFactorArray), [`StandardizeScaleFactors`](upsample_aten_kernels.cc.md#StandardizeScaleFactors)

### <a id="UpsampleGatherConfig"></a>`UpsampleGatherConfig`
- def: [`csrc/ops/upsample/upsample_aten_kernels.cc:76`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L76)
- doc: Configuration for the gather operation used in upsampling.
- signature: `struct UpsampleGatherConfig`
- members:
  - <a id="UpsampleGatherConfig.gather_dimension_numbers"></a>`gather_dimension_numbers` — [`L77`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L77)
  - <a id="UpsampleGatherConfig.slice_sizes"></a>`slice_sizes` — [`L78`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L78)
- uses (calls/refs, reference-scoped): [`SmallInt64Vector`](../../common/dimension_types.h.md#SmallInt64Vector)
- used by: [`BuildUpsampleBilinearShlo`](upsample_aten_kernels.cc.md#BuildUpsampleBilinearShlo), [`AccumulateBilinearInterpolation`](upsample_aten_kernels.cc.md#AccumulateBilinearInterpolation), [`BuildUpsampleNearestShlo`](upsample_aten_kernels.cc.md#BuildUpsampleNearestShlo), [`GetUpsampleScatterConfig`](upsample_aten_kernels.cc.md#GetUpsampleScatterConfig)

### <a id="UpsampleMode"></a>`UpsampleMode`
- def: [`csrc/ops/upsample/upsample_aten_kernels.cc:61`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L61)
- signature: `enum class UpsampleMode`
- members:
  - <a id="UpsampleMode.kNearest"></a>`kNearest` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L63) — Nearest mode uses the floor of the scaled coordinate.
  - <a id="UpsampleMode.kNearestExact"></a>`kNearestExact` — [`L66`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L66) — Nearest exact mode aligns the centers of the pixels by adding 0.5 before
- used by: [`AtenUpsampleNearest1dOut`](upsample_aten_kernels.cc.md#AtenUpsampleNearest1dOut), [`AtenUpsampleNearest2dOut`](upsample_aten_kernels.cc.md#AtenUpsampleNearest2dOut), [`AtenUpsampleNearest3dOut`](upsample_aten_kernels.cc.md#AtenUpsampleNearest3dOut), [`AtenUpsampleNearestExact1dOut`](upsample_aten_kernels.cc.md#AtenUpsampleNearestExact1dOut), [`AtenUpsampleNearestExact2dOut`](upsample_aten_kernels.cc.md#AtenUpsampleNearestExact2dOut), [`AtenUpsampleNearestExact3dOut`](upsample_aten_kernels.cc.md#AtenUpsampleNearestExact3dOut), [`AtenUpsampleNearest1dBackwardGradInput`](upsample_aten_kernels.cc.md#AtenUpsampleNearest1dBackwardGradInput), [`AtenUpsampleNearest2dBackwardGradInput`](upsample_aten_kernels.cc.md#AtenUpsampleNearest2dBackwardGradInput), [`AtenUpsampleNearest3dBackwardGradInput`](upsample_aten_kernels.cc.md#AtenUpsampleNearest3dBackwardGradInput), [`AtenUpsampleNearestExact1dBackwardGradInput`](upsample_aten_kernels.cc.md#AtenUpsampleNearestExact1dBackwardGradInput), [`AtenUpsampleNearestExact2dBackwardGradInput`](upsample_aten_kernels.cc.md#AtenUpsampleNearestExact2dBackwardGradInput), [`AtenUpsampleNearestExact3dBackwardGradInput`](upsample_aten_kernels.cc.md#AtenUpsampleNearestExact3dBackwardGradInput), [`BuildUpsampleNearestBackwardIndexTensor`](upsample_aten_kernels.cc.md#BuildUpsampleNearestBackwardIndexTensor), [`BuildUpsampleNearestBackwardShlo`](upsample_aten_kernels.cc.md#BuildUpsampleNearestBackwardShlo), [`BuildUpsampleNearestShlo`](upsample_aten_kernels.cc.md#BuildUpsampleNearestShlo), [`BuildUpsampleNearestSingleDimIndexTensor`](upsample_aten_kernels.cc.md#BuildUpsampleNearestSingleDimIndexTensor), [`BuildUpsampleNearestIndexTensor`](upsample_aten_kernels.cc.md#BuildUpsampleNearestIndexTensor)

### <a id="UpsampleScatterConfig"></a>`UpsampleScatterConfig`
- def: [`csrc/ops/upsample/upsample_aten_kernels.cc:81`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L81)
- signature: `struct UpsampleScatterConfig`
- members:
  - <a id="UpsampleScatterConfig.scatter_dimension_numbers"></a>`scatter_dimension_numbers` — [`L82`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L82)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildUpsampleNearestBackwardShlo`](upsample_aten_kernels.cc.md#BuildUpsampleNearestBackwardShlo), [`ScatterBilinearBackwardForSingleCorner`](upsample_aten_kernels.cc.md#ScatterBilinearBackwardForSingleCorner)

## Functions
- <a id="AccumulateBilinearInterpolation"></a>`AccumulateBilinearInterpolation(mlir::MlirBuilder& builder, mlir::MlirOp input, at::IntArrayRef output_shape, const std::vector<DimInfo>& dim_infos, const UpsampleGatherConfig& gather_config, int64_t offset_dim_size, int64_t spatial_dim_size, mlir::RankedTensorType broadcast_type, mlir::Type calc_type)` — [`L336`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L336) — Accumulates the weighted values from all 2^k corners for bilinear
- `AccumulateBilinearInterpolation(mlir::MlirBuilder& builder, mlir::MlirOp input, at::IntArrayRef output_shape, const std::vector<DimInfo>& dim_infos, const UpsampleGatherConfig& gather_config, int64_t offset_dim_size, int64_t spatial_dim_size, mlir::RankedTensorType broadcast_type, mlir::Type calc_type)` — [`L336`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L336) — Accumulates the weighted values from all 2^k corners for bilinear
- <a id="AtenUpsampleBilinear2dBackwardGradInput"></a>`AtenUpsampleBilinear2dBackwardGradInput(const at::Tensor& grad_output, at::IntArrayRef output_size, at::IntArrayRef input_size, bool align_corners, std::optional<double> scales_h, std::optional<double> scales_w, at::Tensor& grad_input)` — [`L1141`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L1141)
- <a id="AtenUpsampleBilinear2dOut"></a>`AtenUpsampleBilinear2dOut(const at::Tensor& self, at::IntArrayRef upsample_shape, bool align_corners, std::optional<double> scale_h, std::optional<double> scale_w, at::Tensor& out)` — [`L1106`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L1106) — Bilinear interpolation estimates a new pixel value by taking a weighted
- <a id="AtenUpsampleNearest1dBackwardGradInput"></a>`AtenUpsampleNearest1dBackwardGradInput(const at::Tensor& grad_output, at::IntArrayRef output_shape_in, at::IntArrayRef input_shape, std::optional<double> scale, at::Tensor& grad_input)` — [`L798`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L798)
- <a id="AtenUpsampleNearest1dOut"></a>`AtenUpsampleNearest1dOut(const at::Tensor& self, at::IntArrayRef upsample_shape, std::optional<double> scale, at::Tensor& out)` — [`L1178`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L1178)
- <a id="AtenUpsampleNearest2dBackwardGradInput"></a>`AtenUpsampleNearest2dBackwardGradInput(const at::Tensor& grad_output, at::IntArrayRef output_shape_in, at::IntArrayRef input_shape, std::optional<double> scale_h, std::optional<double> scale_w, at::Tensor& grad_input)` — [`L844`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L844)
- <a id="AtenUpsampleNearest2dOut"></a>`AtenUpsampleNearest2dOut(const at::Tensor& self, at::IntArrayRef upsample_shape, std::optional<double> scale_h, std::optional<double> scale_w, at::Tensor& out)` — [`L1217`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L1217)
- <a id="AtenUpsampleNearest3dBackwardGradInput"></a>`AtenUpsampleNearest3dBackwardGradInput(const at::Tensor& grad_output, at::IntArrayRef output_shape_in, at::IntArrayRef input_shape, std::optional<double> scale_h, std::optional<double> scale_w, std::optional<double> scale_d, at::Tensor& grad_input)` — [`L893`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L893)
- <a id="AtenUpsampleNearest3dOut"></a>`AtenUpsampleNearest3dOut(const at::Tensor& self, at::IntArrayRef upsample_shape, std::optional<double> scale_h, std::optional<double> scale_w, std::optional<double> scale_d, at::Tensor& out)` — [`L1263`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L1263)
- <a id="AtenUpsampleNearestExact1dBackwardGradInput"></a>`AtenUpsampleNearestExact1dBackwardGradInput(const at::Tensor& grad_output, at::IntArrayRef output_shape_in, at::IntArrayRef input_shape, std::optional<double> scale, at::Tensor& grad_input)` — [`L947`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L947)
- <a id="AtenUpsampleNearestExact1dOut"></a>`AtenUpsampleNearestExact1dOut(const at::Tensor& self, at::IntArrayRef upsample_shape, std::optional<double> scale, at::Tensor& out)` — [`L1310`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L1310)
- <a id="AtenUpsampleNearestExact2dBackwardGradInput"></a>`AtenUpsampleNearestExact2dBackwardGradInput(const at::Tensor& grad_output, at::IntArrayRef output_shape_in, at::IntArrayRef input_shape, std::optional<double> scale_h, std::optional<double> scale_w, at::Tensor& grad_input)` — [`L992`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L992)
- <a id="AtenUpsampleNearestExact2dOut"></a>`AtenUpsampleNearestExact2dOut(const at::Tensor& self, at::IntArrayRef upsample_shape, std::optional<double> scale_h, std::optional<double> scale_w, at::Tensor& out)` — [`L1350`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L1350)
- <a id="AtenUpsampleNearestExact3dBackwardGradInput"></a>`AtenUpsampleNearestExact3dBackwardGradInput(const at::Tensor& grad_output, at::IntArrayRef output_shape_in, at::IntArrayRef input_shape, std::optional<double> scale_h, std::optional<double> scale_w, std::optional<double> scale_d, at::Tensor& grad_input)` — [`L1041`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L1041)
- <a id="AtenUpsampleNearestExact3dOut"></a>`AtenUpsampleNearestExact3dOut(const at::Tensor& self, at::IntArrayRef upsample_shape, std::optional<double> scale_h, std::optional<double> scale_w, std::optional<double> scale_d, at::Tensor& out)` — [`L1393`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L1393)
- `BuildUpsampleBilinearBackwardShlo(mlir::MlirOp grad_output, int num_dimensions, at::IntArrayRef grad_input_shape, bool align_corners, const ScaleVector& scales_opt)` — [`L533`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L533)
- <a id="BuildUpsampleBilinearBackwardShlo"></a>`BuildUpsampleBilinearBackwardShlo(mlir::MlirOp grad_output, int num_dimensions, at::IntArrayRef grad_input_shape, bool align_corners, const ScaleVector& scales_opt)` — [`L533`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L533)
- <a id="BuildUpsampleBilinearShlo"></a>`BuildUpsampleBilinearShlo(mlir::MlirOp input, int num_dimensions, at::IntArrayRef output_shape, bool align_corners, const ScaleVector& scales_opt)` — [`L404`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L404) — Prep: Gets input/output shapes and setup types.
- `BuildUpsampleBilinearShlo(mlir::MlirOp input, int num_dimensions, at::IntArrayRef output_shape, bool align_corners, const ScaleVector& scales_opt)` — [`L404`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L404) — Prep: Gets input/output shapes and setup types.
- <a id="BuildUpsampleNearestBackwardIndexTensor"></a>`BuildUpsampleNearestBackwardIndexTensor(mlir::MlirBuilder& builder, int num_dimensions, mlir::MlirOp grad_output, at::IntArrayRef grad_input_shape, const MlirOpVector& inverse_scale_factor_array, UpsampleMode upsample_mode)` — [`L688`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L688)
- `BuildUpsampleNearestBackwardIndexTensor(mlir::MlirBuilder& builder, int num_dimensions, mlir::MlirOp grad_output, at::IntArrayRef grad_input_shape, const MlirOpVector& inverse_scale_factor_array, UpsampleMode upsample_mode)` — [`L688`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L688)
- `BuildUpsampleNearestBackwardShlo(mlir::MlirOp grad_output, at::IntArrayRef grad_input_shape, const MlirOpVector& inverse_scale_factor_array, UpsampleMode upsample_mode)` — [`L722`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L722)
- <a id="BuildUpsampleNearestBackwardShlo"></a>`BuildUpsampleNearestBackwardShlo(mlir::MlirOp grad_output, at::IntArrayRef grad_input_shape, const MlirOpVector& inverse_scale_factor_array, UpsampleMode upsample_mode)` — [`L722`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L722)
- `BuildUpsampleNearestIndexTensor(mlir::MlirBuilder& builder, int num_dimensions, mlir::MlirOp input, at::IntArrayRef output_shape, const MlirOpVector& inverse_scale_factor_array, UpsampleMode upsample_mode)` — [`L632`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L632)
- <a id="BuildUpsampleNearestIndexTensor"></a>`BuildUpsampleNearestIndexTensor(mlir::MlirBuilder& builder, int num_dimensions, mlir::MlirOp input, at::IntArrayRef output_shape, const MlirOpVector& inverse_scale_factor_array, UpsampleMode upsample_mode)` — [`L632`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L632)
- <a id="BuildUpsampleNearestShlo"></a>`BuildUpsampleNearestShlo(mlir::MlirOp input, at::IntArrayRef output_shape, const MlirOpVector& inverse_scale_factor_array, UpsampleMode upsample_mode)` — [`L667`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L667)
- `BuildUpsampleNearestShlo(mlir::MlirOp input, at::IntArrayRef output_shape, const MlirOpVector& inverse_scale_factor_array, UpsampleMode upsample_mode)` — [`L667`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L667)
- `BuildUpsampleNearestSingleDimIndexTensor(mlir::MlirBuilder& builder, int num_dimensions, int dimension, mlir::MlirOp grad_output, at::IntArrayRef grad_output_shape, const MlirOpVector& inverse_scale_factor_array, UpsampleMode upsample_mode)` — [`L605`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L605)
- <a id="BuildUpsampleNearestSingleDimIndexTensor"></a>`BuildUpsampleNearestSingleDimIndexTensor(mlir::MlirBuilder& builder, int num_dimensions, int dimension, mlir::MlirOp grad_output, at::IntArrayRef grad_output_shape, const MlirOpVector& inverse_scale_factor_array, UpsampleMode upsample_mode)` — [`L605`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L605)
- <a id="CheckUpsampleDtypes"></a>`CheckUpsampleDtypes(const at::Tensor& tensor)` — [`L788`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L788)
- `ComputeCornerIndicesAndWeight(int spatial_dim_size, int corner, const std::vector<DimInfo>& dim_infos)` — [`L290`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L290)
- <a id="ComputeCornerIndicesAndWeight"></a>`ComputeCornerIndicesAndWeight(int spatial_dim_size, int corner, const std::vector<DimInfo>& dim_infos)` — [`L290`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L290)
- <a id="ComputeDimInfo"></a>`ComputeDimInfo(mlir::MlirBuilder& builder, mlir::MlirOp src_idx, int64_t out_size, int64_t in_size, mlir::Type calc_type, mlir::RankedTensorType broadcast_type, mlir::RankedTensorType broadcast_type_calc, int spatial_dim_index)` — [`L233`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L233) — Computes the gather indices (floor/ceil) and interpolation weights (lambda)
- <a id="ComputeSourceIndex"></a>`ComputeSourceIndex(mlir::MlirBuilder& builder, int64_t out_size, int64_t in_size, std::optional<double> scale_opt, bool align_corners, mlir::Type calc_type)` — [`L182`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L182) — This function calculates where in the input image we should look for each
- `ConstructScaleFactorArray(absl::InlinedVector<double, 6> scale_array)` — [`L773`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L773)
- <a id="ConstructScaleFactorArray"></a>`ConstructScaleFactorArray(absl::InlinedVector<double, 6> scale_array)` — [`L773`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L773)
- <a id="GetUpsampleGatherConfig"></a>`GetUpsampleGatherConfig(mlir::MlirOp input, int64_t spatial_dim_size)` — [`L121`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L121)
- <a id="GetUpsampleScatterConfig"></a>`GetUpsampleScatterConfig(mlir::MlirOp grad_output, int64_t spatial_dim_size)` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L85)
- <a id="ScatterBilinearBackwardForSingleCorner"></a>`ScatterBilinearBackwardForSingleCorner(mlir::MlirBuilder& builder, mlir::MlirOp grad_input, int spatial_dim_size, int offset_dim_size, int corner, const std::vector<DimInfo>& dim_infos, const UpsampleScatterConfig& scatter_config, absl::FunctionRef<void(mlir::RegionBuilder&)> scatter_body, mlir::MlirOp grad_output, at::IntArrayRef grad_output_shape, mlir::MlirOp grad_output_calc, mlir::RankedTensorType broadcast_type, mlir::Type calc_type, mlir::Type element_type)` — [`L465`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L465)
- `ScatterBilinearBackwardForSingleCorner(mlir::MlirBuilder& builder, mlir::MlirOp grad_input, int spatial_dim_size, int offset_dim_size, int corner, const std::vector<DimInfo>& dim_infos, const UpsampleScatterConfig& scatter_config, absl::FunctionRef<void(mlir::RegionBuilder&)> scatter_body, mlir::MlirOp grad_output, at::IntArrayRef grad_output_shape, mlir::MlirOp grad_output_calc, mlir::RankedTensorType broadcast_type, mlir::Type calc_type, mlir::Type element_type)` — [`L465`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L465)
- <a id="StandardizeScaleFactors"></a>`StandardizeScaleFactors(at::IntArrayRef input_shape, at::IntArrayRef upsample_shape, absl::InlinedVector<std::optional<double>, 6> scale_array, bool inverse)` — [`L755`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L755)
- `StandardizeScaleFactors(at::IntArrayRef input_shape, at::IntArrayRef upsample_shape, absl::InlinedVector<std::optional<double>, 6> scale_array, bool inverse)` — [`L755`](../../../../../../../raw/code/torch_tpu/csrc/ops/upsample/upsample_aten_kernels.cc#L755)

