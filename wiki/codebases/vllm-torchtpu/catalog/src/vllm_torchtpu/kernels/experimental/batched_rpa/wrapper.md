---
title: 'Module: src/vllm_torchtpu/kernels/experimental/batched_rpa/wrapper.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/batched_rpa/wrapper.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.batched_rpa.wrapper`/
symbols:
  ragged_paged_attention: ragged_paged_attention().
  calculate_block_sizes: calculate_block_sizes().
  calculate_block_sizes.find_best_block_sizes: calculate_block_sizes().find_best_block_sizes().
  ragged_paged_attention.run_rpa_kernel: ragged_paged_attention().run_rpa_kernel().
  calculate_block_sizes.calculate_vmem_usage: calculate_block_sizes().calculate_vmem_usage().
  prepare_inputs: prepare_inputs().
  get_kv_cache_shape: get_kv_cache_shape().
  calculate_block_sizes.calculate_compute_buffer_time: calculate_block_sizes().calculate_compute_buffer_time().
  prepare_outputs: prepare_outputs().
  _is_sfs: _is_sfs().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/wrapper.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/wrapper.py)

## Functions
- <a id="_is_sfs"></a>`_is_sfs(tpu_info)` — [`L213`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/wrapper.py#L213) — Returns True on Sunfish (TPU v8i).
- <a id="calculate_block_sizes"></a>`calculate_block_sizes(model_cfgs: configs.ModelConfigs, serve_cfgs: configs.ServingConfigs, vmem_limit_bytes: int, decode_query_size: int = 1)` — [`L226`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/wrapper.py#L226) — Calculate optimal block size for decode and prefill. — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="calculate_block_sizes.calculate_compute_buffer_time"></a>`calculate_compute_buffer_time(batch_size: int, bq_c_sz: int, bkv_sz: int)` — [`L360`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/wrapper.py#L360) — Calculate computational complexity of a single compute block.
- <a id="calculate_block_sizes.calculate_vmem_usage"></a>`calculate_vmem_usage(batch_size: int, bq_sz: int, bkv_sz: int)` — [`L272`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/wrapper.py#L272) — Given tile size, calculate VMEM usage of the kernel.
- <a id="calculate_block_sizes.find_best_block_sizes"></a>`find_best_block_sizes(max_batch_size: int, fixed_bq_sz: int | None = None)` — [`L372`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/wrapper.py#L372) — Loop through different block sizes to find the most optimal one. — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="get_kv_cache_shape"></a>`get_kv_cache_shape(total_num_pages, page_size, actual_num_kv_heads, actual_head_dim, kv_dtype, kv_layout: configs.KVLayout = configs.KVLayout.HEAD_ALONG_SUBLANE, chip_version: pltpu.ChipVersion = pltpu.ChipVersion.TPU_7X, use_per_token_scale: bool = False, scale_dtype: jnp.dtype | None = None)` — [`L175`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/wrapper.py#L175) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="prepare_inputs"></a>`prepare_inputs(q: jax.Array, k: jax.Array, v: jax.Array, q_dtype: jnp.dtype, kv_dtype: jnp.dtype, k_scale: jax.Array | None = None, v_scale: jax.Array | None = None, kv_layout: configs.KVLayout = configs.KVLayout.HEAD_ALONG_SUBLANE, page_size: int = 128)` — [`L32`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/wrapper.py#L32)
- <a id="prepare_outputs"></a>`prepare_outputs(out: jax.Array)` — [`L170`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/wrapper.py#L170)
- <a id="ragged_paged_attention"></a>`ragged_paged_attention(queries: jax.Array, keys: jax.Array, values: jax.Array, kv_cache: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, *, sm_scale: float = 1, sliding_window: int | None = None, soft_cap: float | None = None, mask_value: float | None = None, use_per_token_scale: bool = False, per_token_scale_dtype: jnp.dtype | None = None, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, dynamic_k_scale: jax.Array | None = None, dynamic_v_scale: jax.Array | None = None, chunk_prefill_size: int | None = None, decode_block_sizes: configs.BlockSizes | None = None, prefill_block_sizes: configs.BlockSizes | None = None, vmem_limit_bytes: int | None = None, debug_mode: bool = False, out_dtype: jnp.dtype | None = None, use_causal_mask: bool = True, skip_kv_update: bool = False, update_kv_cache: bool | None = None, kv_layout: configs.KVLayout = configs.KVLayout.HEAD_ALONG_SUBLANE, decode_query_size: int = 1, cp_group_size: int | None = None, cp_rank: jax.Array | None = None, attention_scope: configs.AttentionScope = configs.AttentionScope.FULL, return_lse: bool = False, mask_invalid_v: bool | None = None)` — [`L518`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/wrapper.py#L518) — Perform batched ragged paged attention. — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="ragged_paged_attention.run_rpa_kernel"></a>`run_rpa_kernel(mode: configs.RpaCase, o_hbm_alias_q_hbm: jax.Array, kv_cache: jax.Array, lse_hbm_in: jax.Array | None)` — [`L767`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/wrapper.py#L767) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)

