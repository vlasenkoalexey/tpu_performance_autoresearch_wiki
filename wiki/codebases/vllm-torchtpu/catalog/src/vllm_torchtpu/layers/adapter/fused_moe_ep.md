---
title: 'Module: src/vllm_torchtpu/layers/adapter/fused_moe_ep.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/fused_moe_ep.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.fused_moe_ep`/
symbols:
  prebuild_fused_moe_ep: prebuild_fused_moe_ep().
  _build_split_ops: _build_split_ops().
  _build_op: _build_op().
  fused_moe_ep: fused_moe_ep().
  fused_moe_ep_supported: fused_moe_ep_supported().
  fused_moe_ep_unsupported_reason: fused_moe_ep_unsupported_reason().
  logger: logger.
  _build_op.call: _build_op().call().
  _build_split_ops._route_fake: _build_split_ops()._route_fake().
  _unsupported_routing_reason: _unsupported_routing_reason().
  register_fused_scale_buffers: register_fused_scale_buffers().
  register_score_bias_buffer: register_score_bias_buffer().
  score_bias_operand: score_bias_operand().
  FUSED_MOE_EP_OP_ATTR: FUSED_MOE_EP_OP_ATTR.
  _SortedGatherOp.__call__: _SortedGatherOp#__call__().
  _simulated_routing_operands: _simulated_routing_operands().
  _mesh_expert_order: _mesh_expert_order().
  _OPS._OPS: _OPS._OPS.
  _build_op.moe: _build_op().moe().
  _build_op.moe_with_score_bias: _build_op().moe_with_score_bias().
  _build_op.moe_with_hash_ids: _build_op().moe_with_hash_ids().
  _build_split_ops.route_extra: _build_split_ops().route_extra().
  _build_split_ops.compute_extra: _build_split_ops().compute_extra().
  _TILE_M: _TILE_M.
  _RANK_BUFFER._RANK_BUFFER: _RANK_BUFFER._RANK_BUFFER.
  _SMEM_OVERHEAD_BYTES: _SMEM_OVERHEAD_BYTES.
  FUSED_MOE_EP_OP_NAME: FUSED_MOE_EP_OP_NAME.
  _squeeze_channel_scale: _squeeze_channel_scale().
  _build_split_ops.extra_kw: _build_split_ops().extra_kw().
  FUSED_MOE_EP_SCORE_BIAS_ATTR: FUSED_MOE_EP_SCORE_BIAS_ATTR.
  hash_topk_ids_operand: hash_topk_ids_operand().
  _squeeze_channel_scale_checked: _squeeze_channel_scale_checked().
  _routing_config: _routing_config().
  _build_op._fake: _build_op()._fake().
  _SortedGatherOp: _SortedGatherOp#
  _SortedGatherOp.route: _SortedGatherOp#route.
  _SortedGatherOp.compute: _SortedGatherOp#compute.
  _SortedGatherOp.group: _SortedGatherOp#group.
  _build_split_ops.route: _build_split_ops().route().
  _build_split_ops.compute: _build_split_ops().compute().
  _build_split_ops._compute_fake: _build_split_ops()._compute_fake().
  _max_node_tokens: _max_node_tokens().
  _smem_capacity_bytes: _smem_capacity_bytes().
  _pcp_size: _pcp_size().
  _SortedGatherOp.__init__: _SortedGatherOp#__init__().
---
# Module: [`src/vllm_torchtpu/layers/adapter/fused_moe_ep.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py)

## Classes
### <a id="_SortedGatherOp"></a>`_SortedGatherOp`
- def: [`src/vllm_torchtpu/layers/adapter/fused_moe_ep.py:368`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L368)
- doc: The fused layer as route, a torch all-gather, compute.
- signature: `class _SortedGatherOp:`
- members:
  - <a id="_SortedGatherOp.compute"></a>`compute` — [`L379`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L379)
  - <a id="_SortedGatherOp.group"></a>`group` — [`L380`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L380)
  - <a id="_SortedGatherOp.route"></a>`route` — [`L378`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L378)
