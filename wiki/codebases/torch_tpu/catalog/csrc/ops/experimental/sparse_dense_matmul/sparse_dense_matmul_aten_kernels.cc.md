---
title: 'Module: csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenSparseDenseMatmul: AtenSparseDenseMatmul(5fd15ba20fd682a).
  SparseDenseMatmulBuilder: '`$anonymous_namespace_csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_aten_kernels.cc`/SparseDenseMatmulBuilder(3ee184bc392c63d6).'
---
# Module: [`csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_aten_kernels.cc`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_aten_kernels.cc)

## Functions
- <a id="AtenSparseDenseMatmul"></a>`AtenSparseDenseMatmul(const at::Tensor& row_pointers, const at::Tensor& embedding_ids, const at::Tensor& sample_ids, const at::Tensor& gains, const at::Tensor& embedding_table, int64_t device_batch_size, int64_t max_ids_per_partition, int64_t max_unique_ids_per_partition)` — [`L132`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_aten_kernels.cc#L132) — @brief Performs sparse-dense matrix multiplication, equivalent to embedding — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="SparseDenseMatmulBuilder"></a>`SparseDenseMatmulBuilder(int64_t device_batch_size, int64_t max_ids_per_partition, int64_t max_unique_ids_per_partition)` — [`L51`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_aten_kernels.cc#L51)

