---
title: 'Module: torchtitan/experiments/tpu/muse_glimmer/attention.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/muse_glimmer/attention.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.muse_glimmer.attention`/
symbols:
  TpuMuseGlimmerAttention.forward: TpuMuseGlimmerAttention#forward().
  SlidingWindowScaledDotProductInnerAttention.forward: SlidingWindowScaledDotProductInnerAttention#forward().
  SlidingWindowScaledDotProductInnerAttention: SlidingWindowScaledDotProductInnerAttention#
  SlidingWindowScaledDotProductInnerAttention.Config: SlidingWindowScaledDotProductInnerAttention#Config#
  SlidingWindowScaledDotProductInnerAttention.Config.window_size: SlidingWindowScaledDotProductInnerAttention#Config#window_size.
  SlidingWindowScaledDotProductInnerAttention.__init__: SlidingWindowScaledDotProductInnerAttention#__init__().
  TpuMuseGlimmerAttention.Config: TpuMuseGlimmerAttention#Config#
  SlidingWindowScaledDotProductInnerAttention.window_size: SlidingWindowScaledDotProductInnerAttention#window_size.
  TpuMuseGlimmerAttention: TpuMuseGlimmerAttention#
  packed_sliding_window_causal_mask: packed_sliding_window_causal_mask().
  _unflatten_to_4d: _unflatten_to_4d().
  sliding_window_causal_mask: sliding_window_causal_mask().
  SlidingWindowScaledDotProductInnerAttention.sliding_window_size: SlidingWindowScaledDotProductInnerAttention#sliding_window_size().
---
# Module: [`torchtitan/experiments/tpu/muse_glimmer/attention.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/attention.py)

