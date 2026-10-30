---
title: 'Module: torchtitan/models/llama3/__init__.py'
type: catalog
provenance: extracted
module: torchtitan/models/llama3/__init__.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.llama3`/
symbols:
  _1b: _1b().
  _3b: _3b().
  model_registry: model_registry().
  _debugmodel: _debugmodel().
  _8b: _8b().
  _70b: _70b().
  _405b: _405b().
  _build_llama3_layers: _build_llama3_layers().
  llama3_configs: llama3_configs.
  _NORM_INIT: _NORM_INIT.
  _output_linear_init: _output_linear_init().
  _EMBEDDING_INIT: _EMBEDDING_INIT.
  _EMBEDDING_SKIP_INIT: _EMBEDDING_SKIP_INIT.
  _depth_init: _depth_init().
  _LINEAR_INIT: _LINEAR_INIT.
  __all__: __all__.
---
# Module: [`torchtitan/models/llama3/__init__.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/__init__.py)

## Functions
- <a id="_1b"></a>`_1b(attn_backend: str, tp_gemm_backend: TpGemmBackend = "default", *, seq_len: int)` — [`L151`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/__init__.py#L151) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="_3b"></a>`_3b(attn_backend: str, tp_gemm_backend: TpGemmBackend = "default", *, seq_len: int)` — [`L198`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/__init__.py#L198) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="_405b"></a>`_405b(attn_backend: str, tp_gemm_backend: TpGemmBackend = "default", *, seq_len: int)` — [`L333`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/__init__.py#L333) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="_70b"></a>`_70b(attn_backend: str, tp_gemm_backend: TpGemmBackend = "default", *, seq_len: int)` — [`L289`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/__init__.py#L289) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="_8b"></a>`_8b(attn_backend: str, tp_gemm_backend: TpGemmBackend = "default", *, seq_len: int)` — [`L245`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/__init__.py#L245) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="_build_llama3_layers"></a>`_build_llama3_layers(*, n_layers: int, dim: int, n_heads: int, hidden_dim: int, rope: RoPE.Config, n_kv_heads: int | None = None, fuse_qkv: bool = True, attn_backend: str, tp_gemm_backend: TpGemmBackend = "default")` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/__init__.py#L69) — Build a list of per-layer TransformerBlock configs with depth-scaled inits. — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="_debugmodel"></a>`_debugmodel(attn_backend: str, tp_gemm_backend: TpGemmBackend = "default", *, seq_len: int)` — [`L114`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/__init__.py#L114) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="_depth_init"></a>`_depth_init(layer_id: int)` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/__init__.py#L62)
- <a id="_output_linear_init"></a>`_output_linear_init(dim: int)` — [`L54`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/__init__.py#L54)
- <a id="model_registry"></a>`model_registry(flavor: str, *, seq_len: int | None = None, attn_backend: str = "flex", tp_gemm_backend: TpGemmBackend = "default", converters: list[ModelConfigConverter.Config] | None = None)` — [`L387`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/__init__.py#L387) — documented in [llama3-model](../../../../concepts/llama3-model.md)

## Module values
- <a id="_EMBEDDING_INIT"></a>`_EMBEDDING_INIT` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/__init__.py#L50)
- <a id="_EMBEDDING_SKIP_INIT"></a>`_EMBEDDING_SKIP_INIT` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/__init__.py#L51)
- <a id="_LINEAR_INIT"></a>`_LINEAR_INIT` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/__init__.py#L45)
- <a id="_NORM_INIT"></a>`_NORM_INIT` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/__init__.py#L49) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="__all__"></a>`__all__` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/__init__.py#L38)
- <a id="llama3_configs"></a>`llama3_configs` — [`L377`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/__init__.py#L377) — documented in [llama3-model](../../../../concepts/llama3-model.md)

