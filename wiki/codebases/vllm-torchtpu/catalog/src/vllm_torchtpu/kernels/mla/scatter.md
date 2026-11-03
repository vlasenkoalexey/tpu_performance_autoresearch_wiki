---
title: 'Module: src/vllm_torchtpu/kernels/mla/scatter.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/mla/scatter.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.mla.scatter`/
symbols:
  scatter: scatter().
---
# Module: [`src/vllm_torchtpu/kernels/mla/scatter.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/scatter.py)

## Functions
- <a id="scatter"></a>`scatter(cache: jax.Array, values: jax.Array, spec: kv_cache_utils.SparseMLAKVCacheSpec, seq_lens: jax.Array | None = None, block_tables: jax.Array | None = None, query_start_loc: jax.Array | None = None, dst_rows: jax.Array | None = None)` — [`L21`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/scatter.py#L21) — Packs `values` for `spec`'s layout and scatters one row per token. — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)

