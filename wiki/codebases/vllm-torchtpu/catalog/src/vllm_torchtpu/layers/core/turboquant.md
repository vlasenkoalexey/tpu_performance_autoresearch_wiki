---
title: 'Module: src/vllm_torchtpu/layers/core/turboquant.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/core/turboquant.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.core.turboquant`/
symbols:
  _dequant_tq_page_vreg: _dequant_tq_page_vreg().
  _quantize_kv_components: _quantize_kv_components().
  tq_ragged_paged_attention: tq_ragged_paged_attention().
  _update_tq_page_vreg: _update_tq_page_vreg().
  _plane_word_counts: _plane_word_counts().
  _WORD_SIZE: _WORD_SIZE.
  make_tables: make_tables().
  TQLayout.is_key_fp8: TQLayout#is_key_fp8().
  _pack_new_tq_tokens_128: _pack_new_tq_tokens_128().
  TQLayout.head_dim: TQLayout#head_dim.
  TQLayout.page_words_128: TQLayout#page_words_128().
  TQLayout.page_size_from_words_128: TQLayout#page_size_from_words_128().
  TQLayout: TQLayout#
  TQLayout.__post_init__: TQLayout#__post_init__().
  TQLayout.key_bits: TQLayout#key_bits.
  TQLayout.validate_page_size: TQLayout#validate_page_size().
  TQLayout.supported_page_sizes: TQLayout#supported_page_sizes().
  _dequant_tq_page_vreg._bcast_col: _dequant_tq_page_vreg()._bcast_col().
  TQLayout.key_mse_bytes: TQLayout#key_mse_bytes().
  TQLayout.value_data_bytes: TQLayout#value_data_bytes().
  _pack_new_tq_tokens_128._to_fold_words: _pack_new_tq_tokens_128()._to_fold_words().
  TQTables: TQTables#
  TQLayout.value_bits: TQLayout#value_bits.
  rotate: rotate().
  tq_ragged_paged_attention._apply_tok: tq_ragged_paged_attention()._apply_tok().
  _SUBLANE_WORDS: _SUBLANE_WORDS.
  TQLayout.slot_size_aligned: TQLayout#slot_size_aligned.
  TQTables.hadamard: TQTables#hadamard.
  TQTables.centroids: TQTables#centroids.
  _f32_to_bf16_bytes: _f32_to_bf16_bytes().
  is_turboquant_kv_cache_dtype: is_turboquant_kv_cache_dtype().
  TQLayout.from_tq_config: TQLayout#from_tq_config().
  _KEY_NORM_EPS: _KEY_NORM_EPS.
  TQTables.midpoints: TQTables#midpoints.
  _bf16_u16_to_f32_vreg: _bf16_u16_to_f32_vreg().
  _unpack_bits_vreg: _unpack_bits_vreg().
  _pack_new_tq_tokens_128._pack_half: _pack_new_tq_tokens_128()._pack_half().
  _update_tq_page_vreg._merge_bits_vreg: _update_tq_page_vreg()._merge_bits_vreg().
  _update_tq_page_vreg._reduce_or_axis0: _update_tq_page_vreg()._reduce_or_axis0().
  _CENTROID_NORM_EPS: _CENTROID_NORM_EPS.
  _VALUE_SCALE_MIN: _VALUE_SCALE_MIN.
  TQLayout.norm_correction: TQLayout#norm_correction.
  hadamard_matrix: hadamard_matrix().
  _lookup_centroids_vreg: _lookup_centroids_vreg().
  TURBOQUANT_KV_CACHE_DTYPES.TURBOQUANT_KV_CACHE_DTYPES: TURBOQUANT_KV_CACHE_DTYPES.TURBOQUANT_KV_CACHE_DTYPES.
---
# Module: [`src/vllm_torchtpu/layers/core/turboquant.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py)

