---
title: 'Module: torchtitan/experiments/tpu/qwen3/__init__.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/qwen3/__init__.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.qwen3`/
symbols:
  _8b_tpu: _8b_tpu().
  _testmodel_moe: _testmodel_moe().
  model_registry: model_registry().
  qwen3_configs: qwen3_configs.
  _upstream_flavor: _upstream_flavor().
  TESTMODEL_MAX_CONTEXT_LENGTH: TESTMODEL_MAX_CONTEXT_LENGTH.
  _8B_MAX_CONTEXT_LENGTH: _8B_MAX_CONTEXT_LENGTH.
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/qwen3/__init__.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/__init__.py)

## Functions
- <a id="_8b_tpu"></a>`_8b_tpu(attn_backend: str = "sdpa")` — [`L72`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/__init__.py#L72) — TPU-specific Qwen3 8B model configuration.
- <a id="_testmodel_moe"></a>`_testmodel_moe(attn_backend: str = "sdpa", moe_comm_backend: str = "standard")` — [`L29`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/__init__.py#L29)
- <a id="_upstream_flavor"></a>`_upstream_flavor(flavor: str, attn_backend: str)` — [`L116`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/__init__.py#L116) — Builds an upstream qwen3 flavor at that flavor's full context length.
- <a id="model_registry"></a>`model_registry(flavor: str, attn_backend: str = "flex", moe_comm_backend: str | None = None, converters: list = None)` — [`L144`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/__init__.py#L144)

## Module values
- <a id="TESTMODEL_MAX_CONTEXT_LENGTH"></a>`TESTMODEL_MAX_CONTEXT_LENGTH` — [`L25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/__init__.py#L25)
- <a id="_8B_MAX_CONTEXT_LENGTH"></a>`_8B_MAX_CONTEXT_LENGTH` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/__init__.py#L26)
- <a id="__all__"></a>`__all__` — [`L12`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/__init__.py#L12)
- <a id="qwen3_configs"></a>`qwen3_configs` — [`L130`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/__init__.py#L130)

