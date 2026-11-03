---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compressor_v1.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compressor_v1.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.compress_and_store.compressor_v1`/
symbols:
  derive_metadata: derive_metadata().
  compressor_forward: compressor_forward().
  prepare_boundary_batch: prepare_boundary_batch().
  _pack_array: _pack_array().
  block_table_row_stride: block_table_row_stride().
  prepare_boundary_batch.scatter: prepare_boundary_batch().scatter().
  _get_packing_indices: _get_packing_indices().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compressor_v1.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compressor_v1.py)

## Functions
- <a id="_get_packing_indices"></a>`_get_packing_indices(keep, size)` — [`L148`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compressor_v1.py#L148)
- <a id="_pack_array"></a>`_pack_array(x, safe, valid, default_value)` — [`L155`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compressor_v1.py#L155)
- <a id="block_table_row_stride"></a>`block_table_row_stride(block_table: jax.Array, num_reqs: int)` — [`L24`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compressor_v1.py#L24) — Per-request row stride of a flattened [num_reqs * max_blocks] table.
- <a id="compressor_forward"></a>`compressor_forward(hidden_states: jax.Array, wkv_wgate: jax.Array, ape: jax.Array, norm_weight: jax.Array, cos_sin_cache: jax.Array, positions: jax.Array, block_table: jax.Array, query_start_loc: jax.Array, kv_block_table: jax.Array, cache: jax.Array, rope_cache: jax.Array | None, distribution: jax.Array, state_block_size: int, head_dim: int, compress_ratio: int, overlap: bool, rms_eps: float, quant_block: int, state_cache: jax.Array | None = None, seq_along_lane: bool = False)` — [`L229`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compressor_v1.py#L229) — Projects, saves state, then compresses and stores the boundary records. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="derive_metadata"></a>`derive_metadata(positions: jax.Array, block_table: jax.Array, query_start_loc: jax.Array, kv_block_table: jax.Array, cache: jax.Array, compress_ratio: int, state_block_size: int, head_dim: int, overlap: bool, cos_sin_cache: jax.Array | None, state_cache: jax.Array | None = None, seq_along_lane: bool = False)` — [`L31`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compressor_v1.py#L31) — Derives token_to_req_indices, slot_mapping_slots, and kv_slot_mapping. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="prepare_boundary_batch"></a>`prepare_boundary_batch(positions: jax.Array, token_to_req_indices: jax.Array, kv_slot_mapping: jax.Array, is_boundary: jax.Array, is_decode_token: jax.Array, compress_ratio: int, num_reqs: int, rope_pack: int = 4)` — [`L159`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compressor_v1.py#L159) — Generates a combined batch of boundary tokens in a single scatter. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="prepare_boundary_batch.scatter"></a>`scatter(default_val, src)` — [`L215`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compressor_v1.py#L215)

