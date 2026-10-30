---
title: 'Module: torchtitan/experiments/transformers_modeling_backend/config_registry.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/transformers_modeling_backend/config_registry.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.transformers_modeling_backend.config_registry`/
symbols:
  transformers_modeling_backend_sft_full: transformers_modeling_backend_sft_full().
  transformers_modeling_backend_sft_debugmodel: transformers_modeling_backend_sft_debugmodel().
  transformers_modeling_backend_debugmodel: transformers_modeling_backend_debugmodel().
  transformers_modeling_backend_debugmodel_moe: transformers_modeling_backend_debugmodel_moe().
  transformers_modeling_backend_full: transformers_modeling_backend_full().
  transformers_modeling_backend_full_moe: transformers_modeling_backend_full_moe().
  TransformersBackendConfig: TransformersBackendConfig#
  TransformersBackendConfig.hf_model: TransformersBackendConfig#hf_model.
  transformers_modeling_backend_sft_full.process_sample: transformers_modeling_backend_sft_full().process_sample().
  transformers_modeling_backend_sft_debugmodel.process_sample: transformers_modeling_backend_sft_debugmodel().process_sample().
---
# Module: [`torchtitan/experiments/transformers_modeling_backend/config_registry.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/config_registry.py)

## Classes
### <a id="TransformersBackendConfig"></a>`TransformersBackendConfig`  ·  implements/extends Config
- def: [`torchtitan/experiments/transformers_modeling_backend/config_registry.py:31`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/config_registry.py#L31)
- signature: `class TransformersBackendConfig(Trainer.Config):`
- members:
  - <a id="TransformersBackendConfig.hf_model"></a>`hf_model` — [`L32`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/config_registry.py#L32) — ---
- uses (calls/refs, reference-scoped): [`Trainer`](../../trainer.md#Trainer), [`Config`](../../trainer.md#Trainer.Config)
- used by: [`transformers_modeling_backend_sft_full`](config_registry.md#transformers_modeling_backend_sft_full), [`transformers_modeling_backend_sft_debugmodel`](config_registry.md#transformers_modeling_backend_sft_debugmodel), [`transformers_modeling_backend_debugmodel`](config_registry.md#transformers_modeling_backend_debugmodel), [`transformers_modeling_backend_debugmodel_moe`](config_registry.md#transformers_modeling_backend_debugmodel_moe), [`transformers_modeling_backend_full`](config_registry.md#transformers_modeling_backend_full), [`transformers_modeling_backend_full_moe`](config_registry.md#transformers_modeling_backend_full_moe)  (5 test-only)

## Functions
- <a id="transformers_modeling_backend_sft_full.process_sample"></a>`process_sample(sample)` — [`L188`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/config_registry.py#L188)
- <a id="transformers_modeling_backend_sft_debugmodel.process_sample"></a>`process_sample(sample)` — [`L247`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/config_registry.py#L247)
- <a id="transformers_modeling_backend_debugmodel"></a>`transformers_modeling_backend_debugmodel(seq_len: int = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L36`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/config_registry.py#L36)
- <a id="transformers_modeling_backend_debugmodel_moe"></a>`transformers_modeling_backend_debugmodel_moe(seq_len: int = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/config_registry.py#L74)
- <a id="transformers_modeling_backend_full"></a>`transformers_modeling_backend_full(seq_len: int = 2048)` — [`L146`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/config_registry.py#L146)
- <a id="transformers_modeling_backend_full_moe"></a>`transformers_modeling_backend_full_moe(seq_len: int = 2048)` — [`L111`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/config_registry.py#L111)
- <a id="transformers_modeling_backend_sft_debugmodel"></a>`transformers_modeling_backend_sft_debugmodel(seq_len: int = 1024)` — [`L242`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/config_registry.py#L242) — SFT debug config for the transformers backend.
- <a id="transformers_modeling_backend_sft_full"></a>`transformers_modeling_backend_sft_full(seq_len: int = 2048)` — [`L183`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/config_registry.py#L183) — SFT config with real HF pretrained weights loaded via initial_load_in_hf.

