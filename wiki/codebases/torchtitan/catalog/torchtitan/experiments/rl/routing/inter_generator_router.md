---
title: 'Module: torchtitan/experiments/rl/routing/inter_generator_router.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/routing/inter_generator_router.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.routing.inter_generator_router`/
symbols:
  InterGeneratorRouter._route: InterGeneratorRouter#_route().
  InterGeneratorRouter._generators: InterGeneratorRouter#_generators.
  InterGeneratorRouter._pull_one: InterGeneratorRouter#_pull_one().
  InterGeneratorRouter: InterGeneratorRouter#
  _GeneratorState: _GeneratorState#
  InterGeneratorRouter._set_state: InterGeneratorRouter#_set_state().
  InterGeneratorRouter.Config.strategy: InterGeneratorRouter#Config#strategy.
  InterGeneratorRouter._candidates: InterGeneratorRouter#_candidates().
  InterGeneratorRouter.Config: InterGeneratorRouter#Config#
  _GeneratorHandle.state: _GeneratorHandle#state.
  InterGeneratorRouter._pull_model_state_dict: InterGeneratorRouter#_pull_model_state_dict().
  InterGeneratorRouter.generate: InterGeneratorRouter#generate().
  _GeneratorState.SERVING: _GeneratorState#SERVING.
  _GeneratorHandle: _GeneratorHandle#
  InterGeneratorRouter._reserve: InterGeneratorRouter#_reserve().
  InterGeneratorRouter._release: InterGeneratorRouter#_release().
  _GeneratorHandle.reserved_load: _GeneratorHandle#reserved_load.
  InterGeneratorRouter._fanout: InterGeneratorRouter#_fanout().
  _GeneratorState.SYNCING: _GeneratorState#SYNCING.
  InterGeneratorRouter._refresh_serving_status: InterGeneratorRouter#_refresh_serving_status().
  _GeneratorHandle.idle: _GeneratorHandle#idle.
  InterGeneratorRouter._strategy: InterGeneratorRouter#_strategy.
  InterGeneratorRouter.sync_log_step: InterGeneratorRouter#sync_log_step().
  InterGeneratorRouter._serving: InterGeneratorRouter#_serving.
  InterGeneratorRouter.pull_model_state_dict: InterGeneratorRouter#pull_model_state_dict().
  InterGeneratorRouter.close_generators: InterGeneratorRouter#close_generators().
  _GeneratorHandle.rank0_actor: _GeneratorHandle#rank0_actor.
  InterGeneratorRouter.Config.hot_swap: InterGeneratorRouter#Config#hot_swap.
  InterGeneratorRouter.__init__: InterGeneratorRouter#__init__().
  InterGeneratorRouter.start_engine_loop: InterGeneratorRouter#start_engine_loop().
  _GeneratorHandle.actor: _GeneratorHandle#actor.
  InterGeneratorRouter._config: InterGeneratorRouter#_config.
---
# Module: [`torchtitan/experiments/rl/routing/inter_generator_router.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py)

