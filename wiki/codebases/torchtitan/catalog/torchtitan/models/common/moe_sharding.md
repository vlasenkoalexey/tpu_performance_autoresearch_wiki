---
title: 'Module: torchtitan/models/common/moe_sharding.py'
type: catalog
provenance: extracted
module: torchtitan/models/common/moe_sharding.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.common.moe_sharding`/
symbols:
  _routed_experts_sharding_configs: _routed_experts_sharding_configs().
  _moe_sharding_config: _moe_sharding_config().
  set_moe_sharding_config: set_moe_sharding_config().
  _router_sharding_config: _router_sharding_config().
  _shared_expert_colwise_config: _shared_expert_colwise_config().
  _shared_expert_rowwise_config: _shared_expert_rowwise_config().
  _shared_experts_sharding_configs: _shared_experts_sharding_configs().
  _tokens_per_expert_placement: _tokens_per_expert_placement().
  expert_param_placement_sparse: expert_param_placement_sparse().
  expert_param_placement_dense: expert_param_placement_dense().
  DP: DP.
  CP: CP.
  TP: TP.
  DP_REPLICATE: DP_REPLICATE.
  EP: EP.
  EFSDP: EFSDP.
---
# Module: [`torchtitan/models/common/moe_sharding.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe_sharding.py)

## Functions
- <a id="_moe_sharding_config"></a>`_moe_sharding_config(*, enable_ep: bool, enable_sp: bool)` — [`L273`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe_sharding.py#L273) — ``ShardingConfig`` at the MoE boundary.
- <a id="_routed_experts_sharding_configs"></a>`_routed_experts_sharding_configs(*, enable_ep: bool, enable_sp: bool, expert_param_layout: dict[str, spmd.PerMeshAxisSpmdType])` — [`L200`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe_sharding.py#L200) — Configs for RoutedExperts local_map and inner expert weight state.
- <a id="_router_sharding_config"></a>`_router_sharding_config(*, enable_ep: bool, enable_sp: bool)` — [`L88`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe_sharding.py#L88) — Router gate: Replicate weights, output stays DTensor.
- <a id="_shared_expert_colwise_config"></a>`_shared_expert_colwise_config()` — [`L126`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe_sharding.py#L126) — Colwise shared-expert FFN (w1/w3).
- <a id="_shared_expert_rowwise_config"></a>`_shared_expert_rowwise_config(*, output_layout: SpmdType)` — [`L144`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe_sharding.py#L144) — Rowwise shared-expert FFN (w2).
- <a id="_shared_experts_sharding_configs"></a>`_shared_experts_sharding_configs(*, enable_ep: bool, enable_sp: bool)` — [`L166`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe_sharding.py#L166) — Configs for shared FeedForward parent and w1/w2/w3 linears.
- <a id="_tokens_per_expert_placement"></a>`_tokens_per_expert_placement(*, enable_ep: bool)` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe_sharding.py#L70) — Placement for the ``tokens_per_expert_E`` buffer.
- <a id="expert_param_placement_dense"></a>`expert_param_placement_dense(*, tp_placement: spmd.PerMeshAxisSpmdType)` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe_sharding.py#L51) — Dense-family placement for routed-expert weights (EP disabled, TP > 1).
- <a id="expert_param_placement_sparse"></a>`expert_param_placement_sparse()` — [`L30`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe_sharding.py#L30) — Sparse-family placement for routed-expert weights (EP enabled).
- <a id="set_moe_sharding_config"></a>`set_moe_sharding_config(moe_cfg, *, enable_ep: bool, enable_sp: bool, expert_param_layout: dict[str, spmd.PerMeshAxisSpmdType])` — [`L305`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe_sharding.py#L305) — Populate ``sharding_config`` on every MoE submodule.

## Module values
- <a id="CP"></a>`CP` — [`L24`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe_sharding.py#L24)
- <a id="DP"></a>`DP` — [`L22`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe_sharding.py#L22)
- <a id="DP_REPLICATE"></a>`DP_REPLICATE` — [`L23`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe_sharding.py#L23)
- <a id="EFSDP"></a>`EFSDP` — [`L27`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe_sharding.py#L27)
- <a id="EP"></a>`EP` — [`L26`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe_sharding.py#L26)
- <a id="TP"></a>`TP` — [`L25`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/moe_sharding.py#L25)

