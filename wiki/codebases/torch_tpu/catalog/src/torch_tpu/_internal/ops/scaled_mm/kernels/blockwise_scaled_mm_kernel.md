---
title: 'Module: src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.ops.scaled_mm.kernels.blockwise_scaled_mm_kernel`/
symbols:
  blockwise_scaled_mm: blockwise_scaled_mm().
  export_mlir_module: export_mlir_module().
  _pad_to_tiles: _pad_to_tiles().
  _maybe_use_abstract_tpu_mesh: _maybe_use_abstract_tpu_mesh().
  _next_multiple: _next_multiple().
  pallas_export_experimental: pallas_export_experimental.
  _DEFAULT_TILE_M: _DEFAULT_TILE_M.
  _DEFAULT_TILE_N: _DEFAULT_TILE_N.
  _DEFAULT_TILE_K: _DEFAULT_TILE_K.
  _blockwise_scaled_mm_kernel: _blockwise_scaled_mm_kernel().
  _make_abstract_device: _make_abstract_device().
  get_shapes: get_shapes().
  _VREG_SUBLANE_TILE: _VREG_SUBLANE_TILE.
  _VREG_LANE_TILE: _VREG_LANE_TILE.
---
# Module: [`src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py)

## Functions
- <a id="_blockwise_scaled_mm_kernel"></a>`_blockwise_scaled_mm_kernel(a_ref, b_ref, sa_ref, sb_ref, out_ref, acc_ref, *, block_size: int, steps_k: int, transpose_rhs: bool = False)` — [`L117`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py#L117) — Accumulates one [tile_m, tile_n] output tile across K blocks. — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_make_abstract_device"></a>`_make_abstract_device(device_kind: str, num_cores: int, platform: str)` — [`L313`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py#L313)
- <a id="_maybe_use_abstract_tpu_mesh"></a>`_maybe_use_abstract_tpu_mesh()` — [`L320`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py#L320) — Uses an abstract TPU mesh when exporting without a TPU (build time). — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_next_multiple"></a>`_next_multiple(x: int, multiple: int)` — [`L53`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py#L53)
- <a id="_pad_to_tiles"></a>`_pad_to_tiles(a: jax.Array, b: jax.Array, scale_a: jax.Array, scale_b: jax.Array, *, tile_m: int, tile_n: int, tile_k: int, block_size: int, transpose_rhs: bool = False)` — [`L58`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py#L58) — Zero-pads the operands and block scales up to exact tile multiples. — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="blockwise_scaled_mm"></a>`blockwise_scaled_mm(a: jax.Array, b: jax.Array, scale_a: jax.Array, scale_b: jax.Array, *, block_size: int = 32, out_dtype: Any = jnp.bfloat16, tile_m: int = _DEFAULT_TILE_M, tile_n: int = _DEFAULT_TILE_N, tile_k: int = _DEFAULT_TILE_K, transpose_rhs: bool = False)` — [`L183`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py#L183) — Block-scaled FP8 matmul: returns `a @ b` with per-block scales applied. — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="export_mlir_module"></a>`export_mlir_module(*, block_size: int = 32, out_dtype: Any = jnp.float32, in_dtype: Any = jnp.float8_e4m3fn, tile_m: int = 128, tile_n: int = 128, tile_k: int = 256)` — [`L368`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py#L368) — Exports the kernel and returns the serialized MLIR module string. — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="get_shapes"></a>`get_shapes(*, block_size: int, tile_m: int, tile_n: int, tile_k: int, in_dtype: Any = jnp.float8_e4m3fn)` — [`L335`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py#L335) — Symbolic input shapes `(a, b, scale_a, scale_b)` for AOT export. — documented in [python-ops](../../../../../../../concepts/python-ops.md)

## Module values
- <a id="_DEFAULT_TILE_K"></a>`_DEFAULT_TILE_K` — [`L46`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py#L46) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_DEFAULT_TILE_M"></a>`_DEFAULT_TILE_M` — [`L44`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py#L44) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_DEFAULT_TILE_N"></a>`_DEFAULT_TILE_N` — [`L45`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py#L45) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_VREG_LANE_TILE"></a>`_VREG_LANE_TILE` — [`L50`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py#L50)
- <a id="_VREG_SUBLANE_TILE"></a>`_VREG_SUBLANE_TILE` — [`L49`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py#L49)
- <a id="pallas_export_experimental"></a>`pallas_export_experimental` — [`L41`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel.py#L41) — documented in [python-ops](../../../../../../../concepts/python-ops.md)

