---
title: 'Module: src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py
status: fresh
symbol_base: 'scip-python python vllm-torchtpu 0.0.0 '
symbols:
  _kernel: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_kernel().'
  moe_tp_decode: '`jax._src.pjit`/moe_tp_decode#'
  can_use_moe_tp_decode: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/can_use_moe_tp_decode().'
  _vmem_plan: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_vmem_plan().'
  FP8: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/FP8.'
  _Q_BLOCK: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_Q_BLOCK.'
  _quantize_blocks: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_quantize_blocks().'
  _kernel.finish: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_kernel().finish().'
  _kernel.run_experts: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_kernel().run_experts().'
  _route: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_route().'
  _shared_expert: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_shared_expert().'
  _kernel.run_experts.expert_body: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_kernel().run_experts().expert_body().'
  _N_CHUNK: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_N_CHUNK.'
  FP8_MAX: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/FP8_MAX.'
  kernel_name: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/kernel_name().'
  _kernel.gate_up: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_kernel().gate_up().'
  _NUM_BUFFERS: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_NUM_BUFFERS.'
  _kernel.transfers: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_kernel().transfers().'
  ROW_BUCKETS: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/ROW_BUCKETS.'
  exact_in_bf16: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/exact_in_bf16().'
  _kernel.prime.start: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_kernel().prime().start().'
  _kernel.run_experts.expert_body.wait_next: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_kernel().run_experts().expert_body().wait_next().'
  _kernel.run_experts.expert_body.refill: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_kernel().run_experts().expert_body().refill().'
  ROUTER_NEG: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/ROUTER_NEG.'
  SUM_FLOOR: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/SUM_FLOOR.'
  PAIR: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/PAIR.'
  VMEM_HEADROOM: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/VMEM_HEADROOM.'
  VMEM_FRACTION: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/VMEM_FRACTION.'
  _combine: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_combine().'
  _kernel.compact: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_kernel().compact().'
  _kernel.prime: '`src.vllm_torchtpu.kernels.experimental.moe_tp_decode.kernel`/_kernel().prime().'
---
# Module: [`src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py)

