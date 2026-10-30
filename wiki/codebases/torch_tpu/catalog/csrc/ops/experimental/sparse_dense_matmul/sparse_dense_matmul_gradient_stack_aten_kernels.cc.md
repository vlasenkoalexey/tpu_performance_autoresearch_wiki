---
title: 'Module: csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_gradient_stack_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_gradient_stack_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenSparseDenseMatmulGradientStack: AtenSparseDenseMatmulGradientStack(5f232bf6c25e94a0).
  ValidateSparseDenseMatmulGradientStackInputs: ValidateSparseDenseMatmulGradientStackInputs(4a6aa476d7be490e).
  SparseDenseMatmulGradientStackBuilder: '`$anonymous_namespace_csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_gradient_stack_aten_kernels.cc`/SparseDenseMatmulGradientStackBuilder(6a1197bfb748c94f).'
---
# Module: [`csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_gradient_stack_aten_kernels.cc`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_gradient_stack_aten_kernels.cc)

## Functions
- <a id="AtenSparseDenseMatmulGradientStack"></a>`AtenSparseDenseMatmulGradientStack(at::TensorList unstacked_gradients, int64_t stacked_batch_size, int64_t stacked_feature_dim)` — [`L142`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_gradient_stack_aten_kernels.cc#L142) — @brief Stacks and interleaves unstacked gradients across SparseCore cores. — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="SparseDenseMatmulGradientStackBuilder"></a>`SparseDenseMatmulGradientStackBuilder(int64_t stacked_batch_size, int64_t stacked_feature_dim)` — [`L53`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_gradient_stack_aten_kernels.cc#L53)
- <a id="ValidateSparseDenseMatmulGradientStackInputs"></a>`ValidateSparseDenseMatmulGradientStackInputs(at::TensorList unstacked_gradients, int64_t stacked_batch_size, int64_t stacked_feature_dim)` — [`L104`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_gradient_stack_aten_kernels.cc#L104) — @brief Validates the inputs to the sparse-dense matmul gradient stack op. — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)

