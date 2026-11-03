---
title: 'Module: src/vllm_torchtpu/distributed/pp_push.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/pp_push.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.pp_push`/
symbols:
  _WaveState.before_waiting: _WaveState#before_waiting().
  _PushFuture._before_waiting: _PushFuture#_before_waiting().
  patch_executor_for_pp_ring: patch_executor_for_pp_ring().
  patch_executor_for_pp_wave: patch_executor_for_pp_wave().
  patch_executor_for_pp_wave.execute_model: patch_executor_for_pp_wave().execute_model().
  patch_executor_for_pp_wave.sample_tokens: patch_executor_for_pp_wave().sample_tokens().
  ring_handoff: ring_handoff().
  _WaveState.settle: _WaveState#settle().
  widen_message_rings: widen_message_rings().
  patch_executor_for_pp_handoff: patch_executor_for_pp_handoff().
  _WaveState.dispatched: _WaveState#dispatched().
  _WaveState.push: _WaveState#push().
  _widen_rpc_ring: _widen_rpc_ring().
  _WaveState.pushes: _WaveState#pushes.
  _WaveState.steps: _WaveState#steps.
  _PushFuture._inner: _PushFuture#_inner.
  wave_state: wave_state().
  _WaveState.open: _WaveState#open.
  _PushFuture.result: _PushFuture#result().
  _ring_chunks_needed: _ring_chunks_needed.
  _WaveState.settles: _WaveState#settles.
  _WaveState.real_steps: _WaveState#real_steps.
  logger: logger.
  _PushFuture.exception: _PushFuture#exception().
  _install_take_draft_token_ids: _install_take_draft_token_ids().
  _rides_the_wave: _rides_the_wave().
  _raise_steps_in_flight: _raise_steps_in_flight().
  ring_extra_steps: ring_extra_steps().
  _widen_rpc_ring.__init__: _widen_rpc_ring().__init__().
  _WaveState.lazy: _WaveState#lazy.
  _WaveState: _WaveState#
  _WaveState.last_step: _WaveState#last_step.
  _PushFuture.__init__: _PushFuture#__init__().
  _PushFuture.done: _PushFuture#done().
  _PushFuture.running: _PushFuture#running().
  _PushFuture.cancelled: _PushFuture#cancelled().
  _PushFuture.cancel: _PushFuture#cancel().
  _PushFuture.add_done_callback: _PushFuture#add_done_callback().
  _WaveState.stages: _WaveState#stages.
  _PushFuture: _PushFuture#
  _PushFuture._wave: _PushFuture#_wave.
  _PushFuture._executor: _PushFuture#_executor.
  _PushFuture._step: _PushFuture#_step.
  _PushFuture._real_step: _PushFuture#_real_step.
  rpc_ring_chunks: rpc_ring_chunks().
  _install_take_draft_token_ids.take_draft_token_ids: _install_take_draft_token_ids().take_draft_token_ids().
  _raise_steps_in_flight.max_concurrent_batches: _raise_steps_in_flight().max_concurrent_batches().
  _WaveState.__init__: _WaveState#__init__().
---
# Module: [`src/vllm_torchtpu/distributed/pp_push.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py)

## Classes
### <a id="_PushFuture"></a>`_PushFuture`  ·  implements/extends Future
- def: [`src/vllm_torchtpu/distributed/pp_push.py:166`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L166)
- doc: The result of one forward or sampling call.
- signature: `class _PushFuture(Future):`
- members:
  - <a id="_PushFuture.add_done_callback"></a>`add_done_callback(self, fn)` — [`L214`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L214)
  - <a id="_PushFuture.cancel"></a>`cancel(self)` — [`L211`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L211)
  - <a id="_PushFuture.cancelled"></a>`cancelled(self)` — [`L208`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L208)
  - <a id="_PushFuture.done"></a>`done(self)` — [`L202`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L202)
  - <a id="_PushFuture.exception"></a>`exception(self, timeout=None)` — [`L194`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L194)
  - <a id="_PushFuture.result"></a>`result(self, timeout=None)` — [`L190`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L190)
  - <a id="_PushFuture.running"></a>`running(self)` — [`L205`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L205)
