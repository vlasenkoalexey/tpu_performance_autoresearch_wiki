---
title: 'Module: csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenScaledGroupedMm: AtenScaledGroupedMm(46edff3ab6766984).
  AtenGroupedMm: AtenGroupedMm(f526039e9b635281).
  ScaledGroupedMm: '`$anonymous_namespace_csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc`/ScaledGroupedMm(a6f0e97263126b95).'
  BuildScaledGroupedMmShlo: '`$anonymous_namespace_csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc`/BuildScaledGroupedMmShlo(2d06ea940a577b44).'
  GroupedMm: '`$anonymous_namespace_csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc`/GroupedMm(ec8695e11e7b99de).'
  ValidateGroupedMmInputs: '`$anonymous_namespace_csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc`/ValidateGroupedMmInputs(4129d4059fade77c).'
  GetGroupedMmOutputSize: '`$anonymous_namespace_csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc`/GetGroupedMmOutputSize(4563eb95ee0463c3).'
  BuildGroupedMmShlo: '`$anonymous_namespace_csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc`/BuildGroupedMmShlo(47d2739075c1e0d8).'
  IsScalar: '`$anonymous_namespace_csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc`/IsScalar(b580d0b7e29ca914).'
---
# Module: [`csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc)

## Functions
- <a id="AtenGroupedMm"></a>`AtenGroupedMm(const at::Tensor& self, const at::Tensor& mat2, const std::optional<at::Tensor>& offs, const std::optional<at::Tensor>& bias, std::optional<at::ScalarType> out_dtype)` — [`L582`](../../../../../../../raw/code/torch_tpu/csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc#L582)
- <a id="AtenScaledGroupedMm"></a>`AtenScaledGroupedMm(const at::Tensor& self, const at::Tensor& mat2, const at::Tensor& scale_a, const at::Tensor& scale_b, const std::optional<at::Tensor>& offs, const std::optional<at::Tensor>& bias, const std::optional<at::Tensor>& scale_result, std::optional<at::ScalarType> out_dtype, bool use_fast_accum)` — [`L595`](../../../../../../../raw/code/torch_tpu/csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc#L595)
- `BuildGroupedMmShlo(mlir::MlirOp self_op, mlir::MlirOp mat2_op, std::optional<mlir::MlirOp> offs_op, mlir::ElementType out_dtype, mlir::stablehlo::Precision precision)` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc#L100) — Lowers grouped matmul to MLIR StableHLO/CHLO.
- <a id="BuildGroupedMmShlo"></a>`BuildGroupedMmShlo(mlir::MlirOp self_op, mlir::MlirOp mat2_op, std::optional<mlir::MlirOp> offs_op, mlir::ElementType out_dtype, mlir::stablehlo::Precision precision)` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc#L100) — Lowers grouped matmul to MLIR StableHLO/CHLO.
- `BuildScaledGroupedMmShlo(mlir::MlirOp self_op, mlir::MlirOp mat2_op, mlir::MlirOp scale_a, mlir::MlirOp scale_b, std::optional<mlir::MlirOp> offs_op, std::optional<mlir::MlirOp> bias, std::optional<mlir::MlirOp> scale_result, mlir::ElementType out_dtype, mlir::stablehlo::Precision precision)` — [`L260`](../../../../../../../raw/code/torch_tpu/csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc#L260)
- <a id="BuildScaledGroupedMmShlo"></a>`BuildScaledGroupedMmShlo(mlir::MlirOp self_op, mlir::MlirOp mat2_op, mlir::MlirOp scale_a, mlir::MlirOp scale_b, std::optional<mlir::MlirOp> offs_op, std::optional<mlir::MlirOp> bias, std::optional<mlir::MlirOp> scale_result, mlir::ElementType out_dtype, mlir::stablehlo::Precision precision)` — [`L260`](../../../../../../../raw/code/torch_tpu/csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc#L260)
- <a id="GetGroupedMmOutputSize"></a>`GetGroupedMmOutputSize(const at::Tensor& self, const at::Tensor& mat2, const std::optional<at::Tensor>& offs)` — [`L401`](../../../../../../../raw/code/torch_tpu/csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc#L401)
- <a id="GroupedMm"></a>`GroupedMm(const at::Tensor& self, const at::Tensor& mat2, const std::optional<at::Tensor>& offs, const std::optional<at::Tensor>& bias, std::optional<at::ScalarType> out_dtype, OpParamCacheKeys& param_keys)` — [`L456`](../../../../../../../raw/code/torch_tpu/csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc#L456)
- <a id="IsScalar"></a>`IsScalar(const at::Tensor& t)` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc#L59)
- <a id="ScaledGroupedMm"></a>`ScaledGroupedMm(const at::Tensor& self, const at::Tensor& mat2, const at::Tensor& scale_a, const at::Tensor& scale_b, const std::optional<at::Tensor>& offs, const std::optional<at::Tensor>& bias, const std::optional<at::Tensor>& scale_result, std::optional<at::ScalarType> out_dtype, bool use_fast_accum, OpParamCacheKeys& param_keys)` — [`L504`](../../../../../../../raw/code/torch_tpu/csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc#L504)
- <a id="ValidateGroupedMmInputs"></a>`ValidateGroupedMmInputs(const at::Tensor& self, const at::Tensor& mat2, const std::optional<at::Tensor>& offs, const std::optional<at::Tensor>& bias, std::optional<at::ScalarType> out_dtype)` — [`L351`](../../../../../../../raw/code/torch_tpu/csrc/ops/grouped_mm/grouped_mm_aten_kernels.cc#L351) — Validates the `_grouped_mm` inputs that can be checked without looking at

