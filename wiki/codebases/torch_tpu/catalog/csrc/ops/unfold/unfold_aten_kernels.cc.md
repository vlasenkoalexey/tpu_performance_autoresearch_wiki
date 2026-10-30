---
title: 'Module: csrc/ops/unfold/unfold_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/unfold/unfold_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenUnfold: AtenUnfold(7c68d6e1d5203f3e).
  AtenUnfoldBackward: AtenUnfoldBackward(f52c9033c78ae89b).
  BuildUnfoldBackwardShlo: '`$anonymous_namespace_csrc/ops/unfold/unfold_aten_kernels.cc`/BuildUnfoldBackwardShlo(6e110353d679d902).'
---
# Module: [`csrc/ops/unfold/unfold_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/unfold/unfold_aten_kernels.cc)

## Functions
- <a id="AtenUnfold"></a>`AtenUnfold(const at::Tensor& self, int64_t dimension, int64_t size, int64_t step)` — [`L155`](../../../../../../../raw/code/torch_tpu/csrc/ops/unfold/unfold_aten_kernels.cc#L155)
- <a id="AtenUnfoldBackward"></a>`AtenUnfoldBackward(const at::Tensor& grad_in, at::IntArrayRef input_sizes, int64_t dimension, int64_t size, int64_t step)` — [`L213`](../../../../../../../raw/code/torch_tpu/csrc/ops/unfold/unfold_aten_kernels.cc#L213)
- <a id="BuildUnfoldBackwardShlo"></a>`BuildUnfoldBackwardShlo(mlir::MlirOp grad_in, const SmallInt64Vector& input_sizes, int64_t dimension, int64_t size, int64_t step)` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/ops/unfold/unfold_aten_kernels.cc#L49)

