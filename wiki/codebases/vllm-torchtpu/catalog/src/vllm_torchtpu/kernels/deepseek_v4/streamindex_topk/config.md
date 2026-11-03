---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.streamindex_topk.config`/
symbols:
  KVLayout: KVLayout#
  KVLayout.HEAD_ALONG_SUBLANE: KVLayout#HEAD_ALONG_SUBLANE.
  KVLayout.SEQ_ALONG_LANE: KVLayout#SEQ_ALONG_LANE.
  KVLayout.parse: KVLayout#parse().
  MlaCase.symbol: MlaCase#symbol().
  reserve_scheduling_group_ids: reserve_scheduling_group_ids().
  reset_scheduling_group_ids: reset_scheduling_group_ids().
  MlaCase: MlaCase#
  _scheduling_group_ids: _scheduling_group_ids.
  MlaCase.MIXED: MlaCase#MIXED.
  MlaCase.DECODE: MlaCase#DECODE.
  MlaCase.PREFILL: MlaCase#PREFILL.
  _scheduling_group_ids_lock: _scheduling_group_ids_lock.
  DEFAULT_BUFFER_COUNT.DEFAULT_BUFFER_COUNT: DEFAULT_BUFFER_COUNT.DEFAULT_BUFFER_COUNT.
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py)

## Classes
### <a id="KVLayout"></a>`KVLayout`  ·  implements/extends Enum
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py:42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py#L42) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- doc: Memory layout of the packed FP8 index KV cache.
- signature: `class KVLayout(enum.Enum):`
- members:
  - <a id="KVLayout.parse"></a>`parse(cls, value: str | KVLayout | None)` — [`L69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py#L69) — Parses a `KVLayout` from a case-insensitive string (or passes through). — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
  - <a id="KVLayout.HEAD_ALONG_SUBLANE"></a>`HEAD_ALONG_SUBLANE` — [`L65`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py#L65) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
  - <a id="KVLayout.SEQ_ALONG_LANE"></a>`SEQ_ALONG_LANE` — [`L66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py#L66) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- used by: [`kernel`](streamindex_topk.md#kernel), [`streamindex_topk`](streamindex_topk.md#streamindex_topk), [`scatter_rows`](kv_cache_append.md#scatter_rows), [`check_scatter_rows_supported`](kv_cache_append.md#check_scatter_rows_supported), [`indexer_kv_layout`](streamindex_topk.md#indexer_kv_layout), [`_resolve_indexer_kv_cache_mode`](../../../layers/adapter/custom_ops/mla_attention_op.md#_resolve_indexer_kv_cache_mode), [`KVLayout`](kv_cache_append.md#KVLayout), [`get_kv_cache_shape`](streamindex_topk.md#get_kv_cache_shape), [`scatter_rows_reference`](kv_cache_append.md#scatter_rows_reference), [`KVLayout`](streamindex_topk.md#KVLayout), [`cache_page_size`](kv_cache_append.md#cache_page_size), [`run_scores_kernel`](streamindex_topk.md#streamindex_topk.run_scores_kernel), [`coalesced_kv_append`](kv_cache_append.md#coalesced_kv_append), [`coalesced_kv_append_dcp`](kv_cache_append.md#coalesced_kv_append_dcp), [`streamindex_topk_dcp`](streamindex_topk.md#streamindex_topk_dcp), [`_indexer_local`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.md#_indexer_jax._indexer_local), [`_log_indexer_kv_cache_once`](../../../layers/adapter/custom_ops/mla_attention_op.md#_log_indexer_kv_cache_once), [`_cp_scatter_indexer_k`](../../../layers/adapter/custom_ops/mla_attention_op.md#_cp_scatter_indexer_k), [`_format_rows`](kv_cache_append.md#_format_rows), [`get_kv_cache_spec`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.md#VllmDeepseekV4IndexerCache.get_kv_cache_spec), [`_unsupported_indexer_kv_cache_reason`](../../../layers/adapter/custom_ops/mla_attention_op.md#_unsupported_indexer_kv_cache_reason)

### <a id="MlaCase"></a>`MlaCase`  ·  implements/extends Enum
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py:21`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py#L21)
- doc: Represents the different cases for MLA.
- signature: `class MlaCase(enum.Enum):`
- members:
  - <a id="MlaCase.symbol"></a>`symbol(self)` — [`L34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py#L34)
  - <a id="MlaCase.DECODE"></a>`DECODE` — [`L29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py#L29)
  - <a id="MlaCase.MIXED"></a>`MIXED` — [`L31`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py#L31)
  - <a id="MlaCase.PREFILL"></a>`PREFILL` — [`L30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py#L30)
- used by: [`run_scores_kernel`](streamindex_topk.md#streamindex_topk.run_scores_kernel), [`_pass_specs`](streamindex_topk.md#streamindex_topk._pass_specs), [`MlaCase`](streamindex_topk.md#MlaCase)

## Functions
- <a id="reserve_scheduling_group_ids"></a>`reserve_scheduling_group_ids(count: int)` — [`L109`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py#L109) — Reserves `count` scheduling group ids nobody else in this process gets.
- <a id="reset_scheduling_group_ids"></a>`reset_scheduling_group_ids()` — [`L129`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py#L129) — Restarts the ids at 1, for the start of a new compiled program.

## Module values
- <a id="DEFAULT_BUFFER_COUNT.DEFAULT_BUFFER_COUNT"></a>`DEFAULT_BUFFER_COUNT` — [`L91`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py#L91)
- <a id="_scheduling_group_ids"></a>`_scheduling_group_ids` — [`L105`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py#L105)
- <a id="_scheduling_group_ids_lock"></a>`_scheduling_group_ids_lock` — [`L106`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/config.py#L106)

