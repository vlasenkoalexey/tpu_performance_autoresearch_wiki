---
title: 'Module: torchtitan/experiments/tpu/rl_nc_ray/grpo.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/rl_nc_ray/grpo.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.rl_nc_ray.grpo`/
symbols:
  RayController._multi_node: RayController#_multi_node.
  main: main().
  RayController.start_step: RayController#start_step.
  RayController.generator_profiler_config: RayController#generator_profiler_config.
  RayController.__init__: RayController#__init__().
  RayTrainerProxy.__getattr__.MethodProxy.call: RayTrainerProxy#__getattr__().MethodProxy#call().
  FutureProxy._await_internal: FutureProxy#_await_internal().
  RayInterGeneratorRouter.pull_model_state_dict: RayInterGeneratorRouter#pull_model_state_dict().
  RayController.trainer_profiler_config: RayController#trainer_profiler_config.
  RayController.setup_async: RayController#setup_async().
  RayController._proc_meshes: RayController#_proc_meshes.
  RayInterGeneratorRouter.fanout: RayInterGeneratorRouter#fanout().
  RayController: RayController#
  RayInterGeneratorRouter.ray_generator: RayInterGeneratorRouter#ray_generator.
  ValueMeshProxy.get: ValueMeshProxy#get().
  FutureProxy.__await__: FutureProxy#__await__().
  FutureProxy.get: FutureProxy#get().
  RayTrainerProxy.__getattr__: RayTrainerProxy#__getattr__().
  RayInterGeneratorRouter.route: RayInterGeneratorRouter#route().
  RayController.trainer_dp_degree: RayController#trainer_dp_degree.
  ValueMeshProxy.vals: ValueMeshProxy#vals.
  FutureProxy: FutureProxy#
  FutureProxy.obj_refs: FutureProxy#obj_refs.
  MethodProxy.proxy: MethodProxy#proxy.
  RayController.trainer_world_size: RayController#trainer_world_size.
  ValueMeshProxy: ValueMeshProxy#
  RayTrainerProxy: RayTrainerProxy#
  RayTrainerProxy.__getattr__.MethodProxy: RayTrainerProxy#__getattr__().MethodProxy#
  RayInterGeneratorRouter: RayInterGeneratorRouter#
  RayInterGeneratorRouter.trainer_proxy: RayInterGeneratorRouter#trainer_proxy.
  ValueMeshProxy.__init__: ValueMeshProxy#__init__().
  FutureProxy.__init__: FutureProxy#__init__().
  RayTrainerProxy.__init__: RayTrainerProxy#__init__().
  RayTrainerProxy.ray_trainers: RayTrainerProxy#ray_trainers.
  RayTrainerProxy.__getattr__.MethodProxy.__init__: RayTrainerProxy#__getattr__().MethodProxy#__init__().
  RayInterGeneratorRouter.__init__: RayInterGeneratorRouter#__init__().
  RayInterGeneratorRouter.hot_swap: RayInterGeneratorRouter#hot_swap.
  RayController.generator_world_size: RayController#generator_world_size.
---
# Module: [`torchtitan/experiments/tpu/rl_nc_ray/grpo.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py)

