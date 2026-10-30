---
title: 'Module: torchtitan/experiments/rl/components/work_buffer.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/components/work_buffer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.components.work_buffer`/
symbols:
  RolloutGroupWorkBuffer.take_finalized: RolloutGroupWorkBuffer#take_finalized().
  RolloutGroupWorkBuffer.metrics: RolloutGroupWorkBuffer#metrics().
  RolloutGroupWorkBuffer.claim_next: RolloutGroupWorkBuffer#claim_next().
  RolloutGroupWorkBuffer.finalize_work: RolloutGroupWorkBuffer#finalize_work().
  RolloutGroupWorkBuffer.add_work: RolloutGroupWorkBuffer#add_work().
  RolloutGroupWorkBuffer: RolloutGroupWorkBuffer#
  RolloutGroupWorkBuffer._condition: RolloutGroupWorkBuffer#_condition.
  RolloutGroupWorkBuffer._work_by_group_id: RolloutGroupWorkBuffer#_work_by_group_id.
  RolloutGroupWorkBuffer.Config: RolloutGroupWorkBuffer#Config#
  RolloutGroupWork.state: RolloutGroupWork#state.
  RolloutGroupWorkBuffer.wait_for_slot: RolloutGroupWorkBuffer#wait_for_slot().
  RolloutGroupWorkBuffer.release_active_groups: RolloutGroupWorkBuffer#release_active_groups().
  RolloutGroupWork: RolloutGroupWork#
  RolloutGroupWork.group_id: RolloutGroupWork#group_id.
  RolloutGroupWorkBuffer._active_rollout_groups: RolloutGroupWorkBuffer#_active_rollout_groups.
  RolloutGroupWorkBuffer.close: RolloutGroupWorkBuffer#close().
  _RolloutGroupWorkState: _RolloutGroupWorkState#
  RolloutGroupWorkBuffer._has_active_slot_available: RolloutGroupWorkBuffer#_has_active_slot_available().
  RolloutGroupWork.sample: RolloutGroupWork#sample.
  RolloutGroupWorkBuffer._closed: RolloutGroupWorkBuffer#_closed.
  RolloutGroupWork.rollout_group: RolloutGroupWork#rollout_group.
  RolloutGroupWorkBuffer._active_rollout_groups_peak_since_flush: RolloutGroupWorkBuffer#_active_rollout_groups_peak_since_flush.
  _RolloutGroupWorkState.WAITING: _RolloutGroupWorkState#WAITING.
  _RolloutGroupWorkState.FINALIZED: _RolloutGroupWorkState#FINALIZED.
  RolloutGroupWorkBuffer.__init__: RolloutGroupWorkBuffer#__init__().
  _RolloutGroupWorkState.INFLIGHT: _RolloutGroupWorkState#INFLIGHT.
  RolloutGroupWorkBuffer._max_active_rollout_groups: RolloutGroupWorkBuffer#_max_active_rollout_groups.
  RolloutGroupWorkBuffer._window_size: RolloutGroupWorkBuffer#_window_size.
---
# Module: [`torchtitan/experiments/rl/components/work_buffer.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py)

## Classes
### <a id="RolloutGroupWork"></a>`RolloutGroupWork`
- def: [`torchtitan/experiments/rl/components/work_buffer.py:32`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L32)
- doc: One prompt group's work, tracked through _RolloutGroupWorkState.
- signature: `class RolloutGroupWork:`
- members:
  - <a id="RolloutGroupWork.group_id"></a>`group_id` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L39)
  - <a id="RolloutGroupWork.rollout_group"></a>`rollout_group` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L46)
  - <a id="RolloutGroupWork.sample"></a>`sample` — [`L40`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L40) — ---
  - <a id="RolloutGroupWork.state"></a>`state` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L43)