## Classes
### <a id="SlidingWindowScaledDotProductInnerAttention"></a>`SlidingWindowScaledDotProductInnerAttention`  ·  implements/extends ScaledDotProductInnerAttention
- def: [`torchtitan/experiments/tpu/muse_glimmer/attention.py:118`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/attention.py#L118) — documented in [tpu-context-parallel-attention](../../../../../concepts/tpu-context-parallel-attention.md)
- doc: SDPA inner attention with an optional causal sliding window.
- signature: `class SlidingWindowScaledDotProductInnerAttention(ScaledDotProductInnerAttention):`
- members:
  - <a id="SlidingWindowScaledDotProductInnerAttention.forward"></a>`forward(self, q_BLHK: torch.Tensor, k_BLHK: torch.Tensor, v_BLHV: torch.Tensor, *, attention_masks: AttentionMasksType | None = None, scale: float | None = None, enable_gqa: bool = False, is_causal: bool = True, positions: torch.Tensor | None = None, segment_ids: torch.Tensor | None = None, **kwargs)` — [`L149`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/attention.py#L149)
  - <a id="SlidingWindowScaledDotProductInnerAttention.sliding_window_size"></a>`sliding_window_size(self)` — [`L143`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/attention.py#L143) — Window in Splash ``LocalMask`` convention (see module docstring).
  - <a id="SlidingWindowScaledDotProductInnerAttention.window_size"></a>`window_size` — [`L140`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/attention.py#L140)
- protocol/private: <a id="SlidingWindowScaledDotProductInnerAttention.__init__"></a>`__init__`[`L134`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/attention.py#L134)
- uses (calls/refs, reference-scoped): [`ScaledDotProductInnerAttention`](../../../models/common/attention.md#ScaledDotProductInnerAttention), [`AttentionMasksType`](../../../models/common/attention.md#AttentionMasksType), [`segment_ids_from_positions`](../../../models/common/attention.md#segment_ids_from_positions), [`forward`](../../../models/common/attention.md#ScaledDotProductInnerAttention.forward), [`Config`](attention.md#SlidingWindowScaledDotProductInnerAttention.Config), [`__init__`](../../../models/common/attention.md#ScaledDotProductInnerAttention.__init__), [`window_size`](attention.md#SlidingWindowScaledDotProductInnerAttention.Config.window_size), [`sdpa_backends`](../../../models/common/attention.md#ScaledDotProductInnerAttention.sdpa_backends), [`packed_sliding_window_causal_mask`](attention.md#packed_sliding_window_causal_mask), [`_unflatten_to_4d`](attention.md#_unflatten_to_4d)
- used by: [`ScaledDotProductInnerAttention`](../../../models/common/attention.md#ScaledDotProductInnerAttention), [`use_tpu_modules`](../qwen3_5/__init__.md#use_tpu_modules), [`use_tpu_attention`](__init__.md#use_tpu_attention), [`forward`](../../../models/common/attention.md#ScaledDotProductInnerAttention.forward)  (7 test-only)

### <a id="SlidingWindowScaledDotProductInnerAttention.Config"></a>`SlidingWindowScaledDotProductInnerAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/muse_glimmer/attention.py:130`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/attention.py#L130)
- signature: `class Config(ScaledDotProductInnerAttention.Config):`
- members:
  - <a id="SlidingWindowScaledDotProductInnerAttention.Config.window_size"></a>`window_size` — [`L132`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/attention.py#L132)
- uses (calls/refs, reference-scoped): [`ScaledDotProductInnerAttention`](../../../models/common/attention.md#ScaledDotProductInnerAttention), [`Config`](../../../models/common/attention.md#ScaledDotProductInnerAttention.Config)
- used by: [`use_tpu_modules`](../qwen3_5/__init__.md#use_tpu_modules), [`use_tpu_attention`](__init__.md#use_tpu_attention), [`__init__`](attention.md#SlidingWindowScaledDotProductInnerAttention.__init__), [`window_size`](attention.md#SlidingWindowScaledDotProductInnerAttention.window_size)  (6 test-only)

### <a id="TpuMuseGlimmerAttention"></a>`TpuMuseGlimmerAttention`  ·  implements/extends Attention
- def: [`torchtitan/experiments/tpu/muse_glimmer/attention.py:218`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/attention.py#L218)
- doc: Muse Glimmer `Attention` that passes `positions` to inner attention.
- signature: `class TpuMuseGlimmerAttention(Attention):`
- members:
  - <a id="TpuMuseGlimmerAttention.forward"></a>`forward(self, x_TD: torch.Tensor, attention_masks: AttentionMasksType | None, positions: torch.Tensor | None = None)` — [`L232`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/attention.py#L232)
- uses (calls/refs, reference-scoped): [`AttentionMasksType`](../../../models/common/attention.md#AttentionMasksType), [`k_norm`](../../../models/common/attention.md#GQAttention.k_norm), [`rope`](../../../models/common/attention.md#GQAttention.rope), [`q_norm`](../../../models/common/attention.md#GQAttention.q_norm), [`Attention`](../../../models/muse_glimmer/model.md#Attention), [`o_gate`](../../../models/muse_glimmer/model.md#Attention.o_gate), [`inner_attention`](../../../models/common/attention.md#GQAttention.inner_attention), [`qkv_linear`](../../../models/common/attention.md#GQAttention.qkv_linear), [`enable_gqa`](../../../models/common/attention.md#GQAttention.enable_gqa), [`wo`](../../../models/common/attention.md#GQAttention.wo), [`scaling`](../../../models/common/attention.md#GQAttention.scaling), [`scale_query_by`](../../../models/muse_glimmer/model.md#Attention.scale_query_by)
- used by: [`forward`](../../../models/muse_glimmer/model.md#Attention.forward), [`use_tpu_attention`](__init__.md#use_tpu_attention), [`Attention`](../../../models/muse_glimmer/model.md#Attention)  (1 test-only)

### <a id="TpuMuseGlimmerAttention.Config"></a>`TpuMuseGlimmerAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/muse_glimmer/attention.py:229`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/attention.py#L229)
- signature: `class Config(Attention.Config):`
- uses (calls/refs, reference-scoped): [`Attention`](../../../models/muse_glimmer/model.md#Attention), [`Config`](../../../models/muse_glimmer/model.md#Attention.Config)
- used by: [`use_tpu_attention`](__init__.md#use_tpu_attention)  (1 test-only)

## Functions
- <a id="_unflatten_to_4d"></a>`_unflatten_to_4d(q: torch.Tensor, k: torch.Tensor, v: torch.Tensor)` — [`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/attention.py#L88) — TT-UNFLATTEN-SHIM: reshapes folded ``[T, H, D]`` to ``[B, L, H, D]``.
- <a id="packed_sliding_window_causal_mask"></a>`packed_sliding_window_causal_mask(seq_len: int, window_size: int | None, device: torch.device, *, segment_ids_BL: torch.Tensor | None = None)` — [`L60`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/attention.py#L60) — Causal (optionally windowed) mask restricted to each packed document.
- <a id="sliding_window_causal_mask"></a>`sliding_window_causal_mask(seq_len: int, window_size: int | None, device: torch.device)` — [`L44`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/attention.py#L44) — Returns a ``[seq_len, seq_len]`` bool mask with ``0 <= q - k < window``.

