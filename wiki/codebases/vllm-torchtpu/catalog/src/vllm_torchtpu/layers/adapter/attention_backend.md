---
title: 'Module: src/vllm_torchtpu/layers/adapter/attention_backend.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/attention_backend.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.attention_backend`/
symbols:
  is_registered_attention_backend: is_registered_attention_backend().
  check_attention_backend_config: check_attention_backend_config().
  register_attention_backend: register_attention_backend().
  _REGISTERED_BACKENDS._REGISTERED_BACKENDS: _REGISTERED_BACKENDS._REGISTERED_BACKENDS.
---
# Module: [`src/vllm_torchtpu/layers/adapter/attention_backend.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/attention_backend.py)

## Functions
- <a id="check_attention_backend_config"></a>`check_attention_backend_config(vllm_config: VllmConfig)` — [`L65`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/attention_backend.py#L65) — Raise if a registered backend is selected for an engine whose processes
- <a id="is_registered_attention_backend"></a>`is_registered_attention_backend(backend: AttentionBackendEnum | None)` — [`L60`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/attention_backend.py#L60) — Whether vLLM's backend is one of register_attention_backend.
- <a id="register_attention_backend"></a>`register_attention_backend(name: str, *, vllm_backend: str)` — [`L39`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/attention_backend.py#L39) — Register a new backend for `--attention-backend <name>`.

## Module values
- <a id="_REGISTERED_BACKENDS._REGISTERED_BACKENDS"></a>`_REGISTERED_BACKENDS` — [`L36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/attention_backend.py#L36)

