---
title: 'Module: src/vllm_torchtpu/runner/stage_timing.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/runner/stage_timing.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.runner.stage_timing`/
symbols:
  RunnerStageTiming.stage: RunnerStageTiming#stage().
  RunnerStageTiming.take_samples: RunnerStageTiming#take_samples().
  RunnerStageTiming._pending: RunnerStageTiming#_pending.
  RunnerStageTiming.host_stage: RunnerStageTiming#host_stage().
  RunnerStageTiming._cpu_samples: RunnerStageTiming#_cpu_samples.
  RunnerStageTiming._rank: RunnerStageTiming#_rank.
  _PendingTiming: _PendingTiming#
  _PendingTiming.end: _PendingTiming#end.
  _PendingTiming.end_recorded: _PendingTiming#end_recorded.
  RunnerStageTiming: RunnerStageTiming#
  _PendingTiming.stage: _PendingTiming#stage.
  _PendingTiming.start: _PendingTiming#start.
  RunnerStageTiming.MAX_IN_FLIGHT_DEVICE_TIMINGS: RunnerStageTiming#MAX_IN_FLIGHT_DEVICE_TIMINGS.
  RunnerStageTiming.__init__: RunnerStageTiming#__init__().
---
# Module: [`src/vllm_torchtpu/runner/stage_timing.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/stage_timing.py)

## Classes
### <a id="RunnerStageTiming"></a>`RunnerStageTiming`
- def: [`src/vllm_torchtpu/runner/stage_timing.py:35`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/stage_timing.py#L35)
- doc: Record and drain stages on the runner thread without device waits.
- signature: `class RunnerStageTiming:`
- members:
  - <a id="RunnerStageTiming.host_stage"></a>`host_stage(self, stage: str)` — [`L47`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/stage_timing.py#L47)
  - <a id="RunnerStageTiming.stage"></a>`stage(self, stage: str)` — [`L53`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/stage_timing.py#L53)
  - <a id="RunnerStageTiming.take_samples"></a>`take_samples(self)` — [`L75`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/stage_timing.py#L75)
  - <a id="RunnerStageTiming.MAX_IN_FLIGHT_DEVICE_TIMINGS"></a>`MAX_IN_FLIGHT_DEVICE_TIMINGS` — [`L38`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/stage_timing.py#L38)
- protocol/private: <a id="RunnerStageTiming.__init__"></a>`__init__`[`L40`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/stage_timing.py#L40), <a id="RunnerStageTiming._cpu_samples"></a>`_cpu_samples`[`L42`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/stage_timing.py#L42), <a id="RunnerStageTiming._pending"></a>`_pending`[`L44`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/stage_timing.py#L44), <a id="RunnerStageTiming._rank"></a>`_rank`[`L41`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/stage_timing.py#L41)
- uses (calls/refs, reference-scoped): [`_PendingTiming`](stage_timing.md#_PendingTiming), [`end`](stage_timing.md#_PendingTiming.end), [`end_recorded`](stage_timing.md#_PendingTiming.end_recorded), [`stage`](stage_timing.md#_PendingTiming.stage), [`start`](stage_timing.md#_PendingTiming.start)
- used by: [`execute_model`](tpu_runner.md#TPUModelRunner.execute_model), [`sample_tokens`](tpu_runner.md#TPUModelRunner.sample_tokens), [`get_finished_kv_transfers`](tpu_runner.md#TPUModelRunner.get_finished_kv_transfers), [`_stage_timing`](tpu_runner.md#TPUModelRunner._stage_timing)

### <a id="_PendingTiming"></a>`_PendingTiming`
- def: [`src/vllm_torchtpu/runner/stage_timing.py:28`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/stage_timing.py#L28)
- signature: `class _PendingTiming:`
- members:
  - <a id="_PendingTiming.end"></a>`end` — [`L31`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/stage_timing.py#L31)
  - <a id="_PendingTiming.end_recorded"></a>`end_recorded` — [`L32`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/stage_timing.py#L32)
  - <a id="_PendingTiming.stage"></a>`stage` — [`L29`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/stage_timing.py#L29)
  - <a id="_PendingTiming.start"></a>`start` — [`L30`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/stage_timing.py#L30)
- used by: [`stage`](stage_timing.md#RunnerStageTiming.stage), [`take_samples`](stage_timing.md#RunnerStageTiming.take_samples), [`_pending`](stage_timing.md#RunnerStageTiming._pending)

