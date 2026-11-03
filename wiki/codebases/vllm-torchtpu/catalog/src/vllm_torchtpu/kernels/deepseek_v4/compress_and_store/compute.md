---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.compress_and_store.compute`/
symbols:
  merge_rope_row: merge_rope_row().
  gather_from_page_buffer: gather_from_page_buffer().
  interleaved_rope_vector: interleaved_rope_vector().
  quantize_fp8_tiled: quantize_fp8_tiled().
  quantize_fp8_lane_periodic: quantize_fp8_lane_periodic().
  pack_nope_lane_periodic: pack_nope_lane_periodic().
  pack_nope_tiled: pack_nope_tiled().
  rope_words_tiled: rope_words_tiled().
  merge_slot_updates: merge_slot_updates().
  stage_sal_columns: stage_sal_columns().
  gather_from_page_buffer._gather_indexer_token: gather_from_page_buffer()._gather_indexer_token().
  gather_from_page_buffer._gather_token: gather_from_page_buffer()._gather_token().
  gather_from_page_buffer._gather_token.body_w: gather_from_page_buffer()._gather_token().body_w().
  gather_from_page_buffer._gather_token.body_w.gather_loop: gather_from_page_buffer()._gather_token().body_w().gather_loop().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py)

## Functions
- <a id="gather_from_page_buffer._gather_indexer_token"></a>`_gather_indexer_token(n)` — [`L414`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py#L414)
- <a id="gather_from_page_buffer._gather_token"></a>`_gather_token(n)` — [`L471`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py#L471)
- <a id="gather_from_page_buffer._gather_token.body_w"></a>`body_w(w)` — [`L481`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py#L481)
- <a id="gather_from_page_buffer"></a>`gather_from_page_buffer(page_buffer, positions_ref, kv_window_u8, score_window_u8, *, global_idx: jax.Array, num_tokens: int, window: int, block_size: int, pages_to_buffer_per_token: int, field_rows: int, state_rows_per_token: int, overlap: bool, token_valid: list[jax.Array], is_indexer: bool = False)` — [`L388`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py#L388) — Extracts kv_window, score_window from page buffer.
- <a id="gather_from_page_buffer._gather_token.body_w.gather_loop"></a>`gather_loop(d_idx)` — [`L501`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py#L501)
- <a id="interleaved_rope_vector"></a>`interleaved_rope_vector(x, cos_val_32, sin_val_32)` — [`L23`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py#L23) — Applies interleaved Rotary Position Embedding (RoPE) to a vector.
- <a id="merge_rope_row"></a>`merge_rope_row(row, kv_slots, words, rope_lane, n)` — [`L228`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py#L228) — Writes every tile token whose RoPE lands in token n's row into it.
- <a id="merge_slot_updates"></a>`merge_slot_updates(slots_val, kv_slots, val_padded, n)` — [`L257`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py#L257) — multiple KV slots are packed into a single physical 512-byte row in HBM.
- <a id="pack_nope_lane_periodic"></a>`pack_nope_lane_periodic(q, scale, nope_dim, nope_width_bytes, last_dim_size)` — [`L170`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py#L170) — Pack `nope_dim` fp8 values followed by the e8m0 scales.
- <a id="pack_nope_tiled"></a>`pack_nope_tiled(q, scale, nope_dim, block_size, nope_width_bytes=512, last_dim_size=128)` — [`L180`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py#L180)
- <a id="quantize_fp8_lane_periodic"></a>`quantize_fp8_lane_periodic(x, period, nope_dim)` — [`L139`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py#L139) — Quantize with one e8m0 scale per lane of a `period`-lane cycle.
- <a id="quantize_fp8_tiled"></a>`quantize_fp8_tiled(x, block_size)` — [`L99`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py#L99)
- <a id="rope_words_tiled"></a>`rope_words_tiled(rope_slot_ropped, rope_head_dim)` — [`L214`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py#L214) — RoPE channels as cache words: low half bf16 ``k``, high half ``k + 32``.
- <a id="stage_sal_columns"></a>`stage_sal_columns(records_t_ref, records, first_token)` — [`L303`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compute.py#L303) — Copies `records` into lanes `[first_token, first_token + n)`.

