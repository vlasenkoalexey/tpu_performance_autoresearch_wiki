---
title: 'Module: src/torch_tpu/_internal/distributed/from_local.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/distributed/from_local.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.distributed.from_local`/
symbols:
  from_local: from_local().
  patch_from_local: patch_from_local().
  _is_debug_eager_mode: _is_debug_eager_mode().
  _UNEVEN_SHARDING_WARNING._UNEVEN_SHARDING_WARNING: _UNEVEN_SHARDING_WARNING._UNEVEN_SHARDING_WARNING.
  _original_from_local._original_from_local: _original_from_local._original_from_local.
---
# Module: [`src/torch_tpu/_internal/distributed/from_local.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/from_local.py)

## Functions
- <a id="_is_debug_eager_mode"></a>`_is_debug_eager_mode()` — [`L35`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/from_local.py#L35) — Returns True if running in debug eager mode.
- <a id="from_local"></a>`from_local(*args: Any, run_check: bool | None = None, shape: torch.Size | None = None, stride: tuple[int, ...] | None = None, **kwargs: Any)` — [`L43`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/from_local.py#L43) — Wraps `DTensor.from_local` with shape checks.
- <a id="patch_from_local"></a>`patch_from_local()` — [`L74`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/from_local.py#L74) — Overrides DTensor.from_local with TorchTPU's implementation.

## Module values
- <a id="_UNEVEN_SHARDING_WARNING._UNEVEN_SHARDING_WARNING"></a>`_UNEVEN_SHARDING_WARNING` — [`L26`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/from_local.py#L26)
- <a id="_original_from_local._original_from_local"></a>`_original_from_local` — [`L32`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/from_local.py#L32)

