---
title: 'Module: src/torch_tpu/_loader.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_loader.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._loader`/
symbols:
  _init_device_impl: _init_device_impl().
  load: load().
  _tpu_inductor_wrapper_call: _tpu_inductor_wrapper_call().
  _default_tpu_compile: _default_tpu_compile().
  _init_device: _init_device().
  _orig_inductor_wrapper_call: _orig_inductor_wrapper_call.
  _default_backend_selector: _default_backend_selector().
  _OLD_AUTOLOAD_ENV._OLD_AUTOLOAD_ENV: _OLD_AUTOLOAD_ENV._OLD_AUTOLOAD_ENV.
  _get_default_backend_impl: _get_default_backend_impl().
  _is_tpu_backend: _is_tpu_backend().
  _patch_max_pool: _patch_max_pool().
  _AUTOLOAD_ENV_VAR._AUTOLOAD_ENV_VAR: _AUTOLOAD_ENV_VAR._AUTOLOAD_ENV_VAR.
  _LOADED._LOADED: _LOADED._LOADED.
  _DEVICE_INITIALIZED._DEVICE_INITIALIZED: _DEVICE_INITIALIZED._DEVICE_INITIALIZED.
  _torch_compile: _torch_compile.
  _InductorWrapper: _InductorWrapper.
  _has_tpu_inputs: _has_tpu_inputs().
  _set_libtpu_version: _set_libtpu_version().
  _warn_if_unoptimized: _warn_if_unoptimized().
  _patch_dtensor: _patch_dtensor().
  _init_device_impl._tpu_set_precision: _init_device_impl()._tpu_set_precision().
  _init_device_impl._tpu_get_precision: _init_device_impl()._tpu_get_precision().
  _INIT_LOCK._INIT_LOCK: _INIT_LOCK._INIT_LOCK.
  _INDUCTOR_TPU_ERROR._INDUCTOR_TPU_ERROR: _INDUCTOR_TPU_ERROR._INDUCTOR_TPU_ERROR.
---
# Module: [`src/torch_tpu/_loader.py`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py)

## Functions
- <a id="_default_backend_selector"></a>`_default_backend_selector(graph_module, example_inputs, **kwargs)` — [`L123`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L123) — The backend callable to pass to torch.compile.
- <a id="_default_tpu_compile"></a>`_default_tpu_compile(*args, **kwargs)` — [`L153`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L153)
- <a id="_get_default_backend_impl"></a>`_get_default_backend_impl(example_inputs)` — [`L95`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L95) — Checks for TPU and returns the appropriate backend function.
- <a id="_has_tpu_inputs"></a>`_has_tpu_inputs(example_inputs)` — [`L84`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L84) — Returns True if any tensor in `example_inputs` is on a TPU device.
- <a id="_init_device"></a>`_init_device(device: str)` — [`L369`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L369)
- <a id="_init_device_impl"></a>`_init_device_impl(device: str)` — [`L206`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L206) — Initializes a lazy pytorch device.
- <a id="_is_tpu_backend"></a>`_is_tpu_backend(backend: Any)` — [`L141`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L141) — Returns True if the backend specifies a TorchTPU backend.
- <a id="_patch_dtensor"></a>`_patch_dtensor()` — [`L192`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L192) — Overrides `from_local` to warn when shape/stride are omitted.
- <a id="_patch_max_pool"></a>`_patch_max_pool()` — [`L199`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L199) — Patches PyTorch max pooling operations with TPU-optimized variants.
- <a id="_set_libtpu_version"></a>`_set_libtpu_version()` — [`L162`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L162) — Passes the installed libtpu version to the C++ runtime.
- <a id="_init_device_impl._tpu_get_precision"></a>`_tpu_get_precision()` — [`L341`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L341)
- <a id="_tpu_inductor_wrapper_call"></a>`_tpu_inductor_wrapper_call(self, model_, inputs_, *args, **kwargs)` — [`L130`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L130) — Raises on `torch.compile(..., backend='inductor')` with TPU inputs.
- <a id="_init_device_impl._tpu_set_precision"></a>`_tpu_set_precision(precision: str)` — [`L326`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L326)
- <a id="_warn_if_unoptimized"></a>`_warn_if_unoptimized()` — [`L175`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L175) — Warns if TorchTPU is running in OSS with an unoptimized build.
- <a id="load"></a>`load()` — [`L379`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L379) — Loads the torch_tpu backend.

## Module values
- <a id="_AUTOLOAD_ENV_VAR._AUTOLOAD_ENV_VAR"></a>`_AUTOLOAD_ENV_VAR` — [`L26`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L26)
- <a id="_DEVICE_INITIALIZED._DEVICE_INITIALIZED"></a>`_DEVICE_INITIALIZED` — [`L63`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L63)
- <a id="_INDUCTOR_TPU_ERROR._INDUCTOR_TPU_ERROR"></a>`_INDUCTOR_TPU_ERROR` — [`L65`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L65)
- <a id="_INIT_LOCK._INIT_LOCK"></a>`_INIT_LOCK` — [`L54`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L54)
- <a id="_InductorWrapper"></a>`_InductorWrapper` — [`L60`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L60)
- <a id="_LOADED._LOADED"></a>`_LOADED` — [`L57`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L57)
- <a id="_OLD_AUTOLOAD_ENV._OLD_AUTOLOAD_ENV"></a>`_OLD_AUTOLOAD_ENV` — [`L34`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L34)
- <a id="_orig_inductor_wrapper_call"></a>`_orig_inductor_wrapper_call` — [`L61`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L61)
- <a id="_torch_compile"></a>`_torch_compile` — [`L59`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_loader.py#L59)

