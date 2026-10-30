---
title: 'Module: csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adam_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adam_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenSparseDenseMatmulGradWithAdam: AtenSparseDenseMatmulGradWithAdam(9ebfab7344df7c43).
  SparseDenseMatmulGradWithAdamBuilder: '`$anonymous_namespace_csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adam_aten_kernels.cc`/SparseDenseMatmulGradWithAdamBuilder(572e19a2c33f8da1).'
---
# Module: [`csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adam_aten_kernels.cc`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adam_aten_kernels.cc)

## Functions
- <a id="AtenSparseDenseMatmulGradWithAdam"></a>`AtenSparseDenseMatmulGradWithAdam(const at::Tensor& row_pointers, const at::Tensor& embedding_ids, const at::Tensor& sample_ids, const at::Tensor& gains, const at::Tensor& embedding_table, const at::Tensor& momentum, const at::Tensor& velocity, const at::Tensor& activations_grad, const at::Tensor& alpha_t, double beta_1, double beta_2, double epsilon, int64_t device_batch_size, int64_t max_ids_per_partition, int64_t max_unique_ids_per_partition, std::string_view computation_name)` — [`L303`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adam_aten_kernels.cc#L303) — @brief Computes gradients and updates the embedding table using the Adam — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="SparseDenseMatmulGradWithAdamBuilder"></a>`SparseDenseMatmulGradWithAdamBuilder(int64_t device_batch_size, int64_t max_ids_per_partition, int64_t max_unique_ids_per_partition, double beta_1, double beta_2, double epsilon, std::string_view computation_name)` — [`L61`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adam_aten_kernels.cc#L61) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- `SparseDenseMatmulGradWithAdamBuilder(int64_t device_batch_size, int64_t max_ids_per_partition, int64_t max_unique_ids_per_partition, double beta_1, double beta_2, double epsilon, std::string_view computation_name)` — [`L61`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adam_aten_kernels.cc#L61)

