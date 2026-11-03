---
title: 'Module: src/vllm_torchtpu/layers/adapter/moe_routing.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/moe_routing.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.moe_routing`/
symbols:
  _available: _available.
  route: route().
  select_experts: select_experts().
  is_uniform_random_simulation: is_uniform_random_simulation().
  maybe_simulate_routing: maybe_simulate_routing().
  register_experts_start_buffer: register_experts_start_buffer().
  _strategy_name: _strategy_name.
  _topk: _topk().
  _SIMULATION_STRATEGY: _SIMULATION_STRATEGY.
  validate_linear_ep_placement: validate_linear_ep_placement().
  _ROUTER_TOPK: _ROUTER_TOPK.
  logger: logger.
  _uniform_random_routing: _uniform_random_routing().
  _apply_scoring_fn: _apply_scoring_fn().
  get_experts_start: get_experts_start().
  uniform_random_logits: uniform_random_logits().
  _UNIFORM_RANDOM: _UNIFORM_RANDOM.
  _hash_moe_select: _hash_moe_select().
---
# Module: [`src/vllm_torchtpu/layers/adapter/moe_routing.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py)

## Functions
- <a id="_apply_scoring_fn"></a>`_apply_scoring_fn(scoring_fn: str, router_logits: torch.Tensor)` — [`L189`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L189)
- <a id="_hash_moe_select"></a>`_hash_moe_select(scores: torch.Tensor, hash_indices_table: torch.Tensor, input_ids: torch.Tensor, renormalize: bool, routed_scaling_factor: float)` — [`L204`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L204) — Static token-id based MoE routing for DeepSeek-V4.
- <a id="_topk"></a>`_topk(scores: torch.Tensor, k: int)` — [`L30`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L30) — Top-k over the expert axis, by the configured implementation.
- <a id="_uniform_random_routing"></a>`_uniform_random_routing(hidden_states: torch.Tensor, router_logits: torch.Tensor, topk: int)` — [`L91`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L91) — Uniform-random expert selection that stays anchored to the real input.
- <a id="get_experts_start"></a>`get_experts_start(layer)` — [`L326`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L326) — Return the first global expert id owned by this shard, or None for non-EP.
- <a id="is_uniform_random_simulation"></a>`is_uniform_random_simulation()` — [`L73`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L73) — Whether ``VLLM_MOE_ROUTING_SIMULATION_STRATEGY`` is ``uniform_random``.
- <a id="maybe_simulate_routing"></a>`maybe_simulate_routing(hidden_states: torch.Tensor, router_logits: torch.Tensor, topk: int)` — [`L120`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L120) — Optionally replace routing with a simulated strategy, for profiling.
- <a id="register_experts_start_buffer"></a>`register_experts_start_buffer(layer, *, device: torch.device)` — [`L342`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L342) — Register ``layer._experts_start`` as a persistent 0-d int32 buffer
- <a id="route"></a>`route(layer, hidden_states: torch.Tensor, router_logits: torch.Tensor, input_ids: torch.Tensor | None = None)` — [`L150`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L150) — Quantization-independent routing entry point for the TPU MoE methods. — documented in [kimi-k3-model](../../../../../concepts/kimi-k3-model.md)
- <a id="select_experts"></a>`select_experts(hidden_states: torch.Tensor, router_logits: torch.Tensor, *, topk: int, renormalize: bool, scoring_fn: str, layer=None, input_ids: torch.Tensor | None = None)` — [`L232`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L232) — Compute local routed expert IDs and weights for non-EP execution.
- <a id="uniform_random_logits"></a>`uniform_random_logits(router_logits: torch.Tensor)` — [`L78`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L78) — f32 uniform noise in ``[m, m + 1)``, ``m`` the mean of ``router_logits``.
- <a id="validate_linear_ep_placement"></a>`validate_linear_ep_placement(layer)` — [`L370`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L370) — Validate that this layer uses linear EP placement.

## Module values
- <a id="_ROUTER_TOPK"></a>`_ROUTER_TOPK` — [`L27`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L27)
- <a id="_SIMULATION_STRATEGY"></a>`_SIMULATION_STRATEGY` — [`L51`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L51) — documented in [adaptive-fused-moe-kernel](../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="_UNIFORM_RANDOM"></a>`_UNIFORM_RANDOM` — [`L49`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L49)
- <a id="_available"></a>`_available` — [`L58`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L58)
- <a id="_strategy_name"></a>`_strategy_name` — [`L52`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L52)
- <a id="logger"></a>`logger` — [`L23`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/moe_routing.py#L23)

