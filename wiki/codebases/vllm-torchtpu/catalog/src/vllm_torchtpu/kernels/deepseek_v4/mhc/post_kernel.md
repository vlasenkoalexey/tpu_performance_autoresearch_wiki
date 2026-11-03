---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/mhc/post_kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/mhc/post_kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.mhc.post_kernel`/
symbols:
  mhc_post_2d: mhc_post_2d().
  mhc_post: mhc_post().
  _post_kernel: _post_kernel().
  mhc_post_2d._vmem_need: mhc_post_2d()._vmem_need().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/mhc/post_kernel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/post_kernel.py)

## Functions
- <a id="_post_kernel"></a>`_post_kernel(x_ref, res_ref, post_ref, comb_ref, out_ref, *, hc_mult, hidden_size)` — [`L26`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/post_kernel.py#L26) — One token block of the unrolled stream recombine.
- <a id="mhc_post_2d._vmem_need"></a>`_vmem_need(tb: int)` — [`L82`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/post_kernel.py#L82)
- <a id="mhc_post"></a>`mhc_post(x: jax.Array, residual: jax.Array, post_layer_mix: jax.Array, comb_res_mix: jax.Array, *, token_block_size: int = 64, vmem_limit_bytes: int = DEFAULT_VMEM_LIMIT_BYTES)` — [`L123`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/post_kernel.py#L123) — Pallas replacement for vLLM's ``mhc_post_torch``.
- <a id="mhc_post_2d"></a>`mhc_post_2d(x: jax.Array, res2d: jax.Array, post_layer_mix: jax.Array, comb_res_mix: jax.Array, *, token_block_size: int = 64, vmem_limit_bytes: int = DEFAULT_VMEM_LIMIT_BYTES)` — [`L45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/post_kernel.py#L45) — 2D-native entry: the kernel's own layout as public API.

