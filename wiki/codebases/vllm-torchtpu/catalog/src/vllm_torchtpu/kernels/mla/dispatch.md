---
title: 'Module: src/vllm_torchtpu/kernels/mla/dispatch.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/mla/dispatch.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.mla.dispatch`/
symbols:
  select_tier: select_tier().
  attention_from_parts: attention_from_parts().
  configuration_rejection: configuration_rejection().
  layer_rejection: layer_rejection().
  select_tier.masked_dense_cost: select_tier().masked_dense_cost().
  matches_glm52_tpu7x_profile: matches_glm52_tpu7x_profile().
  attention_from_parts.masked_dense_route.split: attention_from_parts().masked_dense_route().split().
  admit_layer: admit_layer().
  masked_dense_limits: masked_dense_limits().
  attention_from_parts.masked_dense: attention_from_parts().masked_dense().
  attention_from_parts.sparse_route: attention_from_parts().sparse_route().
  applies: applies().
  attention_from_parts.masked_dense_route: attention_from_parts().masked_dense_route().
  attention_from_parts.masked_dense_route.whole: attention_from_parts().masked_dense_route().whole().
  _sparse_prefix: _sparse_prefix().
  attention_from_parts.query: attention_from_parts().query().
  logger: logger.
  _resolve_masked_dense_limit: _resolve_masked_dense_limit().
  attention_from_parts.sparse_chunk: attention_from_parts().sparse_chunk().
  GLM52_INDEX_TOPK: GLM52_INDEX_TOPK.
  MASKED_DENSE_PREFILL_COST_MODEL: MASKED_DENSE_PREFILL_COST_MODEL.
  maybe_order_prefills_by_kv_len: maybe_order_prefills_by_kv_len().
  GLM52_NUM_HEADS: GLM52_NUM_HEADS.
  GLM52_NOPE_DIM: GLM52_NOPE_DIM.
  GLM52_ROPE_DIM: GLM52_ROPE_DIM.
  GLM52_PAGE_SIZE: GLM52_PAGE_SIZE.
  MASKED_DENSE_KV_BLOCK: MASKED_DENSE_KV_BLOCK.
  attention_from_parts.crop: attention_from_parts().crop().
  MASKED_DENSE_MIN_SUFFIX_TOKENS: MASKED_DENSE_MIN_SUFFIX_TOKENS.
  split_point: split_point().
  GLM52_MODEL_TYPE: GLM52_MODEL_TYPE.
  GLM52_ARCHITECTURE: GLM52_ARCHITECTURE.
  MASKED_DENSE_ANALYTIC_MAX_KV_LEN: MASKED_DENSE_ANALYTIC_MAX_KV_LEN.
  MASKED_DENSE_MAX_KV_LEN: MASKED_DENSE_MAX_KV_LEN.
  MASKED_DENSE_KV_PAGES_PER_BLOCK: MASKED_DENSE_KV_PAGES_PER_BLOCK.
  MASKED_DENSE_QUERIES_PER_BLOCK: MASKED_DENSE_QUERIES_PER_BLOCK.
  MASKED_DENSE_MIN_TOKEN_BUCKET: MASKED_DENSE_MIN_TOKEN_BUCKET.
  _align_to: _align_to().
  _layer_topk: _layer_topk().
  order_prefills_by_kv_len: order_prefills_by_kv_len().
---
# Module: [`src/vllm_torchtpu/kernels/mla/dispatch.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py)

