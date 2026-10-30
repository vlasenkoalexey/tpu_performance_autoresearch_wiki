---
title: 'Module: torchtitan/experiments/torchft/trainer.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/torchft/trainer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.torchft.trainer`/FaultTolerantTrainer#
symbols:
  FaultTolerantTrainer.__init__: __init__().
  FaultTolerantTrainer.pp_schedule: pp_schedule.
  FaultTolerantTrainer.train_step: train_step().
  FaultTolerantTrainer.train: train().
  FaultTolerantTrainer.init_distributed: init_distributed().
  FaultTolerantTrainer._configure_chunked_loss: _configure_chunked_loss().
  FaultTolerantTrainer.ft_manager: ft_manager.
  FaultTolerantTrainer.Config: Config#
  FaultTolerantTrainer.sdc_replayer: sdc_replayer.
  FaultTolerantTrainer: ''
  FaultTolerantTrainer.Config.fault_tolerance: Config#fault_tolerance.
  FaultTolerantTrainer.fwd_bwd: fwd_bwd().
---
# Module: [`torchtitan/experiments/torchft/trainer.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/trainer.py)

## Classes
### <a id="FaultTolerantTrainer"></a>`FaultTolerantTrainer`  ·  implements/extends Trainer
- def: [`torchtitan/experiments/torchft/trainer.py:37`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/trainer.py#L37)
- signature: `class FaultTolerantTrainer(Trainer):`
- members:
  - <a id="FaultTolerantTrainer.fwd_bwd"></a>`fwd_bwd()` — [`L503`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/trainer.py#L503)
  - <a id="FaultTolerantTrainer.init_distributed"></a>`init_distributed(self)` — [`L426`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/trainer.py#L426) — documented in [trainer-and-train-loop](../../../../concepts/trainer-and-train-loop.md)
  - <a id="FaultTolerantTrainer.train"></a>`train(self)` — [`L588`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/trainer.py#L588)
  - <a id="FaultTolerantTrainer.train_step"></a>`train_step(self, data_iterator: Iterator[dict[str, Any]])` — [`L454`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/trainer.py#L454)
  - <a id="FaultTolerantTrainer.ft_manager"></a>`ft_manager` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/trainer.py#L42)
  - <a id="FaultTolerantTrainer.pp_schedule"></a>`pp_schedule` — [`L209`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/trainer.py#L209)
  - <a id="FaultTolerantTrainer.sdc_replayer"></a>`sdc_replayer` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/trainer.py#L43)
- protocol/private: <a id="FaultTolerantTrainer.__init__"></a>`__init__`[`L46`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/trainer.py#L46), <a id="FaultTolerantTrainer._configure_chunked_loss"></a>`_configure_chunked_loss`[`L399`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/trainer.py#L399)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`parallelism`](../../trainer.md#Trainer.Config.parallelism), [`build`](../../protocols/module.md#Module.Config.build), [`training`](../../trainer.md#Trainer.Config.training), [`model_spec`](../../trainer.md#Trainer.Config.model_spec), [`Trainer`](../../trainer.md#Trainer), [`model`](../../protocols/model_spec.md#ModelSpec.model), [`ParallelDims`](../../distributed/parallel_dims.md#ParallelDims), [`build`](../../config/configurable.md#Configurable.Config.build), [`max_context_length`](../../config/configs.md#TrainingConfig.max_context_length), [`num_tokens_per_microbatch_per_dp_rank`](../../config/configs.md#TrainingConfig.num_tokens_per_microbatch_per_dp_rank), [`steps`](../../config/configs.md#TrainingConfig.steps), [`TORCH_DTYPE_MAP`](../../config/__init__.md#TORCH_DTYPE_MAP), [`checkpoint`](../../trainer.md#Trainer.Config.checkpoint), [`ChunkedLossWrapper`](../../components/loss.md#ChunkedLossWrapper), [`loss`](../../trainer.md#Trainer.Config.loss), [`activation_checkpoint`](../../trainer.md#Trainer.Config.activation_checkpoint), [`optimizer`](../../trainer.md#Trainer.Config.optimizer), [`dataloader`](../../trainer.md#Trainer.Config.dataloader), [`warmup_steps`](../../components/optimizer/lr_scheduler.md#LRSchedulersContainer.Config.warmup_steps), [`lr_scheduler`](../../trainer.md#Trainer.Config.lr_scheduler), [`hf_assets_path`](../../trainer.md#Trainer.Config.hf_assets_path), [`compile`](../../trainer.md#Trainer.Config.compile), [`spmd_backend`](../../config/configs.md#ParallelismConfig.spmd_backend), [`metrics`](../../trainer.md#Trainer.Config.metrics), [`disable_cuda_graphs`](../../config/configs.md#TrainingConfig.disable_cuda_graphs), [`BaseModel`](../../protocols/model.md#BaseModel), [`config`](../../trainer.md#Trainer.config), [`get_mesh`](../../distributed/parallel_dims.md#ParallelDims.get_mesh), [`log`](../../components/metrics.md#MetricsProcessor.log), [`apply_overrides`](../../config/override.md#apply_overrides), [`parallelize_fn`](../../protocols/model_spec.md#ModelSpec.parallelize_fn), [`__post_init__`](../../trainer.md#Trainer.Config.__post_init__), [`model_parts`](../../trainer.md#Trainer.model_parts), [`forward_backward_step`](../../trainer.md#Trainer.forward_backward_step), [`get_optional_mesh`](../../distributed/parallel_dims.md#ParallelDims.get_optional_mesh), [`name`](../../protocols/model_spec.md#ModelSpec.name), [`load`](../../components/checkpointer/base.md#BaseCheckpointManager.load), [`flavor`](../../protocols/model_spec.md#ModelSpec.flavor), [`imports`](../../config/override.md#OverrideConfig.imports)  (+112 more)
- used by: [`Trainer`](../../trainer.md#Trainer), [`llama3_torchft_debugmodel`](llama3/config_registry.md#llama3_torchft_debugmodel), [`train_step`](../../trainer.md#Trainer.train_step), [`train`](../../trainer.md#Trainer.train), [`init_distributed`](../../trainer.md#Trainer.init_distributed)

### <a id="FaultTolerantTrainer.Config"></a>`FaultTolerantTrainer.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/torchft/trainer.py:39`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/trainer.py#L39)
- signature: `class Config(Trainer.Config):`
- members:
  - <a id="FaultTolerantTrainer.Config.fault_tolerance"></a>`fault_tolerance` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/trainer.py#L40)
- uses (calls/refs, reference-scoped): [`Trainer`](../../trainer.md#Trainer), [`Config`](../../trainer.md#Trainer.Config), [`FaultTolerance`](config/job_config.md#FaultTolerance)
- used by: [`llama3_torchft_debugmodel`](llama3/config_registry.md#llama3_torchft_debugmodel), [`__init__`](trainer.md#FaultTolerantTrainer.__init__)

