---
title: 'Module: csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenScaledMmV2: AtenScaledMmV2(87e26bfc84a8e5e6).
  AtenScaledMm: AtenScaledMm(b5e6365a17b93b).
  AtenScaledMmOut: AtenScaledMmOut(e5b657a0d9c23a41).
  AtenScaledMmV2Out: AtenScaledMmV2Out(b12608b498fb74eb).
  ValidateScaledMmV2Inputs: '`$anonymous_namespace_csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`/ValidateScaledMmV2Inputs(ae355ea8c5ada94).'
  ValidateScaledMmInputs: '`$anonymous_namespace_csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`/ValidateScaledMmInputs(dc2a7ea36858f778).'
  BuildUnswizzle: '`$anonymous_namespace_csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`/BuildUnswizzle(fa912ff7c8bd4af3).'
  ScaledMmV2Out: ScaledMmV2Out(f83e8a7654ec5541).
  ScaledMmOut: '`$anonymous_namespace_csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`/ScaledMmOut(4ad63e994057dc77).'
  BuildScaledMmV2Shlo: '`$anonymous_namespace_csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`/BuildScaledMmV2Shlo(d93149b00ec922ea).'
  BuildDequantizeBlockWise32: '`$anonymous_namespace_csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`/BuildDequantizeBlockWise32(4ae25f1542594282).'
  BuildStablehloDotGeneral: '`$anonymous_namespace_csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`/BuildStablehloDotGeneral(165b6c237c5ec236).'
  BuildScaledMmShlo: '`$anonymous_namespace_csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`/BuildScaledMmShlo(a7da08f33ea0c4e).'
  ApplyScalesAndBias: '`$anonymous_namespace_csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`/ApplyScalesAndBias(556441ba80fc908a).'
  GetScaledMmOpBuilder: '`$anonymous_namespace_csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`/GetScaledMmOpBuilder(8c19d74478cdf01a).'
  ReshapeScaleIfNeeded: '`$anonymous_namespace_csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`/ReshapeScaleIfNeeded(8417f6002b1ef712).'
  SwizzledScaleNumel: '`$anonymous_namespace_csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`/SwizzledScaleNumel(d0a0e4c270da0eca).'
  Operand.kRhs: '`$anonymous_namespace_csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`/Operand#kRhs.'
  Operand: '`$anonymous_namespace_csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`/Operand#'
  BuildScaledMmInputs: '`$anonymous_namespace_csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`/BuildScaledMmInputs(11dcdbe8cc63a54d).'
  Operand.kLhs: '`$anonymous_namespace_csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`/Operand#kLhs.'
---
# Module: [`csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc)

