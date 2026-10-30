---
title: 'Module: src/torch_tpu/_internal/ops/ops.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/ops/ops.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.ops.ops`/
symbols:
  optimization_barrier: optimization_barrier().
  max_pool1d: max_pool1d().
  max_pool1d_backward: max_pool1d_backward().
  max_pool2d: max_pool2d().
  max_pool2d_backward: max_pool2d_backward().
  max_pool3d: max_pool3d().
  max_pool3d_backward: max_pool3d_backward().
  ragged_dot: ragged_dot().
  ragged_dot_weight_grad: ragged_dot_weight_grad().
  ragged_all_to_all: ragged_all_to_all().
  send: send().
  recv: recv().
  sparse_dense_matmul: sparse_dense_matmul().
  sparse_dense_matmul_grad_with_sgd: sparse_dense_matmul_grad_with_sgd().
  sparse_dense_matmul_grad_with_adagrad: sparse_dense_matmul_grad_with_adagrad().
  sparse_dense_matmul_grad_with_adam: sparse_dense_matmul_grad_with_adam().
  sparse_dense_matmul_activation_unstack: sparse_dense_matmul_activation_unstack().
  sparse_dense_matmul_gradient_stack: sparse_dense_matmul_gradient_stack().
  sparse_gather: sparse_gather().
  sparse_gather_backward: sparse_gather_backward().
  sparse_iota: sparse_iota().
  sparse_map_row: sparse_map_row().
  __all__: __all__.
---
# Module: [`src/torch_tpu/_internal/ops/ops.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py)

