---
title: 'Module: csrc/ops/gather/gather_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/gather/gather_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenGatherOut: AtenGatherOut(5113c357da4295a7).
  AtenGather: AtenGather(ef9b660cf87ba855).
  GatherOut: '`$anonymous_namespace_csrc/ops/gather/gather_aten_kernels.cc`/GatherOut(83edabffefe10a54).'
  Gather: '`$anonymous_namespace_csrc/ops/gather/gather_aten_kernels.cc`/Gather(6a12f88663ddb4d0).'
---
# Module: [`csrc/ops/gather/gather_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/gather/gather_aten_kernels.cc)

## Functions
- <a id="AtenGather"></a>`AtenGather(const at::Tensor& self, int64_t dim, const at::Tensor& index, bool sparse_grad)` — [`L110`](../../../../../../../raw/code/torch_tpu/csrc/ops/gather/gather_aten_kernels.cc#L110)
- <a id="AtenGatherOut"></a>`AtenGatherOut(const at::Tensor& self, int64_t dim, const at::Tensor& index, bool sparse_grad, at::Tensor& out)` — [`L119`](../../../../../../../raw/code/torch_tpu/csrc/ops/gather/gather_aten_kernels.cc#L119)
- <a id="Gather"></a>`Gather(const at::Tensor& self, int64_t dim, const at::Tensor& index, bool sparse_grad, OpParamCacheKeys&& param_keys)` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/ops/gather/gather_aten_kernels.cc#L48)
- <a id="GatherOut"></a>`GatherOut(const at::Tensor& self, int64_t dim, const at::Tensor& index, bool sparse_grad, OpParamCacheKeys&& param_keys, at::Tensor& out)` — [`L77`](../../../../../../../raw/code/torch_tpu/csrc/ops/gather/gather_aten_kernels.cc#L77)