## Classes
### <a id="moe_tp_decode"></a>`moe_tp_decode`
- def: [`src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py:457`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L457)
- doc: The layer's bf16 [N, D] output, summed over the n_ranks TP ranks.
- signature: `def moe_tp_decode(x, scores, bias, n_valid, rank, w13, w2, s13, s2, shared_w13, shared_s13, shared_w2, shared_s2, *, routed_scale: float, topk: int, n_ranks: int): # -> Any:`
- uses (calls/refs, reference-scoped): [`_kernel`](kernel.md#_kernel), [`scratch_shapes`](all_reduce.md#scratch_shapes), [`_vmem_plan`](kernel.md#_vmem_plan), [`FP8`](kernel.md#FP8), [`_Q_BLOCK`](kernel.md#_Q_BLOCK), [`make_spec`](all_reduce.md#make_spec), [`kernel_name`](kernel.md#kernel_name), [`_NUM_BUFFERS`](kernel.md#_NUM_BUFFERS), [`exact_in_bf16`](kernel.md#exact_in_bf16), [`COLLECTIVE_ID`](all_reduce.md#COLLECTIVE_ID)
- used by: [`body`](../../../layers/adapter/moe_tp_decode.md#_op_body.body)

## Functions
- <a id="_combine"></a>`_combine(routed_sum, shared_sum, routed_scale)` — [`L241`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L241) — The usual TP path's combine, roundings included:
- <a id="_kernel"></a>`_kernel(meta_ref, x_ref, scores_ref, bias_ref, w1_hbm, w2_hbm, s1_hbm, s2_hbm, sw13_hbm, ss13_hbm, sw2_hbm, ss2_hbm, out_ref, w1_ref, w2_ref, s1_ref, s2_ref, sw13_ref, ss13_ref, sw2_ref, ss2_ref, sxq_ref, xq_ref, xs_ref, owner_ref, shared_ref, wtab_ref, hits_v_ref, hits_s_ref, active_ids_ref, ring_sem, shared_sem, hit_sem, *ar_scr, local_experts, topk, routed_scale, ar_spec)` — [`L251`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L251)
- <a id="_quantize_blocks"></a>`_quantize_blocks(x, q_ref, scale_ref)` — [`L207`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L207) — x [m, h] bf16 to FP8 in q_ref as gmm_v2 quantizes its LHS: per row per
- <a id="_route"></a>`_route(scores, bias, n_valid, *, topk)` — [`L182`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L182) — Routing weights [rows, E] f32: router_topk.select on scores + bias
- <a id="_shared_expert"></a>`_shared_expert(xq_ref, xs, sw13_ref, ss13_ref, sw2_ref, ss2_ref, out_ref)` — [`L223`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L223) — This rank's slice of the shared expert into out_ref (f32), as
- <a id="_vmem_plan"></a>`_vmem_plan(m, h, i, num_experts, shared_inter, info, spec)` — [`L86`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L86) — (need_bytes, vmem_limit_bytes), or None if the limit would exceed
- <a id="can_use_moe_tp_decode"></a>`can_use_moe_tp_decode(x, scores, bias, w13, w2, s13, s2, shared_w13, shared_s13, shared_w2, shared_s2, *, topk: int, n_ranks: int)` — [`L121`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L121) — Trace-time admission; False means the caller keeps its own path.
- <a id="_kernel.compact"></a>`compact(e, count)` — [`L329`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L329)
- <a id="exact_in_bf16"></a>`exact_in_bf16(value: float)` — [`L80`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L80) — True if `value` is a bf16 number, so bf16 and f32 products agree.
- <a id="_kernel.run_experts.expert_body"></a>`expert_body(step, acc1)` — [`L419`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L419)
- <a id="_kernel.finish"></a>`finish(step, slot, acc1)` — [`L386`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L386)
- <a id="_kernel.gate_up"></a>`gate_up(slot)` — [`L369`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L369)
- <a id="kernel_name"></a>`kernel_name(experts, m, h, i, shared_inter, n_ranks)` — [`L114`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L114)
- <a id="_kernel.prime"></a>`prime(step)` — [`L339`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L339)
- <a id="_kernel.run_experts.expert_body.refill"></a>`refill()` — [`L435`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L435)
- <a id="_kernel.run_experts"></a>`run_experts()` — [`L413`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L413)
- <a id="_kernel.prime.start"></a>`start()` — [`L341`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L341)
- <a id="_kernel.transfers"></a>`transfers(step)` — [`L315`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L315)
- <a id="_kernel.run_experts.expert_body.wait_next"></a>`wait_next()` — [`L423`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L423)

## Module values
- <a id="FP8"></a>`FP8` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L58)
- <a id="FP8_MAX"></a>`FP8_MAX` — [`L59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L59)
- <a id="PAIR"></a>`PAIR` — [`L65`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L65)
- <a id="ROUTER_NEG"></a>`ROUTER_NEG` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L62)
- <a id="ROW_BUCKETS"></a>`ROW_BUCKETS` — [`L60`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L60)
- <a id="SUM_FLOOR"></a>`SUM_FLOOR` — [`L64`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L64)
- <a id="VMEM_FRACTION"></a>`VMEM_FRACTION` — [`L69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L69)
- <a id="VMEM_HEADROOM"></a>`VMEM_HEADROOM` — [`L68`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L68)
- <a id="_NUM_BUFFERS"></a>`_NUM_BUFFERS` — [`L77`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L77)
- <a id="_N_CHUNK"></a>`_N_CHUNK` — [`L71`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L71)
- <a id="_Q_BLOCK"></a>`_Q_BLOCK` — [`L74`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_tp_decode/kernel.py#L74)

