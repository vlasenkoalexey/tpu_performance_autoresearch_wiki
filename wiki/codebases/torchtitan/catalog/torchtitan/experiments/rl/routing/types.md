---
title: 'Module: torchtitan/experiments/rl/routing/types.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/routing/types.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.routing.types`/
symbols:
  RoutingContext: RoutingContext#
  RoutingContext.session_id: RoutingContext#session_id.
  RoutingCandidate: RoutingCandidate#
  RoutingContext.estimated_cost: RoutingContext#estimated_cost.
  RoutingCandidate.reserved_load: RoutingCandidate#reserved_load().
---
# Module: [`torchtitan/experiments/rl/routing/types.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/types.py)

## Classes
### <a id="RoutingCandidate"></a>`RoutingCandidate`  ·  implements/extends ABC
- def: [`torchtitan/experiments/rl/routing/types.py:24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/types.py#L24)
- doc: A routable target.
- signature: `class RoutingCandidate(ABC):`
- members:
  - <a id="RoutingCandidate.reserved_load"></a>`reserved_load(self)` — [`L29`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/types.py#L29) — Caller-defined reserved load on this target.
- uses (calls/refs, reference-scoped): [`_GeneratorHandle`](inter_generator_router.md#_GeneratorHandle), [`_DPRankHandle`](intra_generator_router.md#_DPRankHandle)
- used by: [`choose`](strategies.md#StickySessionRoutingStrategy.choose), [`choose`](strategies.md#LeastLoadedRoutingStrategy.choose), [`choose`](strategies.md#RoutingStrategy.choose), [`_GeneratorHandle`](inter_generator_router.md#_GeneratorHandle), [`_sessions`](strategies.md#StickySessionRoutingStrategy._sessions), [`choose`](strategies.md#RoundRobinRoutingStrategy.choose), [`_DPRankHandle`](intra_generator_router.md#_DPRankHandle)

### <a id="RoutingContext"></a>`RoutingContext`
- def: [`torchtitan/experiments/rl/routing/types.py:34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/types.py#L34)
- doc: Routing metadata for one generation request.
- signature: `class RoutingContext:`
- members:
  - <a id="RoutingContext.estimated_cost"></a>`estimated_cost` — [`L37`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/types.py#L37) — ---
  - <a id="RoutingContext.session_id"></a>`session_id` — [`L40`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/types.py#L40) — ---
- used by: [`_route`](inter_generator_router.md#InterGeneratorRouter._route), [`choose`](strategies.md#StickySessionRoutingStrategy.choose), [`reserve`](intra_generator_router.md#IntraGeneratorRouter.reserve), [`choose`](strategies.md#LeastLoadedRoutingStrategy.choose), [`choose`](strategies.md#RoutingStrategy.choose), [`generate`](inter_generator_router.md#InterGeneratorRouter.generate), [`choose`](strategies.md#RoundRobinRoutingStrategy.choose)  (16 test-only)

