---
title: 'Module: src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.fused_moe.v2.kernel`/
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
  _build_fused_ep_moe_kernel.kernel.weight_starts: _build_fused_ep_moe_kernel().kernel().weight_starts().
  N_PREFETCH: N_PREFETCH.
  combine_step_tokens: combine_step_tokens().
  _build_fused_ep_moe_kernel.kernel.prime_expert: _build_fused_ep_moe_kernel().kernel().prime_expert().
  _rows_wait: _rows_wait().
  build_fused_ep_moe_kernel: build_fused_ep_moe_kernel().
  COMBINE_PARITIES: COMBINE_PARITIES.
  _build_fused_ep_moe_kernel.kernel.weight_waits: _build_fused_ep_moe_kernel().kernel().weight_waits().
  _build_fused_ep_moe_kernel.kernel.push_expert: _build_fused_ep_moe_kernel().kernel().push_expert().
  _build_combine_kernel.kernel: _build_combine_kernel().kernel().
  _build_combine_kernel.kernel.one_step: _build_combine_kernel().kernel().one_step().
  build_combine_kernel: build_combine_kernel().
  _apply_act: _apply_act().
  tile_height_rungs: tile_height_rungs().
  expert_ffn_blockscale: expert_ffn_blockscale().
  expert_ffn_int8: expert_ffn_int8().
  _build_fused_ep_moe_kernel.kernel._fp4_block_readers: _build_fused_ep_moe_kernel().kernel()._fp4_block_readers().
  _build_fused_ep_moe_kernel.kernel._fp4_block_readers.w1_block: _build_fused_ep_moe_kernel().kernel()._fp4_block_readers().w1_block().
  _build_fused_ep_moe_kernel.kernel._fp4_block_readers.w2_block: _build_fused_ep_moe_kernel().kernel()._fp4_block_readers().w2_block().
  _build_fused_ep_moe_kernel.kernel.visit_step: _build_fused_ep_moe_kernel().kernel().visit_step().
  _build_fused_ep_moe_kernel.fn: _build_fused_ep_moe_kernel().fn().
  _build_combine_kernel.kernel.one_step.one_chunk: _build_combine_kernel().kernel().one_step().one_chunk().
  WEIGHT_DMA_PRIORITY: WEIGHT_DMA_PRIORITY.
  rowquant_fp8: rowquant_fp8().
  _build_fused_ep_moe_kernel.kernel.count: _build_fused_ep_moe_kernel().kernel().count().
  _build_fused_ep_moe_kernel.kernel.wait_commits: _build_fused_ep_moe_kernel().kernel().wait_commits().
  ACT_FNS: ACT_FNS.
  expert_ffn_blockscale.contract: expert_ffn_blockscale().contract().
  _build_fused_ep_moe_kernel.kernel.lhs_issue_tile: _build_fused_ep_moe_kernel().kernel().lhs_issue_tile().
  _build_fused_ep_moe_kernel.kernel.w1_copy: _build_fused_ep_moe_kernel().kernel().w1_copy().
  _build_fused_ep_moe_kernel.kernel.w2_copy: _build_fused_ep_moe_kernel().kernel().w2_copy().
  _build_fused_ep_moe_kernel.kernel.gather_dma_coords: _build_fused_ep_moe_kernel().kernel().gather_dma_coords().
  _build_fused_ep_moe_kernel.kernel.issue_gather_window: _build_fused_ep_moe_kernel().kernel().issue_gather_window().
  DN: DN.
  wire_row_and_scale: wire_row_and_scale().
  expert_ffn_fp8: expert_ffn_fp8().
  expert_ffn_bf16: expert_ffn_bf16().
  _and_nonempty: _and_nonempty().
  _build_fused_ep_moe_kernel.kernel.prologue: _build_fused_ep_moe_kernel().kernel().prologue().
  _build_fused_ep_moe_kernel.kernel._start_next_gate_up.start: _build_fused_ep_moe_kernel().kernel()._start_next_gate_up().start().
  _build_fused_ep_moe_kernel.kernel._int8_chunk_readers: _build_fused_ep_moe_kernel().kernel()._int8_chunk_readers().
  _build_fused_ep_moe_kernel.kernel._int8_chunk_readers.w1_chunk: _build_fused_ep_moe_kernel().kernel()._int8_chunk_readers().w1_chunk().
  _build_fused_ep_moe_kernel.kernel._int8_chunk_readers.w2_chunk: _build_fused_ep_moe_kernel().kernel()._int8_chunk_readers().w2_chunk().
  _build_fused_ep_moe_kernel.kernel.expert_tiles.commit_tile: _build_fused_ep_moe_kernel().kernel().expert_tiles().commit_tile().
  _build_fused_ep_moe_kernel.kernel.expert_tiles.ship_tile: _build_fused_ep_moe_kernel().kernel().expert_tiles().ship_tile().
  _build_fused_ep_moe_kernel.kernel.drain_shipped: _build_fused_ep_moe_kernel().kernel().drain_shipped().
  _build_combine_kernel.kernel.step_pair: _build_combine_kernel().kernel().step_pair().
  _build_fused_ep_moe_kernel.kernel.w1s_copy: _build_fused_ep_moe_kernel().kernel().w1s_copy().
  _build_fused_ep_moe_kernel.kernel.w2s_copy: _build_fused_ep_moe_kernel().kernel().w2s_copy().
  COMBINE_LEAD: COMBINE_LEAD.
  logger: logger.
  _row_scale: _row_scale().
  _quant_apply: _quant_apply().
  _chunked_dot: _chunked_dot().
  _build_fused_ep_moe_kernel.kernel.wait_gather_window: _build_fused_ep_moe_kernel().kernel().wait_gather_window().
  _build_fused_ep_moe_kernel.kernel.lhs_issue_tile.issue_from: _build_fused_ep_moe_kernel().kernel().lhs_issue_tile().issue_from().
  _build_fused_ep_moe_kernel.kernel._run_tiles: _build_fused_ep_moe_kernel().kernel()._run_tiles().
  _build_fused_ep_moe_kernel.kernel.wait_shipped: _build_fused_ep_moe_kernel().kernel().wait_shipped().
  _slot_copy: _slot_copy().
  _BUILD_CACHE: _BUILD_CACHE.
  _tile_row_scales: _tile_row_scales().
  _build_fused_ep_moe_kernel.kernel._start_next_gate_up: _build_fused_ep_moe_kernel().kernel()._start_next_gate_up().
  _build_fused_ep_moe_kernel.kernel._slab_waiter: _build_fused_ep_moe_kernel().kernel()._slab_waiter().
  _build_fused_ep_moe_kernel.kernel.lhs_issue_tile.issue_from.issue_block: _build_fused_ep_moe_kernel().kernel().lhs_issue_tile().issue_from().issue_block().
  _build_fused_ep_moe_kernel.kernel.drain_commits: _build_fused_ep_moe_kernel().kernel().drain_commits().
  _build_fused_ep_moe_kernel.kernel.push_expert._.push_run: _build_fused_ep_moe_kernel().kernel().push_expert()._().push_run().
  COMBINE_GROUP: COMBINE_GROUP.
  COMBINE_CHUNK: COMBINE_CHUNK.
  _COMBINE_CACHE: _COMBINE_CACHE.
  QCHUNK: QCHUNK.
  FP4_OUTPUT_CHUNK: FP4_OUTPUT_CHUNK.
  N_TRANSPORT_TABLES: N_TRANSPORT_TABLES.
  N_PUSH_TABLES: N_PUSH_TABLES.
  N_SLAB_TABLES: N_SLAB_TABLES.
  _intermediate_rows.half: _intermediate_rows().half().
  _all_pairs_barrier: _all_pairs_barrier().
  _build_fused_ep_moe_kernel.kernel.sync: _build_fused_ep_moe_kernel().kernel().sync().
  _build_fused_ep_moe_kernel.kernel._mirror_base: _build_fused_ep_moe_kernel().kernel()._mirror_base().
  _build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body.compute_tile.store_parity: _build_fused_ep_moe_kernel().kernel().expert_tiles().tile_body().compute_tile().store_parity().
  _build_combine_kernel.kernel.start_row: _build_combine_kernel().kernel().start_row().
  AXIS: AXIS.
  HEIGHT_RUNGS: HEIGHT_RUNGS.
  COLLECTIVE_ID: COLLECTIVE_ID.
  _REF_BITCAST_JAX_VERSION: _REF_BITCAST_JAX_VERSION.
  N_VISIT_TABLES: N_VISIT_TABLES.
  N_COUNT_TABLES: N_COUNT_TABLES.
  N_RANK_TABLES: N_RANK_TABLES.
  N_STAGING_INPUTS: N_STAGING_INPUTS.
  N_WEIGHT_SLABS: N_WEIGHT_SLABS.
  N_SCALE_TABLES: N_SCALE_TABLES.
  _absmax_rows: _absmax_rows().
  _build_fused_ep_moe_kernel.kernel._slab_waiter.wait: _build_fused_ep_moe_kernel().kernel()._slab_waiter().wait().
  _build_fused_ep_moe_kernel.kernel.lhs_ready_tile: _build_fused_ep_moe_kernel().kernel().lhs_ready_tile().
  _BUILD_CACHE_LOCK: _BUILD_CACHE_LOCK.
  COMBINE_TOKENS: COMBINE_TOKENS.
  COMBINE_MIN_TOKENS: COMBINE_MIN_TOKENS.
  _build_combine_kernel.kernel.reduce_token: _build_combine_kernel().kernel().reduce_token().
  _build_combine_kernel.fn: _build_combine_kernel().fn().
  _COMBINE_CACHE_LOCK: _COMBINE_CACHE_LOCK.
