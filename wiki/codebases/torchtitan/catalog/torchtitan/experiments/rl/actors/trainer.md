---
title: 'Module: torchtitan/experiments/rl/actors/trainer.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/actors/trainer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.actors.trainer`/
symbols:
  PolicyTrainer._build_model: PolicyTrainer#_build_model().
  PolicyTrainer.forward_backward: PolicyTrainer#forward_backward().
  PolicyTrainer.optim_step: PolicyTrainer#optim_step().
  PolicyTrainer.Config.training: PolicyTrainer#Config#training.
  PolicyTrainer.Config.parallelism: PolicyTrainer#Config#parallelism.
  PolicyTrainer: PolicyTrainer#
  PolicyTrainer.Config.loss: PolicyTrainer#Config#loss.
  PolicyTrainer.Config: PolicyTrainer#Config#
  PolicyTrainer.Config.optimizer: PolicyTrainer#Config#optimizer.
  PolicyTrainer.checkpointer: PolicyTrainer#checkpointer.
  PolicyTrainer.Config.lr_scheduler: PolicyTrainer#Config#lr_scheduler.
  PolicyTrainer.Config.checkpoint: PolicyTrainer#Config#checkpoint.
  PolicyTrainer.__init__: PolicyTrainer#__init__().
  PolicyTrainer.device: PolicyTrainer#device.
  PolicyTrainer.parallel_dims: PolicyTrainer#parallel_dims.
  PolicyTrainer.train_context: PolicyTrainer#train_context.
  PolicyTrainer.sd_adapter: PolicyTrainer#sd_adapter.
  PolicyTrainer.loss_fn: PolicyTrainer#loss_fn.
  PolicyTrainer.lr_schedulers: PolicyTrainer#lr_schedulers.
  PolicyTrainer.Config.debug: PolicyTrainer#Config#debug.
  PolicyTrainer.model_parts: PolicyTrainer#model_parts.
  PolicyTrainer.Config.ac_config: PolicyTrainer#Config#ac_config.
  PolicyTrainer.optimizers: PolicyTrainer#optimizers.
  PolicyTrainer.reduce_forward_backward_metrics: PolicyTrainer#reduce_forward_backward_metrics().
  PolicyTrainer.push_model_state_dict: PolicyTrainer#push_model_state_dict().
  PolicyTrainer.dp_rank: PolicyTrainer#dp_rank.
  PolicyTrainer.Config.dump_folder: PolicyTrainer#Config#dump_folder.
  PolicyTrainer.Config.override: PolicyTrainer#Config#override.
  PolicyTrainer.policy_version: PolicyTrainer#policy_version.
  PolicyTrainer.dp_enabled: PolicyTrainer#dp_enabled.
  PolicyTrainer._transfer_dtype: PolicyTrainer#_transfer_dtype.
  PolicyTrainer.Config.profiler: PolicyTrainer#Config#profiler.
  PolicyTrainer.save_checkpoint: PolicyTrainer#save_checkpoint().
  logger: logger.
  PolicyTrainer.model: PolicyTrainer#model.
  PolicyTrainer.Config.comm: PolicyTrainer#Config#comm.
  PolicyTrainer.close: PolicyTrainer#close().
  PolicyTrainer.sync_log_step: PolicyTrainer#sync_log_step().
  PolicyTrainer.config: PolicyTrainer#config.
  PolicyTrainer.state_dict: PolicyTrainer#state_dict().
  PolicyTrainer.load_state_dict: PolicyTrainer#load_state_dict().
  PolicyTrainer.get_policy_version: PolicyTrainer#get_policy_version().
  PolicyTrainer.compile_config: PolicyTrainer#compile_config.
  PolicyTrainer.dp_size: PolicyTrainer#dp_size.
  PolicyTrainer.max_num_documents: PolicyTrainer#max_num_documents.
  PolicyTrainer.generator: PolicyTrainer#generator.
---
# Module: [`torchtitan/experiments/rl/actors/trainer.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py)

