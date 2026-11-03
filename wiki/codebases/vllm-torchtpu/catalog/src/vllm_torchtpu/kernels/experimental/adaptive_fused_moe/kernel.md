---
title: 'Module: src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.adaptive_fused_moe.kernel`/
symbols:
  _build_fused_ep_moe_kernel: _build_fused_ep_moe_kernel().
  _build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body.compute_tile: _build_fused_ep_moe_kernel().kernel().expert_tiles().tile_body().compute_tile().
  _build_fused_ep_moe_kernel.make_call: _build_fused_ep_moe_kernel().make_call().
  _build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body: _build_fused_ep_moe_kernel().kernel().expert_tiles().tile_body().
  _build_fused_ep_moe_kernel.kernel: _build_fused_ep_moe_kernel().kernel().
  _build_fused_ep_moe_kernel.kernel.expert_tiles: _build_fused_ep_moe_kernel().kernel().expert_tiles().
  _build_fused_ep_moe_kernel.kernel.drain_transport: _build_fused_ep_moe_kernel().kernel().drain_transport().
  _intermediate_rows: _intermediate_rows().
  _build_combine_kernel: _build_combine_kernel().
  N_PREFETCH: N_PREFETCH.
  combine_step_tokens: combine_step_tokens().
  _build_fused_ep_moe_kernel.kernel.prime_expert: _build_fused_ep_moe_kernel().kernel().prime_expert().
  _rows_wait: _rows_wait().
  _build_fused_ep_moe_kernel.kernel.prefetch_w1: _build_fused_ep_moe_kernel().kernel().prefetch_w1().
  build_fused_ep_moe_kernel: build_fused_ep_moe_kernel().
  COMBINE_PARITIES: COMBINE_PARITIES.
  _build_fused_ep_moe_kernel.kernel.prologue: _build_fused_ep_moe_kernel().kernel().prologue().
  _build_fused_ep_moe_kernel.kernel.push_expert: _build_fused_ep_moe_kernel().kernel().push_expert().
  _build_combine_kernel.kernel: _build_combine_kernel().kernel().
  _build_combine_kernel.kernel.one_step: _build_combine_kernel().kernel().one_step().
  build_combine_kernel: build_combine_kernel().
  expert_ffn_blockscale: expert_ffn_blockscale().
  expert_ffn_int8: expert_ffn_int8().
  _build_fused_ep_moe_kernel.kernel._fp4_block_readers: _build_fused_ep_moe_kernel().kernel()._fp4_block_readers().
  _build_fused_ep_moe_kernel.kernel.visit_step: _build_fused_ep_moe_kernel().kernel().visit_step().
  _build_fused_ep_moe_kernel.fn: _build_fused_ep_moe_kernel().fn().
  _build_combine_kernel.kernel.one_step.one_chunk: _build_combine_kernel().kernel().one_step().one_chunk().
  rowquant_fp8: rowquant_fp8().
  _build_fused_ep_moe_kernel.kernel.count: _build_fused_ep_moe_kernel().kernel().count().
  _build_fused_ep_moe_kernel.kernel.wait_commits: _build_fused_ep_moe_kernel().kernel().wait_commits().
  DN: DN.
  _build_fused_ep_moe_kernel.kernel.lhs_issue_tile: _build_fused_ep_moe_kernel().kernel().lhs_issue_tile().
  _build_fused_ep_moe_kernel.kernel.gather_dma_coords: _build_fused_ep_moe_kernel().kernel().gather_dma_coords().
  _build_fused_ep_moe_kernel.kernel.issue_gather_window: _build_fused_ep_moe_kernel().kernel().issue_gather_window().
  _apply_act: _apply_act().
  tile_height_rungs: tile_height_rungs().
  wire_row_and_scale: wire_row_and_scale().
  expert_ffn_fp8: expert_ffn_fp8().
  expert_ffn_bf16: expert_ffn_bf16().
  _and_nonempty: _and_nonempty().
  _build_fused_ep_moe_kernel.kernel._fp4_block_readers.w1_block: _build_fused_ep_moe_kernel().kernel()._fp4_block_readers().w1_block().
  _build_fused_ep_moe_kernel.kernel._fp4_block_readers.w2_block: _build_fused_ep_moe_kernel().kernel()._fp4_block_readers().w2_block().
  _build_fused_ep_moe_kernel.kernel._int8_chunk_readers: _build_fused_ep_moe_kernel().kernel()._int8_chunk_readers().
  _build_fused_ep_moe_kernel.kernel._int8_chunk_readers.w1_chunk: _build_fused_ep_moe_kernel().kernel()._int8_chunk_readers().w1_chunk().
  _build_fused_ep_moe_kernel.kernel._int8_chunk_readers.w2_chunk: _build_fused_ep_moe_kernel().kernel()._int8_chunk_readers().w2_chunk().
  _build_fused_ep_moe_kernel.kernel.expert_tiles.commit_tile: _build_fused_ep_moe_kernel().kernel().expert_tiles().commit_tile().
  _build_fused_ep_moe_kernel.kernel.expert_tiles.ship_tile: _build_fused_ep_moe_kernel().kernel().expert_tiles().ship_tile().
  _build_fused_ep_moe_kernel.kernel.drain_shipped: _build_fused_ep_moe_kernel().kernel().drain_shipped().
  _build_combine_kernel.kernel.step_pair: _build_combine_kernel().kernel().step_pair().
  _build_fused_ep_moe_kernel.kernel.w2_copy: _build_fused_ep_moe_kernel().kernel().w2_copy().
  _build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body.compute_tile.wait_down_weights: _build_fused_ep_moe_kernel().kernel().expert_tiles().tile_body().compute_tile().wait_down_weights().
  WEIGHT_DMA_PRIORITY: WEIGHT_DMA_PRIORITY.
  COMBINE_LEAD: COMBINE_LEAD.
  _row_scale: _row_scale().
  _quant_apply: _quant_apply().
  _chunked_dot: _chunked_dot().
  _build_fused_ep_moe_kernel.kernel.w1_copy: _build_fused_ep_moe_kernel().kernel().w1_copy().
  _build_fused_ep_moe_kernel.kernel.w1s_copy: _build_fused_ep_moe_kernel().kernel().w1s_copy().
  _build_fused_ep_moe_kernel.kernel.w2s_copy: _build_fused_ep_moe_kernel().kernel().w2s_copy().
  _build_fused_ep_moe_kernel.kernel.wait_gather_window: _build_fused_ep_moe_kernel().kernel().wait_gather_window().
  _build_fused_ep_moe_kernel.kernel.lhs_issue_tile.issue_from: _build_fused_ep_moe_kernel().kernel().lhs_issue_tile().issue_from().
  _build_fused_ep_moe_kernel.kernel._run_tiles: _build_fused_ep_moe_kernel().kernel()._run_tiles().
  _build_fused_ep_moe_kernel.kernel.wait_shipped: _build_fused_ep_moe_kernel().kernel().wait_shipped().
  _build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body.compute_tile.read_down_weights: _build_fused_ep_moe_kernel().kernel().expert_tiles().tile_body().compute_tile().read_down_weights().
  ACT_FNS: ACT_FNS.
  _slot_copy: _slot_copy().
  _build_fused_ep_moe_kernel.kernel.sync: _build_fused_ep_moe_kernel().kernel().sync().
  _BUILD_CACHE: _BUILD_CACHE.
  logger: logger.
  _tile_row_scales: _tile_row_scales().
  _build_fused_ep_moe_kernel.kernel.lhs_issue_tile.issue_from.issue_block: _build_fused_ep_moe_kernel().kernel().lhs_issue_tile().issue_from().issue_block().
  _build_fused_ep_moe_kernel.kernel.drain_commits: _build_fused_ep_moe_kernel().kernel().drain_commits().
  _build_fused_ep_moe_kernel.kernel.push_expert._.push_run: _build_fused_ep_moe_kernel().kernel().push_expert()._().push_run().
  HEIGHT_RUNGS: HEIGHT_RUNGS.
  COMBINE_GROUP: COMBINE_GROUP.
  COMBINE_CHUNK: COMBINE_CHUNK.
  _COMBINE_CACHE: _COMBINE_CACHE.
  QCHUNK: QCHUNK.
  N_TRANSPORT_TABLES: N_TRANSPORT_TABLES.
  N_PUSH_TABLES: N_PUSH_TABLES.
  N_SLAB_TABLES: N_SLAB_TABLES.
  _intermediate_rows.half: _intermediate_rows().half().
  _all_pairs_barrier: _all_pairs_barrier().
  _build_fused_ep_moe_kernel.kernel._mirror_base: _build_fused_ep_moe_kernel().kernel()._mirror_base().
  _build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body.compute_tile.store_parity: _build_fused_ep_moe_kernel().kernel().expert_tiles().tile_body().compute_tile().store_parity().
  _build_combine_kernel.kernel.start_row: _build_combine_kernel().kernel().start_row().
  AXIS: AXIS.
  COLLECTIVE_ID: COLLECTIVE_ID.
  _REF_BITCAST_JAX_VERSION: _REF_BITCAST_JAX_VERSION.
  N_VISIT_TABLES: N_VISIT_TABLES.
  N_COUNT_TABLES: N_COUNT_TABLES.
  N_RANK_TABLES: N_RANK_TABLES.
  N_STAGING_INPUTS: N_STAGING_INPUTS.
  N_WEIGHT_SLABS: N_WEIGHT_SLABS.
  N_SCALE_TABLES: N_SCALE_TABLES.
  _absmax_rows: _absmax_rows().
  _build_fused_ep_moe_kernel.kernel.lhs_ready_tile: _build_fused_ep_moe_kernel().kernel().lhs_ready_tile().
  _BUILD_CACHE_LOCK: _BUILD_CACHE_LOCK.
  COMBINE_TOKENS: COMBINE_TOKENS.
  COMBINE_MIN_TOKENS: COMBINE_MIN_TOKENS.
  _build_combine_kernel.kernel.reduce_token: _build_combine_kernel().kernel().reduce_token().
  _build_combine_kernel.fn: _build_combine_kernel().fn().
  _COMBINE_CACHE_LOCK: _COMBINE_CACHE_LOCK.
