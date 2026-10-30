---
title: 'Module: torchtitan/experiments/rl/tests/test_shutdown.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/tests/test_shutdown.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.tests.test_shutdown`/
symbols:
  test_async_loop_config_derives_window_and_max_offpolicy_steps: test_async_loop_config_derives_window_and_max_offpolicy_steps().
  test_shutdown_calls_actor_close_before_mesh_stop: test_shutdown_calls_actor_close_before_mesh_stop().
  test_shutdown_closes_all_generators: test_shutdown_closes_all_generators().
  test_shutdown_continues_after_actor_close_failure: test_shutdown_continues_after_actor_close_failure().
  test_shutdown_continues_after_generator_close_failure: test_shutdown_continues_after_generator_close_failure().
  test_main_shuts_down_after_success: test_main_shuts_down_after_success().
  test_main_passes_configured_num_generators: test_main_passes_configured_num_generators().
  test_main_shuts_down_after_train_failure: test_main_shuts_down_after_train_failure().
  test_main_shuts_down_after_setup_failure: test_main_shuts_down_after_setup_failure().
  test_main_swallows_cancellation_after_shutdown: test_main_swallows_cancellation_after_shutdown().
  test_async_loop_config_handles_window_fraction_bounds: test_async_loop_config_handles_window_fraction_bounds().
  test_rl_trainer_shutdown_is_noop_before_meshes_spawn: test_rl_trainer_shutdown_is_noop_before_meshes_spawn().
  _set_generator_router: _set_generator_router().
  _FakeController: _FakeController#
  _FakeController.instances: _FakeController#instances.
  _FakeController.setup_async: _FakeController#setup_async().
  _FakeConfigManager: _FakeConfigManager#
  _make_stub_rl_trainer: _make_stub_rl_trainer().
  _StubActor: _StubActor#
  _FakeConfigManager.config: _FakeConfigManager#config.
  _StubEndpoint.call: _StubEndpoint#call().
  _FakeConfig: _FakeConfig#
  _FakeController.run: _FakeController#run().
  _FakeConfig.__class__: _FakeConfig#__class__().
  _make_stub_rl_trainer._StubConfig.metrics: _make_stub_rl_trainer()._StubConfig#metrics.
  _make_stub_rl_trainer._StubConfig.rollout_recorder: _make_stub_rl_trainer()._StubConfig#rollout_recorder.
  _StubMesh: _StubMesh#
  _StubMesh.stop: _StubMesh#stop().
  _FakeController.setup_generator_meshes: _FakeController#setup_generator_meshes.
  _FakeController.config: _FakeController#config.
  _FakeController.events: _FakeController#events.
  _FakeController.close: _FakeController#close().
  _FakeTrainerConfig.debug: _FakeTrainerConfig#debug.
  _FakeConfig.trainer: _FakeConfig#trainer.
  _FakeConfig.build: _FakeConfig#build().
  _FakeConfigManager.parse_args: _FakeConfigManager#parse_args().
  _make_stub_rl_trainer._StubConfig.async_loop: _make_stub_rl_trainer()._StubConfig#async_loop.
  _make_stub_rl_trainer._StubConfig.generator: _make_stub_rl_trainer()._StubConfig#generator.
  _make_stub_rl_trainer._StubConfig.rollouter: _make_stub_rl_trainer()._StubConfig#rollouter.
  stub_mesh_provisioning: stub_mesh_provisioning().
  test_vllm_generator_does_not_touch_cuda_from_finalizer: test_vllm_generator_does_not_touch_cuda_from_finalizer().
  _RouterCloseEndpoint.call_one: _RouterCloseEndpoint#call_one().
  _StubRouterHandle.__init__: _StubRouterHandle#__init__().
  _StubActor.__init__: _StubActor#__init__().
  _StubEndpoint._name: _StubEndpoint#_name.
  _FakeController.setup_trainer_mesh: _FakeController#setup_trainer_mesh.
  _FakeDebug: _FakeDebug#
  _FakeTrainerConfig: _FakeTrainerConfig#
  _make_stub_rl_trainer._StubRollouter: _make_stub_rl_trainer()._StubRollouter#
  _make_stub_rl_trainer._StubConfig: _make_stub_rl_trainer()._StubConfig#
  stub_mesh_provisioning._spawn_proc_mesh: stub_mesh_provisioning()._spawn_proc_mesh().
  _StubEndpoint: _StubEndpoint#
  _StubEndpoint._events: _StubEndpoint#_events.
  _StubEndpoint._raises: _StubEndpoint#_raises.
  _RouterCloseEndpoint: _RouterCloseEndpoint#
  _RouterCloseEndpoint._router: _RouterCloseEndpoint#_router.
  _StubRouterHandle: _StubRouterHandle#
  _StubMesh._name: _StubMesh#_name.
  _StubMesh._events: _StubMesh#_events.
  _FakeController.__init__: _FakeController#__init__().
  _FakeDebug.enable_structured_logging: _FakeDebug#enable_structured_logging.
  _FakeTrainerConfig.parallelism: _FakeTrainerConfig#parallelism.
  _FakeConfig.dump_folder: _FakeConfig#dump_folder.
  _FakeConfig.generator: _FakeConfig#generator.
  _FakeConfig.num_generators: _FakeConfig#num_generators.
  _FakeConfig.__init__: _FakeConfig#__init__().
  _make_stub_rl_trainer._StubRollouter.close: _make_stub_rl_trainer()._StubRollouter#close().
  _make_stub_rl_trainer._StubConfig.dump_folder: _make_stub_rl_trainer()._StubConfig#dump_folder.
  _make_stub_rl_trainer._StubConfig.hf_assets_path: _make_stub_rl_trainer()._StubConfig#hf_assets_path.
  _make_stub_rl_trainer._StubConfig.tokenizer: _make_stub_rl_trainer()._StubConfig#tokenizer.
  _make_stub_rl_trainer._StubConfig.renderer: _make_stub_rl_trainer()._StubConfig#renderer.
  _make_stub_rl_trainer._StubConfig.to_dict: _make_stub_rl_trainer()._StubConfig#to_dict().
  _StubEndpoint.__init__: _StubEndpoint#__init__().
  _RouterCloseEndpoint.__init__: _RouterCloseEndpoint#__init__().
  _StubRouterHandle.close_generators: _StubRouterHandle#close_generators.
  _StubActor.close: _StubActor#close.
  _StubActor.flatten: _StubActor#flatten().
  _StubActor.slice: _StubActor#slice().
  _StubActor.__len__: _StubActor#__len__().
  _StubMesh.__init__: _StubMesh#__init__().
