---
title: 'Module: torchtitan/models/qwen3_5/__init__.py'
type: catalog
provenance: extracted
module: torchtitan/models/qwen3_5/__init__.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.qwen3_5`/
symbols:
  _qwen35_vision_encoder_config: _qwen35_vision_encoder_config().
  _qwen35_deltanet_config: _qwen35_deltanet_config().
  _debugmodel: _debugmodel().
  _debugmodel_moe: _debugmodel_moe().
  _27b: _27b().
  _35b_a3b: _35b_a3b().
  _0_8b: _0_8b().
  _2b: _2b().
  _4b: _4b().
  _9b: _9b().
  _122b_a10b: _122b_a10b().
  _397b_a17b: _397b_a17b().
  _qwen35_attention_config: _qwen35_attention_config().
  model_registry: model_registry().
  _build_qwen35_moe_layers: _build_qwen35_moe_layers().
  _build_qwen35_layers: _build_qwen35_layers().
  _shared_experts_config: _shared_experts_config().
  _offset_norm: _offset_norm().
  qwen3_5_configs: qwen3_5_configs.
  _linear: _linear().
  _qwen35_deltanet_config._conv: _qwen35_deltanet_config()._conv().
  _qwen35_deltanet_config._proj: _qwen35_deltanet_config()._proj().
  _scaled_bias_rowwise_linear: _scaled_bias_rowwise_linear().
  QWEN3_5_SPECIAL_TOKENS: QWEN3_5_SPECIAL_TOKENS.
  _LINEAR_INIT: _LINEAR_INIT.
  _EMBEDDING_INIT: _EMBEDDING_INIT.
  _output_linear_init: _output_linear_init().
  _depth_init: _depth_init().
  _depth_experts_init: _depth_experts_init().
  _OFFSET_NORM_INIT: _OFFSET_NORM_INIT.
  _POS_EMBED_INIT: _POS_EMBED_INIT.
  _EPS: _EPS.
  _a_log_init: _a_log_init().
  __all__: __all__.
---
# Module: [`torchtitan/models/qwen3_5/__init__.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py)

