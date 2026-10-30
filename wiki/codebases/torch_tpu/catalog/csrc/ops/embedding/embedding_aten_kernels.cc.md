---
title: 'Module: csrc/ops/embedding/embedding_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/embedding/embedding_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenEmbeddingRenorm_: AtenEmbeddingRenorm_(38a277dde38ad49a).
  AtenEmbeddingOut: AtenEmbeddingOut(492440082c31cf43).
  AtenEmbeddingBag: AtenEmbeddingBag(ecfb8def86088556).
  AtenEmbeddingBagBackward: AtenEmbeddingBagBackward(43349b7458c7c03f).
  AtenEmbeddingSparseBackward: AtenEmbeddingSparseBackward(42bc10cdf0933e22).
  AtenEmbedding: AtenEmbedding(27a14b506c3a4e0e).
  AtenEmbeddingDenseBackward: AtenEmbeddingDenseBackward(8d0e32d9c28d5c66).
  ValidateEmbeddingArgs: '`$anonymous_namespace_csrc/ops/embedding/embedding_aten_kernels.cc`/ValidateEmbeddingArgs(b2d6689cde60befb).'
  AtenEmbeddingBagForwardOnly: AtenEmbeddingBagForwardOnly(ecfb8def86088556).
  DispatchEmbeddingSparseBackward: '`$anonymous_namespace_csrc/ops/embedding/embedding_aten_kernels.cc`/DispatchEmbeddingSparseBackward(41c400d47f99130a).'
  ValidateEmbeddingBagSparseBackwardArgs: '`$anonymous_namespace_csrc/ops/embedding/embedding_aten_kernels.cc`/ValidateEmbeddingBagSparseBackwardArgs(122f09132ed37ed0).'
  BuildAndDispatchEmbedding: '`$anonymous_namespace_csrc/ops/embedding/embedding_aten_kernels.cc`/BuildAndDispatchEmbedding(e896f04d7651ad8f).'
  ValidateWeightType: '`$anonymous_namespace_csrc/ops/embedding/embedding_aten_kernels.cc`/ValidateWeightType(fd0458bfc68bb174).'
  ValidateStaticShape: '`$anonymous_namespace_csrc/ops/embedding/embedding_aten_kernels.cc`/ValidateStaticShape(d8359b99282c084c).'
  MakeEmptySparseEmbeddingGrad: '`$anonymous_namespace_csrc/ops/embedding/embedding_aten_kernels.cc`/MakeEmptySparseEmbeddingGrad(f37005713c1d1986).'
  ExtractValidCount: '`$anonymous_namespace_csrc/ops/embedding/embedding_aten_kernels.cc`/ExtractValidCount(31c8c37cc6a727c6).'
  GetEmbeddingOutputDims: '`$anonymous_namespace_csrc/ops/embedding/embedding_aten_kernels.cc`/GetEmbeddingOutputDims(f75c5a7b05a5c46f).'
  AtenEmbeddingBackward: AtenEmbeddingBackward(3826408ddcac3b7).
---
# Module: [`csrc/ops/embedding/embedding_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc)

