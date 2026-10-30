---
title: 'Module: csrc/ops/isin/isin_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/isin/isin_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenIsInTensorScalarOut: AtenIsInTensorScalarOut(66c1d9f6f898d6ca).
  AtenIsInScalarTensorOut: AtenIsInScalarTensorOut(c866e2911ea46016).
  AtenIsInTensorTensorOut: AtenIsInTensorTensorOut(27df2ff2a7bf9870).
  AtenIsInHelper: '`$anonymous_namespace_csrc/ops/isin/isin_aten_kernels.cc`/AtenIsInHelper(8fecee6e752b3aae).'
  ToIsUnique: '`$anonymous_namespace_csrc/ops/isin/isin_aten_kernels.cc`/ToIsUnique(cae48c08ff54c86).'
  ToIsInverted: '`$anonymous_namespace_csrc/ops/isin/isin_aten_kernels.cc`/ToIsInverted(38b0c7aa2934336b).'
---
# Module: [`csrc/ops/isin/isin_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/isin/isin_aten_kernels.cc)

## Functions
- <a id="AtenIsInHelper"></a>`AtenIsInHelper(const at::Tensor& elements, const at::Tensor& test_elements, IsUnique uniqueness, IsInverted inversion, at::Tensor& out, OpParamCacheKeys param_keys)` — [`L50`](../../../../../../../raw/code/torch_tpu/csrc/ops/isin/isin_aten_kernels.cc#L50)
- <a id="AtenIsInScalarTensorOut"></a>`AtenIsInScalarTensorOut(const at::Scalar& element, const at::Tensor& test_elements, bool assume_unique, bool invert, at::Tensor& out)` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/ops/isin/isin_aten_kernels.cc#L85)
- <a id="AtenIsInTensorScalarOut"></a>`AtenIsInTensorScalarOut(const at::Tensor& elements, const at::Scalar& test_element, bool assume_unique, bool invert, at::Tensor& out)` — [`L114`](../../../../../../../raw/code/torch_tpu/csrc/ops/isin/isin_aten_kernels.cc#L114)
- <a id="AtenIsInTensorTensorOut"></a>`AtenIsInTensorTensorOut(const at::Tensor& elements, const at::Tensor& test_elements, bool assume_unique, bool invert, at::Tensor& out)` — [`L101`](../../../../../../../raw/code/torch_tpu/csrc/ops/isin/isin_aten_kernels.cc#L101)
- <a id="ToIsInverted"></a>`ToIsInverted(bool invert)` — [`L46`](../../../../../../../raw/code/torch_tpu/csrc/ops/isin/isin_aten_kernels.cc#L46)
- <a id="ToIsUnique"></a>`ToIsUnique(bool assume_unique)` — [`L42`](../../../../../../../raw/code/torch_tpu/csrc/ops/isin/isin_aten_kernels.cc#L42)

