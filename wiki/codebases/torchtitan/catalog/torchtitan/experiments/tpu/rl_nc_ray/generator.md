---
title: 'Module: torchtitan/experiments/tpu/rl_nc_ray/generator.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/rl_nc_ray/generator.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.rl_nc_ray.generator`/
symbols:
  RayVLLMGenerator.sync_log_step: RayVLLMGenerator#sync_log_step().
  RayVLLMGenerator.load_model_state_dict: RayVLLMGenerator#load_model_state_dict().
  RayVLLMGenerator.generator: RayVLLMGenerator#generator.
  RayVLLMGenerator.__init__: RayVLLMGenerator#__init__().
  patch_vllm_for_tpu: patch_vllm_for_tpu().
  patch_vllm_for_tpu.patched_initialize_worker: patch_vllm_for_tpu().patched_initialize_worker().
  RayVLLMGenerator.__init__.CustomModelStateDictPullRequest.refs: RayVLLMGenerator#__init__().CustomModelStateDictPullRequest#refs.
  RayVLLMGenerator.close: RayVLLMGenerator#close().
  patch_vllm_for_tpu.patched_initialize_worker.load_weights_from_state_dict_on_worker: patch_vllm_for_tpu().patched_initialize_worker().load_weights_from_state_dict_on_worker().
  VLLM_ARGS_PATH: VLLM_ARGS_PATH.
  RayVLLMGenerator.stop_profile: RayVLLMGenerator#stop_profile().
  logger: logger.
  RayVLLMGenerator._is_profiling: RayVLLMGenerator#_is_profiling.
  RayVLLMGenerator.start_profile: RayVLLMGenerator#start_profile().
  RayVLLMGenerator.profiler_config: RayVLLMGenerator#profiler_config.
  RayVLLMGenerator.generate: RayVLLMGenerator#generate().
  RayVLLMGenerator.start_engine_loop: RayVLLMGenerator#start_engine_loop().
  RayVLLMGenerator.custom_pull: RayVLLMGenerator#custom_pull().
  RayVLLMGenerator._is_profiling_step: RayVLLMGenerator#_is_profiling_step().
  RayVLLMGenerator: RayVLLMGenerator#
  VLLM_ARGS_PATH_LOCAL: VLLM_ARGS_PATH_LOCAL.
  VLLM_ARGS_PATH_REMOTE: VLLM_ARGS_PATH_REMOTE.
  patch_vllm_for_tpu.patched_driver_environ_setitem: patch_vllm_for_tpu().patched_driver_environ_setitem().
  patch_vllm_for_tpu.patched_ray_nodes: patch_vllm_for_tpu().patched_ray_nodes().
  patch_vllm_for_tpu.patched_cluster_resources: patch_vllm_for_tpu().patched_cluster_resources().
  patch_vllm_for_tpu._get_worker_rank: patch_vllm_for_tpu()._get_worker_rank().
  RayVLLMGenerator.__init__.CustomModelStateDictPullRequest: RayVLLMGenerator#__init__().CustomModelStateDictPullRequest#
  RayVLLMGenerator.__init__.CustomModelStateDictPullRequest.version: RayVLLMGenerator#__init__().CustomModelStateDictPullRequest#version.
---
# Module: [`torchtitan/experiments/tpu/rl_nc_ray/generator.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py)

## Classes
### <a id="RayVLLMGenerator"></a>`RayVLLMGenerator`
- def: [`torchtitan/experiments/tpu/rl_nc_ray/generator.py:194`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L194)
- signature: `class RayVLLMGenerator:`
- members:
  - <a id="RayVLLMGenerator.close"></a>`close(self)` — [`L325`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L325)
  - <a id="RayVLLMGenerator.custom_pull"></a>`custom_pull(gen_self, version)` — [`L239`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L239)
  - <a id="RayVLLMGenerator.generate"></a>`generate(self, *args, **kwargs)` — [`L304`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L304)
  - <a id="RayVLLMGenerator.load_model_state_dict"></a>`load_model_state_dict(self, version: int, state_dict_ref_list: list)` — [`L331`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L331) — Queue Ray-native weight injection into engine loop.
  - <a id="RayVLLMGenerator.start_engine_loop"></a>`start_engine_loop(self)` — [`L307`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L307)
  - <a id="RayVLLMGenerator.start_profile"></a>`start_profile(self, profile_prefix: str | None = None)` — [`L349`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L349)
  - <a id="RayVLLMGenerator.stop_profile"></a>`stop_profile(self)` — [`L353`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L353)
  - <a id="RayVLLMGenerator.sync_log_step"></a>`sync_log_step(self, step: int, relative_step: int | None = None)` — [`L310`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L310)
  - <a id="RayVLLMGenerator.generator"></a>`generator` — [`L283`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L283)
  - <a id="RayVLLMGenerator.profiler_config"></a>`profiler_config` — [`L272`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L272)
