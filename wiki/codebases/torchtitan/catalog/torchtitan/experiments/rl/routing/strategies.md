---
title: 'Module: torchtitan/experiments/rl/routing/strategies.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/routing/strategies.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.routing.strategies`/
symbols:
  LeastLoadedRoutingStrategy: LeastLoadedRoutingStrategy#
  RoutingStrategy: RoutingStrategy#
  StickySessionRoutingStrategy: StickySessionRoutingStrategy#
  LeastLoadedRoutingStrategy.Config: LeastLoadedRoutingStrategy#Config#
  StickySessionRoutingStrategy.Config: StickySessionRoutingStrategy#Config#
  StickySessionRoutingStrategy.Config.fallback_strategy: StickySessionRoutingStrategy#Config#fallback_strategy.
  StickySessionRoutingStrategy.choose: StickySessionRoutingStrategy#choose().
  RoutingStrategy.choose: RoutingStrategy#choose().
  LeastLoadedRoutingStrategy.choose: LeastLoadedRoutingStrategy#choose().
  RoundRobinRoutingStrategy.Config: RoundRobinRoutingStrategy#Config#
  RoundRobinRoutingStrategy: RoundRobinRoutingStrategy#
  StickySessionRoutingStrategy._sessions: StickySessionRoutingStrategy#_sessions.
  RoundRobinRoutingStrategy.choose: RoundRobinRoutingStrategy#choose().
  StickySessionRoutingStrategy._fallback_strategy: StickySessionRoutingStrategy#_fallback_strategy.
  RoutingStrategy.__init__: RoutingStrategy#__init__().
  StickySessionRoutingStrategy.Config.max_sessions: StickySessionRoutingStrategy#Config#max_sessions.
  StickySessionRoutingStrategy._max_sessions: StickySessionRoutingStrategy#_max_sessions.
  RoundRobinRoutingStrategy.__init__: RoundRobinRoutingStrategy#__init__().
  LeastLoadedRoutingStrategy.__init__: LeastLoadedRoutingStrategy#__init__().
  StickySessionRoutingStrategy.Config.__post_init__: StickySessionRoutingStrategy#Config#__post_init__().
  StickySessionRoutingStrategy.__init__: StickySessionRoutingStrategy#__init__().
  LeastLoadedRoutingStrategy._last_chosen: LeastLoadedRoutingStrategy#_last_chosen.
  RoundRobinRoutingStrategy._counter: RoundRobinRoutingStrategy#_counter.
  LeastLoadedRoutingStrategy._selection_counter: LeastLoadedRoutingStrategy#_selection_counter.
---
# Module: [`torchtitan/experiments/rl/routing/strategies.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py)

## Classes
### <a id="LeastLoadedRoutingStrategy"></a>`LeastLoadedRoutingStrategy`  ·  implements/extends RoutingStrategy
- def: [`torchtitan/experiments/rl/routing/strategies.py:79`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L79)
- doc: Pick the least loaded candidate, breaking ties by least recently chosen.
- signature: `class LeastLoadedRoutingStrategy(RoutingStrategy):`
- members:
  - <a id="LeastLoadedRoutingStrategy.choose"></a>`choose(self, routing_ctx: RoutingContext, candidates: Sequence[RoutingCandidate])` — [`L95`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L95) — Return the least recently chosen of the lowest reserved load candidates.
