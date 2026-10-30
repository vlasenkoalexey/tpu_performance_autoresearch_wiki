---
title: 'Module: torchtitan/experiments/rl/routing/intra_generator_router.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/routing/intra_generator_router.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.routing.intra_generator_router`/
symbols:
  IntraGeneratorRouter: IntraGeneratorRouter#
  IntraGeneratorRouter.Config.strategy: IntraGeneratorRouter#Config#strategy.
  IntraGeneratorRouter.Config: IntraGeneratorRouter#Config#
  IntraGeneratorRouter.reserve: IntraGeneratorRouter#reserve().
  IntraGeneratorRouter._handles: IntraGeneratorRouter#_handles.
  IntraGeneratorRouter.release: IntraGeneratorRouter#release().
  _DPRankHandle.reserved_load: _DPRankHandle#reserved_load.
  IntraGeneratorRouter._reservations: IntraGeneratorRouter#_reservations.
  IntraGeneratorRouter._strategy: IntraGeneratorRouter#_strategy.
  _DPRankHandle: _DPRankHandle#
  IntraGeneratorRouter.__init__: IntraGeneratorRouter#__init__().
  _DPRankHandle.dp_rank: _DPRankHandle#dp_rank.
---
# Module: [`torchtitan/experiments/rl/routing/intra_generator_router.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/intra_generator_router.py)

## Classes
### <a id="IntraGeneratorRouter"></a>`IntraGeneratorRouter`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/routing/intra_generator_router.py:32`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/intra_generator_router.py#L32)
- doc: Router that partitions requests across the DP ranks within one generator.
- signature: `class IntraGeneratorRouter(Configurable):`
- members:
  - <a id="IntraGeneratorRouter.release"></a>`release(self, request_id: str)` — [`L85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/intra_generator_router.py#L85) — Free the load unit ``reserve`` placed for ``request_id``.
  - <a id="IntraGeneratorRouter.reserve"></a>`reserve(self, request_id: str, *, routing_session_id: str | None)` — [`L68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/intra_generator_router.py#L68) — Pick a DP rank for one request and reserve one load unit on it.
- protocol/private: <a id="IntraGeneratorRouter.__init__"></a>`__init__`[`L59`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/intra_generator_router.py#L59), <a id="IntraGeneratorRouter._handles"></a>`_handles`[`L63`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/intra_generator_router.py#L63), <a id="IntraGeneratorRouter._reservations"></a>`_reservations`[`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/intra_generator_router.py#L66), <a id="IntraGeneratorRouter._strategy"></a>`_strategy`[`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/intra_generator_router.py#L62)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`build`](../../../config/configurable.md#Configurable.Config.build), [`RoutingContext`](types.md#RoutingContext), [`session_id`](types.md#RoutingContext.session_id), [`strategy`](intra_generator_router.md#IntraGeneratorRouter.Config.strategy), [`Config`](intra_generator_router.md#IntraGeneratorRouter.Config), [`reserved_load`](intra_generator_router.md#_DPRankHandle.reserved_load), [`_DPRankHandle`](intra_generator_router.md#_DPRankHandle), [`dp_rank`](intra_generator_router.md#_DPRankHandle.dp_rank)
- used by: [`Configurable`](../../../config/configurable.md#Configurable), [`_rank0_resolve_futures`](../actors/generator.md#RequestDispatcher._rank0_resolve_futures), [`_rank0_dp_router`](../actors/generator.md#RequestDispatcher._rank0_dp_router), [`rank0_route`](../actors/generator.md#RequestDispatcher.rank0_route), [`intra_generator_router`](../actors/generator.md#VLLMGenerator.Config.intra_generator_router), [`__init__`](../actors/generator.md#RequestDispatcher.__init__)  (14 test-only)

### <a id="IntraGeneratorRouter.Config"></a>`IntraGeneratorRouter.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/routing/intra_generator_router.py:50`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/intra_generator_router.py#L50)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="IntraGeneratorRouter.Config.strategy"></a>`strategy` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/intra_generator_router.py#L51) — ---
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Config`](../../../config/configurable.md#Configurable.Config), [`RoutingStrategy`](strategies.md#RoutingStrategy), [`StickySessionRoutingStrategy`](strategies.md#StickySessionRoutingStrategy), [`Config`](strategies.md#StickySessionRoutingStrategy.Config)
- used by: [`_strategy`](intra_generator_router.md#IntraGeneratorRouter._strategy), [`intra_generator_router`](../actors/generator.md#VLLMGenerator.Config.intra_generator_router), [`__init__`](../actors/generator.md#RequestDispatcher.__init__), [`__init__`](intra_generator_router.md#IntraGeneratorRouter.__init__)  (10 test-only)

### <a id="_DPRankHandle"></a>`_DPRankHandle`  ·  implements/extends RoutingCandidate
- def: [`torchtitan/experiments/rl/routing/intra_generator_router.py:22`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/intra_generator_router.py#L22)
- doc: One data-parallel rank as a routing candidate (satisfies `RoutingCandidate`).
- signature: `class _DPRankHandle(RoutingCandidate):`
- members:
  - <a id="_DPRankHandle.dp_rank"></a>`dp_rank` — [`L25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/intra_generator_router.py#L25) — ---
  - <a id="_DPRankHandle.reserved_load"></a>`reserved_load` — [`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/intra_generator_router.py#L28) — ---
- uses (calls/refs, reference-scoped): [`RoutingCandidate`](types.md#RoutingCandidate)
- used by: [`RoutingCandidate`](types.md#RoutingCandidate), [`_handles`](intra_generator_router.md#IntraGeneratorRouter._handles), [`release`](intra_generator_router.md#IntraGeneratorRouter.release)  (3 test-only)

