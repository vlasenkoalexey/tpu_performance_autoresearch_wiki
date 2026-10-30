---
title: 'Module: csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenSparseDenseMatmulActivationUnstack: AtenSparseDenseMatmulActivationUnstack(d6ce0450f229ebab).
  ValidateSparseDenseMatmulActivationUnstackInputs: ValidateSparseDenseMatmulActivationUnstackInputs(14979be0312f22f).
  AtenSparseDenseMatmulActivationUnstackAutograd.forward: AtenSparseDenseMatmulActivationUnstackAutograd#forward(1cd8dcb717eadb7a).
  SparseDenseMatmulActivationUnstackBuilder.IntVector: '`$anonymous_namespace_csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc`/SparseDenseMatmulActivationUnstackBuilder(da844ba4ca93f550).IntVector#'
  AtenSparseDenseMatmulActivationUnstackAutograd.backward: AtenSparseDenseMatmulActivationUnstackAutograd#backward(305625f81d7e100).
  SparseDenseMatmulActivationUnstackBuilder: '`$anonymous_namespace_csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc`/SparseDenseMatmulActivationUnstackBuilder(57569d64a1733b26).'
---
# Module: [`csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc)

## Classes
### <a id="SparseDenseMatmulActivationUnstackBuilder.IntVector"></a>`SparseDenseMatmulActivationUnstackBuilder.IntVector`
- def: [`csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc:63`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc#L63)
- signature: `using IntVector = std::vector<int64_t>`
- uses (calls/refs, reference-scoped): (none in-repo)

## Functions
- <a id="AtenSparseDenseMatmulActivationUnstack"></a>`AtenSparseDenseMatmulActivationUnstack(const at::Tensor& stacked_activations, at::IntArrayRef per_feature_batch_sizes, at::IntArrayRef per_feature_dims)` — [`L167`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc#L167) — @brief Unstacks and uninterleaves stacked activations across SparseCore — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- `AtenSparseDenseMatmulActivationUnstack(const at::Tensor& stacked_activations, at::IntArrayRef per_feature_batch_sizes, at::IntArrayRef per_feature_dims)` — [`L167`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc#L167) — @brief Unstacks and uninterleaves stacked activations across SparseCore
- <a id="SparseDenseMatmulActivationUnstackBuilder"></a>`SparseDenseMatmulActivationUnstackBuilder(at::IntArrayRef per_feature_batch_sizes, at::IntArrayRef per_feature_dims)` — [`L61`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc#L61)
- `SparseDenseMatmulActivationUnstackBuilder(at::IntArrayRef per_feature_batch_sizes, at::IntArrayRef per_feature_dims)` — [`L61`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc#L61)
- <a id="ValidateSparseDenseMatmulActivationUnstackInputs"></a>`ValidateSparseDenseMatmulActivationUnstackInputs(const at::Tensor& stacked_activations, at::IntArrayRef per_feature_batch_sizes, at::IntArrayRef per_feature_dims)` — [`L119`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc#L119) — @brief Validates the inputs to the sparse-dense matmul activation unstack op.

## Other members
- `forward` — [`L224`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc#L224)
- `backward` — [`L246`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc#L246)
- <a id="AtenSparseDenseMatmulActivationUnstackAutograd.backward"></a>`AtenSparseDenseMatmulActivationUnstackAutograd.backward` — [`L246`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc#L246)
- <a id="AtenSparseDenseMatmulActivationUnstackAutograd.forward"></a>`AtenSparseDenseMatmulActivationUnstackAutograd.forward` — [`L224`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc#L224)

