---
title: 'Module: src/vllm_torchtpu/kernels/mla/v2/kv_utils.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/mla/v2/kv_utils.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.mla.v2.kv_utils`/
symbols:
  pack_new_kv: pack_new_kv().
  unsigned_mod: unsigned_mod().
  pack_new_kv_reference: pack_new_kv_reference().
  unsigned_cdiv: unsigned_cdiv().
  pack_new_kv.merge_loop_body.shift_roll: pack_new_kv().merge_loop_body().shift_roll().
  get_dtype_packing: get_dtype_packing().
  pack_new_kv.merge_loop_body: pack_new_kv().merge_loop_body().
  unsigned_floor_div: unsigned_floor_div().
  unsigned_align_to: unsigned_align_to().
  get_dtype_bitwidth: get_dtype_bitwidth().
  pack_new_kv_reference.merge_loop_body: pack_new_kv_reference().merge_loop_body().
  align_to: align_to().
---
# Module: [`src/vllm_torchtpu/kernels/mla/v2/kv_utils.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kv_utils.py)

## Functions
- <a id="align_to"></a>`align_to(a, b)` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kv_utils.py#L58)
- <a id="get_dtype_bitwidth"></a>`get_dtype_bitwidth(dtype)` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kv_utils.py#L62)
- <a id="get_dtype_packing"></a>`get_dtype_packing(dtype)` — [`L66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kv_utils.py#L66)
- <a id="pack_new_kv.merge_loop_body"></a>`merge_loop_body(i, vals)` — [`L118`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kv_utils.py#L118)
- <a id="pack_new_kv_reference.merge_loop_body"></a>`merge_loop_body(i, vals)` — [`L287`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kv_utils.py#L287)
- <a id="pack_new_kv"></a>`pack_new_kv(bkvc_vmem_ref, bkvpe_vmem_ref, offset, update_sz, q_end, kv_len, bkv_sz)` — [`L71`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kv_utils.py#L71)
- <a id="pack_new_kv_reference"></a>`pack_new_kv_reference(bkvc_vmem_ref, bkvpe_vmem_ref, offset, update_sz, q_end, kv_len, bkv_sz)` — [`L252`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kv_utils.py#L252)
- <a id="pack_new_kv.merge_loop_body.shift_roll"></a>`shift_roll(reg, roll_rolling_amount, roll_shift_bits)` — [`L163`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kv_utils.py#L163)
- <a id="unsigned_align_to"></a>`unsigned_align_to(a, b)` — [`L48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kv_utils.py#L48)
- <a id="unsigned_cdiv"></a>`unsigned_cdiv(a, b)` — [`L32`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kv_utils.py#L32)
- <a id="unsigned_floor_div"></a>`unsigned_floor_div(a, b)` — [`L40`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kv_utils.py#L40)
- <a id="unsigned_mod"></a>`unsigned_mod(a, b)` — [`L24`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kv_utils.py#L24)

