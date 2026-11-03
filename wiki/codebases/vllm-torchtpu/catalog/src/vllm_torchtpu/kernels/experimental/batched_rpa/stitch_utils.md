---
title: 'Module: src/vllm_torchtpu/kernels/experimental/batched_rpa/stitch_utils.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/batched_rpa/stitch_utils.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.batched_rpa.stitch_utils`/
symbols:
  store_new_kv_lane: store_new_kv_lane().
  stitch_new_kv_lane: stitch_new_kv_lane().
  _stitch_prefill_lane: _stitch_prefill_lane().
  _stitch_decode_lane: _stitch_decode_lane().
  _stitch_decode_lane.rolled_src: _stitch_decode_lane().rolled_src().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/stitch_utils.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/stitch_utils.py)

## Functions
- <a id="_stitch_decode_lane"></a>`_stitch_decode_lane(vmem_u32_ref: jax.Array, bkv_sz_cache: jax.Array, cache_end: jax.Array, new_tok_offset: jax.Array, bkv_sz_new: jax.Array, v_len: int, *, cfgs: configs.RpaConfigs)` — [`L24`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/stitch_utils.py#L24) — O(1) Decode Path: Target only the VREGs containing the stitch boundary.
- <a id="_stitch_prefill_lane"></a>`_stitch_prefill_lane(vmem_u32_ref: jax.Array, bkv_sz_cache: jax.Array, cache_end: jax.Array, new_tok_offset: jax.Array, v_len: int, *, cfgs: configs.RpaConfigs)` — [`L98`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/stitch_utils.py#L98) — O(N) Prefill Path: Roll the entire new tokens buffer into place.
- <a id="_stitch_decode_lane.rolled_src"></a>`rolled_src(j: int)` — [`L74`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/stitch_utils.py#L74)
- <a id="stitch_new_kv_lane"></a>`stitch_new_kv_lane(vmem_ref: jax.Ref, b_idx: int, bkv_sz_frm_cache: jax.Array, new_kv_len_start: jax.Array, bkv_sz_frm_new: jax.Array, *, cfgs: configs.RpaConfigs)` — [`L165`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/stitch_utils.py#L165) — Fetches and computes stitched KV tokens (separated to avoid RAW hazards).
- <a id="store_new_kv_lane"></a>`store_new_kv_lane(vmem_ref: jax.Ref, b_idx: int, stitch_result, *, cfgs: configs.RpaConfigs)` — [`L130`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/stitch_utils.py#L130) — Stores the result of stitch_new_kv_lane back into memory.

