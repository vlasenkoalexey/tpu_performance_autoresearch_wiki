---
title: 'Module: src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.custom_ops.deepseek_v4.deepseek_v4_attention_op`/
symbols:
  _attention_hca: _attention_hca().
  _attention_csa: _attention_csa().
  VllmDeepseekV4SWACache.get_kv_cache_spec: VllmDeepseekV4SWACache#get_kv_cache_spec().
  _run_swa: _run_swa().
  get_packed_mla_head_size: get_packed_mla_head_size().
  VllmDeepseekV4SWACache.block_size: VllmDeepseekV4SWACache#block_size.
  VllmDeepseekSparseSWABackend: VllmDeepseekSparseSWABackend#
  VllmDeepseekV4SWACache: VllmDeepseekV4SWACache#
  VllmDeepseekV4SWACache._swa_block_size: VllmDeepseekV4SWACache#_swa_block_size().
  logger: logger.
  VllmDeepseekV4SWACache.__init__: VllmDeepseekV4SWACache#__init__().
  BATCH_AXIS: BATCH_AXIS.
  VllmDeepseekSparseSWABackend.get_min_page_size: VllmDeepseekSparseSWABackend#get_min_page_size().
---
# Module: [`src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py)

## Classes
### <a id="VllmDeepseekSparseSWABackend"></a>`VllmDeepseekSparseSWABackend`
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py:279`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py#L279)
- doc: TPU attention backend for DeepSeek-V4 SWA cache.
- signature: `class VllmDeepseekSparseSWABackend(DeepseekSparseSWABackend):`
- members:
  - <a id="VllmDeepseekSparseSWABackend.get_min_page_size"></a>`get_min_page_size(cls, vllm_config: VllmConfig)` — [`L283`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py#L283)
- used by: [`__init__`](deepseek_v4_attention_op.md#VllmDeepseekV4SWACache.__init__), [`swa_backend_cls`](../../../../models/vllm/deepseek_v4/attention.md#VllmDeepseekV4MLAAttention.swa_backend_cls)

### <a id="VllmDeepseekV4SWACache"></a>`VllmDeepseekV4SWACache`
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py:287`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py#L287) — documented in [custom-ops](../../../../../../../concepts/custom-ops.md)
- doc: Sliding-window KV cache, paged to fit inside a CSA main page.
- signature: `class VllmDeepseekV4SWACache(DeepseekV4SWACache):`
- members:
  - <a id="VllmDeepseekV4SWACache.get_kv_cache_spec"></a>`get_kv_cache_spec(self, vllm_config: VllmConfig)` — [`L327`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py#L327)
  - <a id="VllmDeepseekV4SWACache.block_size"></a>`block_size` — [`L309`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py#L309)
- protocol/private: <a id="VllmDeepseekV4SWACache.__init__"></a>`__init__`[`L290`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py#L290), <a id="VllmDeepseekV4SWACache._swa_block_size"></a>`_swa_block_size`[`L312`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py#L312)
- uses (calls/refs, reference-scoped): [`VllmDeepseekSparseSWABackend`](deepseek_v4_attention_op.md#VllmDeepseekSparseSWABackend)
- used by: [`_build_attn_op`](../../../../models/vllm/deepseek_v4/attention.md#VllmDeepseekV4MLAAttention._build_attn_op), [`__init__`](../../../../models/vllm/deepseek_v4/attention.md#VllmDeepseekV4MLAAttention.__init__)

## Functions
- <a id="_attention_csa"></a>`_attention_csa(q: jax.Array, new_kv: jax.Array, sw_cache: jax.Array, swa_kv_lens: jax.Array, swa_page_indices: jax.Array, swa_cu_q_lens: jax.Array, swa_distribution: jax.Array, main_cache_kv: jax.Array, main_kv_lens: jax.Array, extra: jax.Array, main_page_indices: jax.Array, main_cu_q_lens: jax.Array, main_distribution: jax.Array, attention_sinks: jax.Array, main_cache_rope: jax.Array, *, sm_scale: float, sliding_window: int, logical_page_size: int, swa_only: bool, two_caches_same_buffer: bool, non_causal_block: bool = False, verify_q_len: int | None = None)` — [`L182`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py#L182) — CSA: sparse gather over top-k rows, NoPE and RoPE in two arrays. — documented in [deepseek-v4-model](../../../../../../../concepts/deepseek-v4-model.md)
- <a id="_attention_hca"></a>`_attention_hca(q: jax.Array, new_kv: jax.Array, sw_cache: jax.Array, swa_kv_lens: jax.Array, swa_page_indices: jax.Array, swa_cu_q_lens: jax.Array, swa_distribution: jax.Array, main_cache_kv: jax.Array, main_kv_lens: jax.Array, extra: jax.Array, main_page_indices: jax.Array, main_cu_q_lens: jax.Array, main_distribution: jax.Array, attention_sinks: jax.Array, *, sm_scale: float, sliding_window: int, logical_page_size: int, swa_only: bool, two_caches_same_buffer: bool, non_causal_block: bool = False, verify_q_len: int | None = None)` — [`L98`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py#L98) — SWA-only layers, and HCA layers over a single raw-bf16 latent array. — documented in [deepseek-v4-model](../../../../../../../concepts/deepseek-v4-model.md)
- <a id="_run_swa"></a>`_run_swa(q: jax.Array, new_kv: jax.Array, sw_cache: jax.Array, swa_kv_lens: jax.Array, swa_page_indices: jax.Array, swa_cu_q_lens: jax.Array, swa_distribution: jax.Array, attention_sinks: jax.Array, *, sm_scale: float, sliding_window: int, logical_page_size: int, swa_only: bool, non_causal_block: bool = False, verify_q_len: int | None = None)` — [`L45`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py#L45) — Sliding-window pass: updates the SWA cache and returns its partials.
- <a id="get_packed_mla_head_size"></a>`get_packed_mla_head_size(hf_config)` — [`L271`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py#L271) — Calculate TPU 128-byte aligned packed width for DSv4 FP8 cache entries.

## Module values
- <a id="BATCH_AXIS"></a>`BATCH_AXIS` — [`L42`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py#L42)
- <a id="logger"></a>`logger` — [`L40`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_attention_op.py#L40)