## Classes
### <a id="InterGeneratorRouter"></a>`InterGeneratorRouter`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/routing/inter_generator_router.py:58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L58)
- doc: Routes generation calls across generator meshes and pulls model's state dict.
- signature: `class InterGeneratorRouter(Actor, Configurable):`
- members:
  - <a id="InterGeneratorRouter._candidates"></a>`_candidates(self)` — [`L133`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L133) — Return generator handles that are currently routable.
  - <a id="InterGeneratorRouter._fanout"></a>`_fanout(self, method: str, *args, return_exceptions: bool = False, **kwargs)` — [`L191`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L191) — Call ``method`` on every generator concurrently and gather results.
  - <a id="InterGeneratorRouter._pull_model_state_dict"></a>`_pull_model_state_dict(self, *, policy_version: int)` — [`L218`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L218) — Pull the given policy version's state dict into every generator.
  - <a id="InterGeneratorRouter._refresh_serving_status"></a>`_refresh_serving_status(self)` — [`L138`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L138) — Update whether any generator can serve; only changes while draining (i.e. hot-swap is off).
  - <a id="InterGeneratorRouter._release"></a>`_release(self, h: _GeneratorHandle, cost: int)` — [`L161`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L161) — Release estimated generation work after a routed call finishes.
  - <a id="InterGeneratorRouter._reserve"></a>`_reserve(self, h: _GeneratorHandle, cost: int)` — [`L152`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L152) — Reserve estimated generation work on a handle before dispatch.
  - <a id="InterGeneratorRouter._route"></a>`_route(self, method: str, *args, routing_ctx: RoutingContext, **kwargs)` — [`L171`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L171) — Dispatch one call to a strategy-chosen serving generator's rank 0;
  - <a id="InterGeneratorRouter._set_state"></a>`_set_state(self, h: _GeneratorHandle, state: _GeneratorState)` — [`L146`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L146) — Move a generator between serving and syncing states.
  - <a id="InterGeneratorRouter.close_generators"></a>`close_generators(self)` — [`L296`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L296) — Close every generator, returning each one's result or exception.
  - <a id="InterGeneratorRouter.generate"></a>`generate(self, prompt_token_ids: list[int], *, request_id: str, routing_session_id: str | None, sampling_config: Any | None, metrics_prefix: str)` — [`L251`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L251) — Route one generation call to a generator and return its completion.
  - <a id="InterGeneratorRouter.pull_model_state_dict"></a>`pull_model_state_dict(self, policy_version: int)` — [`L289`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L289) — Pull the given policy version's state dict into every generator.
  - <a id="InterGeneratorRouter.start_engine_loop"></a>`start_engine_loop(self)` — [`L278`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L278) — Start the engine loop on every rank of every generator.
  - <a id="InterGeneratorRouter.sync_log_step"></a>`sync_log_step(self, step: int)` — [`L283`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L283) — Set the step counter in this process and in every generator rank.
