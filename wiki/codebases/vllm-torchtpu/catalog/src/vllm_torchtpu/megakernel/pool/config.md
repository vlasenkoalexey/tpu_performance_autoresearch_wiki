---
title: 'Module: src/vllm_torchtpu/megakernel/pool/config.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/pool/config.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.pool.config`/
symbols:
  cache_exec: cache_exec().
  CacheExec.num_pages: CacheExec#num_pages.
  resolved_max_pages_per_seq: resolved_max_pages_per_seq().
  CacheExec.page_size: CacheExec#page_size.
  CacheExec.GPR: CacheExec#GPR().
  CacheExec.__post_init__: CacheExec#__post_init__().
  CacheExec.pool_gather: CacheExec#pool_gather.
  with_cache: with_cache().
  PoolBackend.layout: PoolBackend#layout.
  POOL_IO_NUMERICS.POOL_IO_NUMERICS: POOL_IO_NUMERICS.POOL_IO_NUMERICS.
  CacheExec.FUSED: CacheExec#FUSED().
  PoolBackend.num_pools: PoolBackend#num_pools().
  PoolBackend.has_recurrent_pool: PoolBackend#has_recurrent_pool().
  PoolBackend.recurrent_slots_per_pool: PoolBackend#recurrent_slots_per_pool().
  PoolBackend.ckpt_pages_per_slot: PoolBackend#ckpt_pages_per_slot().
  DEFAULT_CACHE_EXEC: DEFAULT_CACHE_EXEC.
  CacheExec: CacheExec#
  PoolBackend: PoolBackend#
  POOL_GATHER_VALUES.POOL_GATHER_VALUES: POOL_GATHER_VALUES.POOL_GATHER_VALUES.
  ACT_MODE_VALUES.ACT_MODE_VALUES: ACT_MODE_VALUES.ACT_MODE_VALUES.
  CacheExec.paged_kv: CacheExec#paged_kv.
  CacheExec.max_pages_per_seq: CacheExec#max_pages_per_seq.
  CacheExec.fused_pool_io: CacheExec#fused_pool_io.
  CacheExec.act_mode: CacheExec#act_mode.
  POOL_STATE_NAME: POOL_STATE_NAME.
  PoolBackend.kernel_names: PoolBackend#kernel_names.
  PoolBackend.gather_states: PoolBackend#gather_states.
  PoolBackend.scatter_states: PoolBackend#scatter_states.
  PoolBackend.can_pool_gather: PoolBackend#can_pool_gather.
  PoolBackend.page_table_state_name: PoolBackend#page_table_state_name.
  PoolBackend.supports_fused_io: PoolBackend#supports_fused_io.
  PoolBackend.supports_pool_gather: PoolBackend#supports_pool_gather.
  CacheExec.ckpt_2d: CacheExec#ckpt_2d.
  CacheExec.ckpt_k: CacheExec#ckpt_k.
  CacheExec.roff_1d: CacheExec#roff_1d.
  CacheExec.check_ckpt_bounds: CacheExec#check_ckpt_bounds.
  __all__: __all__.
---
# Module: [`src/vllm_torchtpu/megakernel/pool/config.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py)

## Classes
### <a id="CacheExec"></a>`CacheExec`
- def: [`src/vllm_torchtpu/megakernel/pool/config.py:56`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L56)
- doc: Paged-pool execution settings (`ExecSpec.cache`).
- signature: `class CacheExec:`
- members:
  - <a id="CacheExec.FUSED"></a>`FUSED(self)` — [`L96`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L96)
  - <a id="CacheExec.GPR"></a>`GPR(self)` — [`L100`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L100) — In-kernel recurrent gather on (after `pool_gather` resolves to `True`).
  - <a id="CacheExec.act_mode"></a>`act_mode` — [`L71`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L71)
  - <a id="CacheExec.check_ckpt_bounds"></a>`check_ckpt_bounds` — [`L77`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L77)
  - <a id="CacheExec.ckpt_2d"></a>`ckpt_2d` — [`L72`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L72)
  - <a id="CacheExec.ckpt_k"></a>`ckpt_k` — [`L73`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L73)
  - <a id="CacheExec.fused_pool_io"></a>`fused_pool_io` — [`L63`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L63)
  - <a id="CacheExec.max_pages_per_seq"></a>`max_pages_per_seq` — [`L62`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L62)
  - <a id="CacheExec.num_pages"></a>`num_pages` — [`L61`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L61) — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
  - <a id="CacheExec.page_size"></a>`page_size` — [`L60`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L60) — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
  - <a id="CacheExec.paged_kv"></a>`paged_kv` — [`L59`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L59)
  - <a id="CacheExec.pool_gather"></a>`pool_gather` — [`L69`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L69) — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
  - <a id="CacheExec.roff_1d"></a>`roff_1d` — [`L74`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L74)
