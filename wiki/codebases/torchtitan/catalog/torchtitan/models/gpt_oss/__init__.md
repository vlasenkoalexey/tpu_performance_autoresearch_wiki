---
title: 'Module: torchtitan/models/gpt_oss/__init__.py'
type: catalog
provenance: extracted
module: torchtitan/models/gpt_oss/__init__.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.gpt_oss`/
symbols:
  _build_gptoss_layers: _build_gptoss_layers().
  _make_gptoss_attn_config: _make_gptoss_attn_config().
  _debugmodel: _debugmodel().
  _20b: _20b().
  _120b: _120b().
  model_registry: model_registry().
  _make_gptoss_experts_config: _make_gptoss_experts_config().
  gptoss_configs: gptoss_configs.
  _depth_init: _depth_init().
  _NORM_INIT: _NORM_INIT.
  _EMBEDDING_INIT: _EMBEDDING_INIT.
  _output_linear_init: _output_linear_init().
  __all__: __all__.
---
# Module: [`torchtitan/models/gpt_oss/__init__.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/__init__.py)

## Functions
- <a id="_120b"></a>`_120b(moe_comm_backend: str, attn_backend: str = "varlen", *, seq_len: int)` — [`L342`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/__init__.py#L342) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- <a id="_20b"></a>`_20b(moe_comm_backend: str, attn_backend: str = "varlen", *, seq_len: int)` — [`L296`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/__init__.py#L296) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- <a id="_build_gptoss_layers"></a>`_build_gptoss_layers(*, dim: int, n_layers: int, hidden_dim: int, num_experts: int, top_k: int, load_balance_coeff: float, attn_backend: str = "varlen", fuse_qkv: bool = True, moe_comm_backend: str, non_blocking_capacity_factor: float | None = None, rope: RoPE.Config)` — [`L185`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/__init__.py#L185) — Build per-layer configs for GPT-OSS. — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- <a id="_debugmodel"></a>`_debugmodel(moe_comm_backend: str, attn_backend: str = "varlen", *, seq_len: int)` — [`L250`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/__init__.py#L250) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- <a id="_depth_init"></a>`_depth_init(layer_id: int)` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/__init__.py#L63)
- <a id="_make_gptoss_attn_config"></a>`_make_gptoss_attn_config(*, dim: int, layer_id: int, attn_backend: str = "varlen", n_heads: int = 64, n_kv_heads: int = 8, head_dim: int = 64, sliding_window_size: int | None = None, fuse_qkv: bool = True, rope: RoPE.Config)` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/__init__.py#L70) — Build a fully-specified GPT-OSS Attention.Config for a single layer. — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- <a id="_make_gptoss_experts_config"></a>`_make_gptoss_experts_config(*, dim: int, hidden_dim: int, num_experts: int, layer_id: int, top_k: int, moe_comm_backend: str, non_blocking_capacity_factor: float | None = None)` — [`L150`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/__init__.py#L150) — Build a fully-specified RoutedExperts.Config for a single GPT-OSS layer. — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- <a id="_output_linear_init"></a>`_output_linear_init(dim: int)` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/__init__.py#L55)
- <a id="model_registry"></a>`model_registry(flavor: str, *, seq_len: int | None = None, moe_comm_backend: str = "standard", attn_backend: str = "varlen", converters: list[ModelConfigConverter.Config] | None = None)` — [`L395`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/__init__.py#L395) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)

## Module values
- <a id="_EMBEDDING_INIT"></a>`_EMBEDDING_INIT` — [`L52`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/__init__.py#L52)
- <a id="_NORM_INIT"></a>`_NORM_INIT` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/__init__.py#L50)
- <a id="__all__"></a>`__all__` — [`L44`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/__init__.py#L44)
- <a id="gptoss_configs"></a>`gptoss_configs` — [`L388`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/__init__.py#L388) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)

