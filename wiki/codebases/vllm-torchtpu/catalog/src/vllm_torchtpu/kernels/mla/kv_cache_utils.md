---
title: 'Module: src/vllm_torchtpu/kernels/mla/kv_cache_utils.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/mla/kv_cache_utils.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.mla.kv_cache_utils`/
symbols:
  SparseMLAKVCacheSpec.shape: SparseMLAKVCacheSpec#shape().
  _scatter_rows: _scatter_rows().
  SparseMLAKVCacheSpec.create: SparseMLAKVCacheSpec#create().
  WORD_BYTES: WORD_BYTES.
  SparseMLAKVCacheSpec: SparseMLAKVCacheSpec#
  _scatter_caches: _scatter_caches().
  SparseMLAKVCacheSpec.layout: SparseMLAKVCacheSpec#layout.
  TILE_LANE_BYTES: TILE_LANE_BYTES.
  _get_dcp_page_and_slot: _get_dcp_page_and_slot().
  KVCacheLayout: KVCacheLayout#
  update_sparse_mla_kv_cache: update_sparse_mla_kv_cache().
  SparseMLAKVCacheSpec.page_size: SparseMLAKVCacheSpec#page_size.
  _check_inputs: _check_inputs().
  update_sparse_mla_kv_cache_jax: update_sparse_mla_kv_cache_jax().
  SparseMLAKVCacheSpec.jax_dtype: SparseMLAKVCacheSpec#jax_dtype().
  update_sparse_mla_kv_cache_dcp: update_sparse_mla_kv_cache_dcp().
  KVCacheType: KVCacheType#
  update_sparse_mla_kv_cache_dcp_jax: update_sparse_mla_kv_cache_dcp_jax().
  _LAYOUT_DTYPES: _LAYOUT_DTYPES.
  get_kv_cache_shape: get_kv_cache_shape().
  SparseMLAKVCacheSpec.tokens_per_row: SparseMLAKVCacheSpec#tokens_per_row().
  get_page_and_slot: get_page_and_slot().
  SparseMLAKVCacheSpec.cache_type: SparseMLAKVCacheSpec#cache_type.
  SparseMLAKVCacheSpec.token_bytes: SparseMLAKVCacheSpec#token_bytes().
  SparseMLAKVCacheSpec.num_pages: SparseMLAKVCacheSpec#num_pages.
  pack_tokens: pack_tokens().
  _dst_rows: _dst_rows().
  KVCacheLayout.TENSORCORE: KVCacheLayout#TENSORCORE.
  get_dst_rows: get_dst_rows().
  OOB_PAGE: OOB_PAGE.
  KVCacheLayout.SPARSECORE: KVCacheLayout#SPARSECORE.
  SparseMLAKVCacheSpec.torch_dtype: SparseMLAKVCacheSpec#torch_dtype().
  KVCacheType.NOPE: KVCacheType#NOPE.
  KVCacheType.ROPE: KVCacheType#ROPE.
  SparseMLAKVCacheSpec.head_dim: SparseMLAKVCacheSpec#head_dim.
  SparseMLAKVCacheSpec.kv_packing: SparseMLAKVCacheSpec#kv_packing.
  _row_positions: _row_positions().
  SC_ROPE_ALIGN_BYTES: SC_ROPE_ALIGN_BYTES.
  get_dtype_packing: get_dtype_packing().
  align_to: align_to().
  as_token_bytes: as_token_bytes().
  SKIP_ROW: SKIP_ROW.
  _xla_unpadded_word_rows: _xla_unpadded_word_rows().
  get_dtype_bitwidth: get_dtype_bitwidth().
---
# Module: [`src/vllm_torchtpu/kernels/mla/kv_cache_utils.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py)

## Classes
### <a id="KVCacheLayout"></a>`KVCacheLayout`  ·  implements/extends Enum
- def: [`src/vllm_torchtpu/kernels/mla/kv_cache_utils.py:42`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L42) — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
- doc: Physical HBM layout of a paged KV cache.
- signature: `class KVCacheLayout(enum.Enum):`
- members:
  - <a id="KVCacheLayout.SPARSECORE"></a>`SPARSECORE` — [`L51`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L51)
  - <a id="KVCacheLayout.TENSORCORE"></a>`TENSORCORE` — [`L52`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L52)
