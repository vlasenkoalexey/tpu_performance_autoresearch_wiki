---
title: 'Module: csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenSparseGatherBackward: AtenSparseGatherBackward(7048bed50d562265).
  AtenSparseGather: AtenSparseGather(2f4a0512dc7e15bc).
  ValidateSparseGatherInputs: ValidateSparseGatherInputs(a6cc398f3a6c27d2).
  ValidateSparseGatherBackwardInputs: '`$anonymous_namespace_csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc`/ValidateSparseGatherBackwardInputs(6ddad2e2cbb424ad).'
  SparseGatherBackwardBuilder: '`$anonymous_namespace_csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc`/SparseGatherBackwardBuilder(1d46c14432b47e7a).'
  SparseGatherBuilder: '`$anonymous_namespace_csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc`/SparseGatherBuilder(7e42a56a9293e293).'
  AtenSparseGatherAutograd.forward: AtenSparseGatherAutograd#forward(72a2af3f83194d6d).
  AtenSparseGatherAutograd.backward: AtenSparseGatherAutograd#backward(305625f81d7e100).
---
# Module: [`csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc)

## Functions
- <a id="AtenSparseGather"></a>`AtenSparseGather(const at::Tensor& row_pointers, const at::Tensor& indices, const at::Tensor& operand, int64_t max_non_zeroes_per_row)` — [`L245`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc#L245) — @brief Performs sparse gather from an embedding table on TPU SparseCore. — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="AtenSparseGatherBackward"></a>`AtenSparseGatherBackward(const at::Tensor& grad_output, const at::Tensor& indices, const at::Tensor& grad_operand)` — [`L276`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc#L276) — @brief Performs sparse gather backward (scatter-add) accumulating gradients — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="SparseGatherBackwardBuilder"></a>`SparseGatherBackwardBuilder()` — [`L110`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc#L110) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="SparseGatherBuilder"></a>`SparseGatherBuilder(int64_t max_non_zeroes_per_row)` — [`L58`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc#L58)
- <a id="ValidateSparseGatherBackwardInputs"></a>`ValidateSparseGatherBackwardInputs(const at::Tensor& grad_output, const at::Tensor& indices, const at::Tensor& grad_operand)` — [`L180`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc#L180)
- <a id="ValidateSparseGatherInputs"></a>`ValidateSparseGatherInputs(const at::Tensor& row_pointers, const at::Tensor& indices, const at::Tensor& operand, int64_t max_non_zeroes_per_row)` — [`L209`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc#L209) — @brief Validates the inputs to the sparse gather op. — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)

## Other members
- <a id="AtenSparseGatherAutograd.backward"></a>`AtenSparseGatherAutograd.backward` — [`L336`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc#L336)
- <a id="AtenSparseGatherAutograd.forward"></a>`AtenSparseGatherAutograd.forward` — [`L315`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc#L315)