- uses (calls/refs, reference-scoped): [`RolloutGroup`](../rollout/types.md#RolloutGroup), [`_RolloutGroupWorkState`](work_buffer.md#_RolloutGroupWorkState), [`WAITING`](work_buffer.md#_RolloutGroupWorkState.WAITING)
- used by: [`_rollout_loop`](../controller.md#Controller._rollout_loop), [`take_finalized`](work_buffer.md#RolloutGroupWorkBuffer.take_finalized), [`metrics`](work_buffer.md#RolloutGroupWorkBuffer.metrics), [`_data_input_loop`](../controller.md#Controller._data_input_loop), [`claim_next`](work_buffer.md#RolloutGroupWorkBuffer.claim_next), [`finalize_work`](work_buffer.md#RolloutGroupWorkBuffer.finalize_work), [`add_work`](work_buffer.md#RolloutGroupWorkBuffer.add_work), [`_work_by_group_id`](work_buffer.md#RolloutGroupWorkBuffer._work_by_group_id)  (3 test-only)

### <a id="RolloutGroupWorkBuffer"></a>`RolloutGroupWorkBuffer`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/components/work_buffer.py:54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L54)
- doc: Buffer of `RolloutGroupWork` shared between the data-input, rollout, and batcher loops.
- signature: `class RolloutGroupWorkBuffer(Configurable):`
- members:
  - <a id="RolloutGroupWorkBuffer.add_work"></a>`add_work(self, work: RolloutGroupWork)` — [`L136`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L136) — Admit one rollout group as WAITING and charge one active slot.
  - <a id="RolloutGroupWorkBuffer.claim_next"></a>`claim_next(self)` — [`L151`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L151) — Rollout loop: claim the oldest WAITING group (WAITING -> INFLIGHT). None once closed.
  - <a id="RolloutGroupWorkBuffer.close"></a>`close(self)` — [`L235`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L235) — run() shutdown calls this once. Sets `_closed`, drops buffered work, and wakes every waiter.
  - <a id="RolloutGroupWorkBuffer.finalize_work"></a>`finalize_work(self, rollout_group: RolloutGroup)` — [`L163`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L163) — Rollout loop: store the produced RolloutGroup on its work entry (INFLIGHT -> FINALIZED) and wake the batcher.
  - <a id="RolloutGroupWorkBuffer.metrics"></a>`metrics(self)` — [`L246`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L246) — Trainer loop: point-in-time buffer gauges for this step; resets the per-flush peak.
  - <a id="RolloutGroupWorkBuffer.release_active_groups"></a>`release_active_groups(self, count: int, *, reason: str)` — [`L208`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L208) — Free active slots: the trainer releases trained slots after its weight pull; the batcher
  - <a id="RolloutGroupWorkBuffer.take_finalized"></a>`take_finalized(self)` — [`L175`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L175) — Batcher loop: return the oldest FINALIZED group inside the anchored windowed FIFO range.
  - <a id="RolloutGroupWorkBuffer.wait_for_slot"></a>`wait_for_slot(self)` — [`L120`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L120) — Wait until one more rollout group may enter the active buffer.
- protocol/private: <a id="RolloutGroupWorkBuffer.__init__"></a>`__init__`[`L90`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L90), <a id="RolloutGroupWorkBuffer._active_rollout_groups"></a>`_active_rollout_groups`[`L101`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L101), <a id="RolloutGroupWorkBuffer._active_rollout_groups_peak_since_flush"></a>`_active_rollout_groups_peak_since_flush`[`L103`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L103), <a id="RolloutGroupWorkBuffer._closed"></a>`_closed`[`L113`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L113), <a id="RolloutGroupWorkBuffer._condition"></a>`_condition`[`L112`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L112), <a id="RolloutGroupWorkBuffer._has_active_slot_available"></a>`_has_active_slot_available`[`L117`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L117), <a id="RolloutGroupWorkBuffer._max_active_rollout_groups"></a>`_max_active_rollout_groups`[`L99`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L99), <a id="RolloutGroupWorkBuffer._window_size"></a>`_window_size`[`L100`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L100), <a id="RolloutGroupWorkBuffer._work_by_group_id"></a>`_work_by_group_id`[`L104`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L104)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Metric`](../observability/metrics/types.md#Metric), [`log_trace_span`](../../../observability/structured_logger/structured_logging.md#log_trace_span), [`NoReduce`](../observability/metrics/types.md#NoReduce), [`RolloutGroup`](../rollout/types.md#RolloutGroup), [`log_trace_scalar`](../../../observability/structured_logger/structured_logging.md#log_trace_scalar), [`group_id`](../rollout/types.md#RolloutGroup.group_id), [`Config`](work_buffer.md#RolloutGroupWorkBuffer.Config), [`state`](work_buffer.md#RolloutGroupWork.state), [`RolloutGroupWork`](work_buffer.md#RolloutGroupWork), [`group_id`](work_buffer.md#RolloutGroupWork.group_id), [`_RolloutGroupWorkState`](work_buffer.md#_RolloutGroupWorkState), [`rollout_group`](work_buffer.md#RolloutGroupWork.rollout_group), [`FINALIZED`](work_buffer.md#_RolloutGroupWorkState.FINALIZED), [`WAITING`](work_buffer.md#_RolloutGroupWorkState.WAITING), [`INFLIGHT`](work_buffer.md#_RolloutGroupWorkState.INFLIGHT)
- used by: [`Configurable`](../../../config/configurable.md#Configurable), [`_rollout_loop`](../controller.md#Controller._rollout_loop), [`_batcher_loop`](../controller.md#Controller._batcher_loop), [`_data_input_loop`](../controller.md#Controller._data_input_loop), [`_generator_pull_and_release_buffer_slots`](weight_sync.md#WeightSyncManager._generator_pull_and_release_buffer_slots), [`__init__`](weight_sync.md#WeightSyncManager.__init__), [`group_buffer`](../controller.md#AsyncLoopConfig.group_buffer)  (6 test-only)

### <a id="RolloutGroupWorkBuffer.Config"></a>`RolloutGroupWorkBuffer.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/components/work_buffer.py:87`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L87)
- doc: No tunables: capacity and window size are derived by the controller.
- signature: `class Config(Configurable.Config):`
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Config`](../../../config/configurable.md#Configurable.Config)
- used by: [`group_buffer`](../controller.md#AsyncLoopConfig.group_buffer), [`__init__`](work_buffer.md#RolloutGroupWorkBuffer.__init__)  (3 test-only)

### <a id="_RolloutGroupWorkState"></a>`_RolloutGroupWorkState`  ·  implements/extends Enum
- def: [`torchtitan/experiments/rl/components/work_buffer.py:23`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L23)
- doc: Where a RolloutGroupWork is in the WAITING -&gt; INFLIGHT -&gt; FINALIZED lifecycle.
- signature: `class _RolloutGroupWorkState(enum.Enum):`
- members:
  - <a id="_RolloutGroupWorkState.FINALIZED"></a>`FINALIZED` — [`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L28)
  - <a id="_RolloutGroupWorkState.INFLIGHT"></a>`INFLIGHT` — [`L27`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L27)
  - <a id="_RolloutGroupWorkState.WAITING"></a>`WAITING` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/work_buffer.py#L26)
- used by: [`take_finalized`](work_buffer.md#RolloutGroupWorkBuffer.take_finalized), [`metrics`](work_buffer.md#RolloutGroupWorkBuffer.metrics), [`claim_next`](work_buffer.md#RolloutGroupWorkBuffer.claim_next), [`finalize_work`](work_buffer.md#RolloutGroupWorkBuffer.finalize_work), [`state`](work_buffer.md#RolloutGroupWork.state)

