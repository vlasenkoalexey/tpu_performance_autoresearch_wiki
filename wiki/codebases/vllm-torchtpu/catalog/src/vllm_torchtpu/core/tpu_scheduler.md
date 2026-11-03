---
title: 'Module: src/vllm_torchtpu/core/tpu_scheduler.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/core/tpu_scheduler.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.core.tpu_scheduler`/
symbols:
  TpuDpScheduler._drain_prefill: TpuDpScheduler#_drain_prefill.
  TpuDpScheduler.schedule: TpuDpScheduler#schedule().
  TpuDpScheduler._pause_state: TpuDpScheduler#_pause_state.
  TpuDpScheduler._schedule_paused_new: TpuDpScheduler#_schedule_paused_new().
  logger: logger.
  TpuDpScheduler: TpuDpScheduler#
  TpuDpScheduler.__init__: TpuDpScheduler#__init__().
  TpuDpScheduler.prefill_capacity_bound: TpuDpScheduler#prefill_capacity_bound.
---
# Module: [`src/vllm_torchtpu/core/tpu_scheduler.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/tpu_scheduler.py)

## Classes
### <a id="TpuDpScheduler"></a>`TpuDpScheduler`
- def: [`src/vllm_torchtpu/core/tpu_scheduler.py:22`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/tpu_scheduler.py#L22)
- doc: Scheduler that aligns prefill admission across DP ranks.
- signature: `class TpuDpScheduler(AsyncScheduler):`
- members:
  - <a id="TpuDpScheduler._schedule_paused_new"></a>`_schedule_paused_new(self)` — [`L35`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/tpu_scheduler.py#L35) — Run one step while keeping newly prefills buffered.
  - <a id="TpuDpScheduler.schedule"></a>`schedule(self, throttle_prefills: bool = False)` — [`L45`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/tpu_scheduler.py#L45)
  - <a id="TpuDpScheduler.prefill_capacity_bound"></a>`prefill_capacity_bound` — [`L46`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/tpu_scheduler.py#L46)
- protocol/private: <a id="TpuDpScheduler.__init__"></a>`__init__`[`L30`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/tpu_scheduler.py#L30), <a id="TpuDpScheduler._drain_prefill"></a>`_drain_prefill`[`L32`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/tpu_scheduler.py#L32), <a id="TpuDpScheduler._pause_state"></a>`_pause_state`[`L39`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/tpu_scheduler.py#L39)
- uses (calls/refs, reference-scoped): [`logger`](tpu_scheduler.md#logger)

## Module values
- <a id="logger"></a>`logger` — [`L19`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/tpu_scheduler.py#L19)