## Functions
- <a id="_align_to"></a>`_align_to(value: int, alignment: int)` — [`L118`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L118)
- <a id="_layer_topk"></a>`_layer_topk(attn_module)` — [`L451`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L451) — The layer's top-k width, if its indexer or shared buffer states it.
- <a id="_resolve_masked_dense_limit"></a>`_resolve_masked_dense_limit(name: str, default: int)` — [`L87`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L87)
- <a id="_sparse_prefix"></a>`_sparse_prefix(q, split_token, run_chunk)` — [`L260`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L260) — Sparse attention for query rows `[0, split_token)`, in place.
- <a id="admit_layer"></a>`admit_layer(runner, attn_module, kv_cache_specs, page_size: int)` — [`L496`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L496) — Records whether a sparse MLA layer routes masked-dense MLA.
- <a id="applies"></a>`applies(ql_nope: jax.Array, q_pe: jax.Array, kv_cache_nope: jax.Array, kv_cache_rope: jax.Array, topk_indices: jax.Array, cache_layout: str)` — [`L141`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L141) — Whether an admitted sparse MLA call may take the masked-dense branch.
- <a id="attention_from_parts"></a>`attention_from_parts(ql_nope: jax.Array, q_pe: jax.Array, kv_cache_nope: jax.Array, kv_cache_rope: jax.Array, topk_indices: jax.Array, seq_lens: jax.Array, block_tables: jax.Array, query_start_loc: jax.Array, request_distribution: jax.Array, *, sm_scale: float, k_scale: float)` — [`L282`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L282) — MLA attention for a call `applies` accepted.
- <a id="configuration_rejection"></a>`configuration_rejection(vllm_config)` — [`L401`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L401) — Why this process may not route masked-dense MLA, or None if it may.
- <a id="attention_from_parts.crop"></a>`crop(q)` — [`L309`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L309)
- <a id="layer_rejection"></a>`layer_rejection(attn_module, kv_cache_specs, page_size: int)` — [`L462`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L462) — Why a sparse MLA layer may not route masked-dense, or None if it may.
- <a id="attention_from_parts.masked_dense"></a>`masked_dense(q, max_kv_len, sequence_start=None)` — [`L338`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L338)
- <a id="select_tier.masked_dense_cost"></a>`masked_dense_cost(limit, fixed_ns, token_ns, bitmap)` — [`L213`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L213)
- <a id="masked_dense_limits"></a>`masked_dense_limits()` — [`L100`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L100) — (analytic, bitmap) KV-length limits; zero disables a tier.
- <a id="attention_from_parts.masked_dense_route"></a>`masked_dense_route(limit, max_kv_len)` — [`L363`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L363)
- <a id="matches_glm52_tpu7x_profile"></a>`matches_glm52_tpu7x_profile(q: jax.Array | jax.ShapeDtypeStruct, kv_cache_nope: jax.Array, kv_cache_rope: jax.Array, topk_indices: jax.Array)` — [`L122`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L122) — Whether static operands match the calibrated GLM-5.2 kernel profile.
- <a id="maybe_order_prefills_by_kv_len"></a>`maybe_order_prefills_by_kv_len(runner, num_decode: int, num_reqs: int, scheduler_output, spec_decode_tokens)` — [`L575`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L575) — Order prefill requests by KV length when every layer was admitted.
- <a id="order_prefills_by_kv_len"></a>`order_prefills_by_kv_len(runner, start: int, end: int, scheduler_output)` — [`L538`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L538) — Order requests `[start, end)` by KV length, longest first.
- <a id="attention_from_parts.query"></a>`query()` — [`L306`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L306)
- <a id="select_tier"></a>`select_tier(seq_lens: jax.Array, request_distribution: jax.Array, query_start_loc: jax.Array, limits: tuple[int, int], cost_model: MaskedDensePrefillCostModel | None = None)` — [`L186`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L186) — Selects 0 (analytic), 1 (bitmap) or 2 (sparse) for one step. — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
- <a id="attention_from_parts.sparse_chunk"></a>`sparse_chunk(q, start_pos, token_end, *, preserve_suffix=False)` — [`L322`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L322)
- <a id="attention_from_parts.sparse_route"></a>`sparse_route()` — [`L356`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L356)
- <a id="attention_from_parts.masked_dense_route.split"></a>`split(_)` — [`L369`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L369)
- <a id="split_point"></a>`split_point(seq_lens: jax.Array, request_distribution: jax.Array, limit: int)` — [`L167`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L167) — Splits a step into a sparse prefix and a masked-dense suffix.
- <a id="attention_from_parts.masked_dense_route.whole"></a>`whole(_)` — [`L366`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L366)

## Module values
- <a id="GLM52_ARCHITECTURE"></a>`GLM52_ARCHITECTURE` — [`L69`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L69)
- <a id="GLM52_INDEX_TOPK"></a>`GLM52_INDEX_TOPK` — [`L66`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L66)
- <a id="GLM52_MODEL_TYPE"></a>`GLM52_MODEL_TYPE` — [`L68`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L68)
- <a id="GLM52_NOPE_DIM"></a>`GLM52_NOPE_DIM` — [`L64`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L64)
- <a id="GLM52_NUM_HEADS"></a>`GLM52_NUM_HEADS` — [`L63`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L63)
- <a id="GLM52_PAGE_SIZE"></a>`GLM52_PAGE_SIZE` — [`L67`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L67)
- <a id="GLM52_ROPE_DIM"></a>`GLM52_ROPE_DIM` — [`L65`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L65)
- <a id="MASKED_DENSE_ANALYTIC_MAX_KV_LEN"></a>`MASKED_DENSE_ANALYTIC_MAX_KV_LEN` — [`L71`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L71)
- <a id="MASKED_DENSE_KV_BLOCK"></a>`MASKED_DENSE_KV_BLOCK` — [`L73`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L73)
- <a id="MASKED_DENSE_KV_PAGES_PER_BLOCK"></a>`MASKED_DENSE_KV_PAGES_PER_BLOCK` — [`L74`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L74)
- <a id="MASKED_DENSE_MAX_KV_LEN"></a>`MASKED_DENSE_MAX_KV_LEN` — [`L72`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L72)
- <a id="MASKED_DENSE_MIN_SUFFIX_TOKENS"></a>`MASKED_DENSE_MIN_SUFFIX_TOKENS` — [`L84`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L84)
- <a id="MASKED_DENSE_MIN_TOKEN_BUCKET"></a>`MASKED_DENSE_MIN_TOKEN_BUCKET` — [`L81`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L81)
- <a id="MASKED_DENSE_PREFILL_COST_MODEL"></a>`MASKED_DENSE_PREFILL_COST_MODEL` — [`L76`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L76)
- <a id="MASKED_DENSE_QUERIES_PER_BLOCK"></a>`MASKED_DENSE_QUERIES_PER_BLOCK` — [`L75`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L75)
- <a id="logger"></a>`logger` — [`L58`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/dispatch.py#L58)

