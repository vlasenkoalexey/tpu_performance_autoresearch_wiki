---
title: 'Module: src/vllm_torchtpu/layers/adapter/cp_mla_attention.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/cp_mla_attention.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.cp_mla_attention`/
symbols:
  merge_lse_partials_scatter_heads: merge_lse_partials_scatter_heads().
  all_gather_heads: all_gather_heads().
  merge_lse_partials_all_to_all: merge_lse_partials_all_to_all().
  all_gather_q_nope_pe_heads: all_gather_q_nope_pe_heads().
  _all_to_all: _all_to_all().
  _merge_received: _merge_received().
---
# Module: [`src/vllm_torchtpu/layers/adapter/cp_mla_attention.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_mla_attention.py)

## Functions
- <a id="_all_to_all"></a>`_all_to_all(x: torch.Tensor, group: Any)` — [`L140`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_mla_attention.py#L140) — Block `d` of `x`'s leading axis goes to rank `d`; block `r` of the
- <a id="_merge_received"></a>`_merge_received(o_recv: torch.Tensor, l_recv: torch.Tensor)` — [`L170`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_mla_attention.py#L170) — `[R, T, h, V]` partials and `[R, T, h]` lse -> the f32 `[T, h, V]` merge.
- <a id="all_gather_heads"></a>`all_gather_heads(q: torch.Tensor)` — [`L45`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_mla_attention.py#L45) — Widen a rank's query head slice to the whole DCP group's heads.
- <a id="all_gather_q_nope_pe_heads"></a>`all_gather_q_nope_pe_heads(ql_nope: torch.Tensor, q_pe: torch.Tensor, kv_lora_rank: int)` — [`L65`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_mla_attention.py#L65) — Fused all-gather of `(ql_nope, q_pe)` across DCP ranks in a single call.
- <a id="merge_lse_partials_all_to_all"></a>`merge_lse_partials_all_to_all(output: torch.Tensor, lse: torch.Tensor, group: Any)` — [`L151`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_mla_attention.py#L151) — Same result as the reduce-scatter merge, via all-to-all.
- <a id="merge_lse_partials_scatter_heads"></a>`merge_lse_partials_scatter_heads(output: torch.Tensor, lse: torch.Tensor, is_backbone: bool = True)` — [`L81`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/cp_mla_attention.py#L81) — Combine this rank's partial attention output with its peers'. — documented in [distributed-parallelism-and-meshes](../../../../../concepts/distributed-parallelism-and-meshes.md)

