---
title: 'Module: torchtitan/models/kimi_k2_7/__init__.py'
type: catalog
provenance: extracted
module: torchtitan/models/kimi_k2_7/__init__.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.kimi_k2_7`/
symbols:
  _vision_encoder_config: _vision_encoder_config().
  _debugmodel: _debugmodel().
  _kimi_k2_5: _kimi_k2_5().
  _moonlight_16b_a3b_config: _moonlight_16b_a3b_config().
  model_registry: model_registry().
  _vl_linear: _vl_linear().
  _build_kimi_layers: _build_kimi_layers().
  _scaled_bias_rowwise_linear: _scaled_bias_rowwise_linear().
  _vl_layernorm: _vl_layernorm().
  _register_optimizer_hooks: _register_optimizer_hooks().
  _kimi_vl_a3b: _kimi_vl_a3b().
  kimi_k2_5_configs: kimi_k2_5_configs.
  _moonlight_16b_a3b: _moonlight_16b_a3b().
  _qk_clip_attention_config: _qk_clip_attention_config().
  _NORM_INIT: _NORM_INIT.
  _depth_init: _depth_init().
  _depth_experts_init: _depth_experts_init().
  KIMI_K2_5_SPECIAL_TOKENS: KIMI_K2_5_SPECIAL_TOKENS.
  _LINEAR_INIT: _LINEAR_INIT.
  _EMBEDDING_INIT: _EMBEDDING_INIT.
  _output_linear_init: _output_linear_init().
  _POS_EMB_INIT: _POS_EMB_INIT.
  __all__: __all__.
---
# Module: [`torchtitan/models/kimi_k2_7/__init__.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py)

## Functions
- <a id="_build_kimi_layers"></a>`_build_kimi_layers(**kwargs)` — [`L207`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L207) — Build MLA/MoE layers with the Kimi-family parameter initializers. — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="_debugmodel"></a>`_debugmodel(attn_backend: str, moe_comm_backend: str, non_blocking_capacity_factor: float | None = None, *, seq_len: int)` — [`L219`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L219) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="_depth_experts_init"></a>`_depth_experts_init(layer_id: int)` — [`L95`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L95)
- <a id="_depth_init"></a>`_depth_init(layer_id: int)` — [`L88`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L88)
- <a id="_kimi_k2_5"></a>`_kimi_k2_5(attn_backend: str, moe_comm_backend: str, non_blocking_capacity_factor: float | None = None, *, seq_len: int)` — [`L410`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L410) — Architecture shared by Kimi K2.5, K2.6, and K2.7-Code: a ~1T-total / — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="_kimi_vl_a3b"></a>`_kimi_vl_a3b(attn_backend: str, moe_comm_backend: str, non_blocking_capacity_factor: float | None = None, *, seq_len: int)` — [`L377`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L377) — Kimi-VL 16B-A3B: Moonlight text tower plus a 2D MoonViT vision tower. — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="_moonlight_16b_a3b"></a>`_moonlight_16b_a3b(attn_backend: str, moe_comm_backend: str, non_blocking_capacity_factor: float | None = None, *, seq_len: int)` — [`L359`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L359) — Build the text-only Moonlight 16B-A3B sibling without a vision tower. — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="_moonlight_16b_a3b_config"></a>`_moonlight_16b_a3b_config(*, attn_backend: str, moe_comm_backend: str, non_blocking_capacity_factor: float | None, rope_theta: float, max_context_length: int, vision_encoder: KimiK25VisionEncoder.Config | None = None)` — [`L295`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L295) — Shared Moonshot 16B-A3B DeepSeekV3 text tower (MLA + sigmoid-routed MoE). — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="_output_linear_init"></a>`_output_linear_init(dim: int)` — [`L80`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L80)
- <a id="_qk_clip_attention_config"></a>`_qk_clip_attention_config(attn_backend: str)` — [`L192`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L192)
- <a id="_register_optimizer_hooks"></a>`_register_optimizer_hooks(optimizers: OptimizersContainer, model_parts: list[nn.Module], parallel_dims: ParallelDims)` — [`L198`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L198)
- <a id="_scaled_bias_rowwise_linear"></a>`_scaled_bias_rowwise_linear(in_features: int, out_features: int)` — [`L112`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L112) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="_vision_encoder_config"></a>`_vision_encoder_config(*, dim: int, ffn_dim: int, num_layers: int, num_heads: int, patch_size: int = 14, in_channels: int = 3, init_pos_emb_height: int = 64, init_pos_emb_width: int = 64, rope_theta: float = 10000, merge_kernel_size: list[int] | None = None, text_hidden_size: int = 7168)` — [`L127`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L127) — Build a fully-specified KimiK25VisionEncoder.Config (MoonViT3d). — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="_vl_layernorm"></a>`_vl_layernorm(dim: int, eps: float = 0.00001)` — [`L123`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L123)
- <a id="_vl_linear"></a>`_vl_linear(in_features: int, out_features: int)` — [`L103`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L103) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="model_registry"></a>`model_registry(flavor: str, *, seq_len: int | None = None, attn_backend: str = "flex", moe_comm_backend: str = "standard", non_blocking_capacity_factor: float | None = None, converters: list[ModelConfigConverter.Config] | None = None)` — [`L506`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L506) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)

## Module values
- <a id="KIMI_K2_5_SPECIAL_TOKENS"></a>`KIMI_K2_5_SPECIAL_TOKENS` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L62)
- <a id="_EMBEDDING_INIT"></a>`_EMBEDDING_INIT` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L76)
- <a id="_LINEAR_INIT"></a>`_LINEAR_INIT` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L71)
- <a id="_NORM_INIT"></a>`_NORM_INIT` — [`L75`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L75)
- <a id="_POS_EMB_INIT"></a>`_POS_EMB_INIT` — [`L77`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L77)
- <a id="__all__"></a>`__all__` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L49)
- <a id="kimi_k2_5_configs"></a>`kimi_k2_5_configs` — [`L498`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/__init__.py#L498)

