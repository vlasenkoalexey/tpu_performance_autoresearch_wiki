---
title: 'Module: torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.rl_nc_ray.tpu_env_utils`/
symbols:
  build_trainer_env_vars: build_trainer_env_vars().
  build_generator_env_vars: build_generator_env_vars().
  TRAINER_BASE_PORT: TRAINER_BASE_PORT.
  GENERATOR_BASE_PORT: GENERATOR_BASE_PORT.
  JAX_MEM_FRACTION: JAX_MEM_FRACTION.
  JAX_THREE_G_MEM_ALLOC_ON_FREE: JAX_THREE_G_MEM_ALLOC_ON_FREE.
  XLA_PYTHON_CLIENT_PREALLOCATE: XLA_PYTHON_CLIENT_PREALLOCATE.
  XLA_PYTHON_CLIENT_MEM_FRACTION: XLA_PYTHON_CLIENT_MEM_FRACTION.
  TORCH_DYNAMO_RECOMPILE_LIMIT: TORCH_DYNAMO_RECOMPILE_LIMIT.
  discover_tpu_cluster_layout: discover_tpu_cluster_layout().
  TRAINER_MASTER_PORT: TRAINER_MASTER_PORT.
  VLLM_ENABLE_V1_MULTIPROCESSING: VLLM_ENABLE_V1_MULTIPROCESSING.
  LIBTPU_INIT_ARGS: LIBTPU_INIT_ARGS.
---
# Module: [`torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py)

## Functions
- <a id="build_generator_env_vars"></a>`build_generator_env_vars(layout: dict, worker_pythonpath: str, dump_folder: str = None, **kwargs)` — [`L183`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py#L183) — Build environment variables dictionary for the generator.
- <a id="build_trainer_env_vars"></a>`build_trainer_env_vars(rank: int, layout: dict, worker_pythonpath: str)` — [`L101`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py#L101) — Build environment variables dictionary for the given trainer rank.
- <a id="discover_tpu_cluster_layout"></a>`discover_tpu_cluster_layout(config)` — [`L37`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py#L37) — Query Ray nodes to discover physical TPU node topology, host bounds, and worker arrangements.

## Module values
- <a id="GENERATOR_BASE_PORT"></a>`GENERATOR_BASE_PORT` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py#L26)
- <a id="JAX_MEM_FRACTION"></a>`JAX_MEM_FRACTION` — [`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py#L28)
- <a id="JAX_THREE_G_MEM_ALLOC_ON_FREE"></a>`JAX_THREE_G_MEM_ALLOC_ON_FREE` — [`L29`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py#L29)
- <a id="LIBTPU_INIT_ARGS"></a>`LIBTPU_INIT_ARGS` — [`L32`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py#L32)
- <a id="TORCH_DYNAMO_RECOMPILE_LIMIT"></a>`TORCH_DYNAMO_RECOMPILE_LIMIT` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py#L34)
- <a id="TRAINER_BASE_PORT"></a>`TRAINER_BASE_PORT` — [`L25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py#L25)
- <a id="TRAINER_MASTER_PORT"></a>`TRAINER_MASTER_PORT` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py#L24)
- <a id="VLLM_ENABLE_V1_MULTIPROCESSING"></a>`VLLM_ENABLE_V1_MULTIPROCESSING` — [`L33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py#L33)
- <a id="XLA_PYTHON_CLIENT_MEM_FRACTION"></a>`XLA_PYTHON_CLIENT_MEM_FRACTION` — [`L31`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py#L31)
- <a id="XLA_PYTHON_CLIENT_PREALLOCATE"></a>`XLA_PYTHON_CLIENT_PREALLOCATE` — [`L30`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py#L30)

