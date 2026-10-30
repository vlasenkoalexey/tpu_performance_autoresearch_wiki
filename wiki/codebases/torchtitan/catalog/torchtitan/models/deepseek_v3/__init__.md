---
title: 'Module: torchtitan/models/deepseek_v3/__init__.py'
type: catalog
provenance: extracted
module: torchtitan/models/deepseek_v3/__init__.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.deepseek_v3`/
symbols:
  _debugmodel: _debugmodel().
  _16b: _16b().
  _236b: _236b().
  _671b: _671b().
  _testmodel: _testmodel().
  make_mla_attention_config: make_mla_attention_config().
  build_mla_moe_layers: build_mla_moe_layers().
  _build_mtp_layers: _build_mtp_layers().
  model_registry: model_registry().
  _build_dsv3_layers: _build_dsv3_layers().
  deepseekv3_configs: deepseekv3_configs.
  _NORM_INIT: _NORM_INIT.
  _EMBEDDING_INIT: _EMBEDDING_INIT.
  _output_linear_init: _output_linear_init().
  _post_optimizer_build_fn: _post_optimizer_build_fn().
  _depth_init: _depth_init().
  _depth_experts_init: _depth_experts_init().
  _LINEAR_INIT: _LINEAR_INIT.
  __all__: __all__.
---
# Module: [`torchtitan/models/deepseek_v3/__init__.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py)

## Functions
- <a id="_16b"></a>`_16b(attn_backend: str, moe_comm_backend: str, non_blocking_capacity_factor: float | None = None, num_mtp_layers: int = 0, *, seq_len: int)` — [`L406`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L406) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- <a id="_236b"></a>`_236b(attn_backend: str, moe_comm_backend: str, non_blocking_capacity_factor: float | None = None, num_mtp_layers: int = 0, *, seq_len: int)` — [`L480`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L480) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- <a id="_671b"></a>`_671b(attn_backend: str, moe_comm_backend: str, non_blocking_capacity_factor: float | None = None, num_mtp_layers: int = 0, *, seq_len: int)` — [`L557`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L557) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- <a id="_build_dsv3_layers"></a>`_build_dsv3_layers(**kwargs)` — [`L293`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L293) — Thin wrapper: ``build_mla_moe_layers`` with DeepSeek V3's own inits. — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- <a id="_build_mtp_layers"></a>`_build_mtp_layers(inner_cfg: DeepSeekV3TransformerBlock.Config, *, dim: int, num_mtp_layers: int)` — [`L304`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L304) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- <a id="_debugmodel"></a>`_debugmodel(attn_backend: str, moe_comm_backend: str, non_blocking_capacity_factor: float | None = None, num_mtp_layers: int = 0, *, seq_len: int)` — [`L332`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L332) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- <a id="_depth_experts_init"></a>`_depth_experts_init(layer_id: int)` — [`L77`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L77)
- <a id="_depth_init"></a>`_depth_init(layer_id: int)` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L70)
- <a id="_output_linear_init"></a>`_output_linear_init(dim: int)` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L62)
- <a id="_post_optimizer_build_fn"></a>`_post_optimizer_build_fn(optimizers, model_parts, parallel_dims)` — [`L717`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L717) — Register step pre-hooks for load balancing and aux-loss accumulators.
- <a id="_testmodel"></a>`_testmodel(attn_backend: str, moe_comm_backend: str, non_blocking_capacity_factor: float | None = None, num_mtp_layers: int = 0, *, seq_len: int)` — [`L635`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L635) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- <a id="build_mla_moe_layers"></a>`build_mla_moe_layers(*, n_layers: int, n_dense_layers: int, dim: int, n_heads: int, q_lora_rank: int, kv_lora_rank: int, qk_nope_head_dim: int, qk_rope_head_dim: int, v_head_dim: int, mscale: float, dense_hidden_dim: int, moe_hidden_dim: int, num_experts: int, num_shared_experts: int, router_top_k: int, router_score_func: Literal["sigmoid", "softmax"], router_num_expert_groups: int | None = None, router_num_limited_groups: int | None = None, router_route_scale: float = 1, router_route_norm: bool = False, aux_loss_coeff: float | None = None, attn_backend: str, moe_comm_backend: str, non_blocking_capacity_factor: float | None, linear_init: dict[str, Callable], norm_init: dict[str, Callable], depth_init: Callable[[int], dict[str, Callable]], depth_experts_init: Callable[[int], dict[str, Callable]], rope: RoPE.Config, attention_config_factory: Callable[[str], Module.Config] = get_attention_config)` — [`L175`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L175) — Build the per-layer ``DeepSeekV3TransformerBlock`` configs (MLA + MoE). — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- <a id="make_mla_attention_config"></a>`make_mla_attention_config(*, layer_id: int, dim: int, n_heads: int, q_lora_rank: int, kv_lora_rank: int, qk_nope_head_dim: int, qk_rope_head_dim: int, v_head_dim: int, mscale: float = 1, attn_backend: str, linear_init: dict[str, Callable], norm_init: dict[str, Callable], depth_init: Callable[[int], dict[str, Callable]], rope: RoPE.Config, attention_config_factory: Callable[[str], Module.Config] = get_attention_config)` — [`L85`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L85) — Build a fully-specified DeepSeek V3 MLA ``Attention.Config``. — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- <a id="model_registry"></a>`model_registry(flavor: str, *, seq_len: int | None = None, attn_backend: str = "flex", moe_comm_backend: str = "standard", non_blocking_capacity_factor: float | None = None, converters: list[ModelConfigConverter.Config] | None = None, num_mtp_layers: int = 0)` — [`L723`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L723) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)

## Module values
- <a id="_EMBEDDING_INIT"></a>`_EMBEDDING_INIT` — [`L59`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L59)
- <a id="_LINEAR_INIT"></a>`_LINEAR_INIT` — [`L54`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L54)
- <a id="_NORM_INIT"></a>`_NORM_INIT` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L58)
- <a id="__all__"></a>`__all__` — [`L44`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L44)
- <a id="deepseekv3_configs"></a>`deepseekv3_configs` — [`L708`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/__init__.py#L708) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)

