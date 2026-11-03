---
title: 'Module: src/vllm_torchtpu/core/abort_on_preemption.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/core/abort_on_preemption.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.core.abort_on_preemption`/
symbols:
  patch_scheduler_init.init: patch_scheduler_init().init().
  _CapacityPreemption.preempt_request: _CapacityPreemption#preempt_request().
  _CapacityPreemption.abort: _CapacityPreemption#abort().
  _CapacityPreemption.reset_prefix_cache: _CapacityPreemption#reset_prefix_cache().
  _CapacityPreemption.update_from_output: _CapacityPreemption#update_from_output().
  logger: logger.
  patch_scheduler_init: patch_scheduler_init().
  _CapacityPreemption._in_reset: _CapacityPreemption#_in_reset.
  _CapacityPreemption.pending: _CapacityPreemption#pending.
  _CapacityPreemption: _CapacityPreemption#
  _CapacityPreemption.scheduler: _CapacityPreemption#scheduler.
  _CapacityPreemption.original_preempt: _CapacityPreemption#original_preempt.
  _CapacityPreemption.original_reset: _CapacityPreemption#original_reset.
  _CapacityPreemption.original_update: _CapacityPreemption#original_update.
  _should_enable_abort_on_preemption: _should_enable_abort_on_preemption().
  _CapacityPreemption.__init__: _CapacityPreemption#__init__().
---
# Module: [`src/vllm_torchtpu/core/abort_on_preemption.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/abort_on_preemption.py)

## Classes
### <a id="_CapacityPreemption"></a>`_CapacityPreemption`
- def: [`src/vllm_torchtpu/core/abort_on_preemption.py:51`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/abort_on_preemption.py#L51)
- doc: Own the terminal snapshots and preserve the scheduler's output chain.
- signature: `class _CapacityPreemption:`
- members:
  - <a id="_CapacityPreemption.abort"></a>`abort(self, request: Request, timestamp: float)` — [`L91`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/abort_on_preemption.py#L91) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="_CapacityPreemption.preempt_request"></a>`preempt_request(self, request: Request, timestamp: float, drop_stale_output: bool = False)` — [`L62`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/abort_on_preemption.py#L62) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="_CapacityPreemption.reset_prefix_cache"></a>`reset_prefix_cache(self, reset_running_requests: bool = False, reset_connector: bool = False)` — [`L77`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/abort_on_preemption.py#L77) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="_CapacityPreemption.update_from_output"></a>`update_from_output(self, scheduler_output: SchedulerOutput, model_runner_output: ModelRunnerOutput)` — [`L135`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/abort_on_preemption.py#L135) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="_CapacityPreemption.original_preempt"></a>`original_preempt` — [`L56`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/abort_on_preemption.py#L56)
  - <a id="_CapacityPreemption.original_reset"></a>`original_reset` — [`L57`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/abort_on_preemption.py#L57)
  - <a id="_CapacityPreemption.original_update"></a>`original_update` — [`L58`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/abort_on_preemption.py#L58)
  - <a id="_CapacityPreemption.pending"></a>`pending` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/abort_on_preemption.py#L59)
  - <a id="_CapacityPreemption.scheduler"></a>`scheduler` — [`L55`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/abort_on_preemption.py#L55)
- protocol/private: <a id="_CapacityPreemption.__init__"></a>`__init__`[`L54`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/abort_on_preemption.py#L54), <a id="_CapacityPreemption._in_reset"></a>`_in_reset`[`L60`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/abort_on_preemption.py#L60)
- uses (calls/refs, reference-scoped): [`logger`](abort_on_preemption.md#logger)
- used by: [`init`](abort_on_preemption.md#patch_scheduler_init.init)

## Functions
- <a id="_should_enable_abort_on_preemption"></a>`_should_enable_abort_on_preemption(vllm_config: VllmConfig)` — [`L152`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/abort_on_preemption.py#L152)
- <a id="patch_scheduler_init.init"></a>`init(self: Scheduler, vllm_config: VllmConfig, *args, **kwargs)` — [`L172`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/abort_on_preemption.py#L172) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
- <a id="patch_scheduler_init"></a>`patch_scheduler_init()` — [`L166`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/abort_on_preemption.py#L166) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)

## Module values
- <a id="logger"></a>`logger` — [`L48`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/abort_on_preemption.py#L48)

