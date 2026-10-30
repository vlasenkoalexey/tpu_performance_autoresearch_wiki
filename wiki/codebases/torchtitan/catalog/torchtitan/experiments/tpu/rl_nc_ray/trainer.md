---
title: 'Module: torchtitan/experiments/tpu/rl_nc_ray/trainer.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/rl_nc_ray/trainer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.rl_nc_ray.trainer`/
symbols:
  RayTPUPolicyTrainer._build_model: RayTPUPolicyTrainer#_build_model().
  RayTPUPolicyTrainer._load_initial_hf_weights: RayTPUPolicyTrainer#_load_initial_hf_weights().
  RayTPUPolicyTrainer.profiler: RayTPUPolicyTrainer#profiler.
  RayTPUPolicyTrainer.__init__: RayTPUPolicyTrainer#__init__().
  RayTPUPolicyTrainer.get_model_state_dict: RayTPUPolicyTrainer#get_model_state_dict().
  RayTPUPolicyTrainer.optim_step: RayTPUPolicyTrainer#optim_step().
  RayTPUPolicyTrainer: RayTPUPolicyTrainer#
  patch_torch_and_dist_for_trainer: patch_torch_and_dist_for_trainer().
  load_initial_hf_weights_on_cpu: load_initial_hf_weights_on_cpu().
  RayTPUPolicyTrainer.finish: RayTPUPolicyTrainer#finish().
  load_initial_hf_weights_on_cpu.handle_dtensor_copy: load_initial_hf_weights_on_cpu().handle_dtensor_copy().
  logger: logger.
  patch_torch_and_dist_for_trainer.patched_std: patch_torch_and_dist_for_trainer().patched_std().
  PAD_LEN: PAD_LEN.
  MAX_SEQS: MAX_SEQS.
---
# Module: [`torchtitan/experiments/tpu/rl_nc_ray/trainer.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/trainer.py)

## Classes
### <a id="RayTPUPolicyTrainer"></a>`RayTPUPolicyTrainer`  ·  implements/extends PolicyTrainer
- def: [`torchtitan/experiments/tpu/rl_nc_ray/trainer.py:120`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/trainer.py#L120)
- signature: `class RayTPUPolicyTrainer(PolicyTrainer):`
- members:
  - <a id="RayTPUPolicyTrainer.finish"></a>`finish(self)` — [`L277`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/trainer.py#L277)
  - <a id="RayTPUPolicyTrainer.get_model_state_dict"></a>`get_model_state_dict(self)` — [`L233`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/trainer.py#L233) — Ray-native weight extraction. Returns state dict on CPU.
  - <a id="RayTPUPolicyTrainer.optim_step"></a>`optim_step(self)` — [`L271`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/trainer.py#L271)
  - <a id="RayTPUPolicyTrainer.profiler"></a>`profiler` — [`L154`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/trainer.py#L154)
- protocol/private: <a id="RayTPUPolicyTrainer.__init__"></a>`__init__`[`L122`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/trainer.py#L122), <a id="RayTPUPolicyTrainer._build_model"></a>`_build_model`[`L162`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/trainer.py#L162), <a id="RayTPUPolicyTrainer._load_initial_hf_weights"></a>`_load_initial_hf_weights`[`L216`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/trainer.py#L216)
- uses (calls/refs, reference-scoped): [`build`](../../../protocols/module.md#Module.Config.build), [`model`](../../../protocols/model_spec.md#ModelSpec.model), [`max_context_length`](../../../config/configs.md#TrainingConfig.max_context_length), [`TORCH_DTYPE_MAP`](../../../config/__init__.md#TORCH_DTYPE_MAP), [`apply_overrides`](../../../config/override.md#apply_overrides), [`parallelize_fn`](../../../protocols/model_spec.md#ModelSpec.parallelize_fn), [`imports`](../../../config/override.md#OverrideConfig.imports), [`optim_step`](../../rl/actors/trainer.md#PolicyTrainer.optim_step), [`device_type`](../../../tools/utils.md#device_type), [`training`](../../rl/actors/trainer.md#PolicyTrainer.Config.training), [`parallelism`](../../rl/actors/trainer.md#PolicyTrainer.Config.parallelism), [`PolicyTrainer`](../../rl/actors/trainer.md#PolicyTrainer), [`to_hf`](../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.to_hf), [`from_hf`](../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.from_hf), [`device_module`](../../../tools/utils.md#device_module), [`__init__`](../../rl/actors/trainer.md#PolicyTrainer.__init__), [`parallel_dims`](../../rl/actors/trainer.md#PolicyTrainer.parallel_dims), [`dtype`](../../../config/configs.md#TrainingConfig.dtype), [`dp_enabled`](../../../distributed/parallel_dims.md#ParallelDims.dp_enabled), [`sd_adapter`](../../rl/actors/trainer.md#PolicyTrainer.sd_adapter), [`ac_config`](../../rl/actors/trainer.md#PolicyTrainer.Config.ac_config), [`patch_varlen_attention`](padding_packing_utils.md#patch_varlen_attention), [`prepare_trainer_state_dict`](weight_transfer_utils.md#prepare_trainer_state_dict), [`update_from_config`](../../../protocols/model.md#BaseModel.Config.update_from_config), [`dump_folder`](../../rl/actors/trainer.md#PolicyTrainer.Config.dump_folder), [`get_hf_storage_reader`](../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.get_hf_storage_reader), [`set_default_dtype`](../../../tools/utils.md#set_default_dtype), [`override`](../../rl/actors/trainer.md#PolicyTrainer.Config.override), [`model`](../../rl/actors/trainer.md#PolicyTrainer.model), [`load_initial_hf_weights_on_cpu`](trainer.md#load_initial_hf_weights_on_cpu), [`patch_torch_and_dist_for_trainer`](trainer.md#patch_torch_and_dist_for_trainer), [`config`](../../rl/actors/trainer.md#PolicyTrainer.config), [`compile_config`](../../rl/actors/trainer.md#PolicyTrainer.compile_config), [`logger`](trainer.md#logger)
- used by: [`_multi_node`](grpo.md#RayController._multi_node), [`_build_model`](../../rl/actors/trainer.md#PolicyTrainer._build_model), [`optim_step`](../../rl/actors/trainer.md#PolicyTrainer.optim_step), [`PolicyTrainer`](../../rl/actors/trainer.md#PolicyTrainer)

## Functions
- <a id="load_initial_hf_weights_on_cpu.handle_dtensor_copy"></a>`handle_dtensor_copy(target_dtensor, source_tensor)` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/trainer.py#L86)
- <a id="load_initial_hf_weights_on_cpu"></a>`load_initial_hf_weights_on_cpu(model, torchtitan_state_dict: dict)` — [`L76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/trainer.py#L76) — Manually copies initial HF state dict tensors into model's DTensors on CPU.
- <a id="patch_torch_and_dist_for_trainer"></a>`patch_torch_and_dist_for_trainer(target_device: str)` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/trainer.py#L36) — Apply TPU/CPU-specific PyTorch and distributed backend monkey-patches to PolicyTrainer.
- <a id="patch_torch_and_dist_for_trainer.patched_std"></a>`patched_std(self, *args, **kwargs)` — [`L57`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/trainer.py#L57)

## Module values
- <a id="MAX_SEQS"></a>`MAX_SEQS` — [`L33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/trainer.py#L33)
- <a id="PAD_LEN"></a>`PAD_LEN` — [`L32`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/trainer.py#L32)
- <a id="logger"></a>`logger` — [`L29`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/trainer.py#L29)

