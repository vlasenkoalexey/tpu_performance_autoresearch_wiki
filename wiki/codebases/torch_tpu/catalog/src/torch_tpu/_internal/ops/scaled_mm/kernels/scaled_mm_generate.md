---
title: 'Module: src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.ops.scaled_mm.kernels.scaled_mm_generate`/
symbols:
  main: main().
  generate_kernel_module: generate_kernel_module().
  _RECIPE_GENERATORS._RECIPE_GENERATORS: _RECIPE_GENERATORS._RECIPE_GENERATORS.
  get_supported_recipes: get_supported_recipes().
  _generate_mxfp8: _generate_mxfp8().
  _generate_blockwise_128: _generate_blockwise_128().
  register_recipe: register_recipe().
  _HEADER: _HEADER.
  _IMPLEMENTATION: _IMPLEMENTATION.
  _KERNEL_NAME: _KERNEL_NAME.
  _RECIPE: _RECIPE.
  _IN_DTYPE: _IN_DTYPE.
  _OUT_DTYPE: _OUT_DTYPE.
  _BLOCK_SIZE: _BLOCK_SIZE.
  _TILE_M: _TILE_M.
  _TILE_N: _TILE_N.
  _TILE_K: _TILE_K.
  _HAS_BIAS: _HAS_BIAS.
  _get_in_dtype: _get_in_dtype().
  _get_out_dtype: _get_out_dtype().
---
# Module: [`src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py)

## Functions
- <a id="_generate_blockwise_128"></a>`_generate_blockwise_128(*, in_dtype: Any, out_dtype: Any, block_size: int, tile_m: int, tile_n: int, tile_k: int, has_bias: bool = False, **kwargs: Any)` — [`L162`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L162) — Generates BlockWise1x128 x BlockWise128x128 StableHLO MLIR module string. — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_generate_mxfp8"></a>`_generate_mxfp8(*, in_dtype: Any, out_dtype: Any, block_size: int, tile_m: int, tile_n: int, tile_k: int, has_bias: bool = False, **kwargs: Any)` — [`L135`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L135) — Generates MXFP8 (1x32 block scaling) StableHLO MLIR module string. — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_get_in_dtype"></a>`_get_in_dtype(name: str)` — [`L95`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L95)
- <a id="_get_out_dtype"></a>`_get_out_dtype(name: str)` — [`L104`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L104)
- <a id="generate_kernel_module"></a>`generate_kernel_module(recipe: str, in_dtype_name: str, out_dtype_name: str, block_size: int = 32, tile_m: int = 128, tile_n: int = 128, tile_k: int = 256, has_bias: bool = False, **kwargs: Any)` — [`L210`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L210) — Generates a StableHLO MLIR module string for the specified recipe. — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="get_supported_recipes"></a>`get_supported_recipes()` — [`L205`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L205) — Returns the sorted list of registered recipe names. — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="main"></a>`main(argv: Sequence[str])` — [`L259`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L259) — documented in [pallas-custom-kernels](../../../../../../../concepts/pallas-custom-kernels.md)
- <a id="register_recipe"></a>`register_recipe(name: str, generator: Callable[..., str])` — [`L193`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L193) — Registers a kernel generator for a block-scaling recipe. — documented in [python-ops](../../../../../../../concepts/python-ops.md)

## Module values
- <a id="_BLOCK_SIZE"></a>`_BLOCK_SIZE` — [`L64`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L64) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_HAS_BIAS"></a>`_HAS_BIAS` — [`L88`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L88)
- <a id="_HEADER"></a>`_HEADER` — [`L27`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L27)
- <a id="_IMPLEMENTATION"></a>`_IMPLEMENTATION` — [`L33`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L33)
- <a id="_IN_DTYPE"></a>`_IN_DTYPE` — [`L52`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L52)
- <a id="_KERNEL_NAME"></a>`_KERNEL_NAME` — [`L39`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L39) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_OUT_DTYPE"></a>`_OUT_DTYPE` — [`L58`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L58)
- <a id="_RECIPE"></a>`_RECIPE` — [`L45`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L45) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_RECIPE_GENERATORS._RECIPE_GENERATORS"></a>`_RECIPE_GENERATORS` — [`L186`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L186) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_TILE_K"></a>`_TILE_K` — [`L82`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L82) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="_TILE_M"></a>`_TILE_M` — [`L70`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L70)
- <a id="_TILE_N"></a>`_TILE_N` — [`L76`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/scaled_mm_generate.py#L76)