## Classes
### <a id="FutureProxy"></a>`FutureProxy`
- def: [`torchtitan/experiments/tpu/rl_nc_ray/grpo.py:49`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L49)
- doc: Mocks the Monarch Future returned by .call()
- signature: `class FutureProxy:`
- members:
  - <a id="FutureProxy.get"></a>`get(self)` — [`L61`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L61)
  - <a id="FutureProxy.obj_refs"></a>`obj_refs` — [`L52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L52)
- protocol/private: <a id="FutureProxy.__await__"></a>`__await__`[`L58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L58), <a id="FutureProxy.__init__"></a>`__init__`[`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L51), <a id="FutureProxy._await_internal"></a>`_await_internal`[`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L54)
- uses (calls/refs, reference-scoped): [`ValueMeshProxy`](grpo.md#ValueMeshProxy)
- used by: [`call`](grpo.md#RayTrainerProxy.__getattr__.MethodProxy.call)

### <a id="RayController"></a>`RayController`  ·  implements/extends Controller
- def: [`torchtitan/experiments/tpu/rl_nc_ray/grpo.py:123`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L123)
- doc: Subclasses the GPU Controller, overriding ONLY setup() to inject Ray.
- signature: `class RayController(Controller):`
- members:
  - <a id="RayController.setup_async"></a>`setup_async(self, **kwargs)` — [`L131`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L131)
  - <a id="RayController.generator_profiler_config"></a>`generator_profiler_config` — [`L129`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L129)
  - <a id="RayController.generator_world_size"></a>`generator_world_size` — [`L141`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L141)
  - <a id="RayController.start_step"></a>`start_step` — [`L237`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L237)
  - <a id="RayController.trainer_dp_degree"></a>`trainer_dp_degree` — [`L142`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L142)
  - <a id="RayController.trainer_profiler_config"></a>`trainer_profiler_config` — [`L128`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L128)
  - <a id="RayController.trainer_world_size"></a>`trainer_world_size` — [`L140`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L140)
- protocol/private: <a id="RayController.__init__"></a>`__init__`[`L126`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L126), <a id="RayController._multi_node"></a>`_multi_node`[`L143`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L143), <a id="RayController._proc_meshes"></a>`_proc_meshes`[`L233`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L233)
- uses (calls/refs, reference-scoped): [`enable`](../../../config/configs.md#CompileConfig.enable), [`trainer`](../../rl/controller.md#Controller.Config.trainer), [`generator`](../../rl/controller.md#Controller.Config.generator), [`Controller`](../../rl/controller.md#Controller), [`Config`](../../rl/controller.md#Controller.Config), [`parallelism`](../../rl/actors/generator.md#VLLMGenerator.Config.parallelism), [`async_loop`](../../rl/controller.md#Controller.Config.async_loop), [`model_spec`](../../rl/controller.md#Controller.Config.model_spec), [`hf_assets_path`](../../rl/controller.md#Controller.Config.hf_assets_path), [`data_parallel_degree`](../../rl/models/vllm_registry.md#InferenceParallelismConfig.data_parallel_degree), [`compile`](../../rl/controller.md#Controller.Config.compile), [`validation`](../../rl/controller.md#AsyncLoopConfig.validation), [`model_dtype`](../../rl/actors/generator.md#VLLMGenerator.Config.model_dtype), [`num_samples`](../../rl/controller.md#ValidationConfig.num_samples), [`trainer`](../../rl/controller.md#Controller.trainer), [`build_generator_env_vars`](tpu_env_utils.md#build_generator_env_vars), [`build_trainer_env_vars`](tpu_env_utils.md#build_trainer_env_vars), [`enable_profiling`](../../../tools/profiler.md#Profiler.Config.enable_profiling), [`generator_router`](../../rl/controller.md#Controller.generator_router), [`max_offpolicy_steps`](../../rl/controller.md#AsyncLoopConfig.max_offpolicy_steps), [`dump_folder`](../../rl/controller.md#Controller.Config.dump_folder), [`config`](../../rl/controller.md#Controller.config), [`dump_folder`](../../rl/actors/trainer.md#PolicyTrainer.Config.dump_folder), [`save_traces_folder`](../../../tools/profiler.md#Profiler.Config.save_traces_folder), [`call`](grpo.md#RayTrainerProxy.__getattr__.MethodProxy.call), [`profiler`](../../rl/actors/generator.md#VLLMGenerator.Config.profiler), [`profiler`](../../rl/actors/trainer.md#PolicyTrainer.Config.profiler), [`pull_model_state_dict`](grpo.md#RayInterGeneratorRouter.pull_model_state_dict), [`RayTPUPolicyTrainer`](trainer.md#RayTPUPolicyTrainer), [`_get_rank_0_value`](../../rl/controller.md#Controller._get_rank_0_value), [`__init__`](../../rl/controller.md#Controller.__init__), [`fanout`](grpo.md#RayInterGeneratorRouter.fanout), [`RayVLLMGenerator`](generator.md#RayVLLMGenerator), [`discover_tpu_cluster_layout`](tpu_env_utils.md#discover_tpu_cluster_layout), [`RayInterGeneratorRouter`](grpo.md#RayInterGeneratorRouter), [`RayTrainerProxy`](grpo.md#RayTrainerProxy)
- used by: [`Controller`](../../rl/controller.md#Controller), [`setup_async`](../../rl/controller.md#Controller.setup_async), [`main`](grpo.md#main)

### <a id="RayInterGeneratorRouter"></a>`RayInterGeneratorRouter`
- def: [`torchtitan/experiments/tpu/rl_nc_ray/grpo.py:89`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L89)
- doc: Mocks the InterGeneratorRouter for Ray
- signature: `class RayInterGeneratorRouter:`
- members:
  - <a id="RayInterGeneratorRouter.fanout"></a>`fanout(self, method, *args, return_exceptions=False, **kwargs)` — [`L101`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L101)
  - <a id="RayInterGeneratorRouter.pull_model_state_dict"></a>`pull_model_state_dict(self, *, policy_version: int)` — [`L110`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L110) — Ray-native weight injection.
  - <a id="RayInterGeneratorRouter.route"></a>`route(self, method, *args, routing_ctx, **kwargs)` — [`L96`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L96)
  - <a id="RayInterGeneratorRouter.hot_swap"></a>`hot_swap` — [`L94`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L94)
  - <a id="RayInterGeneratorRouter.ray_generator"></a>`ray_generator` — [`L92`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L92)
  - <a id="RayInterGeneratorRouter.trainer_proxy"></a>`trainer_proxy` — [`L93`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L93)
- protocol/private: <a id="RayInterGeneratorRouter.__init__"></a>`__init__`[`L91`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L91)
- used by: [`_multi_node`](grpo.md#RayController._multi_node), [`start_step`](grpo.md#RayController.start_step)

### <a id="RayTrainerProxy"></a>`RayTrainerProxy`
- def: [`torchtitan/experiments/tpu/rl_nc_ray/grpo.py:66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L66)
- doc: Mocks the Monarch Actor wrapper for the Trainer
- signature: `class RayTrainerProxy:`
- members:
  - <a id="RayTrainerProxy.ray_trainers"></a>`ray_trainers` — [`L69`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L69)
- protocol/private: <a id="RayTrainerProxy.__getattr__"></a>`__getattr__`[`L71`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L71), <a id="RayTrainerProxy.__init__"></a>`__init__`[`L68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L68)
- uses (calls/refs, reference-scoped): [`MethodProxy`](grpo.md#RayTrainerProxy.__getattr__.MethodProxy)
- used by: [`_multi_node`](grpo.md#RayController._multi_node)

### <a id="RayTrainerProxy.__getattr__.MethodProxy"></a>`RayTrainerProxy.__getattr__.MethodProxy`
- def: [`torchtitan/experiments/tpu/rl_nc_ray/grpo.py:72`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L72)
- signature: `class MethodProxy:`
- members:
  - <a id="RayTrainerProxy.__getattr__.MethodProxy.call"></a>`call(self, *args, **kwargs)` — [`L75`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L75)
- protocol/private: <a id="RayTrainerProxy.__getattr__.MethodProxy.__init__"></a>`__init__`[`L73`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L73)
- uses (calls/refs, reference-scoped): [`FutureProxy`](grpo.md#FutureProxy), [`proxy`](grpo.md#MethodProxy.proxy)
- used by: [`start_step`](grpo.md#RayController.start_step), [`_proc_meshes`](grpo.md#RayController._proc_meshes), [`__getattr__`](grpo.md#RayTrainerProxy.__getattr__)

### <a id="ValueMeshProxy"></a>`ValueMeshProxy`
- def: [`torchtitan/experiments/tpu/rl_nc_ray/grpo.py:39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L39)
- doc: Mocks the Monarch ValueMesh returned by awaiting a future
- signature: `class ValueMeshProxy:`
- members:
  - <a id="ValueMeshProxy.get"></a>`get(self, rank)` — [`L44`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L44)
  - <a id="ValueMeshProxy.vals"></a>`vals` — [`L42`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L42)
- protocol/private: <a id="ValueMeshProxy.__init__"></a>`__init__`[`L41`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L41)
- used by: [`_await_internal`](grpo.md#FutureProxy._await_internal)

## Functions
- <a id="main"></a>`main()` — [`L247`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L247)

## Other members
- <a id="MethodProxy.proxy"></a>`MethodProxy.proxy` — [`L74`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/grpo.py#L74)

