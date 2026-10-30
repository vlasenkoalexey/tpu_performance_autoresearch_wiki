---
title: 'Module: src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.ops.scaled_mm.kernels.blockwise128_scaled_mm_kernel_host_test`/
symbols:
  PadToTilesTest.test_pad_shapes_and_fill: PadToTilesTest#test_pad_shapes_and_fill().
  _BLOCK_SIZE: _BLOCK_SIZE.
  _TestCase: _TestCase.
  ExportSymbolicShapesTest.test_get_shapes_bias_is_n_vector: ExportSymbolicShapesTest#test_get_shapes_bias_is_n_vector().
  RecipeRegistryTest.test_generate_kernel_module: RecipeRegistryTest#test_generate_kernel_module().
  ExpandScaleAxisTest: ExpandScaleAxisTest#
  ExpandScaleAxisTest.test_block_one_is_noop: ExpandScaleAxisTest#test_block_one_is_noop().
  ExpandScaleAxisTest.test_expand_axis1_full_bands: ExpandScaleAxisTest#test_expand_axis1_full_bands().
  ExpandScaleAxisTest.test_expand_axis1_partial_trailing_band: ExpandScaleAxisTest#test_expand_axis1_partial_trailing_band().
  ExpandScaleAxisTest.test_expand_axis0_partial_trailing_band: ExpandScaleAxisTest#test_expand_axis0_partial_trailing_band().
  CeilDivTest: CeilDivTest#
  CeilDivTest.test_ceil_div: CeilDivTest#test_ceil_div().
  PadToTilesTest: PadToTilesTest#
  PadBiasTest: PadBiasTest#
  PadBiasTest.test_bias_padding: PadBiasTest#test_bias_padding().
  ExportSymbolicShapesTest: ExportSymbolicShapesTest#
  ExportSymbolicShapesTest.test_export_mlir_module: ExportSymbolicShapesTest#test_export_mlir_module().
  ExportSymbolicShapesTest.test_export_rejects_non_128_block_size: ExportSymbolicShapesTest#test_export_rejects_non_128_block_size().
  ExportSymbolicShapesTest.test_get_shapes_without_bias: ExportSymbolicShapesTest#test_get_shapes_without_bias().
  RecipeRegistryTest: RecipeRegistryTest#
  RecipeRegistryTest.test_recipe_is_registered: RecipeRegistryTest#test_recipe_is_registered().
---
# Module: [`src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py)

> **Collapsed catalog** (21 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="CeilDivTest"></a>`CeilDivTest` — [`L63`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L63)
- <a id="CeilDivTest.test_ceil_div"></a>`CeilDivTest.test_ceil_div` — [`L71`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L71)
- <a id="ExpandScaleAxisTest"></a>`ExpandScaleAxisTest` — [`L29`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L29)
- <a id="ExpandScaleAxisTest.test_block_one_is_noop"></a>`ExpandScaleAxisTest.test_block_one_is_noop` — [`L32`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L32)
- <a id="ExpandScaleAxisTest.test_expand_axis0_partial_trailing_band"></a>`ExpandScaleAxisTest.test_expand_axis0_partial_trailing_band` — [`L54`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L54)
- <a id="ExpandScaleAxisTest.test_expand_axis1_full_bands"></a>`ExpandScaleAxisTest.test_expand_axis1_full_bands` — [`L37`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L37)
- <a id="ExpandScaleAxisTest.test_expand_axis1_partial_trailing_band"></a>`ExpandScaleAxisTest.test_expand_axis1_partial_trailing_band` — [`L45`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L45)
- <a id="ExportSymbolicShapesTest"></a>`ExportSymbolicShapesTest` — [`L142`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L142)
- <a id="ExportSymbolicShapesTest.test_export_mlir_module"></a>`ExportSymbolicShapesTest.test_export_mlir_module` — [`L152`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L152) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="ExportSymbolicShapesTest.test_export_rejects_non_128_block_size"></a>`ExportSymbolicShapesTest.test_export_rejects_non_128_block_size` — [`L160`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L160)
- <a id="ExportSymbolicShapesTest.test_get_shapes_bias_is_n_vector"></a>`ExportSymbolicShapesTest.test_get_shapes_bias_is_n_vector` — [`L166`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L166)
- <a id="ExportSymbolicShapesTest.test_get_shapes_without_bias"></a>`ExportSymbolicShapesTest.test_get_shapes_without_bias` — [`L176`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L176)
- <a id="PadBiasTest"></a>`PadBiasTest` — [`L131`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L131)
- <a id="PadBiasTest.test_bias_padding"></a>`PadBiasTest.test_bias_padding` — [`L134`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L134)
- <a id="PadToTilesTest"></a>`PadToTilesTest` — [`L75`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L75)
- <a id="PadToTilesTest.test_pad_shapes_and_fill"></a>`PadToTilesTest.test_pad_shapes_and_fill` — [`L87`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L87)
- <a id="RecipeRegistryTest"></a>`RecipeRegistryTest` — [`L181`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L181)
- <a id="RecipeRegistryTest.test_generate_kernel_module"></a>`RecipeRegistryTest.test_generate_kernel_module` — [`L191`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L191) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="RecipeRegistryTest.test_recipe_is_registered"></a>`RecipeRegistryTest.test_recipe_is_registered` — [`L184`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L184)
- <a id="_BLOCK_SIZE"></a>`_BLOCK_SIZE` — [`L22`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L22)
- <a id="_TestCase"></a>`_TestCase` — [`L26`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_host_test.py#L26)
