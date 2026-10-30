---
title: 'Module: torchtitan/models/kimi_k2_7/qk_clip.py'
type: catalog
provenance: extracted
module: torchtitan/models/kimi_k2_7/qk_clip.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.kimi_k2_7.qk_clip`/
symbols:
  _clip_mla_weights: _clip_mla_weights().
  register_qk_clip_hook: register_qk_clip_hook().
  qk_clip: qk_clip().
  QKClipFlexInnerAttention.Config: QKClipFlexInnerAttention#Config#
  _scale_mla_heads: _scale_mla_heads().
  QKClipFlexInnerAttention: QKClipFlexInnerAttention#
  QKClipFlexInnerAttention.__init__: QKClipFlexInnerAttention#__init__().
  register_qk_clip_hook._qk_clip_hook: register_qk_clip_hook()._qk_clip_hook().
  QKClipFlexInnerAttention._process_aux: QKClipFlexInnerAttention#_process_aux().
  QKClipFlexInnerAttention.max_attention_logits_H: QKClipFlexInnerAttention#max_attention_logits_H.
  _validate_head_sharding: _validate_head_sharding().
  _replicated_scales: _replicated_scales().
  QKClipFlexInnerAttention._get_aux_request: QKClipFlexInnerAttention#_get_aux_request().
  __all__: __all__.
---
# Module: [`torchtitan/models/kimi_k2_7/qk_clip.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/qk_clip.py)

## Classes
### <a id="QKClipFlexInnerAttention"></a>`QKClipFlexInnerAttention`  ·  implements/extends FlexInnerAttention
- def: [`torchtitan/models/kimi_k2_7/qk_clip.py:27`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/qk_clip.py#L27)
- doc: FlexInnerAttention that records the maximum score for each query head.
- signature: `class QKClipFlexInnerAttention(FlexInnerAttention):`
- members:
  - <a id="QKClipFlexInnerAttention.max_attention_logits_H"></a>`max_attention_logits_H` — [`L36`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/qk_clip.py#L36)
- protocol/private: <a id="QKClipFlexInnerAttention.__init__"></a>`__init__`[`L34`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/qk_clip.py#L34), <a id="QKClipFlexInnerAttention._get_aux_request"></a>`_get_aux_request`[`L38`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/qk_clip.py#L38), <a id="QKClipFlexInnerAttention._process_aux"></a>`_process_aux`[`L41`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/qk_clip.py#L41)
- uses (calls/refs, reference-scoped): [`FlexInnerAttention`](../common/attention.md#FlexInnerAttention), [`Config`](qk_clip.md#QKClipFlexInnerAttention.Config), [`__init__`](../common/attention.md#FlexInnerAttention.__init__)
- used by: [`FlexInnerAttention`](../common/attention.md#FlexInnerAttention), [`qk_clip`](qk_clip.md#qk_clip), [`_qk_clip_attention_config`](__init__.md#_qk_clip_attention_config), [`_get_aux_request`](../common/attention.md#FlexInnerAttention._get_aux_request), [`_process_aux`](../common/attention.md#FlexInnerAttention._process_aux)

### <a id="QKClipFlexInnerAttention.Config"></a>`QKClipFlexInnerAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/kimi_k2_7/qk_clip.py:31`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/qk_clip.py#L31)
- signature: `class Config(FlexInnerAttention.Config):`
- uses (calls/refs, reference-scoped): [`FlexInnerAttention`](../common/attention.md#FlexInnerAttention), [`Config`](../common/attention.md#FlexInnerAttention.Config)
- used by: [`_qk_clip_attention_config`](__init__.md#_qk_clip_attention_config), [`__init__`](qk_clip.md#QKClipFlexInnerAttention.__init__)

## Functions
- <a id="_clip_mla_weights"></a>`_clip_mla_weights(attention: Attention, scales_H: torch.Tensor, *, alpha: float)` — [`L108`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/qk_clip.py#L108) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="register_qk_clip_hook._qk_clip_hook"></a>`_qk_clip_hook(_optimizer: torch.optim.Optimizer, _args: tuple[Any, ...], _kwargs: dict[str, Any])` — [`L188`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/qk_clip.py#L188)
- <a id="_replicated_scales"></a>`_replicated_scales(scales_H: torch.Tensor, weight: DTensor)` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/qk_clip.py#L63) — Represent per-head scales on the same distributed mesh as ``weight``.
- <a id="_scale_mla_heads"></a>`_scale_mla_heads(weight: DTensor, scales_H: torch.Tensor, *, rows_per_head: int, nope_rows_per_head: int, nope_scale_exponent: float, remaining_scale_exponent: float | None)` — [`L80`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/qk_clip.py#L80) — Scale the NoPE and remaining rows of every MLA head in place.
- <a id="_validate_head_sharding"></a>`_validate_head_sharding(weight: DTensor)` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/qk_clip.py#L49) — Require MLA weights to be replicated or contiguously sharded on dim 0.
- <a id="qk_clip"></a>`qk_clip(model_parts: list[nn.Module], *, reduction_mesh: DeviceMesh)` — [`L137`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/qk_clip.py#L137) — Apply the Kimi K2 QK clipping update with the report defaults.
- <a id="register_qk_clip_hook"></a>`register_qk_clip_hook(optimizers: OptimizersContainer, model_parts: list[nn.Module], parallel_dims: ParallelDims)` — [`L180`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/qk_clip.py#L180) — Apply QK clipping after each ordinary optimizer step.

## Module values
- <a id="__all__"></a>`__all__` — [`L201`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/qk_clip.py#L201)

