---
title: 'Module: csrc/ops/nonzero/nonzero_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/nonzero/nonzero_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenNonzeroOut: AtenNonzeroOut(4655895dd4ef7692).
  AtenNonzero: AtenNonzero(28959186f7a4bda8).
  GetNumNonZeroElements: '`$anonymous_namespace_csrc/ops/nonzero/nonzero_aten_kernels.cc`/GetNumNonZeroElements(cd958efedc17238).'
  Nonzero: '`$anonymous_namespace_csrc/ops/nonzero/nonzero_aten_kernels.cc`/Nonzero(6daba7099dd06822).'
  AtenNonzeroHelper: '`$anonymous_namespace_csrc/ops/nonzero/nonzero_aten_kernels.cc`/AtenNonzeroHelper(cd958efedc17238).'
  AtenNonzeroOutHelper: '`$anonymous_namespace_csrc/ops/nonzero/nonzero_aten_kernels.cc`/AtenNonzeroOutHelper(27a803b2289b6b46).'
  NonzeroOut: '`$anonymous_namespace_csrc/ops/nonzero/nonzero_aten_kernels.cc`/NonzeroOut(ed4dfe5280030c86).'
---
# Module: [`csrc/ops/nonzero/nonzero_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/nonzero/nonzero_aten_kernels.cc)

## Functions
- <a id="AtenNonzero"></a>`AtenNonzero(const at::Tensor& self)` — [`L111`](../../../../../../../raw/code/torch_tpu/csrc/ops/nonzero/nonzero_aten_kernels.cc#L111) — This op is implemented by first calculating and materializing the output
- <a id="AtenNonzeroHelper"></a>`AtenNonzeroHelper(const at::Tensor& self)` — [`L78`](../../../../../../../raw/code/torch_tpu/csrc/ops/nonzero/nonzero_aten_kernels.cc#L78)
- <a id="AtenNonzeroOut"></a>`AtenNonzeroOut(const at::Tensor& self, at::Tensor& out)` — [`L118`](../../../../../../../raw/code/torch_tpu/csrc/ops/nonzero/nonzero_aten_kernels.cc#L118)
- <a id="AtenNonzeroOutHelper"></a>`AtenNonzeroOutHelper(const at::Tensor& self, at::Tensor& out)` — [`L94`](../../../../../../../raw/code/torch_tpu/csrc/ops/nonzero/nonzero_aten_kernels.cc#L94)
- <a id="GetNumNonZeroElements"></a>`GetNumNonZeroElements(const at::Tensor& self)` — [`L41`](../../../../../../../raw/code/torch_tpu/csrc/ops/nonzero/nonzero_aten_kernels.cc#L41)
- <a id="Nonzero"></a>`Nonzero(const at::Tensor& self, const int64_t num_non_zero_elements)` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/nonzero/nonzero_aten_kernels.cc#L56)
- <a id="NonzeroOut"></a>`NonzeroOut(const at::Tensor& self, at::Tensor& out, const int64_t num_non_zero_elements)` — [`L68`](../../../../../../../raw/code/torch_tpu/csrc/ops/nonzero/nonzero_aten_kernels.cc#L68)

