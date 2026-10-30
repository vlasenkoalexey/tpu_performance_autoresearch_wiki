---
title: 'Module: src/torch_tpu/_internal/profiler/profiler_config.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/profiler/profiler_config.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.profiler.profiler_config`/
symbols:
  TpuProfilerConfig._get_parts: TpuProfilerConfig#_get_parts().
  _STABLE_KEYS: _STABLE_KEYS.
  TpuProfilerConfig.__init__: TpuProfilerConfig#__init__().
  _format_experimental_value: _format_experimental_value().
  _PK_CHECK_EXPERIMENTAL_OPTIONS: _PK_CHECK_EXPERIMENTAL_OPTIONS.
  _PK_DEVICE_TRACER_LEVEL: _PK_DEVICE_TRACER_LEVEL.
  _PK_HOST_TRACER_LEVEL: _PK_HOST_TRACER_LEVEL.
  _PK_PYTHON_TRACER_LEVEL: _PK_PYTHON_TRACER_LEVEL.
  _PK_RUN_DIR: _PK_RUN_DIR.
  _PK_WORKER_RANK: _PK_WORKER_RANK.
  _ExperimentalValue._ExperimentalValue: _ExperimentalValue._ExperimentalValue.
  TpuProfilerConfig: TpuProfilerConfig#
---
# Module: [`src/torch_tpu/_internal/profiler/profiler_config.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/profiler_config.py)

## Classes
### <a id="TpuProfilerConfig"></a>`TpuProfilerConfig`
- def: [`src/torch_tpu/_internal/profiler/profiler_config.py:89`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/profiler_config.py#L89)
- doc: Configuration for TPU-specific profiler options with standard XLA defaults.
- signature: `class TpuProfilerConfig(torch.profiler._ExperimentalConfig):`
- members:
  - <a id="TpuProfilerConfig.__init__"></a>`__init__(self, *, host_tracer_level: int = 2, device_tracer_level: int = 1, python_tracer_level: int = 0, run_dir: os.PathLike[str] | str | None = None, worker_rank: str | None = None, experimental_options: Mapping[str, _ExperimentalValue] | None = None, check_experimental_options: bool = True)` — [`L92`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/profiler_config.py#L92) — Initializes the TPU profiler configuration.
- protocol/private: <a id="TpuProfilerConfig._get_parts"></a>`_get_parts`[`L157`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/profiler_config.py#L157)
- uses (calls/refs, reference-scoped): [`_STABLE_KEYS`](profiler_config.md#_STABLE_KEYS), [`_format_experimental_value`](profiler_config.md#_format_experimental_value), [`_ExperimentalValue`](profiler_config.md#_ExperimentalValue._ExperimentalValue), [`_PK_CHECK_EXPERIMENTAL_OPTIONS`](profiler_config.md#_PK_CHECK_EXPERIMENTAL_OPTIONS), [`_PK_DEVICE_TRACER_LEVEL`](profiler_config.md#_PK_DEVICE_TRACER_LEVEL), [`_PK_HOST_TRACER_LEVEL`](profiler_config.md#_PK_HOST_TRACER_LEVEL), [`_PK_PYTHON_TRACER_LEVEL`](profiler_config.md#_PK_PYTHON_TRACER_LEVEL), [`_PK_RUN_DIR`](profiler_config.md#_PK_RUN_DIR), [`_PK_WORKER_RANK`](profiler_config.md#_PK_WORKER_RANK)

## Functions
- <a id="_format_experimental_value"></a>`_format_experimental_value(value: _ExperimentalValue)` — [`L56`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/profiler_config.py#L56) — Formats an experimental option value for the config string.

## Module values
- <a id="_ExperimentalValue._ExperimentalValue"></a>`_ExperimentalValue` — [`L27`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/profiler_config.py#L27)
- <a id="_PK_CHECK_EXPERIMENTAL_OPTIONS"></a>`_PK_CHECK_EXPERIMENTAL_OPTIONS` — [`L31`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/profiler_config.py#L31)
- <a id="_PK_DEVICE_TRACER_LEVEL"></a>`_PK_DEVICE_TRACER_LEVEL` — [`L32`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/profiler_config.py#L32)
- <a id="_PK_HOST_TRACER_LEVEL"></a>`_PK_HOST_TRACER_LEVEL` — [`L33`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/profiler_config.py#L33)
- <a id="_PK_PYTHON_TRACER_LEVEL"></a>`_PK_PYTHON_TRACER_LEVEL` — [`L34`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/profiler_config.py#L34)
- <a id="_PK_RUN_DIR"></a>`_PK_RUN_DIR` — [`L35`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/profiler_config.py#L35)
- <a id="_PK_WORKER_RANK"></a>`_PK_WORKER_RANK` — [`L36`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/profiler_config.py#L36)
- <a id="_STABLE_KEYS"></a>`_STABLE_KEYS` — [`L43`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/profiler/profiler_config.py#L43)

