---
title: 'Module: torchtitan/experiments/rl/tests/test_rollouter_pool.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/tests/test_rollouter_pool.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.tests.test_rollouter_pool`/
symbols:
  test_setup_spawns_worker_pool_on_controller_host.run: test_setup_spawns_worker_pool_on_controller_host().run().
  test_rollout_group_dispatch_uses_choose.run: test_rollout_group_dispatch_uses_choose().run().
  _setup: _setup().
  _rollouter_without_datasets: _rollouter_without_datasets().
  _ChooseRunGroupEndpoint._execute: _ChooseRunGroupEndpoint#_execute().
  _ChooseRunGroupEndpoint.choose: _ChooseRunGroupEndpoint#choose().
  _WorkerMesh.spawn: _WorkerMesh#spawn().
  _WorkerMesh.stop: _WorkerMesh#stop().
  _ControllerHost.spawn_procs: _ControllerHost#spawn_procs().
  _WorkerActorMesh.run_group: _WorkerActorMesh#run_group.
  _WorkerActorMesh: _WorkerActorMesh#
  _WorkerMesh: _WorkerMesh#
  _WorkerMesh.actor_mesh: _WorkerMesh#actor_mesh.
  _WorkerActorMesh.setup_async: _WorkerActorMesh#setup_async.
  _WorkerActorMesh.stop: _WorkerActorMesh#stop().
  _WorkerActorMesh.stopped: _WorkerActorMesh#stopped.
  _SetupEndpoint.call: _SetupEndpoint#call().
  _WorkerMesh.__init__: _WorkerMesh#__init__().
  _ControllerHost.__init__: _ControllerHost#__init__().
  test_setup_spawns_worker_pool_on_controller_host: test_setup_spawns_worker_pool_on_controller_host().
  test_rollout_group_dispatch_uses_choose: test_rollout_group_dispatch_uses_choose().
  _ChooseRunGroupEndpoint.calls: _ChooseRunGroupEndpoint#calls.
  _ChooseRunGroupEndpoint.started: _ChooseRunGroupEndpoint#started.
  _ChooseRunGroupEndpoint.release: _ChooseRunGroupEndpoint#release.
  _SetupEndpoint.calls: _SetupEndpoint#calls.
  _WorkerMesh.spawn_args: _WorkerMesh#spawn_args.
  _WorkerMesh.stopped: _WorkerMesh#stopped.
  _ControllerHost: _ControllerHost#
  _ControllerHost.spawn_kwargs: _ControllerHost#spawn_kwargs.
  _ChooseRunGroupEndpoint: _ChooseRunGroupEndpoint#
  _SetupEndpoint: _SetupEndpoint#
  _ControllerHost.worker_mesh: _ControllerHost#worker_mesh.
  _ChooseRunGroupEndpoint.__init__: _ChooseRunGroupEndpoint#__init__().
  _SetupEndpoint.__init__: _SetupEndpoint#__init__().
  _WorkerActorMesh.__init__: _WorkerActorMesh#__init__().
---
# Module: [`torchtitan/experiments/rl/tests/test_rollouter_pool.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py)

> **Collapsed catalog** (35 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="_ChooseRunGroupEndpoint"></a>`_ChooseRunGroupEndpoint` — [`L19`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L19)
- <a id="_ChooseRunGroupEndpoint.__init__"></a>`_ChooseRunGroupEndpoint.__init__` — [`L20`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L20)
- <a id="_ChooseRunGroupEndpoint._execute"></a>`_ChooseRunGroupEndpoint._execute` — [`L30`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L30)
- <a id="_ChooseRunGroupEndpoint.calls"></a>`_ChooseRunGroupEndpoint.calls` — [`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L21)
- <a id="_ChooseRunGroupEndpoint.choose"></a>`_ChooseRunGroupEndpoint.choose` — [`L25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L25)
- <a id="_ChooseRunGroupEndpoint.release"></a>`_ChooseRunGroupEndpoint.release` — [`L23`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L23)
- <a id="_ChooseRunGroupEndpoint.started"></a>`_ChooseRunGroupEndpoint.started` — [`L22`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L22)
- <a id="_ControllerHost"></a>`_ControllerHost` — [`L68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L68)
- <a id="_ControllerHost.__init__"></a>`_ControllerHost.__init__` — [`L69`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L69)
- <a id="_ControllerHost.spawn_kwargs"></a>`_ControllerHost.spawn_kwargs` — [`L71`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L71)
- <a id="_ControllerHost.spawn_procs"></a>`_ControllerHost.spawn_procs` — [`L73`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L73)
- <a id="_ControllerHost.worker_mesh"></a>`_ControllerHost.worker_mesh` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L70)
- <a id="_SetupEndpoint"></a>`_SetupEndpoint` — [`L35`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L35)
- <a id="_SetupEndpoint.__init__"></a>`_SetupEndpoint.__init__` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L36)
- <a id="_SetupEndpoint.call"></a>`_SetupEndpoint.call` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L39)
- <a id="_SetupEndpoint.calls"></a>`_SetupEndpoint.calls` — [`L37`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L37)
- <a id="_WorkerActorMesh"></a>`_WorkerActorMesh` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L43)
- <a id="_WorkerActorMesh.__init__"></a>`_WorkerActorMesh.__init__` — [`L44`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L44)
- <a id="_WorkerActorMesh.run_group"></a>`_WorkerActorMesh.run_group` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L46)
- <a id="_WorkerActorMesh.setup_async"></a>`_WorkerActorMesh.setup_async` — [`L45`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L45)
- <a id="_WorkerActorMesh.stop"></a>`_WorkerActorMesh.stop` — [`L49`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L49)
- <a id="_WorkerActorMesh.stopped"></a>`_WorkerActorMesh.stopped` — [`L47`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L47)
- <a id="_WorkerMesh"></a>`_WorkerMesh` — [`L53`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L53)
- <a id="_WorkerMesh.__init__"></a>`_WorkerMesh.__init__` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L54)
- <a id="_WorkerMesh.actor_mesh"></a>`_WorkerMesh.actor_mesh` — [`L55`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L55)
- <a id="_WorkerMesh.spawn"></a>`_WorkerMesh.spawn` — [`L59`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L59)
- <a id="_WorkerMesh.spawn_args"></a>`_WorkerMesh.spawn_args` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L56)
- <a id="_WorkerMesh.stop"></a>`_WorkerMesh.stop` — [`L63`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L63)
- <a id="_WorkerMesh.stopped"></a>`_WorkerMesh.stopped` — [`L57`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L57)
- <a id="_rollouter_without_datasets"></a>`_rollouter_without_datasets` — [`L78`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L78)
- <a id="_setup"></a>`_setup` — [`L90`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L90)
- <a id="test_rollout_group_dispatch_uses_choose"></a>`test_rollout_group_dispatch_uses_choose` — [`L142`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L142)
- <a id="test_rollout_group_dispatch_uses_choose.run"></a>`test_rollout_group_dispatch_uses_choose.run` — [`L143`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L143)
- <a id="test_setup_spawns_worker_pool_on_controller_host"></a>`test_setup_spawns_worker_pool_on_controller_host` — [`L106`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L106)
- <a id="test_setup_spawns_worker_pool_on_controller_host.run"></a>`test_setup_spawns_worker_pool_on_controller_host.run` — [`L107`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_rollouter_pool.py#L107)
