---
title: 'Module: src/vllm_torchtpu/experimental/export/rope_patch.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/experimental/export/rope_patch.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.experimental.export.rope_patch`/
symbols:
  InGraphCosSinCache._rows: InGraphCosSinCache#_rows().
  _module_cos_sin_segments: _module_cos_sin_segments().
  patch_in_graph_rotary_embedding: patch_in_graph_rotary_embedding().
  InGraphCosSinCache.to: InGraphCosSinCache#to().
  _in_graph_rope_forward: _in_graph_rope_forward().
  patch_cos_sin_cache_buffers: patch_cos_sin_cache_buffers().
  CosSinSegment: CosSinSegment#
  CosSinSegment.start: CosSinSegment#start.
  _in_graph_cos_sin: _in_graph_cos_sin().
  compute_mrope_dim_modalities: compute_mrope_dim_modalities().
  CosSinSegment.mscale: CosSinSegment#mscale.
  InGraphCosSinCache: InGraphCosSinCache#
  InGraphCosSinCache.shape: InGraphCosSinCache#shape.
  InGraphCosSinCache.__init__: InGraphCosSinCache#__init__().
  InGraphCosSinCache.size: InGraphCosSinCache#size().
  InGraphCosSinCache.index_select: InGraphCosSinCache#index_select().
  InGraphCosSinCache.__getitem__: InGraphCosSinCache#__getitem__().
  is_in_graph_rope_eligible: is_in_graph_rope_eligible().
  _apply_rotary_emb: _apply_rotary_emb().
  _build_device_vector_f32: _build_device_vector_f32().
  CosSinSegment.inv_freq: CosSinSegment#inv_freq.
  InGraphCosSinCache.segments: InGraphCosSinCache#segments.
  InGraphCosSinCache.dtype: InGraphCosSinCache#dtype.
  _select_mrope_positions: _select_mrope_positions().
  CosSinSegment.length: CosSinSegment#length.
  _call_compute_inv_freq: _call_compute_inv_freq().
  InGraphCosSinCache.ndim: InGraphCosSinCache#ndim.
  InGraphCosSinCache.__torch_function__: InGraphCosSinCache#__torch_function__().
---
# Module: [`src/vllm_torchtpu/experimental/export/rope_patch.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py)

## Classes
### <a id="CosSinSegment"></a>`CosSinSegment`
- def: [`src/vllm_torchtpu/experimental/export/rope_patch.py:314`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L314)
- doc: Rows `[start, start + length)` of a cache: `[cos | sin](p * inv_freq) * mscale`.
- signature: `class CosSinSegment:`
- members:
  - <a id="CosSinSegment.inv_freq"></a>`inv_freq` — [`L322`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L322)
  - <a id="CosSinSegment.length"></a>`length` — [`L321`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L321)
  - <a id="CosSinSegment.mscale"></a>`mscale` — [`L323`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L323)
  - <a id="CosSinSegment.start"></a>`start` — [`L320`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L320)
