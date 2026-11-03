---
title: 'Module: src/vllm_torchtpu/runner/mm_video_chunking.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/runner/mm_video_chunking.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.runner.mm_video_chunking`/
symbols:
  embed_multimodal_chunked: embed_multimodal_chunked().
  chunked_video_encoding: chunked_video_encoding().
  _encode_video_item: _encode_video_item().
  get_video_chunk_patch_size: get_video_chunk_patch_size().
  logger: logger.
  chunked_video_encoding.chunked_embed_multimodal: chunked_video_encoding().chunked_embed_multimodal().
  _UNSET: _UNSET.
  _VIDEO_PIXEL_KEYS: _VIDEO_PIXEL_KEYS.
  _VIDEO_GRID_KEYS: _VIDEO_GRID_KEYS.
  _select_item_timestamps: _select_item_timestamps().
  _slice_timestamps: _slice_timestamps().
---
# Module: [`src/vllm_torchtpu/runner/mm_video_chunking.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_video_chunking.py)

## Functions
- <a id="_encode_video_item"></a>`_encode_video_item(embed_fn: Callable[..., MultiModalEmbeddings], pixel_key: str, grid_key: str, item_kwargs: dict[str, Any], max_patches: int)` — [`L251`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_video_chunking.py#L251) — Encode one video item, splitting into chunks when patch count exceeds budget.
- <a id="_select_item_timestamps"></a>`_select_item_timestamps(timestamps: Any, i: int)` — [`L328`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_video_chunking.py#L328) — Select item `i`'s timestamps from a batched group.
- <a id="_slice_timestamps"></a>`_slice_timestamps(timestamps: Any, start: int, end: int)` — [`L351`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_video_chunking.py#L351) — Slice a per-temporal-patch timestamps field to `[start, end)`.
- <a id="chunked_video_encoding.chunked_embed_multimodal"></a>`chunked_embed_multimodal(**mm_kwargs: Any)` — [`L128`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_video_chunking.py#L128)
- <a id="chunked_video_encoding"></a>`chunked_video_encoding(model: torch.nn.Module, model_config: ModelConfig | None)` — [`L106`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_video_chunking.py#L106) — Wrap the model's `embed_multimodal` to temporally chunk oversized videos.
- <a id="embed_multimodal_chunked"></a>`embed_multimodal_chunked(embed_fn: Callable[..., MultiModalEmbeddings], mm_kwargs: dict[str, Any], max_patches: int)` — [`L143`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_video_chunking.py#L143) — Run `embed_fn` on multimodal kwargs, splitting large videos into chunks.
- <a id="get_video_chunk_patch_size"></a>`get_video_chunk_patch_size(model_config: ModelConfig | None, default_max_patches: int = 0)` — [`L65`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_video_chunking.py#L65) — Return the per-forward patch budget, or 0 when chunking is disabled.

## Module values
- <a id="_UNSET"></a>`_UNSET` — [`L62`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_video_chunking.py#L62)
- <a id="_VIDEO_GRID_KEYS"></a>`_VIDEO_GRID_KEYS` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_video_chunking.py#L59)
- <a id="_VIDEO_PIXEL_KEYS"></a>`_VIDEO_PIXEL_KEYS` — [`L58`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_video_chunking.py#L58)
- <a id="logger"></a>`logger` — [`L52`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_video_chunking.py#L52)

