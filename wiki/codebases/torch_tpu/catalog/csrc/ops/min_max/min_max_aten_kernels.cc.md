---
title: 'Module: csrc/ops/min_max/min_max_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/min_max/min_max_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenMax: AtenMax(28959186f7a4bda8).
  AtenMin: AtenMin(28959186f7a4bda8).
  AtenMinUnaryOut: AtenMinUnaryOut(4655895dd4ef7692).
  AtenMaxUnaryOut: AtenMaxUnaryOut(4655895dd4ef7692).
  AtenMinDimMin: AtenMinDimMin(a4fecd119c398488).
  AtenArgmaxOut: AtenArgmaxOut(148731b8330b0542).
  AtenMaxDimMax: AtenMaxDimMax(a4fecd119c398488).
  AtenArgminOut: AtenArgminOut(148731b8330b0542).
  ArgMinMax: ArgMinMax(3e11a20b0b2c756b).
  UnaryMinMax: '`$anonymous_namespace_csrc/ops/min_max/min_max_aten_kernels.cc`/UnaryMinMax(46f4fcead888e3e8).'
  AtenMinMaxDim: '`$anonymous_namespace_csrc/ops/min_max/min_max_aten_kernels.cc`/AtenMinMaxDim(acda23ef709aaceb).'
  DispatchUnaryMinMax: DispatchUnaryMinMax(c7027b9acc8350e6).
  ValidateNotZeroElementTensor: '`$anonymous_namespace_csrc/ops/min_max/min_max_aten_kernels.cc`/ValidateNotZeroElementTensor(fd0458bfc68bb174).'
---
# Module: [`csrc/ops/min_max/min_max_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max_aten_kernels.cc)

## Functions
- <a id="ArgMinMax"></a>`ArgMinMax(const at::Tensor& self, c10::optional<int64_t> dim, bool keep_dim, MinMaxOp op, at::Tensor& out, OpParamCacheKeys param_keys)` — [`L155`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max_aten_kernels.cc#L155)
- <a id="AtenArgmaxOut"></a>`AtenArgmaxOut(const at::Tensor& self, c10::optional<int64_t> dim, bool keep_dim, at::Tensor& out)` — [`L204`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max_aten_kernels.cc#L204)
- <a id="AtenArgminOut"></a>`AtenArgminOut(const at::Tensor& self, c10::optional<int64_t> dim, bool keep_dim, at::Tensor& out)` — [`L213`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max_aten_kernels.cc#L213)
- <a id="AtenMax"></a>`AtenMax(const at::Tensor& self)` — [`L222`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max_aten_kernels.cc#L222)
- <a id="AtenMaxDimMax"></a>`AtenMaxDimMax(const at::Tensor& self, int64_t dim, bool keep_dim, at::Tensor& max, at::Tensor& max_indices)` — [`L240`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max_aten_kernels.cc#L240)
- <a id="AtenMaxUnaryOut"></a>`AtenMaxUnaryOut(const at::Tensor& self, at::Tensor& out)` — [`L232`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max_aten_kernels.cc#L232)
- <a id="AtenMin"></a>`AtenMin(const at::Tensor& self)` — [`L252`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max_aten_kernels.cc#L252)
- <a id="AtenMinDimMin"></a>`AtenMinDimMin(const at::Tensor& self, int64_t dim, bool keep_dim, at::Tensor& min, at::Tensor& min_indices)` — [`L270`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max_aten_kernels.cc#L270)
- <a id="AtenMinMaxDim"></a>`AtenMinMaxDim(const at::Tensor& self, int64_t dim, bool keep_dim, MinMaxOp min_max_op, OpParamCacheKeys& op_param_cache_keys, at::Tensor& value, at::Tensor& indices)` — [`L75`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max_aten_kernels.cc#L75)
- <a id="AtenMinUnaryOut"></a>`AtenMinUnaryOut(const at::Tensor& self, at::Tensor& out)` — [`L262`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max_aten_kernels.cc#L262)
- <a id="DispatchUnaryMinMax"></a>`DispatchUnaryMinMax(const at::Tensor& self, MinMaxOp op, std::optional<OpName> op_name)` — [`L51`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max_aten_kernels.cc#L51) — Computes the global minimum or maximum of the input tensor on the TPU
- <a id="UnaryMinMax"></a>`UnaryMinMax(const at::Tensor& self, MinMaxOp op, at::Tensor& out)` — [`L125`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max_aten_kernels.cc#L125)
- <a id="ValidateNotZeroElementTensor"></a>`ValidateNotZeroElementTensor(const at::Tensor& tensor)` — [`L117`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max_aten_kernels.cc#L117)

