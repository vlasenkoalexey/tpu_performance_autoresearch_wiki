---
title: 'Module: src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.kimi_k3.mega_kda.kernel`/
symbols:
  _chunk_kda_fwd_native_segids_impl: _chunk_kda_fwd_native_segids_impl().
  _build_chunk_metadata: _build_chunk_metadata().
  _fwd_mega_kernel_native_segids._boundary: _fwd_mega_kernel_native_segids()._boundary().
  _fwd_mega_kernel_native_segids._dma_state_to_ht: _fwd_mega_kernel_native_segids()._dma_state_to_ht().
  _chunk_kda_fwd_native_segids: _chunk_kda_fwd_native_segids.
  _fwd_mega_kernel_native_segids._partial: _fwd_mega_kernel_native_segids()._partial().
  _native_residual_layout_jit_for_sharding: _native_residual_layout_jit_for_sharding().
  CHUNK_KIND_ALL_PAD: CHUNK_KIND_ALL_PAD.
  _get_native_residual_layout_jit: _get_native_residual_layout_jit().
  _fwd_mega_kernel_native_segids: _fwd_mega_kernel_native_segids().
  align_up: align_up().
  _fwd_mega_kernel_native_segids._read_h0: _fwd_mega_kernel_native_segids()._read_h0().
  _chunk_kda_fwd_native_segids_impl._pad: _chunk_kda_fwd_native_segids_impl()._pad().
  _chunk_kda_fwd_native_segids_impl._in_map: _chunk_kda_fwd_native_segids_impl()._in_map().
  _chunk_kda_fwd_native_segids_impl._out_map: _chunk_kda_fwd_native_segids_impl()._out_map().
  _fwd_mega_kernel_native_segids_packed: _fwd_mega_kernel_native_segids_packed().
  CHUNK_KIND_FULL_IN_SEGMENT: CHUNK_KIND_FULL_IN_SEGMENT.
  _fwd_mega_kernel_native_segids._all_pad: _fwd_mega_kernel_native_segids()._all_pad().
  _fwd_mega_kernel_native_segids._full: _fwd_mega_kernel_native_segids()._full().
  _fwd_mega_kernel_native_segids._full._save_prev: _fwd_mega_kernel_native_segids()._full()._save_prev().
  _fwd_mega_kernel_native_segids._full._load_h0: _fwd_mega_kernel_native_segids()._full()._load_h0().
  _fwd_mega_kernel_native_segids._full._final: _fwd_mega_kernel_native_segids()._full()._final().
  _fwd_mega_kernel_native_segids._partial._save_prev: _fwd_mega_kernel_native_segids()._partial()._save_prev().
  _fwd_mega_kernel_native_segids._partial._load_h0: _fwd_mega_kernel_native_segids()._partial()._load_h0().
  _fwd_mega_kernel_native_segids._partial._final: _fwd_mega_kernel_native_segids()._partial()._final().
  _fwd_mega_kernel_native_segids._boundary._save_prev: _fwd_mega_kernel_native_segids()._boundary()._save_prev().
  _fwd_mega_kernel_native_segids._boundary._load_h0: _fwd_mega_kernel_native_segids()._boundary()._load_h0().
  _fwd_mega_kernel_native_segids._boundary._final: _fwd_mega_kernel_native_segids()._boundary()._final().
  CHUNK_KIND_BOUNDARY: CHUNK_KIND_BOUNDARY.
  CHUNK_KIND_PARTIAL_PAD: CHUNK_KIND_PARTIAL_PAD.
  CHUNK_FLAG_LAST_REAL: CHUNK_FLAG_LAST_REAL.
  _fwd_mega_kernel_native_segids._load_token_segment_ids: _fwd_mega_kernel_native_segids()._load_token_segment_ids().
  _NATIVE_SEGIDS_STATIC_ARGNAMES: _NATIVE_SEGIDS_STATIC_ARGNAMES.
  _chunk_kda_fwd_native_segids_impl._out_chunk_map: _chunk_kda_fwd_native_segids_impl()._out_chunk_map().
  _chunk_kda_fwd_native_segids_impl._beta_map: _chunk_kda_fwd_native_segids_impl()._beta_map().
  _RCP_LN2: _RCP_LN2.
  _chunk_kda_fwd_native_segids_impl._seg_map: _chunk_kda_fwd_native_segids_impl()._seg_map().
  _chunk_kda_fwd_native_segids_impl._h0_map: _chunk_kda_fwd_native_segids_impl()._h0_map().
  _chunk_kda_fwd_native_segids_impl._ht_map: _chunk_kda_fwd_native_segids_impl()._ht_map().
  _chunk_kda_fwd_native_segids_impl._alog_map: _chunk_kda_fwd_native_segids_impl()._alog_map().
  _chunk_kda_fwd_native_segids_impl._dtbias_map: _chunk_kda_fwd_native_segids_impl()._dtbias_map().
  _chunk_kda_fwd_native_segids_impl._o_map: _chunk_kda_fwd_native_segids_impl()._o_map().
  _fwd_mega_kernel_native_segids._full._init: _fwd_mega_kernel_native_segids()._full()._init().
  _fwd_mega_kernel_native_segids._partial._init: _fwd_mega_kernel_native_segids()._partial()._init().
  _fwd_mega_kernel_native_segids._boundary._init: _fwd_mega_kernel_native_segids()._boundary()._init().