## Functions
- <a id="_0_8b"></a>`_0_8b(attn_backend: str, *, seq_len: int)` — [`L593`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L593) — Qwen3.5-0.8B dense config with vision encoder. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_122b_a10b"></a>`_122b_a10b(attn_backend: str, moe_comm_backend: str = "standard", *, seq_len: int)` — [`L952`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L952) — Qwen3.5-122B-A10B MoE config with vision encoder. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_27b"></a>`_27b(attn_backend: str, *, seq_len: int)` — [`L831`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L831) — Qwen3.5-27B dense config with vision encoder. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_2b"></a>`_2b(attn_backend: str, *, seq_len: int)` — [`L654`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L654) — Qwen3.5-2B dense config with vision encoder. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_35b_a3b"></a>`_35b_a3b(attn_backend: str, moe_comm_backend: str = "standard", *, seq_len: int)` — [`L887`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L887) — Qwen3.5-35B-A3B MoE config with vision encoder. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_397b_a17b"></a>`_397b_a17b(attn_backend: str, moe_comm_backend: str = "standard", *, seq_len: int)` — [`L1017`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L1017) — Qwen3.5-397B-A17B MoE config with vision encoder. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_4b"></a>`_4b(attn_backend: str, *, seq_len: int)` — [`L715`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L715) — Qwen3.5-4B dense config with vision encoder. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_9b"></a>`_9b(attn_backend: str, *, seq_len: int)` — [`L775`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L775) — Qwen3.5-9B dense config with vision encoder. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_a_log_init"></a>`_a_log_init(param: nn.Parameter)` — [`L100`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L100)
- <a id="_build_qwen35_layers"></a>`_build_qwen35_layers(*, n_layers: int, dim: int, n_heads: int, n_kv_heads: int, head_dim: int, rotary_dim: int, rope: MRoPE.Config, hidden_dim: int, n_key_heads: int, n_value_heads: int, key_head_dim: int, value_head_dim: int, full_attention_interval: int = 4, attn_backend: str)` — [`L313`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L313) — Build per-layer configs for dense Qwen3.5 models. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_build_qwen35_moe_layers"></a>`_build_qwen35_moe_layers(*, n_layers: int, dim: int, n_heads: int, n_kv_heads: int, head_dim: int, rotary_dim: int, rope: MRoPE.Config, moe_hidden_dim: int, num_experts: int, top_k: int, shared_expert_hidden_dim: int, n_key_heads: int, n_value_heads: int, key_head_dim: int, value_head_dim: int, full_attention_interval: int = 4, attn_backend: str, moe_comm_backend: str = "standard", non_blocking_capacity_factor: float | None = None)` — [`L379`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L379) — Build per-layer configs for MoE Qwen3.5 models with shared expert. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_qwen35_deltanet_config._conv"></a>`_conv(channels: int)` — [`L272`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L272)
- <a id="_debugmodel"></a>`_debugmodel(attn_backend: str, *, seq_len: int)` — [`L469`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L469) — Debug config for Qwen3.5 with vision encoder. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_debugmodel_moe"></a>`_debugmodel_moe(attn_backend: str, moe_comm_backend: str = "standard", *, seq_len: int)` — [`L528`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L528) — Debug MoE config for Qwen3.5 with shared expert. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_depth_experts_init"></a>`_depth_experts_init(layer_id: int)` — [`L92`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L92)
- <a id="_depth_init"></a>`_depth_init(layer_id: int)` — [`L85`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L85)
- <a id="_linear"></a>`_linear(in_features: int, out_features: int)` — [`L106`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L106)
- <a id="_offset_norm"></a>`_offset_norm(dim: int)` — [`L126`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L126) — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_output_linear_init"></a>`_output_linear_init(dim: int)` — [`L77`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L77)
- <a id="_qwen35_deltanet_config._proj"></a>`_proj(in_f: int, out_f: int, init: dict)` — [`L267`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L267)
- <a id="_qwen35_attention_config"></a>`_qwen35_attention_config(*, dim: int, n_heads: int, n_kv_heads: int, head_dim: int, rotary_dim: int, rope: MRoPE.Config, attn_backend: str, layer_id: int)` — [`L208`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L208) — Build a fully-specified Qwen35Attention.Config. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_qwen35_deltanet_config"></a>`_qwen35_deltanet_config(*, dim: int, n_key_heads: int, n_value_heads: int, key_head_dim: int, value_head_dim: int, layer_id: int, conv_kernel_size: int = 4)` — [`L253`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L253) — Build a fully-specified GatedDeltaNet.Config. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_qwen35_vision_encoder_config"></a>`_qwen35_vision_encoder_config(*, dim: int, ffn_dim: int, num_layers: int, num_heads: int, patch_size: int, temporal_patch_size: int, spatial_merge_size: int, out_hidden_size: int, num_position_embeddings: int, layer_norm_eps: float = 0.000001, rope_theta: float = 10000, in_channels: int = 3)` — [`L148`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L148) — Build a fully-specified Qwen35VisionEncoder.Config. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_scaled_bias_rowwise_linear"></a>`_scaled_bias_rowwise_linear(in_features: int, out_features: int)` — [`L115`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L115)
- <a id="_shared_experts_config"></a>`_shared_experts_config(*, dim: int, hidden_dim: int, layer_id: int)` — [`L130`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L130) — Build Qwen3.5's sigmoid-gated shared-expert config (SwiGLU FFN + gate). — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="model_registry"></a>`model_registry(flavor: str, *, seq_len: int | None = None, attn_backend: str = "flex", moe_comm_backend: str | None = None, converters: list[ModelConfigConverter.Config] | None = None)` — [`L1096`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L1096) — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)

## Module values
- <a id="QWEN3_5_SPECIAL_TOKENS"></a>`QWEN3_5_SPECIAL_TOKENS` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L57)
- <a id="_EMBEDDING_INIT"></a>`_EMBEDDING_INIT` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L71)
- <a id="_EPS"></a>`_EPS` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L74)
- <a id="_LINEAR_INIT"></a>`_LINEAR_INIT` — [`L66`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L66)
- <a id="_OFFSET_NORM_INIT"></a>`_OFFSET_NORM_INIT` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L70)
- <a id="_POS_EMBED_INIT"></a>`_POS_EMBED_INIT` — [`L72`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L72)
- <a id="__all__"></a>`__all__` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L50)
- <a id="qwen3_5_configs"></a>`qwen3_5_configs` — [`L1082`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/__init__.py#L1082) — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)

