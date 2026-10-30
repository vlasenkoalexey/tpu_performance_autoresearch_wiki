---
title: 'Module: csrc/ops/select_scatter/select_scatter_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/select_scatter/select_scatter_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenSelectScatterOut: AtenSelectScatterOut(9f3ca845d33a007a).
  AtenSelectScatter: AtenSelectScatter(1bdf6ba18803ff10).
  BuildSelectScatterShlo: '`$anonymous_namespace_csrc/ops/select_scatter/select_scatter_aten_kernels.cc`/BuildSelectScatterShlo(22386da5209308fc).'
---
# Module: [`csrc/ops/select_scatter/select_scatter_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/select_scatter/select_scatter_aten_kernels.cc)

## Functions
- <a id="AtenSelectScatter"></a>`AtenSelectScatter(const at::Tensor& self, const at::Tensor& src, int64_t dim, int64_t index)` — [`L91`](../../../../../../../raw/code/torch_tpu/csrc/ops/select_scatter/select_scatter_aten_kernels.cc#L91) — Implements aten::select_scatter on TPU by lowering directly to StableHLO:
- <a id="AtenSelectScatterOut"></a>`AtenSelectScatterOut(const at::Tensor& self, const at::Tensor& src, int64_t dim, int64_t index, at::Tensor& out)` — [`L147`](../../../../../../../raw/code/torch_tpu/csrc/ops/select_scatter/select_scatter_aten_kernels.cc#L147) — Implements aten::select_scatter.out on TPU with direct StableHLO lowerings
- <a id="BuildSelectScatterShlo"></a>`BuildSelectScatterShlo(mlir::MlirOp self_op, mlir::MlirOp src_op, const Dimensions& input_sizes, const int64_t dim, const int64_t index)` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/select_scatter/select_scatter_aten_kernels.cc#L54) — Builds the StableHLO graph for `aten::select_scatter`.

