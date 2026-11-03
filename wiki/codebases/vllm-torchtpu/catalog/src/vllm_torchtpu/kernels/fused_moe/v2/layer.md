---
title: 'Module: src/vllm_torchtpu/kernels/fused_moe/v2/layer.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/fused_moe/v2/layer.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.fused_moe.v2.layer`/
symbols:
  fused_ep_moe_v2.compute_local: fused_ep_moe_v2().compute_local().
  fused_ep_moe_v2: fused_ep_moe_v2().
  fused_ep_moe_v2.select_local: fused_ep_moe_v2().select_local().
  fused_ep_moe_v2.quantize_local: fused_ep_moe_v2().quantize_local().
  fused_ep_moe_v2.local_fn: fused_ep_moe_v2().local_fn().
  _exchange_layout: _exchange_layout().
  _combine_arrivals: _combine_arrivals().
  fused_ep_moe_v2.route_fn: fused_ep_moe_v2().route_fn().
  fused_ep_moe_v2.compute_fn: fused_ep_moe_v2().compute_fn().
  SCORING_FNS: SCORING_FNS.
  fused_ep_moe_v2.unpack_operands: fused_ep_moe_v2().unpack_operands().
  _apply_scoring_fn: _apply_scoring_fn().
  _LAYER_SM_CACHE: _LAYER_SM_CACHE.
  _row_routes: _row_routes().
  _pack_routing_exchange: _pack_routing_exchange().
  _unpack_routing_exchange: _unpack_routing_exchange().
  _relabel_expert_ids_to_mesh_order: _relabel_expert_ids_to_mesh_order().
  AGQ_MIN_LOCAL_TOKENS: AGQ_MIN_LOCAL_TOKENS.
  _LAYER_SM_CACHE_LOCK: _LAYER_SM_CACHE_LOCK.
---
# Module: [`src/vllm_torchtpu/kernels/fused_moe/v2/layer.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py)

## Functions
- <a id="_apply_scoring_fn"></a>`_apply_scoring_fn(logits, scoring_fn)` — [`L73`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L73) — Gate logits -> f32 routing scores.
- <a id="_combine_arrivals"></a>`_combine_arrivals(arrivals, arrival_scales, pos, mirror_pos, topk_weights, out_dtype)` — [`L99`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L99) — Combine arrivals [rows, lane blocks, 128] into [t_local, hidden].
- <a id="_exchange_layout"></a>`_exchange_layout(t_local, topk, e_total, quantized)` — [`L157`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L157) — (scale offset, count offset, width) of the flat routing payload. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="_pack_routing_exchange"></a>`_pack_routing_exchange(pairs, scale_bits, counts, layout)` — [`L175`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L175) — The flat i32 payload: pairs [t*K], row-scale bits [t], counts [E].
- <a id="_relabel_expert_ids_to_mesh_order"></a>`_relabel_expert_ids_to_mesh_order(topk_idx, *, g_local, mesh_ep_ranks)` — [`L211`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L211) — Map selected experts from EP-rank order to device-mesh order.
- <a id="_row_routes"></a>`_row_routes(scores, gate_l)` — [`L87`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L87) — Per-token `[rows, 1]` mask: True iff the row has a finite score and logit.
- <a id="_unpack_routing_exchange"></a>`_unpack_routing_exchange(exchange, layout, t_local, topk, e_total)` — [`L192`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L192) — Inverse of _pack_routing_exchange over the gathered [ep, width] rows.
- <a id="fused_ep_moe_v2.compute_fn"></a>`compute_fn(x_l, rank_l, w1_l, w2_l, *scales_gating_biases_routed)` — [`L839`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L839) — stage="compute": the layer from route's outputs, rows gathered. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="fused_ep_moe_v2.compute_local"></a>`compute_local(q_g, exchange, local_blocks, block_hist, topk_weights, row_routes, rank_l, w1_l, w2_l, w1s_l, w2s_l, bias_it, out_dtype)` — [`L621`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L621) — Plan, kernel and combine over the gathered rows and payload. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="fused_ep_moe_v2"></a>`fused_ep_moe_v2(x, w1, w2, w1_scale, w2_scale, gating, w1_bias=None, w2_bias=None, *, topk, renormalize, mesh, capacity, block=None, ragged_stride=None, weight_format=WeightFormat.FP8, rhs_qb=None, act_fn="silu", rank=None, mesh_ep_ranks=None, sharded_plan=False, scoring_fn="softmax", score_bias=None, hash_topk_ids=None, routed_scaling_factor=1, token_replica_groups=None, stage="fused", routed=None, gather_positions=None)` — [`L253`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L253) — Run one MoE layer through the fused expert-parallel kernel. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="fused_ep_moe_v2.local_fn"></a>`local_fn(x_l, rank_l, w1_l, w2_l, *scales_gating_biases)` — [`L796`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L796) — One shard's half of the layer: route, dispatch, kernel, combine. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="fused_ep_moe_v2.quantize_local"></a>`quantize_local(x_l, rank_l, gate_l, hash_l)` — [`L512`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L512) — Split this shard's rows out of a replica group and quantize them. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="fused_ep_moe_v2.route_fn"></a>`route_fn(x_l, rank_l, w1_l, w2_l, *scales_gating_biases)` — [`L825`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L825) — stage="route": the wire rows, router weights and payload. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="fused_ep_moe_v2.select_local"></a>`select_local(gate_l, hash_l, score_bias_l, row_scale_l)` — [`L540`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L540) — Top-k, router weights, and this shard's routing payload. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="fused_ep_moe_v2.unpack_operands"></a>`unpack_operands(scales_gating_biases)` — [`L498`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L498) — (w1 scale, w2 scale, gate, hash ids, score bias, bias iterator).

## Module values
- <a id="AGQ_MIN_LOCAL_TOKENS"></a>`AGQ_MIN_LOCAL_TOKENS` — [`L245`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L245)
- <a id="SCORING_FNS"></a>`SCORING_FNS` — [`L70`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L70) — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="_LAYER_SM_CACHE"></a>`_LAYER_SM_CACHE` — [`L249`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L249)
- <a id="_LAYER_SM_CACHE_LOCK"></a>`_LAYER_SM_CACHE_LOCK` — [`L250`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/layer.py#L250)

