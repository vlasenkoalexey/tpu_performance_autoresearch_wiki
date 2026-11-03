---
title: 'Module: src/vllm_torchtpu/core/pp_lazy_step.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/core/pp_lazy_step.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.core.pp_lazy_step`/
symbols:
  LazyPushStepper._dispatch: LazyPushStepper#_dispatch().
  LazyPushStepper.step: LazyPushStepper#step().
  LazyPushStepper._push_due: LazyPushStepper#_push_due().
  LazyPushStepper._settle: LazyPushStepper#_settle().
  LazyPushStepper._sampled: LazyPushStepper#_sampled().
  patch_engine_core_for_lazy_push.__init__: patch_engine_core_for_lazy_push().__init__().
  LazyPushStepper._handoff: LazyPushStepper#_handoff().
  LazyPushStepper._process: LazyPushStepper#_process().
  LazyPushStepper._push: LazyPushStepper#_push().
  LazyPushStepper.in_flight: LazyPushStepper#in_flight.
  patch_engine_core_for_lazy_push: patch_engine_core_for_lazy_push().
  LazyPushStepper.wave: LazyPushStepper#wave.
  LazyPushStepper.slots: LazyPushStepper#slots.
  LazyPushStepper.stages: LazyPushStepper#stages.
  LazyPushStepper._add_slot: LazyPushStepper#_add_slot().
  LazyPushStepper._others: LazyPushStepper#_others().
  LazyPushStepper._started_last: LazyPushStepper#_started_last().
  LazyPushStepper._finished: LazyPushStepper#_finished().
  LazyPushStepper._drain: LazyPushStepper#_drain().
  LazyPushStepper.executor: LazyPushStepper#executor.
  _Slot: _Slot#
  LazyPushStepper.first_slot: LazyPushStepper#first_slot.
  LazyPushStepper._real_in_flight: LazyPushStepper#_real_in_flight().
  logger: logger.
  LazyPushStepper.measured: LazyPushStepper#measured.
  _Step: _Step#
  LazyPushStepper.ratio: LazyPushStepper#ratio.
  _banded: _banded().
  _Step.slot: _Step#slot.
  LazyPushStepper.socket: LazyPushStepper#socket.
  _Slot.started_last: _Slot#started_last.
  _Step.future: _Step#future.
  _carries_state: _carries_state().
  _patch_collective_rpc: _patch_collective_rpc().
  _patch_collective_rpc.collective_rpc: _patch_collective_rpc().collective_rpc().
  _Step.scheduler_output: _Step#scheduler_output.
  LazyPushStepper.core: LazyPushStepper#core.
  LazyPushStepper.drains: LazyPushStepper#drains.
  _MEASURE_WEIGHT: _MEASURE_WEIGHT.
  _MEASURE_BAND: _MEASURE_BAND.
  _Slot.dispatched: _Slot#dispatched.
  _Slot.expected: _Slot#expected.
  _Slot.modelled_ms: _Slot#modelled_ms.
  _Slot.started_drain: _Slot#started_drain.
  LazyPushStepper.modelled: LazyPushStepper#modelled.
  LazyPushStepper.last_real: LazyPushStepper#last_real.
  LazyPushStepper.dropped: LazyPushStepper#dropped.
  _PUSH_DELAY: _PUSH_DELAY.
  _STEP_METHODS: _STEP_METHODS.
  _STATELESS_FIELDS: _STATELESS_FIELDS.
  _Step.exec_future: _Step#exec_future.
  _Step.dispatched: _Step#dispatched.
  LazyPushStepper: LazyPushStepper#
  LazyPushStepper.timeout: LazyPushStepper#timeout.
  _lazy_push_blocker: _lazy_push_blocker().
  LazyPushStepper.__init__: LazyPushStepper#__init__().
---
# Module: [`src/vllm_torchtpu/core/pp_lazy_step.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py)