---
# Module: [`src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py)

## Functions
- <a id="_absmax_rows"></a>`_absmax_rows(x)` — [`L198`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L198)
- <a id="_all_pairs_barrier"></a>`_all_pairs_barrier(ep)` — [`L461`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L461) — Barrier over every shard: transport peers are not only neighbours.
- <a id="_and_nonempty"></a>`_and_nonempty(pred, rows)` — [`L495`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L495) — `pred` and a nonzero length: a zero-length DMA must never issue.
- <a id="_apply_act"></a>`_apply_act(gate, up, act_fn)` — [`L124`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L124) — The FFN activation, on the POST-SCALE gate and up halves.
- <a id="_build_combine_kernel"></a>`_build_combine_kernel(*, t_local, topk, hidden, lane_blocks, wire_dtype, out_dtype)` — [`L2220`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2220) — out[i] = sum_k coef[i, k] * arrivals[pos[i * topk + k]]. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="_build_fused_ep_moe_kernel"></a>`_build_fused_ep_moe_kernel(*, g_local, capacity, hidden, inter, ep, weight_format=host.WeightFormat.FP8, rhs_qb=QB4, ragged_rows_alloc=None, act_fn="silu", has_w1_bias=False, has_w2_bias=False)` — [`L524`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L524) — Build the pallas_call and the function that invokes it. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="_chunked_dot"></a>`_chunked_dot(lhs, rhs_chunk, n_chunks, kb)` — [`L304`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L304) — Contract lhs against a weight handed over one contraction chunk at a
- <a id="_build_fused_ep_moe_kernel.kernel._fp4_block_readers"></a>`_fp4_block_readers(slot, wait_slab=None, slab_retired=None)` — [`L1006`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1006) — (w1_block, w2_block) fp4 block readers at weight slot `slot`. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="_build_fused_ep_moe_kernel.kernel._int8_chunk_readers"></a>`_int8_chunk_readers(slot)` — [`L1060`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1060) — (w1_chunk, w2_chunk) integer chunk readers at slot `slot`.
- <a id="_intermediate_rows"></a>`_intermediate_rows(acc1, act_scale, inter, *, w1s, act_fn, w1b, requantize=True)` — [`L250`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L250) — acc1's gate and up halves through the activation, as the second — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="_build_fused_ep_moe_kernel.kernel._mirror_base"></a>`_mirror_base(e)` — [`L1184`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1184) — Sublane expert e's tiles start at in the contribution mirror.
- <a id="_quant_apply"></a>`_quant_apply(x, sinv_native, usable)` — [`L202`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L202) — Quantize a row, or zero it whole where its scale is unusable.
- <a id="_row_scale"></a>`_row_scale(amax)` — [`L171`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L171) — The row scale and its inverse, with the rows that have no usable one.
- <a id="_rows_wait"></a>`_rows_wait(sem, ref, rows)` — [`L490`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L490) — Block until `rows` rows' worth of DMAs on `sem` have landed.
- <a id="_build_fused_ep_moe_kernel.kernel._run_tiles"></a>`_run_tiles(e, d, region_blocks)` — [`L1195`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1195) — A run's mirror sublanes: (source, destination, count).
- <a id="_build_fused_ep_moe_kernel.kernel._slab_waiter"></a>`_slab_waiter(expert, slot, first_tile)` — [`L983`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L983) — `(copy, block) -> ()`: land the slab that block `block` opens,
- <a id="_slot_copy"></a>`_slot_copy(src, vm, sems, slot)` — [`L485`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L485) — A copy of `src` into buffer slot `slot`, on that slot's semaphore.
- <a id="_build_fused_ep_moe_kernel.kernel._start_next_gate_up"></a>`_start_next_gate_up(visit_i, slot, last_tile)` — [`L964`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L964) — `() -> ()`: start the NEXT expert's gate/up slab, called from
- <a id="_tile_row_scales"></a>`_tile_row_scales(window, row_base, tile_m)` — [`L500`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L500) — One tile's activation row scales as the [tile_m, 1] column the FFN
- <a id="build_combine_kernel"></a>`build_combine_kernel(**kwargs)` — [`L2366`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2366) — Memoizing front door; see build_fused_ep_moe_kernel for why.
- <a id="build_fused_ep_moe_kernel"></a>`build_fused_ep_moe_kernel(**kwargs)` — [`L2125`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2125) — Memoizing front door for _build_fused_ep_moe_kernel. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="combine_step_tokens"></a>`combine_step_tokens(t_local)` — [`L2196`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2196) — Tokens a combine step stages, or 0 where this path does not apply. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="_build_fused_ep_moe_kernel.kernel.expert_tiles.commit_tile"></a>`commit_tile(parity, t, tile_block_base, live_blocks)` — [`L1323`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1323) — Commit the tile's intersection with each (expert, dest) run.
- <a id="_build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body.compute_tile"></a>`compute_tile(height)` — [`L1538`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1538) — Run the FFN on the tile's leading `height` rows. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="expert_ffn_blockscale.contract"></a>`contract(lhs, rhs_block, scales, n_blocks, n_out)` — [`L372`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L372)
- <a id="_build_fused_ep_moe_kernel.kernel.count"></a>`count(row)` — [`L789`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L789) — Close one count's reduction on the scalar core.
- <a id="_build_fused_ep_moe_kernel.kernel.drain_commits"></a>`drain_commits(carried)` — [`L1743`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1743) — Drain both parities' pending commits, then zero the counts.
- <a id="_build_fused_ep_moe_kernel.kernel.drain_shipped"></a>`drain_shipped(carried)` — [`L1758`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1758) — Wait out whatever the last tile on each parity put on the wire.
- <a id="_build_fused_ep_moe_kernel.kernel.drain_transport"></a>`drain_transport()` — [`L1849`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1849) — Consume the pushes and the commits the per-tile waits left. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="expert_ffn_bf16"></a>`expert_ffn_bf16(act, w1, w2, act_fn="silu", w1b=None)` — [`L400`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L400) — One expert's FFN on unquantized sixteen-bit weights.
- <a id="expert_ffn_blockscale"></a>`expert_ffn_blockscale(act_q, act_scale, w1_block, w2_block, w1s_blocks, w2s_blocks, *, qb=QB4, act_fn="silu", w1b=None)` — [`L342`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L342) — One expert's FFN on block-scaled weights: the same body as
- <a id="expert_ffn_fp8"></a>`expert_ffn_fp8(act_q, act_scale, w1, w2, w1s, act_fn="silu", w1b=None)` — [`L325`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L325) — One expert's FFN on eight-bit weights: the gate/up matmul, the
- <a id="expert_ffn_int8"></a>`expert_ffn_int8(act, w1_chunk, w2_chunk, w1s, *, n_chunks1, n_chunks2, kb=host.WIDEN_KCHUNK, act_fn="silu", w1b=None)` — [`L421`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L421) — One expert's FFN on eight-bit INTEGER weights with per-channel scales.
- <a id="_build_fused_ep_moe_kernel.kernel.expert_tiles"></a>`expert_tiles(e, visit_i, carry)` — [`L1269`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1269) — One expert step: a fori_loop over its [tile_m, H] tiles. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="_build_fused_ep_moe_kernel.fn"></a>`fn(tables, token_gather, expert_rows, expert_base, act_q_gathered, act_scales, w1, w2, w1s, w2s, w1b=None, w2b=None, *, recv_rows, visit, counts, rank)` — [`L2026`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2026) — The served ragged transport form; returns arrivals and scales.
- <a id="_build_combine_kernel.fn"></a>`fn(arrivals, coef, pos)` — [`L2346`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2346)
- <a id="_build_fused_ep_moe_kernel.kernel.gather_dma_coords"></a>`gather_dma_coords(logical_base)` — [`L1084`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1084) — Aligned HBM base and in-window offset for a slab row.
- <a id="_intermediate_rows.half"></a>`half(lo, hi)` — [`L268`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L268) — One post-scale half of the accumulator, columns [lo, hi).
- <a id="_build_fused_ep_moe_kernel.kernel.lhs_issue_tile.issue_from.issue_block"></a>`issue_block(i, _)` — [`L1137`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1137) — Fetch eight token rows of block i by their numbers.
- <a id="_build_fused_ep_moe_kernel.kernel.lhs_issue_tile.issue_from"></a>`issue_from(gather_smem)` — [`L1136`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1136)
- <a id="_build_fused_ep_moe_kernel.kernel.issue_gather_window"></a>`issue_gather_window(logical_base, slot)` — [`L1093`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1093) — Start one fixed token-index window in SMEM slot ``slot``.
- <a id="_build_fused_ep_moe_kernel.kernel"></a>`kernel(*refs)` — [`L758`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L758) — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="_build_combine_kernel.kernel"></a>`kernel(pos_sm, coef_sm, arr_hbm, out_hbm, rows_vm, tile_vm, out_vm, row_sems, out_sems)` — [`L2242`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2242)
- <a id="_build_fused_ep_moe_kernel.kernel.lhs_issue_tile"></a>`lhs_issue_tile(row_base, live_blocks, slot, gather_slot, gather_offset)` — [`L1133`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1133) — Issue one tile's activations using a resident index window.
- <a id="_build_fused_ep_moe_kernel.kernel.lhs_ready_tile"></a>`lhs_ready_tile(live_rows, slot)` — [`L1169`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1169) — Wait the token rows and the scale window of one tile.
- <a id="_build_fused_ep_moe_kernel.make_call"></a>`make_call(recv_rows)` — [`L1960`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1960) — The pallas_call for this build, at this arrival-buffer height. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="_build_combine_kernel.kernel.one_step.one_chunk"></a>`one_chunk(chunk, carry)` — [`L2287`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2287)
- <a id="_build_combine_kernel.kernel.one_step"></a>`one_step(step, parity)` — [`L2268`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2268)
- <a id="_build_fused_ep_moe_kernel.kernel.prime_expert"></a>`prime_expert(e, lhs_slot, wslot, window_started)` — [`L1237`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1237) — Prime expert ``e``'s metadata and first activation tile. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="_build_fused_ep_moe_kernel.kernel.prologue"></a>`prologue()` — [`L945`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L945) — Land the resident tables and start the first weight refills.
- <a id="_build_fused_ep_moe_kernel.kernel.push_expert"></a>`push_expert(e)` — [`L1772`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1772) — Push expert e's remote regions and hop its own-dest region.
- <a id="_build_fused_ep_moe_kernel.kernel.push_expert._.push_run"></a>`push_run()` — [`L1788`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1788) — The rows themselves, at their true length.
- <a id="_build_combine_kernel.kernel.reduce_token"></a>`reduce_token(base, parity, i)` — [`L2257`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2257) — One token's weighted sum, in the arrival rows' own layout.
- <a id="rowquant_fp8"></a>`rowquant_fp8(x)` — [`L191`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L191) — Per-row dynamic fp8 quant, reducing and applying in bf16.
- <a id="_build_fused_ep_moe_kernel.kernel.expert_tiles.ship_tile"></a>`ship_tile(parity, t, tile_block_base, live_blocks)` — [`L1368`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1368) — Ship the tile straight out of `out_vm`, no slab in between.
- <a id="_build_fused_ep_moe_kernel.kernel._start_next_gate_up.start"></a>`start()` — [`L974`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L974)
- <a id="_build_combine_kernel.kernel.start_row"></a>`start_row(base, parity, i, k)` — [`L2245`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2245)
- <a id="_build_combine_kernel.kernel.step_pair"></a>`step_pair(pair, carry)` — [`L2304`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2304)
- <a id="_build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body.compute_tile.store_parity"></a>`store_parity(static_parity)` — [`L1651`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1651) — Stage the tile's rows and scales in one out_vm
- <a id="_build_fused_ep_moe_kernel.kernel.sync"></a>`sync(src, dst)` — [`L893`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L893) — Copy `src` into `dst` and wait for it before returning.
- <a id="_build_fused_ep_moe_kernel.kernel.expert_tiles.tile_body"></a>`tile_body(t, carried)` — [`L1465`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1465) — Compute tile t, stage it for the wire and ship it. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="tile_height_rungs"></a>`tile_height_rungs(tile_m, rows_alloc, g_local, ep)` — [`L142`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L142) — The ascending static tile heights a build emits, ending at tile_m.
- <a id="_build_fused_ep_moe_kernel.kernel.visit_step"></a>`visit_step(visit_i, carry)` — [`L1835`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1835) — One step of the visit list: compute, then drain and push.
- <a id="_build_fused_ep_moe_kernel.kernel._fp4_block_readers.w1_block"></a>`w1_block(b, n_start, n_end)` — [`L1023`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1023)
- <a id="_build_fused_ep_moe_kernel.kernel._int8_chunk_readers.w1_chunk"></a>`w1_chunk(b)` — [`L1069`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1069)
- <a id="_build_fused_ep_moe_kernel.kernel.w1_copy"></a>`w1_copy(expert, slot)` — [`L899`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L899) — The gate/up weight slab of `expert`, into weight slot `slot`.
- <a id="_build_fused_ep_moe_kernel.kernel.w1s_copy"></a>`w1s_copy(expert, slot)` — [`L907`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L907)
- <a id="_build_fused_ep_moe_kernel.kernel._fp4_block_readers.w2_block"></a>`w2_block(b, n_start, n_end)` — [`L1046`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1046)
- <a id="_build_fused_ep_moe_kernel.kernel._int8_chunk_readers.w2_chunk"></a>`w2_chunk(b)` — [`L1074`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1074)
- <a id="_build_fused_ep_moe_kernel.kernel.w2_copy"></a>`w2_copy(expert, slot)` — [`L903`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L903) — The down weight slab of `expert`, into weight slot `slot`.
- <a id="_build_fused_ep_moe_kernel.kernel.w2s_copy"></a>`w2s_copy(expert, slot)` — [`L911`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L911)
- <a id="_build_fused_ep_moe_kernel.kernel._slab_waiter.wait"></a>`wait(copy, block)` — [`L996`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L996)
- <a id="_build_fused_ep_moe_kernel.kernel.wait_commits"></a>`wait_commits(parity, live_blocks)` — [`L1211`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1211) — Wait one tile's commits on `parity`: data rows, then scales.
- <a id="_build_fused_ep_moe_kernel.kernel.wait_gather_window"></a>`wait_gather_window(logical_base, slot)` — [`L1113`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1113) — Wait for the fixed token-index window in ``slot``.
- <a id="_build_fused_ep_moe_kernel.kernel.wait_shipped"></a>`wait_shipped(parity, rows, subs)` — [`L1218`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L1218) — Wait until the wire has read `parity`'s staging slot.
- <a id="_build_fused_ep_moe_kernel.kernel.weight_starts"></a>`weight_starts(expert, slot)` — [`L915`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L915) — Start every buffer slot `slot` holds for `expert`. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="_build_fused_ep_moe_kernel.kernel.weight_waits"></a>`weight_waits(expert, slot)` — [`L930`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L930) — Wait for what the expert's first block needs.
- <a id="wire_row_and_scale"></a>`wire_row_and_scale(acc2, mid_scale, *, w2s=None, w2b=None, wire_dtype=FP8, tile_m=None)` — [`L207`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L207) — One tile's rows as they go on the wire, and the scale that rides with

