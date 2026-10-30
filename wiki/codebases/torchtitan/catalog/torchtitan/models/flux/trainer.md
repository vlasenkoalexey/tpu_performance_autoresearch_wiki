---
title: 'Module: torchtitan/models/flux/trainer.py'
type: catalog
provenance: extracted
module: torchtitan/models/flux/trainer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.flux.trainer`/FluxTrainer#
symbols:
  FluxTrainer.t5_encoder: t5_encoder.
  FluxTrainer.train_step: train_step().
  FluxTrainer.forward_backward_step: forward_backward_step().
  FluxTrainer._dtype: _dtype.
  FluxTrainer.__init__: __init__().
  FluxTrainer.batch_generator: batch_generator().
  FluxTrainer: ''
  FluxTrainer.Config.encoder: Config#encoder.
  FluxTrainer.Config: Config#
  FluxTrainer.Config.tokenizer: Config#tokenizer.
  FluxTrainer.Config.inference: Config#inference.
  FluxTrainer.clip_encoder: clip_encoder.
  FluxTrainer.autoencoder: autoencoder.
---
# Module: [`torchtitan/models/flux/trainer.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/trainer.py)

## Classes
### <a id="FluxTrainer"></a>`FluxTrainer`  ·  implements/extends Trainer
- def: [`torchtitan/models/flux/trainer.py:38`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/trainer.py#L38) — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)
- signature: `class FluxTrainer(Trainer):`
- members:
  - <a id="FluxTrainer.batch_generator"></a>`batch_generator(self, data_iterable: Iterable[TrainerBatch])` — [`L195`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/trainer.py#L195) — Override to count transformer tokens (image patches + text tokens) — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)
  - <a id="FluxTrainer.forward_backward_step"></a>`forward_backward_step(self, *, input_dict: dict[str, Any] | list[dict[str, Any]], global_valid_tokens: torch.Tensor | None = None)` — [`L216`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/trainer.py#L216) — Perform a single forward and backward pass through the model. — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)
  - <a id="FluxTrainer.train_step"></a>`train_step(self, data_iterator: Iterator[dict[str, Any]])` — [`L357`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/trainer.py#L357) — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)
  - <a id="FluxTrainer.autoencoder"></a>`autoencoder` — [`L90`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/trainer.py#L90)
  - <a id="FluxTrainer.clip_encoder"></a>`clip_encoder` — [`L91`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/trainer.py#L91)
  - <a id="FluxTrainer.t5_encoder"></a>`t5_encoder` — [`L92`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/trainer.py#L92) — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)
- protocol/private: <a id="FluxTrainer.__init__"></a>`__init__`[`L49`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/trainer.py#L49), <a id="FluxTrainer._dtype"></a>`_dtype`[`L71`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/trainer.py#L71)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`parallelism`](../../trainer.md#Trainer.Config.parallelism), [`build`](../../protocols/module.md#Module.Config.build), [`training`](../../trainer.md#Trainer.Config.training), [`model_spec`](../../trainer.md#Trainer.Config.model_spec), [`Trainer`](../../trainer.md#Trainer), [`model`](../../protocols/model_spec.md#ModelSpec.model), [`max_context_length`](../../config/configs.md#TrainingConfig.max_context_length), [`num_tokens_per_microbatch_per_dp_rank`](../../config/configs.md#TrainingConfig.num_tokens_per_microbatch_per_dp_rank), [`steps`](../../config/configs.md#TrainingConfig.steps), [`TORCH_DTYPE_MAP`](../../config/__init__.md#TORCH_DTYPE_MAP), [`dataloader`](../../trainer.md#Trainer.Config.dataloader), [`spmd_backend`](../../config/configs.md#ParallelismConfig.spmd_backend), [`config`](../../trainer.md#Trainer.config), [`get_mesh`](../../distributed/parallel_dims.md#ParallelDims.get_mesh), [`log`](../../components/metrics.md#MetricsProcessor.log), [`model_parts`](../../trainer.md#Trainer.model_parts), [`parallelize_encoders`](parallelize.md#parallelize_encoders), [`get_optional_mesh`](../../distributed/parallel_dims.md#ParallelDims.get_optional_mesh), [`cp`](../../distributed/parallel_dims.md#ParallelDims.cp), [`device`](../../trainer.md#Trainer.device), [`mixed_precision_param`](../../config/configs.md#TrainingConfig.mixed_precision_param), [`validator`](../../trainer.md#Trainer.Config.validator), [`set_determinism`](../../distributed/utils.md#set_determinism), [`debug`](../../trainer.md#Trainer.Config.debug), [`parallel_dims`](../../trainer.md#Trainer.parallel_dims), [`step`](../../trainer.md#Trainer.step), [`cp_enabled`](../../distributed/parallel_dims.md#ParallelDims.cp_enabled), [`metrics_processor`](../../trainer.md#Trainer.metrics_processor), [`optimizers`](../../trainer.md#Trainer.optimizers), [`ep_enabled`](../../distributed/parallel_dims.md#ParallelDims.ep_enabled), [`dump_folder`](../../trainer.md#Trainer.Config.dump_folder), [`FluxModel`](model/model.md#FluxModel), [`loss_fn`](../../trainer.md#Trainer.loss_fn), [`__init__`](../../trainer.md#Trainer.__init__), [`ntokens_seen`](../../trainer.md#Trainer.ntokens_seen), [`enable`](../../components/validate.md#Validator.Config.enable), [`dp_enabled`](../../distributed/parallel_dims.md#ParallelDims.dp_enabled), [`dataloader`](../../trainer.md#Trainer.dataloader), [`lr_schedulers`](../../trainer.md#Trainer.lr_schedulers)  (+49 more)
- used by: [`Trainer`](../../trainer.md#Trainer), [`flux_debugmodel`](config_registry.md#flux_debugmodel), [`flux_dev`](config_registry.md#flux_dev), [`flux_schnell`](config_registry.md#flux_schnell), [`train_step`](../../trainer.md#Trainer.train_step), [`start_trainer`](../../experiments/tpu/train.md#start_trainer), [`inference`](inference/infer.md#inference), [`forward_backward_step`](../../trainer.md#Trainer.forward_backward_step), [`flux_testmodel`](../../experiments/tpu/flux/config_registry.md#flux_testmodel), [`flux_dev_mxfp8`](config_registry.md#flux_dev_mxfp8), [`flux_schnell_mxfp8`](config_registry.md#flux_schnell_mxfp8), [`batch_generator`](../../trainer.md#Trainer.batch_generator)

### <a id="FluxTrainer.Config"></a>`FluxTrainer.Config`  ·  implements/extends TPUTrainerConfig
- def: [`torchtitan/models/flux/trainer.py:40`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/trainer.py#L40)
- signature: `class Config(TPUTrainerConfig):`
- members:
  - <a id="FluxTrainer.Config.encoder"></a>`encoder` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/trainer.py#L45) — ---
  - <a id="FluxTrainer.Config.inference"></a>`inference` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/trainer.py#L47)
  - <a id="FluxTrainer.Config.tokenizer"></a>`tokenizer` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/trainer.py#L42)
- uses (calls/refs, reference-scoped): [`TPUTrainerConfig`](../../experiments/tpu/tpu_job_config.md#TPUTrainerConfig), [`FluxTokenizerContainer`](tokenizer.md#FluxTokenizerContainer), [`Config`](tokenizer.md#FluxTokenizerContainer.Config), [`Inference`](configs.md#Inference), [`FluxEncoderConfig`](configs.md#FluxEncoderConfig)
- used by: [`flux_debugmodel`](config_registry.md#flux_debugmodel), [`flux_dev`](config_registry.md#flux_dev), [`flux_schnell`](config_registry.md#flux_schnell), [`TPUTrainerConfig`](../../experiments/tpu/tpu_job_config.md#TPUTrainerConfig), [`t5_encoder`](trainer.md#FluxTrainer.t5_encoder), [`inference`](inference/infer.md#inference), [`flux_testmodel`](../../experiments/tpu/flux/config_registry.md#flux_testmodel), [`flux_dev_mxfp8`](config_registry.md#flux_dev_mxfp8), [`flux_schnell_mxfp8`](config_registry.md#flux_schnell_mxfp8), [`__init__`](trainer.md#FluxTrainer.__init__)

