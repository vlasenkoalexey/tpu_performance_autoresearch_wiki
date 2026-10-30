---
title: 'Module: src/torch_tpu/_internal/warnings.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/warnings.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.warnings`/
symbols:
  WarningCategory: WarningCategory.
  format_message: format_message().
  get_prefix: get_prefix().
  get_builtin_category: get_builtin_category().
  API_STAGE.API_STAGE: API_STAGE.API_STAGE.
  CORRECTNESS.CORRECTNESS: CORRECTNESS.CORRECTNESS.
  DEPRECATED_API.DEPRECATED_API: DEPRECATED_API.DEPRECATED_API.
  EXPERIMENTAL_API.EXPERIMENTAL_API: EXPERIMENTAL_API.EXPERIMENTAL_API.
  INTERNAL_API.INTERNAL_API: INTERNAL_API.INTERNAL_API.
  PERFORMANCE.PERFORMANCE: PERFORMANCE.PERFORMANCE.
  TCMALLOC.TCMALLOC: TCMALLOC.TCMALLOC.
  TORCH_TPU.TORCH_TPU: TORCH_TPU.TORCH_TPU.
  UNOPTIMIZED_BUILD.UNOPTIMIZED_BUILD: UNOPTIMIZED_BUILD.UNOPTIMIZED_BUILD.
---
# Module: [`src/torch_tpu/_internal/warnings.py`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/warnings.py)

## Functions
- <a id="format_message"></a>`format_message(category: WarningCategory, message: str)` — [`L135`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/warnings.py#L135) — Returns `message` prefixed with the prefix of `category`.
- <a id="get_builtin_category"></a>`get_builtin_category(category: WarningCategory)` — [`L128`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/warnings.py#L128) — Returns the built-in Python warning category to emit `category` with.
- <a id="get_prefix"></a>`get_prefix(category: WarningCategory)` — [`L123`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/warnings.py#L123) — Returns the prefix of the messages of warnings in `category`.

## Module values
- <a id="API_STAGE.API_STAGE"></a>`API_STAGE` — [`L111`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/warnings.py#L111)
- <a id="CORRECTNESS.CORRECTNESS"></a>`CORRECTNESS` — [`L112`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/warnings.py#L112)
- <a id="DEPRECATED_API.DEPRECATED_API"></a>`DEPRECATED_API` — [`L113`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/warnings.py#L113)
- <a id="EXPERIMENTAL_API.EXPERIMENTAL_API"></a>`EXPERIMENTAL_API` — [`L114`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/warnings.py#L114)
- <a id="INTERNAL_API.INTERNAL_API"></a>`INTERNAL_API` — [`L115`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/warnings.py#L115)
- <a id="PERFORMANCE.PERFORMANCE"></a>`PERFORMANCE` — [`L116`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/warnings.py#L116)
- <a id="TCMALLOC.TCMALLOC"></a>`TCMALLOC` — [`L117`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/warnings.py#L117)
- <a id="TORCH_TPU.TORCH_TPU"></a>`TORCH_TPU` — [`L118`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/warnings.py#L118)
- <a id="UNOPTIMIZED_BUILD.UNOPTIMIZED_BUILD"></a>`UNOPTIMIZED_BUILD` — [`L119`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/warnings.py#L119)
- <a id="WarningCategory"></a>`WarningCategory` — [`L108`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/warnings.py#L108)

