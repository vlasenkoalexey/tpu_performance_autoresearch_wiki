---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/csa_cache_layout.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/csa_cache_layout.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.csa_cache_layout`/
symbols:
  as_u8_slabs: as_u8_slabs().
  ROW_WORDS: ROW_WORDS.
  ROPE_WORDS: ROPE_WORDS.
  ROPE_TOKENS_PER_ROW: ROPE_TOKENS_PER_ROW.
  u8_slab_shape: u8_slab_shape().
  words_to_slabs: words_to_slabs().
  is_word_array: is_word_array().
  encode_rope: encode_rope().
  ROPE_DIM: ROPE_DIM.
  rope_words: rope_words().
  SLAB_ROWS: SLAB_ROWS.
  slabs_to_words: slabs_to_words().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/csa_cache_layout.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/csa_cache_layout.py)

## Functions
- <a id="as_u8_slabs"></a>`as_u8_slabs(ref)` — [`L67`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/csa_cache_layout.py#L67) — View a cache ref as ``uint8[num_pages, rows, 4, lanes]`` slabs. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="encode_rope"></a>`encode_rope(rope: jax.Array)` — [`L112`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/csa_cache_layout.py#L112) — bf16 ``[num_tokens, 64]`` -> the int32 ``[num_tokens // 4, 128]`` rows.
- <a id="is_word_array"></a>`is_word_array(dtype)` — [`L54`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/csa_cache_layout.py#L54) — Whether a cache is declared as 32-bit words rather than uint8 slabs.
- <a id="rope_words"></a>`rope_words(rope: jax.Array)` — [`L104`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/csa_cache_layout.py#L104) — bf16 ``[..., 64]`` -> int32 ``[..., 32]``: word k = bf16 k | bf16 k+32.
- <a id="slabs_to_words"></a>`slabs_to_words(x: jax.Array)` — [`L87`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/csa_cache_layout.py#L87) — uint8 ``[..., 4, n]`` -> int32 ``[..., n]``; byte b from sub-row b.
- <a id="u8_slab_shape"></a>`u8_slab_shape(shape: tuple[int, ...], dtype)` — [`L59`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/csa_cache_layout.py#L59) — The ``(num_pages, rows, 4, lanes)`` uint8 view of a cache array.
- <a id="words_to_slabs"></a>`words_to_slabs(w: jax.Array)` — [`L95`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/csa_cache_layout.py#L95) — int32 ``[..., n]`` -> uint8 ``[..., 4, n]``; inverse of the above.

## Module values
- <a id="ROPE_DIM"></a>`ROPE_DIM` — [`L50`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/csa_cache_layout.py#L50)
- <a id="ROPE_TOKENS_PER_ROW"></a>`ROPE_TOKENS_PER_ROW` — [`L51`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/csa_cache_layout.py#L51)
- <a id="ROPE_WORDS"></a>`ROPE_WORDS` — [`L49`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/csa_cache_layout.py#L49)
- <a id="ROW_WORDS"></a>`ROW_WORDS` — [`L47`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/csa_cache_layout.py#L47)
- <a id="SLAB_ROWS"></a>`SLAB_ROWS` — [`L48`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/csa_cache_layout.py#L48)