- protocol/private: <a id="RayVLLMGenerator.__init__"></a>`__init__`[`L195`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L195), <a id="RayVLLMGenerator._is_profiling"></a>`_is_profiling`[`L273`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L273), <a id="RayVLLMGenerator._is_profiling_step"></a>`_is_profiling_step`[`L292`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L292)
- uses (calls/refs, reference-scoped): [`VLLMGenerator`](../../rl/actors/generator.md#VLLMGenerator), [`generate`](../../rl/actors/generator.md#VLLMGenerator.generate), [`_pull_model_state_dict`](../../rl/actors/generator.md#VLLMGenerator._pull_model_state_dict), [`close`](../../rl/actors/generator.md#VLLMGenerator.close), [`_engine`](../../rl/actors/generator.md#VLLMGenerator._engine), [`load_weights_on_driver`](weight_transfer_utils.md#load_weights_on_driver), [`patch_vllm_for_tpu`](generator.md#patch_vllm_for_tpu), [`_model_state_dict_pull_request`](../../rl/actors/generator.md#VLLMGenerator._model_state_dict_pull_request), [`_engine_loop_condition`](../../rl/actors/generator.md#VLLMGenerator._engine_loop_condition), [`_pull_model_state_dict_future`](../../rl/actors/generator.md#VLLMGenerator._pull_model_state_dict_future), [`ModelStateDictPullRequest`](../../rl/actors/generator.md#ModelStateDictPullRequest), [`_rank0_check_engine_loop_running`](../../rl/actors/generator.md#VLLMGenerator._rank0_check_engine_loop_running), [`VLLM_ARGS_PATH`](generator.md#VLLM_ARGS_PATH), [`logger`](generator.md#logger), [`start_engine_loop`](../../rl/actors/generator.md#VLLMGenerator.start_engine_loop), [`version`](../../rl/actors/generator.md#ModelStateDictPullRequest.version), [`sync_log_step`](../../rl/actors/generator.md#VLLMGenerator.sync_log_step)
- used by: [`_multi_node`](grpo.md#RayController._multi_node)

### <a id="RayVLLMGenerator.__init__.CustomModelStateDictPullRequest"></a>`RayVLLMGenerator.__init__.CustomModelStateDictPullRequest`
- def: [`torchtitan/experiments/tpu/rl_nc_ray/generator.py:230`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L230)
- signature: `class CustomModelStateDictPullRequest:`
- members:
  - <a id="RayVLLMGenerator.__init__.CustomModelStateDictPullRequest.refs"></a>`refs` — [`L232`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L232)
  - <a id="RayVLLMGenerator.__init__.CustomModelStateDictPullRequest.version"></a>`version` — [`L231`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L231)
- uses (calls/refs, reference-scoped): [`VLLMGenerator`](../../rl/actors/generator.md#VLLMGenerator), [`_pull_model_state_dict`](../../rl/actors/generator.md#VLLMGenerator._pull_model_state_dict), [`ModelStateDictPullRequest`](../../rl/actors/generator.md#ModelStateDictPullRequest)

## Functions
- <a id="patch_vllm_for_tpu._get_worker_rank"></a>`_get_worker_rank(worker_obj)` — [`L95`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L95)
- <a id="patch_vllm_for_tpu.patched_initialize_worker.load_weights_from_state_dict_on_worker"></a>`load_weights_from_state_dict_on_worker(self, state_dict)` — [`L136`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L136)
- <a id="patch_vllm_for_tpu"></a>`patch_vllm_for_tpu(vllm_args_path: str)` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L39) — Apply TPU-specific patches and workarounds to vLLM and torchtpu-vllm workers.
- <a id="patch_vllm_for_tpu.patched_cluster_resources"></a>`patched_cluster_resources(*args, **kwargs)` — [`L80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L80)
- <a id="patch_vllm_for_tpu.patched_driver_environ_setitem"></a>`patched_driver_environ_setitem(self, key, value)` — [`L59`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L59)
- <a id="patch_vllm_for_tpu.patched_initialize_worker"></a>`patched_initialize_worker(self, local_rank, env_vars=None, driver_env_vars=None, *args, **kwargs)` — [`L112`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L112)
- <a id="patch_vllm_for_tpu.patched_ray_nodes"></a>`patched_ray_nodes(*args, **kwargs)` — [`L74`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L74)

## Module values
- <a id="VLLM_ARGS_PATH"></a>`VLLM_ARGS_PATH` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L36)
- <a id="VLLM_ARGS_PATH_LOCAL"></a>`VLLM_ARGS_PATH_LOCAL` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L34)
- <a id="VLLM_ARGS_PATH_REMOTE"></a>`VLLM_ARGS_PATH_REMOTE` — [`L35`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L35)
- <a id="logger"></a>`logger` — [`L30`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/generator.py#L30)

