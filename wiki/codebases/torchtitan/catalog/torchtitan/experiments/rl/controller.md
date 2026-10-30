---
title: 'Module: torchtitan/experiments/rl/controller.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/controller.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.controller`/
symbols:
  Controller._trainer_loop: Controller#_trainer_loop().
  Controller.Config.trainer: Controller#Config#trainer.
  Controller.trainer_dp_degree: Controller#trainer_dp_degree.
  Controller.Config.generator: Controller#Config#generator.
  Controller: Controller#
  Controller._weight_sync: Controller#_weight_sync.
  Controller.Config: Controller#Config#
  Controller._rollout_loop: Controller#_rollout_loop().
  Controller.Config.__post_init__: Controller#Config#__post_init__().
  AsyncLoopConfig: AsyncLoopConfig#
  Controller.Config.async_loop: Controller#Config#async_loop.
  Controller.Config.model_spec: Controller#Config#model_spec.
  Controller.close: Controller#close().
  AsyncLoopConfig.num_prompts_per_train_step: AsyncLoopConfig#num_prompts_per_train_step.
  Controller.Config.hf_assets_path: Controller#Config#hf_assets_path.
  Controller._collect_validation_rollouts: Controller#_collect_validation_rollouts().
  Controller.setup_async: Controller#setup_async().
  Controller.Config.compile: Controller#Config#compile.
  Controller.validate: Controller#validate().
  Controller._data_input_loop: Controller#_data_input_loop().
  Controller._batcher_loop: Controller#_batcher_loop().
  AsyncLoopConfig.validation: AsyncLoopConfig#validation.
  ValidationConfig: ValidationConfig#
  Controller.Config.rollouter: Controller#Config#rollouter.
  Controller.Config.metrics: Controller#Config#metrics.
  Controller.Config.renderer: Controller#Config#renderer.
  logger: logger.
  ValidationConfig.num_samples: ValidationConfig#num_samples.
  Controller.trainer: Controller#trainer.
  AsyncLoopConfig.num_samples_per_prompt: AsyncLoopConfig#num_samples_per_prompt.
  AsyncLoopConfig.window_fraction: AsyncLoopConfig#window_fraction.
  Controller.run: Controller#run().
  AsyncLoopConfig.num_training_steps: AsyncLoopConfig#num_training_steps.
  AsyncLoopConfig.target_offpolicy_steps: AsyncLoopConfig#target_offpolicy_steps.
  Controller.metrics_processor: Controller#metrics_processor.
  Controller.generator_router: Controller#generator_router.
  Controller._sampling: Controller#_sampling.
  Controller._rollouter: Controller#_rollouter.
  Controller._trainer_policy_version: Controller#_trainer_policy_version.
  Controller._validate_and_log: Controller#_validate_and_log().
  AsyncLoopConfig.window_size: AsyncLoopConfig#window_size().
  AsyncLoopConfig.max_offpolicy_steps: AsyncLoopConfig#max_offpolicy_steps().
  AsyncLoopConfig.max_active_rollout_groups: AsyncLoopConfig#max_active_rollout_groups().
  Controller.Config.dump_folder: Controller#Config#dump_folder.
  Controller.Config.generator_router: Controller#Config#generator_router.
  AsyncLoopConfig.training_sample_builder: AsyncLoopConfig#training_sample_builder.
  Controller.generate: Controller#generate().
  Controller._group_buffer: Controller#_group_buffer.
  AsyncLoopConfig.__post_init__: AsyncLoopConfig#__post_init__().
  Controller.config: Controller#config.
  Controller.tokenizer: Controller#tokenizer.
  Controller.rollout_recorder: Controller#rollout_recorder.
  Controller._make_generate_fn: Controller#_make_generate_fn().
  AsyncLoopConfig.batcher: AsyncLoopConfig#batcher.
  Controller._proc_meshes: Controller#_proc_meshes.
  Controller.renderer: Controller#renderer.
  Controller.Config.tokenizer: Controller#Config#tokenizer.
  Controller.Config.num_generators: Controller#Config#num_generators.
  Controller.start_step: Controller#start_step.
  AsyncLoopConfig.group_buffer: AsyncLoopConfig#group_buffer.
  Controller.Config.rollout_recorder: Controller#Config#rollout_recorder.
  Controller._get_rank_0_value: Controller#_get_rank_0_value().
  Controller.__init__: Controller#__init__().
  Controller._log_reward_delta: Controller#_log_reward_delta().
