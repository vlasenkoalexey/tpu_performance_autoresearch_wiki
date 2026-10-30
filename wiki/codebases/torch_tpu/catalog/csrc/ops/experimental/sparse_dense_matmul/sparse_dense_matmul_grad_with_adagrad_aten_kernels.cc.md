---
title: 'Module: csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adagrad_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adagrad_aten_kernels.cc
status: fresh
symbol_base: 'cxx . . $ '
symbols:
  AtenSparseDenseMatmulGradWithAdagrad: torch_tpu/AtenSparseDenseMatmulGradWithAdagrad(a0c1708e567e2eab).
  SparseDenseMatmulGradWithAdagradBuilder: torch_tpu/`$anonymous_namespace_csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adagrad_aten_kernels.cc`/SparseDenseMatmulGradWithAdagradBuilder(7cf442c555d8bf4d).
  is_status_or_ref: is_status_or_ref#
---
# Module: [`csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adagrad_aten_kernels.cc`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adagrad_aten_kernels.cc)

## Classes
### <a id="is_status_or_ref"></a>`is_status_or_ref`
- def: [`csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adagrad_aten_kernels.cc:55`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adagrad_aten_kernels.cc#L55)
- signature: `using torch_tpu::is_status_or_ref`
- uses (calls/refs, reference-scoped): [`is_status_or_ref`](../../../common/error_utils.h.md#is_status_or_ref)

## Functions
- <a id="AtenSparseDenseMatmulGradWithAdagrad"></a>`AtenSparseDenseMatmulGradWithAdagrad(const at::Tensor& row_pointers, const at::Tensor& embedding_ids, const at::Tensor& sample_ids, const at::Tensor& gains, const at::Tensor& embedding_table, const at::Tensor& accumulator, const at::Tensor& activations_grad, const at::Tensor& learning_rate, double epsilon, int64_t device_batch_size, int64_t max_ids_per_partition, int64_t max_unique_ids_per_partition, std::string_view computation_name)` — [`L241`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adagrad_aten_kernels.cc#L241) — @brief Computes gradients and updates the embedding table using the Adagrad — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="SparseDenseMatmulGradWithAdagradBuilder"></a>`SparseDenseMatmulGradWithAdagradBuilder(int64_t device_batch_size, int64_t max_ids_per_partition, int64_t max_unique_ids_per_partition, std::string_view computation_name, double epsilon)` — [`L61`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adagrad_aten_kernels.cc#L61) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- `SparseDenseMatmulGradWithAdagradBuilder(int64_t device_batch_size, int64_t max_ids_per_partition, int64_t max_unique_ids_per_partition, std::string_view computation_name, double epsilon)` — [`L61`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adagrad_aten_kernels.cc#L61)