---
# Module: [`src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py)

## Functions
- <a id="_fwd_mega_kernel_native_segids._all_pad"></a>`_all_pad()` — [`L216`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L216)
- <a id="_chunk_kda_fwd_native_segids_impl._alog_map"></a>`_alog_map(h, b, c, *refs)` — [`L1538`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1538)
- <a id="_chunk_kda_fwd_native_segids_impl._beta_map"></a>`_beta_map(h, b, c, *refs)` — [`L1497`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1497)
- <a id="_fwd_mega_kernel_native_segids._boundary"></a>`_boundary()` — [`L816`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L816) — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)
- <a id="_build_chunk_metadata"></a>`_build_chunk_metadata(segment_ids, chunk_size)` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L52) — Build per-chunk metadata from segment IDs with zero denoting padding. — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)
- <a id="_chunk_kda_fwd_native_segids_impl"></a>`_chunk_kda_fwd_native_segids_impl(q: jax.Array, k: jax.Array, v: jax.Array, g: jax.Array, beta: jax.Array, segment_ids: jax.Array, initial_state=None, output_final_state=False, scale=1, chunk_size=64, store_h=False, store_v_new=False, disable_recompute=False, only_fwd=False, safe_gate=True, use_qk_l2norm_in_kernel=False, use_gate_in_kernel=False, A_log=None, dt_bias=None, lower_bound=None, mini_batch=None, N_max=None, residual_chunk_layout=False, batch_first=False)` — [`L1264`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1264) — Native segment_ids mega kernel wrapper. No _align_seqs. — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)
- <a id="_fwd_mega_kernel_native_segids._dma_state_to_ht"></a>`_dma_state_to_ht(src_ref, segment_id)` — [`L195`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L195) — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)
- <a id="_chunk_kda_fwd_native_segids_impl._dtbias_map"></a>`_dtbias_map(h, b, c, *refs)` — [`L1541`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1541)
- <a id="_fwd_mega_kernel_native_segids._full._final"></a>`_final()` — [`L526`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L526)
- <a id="_fwd_mega_kernel_native_segids._partial._final"></a>`_final()` — [`L806`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L806)
- <a id="_fwd_mega_kernel_native_segids._boundary._final"></a>`_final()` — [`L1226`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1226)
- <a id="_fwd_mega_kernel_native_segids._full"></a>`_full()` — [`L235`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L235)
- <a id="_fwd_mega_kernel_native_segids"></a>`_fwd_mega_kernel_native_segids(chunk_kind_meta_ref, seg_first_meta_ref, seg_last_meta_ref, seg_ids_ref, q_ref, k_ref, v_ref, g_ref, beta_ref, h0_ref, A_scale_ref, dt_bias_ref, o_ref, ht_ref, Aqk_ref, Akk_ref, g_cumsum_out_ref, chunk_h_out_ref, scratch_ref, prev_seg_ref, final_state_dma_ref, state_dma_sem, *, NT, BT, N_max, scale, cumsum_scale, MB, K_PAD, V_PAD, OUTPUT_PRECISION, safe_gate, NORMALIZE_QK, use_gate_in_kernel, lower_bound, USE_NEUMANN, QK_BC, INV_BC, SKIP_STAGE4_MASK, PACK_HEAD_INV, CLIP_BETA_IN_KERNEL, PACKED_METADATA, HAS_H0, STORE_RESIDUALS, STORE_H, STORE_FINAL_STATE, BATCH_FIRST, MANUAL_H0_DMA, MANUAL_HT_DMA, OVERLAP_H0_DMA, OVERLAP_HT_DMA, RESIDUAL_CHUNK_LAYOUT)` — [`L108`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L108) — Native segment_ids mega kernel body. — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)
- <a id="_fwd_mega_kernel_native_segids_packed"></a>`_fwd_mega_kernel_native_segids_packed(packed_metadata_ref, *args, **kwargs)` — [`L1235`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1235) — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)
- <a id="_get_native_residual_layout_jit"></a>`_get_native_residual_layout_jit(q)` — [`L1813`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1813) — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)
- <a id="_chunk_kda_fwd_native_segids_impl._h0_map"></a>`_h0_map(h, b, c, *refs)` — [`L1488`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1488)
- <a id="_chunk_kda_fwd_native_segids_impl._ht_map"></a>`_ht_map(h, b, c, *refs)` — [`L1500`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1500)
- <a id="_chunk_kda_fwd_native_segids_impl._in_map"></a>`_in_map(h, b, c, *refs)` — [`L1485`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1485) — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)
- <a id="_fwd_mega_kernel_native_segids._full._init"></a>`_init()` — [`L251`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L251)
- <a id="_fwd_mega_kernel_native_segids._partial._init"></a>`_init()` — [`L553`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L553)
- <a id="_fwd_mega_kernel_native_segids._boundary._init"></a>`_init()` — [`L833`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L833)
- <a id="_fwd_mega_kernel_native_segids._full._load_h0"></a>`_load_h0()` — [`L257`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L257)
- <a id="_fwd_mega_kernel_native_segids._partial._load_h0"></a>`_load_h0()` — [`L559`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L559)
- <a id="_fwd_mega_kernel_native_segids._boundary._load_h0"></a>`_load_h0()` — [`L839`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L839)
- <a id="_fwd_mega_kernel_native_segids._load_token_segment_ids"></a>`_load_token_segment_ids()` — [`L174`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L174)
- <a id="_native_residual_layout_jit_for_sharding"></a>`_native_residual_layout_jit_for_sharding(sharding)` — [`L1784`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1784) — JIT variant whose ABI accepts the Pallas Aqk/Akk physical layout. — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)
- <a id="_chunk_kda_fwd_native_segids_impl._o_map"></a>`_o_map(h, b, c, *refs)` — [`L1548`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1548)
- <a id="_chunk_kda_fwd_native_segids_impl._out_chunk_map"></a>`_out_chunk_map(h, b, c, *refs)` — [`L1494`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1494)
- <a id="_chunk_kda_fwd_native_segids_impl._out_map"></a>`_out_map(h, b, c, *refs)` — [`L1491`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1491) — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)
- <a id="_chunk_kda_fwd_native_segids_impl._pad"></a>`_pad(x, t)` — [`L1341`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1341) — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)
- <a id="_fwd_mega_kernel_native_segids._partial"></a>`_partial()` — [`L536`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L536) — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)
- <a id="_fwd_mega_kernel_native_segids._read_h0"></a>`_read_h0(segment_id)` — [`L211`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L211) — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)
- <a id="_fwd_mega_kernel_native_segids._full._save_prev"></a>`_save_prev()` — [`L242`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L242)
- <a id="_fwd_mega_kernel_native_segids._partial._save_prev"></a>`_save_prev()` — [`L544`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L544)
- <a id="_fwd_mega_kernel_native_segids._boundary._save_prev"></a>`_save_prev()` — [`L824`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L824)
- <a id="_chunk_kda_fwd_native_segids_impl._seg_map"></a>`_seg_map(h, b, c, *refs)` — [`L1478`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1478)
- <a id="align_up"></a>`align_up(x, align: int)` — [`L48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L48) — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)

## Module values
- <a id="CHUNK_FLAG_LAST_REAL"></a>`CHUNK_FLAG_LAST_REAL` — [`L45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L45)
- <a id="CHUNK_KIND_ALL_PAD"></a>`CHUNK_KIND_ALL_PAD` — [`L41`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L41) — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)
- <a id="CHUNK_KIND_BOUNDARY"></a>`CHUNK_KIND_BOUNDARY` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L43)
- <a id="CHUNK_KIND_FULL_IN_SEGMENT"></a>`CHUNK_KIND_FULL_IN_SEGMENT` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L42) — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)
- <a id="CHUNK_KIND_PARTIAL_PAD"></a>`CHUNK_KIND_PARTIAL_PAD` — [`L44`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L44)
- <a id="_NATIVE_SEGIDS_STATIC_ARGNAMES"></a>`_NATIVE_SEGIDS_STATIC_ARGNAMES` — [`L1245`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1245)
- <a id="_RCP_LN2"></a>`_RCP_LN2` — [`L39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L39)
- <a id="_chunk_kda_fwd_native_segids"></a>`_chunk_kda_fwd_native_segids` — [`L1777`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/mega_kda/kernel.py#L1777) — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)

