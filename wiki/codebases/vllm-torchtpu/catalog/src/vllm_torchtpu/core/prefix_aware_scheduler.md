---
title: 'Module: src/vllm_torchtpu/core/prefix_aware_scheduler.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/core/prefix_aware_scheduler.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.core.prefix_aware_scheduler`/
symbols:
  PrefixAwareScheduler._promote_warmest: PrefixAwareScheduler#_promote_warmest().
  PrefixAwareScheduler._rank_and_warmth: PrefixAwareScheduler#_rank_and_warmth().
  PrefixAwareScheduler._paw_scoring_broken: PrefixAwareScheduler#_paw_scoring_broken.
  PrefixAwareScheduler._prefix_warmth: PrefixAwareScheduler#_prefix_warmth().
  PrefixAwareScheduler._paw_n: PrefixAwareScheduler#_paw_n.
  logger: logger.
  PrefixAwareScheduler._paw_cold_tokens: PrefixAwareScheduler#_paw_cold_tokens.
  PrefixAwareScheduler._select_waiting_queue_for_scheduling: PrefixAwareScheduler#_select_waiting_queue_for_scheduling().
  PrefixAwareScheduler.schedule: PrefixAwareScheduler#schedule().
  PrefixAwareScheduler.WINDOW: PrefixAwareScheduler#WINDOW.
  PrefixAwareScheduler._paw_prompt_tokens: PrefixAwareScheduler#_paw_prompt_tokens.
  _LOG_EVERY: _LOG_EVERY.
  _TIER_PREEMPTED: _TIER_PREEMPTED.
  _TIER_NORMAL: _TIER_NORMAL.
  PrefixAwareScheduler: PrefixAwareScheduler#
  PrefixAwareScheduler.__init__: PrefixAwareScheduler#__init__().
---
# Module: [`src/vllm_torchtpu/core/prefix_aware_scheduler.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/prefix_aware_scheduler.py)

## Classes
### <a id="PrefixAwareScheduler"></a>`PrefixAwareScheduler`
- def: [`src/vllm_torchtpu/core/prefix_aware_scheduler.py:52`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/prefix_aware_scheduler.py#L52)
- doc: Admit ready requests prioritizing fewest uncached prompt tokens.
- signature: `class PrefixAwareScheduler(AsyncScheduler):`
- members:
  - <a id="PrefixAwareScheduler._prefix_warmth"></a>`_prefix_warmth(self, request: Request)` — [`L67`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/prefix_aware_scheduler.py#L67) — Prompt tokens of ``request`` resident in the KV cache.
  - <a id="PrefixAwareScheduler._promote_warmest"></a>`_promote_warmest(self, queue: RequestQueue)` — [`L112`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/prefix_aware_scheduler.py#L112) — Promote the request with the fewest uncached tokens within WINDOW. — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="PrefixAwareScheduler._rank_and_warmth"></a>`_rank_and_warmth(self, request: Request)` — [`L87`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/prefix_aware_scheduler.py#L87) — Return (sort_key, warmth). Lower sort_key is admitted first.
  - <a id="PrefixAwareScheduler.schedule"></a>`schedule(self, throttle_prefills: bool = False)` — [`L104`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/prefix_aware_scheduler.py#L104)
  - <a id="PrefixAwareScheduler.WINDOW"></a>`WINDOW` — [`L56`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/prefix_aware_scheduler.py#L56)
- protocol/private: <a id="PrefixAwareScheduler.__init__"></a>`__init__`[`L58`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/prefix_aware_scheduler.py#L58), <a id="PrefixAwareScheduler._paw_cold_tokens"></a>`_paw_cold_tokens`[`L61`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/prefix_aware_scheduler.py#L61), <a id="PrefixAwareScheduler._paw_n"></a>`_paw_n`[`L60`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/prefix_aware_scheduler.py#L60), <a id="PrefixAwareScheduler._paw_prompt_tokens"></a>`_paw_prompt_tokens`[`L62`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/prefix_aware_scheduler.py#L62), <a id="PrefixAwareScheduler._paw_scoring_broken"></a>`_paw_scoring_broken`[`L63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/prefix_aware_scheduler.py#L63), <a id="PrefixAwareScheduler._select_waiting_queue_for_scheduling"></a>`_select_waiting_queue_for_scheduling`[`L96`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/prefix_aware_scheduler.py#L96)
- uses (calls/refs, reference-scoped): [`logger`](prefix_aware_scheduler.md#logger), [`_LOG_EVERY`](prefix_aware_scheduler.md#_LOG_EVERY), [`_TIER_NORMAL`](prefix_aware_scheduler.md#_TIER_NORMAL), [`_TIER_PREEMPTED`](prefix_aware_scheduler.md#_TIER_PREEMPTED)

## Module values
- <a id="_LOG_EVERY"></a>`_LOG_EVERY` — [`L45`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/prefix_aware_scheduler.py#L45)
- <a id="_TIER_NORMAL"></a>`_TIER_NORMAL` — [`L49`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/prefix_aware_scheduler.py#L49)
- <a id="_TIER_PREEMPTED"></a>`_TIER_PREEMPTED` — [`L48`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/prefix_aware_scheduler.py#L48)
- <a id="logger"></a>`logger` — [`L43`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/prefix_aware_scheduler.py#L43)

