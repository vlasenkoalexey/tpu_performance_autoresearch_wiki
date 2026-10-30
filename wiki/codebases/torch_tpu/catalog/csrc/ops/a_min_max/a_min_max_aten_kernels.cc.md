---
title: 'Module: csrc/ops/a_min_max/a_min_max_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/a_min_max/a_min_max_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenAminmaxOut: AtenAminmaxOut(cf79b64ad737c976).
  AtenAminOut: AtenAminOut(77898a4aaed14e63).
  AtenAmaxOut: AtenAmaxOut(77898a4aaed14e63).
  AMinMax: '`$anonymous_namespace_csrc/ops/a_min_max/a_min_max_aten_kernels.cc`/AMinMax(c2ced51df80f555).'
  ValidateAMinMaxInputs: '`$anonymous_namespace_csrc/ops/a_min_max/a_min_max_aten_kernels.cc`/ValidateAMinMaxInputs(27a803b2289b6b46).'
  GetOpName: '`$anonymous_namespace_csrc/ops/a_min_max/a_min_max_aten_kernels.cc`/GetOpName(a5d1cb7259704105).'
---
# Module: [`csrc/ops/a_min_max/a_min_max_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/a_min_max/a_min_max_aten_kernels.cc)

## Functions
- <a id="AMinMax"></a>`AMinMax(const at::Tensor& self, const at::IntArrayRef dims, const bool keep_dim, const AMinMaxOp a_min_max_op, at::Tensor& out)` — [`L73`](../../../../../../../raw/code/torch_tpu/csrc/ops/a_min_max/a_min_max_aten_kernels.cc#L73)
- <a id="AtenAmaxOut"></a>`AtenAmaxOut(const at::Tensor& self, const at::IntArrayRef dims, const bool keep_dim, at::Tensor& out)` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/ops/a_min_max/a_min_max_aten_kernels.cc#L106)
- <a id="AtenAminOut"></a>`AtenAminOut(const at::Tensor& self, const at::IntArrayRef dims, const bool keep_dim, at::Tensor& out)` — [`L118`](../../../../../../../raw/code/torch_tpu/csrc/ops/a_min_max/a_min_max_aten_kernels.cc#L118)
- <a id="AtenAminmaxOut"></a>`AtenAminmaxOut(const at::Tensor& self, const c10::optional<int64_t> dim, const bool keep_dim, at::Tensor& min, at::Tensor& max)` — [`L130`](../../../../../../../raw/code/torch_tpu/csrc/ops/a_min_max/a_min_max_aten_kernels.cc#L130)
- <a id="GetOpName"></a>`GetOpName(AMinMaxOp op)` — [`L51`](../../../../../../../raw/code/torch_tpu/csrc/ops/a_min_max/a_min_max_aten_kernels.cc#L51)
- <a id="ValidateAMinMaxInputs"></a>`ValidateAMinMaxInputs(const at::Tensor& self, at::Tensor& out)` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/a_min_max/a_min_max_aten_kernels.cc#L55)

