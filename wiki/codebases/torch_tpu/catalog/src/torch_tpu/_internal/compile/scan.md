---
title: 'Module: src/torch_tpu/_internal/compile/scan.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/scan.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.scan`/
symbols:
  _tpu_associative_scan: _tpu_associative_scan().
  _eager_tpu_associative_scan: _eager_tpu_associative_scan().
  key: key.
  _value_cache_key: _value_cache_key().
  _handle_scan_impl: _handle_scan_impl().
  _handle_associative_scan_impl: _handle_associative_scan_impl().
  _callable_cache_key: _callable_cache_key().
  _slice_placeholders: _slice_placeholders().
  _tpu_associative_scan_hop: _tpu_associative_scan_hop().
  _install_associative_scan_patch: _install_associative_scan_patch().
  _to_placeholder: _to_placeholder().
  _referenced_names: _referenced_names().
  _delegating_entrypoint: _delegating_entrypoint().
  _ASSOCIATIVE_BODY_MLIR_CACHE._ASSOCIATIVE_BODY_MLIR_CACHE: _ASSOCIATIVE_BODY_MLIR_CACHE._ASSOCIATIVE_BODY_MLIR_CACHE.
  _body_asks_for_reverse: _body_asks_for_reverse().
  _tpu_associative_scan_hop.run_flattened_associative_scan: _tpu_associative_scan_hop().run_flattened_associative_scan().
  _handle_scan_impl.to_fake: _handle_scan_impl().to_fake().
  _assoc_scan_module: _assoc_scan_module.
  _pin_offloaded_body_args: _pin_offloaded_body_args().
  _build_body_mlir: _build_body_mlir().
  _eager_tpu_associative_scan.flat_combine_fn: _eager_tpu_associative_scan().flat_combine_fn().
  SCAN_REVERSE_ANNOTATION: SCAN_REVERSE_ANNOTATION.
  _MAX_BODY_MLIR_CACHE_SIZE: _MAX_BODY_MLIR_CACHE_SIZE.
  _IMMUTABLE_SCALAR_TYPES: _IMMUTABLE_SCALAR_TYPES.
  _SAVED_ORIG_ASSOCIATIVE_SCAN: _SAVED_ORIG_ASSOCIATIVE_SCAN.
  _tpu_scan_dim: _tpu_scan_dim().
  _can_use_eager_fast_path: _can_use_eager_fast_path().
---
# Module: [`src/torch_tpu/_internal/compile/scan.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py)

## Functions
- <a id="_body_asks_for_reverse"></a>`_body_asks_for_reverse(combine_fn)` — [`L115`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L115)
- <a id="_build_body_mlir"></a>`_build_body_mlir(combine_fn, body_args)` — [`L216`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L216) — Traces `combine_fn` on `body_args` into an MLIR module with an `@main`.
- <a id="_callable_cache_key"></a>`_callable_cache_key(fn, seen=frozenset())` — [`L349`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L349) — Returns a hashable key that determines the body traced from `fn`, or None.
- <a id="_can_use_eager_fast_path"></a>`_can_use_eager_fast_path(combine_fn, leaves_xs, combine_mode)` — [`L545`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L545) — Returns whether `_eager_tpu_associative_scan` supports this call.
- <a id="_delegating_entrypoint"></a>`_delegating_entrypoint(combine_fn, xs, dim: int, reverse: bool = False, combine_mode: str = "pointwise")` — [`L651`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L651)
- <a id="_eager_tpu_associative_scan"></a>`_eager_tpu_associative_scan(combine_fn, leaves_xs: list[torch.Tensor], spec_xs: pytree.TreeSpec, dim: int, reverse: bool, combine_mode: str, fn_key: object)` — [`L397`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L397) — Runs `associative_scan` on TPU in eager mode as a single deferred op.
- <a id="_handle_associative_scan_impl"></a>`_handle_associative_scan_impl(combine_fn, xs, additional_inputs)` — [`L261`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L261) — TPU implementation for `torch.ops.higher_order.associative_scan`.
- <a id="_handle_scan_impl"></a>`_handle_scan_impl(combine_fn, init, xs, additional_inputs, reverse=False)` — [`L124`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L124) — TPU implementation for scan higher-order op.
- <a id="_install_associative_scan_patch"></a>`_install_associative_scan_patch()` — [`L665`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L665) — Routes `torch._higher_order_ops.associative_scan` to the TPU fast path.
- <a id="_pin_offloaded_body_args"></a>`_pin_offloaded_body_args(combine_fn, body_args)` — [`L59`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L59) — Returns `body_args` with the offloaded operands marked as host memory.
- <a id="_referenced_names"></a>`_referenced_names(code: types.CodeType)` — [`L320`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L320) — Returns the global/attribute names used by `code` and its nested code.
- <a id="_slice_placeholders"></a>`_slice_placeholders(xs_list, dim)` — [`L208`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L208) — Returns placeholders for one slice of each `xs` along `dim`.
- <a id="_to_placeholder"></a>`_to_placeholder(t, shape=None)` — [`L40`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L40) — Returns `t` as a like-shaped placeholder, or `t` itself if not a tensor.
- <a id="_tpu_associative_scan"></a>`_tpu_associative_scan(combine_fn, xs, dim: int, reverse: bool = False, combine_mode: str = "pointwise")` — [`L614`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L614) — TPU-aware replacement for `torch._higher_order_ops.associative_scan`.
- <a id="_tpu_associative_scan_hop"></a>`_tpu_associative_scan_hop(combine_fn, leaves_xs, spec_xs, dim: int, reverse: bool)` — [`L562`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L562) — Calls the `associative_scan` HOP for TPU inputs with `'pointwise'` mode.
- <a id="_tpu_scan_dim"></a>`_tpu_scan_dim(leaves_xs, dim, reverse)` — [`L524`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L524) — Returns the non-negative scan dim if the TPU paths apply, else None.
- <a id="_value_cache_key"></a>`_value_cache_key(value, seen)` — [`L329`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L329) — Returns a hashable key that pins down `value`, or None if it cannot.
- <a id="_eager_tpu_associative_scan.flat_combine_fn"></a>`flat_combine_fn(*flat_args)` — [`L441`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L441)
- <a id="_tpu_associative_scan_hop.run_flattened_associative_scan"></a>`run_flattened_associative_scan(combine_fn, leaves_xs)` — [`L598`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L598)
- <a id="_handle_scan_impl.to_fake"></a>`to_fake(tensors)` — [`L163`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L163)

## Module values
- <a id="SCAN_REVERSE_ANNOTATION"></a>`SCAN_REVERSE_ANNOTATION` — [`L112`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L112)
- <a id="_ASSOCIATIVE_BODY_MLIR_CACHE._ASSOCIATIVE_BODY_MLIR_CACHE"></a>`_ASSOCIATIVE_BODY_MLIR_CACHE` — [`L304`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L304)
- <a id="_IMMUTABLE_SCALAR_TYPES"></a>`_IMMUTABLE_SCALAR_TYPES` — [`L308`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L308)
- <a id="_MAX_BODY_MLIR_CACHE_SIZE"></a>`_MAX_BODY_MLIR_CACHE_SIZE` — [`L303`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L303)
- <a id="_SAVED_ORIG_ASSOCIATIVE_SCAN"></a>`_SAVED_ORIG_ASSOCIATIVE_SCAN` — [`L515`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L515)
- <a id="_assoc_scan_module"></a>`_assoc_scan_module` — [`L35`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L35)
- <a id="key"></a>`key` — [`L686`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/scan.py#L686)

