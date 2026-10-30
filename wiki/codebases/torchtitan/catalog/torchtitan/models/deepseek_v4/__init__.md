---
title: 'Module: torchtitan/models/deepseek_v4/__init__.py'
type: catalog
provenance: extracted
module: torchtitan/models/deepseek_v4/__init__.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.deepseek_v4`/
symbols:
  _build_mtp_layers: _build_mtp_layers().
  _debugmodel: _debugmodel().
  _deepseek_v4_flash: _deepseek_v4_flash().
  _deepseek_v4_pro: _deepseek_v4_pro().
  _make_v4_attn_config: _make_v4_attn_config().
  _build_v4_layers: _build_v4_layers().
  _make_v4_moe_config: _make_v4_moe_config().
  _make_compressor_config: _make_compressor_config().
  model_registry: model_registry().
  _make_indexer_config: _make_indexer_config().
  _make_mtp_inner_block: _make_mtp_inner_block().
  _LINEAR_INIT: _LINEAR_INIT.
  _make_v4_dense_config: _make_v4_dense_config().
  _NORM_INIT: _NORM_INIT.
  deepseek_v4_configs: deepseek_v4_configs.
  _depth_init: _depth_init().
  _HC_INIT: _HC_INIT.
  _depth_experts_init: _depth_experts_init().
  _EMBEDDING_INIT: _EMBEDDING_INIT.
  _output_linear_init: _output_linear_init().
  __all__: __all__.
---
# Module: [`torchtitan/models/deepseek_v4/__init__.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py)

## Functions
- <a id="_build_mtp_layers"></a>`_build_mtp_layers(inner_cfg: DeepSeekV4TransformerBlock.Config, *, dim: int, n_main_layers: int, num_mtp_layers: int, hc_mult: int = 4, norm_eps: float = 0.000001, hc_eps: float = 0.000001, rope: RoPE.Config)` — [`L535`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L535) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- <a id="_build_v4_layers"></a>`_build_v4_layers(*, n_layers: int, layer_offset: int = 0, dim: int, n_heads: int, head_dim: int, rope_head_dim: int, q_lora_rank: int, o_lora_rank: int, n_groups: int, compress_ratios: tuple[int, ...], window_size: int, norm_eps: float, index_n_heads: int, index_head_dim: int, index_topk: int, moe_inter_dim: int, num_experts: int, num_shared_experts: int, top_k: int, vocab_size: int, n_hash_layers: int, route_norm: bool, route_scale: float, load_balance_coeff: float, moe_comm_backend: str, non_blocking_capacity_factor: float | None, rope: RoPE.Config, rope_compress: RoPE.Config, hc_mult: int = 4, sinkhorn_iters: int = 20, hc_eps: float = 0.000001, dense_hidden_dim: int | None = None, dense_layers: set[int] | None = None)` — [`L387`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L387) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- <a id="_debugmodel"></a>`_debugmodel(moe_comm_backend: str = "standard", non_blocking_capacity_factor: float | None = None, n_mtp_layers: int = 0, *, seq_len: int)` — [`L610`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L610)
- <a id="_deepseek_v4_flash"></a>`_deepseek_v4_flash(moe_comm_backend: str = "standard", non_blocking_capacity_factor: float | None = None, n_mtp_layers: int = 0, *, seq_len: int)` — [`L742`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L742) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- <a id="_deepseek_v4_pro"></a>`_deepseek_v4_pro(moe_comm_backend: str = "standard", non_blocking_capacity_factor: float | None = None, n_mtp_layers: int = 0, *, seq_len: int)` — [`L874`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L874) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- <a id="_depth_experts_init"></a>`_depth_experts_init(layer_id: int)` — [`L85`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L85)
- <a id="_depth_init"></a>`_depth_init(layer_id: int)` — [`L78`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L78)
- <a id="_make_compressor_config"></a>`_make_compressor_config(*, dim: int, head_dim: int, rope_head_dim: int, compress_ratio: int, norm_eps: float, coff: int, rope: RoPE.Config)` — [`L93`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L93) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- <a id="_make_indexer_config"></a>`_make_indexer_config(*, dim: int, num_index_heads: int, index_head_dim: int, rope_head_dim: int, q_lora_rank: int, compress_ratio: int, norm_eps: float, rope: RoPE.Config)` — [`L131`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L131) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- <a id="_make_mtp_inner_block"></a>`_make_mtp_inner_block(inner_cfg: DeepSeekV4TransformerBlock.Config, rope: RoPE.Config)` — [`L514`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L514) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- <a id="_make_v4_attn_config"></a>`_make_v4_attn_config(*, layer_id: int, dim: int, n_heads: int, head_dim: int, rope_head_dim: int, q_lora_rank: int, o_lora_rank: int, n_groups: int, compress_ratio: int, window_size: int, norm_eps: float, index_n_heads: int, index_head_dim: int, index_topk: int, n_layers: int, rope: RoPE.Config)` — [`L172`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L172) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- <a id="_make_v4_dense_config"></a>`_make_v4_dense_config(*, layer_id: int, dim: int, hidden_dim: int)` — [`L373`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L373)
- <a id="_make_v4_moe_config"></a>`_make_v4_moe_config(*, layer_id: int, dim: int, moe_inter_dim: int, num_experts: int, num_shared_experts: int, top_k: int, vocab_size: int, n_hash_layers: int, route_norm: bool, route_scale: float, load_balance_coeff: float, moe_comm_backend: str, non_blocking_capacity_factor: float | None)` — [`L316`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L316) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- <a id="_output_linear_init"></a>`_output_linear_init(dim: int)` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L70)
- <a id="model_registry"></a>`model_registry(flavor: str, *, seq_len: int | None = None, moe_comm_backend: str = "standard", non_blocking_capacity_factor: float | None = None, n_mtp_layers: int = 0, converters: list[ModelConfigConverter.Config] | None = None)` — [`L1013`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L1013) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)

## Module values
- <a id="_EMBEDDING_INIT"></a>`_EMBEDDING_INIT` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L62)
- <a id="_HC_INIT"></a>`_HC_INIT` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L63)
- <a id="_LINEAR_INIT"></a>`_LINEAR_INIT` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L57)
- <a id="_NORM_INIT"></a>`_NORM_INIT` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L61)
- <a id="__all__"></a>`__all__` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L50)
- <a id="deepseek_v4_configs"></a>`deepseek_v4_configs` — [`L1006`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/__init__.py#L1006)

