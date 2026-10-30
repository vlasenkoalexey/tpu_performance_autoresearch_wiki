---
title: 'Module: src/torch_tpu/_internal/profiler/_api.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/profiler/_api.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.profiler._api`/
symbols:
  _get_profile_options: _get_profile_options().
  profile: profile().
  ProfilerActivity: ProfilerActivity#
  xprof_trace_handler: xprof_trace_handler().
  ProfilerActivity.CPU: ProfilerActivity#CPU.
  ProfilerActivity.TPU: ProfilerActivity#TPU.
  xprof_trace_handler.handler_fn: xprof_trace_handler().handler_fn().
  ProfilerActivity.GPU: ProfilerActivity#GPU.
  register_kineto_backend: register_kineto_backend().
---
# Module: [`src/torch_tpu/_internal/profiler/_api.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_api.py)

## Classes
### <a id="ProfilerActivity"></a>`ProfilerActivity`  ·  implements/extends Enum
- def: [`src/torch_tpu/_internal/profiler/_api.py:28`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_api.py#L28)
- doc: Enum to specify the activities to profile.
- signature: `class ProfilerActivity(enum.Enum):`
- members:
  - <a id="ProfilerActivity.CPU"></a>`CPU` — [`L37`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_api.py#L37)
  - <a id="ProfilerActivity.GPU"></a>`GPU` — [`L39`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_api.py#L39)
  - <a id="ProfilerActivity.TPU"></a>`TPU` — [`L38`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_api.py#L38)
- used by: [`_get_profile_options`](_api.md#_get_profile_options), [`profile`](_api.md#profile)

## Functions
- <a id="_get_profile_options"></a>`_get_profile_options(activities: list[ProfilerActivity])` — [`L78`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_api.py#L78) — Determines the profiler options based on the selected activities.
- <a id="xprof_trace_handler.handler_fn"></a>`handler_fn(prof: Any)` — [`L70`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_api.py#L70)
- <a id="profile"></a>`profile(activities: list[ProfilerActivity] | None = None, on_trace_ready: Callable[[Any], str] | None = None)` — [`L119`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_api.py#L119) — Context manager to take a profiler trace, compatible with torch.profiler.
- <a id="register_kineto_backend"></a>`register_kineto_backend()` — [`L171`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_api.py#L171) — Explicitly registers the Kineto backend for TPU profiling.
- <a id="xprof_trace_handler"></a>`xprof_trace_handler(dir_name: os.PathLike[str] | str, worker_rank: str | None = None)` — [`L42`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/_api.py#L42) — Standard handler to be used with the `on_trace_ready` argument in `profiler.profile`.

