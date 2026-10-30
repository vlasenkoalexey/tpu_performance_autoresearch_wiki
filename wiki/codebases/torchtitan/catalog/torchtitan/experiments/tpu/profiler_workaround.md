---
title: 'Module: torchtitan/experiments/tpu/profiler_workaround.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/profiler_workaround.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.profiler_workaround`/
symbols:
  custom_enter: custom_enter().
  custom_step: custom_step().
  custom_exit: custom_exit().
  custom_init: custom_init().
  _original_enter: _original_enter.
  _original_init: _original_init.
  _original_step: _original_step.
  _original_exit: _original_exit.
  init: init().
  _global_job_config: _global_job_config.
---
# Module: [`torchtitan/experiments/tpu/profiler_workaround.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/profiler_workaround.py)

## Functions
- <a id="custom_enter"></a>`custom_enter(self: torchtitan_profiler.Profiler)` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/profiler_workaround.py#L39) — Patched __enter__ to redirect to custom TPU profilers if configured.
- <a id="custom_exit"></a>`custom_exit(self: torchtitan_profiler.Profiler, exc_type: Any, exc_val: Any, exc_tb: Any)` — [`L118`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/profiler_workaround.py#L118) — Patched __exit__ to ensure custom profilers are stopped.
- <a id="custom_init"></a>`custom_init(self: torchtitan_profiler.Profiler, *args: Any, **kwargs: Any)` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/profiler_workaround.py#L29) — Patched __init__ to initialize TPU-specific attributes.
- <a id="custom_step"></a>`custom_step(self: torchtitan_profiler.Profiler)` — [`L87`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/profiler_workaround.py#L87) — Patched step to manually schedule JAX/XProf profiling cycles.
- <a id="init"></a>`init(job_config: Any)` — [`L13`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/profiler_workaround.py#L13) — Initialize the profiler workaround with the global job config.

## Module values
- <a id="_global_job_config"></a>`_global_job_config` — [`L10`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/profiler_workaround.py#L10)
- <a id="_original_enter"></a>`_original_enter` — [`L24`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/profiler_workaround.py#L24)
- <a id="_original_exit"></a>`_original_exit` — [`L26`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/profiler_workaround.py#L26)
- <a id="_original_init"></a>`_original_init` — [`L23`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/profiler_workaround.py#L23)
- <a id="_original_step"></a>`_original_step` — [`L25`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/profiler_workaround.py#L25)

