---
title: 'Module: src/vllm_torchtpu/kernels/fused_moe/v2/router_ops.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/fused_moe/v2/router_ops.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.fused_moe.v2.router_ops`/
symbols:
  pallas_select: pallas_select().
  _select_kernel: _select_kernel().
  _select_kernel_split: _select_kernel_split().
  NEG: NEG.
---
# Module: [`src/vllm_torchtpu/kernels/fused_moe/v2/router_ops.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/router_ops.py)

## Functions
- <a id="_select_kernel"></a>`_select_kernel(x_ref, w_ref, i_ref, *, topk, n, v_ref=None)` — [`L36`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/router_ops.py#L36) — One block of rows: take the top `topk` by repeated max-and-mask.
- <a id="_select_kernel_split"></a>`_select_kernel_split(x_ref, v_ref, w_ref, i_ref, *, topk, n)` — [`L59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/router_ops.py#L59) — Select by x_ref and read the selected weights from v_ref.
- <a id="pallas_select"></a>`pallas_select(scores, topk=10, block_rows=256, weight_scores=None, interpret=False)` — [`L69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/router_ops.py#L69) — Top-k over [R, N] scores -> (weights f32, indices i32) [R, topk].

## Module values
- <a id="NEG"></a>`NEG` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/router_ops.py#L33)

