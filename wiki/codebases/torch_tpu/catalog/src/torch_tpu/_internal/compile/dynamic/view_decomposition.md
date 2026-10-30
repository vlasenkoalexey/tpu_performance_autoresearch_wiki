---
title: 'Module: src/torch_tpu/_internal/compile/dynamic/view_decomposition.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/dynamic/view_decomposition.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.dynamic.view_decomposition`/
symbols:
  _fmt_sym: _fmt_sym().
  _decompose_layout: _decompose_layout().
  decompose_into_view_sequence: decompose_into_view_sequence().
  _build_body: _build_body().
  _delinearize_storage_offset: _delinearize_storage_offset().
  _build_unit_free_tail: _build_unit_free_tail().
  _assemble_slice_ops: _assemble_slice_ops().
  get_base_tensor: get_base_tensor().
  _is_contiguous_tensor: _is_contiguous_tensor().
  _build_tail: _build_tail().
  _div_expr: _div_expr().
  _compute_base_strides_and_shapes: _compute_base_strides_and_shapes().
  _validate_dimension_slice: _validate_dimension_slice().
  _to_sym: _to_sym().
  _is_unit_dim: _is_unit_dim().
  needs_view_decomposition: needs_view_decomposition().
  _to_expr: _to_expr().
  _hint: _hint().
  _build_tail._cmp_strides: _build_tail()._cmp_strides().
  _assemble_canonical_view_ops: _assemble_canonical_view_ops().
---
# Module: [`src/torch_tpu/_internal/compile/dynamic/view_decomposition.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py)

## Functions
- <a id="_assemble_canonical_view_ops"></a>`_assemble_canonical_view_ops(slice_ops: Sequence[tuple[int, Any, Any, Any]], perm_list: Sequence[int] | None)` — [`L597`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L597) — Assembles canonical FX view operations (slice, permute).
- <a id="_assemble_slice_ops"></a>`_assemble_slice_ops(phys_shape: Sequence[Any], phys_strides: Sequence[Any], dim_offsets: Sequence[Any], base_shape: list[Any], base_strides: Sequence[Any], compute_slice_ops: bool = True)` — [`L437`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L437) — Generates canonical slice operations after verifying dimension bounds and divisibility.
- <a id="_build_body"></a>`_build_body(phys_shape: Sequence[Any], phys_strides: Sequence[Any], storage_offset: Any, compute_slice_ops: bool = True)` — [`L567`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L567) — Computes per-dimension contiguous base shape and slice operations.
- <a id="_build_tail"></a>`_build_tail(shape: Sequence[Any], strides: Sequence[Any])` — [`L165`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L165) — Sorts dimensions into descending physical stride order and computes permutation.
- <a id="_build_unit_free_tail"></a>`_build_unit_free_tail(shape: Sequence[Any], strides: Sequence[Any])` — [`L222`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L222) — Like `_build_tail`, but orders size-1 dims innermost with stride 1.
- <a id="_build_tail._cmp_strides"></a>`_cmp_strides(a_idx: int, b_idx: int)` — [`L188`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L188)
- <a id="_compute_base_strides_and_shapes"></a>`_compute_base_strides_and_shapes(phys_shape: Sequence[Any], phys_strides: Sequence[Any])` — [`L310`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L310) — Computes contiguous base strides and shapes assuming slice step=1.
- <a id="_decompose_layout"></a>`_decompose_layout(val: torch.Tensor, compute_slice_ops: bool = True)` — [`L622`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L622) — Computes the base shape, slice ops and permutation of a non-contiguous view. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
- <a id="_delinearize_storage_offset"></a>`_delinearize_storage_offset(storage_offset: Any, base_strides: Sequence[Any])` — [`L237`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L237) — Converts a 1D linear storage offset into per-dimension coordinate offsets.
- <a id="_div_expr"></a>`_div_expr(curr_expr: Any, st_expr: Any)` — [`L83`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L83) — Performs algebraic polynomial division on SymPy expressions.
- <a id="_fmt_sym"></a>`_fmt_sym(val: Any)` — [`L30`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L30) — Formats a numeric value for debug logging.
- <a id="_hint"></a>`_hint(val: Any)` — [`L611`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L611) — Returns the concrete value of an int or the traced example value of a SymInt.
- <a id="_is_contiguous_tensor"></a>`_is_contiguous_tensor(val: Any)` — [`L118`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L118) — Checks if a tensor or FakeTensor metadata represents a standard contiguous layout.
- <a id="_is_unit_dim"></a>`_is_unit_dim(size: Any)` — [`L104`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L104) — Returns whether a dimension is statically known to have size 1.
- <a id="_to_expr"></a>`_to_expr(val: Any)` — [`L38`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L38) — Extracts or converts a PyTorch value to a SymPy expression.
- <a id="_to_sym"></a>`_to_sym(expr: Any, shape_env: Any)` — [`L59`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L59) — Converts a SymPy expression back to a PyTorch representation (int or SymInt).
- <a id="_validate_dimension_slice"></a>`_validate_dimension_slice(dim_idx: int, size: Any, stride: Any, prev_stride: Any, dim_offset: Any, base_size: Any, is_reshaped_dim: bool)` — [`L369`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L369) — Validates that slice fits within base bounds and enforces divisibility guards.
- <a id="decompose_into_view_sequence"></a>`decompose_into_view_sequence(node_or_val: torch.fx.Node | torch.Tensor)` — [`L667`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L667) — Decomposes a non-contiguous view tensor or placeholder into:
- <a id="get_base_tensor"></a>`get_base_tensor(tensor: torch.Tensor)` — [`L714`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L714) — Reconstructs the contiguous base tensor view for a runtime view tensor.
- <a id="needs_view_decomposition"></a>`needs_view_decomposition(node_or_tensor: torch.fx.Node | torch.Tensor)` — [`L151`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_decomposition.py#L151) — Checks if an FX node or runtime tensor requires view decomposition.

