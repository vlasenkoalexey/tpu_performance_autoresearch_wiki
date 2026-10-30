---
title: 'Module: csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenGridSampler3dBackward: AtenGridSampler3dBackward(627d6579a1f7ed8a).
  AtenGridSampler2d: AtenGridSampler2d(42bc10cdf0933e22).
  AtenGridSampler2dBackward: AtenGridSampler2dBackward(627d6579a1f7ed8a).
  AtenGridSampler3d: AtenGridSampler3d(42bc10cdf0933e22).
  CalculateBicubicBackwardCorners: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/CalculateBicubicBackwardCorners(3349cfa7fed5983d).'
  BuildGridSamplerBicubicShlo: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BuildGridSamplerBicubicShlo(5300c49393ce9306).'
  BuildGridSamplerBicubicBackwardShlo: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BuildGridSamplerBicubicBackwardShlo(1624153532898a58).'
  ComputeBuildBilinearScatterIndicesForCorner: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/ComputeBuildBilinearScatterIndicesForCorner(2b3b90a62aad4da2).'
  BuildGridSamplerBilinearBackwardShlo: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BuildGridSamplerBilinearBackwardShlo(1624153532898a58).'
  AccumulateBicubicInterpolation: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/AccumulateBicubicInterpolation(7f2816a8047514a9).'
  BuildGridSamplerNearestShlo: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BuildGridSamplerNearestShlo(5300c49393ce9306).'
  UpdateIndicesForPaddingMode: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/UpdateIndicesForPaddingMode(2831c71bb0c475c6).'
  BuildBilinearScatterIndices: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BuildBilinearScatterIndices(83965b79a5047157).'
  AccumulateBilinearInterpolation2D: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/AccumulateBilinearInterpolation2D(dedc5b912676516c).'
  AccumulateBilinearInterpolation3D: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/AccumulateBilinearInterpolation3D(a04ddaf75254336).'
  BuildGridSamplerBilinearShlo: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BuildGridSamplerBilinearShlo(5300c49393ce9306).'
  BuildGridSamplerNearestBackwardShlo: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BuildGridSamplerNearestBackwardShlo(1624153532898a58).'
  ComputeCubicDimInfo: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/ComputeCubicDimInfo(e6eb591dacf4eea9).'
  ComputeSourceCoord: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/ComputeSourceCoord(f3ce9990a4d5af70).'
  CalculateBicubicBackwardWeightsAndIndices: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/CalculateBicubicBackwardWeightsAndIndices(967eb29877eb6102).'
  AccumulateBilinearInterpolation: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/AccumulateBilinearInterpolation(c7df9e9e381a5c82).'
  ValidateInputAndPaddingMode: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/ValidateInputAndPaddingMode(9c48db921af89c2d).'
  Validate2DInterpolationMode: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/Validate2DInterpolationMode(54be189a5a24de57).'
  Validate3DInterpolationMode: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/Validate3DInterpolationMode(54be189a5a24de57).'
  BuildGradGrid: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BuildGradGrid(83c8f8340e086940).'
  ApplyZeroPadding: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/ApplyZeroPadding(5314b8abc4d87b21).'
  ComputeGradInputOperandsForCorner: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/ComputeGradInputOperandsForCorner(12ee12cfe89cb70c).'
  ComputeDimInfo: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/ComputeDimInfo(cc54e0e0cae1b9b2).'
  GatherOrDynamicGather: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/GatherOrDynamicGather(afac15ca2cd83fc4).'
  PaddingMode: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/PaddingMode#'
  GetBilinearDimInfo: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/GetBilinearDimInfo(217e3fd8d3e9a6d8).'
  DimensionInfoToOp: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/DimensionInfoToOp(24b76d831463e9d9).'
  CalculateBicubicBackwardTotalDL: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/CalculateBicubicBackwardTotalDL(e85ed9e810970a35).'
  GatherInterpolatedValue: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/GatherInterpolatedValue(1f58a6f681a51887).'
  GetGridSamplerGatherConfig: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/GetGridSamplerGatherConfig(1ee7d4e1ca2b15cc).'
  GridSamplerGatherConfig: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/GridSamplerGatherConfig#'
  BicubicWeightsAndIndices.BicubicWeightsAndIndices: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BicubicWeightsAndIndices#BicubicWeightsAndIndices(1624ee8275b10bda).'
  ReshapeIndexTo2D: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/ReshapeIndexTo2D(cf97982c188f832c).'
  DimInfo: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/DimInfo#'
  BilinearDimInfo: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BilinearDimInfo#'
  PaddingMode.kZeros: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/PaddingMode#kZeros.'
  BilinearDimInfo.idx: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BilinearDimInfo#idx.'
  BilinearDimInfo.idx_unclamped: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BilinearDimInfo#idx_unclamped.'
  InterpolationMode: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/InterpolationMode#'
  CubicDimInfo.indices_unclamped: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/CubicDimInfo#indices_unclamped.'
  CubicDimInfo.indices: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/CubicDimInfo#indices.'
  BilinearDimInfo.weight: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BilinearDimInfo#weight.'
  GridSamplerGatherConfig.slice_sizes: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/GridSamplerGatherConfig#slice_sizes.'
  CubicDimInfo: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/CubicDimInfo#'
  PaddingMode.kReflection: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/PaddingMode#kReflection.'
  CubicDimInfo.weights: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/CubicDimInfo#weights.'
  CornerScatterOperands: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/CornerScatterOperands#'
  CornerScatterOperands.updates: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/CornerScatterOperands#updates.'
  InterpolationMode.kBilinear: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/InterpolationMode#kBilinear.'
  BicubicWeightsAndIndices: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BicubicWeightsAndIndices#'
  BicubicBackwardCornerOperands: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BicubicBackwardCornerOperands#'
  BilinearScatterOperands.all_scatter_indices: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BilinearScatterOperands#all_scatter_indices.'
  InterpolationMode.kNearest: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/InterpolationMode#kNearest.'
  BicubicBackwardOperands.total_dl: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BicubicBackwardOperands#total_dl.'
  BicubicBackwardCornerOperands.all_updates: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BicubicBackwardCornerOperands#all_updates.'
  GridSamplerGatherConfig.gather_dimension_numbers: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/GridSamplerGatherConfig#gather_dimension_numbers.'
  BicubicBackwardOperands: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BicubicBackwardOperands#'
  BilinearScatterOperands: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BilinearScatterOperands#'
  DimInfo.weight_ceil: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/DimInfo#weight_ceil.'
  DimInfo.idx_ceil: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/DimInfo#idx_ceil.'
  BicubicWeightsAndIndices.all_indices: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BicubicWeightsAndIndices#all_indices.'
  BicubicWeightsAndIndices.all_d_weights: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BicubicWeightsAndIndices#all_d_weights.'
  InterpolationMode.kBicubic: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/InterpolationMode#kBicubic.'
  BicubicWeightsAndIndices.all_weights: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BicubicWeightsAndIndices#all_weights.'
  DimInfo.idx_floor_unclamped: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/DimInfo#idx_floor_unclamped.'
  BicubicWeightsAndIndices.all_indices_unclamped: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BicubicWeightsAndIndices#all_indices_unclamped.'
  DimInfo.idx_floor: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/DimInfo#idx_floor.'
  DimInfo.weight_floor: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/DimInfo#weight_floor.'
  CornerScatterOperands.scatter_indices: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/CornerScatterOperands#scatter_indices.'
  BilinearScatterOperands.all_updates: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BilinearScatterOperands#all_updates.'
  BicubicBackwardOperands.grad_input_accum: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BicubicBackwardOperands#grad_input_accum.'
  BicubicBackwardCornerOperands.total_dl: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BicubicBackwardCornerOperands#total_dl.'
  BicubicBackwardCornerOperands.all_scatter_indices: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BicubicBackwardCornerOperands#all_scatter_indices.'
  DimInfo.idx_ceil_unclamped: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/DimInfo#idx_ceil_unclamped.'
  PaddingMode.kBorder: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/PaddingMode#kBorder.'
  BicubicWeightsAndIndices.grid_coords: '`$anonymous_namespace_csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`/BicubicWeightsAndIndices#grid_coords.'