---
# Module: [`torchtitan/experiments/rl/controller.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py)

## Classes
### <a id="AsyncLoopConfig"></a>`AsyncLoopConfig`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/controller.py:155`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L155) — documented in [rl-training](../../../../concepts/rl-training.md)
- signature: `class AsyncLoopConfig(Configurable.Config):`
- members:
  - <a id="AsyncLoopConfig.max_active_rollout_groups"></a>`max_active_rollout_groups(self)` — [`L220`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L220)
  - <a id="AsyncLoopConfig.max_offpolicy_steps"></a>`max_offpolicy_steps(self)` — [`L246`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L246) — Return the worst case consume-time offpolicy bound.
  - <a id="AsyncLoopConfig.window_size"></a>`window_size(self)` — [`L224`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L224) — Derive the fixed FIFO look-ahead window from the configured fraction.
  - <a id="AsyncLoopConfig.batcher"></a>`batcher` — [`L190`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L190)
  - <a id="AsyncLoopConfig.group_buffer"></a>`group_buffer` — [`L184`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L184)
  - <a id="AsyncLoopConfig.num_prompts_per_train_step"></a>`num_prompts_per_train_step` — [`L159`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L159) — ---
  - <a id="AsyncLoopConfig.num_samples_per_prompt"></a>`num_samples_per_prompt` — [`L163`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L163) — ---
  - <a id="AsyncLoopConfig.num_training_steps"></a>`num_training_steps` — [`L156`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L156) — ---
  - <a id="AsyncLoopConfig.target_offpolicy_steps"></a>`target_offpolicy_steps` — [`L166`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L166) — ---
  - <a id="AsyncLoopConfig.training_sample_builder"></a>`training_sample_builder` — [`L187`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L187)
  - <a id="AsyncLoopConfig.validation"></a>`validation` — [`L191`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L191)
  - <a id="AsyncLoopConfig.window_fraction"></a>`window_fraction` — [`L175`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L175) — ---
