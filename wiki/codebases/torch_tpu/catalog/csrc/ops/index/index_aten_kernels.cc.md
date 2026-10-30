---
title: 'Module: csrc/ops/index/index_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/index/index_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenIndexTensorOut: AtenIndexTensorOut(52ecb026baf64717).
  ValidateAndGetIndicesInfo: '`$anonymous_namespace_csrc/ops/index/index_aten_kernels.cc`/ValidateAndGetIndicesInfo(2bce3ef013586d69).'
  GetNumNonZeroElements: '`$anonymous_namespace_csrc/ops/index/index_aten_kernels.cc`/GetNumNonZeroElements(31c8c37cc6a727c6).'
  GetOutputDims: '`$anonymous_namespace_csrc/ops/index/index_aten_kernels.cc`/GetOutputDims(aeb443fa6d134e8c).'
  IndicesInfo.indices: '`$anonymous_namespace_csrc/ops/index/index_aten_kernels.cc`/IndicesInfo#indices.'
  IndicesInfo.dimensions: '`$anonymous_namespace_csrc/ops/index/index_aten_kernels.cc`/IndicesInfo#dimensions.'
  IndicesInfo: '`$anonymous_namespace_csrc/ops/index/index_aten_kernels.cc`/IndicesInfo#'
  IndicesInfo.num_non_zero_elements: '`$anonymous_namespace_csrc/ops/index/index_aten_kernels.cc`/IndicesInfo#num_non_zero_elements.'
---
# Module: [`csrc/ops/index/index_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/index/index_aten_kernels.cc)

## Classes
### <a id="IndicesInfo"></a>`IndicesInfo`
- def: [`csrc/ops/index/index_aten_kernels.cc:52`](../../../../../../../raw/code/torch_tpu/csrc/ops/index/index_aten_kernels.cc#L52)
- signature: `struct IndicesInfo`
- members:
  - <a id="IndicesInfo.dimensions"></a>`dimensions` — [`L64`](../../../../../../../raw/code/torch_tpu/csrc/ops/index/index_aten_kernels.cc#L64) — List of indexed dimensions.
  - <a id="IndicesInfo.indices"></a>`indices` — [`L58`](../../../../../../../raw/code/torch_tpu/csrc/ops/index/index_aten_kernels.cc#L58) — Defined tensor indices.
  - <a id="IndicesInfo.num_non_zero_elements"></a>`num_non_zero_elements` — [`L67`](../../../../../../../raw/code/torch_tpu/csrc/ops/index/index_aten_kernels.cc#L67) — Number of non-zero (`True`) elements when indexing with a boolean mask.
- uses (calls/refs, reference-scoped): [`Indices`](../../common/dimension_types.h.md#Indices)
- used by: [`AtenIndexTensorOut`](index_aten_kernels.cc.md#AtenIndexTensorOut), [`ValidateAndGetIndicesInfo`](index_aten_kernels.cc.md#ValidateAndGetIndicesInfo), [`GetNumNonZeroElements`](index_aten_kernels.cc.md#GetNumNonZeroElements), [`GetOutputDims`](index_aten_kernels.cc.md#GetOutputDims)

## Functions
- <a id="AtenIndexTensorOut"></a>`AtenIndexTensorOut(const at::Tensor& self, const c10::List<c10::optional<at::Tensor>>& indices_list_opt, at::Tensor& out)` — [`L236`](../../../../../../../raw/code/torch_tpu/csrc/ops/index/index_aten_kernels.cc#L236) — documented in [op-names-and-python-context](../../../../concepts/op-names-and-python-context.md)
- <a id="GetNumNonZeroElements"></a>`GetNumNonZeroElements(const at::Tensor& mask)` — [`L74`](../../../../../../../raw/code/torch_tpu/csrc/ops/index/index_aten_kernels.cc#L74) — Computes the number of non-zero (`True`) elements in `mask` on TPU via
- <a id="GetOutputDims"></a>`GetOutputDims(const at::Tensor& self, const IndicesInfo& info)` — [`L167`](../../../../../../../raw/code/torch_tpu/csrc/ops/index/index_aten_kernels.cc#L167)
- <a id="ValidateAndGetIndicesInfo"></a>`ValidateAndGetIndicesInfo(const at::Tensor& self, const c10::List<c10::optional<at::Tensor>>& indices_list_opt)` — [`L90`](../../../../../../../raw/code/torch_tpu/csrc/ops/index/index_aten_kernels.cc#L90) — Preprocess and check the `indices_list_opt` input into `IndicesInfo`.