- used by: [`_rows`](rope_patch.md#InGraphCosSinCache._rows), [`_module_cos_sin_segments`](rope_patch.md#_module_cos_sin_segments), [`__init__`](rope_patch.md#InGraphCosSinCache.__init__)

### <a id="InGraphCosSinCache"></a>`InGraphCosSinCache`
- def: [`src/vllm_torchtpu/experimental/export/rope_patch.py:416`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L416)
- doc: Stands in for a rotary cos/sin buffer, computing looked-up rows in-graph.
- signature: `class InGraphCosSinCache:`
- members:
  - <a id="InGraphCosSinCache.index_select"></a>`index_select(self, dim: int, index: torch.Tensor)` — [`L451`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L451)
  - <a id="InGraphCosSinCache.size"></a>`size(self, dim: int | None = None)` — [`L437`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L437)
  - <a id="InGraphCosSinCache.to"></a>`to(self, *args: Any, **kwargs: Any)` — [`L440`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L440)
  - <a id="InGraphCosSinCache.dtype"></a>`dtype` — [`L433`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L433)
  - <a id="InGraphCosSinCache.ndim"></a>`ndim` — [`L435`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L435)
  - <a id="InGraphCosSinCache.segments"></a>`segments` — [`L432`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L432)
  - <a id="InGraphCosSinCache.shape"></a>`shape` — [`L434`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L434)
- protocol/private: <a id="InGraphCosSinCache.__getitem__"></a>`__getitem__`[`L456`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L456), <a id="InGraphCosSinCache.__init__"></a>`__init__`[`L425`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L425), <a id="InGraphCosSinCache.__torch_function__"></a>`__torch_function__`[`L465`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L465), <a id="InGraphCosSinCache._rows"></a>`_rows`[`L480`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L480)
- uses (calls/refs, reference-scoped): [`CosSinSegment`](rope_patch.md#CosSinSegment), [`start`](rope_patch.md#CosSinSegment.start), [`mscale`](rope_patch.md#CosSinSegment.mscale), [`_build_device_vector_f32`](rope_patch.md#_build_device_vector_f32), [`inv_freq`](rope_patch.md#CosSinSegment.inv_freq)
- used by: [`patch_cos_sin_cache_buffers`](rope_patch.md#patch_cos_sin_cache_buffers)

## Functions
- <a id="_apply_rotary_emb"></a>`_apply_rotary_emb(x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor, is_neox_style: bool)` — [`L115`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L115) — Applies rotary embedding to `x[num_tokens, num_heads, rotary_dim]`.
- <a id="_build_device_vector_f32"></a>`_build_device_vector_f32(values: tuple[float, ...], device: torch.device, *, base: float | None = None, rotary_dim: int | None = None)` — [`L150`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L150) — Materializes a 1-D float32 frequency vector as pure in-graph HLO ops.
- <a id="_call_compute_inv_freq"></a>`_call_compute_inv_freq(module: Any)` — [`L326`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L326) — Calls `module._compute_inv_freq` with the attribute its signature names.
- <a id="_in_graph_cos_sin"></a>`_in_graph_cos_sin(pos_for_freq: torch.Tensor, inv_freq: tuple[float, ...], cache_dtype: torch.dtype, dtype: torch.dtype, *, base: float | None = None, rotary_dim: int | None = None)` — [`L195`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L195) — Returns `[cos | sin]` rows in `dtype` for `[N]` or `[N, D/2]` positions.
- <a id="_in_graph_rope_forward"></a>`_in_graph_rope_forward(self: Any, positions: torch.Tensor, query: torch.Tensor, key: torch.Tensor | None = None, offsets: torch.Tensor | None = None)` — [`L219`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L219) — In-graph `RotaryEmbedding` / `MRotaryEmbedding` forward, no `cos_sin_cache`.
- <a id="_module_cos_sin_segments"></a>`_module_cos_sin_segments(module: nn.Module, cache: torch.Tensor)` — [`L343`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L343) — Extracts analytical `CosSinSegment`s from `module`'s RoPE attributes.
- <a id="_select_mrope_positions"></a>`_select_mrope_positions(pos_2d: torch.Tensor, dim_modalities: tuple[int, ...])` — [`L173`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L173) — Selects per-frequency positions `[N, D/2]` from `pos_2d[3, N]` in pure HLO.
- <a id="compute_mrope_dim_modalities"></a>`compute_mrope_dim_modalities(module: nn.Module)` — [`L84`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L84) — Returns the per-frequency modality `{0, 1, 2}` for `[3, N]` M-RoPE positions.
- <a id="is_in_graph_rope_eligible"></a>`is_in_graph_rope_eligible(module: nn.Module)` — [`L35`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L35) — Returns True if `module`'s cos/sin depend only on `positions` and `inv_freq`.
- <a id="patch_cos_sin_cache_buffers"></a>`patch_cos_sin_cache_buffers(model: nn.Module)` — [`L499`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L499) — Replaces every remaining rotary cos/sin cache buffer with in-graph rows.
- <a id="patch_in_graph_rotary_embedding"></a>`patch_in_graph_rotary_embedding(model: nn.Module)` — [`L269`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/rope_patch.py#L269) — Replaces `cos_sin_cache` buffer lookup with pure in-graph RoPE on `model`.

