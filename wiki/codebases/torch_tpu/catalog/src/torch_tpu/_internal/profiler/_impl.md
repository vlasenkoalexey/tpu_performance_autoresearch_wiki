---
title: 'Module: src/torch_tpu/_internal/profiler/_impl.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/profiler/_impl.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.profiler._impl`/
symbols:
  start_trace: start_trace().
  stop_trace: stop_trace().
  _profile_state: _profile_state.
  _ProfileState.reset: _ProfileState#reset().
  _profiler_server: _profiler_server.
  _ProfileState.profile_session: _ProfileState#profile_session.
  _ProfileState.worker_rank: _ProfileState#worker_rank.
  start_server: start_server().
  stop_server: stop_server().
  ProfileOptions: ProfileOptions#
  _ProfileState.log_dir: _ProfileState#log_dir.
  ProfileOptions.host_tracer_level: ProfileOptions#host_tracer_level.
  ProfileOptions.device_tracer_level: ProfileOptions#device_tracer_level.
  ProfileOptions.python_tracer_level: ProfileOptions#python_tracer_level.
  _ProfileState.lock: _ProfileState#lock.
  _ProfileState: _ProfileState#
  _ProfileState.__init__: _ProfileState#__init__().
---
# Module: [`src/torch_tpu/_internal/profiler/_impl.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py)

## Classes
### <a id="ProfileOptions"></a>`ProfileOptions`
- def: [`src/torch_tpu/_internal/profiler/_impl.py:34`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py#L34)
- doc: Options for profiling.
- signature: `class ProfileOptions:`
- members:
  - <a id="ProfileOptions.device_tracer_level"></a>`device_tracer_level` — [`L38`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py#L38)
  - <a id="ProfileOptions.host_tracer_level"></a>`host_tracer_level` — [`L37`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py#L37)
  - <a id="ProfileOptions.python_tracer_level"></a>`python_tracer_level` — [`L39`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py#L39)
- used by: [`_get_profile_options`](_api.md#_get_profile_options), [`start_trace`](_impl.md#start_trace)

### <a id="_ProfileState"></a>`_ProfileState`
- def: [`src/torch_tpu/_internal/profiler/_impl.py:80`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py#L80)
- doc: Internal class to hold the state of the profiler.
- signature: `class _ProfileState:`
- members:
  - <a id="_ProfileState.reset"></a>`reset(self)` — [`L97`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py#L97) — Resets the profiler state.
  - <a id="_ProfileState.lock"></a>`lock` — [`L95`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py#L95)
  - <a id="_ProfileState.log_dir"></a>`log_dir` — [`L93`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py#L93)
  - <a id="_ProfileState.profile_session"></a>`profile_session` — [`L92`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py#L92)
  - <a id="_ProfileState.worker_rank"></a>`worker_rank` — [`L94`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py#L94)
- protocol/private: <a id="_ProfileState.__init__"></a>`__init__`[`L91`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py#L91)
- used by: [`start_trace`](_impl.md#start_trace), [`stop_trace`](_impl.md#stop_trace), [`_profile_state`](_impl.md#_profile_state)

## Functions
- <a id="start_server"></a>`start_server(port: int)` — [`L42`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py#L42) — Starts the profiler server on port `port`.
- <a id="start_trace"></a>`start_trace(log_dir: os.PathLike[str] | str, profiler_options: ProfileOptions | None = None, worker_rank: str | None = None)` — [`L107`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py#L107) — Starts a profiler trace.
- <a id="stop_server"></a>`stop_server()` — [`L67`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py#L67) — Stops the running profiler server.
- <a id="stop_trace"></a>`stop_trace()` — [`L161`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py#L161) — Stops the currently-running profiler trace.

## Module values
- <a id="_profile_state"></a>`_profile_state` — [`L104`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py#L104)
- <a id="_profiler_server"></a>`_profiler_server` — [`L30`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_impl.py#L30)

