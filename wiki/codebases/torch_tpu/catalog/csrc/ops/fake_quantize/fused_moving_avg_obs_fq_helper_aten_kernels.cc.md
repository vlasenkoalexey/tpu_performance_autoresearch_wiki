---
title: 'Module: csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  FusedMovingAvgObsFqHelper: FusedMovingAvgObsFqHelper(7f2f47a5ab53b098).
  FusedMovingAvgObsFqHelperImpl: '`$anonymous_namespace_csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc`/FusedMovingAvgObsFqHelperImpl(293dfa8c1384eb9d).'
  ValidateFusedMovingAvgObsFqInputs: '`$anonymous_namespace_csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc`/ValidateFusedMovingAvgObsFqInputs(aa5d49057e097604).'
  BuildMinMaxObservationShlo: '`$anonymous_namespace_csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc`/BuildMinMaxObservationShlo(4c7332903f65f34a).'
  BuildFakeQuantizeAndMaskShlo: '`$anonymous_namespace_csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc`/BuildFakeQuantizeAndMaskShlo(bbdab4435c3e869e).'
  BuildFusedMovingAvgObsFqHelperShlo: '`$anonymous_namespace_csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc`/BuildFusedMovingAvgObsFqHelperShlo(40782e0c33bc3fd8).'
  BuildChooseQParamsShlo: '`$anonymous_namespace_csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc`/BuildChooseQParamsShlo(553885657c1ddc1f).'
---
# Module: [`csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc)

## Functions
- <a id="BuildChooseQParamsShlo"></a>`BuildChooseQParamsShlo(mlir::MlirOp min_op, mlir::MlirOp max_op, mlir::MlirOp scale_op, mlir::MlirOp zero_point_op, mlir::MlirOp fake_quant_on_op, int64_t quant_min, int64_t quant_max, bool symmetric_quant, bool is_uninitialized_observer)` — [`L174`](../../../../../../../raw/code/torch_tpu/csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc#L174) — Builds the StableHLO graph for computing quantization scale and zero point
- <a id="BuildFakeQuantizeAndMaskShlo"></a>`BuildFakeQuantizeAndMaskShlo(mlir::MlirOp self_op, mlir::MlirOp scale_op, mlir::MlirOp zero_point_op, mlir::MlirOp fake_quant_on_op, int64_t quant_min, int64_t quant_max, int64_t norm_ch_axis, bool per_row_fake_quant)` — [`L309`](../../../../../../../raw/code/torch_tpu/csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc#L309) — Builds the StableHLO graph for fake quantization and boolean mask generation.
- <a id="BuildFusedMovingAvgObsFqHelperShlo"></a>`BuildFusedMovingAvgObsFqHelperShlo(FixedSizeSpan<mlir::MlirOp, 7> inputs, double averaging_const, int64_t quant_min, int64_t quant_max, int64_t norm_ch_axis, bool per_row_fake_quant, bool symmetric_quant, bool is_uninitialized_observer)` — [`L397`](../../../../../../../raw/code/torch_tpu/csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc#L397) — Master StableHLO builder composing min/max observation, qparam calculation,
- `BuildFusedMovingAvgObsFqHelperShlo(FixedSizeSpan<mlir::MlirOp, 7> inputs, double averaging_const, int64_t quant_min, int64_t quant_max, int64_t norm_ch_axis, bool per_row_fake_quant, bool symmetric_quant, bool is_uninitialized_observer)` — [`L397`](../../../../../../../raw/code/torch_tpu/csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc#L397) — Master StableHLO builder composing min/max observation, qparam calculation,
- <a id="BuildMinMaxObservationShlo"></a>`BuildMinMaxObservationShlo(mlir::MlirOp self_op, mlir::MlirOp observer_on_op, mlir::MlirOp running_min_op, mlir::MlirOp running_max_op, double averaging_const, int64_t norm_ch_axis, bool per_row_fake_quant, bool is_uninitialized_observer)` — [`L82`](../../../../../../../raw/code/torch_tpu/csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc#L82) — Builds the StableHLO graph for updating running min and max using exponential
- <a id="FusedMovingAvgObsFqHelper"></a>`FusedMovingAvgObsFqHelper(const at::Tensor& self, const at::Tensor& observer_on, const at::Tensor& fake_quant_on, at::Tensor& running_min, at::Tensor& running_max, at::Tensor& scale, at::Tensor& zero_point, double averaging_const, int64_t quant_min, int64_t quant_max, int64_t ch_axis, bool per_row_fake_quant, bool symmetric_quant)` — [`L520`](../../../../../../../raw/code/torch_tpu/csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc#L520)
- <a id="FusedMovingAvgObsFqHelperImpl"></a>`FusedMovingAvgObsFqHelperImpl(const at::Tensor& self, const at::Tensor& observer_on, const at::Tensor& fake_quant_on, at::Tensor& running_min, at::Tensor& running_max, at::Tensor& scale, at::Tensor& zero_point, double averaging_const, int64_t quant_min, int64_t quant_max, int64_t norm_ch_axis, bool per_row_fake_quant, bool symmetric_quant, OpParamCacheKeys param_keys)` — [`L446`](../../../../../../../raw/code/torch_tpu/csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc#L446)
- <a id="ValidateFusedMovingAvgObsFqInputs"></a>`ValidateFusedMovingAvgObsFqInputs(const at::Tensor& self, int64_t quant_min, int64_t quant_max, int64_t ch_axis, bool per_row_fake_quant)` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/fake_quantize/fused_moving_avg_obs_fq_helper_aten_kernels.cc#L59) — Validates input tensor preconditions and normalizes ch_axis.

