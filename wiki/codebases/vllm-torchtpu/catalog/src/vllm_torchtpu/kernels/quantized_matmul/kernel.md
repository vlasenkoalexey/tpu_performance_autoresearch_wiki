---
title: 'Module: src/vllm_torchtpu/kernels/quantized_matmul/kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/quantized_matmul/kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.quantized_matmul.kernel`/
symbols:
  quantized_matmul_kernel: quantized_matmul_kernel().
  matmul_kernel: matmul_kernel().
  matmul_kernel.matmul_body: matmul_kernel().matmul_body().
  quantize_array: quantize_array().
  get_vmem_limit: get_vmem_limit().
  validate_inputs: validate_inputs().
---
# Module: [`src/vllm_torchtpu/kernels/quantized_matmul/kernel.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/kernel.py)

## Functions
- <a id="get_vmem_limit"></a>`get_vmem_limit(n_batch: int, n_out: int, n_in: int, batch_block_size: int, out_block_size: int, in_block_size: int, x_dtype: jnp.dtype, x_q_dtype: jnp.dtype, w_q_dtype: jnp.dtype, scale_dtype: jnp.dtype, out_dtype: jnp.dtype, acc_dtype: jnp.dtype, save_acc: bool, save_x_q: bool, upper_limit_bytes: int)` — [`L50`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/kernel.py#L50) — Calculate VMEM limit for the kernel.
- <a id="matmul_kernel.matmul_body"></a>`matmul_body(quant: bool, is_first_step: bool, is_last_step: bool)` — [`L185`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/kernel.py#L185)
- <a id="matmul_kernel"></a>`matmul_kernel(x_ref: jax.Array, w_q_ref: jax.Array, w_scale_ref: jax.Array, x_abs_max_ref: jax.Array, out_ref: jax.Array, acc_scratch: jax.Array, x_q_scratch: jax.Array, x_scale_scratch: jax.Array, *, x_q_dtype: jnp.dtype, save_acc: bool, save_x_q: bool)` — [`L140`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/kernel.py#L140)
- <a id="quantize_array"></a>`quantize_array(x: jax.Array, x_abs_max: jax.Array, quant_dtype: jnp.dtype)` — [`L36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/kernel.py#L36)
- <a id="quantized_matmul_kernel"></a>`quantized_matmul_kernel(x: jax.Array, w_q: jax.Array, w_scale: jax.Array, w_zp: jax.Array | None = None, block_size: int | None = None, x_q_dtype: jnp.dtype | None = None, *, tuned_value: TunedValue | None = None)` — [`L241`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/kernel.py#L241) — Quantized matmul kernel.
- <a id="validate_inputs"></a>`validate_inputs(x: jax.Array, w_q: jax.Array, w_scale: jax.Array, x_abs_max: jax.Array, x_q_dtype: jnp.dtype, batch_block_size: int, out_block_size: int, in_block_size: int)` — [`L105`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/kernel.py#L105) — Verify inputs invoking the kernel.

