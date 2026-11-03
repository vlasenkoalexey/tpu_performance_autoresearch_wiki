---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/mhc/pre_kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/mhc/pre_kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.mhc.pre_kernel`/
symbols:
  mhc_pre_mixes_collapse: mhc_pre_mixes_collapse().
  mhc_pre_mixes: mhc_pre_mixes().
  mhc_pre: mhc_pre().
  _mixes_kernel: _mixes_kernel().
  _mixes_collapse_kernel: _mixes_collapse_kernel().
  _dot3: _dot3().
  mhc_pre_mixes._vmem_need: mhc_pre_mixes()._vmem_need().
  mhc_pre_mixes_collapse._vmem_need: mhc_pre_mixes_collapse()._vmem_need().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/mhc/pre_kernel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/pre_kernel.py)

## Functions
- <a id="_dot3"></a>`_dot3(x, fn_hi_ref, fn_mid_ref, fn_lo_ref)` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/pre_kernel.py#L27) — 3-pass exact GEMM: x is bf16 (its low chunks are zero), so three
- <a id="_mixes_collapse_kernel"></a>`_mixes_collapse_kernel(x_ref, fn_hi_ref, fn_mid_ref, fn_lo_ref, sc_ref, hb_ref, mixes_ref, sqrsum_ref, layer_ref, *, hc_mult, hidden_size, rms_eps, hc_pre_eps)` — [`L51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/pre_kernel.py#L51) — Mixes kernel plus the in-block collapse.
- <a id="_mixes_kernel"></a>`_mixes_kernel(x_ref, fn_hi_ref, fn_mid_ref, fn_lo_ref, mixes_ref, sqrsum_ref)` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/pre_kernel.py#L43) — One token block: 3-pass exact GEMM against resident fn chunks.
- <a id="mhc_pre_mixes._vmem_need"></a>`_vmem_need(tb: int)` — [`L117`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/pre_kernel.py#L117)
- <a id="mhc_pre_mixes_collapse._vmem_need"></a>`_vmem_need(tb: int)` — [`L198`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/pre_kernel.py#L198)
- <a id="mhc_pre"></a>`mhc_pre(residual: jax.Array, fn: jax.Array, hc_scale: jax.Array, hc_base: jax.Array, rms_eps: float, hc_pre_eps: float, hc_sinkhorn_eps: float, hc_post_mult_value: float, sinkhorn_repeat: int, *, token_block_size: int = 64, vmem_limit_bytes: int = DEFAULT_VMEM_LIMIT_BYTES)` — [`L260`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/pre_kernel.py#L260) — ``mhc_pre`` with the mix GEMM AND the collapse in Pallas; only the
- <a id="mhc_pre_mixes"></a>`mhc_pre_mixes(x2d: jax.Array, fn: jax.Array, *, token_block_size: int = 64, vmem_limit_bytes: int = DEFAULT_VMEM_LIMIT_BYTES)` — [`L91`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/pre_kernel.py#L91) — Pallas replacement for the mix GEMM + squared sum of mhc_pre.
- <a id="mhc_pre_mixes_collapse"></a>`mhc_pre_mixes_collapse(x2d: jax.Array, fn: jax.Array, hc_scale: jax.Array, hc_base: jax.Array, rms_eps: float, hc_pre_eps: float, *, token_block_size: int = 64, vmem_limit_bytes: int = DEFAULT_VMEM_LIMIT_BYTES)` — [`L169`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/pre_kernel.py#L169) — Mixes + in-block collapse: the full memory-bound half of ``mhc_pre``.

