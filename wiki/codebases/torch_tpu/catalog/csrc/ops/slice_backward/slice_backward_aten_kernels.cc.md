---
title: 'Module: csrc/ops/slice_backward/slice_backward_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/slice_backward/slice_backward_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenSliceBackward: AtenSliceBackward(fa5b2e086c069394).
  AtenSelectBackward: AtenSelectBackward(8d8c1ff7a6f1d592).
  BuildSliceBackwardShlo: '`$anonymous_namespace_csrc/ops/slice_backward/slice_backward_aten_kernels.cc`/BuildSliceBackwardShlo(1704595f26caac0c).'
  BuildSelectBackwardShlo: '`$anonymous_namespace_csrc/ops/slice_backward/slice_backward_aten_kernels.cc`/BuildSelectBackwardShlo(1350d441ee8160d2).'
  BuildUnitStrideSliceBackwardShlo: '`$anonymous_namespace_csrc/ops/slice_backward/slice_backward_aten_kernels.cc`/BuildUnitStrideSliceBackwardShlo(8ba65935470598d9).'
  BuildStridedSliceBackwardShlo: '`$anonymous_namespace_csrc/ops/slice_backward/slice_backward_aten_kernels.cc`/BuildStridedSliceBackwardShlo(8ba65935470598d9).'
---
# Module: [`csrc/ops/slice_backward/slice_backward_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/slice_backward/slice_backward_aten_kernels.cc)

## Functions
- <a id="AtenSelectBackward"></a>`AtenSelectBackward(const at::Tensor& grad_output, at::IntArrayRef input_sizes, int64_t dim, int64_t index)` — [`L309`](../../../../../../../raw/code/torch_tpu/csrc/ops/slice_backward/slice_backward_aten_kernels.cc#L309) — Implements aten::select_backward on TPU by lowering directly to a single
- <a id="AtenSliceBackward"></a>`AtenSliceBackward(const at::Tensor& grad_output, at::IntArrayRef input_sizes, int64_t dim, int64_t start, int64_t end, int64_t step)` — [`L357`](../../../../../../../raw/code/torch_tpu/csrc/ops/slice_backward/slice_backward_aten_kernels.cc#L357) — Implements aten::slice_backward on TPU by lowering directly to StableHLO:
- <a id="BuildSelectBackwardShlo"></a>`BuildSelectBackwardShlo(mlir::MlirOp grad_op, const Dimensions& input_sizes, const int64_t dim, const int64_t index, const mlir::ElementType element_type)` — [`L57`](../../../../../../../raw/code/torch_tpu/csrc/ops/slice_backward/slice_backward_aten_kernels.cc#L57) — Builds the StableHLO graph for `aten::select_backward`.
- <a id="BuildSliceBackwardShlo"></a>`BuildSliceBackwardShlo(mlir::MlirOp grad_op, const Dimensions& input_sizes, const int64_t dim, const int64_t start, const int64_t end, const int64_t step, const mlir::ElementType element_type)` — [`L262`](../../../../../../../raw/code/torch_tpu/csrc/ops/slice_backward/slice_backward_aten_kernels.cc#L262) — Builds the StableHLO graph for `aten::slice_backward`.
- <a id="BuildStridedSliceBackwardShlo"></a>`BuildStridedSliceBackwardShlo(mlir::MlirOp grad_op, mlir::MlirOp zero_scalar, const Dimensions& input_sizes, const int64_t dim, const int64_t start, const int64_t step)` — [`L162`](../../../../../../../raw/code/torch_tpu/csrc/ops/slice_backward/slice_backward_aten_kernels.cc#L162) — Helper for strided (`step > 1`, `grad_len > 1`) `slice_backward` lowerings.
- <a id="BuildUnitStrideSliceBackwardShlo"></a>`BuildUnitStrideSliceBackwardShlo(mlir::MlirOp grad_op, mlir::MlirOp zero_scalar, const Dimensions& input_sizes, const int64_t dim, const int64_t start, const int64_t end)` — [`L99`](../../../../../../../raw/code/torch_tpu/csrc/ops/slice_backward/slice_backward_aten_kernels.cc#L99) — Helper for unit-stride (`step == 1`) `slice_backward` lowerings.

