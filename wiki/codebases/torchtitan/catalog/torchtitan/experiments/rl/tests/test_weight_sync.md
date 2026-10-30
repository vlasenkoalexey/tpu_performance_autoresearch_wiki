---
title: 'Module: torchtitan/experiments/rl/tests/test_weight_sync.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/tests/test_weight_sync.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.tests.test_weight_sync`/
symbols:
  test_push_then_pull_then_buffer_release_in_order.run: test_push_then_pull_then_buffer_release_in_order().run().
  test_wait_before_first_start_returns_zero_metrics.run: test_wait_before_first_start_returns_zero_metrics().run().
  test_start_async_push_pull_returns_before_work_runs.run: test_start_async_push_pull_returns_before_work_runs().run().
  test_push_exception_propagates_through_wait.run: test_push_exception_propagates_through_wait().run().
  test_buffer_release_uses_num_prompts_per_train_step_and_trained_reason.run: test_buffer_release_uses_num_prompts_per_train_step_and_trained_reason().run().
  test_pull_threads_the_started_version.run: test_pull_threads_the_started_version().run().
  test_pull_waits_for_its_own_push_not_a_later_one.run: test_pull_waits_for_its_own_push_not_a_later_one().run().
  _manager: _manager().
  _noop: _noop().
  _FakeTrainer: _FakeTrainer#
  _FakeRouter: _FakeRouter#
  _FakeBuffer: _FakeBuffer#
  _FakeBuffer.release_active_groups: _FakeBuffer#release_active_groups().
  _Endpoint.call: _Endpoint#call().
  _FakeTrainer.__init__: _FakeTrainer#__init__().
  _FakeRouter.pull_model_state_dict: _FakeRouter#pull_model_state_dict.
  _PullEndpoint.call_one: _PullEndpoint#call_one().
  test_push_then_pull_then_buffer_release_in_order: test_push_then_pull_then_buffer_release_in_order().
  test_start_async_push_pull_returns_before_work_runs: test_start_async_push_pull_returns_before_work_runs().
  test_buffer_release_uses_num_prompts_per_train_step_and_trained_reason: test_buffer_release_uses_num_prompts_per_train_step_and_trained_reason().
  test_pull_threads_the_started_version: test_pull_threads_the_started_version().
  test_wait_before_first_start_returns_zero_metrics: test_wait_before_first_start_returns_zero_metrics().
  test_pull_waits_for_its_own_push_not_a_later_one: test_pull_waits_for_its_own_push_not_a_later_one().
  test_push_exception_propagates_through_wait: test_push_exception_propagates_through_wait().
  TRAINER_PUSH_KEY: TRAINER_PUSH_KEY.
  _PullEndpoint._router: _PullEndpoint#_router.
  _FakeBuffer.releases: _FakeBuffer#releases.
  _FakeBuffer._events: _FakeBuffer#_events.
  GENERATOR_PULL_KEY: GENERATOR_PULL_KEY.
  _Endpoint: _Endpoint#
  _Endpoint._on_call: _Endpoint#_on_call.
  _FakeRouter.pulled_versions: _FakeRouter#pulled_versions.
  test_push_then_pull_then_buffer_release_in_order.run.on_push: test_push_then_pull_then_buffer_release_in_order().run().on_push().
  test_push_then_pull_then_buffer_release_in_order.run.on_pull: test_push_then_pull_then_buffer_release_in_order().run().on_pull().
  test_start_async_push_pull_returns_before_work_runs.run.on_push: test_start_async_push_pull_returns_before_work_runs().run().on_push().
  test_start_async_push_pull_returns_before_work_runs.run.on_pull: test_start_async_push_pull_returns_before_work_runs().run().on_pull().
  test_pull_waits_for_its_own_push_not_a_later_one.run.on_push: test_pull_waits_for_its_own_push_not_a_later_one().run().on_push().
  test_push_exception_propagates_through_wait.run.boom: test_push_exception_propagates_through_wait().run().boom().
  _PullEndpoint: _PullEndpoint#
  _Endpoint.__init__: _Endpoint#__init__().
  _FakeTrainer.push_model_state_dict: _FakeTrainer#push_model_state_dict.
  _FakeRouter.__init__: _FakeRouter#__init__().
  _FakeRouter._on_pull: _FakeRouter#_on_pull.
  _PullEndpoint.__init__: _PullEndpoint#__init__().
  _FakeBuffer.__init__: _FakeBuffer#__init__().
---
# Module: [`torchtitan/experiments/rl/tests/test_weight_sync.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py)

