---
title: 'Module: torchtitan/models/qwen3/__init__.py'
type: catalog
provenance: extracted
module: torchtitan/models/qwen3/__init__.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.qwen3`/
symbols:
  model_registry: model_registry().
  _debugmodel: _debugmodel().
  _0_6b: _0_6b().
  _1_7b: _1_7b().
  _4b: _4b().
  _testmodel: _testmodel().
  _30b_a3b: _30b_a3b().
  _8b: _8b().
  _14b: _14b().
  _32b: _32b().
  _debugmodel_moe: _debugmodel_moe().
  _235b_a22b: _235b_a22b().
  _build_qwen3_moe_layers: _build_qwen3_moe_layers().
  _build_qwen3_layers: _build_qwen3_layers().
  qwen3_configs: qwen3_configs.
  _qwen3_norm: _qwen3_norm().
  _debugmodel_non_fused_qkv: _debugmodel_non_fused_qkv().
  _LINEAR_INIT._LINEAR_INIT: _LINEAR_INIT._LINEAR_INIT.
  _30b_a3b_global_aux: _30b_a3b_global_aux().
  _EMBEDDING_INIT: _EMBEDDING_INIT.
  _EMBEDDING_SKIP_INIT: _EMBEDDING_SKIP_INIT.
  _moe_experts_init: _moe_experts_init().
  _residual_output_init: _residual_output_init().
  _EXPERTS_INIT._EXPERTS_INIT: _EXPERTS_INIT._EXPERTS_INIT.
  _residual_output_weight_init: _residual_output_weight_init().
  _NORM_INIT: _NORM_INIT.
  _EPS: _EPS.
  __all__: __all__.
---
# Module: [`torchtitan/models/qwen3/__init__.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py)

## Functions
- <a id="_0_6b"></a>`_0_6b(attn_backend: str, *, seq_len: int, fuse_qkv: bool = True)` — [`L264`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L264) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="_14b"></a>`_14b(attn_backend: str, *, seq_len: int, fuse_qkv: bool = True)` — [`L413`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L413) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="_1_7b"></a>`_1_7b(attn_backend: str, *, seq_len: int, fuse_qkv: bool = True)` — [`L302`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L302) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="_235b_a22b"></a>`_235b_a22b(attn_backend: str, moe_comm_backend: str = "standard", *, seq_len: int, fuse_qkv: bool = True)` — [`L595`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L595) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="_30b_a3b"></a>`_30b_a3b(attn_backend: str, moe_comm_backend: str = "standard", *, seq_len: int, fuse_qkv: bool = True, load_balance_coeff: float | None = 0.001, global_aux_loss_coeff: float | None = None)` — [`L530`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L530) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="_30b_a3b_global_aux"></a>`_30b_a3b_global_aux(attn_backend: str, moe_comm_backend: str = "standard", *, seq_len: int, fuse_qkv: bool = True)` — [`L578`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L578)
- <a id="_32b"></a>`_32b(attn_backend: str, *, seq_len: int, fuse_qkv: bool = True)` — [`L448`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L448) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="_4b"></a>`_4b(attn_backend: str, *, seq_len: int, fuse_qkv: bool = True)` — [`L340`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L340) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="_8b"></a>`_8b(attn_backend: str, *, seq_len: int, fuse_qkv: bool = True)` — [`L378`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L378) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="_build_qwen3_layers"></a>`_build_qwen3_layers(*, n_layers: int, dim: int, n_heads: int, n_kv_heads: int, head_dim: int, hidden_dim: int, fuse_qkv: bool = True, attn_backend: str, rope: RoPE.Config)` — [`L92`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L92) — Build per-layer configs for dense Qwen3 models. — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="_build_qwen3_moe_layers"></a>`_build_qwen3_moe_layers(*, n_layers: int, dim: int, n_heads: int, n_kv_heads: int, head_dim: int, moe_hidden_dim: int, num_experts: int, top_k: int, fuse_qkv: bool = True, attn_backend: str, moe_comm_backend: str, non_blocking_capacity_factor: float | None = None, rope: RoPE.Config, load_balance_coeff: float | None = 0.001, global_aux_loss_coeff: float | None = None)` — [`L135`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L135) — Build per-layer configs for MoE Qwen3 models. — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="_debugmodel"></a>`_debugmodel(attn_backend: str, *, seq_len: int, fuse_qkv: bool = True)` — [`L208`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L208) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="_debugmodel_moe"></a>`_debugmodel_moe(attn_backend: str, moe_comm_backend: str = "standard", *, seq_len: int, fuse_qkv: bool = True)` — [`L486`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L486) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="_debugmodel_non_fused_qkv"></a>`_debugmodel_non_fused_qkv(attn_backend: str, *, seq_len: int)` — [`L246`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L246) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="_moe_experts_init"></a>`_moe_experts_init(n_layers: int)` — [`L81`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L81)
- <a id="_qwen3_norm"></a>`_qwen3_norm(dim: int)` — [`L88`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L88) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="_residual_output_init"></a>`_residual_output_init(n_layers: int)` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L74)
- <a id="_residual_output_weight_init"></a>`_residual_output_weight_init(n_layers: int)` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L69)
- <a id="_testmodel"></a>`_testmodel(attn_backend: str, *, seq_len: int, fuse_qkv: bool = True)` — [`L639`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L639) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="model_registry"></a>`model_registry(flavor: str, *, seq_len: int | None = None, attn_backend: str = "flex", moe_comm_backend: str | None = None, fuse_qkv: bool | None = None, converters: list[ModelConfigConverter.Config] | None = None)` — [`L697`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L697) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)

## Module values
- <a id="_EMBEDDING_INIT"></a>`_EMBEDDING_INIT` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L58)
- <a id="_EMBEDDING_SKIP_INIT"></a>`_EMBEDDING_SKIP_INIT` — [`L59`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L59)
- <a id="_EPS"></a>`_EPS` — [`L66`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L66)
- <a id="_EXPERTS_INIT._EXPERTS_INIT"></a>`_EXPERTS_INIT` — [`L60`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L60)
- <a id="_LINEAR_INIT._LINEAR_INIT"></a>`_LINEAR_INIT` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L53) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="_NORM_INIT"></a>`_NORM_INIT` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L57)
- <a id="__all__"></a>`__all__` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L42)
- <a id="qwen3_configs"></a>`qwen3_configs` — [`L680`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/__init__.py#L680) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)

