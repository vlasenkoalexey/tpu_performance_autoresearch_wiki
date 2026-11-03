---
title: 'Module: src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.fused_moe_decode.fused_moe_decode_kernel`/
symbols:
  plan_weight_ring: plan_weight_ring().
  _kernel: _kernel().
  _Q_BLOCK: _Q_BLOCK.
  vmem_bytes: vmem_bytes().
  fused_moe_decode: fused_moe_decode().
  plan_weight_ring.fit: plan_weight_ring().fit().
  _kernel.run_routed: _kernel().run_routed().
  _kernel.accumulate: _kernel().accumulate().
  _token_side_bytes: _token_side_bytes().
  _kernel.transfers: _kernel().transfers().
  _kernel.run_routed.expert_body: _kernel().run_routed().expert_body().
  _kernel.first_matmul: _kernel().first_matmul().
  _N_CHUNK: _N_CHUNK.
  _unit_bytes: _unit_bytes().
  _weight_ring_depth: _weight_ring_depth().
  _kernel.prime_routed.prime: _kernel().prime_routed().prime().
  _kernel.run_routed.expert_body.wait_next: _kernel().run_routed().expert_body().wait_next().
  _kernel.run_routed.expert_body.refill: _kernel().run_routed().expert_body().refill().
  _NUM_BUFFERS: _NUM_BUFFERS.
  _kernel.all_to_all_sum: _kernel().all_to_all_sum().
  _kernel.compact: _kernel().compact().
  _kernel.block_transfers: _kernel().block_transfers().
  _I_BLOCKS: _I_BLOCKS.
  _VMEM_RESERVE: _VMEM_RESERVE.
  _kernel.compact.record: _kernel().compact().record().
  _kernel.prime_routed: _kernel().prime_routed().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py)

## Functions
- <a id="_kernel"></a>`_kernel(active_ref, rank_ref, x_ref, coeff_ref, shared_gate_ref, w1_hbm, w2_hbm, w1_scale_hbm, w2_scale_hbm, shared_w1_hbm, shared_w1_scale_hbm, shared_w2_hbm, shared_w2_scale_hbm, out_ref, w1_ring, w2_ring, w1_scale_ring, w2_scale_ring, shared_w1_vmem, shared_w1_scale_vmem, shared_w2_vmem, shared_w2_scale_vmem, xq_ref, xs_ref, acc_ref, acc_bf16, recv, red, ids_ref, sem_ref, shared_sem, a2a_send, a2a_recv, ag_send, ag_recv, *, m, h, i, experts, nb, n_ranks, weight_dtype, rows=None, ib=None)` — [`L89`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L89) — One rank's MoE block. Shapes use m tokens (padded to 16), h hidden, i
- <a id="_token_side_bytes"></a>`_token_side_bytes(m, h, i_s, experts, n_ranks, wt)` — [`L483`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L483) — Everything the call declares but the routed weight ring: the shared
- <a id="_unit_bytes"></a>`_unit_bytes(h, width, wt)` — [`L478`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L478) — One ring slot: w13 [h, 2 width] + w2 [width, h] plus their f32 scales.
- <a id="_weight_ring_depth"></a>`_weight_ring_depth(h, i, weight_dtype)` — [`L462`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L462) — Deepest weight ring (at most _NUM_BUFFERS slots, at least 3) whose slots
- <a id="_kernel.accumulate"></a>`accumulate(acc1, coeff, w1_scale, w2, w2_scale)` — [`L302`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L302) — Finish one expert from its first-matmul result acc1 [m, 2 width]
- <a id="_kernel.all_to_all_sum"></a>`all_to_all_sum(send_slice, dst)` — [`L395`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L395) — Reduce-scatter semantics by a direct all-to-all and a local sum,
- <a id="_kernel.block_transfers"></a>`block_transfers(step)` — [`L252`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L252) — Unit `step` = block step % nblk of active expert step // nblk.
- <a id="_kernel.compact"></a>`compact(e, count)` — [`L226`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L226)
- <a id="_kernel.run_routed.expert_body"></a>`expert_body(step, acc1)` — [`L363`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L363)
- <a id="_kernel.first_matmul"></a>`first_matmul(w1)` — [`L286`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L286) — xq @ w1 ([h, 2 width] ref) in f32, each _Q_BLOCK-row slab of w1
- <a id="plan_weight_ring.fit"></a>`fit(w)` — [`L526`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L526)
- <a id="fused_moe_decode"></a>`fused_moe_decode(rank, hidden, w1, w2, w1_scale, w2_scale, shared_w1, shared_w1_scale, shared_w2, shared_w2_scale, shared_gate_weight, topk_weights, topk_ids, *, n_ranks, expert_start=None, scatter_rows=False, routed_scale=1, i_block=None)` — [`L552`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L552) — Per-rank body; call inside shard_map over the TP mesh.
- <a id="plan_weight_ring"></a>`plan_weight_ring(m, h, i, i_s, experts, n_ranks, weight_dtype, i_block=None)` — [`L503`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L503) — (ib, nb) for `m` padded tokens: the block width (None for whole
- <a id="_kernel.prime_routed.prime"></a>`prime(*, initial=initial)` — [`L342`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L342)
- <a id="_kernel.prime_routed"></a>`prime_routed()` — [`L338`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L338)
- <a id="_kernel.compact.record"></a>`record()` — [`L228`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L228)
- <a id="_kernel.run_routed.expert_body.refill"></a>`refill()` — [`L382`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L382)
- <a id="_kernel.run_routed"></a>`run_routed()` — [`L359`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L359)
- <a id="_kernel.transfers"></a>`transfers(step)` — [`L237`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L237)
- <a id="vmem_bytes"></a>`vmem_bytes(tokens, h, i, i_s, experts, n_ranks, weight_dtype)` — [`L540`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L540) — VMEM the call declares for `tokens` rows: its VMEM operands, output and
- <a id="_kernel.run_routed.expert_body.wait_next"></a>`wait_next()` — [`L367`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L367)

## Module values
- <a id="_I_BLOCKS"></a>`_I_BLOCKS` — [`L474`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L474)
- <a id="_NUM_BUFFERS"></a>`_NUM_BUFFERS` — [`L72`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L72)
- <a id="_N_CHUNK"></a>`_N_CHUNK` — [`L63`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L63)
- <a id="_Q_BLOCK"></a>`_Q_BLOCK` — [`L77`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L77)
- <a id="_VMEM_RESERVE"></a>`_VMEM_RESERVE` — [`L475`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.py#L475)

