---
title: 'Module: torchtitan/experiments/tpu/train_minimal.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/train_minimal.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.train_minimal`/
symbols:
  TrainerMinimal.train: TrainerMinimal#train().
  TrainerMinimal.parallel_dims: TrainerMinimal#parallel_dims.
  TrainerMinimal.loss_fn: TrainerMinimal#loss_fn.
  TrainerMinimal.model_config: TrainerMinimal#model_config.
  TrainerMinimal.job_config: TrainerMinimal#job_config.
  TrainerMinimal.loss_mesh: TrainerMinimal#loss_mesh.
  start_trainer: start_trainer().
  TrainerMinimal.model: TrainerMinimal#model.
  TrainerMinimal.dataloader: TrainerMinimal#dataloader.
  logger: logger.
  TrainerMinimal.get_batch: TrainerMinimal#get_batch().
  TrainerMinimal.tokenizer: TrainerMinimal#tokenizer.
  TrainerMinimal._get_dummy_batch: TrainerMinimal#_get_dummy_batch().
  TrainerMinimal.device: TrainerMinimal#device.
  TrainerMinimal.model_spec: TrainerMinimal#model_spec.
  TrainerMinimal.optimizers: TrainerMinimal#optimizers.
  JobConfig: JobConfig.
  TrainerMinimal.train_context: TrainerMinimal#train_context.
  TrainerMinimal._undo_headtail: TrainerMinimal#_undo_headtail().
  TrainerMinimal.__init__: TrainerMinimal#__init__().
  TrainerMinimal: TrainerMinimal#
  TrainerMinimal.batch_mesh: TrainerMinimal#batch_mesh.
  TORCH_DTYPE_MAP: TORCH_DTYPE_MAP.
  ParallelDims: ParallelDims.
  _gather_along_first_dim: _gather_along_first_dim().
  TrainerMinimal.world_size: TrainerMinimal#world_size.
  TrainerMinimal.cp_mesh: TrainerMinimal#cp_mesh.
  TrainerMinimal.step_callback: TrainerMinimal#step_callback.
  TrainStepCallback: TrainStepCallback.
  TrainerMinimal.rank: TrainerMinimal#rank.
---
# Module: [`torchtitan/experiments/tpu/train_minimal.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py)

## Classes
### <a id="TrainerMinimal"></a>`TrainerMinimal`
- def: [`torchtitan/experiments/tpu/train_minimal.py:66`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L66)
- doc: Minimal trainer for TorchTitan models.
- signature: `class TrainerMinimal:`
- members:
  - <a id="TrainerMinimal.__init__"></a>`__init__(self, device: torch.device, rank: int, world_size: int, job_config: JobConfig, step_callback: Optional[TrainStepCallback] = None)` — [`L73`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L73) — Initializes the TrainerMinimal.
  - <a id="TrainerMinimal.get_batch"></a>`get_batch()` — [`L314`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L314) — One microbatch as ``(tokens, labels, forward_kwargs)``.
  - <a id="TrainerMinimal.train"></a>`train(self)` — [`L295`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L295) — Runs a simple training loop on the specified device. — documented in [trainer-and-train-loop](../../../../concepts/trainer-and-train-loop.md)
  - <a id="TrainerMinimal.batch_mesh"></a>`batch_mesh` — [`L131`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L131)
  - <a id="TrainerMinimal.cp_mesh"></a>`cp_mesh` — [`L132`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L132)
  - <a id="TrainerMinimal.dataloader"></a>`dataloader` — [`L179`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L179)
  - <a id="TrainerMinimal.device"></a>`device` — [`L92`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L92)
  - <a id="TrainerMinimal.job_config"></a>`job_config` — [`L95`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L95)
  - <a id="TrainerMinimal.loss_fn"></a>`loss_fn` — [`L247`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L247)
  - <a id="TrainerMinimal.loss_mesh"></a>`loss_mesh` — [`L133`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L133)
  - <a id="TrainerMinimal.model"></a>`model` — [`L268`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L268)
  - <a id="TrainerMinimal.model_config"></a>`model_config` — [`L207`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L207)
  - <a id="TrainerMinimal.model_spec"></a>`model_spec` — [`L167`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L167)
  - <a id="TrainerMinimal.optimizers"></a>`optimizers` — [`L283`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L283)
  - <a id="TrainerMinimal.parallel_dims"></a>`parallel_dims` — [`L116`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L116)
  - <a id="TrainerMinimal.rank"></a>`rank` — [`L93`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L93)
  - <a id="TrainerMinimal.step_callback"></a>`step_callback` — [`L293`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L293)
  - <a id="TrainerMinimal.tokenizer"></a>`tokenizer` — [`L169`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L169)
  - <a id="TrainerMinimal.train_context"></a>`train_context` — [`L290`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L290)
  - <a id="TrainerMinimal.world_size"></a>`world_size` — [`L94`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L94)