## Classes
### <a id="LazyPushStepper"></a>`LazyPushStepper`
- def: [`src/vllm_torchtpu/core/pp_lazy_step.py:138`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L138)
- doc: One engine core's step loop; see the module docstring.
- signature: `class LazyPushStepper:`
- members:
  - <a id="LazyPushStepper._add_slot"></a>`_add_slot(self, slot: _Slot)` — [`L322`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L322) — Appends a slot and drops any older than the ``stages`` newest, — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="LazyPushStepper._dispatch"></a>`_dispatch(self)` — [`L238`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L238) — Schedules a step and dispatches it unless it holds nothing for — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="LazyPushStepper._drain"></a>`_drain(self)` — [`L196`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L196) — Reads every reply that has arrived, oldest call first; waits for — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="LazyPushStepper._handoff"></a>`_handoff(self, k: int)` — [`L330`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L330) — When hand-off ``k`` of the burst happened: read from the last — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="LazyPushStepper._others"></a>`_others(self, k: int)` — [`L345`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L345) — The longest expected forward stages 1 and up run between — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="LazyPushStepper._push_due"></a>`_push_due(self)` — [`L287`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L287) — Whether to push the burst's next step now: a step with tokens — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="LazyPushStepper._sampled"></a>`_sampled(self, slot: _Slot)` — [`L358`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L358) — Measures the step's forward on the last stage, from its start to — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="LazyPushStepper.step"></a>`step(self)` — [`L165`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L165) — Reads the replies that arrived, processes the oldest step if it — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="LazyPushStepper.core"></a>`core` — [`L142`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L142)
  - <a id="LazyPushStepper.drains"></a>`drains` — [`L162`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L162)
  - <a id="LazyPushStepper.dropped"></a>`dropped` — [`L163`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L163)
  - <a id="LazyPushStepper.executor"></a>`executor` — [`L143`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L143)
  - <a id="LazyPushStepper.first_slot"></a>`first_slot` — [`L156`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L156)
  - <a id="LazyPushStepper.in_flight"></a>`in_flight` — [`L152`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L152) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="LazyPushStepper.last_real"></a>`last_real` — [`L157`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L157)
  - <a id="LazyPushStepper.measured"></a>`measured` — [`L161`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L161)
  - <a id="LazyPushStepper.modelled"></a>`modelled` — [`L150`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L150)
  - <a id="LazyPushStepper.ratio"></a>`ratio` — [`L160`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L160)
  - <a id="LazyPushStepper.slots"></a>`slots` — [`L155`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L155) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="LazyPushStepper.socket"></a>`socket` — [`L146`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L146)
  - <a id="LazyPushStepper.stages"></a>`stages` — [`L145`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L145) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="LazyPushStepper.timeout"></a>`timeout` — [`L149`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L149)
  - <a id="LazyPushStepper.wave"></a>`wave` — [`L144`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L144) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
