---
title: 'Module: csrc/ops/view/view_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/view/view_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenViewAsComplex: AtenViewAsComplex(28959186f7a4bda8).
  AtenView: AtenView(9fe15d6baae0848c).
  AtenViewAsReal: AtenViewAsReal(28959186f7a4bda8).
  ViewSymIntsToDimensions: '`$anonymous_namespace_csrc/ops/view/view_aten_kernels.cc`/ViewSymIntsToDimensions(725ecc5117148cb9).'
  AtenReshapeAlias: AtenReshapeAlias(979ffb5099922e90).
  GetNegativeOneDimensionsIndexStr: '`$anonymous_namespace_csrc/ops/view/view_aten_kernels.cc`/GetNegativeOneDimensionsIndexStr(51b83c67fbc9a836).'
  FilterIndicesAndBuildErrorStr: '`$anonymous_namespace_csrc/ops/view/view_aten_kernels.cc`/FilterIndicesAndBuildErrorStr(d279f18d296ff5bb).'
  DropLastAndGetOddStridesStr: '`$anonymous_namespace_csrc/ops/view/view_aten_kernels.cc`/DropLastAndGetOddStridesStr(51b83c67fbc9a836).'
  GetInvalidDimensionIndexStr: '`$anonymous_namespace_csrc/ops/view/view_aten_kernels.cc`/GetInvalidDimensionIndexStr(51b83c67fbc9a836).'
---
# Module: [`csrc/ops/view/view_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/view/view_aten_kernels.cc)

## Functions
- <a id="AtenReshapeAlias"></a>`AtenReshapeAlias(const at::Tensor& self, c10::SymIntArrayRef size_sym, c10::SymIntArrayRef stride_sym)` — [`L227`](../../../../../../../raw/code/torch_tpu/csrc/ops/view/view_aten_kernels.cc#L227) — at::_reshape_alias
- <a id="AtenView"></a>`AtenView(const at::Tensor& self, c10::SymIntArrayRef size_sym)` — [`L237`](../../../../../../../raw/code/torch_tpu/csrc/ops/view/view_aten_kernels.cc#L237) — at::view
- <a id="AtenViewAsComplex"></a>`AtenViewAsComplex(const at::Tensor& self)` — [`L299`](../../../../../../../raw/code/torch_tpu/csrc/ops/view/view_aten_kernels.cc#L299) — at::view_as_complex
- <a id="AtenViewAsReal"></a>`AtenViewAsReal(const at::Tensor& self)` — [`L271`](../../../../../../../raw/code/torch_tpu/csrc/ops/view/view_aten_kernels.cc#L271) — at::view_as_real
- <a id="DropLastAndGetOddStridesStr"></a>`DropLastAndGetOddStridesStr(absl::Span<const int64_t> strides)` — [`L121`](../../../../../../../raw/code/torch_tpu/csrc/ops/view/view_aten_kernels.cc#L121)
- <a id="FilterIndicesAndBuildErrorStr"></a>`FilterIndicesAndBuildErrorStr(const size_t size, const std::string_view singular, const std::string_view plural, const Predicate& pred, const ToValue& to_value)` — [`L102`](../../../../../../../raw/code/torch_tpu/csrc/ops/view/view_aten_kernels.cc#L102) — Convenience function for building an error message with the same format.
- <a id="GetInvalidDimensionIndexStr"></a>`GetInvalidDimensionIndexStr(absl::Span<const int64_t> sizes)` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/view/view_aten_kernels.cc#L112)
- <a id="GetNegativeOneDimensionsIndexStr"></a>`GetNegativeOneDimensionsIndexStr(absl::Span<const int64_t> sizes)` — [`L134`](../../../../../../../raw/code/torch_tpu/csrc/ops/view/view_aten_kernels.cc#L134) — Returns a string of the comma-separated indices corresponding to -1 elements.
- <a id="ViewSymIntsToDimensions"></a>`ViewSymIntsToDimensions(const at::Tensor& self, c10::SymIntArrayRef size_sym)` — [`L151`](../../../../../../../raw/code/torch_tpu/csrc/ops/view/view_aten_kernels.cc#L151) — torch passes the target size for view (and reshape) as SymInts.