- protocol/private: <a id="InterGeneratorRouter.__init__"></a>`__init__`[`L105`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L105), <a id="InterGeneratorRouter._config"></a>`_config`[`L116`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L116), <a id="InterGeneratorRouter._generators"></a>`_generators`[`L117`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L117), <a id="InterGeneratorRouter._pull_one"></a>`_pull_one`[`L225`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L225), <a id="InterGeneratorRouter._serving"></a>`_serving`[`L130`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L130), <a id="InterGeneratorRouter._strategy"></a>`_strategy`[`L129`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L129)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`build`](../../../config/configurable.md#Configurable.Config.build), [`log_trace_span`](../../../observability/structured_logger/structured_logging.md#log_trace_span), [`RoutingContext`](types.md#RoutingContext), [`session_id`](types.md#RoutingContext.session_id), [`set_step`](../../../observability/structured_logger/step_state.md#set_step), [`_GeneratorState`](inter_generator_router.md#_GeneratorState), [`strategy`](inter_generator_router.md#InterGeneratorRouter.Config.strategy), [`Config`](inter_generator_router.md#InterGeneratorRouter.Config), [`state`](inter_generator_router.md#_GeneratorHandle.state), [`SERVING`](inter_generator_router.md#_GeneratorState.SERVING), [`_GeneratorHandle`](inter_generator_router.md#_GeneratorHandle), [`estimated_cost`](types.md#RoutingContext.estimated_cost), [`reserved_load`](inter_generator_router.md#_GeneratorHandle.reserved_load), [`SYNCING`](inter_generator_router.md#_GeneratorState.SYNCING), [`idle`](inter_generator_router.md#_GeneratorHandle.idle), [`hot_swap`](inter_generator_router.md#InterGeneratorRouter.Config.hot_swap), [`rank0_actor`](inter_generator_router.md#_GeneratorHandle.rank0_actor), [`actor`](inter_generator_router.md#_GeneratorHandle.actor)
- used by: [`Configurable`](../../../config/configurable.md#Configurable), [`_trainer_loop`](../controller.md#Controller._trainer_loop), [`trainer_dp_degree`](../controller.md#Controller.trainer_dp_degree), [`close`](../controller.md#Controller.close), [`_generator_pull_and_release_buffer_slots`](../components/weight_sync.md#WeightSyncManager._generator_pull_and_release_buffer_slots), [`generator_router`](../controller.md#Controller.generator_router), [`generator_router`](../controller.md#Controller.Config.generator_router), [`generate`](../controller.md#Controller.generate), [`__init__`](../components/weight_sync.md#WeightSyncManager.__init__)  (22 test-only)

### <a id="InterGeneratorRouter.Config"></a>`InterGeneratorRouter.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/routing/inter_generator_router.py:87`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L87)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="InterGeneratorRouter.Config.hot_swap"></a>`hot_swap` — [`L95`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L95) — ---
  - <a id="InterGeneratorRouter.Config.strategy"></a>`strategy` — [`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L88) — ---
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Config`](../../../config/configurable.md#Configurable.Config), [`LeastLoadedRoutingStrategy`](strategies.md#LeastLoadedRoutingStrategy), [`RoutingStrategy`](strategies.md#RoutingStrategy), [`Config`](strategies.md#LeastLoadedRoutingStrategy.Config)
- used by: [`__post_init__`](../controller.md#Controller.Config.__post_init__), [`_pull_one`](inter_generator_router.md#InterGeneratorRouter._pull_one), [`generator_router`](../controller.md#Controller.Config.generator_router), [`_strategy`](inter_generator_router.md#InterGeneratorRouter._strategy), [`__init__`](inter_generator_router.md#InterGeneratorRouter.__init__)  (6 test-only)

### <a id="_GeneratorHandle"></a>`_GeneratorHandle`  ·  implements/extends RoutingCandidate
- def: [`torchtitan/experiments/rl/routing/inter_generator_router.py:37`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L37)
- doc: Router-side metadata for one generator mesh.
- signature: `class _GeneratorHandle(RoutingCandidate):`
- members:
  - <a id="_GeneratorHandle.actor"></a>`actor` — [`L40`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L40) — ---
  - <a id="_GeneratorHandle.idle"></a>`idle` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L54) — ---
  - <a id="_GeneratorHandle.rank0_actor"></a>`rank0_actor` — [`L44`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L44) — ---
  - <a id="_GeneratorHandle.reserved_load"></a>`reserved_load` — [`L48`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L48) — ---
  - <a id="_GeneratorHandle.state"></a>`state` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L51) — ---
- uses (calls/refs, reference-scoped): [`RoutingCandidate`](types.md#RoutingCandidate), [`_GeneratorState`](inter_generator_router.md#_GeneratorState), [`SERVING`](inter_generator_router.md#_GeneratorState.SERVING)
- used by: [`_generators`](inter_generator_router.md#InterGeneratorRouter._generators), [`_pull_one`](inter_generator_router.md#InterGeneratorRouter._pull_one), [`RoutingCandidate`](types.md#RoutingCandidate), [`_set_state`](inter_generator_router.md#InterGeneratorRouter._set_state), [`_candidates`](inter_generator_router.md#InterGeneratorRouter._candidates), [`_release`](inter_generator_router.md#InterGeneratorRouter._release), [`_reserve`](inter_generator_router.md#InterGeneratorRouter._reserve), [`_fanout`](inter_generator_router.md#InterGeneratorRouter._fanout)  (6 test-only)

### <a id="_GeneratorState"></a>`_GeneratorState`  ·  implements/extends Enum
- def: [`torchtitan/experiments/rl/routing/inter_generator_router.py:29`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L29)
- doc: Lifecycle state controlling routability; `SYNCING` is only entered when draining (i.e. hot-swap is off).
- signature: `class _GeneratorState(Enum):`
- members:
  - <a id="_GeneratorState.SERVING"></a>`SERVING` — [`L32`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L32)
  - <a id="_GeneratorState.SYNCING"></a>`SYNCING` — [`L33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/routing/inter_generator_router.py#L33)
- used by: [`_pull_one`](inter_generator_router.md#InterGeneratorRouter._pull_one), [`_set_state`](inter_generator_router.md#InterGeneratorRouter._set_state), [`_candidates`](inter_generator_router.md#InterGeneratorRouter._candidates), [`state`](inter_generator_router.md#_GeneratorHandle.state)  (7 test-only)