- protocol/private: <a id="CacheExec.__post_init__"></a>`__post_init__`[`L79`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L79)
- uses (calls/refs, reference-scoped): [`ACT_MODE_VALUES`](config.md#ACT_MODE_VALUES.ACT_MODE_VALUES), [`POOL_GATHER_VALUES`](config.md#POOL_GATHER_VALUES.POOL_GATHER_VALUES)
- used by: [`scatter_pool_states`](scatter.md#scatter_pool_states), [`validate`](layout.md#PoolLayout.validate), [`gather_gdn_states`](gather.md#gather_gdn_states), [`pool_to_states`](pack.md#pool_to_states), [`states_to_pool`](pack.md#states_to_pool), [`scatter_single_token_across_att`](scatter_kv.md#scatter_single_token_across_att), [`cache_exec`](config.md#cache_exec), [`pb_for`](scatter_ckpt.md#pb_for), [`can_pool_gather`](backend.md#can_pool_gather), [`slot_copy`](scatter_ckpt.md#slot_copy), [`min_num_pages`](layout.md#PoolLayout.min_num_pages), [`scatter_kv_seq`](scatter_kv.md#scatter_kv.scatter_kv_seq), [`exec_for`](../profile.md#Profile.exec_for), [`_scatter`](backend.md#make_pool_backend._scatter), [`resolved_max_pages_per_seq`](config.md#resolved_max_pages_per_seq), [`_gather`](backend.md#make_pool_backend._gather), [`_pages_per_seq`](pack.md#_pages_per_seq), [`page_base_for`](gather.md#gather_gdn_states._kernel.page_base_for), [`DEFAULT_CACHE_EXEC`](config.md#DEFAULT_CACHE_EXEC)

### <a id="PoolBackend"></a>`PoolBackend`
- def: [`src/vllm_torchtpu/megakernel/pool/config.py:136`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L136)
- doc: Unified pool layout and gather/scatter callbacks.
- signature: `class PoolBackend:`
- members:
  - <a id="PoolBackend.ckpt_pages_per_slot"></a>`ckpt_pages_per_slot(self)` — [`L165`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L165)
  - <a id="PoolBackend.has_recurrent_pool"></a>`has_recurrent_pool(self)` — [`L157`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L157)
  - <a id="PoolBackend.num_pools"></a>`num_pools(self)` — [`L153`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L153)
  - <a id="PoolBackend.recurrent_slots_per_pool"></a>`recurrent_slots_per_pool(self)` — [`L161`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L161)
  - <a id="PoolBackend.can_pool_gather"></a>`can_pool_gather` — [`L147`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L147)
  - <a id="PoolBackend.gather_states"></a>`gather_states` — [`L145`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L145)
  - <a id="PoolBackend.kernel_names"></a>`kernel_names` — [`L144`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L144)
  - <a id="PoolBackend.layout"></a>`layout` — [`L143`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L143)
  - <a id="PoolBackend.page_table_state_name"></a>`page_table_state_name` — [`L148`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L148)
  - <a id="PoolBackend.scatter_states"></a>`scatter_states` — [`L146`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L146)
  - <a id="PoolBackend.supports_fused_io"></a>`supports_fused_io` — [`L149`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L149)
  - <a id="PoolBackend.supports_pool_gather"></a>`supports_pool_gather` — [`L150`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L150)
- uses (calls/refs, reference-scoped): [`PoolLayout`](layout.md#PoolLayout), [`pages_per_slot`](layout.md#PoolLayout.pages_per_slot), [`num_pools`](layout.md#PoolLayout.num_pools), [`has_recurrent`](layout.md#PoolLayout.has_recurrent), [`recurrent_slots_per_pool`](layout.md#PoolLayout.recurrent_slots_per_pool)
- used by: [`make_pool_backend`](backend.md#make_pool_backend)

## Functions
- <a id="cache_exec"></a>`cache_exec(ex: ExecSpec)` — [`L110`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L110) — The `CacheExec` of `ex` (`CacheExec()` when `ex.cache` is unset). — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="resolved_max_pages_per_seq"></a>`resolved_max_pages_per_seq(ex: ExecSpec)` — [`L125`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L125) — Page-table width per sequence (`max_pages_per_seq`, else `ceil(ctx / page)`). — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="with_cache"></a>`with_cache(ex: ExecSpec, **fields: Any)` — [`L120`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L120) — `ex` with `CacheExec` `fields` replaced. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)

## Module values
- <a id="ACT_MODE_VALUES.ACT_MODE_VALUES"></a>`ACT_MODE_VALUES` — [`L41`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L41)
- <a id="DEFAULT_CACHE_EXEC"></a>`DEFAULT_CACHE_EXEC` — [`L107`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L107)
- <a id="POOL_GATHER_VALUES.POOL_GATHER_VALUES"></a>`POOL_GATHER_VALUES` — [`L40`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L40)
- <a id="POOL_IO_NUMERICS.POOL_IO_NUMERICS"></a>`POOL_IO_NUMERICS` — [`L44`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L44) — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="POOL_STATE_NAME"></a>`POOL_STATE_NAME` — [`L37`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L37)
- <a id="__all__"></a>`__all__` — [`L169`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/config.py#L169)

