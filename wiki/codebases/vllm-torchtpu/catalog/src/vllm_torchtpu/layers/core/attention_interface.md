---
title: 'Module: src/vllm_torchtpu/layers/core/attention_interface.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/core/attention_interface.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.core.attention_interface`/
symbols:
  mla_attention._mla_ragged_paged_attention: mla_attention()._mla_ragged_paged_attention().
  sharded_ragged_paged_attention: sharded_ragged_paged_attention().
  sparse_mla_attention_dcp._local: sparse_mla_attention_dcp()._local().
  attention: attention().
  attention_bundled: attention_bundled().
  mla_attention: mla_attention().
  sparse_mla_attention: sparse_mla_attention().
  sparse_mla_attention_dcp: sparse_mla_attention_dcp().
  sparse_mla_attention._sparse_mla_ragged_paged_attention: sparse_mla_attention()._sparse_mla_ragged_paged_attention().
  ragged_paged_attention: ragged_paged_attention.
  sparse_mla_chunk_kwargs: sparse_mla_chunk_kwargs().
  sharded_paged_attention._paged_attention_fn: sharded_paged_attention()._paged_attention_fn().
  ragged_paged_attention_batched: ragged_paged_attention_batched.
  sharded_ragged_paged_attention._capped: sharded_ragged_paged_attention()._capped().
  ragged_paged_attention_hd64: ragged_paged_attention_hd64.
  mla_ragged_paged_attention: mla_ragged_paged_attention.
  sparse_mla_ragged_paged_attention: sparse_mla_ragged_paged_attention.
  sharded_flash_attention._flash_attention: sharded_flash_attention()._flash_attention().
  attention_bundled._run: attention_bundled()._run().
  MAX_ALLOWED_PAGE_INDICES_N: MAX_ALLOWED_PAGE_INDICES_N.
  logger: logger.
  get_kv_cache_shape: get_kv_cache_shape.
  get_kv_cache_shape_hd64: get_kv_cache_shape_hd64.
  sharded_flash_attention: sharded_flash_attention().
  sharded_paged_attention: sharded_paged_attention().
  paged_attention_with_guarded_smem: paged_attention_with_guarded_smem().
  sharded_splash_attention: sharded_splash_attention().
  sharded_ragged_paged_attention._ragged_paged_attention: sharded_ragged_paged_attention()._ragged_paged_attention().
  apply_splash: apply_splash().
  update_cache: update_cache().
---
# Module: [`src/vllm_torchtpu/layers/core/attention_interface.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py)

