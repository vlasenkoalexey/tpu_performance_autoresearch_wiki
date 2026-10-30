---
title: 'Module: src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.ops.scaled_mm.kernels.blockwise128_scaled_mm_kernel`/
symbols:
  export_mlir_module: export_mlir_module().
  _blockwise128_scaled_mm: _blockwise128_scaled_mm().
  scaled_mm_1x128_128x128: scaled_mm_1x128_128x128().
  _BLOCK_SIZE: _BLOCK_SIZE.
  _pad_to_tiles: _pad_to_tiles().
  _ceil_div: _ceil_div.
  _expand_scale_axis: _expand_scale_axis().
  get_shapes: get_shapes().
  _maybe_use_abstract_tpu_mesh: _maybe_use_abstract_tpu_mesh().
  _next_multiple: _next_multiple().
  _DEFAULT_TILE_M: _DEFAULT_TILE_M.
  _DEFAULT_TILE_N: _DEFAULT_TILE_N.
  _DEFAULT_TILE_K: _DEFAULT_TILE_K.
  _pad_bias: _pad_bias().
  make_abstract_device: make_abstract_device().
  _blockwise_scaled_mm_kernel: _blockwise_scaled_mm_kernel().
---
# Module: [`src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py)

## Functions
- <a id="_blockwise128_scaled_mm"></a>`_blockwise128_scaled_mm(a: jax.Array, b: jax.Array, scale_a: jax.Array, scale_b: jax.Array, *, scale_block_m: int, scale_block_n: int, out_dtype: Any, tile_m: int, tile_n: int, tile_k: int, bias: jax.Array | None = None)` — [`L179`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py#L179) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_blockwise_scaled_mm_kernel"></a>`_blockwise_scaled_mm_kernel(a_ref, b_ref, sa_ref, sb_ref, *args, block_size: int, steps_k: int, has_bias: bool = False)` — [`L126`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py#L126) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_expand_scale_axis"></a>`_expand_scale_axis(scale: jax.Array, block: int, *, axis: int, size: int)` — [`L68`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py#L68) — Expands a coarse block-level scale into a per-element scale along `axis` by repeating each entry `block` times. — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_maybe_use_abstract_tpu_mesh"></a>`_maybe_use_abstract_tpu_mesh()` — [`L356`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py#L356) — Uses an abstract TPU mesh when exporting without a TPU (build time).
- <a id="_next_multiple"></a>`_next_multiple(x: int, multiple: int)` — [`L61`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py#L61)
- <a id="_pad_bias"></a>`_pad_bias(bias: jax.Array, n: int, padded_n: int)` — [`L119`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py#L119) — Zero-pads the bias up to the exact column tile multiple. — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_pad_to_tiles"></a>`_pad_to_tiles(a: jax.Array, b: jax.Array, scale_a: jax.Array, scale_b: jax.Array, *, tile_m: int, tile_n: int, tile_k: int, block_size: int)` — [`L86`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py#L86) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="export_mlir_module"></a>`export_mlir_module(*, block_size: int = _BLOCK_SIZE, in_dtype: Any = jnp.float8_e4m3fn, out_dtype: Any = jnp.bfloat16, tile_m: int = _DEFAULT_TILE_M, tile_n: int = _DEFAULT_TILE_N, tile_k: int = _DEFAULT_TILE_K, has_bias: bool = False)` — [`L399`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py#L399) — Exports the kernel and returns the serialized MLIR module string. — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="get_shapes"></a>`get_shapes(*, in_dtype: Any = jnp.float8_e4m3fn, has_bias: bool = False)` — [`L371`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py#L371) — Symbolic input shapes for AOT export, as `(positional_args, bias)`. — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="make_abstract_device"></a>`make_abstract_device(device_kind: str = "TPU v6e", num_cores: int = 1, platform: str = "tpu")` — [`L52`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py#L52) — Compatible across Google3 HEAD (with platform) and OSS jax==0.9.2 (without platform).
- <a id="scaled_mm_1x128_128x128"></a>`scaled_mm_1x128_128x128(a: jax.Array, b: jax.Array, scale_a: jax.Array, scale_b: jax.Array, *, out_dtype: jnp.dtype = jnp.bfloat16, tile_m: int = _DEFAULT_TILE_M, tile_n: int = _DEFAULT_TILE_N, tile_k: int = _DEFAULT_TILE_K, bias: jax.Array | None = None)` — [`L328`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py#L328) — documented in [python-ops](../../../../../../../concepts/python-ops.md)

## Module values
- <a id="_BLOCK_SIZE"></a>`_BLOCK_SIZE` — [`L49`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py#L49) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_DEFAULT_TILE_K"></a>`_DEFAULT_TILE_K` — [`L47`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py#L47) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_DEFAULT_TILE_M"></a>`_DEFAULT_TILE_M` — [`L45`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py#L45) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_DEFAULT_TILE_N"></a>`_DEFAULT_TILE_N` — [`L46`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py#L46) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_ceil_div"></a>`_ceil_div` — [`L65`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel.py#L65)