- protocol/private: <a id="_SortedGatherOp.__call__"></a>`__call__`[`L382`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L382), <a id="_SortedGatherOp.__init__"></a>`__init__`[`L377`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L377)
- used by: [`_build_split_ops`](fused_moe_ep.md#_build_split_ops)

## Functions
- <a id="_build_op"></a>`_build_op(mesh, topk: int, renormalize: bool, activation: str, mesh_expert_order: tuple[int, ...] | None, sharded_plan: bool, weight_format="fp8", rhs_qb=None, scoring_fn="softmax", has_score_bias=False, routed_scaling_factor=1, has_hash_ids=False, *, token_replica_groups=None, sorted_gather=None)` — [`L168`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L168) — The op for this closure, built once per distinct closure and reused. — documented in [fused-moe-kernels](../../../../../concepts/fused-moe-kernels.md)
- <a id="_build_split_ops"></a>`_build_split_ops(name, call, mesh, input_specs, spec, topk, weight_format, has_score_bias, has_hash_ids, token_replica_groups, sorted_gather)` — [`L391`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L391) — `_SortedGatherOp` for the closure `call` was built for. — documented in [fused-moe-kernels](../../../../../concepts/fused-moe-kernels.md)
- <a id="_build_split_ops._compute_fake"></a>`_compute_fake(x, *_args, **_kwargs)` — [`L541`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L541)
- <a id="_build_op._fake"></a>`_fake(x, *_args, **_kwargs)` — [`L346`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L346)
- <a id="_max_node_tokens"></a>`_max_node_tokens(ep: int, pcp: int = 1)` — [`L1151`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L1151) — The largest node-wide token count a step can carry, or 0 if unknown.
- <a id="_mesh_expert_order"></a>`_mesh_expert_order(ep: int)` — [`L718`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L718) — Which EP rank's expert block belongs at each mesh index, or None.
- <a id="_pcp_size"></a>`_pcp_size(layer)` — [`L1183`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L1183) — Returns the layer's configured prefill-context-parallel width.
- <a id="_build_split_ops._route_fake"></a>`_route_fake(x, w1, *_args, **_kwargs)` — [`L528`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L528)
- <a id="_routing_config"></a>`_routing_config(layer)` — [`L1053`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L1053) — The three routing knobs the op closes over, read off the layer.
- <a id="_simulated_routing_operands"></a>`_simulated_routing_operands(router_logits: torch.Tensor, score_bias: torch.Tensor | None, hash_ids: torch.Tensor | None)` — [`L601`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L601) — The kernel's routing operands, under `uniform_random` routing simulation.
- <a id="_smem_capacity_bytes"></a>`_smem_capacity_bytes()` — [`L1173`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L1173) — This chip's scalar memory, or tpu7x's outside a device process.
- <a id="_squeeze_channel_scale"></a>`_squeeze_channel_scale(scale: torch.Tensor, experts: int, channels: int)` — [`L123`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L123) — Our GMM scales are 4-D ``[E, blocks, 1, N]``; the kernel takes ``[E, N]``.
- <a id="_squeeze_channel_scale_checked"></a>`_squeeze_channel_scale_checked(scale: torch.Tensor)` — [`L742`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L742) — `_squeeze_channel_scale` without the shape arguments, for the hot path.
- <a id="_unsupported_routing_reason"></a>`_unsupported_routing_reason(layer, *, supplies_hash_ids=False)` — [`L1067`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L1067) — Why this layer's ROUTING cannot go through the kernel, or None.
- <a id="_build_op.call"></a>`call(x, w1, w2, w1_scale, w2_scale, gating, rank, **bias_kw)` — [`L222`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L222)
- <a id="_build_split_ops.compute"></a>`compute(x: jax.Array, w1: jax.Array, w2: jax.Array, w1_scale: jax.Array, w2_scale: jax.Array, gating: jax.Array, rank: jax.Array, q_g: jax.Array, router_weights: jax.Array, payload: jax.Array)` — [`L454`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L454)
- <a id="_build_split_ops.compute_extra"></a>`compute_extra(x: jax.Array, w1: jax.Array, w2: jax.Array, w1_scale: jax.Array, w2_scale: jax.Array, gating: jax.Array, rank: jax.Array, extra: jax.Array, q_g: jax.Array, router_weights: jax.Array, payload: jax.Array)` — [`L479`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L479)
- <a id="_build_split_ops.extra_kw"></a>`extra_kw(extra)` — [`L414`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L414)
- <a id="fused_moe_ep"></a>`fused_moe_ep(owner: Any, hidden_states: torch.Tensor, w1: torch.Tensor, w2: torch.Tensor, w1_scale: torch.Tensor, w2_scale: torch.Tensor, router_logits: torch.Tensor, score_bias: torch.Tensor | None = None, hash_ids: torch.Tensor | None = None)` — [`L554`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L554) — Run one MoE layer through the fused EP kernel.
- <a id="fused_moe_ep_supported"></a>`fused_moe_ep_supported(owner: Any)` — [`L144`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L144) — Whether `prebuild_fused_moe_ep` armed the fused path for this layer.
- <a id="fused_moe_ep_unsupported_reason"></a>`fused_moe_ep_unsupported_reason(layer, weights, activation, *, weight_format="fp8", rhs_qb=None, supplies_hash_ids=False)` — [`L985`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L985) — Validate prepared (or meta) weights and routing before installation.
- <a id="hash_topk_ids_operand"></a>`hash_topk_ids_operand(layer, input_ids: torch.Tensor | None)` — [`L694`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L694) — DeepSeek-V4's per-token expert ids, or None for a top-k layer.
- <a id="_build_op.moe"></a>`moe(x: jax.Array, w1: jax.Array, w2: jax.Array, w1_scale: jax.Array, w2_scale: jax.Array, gating: jax.Array, rank: jax.Array)` — [`L253`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L253)
- <a id="_build_op.moe_with_hash_ids"></a>`moe_with_hash_ids(x: jax.Array, w1: jax.Array, w2: jax.Array, w1_scale: jax.Array, w2_scale: jax.Array, gating: jax.Array, rank: jax.Array, hash_ids: jax.Array)` — [`L285`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L285)
- <a id="_build_op.moe_with_score_bias"></a>`moe_with_score_bias(x: jax.Array, w1: jax.Array, w2: jax.Array, w1_scale: jax.Array, w2_scale: jax.Array, gating: jax.Array, rank: jax.Array, score_bias: jax.Array)` — [`L264`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L264)
- <a id="prebuild_fused_moe_ep"></a>`prebuild_fused_moe_ep(layer, topk: int, renormalize: bool, activation: str, *, weight_format="fp8", rhs_qb=None, weights=None, supplies_hash_ids=False)` — [`L759`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L759) — Resolve the mesh and build the fused-EP op for one layer. — documented in [distributed-parallelism-and-meshes](../../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="register_fused_scale_buffers"></a>`register_fused_scale_buffers(layer)` — [`L642`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L642) — Stage the fp4 weight scales as the `[E, K/block, N]` tables the op takes.
- <a id="register_score_bias_buffer"></a>`register_score_bias_buffer(layer)` — [`L672`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L672) — Stage `e_score_correction_bias` as the f32 operand the op takes.
- <a id="_build_split_ops.route"></a>`route(x: jax.Array, w1: jax.Array, w2: jax.Array, w1_scale: jax.Array, w2_scale: jax.Array, gating: jax.Array, rank: jax.Array)` — [`L421`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L421)
- <a id="_build_split_ops.route_extra"></a>`route_extra(x: jax.Array, w1: jax.Array, w2: jax.Array, w1_scale: jax.Array, w2_scale: jax.Array, gating: jax.Array, rank: jax.Array, extra: jax.Array)` — [`L432`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L432)
- <a id="score_bias_operand"></a>`score_bias_operand(layer)` — [`L689`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L689) — The staged bias for this layer, or None. Safe inside a traced forward.

## Module values
- <a id="FUSED_MOE_EP_OP_ATTR"></a>`FUSED_MOE_EP_OP_ATTR` — [`L120`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L120)
- <a id="FUSED_MOE_EP_OP_NAME"></a>`FUSED_MOE_EP_OP_NAME` — [`L88`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L88)
- <a id="FUSED_MOE_EP_SCORE_BIAS_ATTR"></a>`FUSED_MOE_EP_SCORE_BIAS_ATTR` — [`L669`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L669)
- <a id="_OPS._OPS"></a>`_OPS` — [`L108`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L108)
- <a id="_RANK_BUFFER._RANK_BUFFER"></a>`_RANK_BUFFER` — [`L114`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L114)
- <a id="_SMEM_OVERHEAD_BYTES"></a>`_SMEM_OVERHEAD_BYTES` — [`L82`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L82)
- <a id="_TILE_M"></a>`_TILE_M` — [`L77`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L77)
- <a id="logger"></a>`logger` — [`L72`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe_ep.py#L72)

