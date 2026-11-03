---
title: 'Module: src/vllm_torchtpu/kernels/mla/masked_dense/csa_mask.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/mla/masked_dense/csa_mask.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.mla.masked_dense.csa_mask`/
symbols:
  mask_kernel._body: mask_kernel()._body().
  mask_kernel: mask_kernel().
  mask_kernel._body.vec_k_loop: mask_kernel()._body().vec_k_loop().
  mask_kernel._body.k_loop: mask_kernel()._body().k_loop().
  generate_mask_sc: generate_mask_sc().
  mask_kernel._body.vec_k_loop.write_fn: mask_kernel()._body().vec_k_loop().write_fn().
  mask_kernel._body.k_loop.write_fn: mask_kernel()._body().k_loop().write_fn().
---
# Module: [`src/vllm_torchtpu/kernels/mla/masked_dense/csa_mask.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/csa_mask.py)

## Functions
- <a id="mask_kernel._body"></a>`_body(topk_indices_vmem_ref, mask_out_vmem_ref)` — [`L53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/csa_mask.py#L53)
- <a id="generate_mask_sc"></a>`generate_mask_sc(topk_indices: jax.Array, max_kv_len: int)` — [`L103`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/csa_mask.py#L103) — Expands `topk_indices` into a dense `[num_tokens, max_kv_len]` bitmap.
- <a id="mask_kernel._body.k_loop"></a>`k_loop(k, _)` — [`L78`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/csa_mask.py#L78)
- <a id="mask_kernel"></a>`mask_kernel(topk_indices_hbm_ref: Any, mask_out_hbm_ref: Any, *, core_axis_name: str, subcore_axis_name: str, topk: int, max_kv_len: int)` — [`L37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/csa_mask.py#L37) — Writes one row of the bitmap per grid step, striped across subcores.
- <a id="mask_kernel._body.vec_k_loop"></a>`vec_k_loop(k_chunk, _)` — [`L61`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/csa_mask.py#L61)
- <a id="mask_kernel._body.vec_k_loop.write_fn"></a>`write_fn(i=idx)` — [`L66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/csa_mask.py#L66)
- <a id="mask_kernel._body.k_loop.write_fn"></a>`write_fn(i=idx)` — [`L81`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/csa_mask.py#L81)

