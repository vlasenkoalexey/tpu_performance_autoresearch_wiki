---
title: 'Module: src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.ops.scaled_mm.kernels.blockwise_scaled_mm_kernel_host_test`/
symbols:
  PreconditionValidationTest.test_contraction_mismatch_raises: PreconditionValidationTest#test_contraction_mismatch_raises().
  PreconditionValidationTest.test_scale_a_shape_mismatch_raises: PreconditionValidationTest#test_scale_a_shape_mismatch_raises().
  PreconditionValidationTest.test_scale_b_shape_mismatch_raises: PreconditionValidationTest#test_scale_b_shape_mismatch_raises().
  PreconditionValidationTest.test_k_not_divisible_by_block_size_raises: PreconditionValidationTest#test_k_not_divisible_by_block_size_raises().
  PreconditionValidationTest.test_tile_k_not_divisible_by_block_size_raises: PreconditionValidationTest#test_tile_k_not_divisible_by_block_size_raises().
  KernelGeneratorRegistryTest.test_register_custom_recipe: KernelGeneratorRegistryTest#test_register_custom_recipe().
  PreconditionValidationTest.sa: PreconditionValidationTest#sa.
  PreconditionValidationTest.sb: PreconditionValidationTest#sb.
  PreconditionValidationTest.block_size: PreconditionValidationTest#block_size.
  PreconditionValidationTest.a_q: PreconditionValidationTest#a_q.
  PreconditionValidationTest.b_q: PreconditionValidationTest#b_q.
  PreconditionValidationTest.k: PreconditionValidationTest#k.
  PreconditionValidationTest.n: PreconditionValidationTest#n.
  PreconditionValidationTest.m: PreconditionValidationTest#m.
  PadToTilesTest.test_pad_shapes_and_fill: PadToTilesTest#test_pad_shapes_and_fill().
  PadToTilesTest.test_already_aligned_is_noop: PadToTilesTest#test_already_aligned_is_noop().
  ExportTest.test_export_host_e4m3: ExportTest#test_export_host_e4m3().
  ExportTest.test_export_host_e5m2: ExportTest#test_export_host_e5m2().
  KernelGeneratorRegistryTest.test_supported_recipes_contains_mxfp8: KernelGeneratorRegistryTest#test_supported_recipes_contains_mxfp8().
  KernelGeneratorRegistryTest.test_generate_mxfp8_success: KernelGeneratorRegistryTest#test_generate_mxfp8_success().
  KernelGeneratorRegistryTest.test_unsupported_recipe_raises: KernelGeneratorRegistryTest#test_unsupported_recipe_raises().
  KernelGeneratorRegistryTest.test_unsupported_in_dtype_raises: KernelGeneratorRegistryTest#test_unsupported_in_dtype_raises().
  KernelGeneratorRegistryTest.test_unsupported_out_dtype_raises: KernelGeneratorRegistryTest#test_unsupported_out_dtype_raises().
  KernelGeneratorRegistryTest.dummy_generator: KernelGeneratorRegistryTest#dummy_generator().
  PreconditionValidationTest: PreconditionValidationTest#
  PreconditionValidationTest.setUp: PreconditionValidationTest#setUp().
  PadToTilesTest: PadToTilesTest#
  ExportTest: ExportTest#
  KernelGeneratorRegistryTest: KernelGeneratorRegistryTest#
---
# Module: [`src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py)

