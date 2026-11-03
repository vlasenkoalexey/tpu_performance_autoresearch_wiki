---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/mhc/fused_post_pre_kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/mhc/fused_post_pre_kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.mhc.fused_post_pre_kernel`/
symbols:
  fused_post_pre_mixes: fused_post_pre_mixes().
  mhc_fused_post_pre: mhc_fused_post_pre().
  _fused_kernel: _fused_kernel().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/mhc/fused_post_pre_kernel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/fused_post_pre_kernel.py)

## Functions
- <a id="_fused_kernel"></a>`_fused_kernel(x_ref, res_ref, post_ref, comb_ref, fn_hi_ref, fn_mid_ref, fn_lo_ref, sc_ref, hb_ref, newres_ref, mixes_ref, sqrsum_ref, layer_ref, *, hc_mult, hidden_size, gemm_precision, rms_eps, hc_pre_eps)` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/fused_post_pre_kernel.py#L27) — One token block: recombine, store once, 3-pass GEMM, collapse.
- <a id="fused_post_pre_mixes"></a>`fused_post_pre_mixes(x2d: jax.Array, res2d: jax.Array, post2d: jax.Array, comb2d: jax.Array, fn: jax.Array, hc_scale: jax.Array, hc_base: jax.Array, rms_eps: float, hc_pre_eps: float, *, token_block_size: int = 32, gemm_precision: str = "highest", vmem_limit_bytes: int = DEFAULT_VMEM_LIMIT_BYTES)` — [`L109`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/fused_post_pre_kernel.py#L109) — The Pallas seam kernel: post recombine fused with pre's mix GEMM
- <a id="mhc_fused_post_pre"></a>`mhc_fused_post_pre(x: jax.Array, residual: jax.Array, post_layer_mix: jax.Array, comb_res_mix: jax.Array, fn: jax.Array, hc_scale: jax.Array, hc_base: jax.Array, rms_eps: float, hc_pre_eps: float, hc_sinkhorn_eps: float, hc_post_mult_value: float, sinkhorn_repeat: int, *, token_block_size: int = 32, gemm_precision: str = "highest", vmem_limit_bytes: int = DEFAULT_VMEM_LIMIT_BYTES)` — [`L226`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/fused_post_pre_kernel.py#L226) — Fused seam op: Pallas post+GEMM+collapse kernel, XLA gates epilogue.

