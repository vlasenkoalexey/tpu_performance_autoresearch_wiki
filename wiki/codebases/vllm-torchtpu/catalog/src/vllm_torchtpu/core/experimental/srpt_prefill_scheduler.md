---
title: 'Module: src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.core.experimental.srpt_prefill_scheduler`/
symbols:
  SrptPrefillScheduler.schedule: SrptPrefillScheduler#schedule().
  SrptPrefillScheduler._select_chunks_to_hold: SrptPrefillScheduler#_select_chunks_to_hold().
  SrptPrefillScheduler._reserve_prefill_lookahead: SrptPrefillScheduler#_reserve_prefill_lookahead().
  SrptPrefillScheduler._attn_capped_chunks: SrptPrefillScheduler#_attn_capped_chunks.
  SrptPrefillScheduler._attn_cap_tokens: SrptPrefillScheduler#_attn_cap_tokens().
  SrptPrefillScheduler._plan_running: SrptPrefillScheduler#_plan_running().
  SrptPrefillScheduler._hold_backoff: SrptPrefillScheduler#_hold_backoff.
  SrptPrefillScheduler._is_stalled: SrptPrefillScheduler#_is_stalled().
  SrptPrefillScheduler.attn_work_cap: SrptPrefillScheduler#attn_work_cap.
  SrptPrefillScheduler.attn_tile_tokens: SrptPrefillScheduler#attn_tile_tokens.
  SrptPrefillScheduler._stalled_steps: SrptPrefillScheduler#_stalled_steps.
  SrptPrefillScheduler._order_running: SrptPrefillScheduler#_order_running().
  SrptPrefillScheduler._prune_hold_state: SrptPrefillScheduler#_prune_hold_state().
  SrptPrefillScheduler._record_hold_outcome: SrptPrefillScheduler#_record_hold_outcome().
  SrptPrefillScheduler._attn_cap_on: SrptPrefillScheduler#_attn_cap_on.
  logger: logger.
  SrptPrefillScheduler.max_consecutive_holds: SrptPrefillScheduler#max_consecutive_holds.
  SrptPrefillScheduler._tokens_to_next_tile: SrptPrefillScheduler#_tokens_to_next_tile().
  SrptPrefillScheduler._attn_capped: SrptPrefillScheduler#_attn_capped.
  SrptPrefillScheduler._kv_fits_hold: SrptPrefillScheduler#_kv_fits_hold().
  SrptPrefillScheduler._in_schedule: SrptPrefillScheduler#_in_schedule.
  SrptPrefillScheduler._attn_work: SrptPrefillScheduler#_attn_work.
  SrptPrefillScheduler._attn_prefill_scheduled: SrptPrefillScheduler#_attn_prefill_scheduled.
  SrptPrefillScheduler._attn_steps: SrptPrefillScheduler#_attn_steps.
  SrptPrefillScheduler.update_from_output: SrptPrefillScheduler#update_from_output().
  SrptPrefillScheduler._other_rank_decoding: SrptPrefillScheduler#_other_rank_decoding.
  SrptPrefillScheduler._attn_cap_on_steps: SrptPrefillScheduler#_attn_cap_on_steps.
  SrptPrefillScheduler._remaining: SrptPrefillScheduler#_remaining().
  SrptPrefillScheduler.blocks_for: SrptPrefillScheduler#blocks_for().
  _MAX_BACKOFF_SHIFT: _MAX_BACKOFF_SHIFT.
  _ATTN_CAP_LOG_EVERY: _ATTN_CAP_LOG_EVERY.
  SrptPrefillScheduler._long_prefill_threshold: SrptPrefillScheduler#_long_prefill_threshold().
  SrptPrefillScheduler._next_waiting: SrptPrefillScheduler#_next_waiting().
  SrptPrefillScheduler._prefix_hit: SrptPrefillScheduler#_prefix_hit().
  SrptPrefillScheduler: SrptPrefillScheduler#
  SrptPrefillScheduler.__init__: SrptPrefillScheduler#__init__().
---
# Module: [`src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py)