## Classes
### <a id="PolicyTrainer"></a>`PolicyTrainer`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/actors/trainer.py:48`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L48) — documented in [rl-training](../../../../../concepts/rl-training.md)
- doc: Updates policy based on collected TrainingSample using TorchTitan components.
- signature: `class PolicyTrainer(Actor, Configurable):`
- members:
  - <a id="PolicyTrainer._build_model"></a>`_build_model(self, model_spec: ModelSpec, config: Config, device_type: str)` — [`L249`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L249) — Build, parallelize, and initialize a model with random weights.
  - <a id="PolicyTrainer.close"></a>`close(self)` — [`L238`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L238) — Close actor-local resources before the process mesh stops.
  - <a id="PolicyTrainer.forward_backward"></a>`forward_backward(self, training_data: list[TrainingMicrobatch], num_global_valid_tokens: int)` — [`L348`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L348) — Run forward pass, compute loss, call backward, and reduce metrics.
  - <a id="PolicyTrainer.get_policy_version"></a>`get_policy_version(self)` — [`L232`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L232) — Current policy version: after load(), the step a resume restored from
  - <a id="PolicyTrainer.load_state_dict"></a>`load_state_dict(self, state_dict: dict[str, Any])` — [`L228`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L228)
  - <a id="PolicyTrainer.optim_step"></a>`optim_step(self)` — [`L431`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L431) — Clip gradients, step optimizer + LR scheduler, return updated state.
  - <a id="PolicyTrainer.push_model_state_dict"></a>`push_model_state_dict(self)` — [`L491`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L491) — Stage model weights to a CPU StorageVolume for the generators to pull (TorchStore).
  - <a id="PolicyTrainer.reduce_forward_backward_metrics"></a>`reduce_forward_backward_metrics(self, *, sum_reduced_metrics: dict[str, torch.Tensor], max_reduced_metrics: dict[str, torch.Tensor])` — [`L312`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L312) — Reduce forward/backward metrics across the loss mesh.
  - <a id="PolicyTrainer.save_checkpoint"></a>`save_checkpoint(self, step: int, last_step: bool = False)` — [`L477`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L477) — Save checkpoint via CheckpointManager.
  - <a id="PolicyTrainer.state_dict"></a>`state_dict(self)` — [`L223`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L223)
  - <a id="PolicyTrainer.sync_log_step"></a>`sync_log_step(self, step: int, relative_step: int | None = None)` — [`L308`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L308) — Sync the structured-logger step counter from the controller.
  - <a id="PolicyTrainer.checkpointer"></a>`checkpointer` — [`L191`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L191)
  - <a id="PolicyTrainer.compile_config"></a>`compile_config` — [`L120`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L120)
  - <a id="PolicyTrainer.config"></a>`config` — [`L119`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L119)
  - <a id="PolicyTrainer.device"></a>`device` — [`L133`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L133)
  - <a id="PolicyTrainer.dp_enabled"></a>`dp_enabled` — [`L210`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L210)
  - <a id="PolicyTrainer.dp_rank"></a>`dp_rank` — [`L214`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L214)
  - <a id="PolicyTrainer.dp_size"></a>`dp_size` — [`L213`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L213)
  - <a id="PolicyTrainer.generator"></a>`generator` — [`L207`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L207)
  - <a id="PolicyTrainer.loss_fn"></a>`loss_fn` — [`L122`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L122)
  - <a id="PolicyTrainer.lr_schedulers"></a>`lr_schedulers` — [`L182`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L182)
  - <a id="PolicyTrainer.max_num_documents"></a>`max_num_documents` — [`L121`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L121)
  - <a id="PolicyTrainer.model"></a>`model` — [`L171`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L171)
  - <a id="PolicyTrainer.model_parts"></a>`model_parts` — [`L172`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L172)
  - <a id="PolicyTrainer.optimizers"></a>`optimizers` — [`L181`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L181)
  - <a id="PolicyTrainer.parallel_dims"></a>`parallel_dims` — [`L145`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L145)
  - <a id="PolicyTrainer.policy_version"></a>`policy_version` — [`L187`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L187)
  - <a id="PolicyTrainer.sd_adapter"></a>`sd_adapter` — [`L162`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L162)
  - <a id="PolicyTrainer.train_context"></a>`train_context` — [`L147`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L147)
