---
title: 'Module: csrc/ops/masked_scatter/masked_scatter_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/masked_scatter/masked_scatter_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenMaskedScatter_: AtenMaskedScatter_(2db65acdbc4fe769).
  NarrowBroadcastTrailingDims: '`$anonymous_namespace_csrc/ops/masked_scatter/masked_scatter_aten_kernels.cc`/NarrowBroadcastTrailingDims(28959186f7a4bda8).'
---
# Module: [`csrc/ops/masked_scatter/masked_scatter_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_scatter/masked_scatter_aten_kernels.cc)

## Functions
- <a id="AtenMaskedScatter_"></a>`AtenMaskedScatter_(at::Tensor& self, const at::Tensor& mask, const at::Tensor& source)` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_scatter/masked_scatter_aten_kernels.cc#L65) — documented in [op-names-and-python-context](../../../../concepts/op-names-and-python-context.md)
- <a id="NarrowBroadcastTrailingDims"></a>`NarrowBroadcastTrailingDims(const at::Tensor& mask)` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_scatter/masked_scatter_aten_kernels.cc#L49) — Undoes the expansion of `mask` along its trailing dimensions. ATen's