## Classes
### <a id="Operand"></a>`Operand`
- def: [`csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc:60`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L60)
- signature: `enum class Operand`
- members:
  - <a id="Operand.kLhs"></a>`kLhs` — [`L60`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L60)
  - <a id="Operand.kRhs"></a>`kRhs` — [`L60`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L60)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildUnswizzle`](scaled_mm_aten_kernels.cc.md#BuildUnswizzle), [`BuildScaledMmV2Shlo`](scaled_mm_aten_kernels.cc.md#BuildScaledMmV2Shlo), [`BuildDequantizeBlockWise32`](scaled_mm_aten_kernels.cc.md#BuildDequantizeBlockWise32)

## Functions
- <a id="ApplyScalesAndBias"></a>`ApplyScalesAndBias(mlir::MlirOp mm_result, mlir::MlirOp scale_a, bool apply_scale_a, mlir::MlirOp scale_b, bool apply_scale_b, std::optional<mlir::MlirOp> bias, std::optional<mlir::Type> out_dtype)` — [`L486`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L486)
- <a id="AtenScaledMm"></a>`AtenScaledMm(const at::Tensor& self, const at::Tensor& mat2, const at::Tensor& scale_a, const at::Tensor& scale_b, const std::optional<at::Tensor>& bias, const std::optional<at::Tensor>& scale_result, std::optional<at::ScalarType> out_dtype, bool use_fast_accum)` — [`L730`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L730)
- <a id="AtenScaledMmOut"></a>`AtenScaledMmOut(const at::Tensor& self, const at::Tensor& mat2, const at::Tensor& scale_a, const at::Tensor& scale_b, const std::optional<at::Tensor>& bias, const std::optional<at::Tensor>& scale_result, std::optional<at::ScalarType> out_dtype, bool use_fast_accum, at::Tensor& out)` — [`L754`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L754)
- <a id="AtenScaledMmV2"></a>`AtenScaledMmV2(const at::Tensor& self, const at::Tensor& mat2, at::TensorList scale_a, at::IntArrayRef recipe_a, at::IntArrayRef swizzle_a, at::TensorList scale_b, at::IntArrayRef recipe_b, at::IntArrayRef swizzle_b, const std::optional<at::Tensor>& bias, std::optional<at::ScalarType> out_dtype, at::IntArrayRef contraction_dim, bool use_fast_accum)` — [`L874`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L874)
- <a id="AtenScaledMmV2Out"></a>`AtenScaledMmV2Out(const at::Tensor& self, const at::Tensor& mat2, at::TensorList scale_a, at::IntArrayRef recipe_a, at::IntArrayRef swizzle_a, at::TensorList scale_b, at::IntArrayRef recipe_b, at::IntArrayRef swizzle_b, const std::optional<at::Tensor>& bias, std::optional<at::ScalarType> out_dtype, at::IntArrayRef contraction_dim, bool use_fast_accum, at::Tensor& out)` — [`L911`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L911)
- <a id="BuildDequantizeBlockWise32"></a>`BuildDequantizeBlockWise32(mlir::MlirOp input, mlir::MlirOp scale, Operand operand)` — [`L436`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L436)
- `BuildScaledMmInputs(const at::Tensor& self, const at::Tensor& mat2, const at::Tensor& scale_a, const at::Tensor& scale_b, const std::optional<at::Tensor>& bias, const std::optional<at::Tensor>& scale_result, bool has_bias, bool has_scale_result)` — [`L670`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L670)
- <a id="BuildScaledMmInputs"></a>`BuildScaledMmInputs(const at::Tensor& self, const at::Tensor& mat2, const at::Tensor& scale_a, const at::Tensor& scale_b, const std::optional<at::Tensor>& bias, const std::optional<at::Tensor>& scale_result, bool has_bias, bool has_scale_result)` — [`L670`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L670)
- <a id="BuildScaledMmShlo"></a>`BuildScaledMmShlo(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::MlirOp scale_a, mlir::MlirOp scale_b, std::optional<mlir::MlirOp> bias, std::optional<mlir::MlirOp> scale_result, std::optional<mlir::Type> out_dtype, mlir::stablehlo::Precision precision)` — [`L113`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L113) — Builds the StableHLO operations for scaled matrix multiplication.
- `BuildScaledMmShlo(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::MlirOp scale_a, mlir::MlirOp scale_b, std::optional<mlir::MlirOp> bias, std::optional<mlir::MlirOp> scale_result, std::optional<mlir::Type> out_dtype, mlir::stablehlo::Precision precision)` — [`L113`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L113) — Builds the StableHLO operations for scaled matrix multiplication.
- <a id="BuildScaledMmV2Shlo"></a>`BuildScaledMmV2Shlo(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::MlirOp scale_a, mlir::MlirOp scale_b, std::optional<mlir::MlirOp> bias, std::optional<mlir::Type> out_dtype, mlir::stablehlo::Precision precision, at::blas::ScalingType scaling_a, at::blas::ScalingType scaling_b, at::blas::SwizzleType swiz_a, at::blas::SwizzleType swiz_b)` — [`L532`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L532)
- `BuildScaledMmV2Shlo(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::MlirOp scale_a, mlir::MlirOp scale_b, std::optional<mlir::MlirOp> bias, std::optional<mlir::Type> out_dtype, mlir::stablehlo::Precision precision, at::blas::ScalingType scaling_a, at::blas::ScalingType scaling_b, at::blas::SwizzleType swiz_a, at::blas::SwizzleType swiz_b)` — [`L532`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L532)
- `BuildStablehloDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::Precision precision)` — [`L62`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L62)
- <a id="BuildStablehloDotGeneral"></a>`BuildStablehloDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::Precision precision)` — [`L62`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L62)
- <a id="BuildUnswizzle"></a>`BuildUnswizzle(mlir::MlirOp scale, Operand operand, int64_t outer, int64_t k_logical)` — [`L366`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L366) — Unswizzles a SWIZZLE_32_4_4 block-scale buffer back to its logical shape.
- `GetScaledMmOpBuilder(bool has_bias, bool has_scale_result, mlir::ElementType target_elem_dtype, mlir::stablehlo::Precision current_precision)` — [`L640`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L640)
- <a id="GetScaledMmOpBuilder"></a>`GetScaledMmOpBuilder(bool has_bias, bool has_scale_result, mlir::ElementType target_elem_dtype, mlir::stablehlo::Precision current_precision)` — [`L640`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L640)
- <a id="ReshapeScaleIfNeeded"></a>`ReshapeScaleIfNeeded(mlir::MlirOp scale, const Dimensions& target)` — [`L90`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L90)
- <a id="ScaledMmOut"></a>`ScaledMmOut(const at::Tensor& self, const at::Tensor& mat2, const at::Tensor& scale_a, const at::Tensor& scale_b, std::optional<at::Tensor> bias, std::optional<at::Tensor> scale_result, std::optional<at::ScalarType> out_dtype, bool use_fast_accum, OpParamCacheKeys param_keys, at::Tensor& out)` — [`L685`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L685)
- <a id="ScaledMmV2Out"></a>`ScaledMmV2Out(const at::Tensor& self, const at::Tensor& mat2, at::TensorList scale_a, at::IntArrayRef recipe_a, at::IntArrayRef swizzle_a, at::TensorList scale_b, at::IntArrayRef recipe_b, at::IntArrayRef swizzle_b, std::optional<at::Tensor> bias, std::optional<at::ScalarType> out_dtype, at::IntArrayRef contraction_dim, bool use_fast_accum, OpParamCacheKeys param_keys, at::Tensor& out)` — [`L783`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L783)
- <a id="SwizzledScaleNumel"></a>`SwizzledScaleNumel(int64_t outer, int64_t k_logical)` — [`L198`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L198) — SWIZZLE_32_4_4 requires fixed 128x4 hardware tiles (interleaving
- <a id="ValidateScaledMmInputs"></a>`ValidateScaledMmInputs(const at::Tensor& self, const at::Tensor& mat2, const at::Tensor& scale_a, const at::Tensor& scale_b, const std::optional<at::Tensor>& bias, const std::optional<at::Tensor>& scale_result, bool use_fast_accum)` — [`L586`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L586)
- <a id="ValidateScaledMmV2Inputs"></a>`ValidateScaledMmV2Inputs(const at::Tensor& self, const at::Tensor& mat2, at::TensorList scale_a, at::IntArrayRef recipe_a, at::IntArrayRef swizzle_a, at::TensorList scale_b, at::IntArrayRef recipe_b, at::IntArrayRef swizzle_b, const std::optional<at::Tensor>& bias, std::optional<at::ScalarType> out_dtype, at::IntArrayRef contraction_dim, bool use_fast_accum)` — [`L213`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_mm/scaled_mm_aten_kernels.cc#L213)

