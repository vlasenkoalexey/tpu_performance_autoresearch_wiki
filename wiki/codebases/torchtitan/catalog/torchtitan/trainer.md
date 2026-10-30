---
title: 'Module: torchtitan/trainer.py'
type: catalog
provenance: extracted
module: torchtitan/trainer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.trainer`/Trainer#
symbols:
  Trainer.Config.parallelism: Config#parallelism.
  Trainer.Config.training: Config#training.
  Trainer.Config.model_spec: Config#model_spec.
  Trainer: ''
  Trainer.Config: Config#
  Trainer._collect_moe_routing_metrics: _collect_moe_routing_metrics.
  Trainer.transfer_stream: transfer_stream.
  Trainer.Config.checkpoint: Config#checkpoint.
  Trainer.Config.loss: Config#loss.
  Trainer.Config.activation_checkpoint: Config#activation_checkpoint.
  Trainer.train_step: train_step().
  Trainer.Config.optimizer: Config#optimizer.
  Trainer.Config.dataloader: Config#dataloader.
  Trainer.Config.lr_scheduler: Config#lr_scheduler.
  Trainer.train: train().
  Trainer.Config.hf_assets_path: Config#hf_assets_path.
  Trainer.Config.compile: Config#compile.
  Trainer.Config.metrics: Config#metrics.
  Trainer.config: config.
  Trainer.Config.__post_init__: Config#__post_init__().
  Trainer.model_parts: model_parts.
  Trainer.Config._validate_cuda_graphs: Config#_validate_cuda_graphs().
  Trainer.forward_backward_step: forward_backward_step().
  Trainer.device: device.
  Trainer.pp_schedule: pp_schedule.
  Trainer.Config.override: Config#override.
  Trainer.Config.validator: Config#validator.
  Trainer.Config.tokenizer: Config#tokenizer.
  Trainer.Config.debug: Config#debug.
  Trainer.parallel_dims: parallel_dims.
  Trainer.step: step.
  Trainer.metrics_processor: metrics_processor.
  Trainer.close: close().
  Trainer.optimizers: optimizers.
  Trainer.init_distributed: init_distributed().
  Trainer._clip_grad_norm: _clip_grad_norm().
  Trainer.Config.dump_folder: Config#dump_folder.
  Trainer.Config.profiler: Config#profiler.
  Trainer.loss_fn: loss_fn.
  Trainer.__init__: __init__().
  Trainer.ntokens_seen: ntokens_seen.
  Trainer.Config.maybe_log: Config#maybe_log().
  Trainer.Config.to_dict: Config#to_dict().
  Trainer.Config._validate_sdc_replay: Config#_validate_sdc_replay().
  Trainer.dataloader: dataloader.
  Trainer.lr_schedulers: lr_schedulers.
  Trainer.Config.sdc_replayer: Config#sdc_replayer.
  Trainer.batch_generator: batch_generator().
  Trainer.checkpointer: checkpointer.
  Trainer.train_context: train_context.
  Trainer._pp_forward_backward_body: _pp_forward_backward_body().
  Trainer.Config.comm: Config#comm.
  Trainer.model_config: model_config.
  Trainer.gradient_accumulation_steps: gradient_accumulation_steps.
  Trainer.should_continue_training: should_continue_training().
  Trainer.fwd_bwd_fn: fwd_bwd_fn.
  Trainer.sdc_replayer: sdc_replayer.
  Trainer._forward_backward_body: _forward_backward_body().
  Trainer.pp_has_last_stage: pp_has_last_stage.
  Trainer.load_state_dict: load_state_dict().
  Trainer.tokenizer: tokenizer.
  Trainer.validator: validator.
  Trainer.gc_handler: gc_handler.
  Trainer.num_pp_microbatches: num_pp_microbatches.
  Trainer.pp_has_first_stage: pp_has_first_stage.
  Trainer.state_dict: state_dict().
  Trainer.fwd_bwd: fwd_bwd().
  Trainer._pp_loss_sentinel_on_non_last_stage: _pp_loss_sentinel_on_non_last_stage.
---
# Module: [`torchtitan/trainer.py`](../../../../../raw/code/torchtitan/torchtitan/trainer.py)

## Classes
### <a id="Trainer"></a>`Trainer`  ·  implements/extends Configurable
- def: [`torchtitan/trainer.py:74`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L74) — documented in [checkpointing](../../concepts/checkpointing.md)
- signature: `class Trainer(torch.distributed.checkpoint.stateful.Stateful, Configurable):`
- members:
  - <a id="Trainer.batch_generator"></a>`batch_generator(self, data_iterable: Iterable[TrainerBatch])` — [`L766`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L766) — Returns an iterator that processes batches from the data iterator.
  - <a id="Trainer.close"></a>`close(self)` — [`L1208`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L1208)
  - <a id="Trainer.forward_backward_step"></a>`forward_backward_step(self, *, input_dict: dict[str, Any] | list[dict[str, Any]], global_valid_tokens: torch.Tensor)` — [`L795`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L795) — documented in [trainer-and-train-loop](../../concepts/trainer-and-train-loop.md)
  - <a id="Trainer.fwd_bwd"></a>`fwd_bwd()` — [`L988`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L988)
  - <a id="Trainer.init_distributed"></a>`init_distributed(self)` — [`L756`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L756) — documented in [trainer-and-train-loop](../../concepts/trainer-and-train-loop.md)
  - <a id="Trainer.load_state_dict"></a>`load_state_dict(self, state_dict: dict[str, Any])` — [`L1202`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L1202)
  - <a id="Trainer.should_continue_training"></a>`should_continue_training(self)` — [`L1196`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L1196)
  - <a id="Trainer.state_dict"></a>`state_dict(self)` — [`L1199`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L1199)
  - <a id="Trainer.train"></a>`train(self)` — [`L1129`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L1129) — documented in [trainer-and-train-loop](../../concepts/trainer-and-train-loop.md)
  - <a id="Trainer.train_step"></a>`train_step(self, data_iterator: Iterator[dict[str, Any]])` — [`L913`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L913) — documented in [trainer-and-train-loop](../../concepts/trainer-and-train-loop.md)
  - <a id="Trainer.checkpointer"></a>`checkpointer` — [`L324`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L324)
  - <a id="Trainer.config"></a>`config` — [`L309`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L309)
  - <a id="Trainer.dataloader"></a>`dataloader` — [`L314`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L314)
  - <a id="Trainer.device"></a>`device` — [`L327`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L327)
  - <a id="Trainer.fwd_bwd_fn"></a>`fwd_bwd_fn` — [`L330`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L330)
  - <a id="Trainer.gc_handler"></a>`gc_handler` — [`L328`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L328)
  - <a id="Trainer.gradient_accumulation_steps"></a>`gradient_accumulation_steps` — [`L332`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L332)
  - <a id="Trainer.loss_fn"></a>`loss_fn` — [`L319`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L319)
  - <a id="Trainer.lr_schedulers"></a>`lr_schedulers` — [`L321`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L321)
  - <a id="Trainer.metrics_processor"></a>`metrics_processor` — [`L323`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L323)
  - <a id="Trainer.model_config"></a>`model_config` — [`L315`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L315)
  - <a id="Trainer.model_parts"></a>`model_parts` — [`L318`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L318)
  - <a id="Trainer.ntokens_seen"></a>`ntokens_seen` — [`L340`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L340)
  - <a id="Trainer.num_pp_microbatches"></a>`num_pp_microbatches` — [`L333`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L333)
  - <a id="Trainer.optimizers"></a>`optimizers` — [`L320`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L320)
  - <a id="Trainer.parallel_dims"></a>`parallel_dims` — [`L310`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L310)
  - <a id="Trainer.pp_has_first_stage"></a>`pp_has_first_stage` — [`L334`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L334)
  - <a id="Trainer.pp_has_last_stage"></a>`pp_has_last_stage` — [`L335`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L335)
  - <a id="Trainer.pp_schedule"></a>`pp_schedule` — [`L529`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L529)
  - <a id="Trainer.sdc_replayer"></a>`sdc_replayer` — [`L336`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L336)
  - <a id="Trainer.step"></a>`step` — [`L339`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L339)
  - <a id="Trainer.tokenizer"></a>`tokenizer` — [`L313`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L313)
  - <a id="Trainer.train_context"></a>`train_context` — [`L329`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L329)
  - <a id="Trainer.transfer_stream"></a>`transfer_stream` — [`L356`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L356)
  - <a id="Trainer.validator"></a>`validator` — [`L322`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L322)
- protocol/private: <a id="Trainer.__init__"></a>`__init__`[`L344`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L344), <a id="Trainer._clip_grad_norm"></a>`_clip_grad_norm`[`L1119`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L1119), <a id="Trainer._collect_moe_routing_metrics"></a>`_collect_moe_routing_metrics`[`L587`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L587), <a id="Trainer._forward_backward_body"></a>`_forward_backward_body`[`L858`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L858), <a id="Trainer._pp_forward_backward_body"></a>`_pp_forward_backward_body`[`L885`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L885), <a id="Trainer._pp_loss_sentinel_on_non_last_stage"></a>`_pp_loss_sentinel_on_non_last_stage`[`L331`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L331)
- uses (calls/refs, reference-scoped): [`logger`](tools/logging.md#logger), [`parallelism`](trainer.md#Trainer.Config.parallelism), [`build`](protocols/module.md#Module.Config.build), [`training`](trainer.md#Trainer.Config.training), [`model_spec`](trainer.md#Trainer.Config.model_spec), [`Configurable`](config/configurable.md#Configurable), [`Config`](trainer.md#Trainer.Config), [`model`](protocols/model_spec.md#ModelSpec.model), [`ParallelDims`](distributed/parallel_dims.md#ParallelDims), [`build`](config/configurable.md#Configurable.Config.build), [`max_context_length`](config/configs.md#TrainingConfig.max_context_length), [`num_tokens_per_microbatch_per_dp_rank`](config/configs.md#TrainingConfig.num_tokens_per_microbatch_per_dp_rank), [`LRSchedulersContainer`](components/optimizer/lr_scheduler.md#LRSchedulersContainer), [`steps`](config/configs.md#TrainingConfig.steps), [`TORCH_DTYPE_MAP`](config/__init__.md#TORCH_DTYPE_MAP), [`checkpoint`](trainer.md#Trainer.Config.checkpoint), [`ChunkedLossWrapper`](components/loss.md#ChunkedLossWrapper), [`loss`](trainer.md#Trainer.Config.loss), [`activation_checkpoint`](trainer.md#Trainer.Config.activation_checkpoint), [`optimizer`](trainer.md#Trainer.Config.optimizer), [`dataloader`](trainer.md#Trainer.Config.dataloader), [`warmup_steps`](components/optimizer/lr_scheduler.md#LRSchedulersContainer.Config.warmup_steps), [`train_step`](experiments/torchft/trainer.md#FaultTolerantTrainer.train_step), [`lr_scheduler`](trainer.md#Trainer.Config.lr_scheduler), [`MetricsProcessor`](components/metrics.md#MetricsProcessor), [`train`](experiments/torchft/trainer.md#FaultTolerantTrainer.train), [`hf_assets_path`](trainer.md#Trainer.Config.hf_assets_path), [`compile`](trainer.md#Trainer.Config.compile), [`spmd_backend`](config/configs.md#ParallelismConfig.spmd_backend), [`metrics`](trainer.md#Trainer.Config.metrics), [`GraphTrainer`](experiments/graph_trainer/trainer.md#GraphTrainer), [`disable_cuda_graphs`](config/configs.md#TrainingConfig.disable_cuda_graphs), [`BaseModel`](protocols/model.md#BaseModel), [`log_trace_span`](observability/structured_logger/structured_logging.md#log_trace_span), [`get_mesh`](distributed/parallel_dims.md#ParallelDims.get_mesh), [`log`](components/metrics.md#MetricsProcessor.log), [`train_step`](models/flux/trainer.md#FluxTrainer.train_step), [`apply_overrides`](config/override.md#apply_overrides), [`parallelize_fn`](protocols/model_spec.md#ModelSpec.parallelize_fn), [`__post_init__`](trainer.md#Trainer.Config.__post_init__)  (+118 more; 3 test-only)
- used by: [`Configurable`](config/configurable.md#Configurable), [`llama3_debugmodel`](models/llama3/config_registry.md#llama3_debugmodel), [`__init__`](experiments/torchft/trainer.md#FaultTolerantTrainer.__init__), [`llama3_405b`](models/llama3/config_registry.md#llama3_405b), [`pp_schedule`](experiments/torchft/trainer.md#FaultTolerantTrainer.pp_schedule), [`sft_debugmodel`](models/llama3/config_registry.md#sft_debugmodel), [`sft_qwen3_8b_math`](models/qwen3/config_registry.md#sft_qwen3_8b_math), [`qwen35_debugmodel_moe`](models/qwen3_5/config_registry.md#qwen35_debugmodel_moe), [`deepseek_v4_debugmodel`](models/deepseek_v4/config_registry.md#deepseek_v4_debugmodel), [`qwen38_debugmodel_moe`](models/qwen3_8/config_registry.md#qwen38_debugmodel_moe), [`deepseek_v3_debugmodel`](models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel), [`deepseek_v4_flash`](models/deepseek_v4/config_registry.md#deepseek_v4_flash), [`deepseek_v4_pro`](models/deepseek_v4/config_registry.md#deepseek_v4_pro), [`qwen36_debugmodel_moe`](models/qwen3_6/config_registry.md#qwen36_debugmodel_moe), [`_gpt_oss_debugmodel`](models/gpt_oss/config_registry.md#_gpt_oss_debugmodel), [`deepseek_v4_mtp_debugmodel`](models/deepseek_v4/config_registry.md#deepseek_v4_mtp_debugmodel), [`kimi_k2_5_debugmodel`](models/kimi_k2_7/config_registry.md#kimi_k2_5_debugmodel), [`muse_glimmer_debugmodel`](models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel), [`qwen35_debugmodel`](models/qwen3_5/config_registry.md#qwen35_debugmodel), [`qwen38_debugmodel`](models/qwen3_8/config_registry.md#qwen38_debugmodel), [`kimi_k2_5`](models/kimi_k2_7/config_registry.md#kimi_k2_5), [`llama3_70b`](models/llama3/config_registry.md#llama3_70b), [`muse_glimmer_debugmodel_mm`](models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel_mm), [`qwen36_debugmodel`](models/qwen3_6/config_registry.md#qwen36_debugmodel), [`deepseek_v3_671b`](models/deepseek_v3/config_registry.md#deepseek_v3_671b), [`qwen3_debugmodel`](models/qwen3/config_registry.md#qwen3_debugmodel), [`deepseek_v3_16b`](models/deepseek_v3/config_registry.md#deepseek_v3_16b), [`qwen3_moe_debug`](models/qwen3/config_registry.md#qwen3_moe_debug), [`llama3_8b`](models/llama3/config_registry.md#llama3_8b), [`qwen35_122b_a10b`](models/qwen3_5/config_registry.md#qwen35_122b_a10b), [`qwen35_35b_a3b`](models/qwen3_5/config_registry.md#qwen35_35b_a3b), [`qwen35_397b_a17b`](models/qwen3_5/config_registry.md#qwen35_397b_a17b), [`qwen36_35b_a3b`](models/qwen3_6/config_registry.md#qwen36_35b_a3b), [`kimi_k3_debugmodel`](models/kimi_k3/config_registry.md#kimi_k3_debugmodel), [`qwen3_moe_deepep`](models/qwen3/config_registry.md#qwen3_moe_deepep), [`qwen35_27b`](models/qwen3_5/config_registry.md#qwen35_27b), [`qwen35_9b`](models/qwen3_5/config_registry.md#qwen35_9b), [`qwen36_27b`](models/qwen3_6/config_registry.md#qwen36_27b), [`qwen38_27b`](models/qwen3_8/config_registry.md#qwen38_27b), [`qwen3_debugmodel_flex_flash`](models/qwen3/config_registry.md#qwen3_debugmodel_flex_flash)  (+106 more; 125 test-only)

### <a id="Trainer.Config"></a>`Trainer.Config`  ·  implements/extends Config
- def: [`torchtitan/trainer.py:76`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L76) — documented in [tpu-trainer-and-job-config](../../concepts/tpu-trainer-and-job-config.md)
- doc: Default container for training configuration.
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="Trainer.Config.maybe_log"></a>`maybe_log(self)` — [`L287`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L287)
  - <a id="Trainer.Config.to_dict"></a>`to_dict(self)` — [`L267`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L267)
  - <a id="Trainer.Config.activation_checkpoint"></a>`activation_checkpoint` — [`L118`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L118)
  - <a id="Trainer.Config.checkpoint"></a>`checkpoint` — [`L115`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L115)
  - <a id="Trainer.Config.comm"></a>`comm` — [`L122`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L122)
  - <a id="Trainer.Config.compile"></a>`compile` — [`L121`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L121)
  - <a id="Trainer.Config.dataloader"></a>`dataloader` — [`L106`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L106)
  - <a id="Trainer.Config.debug"></a>`debug` — [`L124`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L124)
  - <a id="Trainer.Config.dump_folder"></a>`dump_folder` — [`L96`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L96) — ---
  - <a id="Trainer.Config.hf_assets_path"></a>`hf_assets_path` — [`L89`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L89) — ---
  - <a id="Trainer.Config.loss"></a>`loss` — [`L130`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L130)
  - <a id="Trainer.Config.lr_scheduler"></a>`lr_scheduler` — [`L110`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L110)
  - <a id="Trainer.Config.metrics"></a>`metrics` — [`L100`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L100)
  - <a id="Trainer.Config.model_spec"></a>`model_spec` — [`L83`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L83) — documented in [tpu-trainer-and-job-config](../../concepts/tpu-trainer-and-job-config.md)
  - <a id="Trainer.Config.optimizer"></a>`optimizer` — [`L107`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L107)
  - <a id="Trainer.Config.override"></a>`override` — [`L129`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L129)
  - <a id="Trainer.Config.parallelism"></a>`parallelism` — [`L114`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L114) — documented in [job-config](../../concepts/job-config.md)
  - <a id="Trainer.Config.profiler"></a>`profiler` — [`L99`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L99)
  - <a id="Trainer.Config.sdc_replayer"></a>`sdc_replayer` — [`L128`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L128)
  - <a id="Trainer.Config.tokenizer"></a>`tokenizer` — [`L103`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L103)
  - <a id="Trainer.Config.training"></a>`training` — [`L113`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L113) — documented in [job-config](../../concepts/job-config.md)
  - <a id="Trainer.Config.validator"></a>`validator` — [`L123`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L123)
- protocol/private: <a id="Trainer.Config.__post_init__"></a>`__post_init__`[`L132`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L132), <a id="Trainer.Config._validate_cuda_graphs"></a>`_validate_cuda_graphs`[`L186`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L186), <a id="Trainer.Config._validate_sdc_replay"></a>`_validate_sdc_replay`[`L245`](../../../../../raw/code/torchtitan/torchtitan/trainer.py#L245)
- uses (calls/refs, reference-scoped): [`logger`](tools/logging.md#logger), [`Configurable`](config/configurable.md#Configurable), [`ParallelismConfig`](config/configs.md#ParallelismConfig), [`TrainingConfig`](config/configs.md#TrainingConfig), [`model`](protocols/model_spec.md#ModelSpec.model), [`CheckpointManager`](components/checkpointer/dcp.md#CheckpointManager), [`enable`](config/configs.md#CompileConfig.enable), [`LRSchedulersContainer`](components/optimizer/lr_scheduler.md#LRSchedulersContainer), [`CompileConfig`](config/configs.md#CompileConfig), [`Config`](components/checkpointer/dcp.md#CheckpointManager.Config), [`FlexInnerAttention`](models/common/attention.md#FlexInnerAttention), [`SelectiveAC`](distributed/activation_checkpoint.md#SelectiveAC), [`Config`](components/optimizer/lr_scheduler.md#LRSchedulersContainer.Config), [`ModelSpec`](protocols/model_spec.md#ModelSpec), [`MetricsProcessor`](components/metrics.md#MetricsProcessor), [`expert_parallel_degree`](config/configs.md#ParallelismConfig.expert_parallel_degree), [`Config`](distributed/activation_checkpoint.md#SelectiveAC.Config), [`spmd_backend`](config/configs.md#ParallelismConfig.spmd_backend), [`Config`](config/configurable.md#Configurable.Config), [`disable_cuda_graphs`](config/configs.md#TrainingConfig.disable_cuda_graphs), [`Config`](components/metrics.md#MetricsProcessor.Config), [`components`](config/configs.md#CompileConfig.components), [`ActivationCheckpointingConfig`](distributed/activation_checkpoint.md#ActivationCheckpointingConfig), [`VarlenInnerAttention`](models/common/attention.md#VarlenInnerAttention), [`OptimizersContainer`](components/optimizer/optimizer.md#OptimizersContainer), [`pipeline_parallel_degree`](config/configs.md#ParallelismConfig.pipeline_parallel_degree), [`Profiler`](tools/profiler.md#Profiler), [`HuggingFaceTokenizer`](components/tokenizer.md#HuggingFaceTokenizer), [`name`](protocols/model_spec.md#ModelSpec.name), [`flavor`](protocols/model_spec.md#ModelSpec.flavor), [`pipeline_parallel_schedule`](config/configs.md#ParallelismConfig.pipeline_parallel_schedule), [`traverse`](config/configurable.md#Configurable.Config.traverse), [`Validator`](components/validate.md#Validator), [`BaseLoss`](components/loss.md#BaseLoss), [`validate_context_parallel`](config/validation.md#validate_context_parallel), [`Config`](models/common/attention.md#FlexInnerAttention.Config), [`Config`](components/validate.md#Validator.Config), [`Config`](models/common/attention.md#VarlenInnerAttention.Config), [`num_pp_microbatches`](config/configs.md#ParallelismConfig.num_pp_microbatches), [`OverrideConfig`](config/override.md#OverrideConfig)  (+34 more)
- used by: [`sft_llama3_8b_metamath`](experiments/tpu/llama3/config_registry.md#sft_llama3_8b_metamath), [`qwen3_8b`](experiments/tpu/qwen3/config_registry.md#qwen3_8b), [`flux_debugmodel`](models/flux/config_registry.md#flux_debugmodel), [`reg_trainer_qwen3_8b`](experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b), [`start_trainer`](experiments/tpu/conformer/train_minimal.md#start_trainer), [`qwen3_1_7b`](experiments/tpu/qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](experiments/tpu/llama3/config_registry.md#llama3_70b), [`llama3_405b`](experiments/tpu/llama3/config_registry.md#llama3_405b), [`llama3_8b`](experiments/tpu/llama3/config_registry.md#llama3_8b), [`llama3_debugmodel`](models/llama3/config_registry.md#llama3_debugmodel), [`_qwen3_moe_30b_fsdp_only_full_ac`](experiments/tpu/qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`llama3_torchft_debugmodel`](experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel), [`_muse_glimmer_30b_base`](experiments/tpu/muse_glimmer/config_registry.md#_muse_glimmer_30b_base), [`flux_dev`](models/flux/config_registry.md#flux_dev), [`flux_schnell`](models/flux/config_registry.md#flux_schnell), [`__init__`](experiments/torchft/trainer.md#FaultTolerantTrainer.__init__), [`llama3_405b`](models/llama3/config_registry.md#llama3_405b), [`pp_schedule`](experiments/torchft/trainer.md#FaultTolerantTrainer.pp_schedule), [`qwen3_moe_30b`](experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b), [`_tpu_hf_config`](experiments/tpu/transformers_modeling_backend/config_registry.md#_tpu_hf_config), [`_collect_moe_routing_metrics`](trainer.md#Trainer._collect_moe_routing_metrics), [`transformers_modeling_backend_sft_full`](experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_full), [`sft_debugmodel`](models/llama3/config_registry.md#sft_debugmodel), [`sft_qwen3_8b_math`](models/qwen3/config_registry.md#sft_qwen3_8b_math), [`transformers_modeling_backend_sft_debugmodel`](experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_debugmodel), [`qwen35_debugmodel_moe`](models/qwen3_5/config_registry.md#qwen35_debugmodel_moe), [`deepseek_v4_debugmodel`](models/deepseek_v4/config_registry.md#deepseek_v4_debugmodel), [`qwen35_moe_35b`](experiments/tpu/qwen3_5/config_registry.md#qwen35_moe_35b), [`qwen38_debugmodel_moe`](models/qwen3_8/config_registry.md#qwen38_debugmodel_moe), [`deepseek_v3_debugmodel`](models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel), [`transfer_stream`](trainer.md#Trainer.transfer_stream), [`deepseek_v4_flash`](models/deepseek_v4/config_registry.md#deepseek_v4_flash), [`deepseek_v4_pro`](models/deepseek_v4/config_registry.md#deepseek_v4_pro), [`qwen36_debugmodel_moe`](models/qwen3_6/config_registry.md#qwen36_debugmodel_moe), [`_gpt_oss_debugmodel`](models/gpt_oss/config_registry.md#_gpt_oss_debugmodel), [`deepseek_v4_mtp_debugmodel`](models/deepseek_v4/config_registry.md#deepseek_v4_mtp_debugmodel), [`kimi_k2_5_debugmodel`](models/kimi_k2_7/config_registry.md#kimi_k2_5_debugmodel), [`muse_glimmer_debugmodel`](models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel), [`transformers_modeling_backend_debugmodel`](experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel), [`qwen3_debugmodel`](experiments/tpu/qwen3/config_registry.md#qwen3_debugmodel)  (+201 more; 181 test-only)