> **Collapsed catalog** (29 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="ExportTest"></a>`ExportTest` — [`L172`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L172)
- <a id="ExportTest.test_export_host_e4m3"></a>`ExportTest.test_export_host_e4m3` — [`L175`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L175)
- <a id="ExportTest.test_export_host_e5m2"></a>`ExportTest.test_export_host_e5m2` — [`L187`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L187)
- <a id="KernelGeneratorRegistryTest"></a>`KernelGeneratorRegistryTest` — [`L200`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L200)
- <a id="KernelGeneratorRegistryTest.dummy_generator"></a>`KernelGeneratorRegistryTest.dummy_generator` — [`L251`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L251)
- <a id="KernelGeneratorRegistryTest.test_generate_mxfp8_success"></a>`KernelGeneratorRegistryTest.test_generate_mxfp8_success` — [`L207`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L207)
- <a id="KernelGeneratorRegistryTest.test_register_custom_recipe"></a>`KernelGeneratorRegistryTest.test_register_custom_recipe` — [`L250`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L250)
- <a id="KernelGeneratorRegistryTest.test_supported_recipes_contains_mxfp8"></a>`KernelGeneratorRegistryTest.test_supported_recipes_contains_mxfp8` — [`L203`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L203)
- <a id="KernelGeneratorRegistryTest.test_unsupported_in_dtype_raises"></a>`KernelGeneratorRegistryTest.test_unsupported_in_dtype_raises` — [`L230`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L230)
- <a id="KernelGeneratorRegistryTest.test_unsupported_out_dtype_raises"></a>`KernelGeneratorRegistryTest.test_unsupported_out_dtype_raises` — [`L240`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L240)
- <a id="KernelGeneratorRegistryTest.test_unsupported_recipe_raises"></a>`KernelGeneratorRegistryTest.test_unsupported_recipe_raises` — [`L220`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L220)
- <a id="PadToTilesTest"></a>`PadToTilesTest` — [`L97`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L97)
- <a id="PadToTilesTest.test_already_aligned_is_noop"></a>`PadToTilesTest.test_already_aligned_is_noop` — [`L156`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L156)
- <a id="PadToTilesTest.test_pad_shapes_and_fill"></a>`PadToTilesTest.test_pad_shapes_and_fill` — [`L108`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L108)
- <a id="PreconditionValidationTest"></a>`PreconditionValidationTest` — [`L30`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L30)
- <a id="PreconditionValidationTest.a_q"></a>`PreconditionValidationTest.a_q` — [`L37`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L37)
- <a id="PreconditionValidationTest.b_q"></a>`PreconditionValidationTest.b_q` — [`L38`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L38)
- <a id="PreconditionValidationTest.block_size"></a>`PreconditionValidationTest.block_size` — [`L36`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L36)
- <a id="PreconditionValidationTest.k"></a>`PreconditionValidationTest.k` — [`L35`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L35)
- <a id="PreconditionValidationTest.m"></a>`PreconditionValidationTest.m` — [`L35`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L35)
- <a id="PreconditionValidationTest.n"></a>`PreconditionValidationTest.n` — [`L35`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L35)
- <a id="PreconditionValidationTest.sa"></a>`PreconditionValidationTest.sa` — [`L39`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L39)
- <a id="PreconditionValidationTest.sb"></a>`PreconditionValidationTest.sb` — [`L40`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L40)
- <a id="PreconditionValidationTest.setUp"></a>`PreconditionValidationTest.setUp` — [`L33`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L33)
- <a id="PreconditionValidationTest.test_contraction_mismatch_raises"></a>`PreconditionValidationTest.test_contraction_mismatch_raises` — [`L42`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L42) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="PreconditionValidationTest.test_k_not_divisible_by_block_size_raises"></a>`PreconditionValidationTest.test_k_not_divisible_by_block_size_raises` — [`L51`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L51)
- <a id="PreconditionValidationTest.test_scale_a_shape_mismatch_raises"></a>`PreconditionValidationTest.test_scale_a_shape_mismatch_raises` — [`L74`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L74) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="PreconditionValidationTest.test_scale_b_shape_mismatch_raises"></a>`PreconditionValidationTest.test_scale_b_shape_mismatch_raises` — [`L85`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L85)
- <a id="PreconditionValidationTest.test_tile_k_not_divisible_by_block_size_raises"></a>`PreconditionValidationTest.test_tile_k_not_divisible_by_block_size_raises` — [`L61`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_host_test.py#L61)
