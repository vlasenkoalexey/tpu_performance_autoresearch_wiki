---
title: 'Module: src/vllm_torchtpu/kernels/quantized_matmul/util.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/quantized_matmul/util.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.quantized_matmul.util`/
symbols:
  get_kernel_name: get_kernel_name().
  unfold_args: unfold_args().
  quantize_block: quantize_block().
  next_multiple: next_multiple().
  xla_quantized_matmul: xla_quantized_matmul().
  quantize_tensor: quantize_tensor().
  xla_quantized_batched_matmul: xla_quantized_batched_matmul().
  get_vmem_limit: get_vmem_limit().
  validate_inputs: validate_inputs().
  get_max_min: get_max_min().
  quantize_array: quantize_array().
---
# Module: [`src/vllm_torchtpu/kernels/quantized_matmul/util.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/util.py)

## Functions
- <a id="get_kernel_name"></a>`get_kernel_name(tuned_value: TunedValue)` — [`L71`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/util.py#L71)
- <a id="get_max_min"></a>`get_max_min(target_dtype)` — [`L294`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/util.py#L294)
- <a id="get_vmem_limit"></a>`get_vmem_limit(n_batch: int, n_out: int, n_in: int, batch_block_size: int, out_block_size: int, in_block_size: int, x_dtype: jnp.dtype, x_q_dtype: jnp.dtype, w_q_dtype: jnp.dtype, scale_dtype: jnp.dtype, out_dtype: jnp.dtype, acc_dtype: jnp.dtype, save_acc: bool, save_x_q: bool, upper_limit_bytes: int)` — [`L211`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/util.py#L211) — Calculate VMEM limit for the kernel.
- <a id="next_multiple"></a>`next_multiple(x, multiple)` — [`L67`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/util.py#L67)
- <a id="quantize_array"></a>`quantize_array(x: jax.Array, x_abs_max: jax.Array, quant_dtype: jnp.dtype)` — [`L196`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/util.py#L196)
- <a id="quantize_block"></a>`quantize_block(data, axis, target_dtype)` — [`L303`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/util.py#L303) — Calculates scale and quantizes a block of data.
- <a id="quantize_tensor"></a>`quantize_tensor(x: jax.Array, dtype: jnp.dtype, dim: int = -1, block_size: int | None = None)` — [`L47`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/util.py#L47)
- <a id="unfold_args"></a>`unfold_args(conditions: tuple[jax.Array | bool, ...], fn_conditions: tuple[bool, ...], fn: Callable[..., Any])` — [`L26`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/util.py#L26) — Minimize run-time branching of fn by converting jnp.bool to python bool.
- <a id="validate_inputs"></a>`validate_inputs(x: jax.Array, w_q: jax.Array, w_scale: jax.Array, x_abs_max: jax.Array | None, batch_block_size: int, out_block_size: int, in_block_size: int)` — [`L266`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/util.py#L266) — Verify inputs invoking the kernel.
- <a id="xla_quantized_batched_matmul"></a>`xla_quantized_batched_matmul(x: jax.Array, w_q: jax.Array, w_scale: jax.Array, dimension_numbers: tuple, quantize_activation: bool = True)` — [`L127`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/util.py#L127) — Quantized matmul with batch dimensions via dot_general.
- <a id="xla_quantized_matmul"></a>`xla_quantized_matmul(x: jax.Array, w_q: jax.Array, w_scale: jax.Array, quantize_activation=True)` — [`L80`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/util.py#L80) — Reference (pure JAX) implementation of the quantized matmul kernel.

