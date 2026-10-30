---
title: 'Module: src/torch_tpu/_internal/execution_mode/__init__.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/execution_mode/__init__.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.execution_mode`/
symbols:
  _ExecutionModeModule: _ExecutionModeModule#
  _EagerMode._EagerMode: _EagerMode._EagerMode.
  EagerMode: EagerMode#
  _ExecutionModeModule.eager_mode: _ExecutionModeModule#eager_mode().
  set_eager_mode: set_eager_mode().
  _unwrap_eager_mode: _unwrap_eager_mode().
  _wrap_eager_mode: _wrap_eager_mode().
  EagerMode.__eq__: EagerMode#__eq__().
  EagerMode.DEFER_AND_FUSE: EagerMode#DEFER_AND_FUSE.
  EagerMode.DEFER_NEVER: EagerMode#DEFER_NEVER.
  EagerMode.DEFER_NEVER_AND_LAUNCH_BLOCKING: EagerMode#DEFER_NEVER_AND_LAUNCH_BLOCKING.
  EagerMode._INTERNAL_COMPILE_FX_GRAPH: EagerMode#_INTERNAL_COMPILE_FX_GRAPH.
  eager_mode: eager_mode.
  _ExecutionModeModule.enable_cpu_fallback: _ExecutionModeModule#enable_cpu_fallback().
  _ExecutionModeModule.disable_inplace_buffer_donation: _ExecutionModeModule#disable_inplace_buffer_donation().
  EagerMode.__hash__: EagerMode#__hash__().
  __all__: __all__.
  disable_inplace_buffer_donation: disable_inplace_buffer_donation.
  enable_cpu_fallback: enable_cpu_fallback.
---
# Module: [`src/torch_tpu/_internal/execution_mode/__init__.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py)

## Classes
### <a id="EagerMode"></a>`EagerMode`  ·  implements/extends Enum
- def: [`src/torch_tpu/_internal/execution_mode/__init__.py:30`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L30) — documented in [context-states-and-execution-modes](../../../../../concepts/context-states-and-execution-modes.md)
- doc: Eager execution mode for TPU operations.
- signature: `class EagerMode(enum.Enum):`
- members:
  - <a id="EagerMode.DEFER_AND_FUSE"></a>`DEFER_AND_FUSE` — [`L33`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L33)
  - <a id="EagerMode.DEFER_NEVER"></a>`DEFER_NEVER` — [`L34`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L34)
  - <a id="EagerMode.DEFER_NEVER_AND_LAUNCH_BLOCKING"></a>`DEFER_NEVER_AND_LAUNCH_BLOCKING` — [`L35`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L35)
- protocol/private: <a id="EagerMode._INTERNAL_COMPILE_FX_GRAPH"></a>`_INTERNAL_COMPILE_FX_GRAPH`[`L36`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L36), <a id="EagerMode.__eq__"></a>`__eq__`[`L38`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L38), <a id="EagerMode.__hash__"></a>`__hash__`[`L45`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L45)
- uses (calls/refs, reference-scoped): [`_EagerMode`](__init__.md#_EagerMode._EagerMode)
- used by: [`_ExecutionModeModule`](__init__.md#_ExecutionModeModule), [`eager_mode`](__init__.md#_ExecutionModeModule.eager_mode), [`set_eager_mode`](__init__.md#set_eager_mode), [`_unwrap_eager_mode`](__init__.md#_unwrap_eager_mode), [`_wrap_eager_mode`](__init__.md#_wrap_eager_mode)

### <a id="_ExecutionModeModule"></a>`_ExecutionModeModule`  ·  implements/extends ModuleType
- def: [`src/torch_tpu/_internal/execution_mode/__init__.py:88`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L88)
- doc: Custom module for managing TorchTPU execution settings.
- signature: `class _ExecutionModeModule(types.ModuleType):`
- members:
  - <a id="_ExecutionModeModule.disable_inplace_buffer_donation"></a>`disable_inplace_buffer_donation(self)` — [`L112`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L112)
  - <a id="_ExecutionModeModule.eager_mode"></a>`eager_mode(self)` — [`L92`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L92)
  - <a id="_ExecutionModeModule.enable_cpu_fallback"></a>`enable_cpu_fallback(self)` — [`L102`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L102)
- uses (calls/refs, reference-scoped): [`_EagerMode`](__init__.md#_EagerMode._EagerMode), [`EagerMode`](__init__.md#EagerMode), [`_unwrap_eager_mode`](__init__.md#_unwrap_eager_mode), [`_wrap_eager_mode`](__init__.md#_wrap_eager_mode)

## Functions
- <a id="_unwrap_eager_mode"></a>`_unwrap_eager_mode(mode: EagerMode | _EagerMode)` — [`L49`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L49) — Unwraps an EagerMode wrapper to extract the underlying C++ pybind _EagerMode.
- <a id="_wrap_eager_mode"></a>`_wrap_eager_mode(mode: _EagerMode | EagerMode)` — [`L64`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L64) — Wraps a raw C++ pybind _EagerMode into the public EagerMode enum.
- <a id="set_eager_mode"></a>`set_eager_mode(mode: EagerMode | _EagerMode)` — [`L130`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L130) — Context manager for setting the eager mode.

## Module values
- <a id="_EagerMode._EagerMode"></a>`_EagerMode` — [`L26`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L26)
- <a id="__all__"></a>`__all__` — [`L142`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L142)
- <a id="disable_inplace_buffer_donation"></a>`disable_inplace_buffer_donation` — [`L83`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L83)
- <a id="eager_mode"></a>`eager_mode` — [`L84`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L84)
- <a id="enable_cpu_fallback"></a>`enable_cpu_fallback` — [`L85`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/execution_mode/__init__.py#L85)

