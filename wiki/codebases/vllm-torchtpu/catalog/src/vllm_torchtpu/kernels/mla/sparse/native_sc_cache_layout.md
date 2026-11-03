---
title: 'Module: src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.mla.sparse.native_sc_cache_layout`/
symbols:
  LANE_BYTES: LANE_BYTES.
  NOPE_SUBROWS: NOPE_SUBROWS.
  pack_rope_banded: pack_rope_banded().
  pack_native_caches: pack_native_caches().
  pack_nope: pack_nope().
  ROPE_WORDS: ROPE_WORDS.
  unpack_rope_banded: unpack_rope_banded().
  WORD_BYTES: WORD_BYTES.
  unpack_nope: unpack_nope().
  pack_rope_packed: pack_rope_packed().
  pack_selected_rope_for_tc: pack_selected_rope_for_tc().
  flatten_rope_rows: flatten_rope_rows().
  flatten_nope_rows: flatten_nope_rows().
  source_bytes_per_token: source_bytes_per_token().
  _require_u8: _require_u8().
---
# Module: [`src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py)

## Functions
- <a id="_require_u8"></a>`_require_u8(name: str, value: np.ndarray, suffix: tuple[int, ...])` — [`L31`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py#L31)
- <a id="flatten_nope_rows"></a>`flatten_nope_rows(nope_i32: np.ndarray)` — [`L163`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py#L163)
- <a id="flatten_rope_rows"></a>`flatten_rope_rows(rope_i32: np.ndarray, rope_words: int = ROPE_WORDS)` — [`L170`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py#L170)
- <a id="pack_native_caches"></a>`pack_native_caches(nope_u8: np.ndarray, rope_u8: np.ndarray, page_size: int = 256)` — [`L137`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py#L137) — Pack complete paged caches into the standalone native-SC ABI.
- <a id="pack_nope"></a>`pack_nope(nope_u8: np.ndarray)` — [`L41`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py#L41) — Pack ``[..., token, 4, 128] u8`` as ``[..., token, 128] u32``.
- <a id="pack_rope_banded"></a>`pack_rope_banded(rope_u8: np.ndarray)` — [`L68`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py#L68) — Pack native-SC ROPE words into four-token, 128-word HBM rows.
- <a id="pack_rope_packed"></a>`pack_rope_packed(rope_u8: np.ndarray)` — [`L104`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py#L104) — Pack ``[..., token, D] u8`` as ``[..., token / k, 128] u32`` (``k = 512 / D``).
- <a id="pack_selected_rope_for_tc"></a>`pack_selected_rope_for_tc(rope_u8: np.ndarray)` — [`L156`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py#L156) — Host oracle for the gather's four-token register delta-swap.
- <a id="source_bytes_per_token"></a>`source_bytes_per_token(nope_i32: np.ndarray, rope_i32: np.ndarray)` — [`L179`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py#L179) — Return the logical allocation bytes per token for both caches.
- <a id="unpack_nope"></a>`unpack_nope(nope_i32: np.ndarray)` — [`L53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py#L53) — Inverse of :func:`pack_nope`.
- <a id="unpack_rope_banded"></a>`unpack_rope_banded(rope_i32: np.ndarray)` — [`L83`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py#L83) — Inverse of :func:`pack_rope_banded`.

## Module values
- <a id="LANE_BYTES"></a>`LANE_BYTES` — [`L26`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py#L26)
- <a id="NOPE_SUBROWS"></a>`NOPE_SUBROWS` — [`L25`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py#L25)
- <a id="ROPE_WORDS"></a>`ROPE_WORDS` — [`L28`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py#L28)
- <a id="WORD_BYTES"></a>`WORD_BYTES` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/native_sc_cache_layout.py#L27)

