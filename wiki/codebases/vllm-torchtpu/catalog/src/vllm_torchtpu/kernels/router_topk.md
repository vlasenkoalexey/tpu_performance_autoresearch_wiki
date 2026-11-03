---
title: 'Module: src/vllm_torchtpu/kernels/router_topk.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/router_topk.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.router_topk`/
symbols:
  select: select().
  router_topk: router_topk().
  _select_kernel: _select_kernel().
  NEG: NEG.
  MAX_BLOCK_ROWS: MAX_BLOCK_ROWS.
---
# Module: [`src/vllm_torchtpu/kernels/router_topk.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/router_topk.py)

## Functions
- <a id="_select_kernel"></a>`_select_kernel(x_ref, w_ref, i_ref, *, topk: int, n: int)` — [`L38`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/router_topk.py#L38) — One block of rows: top ``topk`` by repeated max-and-mask.
- <a id="router_topk"></a>`router_topk(scores: jax.Array, topk: int)` — [`L98`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/router_topk.py#L98) — ``select`` with a jax_op-compatible signature (arrays, then statics).
- <a id="select"></a>`select(scores: jax.Array, topk: int, interpret: bool = False)` — [`L66`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/router_topk.py#L66) — Top-k over ``[rows, experts]`` f32 scores, values descending.

## Module values
- <a id="MAX_BLOCK_ROWS"></a>`MAX_BLOCK_ROWS` — [`L35`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/router_topk.py#L35)
- <a id="NEG"></a>`NEG` — [`L31`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/router_topk.py#L31)

