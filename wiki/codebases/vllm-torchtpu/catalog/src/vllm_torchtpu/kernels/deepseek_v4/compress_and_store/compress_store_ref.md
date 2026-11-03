---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compress_store_ref.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compress_store_ref.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.compress_and_store.compress_store_ref`/
symbols:
  ref_compress_norm_rope_store: ref_compress_norm_rope_store().
  compress_norm_rope: compress_norm_rope().
  _boundary_dest: _boundary_dest().
  quantize_fp8_ue8m0: quantize_fp8_ue8m0().
  quantize_fp8_lane_periodic: quantize_fp8_lane_periodic().
  interleaved_rope: interleaved_rope().
  gather_state_windows: gather_state_windows().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compress_store_ref.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compress_store_ref.py)

## Functions
- <a id="_boundary_dest"></a>`_boundary_dest(positions: jax.Array, slot_mapping: jax.Array, kv_slot_mapping: jax.Array, compress_ratio: int, num_slots: int)` — [`L165`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compress_store_ref.py#L165)
- <a id="compress_norm_rope"></a>`compress_norm_rope(kv_window: jax.Array, score_window: jax.Array, valid_mask: jax.Array, rms_weight: jax.Array, cos_sin_cache: jax.Array, compressed_pos: jax.Array, rms_eps: float, rope_head_dim: int)` — [`L127`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compress_store_ref.py#L127) — Window softmax-pool, RMSNorm, and interleaved RoPE.
- <a id="gather_state_windows"></a>`gather_state_windows(state_cache: jax.Array, positions: jax.Array, block_table: jax.Array, block_table_stride: int, token_to_req_indices: jax.Array, block_size: int, head_dim: int, compress_ratio: int, overlap: bool)` — [`L91`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compress_store_ref.py#L91) — Gather ``[kv_window, score_window, valid_mask]`` from the paged cache.
- <a id="interleaved_rope"></a>`interleaved_rope(x: jax.Array, cos_sin: jax.Array, rope_head_dim: int)` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compress_store_ref.py#L50) — Interleaved (GPT-J) RoPE on the trailing ``rope_head_dim`` elements.
- <a id="quantize_fp8_lane_periodic"></a>`quantize_fp8_lane_periodic(x: jax.Array, period: int, nope_dim: int)` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compress_store_ref.py#L33) — Block fp8 quantization with one UE8M0 scale per lane of `period`.
- <a id="quantize_fp8_ue8m0"></a>`quantize_fp8_ue8m0(x: jax.Array, block_size: int)` — [`L21`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compress_store_ref.py#L21) — Block fp8 quantization with UE8M0 (power-of-two) block scales.
- <a id="ref_compress_norm_rope_store"></a>`ref_compress_norm_rope_store(cache: jax.Array, rope_cache: jax.Array, positions: jax.Array, slot_mapping: jax.Array, block_table: jax.Array, token_to_req_indices: jax.Array, kv_slot_mapping: jax.Array, rms_weight: jax.Array, cos_sin_cache: jax.Array, block_table_stride: int, state_block_size: int, head_dim: int, rope_head_dim: int, compress_ratio: int, overlap: bool, rms_eps: float, quant_block: int, is_quantized: bool = True, has_rope: bool = True, has_rope_cache: bool | None = None, state_cache: jax.Array | None = None)` — [`L177`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/compress_store_ref.py#L177) — Golden JAX reference for Kernel 2 (compress + store). — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)