## Functions
- <a id="sharded_ragged_paged_attention._capped"></a>`_capped(case)` — [`L429`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L429)
- <a id="sharded_flash_attention._flash_attention"></a>`_flash_attention(q, k, v, segment_ids)` — [`L110`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L110)
- <a id="sparse_mla_attention_dcp._local"></a>`_local(ql_nope, q_pe, kv_c_normed, k_pe, kv_cache_nope, kv_cache_rope, topk_idx, seq_lens_, block_tables_, query_start_loc_, request_distribution_)` — [`L1169`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L1169) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="mla_attention._mla_ragged_paged_attention"></a>`_mla_ragged_paged_attention(q, q_rope, k, k_rope, cache, seq_lens, block_tables, query_start_loc, request_distribution)` — [`L746`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L746) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="sharded_paged_attention._paged_attention_fn"></a>`_paged_attention_fn(q, k, v, lengths, page_indices)` — [`L146`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L146)
- <a id="sharded_ragged_paged_attention._ragged_paged_attention"></a>`_ragged_paged_attention(*args)` — [`L451`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L451)
- <a id="attention_bundled._run"></a>`_run(q, k, v, kv_cache_bundle, layer_idx, seq_lens, block_tables, query_start_loc, request_distribution)` — [`L533`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L533)
- <a id="sparse_mla_attention._sparse_mla_ragged_paged_attention"></a>`_sparse_mla_ragged_paged_attention(ql_nope, q_pe, kv_c_normed, k_pe, kv_cache_nope, kv_cache_rope, topk_idx, seq_lens_, block_tables_, query_start_loc_, request_distribution_)` — [`L971`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L971)
- <a id="apply_splash"></a>`apply_splash(q, k, v, window_size, attn_logits_soft_cap, is_mqa)` — [`L295`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L295)
- <a id="attention"></a>`attention(kv_cache: jax.Array, q: jax.Array, k: jax.Array, v: jax.Array, attention_metadata: AttentionMetadata, mesh: Mesh, head_dim_original: int | None = None, attention_chunk_size: int | None = None, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, sinks: jax.Array | None = None, skip_kv_update: bool = False, rpa_func: Callable = ragged_paged_attention, sm_scale: float | None = None, soft_cap: float | None = None, shard: bool = True, kv_block_cap: int | None = None, use_causal_mask: bool = True, kv_layout: batched_rpa_configs.KVLayout | None = None)` — [`L607`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L607) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="attention_bundled"></a>`attention_bundled(kv_cache_bundle: jax.Array, layer_idx: jax.Array, q: jax.Array, k: jax.Array, v: jax.Array, attention_metadata: AttentionMetadata, mesh: Mesh, head_dim_original: int | None = None, attention_chunk_size: int | None = None, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, sm_scale: float | None = None, soft_cap: float | None = None, use_causal_mask: bool = True)` — [`L479`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L479) — Dispatches ragged paged attention over the bundled block-major KV cache — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="mla_attention"></a>`mla_attention(q_TNA: jax.Array, q_rope_TNH: jax.Array, k_SA: jax.Array, k_rope_SH: jax.Array, kv_cache: jax.Array, md: AttentionMetadata, mesh: Mesh, num_attention_heads: int, qk_nope_head_dim: int, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, sm_scale: float | None = None, use_causal_mask: bool = True, return_lse: bool = False)` — [`L678`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L678) — Main shared interface for Multi-Head Latent Attention (MLA). — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="paged_attention_with_guarded_smem"></a>`paged_attention_with_guarded_smem(paged_attention_kernel: Callable, q: jax.Array, k_pages: jax.Array, v_pages: jax.Array, lengths: jax.Array, page_indices: jax.Array)` — [`L178`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L178)
- <a id="sharded_flash_attention"></a>`sharded_flash_attention(mesh: Mesh, causal: bool = True, sm_scale: float | None = None, vmem_limit_bytes: int | None = None)` — [`L96`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L96)
- <a id="sharded_paged_attention"></a>`sharded_paged_attention(mesh: Mesh, attn_logits_soft_cap: float | None = None)` — [`L132`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L132) — Shards GQA PagedAttention along KV heads.
- <a id="sharded_ragged_paged_attention"></a>`sharded_ragged_paged_attention(mesh: Mesh, q: jax.Array, k: jax.Array, v: jax.Array, kv_cache: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, attention_sink: jax.Array | None, sm_scale: float, attention_chunk_size: int | None = None, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, skip_kv_update: bool = False, rpa_func: Callable = ragged_paged_attention, soft_cap: float | None = None, shard: bool = True, kv_block_cap: int | None = None, use_causal_mask: bool = True, kv_layout: batched_rpa_configs.KVLayout | None = None)` — [`L353`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L353) — Shards along KV heads. — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="sharded_splash_attention"></a>`sharded_splash_attention(mesh: Mesh, window_size: int | None = None, attn_logits_soft_cap: float | None = None, is_mqa: bool = False)` — [`L325`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L325)
- <a id="sparse_mla_attention"></a>`sparse_mla_attention(ql_nope: jax.Array, q_pe: jax.Array, kv_c_normed: jax.Array, k_pe: jax.Array, kv_cache_nope: jax.Array, kv_cache_rope: jax.Array, topk_indices: jax.Array, seq_lens: jax.Array, block_tables: jax.Array, query_start_loc: jax.Array, request_distribution: jax.Array, mesh: Mesh, nope_spec: SparseMLAKVCacheSpec, rope_spec: SparseMLAKVCacheSpec, sm_scale: float | None = None, k_scale: float | None = None, *, allow_masked_dense: bool = False)` — [`L867`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L867) — Sharded wrapper for the GLM-5.2 sparse (DSA) MLA Pallas kernel.
- <a id="sparse_mla_attention_dcp"></a>`sparse_mla_attention_dcp(ql_nope: jax.Array, q_pe: jax.Array, kv_c_normed: jax.Array, k_pe: jax.Array, kv_cache_nope: jax.Array, kv_cache_rope: jax.Array, local_topk_indices: jax.Array, seq_lens: jax.Array, block_tables: jax.Array, query_start_loc: jax.Array, request_distribution: jax.Array, mesh: Mesh, nope_spec: SparseMLAKVCacheSpec, rope_spec: SparseMLAKVCacheSpec, sm_scale: float | None = None, k_scale: float | None = None, *, dcp_size: int, interleave_size: int, dcp_axis_name: str = streamindex_topk.DCP_AXIS_NAME)` — [`L1060`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L1060) — Sparse MLA attention over a DCP position-sharded latent cache. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="sparse_mla_chunk_kwargs"></a>`sparse_mla_chunk_kwargs()` — [`L76`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L76) — Kernel kwargs for the sparse MLA gather + attention chunk size.
- <a id="update_cache"></a>`update_cache(is_prefill, cache, indices, operand, prefill_seq_len=None, sliding_window=None)` — [`L232`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L232)

## Module values
- <a id="MAX_ALLOWED_PAGE_INDICES_N"></a>`MAX_ALLOWED_PAGE_INDICES_N` — [`L59`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L59)
- <a id="get_kv_cache_shape"></a>`get_kv_cache_shape` — [`L67`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L67)
- <a id="get_kv_cache_shape_hd64"></a>`get_kv_cache_shape_hd64` — [`L70`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L70)
- <a id="logger"></a>`logger` — [`L55`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L55)
- <a id="mla_ragged_paged_attention"></a>`mla_ragged_paged_attention` — [`L72`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L72)
- <a id="ragged_paged_attention"></a>`ragged_paged_attention` — [`L65`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L65)
- <a id="ragged_paged_attention_batched"></a>`ragged_paged_attention_batched` — [`L66`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L66)
- <a id="ragged_paged_attention_hd64"></a>`ragged_paged_attention_hd64` — [`L69`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L69)
- <a id="sparse_mla_ragged_paged_attention"></a>`sparse_mla_ragged_paged_attention` — [`L73`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_interface.py#L73)