---
# Module: [`torchtitan/experiments/rl/tests/test_shutdown.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py)

> **Collapsed catalog** (80 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="_FakeConfig"></a>`_FakeConfig` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L66)
- <a id="_FakeConfig.__class__"></a>`_FakeConfig.__class__` — [`L76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L76)
- <a id="_FakeConfig.__init__"></a>`_FakeConfig.__init__` — [`L82`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L82)
- <a id="_FakeConfig.build"></a>`_FakeConfig.build` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L86)
- <a id="_FakeConfig.dump_folder"></a>`_FakeConfig.dump_folder` — [`L69`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L69)
- <a id="_FakeConfig.generator"></a>`_FakeConfig.generator` — [`L72`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L72)
- <a id="_FakeConfig.num_generators"></a>`_FakeConfig.num_generators` — [`L73`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L73)
- <a id="_FakeConfig.trainer"></a>`_FakeConfig.trainer` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L70)
- <a id="_FakeConfigManager"></a>`_FakeConfigManager` — [`L90`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L90)
- <a id="_FakeConfigManager.config"></a>`_FakeConfigManager.config` — [`L91`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L91)
- <a id="_FakeConfigManager.parse_args"></a>`_FakeConfigManager.parse_args` — [`L93`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L93) — documented in [trainer-and-train-loop](../../../../../concepts/trainer-and-train-loop.md)
- <a id="_FakeController"></a>`_FakeController` — [`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L21)
- <a id="_FakeController.__init__"></a>`_FakeController.__init__` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L24)
- <a id="_FakeController.close"></a>`_FakeController.close` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L50)
- <a id="_FakeController.config"></a>`_FakeController.config` — [`L25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L25)
- <a id="_FakeController.events"></a>`_FakeController.events` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L26)
- <a id="_FakeController.instances"></a>`_FakeController.instances` — [`L22`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L22)
- <a id="_FakeController.run"></a>`_FakeController.run` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L43)
- <a id="_FakeController.setup_async"></a>`_FakeController.setup_async` — [`L31`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L31)
- <a id="_FakeController.setup_generator_meshes"></a>`_FakeController.setup_generator_meshes` — [`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L28)
- <a id="_FakeController.setup_trainer_mesh"></a>`_FakeController.setup_trainer_mesh` — [`L27`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L27)
- <a id="_FakeDebug"></a>`_FakeDebug` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L54)
- <a id="_FakeDebug.enable_structured_logging"></a>`_FakeDebug.enable_structured_logging` — [`L55`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L55)
- <a id="_FakeTrainerConfig"></a>`_FakeTrainerConfig` — [`L58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L58)
- <a id="_FakeTrainerConfig.debug"></a>`_FakeTrainerConfig.debug` — [`L59`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L59)
- <a id="_FakeTrainerConfig.parallelism"></a>`_FakeTrainerConfig.parallelism` — [`L63`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L63)
- <a id="_RouterCloseEndpoint"></a>`_RouterCloseEndpoint` — [`L308`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L308)
- <a id="_RouterCloseEndpoint.__init__"></a>`_RouterCloseEndpoint.__init__` — [`L309`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L309)
- <a id="_RouterCloseEndpoint._router"></a>`_RouterCloseEndpoint._router` — [`L310`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L310)
- <a id="_RouterCloseEndpoint.call_one"></a>`_RouterCloseEndpoint.call_one` — [`L312`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L312)
- <a id="_StubActor"></a>`_StubActor` — [`L323`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L323)
- <a id="_StubActor.__init__"></a>`_StubActor.__init__` — [`L324`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L324)
- <a id="_StubActor.__len__"></a>`_StubActor.__len__` — [`L335`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L335)
- <a id="_StubActor.close"></a>`_StubActor.close` — [`L325`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L325)
- <a id="_StubActor.flatten"></a>`_StubActor.flatten` — [`L327`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L327)
- <a id="_StubActor.slice"></a>`_StubActor.slice` — [`L332`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L332)
- <a id="_StubEndpoint"></a>`_StubEndpoint` — [`L296`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L296)
- <a id="_StubEndpoint.__init__"></a>`_StubEndpoint.__init__` — [`L297`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L297)
- <a id="_StubEndpoint._events"></a>`_StubEndpoint._events` — [`L299`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L299)
- <a id="_StubEndpoint._name"></a>`_StubEndpoint._name` — [`L298`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L298)
- <a id="_StubEndpoint._raises"></a>`_StubEndpoint._raises` — [`L300`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L300)
- <a id="_StubEndpoint.call"></a>`_StubEndpoint.call` — [`L302`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L302)
- <a id="_StubMesh"></a>`_StubMesh` — [`L339`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L339)
- <a id="_StubMesh.__init__"></a>`_StubMesh.__init__` — [`L340`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L340)
- <a id="_StubMesh._events"></a>`_StubMesh._events` — [`L342`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L342)
- <a id="_StubMesh._name"></a>`_StubMesh._name` — [`L341`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L341)
- <a id="_StubMesh.stop"></a>`_StubMesh.stop` — [`L344`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L344)
- <a id="_StubRouterHandle"></a>`_StubRouterHandle` — [`L316`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L316)
- <a id="_StubRouterHandle.__init__"></a>`_StubRouterHandle.__init__` — [`L319`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L319)
- <a id="_StubRouterHandle.close_generators"></a>`_StubRouterHandle.close_generators` — [`L320`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L320)
- <a id="_make_stub_rl_trainer"></a>`_make_stub_rl_trainer` — [`L163`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L163)
- <a id="_make_stub_rl_trainer._StubConfig"></a>`_make_stub_rl_trainer._StubConfig` — [`L171`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L171)
- <a id="_make_stub_rl_trainer._StubConfig.async_loop"></a>`_make_stub_rl_trainer._StubConfig.async_loop` — [`L172`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L172)
- <a id="_make_stub_rl_trainer._StubConfig.dump_folder"></a>`_make_stub_rl_trainer._StubConfig.dump_folder` — [`L174`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L174)
- <a id="_make_stub_rl_trainer._StubConfig.generator"></a>`_make_stub_rl_trainer._StubConfig.generator` — [`L185`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L185)
- <a id="_make_stub_rl_trainer._StubConfig.hf_assets_path"></a>`_make_stub_rl_trainer._StubConfig.hf_assets_path` — [`L176`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L176)
- <a id="_make_stub_rl_trainer._StubConfig.metrics"></a>`_make_stub_rl_trainer._StubConfig.metrics` — [`L173`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L173)
- <a id="_make_stub_rl_trainer._StubConfig.renderer"></a>`_make_stub_rl_trainer._StubConfig.renderer` — [`L181`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L181)
- <a id="_make_stub_rl_trainer._StubConfig.rollout_recorder"></a>`_make_stub_rl_trainer._StubConfig.rollout_recorder` — [`L175`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L175)
- <a id="_make_stub_rl_trainer._StubConfig.rollouter"></a>`_make_stub_rl_trainer._StubConfig.rollouter` — [`L188`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L188)
- <a id="_make_stub_rl_trainer._StubConfig.to_dict"></a>`_make_stub_rl_trainer._StubConfig.to_dict` — [`L190`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L190)
- <a id="_make_stub_rl_trainer._StubConfig.tokenizer"></a>`_make_stub_rl_trainer._StubConfig.tokenizer` — [`L178`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L178)
- <a id="_make_stub_rl_trainer._StubRollouter"></a>`_make_stub_rl_trainer._StubRollouter` — [`L167`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L167)
- <a id="_make_stub_rl_trainer._StubRollouter.close"></a>`_make_stub_rl_trainer._StubRollouter.close` — [`L168`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L168)
- <a id="_set_generator_router"></a>`_set_generator_router` — [`L348`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L348)
- <a id="stub_mesh_provisioning"></a>`stub_mesh_provisioning` — [`L197`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L197)
- <a id="stub_mesh_provisioning._spawn_proc_mesh"></a>`stub_mesh_provisioning._spawn_proc_mesh` — [`L208`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L208)
- <a id="test_async_loop_config_derives_window_and_max_offpolicy_steps"></a>`test_async_loop_config_derives_window_and_max_offpolicy_steps` — [`L97`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L97)
- <a id="test_async_loop_config_handles_window_fraction_bounds"></a>`test_async_loop_config_handles_window_fraction_bounds` — [`L149`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L149)
- <a id="test_main_passes_configured_num_generators"></a>`test_main_passes_configured_num_generators` — [`L230`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L230)
- <a id="test_main_shuts_down_after_setup_failure"></a>`test_main_shuts_down_after_setup_failure` — [`L256`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L256)
- <a id="test_main_shuts_down_after_success"></a>`test_main_shuts_down_after_success` — [`L217`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L217)
- <a id="test_main_shuts_down_after_train_failure"></a>`test_main_shuts_down_after_train_failure` — [`L245`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L245)
- <a id="test_main_swallows_cancellation_after_shutdown"></a>`test_main_swallows_cancellation_after_shutdown` — [`L277`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L277)
- <a id="test_rl_trainer_shutdown_is_noop_before_meshes_spawn"></a>`test_rl_trainer_shutdown_is_noop_before_meshes_spawn` — [`L267`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L267)
- <a id="test_shutdown_calls_actor_close_before_mesh_stop"></a>`test_shutdown_calls_actor_close_before_mesh_stop` — [`L357`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L357)
- <a id="test_shutdown_closes_all_generators"></a>`test_shutdown_closes_all_generators` — [`L378`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L378)
- <a id="test_shutdown_continues_after_actor_close_failure"></a>`test_shutdown_continues_after_actor_close_failure` — [`L401`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L401)
- <a id="test_shutdown_continues_after_generator_close_failure"></a>`test_shutdown_continues_after_generator_close_failure` — [`L414`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L414)
- <a id="test_vllm_generator_does_not_touch_cuda_from_finalizer"></a>`test_vllm_generator_does_not_touch_cuda_from_finalizer` — [`L292`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_shutdown.py#L292)
