---
title: 'Module: src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/layer.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/layer.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.adaptive_fused_moe.layer`/
symbols:
  adaptive_fused_moe.local_fn: adaptive_fused_moe().local_fn().
  adaptive_fused_moe: adaptive_fused_moe().
  _combine_arrivals: _combine_arrivals().
  _exchange_layout: _exchange_layout().
  _LAYER_SM_CACHE: _LAYER_SM_CACHE.
  _pack_routing_exchange: _pack_routing_exchange().
  _unpack_routing_exchange: _unpack_routing_exchange().
  _relabel_expert_ids_to_mesh_order: _relabel_expert_ids_to_mesh_order().
  AGQ_MIN_LOCAL_TOKENS: AGQ_MIN_LOCAL_TOKENS.
  _LAYER_SM_CACHE_LOCK: _LAYER_SM_CACHE_LOCK.
---
# Module: [`src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/layer.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/layer.py)

## Functions
- <a id="_combine_arrivals"></a>`_combine_arrivals(arrivals, arrival_scales, pos, mirror_pos, topk_weights, out_dtype)` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/layer.py#L67) — Combine arrivals [rows, lane blocks, 128] into [t_local, hidden]. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="_exchange_layout"></a>`_exchange_layout(t_local, topk, e_total, quantized)` — [`L125`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/layer.py#L125) — (scale offset, count offset, width) of the flat routing payload.
- <a id="_pack_routing_exchange"></a>`_pack_routing_exchange(pairs, scale_bits, counts, layout)` — [`L143`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/layer.py#L143) — The flat i32 payload: pairs [t*K], row-scale bits [t], counts [E].
- <a id="_relabel_expert_ids_to_mesh_order"></a>`_relabel_expert_ids_to_mesh_order(topk_idx, *, g_local, mesh_ep_ranks)` — [`L179`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/layer.py#L179) — Map selected experts from EP-rank order to device-mesh order.
- <a id="_unpack_routing_exchange"></a>`_unpack_routing_exchange(exchange, layout, t_local, topk, e_total)` — [`L160`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/layer.py#L160) — Inverse of _pack_routing_exchange over the gathered [ep, width] rows.
- <a id="adaptive_fused_moe"></a>`adaptive_fused_moe(x, w1, w2, w1_scale, w2_scale, gating, w1_bias=None, w2_bias=None, *, topk, renormalize, mesh, capacity, block=None, ragged_stride=None, weight_format=None, rhs_qb=None, act_fn="silu", rank=None, mesh_ep_ranks=None, token_replica_groups=None)` — [`L221`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/layer.py#L221) — Run one MoE layer through the fused expert-parallel kernel. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="adaptive_fused_moe.local_fn"></a>`local_fn(x_l, rank_l, w1_l, w2_l, *scales_gating_biases)` — [`L430`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/layer.py#L430) — One shard's half of the layer: route, dispatch, kernel, combine. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)

## Module values
- <a id="AGQ_MIN_LOCAL_TOKENS"></a>`AGQ_MIN_LOCAL_TOKENS` — [`L213`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/layer.py#L213)
- <a id="_LAYER_SM_CACHE"></a>`_LAYER_SM_CACHE` — [`L217`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/layer.py#L217)
- <a id="_LAYER_SM_CACHE_LOCK"></a>`_LAYER_SM_CACHE_LOCK` — [`L218`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/layer.py#L218)