> **Collapsed catalog** (45 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="GENERATOR_PULL_KEY"></a>`GENERATOR_PULL_KEY` — [`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L21)
- <a id="TRAINER_PUSH_KEY"></a>`TRAINER_PUSH_KEY` — [`L20`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L20)
- <a id="_Endpoint"></a>`_Endpoint` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L24)
- <a id="_Endpoint.__init__"></a>`_Endpoint.__init__` — [`L27`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L27)
- <a id="_Endpoint._on_call"></a>`_Endpoint._on_call` — [`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L28)
- <a id="_Endpoint.call"></a>`_Endpoint.call` — [`L30`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L30)
- <a id="_FakeBuffer"></a>`_FakeBuffer` — [`L55`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L55)
- <a id="_FakeBuffer.__init__"></a>`_FakeBuffer.__init__` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L56)
- <a id="_FakeBuffer._events"></a>`_FakeBuffer._events` — [`L58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L58)
- <a id="_FakeBuffer.release_active_groups"></a>`_FakeBuffer.release_active_groups` — [`L60`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L60)
- <a id="_FakeBuffer.releases"></a>`_FakeBuffer.releases` — [`L57`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L57)
- <a id="_FakeRouter"></a>`_FakeRouter` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L39)
- <a id="_FakeRouter.__init__"></a>`_FakeRouter.__init__` — [`L40`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L40)
- <a id="_FakeRouter._on_pull"></a>`_FakeRouter._on_pull` — [`L41`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L41)
- <a id="_FakeRouter.pull_model_state_dict"></a>`_FakeRouter.pull_model_state_dict` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L43)
- <a id="_FakeRouter.pulled_versions"></a>`_FakeRouter.pulled_versions` — [`L42`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L42)
- <a id="_FakeTrainer"></a>`_FakeTrainer` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L34)
- <a id="_FakeTrainer.__init__"></a>`_FakeTrainer.__init__` — [`L35`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L35)
- <a id="_FakeTrainer.push_model_state_dict"></a>`_FakeTrainer.push_model_state_dict` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L36)
- <a id="_PullEndpoint"></a>`_PullEndpoint` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L46)
- <a id="_PullEndpoint.__init__"></a>`_PullEndpoint.__init__` — [`L47`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L47)
- <a id="_PullEndpoint._router"></a>`_PullEndpoint._router` — [`L48`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L48)
- <a id="_PullEndpoint.call_one"></a>`_PullEndpoint.call_one` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L50)
- <a id="_manager"></a>`_manager` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L70)
- <a id="_noop"></a>`_noop` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L66)
- <a id="test_buffer_release_uses_num_prompts_per_train_step_and_trained_reason"></a>`test_buffer_release_uses_num_prompts_per_train_step_and_trained_reason` — [`L137`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L137)
- <a id="test_buffer_release_uses_num_prompts_per_train_step_and_trained_reason.run"></a>`test_buffer_release_uses_num_prompts_per_train_step_and_trained_reason.run` — [`L138`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L138)
- <a id="test_pull_threads_the_started_version"></a>`test_pull_threads_the_started_version` — [`L153`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L153)
- <a id="test_pull_threads_the_started_version.run"></a>`test_pull_threads_the_started_version.run` — [`L154`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L154)
- <a id="test_pull_waits_for_its_own_push_not_a_later_one"></a>`test_pull_waits_for_its_own_push_not_a_later_one` — [`L178`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L178)
- <a id="test_pull_waits_for_its_own_push_not_a_later_one.run"></a>`test_pull_waits_for_its_own_push_not_a_later_one.run` — [`L181`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L181)
- <a id="test_pull_waits_for_its_own_push_not_a_later_one.run.on_push"></a>`test_pull_waits_for_its_own_push_not_a_later_one.run.on_push` — [`L185`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L185)
- <a id="test_push_exception_propagates_through_wait"></a>`test_push_exception_propagates_through_wait` — [`L213`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L213)
- <a id="test_push_exception_propagates_through_wait.run"></a>`test_push_exception_propagates_through_wait.run` — [`L214`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L214)
- <a id="test_push_exception_propagates_through_wait.run.boom"></a>`test_push_exception_propagates_through_wait.run.boom` — [`L215`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L215)
- <a id="test_push_then_pull_then_buffer_release_in_order"></a>`test_push_then_pull_then_buffer_release_in_order` — [`L79`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L79)
- <a id="test_push_then_pull_then_buffer_release_in_order.run"></a>`test_push_then_pull_then_buffer_release_in_order.run` — [`L80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L80)
- <a id="test_push_then_pull_then_buffer_release_in_order.run.on_pull"></a>`test_push_then_pull_then_buffer_release_in_order.run.on_pull` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L86)
- <a id="test_push_then_pull_then_buffer_release_in_order.run.on_push"></a>`test_push_then_pull_then_buffer_release_in_order.run.on_push` — [`L83`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L83)
- <a id="test_start_async_push_pull_returns_before_work_runs"></a>`test_start_async_push_pull_returns_before_work_runs` — [`L107`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L107)
- <a id="test_start_async_push_pull_returns_before_work_runs.run"></a>`test_start_async_push_pull_returns_before_work_runs.run` — [`L108`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L108)
- <a id="test_start_async_push_pull_returns_before_work_runs.run.on_pull"></a>`test_start_async_push_pull_returns_before_work_runs.run.on_pull` — [`L116`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L116)
- <a id="test_start_async_push_pull_returns_before_work_runs.run.on_push"></a>`test_start_async_push_pull_returns_before_work_runs.run.on_push` — [`L112`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L112)
- <a id="test_wait_before_first_start_returns_zero_metrics"></a>`test_wait_before_first_start_returns_zero_metrics` — [`L164`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L164)
- <a id="test_wait_before_first_start_returns_zero_metrics.run"></a>`test_wait_before_first_start_returns_zero_metrics.run` — [`L165`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_weight_sync.py#L165)