## Module values
- <a id="ACT_FNS"></a>`ACT_FNS` — [`L121`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L121)
- <a id="AXIS"></a>`AXIS` — [`L54`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L54)
- <a id="COLLECTIVE_ID"></a>`COLLECTIVE_ID` — [`L73`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L73)
- <a id="COMBINE_CHUNK"></a>`COMBINE_CHUNK` — [`L2183`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2183)
- <a id="COMBINE_GROUP"></a>`COMBINE_GROUP` — [`L2177`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2177)
- <a id="COMBINE_LEAD"></a>`COMBINE_LEAD` — [`L2193`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2193)
- <a id="COMBINE_MIN_TOKENS"></a>`COMBINE_MIN_TOKENS` — [`L2187`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2187)
- <a id="COMBINE_PARITIES"></a>`COMBINE_PARITIES` — [`L2188`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2188)
- <a id="COMBINE_TOKENS"></a>`COMBINE_TOKENS` — [`L2173`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2173)
- <a id="DN"></a>`DN` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L52)
- <a id="FP4_OUTPUT_CHUNK"></a>`FP4_OUTPUT_CHUNK` — [`L59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L59)
- <a id="HEIGHT_RUNGS"></a>`HEIGHT_RUNGS` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L67)
- <a id="N_COUNT_TABLES"></a>`N_COUNT_TABLES` — [`L91`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L91)
- <a id="N_PREFETCH"></a>`N_PREFETCH` — [`L100`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L100) — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="N_PUSH_TABLES"></a>`N_PUSH_TABLES` — [`L88`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L88)
- <a id="N_RANK_TABLES"></a>`N_RANK_TABLES` — [`L99`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L99)
- <a id="N_SCALE_TABLES"></a>`N_SCALE_TABLES` — [`L115`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L115)
- <a id="N_SLAB_TABLES"></a>`N_SLAB_TABLES` — [`L89`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L89)
- <a id="N_STAGING_INPUTS"></a>`N_STAGING_INPUTS` — [`L113`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L113)
- <a id="N_TRANSPORT_TABLES"></a>`N_TRANSPORT_TABLES` — [`L87`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L87)
- <a id="N_VISIT_TABLES"></a>`N_VISIT_TABLES` — [`L90`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L90)
- <a id="N_WEIGHT_SLABS"></a>`N_WEIGHT_SLABS` — [`L114`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L114)
- <a id="QCHUNK"></a>`QCHUNK` — [`L57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L57)
- <a id="WEIGHT_DMA_PRIORITY"></a>`WEIGHT_DMA_PRIORITY` — [`L70`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L70)
- <a id="_BUILD_CACHE"></a>`_BUILD_CACHE` — [`L2119`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2119)
- <a id="_BUILD_CACHE_LOCK"></a>`_BUILD_CACHE_LOCK` — [`L2122`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2122)
- <a id="_COMBINE_CACHE"></a>`_COMBINE_CACHE` — [`L2362`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2362)
- <a id="_COMBINE_CACHE_LOCK"></a>`_COMBINE_CACHE_LOCK` — [`L2363`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L2363)
- <a id="_REF_BITCAST_JAX_VERSION"></a>`_REF_BITCAST_JAX_VERSION` — [`L77`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L77)
- <a id="logger"></a>`logger` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/kernel.py#L50)

