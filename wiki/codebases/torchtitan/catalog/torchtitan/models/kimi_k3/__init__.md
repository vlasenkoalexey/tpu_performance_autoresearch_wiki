---
title: 'Module: torchtitan/models/kimi_k3/__init__.py'
type: catalog
provenance: extracted
module: torchtitan/models/kimi_k3/__init__.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.kimi_k3`/
symbols:
  _vision_encoder_config: _vision_encoder_config().
  _kimi_k3_config: _kimi_k3_config().
  _latent_moe_config: _latent_moe_config().
  _kda_config: _kda_config().
  _mla_config: _mla_config().
  _linear: _linear().
  model_registry: model_registry().
  _kda_config.conv: _kda_config().conv().
  _norm: _norm().
  _feed_forward_config: _feed_forward_config().
  _debugmodel: _debugmodel().
  _kimi_k3: _kimi_k3().
  kimi_k3_configs: kimi_k3_configs.
  _NORM_INIT: _NORM_INIT.
  _fan_in_linear_init: _fan_in_linear_init().
  KIMI_K3_SPECIAL_TOKENS: KIMI_K3_SPECIAL_TOKENS.
  _LINEAR_INIT: _LINEAR_INIT.
  _CONV_INIT: _CONV_INIT.
  _EMBEDDING_INIT: _EMBEDDING_INIT.
  _POS_EMBED_INIT: _POS_EMBED_INIT.
  _output_linear_init: _output_linear_init().
  _a_log_init: _a_log_init().
  __all__: __all__.
---
# Module: [`torchtitan/models/kimi_k3/__init__.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py)

## Functions
- <a id="_a_log_init"></a>`_a_log_init(parameter: nn.Parameter)` — [`L90`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L90)
- <a id="_debugmodel"></a>`_debugmodel(attn_backend: str, moe_comm_backend: str)` — [`L474`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L474)
- <a id="_fan_in_linear_init"></a>`_fan_in_linear_init(in_features: int)` — [`L80`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L80)
- <a id="_feed_forward_config"></a>`_feed_forward_config(*, dim: int, hidden_dim: int)` — [`L119`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L119) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
- <a id="_kda_config"></a>`_kda_config(*, dim: int, num_heads: int, head_dim: int, conv_kernel_size: int)` — [`L169`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L169) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
- <a id="_kimi_k3"></a>`_kimi_k3(attn_backend: str, moe_comm_backend: str)` — [`L511`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L511)
- <a id="_kimi_k3_config"></a>`_kimi_k3_config(*, dim: int, vocab_size: int, num_layers: int, full_attention_layers: set[int], attn_res_block_size: int, num_heads: int, q_lora_rank: int, kv_lora_rank: int, qk_nope_head_dim: int, qk_rope_head_dim: int, v_head_dim: int, kda_head_dim: int, conv_kernel_size: int, dense_hidden_dim: int, latent_dim: int, expert_hidden_dim: int, num_experts: int, top_k: int, num_shared_experts: int, vision_encoder: KimiK3VisionEncoder.Config, attn_backend: str, moe_comm_backend: str = "standard")` — [`L364`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L364) — Assemble a Kimi K3 config from the released topology's free parameters. — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
- <a id="_latent_moe_config"></a>`_latent_moe_config(*, dim: int, latent_dim: int, expert_hidden_dim: int, num_experts: int, top_k: int, num_shared_experts: int, moe_comm_backend: str)` — [`L219`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L219) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
- <a id="_linear"></a>`_linear(in_features: int, out_features: int, *, bias: bool = False, param_init: dict[str, Callable] | None = None)` — [`L96`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L96) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
- <a id="_mla_config"></a>`_mla_config(*, dim: int, num_heads: int, q_lora_rank: int, kv_lora_rank: int, qk_nope_head_dim: int, qk_rope_head_dim: int, v_head_dim: int, attn_backend: str)` — [`L133`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L133) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
- <a id="_norm"></a>`_norm(dim: int, eps: float = 0.00001)` — [`L111`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L111) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
- <a id="_output_linear_init"></a>`_output_linear_init(dim: int)` — [`L68`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L68)
- <a id="_vision_encoder_config"></a>`_vision_encoder_config(*, text_dim: int, dim: int, qkv_dim: int, hidden_dim: int, num_layers: int, num_heads: int, patch_size: int = 14, in_channels: int = 3, merge_kernel_size: tuple[int, int] = (2, 2), init_pos_emb_height: int = 16, init_pos_emb_width: int = 16, max_num_frames: int = 4)` — [`L280`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L280) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="_kda_config.conv"></a>`conv()` — [`L178`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L178) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
- <a id="model_registry"></a>`model_registry(flavor: str, attn_backend: str = "flex", converters: list[ModelConfigConverter.Config] | None = None, moe_comm_backend: str = "standard", *, seq_len: int | None = None)` — [`L554`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L554) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)

## Module values
- <a id="KIMI_K3_SPECIAL_TOKENS"></a>`KIMI_K3_SPECIAL_TOKENS` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L49)
- <a id="_CONV_INIT"></a>`_CONV_INIT` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L62)
- <a id="_EMBEDDING_INIT"></a>`_EMBEDDING_INIT` — [`L64`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L64)
- <a id="_LINEAR_INIT"></a>`_LINEAR_INIT` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L58)
- <a id="_NORM_INIT"></a>`_NORM_INIT` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L63)
- <a id="_POS_EMBED_INIT"></a>`_POS_EMBED_INIT` — [`L65`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L65)
- <a id="__all__"></a>`__all__` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L38)
- <a id="kimi_k3_configs"></a>`kimi_k3_configs` — [`L548`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/__init__.py#L548)

