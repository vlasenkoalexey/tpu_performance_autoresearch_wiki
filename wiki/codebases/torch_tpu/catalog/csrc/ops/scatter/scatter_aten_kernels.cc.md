---
title: 'Module: csrc/ops/scatter/scatter_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/scatter/scatter_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  Scatter: '`$anonymous_namespace_csrc/ops/scatter/scatter_aten_kernels.cc`/Scatter(c14b2fff65b264fb).'
  AtenScatterReduceOut: AtenScatterReduceOut(d11a58d569fc9f2e).
  AtenScatterReduceTwoOut: AtenScatterReduceTwoOut(a389afc076f3a1ca).
  AtenScatterValueOut: AtenScatterValueOut(484572ca928fd664).
  AtenScatterValueReduceOut: AtenScatterValueReduceOut(37f51dbc923937b4).
  AtenScatterSrcOut: AtenScatterSrcOut(679ed56937960e6d).
  AtenScatterAddOut: AtenScatterAddOut(679ed56937960e6d).
  ParseScatterOp: '`$anonymous_namespace_csrc/ops/scatter/scatter_aten_kernels.cc`/ParseScatterOp(70fd3e5aeffd31df).'
---
# Module: [`csrc/ops/scatter/scatter_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter_aten_kernels.cc)

## Functions
- <a id="AtenScatterAddOut"></a>`AtenScatterAddOut(const at::Tensor& self, int64_t dim, const at::Tensor& index, const at::Tensor& src, at::Tensor& out)` — [`L225`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter_aten_kernels.cc#L225)
- <a id="AtenScatterReduceOut"></a>`AtenScatterReduceOut(const at::Tensor& self, int64_t dim, const at::Tensor& index, const at::Tensor& src, std::string_view reduction_op, at::Tensor& out)` — [`L166`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter_aten_kernels.cc#L166)
- <a id="AtenScatterReduceTwoOut"></a>`AtenScatterReduceTwoOut(const at::Tensor& self, int64_t dim, const at::Tensor& index, const at::Tensor& src, c10::string_view reduction, bool include_self, at::Tensor& out)` — [`L182`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter_aten_kernels.cc#L182)
- <a id="AtenScatterSrcOut"></a>`AtenScatterSrcOut(const at::Tensor& self, int64_t dim, const at::Tensor& index, const at::Tensor& src, at::Tensor& out)` — [`L135`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter_aten_kernels.cc#L135)
- <a id="AtenScatterValueOut"></a>`AtenScatterValueOut(const at::Tensor& self, int64_t dim, const at::Tensor& index, const at::Scalar& value, at::Tensor& out)` — [`L148`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter_aten_kernels.cc#L148)
- <a id="AtenScatterValueReduceOut"></a>`AtenScatterValueReduceOut(const at::Tensor& self, int64_t dim, const at::Tensor& index, const at::Scalar& value, std::string_view reduction_op, at::Tensor& out)` — [`L203`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter_aten_kernels.cc#L203)
- <a id="ParseScatterOp"></a>`ParseScatterOp(std::string_view reduction_op, ScatterVersion version = ScatterVersion::kV1)` — [`L98`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter_aten_kernels.cc#L98)
- <a id="Scatter"></a>`Scatter(const at::Tensor& self, int64_t dim, const at::Tensor& index, const at::Tensor& src, ScatterOp reduction_op, ScatterIncludeSelf include_self, at::Tensor& out)` — [`L50`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter_aten_kernels.cc#L50)

