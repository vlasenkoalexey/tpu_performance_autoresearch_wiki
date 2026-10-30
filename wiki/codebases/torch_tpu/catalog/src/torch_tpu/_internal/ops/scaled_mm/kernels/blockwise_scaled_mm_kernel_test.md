---
title: 'Module: src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.ops.scaled_mm.kernels.blockwise_scaled_mm_kernel_test`/
symbols:
  BlockwiseScaledMmRandomTest.test_random_exact_e4m3_scales_one: BlockwiseScaledMmRandomTest#test_random_exact_e4m3_scales_one().
  BlockwiseScaledMmRandomTest.test_random_data_derived_scales: BlockwiseScaledMmRandomTest#test_random_data_derived_scales().
  _BLOCK_SIZE: _BLOCK_SIZE.
  _FP8_E4M3: _FP8_E4M3.
  BlockwiseScaledMmStructuralTest.test_a_scale_marker: BlockwiseScaledMmStructuralTest#test_a_scale_marker().
  BlockwiseScaledMmStructuralTest.test_b_scale_marker: BlockwiseScaledMmStructuralTest#test_b_scale_marker().
  _mx_quantize: _mx_quantize().
  _run_kernel: _run_kernel().
  BlockwiseScaledMmStructuralTest.test_a_payload_marker: BlockwiseScaledMmStructuralTest#test_a_payload_marker().
  BlockwiseScaledMmStructuralTest.test_b_payload_marker: BlockwiseScaledMmStructuralTest#test_b_payload_marker().
  BlockwiseScaledMmEdgeCaseTest.test_fp8_saturation: BlockwiseScaledMmEdgeCaseTest#test_fp8_saturation().
  _BlockwiseScaledMmTestBase: _BlockwiseScaledMmTestBase#
  BlockwiseScaledMmStructuralTest.test_a_eye_b_eye: BlockwiseScaledMmStructuralTest#test_a_eye_b_eye().
  BlockwiseScaledMmStructuralTest.test_a_ones_b_ones: BlockwiseScaledMmStructuralTest#test_a_ones_b_ones().
  _decode: _decode().
  _reference_matmul: _reference_matmul().
  _random_e4m3: _random_e4m3().
  _MARKER_SHAPES: _MARKER_SHAPES.
  _E4M3_MAX: _E4M3_MAX.
  _SHAPES: _SHAPES.
  _SQUARE_SHAPES: _SQUARE_SHAPES.
  _COSINE_SIM_FLOOR: _COSINE_SIM_FLOOR.
  _cosine_similarity: _cosine_similarity().
  BlockwiseScaledMmStructuralTest: BlockwiseScaledMmStructuralTest#
  BlockwiseScaledMmRandomTest: BlockwiseScaledMmRandomTest#
  BlockwiseScaledMmEdgeCaseTest: BlockwiseScaledMmEdgeCaseTest#
  _F8E8M0_EXP_BIAS: _F8E8M0_EXP_BIAS.
  _BF16_RTOL: _BF16_RTOL.
  _BF16_ATOL: _BF16_ATOL.
  _max_abs_error: _max_abs_error().
  _F8E4M3_LARGEST_POW2: _F8E4M3_LARGEST_POW2.
  _BlockwiseScaledMmTestBase.setUp: _BlockwiseScaledMmTestBase#setUp().
---
# Module: [`src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py)

