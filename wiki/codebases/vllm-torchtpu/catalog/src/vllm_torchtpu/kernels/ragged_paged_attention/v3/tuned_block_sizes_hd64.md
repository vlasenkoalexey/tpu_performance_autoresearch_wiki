---
title: 'Module: src/vllm_torchtpu/kernels/ragged_paged_attention/v3/tuned_block_sizes_hd64.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/ragged_paged_attention/v3/tuned_block_sizes_hd64.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.ragged_paged_attention.v3.tuned_block_sizes_hd64`/
symbols:
  get_tuned_block_sizes: get_tuned_block_sizes().
  get_lookup_keys: get_lookup_keys().
  get_simplified_raw_key: get_simplified_raw_key().
  logger: logger.
  TUNED_BLOCK_SIZES: TUNED_BLOCK_SIZES.
---
# Module: [`src/vllm_torchtpu/kernels/ragged_paged_attention/v3/tuned_block_sizes_hd64.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/tuned_block_sizes_hd64.py)

## Functions
- <a id="get_lookup_keys"></a>`get_lookup_keys(page_size, q_dtype, kv_dtype, num_q_heads, num_kv_heads, head_dim, max_model_len)` — [`L323`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/tuned_block_sizes_hd64.py#L323) — Get the lookup keys for tuned block sizes. — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="get_simplified_raw_key"></a>`get_simplified_raw_key(page_size, q_dtype, kv_dtype, actual_num_q_heads, actual_num_kv_heads, head_dim, max_model_len)` — [`L360`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/tuned_block_sizes_hd64.py#L360) — Get the simplified key. — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="get_tuned_block_sizes"></a>`get_tuned_block_sizes(q_dtype, kv_dtype, actual_num_q_heads, actual_num_kv_heads, head_dim, page_size, max_num_tokens, pages_per_seq)` — [`L275`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/tuned_block_sizes_hd64.py#L275) — Search tuned values for (num_kv_pages_per_blk, num_queries_per_blk). — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)

## Module values
- <a id="TUNED_BLOCK_SIZES"></a>`TUNED_BLOCK_SIZES` — [`L37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/tuned_block_sizes_hd64.py#L37)
- <a id="logger"></a>`logger` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/tuned_block_sizes_hd64.py#L27)