## Functions
- <a id="AtenEmbedding"></a>`AtenEmbedding(const at::Tensor& weight, const at::Tensor& indices, at::SymInt padding_idx, bool scale_grad_by_freq, bool sparse)` — [`L270`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L270) — Note: `padding_idx`, `scale_grad_by_freq`, and `sparse` are wrapped in
- <a id="AtenEmbeddingBackward"></a>`AtenEmbeddingBackward(const at::Tensor& grad, const at::Tensor& indices, const at::SymInt num_weights, const at::SymInt padding_idx, const bool scale_grad_by_freq, const bool sparse)` — [`L566`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L566)
- <a id="AtenEmbeddingBag"></a>`AtenEmbeddingBag(const at::Tensor& weight, const at::Tensor& indices, const at::Tensor& offsets, bool scale_grad_by_freq, int64_t mode, bool sparse, const std::optional<at::Tensor>& per_sample_weights, bool include_last_offset, int64_t padding_idx)` — [`L314`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L314)
- <a id="AtenEmbeddingBagBackward"></a>`AtenEmbeddingBagBackward(const at::Tensor& grad, const at::Tensor& indices, const at::Tensor& offsets, const at::Tensor& offset2bag, const at::Tensor& bag_size, const at::Tensor& max_indices, at::SymInt num_weights, bool scale_grad_by_freq, int64_t mode, bool sparse, const std::optional<at::Tensor>& per_sample_weights, int64_t padding_idx)` — [`L402`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L402)
- <a id="AtenEmbeddingBagForwardOnly"></a>`AtenEmbeddingBagForwardOnly(const at::Tensor& weight, const at::Tensor& indices, const at::Tensor& offsets, bool scale_grad_by_freq, int64_t mode, bool sparse, const std::optional<at::Tensor>& per_sample_weights, bool include_last_offset, int64_t padding_idx)` — [`L381`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L381)
- <a id="AtenEmbeddingDenseBackward"></a>`AtenEmbeddingDenseBackward(const at::Tensor& grad_output, const at::Tensor& indices, at::SymInt num_weights, at::SymInt padding_idx, bool scale_grad_by_freq)` — [`L481`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L481) — This implementation is adapted from:
- <a id="AtenEmbeddingOut"></a>`AtenEmbeddingOut(const at::Tensor& weight, const at::Tensor& indices, at::SymInt padding_idx, bool scale_grad_by_freq, bool sparse, at::Tensor& out)` — [`L288`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L288)
- <a id="AtenEmbeddingRenorm_"></a>`AtenEmbeddingRenorm_(at::Tensor& self, const at::Tensor& indices, double max_norm, double norm_type)` — [`L513`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L513)
- <a id="AtenEmbeddingSparseBackward"></a>`AtenEmbeddingSparseBackward(const at::Tensor& grad, const at::Tensor& indices, const int64_t num_weights, const int64_t padding_idx, const bool scale_grad_by_freq)` — [`L546`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L546)
- <a id="BuildAndDispatchEmbedding"></a>`BuildAndDispatchEmbedding(const at::Tensor& weight, const at::Tensor& indices, const Dimensions& out_dims, OpParamCacheKeys&& pk)` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L100)
- <a id="DispatchEmbeddingSparseBackward"></a>`DispatchEmbeddingSparseBackward(const at::Tensor& grad, const at::Tensor& indices, const int64_t num_weights, const int64_t padding_idx, const bool scale_grad_by_freq, OpParamCacheKeys&& pk)` — [`L163`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L163)
- <a id="ExtractValidCount"></a>`ExtractValidCount(const at::Tensor& count_tensor)` — [`L116`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L116)
- <a id="GetEmbeddingOutputDims"></a>`GetEmbeddingOutputDims(const at::Tensor& weight, const at::Tensor& indices)` — [`L90`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L90)
- <a id="MakeEmptySparseEmbeddingGrad"></a>`MakeEmptySparseEmbeddingGrad(const at::Tensor& grad, const int64_t num_weights, const int64_t num_features)` — [`L124`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L124)
- <a id="ValidateEmbeddingArgs"></a>`ValidateEmbeddingArgs(const at::Tensor& weight, const at::Tensor& indices)` — [`L76`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L76)
- <a id="ValidateEmbeddingBagSparseBackwardArgs"></a>`ValidateEmbeddingBagSparseBackwardArgs(const at::Tensor& indices, bool scale_grad_by_freq, int64_t mode, bool has_psw)` — [`L138`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L138)
- <a id="ValidateStaticShape"></a>`ValidateStaticShape(const at::Tensor& tensor, const std::string_view arg_name)` — [`L70`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L70)
- <a id="ValidateWeightType"></a>`ValidateWeightType(const at::Tensor& weight)` — [`L60`](../../../../../../../raw/code/torch_tpu/csrc/ops/embedding/embedding_aten_kernels.cc#L60)