- protocol/private: <a id="LazyPushStepper.__init__"></a>`__init__`[`L141`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L141), <a id="LazyPushStepper._finished"></a>`_finished`[`L213`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L213), <a id="LazyPushStepper._process"></a>`_process`[`L216`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L216), <a id="LazyPushStepper._push"></a>`_push`[`L316`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L316), <a id="LazyPushStepper._real_in_flight"></a>`_real_in_flight`[`L193`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L193), <a id="LazyPushStepper._settle"></a>`_settle`[`L302`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L302), <a id="LazyPushStepper._started_last"></a>`_started_last`[`L354`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L354)
- uses (calls/refs, reference-scoped): [`settle`](../distributed/pp_push.md#_WaveState.settle), [`push`](../distributed/pp_push.md#_WaveState.push), [`pushes`](../distributed/pp_push.md#_WaveState.pushes), [`wave_state`](../distributed/pp_push.md#wave_state), [`_Slot`](pp_lazy_step.md#_Slot), [`open`](../distributed/pp_push.md#_WaveState.open), [`logger`](pp_lazy_step.md#logger), [`_Step`](pp_lazy_step.md#_Step), [`real_steps`](../distributed/pp_push.md#_WaveState.real_steps), [`settles`](../distributed/pp_push.md#_WaveState.settles), [`_banded`](pp_lazy_step.md#_banded), [`slot`](pp_lazy_step.md#_Step.slot), [`future`](pp_lazy_step.md#_Step.future), [`started_last`](pp_lazy_step.md#_Slot.started_last), [`_carries_state`](pp_lazy_step.md#_carries_state), [`scheduler_output`](pp_lazy_step.md#_Step.scheduler_output), [`_MEASURE_WEIGHT`](pp_lazy_step.md#_MEASURE_WEIGHT), [`dispatched`](pp_lazy_step.md#_Slot.dispatched), [`expected`](pp_lazy_step.md#_Slot.expected), [`modelled_ms`](pp_lazy_step.md#_Slot.modelled_ms), [`stages`](../distributed/pp_push.md#_WaveState.stages), [`started_drain`](pp_lazy_step.md#_Slot.started_drain), [`_PUSH_DELAY`](pp_lazy_step.md#_PUSH_DELAY), [`dispatched`](pp_lazy_step.md#_Step.dispatched), [`exec_future`](pp_lazy_step.md#_Step.exec_future)
- used by: [`__init__`](pp_lazy_step.md#patch_engine_core_for_lazy_push.__init__)

### <a id="_Slot"></a>`_Slot`
- def: [`src/vllm_torchtpu/core/pp_lazy_step.py:110`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L110)
- doc: One step of the burst on its way through the pipeline, pushes
- signature: `class _Slot:`
- members:
  - <a id="_Slot.dispatched"></a>`dispatched` — [`L114`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L114)
  - <a id="_Slot.expected"></a>`expected` — [`L116`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L116)
  - <a id="_Slot.modelled_ms"></a>`modelled_ms` — [`L118`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L118)
  - <a id="_Slot.started_drain"></a>`started_drain` — [`L122`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L122)
  - <a id="_Slot.started_last"></a>`started_last` — [`L121`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L121)
- used by: [`_dispatch`](pp_lazy_step.md#LazyPushStepper._dispatch), [`_sampled`](pp_lazy_step.md#LazyPushStepper._sampled), [`_handoff`](pp_lazy_step.md#LazyPushStepper._handoff), [`_push`](pp_lazy_step.md#LazyPushStepper._push), [`slots`](pp_lazy_step.md#LazyPushStepper.slots), [`_add_slot`](pp_lazy_step.md#LazyPushStepper._add_slot), [`_others`](pp_lazy_step.md#LazyPushStepper._others), [`_started_last`](pp_lazy_step.md#LazyPushStepper._started_last), [`slot`](pp_lazy_step.md#_Step.slot)

### <a id="_Step"></a>`_Step`
- def: [`src/vllm_torchtpu/core/pp_lazy_step.py:126`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L126)
- doc: A dispatched scheduler step whose result the engine has not read.
- signature: `class _Step:`
- members:
  - <a id="_Step.dispatched"></a>`dispatched` — [`L133`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L133)
  - <a id="_Step.exec_future"></a>`exec_future` — [`L130`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L130)
  - <a id="_Step.future"></a>`future` — [`L132`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L132)
  - <a id="_Step.scheduler_output"></a>`scheduler_output` — [`L129`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L129)
  - <a id="_Step.slot"></a>`slot` — [`L135`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L135)
- uses (calls/refs, reference-scoped): [`_Slot`](pp_lazy_step.md#_Slot)
- used by: [`_dispatch`](pp_lazy_step.md#LazyPushStepper._dispatch), [`_push_due`](pp_lazy_step.md#LazyPushStepper._push_due), [`_process`](pp_lazy_step.md#LazyPushStepper._process), [`in_flight`](pp_lazy_step.md#LazyPushStepper.in_flight), [`_finished`](pp_lazy_step.md#LazyPushStepper._finished), [`_real_in_flight`](pp_lazy_step.md#LazyPushStepper._real_in_flight)

## Functions
- <a id="patch_engine_core_for_lazy_push.__init__"></a>`__init__(self, *args, **kwargs)` — [`L464`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L464) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
- <a id="_banded"></a>`_banded(value: float, estimate: float)` — [`L105`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L105)
- <a id="_carries_state"></a>`_carries_state(scheduler_output: Any)` — [`L92`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L92) — Whether a step without tokens changes the workers' state: finished
- <a id="_lazy_push_blocker"></a>`_lazy_push_blocker(core: Any, vllm_config: Any)` — [`L403`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L403) — Why this engine core keeps vLLM's step loop, None if it need not.
- <a id="_patch_collective_rpc"></a>`_patch_collective_rpc()` — [`L377`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L377) — Have every lazy-push executor settle before a call that is not part
- <a id="_patch_collective_rpc.collective_rpc"></a>`collective_rpc(self, method, *args, **kwargs)` — [`L387`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L387)
- <a id="patch_engine_core_for_lazy_push"></a>`patch_engine_core_for_lazy_push(vllm_config: Any)` — [`L440`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L440) — Have every engine core of a pipeline deeper than two stages run — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)

## Module values
- <a id="_MEASURE_BAND"></a>`_MEASURE_BAND` — [`L77`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L77)
- <a id="_MEASURE_WEIGHT"></a>`_MEASURE_WEIGHT` — [`L76`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L76)
- <a id="_PUSH_DELAY"></a>`_PUSH_DELAY` — [`L73`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L73)
- <a id="_STATELESS_FIELDS"></a>`_STATELESS_FIELDS` — [`L83`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L83)
- <a id="_STEP_METHODS"></a>`_STEP_METHODS` — [`L80`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L80)
- <a id="logger"></a>`logger` — [`L69`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_lazy_step.py#L69)

