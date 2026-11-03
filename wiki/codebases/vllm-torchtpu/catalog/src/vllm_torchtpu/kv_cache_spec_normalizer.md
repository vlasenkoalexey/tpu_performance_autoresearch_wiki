---
title: 'Module: src/vllm_torchtpu/kv_cache_spec_normalizer.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kv_cache_spec_normalizer.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kv_cache_spec_normalizer`/
symbols:
  normalize_kv_cache_specs_for_tpu: normalize_kv_cache_specs_for_tpu().
  _normalize_one_spec: _normalize_one_spec().
  _pooled_physical_mamba_spec: _pooled_physical_mamba_spec().
  _required_page_size_bytes: _required_page_size_bytes().
  _pad_page_size: _pad_page_size().
  _as_torch_dtype: _as_torch_dtype().
  _mamba_unpadded_page_size_bytes: _mamba_unpadded_page_size_bytes().
  _is_deepseek_v32_indexer_spec: _is_deepseek_v32_indexer_spec().
  _has_hybrid_attention_and_mamba: _has_hybrid_attention_and_mamba().
---
# Module: [`src/vllm_torchtpu/kv_cache_spec_normalizer.py`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_spec_normalizer.py)

## Functions
- <a id="_as_torch_dtype"></a>`_as_torch_dtype(dtype: object)` — [`L90`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_spec_normalizer.py#L90)
- <a id="_has_hybrid_attention_and_mamba"></a>`_has_hybrid_attention_and_mamba(kv_cache_specs: dict[str, KVCacheSpec])` — [`L160`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_spec_normalizer.py#L160)
- <a id="_is_deepseek_v32_indexer_spec"></a>`_is_deepseek_v32_indexer_spec(spec: KVCacheSpec)` — [`L110`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_spec_normalizer.py#L110) — True for packed uint8 DSA indexer K-cache (`DeepseekV32IndexerCache`).
- <a id="_mamba_unpadded_page_size_bytes"></a>`_mamba_unpadded_page_size_bytes(spec: MambaSpec)` — [`L170`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_spec_normalizer.py#L170)
- <a id="_normalize_one_spec"></a>`_normalize_one_spec(spec: KVCacheSpec, kv_cache_dtype: torch.dtype, *, attention_backend: type[PallasAttentionBackend] | None)` — [`L121`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_spec_normalizer.py#L121) — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- <a id="_pad_page_size"></a>`_pad_page_size(spec: KVCacheSpec, page_size: int)` — [`L183`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_spec_normalizer.py#L183)
- <a id="_pooled_physical_mamba_spec"></a>`_pooled_physical_mamba_spec(spec: KVCacheSpec)` — [`L96`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_spec_normalizer.py#L96) — Retype a two-state (conv, ssm) mamba spec to the dtypes the unified
- <a id="_required_page_size_bytes"></a>`_required_page_size_bytes(spec: KVCacheSpec)` — [`L177`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_spec_normalizer.py#L177)
- <a id="normalize_kv_cache_specs_for_tpu"></a>`normalize_kv_cache_specs_for_tpu(kv_cache_specs: dict[str, KVCacheSpec], kv_cache_dtype: torch.dtype, *, enable_unified_kv_layout: bool = False, exempt_layers: set[str] | None = None, attention_backend: type[PallasAttentionBackend] | None)` — [`L34`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kv_cache_spec_normalizer.py#L34) — Normalize KV cache specs to the TPU's real page geometry. — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)

