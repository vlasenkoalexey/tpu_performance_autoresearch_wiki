---
title: 'Module: src/vllm_torchtpu/omni/profiler.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/omni/profiler.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.omni.profiler`/
symbols:
  TpuOmniTorchProfilerWrapper._stop: TpuOmniTorchProfilerWrapper#_stop().
  TpuOmniTorchProfilerWrapper.profiler: TpuOmniTorchProfilerWrapper#profiler.
  TpuOmniTorchProfilerWrapper._start: TpuOmniTorchProfilerWrapper#_start().
  TpuOmniTorchProfilerWrapper._tpu_python_tracer: TpuOmniTorchProfilerWrapper#_tpu_python_tracer.
  TpuOmniTorchProfilerWrapper._capture_state: TpuOmniTorchProfilerWrapper#_capture_state.
  logger: logger.
  _CaptureState.run_root: _CaptureState#run_root.
  _CaptureState.rank: _CaptureState#rank.
  TpuOmniTorchProfilerWrapper._create_profiler: TpuOmniTorchProfilerWrapper#_create_profiler().
  _CaptureState: _CaptureState#
  _CaptureState.capture_dir: _CaptureState#capture_dir.
  _CaptureState.canonical_ts: _CaptureState#canonical_ts.
  _CaptureState.world_size: _CaptureState#world_size.
  _CaptureState.session_key: _CaptureState#session_key.
  TpuOmniTorchProfilerWrapper._profile_session_index: TpuOmniTorchProfilerWrapper#_profile_session_index.
  TpuOmniTorchProfilerWrapper: TpuOmniTorchProfilerWrapper#
  TpuOmniTorchProfilerWrapper.__init__: TpuOmniTorchProfilerWrapper#__init__().
  TpuOmniTorchProfilerWrapper._get_default_activities: TpuOmniTorchProfilerWrapper#_get_default_activities().
---
# Module: [`src/vllm_torchtpu/omni/profiler.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py)

## Classes
### <a id="TpuOmniTorchProfilerWrapper"></a>`TpuOmniTorchProfilerWrapper`
- def: [`src/vllm_torchtpu/omni/profiler.py:63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L63)
- doc: Omni torch profiler wrapper that captures TPU device activity.
- signature: `class TpuOmniTorchProfilerWrapper(OmniTorchProfilerWrapper):`
- members:
  - <a id="TpuOmniTorchProfilerWrapper.profiler"></a>`profiler` — [`L134`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L134) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- protocol/private: <a id="TpuOmniTorchProfilerWrapper.__init__"></a>`__init__`[`L66`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L66), <a id="TpuOmniTorchProfilerWrapper._capture_state"></a>`_capture_state`[`L84`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L84), <a id="TpuOmniTorchProfilerWrapper._create_profiler"></a>`_create_profiler`[`L95`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L95), <a id="TpuOmniTorchProfilerWrapper._get_default_activities"></a>`_get_default_activities`[`L86`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L86), <a id="TpuOmniTorchProfilerWrapper._profile_session_index"></a>`_profile_session_index`[`L83`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L83), <a id="TpuOmniTorchProfilerWrapper._start"></a>`_start`[`L102`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L102), <a id="TpuOmniTorchProfilerWrapper._stop"></a>`_stop`[`L163`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L163), <a id="TpuOmniTorchProfilerWrapper._tpu_python_tracer"></a>`_tpu_python_tracer`[`L73`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L73)
- uses (calls/refs, reference-scoped): [`resolve_profile_dir_and_opts`](../tracing/options.md#resolve_profile_dir_and_opts), [`resolve_canonical_dst_ts`](../profiler_trace.md#resolve_canonical_dst_ts), [`clear_canonical_ts_marker`](../profiler_trace.md#clear_canonical_ts_marker), [`merge_rank_capture`](../profiler_trace.md#merge_rank_capture), [`logger`](profiler.md#logger), [`profile_session_id`](../profiler_trace.md#profile_session_id), [`rank`](profiler.md#_CaptureState.rank), [`rank_capture_dir`](../profiler_trace.md#rank_capture_dir), [`run_root`](profiler.md#_CaptureState.run_root), [`_CaptureState`](profiler.md#_CaptureState), [`canonical_ts`](profiler.md#_CaptureState.canonical_ts), [`capture_dir`](profiler.md#_CaptureState.capture_dir), [`session_key`](profiler.md#_CaptureState.session_key), [`world_size`](profiler.md#_CaptureState.world_size)

### <a id="_CaptureState"></a>`_CaptureState`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/omni/profiler.py:52`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L52)
- doc: What _start() hands to _stop() for the per-rank merge.
- signature: `class _CaptureState(NamedTuple):`
- members:
  - <a id="_CaptureState.canonical_ts"></a>`canonical_ts` — [`L57`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L57)
  - <a id="_CaptureState.capture_dir"></a>`capture_dir` — [`L55`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L55)
  - <a id="_CaptureState.rank"></a>`rank` — [`L58`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L58) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
  - <a id="_CaptureState.run_root"></a>`run_root` — [`L56`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L56) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
  - <a id="_CaptureState.session_key"></a>`session_key` — [`L60`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L60)
  - <a id="_CaptureState.world_size"></a>`world_size` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L59)
- used by: [`_stop`](profiler.md#TpuOmniTorchProfilerWrapper._stop), [`profiler`](profiler.md#TpuOmniTorchProfilerWrapper.profiler), [`_capture_state`](profiler.md#TpuOmniTorchProfilerWrapper._capture_state)

## Module values
- <a id="logger"></a>`logger` — [`L49`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/profiler.py#L49)

