---
title: 'Module: src/vllm_torchtpu/models/vllm/qwen3_5_patch.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/qwen3_5_patch.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.qwen3_5_patch`/
symbols:
  maybe_patch_qwen3_5_attn_moe_overlap: maybe_patch_qwen3_5_attn_moe_overlap().
  _patched_init: _patched_init().
  _overlap_forward: _overlap_forward().
  logger: logger.
  _overlap_min_tokens: _overlap_min_tokens().
  _orig_init: _orig_init.
  _MIN_PER_CHIP_SIZE_MB: _MIN_PER_CHIP_SIZE_MB.
  _configure_layer: _configure_layer().
---
# Module: [`src/vllm_torchtpu/models/vllm/qwen3_5_patch.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_5_patch.py)

## Functions
- <a id="_configure_layer"></a>`_configure_layer(layer: Qwen3_5DecoderLayer)` — [`L58`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_5_patch.py#L58)
- <a id="_overlap_forward"></a>`_overlap_forward(self: Qwen3_5DecoderLayer, hidden_states: torch.Tensor, residual: torch.Tensor | None, positions: torch.Tensor, **kwargs: object)` — [`L93`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_5_patch.py#L93) — documented in [compilation-and-graph-capture](../../../../../concepts/compilation-and-graph-capture.md)
- <a id="_overlap_min_tokens"></a>`_overlap_min_tokens(hidden_size: int, tp_size: int, element_size: int)` — [`L52`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_5_patch.py#L52)
- <a id="_patched_init"></a>`_patched_init(self: Qwen3_5DecoderLayer, vllm_config: Any, layer_type: str, prefix: str = "")` — [`L83`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_5_patch.py#L83)
- <a id="maybe_patch_qwen3_5_attn_moe_overlap"></a>`maybe_patch_qwen3_5_attn_moe_overlap(model_config: ModelConfig | None)` — [`L144`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_5_patch.py#L144) — Returns False until a Qwen3.5 MoE model config is available.

## Module values
- <a id="_MIN_PER_CHIP_SIZE_MB"></a>`_MIN_PER_CHIP_SIZE_MB` — [`L49`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_5_patch.py#L49)
- <a id="_orig_init"></a>`_orig_init` — [`L47`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_5_patch.py#L47)
- <a id="logger"></a>`logger` — [`L45`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_5_patch.py#L45)