## Classes
### <a id="TQLayout"></a>`TQLayout`
- def: [`src/vllm_torchtpu/layers/core/turboquant.py:84`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L84)
- doc: Byte geometry of one TurboQuant page and slot (one token, one KV head).
- signature: `class TQLayout:`
- members:
  - <a id="TQLayout.from_tq_config"></a>`from_tq_config(cls, tq_config: Any)` — [`L106`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L106)
  - <a id="TQLayout.is_key_fp8"></a>`is_key_fp8(self)` — [`L116`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L116) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
  - <a id="TQLayout.key_mse_bytes"></a>`key_mse_bytes(self)` — [`L132`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L132)
  - <a id="TQLayout.page_size_from_words_128"></a>`page_size_from_words_128(self, page_words: int)` — [`L145`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L145) — Recovers `page_size` (slots per page) from `page_words_128(page_size)`.
  - <a id="TQLayout.page_words_128"></a>`page_words_128(self, page_size: int)` — [`L139`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L139) — Number of 128-byte words needed to store `page_size` slots per head.
  - <a id="TQLayout.supported_page_sizes"></a>`supported_page_sizes(self)` — [`L120`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L120)
  - <a id="TQLayout.validate_page_size"></a>`validate_page_size(self, page_size: int)` — [`L123`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L123)
  - <a id="TQLayout.value_data_bytes"></a>`value_data_bytes(self)` — [`L136`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L136)
  - <a id="TQLayout.head_dim"></a>`head_dim` — [`L87`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L87)
  - <a id="TQLayout.key_bits"></a>`key_bits` — [`L88`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L88)
  - <a id="TQLayout.norm_correction"></a>`norm_correction` — [`L90`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L90)
  - <a id="TQLayout.slot_size_aligned"></a>`slot_size_aligned` — [`L91`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L91)
  - <a id="TQLayout.value_bits"></a>`value_bits` — [`L89`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L89)
