---
title: 'Module: src/vllm_torchtpu/kernels/diffusion_attention/qk_norm_rope.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/diffusion_attention/qk_norm_rope.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.diffusion_attention.qk_norm_rope`/
symbols:
  qk_norm_rope: qk_norm_rope().
  DEFAULT_BLOCK_ROWS: DEFAULT_BLOCK_ROWS.
  _pair_swap: _pair_swap().
  _kernel: _kernel().
---
# Module: [`src/vllm_torchtpu/kernels/diffusion_attention/qk_norm_rope.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/qk_norm_rope.py)

## Functions
- <a id="_kernel"></a>`_kernel(q_ref: jax.Ref, k_ref: jax.Ref, wq_ref: jax.Ref, wk_ref: jax.Ref, cos_ref: jax.Ref, sin_ref: jax.Ref, p_ref: jax.Ref, q_out_ref: jax.Ref, k_out_ref: jax.Ref, *, eps: float, head_dim: int, num_heads: int)` — [`L53`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/qk_norm_rope.py#L53)
- <a id="_pair_swap"></a>`_pair_swap(head_dim: int)` — [`L45`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/qk_norm_rope.py#L45)
- <a id="qk_norm_rope"></a>`qk_norm_rope(qkv: jax.Array, wq: jax.Array, wk: jax.Array, cos: jax.Array, sin: jax.Array, *, eps: float, head_dim: int, block_rows: int = DEFAULT_BLOCK_ROWS)` — [`L90`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/qk_norm_rope.py#L90) — Normalized, rotated ``(q, k)`` from a fused QKV projection output.

## Module values
- <a id="DEFAULT_BLOCK_ROWS"></a>`DEFAULT_BLOCK_ROWS` — [`L42`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/qk_norm_rope.py#L42)

