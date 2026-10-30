---
title: 'Module: csrc/ops/slice_scatter/slice_scatter_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/slice_scatter/slice_scatter_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenSliceScatterOut: AtenSliceScatterOut(f0afa432354f432b).
  AtenSliceScatter: AtenSliceScatter(73b78eeee127a89c).
  BuildSliceScatterShlo: '`$anonymous_namespace_csrc/ops/slice_scatter/slice_scatter_aten_kernels.cc`/BuildSliceScatterShlo(dcba75946ec08912).'
  BuildStridedSliceScatterShlo: '`$anonymous_namespace_csrc/ops/slice_scatter/slice_scatter_aten_kernels.cc`/BuildStridedSliceScatterShlo(dcba75946ec08912).'
  BuildBoundaryConcatenateSliceScatterShlo: '`$anonymous_namespace_csrc/ops/slice_scatter/slice_scatter_aten_kernels.cc`/BuildBoundaryConcatenateSliceScatterShlo(db4488c4824596d0).'
---
# Module: [`csrc/ops/slice_scatter/slice_scatter_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/slice_scatter/slice_scatter_aten_kernels.cc)

## Functions
- <a id="AtenSliceScatter"></a>`AtenSliceScatter(const at::Tensor& self, const at::Tensor& src, int64_t dim, std::optional<int64_t> start, std::optional<int64_t> end, int64_t step)` — [`L240`](../../../../../../../raw/code/torch_tpu/csrc/ops/slice_scatter/slice_scatter_aten_kernels.cc#L240) — Implements aten::slice_scatter on TPU with direct StableHLO lowerings and
- <a id="AtenSliceScatterOut"></a>`AtenSliceScatterOut(const at::Tensor& self, const at::Tensor& src, int64_t dim, std::optional<int64_t> start, std::optional<int64_t> end, int64_t step, at::Tensor& out)` — [`L317`](../../../../../../../raw/code/torch_tpu/csrc/ops/slice_scatter/slice_scatter_aten_kernels.cc#L317) — Implements aten::slice_scatter.out on TPU with direct StableHLO lowerings and
- <a id="BuildBoundaryConcatenateSliceScatterShlo"></a>`BuildBoundaryConcatenateSliceScatterShlo(mlir::MlirOp self_op, mlir::MlirOp src_op, const Dimensions& input_sizes, const int64_t dim, const int64_t start, const int64_t end, const int64_t total_len)` — [`L139`](../../../../../../../raw/code/torch_tpu/csrc/ops/slice_scatter/slice_scatter_aten_kernels.cc#L139)
- <a id="BuildSliceScatterShlo"></a>`BuildSliceScatterShlo(mlir::MlirOp self_op, mlir::MlirOp src_op, const Dimensions& input_sizes, const int64_t dim, const int64_t start, const int64_t end, const int64_t step, const mlir::ElementType element_type)` — [`L192`](../../../../../../../raw/code/torch_tpu/csrc/ops/slice_scatter/slice_scatter_aten_kernels.cc#L192) — Builds the StableHLO graph for `aten::slice_scatter`.
- <a id="BuildStridedSliceScatterShlo"></a>`BuildStridedSliceScatterShlo(mlir::MlirOp self_op, mlir::MlirOp src_op, const Dimensions& input_sizes, const int64_t dim, const int64_t start, const int64_t step, const int64_t slice_len, const mlir::ElementType element_type)` — [`L73`](../../../../../../../raw/code/torch_tpu/csrc/ops/slice_scatter/slice_scatter_aten_kernels.cc#L73) — Builds the StableHLO graph for strided `aten::slice_scatter` (`step > 1`).