---
# Module: [`src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py)

## Functions
- <a id="_absmax_rows"></a>`_absmax_rows(x)` — [`L190`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L190)
- <a id="_all_pairs_barrier"></a>`_all_pairs_barrier(ep)` — [`L451`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L451) — Barrier over every shard: transport peers are not only neighbours.
- <a id="_and_nonempty"></a>`_and_nonempty(pred, rows)` — [`L485`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L485) — `pred` and a nonzero length: a zero-length DMA must never issue.
- <a id="_apply_act"></a>`_apply_act(gate, up, act_fn)` — [`L120`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L120) — The FFN activation, on the POST-SCALE gate and up halves.
- <a id="_build_combine_kernel"></a>`_build_combine_kernel(*, t_local, topk, hidden, lane_blocks, wire_dtype, out_dtype)` — [`L2021`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L2021) — out[i] = sum_k coef[i, k] * arrivals[pos[i * topk + k]]. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="_build_fused_ep_moe_kernel"></a>`_build_fused_ep_moe_kernel(*, g_local, capacity, hidden, inter, ep, weight_format=host.WeightFormat.FP8, rhs_qb=QB4, ragged_rows_alloc=None, act_fn="silu", has_w1_bias=False, has_w2_bias=False)` — [`L514`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L514) — Build the pallas_call and the function that invokes it. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="_chunked_dot"></a>`_chunked_dot(lhs, rhs_chunk, n_chunks, kb)` — [`L296`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L296) — Contract lhs against a weight handed over one contraction chunk at a
- <a id="_build_fused_ep_moe_kernel.kernel._fp4_block_readers"></a>`_fp4_block_readers(w1_slot, w2_slot, wait_down)` — [`L859`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L859) — FP4 block readers for the independent W1 and W2 slots.
- <a id="_build_fused_ep_moe_kernel.kernel._int8_chunk_readers"></a>`_int8_chunk_readers(w1_slot, w2_slot, wait_down)` — [`L884`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L884) — Integer chunk readers for the independent W1 and W2 slots.
- <a id="_intermediate_rows"></a>`_intermediate_rows(acc1, act_scale, inter, *, w1s, act_fn, w1b, requantize=True)` — [`L242`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L242) — acc1's gate and up halves through the activation, as the second
- <a id="_build_fused_ep_moe_kernel.kernel._mirror_base"></a>`_mirror_base(e)` — [`L1010`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1010) — Sublane expert e's tiles start at in the contribution mirror.
- <a id="_quant_apply"></a>`_quant_apply(x, sinv_native, usable)` — [`L194`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L194) — Quantize a row, or zero it whole where its scale is unusable.
- <a id="_row_scale"></a>`_row_scale(amax)` — [`L163`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L163) — The row scale and its inverse, with the rows that have no usable one.
- <a id="_rows_wait"></a>`_rows_wait(sem, ref, rows)` — [`L480`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L480) — Block until `rows` rows' worth of DMAs on `sem` have landed.
- <a id="_build_fused_ep_moe_kernel.kernel._run_tiles"></a>`_run_tiles(e, d, region_blocks)` — [`L1021`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1021) — A run's mirror sublanes: (source, destination, count).
- <a id="_slot_copy"></a>`_slot_copy(src, vm, sems, slot)` — [`L475`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L475) — A copy of `src` into buffer slot `slot`, on that slot's semaphore.
- <a id="_tile_row_scales"></a>`_tile_row_scales(window, row_base, tile_m)` — [`L490`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L490) — One tile's activation row scales as the [tile_m, 1] column the FFN
- <a id="build_combine_kernel"></a>`build_combine_kernel(**kwargs)` — [`L2167`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L2167) — Memoizing front door; see build_fused_ep_moe_kernel for why.
- <a id="build_fused_ep_moe_kernel"></a>`build_fused_ep_moe_kernel(**kwargs)` — [`L1926`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1926) — Memoizing front door for _build_fused_ep_moe_kernel.
- <a id="combine_step_tokens"></a>`combine_step_tokens(t_local)` — [`L1997`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1997) — Tokens a combine step stages, or 0 where this path does not apply. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="_build_fused_ep_moe_kernel.kernel.expert_tiles.commit_tile"></a>`commit_tile(parity, t, tile_block_base, live_blocks)` — [`L1144`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1144) — Commit the tile's intersection with each (expert, dest) run.
- <a id="_build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body.compute_tile"></a>`compute_tile(height)` — [`L1359`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1359) — Run the FFN on the tile's leading `height` rows. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="_build_fused_ep_moe_kernel.kernel.count"></a>`count(row)` — [`L704`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L704) — Close one count's reduction on the scalar core.
- <a id="_build_fused_ep_moe_kernel.kernel.drain_commits"></a>`drain_commits(carried)` — [`L1550`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1550) — Drain both parities' pending commits, then zero the counts.
- <a id="_build_fused_ep_moe_kernel.kernel.drain_shipped"></a>`drain_shipped(carried)` — [`L1565`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1565) — Wait out whatever the last tile on each parity put on the wire.
- <a id="_build_fused_ep_moe_kernel.kernel.drain_transport"></a>`drain_transport()` — [`L1656`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1656) — Consume the pushes and the commits the per-tile waits left. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="expert_ffn_bf16"></a>`expert_ffn_bf16(act, w1, w2_read, act_fn="silu", w1b=None)` — [`L390`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L390) — One expert's FFN on unquantized sixteen-bit weights.
- <a id="expert_ffn_blockscale"></a>`expert_ffn_blockscale(act_q, act_scale, w1_block, w2_block, w1s_blocks, w2s_blocks, *, qb=QB4, act_fn="silu", w1b=None)` — [`L335`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L335) — One expert's FFN on block-scaled weights: the same body as
- <a id="expert_ffn_fp8"></a>`expert_ffn_fp8(act_q, act_scale, w1, w2_read, w1s, act_fn="silu", w1b=None)` — [`L317`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L317) — One expert's FFN on eight-bit weights: the gate/up matmul, the
- <a id="expert_ffn_int8"></a>`expert_ffn_int8(act, w1_chunk, w2_chunk, w1s, *, n_chunks1, n_chunks2, kb=host.WIDEN_KCHUNK, act_fn="silu", w1b=None)` — [`L411`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L411) — One expert's FFN on eight-bit INTEGER weights with per-channel scales.
- <a id="_build_fused_ep_moe_kernel.kernel.expert_tiles"></a>`expert_tiles(e, visit_i, carry)` — [`L1095`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1095) — One expert step: a fori_loop over its [tile_m, H] tiles. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="_build_fused_ep_moe_kernel.fn"></a>`fn(tables, token_gather, expert_rows, expert_base, act_q_gathered, act_scales, w1, w2, w1s, w2s, w1b=None, w2b=None, *, recv_rows, visit, counts, rank)` — [`L1827`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1827) — The served ragged transport form; returns arrivals and scales. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="_build_combine_kernel.fn"></a>`fn(arrivals, coef, pos)` — [`L2147`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L2147)
- <a id="_build_fused_ep_moe_kernel.kernel.gather_dma_coords"></a>`gather_dma_coords(logical_base)` — [`L910`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L910) — Aligned HBM base and in-window offset for a slab row.
- <a id="_intermediate_rows.half"></a>`half(lo, hi)` — [`L260`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L260) — One post-scale half of the accumulator, columns [lo, hi).
- <a id="_build_fused_ep_moe_kernel.kernel.lhs_issue_tile.issue_from.issue_block"></a>`issue_block(i, _)` — [`L963`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L963) — Fetch eight token rows of block i by their numbers.
- <a id="_build_fused_ep_moe_kernel.kernel.lhs_issue_tile.issue_from"></a>`issue_from(gather_smem)` — [`L962`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L962)
- <a id="_build_fused_ep_moe_kernel.kernel.issue_gather_window"></a>`issue_gather_window(logical_base, slot)` — [`L919`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L919) — Start one fixed token-index window in SMEM slot ``slot``.
- <a id="_build_fused_ep_moe_kernel.kernel"></a>`kernel(*refs)` — [`L673`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L673) — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="_build_combine_kernel.kernel"></a>`kernel(pos_sm, coef_sm, arr_hbm, out_hbm, rows_vm, tile_vm, out_vm, row_sems, out_sems)` — [`L2043`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L2043)
- <a id="_build_fused_ep_moe_kernel.kernel.lhs_issue_tile"></a>`lhs_issue_tile(row_base, live_blocks, slot, gather_slot, gather_offset)` — [`L959`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L959) — Issue one tile's activations using a resident index window.
- <a id="_build_fused_ep_moe_kernel.kernel.lhs_ready_tile"></a>`lhs_ready_tile(live_rows, slot)` — [`L995`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L995) — Wait the token rows and the scale window of one tile.
- <a id="_build_fused_ep_moe_kernel.make_call"></a>`make_call(recv_rows)` — [`L1764`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1764) — The pallas_call for this build, at this arrival-buffer height. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="_build_combine_kernel.kernel.one_step.one_chunk"></a>`one_chunk(chunk, carry)` — [`L2088`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L2088)
- <a id="_build_combine_kernel.kernel.one_step"></a>`one_step(step, parity)` — [`L2069`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L2069)
- <a id="_build_fused_ep_moe_kernel.kernel.prefetch_w1"></a>`prefetch_w1(expert, slot)` — [`L829`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L829)
- <a id="_build_fused_ep_moe_kernel.kernel.prime_expert"></a>`prime_expert(e, lhs_slot, wslot, window_started)` — [`L1063`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1063) — Prime expert ``e``'s metadata and first activation tile.
- <a id="_build_fused_ep_moe_kernel.kernel.prologue"></a>`prologue()` — [`L835`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L835) — Land the resident tables and start the first weight refills.
- <a id="_build_fused_ep_moe_kernel.kernel.push_expert"></a>`push_expert(e)` — [`L1579`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1579) — Push expert e's remote regions and hop its own-dest region.
- <a id="_build_fused_ep_moe_kernel.kernel.push_expert._.push_run"></a>`push_run()` — [`L1595`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1595) — The rows themselves, at their true length.
- <a id="_build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body.compute_tile.read_down_weights"></a>`read_down_weights()` — [`L1386`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1386)
- <a id="_build_combine_kernel.kernel.reduce_token"></a>`reduce_token(base, parity, i)` — [`L2058`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L2058) — One token's weighted sum, in the arrival rows' own layout.
- <a id="rowquant_fp8"></a>`rowquant_fp8(x)` — [`L183`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L183) — Per-row dynamic fp8 quant, reducing and applying in bf16. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="_build_fused_ep_moe_kernel.kernel.expert_tiles.ship_tile"></a>`ship_tile(parity, t, tile_block_base, live_blocks)` — [`L1189`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1189) — Ship the tile straight out of `out_vm`, no slab in between.
- <a id="_build_combine_kernel.kernel.start_row"></a>`start_row(base, parity, i, k)` — [`L2046`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L2046)
- <a id="_build_combine_kernel.kernel.step_pair"></a>`step_pair(pair, carry)` — [`L2105`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L2105)
- <a id="_build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body.compute_tile.store_parity"></a>`store_parity(static_parity)` — [`L1475`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1475) — Stage the tile's rows and scales in one out_vm
- <a id="_build_fused_ep_moe_kernel.kernel.sync"></a>`sync(src, dst)` — [`L807`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L807) — Copy `src` into `dst` and wait for it before returning.
- <a id="_build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body"></a>`tile_body(t, carried)` — [`L1286`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1286) — Compute tile t, stage it for the wire and ship it. — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="tile_height_rungs"></a>`tile_height_rungs(tile_m, rows_alloc, g_local, ep)` — [`L136`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L136) — The ascending static tile heights a build emits, ending at tile_m.
- <a id="_build_fused_ep_moe_kernel.kernel.visit_step"></a>`visit_step(visit_i, carry)` — [`L1642`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1642) — One step of the visit list: compute, then drain and push.
- <a id="_build_fused_ep_moe_kernel.kernel._fp4_block_readers.w1_block"></a>`w1_block(b)` — [`L870`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L870)
- <a id="_build_fused_ep_moe_kernel.kernel._int8_chunk_readers.w1_chunk"></a>`w1_chunk(b)` — [`L893`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L893)
- <a id="_build_fused_ep_moe_kernel.kernel.w1_copy"></a>`w1_copy(expert, slot)` — [`L813`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L813) — The gate/up weight slab of `expert`, into weight slot `slot`.
- <a id="_build_fused_ep_moe_kernel.kernel.w1s_copy"></a>`w1s_copy(expert, slot)` — [`L821`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L821)
- <a id="_build_fused_ep_moe_kernel.kernel._fp4_block_readers.w2_block"></a>`w2_block(b)` — [`L875`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L875)
- <a id="_build_fused_ep_moe_kernel.kernel._int8_chunk_readers.w2_chunk"></a>`w2_chunk(b)` — [`L898`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L898)
- <a id="_build_fused_ep_moe_kernel.kernel.w2_copy"></a>`w2_copy(expert, slot)` — [`L817`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L817) — The down weight slab of `expert`, into weight slot `slot`.
- <a id="_build_fused_ep_moe_kernel.kernel.w2s_copy"></a>`w2s_copy(expert, slot)` — [`L825`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L825)
- <a id="_build_fused_ep_moe_kernel.kernel.wait_commits"></a>`wait_commits(parity, live_blocks)` — [`L1037`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1037) — Wait one tile's commits on `parity`: data rows, then scales.
- <a id="_build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body.compute_tile.wait_down_weights"></a>`wait_down_weights()` — [`L1379`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1379)
- <a id="_build_fused_ep_moe_kernel.kernel.wait_gather_window"></a>`wait_gather_window(logical_base, slot)` — [`L939`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L939) — Wait for the fixed token-index window in ``slot``.
- <a id="_build_fused_ep_moe_kernel.kernel.wait_shipped"></a>`wait_shipped(parity, rows, subs)` — [`L1044`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1044) — Wait until the wire has read `parity`'s staging slot.
- <a id="wire_row_and_scale"></a>`wire_row_and_scale(acc2, mid_scale, *, w2s=None, w2b=None, wire_dtype=FP8, tile_m=None)` — [`L199`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L199) — One tile's rows as they go on the wire, and the scale that rides with

