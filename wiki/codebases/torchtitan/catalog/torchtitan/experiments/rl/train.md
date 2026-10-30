---
title: 'Module: torchtitan/experiments/rl/train.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/train.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.train`/
symbols:
  main: main().
  spawn_proc_mesh: spawn_proc_mesh().
  _compute_trainer_world_size: _compute_trainer_world_size().
  PerHostProvisioner.allocate: PerHostProvisioner#allocate().
  _compute_generator_world_size: _compute_generator_world_size().
  PerHostProvisioner.available: PerHostProvisioner#available().
  _spawn_proc_mesh: _spawn_proc_mesh().
  PerHostProvisioner.next_gpu: PerHostProvisioner#next_gpu.
  _bootstrap_generator: _bootstrap_generator().
  _preimport_torch: _preimport_torch().
  logger: logger.
  PerHostProvisioner: PerHostProvisioner#
  PerHostProvisioner.total_gpus: PerHostProvisioner#total_gpus.
  breakable_cudagraph_env: breakable_cudagraph_env().
  HostMeshes: HostMeshes#
  HostMeshes.trainer: HostMeshes#trainer.
  HostMeshes.generators: HostMeshes#generators.
  HostMeshes.gpus_per_node: HostMeshes#gpus_per_node.
  PerHostProvisioner.__init__: PerHostProvisioner#__init__().
---
# Module: [`torchtitan/experiments/rl/train.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py)

## Classes
### <a id="HostMeshes"></a>`HostMeshes`
- def: [`torchtitan/experiments/rl/train.py:138`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L138)
- signature: `class HostMeshes:`
- members:
  - <a id="HostMeshes.generators"></a>`generators` — [`L140`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L140)
  - <a id="HostMeshes.gpus_per_node"></a>`gpus_per_node` — [`L141`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L141)
  - <a id="HostMeshes.trainer"></a>`trainer` — [`L139`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L139)
- used by: [`spawn_proc_mesh`](train.md#spawn_proc_mesh)

### <a id="PerHostProvisioner"></a>`PerHostProvisioner`
- def: [`torchtitan/experiments/rl/train.py:102`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L102) — documented in [rl-training](../../../../concepts/rl-training.md)
- doc: Allocates non-overlapping GPU ranges within a single host.
- signature: `class PerHostProvisioner:`
- members:
  - <a id="PerHostProvisioner.allocate"></a>`allocate(self, num_gpus: int, *, extra_env: dict[str, str] | None = None)` — [`L120`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L120)
  - <a id="PerHostProvisioner.available"></a>`available(self)` — [`L117`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L117)
  - <a id="PerHostProvisioner.next_gpu"></a>`next_gpu` — [`L114`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L114)
  - <a id="PerHostProvisioner.total_gpus"></a>`total_gpus` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L113)
- protocol/private: <a id="PerHostProvisioner.__init__"></a>`__init__`[`L112`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L112)
- used by: [`spawn_proc_mesh`](train.md#spawn_proc_mesh), [`_spawn_proc_mesh`](train.md#_spawn_proc_mesh)

## Functions
- <a id="_bootstrap_generator"></a>`_bootstrap_generator()` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L69) — ``bootstrap`` setup callable for VLLMGenerator.
- <a id="_compute_generator_world_size"></a>`_compute_generator_world_size(p: InferenceParallelismConfig)` — [`L156`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L156) — Number of GPU processes for one generator (vLLM) instance.
- <a id="_compute_trainer_world_size"></a>`_compute_trainer_world_size(p: ParallelismConfig)` — [`L144`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L144) — Compute world size from all parallel dimensions.
- <a id="_preimport_torch"></a>`_preimport_torch()` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L63) — ``bootstrap`` setup callable: pre-import torch on the spawned proc.
- <a id="_spawn_proc_mesh"></a>`_spawn_proc_mesh(host_mesh: HostMesh, role_world_size: int, gpus_per_node: int, *, bootstrap: Callable[[], None], role: str, extra_env: dict[str, str] | None = None)` — [`L161`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L161) — Spawn one role's proc mesh on ``host_mesh``, splitting ``role_world_size``
- <a id="breakable_cudagraph_env"></a>`breakable_cudagraph_env(generator_cfg)` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L41) — Per-proc launch env a FULL_AND_PIECEWISE generator needs: ``VLLM_USE_BREAKABLE_CUDAGRAPH``.
- <a id="main"></a>`main()` — [`L273`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L273) — documented in [rl-training](../../../../concepts/rl-training.md)
- <a id="spawn_proc_mesh"></a>`spawn_proc_mesh(trainer_world_size: int, per_generator_world_size: int, host_meshes: HostMeshes | None = None, *, num_generators: int = 1, generator_env: dict[str, str] | None = None)` — [`L188`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L188) — Spawn the trainer and generator proc meshes.

## Module values
- <a id="logger"></a>`logger` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/train.py#L38)

