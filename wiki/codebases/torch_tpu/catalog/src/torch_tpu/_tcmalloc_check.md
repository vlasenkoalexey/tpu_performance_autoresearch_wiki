---
title: 'Module: src/torch_tpu/_tcmalloc_check.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_tcmalloc_check.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._tcmalloc_check`/
symbols:
  check_tcmalloc: check_tcmalloc().
  install_default_filters: install_default_filters().
  TCMALLOC_WARNING_PREFIX.TCMALLOC_WARNING_PREFIX: TCMALLOC_WARNING_PREFIX.TCMALLOC_WARNING_PREFIX.
  _has_sanitizer_init: _has_sanitizer_init().
  _TCMALLOC_OR_SANITIZER_RE._TCMALLOC_OR_SANITIZER_RE: _TCMALLOC_OR_SANITIZER_RE._TCMALLOC_OR_SANITIZER_RE.
---
# Module: [`src/torch_tpu/_tcmalloc_check.py`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_tcmalloc_check.py)

## Functions
- <a id="_has_sanitizer_init"></a>`_has_sanitizer_init(global_syms: ctypes.CDLL)` — [`L64`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_tcmalloc_check.py#L64) — Returns whether a sanitizer runtime's init symbol is in `global_syms`.
- <a id="check_tcmalloc"></a>`check_tcmalloc()` — [`L100`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_tcmalloc_check.py#L100) — Warns if tcmalloc is not the allocator of the current process.
- <a id="install_default_filters"></a>`install_default_filters()` — [`L85`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_tcmalloc_check.py#L85) — Installs TorchTPU's default warning filter for the tcmalloc warning.

## Module values
- <a id="TCMALLOC_WARNING_PREFIX.TCMALLOC_WARNING_PREFIX"></a>`TCMALLOC_WARNING_PREFIX` — [`L82`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_tcmalloc_check.py#L82)
- <a id="_TCMALLOC_OR_SANITIZER_RE._TCMALLOC_OR_SANITIZER_RE"></a>`_TCMALLOC_OR_SANITIZER_RE` — [`L45`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_tcmalloc_check.py#L45)