---
# Module: [`csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc)

## Classes
### <a id="BicubicBackwardCornerOperands"></a>`BicubicBackwardCornerOperands`
- def: [`csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc:1694`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1694)
- signature: `struct BicubicBackwardCornerOperands`
- members:
  - <a id="BicubicBackwardCornerOperands.all_scatter_indices"></a>`all_scatter_indices` — [`L1696`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1696)
  - <a id="BicubicBackwardCornerOperands.all_updates"></a>`all_updates` — [`L1697`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1697)
  - <a id="BicubicBackwardCornerOperands.total_dl"></a>`total_dl` — [`L1695`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1695)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`CalculateBicubicBackwardCorners`](grid_sampler_aten_kernels.cc.md#CalculateBicubicBackwardCorners), [`CalculateBicubicBackwardTotalDL`](grid_sampler_aten_kernels.cc.md#CalculateBicubicBackwardTotalDL)

### <a id="BicubicBackwardOperands"></a>`BicubicBackwardOperands`
- def: [`csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc:1863`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1863)
- signature: `struct BicubicBackwardOperands`
- members:
  - <a id="BicubicBackwardOperands.grad_input_accum"></a>`grad_input_accum` — [`L1864`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1864)
  - <a id="BicubicBackwardOperands.total_dl"></a>`total_dl` — [`L1865`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1865)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`CalculateBicubicBackwardTotalDL`](grid_sampler_aten_kernels.cc.md#CalculateBicubicBackwardTotalDL)

### <a id="BicubicWeightsAndIndices"></a>`BicubicWeightsAndIndices`
- def: [`csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc:1588`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1588)
- signature: `struct BicubicWeightsAndIndices`
- members:
  - <a id="BicubicWeightsAndIndices.BicubicWeightsAndIndices"></a>`BicubicWeightsAndIndices(int64_t size)` — [`L1595`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1595)
  - <a id="BicubicWeightsAndIndices.all_d_weights"></a>`all_d_weights` — [`L1590`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1590)
  - <a id="BicubicWeightsAndIndices.all_indices"></a>`all_indices` — [`L1591`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1591)
  - <a id="BicubicWeightsAndIndices.all_indices_unclamped"></a>`all_indices_unclamped` — [`L1592`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1592)
  - <a id="BicubicWeightsAndIndices.all_weights"></a>`all_weights` — [`L1589`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1589)
  - <a id="BicubicWeightsAndIndices.grid_coords"></a>`grid_coords` — [`L1593`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1593)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`CalculateBicubicBackwardCorners`](grid_sampler_aten_kernels.cc.md#CalculateBicubicBackwardCorners), [`CalculateBicubicBackwardWeightsAndIndices`](grid_sampler_aten_kernels.cc.md#CalculateBicubicBackwardWeightsAndIndices)

### <a id="BilinearDimInfo"></a>`BilinearDimInfo`
- def: [`csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc:365`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L365)
- signature: `struct BilinearDimInfo`
- members:
  - <a id="BilinearDimInfo.idx"></a>`idx` — [`L366`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L366)
  - <a id="BilinearDimInfo.idx_unclamped"></a>`idx_unclamped` — [`L368`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L368)
  - <a id="BilinearDimInfo.weight"></a>`weight` — [`L367`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L367)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ComputeBuildBilinearScatterIndicesForCorner`](grid_sampler_aten_kernels.cc.md#ComputeBuildBilinearScatterIndicesForCorner), [`AccumulateBilinearInterpolation2D`](grid_sampler_aten_kernels.cc.md#AccumulateBilinearInterpolation2D), [`AccumulateBilinearInterpolation3D`](grid_sampler_aten_kernels.cc.md#AccumulateBilinearInterpolation3D), [`GetBilinearDimInfo`](grid_sampler_aten_kernels.cc.md#GetBilinearDimInfo)

### <a id="BilinearScatterOperands"></a>`BilinearScatterOperands`
- def: [`csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc:1253`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1253)
- signature: `struct BilinearScatterOperands`
- members:
  - <a id="BilinearScatterOperands.all_scatter_indices"></a>`all_scatter_indices` — [`L1254`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1254)
  - <a id="BilinearScatterOperands.all_updates"></a>`all_updates` — [`L1255`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1255)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ComputeBuildBilinearScatterIndicesForCorner`](grid_sampler_aten_kernels.cc.md#ComputeBuildBilinearScatterIndicesForCorner), [`BuildGridSamplerBilinearBackwardShlo`](grid_sampler_aten_kernels.cc.md#BuildGridSamplerBilinearBackwardShlo), [`BuildBilinearScatterIndices`](grid_sampler_aten_kernels.cc.md#BuildBilinearScatterIndices)

### <a id="CornerScatterOperands"></a>`CornerScatterOperands`
- def: [`csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc:1258`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1258)
- signature: `struct CornerScatterOperands`
- members:
  - <a id="CornerScatterOperands.scatter_indices"></a>`scatter_indices` — [`L1259`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1259)
  - <a id="CornerScatterOperands.updates"></a>`updates` — [`L1260`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1260)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ComputeBuildBilinearScatterIndicesForCorner`](grid_sampler_aten_kernels.cc.md#ComputeBuildBilinearScatterIndicesForCorner), [`BuildBilinearScatterIndices`](grid_sampler_aten_kernels.cc.md#BuildBilinearScatterIndices), [`ComputeGradInputOperandsForCorner`](grid_sampler_aten_kernels.cc.md#ComputeGradInputOperandsForCorner)

### <a id="CubicDimInfo"></a>`CubicDimInfo`
- def: [`csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc:509`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L509)
- signature: `struct CubicDimInfo`
- members:
  - <a id="CubicDimInfo.indices"></a>`indices` — [`L510`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L510)
  - <a id="CubicDimInfo.indices_unclamped"></a>`indices_unclamped` — [`L512`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L512)
  - <a id="CubicDimInfo.weights"></a>`weights` — [`L511`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L511)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildGridSamplerBicubicShlo`](grid_sampler_aten_kernels.cc.md#BuildGridSamplerBicubicShlo), [`AccumulateBicubicInterpolation`](grid_sampler_aten_kernels.cc.md#AccumulateBicubicInterpolation), [`UpdateIndicesForPaddingMode`](grid_sampler_aten_kernels.cc.md#UpdateIndicesForPaddingMode), [`ComputeCubicDimInfo`](grid_sampler_aten_kernels.cc.md#ComputeCubicDimInfo), [`CalculateBicubicBackwardWeightsAndIndices`](grid_sampler_aten_kernels.cc.md#CalculateBicubicBackwardWeightsAndIndices)

### <a id="DimInfo"></a>`DimInfo`
- def: [`csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc:174`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L174)
- signature: `struct DimInfo`
- members:
  - <a id="DimInfo.idx_ceil"></a>`idx_ceil` — [`L176`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L176)
  - <a id="DimInfo.idx_ceil_unclamped"></a>`idx_ceil_unclamped` — [`L180`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L180)
  - <a id="DimInfo.idx_floor"></a>`idx_floor` — [`L175`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L175)
  - <a id="DimInfo.idx_floor_unclamped"></a>`idx_floor_unclamped` — [`L179`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L179)
  - <a id="DimInfo.weight_ceil"></a>`weight_ceil` — [`L178`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L178)
  - <a id="DimInfo.weight_floor"></a>`weight_floor` — [`L177`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L177)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ComputeBuildBilinearScatterIndicesForCorner`](grid_sampler_aten_kernels.cc.md#ComputeBuildBilinearScatterIndicesForCorner), [`BuildGridSamplerBilinearBackwardShlo`](grid_sampler_aten_kernels.cc.md#BuildGridSamplerBilinearBackwardShlo), [`AccumulateBilinearInterpolation2D`](grid_sampler_aten_kernels.cc.md#AccumulateBilinearInterpolation2D), [`BuildBilinearScatterIndices`](grid_sampler_aten_kernels.cc.md#BuildBilinearScatterIndices), [`AccumulateBilinearInterpolation3D`](grid_sampler_aten_kernels.cc.md#AccumulateBilinearInterpolation3D), [`BuildGridSamplerBilinearShlo`](grid_sampler_aten_kernels.cc.md#BuildGridSamplerBilinearShlo), [`ComputeSourceCoord`](grid_sampler_aten_kernels.cc.md#ComputeSourceCoord), [`AccumulateBilinearInterpolation`](grid_sampler_aten_kernels.cc.md#AccumulateBilinearInterpolation), [`ComputeDimInfo`](grid_sampler_aten_kernels.cc.md#ComputeDimInfo), [`GetBilinearDimInfo`](grid_sampler_aten_kernels.cc.md#GetBilinearDimInfo)

### <a id="GridSamplerGatherConfig"></a>`GridSamplerGatherConfig`
- def: [`csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc:80`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L80)
- signature: `struct GridSamplerGatherConfig`
- members:
  - <a id="GridSamplerGatherConfig.gather_dimension_numbers"></a>`gather_dimension_numbers` — [`L81`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L81)
  - <a id="GridSamplerGatherConfig.slice_sizes"></a>`slice_sizes` — [`L82`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L82)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`CalculateBicubicBackwardCorners`](grid_sampler_aten_kernels.cc.md#CalculateBicubicBackwardCorners), [`BuildGridSamplerBicubicShlo`](grid_sampler_aten_kernels.cc.md#BuildGridSamplerBicubicShlo), [`ComputeBuildBilinearScatterIndicesForCorner`](grid_sampler_aten_kernels.cc.md#ComputeBuildBilinearScatterIndicesForCorner), [`BuildGridSamplerBilinearBackwardShlo`](grid_sampler_aten_kernels.cc.md#BuildGridSamplerBilinearBackwardShlo), [`AccumulateBicubicInterpolation`](grid_sampler_aten_kernels.cc.md#AccumulateBicubicInterpolation), [`BuildGridSamplerNearestShlo`](grid_sampler_aten_kernels.cc.md#BuildGridSamplerNearestShlo), [`AccumulateBilinearInterpolation2D`](grid_sampler_aten_kernels.cc.md#AccumulateBilinearInterpolation2D), [`BuildBilinearScatterIndices`](grid_sampler_aten_kernels.cc.md#BuildBilinearScatterIndices), [`AccumulateBilinearInterpolation3D`](grid_sampler_aten_kernels.cc.md#AccumulateBilinearInterpolation3D), [`BuildGridSamplerBilinearShlo`](grid_sampler_aten_kernels.cc.md#BuildGridSamplerBilinearShlo), [`AccumulateBilinearInterpolation`](grid_sampler_aten_kernels.cc.md#AccumulateBilinearInterpolation), [`GatherOrDynamicGather`](grid_sampler_aten_kernels.cc.md#GatherOrDynamicGather), [`GatherInterpolatedValue`](grid_sampler_aten_kernels.cc.md#GatherInterpolatedValue)

### <a id="InterpolationMode"></a>`InterpolationMode`
- def: [`csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc:64`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L64)
- doc: Enum class for interpolation modes.
- signature: `enum class InterpolationMode`
- members:
  - <a id="InterpolationMode.kBicubic"></a>`kBicubic` — [`L67`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L67)
  - <a id="InterpolationMode.kBilinear"></a>`kBilinear` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L65)
  - <a id="InterpolationMode.kNearest"></a>`kNearest` — [`L66`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L66)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`AtenGridSampler3dBackward`](grid_sampler_aten_kernels.cc.md#AtenGridSampler3dBackward), [`AtenGridSampler2d`](grid_sampler_aten_kernels.cc.md#AtenGridSampler2d), [`AtenGridSampler2dBackward`](grid_sampler_aten_kernels.cc.md#AtenGridSampler2dBackward), [`AtenGridSampler3d`](grid_sampler_aten_kernels.cc.md#AtenGridSampler3d), [`Validate2DInterpolationMode`](grid_sampler_aten_kernels.cc.md#Validate2DInterpolationMode), [`Validate3DInterpolationMode`](grid_sampler_aten_kernels.cc.md#Validate3DInterpolationMode)

### <a id="PaddingMode"></a>`PaddingMode`
- def: [`csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc:183`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L183)
- signature: `enum class PaddingMode`
- members:
  - <a id="PaddingMode.kBorder"></a>`kBorder` — [`L183`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L183)
  - <a id="PaddingMode.kReflection"></a>`kReflection` — [`L183`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L183)
  - <a id="PaddingMode.kZeros"></a>`kZeros` — [`L183`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L183)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`AtenGridSampler3dBackward`](grid_sampler_aten_kernels.cc.md#AtenGridSampler3dBackward), [`AtenGridSampler2d`](grid_sampler_aten_kernels.cc.md#AtenGridSampler2d), [`AtenGridSampler2dBackward`](grid_sampler_aten_kernels.cc.md#AtenGridSampler2dBackward), [`AtenGridSampler3d`](grid_sampler_aten_kernels.cc.md#AtenGridSampler3d), [`CalculateBicubicBackwardCorners`](grid_sampler_aten_kernels.cc.md#CalculateBicubicBackwardCorners), [`BuildGridSamplerBicubicShlo`](grid_sampler_aten_kernels.cc.md#BuildGridSamplerBicubicShlo), [`BuildGridSamplerBicubicBackwardShlo`](grid_sampler_aten_kernels.cc.md#BuildGridSamplerBicubicBackwardShlo), [`ComputeBuildBilinearScatterIndicesForCorner`](grid_sampler_aten_kernels.cc.md#ComputeBuildBilinearScatterIndicesForCorner), [`BuildGridSamplerBilinearBackwardShlo`](grid_sampler_aten_kernels.cc.md#BuildGridSamplerBilinearBackwardShlo), [`AccumulateBicubicInterpolation`](grid_sampler_aten_kernels.cc.md#AccumulateBicubicInterpolation), [`BuildGridSamplerNearestShlo`](grid_sampler_aten_kernels.cc.md#BuildGridSamplerNearestShlo), [`UpdateIndicesForPaddingMode`](grid_sampler_aten_kernels.cc.md#UpdateIndicesForPaddingMode), [`AccumulateBilinearInterpolation2D`](grid_sampler_aten_kernels.cc.md#AccumulateBilinearInterpolation2D), [`BuildBilinearScatterIndices`](grid_sampler_aten_kernels.cc.md#BuildBilinearScatterIndices), [`AccumulateBilinearInterpolation3D`](grid_sampler_aten_kernels.cc.md#AccumulateBilinearInterpolation3D), [`BuildGridSamplerBilinearShlo`](grid_sampler_aten_kernels.cc.md#BuildGridSamplerBilinearShlo), [`BuildGridSamplerNearestBackwardShlo`](grid_sampler_aten_kernels.cc.md#BuildGridSamplerNearestBackwardShlo), [`ComputeCubicDimInfo`](grid_sampler_aten_kernels.cc.md#ComputeCubicDimInfo), [`ComputeSourceCoord`](grid_sampler_aten_kernels.cc.md#ComputeSourceCoord), [`AccumulateBilinearInterpolation`](grid_sampler_aten_kernels.cc.md#AccumulateBilinearInterpolation), [`CalculateBicubicBackwardWeightsAndIndices`](grid_sampler_aten_kernels.cc.md#CalculateBicubicBackwardWeightsAndIndices), [`ComputeGradInputOperandsForCorner`](grid_sampler_aten_kernels.cc.md#ComputeGradInputOperandsForCorner)

## Functions
- <a id="AccumulateBicubicInterpolation"></a>`AccumulateBicubicInterpolation(mlir::MlirBuilder& builder, mlir::MlirOp input, const std::vector<CubicDimInfo>& dim_infos, const std::vector<mlir::MlirOp>& grid_coords, const GridSamplerGatherConfig& gather_config, int64_t spatial_dim_size, PaddingMode padding_mode, mlir::Type calc_type)` — [`L668`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L668)
- `AccumulateBicubicInterpolation(mlir::MlirBuilder& builder, mlir::MlirOp input, const std::vector<CubicDimInfo>& dim_infos, const std::vector<mlir::MlirOp>& grid_coords, const GridSamplerGatherConfig& gather_config, int64_t spatial_dim_size, PaddingMode padding_mode, mlir::Type calc_type)` — [`L668`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L668)
- <a id="AccumulateBilinearInterpolation"></a>`AccumulateBilinearInterpolation(mlir::MlirBuilder& builder, const mlir::MlirOp input, const std::vector<DimInfo>& dim_infos, const GridSamplerGatherConfig& gather_config, const int64_t spatial_dim_size, PaddingMode padding_mode, mlir::Type calc_type)` — [`L489`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L489)
- `AccumulateBilinearInterpolation(mlir::MlirBuilder& builder, const mlir::MlirOp input, const std::vector<DimInfo>& dim_infos, const GridSamplerGatherConfig& gather_config, const int64_t spatial_dim_size, PaddingMode padding_mode, mlir::Type calc_type)` — [`L489`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L489)
- `AccumulateBilinearInterpolation2D(mlir::MlirBuilder& builder, mlir::MlirOp input, const std::vector<DimInfo>& dim_infos, const GridSamplerGatherConfig& gather_config, PaddingMode padding_mode, mlir::Type calc_type)` — [`L386`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L386)
- <a id="AccumulateBilinearInterpolation2D"></a>`AccumulateBilinearInterpolation2D(mlir::MlirBuilder& builder, mlir::MlirOp input, const std::vector<DimInfo>& dim_infos, const GridSamplerGatherConfig& gather_config, PaddingMode padding_mode, mlir::Type calc_type)` — [`L386`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L386)
- <a id="AccumulateBilinearInterpolation3D"></a>`AccumulateBilinearInterpolation3D(mlir::MlirBuilder& builder, mlir::MlirOp input, const std::vector<DimInfo>& dim_infos, const GridSamplerGatherConfig& gather_config, PaddingMode padding_mode, mlir::Type calc_type)` — [`L434`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L434)
- `AccumulateBilinearInterpolation3D(mlir::MlirBuilder& builder, mlir::MlirOp input, const std::vector<DimInfo>& dim_infos, const GridSamplerGatherConfig& gather_config, PaddingMode padding_mode, mlir::Type calc_type)` — [`L434`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L434)
- <a id="ApplyZeroPadding"></a>`ApplyZeroPadding(mlir::MlirBuilder& builder, mlir::MlirOp gathered, const std::vector<mlir::MlirOp>& indices_unclamped, const mlir::stablehlo::Dimensions& input_shape, int64_t spatial_dim_size, mlir::Type calc_type, const Dimensions& bcast_dims)` — [`L313`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L313)
- `ApplyZeroPadding(mlir::MlirBuilder& builder, mlir::MlirOp gathered, const std::vector<mlir::MlirOp>& indices_unclamped, const mlir::stablehlo::Dimensions& input_shape, int64_t spatial_dim_size, mlir::Type calc_type, const Dimensions& bcast_dims)` — [`L313`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L313)
- <a id="AtenGridSampler2d"></a>`AtenGridSampler2d(const at::Tensor& input, const at::Tensor& grid, int64_t interpolation_mode, int64_t padding_mode, bool align_corners)` — [`L1965`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1965)
- <a id="AtenGridSampler2dBackward"></a>`AtenGridSampler2dBackward(const at::Tensor& grad_output, const at::Tensor& input, const at::Tensor& grid, int64_t interpolation_mode, int64_t padding_mode, bool align_corners, std::array<bool, 2> output_mask)` — [`L2066`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L2066)
- <a id="AtenGridSampler3d"></a>`AtenGridSampler3d(const at::Tensor& input, const at::Tensor& grid, int64_t interpolation_mode, int64_t padding_mode, bool align_corners)` — [`L2018`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L2018)
- <a id="AtenGridSampler3dBackward"></a>`AtenGridSampler3dBackward(const at::Tensor& grad_output, const at::Tensor& input, const at::Tensor& grid, int64_t interpolation_mode, int64_t padding_mode, bool align_corners, std::array<bool, 2> output_mask)` — [`L2134`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L2134)
- <a id="BuildBilinearScatterIndices"></a>`BuildBilinearScatterIndices(mlir::MlirBuilder& builder, mlir::MlirOp input, mlir::MlirOp grad_output, mlir::MlirOp grad_output_calc, const std::vector<DimInfo>& dim_infos, const std::vector<mlir::MlirOp>& grid_coords, const GridSamplerGatherConfig& gather_config, int64_t spatial_dim_size, PaddingMode padding_mode, mlir::Type calc_type, std::vector<mlir::MlirOp>& total_dl)` — [`L1380`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1380)
- `BuildBilinearScatterIndices(mlir::MlirBuilder& builder, mlir::MlirOp input, mlir::MlirOp grad_output, mlir::MlirOp grad_output_calc, const std::vector<DimInfo>& dim_infos, const std::vector<mlir::MlirOp>& grid_coords, const GridSamplerGatherConfig& gather_config, int64_t spatial_dim_size, PaddingMode padding_mode, mlir::Type calc_type, std::vector<mlir::MlirOp>& total_dl)` — [`L1380`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1380)
- `BuildGradGrid(mlir::MlirBuilder& builder, int64_t spatial_dim_size, mlir::stablehlo::Dimensions input_shape, int64_t offset_dim_size, mlir::Type calc_type, bool align_corners, const std::vector<mlir::MlirOp>& total_dl)` — [`L1436`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1436)
- <a id="BuildGradGrid"></a>`BuildGradGrid(mlir::MlirBuilder& builder, int64_t spatial_dim_size, mlir::stablehlo::Dimensions input_shape, int64_t offset_dim_size, mlir::Type calc_type, bool align_corners, const std::vector<mlir::MlirOp>& total_dl)` — [`L1436`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1436)
- <a id="BuildGridSamplerBicubicBackwardShlo"></a>`BuildGridSamplerBicubicBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp input, mlir::MlirOp grid, bool align_corners, PaddingMode padding_mode, bool compute_grad_input)` — [`L1909`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1909)
- <a id="BuildGridSamplerBicubicShlo"></a>`BuildGridSamplerBicubicShlo(mlir::MlirOp input, mlir::MlirOp grid, bool align_corners, PaddingMode padding_mode)` — [`L757`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L757)
- <a id="BuildGridSamplerBilinearBackwardShlo"></a>`BuildGridSamplerBilinearBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp input, mlir::MlirOp grid, bool align_corners, PaddingMode padding_mode, bool compute_grad_input)` — [`L1472`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1472)
- <a id="BuildGridSamplerBilinearShlo"></a>`BuildGridSamplerBilinearShlo(mlir::MlirOp input, mlir::MlirOp grid, bool align_corners, PaddingMode padding_mode)` — [`L823`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L823)
- <a id="BuildGridSamplerNearestBackwardShlo"></a>`BuildGridSamplerNearestBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp input, mlir::MlirOp grid, bool align_corners, PaddingMode padding_mode, bool compute_grad_input)` — [`L1057`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1057)
- <a id="BuildGridSamplerNearestShlo"></a>`BuildGridSamplerNearestShlo(mlir::MlirOp input, mlir::MlirOp grid, bool align_corners, PaddingMode padding_mode)` — [`L882`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L882)
- <a id="CalculateBicubicBackwardCorners"></a>`CalculateBicubicBackwardCorners(mlir::MlirBuilder& builder, mlir::MlirOp input, mlir::MlirOp grad_output, const BicubicWeightsAndIndices& weights_and_indices, int64_t spatial_dim_size, PaddingMode padding_mode, mlir::Type calc_type, bool compute_grad_input, int64_t rank)` — [`L1700`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1700)
- <a id="CalculateBicubicBackwardTotalDL"></a>`CalculateBicubicBackwardTotalDL(mlir::MlirBuilder& builder, mlir::MlirOp input, mlir::Type calc_type, bool compute_grad_input, int64_t rank, BicubicBackwardCornerOperands corner_results)` — [`L1868`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1868)
- <a id="CalculateBicubicBackwardWeightsAndIndices"></a>`CalculateBicubicBackwardWeightsAndIndices(mlir::MlirBuilder& builder, int64_t spatial_dim_size, Dimensions grid_shape, mlir::MlirOp grid, mlir::Type calc_type, mlir::stablehlo::Dimensions input_shape, int64_t offset_dim_size, bool align_corners, PaddingMode padding_mode)` — [`L1603`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1603)
- `CalculateBicubicBackwardWeightsAndIndices(mlir::MlirBuilder& builder, int64_t spatial_dim_size, Dimensions grid_shape, mlir::MlirOp grid, mlir::Type calc_type, mlir::stablehlo::Dimensions input_shape, int64_t offset_dim_size, bool align_corners, PaddingMode padding_mode)` — [`L1603`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1603)
- <a id="ComputeBuildBilinearScatterIndicesForCorner"></a>`ComputeBuildBilinearScatterIndicesForCorner(int corner_idx, int64_t spatial_dim_size, mlir::MlirBuilder& builder, mlir::Type calc_type, const std::vector<DimInfo>& dim_infos, mlir::MlirOp input, const GridSamplerGatherConfig& gather_config, PaddingMode padding_mode, const mlir::stablehlo::Dimensions& input_shape, Dimensions bcast_dims, mlir::MlirOp grad_output_calc, mlir::MlirOp n_iota_reshaped, mlir::MlirOp c_iota_reshaped, Dimensions grad_output_shape, mlir::Type i32_type, mlir::RankedTensorType index_reshaped_ty, int64_t rank, mlir::MlirOp one_tensor, mlir::MlirOp minus_one_tensor, const std::vector<mlir::MlirOp>& grid_coords, std::vector<mlir::MlirOp>& total_dl)` — [`L1301`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1301)
- `ComputeBuildBilinearScatterIndicesForCorner(int corner_idx, int64_t spatial_dim_size, mlir::MlirBuilder& builder, mlir::Type calc_type, const std::vector<DimInfo>& dim_infos, mlir::MlirOp input, const GridSamplerGatherConfig& gather_config, PaddingMode padding_mode, const mlir::stablehlo::Dimensions& input_shape, Dimensions bcast_dims, mlir::MlirOp grad_output_calc, mlir::MlirOp n_iota_reshaped, mlir::MlirOp c_iota_reshaped, Dimensions grad_output_shape, mlir::Type i32_type, mlir::RankedTensorType index_reshaped_ty, int64_t rank, mlir::MlirOp one_tensor, mlir::MlirOp minus_one_tensor, const std::vector<mlir::MlirOp>& grid_coords, std::vector<mlir::MlirOp>& total_dl)` — [`L1301`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1301)
- <a id="ComputeCubicDimInfo"></a>`ComputeCubicDimInfo(mlir::MlirBuilder& builder, mlir::MlirOp src_idx, mlir::MlirOp in_size, PaddingMode padding_mode, bool align_corners, mlir::Type calc_type)` — [`L591`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L591)
- <a id="ComputeDimInfo"></a>`ComputeDimInfo(mlir::MlirBuilder& builder, mlir::MlirOp src_idx, mlir::MlirOp in_size, mlir::Type calc_type)` — [`L258`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L258)
- <a id="ComputeGradInputOperandsForCorner"></a>`ComputeGradInputOperandsForCorner(mlir::MlirBuilder& builder, mlir::MlirOp gathered, mlir::MlirOp current_weight, Dimensions bcast_dims, mlir::MlirOp grad_output_calc, PaddingMode padding_mode, const std::vector<mlir::MlirOp>& indices_unclamped, const mlir::stablehlo::Dimensions& input_shape, int64_t spatial_dim_size, mlir::Type calc_type, mlir::MlirOp n_iota_reshaped, mlir::MlirOp c_iota_reshaped, const std::vector<mlir::MlirOp>& current_indices, Dimensions grad_output_shape, mlir::Type i32_type, mlir::RankedTensorType index_reshaped_ty, int64_t rank)` — [`L1263`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1263)
- `ComputeGradInputOperandsForCorner(mlir::MlirBuilder& builder, mlir::MlirOp gathered, mlir::MlirOp current_weight, Dimensions bcast_dims, mlir::MlirOp grad_output_calc, PaddingMode padding_mode, const std::vector<mlir::MlirOp>& indices_unclamped, const mlir::stablehlo::Dimensions& input_shape, int64_t spatial_dim_size, mlir::Type calc_type, mlir::MlirOp n_iota_reshaped, mlir::MlirOp c_iota_reshaped, const std::vector<mlir::MlirOp>& current_indices, Dimensions grad_output_shape, mlir::Type i32_type, mlir::RankedTensorType index_reshaped_ty, int64_t rank)` — [`L1263`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1263)
- <a id="ComputeSourceCoord"></a>`ComputeSourceCoord(mlir::MlirOp grid_coord, mlir::MlirOp in_size, bool align_corners, PaddingMode padding_mode, mlir::Type calc_type)` — [`L185`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L185)
- <a id="DimensionInfoToOp"></a>`DimensionInfoToOp(mlir::MlirBuilder& builder, mlir::stablehlo::DimensionInfo in_size)` — [`L126`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L126) — Convert a potentially dynamic dimension to an MLIR op.
- <a id="GatherInterpolatedValue"></a>`GatherInterpolatedValue(mlir::MlirBuilder& builder, mlir::MlirOp input_calc, const std::vector<mlir::MlirOp>& current_indices, const GridSamplerGatherConfig& gather_config)` — [`L295`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L295)
- `GatherInterpolatedValue(mlir::MlirBuilder& builder, mlir::MlirOp input_calc, const std::vector<mlir::MlirOp>& current_indices, const GridSamplerGatherConfig& gather_config)` — [`L295`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L295)
- <a id="GatherOrDynamicGather"></a>`GatherOrDynamicGather(mlir::MlirBuilder& builder, mlir::MlirOp input, mlir::MlirOp index_tensor, const GridSamplerGatherConfig& gather_config, bool indices_are_sorted)` — [`L140`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L140)
- <a id="GetBilinearDimInfo"></a>`GetBilinearDimInfo(DimInfo dim_info, int bit)` — [`L371`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L371)
- <a id="GetGridSamplerGatherConfig"></a>`GetGridSamplerGatherConfig(mlir::MlirOp input, int64_t spatial_dim_size)` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L85)
- <a id="ReshapeIndexTo2D"></a>`ReshapeIndexTo2D(mlir::MlirOp index)` — [`L70`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L70)
- <a id="UpdateIndicesForPaddingMode"></a>`UpdateIndicesForPaddingMode(mlir::MlirBuilder& builder, const PaddingMode padding_mode, CubicDimInfo& info, mlir::MlirOp src_idx, mlir::MlirOp in_size, mlir::MlirOp in_size_minus_1_i32, bool align_corners, mlir::MlirOp one_i32, mlir::MlirOp zero_i32)` — [`L515`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L515)
- <a id="Validate2DInterpolationMode"></a>`Validate2DInterpolationMode(const InterpolationMode interpolation_mode)` — [`L1031`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1031) — Checks for the `interpolation_mode` argument for 2D grid sampler.
- <a id="Validate3DInterpolationMode"></a>`Validate3DInterpolationMode(const InterpolationMode interpolation_mode)` — [`L1045`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1045) — Checks for the `interpolation_mode` argument for 3D grid sampler.
- <a id="ValidateInputAndPaddingMode"></a>`ValidateInputAndPaddingMode(const at::Tensor& input, const int64_t padding_mode)` — [`L1015`](../../../../../../../raw/code/torch_tpu/csrc/ops/grid_sampler/grid_sampler_aten_kernels.cc#L1015) — Checks for the `input` and `padding_mode` arguments.

