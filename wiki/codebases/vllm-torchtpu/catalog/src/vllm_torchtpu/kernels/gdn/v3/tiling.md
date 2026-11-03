---
title: 'Module: src/vllm_torchtpu/kernels/gdn/v3/tiling.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/gdn/v3/tiling.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.gdn.v3.tiling`/
symbols:
  get_tile_sizes: get_tile_sizes().
  decode_tile_target: decode_tile_target().
  calculate_decode_tile_size: calculate_decode_tile_size().
  calculate_mixed_tile_size: calculate_mixed_tile_size().
  align_to: align_to().
  get_vmem_estimate_bytes: get_vmem_estimate_bytes().
  DECODE_TILE_SIZES: DECODE_TILE_SIZES.
  MIXED_TILE_SIZES: MIXED_TILE_SIZES.
  _DECODE_STEP_COST_IN_HEAD_TRANSFERS: _DECODE_STEP_COST_IN_HEAD_TRANSFERS.
---
# Module: [`src/vllm_torchtpu/kernels/gdn/v3/tiling.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/tiling.py)

## Functions
- <a id="align_to"></a>`align_to(x: int, alignment: int)` — [`L40`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/tiling.py#L40) — Aligns an integer upward to the nearest multiple of alignment.
- <a id="calculate_decode_tile_size"></a>`calculate_decode_tile_size(batch_size: int, n_kq: int, n_v: int, d_k: int, d_v: int, conv_state_dim_size: int, act_out_dtype: jnp.dtype, recurrent_state_dtype: jnp.dtype, num_lanes: int, vmem_capacity_limit_bytes: int, kernel_size: int = 4, window_size: int = 1)` — [`L135`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/tiling.py#L135) — Largest decode tile whose VMEM estimate fits the limit.
- <a id="calculate_mixed_tile_size"></a>`calculate_mixed_tile_size(seq_len: int, n_kq: int, n_v: int, d_k: int, d_v: int, conv_state_dim_size: int, act_out_dtype: jnp.dtype, recurrent_state_dtype: jnp.dtype, num_lanes: int, vmem_capacity_limit_bytes: int, kernel_size: int = 4)` — [`L204`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/tiling.py#L204) — Largest prefill chunk whose VMEM estimate fits the limit.
- <a id="decode_tile_target"></a>`decode_tile_target(num_seqs: int, n_v: int)` — [`L34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/tiling.py#L34) — Returns the largest candidate T with T^2 * n_v <= K * num_seqs, else 1.
- <a id="get_tile_sizes"></a>`get_tile_sizes(batch_size: int, num_seqs: int, padded_batch_size: int, n_kq: int, n_v: int, d_k: int, d_v: int, kernel_size: int, conv_state_dim_size: int, act_out_dtype: jnp.dtype, recurrent_state_dtype: jnp.dtype, num_lanes: int, decode_vmem_limit_bytes: int, mixed_vmem_limit_bytes: int, window_size: int = 1, decode_tile_size: int | None = None, mixed_tile_size: int | None = None)` — [`L268`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/tiling.py#L268) — Derives decode and mixed tile sizes within each kernel's VMEM limit. — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)
- <a id="get_vmem_estimate_bytes"></a>`get_vmem_estimate_bytes(tile_b: int, chunk_sz: int, n_kq: int, n_v: int, d_k: int, d_v: int, kernel_size: int, act_out_bytes: int, rec_state_bytes: int, num_lanes: int, conv_state_dim_size: int, is_decode: bool = False, carry_scratch_bytes: int = 4, window_size: int = 1)` — [`L45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/tiling.py#L45) — Estimates total on-chip VMEM footprint in bytes for a GDN tile.

## Module values
- <a id="DECODE_TILE_SIZES"></a>`DECODE_TILE_SIZES` — [`L23`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/tiling.py#L23)
- <a id="MIXED_TILE_SIZES"></a>`MIXED_TILE_SIZES` — [`L24`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/tiling.py#L24)
- <a id="_DECODE_STEP_COST_IN_HEAD_TRANSFERS"></a>`_DECODE_STEP_COST_IN_HEAD_TRANSFERS` — [`L31`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/tiling.py#L31)