## Module values
- <a id="ACT_FNS"></a>`ACT_FNS` — [`L117`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L117)
- <a id="AXIS"></a>`AXIS` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L52)
- <a id="COLLECTIVE_ID"></a>`COLLECTIVE_ID` — [`L68`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L68)
- <a id="COMBINE_CHUNK"></a>`COMBINE_CHUNK` — [`L1984`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1984)
- <a id="COMBINE_GROUP"></a>`COMBINE_GROUP` — [`L1978`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1978)
- <a id="COMBINE_LEAD"></a>`COMBINE_LEAD` — [`L1994`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1994)
- <a id="COMBINE_MIN_TOKENS"></a>`COMBINE_MIN_TOKENS` — [`L1988`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1988)
- <a id="COMBINE_PARITIES"></a>`COMBINE_PARITIES` — [`L1989`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1989)
- <a id="COMBINE_TOKENS"></a>`COMBINE_TOKENS` — [`L1974`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1974)
- <a id="DN"></a>`DN` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L50)
- <a id="HEIGHT_RUNGS"></a>`HEIGHT_RUNGS` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L62)
- <a id="N_COUNT_TABLES"></a>`N_COUNT_TABLES` — [`L86`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L86)
- <a id="N_PREFETCH"></a>`N_PREFETCH` — [`L95`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L95) — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="N_PUSH_TABLES"></a>`N_PUSH_TABLES` — [`L83`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L83)
- <a id="N_RANK_TABLES"></a>`N_RANK_TABLES` — [`L94`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L94)
- <a id="N_SCALE_TABLES"></a>`N_SCALE_TABLES` — [`L110`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L110)
- <a id="N_SLAB_TABLES"></a>`N_SLAB_TABLES` — [`L84`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L84)
- <a id="N_STAGING_INPUTS"></a>`N_STAGING_INPUTS` — [`L108`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L108)
- <a id="N_TRANSPORT_TABLES"></a>`N_TRANSPORT_TABLES` — [`L82`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L82)
- <a id="N_VISIT_TABLES"></a>`N_VISIT_TABLES` — [`L85`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L85)
- <a id="N_WEIGHT_SLABS"></a>`N_WEIGHT_SLABS` — [`L109`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L109)
- <a id="QCHUNK"></a>`QCHUNK` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L55)
- <a id="WEIGHT_DMA_PRIORITY"></a>`WEIGHT_DMA_PRIORITY` — [`L65`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L65)
- <a id="_BUILD_CACHE"></a>`_BUILD_CACHE` — [`L1920`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1920)
- <a id="_BUILD_CACHE_LOCK"></a>`_BUILD_CACHE_LOCK` — [`L1923`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L1923)
- <a id="_COMBINE_CACHE"></a>`_COMBINE_CACHE` — [`L2163`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L2163)
- <a id="_COMBINE_CACHE_LOCK"></a>`_COMBINE_CACHE_LOCK` — [`L2164`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L2164)
- <a id="_REF_BITCAST_JAX_VERSION"></a>`_REF_BITCAST_JAX_VERSION` — [`L72`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L72)
- <a id="logger"></a>`logger` — [`L48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/kernel.py#L48)