## Classes
### <a id="SrptPrefillScheduler"></a>`SrptPrefillScheduler`
- def: [`src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py:89`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L89)
- doc: Order RUNNING prefill chunks by fewest remaining tokens and hold back
- signature: `class SrptPrefillScheduler(AsyncScheduler):`
- members:
  - <a id="SrptPrefillScheduler._attn_cap_tokens"></a>`_attn_cap_tokens(self, context: int, num_new_tokens: int, work: float, prefill_scheduled: bool)` — [`L203`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L203) — Tokens of a prefill chunk of ``num_new_tokens`` after ``context``
  - <a id="SrptPrefillScheduler._kv_fits_hold"></a>`_kv_fits_hold(self, kept: list[Request], alloc: dict[str, int], target: Request, hit_blocks: KVCacheBlocks, hit_tokens: int, target_tokens: int)` — [`L466`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L466) — Whether free KV blocks cover ``kept`` running requests plus
  - <a id="SrptPrefillScheduler._next_waiting"></a>`_next_waiting(self)` — [`L381`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L381) — The request upstream's WAITING pass admits next.
  - <a id="SrptPrefillScheduler._plan_running"></a>`_plan_running(self, reqs: list[Request], lptt: int)` — [`L317`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L317) — Tokens the RUNNING pass of Scheduler.schedule() would give ``reqs``,
  - <a id="SrptPrefillScheduler._select_chunks_to_hold"></a>`_select_chunks_to_hold(self)` — [`L401`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L401) — Return ``(chunks_to_hold, target_waiting_request)``. — documented in [tpu-schedulers](../../../../../concepts/tpu-schedulers.md)
  - <a id="SrptPrefillScheduler._tokens_to_next_tile"></a>`_tokens_to_next_tile(self, context: int)` — [`L223`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L223) — Tokens from ``context`` to the next multiple of the attention tile.
  - <a id="SrptPrefillScheduler.blocks_for"></a>`blocks_for(request: Request, computed_tokens: int, num_new_tokens: int, computed_blocks: tuple)` — [`L481`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L481)
  - <a id="SrptPrefillScheduler.schedule"></a>`schedule(self, throttle_prefills: bool = False)` — [`L124`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L124) — documented in [tpu-schedulers](../../../../../concepts/tpu-schedulers.md)
  - <a id="SrptPrefillScheduler.update_from_output"></a>`update_from_output(self, scheduler_output: SchedulerOutput, model_runner_output: ModelRunnerOutput)` — [`L189`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L189)
  - <a id="SrptPrefillScheduler.attn_tile_tokens"></a>`attn_tile_tokens` — [`L102`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L102)
  - <a id="SrptPrefillScheduler.attn_work_cap"></a>`attn_work_cap` — [`L101`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L101)
  - <a id="SrptPrefillScheduler.max_consecutive_holds"></a>`max_consecutive_holds` — [`L95`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L95)
- protocol/private: <a id="SrptPrefillScheduler.__init__"></a>`__init__`[`L93`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L93), <a id="SrptPrefillScheduler._attn_cap_on"></a>`_attn_cap_on`[`L106`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L106), <a id="SrptPrefillScheduler._attn_cap_on_steps"></a>`_attn_cap_on_steps`[`L114`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L114), <a id="SrptPrefillScheduler._attn_capped"></a>`_attn_capped`[`L112`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L112), <a id="SrptPrefillScheduler._attn_capped_chunks"></a>`_attn_capped_chunks`[`L115`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L115), <a id="SrptPrefillScheduler._attn_prefill_scheduled"></a>`_attn_prefill_scheduled`[`L111`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L111), <a id="SrptPrefillScheduler._attn_steps"></a>`_attn_steps`[`L113`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L113), <a id="SrptPrefillScheduler._attn_work"></a>`_attn_work`[`L110`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L110), <a id="SrptPrefillScheduler._hold_backoff"></a>`_hold_backoff`[`L100`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L100), <a id="SrptPrefillScheduler._in_schedule"></a>`_in_schedule`[`L109`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L109), <a id="SrptPrefillScheduler._is_stalled"></a>`_is_stalled`[`L262`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L262), <a id="SrptPrefillScheduler._long_prefill_threshold"></a>`_long_prefill_threshold`[`L301`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L301), <a id="SrptPrefillScheduler._order_running"></a>`_order_running`[`L267`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L267), <a id="SrptPrefillScheduler._other_rank_decoding"></a>`_other_rank_decoding`[`L105`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L105), <a id="SrptPrefillScheduler._prefix_hit"></a>`_prefix_hit`[`L392`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L392), <a id="SrptPrefillScheduler._prune_hold_state"></a>`_prune_hold_state`[`L275`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L275), <a id="SrptPrefillScheduler._record_hold_outcome"></a>`_record_hold_outcome`[`L288`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L288), <a id="SrptPrefillScheduler._remaining"></a>`_remaining`[`L259`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L259), <a id="SrptPrefillScheduler._reserve_prefill_lookahead"></a>`_reserve_prefill_lookahead`[`L227`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L227), <a id="SrptPrefillScheduler._stalled_steps"></a>`_stalled_steps`[`L98`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L98)
- uses (calls/refs, reference-scoped): [`logger`](srpt_prefill_scheduler.md#logger), [`VLLM_TPU_SRPT_ATTN_WORK_CAP`](../../envs.md#VLLM_TPU_SRPT_ATTN_WORK_CAP), [`VLLM_TPU_SRPT_ATTN_TILE_TOKENS`](../../envs.md#VLLM_TPU_SRPT_ATTN_TILE_TOKENS), [`VLLM_TPU_SRPT_MAX_CONSECUTIVE_HOLDS`](../../envs.md#VLLM_TPU_SRPT_MAX_CONSECUTIVE_HOLDS), [`_ATTN_CAP_LOG_EVERY`](srpt_prefill_scheduler.md#_ATTN_CAP_LOG_EVERY), [`_MAX_BACKOFF_SHIFT`](srpt_prefill_scheduler.md#_MAX_BACKOFF_SHIFT)

## Module values
- <a id="_ATTN_CAP_LOG_EVERY"></a>`_ATTN_CAP_LOG_EVERY` — [`L86`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L86)
- <a id="_MAX_BACKOFF_SHIFT"></a>`_MAX_BACKOFF_SHIFT` — [`L85`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L85)
- <a id="logger"></a>`logger` — [`L83`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/experimental/srpt_prefill_scheduler.py#L83)