- protocol/private: <a id="LeastLoadedRoutingStrategy.__init__"></a>`__init__`[`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L86), <a id="LeastLoadedRoutingStrategy._last_chosen"></a>`_last_chosen`[`L93`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L93), <a id="LeastLoadedRoutingStrategy._selection_counter"></a>`_selection_counter`[`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L88)
- uses (calls/refs, reference-scoped): [`RoutingContext`](types.md#RoutingContext), [`RoutingStrategy`](strategies.md#RoutingStrategy), [`Config`](strategies.md#LeastLoadedRoutingStrategy.Config), [`RoutingCandidate`](types.md#RoutingCandidate), [`reserved_load`](types.md#RoutingCandidate.reserved_load)
- used by: [`RoutingStrategy`](strategies.md#RoutingStrategy), [`strategy`](inter_generator_router.md#InterGeneratorRouter.Config.strategy), [`fallback_strategy`](strategies.md#StickySessionRoutingStrategy.Config.fallback_strategy), [`choose`](strategies.md#RoutingStrategy.choose)  (12 test-only)

### <a id="LeastLoadedRoutingStrategy.Config"></a>`LeastLoadedRoutingStrategy.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/routing/strategies.py:83`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L83)
- signature: `class Config(Configurable.Config):`
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Config`](../../../config/configurable.md#Configurable.Config)
- used by: [`strategy`](inter_generator_router.md#InterGeneratorRouter.Config.strategy), [`fallback_strategy`](strategies.md#StickySessionRoutingStrategy.Config.fallback_strategy), [`__init__`](strategies.md#LeastLoadedRoutingStrategy.__init__)  (12 test-only)

### <a id="RoundRobinRoutingStrategy"></a>`RoundRobinRoutingStrategy`  ·  implements/extends RoutingStrategy
- def: [`torchtitan/experiments/rl/routing/strategies.py:57`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L57)
- doc: Cycle over the candidates in order, ignoring load.
- signature: `class RoundRobinRoutingStrategy(RoutingStrategy):`
- members:
  - <a id="RoundRobinRoutingStrategy.choose"></a>`choose(self, routing_ctx: RoutingContext, candidates: Sequence[RoutingCandidate])` — [`L68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L68) — Return the next candidate in round-robin order.
- protocol/private: <a id="RoundRobinRoutingStrategy.__init__"></a>`__init__`[`L64`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L64), <a id="RoundRobinRoutingStrategy._counter"></a>`_counter`[`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L66)
- uses (calls/refs, reference-scoped): [`RoutingContext`](types.md#RoutingContext), [`RoutingStrategy`](strategies.md#RoutingStrategy), [`RoutingCandidate`](types.md#RoutingCandidate), [`Config`](strategies.md#RoundRobinRoutingStrategy.Config)
- used by: [`RoutingStrategy`](strategies.md#RoutingStrategy), [`choose`](strategies.md#RoutingStrategy.choose)  (6 test-only)

### <a id="RoundRobinRoutingStrategy.Config"></a>`RoundRobinRoutingStrategy.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/routing/strategies.py:61`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L61)
- signature: `class Config(Configurable.Config):`
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Config`](../../../config/configurable.md#Configurable.Config)
- used by: [`__init__`](strategies.md#RoundRobinRoutingStrategy.__init__)  (6 test-only)

### <a id="RoutingStrategy"></a>`RoutingStrategy`  ·  implements/extends ABC, Configurable
- def: [`torchtitan/experiments/rl/routing/strategies.py:36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L36)
- doc: Policy object that chooses one candidate for a request.
- signature: `class RoutingStrategy(Configurable, ABC):`
- members:
  - <a id="RoutingStrategy.choose"></a>`choose(self, routing_ctx: RoutingContext, candidates: Sequence[RoutingCandidate])` — [`L49`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L49) — Choose one candidate from the (non-empty) candidates.
- protocol/private: <a id="RoutingStrategy.__init__"></a>`__init__`[`L44`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L44)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Config`](../../../config/configurable.md#Configurable.Config), [`RoutingContext`](types.md#RoutingContext), [`LeastLoadedRoutingStrategy`](strategies.md#LeastLoadedRoutingStrategy), [`StickySessionRoutingStrategy`](strategies.md#StickySessionRoutingStrategy), [`RoutingCandidate`](types.md#RoutingCandidate), [`choose`](strategies.md#StickySessionRoutingStrategy.choose), [`choose`](strategies.md#LeastLoadedRoutingStrategy.choose), [`RoundRobinRoutingStrategy`](strategies.md#RoundRobinRoutingStrategy), [`choose`](strategies.md#RoundRobinRoutingStrategy.choose)
- used by: [`Configurable`](../../../config/configurable.md#Configurable), [`LeastLoadedRoutingStrategy`](strategies.md#LeastLoadedRoutingStrategy), [`strategy`](intra_generator_router.md#IntraGeneratorRouter.Config.strategy), [`StickySessionRoutingStrategy`](strategies.md#StickySessionRoutingStrategy), [`strategy`](inter_generator_router.md#InterGeneratorRouter.Config.strategy), [`fallback_strategy`](strategies.md#StickySessionRoutingStrategy.Config.fallback_strategy), [`RoundRobinRoutingStrategy`](strategies.md#RoundRobinRoutingStrategy)  (1 test-only)

### <a id="StickySessionRoutingStrategy"></a>`StickySessionRoutingStrategy`  ·  implements/extends RoutingStrategy
- def: [`torchtitan/experiments/rl/routing/strategies.py:125`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L125)
- doc: Keep requests from the same session on the same candidate.
- signature: `class StickySessionRoutingStrategy(RoutingStrategy):`
- members:
  - <a id="StickySessionRoutingStrategy.choose"></a>`choose(self, routing_ctx: RoutingContext, candidates: Sequence[RoutingCandidate])` — [`L150`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L150) — Return the session's assigned candidate, or assign a new one.
- protocol/private: <a id="StickySessionRoutingStrategy.__init__"></a>`__init__`[`L145`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L145), <a id="StickySessionRoutingStrategy._fallback_strategy"></a>`_fallback_strategy`[`L147`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L147), <a id="StickySessionRoutingStrategy._max_sessions"></a>`_max_sessions`[`L146`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L146), <a id="StickySessionRoutingStrategy._sessions"></a>`_sessions`[`L148`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L148)
- uses (calls/refs, reference-scoped): [`build`](../../../config/configurable.md#Configurable.Config.build), [`RoutingContext`](types.md#RoutingContext), [`RoutingStrategy`](strategies.md#RoutingStrategy), [`session_id`](types.md#RoutingContext.session_id), [`RoutingCandidate`](types.md#RoutingCandidate), [`Config`](strategies.md#StickySessionRoutingStrategy.Config), [`fallback_strategy`](strategies.md#StickySessionRoutingStrategy.Config.fallback_strategy), [`max_sessions`](strategies.md#StickySessionRoutingStrategy.Config.max_sessions)
- used by: [`RoutingStrategy`](strategies.md#RoutingStrategy), [`strategy`](intra_generator_router.md#IntraGeneratorRouter.Config.strategy), [`choose`](strategies.md#RoutingStrategy.choose)  (11 test-only)

### <a id="StickySessionRoutingStrategy.Config"></a>`StickySessionRoutingStrategy.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/routing/strategies.py:129`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L129)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="StickySessionRoutingStrategy.Config.fallback_strategy"></a>`fallback_strategy` — [`L134`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L134) — ---
  - <a id="StickySessionRoutingStrategy.Config.max_sessions"></a>`max_sessions` — [`L130`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L130) — ---
- protocol/private: <a id="StickySessionRoutingStrategy.Config.__post_init__"></a>`__post_init__`[`L139`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/strategies.py#L139)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Config`](../../../config/configurable.md#Configurable.Config), [`LeastLoadedRoutingStrategy`](strategies.md#LeastLoadedRoutingStrategy), [`RoutingStrategy`](strategies.md#RoutingStrategy), [`Config`](strategies.md#LeastLoadedRoutingStrategy.Config)
- used by: [`strategy`](intra_generator_router.md#IntraGeneratorRouter.Config.strategy), [`_fallback_strategy`](strategies.md#StickySessionRoutingStrategy._fallback_strategy), [`_max_sessions`](strategies.md#StickySessionRoutingStrategy._max_sessions), [`__init__`](strategies.md#StickySessionRoutingStrategy.__init__)  (11 test-only)