- protocol/private: <a id="TrainerMinimal._get_dummy_batch"></a>`_get_dummy_batch`[`L348`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L348), <a id="TrainerMinimal._undo_headtail"></a>`_undo_headtail`[`L446`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L446)
- uses (calls/refs, reference-scoped): [`parallelism`](../../trainer.md#Trainer.Config.parallelism), [`build`](../../protocols/module.md#Module.Config.build), [`training`](../../trainer.md#Trainer.Config.training), [`model_spec`](../../trainer.md#Trainer.Config.model_spec), [`model`](../../protocols/model_spec.md#ModelSpec.model), [`build`](../../config/configurable.md#Configurable.Config.build), [`max_context_length`](../../config/configs.md#TrainingConfig.max_context_length), [`num_tokens_per_microbatch_per_dp_rank`](../../config/configs.md#TrainingConfig.num_tokens_per_microbatch_per_dp_rank), [`steps`](../../config/configs.md#TrainingConfig.steps), [`ChunkedLossWrapper`](../../components/loss.md#ChunkedLossWrapper), [`loss`](../../trainer.md#Trainer.Config.loss), [`activation_checkpoint`](../../trainer.md#Trainer.Config.activation_checkpoint), [`optimizer`](../../trainer.md#Trainer.Config.optimizer), [`data_parallel_shard_degree`](../../config/configs.md#ParallelismConfig.data_parallel_shard_degree), [`dataloader`](../../trainer.md#Trainer.Config.dataloader), [`warmup_steps`](../../components/optimizer/lr_scheduler.md#LRSchedulersContainer.Config.warmup_steps), [`tensor_parallel_degree`](../../config/configs.md#ParallelismConfig.tensor_parallel_degree), [`Decoder`](../../models/common/decoder.md#Decoder), [`lr_scheduler`](../../trainer.md#Trainer.Config.lr_scheduler), [`hf_assets_path`](../../trainer.md#Trainer.Config.hf_assets_path), [`compile`](../../trainer.md#Trainer.Config.compile), [`expert_parallel_degree`](../../config/configs.md#ParallelismConfig.expert_parallel_degree), [`spmd_backend`](../../config/configs.md#ParallelismConfig.spmd_backend), [`BaseModel`](../../protocols/model.md#BaseModel), [`set_unflatten_seq_len`](unflatten_shim.md#set_unflatten_seq_len), [`get_mesh`](../../distributed/parallel_dims.md#ParallelDims.get_mesh), [`parallelize_fn`](../../protocols/model_spec.md#ModelSpec.parallelize_fn), [`context_parallel_degree`](../../config/configs.md#ParallelismConfig.context_parallel_degree), [`pp`](../../distributed/parallel_dims.md#ParallelDims.pp), [`pipeline_parallel_degree`](../../config/configs.md#ParallelismConfig.pipeline_parallel_degree), [`Profiler`](../../tools/profiler.md#Profiler), [`tp`](../../distributed/parallel_dims.md#ParallelDims.tp), [`HuggingFaceTokenizer`](../../components/tokenizer.md#HuggingFaceTokenizer), [`name`](../../protocols/model_spec.md#ModelSpec.name), [`cp`](../../distributed/parallel_dims.md#ParallelDims.cp), [`dp_shard`](../../distributed/parallel_dims.md#ParallelDims.dp_shard), [`ep`](../../distributed/parallel_dims.md#ParallelDims.ep), [`flavor`](../../protocols/model_spec.md#ModelSpec.flavor), [`dp_replicate`](../../distributed/parallel_dims.md#ParallelDims.dp_replicate), [`IGNORE_INDEX`](../../components/loss.md#IGNORE_INDEX)  (+38 more)
- used by: [`_run_cpu_verification`](base_distributed_device_test.md#_run_cpu_verification), [`start_trainer`](train_minimal.md#start_trainer), [`__call__`](base_distributed_device_test.md#DistributedTrainWithRecorder.__call__)  (1 test-only)

## Functions
- <a id="_gather_along_first_dim"></a>`_gather_along_first_dim(tensor: torch.Tensor, group)` — [`L48`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L48) — Gathers a standard PyTorch tensor along its first (batch) dimension across ranks.
- <a id="start_trainer"></a>`start_trainer(config: JobConfig)` — [`L507`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L507) — Initializes and starts the training process. — documented in [tpu-trainer-and-job-config](../../../../concepts/tpu-trainer-and-job-config.md)

## Module values
- <a id="JobConfig"></a>`JobConfig` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L41)
- <a id="ParallelDims"></a>`ParallelDims` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L42)
- <a id="TORCH_DTYPE_MAP"></a>`TORCH_DTYPE_MAP` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L40)
- <a id="TrainStepCallback"></a>`TrainStepCallback` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L45)
- <a id="logger"></a>`logger` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train_minimal.py#L43)

