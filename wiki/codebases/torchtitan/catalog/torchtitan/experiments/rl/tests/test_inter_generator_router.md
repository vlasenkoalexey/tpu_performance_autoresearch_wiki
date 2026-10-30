---
title: 'Module: torchtitan/experiments/rl/tests/test_inter_generator_router.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/tests/test_inter_generator_router.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.tests.test_inter_generator_router`/
symbols:
  test_drain_excludes_syncing_generator_from_routes._run: test_drain_excludes_syncing_generator_from_routes()._run().
  test_drain_pulls_idle_generators_while_busy_generator_drains._run: test_drain_pulls_idle_generators_while_busy_generator_drains()._run().
  test_hot_swap_keeps_generators_serving_during_pull._run: test_hot_swap_keeps_generators_serving_during_pull()._run().
  _router: _router().
  test_round_robin_skips_syncing_generators._run: test_round_robin_skips_syncing_generators()._run().
  test_sticky_session_reuses_generator_for_same_session._run: test_sticky_session_reuses_generator_for_same_session()._run().
  test_sticky_session_assigns_new_generator_when_sticky_target_is_syncing._run: test_sticky_session_assigns_new_generator_when_sticky_target_is_syncing()._run().
  _Actor: _Actor#
  test_least_loaded_routes_to_lowest_reserved_load._run: test_least_loaded_routes_to_lowest_reserved_load()._run().
  test_sticky_session_respects_max_sessions._run: test_sticky_session_respects_max_sessions()._run().
  test_route_releases_reserved_load_on_failure._run: test_route_releases_reserved_load_on_failure()._run().
  test_sticky_session_can_use_round_robin_for_new_sessions._run: test_sticky_session_can_use_round_robin_for_new_sessions()._run().
  test_single_generator_blocks_routes_while_draining._run: test_single_generator_blocks_routes_while_draining()._run().
  test_sticky_session_without_session_id_uses_fallback_without_affinity._run: test_sticky_session_without_session_id_uses_fallback_without_affinity()._run().
  test_drain_restores_serving_on_pull_failure._run: test_drain_restores_serving_on_pull_failure()._run().
  test_least_loaded_tie_break_spreads_over_a_changing_candidate_set._run: test_least_loaded_tie_break_spreads_over_a_changing_candidate_set()._run().
  _Actor.generate: _Actor#generate.
  test_round_robin_cycles_through_generators._run: test_round_robin_cycles_through_generators()._run().
  test_sticky_session_spreads_new_sessions_started_on_idle_generators._run: test_sticky_session_spreads_new_sessions_started_on_idle_generators()._run().
  _Actor.pull_model_state_dict: _Actor#pull_model_state_dict.
  _Endpoint.release: _Endpoint#release.
  test_pull_model_state_dict_pulls_every_generator._run: test_pull_model_state_dict_pulls_every_generator()._run().
  _Endpoint.call_one: _Endpoint#call_one().
  _Endpoint.calls: _Endpoint#calls.
  _Endpoint.started: _Endpoint#started.
  test_sticky_session_rejects_non_positive_max_sessions: test_sticky_session_rejects_non_positive_max_sessions().
  test_least_loaded_routes_to_lowest_reserved_load: test_least_loaded_routes_to_lowest_reserved_load().
  test_route_releases_reserved_load_on_failure: test_route_releases_reserved_load_on_failure().
  test_least_loaded_tie_break_spreads_over_a_changing_candidate_set: test_least_loaded_tie_break_spreads_over_a_changing_candidate_set().
  test_round_robin_cycles_through_generators: test_round_robin_cycles_through_generators().
  test_round_robin_skips_syncing_generators: test_round_robin_skips_syncing_generators().
  test_sticky_session_reuses_generator_for_same_session: test_sticky_session_reuses_generator_for_same_session().
  test_sticky_session_spreads_new_sessions_started_on_idle_generators: test_sticky_session_spreads_new_sessions_started_on_idle_generators().
  test_sticky_session_assigns_new_generator_when_sticky_target_is_syncing: test_sticky_session_assigns_new_generator_when_sticky_target_is_syncing().
  test_sticky_session_can_use_round_robin_for_new_sessions: test_sticky_session_can_use_round_robin_for_new_sessions().
  test_sticky_session_without_session_id_uses_fallback_without_affinity: test_sticky_session_without_session_id_uses_fallback_without_affinity().
  test_sticky_session_respects_max_sessions: test_sticky_session_respects_max_sessions().
  test_drain_excludes_syncing_generator_from_routes: test_drain_excludes_syncing_generator_from_routes().
  test_drain_pulls_idle_generators_while_busy_generator_drains: test_drain_pulls_idle_generators_while_busy_generator_drains().
  test_hot_swap_keeps_generators_serving_during_pull: test_hot_swap_keeps_generators_serving_during_pull().
  test_single_generator_blocks_routes_while_draining: test_single_generator_blocks_routes_while_draining().
  test_drain_restores_serving_on_pull_failure: test_drain_restores_serving_on_pull_failure().
  test_pull_model_state_dict_pulls_every_generator: test_pull_model_state_dict_pulls_every_generator().
  _Endpoint: _Endpoint#
  _Endpoint.raises: _Endpoint#raises.
  _Endpoint.value: _Endpoint#value.
  _Endpoint.__init__: _Endpoint#__init__().
  _Actor.__init__: _Actor#__init__().
  _Actor.flatten: _Actor#flatten().
  _Actor.slice: _Actor#slice().
  _Actor.__len__: _Actor#__len__().
