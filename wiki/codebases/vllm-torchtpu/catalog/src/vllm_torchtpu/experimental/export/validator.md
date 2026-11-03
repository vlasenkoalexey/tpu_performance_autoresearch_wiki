---
title: 'Module: src/vllm_torchtpu/experimental/export/validator.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/experimental/export/validator.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.experimental.export.validator`/
symbols:
  validate_exported_model_dir: validate_exported_model_dir().
  _check_dtype: _check_dtype().
  parse_mlir_main_signature: parse_mlir_main_signature().
  canonical_dtype: canonical_dtype().
  validate_mlir_custom_calls: validate_mlir_custom_calls().
  _shard_local_shape: _shard_local_shape().
  _require_key: _require_key().
  ALLOWED_CUSTOM_CALLS: ALLOWED_CUSTOM_CALLS.
  _DTYPE_ALIASES: _DTYPE_ALIASES.
  MLIR_SHAPES: MLIR_SHAPES.
  STABLEHLO_DTYPES: STABLEHLO_DTYPES.
  _scan_attr_dict: _scan_attr_dict().
---
# Module: [`src/vllm_torchtpu/experimental/export/validator.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/validator.py)

## Functions
- <a id="_check_dtype"></a>`_check_dtype(entry: dict[str, Any], actual: str, where: str)` — [`L254`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/validator.py#L254)
- <a id="_require_key"></a>`_require_key(entry: dict[str, Any], key: str, where: str)` — [`L211`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/validator.py#L211) — Returns `entry[key]`, failing loudly when metadata omits it.
- <a id="_scan_attr_dict"></a>`_scan_attr_dict(text: str, start: int)` — [`L119`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/validator.py#L119) — Returns the index just past the `{...}` attribute dict at `text[start]`.
- <a id="_shard_local_shape"></a>`_shard_local_shape(entry: dict[str, Any], axis_sizes: dict[str, int], where: str)` — [`L218`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/validator.py#L218) — Validates `entry`'s global shape and sharding; returns one device's shape.
- <a id="canonical_dtype"></a>`canonical_dtype(dtype_str: str)` — [`L111`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/validator.py#L111) — Normalizes a dtype spelling to its canonical short name.
- <a id="parse_mlir_main_signature"></a>`parse_mlir_main_signature(mlir_text: str)` — [`L143`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/validator.py#L143) — Parses @main input and output tensor specs from a StableHLO MLIR string.
- <a id="validate_exported_model_dir"></a>`validate_exported_model_dir(output_dir: str)` — [`L262`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/validator.py#L262) — Validates an exported model directory against the artifact contract. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="validate_mlir_custom_calls"></a>`validate_mlir_custom_calls(mlir_text: str, file_name: str = "")` — [`L199`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/validator.py#L199) — Verifies that all stablehlo.custom_call targets are in ALLOWED_CUSTOM_CALLS.

## Module values
- <a id="ALLOWED_CUSTOM_CALLS"></a>`ALLOWED_CUSTOM_CALLS` — [`L23`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/validator.py#L23)
- <a id="MLIR_SHAPES"></a>`MLIR_SHAPES` — [`L108`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/validator.py#L108)
- <a id="STABLEHLO_DTYPES"></a>`STABLEHLO_DTYPES` — [`L86`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/validator.py#L86)
- <a id="_DTYPE_ALIASES"></a>`_DTYPE_ALIASES` — [`L38`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/validator.py#L38)

