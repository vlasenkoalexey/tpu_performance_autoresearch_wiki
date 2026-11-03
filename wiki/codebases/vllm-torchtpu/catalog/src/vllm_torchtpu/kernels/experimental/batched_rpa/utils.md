---
title: 'Module: src/vllm_torchtpu/kernels/experimental/batched_rpa/utils.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/batched_rpa/utils.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.batched_rpa.utils`/
symbols:
  align_to: align_to().
  get_dtype_packing: get_dtype_packing().
  broadcast_minor: broadcast_minor().
  strided_load: strided_load().
  convert_to_target_bitwidth: convert_to_target_bitwidth().
  align_span: align_span().
  strided_store: strided_store().
  get_dtype_bits: get_dtype_bits().
  has_bank_conflicts: has_bank_conflicts().
  cp_local_cache_len: cp_local_cache_len().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/utils.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/utils.py)

## Functions
- <a id="align_span"></a>`align_span(start, size, align)` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/utils.py#L27) — Returns (aligned_start, lead, aligned_size) for [start, start + size).
- <a id="align_to"></a>`align_to(a, b)` — [`L22`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/utils.py#L22) — Returns 'a' aligned to 'b'. — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="broadcast_minor"></a>`broadcast_minor(src, shape)` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/utils.py#L50) — Broadcasts 'src' to 'shape' in the minor dimension.
- <a id="convert_to_target_bitwidth"></a>`convert_to_target_bitwidth(val, target_bitwidth: int, kv_dtype: jnp.dtype)` — [`L113`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/utils.py#L113) — Converts a value to a target bitwidth.
- <a id="cp_local_cache_len"></a>`cp_local_cache_len(global_kv_cache_len, cp_group_size, cp_rank, page_size)` — [`L34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/utils.py#L34) — Number of cache tokens owned by this CP rank.
- <a id="get_dtype_bits"></a>`get_dtype_bits(dtype)` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/utils.py#L67)
- <a id="get_dtype_packing"></a>`get_dtype_packing(dtype)` — [`L63`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/utils.py#L63) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="has_bank_conflicts"></a>`has_bank_conflicts(stride: int, distance=24, num_banks=32)` — [`L155`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/utils.py#L155)
- <a id="strided_load"></a>`strided_load(ref, start_row, num_rows, step, *, dtype=None)` — [`L71`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/utils.py#L71) — Loads data from HBM with strided access, handling 128-lane alignment.
- <a id="strided_store"></a>`strided_store(ref, start, sz, step, val)` — [`L93`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/utils.py#L93) — Stores data to HBM with strided access, handling 128-lane alignment.

