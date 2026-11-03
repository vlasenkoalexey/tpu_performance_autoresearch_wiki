---
title: 'Module: src/vllm_torchtpu/layers/adapter/rotary_embedding.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/rotary_embedding.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.rotary_embedding`/
symbols:
  TPU_ROPE_CLASSES.TPU_ROPE_CLASSES: TPU_ROPE_CLASSES.TPU_ROPE_CLASSES.
  _discover_static_rope_classes: _discover_static_rope_classes().
  _make_tpu_rope_class: _make_tpu_rope_class().
  TpuRotaryEmbedding: TpuRotaryEmbedding.
  _all_subclasses: _all_subclasses().
  logger: logger.
  _STATIC_ROPE_CLASSES: _STATIC_ROPE_CLASSES.
  _rotary_forward_fp32: _rotary_forward_fp32().
  TpuApplyRotaryEmb.forward_tpu: TpuApplyRotaryEmb#forward_tpu.
  _uses_static_rotary_forward: _uses_static_rotary_forward().
  TpuApplyRotaryEmb.forward_oot: TpuApplyRotaryEmb#forward_oot().
  TpuApplyRotaryEmb: TpuApplyRotaryEmb#
  TpuApplyRotaryEmb.__init__: TpuApplyRotaryEmb#__init__().
---
# Module: [`src/vllm_torchtpu/layers/adapter/rotary_embedding.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/rotary_embedding.py)

## Classes
### <a id="TpuApplyRotaryEmb"></a>`TpuApplyRotaryEmb`
- def: [`src/vllm_torchtpu/layers/adapter/rotary_embedding.py:57`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/rotary_embedding.py#L57)
- doc: `ApplyRotaryEmb` that always rotates in FP32, like the CUDA kernel.
- signature: `class TpuApplyRotaryEmb(ApplyRotaryEmb):`
- members:
  - <a id="TpuApplyRotaryEmb.forward_oot"></a>`forward_oot(self, x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor)` — [`L77`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/rotary_embedding.py#L77)
  - <a id="TpuApplyRotaryEmb.forward_tpu"></a>`forward_tpu` — [`L82`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/rotary_embedding.py#L82)
- protocol/private: <a id="TpuApplyRotaryEmb.__init__"></a>`__init__`[`L60`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/rotary_embedding.py#L60)

## Functions
- <a id="_all_subclasses"></a>`_all_subclasses(cls: type)` — [`L124`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/rotary_embedding.py#L124)
- <a id="_discover_static_rope_classes"></a>`_discover_static_rope_classes()` — [`L145`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/rotary_embedding.py#L145) — Upstream RotaryEmbedding classes whose forward is the static path.
- <a id="_make_tpu_rope_class"></a>`_make_tpu_rope_class(base: type[RotaryEmbedding])` — [`L166`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/rotary_embedding.py#L166)
- <a id="_rotary_forward_fp32"></a>`_rotary_forward_fp32(self: RotaryEmbedding, positions: torch.Tensor, query: torch.Tensor, key: torch.Tensor | None = None)` — [`L85`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/rotary_embedding.py#L85) — ``RotaryEmbedding.forward_static`` with ``enable_fp32_compute=True``.
- <a id="_uses_static_rotary_forward"></a>`_uses_static_rotary_forward(cls: type[RotaryEmbedding])` — [`L132`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/rotary_embedding.py#L132) — True if ``cls.forward_native`` resolves to ``RotaryEmbedding``'s.

## Module values
- <a id="TPU_ROPE_CLASSES.TPU_ROPE_CLASSES"></a>`TPU_ROPE_CLASSES` — [`L185`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/rotary_embedding.py#L185)
- <a id="TpuRotaryEmbedding"></a>`TpuRotaryEmbedding` — [`L188`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/rotary_embedding.py#L188)
- <a id="_STATIC_ROPE_CLASSES"></a>`_STATIC_ROPE_CLASSES` — [`L163`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/rotary_embedding.py#L163)
- <a id="logger"></a>`logger` — [`L53`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/rotary_embedding.py#L53)