- protocol/private: <a id="_PushFuture.__init__"></a>`__init__`[`L176`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L176), <a id="_PushFuture._before_waiting"></a>`_before_waiting`[`L186`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L186), <a id="_PushFuture._executor"></a>`_executor`[`L181`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L181), <a id="_PushFuture._inner"></a>`_inner`[`L180`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L180), <a id="_PushFuture._real_step"></a>`_real_step`[`L184`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L184), <a id="_PushFuture._step"></a>`_step`[`L183`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L183), <a id="_PushFuture._wave"></a>`_wave`[`L182`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L182)
- uses (calls/refs, reference-scoped): [`before_waiting`](pp_push.md#_WaveState.before_waiting), [`_WaveState`](pp_push.md#_WaveState), [`lazy`](pp_push.md#_WaveState.lazy)
- used by: [`execute_model`](pp_push.md#patch_executor_for_pp_wave.execute_model), [`sample_tokens`](pp_push.md#patch_executor_for_pp_wave.sample_tokens)

### <a id="_WaveState"></a>`_WaveState`
- def: [`src/vllm_torchtpu/distributed/pp_push.py:78`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L78)
- doc: One executor's count of the steps it dispatched to the pipeline.
- signature: `class _WaveState:`
- members:
  - <a id="_WaveState.before_waiting"></a>`before_waiting(self, executor: Any, step: int, real_step: int)` — [`L132`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L132) — Send what carries ``step`` to the last stage before the engine
  - <a id="_WaveState.dispatched"></a>`dispatched(self)` — [`L96`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L96) — Records a scheduler step and returns its number.
  - <a id="_WaveState.push"></a>`push(self, executor: Any)` — [`L104`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L104) — Sends one ``pp_push`` and returns its step number and the last
  - <a id="_WaveState.settle"></a>`settle(self, executor: Any)` — [`L116`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L116) — Sends the ``pp_settle`` that closes the burst and returns the last
  - <a id="_WaveState.last_step"></a>`last_step` — [`L86`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L86)
  - <a id="_WaveState.lazy"></a>`lazy` — [`L94`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L94)
  - <a id="_WaveState.open"></a>`open` — [`L90`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L90)
  - <a id="_WaveState.pushes"></a>`pushes` — [`L91`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L91)
  - <a id="_WaveState.real_steps"></a>`real_steps` — [`L88`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L88)
  - <a id="_WaveState.settles"></a>`settles` — [`L92`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L92)
  - <a id="_WaveState.stages"></a>`stages` — [`L82`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L82)
  - <a id="_WaveState.steps"></a>`steps` — [`L85`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L85)
- protocol/private: <a id="_WaveState.__init__"></a>`__init__`[`L81`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L81)
- uses (calls/refs, reference-scoped): [`logger`](pp_push.md#logger)
- used by: [`_dispatch`](../core/pp_lazy_step.md#LazyPushStepper._dispatch), [`step`](../core/pp_lazy_step.md#LazyPushStepper.step), [`__init__`](../core/pp_lazy_step.md#patch_engine_core_for_lazy_push.__init__), [`_settle`](../core/pp_lazy_step.md#LazyPushStepper._settle), [`_before_waiting`](pp_push.md#_PushFuture._before_waiting), [`_push`](../core/pp_lazy_step.md#LazyPushStepper._push), [`execute_model`](pp_push.md#patch_executor_for_pp_wave.execute_model), [`sample_tokens`](pp_push.md#patch_executor_for_pp_wave.sample_tokens), [`stages`](../core/pp_lazy_step.md#LazyPushStepper.stages), [`wave_state`](pp_push.md#wave_state), [`__init__`](pp_push.md#_PushFuture.__init__)

## Functions
- <a id="_widen_rpc_ring.__init__"></a>`__init__(self, n_reader, n_local_reader, *args, **kwargs)` — [`L275`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L275)
- <a id="_install_take_draft_token_ids"></a>`_install_take_draft_token_ids(executor_cls: Any)` — [`L311`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L311) — Have a pipeline executor's ``take_draft_token_ids`` return None
- <a id="_raise_steps_in_flight"></a>`_raise_steps_in_flight(extra: int)` — [`L344`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L344) — Have ``VllmConfig.max_concurrent_batches`` count ``extra`` more steps
- <a id="_rides_the_wave"></a>`_rides_the_wave(executor: Any)` — [`L337`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L337) — Whether an executor's steps go through the wave: a pipeline whose
- <a id="_widen_rpc_ring"></a>`_widen_rpc_ring(stages: int, extra: int = 0)` — [`L261`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L261) — Give every ``MessageQueue`` created from now on, the engine's
- <a id="patch_executor_for_pp_wave.execute_model"></a>`execute_model(self, scheduler_output, non_block=False)` — [`L437`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L437) — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="_raise_steps_in_flight.max_concurrent_batches"></a>`max_concurrent_batches(self: Any)` — [`L362`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L362)
- <a id="patch_executor_for_pp_handoff"></a>`patch_executor_for_pp_handoff(vllm_config: Any)` — [`L380`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L380) — Install the engine side of the hand-off ``TPU_PP_HANDOFF`` selects. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="patch_executor_for_pp_ring"></a>`patch_executor_for_pp_ring(vllm_config: Any)` — [`L388`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L388) — Install the ring hand-off's engine side: the extra steps in flight, — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="patch_executor_for_pp_wave"></a>`patch_executor_for_pp_wave(vllm_config: Any)` — [`L417`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L417) — Install the push, the settle and the wider ring buffer on — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="ring_extra_steps"></a>`ring_extra_steps(stages: int)` — [`L229`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L229) — Steps the engine keeps in flight beyond the stage count under the
- <a id="ring_handoff"></a>`ring_handoff()` — [`L303`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L303) — Whether pipeline stages hand forwards on point to point (``pp_ring``) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
- <a id="rpc_ring_chunks"></a>`rpc_ring_chunks(stages: int, extra: int = 0)` — [`L244`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L244) — Messages each ring buffer between the engine and its workers must hold.
- <a id="patch_executor_for_pp_wave.sample_tokens"></a>`sample_tokens(self, grammar_output, non_block=False)` — [`L450`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L450) — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="_install_take_draft_token_ids.take_draft_token_ids"></a>`take_draft_token_ids(self: Any)` — [`L328`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L328)
- <a id="wave_state"></a>`wave_state(executor: Any)` — [`L218`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L218) — The executor's step count, created on first use.
- <a id="widen_message_rings"></a>`widen_message_rings(vllm_config: Any)` — [`L285`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L285) — Widen the message rings this process will create for a pipeline.

## Module values
- <a id="_ring_chunks_needed"></a>`_ring_chunks_needed` — [`L258`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L258)
- <a id="logger"></a>`logger` — [`L75`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_push.py#L75)

