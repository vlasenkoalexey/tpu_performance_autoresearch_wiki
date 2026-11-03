---
title: 'Module: src/vllm_torchtpu/platforms/pp_validation.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/platforms/pp_validation.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.platforms.pp_validation`/
symbols:
  validate_pipeline_parallel_config: validate_pipeline_parallel_config().
  _non_raiden_connectors: _non_raiden_connectors().
  _legacy_ray_executor: _legacy_ray_executor().
  _stage_without_full_attention: _stage_without_full_attention().
  _torch_tpu_builds_stage_meshes: _torch_tpu_builds_stage_meshes().
  _FULL_ATTENTION_LAYER_TYPES: _FULL_ATTENTION_LAYER_TYPES.
  _RAIDEN_CONNECTORS: _RAIDEN_CONNECTORS.
  _kv_connector_names: _kv_connector_names().
---
# Module: [`src/vllm_torchtpu/platforms/pp_validation.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pp_validation.py)

## Functions
- <a id="_kv_connector_names"></a>`_kv_connector_names(kv_transfer_config: Any)` — [`L58`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pp_validation.py#L58) — The connector a config names, or the children of a TPUMultiConnector.
- <a id="_legacy_ray_executor"></a>`_legacy_ray_executor()` — [`L19`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pp_validation.py#L19)
- <a id="_non_raiden_connectors"></a>`_non_raiden_connectors(kv_transfer_config: Any)` — [`L67`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pp_validation.py#L67) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
- <a id="_stage_without_full_attention"></a>`_stage_without_full_attention(vllm_config: Any)` — [`L75`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pp_validation.py#L75) — Describe the first stage holding no full-attention layer, or None.
- <a id="_torch_tpu_builds_stage_meshes"></a>`_torch_tpu_builds_stage_meshes()` — [`L30`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pp_validation.py#L30) — Whether the installed torch_tpu builds a Pallas mesh over a pipeline
- <a id="validate_pipeline_parallel_config"></a>`validate_pipeline_parallel_config(vllm_config: Any)` — [`L99`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pp_validation.py#L99) — Reject configurations the TPU pipeline-parallel path does not serve. — documented in [tpu-platform](../../../../concepts/tpu-platform.md)

## Module values
- <a id="_FULL_ATTENTION_LAYER_TYPES"></a>`_FULL_ATTENTION_LAYER_TYPES` — [`L45`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pp_validation.py#L45)
- <a id="_RAIDEN_CONNECTORS"></a>`_RAIDEN_CONNECTORS` — [`L55`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/pp_validation.py#L55)

