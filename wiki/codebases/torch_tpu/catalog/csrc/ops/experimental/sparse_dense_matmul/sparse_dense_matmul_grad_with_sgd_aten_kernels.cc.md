---
title: 'Module: csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_sgd_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_sgd_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenSparseDenseMatmulGradWithSgd: AtenSparseDenseMatmulGradWithSgd(bad6584aa36d7ea1).
  SparseDenseMatmulGradWithSgdBuilder: '`$anonymous_namespace_csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_sgd_aten_kernels.cc`/SparseDenseMatmulGradWithSgdBuilder(f6bbf215167e7dbb).'
---
# Module: [`csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_sgd_aten_kernels.cc`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_sgd_aten_kernels.cc)

## Functions
- <a id="AtenSparseDenseMatmulGradWithSgd"></a>`AtenSparseDenseMatmulGradWithSgd(const at::Tensor& row_pointers, const at::Tensor& embedding_ids, const at::Tensor& sample_ids, const at::Tensor& gains, const at::Tensor& embedding_table, const at::Tensor& activations_grad, const at::Tensor& learning_rate, int64_t device_batch_size, int64_t max_ids_per_partition, int64_t max_unique_ids_per_partition, std::string_view computation_name)` — [`L176`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_sgd_aten_kernels.cc#L176) — @brief Computes gradients and updates the embedding table using Exact SGD. — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="SparseDenseMatmulGradWithSgdBuilder"></a>`SparseDenseMatmulGradWithSgdBuilder(int64_t device_batch_size, int64_t max_ids_per_partition, int64_t max_unique_ids_per_partition, std::string_view computation_name)` — [`L57`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_sgd_aten_kernels.cc#L57) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)

