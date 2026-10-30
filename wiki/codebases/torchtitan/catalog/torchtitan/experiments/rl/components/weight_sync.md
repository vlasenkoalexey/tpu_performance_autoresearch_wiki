---
title: 'Module: torchtitan/experiments/rl/components/weight_sync.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/components/weight_sync.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.components.weight_sync`/
symbols:
  WeightSyncManager._generator_pull_and_release_buffer_slots: WeightSyncManager#_generator_pull_and_release_buffer_slots().
  WeightSyncManager.start_async_push_pull: WeightSyncManager#start_async_push_pull().
  WeightSyncManager.wait_prev_pull: WeightSyncManager#wait_prev_pull().
  WeightSyncManager.wait_prev_push: WeightSyncManager#wait_prev_push().
  WeightSyncManager._trainer_push: WeightSyncManager#_trainer_push().
  WeightSyncManager.__init__: WeightSyncManager#__init__().
  WeightSyncManager._generator_pull_task: WeightSyncManager#_generator_pull_task.
  WeightSyncManager.wait_inflight_push_pull: WeightSyncManager#wait_inflight_push_pull().
  WeightSyncManager._trainer_push_task: WeightSyncManager#_trainer_push_task.
  WeightSyncManager: WeightSyncManager#
  _noop: _noop().
  WeightSyncManager._last_push_s: WeightSyncManager#_last_push_s.
  WeightSyncManager._last_pull_s: WeightSyncManager#_last_pull_s.
  WeightSyncManager._trainer: WeightSyncManager#_trainer.
  WeightSyncManager._generator_router: WeightSyncManager#_generator_router.
  WeightSyncManager._group_buffer: WeightSyncManager#_group_buffer.
  WeightSyncManager._num_prompts_per_train_step: WeightSyncManager#_num_prompts_per_train_step.
---
# Module: [`torchtitan/experiments/rl/components/weight_sync.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py)

## Classes
### <a id="WeightSyncManager"></a>`WeightSyncManager`
- def: [`torchtitan/experiments/rl/components/weight_sync.py:30`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py#L30)
- doc: Overlap the trainer-&gt;generator weight sync with the next training step.
- signature: `class WeightSyncManager:`
- members:
  - <a id="WeightSyncManager.start_async_push_pull"></a>`start_async_push_pull(self, *, version: int)` — [`L74`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py#L74) — Fire push -> pull -> buffer-slot release in the background; returns immediately.
  - <a id="WeightSyncManager.wait_inflight_push_pull"></a>`wait_inflight_push_pull(self)` — [`L104`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py#L104) — Finish the last in-flight push+pull so generators hold the final weights (e.g. before validation).
  - <a id="WeightSyncManager.wait_prev_pull"></a>`wait_prev_pull(self)` — [`L95`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py#L95)
  - <a id="WeightSyncManager.wait_prev_push"></a>`wait_prev_push(self)` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py#L86)
- protocol/private: <a id="WeightSyncManager.__init__"></a>`__init__`[`L53`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py#L53), <a id="WeightSyncManager._generator_pull_and_release_buffer_slots"></a>`_generator_pull_and_release_buffer_slots`[`L115`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py#L115), <a id="WeightSyncManager._generator_pull_task"></a>`_generator_pull_task`[`L68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py#L68), <a id="WeightSyncManager._generator_router"></a>`_generator_router`[`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py#L62), <a id="WeightSyncManager._group_buffer"></a>`_group_buffer`[`L63`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py#L63), <a id="WeightSyncManager._last_pull_s"></a>`_last_pull_s`[`L72`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py#L72), <a id="WeightSyncManager._last_push_s"></a>`_last_push_s`[`L71`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py#L71), <a id="WeightSyncManager._num_prompts_per_train_step"></a>`_num_prompts_per_train_step`[`L64`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py#L64), <a id="WeightSyncManager._trainer"></a>`_trainer`[`L61`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py#L61), <a id="WeightSyncManager._trainer_push"></a>`_trainer_push`[`L109`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py#L109), <a id="WeightSyncManager._trainer_push_task"></a>`_trainer_push_task`[`L67`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py#L67)
- uses (calls/refs, reference-scoped): [`Metric`](../observability/metrics/types.md#Metric), [`log_trace_span`](../../../observability/structured_logger/structured_logging.md#log_trace_span), [`NoReduce`](../observability/metrics/types.md#NoReduce), [`PolicyTrainer`](../actors/trainer.md#PolicyTrainer), [`InterGeneratorRouter`](../routing/inter_generator_router.md#InterGeneratorRouter), [`RolloutGroupWorkBuffer`](work_buffer.md#RolloutGroupWorkBuffer), [`push_model_state_dict`](../actors/trainer.md#PolicyTrainer.push_model_state_dict), [`release_active_groups`](work_buffer.md#RolloutGroupWorkBuffer.release_active_groups), [`pull_model_state_dict`](../routing/inter_generator_router.md#InterGeneratorRouter.pull_model_state_dict), [`_noop`](weight_sync.md#_noop)
- used by: [`_trainer_loop`](../controller.md#Controller._trainer_loop), [`_weight_sync`](../controller.md#Controller._weight_sync)  (8 test-only)

## Functions
- <a id="_noop"></a>`_noop()` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/weight_sync.py#L26)