- used by: [`shape`](kv_cache_utils.md#SparseMLAKVCacheSpec.shape), [`_scatter_rows`](kv_cache_utils.md#_scatter_rows), [`create`](kv_cache_utils.md#SparseMLAKVCacheSpec.create), [`scatter`](scatter.md#scatter), [`get_sparse_kv_cache_specs`](../../layers/adapter/attention.md#PallasMLAttentionBackend.get_sparse_kv_cache_specs), [`_scatter_caches`](kv_cache_utils.md#_scatter_caches), [`layout`](kv_cache_utils.md#SparseMLAKVCacheSpec.layout), [`_LAYOUT_DTYPES`](kv_cache_utils.md#_LAYOUT_DTYPES)

### <a id="KVCacheType"></a>`KVCacheType`  ·  implements/extends Enum
- def: [`src/vllm_torchtpu/kernels/mla/kv_cache_utils.py:55`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L55) — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
- doc: The type of a paged KV cache.
- signature: `class KVCacheType(enum.Enum):`
- members:
  - <a id="KVCacheType.NOPE"></a>`NOPE` — [`L58`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L58)
  - <a id="KVCacheType.ROPE"></a>`ROPE` — [`L59`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L59)
- used by: [`shape`](kv_cache_utils.md#SparseMLAKVCacheSpec.shape), [`_scatter_rows`](kv_cache_utils.md#_scatter_rows), [`create`](kv_cache_utils.md#SparseMLAKVCacheSpec.create), [`get_sparse_kv_cache_specs`](../../layers/adapter/attention.md#PallasMLAttentionBackend.get_sparse_kv_cache_specs), [`cache_type`](kv_cache_utils.md#SparseMLAKVCacheSpec.cache_type)

### <a id="SparseMLAKVCacheSpec"></a>`SparseMLAKVCacheSpec`
- def: [`src/vllm_torchtpu/kernels/mla/kv_cache_utils.py:107`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L107) — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
- signature: `class SparseMLAKVCacheSpec:`
- members:
  - <a id="SparseMLAKVCacheSpec.create"></a>`create(cls, cache_type: KVCacheType, layout: KVCacheLayout, num_pages: int, page_size: int, head_dim: int, kv_packing: int = 4)` — [`L116`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L116) — Builds a spec with the kernel's page/head-dim padding applied. — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
  - <a id="SparseMLAKVCacheSpec.jax_dtype"></a>`jax_dtype(self)` — [`L181`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L181) — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
  - <a id="SparseMLAKVCacheSpec.shape"></a>`shape(self)` — [`L199`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L199) — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
  - <a id="SparseMLAKVCacheSpec.token_bytes"></a>`token_bytes(self)` — [`L189`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L189) — Bytes reserved per token slot (assumes 1 byte/element for FP8).
  - <a id="SparseMLAKVCacheSpec.tokens_per_row"></a>`tokens_per_row(self)` — [`L194`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L194) — Tokens sharing one `TILE_LANE_BYTES`-word row of a ROPE/SC cache. — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
  - <a id="SparseMLAKVCacheSpec.torch_dtype"></a>`torch_dtype(self)` — [`L185`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L185) — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
  - <a id="SparseMLAKVCacheSpec.cache_type"></a>`cache_type` — [`L108`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L108)
  - <a id="SparseMLAKVCacheSpec.head_dim"></a>`head_dim` — [`L112`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L112)
  - <a id="SparseMLAKVCacheSpec.kv_packing"></a>`kv_packing` — [`L113`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L113)
  - <a id="SparseMLAKVCacheSpec.layout"></a>`layout` — [`L109`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L109) — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
  - <a id="SparseMLAKVCacheSpec.num_pages"></a>`num_pages` — [`L110`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L110)
  - <a id="SparseMLAKVCacheSpec.page_size"></a>`page_size` — [`L111`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L111) — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
- uses (calls/refs, reference-scoped): [`WORD_BYTES`](kv_cache_utils.md#WORD_BYTES), [`TILE_LANE_BYTES`](kv_cache_utils.md#TILE_LANE_BYTES), [`KVCacheLayout`](kv_cache_utils.md#KVCacheLayout), [`KVCacheType`](kv_cache_utils.md#KVCacheType), [`_LAYOUT_DTYPES`](kv_cache_utils.md#_LAYOUT_DTYPES), [`get_kv_cache_shape`](kv_cache_utils.md#get_kv_cache_shape), [`TENSORCORE`](kv_cache_utils.md#KVCacheLayout.TENSORCORE), [`SPARSECORE`](kv_cache_utils.md#KVCacheLayout.SPARSECORE), [`NOPE`](kv_cache_utils.md#KVCacheType.NOPE), [`ROPE`](kv_cache_utils.md#KVCacheType.ROPE), [`SC_ROPE_ALIGN_BYTES`](kv_cache_utils.md#SC_ROPE_ALIGN_BYTES), [`align_to`](kv_cache_utils.md#align_to), [`_xla_unpadded_word_rows`](kv_cache_utils.md#_xla_unpadded_word_rows)
- used by: [`initialize_kv_cache`](../../runner/kv_cache_manager.md#KVCacheManager.initialize_kv_cache), [`_scatter_rows`](kv_cache_utils.md#_scatter_rows), [`scatter`](scatter.md#scatter), [`get_sparse_kv_cache_specs`](../../layers/adapter/attention.md#PallasMLAttentionBackend.get_sparse_kv_cache_specs), [`_local`](../../layers/core/attention_interface.md#sparse_mla_attention_dcp._local), [`_scatter_caches`](kv_cache_utils.md#_scatter_caches), [`_get_dcp_page_and_slot`](kv_cache_utils.md#_get_dcp_page_and_slot), [`sparse_mla_attention`](../../layers/core/attention_interface.md#sparse_mla_attention), [`sparse_mla_attention_dcp`](../../layers/core/attention_interface.md#sparse_mla_attention_dcp), [`update_sparse_mla_kv_cache`](kv_cache_utils.md#update_sparse_mla_kv_cache), [`_check_inputs`](kv_cache_utils.md#_check_inputs), [`update_sparse_mla_kv_cache_jax`](kv_cache_utils.md#update_sparse_mla_kv_cache_jax), [`update_sparse_mla_kv_cache_dcp`](kv_cache_utils.md#update_sparse_mla_kv_cache_dcp), [`get_sparse_kv_cache_page_size_bytes`](../../layers/adapter/attention.md#PallasMLAttentionBackend.get_sparse_kv_cache_page_size_bytes), [`update_sparse_mla_kv_cache_dcp_jax`](kv_cache_utils.md#update_sparse_mla_kv_cache_dcp_jax)

## Functions
- <a id="_check_inputs"></a>`_check_inputs(kv_cache_nope: jax.Array, kv_cache_rope: jax.Array, kv_c_normed: jax.Array, nope_spec: SparseMLAKVCacheSpec, rope_spec: SparseMLAKVCacheSpec)` — [`L346`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L346) — Assert the caches were allocated from the specs they are written with. — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
- <a id="_dst_rows"></a>`_dst_rows(page: jax.Array, slot: jax.Array, page_size: int)` — [`L313`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L313) — (page, slot) -> flattened row, `SKIP_ROW` wherever `page` is `OOB_PAGE`.
- <a id="_get_dcp_page_and_slot"></a>`_get_dcp_page_and_slot(num_tokens: int, seq_lens: jax.Array, block_tables: jax.Array, query_start_loc: jax.Array, dcp_rank: jax.Array, *, nope_spec: SparseMLAKVCacheSpec, dcp_size: int, interleave_size: int)` — [`L614`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L614) — This rank's (page, slot) per token; `OOB_PAGE` for rows it does not own. — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
- <a id="_row_positions"></a>`_row_positions(num_tokens: int, seq_lens: jax.Array, query_start_loc: jax.Array)` — [`L254`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L254) — Per-row `(token, sequence, global KV position, valid)`.
- <a id="_scatter_caches"></a>`_scatter_caches(kv_cache_nope: jax.Array, kv_cache_rope: jax.Array, kv_c_normed: jax.Array, k_pe: jax.Array, page: jax.Array, slot: jax.Array, nope_spec: SparseMLAKVCacheSpec, rope_spec: SparseMLAKVCacheSpec)` — [`L430`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L430) — Write both caches at (`page`, `slot`), with Pallas wherever it can. — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
- <a id="_scatter_rows"></a>`_scatter_rows(cache: jax.Array, spec: SparseMLAKVCacheSpec, values: jax.Array, page: jax.Array, slot: jax.Array)` — [`L325`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L325) — Write each token's `values` into the (`page`, `slot`) it lands in. — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
- <a id="_xla_unpadded_word_rows"></a>`_xla_unpadded_word_rows(rows: int)` — [`L72`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L72) — Whether `rows` 128-word rows per page avoid XLA `(8, 128)` tile padding.
- <a id="align_to"></a>`align_to(x: int, a: int)` — [`L68`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L68)
- <a id="as_token_bytes"></a>`as_token_bytes(values: jax.Array, token_bytes: int)` — [`L228`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L228) — `[num_tokens, n]` -> `[num_tokens, token_bytes]` uint8, zero-padded.
- <a id="get_dst_rows"></a>`get_dst_rows(num_tokens: int, seq_lens: jax.Array, block_tables: jax.Array, query_start_loc: jax.Array, page_size: int)` — [`L299`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L299) — Computes flattened row indices for SparseCore scatter kernels.
- <a id="get_dtype_bitwidth"></a>`get_dtype_bitwidth(dtype: jnp.dtype)` — [`L77`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L77)
- <a id="get_dtype_packing"></a>`get_dtype_packing(dtype: jnp.dtype)` — [`L81`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L81)
- <a id="get_kv_cache_shape"></a>`get_kv_cache_shape(total_num_pages: int, page_size: int, kv_dim: int, kv_dtype: jnp.dtype | None = None, kv_packing: int | None = None)` — [`L86`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L86) — Computes padded 4D shape
- <a id="get_page_and_slot"></a>`get_page_and_slot(num_tokens: int, seq_lens: jax.Array, block_tables: jax.Array, query_start_loc: jax.Array, page_size: int)` — [`L281`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L281) — Computes target (page, slot) in the paged KV cache for each token.
- <a id="pack_tokens"></a>`pack_tokens(values: jax.Array, token_bytes: int)` — [`L238`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L238) — `[num_tokens, n]` -> `[num_tokens, token_bytes // WORD_BYTES]` uint32.
- <a id="update_sparse_mla_kv_cache"></a>`update_sparse_mla_kv_cache(kv_cache_nope: jax.Array, kv_cache_rope: jax.Array, kv_c_normed: jax.Array, k_pe: jax.Array, seq_lens: jax.Array, block_tables: jax.Array, query_start_loc: jax.Array, *, nope_spec: SparseMLAKVCacheSpec, rope_spec: SparseMLAKVCacheSpec)` — [`L376`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L376) — Scatter this step's new MLA latents into the split sparse-MLA cache. — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
- <a id="update_sparse_mla_kv_cache_dcp"></a>`update_sparse_mla_kv_cache_dcp(kv_cache_nope: jax.Array, kv_cache_rope: jax.Array, kv_c_normed: jax.Array, k_pe: jax.Array, seq_lens: jax.Array, block_tables: jax.Array, query_start_loc: jax.Array, dcp_rank: jax.Array, *, nope_spec: SparseMLAKVCacheSpec, rope_spec: SparseMLAKVCacheSpec, dcp_size: int, interleave_size: int)` — [`L495`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L495) — Scatter this step's MLA latents into a DCP position-sharded cache. — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
- <a id="update_sparse_mla_kv_cache_dcp_jax"></a>`update_sparse_mla_kv_cache_dcp_jax(kv_cache_nope: jax.Array, kv_cache_rope: jax.Array, kv_c_normed: jax.Array, k_pe: jax.Array, seq_lens: jax.Array, block_tables: jax.Array, query_start_loc: jax.Array, dcp_rank: jax.Array, *, nope_spec: SparseMLAKVCacheSpec, rope_spec: SparseMLAKVCacheSpec, dcp_size: int, interleave_size: int)` — [`L576`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L576) — Pure-XLA `update_sparse_mla_kv_cache_dcp`, for every layout. — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
- <a id="update_sparse_mla_kv_cache_jax"></a>`update_sparse_mla_kv_cache_jax(kv_cache_nope: jax.Array, kv_cache_rope: jax.Array, kv_c_normed: jax.Array, k_pe: jax.Array, seq_lens: jax.Array, block_tables: jax.Array, query_start_loc: jax.Array, *, nope_spec: SparseMLAKVCacheSpec, rope_spec: SparseMLAKVCacheSpec)` — [`L463`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L463) — Pure-XLA `update_sparse_mla_kv_cache`, for every layout. — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)

## Module values
- <a id="OOB_PAGE"></a>`OOB_PAGE` — [`L38`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L38)
- <a id="SC_ROPE_ALIGN_BYTES"></a>`SC_ROPE_ALIGN_BYTES` — [`L34`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L34)
- <a id="SKIP_ROW"></a>`SKIP_ROW` — [`L39`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L39)
- <a id="TILE_LANE_BYTES"></a>`TILE_LANE_BYTES` — [`L32`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L32) — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
- <a id="WORD_BYTES"></a>`WORD_BYTES` — [`L31`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L31) — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
- <a id="_LAYOUT_DTYPES"></a>`_LAYOUT_DTYPES` — [`L62`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/kv_cache_utils.py#L62)

