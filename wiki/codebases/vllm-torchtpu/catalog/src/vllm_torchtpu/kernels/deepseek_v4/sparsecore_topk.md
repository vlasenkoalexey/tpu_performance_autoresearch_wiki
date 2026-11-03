---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.sparsecore_topk`/
symbols:
  LANES: LANES.
  _topk_body._run_step: _topk_body()._run_step().
  NUM_BUCKETS: NUM_BUCKETS.
  _topk_body: _topk_body().
  _sc_topk_direct: _sc_topk_direct().
  _topk_body._run_step._.hist0_body: _topk_body()._run_step()._().hist0_body().
  _topk_body.sync_and_reduce_hist: _topk_body().sync_and_reduce_hist().
  sparsecore_topk: sparsecore_topk().
  _topk_body._run_step._.gather_peer: _topk_body()._run_step()._().gather_peer().
  _topk_body.vec_at: _topk_body().vec_at().
  _topk_body.sync_and_reduce_hist._.add_peer: _topk_body().sync_and_reduce_hist()._().add_peer().
  _pick_partition: _pick_partition().
  _topk_body._run_step.emit: _topk_body()._run_step().emit().
  _topk_body.sync_and_reduce_hist._.add_peer.add_chunk: _topk_body().sync_and_reduce_hist()._().add_peer().add_chunk().
  _topk_body._run_step.ref_body: _topk_body()._run_step().ref_body().
  _topk_body._run_step.fill_body: _topk_body()._run_step().fill_body().
  _topk_body._run_step.tie_body: _topk_body()._run_step().tie_body().
  _topk_body._run_step.emit_whole: _topk_body()._run_step().emit_whole().
  _topk_body._run_step.emit_ranked: _topk_body()._run_step().emit_ranked().
  _cdiv_dyn: _cdiv_dyn().
  BITS_NEG_INF: BITS_NEG_INF.
  _topk_body.monotone_key: _topk_body().monotone_key().
  _topk_body.zero_hist: _topk_body().zero_hist().
  _topk_body.scan_glob: _topk_body().scan_glob().
  _topk_body.find_bucket: _topk_body().find_bucket().
  sparsecore_topk_dcp_merge: sparsecore_topk_dcp_merge().
  KEY_NEG_INF: KEY_NEG_INF.
  _align_to: _align_to().
  _topk_body.zero_hist.body: _topk_body().zero_hist().body().
  _topk_body.sync_and_reduce_hist._.init_hist: _topk_body().sync_and_reduce_hist()._().init_hist().
  _topk_body.scan_glob.body: _topk_body().scan_glob().body().
  _topk_body.find_bucket.body: _topk_body().find_bucket().body().
  _topk_body._run_step.count_prior_ties: _topk_body()._run_step().count_prior_ties().
  _topk_body._run_step.copy_out: _topk_body()._run_step().copy_out().
  _topk_body._run_step._.gather_peer._.append_full: _topk_body()._run_step()._().gather_peer()._().append_full().
  _topk_body.pipeline_step_p1_scores: _topk_body().pipeline_step_p1_scores().
  _topk_body.pipeline_step_p1_idx: _topk_body().pipeline_step_p1_idx().
  _topk_body.pipeline_step_coop: _topk_body().pipeline_step_coop().
  SCAN_UNROLL: SCAN_UNROLL.
  _cdiv: _cdiv().
  MAX_SLICE_WORDS: MAX_SLICE_WORDS.
  L0_SHIFT: L0_SHIFT.
  _topk_body.key_window: _topk_body().key_window().
  _topk_body.hist_add: _topk_body().hist_add().
  REFINEMENT_LEVELS: REFINEMENT_LEVELS.
  MONO_MASK: MONO_MASK.
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py)

## Functions
- <a id="_align_to"></a>`_align_to(x, a)` — [`L64`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L64)
- <a id="_cdiv"></a>`_cdiv(a, b)` — [`L60`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L60)
- <a id="_cdiv_dyn"></a>`_cdiv_dyn(x)` — [`L68`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L68)
- <a id="_pick_partition"></a>`_pick_partition(b: int, n: int, k: int)` — [`L777`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L777) — Picks the power-of-two partition factor P (1..16) per row to maximize
- <a id="_topk_body._run_step"></a>`_run_step(scores_vmem, len_slice_vmem, out_vmem: Any = None, keys_vmem: Any = None, local_idxs_vmem: Any = None)` — [`L206`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L206)
- <a id="_sc_topk_direct"></a>`_sc_topk_direct(scores: jax.Array, k: int, row_lengths: jax.Array, *, local_idxs: jax.Array | None = None, p: int = 1, write_empty: bool = True, return_scores: bool = True, scheduling_group_id: int | None = None)` — [`L649`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L649) — Single-stage SparseCore top-k on 32 subcores.
- <a id="_topk_body"></a>`_topk_body(scores_hbm, lengths_hbm, out_hbm, keys_hbm, glob_vmem, rowbuf_vmem, keybuf_vmem, peer_hist_vmem, peer_idx_vmem, peer_key_vmem, shared_hist_vmem, shared_counts_vmem, shared_idx_vmem, shared_key_vmem, *, b: int, n: int, k: int, p: int = 1, slice_len: int, num_waves: int, write_empty: bool, return_scores: bool, local_idxs_hbm: Any = None)` — [`L72`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L72)
- <a id="_topk_body.sync_and_reduce_hist._.add_peer.add_chunk"></a>`add_chunk(i)` — [`L177`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L177)
- <a id="_topk_body.sync_and_reduce_hist._.add_peer"></a>`add_peer(t)` — [`L176`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L176)
- <a id="_topk_body._run_step._.gather_peer._.append_full"></a>`append_full(c)` — [`L511`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L511)
- <a id="_topk_body.zero_hist.body"></a>`body(i)` — [`L134`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L134)
- <a id="_topk_body.scan_glob.body"></a>`body(i, carry)` — [`L188`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L188)
- <a id="_topk_body.find_bucket.body"></a>`body(i, cnt)` — [`L198`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L198)
- <a id="_topk_body._run_step.copy_out"></a>`copy_out(i)` — [`L435`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L435)
- <a id="_topk_body._run_step.count_prior_ties"></a>`count_prior_ties(i, rank)` — [`L364`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L364)
- <a id="_topk_body._run_step.emit"></a>`emit(i, woff, key, sel)` — [`L381`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L381)
- <a id="_topk_body._run_step.emit_ranked"></a>`emit_ranked(i, carry)` — [`L415`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L415)
- <a id="_topk_body._run_step.emit_whole"></a>`emit_whole(i, woff)` — [`L404`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L404)
- <a id="_topk_body._run_step.fill_body"></a>`fill_body(i)` — [`L309`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L309)
- <a id="_topk_body.find_bucket"></a>`find_bucket(bound, thresh)` — [`L197`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L197)
- <a id="_topk_body._run_step._.gather_peer"></a>`gather_peer(t, woff)` — [`L489`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L489)
- <a id="_topk_body._run_step._.hist0_body"></a>`hist0_body(i)` — [`L242`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L242)
- <a id="_topk_body.hist_add"></a>`hist_add(bucket, mask)` — [`L139`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L139) — Accumulates one chunk's bucket counts into the histogram.
- <a id="_topk_body.sync_and_reduce_hist._.init_hist"></a>`init_hist(i)` — [`L169`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L169)
- <a id="_topk_body.key_window"></a>`key_window(prefix, shift)` — [`L127`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L127) — Scalar bounds of the key range ``key >> shift == prefix``.
- <a id="_topk_body.monotone_key"></a>`monotone_key(bits)` — [`L123`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L123)
- <a id="_topk_body.pipeline_step_coop"></a>`pipeline_step_coop(scores_vmem, len_slice_vmem)` — [`L626`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L626)
- <a id="_topk_body.pipeline_step_p1_idx"></a>`pipeline_step_p1_idx(scores_vmem, len_slice_vmem, *rest_vmem)` — [`L601`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L601)
- <a id="_topk_body.pipeline_step_p1_scores"></a>`pipeline_step_p1_scores(scores_vmem, len_slice_vmem, out_vmem, keys_vmem)` — [`L576`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L576)
- <a id="_topk_body._run_step.ref_body"></a>`ref_body(i, lvl_shift=lvl_shift, lvl_mask=lvl_mask, lo_excl=lo_excl, hi_incl=hi_incl)` — [`L272`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L272)
- <a id="_topk_body.scan_glob"></a>`scan_glob(bound)` — [`L187`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L187)
- <a id="sparsecore_topk"></a>`sparsecore_topk(scores: jax.Array, k: int, row_lengths: jax.Array | None = None, *, write_empty_rows: bool = True, scheduling_group_id: int | None = None, return_scores: bool = False)` — [`L808`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L808) — Exact top-k indices per row, unsorted, -1 suffix-padded. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="sparsecore_topk_dcp_merge"></a>`sparsecore_topk_dcp_merge(scores: jax.Array, local_idxs: jax.Array, k: int, *, dcp_rank: jax.Array, dcp_size: int, scheduling_group_id: int | None = None)` — [`L858`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L858) — Fused global top-k threshold selection, owner filter, and prefix compact.
- <a id="_topk_body.sync_and_reduce_hist"></a>`sync_and_reduce_hist(slot: int, active_hist)` — [`L144`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L144) — Syncs per-subcore histograms via VMEM_SHARED, reducing across P slices.
- <a id="_topk_body._run_step.tie_body"></a>`tie_body(t, carry)` — [`L333`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L333)
- <a id="_topk_body.vec_at"></a>`vec_at(ref, idx)` — [`L120`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L120)
- <a id="_topk_body.zero_hist"></a>`zero_hist(bound)` — [`L133`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L133)

## Module values
- <a id="BITS_NEG_INF"></a>`BITS_NEG_INF` — [`L56`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L56)
- <a id="KEY_NEG_INF"></a>`KEY_NEG_INF` — [`L57`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L57)
- <a id="L0_SHIFT"></a>`L0_SHIFT` — [`L53`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L53)
- <a id="LANES"></a>`LANES` — [`L44`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L44)
- <a id="MAX_SLICE_WORDS"></a>`MAX_SLICE_WORDS` — [`L49`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L49)
- <a id="MONO_MASK"></a>`MONO_MASK` — [`L55`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L55)
- <a id="NUM_BUCKETS"></a>`NUM_BUCKETS` — [`L45`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L45)
- <a id="REFINEMENT_LEVELS"></a>`REFINEMENT_LEVELS` — [`L54`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L54)
- <a id="SCAN_UNROLL"></a>`SCAN_UNROLL` — [`L51`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/sparsecore_topk.py#L51)

