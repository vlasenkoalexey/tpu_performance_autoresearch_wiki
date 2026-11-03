---
title: 'Module: src/vllm_torchtpu/megakernel/pool/derive.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/pool/derive.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.pool.derive`/
symbols:
  derive_pool_layout: derive_pool_layout().
  _unwrap_cache_decl: _unwrap_cache_decl().
  __all__: __all__.
---
# Module: [`src/vllm_torchtpu/megakernel/pool/derive.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/derive.py)

## Functions
- <a id="_unwrap_cache_decl"></a>`_unwrap_cache_decl(item: Any)` — [`L32`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/derive.py#L32)
- <a id="derive_pool_layout"></a>`derive_pool_layout(decls_or_kv: Sequence[KVCacheDecl | RecurrentCacheDecl | Any | None] | KVCacheDecl | Any, rec_decl: RecurrentCacheDecl | Any | None = None, *, num_pools: int | None = None, slots_per_pool: int | None = None, R: int | None = None)` — [`L38`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/derive.py#L38) — Derive a `PoolLayout` from per-layer module cache declarations. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)

## Module values
- <a id="__all__"></a>`__all__` — [`L220`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/derive.py#L220)

