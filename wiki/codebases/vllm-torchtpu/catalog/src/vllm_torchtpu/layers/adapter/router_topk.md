---
title: 'Module: src/vllm_torchtpu/layers/adapter/router_topk.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/router_topk.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.router_topk`/
symbols:
  _op: _op.
  rowmax_select: rowmax_select().
  _fake_router_topk: _fake_router_topk().
---
# Module: [`src/vllm_torchtpu/layers/adapter/router_topk.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/router_topk.py)

## Functions
- <a id="_fake_router_topk"></a>`_fake_router_topk(scores: torch.Tensor, topk: int)` — [`L28`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/router_topk.py#L28)
- <a id="rowmax_select"></a>`rowmax_select(scores: torch.Tensor, topk: int)` — [`L42`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/router_topk.py#L42) — Sort-free ``topk`` over the expert axis of ``[rows, experts]`` scores.

## Module values
- <a id="_op"></a>`_op` — [`L38`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/router_topk.py#L38)

