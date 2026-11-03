---
title: 'Module: src/vllm_torchtpu/kernels/quantized_matmul/blockwise_kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/quantized_matmul/blockwise_kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.quantized_matmul.blockwise_kernel`/
symbols:
  quantized_matmul_kernel: quantized_matmul_kernel().
  quantized_matmul_kernel.kernel: quantized_matmul_kernel().kernel().
  quantized_matmul_kernel.kernel.accum: quantized_matmul_kernel().kernel().accum().
  quantize_tensor: quantize_tensor.
  MXU_SIZE: MXU_SIZE.
---
# Module: [`src/vllm_torchtpu/kernels/quantized_matmul/blockwise_kernel.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/blockwise_kernel.py)

## Functions
- <a id="quantized_matmul_kernel.kernel.accum"></a>`accum(is_first_step, is_last_step)` — [`L202`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/blockwise_kernel.py#L202)
- <a id="quantized_matmul_kernel.kernel"></a>`kernel(lhs_ref, rhs_ref, w_scales_ref, out_ref, acc_scratch)` — [`L197`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/blockwise_kernel.py#L197)
- <a id="quantized_matmul_kernel"></a>`quantized_matmul_kernel(x: jax.Array, w_q: jax.Array, w_scale: jax.Array, w_zp: jax.Array | None = None, block_size: int | None = None, x_q_dtype: jnp.dtype | None = None, *, tuned_value: TunedValue | None = None)` — [`L46`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/blockwise_kernel.py#L46) — Quantized matmul kernel with blockwise support.

## Module values
- <a id="MXU_SIZE"></a>`MXU_SIZE` — [`L36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/blockwise_kernel.py#L36)
- <a id="quantize_tensor"></a>`quantize_tensor` — [`L35`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/quantized_matmul/blockwise_kernel.py#L35)

