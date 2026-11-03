---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.compress_and_store.kernel`/
symbols:
  inner_kernel: inner_kernel().
  compress_norm_rope_store: compress_norm_rope_store().
  kernel_fn: kernel_fn().
  _select_mode: _select_mode().
  inner_kernel._merge_nope: inner_kernel()._merge_nope().
  inner_kernel._merge_rope: inner_kernel()._merge_rope().
  compute_is_first_mask: compute_is_first_mask().
  _SAL_MAX_WAVE: _SAL_MAX_WAVE.
  kernel_fn._run: kernel_fn()._run().
  derive_aliases: derive_aliases().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/kernel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/kernel.py)

## Functions
- <a id="inner_kernel._merge_nope"></a>`_merge_nope()` — [`L172`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/kernel.py#L172)
- <a id="inner_kernel._merge_rope"></a>`_merge_rope()` — [`L198`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/kernel.py#L198)
- <a id="kernel_fn._run"></a>`_run(allocations)` — [`L272`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/kernel.py#L272)
- <a id="_select_mode"></a>`_select_mode(head_dim: int, overlap: bool)` — [`L315`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/kernel.py#L315)
- <a id="compress_norm_rope_store"></a>`compress_norm_rope_store(cache: jax.Array, positions: jax.Array, block_table: jax.Array, token_to_req_indices: jax.Array, kv_slot_mapping: jax.Array, rms_weight: jax.Array, *, block_table_stride: int, state_block_size: int, state_cache: jax.Array | None = None, rope_cache: jax.Array | None = None, cos_sin_cache: jax.Array | None = None, compress_ratio: int, overlap: bool, quant_block: int = 64, rms_eps: float = 0.000001, interpret: bool = False, name: str = "compress_norm_rope_store", seq_along_lane: bool = False)` — [`L376`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/kernel.py#L376) — Compresses, normalizes, applies RoPE and stores to cache. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="compute_is_first_mask"></a>`compute_is_first_mask(kv_slot_mapping, tile_n, pack_factor=4)` — [`L329`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/kernel.py#L329) — Determines, for every token in a sequence, whether it is the first token within
- <a id="derive_aliases"></a>`derive_aliases(has_rope: bool, has_rope_cache: bool, num_scalar_prefetch: int)` — [`L319`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/kernel.py#L319)
- <a id="inner_kernel"></a>`inner_kernel(cos_sin_vmem, out_vmem, page_buffer_vmem, rope_out_vmem, positions_ref, rms_weight_vmem_ref, window_vmem, kv_slot_mapping_ref, is_first_mask_ref, is_first_mask_rope_ref, records_t_ref=None, *, cfgs: config.Configs)` — [`L37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/kernel.py#L37) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="kernel_fn"></a>`kernel_fn(token_pages_ref, positions_ref, kv_slot_mapping_ref, is_first_mask_ref, is_first_mask_rope_ref, grid_size_ref, rms_weight_ref, cos_sin_cache_ref, cache_ref, rope_cache_ref, state_cache_ref, _out_cache_ref, _out_rope_cache_ref, window_scratch_ref, *sal_scratch, cfgs: config.Configs)` — [`L212`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/kernel.py#L212) — Pallas kernel entry point. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)

## Module values
- <a id="_SAL_MAX_WAVE"></a>`_SAL_MAX_WAVE` — [`L34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/kernel.py#L34)