---
# Module: [`torchtitan/experiments/rl/tests/test_inter_generator_router.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py)

> **Collapsed catalog** (51 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="_Actor"></a>`_Actor` — [`L42`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L42)
- <a id="_Actor.__init__"></a>`_Actor.__init__` — [`L45`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L45)
- <a id="_Actor.__len__"></a>`_Actor.__len__` — [`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L62)
- <a id="_Actor.flatten"></a>`_Actor.flatten` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L56)
- <a id="_Actor.generate"></a>`_Actor.generate` — [`L53`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L53)
- <a id="_Actor.pull_model_state_dict"></a>`_Actor.pull_model_state_dict` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L54)
- <a id="_Actor.slice"></a>`_Actor.slice` — [`L59`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L59)
- <a id="_Endpoint"></a>`_Endpoint` — [`L23`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L23)
- <a id="_Endpoint.__init__"></a>`_Endpoint.__init__` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L24)
- <a id="_Endpoint.call_one"></a>`_Endpoint.call_one` — [`L33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L33)
- <a id="_Endpoint.calls"></a>`_Endpoint.calls` — [`L27`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L27)
- <a id="_Endpoint.raises"></a>`_Endpoint.raises` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L26)
- <a id="_Endpoint.release"></a>`_Endpoint.release` — [`L29`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L29)
- <a id="_Endpoint.started"></a>`_Endpoint.started` — [`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L28)
- <a id="_Endpoint.value"></a>`_Endpoint.value` — [`L25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L25)
- <a id="_router"></a>`_router` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L66)
- <a id="test_drain_excludes_syncing_generator_from_routes"></a>`test_drain_excludes_syncing_generator_from_routes` — [`L337`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L337)
- <a id="test_drain_excludes_syncing_generator_from_routes._run"></a>`test_drain_excludes_syncing_generator_from_routes._run` — [`L338`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L338)
- <a id="test_drain_pulls_idle_generators_while_busy_generator_drains"></a>`test_drain_pulls_idle_generators_while_busy_generator_drains` — [`L365`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L365)
- <a id="test_drain_pulls_idle_generators_while_busy_generator_drains._run"></a>`test_drain_pulls_idle_generators_while_busy_generator_drains._run` — [`L366`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L366)
- <a id="test_drain_restores_serving_on_pull_failure"></a>`test_drain_restores_serving_on_pull_failure` — [`L457`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L457)
- <a id="test_drain_restores_serving_on_pull_failure._run"></a>`test_drain_restores_serving_on_pull_failure._run` — [`L458`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L458)
- <a id="test_hot_swap_keeps_generators_serving_during_pull"></a>`test_hot_swap_keeps_generators_serving_during_pull` — [`L415`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L415)
- <a id="test_hot_swap_keeps_generators_serving_during_pull._run"></a>`test_hot_swap_keeps_generators_serving_during_pull._run` — [`L416`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L416)
- <a id="test_least_loaded_routes_to_lowest_reserved_load"></a>`test_least_loaded_routes_to_lowest_reserved_load` — [`L76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L76)
- <a id="test_least_loaded_routes_to_lowest_reserved_load._run"></a>`test_least_loaded_routes_to_lowest_reserved_load._run` — [`L77`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L77)
- <a id="test_least_loaded_tie_break_spreads_over_a_changing_candidate_set"></a>`test_least_loaded_tie_break_spreads_over_a_changing_candidate_set` — [`L123`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L123)
- <a id="test_least_loaded_tie_break_spreads_over_a_changing_candidate_set._run"></a>`test_least_loaded_tie_break_spreads_over_a_changing_candidate_set._run` — [`L124`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L124)
- <a id="test_pull_model_state_dict_pulls_every_generator"></a>`test_pull_model_state_dict_pulls_every_generator` — [`L471`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L471)
- <a id="test_pull_model_state_dict_pulls_every_generator._run"></a>`test_pull_model_state_dict_pulls_every_generator._run` — [`L472`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L472)
- <a id="test_round_robin_cycles_through_generators"></a>`test_round_robin_cycles_through_generators` — [`L146`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L146)
- <a id="test_round_robin_cycles_through_generators._run"></a>`test_round_robin_cycles_through_generators._run` — [`L147`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L147)
- <a id="test_round_robin_skips_syncing_generators"></a>`test_round_robin_skips_syncing_generators` — [`L161`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L161)
- <a id="test_round_robin_skips_syncing_generators._run"></a>`test_round_robin_skips_syncing_generators._run` — [`L162`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L162)
- <a id="test_route_releases_reserved_load_on_failure"></a>`test_route_releases_reserved_load_on_failure` — [`L106`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L106)
- <a id="test_route_releases_reserved_load_on_failure._run"></a>`test_route_releases_reserved_load_on_failure._run` — [`L107`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L107)
- <a id="test_single_generator_blocks_routes_while_draining"></a>`test_single_generator_blocks_routes_while_draining` — [`L434`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L434)
- <a id="test_single_generator_blocks_routes_while_draining._run"></a>`test_single_generator_blocks_routes_while_draining._run` — [`L435`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L435)
- <a id="test_sticky_session_assigns_new_generator_when_sticky_target_is_syncing"></a>`test_sticky_session_assigns_new_generator_when_sticky_target_is_syncing` — [`L227`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L227)
- <a id="test_sticky_session_assigns_new_generator_when_sticky_target_is_syncing._run"></a>`test_sticky_session_assigns_new_generator_when_sticky_target_is_syncing._run` — [`L228`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L228)
- <a id="test_sticky_session_can_use_round_robin_for_new_sessions"></a>`test_sticky_session_can_use_round_robin_for_new_sessions` — [`L252`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L252)
- <a id="test_sticky_session_can_use_round_robin_for_new_sessions._run"></a>`test_sticky_session_can_use_round_robin_for_new_sessions._run` — [`L253`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L253)
- <a id="test_sticky_session_rejects_non_positive_max_sessions"></a>`test_sticky_session_rejects_non_positive_max_sessions` — [`L332`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L332)
- <a id="test_sticky_session_respects_max_sessions"></a>`test_sticky_session_respects_max_sessions` — [`L299`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L299)
- <a id="test_sticky_session_respects_max_sessions._run"></a>`test_sticky_session_respects_max_sessions._run` — [`L300`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L300)
- <a id="test_sticky_session_reuses_generator_for_same_session"></a>`test_sticky_session_reuses_generator_for_same_session` — [`L174`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L174)
- <a id="test_sticky_session_reuses_generator_for_same_session._run"></a>`test_sticky_session_reuses_generator_for_same_session._run` — [`L175`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L175)
- <a id="test_sticky_session_spreads_new_sessions_started_on_idle_generators"></a>`test_sticky_session_spreads_new_sessions_started_on_idle_generators` — [`L208`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L208)
- <a id="test_sticky_session_spreads_new_sessions_started_on_idle_generators._run"></a>`test_sticky_session_spreads_new_sessions_started_on_idle_generators._run` — [`L209`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L209)
- <a id="test_sticky_session_without_session_id_uses_fallback_without_affinity"></a>`test_sticky_session_without_session_id_uses_fallback_without_affinity` — [`L282`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L282)
- <a id="test_sticky_session_without_session_id_uses_fallback_without_affinity._run"></a>`test_sticky_session_without_session_id_uses_fallback_without_affinity._run` — [`L283`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_inter_generator_router.py#L283)