## Functions
- <a id="max_pool1d"></a>`max_pool1d(input: torch.Tensor, kernel_size: Sequence[int], stride: Sequence[int], padding: Sequence[int], dilation: Sequence[int], ceil_mode: bool)` — [`L64`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L64) — Applies 1D max pooling to a TPU tensor without computing indices.
- <a id="max_pool1d_backward"></a>`max_pool1d_backward(grad_output: torch.Tensor, input: torch.Tensor, kernel_size: Sequence[int], stride: Sequence[int], padding: Sequence[int], dilation: Sequence[int], ceil_mode: bool)` — [`L94`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L94) — Computes the gradient of `max_pool1d` with respect to its input.
- <a id="max_pool2d"></a>`max_pool2d(input: torch.Tensor, kernel_size: Sequence[int], stride: Sequence[int], padding: Sequence[int], dilation: Sequence[int], ceil_mode: bool)` — [`L126`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L126) — Applies 2D max pooling to a TPU tensor without computing indices.
- <a id="max_pool2d_backward"></a>`max_pool2d_backward(grad_output: torch.Tensor, input: torch.Tensor, kernel_size: Sequence[int], stride: Sequence[int], padding: Sequence[int], dilation: Sequence[int], ceil_mode: bool)` — [`L156`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L156) — Computes the gradient of `max_pool2d` with respect to its input.
- <a id="max_pool3d"></a>`max_pool3d(input: torch.Tensor, kernel_size: Sequence[int], stride: Sequence[int], padding: Sequence[int], dilation: Sequence[int], ceil_mode: bool)` — [`L188`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L188) — Applies 3D max pooling to a TPU tensor without computing indices.
- <a id="max_pool3d_backward"></a>`max_pool3d_backward(grad_output: torch.Tensor, input: torch.Tensor, kernel_size: Sequence[int], stride: Sequence[int], padding: Sequence[int], dilation: Sequence[int], ceil_mode: bool)` — [`L220`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L220) — Computes the gradient of `max_pool3d` with respect to its input.
- <a id="optimization_barrier"></a>`optimization_barrier(inputs: Sequence[torch.Tensor])` — [`L27`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L27) — Inserts an XLA optimization barrier around `inputs`.
- <a id="ragged_all_to_all"></a>`ragged_all_to_all(operand: torch.Tensor, output: torch.Tensor, input_offsets: torch.Tensor, send_sizes: torch.Tensor, output_offsets: torch.Tensor, recv_sizes: torch.Tensor, process_group_name: str, *, out: torch.Tensor | None = None)` — [`L321`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L321) — Exchanges ragged slices of a tensor among the ranks of a process group.
- <a id="ragged_dot"></a>`ragged_dot(lhs: torch.Tensor, rhs: torch.Tensor, group_sizes: torch.Tensor, *, out: torch.Tensor | None = None)` — [`L254`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L254) — Computes a ragged dot product, e.g. for Mixture-of-Experts models.
- <a id="ragged_dot_weight_grad"></a>`ragged_dot_weight_grad(lhs: torch.Tensor, grad_output: torch.Tensor, group_sizes: torch.Tensor)` — [`L292`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L292) — Computes the gradient of `ragged_dot` with respect to `rhs`.
- <a id="recv"></a>`recv(tensors: Sequence[torch.Tensor], src: int, tag: int)` — [`L402`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L402) — Receives tensors from another rank of the default TPU process group.
- <a id="send"></a>`send(tensors: Sequence[torch.Tensor], dst: int, tag: int)` — [`L384`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L384) — Sends tensors to another rank of the default TPU process group.
- <a id="sparse_dense_matmul"></a>`sparse_dense_matmul(row_pointers: torch.Tensor, embedding_ids: torch.Tensor, sample_ids: torch.Tensor, gains: torch.Tensor, embedding_table: torch.Tensor, device_batch_size: int, max_ids_per_partition: int, max_unique_ids_per_partition: int)` — [`L421`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L421) — Looks up and combines embeddings on TPU SparseCore.
- <a id="sparse_dense_matmul_activation_unstack"></a>`sparse_dense_matmul_activation_unstack(stacked_activations: torch.Tensor, per_feature_batch_sizes: Sequence[int], per_feature_dims: Sequence[int])` — [`L642`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L642) — Splits the stacked activations of multiple features into one per feature.
- <a id="sparse_dense_matmul_grad_with_adagrad"></a>`sparse_dense_matmul_grad_with_adagrad(row_pointers: torch.Tensor, embedding_ids: torch.Tensor, sample_ids: torch.Tensor, gains: torch.Tensor, embedding_table: torch.Tensor, accumulator: torch.Tensor, activations_grad: torch.Tensor, learning_rate: torch.Tensor, epsilon: float, device_batch_size: int, max_ids_per_partition: int, max_unique_ids_per_partition: int, computation_name: str)` — [`L518`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L518) — Backpropagates through `sparse_dense_matmul` and applies an Adagrad update.
- <a id="sparse_dense_matmul_grad_with_adam"></a>`sparse_dense_matmul_grad_with_adam(row_pointers: torch.Tensor, embedding_ids: torch.Tensor, sample_ids: torch.Tensor, gains: torch.Tensor, embedding_table: torch.Tensor, momentum: torch.Tensor, velocity: torch.Tensor, activations_grad: torch.Tensor, alpha_t: torch.Tensor, beta_1: float, beta_2: float, epsilon: float, device_batch_size: int, max_ids_per_partition: int, max_unique_ids_per_partition: int, computation_name: str)` — [`L576`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L576) — Backpropagates through `sparse_dense_matmul` and applies an Adam update.
- <a id="sparse_dense_matmul_grad_with_sgd"></a>`sparse_dense_matmul_grad_with_sgd(row_pointers: torch.Tensor, embedding_ids: torch.Tensor, sample_ids: torch.Tensor, gains: torch.Tensor, embedding_table: torch.Tensor, activations_grad: torch.Tensor, learning_rate: torch.Tensor, device_batch_size: int, max_ids_per_partition: int, max_unique_ids_per_partition: int, computation_name: str)` — [`L467`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L467) — Backpropagates through `sparse_dense_matmul` and applies an SGD update.
- <a id="sparse_dense_matmul_gradient_stack"></a>`sparse_dense_matmul_gradient_stack(unstacked_gradients: Sequence[torch.Tensor], stacked_batch_size: int, stacked_feature_dim: int)` — [`L669`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L669) — Stacks the activation gradients of multiple features into one tensor.
- <a id="sparse_gather"></a>`sparse_gather(row_pointers: torch.Tensor, indices: torch.Tensor, operand: torch.Tensor, max_non_zeroes_per_row: int)` — [`L694`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L694) — Gathers rows of `operand` on TPU SparseCore.
- <a id="sparse_gather_backward"></a>`sparse_gather_backward(grad_output: torch.Tensor, indices: torch.Tensor, grad_operand: torch.Tensor)` — [`L724`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L724) — Scatter-adds the gradient of `sparse_gather` into `grad_operand`.
- <a id="sparse_iota"></a>`sparse_iota(row_pointers: torch.Tensor, max_non_zeroes: int, max_non_zeroes_per_row: int)` — [`L748`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L748) — Generates the position of each non-zero within its CSR row on SparseCore.
- <a id="sparse_map_row"></a>`sparse_map_row(csr_tensors: Sequence[torch.Tensor], csr_lengths: Sequence[int], dense_args: Sequence[torch.Tensor], body_mlir: str, dummy_outputs: Sequence[torch.Tensor], max_non_zeroes_per_row: int, pad_value: int, max_pad_per_row: int, wait_threshold: float, result_row_pointer_op_index: int)` — [`L771`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L771) — Maps a row-wise computation over sparse CSR matrices on TPU SparseCore.

## Module values
- <a id="__all__"></a>`__all__` — [`L816`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/ops.py#L816)

