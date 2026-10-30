---
title: 'Module: csrc/ops/index_reduce/index_reduce_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/index_reduce/index_reduce_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  TpuAtenIndexReduceOut: TpuAtenIndexReduceOut(a389afc076f3a1ca).
  IndexReduce: '`$anonymous_namespace_csrc/ops/index_reduce/index_reduce_aten_kernels.cc`/IndexReduce(9221f94b44015337).'
  GetReduceOp: '`$anonymous_namespace_csrc/ops/index_reduce/index_reduce_aten_kernels.cc`/GetReduceOp(de686d2070a75e57).'
---
# Module: [`csrc/ops/index_reduce/index_reduce_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_reduce/index_reduce_aten_kernels.cc)

## Functions
- <a id="GetReduceOp"></a>`GetReduceOp(const std::string_view reduce)` — [`L47`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_reduce/index_reduce_aten_kernels.cc#L47)
- <a id="IndexReduce"></a>`IndexReduce(const at::Tensor& self, int64_t dim, const at::Tensor& index, const at::Tensor& source, const std::string_view reduce, bool include_self, at::Tensor& out, OpParamCacheKeys param_keys)` — [`L62`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_reduce/index_reduce_aten_kernels.cc#L62)
- <a id="TpuAtenIndexReduceOut"></a>`TpuAtenIndexReduceOut(const at::Tensor& self, int64_t dim, const at::Tensor& index, const at::Tensor& source, std::string_view reduce, bool include_self, at::Tensor& out)` — [`L98`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_reduce/index_reduce_aten_kernels.cc#L98)

