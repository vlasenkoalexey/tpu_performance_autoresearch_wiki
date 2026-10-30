---
title: 'Module: torchtitan/experiments/tpu/train.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/train.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.train`/
symbols:
  start_trainer: start_trainer().
  TPUTrainer.forward_backward_step: TPUTrainer#forward_backward_step().
  TPUTrainer._compiled_grad_norm: TPUTrainer#_compiled_grad_norm.
  _apply_flux_img_size: _apply_flux_img_size().
  TPUTrainer._clip_grad_norm: TPUTrainer#_clip_grad_norm().
  start_trainer.patched_parallelize: start_trainer().patched_parallelize().
  TPUTrainer.__init__: TPUTrainer#__init__().
  TPUTrainer: TPUTrainer#
  _fit_rope_to_context: _fit_rope_to_context().
  _apply_flux_img_size._with_img_size: _apply_flux_img_size()._with_img_size().
---
# Module: [`torchtitan/experiments/tpu/train.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train.py)

## Classes
### <a id="TPUTrainer"></a>`TPUTrainer`  ·  implements/extends Trainer
- def: [`torchtitan/experiments/tpu/train.py:36`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train.py#L36) — documented in [tpu-trainer-and-job-config](../../../../concepts/tpu-trainer-and-job-config.md)
- doc: Trainer subclass with TPU-specific optimizations.
- signature: `class TPUTrainer(torchtitan.train.Trainer):`
- members:
  - <a id="TPUTrainer.forward_backward_step"></a>`forward_backward_step(self, *, input_dict: dict[str, Any] | list[dict[str, Any]], global_valid_tokens: torch.Tensor)` — [`L81`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train.py#L81) — documented in [trainer-and-train-loop](../../../../concepts/trainer-and-train-loop.md)
- protocol/private: <a id="TPUTrainer.__init__"></a>`__init__`[`L55`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train.py#L55), <a id="TPUTrainer._clip_grad_norm"></a>`_clip_grad_norm`[`L72`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train.py#L72), <a id="TPUTrainer._compiled_grad_norm"></a>`_compiled_grad_norm`[`L58`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train.py#L58)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`parallelism`](../../trainer.md#Trainer.Config.parallelism), [`training`](../../trainer.md#Trainer.Config.training), [`Trainer`](../../trainer.md#Trainer), [`Configurable`](../../config/configurable.md#Configurable), [`max_context_length`](../../config/configs.md#TrainingConfig.max_context_length), [`TPUTrainerConfig`](tpu_job_config.md#TPUTrainerConfig), [`Config`](../../config/configurable.md#Configurable.Config), [`BaseModel`](../../protocols/model.md#BaseModel), [`config`](../../trainer.md#Trainer.config), [`set_unflatten_seq_len`](unflatten_shim.md#set_unflatten_seq_len), [`compile`](tpu_job_config.md#TPUTrainerConfig.compile), [`model_parts`](../../trainer.md#Trainer.model_parts), [`forward_backward_step`](../../trainer.md#Trainer.forward_backward_step), [`pp_enabled`](../../distributed/parallel_dims.md#ParallelDims.pp_enabled), [`parallel_dims`](../../trainer.md#Trainer.parallel_dims), [`tpu_config`](tpu_job_config.md#TPUTrainerConfig.tpu_config), [`build_cross_entropy_loss`](loss.md#build_cross_entropy_loss), [`clip_grad_norm_`](grad_norm.md#CompiledGradNorm.clip_grad_norm_), [`_clip_grad_norm`](../../trainer.md#Trainer._clip_grad_norm), [`loss_fn`](../../trainer.md#Trainer.loss_fn), [`__init__`](../../trainer.md#Trainer.__init__), [`ntokens_seen`](../../trainer.md#Trainer.ntokens_seen), [`preprocess_inputs`](../../protocols/model.md#BaseModel.preprocess_inputs), [`dataloader`](../../trainer.md#Trainer.dataloader), [`train_context`](../../trainer.md#Trainer.train_context), [`max_norm`](../../config/configs.md#TrainingConfig.max_norm), [`apply_compiled_optimizer`](compiled_optimizers/separate_graph.md#apply_compiled_optimizer), [`compile_grad_norm`](tpu_job_config.md#TpuTrainerCompileConfig.compile_grad_norm), [`materialize_forward_before_backward`](tpu_job_config.md#TpuTrainerCompileConfig.materialize_forward_before_backward), [`CompiledGradNorm`](grad_norm.md#CompiledGradNorm), [`optimizer_compile`](tpu_job_config.md#TpuTrainerCompileConfig.optimizer_compile), [`enable_amp`](tpu_job_config.md#TPUConfig.enable_amp), [`max_num_documents`](../../components/data/loader.md#BaseDataLoader.max_num_documents)
- used by: [`Trainer`](../../trainer.md#Trainer), [`start_trainer`](train.md#start_trainer), [`forward_backward_step`](../../trainer.md#Trainer.forward_backward_step), [`_clip_grad_norm`](../../trainer.md#Trainer._clip_grad_norm)  (2 test-only)

## Functions
- <a id="_apply_flux_img_size"></a>`_apply_flux_img_size(train_config: tpu_job_config_module.TPUTrainerConfig)` — [`L143`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train.py#L143) — Applies `--flux.img_size` to the dataset processors and context length.
- <a id="_fit_rope_to_context"></a>`_fit_rope_to_context(model_config: Any, max_context_length: int)` — [`L185`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train.py#L185) — Sizes every RoPE cache to `max_context_length` (pre-d771abb0 behaviour).
- <a id="_apply_flux_img_size._with_img_size"></a>`_with_img_size(dataset)` — [`L153`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train.py#L153)
- <a id="start_trainer.patched_parallelize"></a>`patched_parallelize(model, *args, **kwargs)` — [`L282`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train.py#L282)
- <a id="start_trainer"></a>`start_trainer(train_config: tpu_job_config_module.TPUTrainerConfig | TpuGraphTrainer.Config)` — [`L208`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/train.py#L208) — Starts the training process. — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)