> **Collapsed catalog** (32 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="BlockwiseScaledMmEdgeCaseTest"></a>`BlockwiseScaledMmEdgeCaseTest` — [`L346`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L346)
- <a id="BlockwiseScaledMmEdgeCaseTest.test_fp8_saturation"></a>`BlockwiseScaledMmEdgeCaseTest.test_fp8_saturation` — [`L349`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L349) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
- <a id="BlockwiseScaledMmRandomTest"></a>`BlockwiseScaledMmRandomTest` — [`L283`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L283)
- <a id="BlockwiseScaledMmRandomTest.test_random_data_derived_scales"></a>`BlockwiseScaledMmRandomTest.test_random_data_derived_scales` — [`L312`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L312)
- <a id="BlockwiseScaledMmRandomTest.test_random_exact_e4m3_scales_one"></a>`BlockwiseScaledMmRandomTest.test_random_exact_e4m3_scales_one` — [`L287`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L287)
- <a id="BlockwiseScaledMmStructuralTest"></a>`BlockwiseScaledMmStructuralTest` — [`L190`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L190)
- <a id="BlockwiseScaledMmStructuralTest.test_a_eye_b_eye"></a>`BlockwiseScaledMmStructuralTest.test_a_eye_b_eye` — [`L193`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L193)
- <a id="BlockwiseScaledMmStructuralTest.test_a_ones_b_ones"></a>`BlockwiseScaledMmStructuralTest.test_a_ones_b_ones` — [`L204`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L204)
- <a id="BlockwiseScaledMmStructuralTest.test_a_payload_marker"></a>`BlockwiseScaledMmStructuralTest.test_a_payload_marker` — [`L215`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L215)
- <a id="BlockwiseScaledMmStructuralTest.test_a_scale_marker"></a>`BlockwiseScaledMmStructuralTest.test_a_scale_marker` — [`L243`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L243)
- <a id="BlockwiseScaledMmStructuralTest.test_b_payload_marker"></a>`BlockwiseScaledMmStructuralTest.test_b_payload_marker` — [`L229`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L229)
- <a id="BlockwiseScaledMmStructuralTest.test_b_scale_marker"></a>`BlockwiseScaledMmStructuralTest.test_b_scale_marker` — [`L263`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L263)
- <a id="_BF16_ATOL"></a>`_BF16_ATOL` — [`L52`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L52)
- <a id="_BF16_RTOL"></a>`_BF16_RTOL` — [`L51`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L51)
- <a id="_BLOCK_SIZE"></a>`_BLOCK_SIZE` — [`L86`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L86)
- <a id="_BlockwiseScaledMmTestBase"></a>`_BlockwiseScaledMmTestBase` — [`L179`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L179)
- <a id="_BlockwiseScaledMmTestBase.setUp"></a>`_BlockwiseScaledMmTestBase.setUp` — [`L182`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L182)
- <a id="_COSINE_SIM_FLOOR"></a>`_COSINE_SIM_FLOOR` — [`L50`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L50)
- <a id="_E4M3_MAX"></a>`_E4M3_MAX` — [`L43`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L43)
- <a id="_F8E4M3_LARGEST_POW2"></a>`_F8E4M3_LARGEST_POW2` — [`L45`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L45)
- <a id="_F8E8M0_EXP_BIAS"></a>`_F8E8M0_EXP_BIAS` — [`L46`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L46)
- <a id="_FP8_E4M3"></a>`_FP8_E4M3` — [`L42`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L42)
- <a id="_MARKER_SHAPES"></a>`_MARKER_SHAPES` — [`L80`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L80)
- <a id="_SHAPES"></a>`_SHAPES` — [`L56`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L56)
- <a id="_SQUARE_SHAPES"></a>`_SQUARE_SHAPES` — [`L75`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L75)
- <a id="_cosine_similarity"></a>`_cosine_similarity` — [`L89`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L89)
- <a id="_decode"></a>`_decode` — [`L119`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L119)
- <a id="_max_abs_error"></a>`_max_abs_error` — [`L100`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L100)
- <a id="_mx_quantize"></a>`_mx_quantize` — [`L152`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L152)
- <a id="_random_e4m3"></a>`_random_e4m3` — [`L136`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L136)
- <a id="_reference_matmul"></a>`_reference_matmul` — [`L131`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L131)
- <a id="_run_kernel"></a>`_run_kernel` — [`L106`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise_scaled_mm_kernel_test.py#L106) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