- protocol/private: <a id="PolicyTrainer.__init__"></a>`__init__`[`L95`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L95), <a id="PolicyTrainer._transfer_dtype"></a>`_transfer_dtype`[`L129`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L129)
- uses (calls/refs, reference-scoped): [`build`](../../../protocols/module.md#Module.Config.build), [`Configurable`](../../../config/configurable.md#Configurable), [`model`](../../../protocols/model_spec.md#ModelSpec.model), [`ParallelDims`](../../../distributed/parallel_dims.md#ParallelDims), [`build`](../../../config/configurable.md#Configurable.Config.build), [`max_context_length`](../../../config/configs.md#TrainingConfig.max_context_length), [`CompileConfig`](../../../config/configs.md#CompileConfig), [`steps`](../../../config/configs.md#TrainingConfig.steps), [`TORCH_DTYPE_MAP`](../../../config/__init__.md#TORCH_DTYPE_MAP), [`FlexInnerAttention`](../../../models/common/attention.md#FlexInnerAttention), [`ChunkedLossWrapper`](../../../components/loss.md#ChunkedLossWrapper), [`ModelSpec`](../../../protocols/model_spec.md#ModelSpec), [`spmd_backend`](../../../config/configs.md#ParallelismConfig.spmd_backend), [`log_trace_span`](../../../observability/structured_logger/structured_logging.md#log_trace_span), [`apply_overrides`](../../../config/override.md#apply_overrides), [`parallelize_fn`](../../../protocols/model_spec.md#ModelSpec.parallelize_fn), [`VarlenInnerAttention`](../../../models/common/attention.md#VarlenInnerAttention), [`get_optional_mesh`](../../../distributed/parallel_dims.md#ParallelDims.get_optional_mesh), [`imports`](../../../config/override.md#OverrideConfig.imports), [`device_type`](../../../tools/utils.md#device_type), [`_build_model`](../../tpu/rl_nc_ray/trainer.md#RayTPUPolicyTrainer._build_model), [`training`](trainer.md#PolicyTrainer.Config.training), [`set_determinism`](../../../distributed/utils.md#set_determinism), [`Config`](../../../models/common/attention.md#FlexInnerAttention.Config), [`parallelism`](trainer.md#PolicyTrainer.Config.parallelism), [`state_dict_adapter`](../../../protocols/model_spec.md#ModelSpec.state_dict_adapter), [`init_distributed`](../../../distributed/utils.md#init_distributed), [`Config`](../../../models/common/attention.md#VarlenInnerAttention.Config), [`ep_enabled`](../../../distributed/parallel_dims.md#ParallelDims.ep_enabled), [`loss`](trainer.md#PolicyTrainer.Config.loss), [`device_module`](../../../tools/utils.md#device_module), [`from_config`](../../../distributed/parallel_dims.md#ParallelDims.from_config), [`Config`](trainer.md#PolicyTrainer.Config), [`init_structured_logger`](../../../observability/structured_logger/structured_logging.md#init_structured_logger), [`optimizer`](trainer.md#PolicyTrainer.Config.optimizer), [`build`](../../../components/optimizer/lr_scheduler.md#LRSchedulersContainer.Config.build), [`checkpoint`](trainer.md#PolicyTrainer.Config.checkpoint), [`lr_scheduler`](trainer.md#PolicyTrainer.Config.lr_scheduler), [`log_trace_instant`](../../../observability/structured_logger/structured_logging.md#log_trace_instant), [`dtype`](../../../config/configs.md#TrainingConfig.dtype)  (+38 more)
- used by: [`Configurable`](../../../config/configurable.md#Configurable), [`_trainer_loop`](../controller.md#Controller._trainer_loop), [`trainer`](../controller.md#Controller.Config.trainer), [`trainer_dp_degree`](../controller.md#Controller.trainer_dp_degree), [`_build_model`](../../tpu/rl_nc_ray/trainer.md#RayTPUPolicyTrainer._build_model), [`close`](../controller.md#Controller.close), [`trainer`](../controller.md#Controller.trainer), [`_load_initial_hf_weights`](../../tpu/rl_nc_ray/trainer.md#RayTPUPolicyTrainer._load_initial_hf_weights), [`profiler`](../../tpu/rl_nc_ray/trainer.md#RayTPUPolicyTrainer.profiler), [`_trainer_push`](../components/weight_sync.md#WeightSyncManager._trainer_push), [`__init__`](../../tpu/rl_nc_ray/trainer.md#RayTPUPolicyTrainer.__init__), [`__init__`](../components/weight_sync.md#WeightSyncManager.__init__), [`get_model_state_dict`](../../tpu/rl_nc_ray/trainer.md#RayTPUPolicyTrainer.get_model_state_dict), [`optim_step`](../../tpu/rl_nc_ray/trainer.md#RayTPUPolicyTrainer.optim_step), [`RayTPUPolicyTrainer`](../../tpu/rl_nc_ray/trainer.md#RayTPUPolicyTrainer)  (18 test-only)

### <a id="PolicyTrainer.Config"></a>`PolicyTrainer.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/actors/trainer.py:65`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L65)
- doc: PolicyTrainer configuration for optimizer, training, and parallelism.
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="PolicyTrainer.Config.ac_config"></a>`ac_config` — [`L79`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L79)
  - <a id="PolicyTrainer.Config.checkpoint"></a>`checkpoint` — [`L82`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L82)
  - <a id="PolicyTrainer.Config.comm"></a>`comm` — [`L76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L76)
  - <a id="PolicyTrainer.Config.debug"></a>`debug` — [`L77`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L77)
  - <a id="PolicyTrainer.Config.dump_folder"></a>`dump_folder` — [`L89`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L89) — ---
  - <a id="PolicyTrainer.Config.loss"></a>`loss` — [`L78`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L78)
  - <a id="PolicyTrainer.Config.lr_scheduler"></a>`lr_scheduler` — [`L71`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L71)
  - <a id="PolicyTrainer.Config.optimizer"></a>`optimizer` — [`L68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L68)
  - <a id="PolicyTrainer.Config.override"></a>`override` — [`L85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L85) — ---
  - <a id="PolicyTrainer.Config.parallelism"></a>`parallelism` — [`L75`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L75)
  - <a id="PolicyTrainer.Config.profiler"></a>`profiler` — [`L92`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L92) — ---
  - <a id="PolicyTrainer.Config.training"></a>`training` — [`L74`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L74)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`ParallelismConfig`](../../../config/configs.md#ParallelismConfig), [`TrainingConfig`](../../../config/configs.md#TrainingConfig), [`CheckpointManager`](../../../components/checkpointer/dcp.md#CheckpointManager), [`LRSchedulersContainer`](../../../components/optimizer/lr_scheduler.md#LRSchedulersContainer), [`Config`](../../../components/checkpointer/dcp.md#CheckpointManager.Config), [`SelectiveAC`](../../../distributed/activation_checkpoint.md#SelectiveAC), [`Config`](../../../components/optimizer/lr_scheduler.md#LRSchedulersContainer.Config), [`Config`](../../../distributed/activation_checkpoint.md#SelectiveAC.Config), [`Config`](../../../config/configurable.md#Configurable.Config), [`ActivationCheckpointingConfig`](../../../distributed/activation_checkpoint.md#ActivationCheckpointingConfig), [`OptimizersContainer`](../../../components/optimizer/optimizer.md#OptimizersContainer), [`Profiler`](../../../tools/profiler.md#Profiler), [`BaseLoss`](../../../components/loss.md#BaseLoss), [`OverrideConfig`](../../../config/override.md#OverrideConfig), [`Config`](../../../tools/profiler.md#Profiler.Config), [`DebugConfig`](../../../config/configs.md#DebugConfig), [`GRPOLoss`](../losses/grpo.md#GRPOLoss), [`Config`](../../../components/optimizer/optimizer.md#OptimizersContainer.Config), [`Config`](../losses/grpo.md#GRPOLoss.Config), [`CommConfig`](../../../config/configs.md#CommConfig), [`Config`](../../../components/loss.md#BaseLoss.Config)
- used by: [`trainer`](../controller.md#Controller.Config.trainer), [`_multi_node`](../../tpu/rl_nc_ray/grpo.md#RayController._multi_node), [`main`](../train.md#main), [`_weight_sync`](../controller.md#Controller._weight_sync), [`_build_model`](trainer.md#PolicyTrainer._build_model), [`forward_backward`](trainer.md#PolicyTrainer.forward_backward), [`optim_step`](trainer.md#PolicyTrainer.optim_step), [`__post_init__`](../controller.md#Controller.Config.__post_init__), [`_build_model`](../../tpu/rl_nc_ray/trainer.md#RayTPUPolicyTrainer._build_model), [`setup_async`](../controller.md#Controller.setup_async), [`checkpointer`](trainer.md#PolicyTrainer.checkpointer), [`__init__`](trainer.md#PolicyTrainer.__init__), [`device`](trainer.md#PolicyTrainer.device), [`parallel_dims`](trainer.md#PolicyTrainer.parallel_dims), [`train_context`](trainer.md#PolicyTrainer.train_context), [`loss_fn`](trainer.md#PolicyTrainer.loss_fn), [`lr_schedulers`](trainer.md#PolicyTrainer.lr_schedulers), [`profiler`](../../tpu/rl_nc_ray/trainer.md#RayTPUPolicyTrainer.profiler), [`optimizers`](trainer.md#PolicyTrainer.optimizers), [`trainer_profiler_config`](../../tpu/rl_nc_ray/grpo.md#RayController.trainer_profiler_config)  (28 test-only)

## Module values
- <a id="logger"></a>`logger` — [`L45`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/trainer.py#L45)

