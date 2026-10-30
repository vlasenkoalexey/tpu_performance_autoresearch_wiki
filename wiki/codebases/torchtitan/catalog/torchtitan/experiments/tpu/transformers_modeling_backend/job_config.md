---
title: 'Module: torchtitan/experiments/tpu/transformers_modeling_backend/job_config.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/transformers_modeling_backend/job_config.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.transformers_modeling_backend.job_config`/TPUTransformersBackendConfig#
symbols:
  TPUTransformersBackendConfig: ''
  TPUTransformersBackendConfig.hf_model: hf_model.
  TPUTransformersBackendConfig.hf_config_overrides: hf_config_overrides.
---
# Module: [`torchtitan/experiments/tpu/transformers_modeling_backend/job_config.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/job_config.py)

## Classes
### <a id="TPUTransformersBackendConfig"></a>`TPUTransformersBackendConfig`  ·  implements/extends TPUTrainerConfig
- def: [`torchtitan/experiments/tpu/transformers_modeling_backend/job_config.py:9`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/job_config.py#L9)
- doc: A TPU job config that also carries the HuggingFace model id.
- signature: `class TPUTransformersBackendConfig(TPUTrainerConfig):`
- members:
  - <a id="TPUTransformersBackendConfig.hf_config_overrides"></a>`hf_config_overrides` — [`L30`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/job_config.py#L30)
  - <a id="TPUTransformersBackendConfig.hf_model"></a>`hf_model` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/job_config.py#L24)
- uses (calls/refs, reference-scoped): [`TPUTrainerConfig`](../tpu_job_config.md#TPUTrainerConfig)
- used by: [`_tpu_hf_config`](config_registry.md#_tpu_hf_config), [`TPUTrainerConfig`](../tpu_job_config.md#TPUTrainerConfig), [`as_cpu_reference`](config_registry.md#as_cpu_reference), [`hf_debugmodel`](config_registry.md#hf_debugmodel), [`hf_debugmodel_kernels_sdpa`](config_registry.md#hf_debugmodel_kernels_sdpa), [`hf_debugmodel_kernels_splash`](config_registry.md#hf_debugmodel_kernels_splash), [`hf_debugmodel_max`](config_registry.md#hf_debugmodel_max), [`hf_full_max`](config_registry.md#hf_full_max), [`hf_full_max_plain_ce`](config_registry.md#hf_full_max_plain_ce), [`hf_moe_auto`](config_registry.md#hf_moe_auto), [`hf_moe_auto_compile`](config_registry.md#hf_moe_auto_compile), [`hf_moe_auto_eager`](config_registry.md#hf_moe_auto_eager)

