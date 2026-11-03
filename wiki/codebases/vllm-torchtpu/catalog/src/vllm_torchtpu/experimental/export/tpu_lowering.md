---
title: 'Module: src/vllm_torchtpu/experimental/export/tpu_lowering.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/experimental/export/tpu_lowering.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.experimental.export.tpu_lowering`/
symbols:
  lower_torch_forward_to_mlir: lower_torch_forward_to_mlir().
  dtype_name: dtype_name().
  lower_torch_callable_to_mlir: lower_torch_callable_to_mlir().
  _spec: _spec.
  _DtypeSpec: _DtypeSpec#
  _BY_NAME._BY_NAME: _BY_NAME._BY_NAME.
  dtype_spec: dtype_spec().
  torch_dtype: torch_dtype().
  lower_abstract_params_mlir: lower_abstract_params_mlir().
  fx_graph_to_mlir_text: fx_graph_to_mlir_text().
  set_aliasing_outputs: set_aliasing_outputs().
  lower_torch_forward_to_mlir._i32_specs: lower_torch_forward_to_mlir()._i32_specs().
  _DTYPE_SPECS._DTYPE_SPECS: _DTYPE_SPECS._DTYPE_SPECS.
  lower_torch_forward_to_mlir._torch_forward_entry: lower_torch_forward_to_mlir()._torch_forward_entry().
  _DtypeSpec.canonical: _DtypeSpec#canonical.
  _DtypeSpec.torch_dtype: _DtypeSpec#torch_dtype.
  _DtypeSpec.torch_name: _DtypeSpec#torch_name.
  normalize_mlir_text: normalize_mlir_text().
  set_aliasing_outputs._replace: set_aliasing_outputs()._replace().
  ensure_tuple_output: ensure_tuple_output().
---
# Module: [`src/vllm_torchtpu/experimental/export/tpu_lowering.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py)

## Classes
### <a id="_DtypeSpec"></a>`_DtypeSpec`
- def: [`src/vllm_torchtpu/experimental/export/tpu_lowering.py:32`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L32)
- signature: `class _DtypeSpec:`
- members:
  - <a id="_DtypeSpec.canonical"></a>`canonical` — [`L34`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L34)
  - <a id="_DtypeSpec.torch_dtype"></a>`torch_dtype` — [`L35`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L35)
  - <a id="_DtypeSpec.torch_name"></a>`torch_name` — [`L36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L36)
- used by: [`dtype_name`](tpu_lowering.md#dtype_name), [`_spec`](tpu_lowering.md#_spec), [`_BY_NAME`](tpu_lowering.md#_BY_NAME._BY_NAME), [`dtype_spec`](tpu_lowering.md#dtype_spec), [`torch_dtype`](tpu_lowering.md#torch_dtype), [`_DTYPE_SPECS`](tpu_lowering.md#_DTYPE_SPECS._DTYPE_SPECS)

## Functions
- <a id="lower_torch_forward_to_mlir._i32_specs"></a>`_i32_specs(inputs: Sequence[tuple[str, tuple[int, ...] | int]])` — [`L312`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L312)
- <a id="set_aliasing_outputs._replace"></a>`_replace(m: re.Match[str])` — [`L150`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L150)
- <a id="lower_torch_forward_to_mlir._torch_forward_entry"></a>`_torch_forward_entry(*args: torch.Tensor)` — [`L340`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L340)
- <a id="dtype_name"></a>`dtype_name(dt: Any)` — [`L104`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L104) — Returns the StableHLO element type name (`bf16`, `i32`, `f8E4M3FN`, ...). — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="dtype_spec"></a>`dtype_spec(dt: Any)` — [`L81`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L81) — Resolves a string or `torch.dtype` to its `_DtypeSpec`.
- <a id="ensure_tuple_output"></a>`ensure_tuple_output(graph: fx.GraphModule)` — [`L167`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L167) — Ensures `graph` returns a tuple of tensors.
- <a id="fx_graph_to_mlir_text"></a>`fx_graph_to_mlir_text(graph: fx.GraphModule, example_inputs: Sequence[torch.Tensor], *, donated_inputs: Sequence[int] | None = None, module_name: str | None = None)` — [`L179`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L179) — Lowers a `torch.fx.GraphModule` to StableHLO MLIR text via TorchTPU.
- <a id="lower_abstract_params_mlir"></a>`lower_abstract_params_mlir(param_items: Sequence[tuple[str, api.ShapeDtypeStruct]])` — [`L269`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L269) — Lowers the `abstract_params.mlir` identity, input `i` aliased to output `i`.
- <a id="lower_torch_callable_to_mlir"></a>`lower_torch_callable_to_mlir(fn: Callable[..., Any], arg_specs: Sequence[api.ShapeDtypeStruct], *, donate_argnums: Sequence[int] = (), module_name: str | None = None)` — [`L204`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L204) — Lowers a PyTorch callable over abstract tensor specs to StableHLO MLIR text. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="lower_torch_forward_to_mlir"></a>`lower_torch_forward_to_mlir(model: api.ExportableTextOnlyLLM, *, user_inputs: Sequence[tuple[str, tuple[int, ...] | int]], forward_names: Sequence[str], params_map: Mapping[str, api.ShapeDtypeStruct], state_specs: Sequence[api.ShapeDtypeStruct], bucket_size: int, weight_reshapes: Mapping[str, tuple[int, ...]] | None = None, trailing_user_inputs: Sequence[tuple[str, tuple[int, ...] | int]] = ())` — [`L284`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L284) — Lowers `model.forward` for `bucket_size` to StableHLO MLIR text via TorchTPU. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="normalize_mlir_text"></a>`normalize_mlir_text(text: str)` — [`L117`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L117) — Normalizes StableHLO MLIR text for portable consumption.
- <a id="set_aliasing_outputs"></a>`set_aliasing_outputs(mlir_text: str, aliases: Mapping[int, int])` — [`L134`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L134) — Marks each donated `@main` argument with the result that reuses its buffer.
- <a id="torch_dtype"></a>`torch_dtype(dt: Any)` — [`L109`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L109) — Converts a canonical dtype string or `torch.dtype` to `torch.dtype`. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)

## Module values
- <a id="_BY_NAME._BY_NAME"></a>`_BY_NAME` — [`L72`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L72)
- <a id="_DTYPE_SPECS._DTYPE_SPECS"></a>`_DTYPE_SPECS` — [`L39`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L39)
- <a id="_spec"></a>`_spec` — [`L73`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/tpu_lowering.py#L73)