- protocol/private: <a id="AsyncLoopConfig.__post_init__"></a>`__post_init__`[`L193`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L193)
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`Config`](../../config/configurable.md#Configurable.Config), [`ValidationConfig`](controller.md#ValidationConfig), [`RolloutGroupWorkBuffer`](components/work_buffer.md#RolloutGroupWorkBuffer), [`Batcher`](components/batcher.md#Batcher), [`Config`](components/batcher.md#Batcher.Config), [`TrainingSampleBuilder`](components/training_sample_builder.md#TrainingSampleBuilder), [`Config`](components/training_sample_builder.md#TrainingSampleBuilder.Config), [`Config`](components/work_buffer.md#RolloutGroupWorkBuffer.Config)
- used by: [`_trainer_loop`](controller.md#Controller._trainer_loop), [`trainer_dp_degree`](controller.md#Controller.trainer_dp_degree), [`_multi_node`](../tpu/rl_nc_ray/grpo.md#RayController._multi_node), [`_weight_sync`](controller.md#Controller._weight_sync), [`_rollout_loop`](controller.md#Controller._rollout_loop), [`async_loop`](controller.md#Controller.Config.async_loop), [`setup_async`](controller.md#Controller.setup_async), [`validate`](controller.md#Controller.validate), [`run`](controller.md#Controller.run), [`_trainer_policy_version`](controller.md#Controller._trainer_policy_version), [`_group_buffer`](controller.md#Controller._group_buffer)  (23 test-only)

### <a id="Controller"></a>`Controller`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/controller.py:260`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L260) — documented in [rl-training](../../../../concepts/rl-training.md)
- doc: Top-level RL async training orchestrator.
- signature: `class Controller(Configurable):`
- members:
  - <a id="Controller._batcher_loop"></a>`_batcher_loop(self, *, group_buffer: RolloutGroupWorkBuffer, training_sample_builder: TrainingSampleBuilder, batcher: Batcher, training_batch_queue: asyncio.Queue[TrainingBatch | None])` — [`L999`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L999) — Take finalized groups, build training_samples, accumulate them, and queue each ready training batch.
  - <a id="Controller._collect_validation_rollouts"></a>`_collect_validation_rollouts(self, *, num_groups: int, sampling: SamplingConfig, step: int)` — [`L683`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L683) — Sample held-out prompts, run each greedily (n=1) concurrently, and emit validation metrics.
  - <a id="Controller._data_input_loop"></a>`_data_input_loop(self, group_buffer: RolloutGroupWorkBuffer)` — [`L920`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L920) — produces a RolloutGroupWork into group_buffer.
  - <a id="Controller._get_rank_0_value"></a>`_get_rank_0_value(self, result)` — [`L495`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L495) — Extract rank 0 result from a Monarch ValueMesh.
  - <a id="Controller._log_reward_delta"></a>`_log_reward_delta(self, pre: dict[str, float], post: dict[str, float])` — [`L909`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L909) — Console pre/post reward summary, visible without scrolling back through the loop.
  - <a id="Controller._make_generate_fn"></a>`_make_generate_fn(self, metrics_prefix: str)` — [`L504`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L504) — Build the rollouter's `GenerateFn`: route a completion via the generator router, namespacing
  - <a id="Controller._rollout_loop"></a>`_rollout_loop(self, *, group_buffer: RolloutGroupWorkBuffer, generate_fn: GenerateFn)` — [`L949`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L949) — Generate + score one group at a time; a failed group becomes an empty group + a failure metric. — documented in [rl-training](../../../../concepts/rl-training.md)
  - <a id="Controller._trainer_loop"></a>`_trainer_loop(self, training_batch_queue: asyncio.Queue[TrainingBatch | None], *, num_training_steps: int)` — [`L1043`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L1043) — Run num_training_steps optimizer steps: train one packed batch, publish trainer weights,
  - <a id="Controller._validate_and_log"></a>`_validate_and_log(self, *, step: int)` — [`L903`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L903) — Run one validation pass, log it, and return its aggregated values for the pre/post delta.
  - <a id="Controller.close"></a>`close(self)` — [`L450`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L450) — Best-effort: tear down actors, close metric backends, then stop proc meshes.
  - <a id="Controller.generate"></a>`generate(prompt_token_ids: list[int], *, request_id: str, routing_session_id: str | None = None, sampling_config: SamplingConfig | None = None)` — [`L515`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L515)
  - <a id="Controller.run"></a>`run(self)` — [`L762`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L762) — Start every async loop and run until training completes or a stage crashes.
  - <a id="Controller.setup_async"></a>`setup_async(self, *, trainer_mesh: ProcMesh, generator_meshes: list[ProcMesh])` — [`L533`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L533) — Spawn Monarch actors on separate meshes and initialize weights.
  - <a id="Controller.validate"></a>`validate(self, *, step: int)` — [`L734`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L734) — Run greedy validation on held-out prompts.
  - <a id="Controller.config"></a>`config` — [`L424`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L424)
  - <a id="Controller.generator_router"></a>`generator_router` — [`L426`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L426)
  - <a id="Controller.metrics_processor"></a>`metrics_processor` — [`L430`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L430)
  - <a id="Controller.renderer"></a>`renderer` — [`L435`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L435)
  - <a id="Controller.rollout_recorder"></a>`rollout_recorder` — [`L446`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L446)
  - <a id="Controller.start_step"></a>`start_step` — [`L428`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L428)
  - <a id="Controller.tokenizer"></a>`tokenizer` — [`L434`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L434)
  - <a id="Controller.trainer"></a>`trainer` — [`L425`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L425)
  - <a id="Controller.trainer_dp_degree"></a>`trainer_dp_degree` — [`L569`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L569) — documented in [rl-training](../../../../concepts/rl-training.md)
- protocol/private: <a id="Controller.__init__"></a>`__init__`[`L423`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L423), <a id="Controller._group_buffer"></a>`_group_buffer`[`L794`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L794), <a id="Controller._proc_meshes"></a>`_proc_meshes`[`L429`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L429), <a id="Controller._rollouter"></a>`_rollouter`[`L445`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L445), <a id="Controller._sampling"></a>`_sampling`[`L440`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L440), <a id="Controller._trainer_policy_version"></a>`_trainer_policy_version`[`L785`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L785), <a id="Controller._weight_sync"></a>`_weight_sync`[`L800`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L800)
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`build`](../../config/configurable.md#Configurable.Config.build), [`max_context_length`](../../config/configs.md#TrainingConfig.max_context_length), [`num_tokens_per_microbatch_per_dp_rank`](../../config/configs.md#TrainingConfig.num_tokens_per_microbatch_per_dp_rank), [`Metric`](observability/metrics/types.md#Metric), [`data_parallel_shard_degree`](../../config/configs.md#ParallelismConfig.data_parallel_shard_degree), [`MetricsProcessor`](observability/metrics/processor.md#MetricsProcessor), [`trainer`](controller.md#Controller.Config.trainer), [`build_from_group`](components/training_sample_builder.md#TrainingSampleBuilder.build_from_group), [`generator`](controller.md#Controller.Config.generator), [`log_trace_span`](../../observability/structured_logger/structured_logging.md#log_trace_span), [`Config`](controller.md#Controller.Config), [`_aggregate_metrics`](observability/metrics/processor.md#MetricsProcessor._aggregate_metrics), [`forward_backward`](actors/trainer.md#PolicyTrainer.forward_backward), [`SamplingConfig`](actors/generator.md#SamplingConfig), [`optim_step`](actors/trainer.md#PolicyTrainer.optim_step), [`compute_rollout_metrics`](controller_metrics.md#compute_rollout_metrics), [`parallelism`](actors/generator.md#VLLMGenerator.Config.parallelism), [`add_training_samples`](components/batcher.md#Batcher.add_training_samples), [`NoReduce`](observability/metrics/types.md#NoReduce), [`VLLMGenerator`](actors/generator.md#VLLMGenerator), [`training`](actors/trainer.md#PolicyTrainer.Config.training), [`RolloutGroup`](rollout/types.md#RolloutGroup), [`parallelism`](actors/trainer.md#PolicyTrainer.Config.parallelism), [`async_loop`](controller.md#Controller.Config.async_loop), [`PolicyTrainer`](actors/trainer.md#PolicyTrainer), [`model_spec`](controller.md#Controller.Config.model_spec), [`Rollouter`](rollout/rollouter.md#Rollouter), [`log`](observability/metrics/processor.md#MetricsProcessor.log), [`data_parallel_replicate_degree`](../../config/configs.md#ParallelismConfig.data_parallel_replicate_degree), [`hf_assets_path`](controller.md#Controller.Config.hf_assets_path), [`num_prompts_per_train_step`](controller.md#AsyncLoopConfig.num_prompts_per_train_step), [`take_finalized`](components/work_buffer.md#RolloutGroupWorkBuffer.take_finalized), [`setup_async`](rollout/rollouter.md#Rollouter.setup_async), [`data_parallel_degree`](models/vllm_registry.md#InferenceParallelismConfig.data_parallel_degree), [`compile`](controller.md#Controller.Config.compile), [`InterGeneratorRouter`](routing/inter_generator_router.md#InterGeneratorRouter), [`validation`](controller.md#AsyncLoopConfig.validation), [`Completion`](types.md#Completion), [`metrics`](controller.md#Controller.Config.metrics)  (+72 more)
- used by: [`Configurable`](../../config/configurable.md#Configurable), [`_multi_node`](../tpu/rl_nc_ray/grpo.md#RayController._multi_node), [`main`](train.md#main), [`main`](../tpu/rl_nc_ray/grpo.md#main), [`start_step`](../tpu/rl_nc_ray/grpo.md#RayController.start_step), [`__init__`](../tpu/rl_nc_ray/grpo.md#RayController.__init__), [`setup_async`](../tpu/rl_nc_ray/grpo.md#RayController.setup_async), [`_proc_meshes`](../tpu/rl_nc_ray/grpo.md#RayController._proc_meshes), [`RayController`](../tpu/rl_nc_ray/grpo.md#RayController)  (39 test-only)

### <a id="Controller.Config"></a>`Controller.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/controller.py:281`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L281)
- doc: Top-level config for RL training.
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="Controller.Config.async_loop"></a>`async_loop` — [`L294`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L294) — ---
  - <a id="Controller.Config.compile"></a>`compile` — [`L315`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L315) — ---
  - <a id="Controller.Config.dump_folder"></a>`dump_folder` — [`L291`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L291) — ---
  - <a id="Controller.Config.generator"></a>`generator` — [`L324`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L324) — ---
  - <a id="Controller.Config.generator_router"></a>`generator_router` — [`L335`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L335) — ---
  - <a id="Controller.Config.hf_assets_path"></a>`hf_assets_path` — [`L288`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L288) — ---
  - <a id="Controller.Config.metrics"></a>`metrics` — [`L341`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L341)
  - <a id="Controller.Config.model_spec"></a>`model_spec` — [`L284`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L284) — ---
  - <a id="Controller.Config.num_generators"></a>`num_generators` — [`L327`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L327) — ---
  - <a id="Controller.Config.renderer"></a>`renderer` — [`L306`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L306) — ---
  - <a id="Controller.Config.rollout_recorder"></a>`rollout_recorder` — [`L310`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L310) — ---
  - <a id="Controller.Config.rollouter"></a>`rollouter` — [`L297`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L297) — ---
  - <a id="Controller.Config.tokenizer"></a>`tokenizer` — [`L301`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L301) — ---
  - <a id="Controller.Config.trainer"></a>`trainer` — [`L318`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L318) — ---
- protocol/private: <a id="Controller.Config.__post_init__"></a>`__post_init__`[`L345`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L345)
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`max_context_length`](../../config/configs.md#TrainingConfig.max_context_length), [`CompileConfig`](../../config/configs.md#CompileConfig), [`ModelSpec`](../../protocols/model_spec.md#ModelSpec), [`tensor_parallel_degree`](../../config/configs.md#ParallelismConfig.tensor_parallel_degree), [`MetricsProcessor`](observability/metrics/processor.md#MetricsProcessor), [`Config`](../../config/configurable.md#Configurable.Config), [`enable`](../../components/checkpointer/base.md#BaseCheckpointManager.Config.enable), [`HuggingFaceTokenizer`](../../components/tokenizer.md#HuggingFaceTokenizer), [`VLLMGenerator`](actors/generator.md#VLLMGenerator), [`Config`](observability/metrics/processor.md#MetricsProcessor.Config), [`mixed_precision_param`](../../config/configs.md#TrainingConfig.mixed_precision_param), [`training`](actors/trainer.md#PolicyTrainer.Config.training), [`AsyncLoopConfig`](controller.md#AsyncLoopConfig), [`parallelism`](actors/trainer.md#PolicyTrainer.Config.parallelism), [`PolicyTrainer`](actors/trainer.md#PolicyTrainer), [`Rollouter`](rollout/rollouter.md#Rollouter), [`loss`](actors/trainer.md#PolicyTrainer.Config.loss), [`Config`](actors/generator.md#VLLMGenerator.Config), [`Config`](actors/trainer.md#PolicyTrainer.Config), [`checkpoint`](actors/generator.md#VLLMGenerator.Config.checkpoint), [`InterGeneratorRouter`](routing/inter_generator_router.md#InterGeneratorRouter), [`RendererConfig`](renderer.md#RendererConfig), [`model_dtype`](actors/generator.md#VLLMGenerator.Config.model_dtype), [`num_tokens_per_train_step`](../../config/configs.md#TrainingConfig.num_tokens_per_train_step), [`GRPOLoss`](losses/grpo.md#GRPOLoss), [`Config`](losses/grpo.md#GRPOLoss.Config), [`Config`](../../components/tokenizer.md#HuggingFaceTokenizer.Config), [`enable_sequence_parallel`](../../config/configs.md#ParallelismConfig.enable_sequence_parallel), [`Config`](rollout_recorder.md#RolloutSampleRecorder.Config), [`Config`](routing/inter_generator_router.md#InterGeneratorRouter.Config), [`deterministic`](../../config/configs.md#DebugConfig.deterministic), [`debug`](actors/trainer.md#PolicyTrainer.Config.debug), [`Config`](rollout/rollouter.md#Rollouter.Config), [`batch_invariant`](../../config/configs.md#DebugConfig.batch_invariant), [`RolloutSampleRecorder`](rollout_recorder.md#RolloutSampleRecorder), [`reset_prefix_cache_on_weight_sync`](actors/generator.md#VLLMGenerator.Config.reset_prefix_cache_on_weight_sync), [`hot_swap`](routing/inter_generator_router.md#InterGeneratorRouter.Config.hot_swap)
- used by: [`_trainer_loop`](controller.md#Controller._trainer_loop), [`trainer_dp_degree`](controller.md#Controller.trainer_dp_degree), [`_multi_node`](../tpu/rl_nc_ray/grpo.md#RayController._multi_node), [`main`](train.md#main), [`_weight_sync`](controller.md#Controller._weight_sync), [`_rollout_loop`](controller.md#Controller._rollout_loop), [`setup_async`](controller.md#Controller.setup_async), [`validate`](controller.md#Controller.validate), [`main`](../tpu/rl_nc_ray/grpo.md#main), [`run`](controller.md#Controller.run), [`metrics_processor`](controller.md#Controller.metrics_processor), [`_rollouter`](controller.md#Controller._rollouter), [`_sampling`](controller.md#Controller._sampling), [`rollout_recorder`](controller.md#Controller.rollout_recorder), [`tokenizer`](controller.md#Controller.tokenizer), [`renderer`](controller.md#Controller.renderer), [`generator_profiler_config`](../tpu/rl_nc_ray/grpo.md#RayController.generator_profiler_config), [`__init__`](../tpu/rl_nc_ray/grpo.md#RayController.__init__), [`trainer_profiler_config`](../tpu/rl_nc_ray/grpo.md#RayController.trainer_profiler_config), [`__init__`](controller.md#Controller.__init__)  (37 test-only)

### <a id="ValidationConfig"></a>`ValidationConfig`
- def: [`torchtitan/experiments/rl/controller.py:145`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L145)
- doc: Held-out validation that runs at the start and end of training
- signature: `class ValidationConfig:`
- members:
  - <a id="ValidationConfig.num_samples"></a>`num_samples` — [`L150`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L150) — ---
- used by: [`_multi_node`](../tpu/rl_nc_ray/grpo.md#RayController._multi_node), [`setup_async`](controller.md#Controller.setup_async), [`validate`](controller.md#Controller.validate), [`validation`](controller.md#AsyncLoopConfig.validation)  (19 test-only)

## Module values
- <a id="logger"></a>`logger` — [`L141`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller.py#L141)