- protocol/private: <a id="TQLayout.__post_init__"></a>`__post_init__`[`L93`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L93)
- uses (calls/refs, reference-scoped): [`_WORD_SIZE`](turboquant.md#_WORD_SIZE), [`_SUBLANE_WORDS`](turboquant.md#_SUBLANE_WORDS)
- used by: [`_dequant_tq_page_vreg`](turboquant.md#_dequant_tq_page_vreg), [`_quantize_kv_components`](turboquant.md#_quantize_kv_components), [`tq_ragged_paged_attention`](turboquant.md#tq_ragged_paged_attention), [`_update_tq_page_vreg`](turboquant.md#_update_tq_page_vreg), [`_plane_word_counts`](turboquant.md#_plane_word_counts), [`make_tables`](turboquant.md#make_tables), [`_pack_new_tq_tokens_128`](turboquant.md#_pack_new_tq_tokens_128)

### <a id="TQTables"></a>`TQTables`
- def: [`src/vllm_torchtpu/layers/core/turboquant.py:157`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L157)
- doc: Constant tables used by quantize/dequantize (host numpy arrays).
- signature: `class TQTables:`
- members:
  - <a id="TQTables.centroids"></a>`centroids` — [`L164`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L164)
  - <a id="TQTables.hadamard"></a>`hadamard` — [`L163`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L163)
  - <a id="TQTables.midpoints"></a>`midpoints` — [`L165`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L165)
- used by: [`_dequant_tq_page_vreg`](turboquant.md#_dequant_tq_page_vreg), [`_quantize_kv_components`](turboquant.md#_quantize_kv_components), [`tq_ragged_paged_attention`](turboquant.md#tq_ragged_paged_attention), [`make_tables`](turboquant.md#make_tables)

## Functions
- <a id="tq_ragged_paged_attention._apply_tok"></a>`_apply_tok(tok_i, cache)` — [`L789`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L789)
- <a id="_dequant_tq_page_vreg._bcast_col"></a>`_bcast_col(row: jax.Array)` — [`L324`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L324)
- <a id="_bf16_u16_to_f32_vreg"></a>`_bf16_u16_to_f32_vreg(lo_u32: jax.Array, hi_u32: jax.Array)` — [`L232`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L232) — Reconstructs `f32` in VREGs from low/high `bfloat16` byte planes (`u32`).
- <a id="_dequant_tq_page_vreg"></a>`_dequant_tq_page_vreg(pages_h: Any, kv_dtype: jnp.dtype, *, layout: TQLayout, tables: TQTables, return_k_norm: bool = False)` — [`L302`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L302) — Dequantizes `(page, kv_head)` blocks from `u8[W, 128]` into VREGs. — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="_f32_to_bf16_bytes"></a>`_f32_to_bf16_bytes(val: jax.Array)` — [`L457`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L457) — Splits `f32[..., 1]` into `(lo_u8[..., 1], hi_u8[..., 1])` as `bf16` bytes.
- <a id="_lookup_centroids_vreg"></a>`_lookup_centroids_vreg(idx: jax.Array, bits: int, centroids: np.ndarray, *, scale: jax.Array | None = None)` — [`L237`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L237) — VREG packed-pair select of `centroids[idx]` with IEEE-754 bitwise sign.
- <a id="_update_tq_page_vreg._merge_bits_vreg"></a>`_merge_bits_vreg(old_plane: jax.Array, new_idx: jax.Array, bits: int)` — [`L605`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L605)
- <a id="_pack_new_tq_tokens_128._pack_half"></a>`_pack_half(cols: list[jax.Array], base: int)` — [`L564`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L564)
- <a id="_pack_new_tq_tokens_128"></a>`_pack_new_tq_tokens_128(nk_u: jax.Array, nv_i: jax.Array, n_meta: jax.Array, page_size: int, layout: TQLayout)` — [`L523`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L523) — Packs per-token quantized components into `u8[T, W_new, H, 128]`.
- <a id="_plane_word_counts"></a>`_plane_word_counts(page_size: int, layout: TQLayout)` — [`L209`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L209) — Number of 128-byte words per head for `(k_plane, v_plane, meta_plane)`. — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="_quantize_kv_components"></a>`_quantize_kv_components(key: jax.Array, value: jax.Array, layout: TQLayout, tables: TQTables, *, rotated_key: jax.Array | None = None)` — [`L465`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L465) — Quantizes K/V directly into lane-aligned `(k_unpacked, v_idx, meta_bytes)`. — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="_update_tq_page_vreg._reduce_or_axis0"></a>`_reduce_or_axis0(val: jax.Array)` — [`L645`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L645)
- <a id="_pack_new_tq_tokens_128._to_fold_words"></a>`_to_fold_words(arr: jax.Array)` — [`L535`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L535)
- <a id="_unpack_bits_vreg"></a>`_unpack_bits_vreg(planes: list[jax.Array], bits: int, *, mask_lo: bool = True, out_dtype: Any = jnp.uint32)` — [`L272`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L272) — Unpacks `u8[P*bits//8, 128]` slices -> `out_dtype[len(planes)*P, 128]`.
- <a id="_update_tq_page_vreg"></a>`_update_tq_page_vreg(old_page: jax.Array, new_tok: jax.Array | list[jax.Array], valid_mask: jax.Array, *, slot_idx: jax.Array | None = None, layout: TQLayout)` — [`L580`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L580) — Merges new tokens' quantized components into a single KV head's page in VREGs. — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="hadamard_matrix"></a>`hadamard_matrix(head_dim: int)` — [`L168`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L168) — Orthonormal Sylvester Hadamard matrix, as in vLLM's `_build_hadamard`.
- <a id="is_turboquant_kv_cache_dtype"></a>`is_turboquant_kv_cache_dtype(cache_dtype: object)` — [`L70`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L70)
- <a id="make_tables"></a>`make_tables(layout: TQLayout, centroids: np.ndarray)` — [`L178`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L178) — Builds the constant tables from the Lloyd-Max centroids. — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="rotate"></a>`rotate(inputs: jax.Array, hadamard: jax.Array)` — [`L192`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L192) — `inputs @ H` in `f32` (uses `bf16` MXU with `f32` accum for `bf16` inputs).
- <a id="tq_ragged_paged_attention"></a>`tq_ragged_paged_attention(queries: jax.Array, keys: jax.Array, values: jax.Array, kv_cache: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, *, layout: TQLayout, tables: TQTables, rpa_fn: Callable, sm_scale: float, sliding_window: int | None = None, soft_cap: float | None = None, skip_kv_update: bool = False)` — [`L712`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L712) — Ragged paged attention over a compressed TurboQuant `uint8` KV cache. — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)

## Module values
- <a id="TURBOQUANT_KV_CACHE_DTYPES.TURBOQUANT_KV_CACHE_DTYPES"></a>`TURBOQUANT_KV_CACHE_DTYPES` — [`L62`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L62)
- <a id="_CENTROID_NORM_EPS"></a>`_CENTROID_NORM_EPS` — [`L79`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L79)
- <a id="_KEY_NORM_EPS"></a>`_KEY_NORM_EPS` — [`L78`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L78)
- <a id="_SUBLANE_WORDS"></a>`_SUBLANE_WORDS` — [`L58`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L58)
- <a id="_VALUE_SCALE_MIN"></a>`_VALUE_SCALE_MIN` — [`L80`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L80)
- <a id="_WORD_SIZE"></a>`_WORD_SIZE` — [`L57`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/turboquant.py#L57) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)

