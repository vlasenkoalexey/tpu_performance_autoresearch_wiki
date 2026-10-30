---
title: 'Module: src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.ops.scaled_mm.kernels.blockwise128_scaled_mm_kernel_test`/
symbols:
  _FP8_E4M3: _FP8_E4M3.
  BlockWise128ScaledMmStructuralTest.test_a_scale_marker: BlockWise128ScaledMmStructuralTest#test_a_scale_marker().
  BlockWise128ScaledMmRandomTest.test_random_data_derived_scales: BlockWise128ScaledMmRandomTest#test_random_data_derived_scales().
  _BLOCK_SIZE: _BLOCK_SIZE.
  BlockWise128ScaledMmStructuralTest.test_a_payload_marker: BlockWise128ScaledMmStructuralTest#test_a_payload_marker().
  BlockWise128ScaledMmStructuralTest.test_b_payload_marker: BlockWise128ScaledMmStructuralTest#test_b_payload_marker().
  BlockWise128ScaledMmStructuralTest.test_b_scale_marker: BlockWise128ScaledMmStructuralTest#test_b_scale_marker().
  BlockWise128ScaledMmStructuralTest.test_b_scale_tail_corner_marker: BlockWise128ScaledMmStructuralTest#test_b_scale_tail_corner_marker().
  BlockWise128ScaledMmRandomTest.test_random_exact_e4m3_scales_one: BlockWise128ScaledMmRandomTest#test_random_exact_e4m3_scales_one().
  _run_kernel: _run_kernel().
  BlockWise128ScaledMmStructuralTest.test_a_eye_b_eye: BlockWise128ScaledMmStructuralTest#test_a_eye_b_eye().
  BlockWise128ScaledMmStructuralTest.test_a_ones_b_ones: BlockWise128ScaledMmStructuralTest#test_a_ones_b_ones().
  BlockWise128ScaledMmStructuralTest.test_bias_added: BlockWise128ScaledMmStructuralTest#test_bias_added().
  BlockWise128ScaledMmRandomTest._assert_pytorch_gates: BlockWise128ScaledMmRandomTest#_assert_pytorch_gates().
  _ones_sa: _ones_sa().
  _ones_sb: _ones_sb().
  BlockWise128ScaledMmRandomTest.test_random_bias_isolation: BlockWise128ScaledMmRandomTest#test_random_bias_isolation().
  _reference_matmul: _reference_matmul().
  _quantize_blocked: _quantize_blocked().
  _DERIVED_DTYPE_SHAPES: _DERIVED_DTYPE_SHAPES.
  _STRUCTURAL_TILE: _STRUCTURAL_TILE.
  _ALIGNED_SHAPES: _ALIGNED_SHAPES.
  _BIAS_ISOLATION_SHAPES: _BIAS_ISOLATION_SHAPES.
  _EXACT_DTYPE_SHAPES: _EXACT_DTYPE_SHAPES.
  _dequant_b: _dequant_b().
  _COSINE_FLOOR: _COSINE_FLOOR.
  _dequant_a: _dequant_a().
  _E4M3_MAX: _E4M3_MAX.
  _SHAPES: _SHAPES.
  _cosine: _cosine().
  BlockWise128ScaledMmStructuralTest: BlockWise128ScaledMmStructuralTest#
  BlockWise128ScaledMmRandomTest: BlockWise128ScaledMmRandomTest#
  _LARGE_SHAPES: _LARGE_SHAPES.
  _RANDOM_DTYPES: _RANDOM_DTYPES.
  _TestCase: _TestCase.
  _ATOL_RTOL: _ATOL_RTOL.
  _cast_ref: _cast_ref().
---
# Module: [`src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py)

> **Collapsed catalog** (37 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="BlockWise128ScaledMmRandomTest"></a>`BlockWise128ScaledMmRandomTest` — [`L305`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L305)
- <a id="BlockWise128ScaledMmRandomTest._assert_pytorch_gates"></a>`BlockWise128ScaledMmRandomTest._assert_pytorch_gates` — [`L312`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L312)
- <a id="BlockWise128ScaledMmRandomTest.test_random_bias_isolation"></a>`BlockWise128ScaledMmRandomTest.test_random_bias_isolation` — [`L406`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L406)
- <a id="BlockWise128ScaledMmRandomTest.test_random_data_derived_scales"></a>`BlockWise128ScaledMmRandomTest.test_random_data_derived_scales` — [`L386`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L386)
- <a id="BlockWise128ScaledMmRandomTest.test_random_exact_e4m3_scales_one"></a>`BlockWise128ScaledMmRandomTest.test_random_exact_e4m3_scales_one` — [`L365`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L365)
- <a id="BlockWise128ScaledMmStructuralTest"></a>`BlockWise128ScaledMmStructuralTest` — [`L168`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L168)
- <a id="BlockWise128ScaledMmStructuralTest.test_a_eye_b_eye"></a>`BlockWise128ScaledMmStructuralTest.test_a_eye_b_eye` — [`L174`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L174)
- <a id="BlockWise128ScaledMmStructuralTest.test_a_ones_b_ones"></a>`BlockWise128ScaledMmStructuralTest.test_a_ones_b_ones` — [`L184`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L184)
- <a id="BlockWise128ScaledMmStructuralTest.test_a_payload_marker"></a>`BlockWise128ScaledMmStructuralTest.test_a_payload_marker` — [`L216`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L216)
- <a id="BlockWise128ScaledMmStructuralTest.test_a_scale_marker"></a>`BlockWise128ScaledMmStructuralTest.test_a_scale_marker` — [`L249`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L249)
- <a id="BlockWise128ScaledMmStructuralTest.test_b_payload_marker"></a>`BlockWise128ScaledMmStructuralTest.test_b_payload_marker` — [`L232`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L232)
- <a id="BlockWise128ScaledMmStructuralTest.test_b_scale_marker"></a>`BlockWise128ScaledMmStructuralTest.test_b_scale_marker` — [`L268`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L268)
- <a id="BlockWise128ScaledMmStructuralTest.test_b_scale_tail_corner_marker"></a>`BlockWise128ScaledMmStructuralTest.test_b_scale_tail_corner_marker` — [`L286`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L286)
- <a id="BlockWise128ScaledMmStructuralTest.test_bias_added"></a>`BlockWise128ScaledMmStructuralTest.test_bias_added` — [`L198`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L198)
- <a id="_ALIGNED_SHAPES"></a>`_ALIGNED_SHAPES` — [`L61`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L61)
- <a id="_ATOL_RTOL"></a>`_ATOL_RTOL` — [`L30`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L30)
- <a id="_BIAS_ISOLATION_SHAPES"></a>`_BIAS_ISOLATION_SHAPES` — [`L65`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L65)
- <a id="_BLOCK_SIZE"></a>`_BLOCK_SIZE` — [`L25`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L25)
- <a id="_COSINE_FLOOR"></a>`_COSINE_FLOOR` — [`L34`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L34)
- <a id="_DERIVED_DTYPE_SHAPES"></a>`_DERIVED_DTYPE_SHAPES` — [`L85`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L85)
- <a id="_E4M3_MAX"></a>`_E4M3_MAX` — [`L23`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L23)
- <a id="_EXACT_DTYPE_SHAPES"></a>`_EXACT_DTYPE_SHAPES` — [`L79`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L79)
- <a id="_FP8_E4M3"></a>`_FP8_E4M3` — [`L22`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L22)
- <a id="_LARGE_SHAPES"></a>`_LARGE_SHAPES` — [`L47`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L47)
- <a id="_RANDOM_DTYPES"></a>`_RANDOM_DTYPES` — [`L77`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L77)
- <a id="_SHAPES"></a>`_SHAPES` — [`L36`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L36)
- <a id="_STRUCTURAL_TILE"></a>`_STRUCTURAL_TILE` — [`L57`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L57)
- <a id="_TestCase"></a>`_TestCase` — [`L165`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L165)
- <a id="_cast_ref"></a>`_cast_ref` — [`L98`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L98)
- <a id="_cosine"></a>`_cosine` — [`L92`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L92)
- <a id="_dequant_a"></a>`_dequant_a` — [`L122`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L122)
- <a id="_dequant_b"></a>`_dequant_b` — [`L128`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L128)
- <a id="_ones_sa"></a>`_ones_sa` — [`L154`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L154)
- <a id="_ones_sb"></a>`_ones_sb` — [`L158`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L158)
- <a id="_quantize_blocked"></a>`_quantize_blocked` — [`L139`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L139)
- <a id="_reference_matmul"></a>`_reference_matmul` — [`L135`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L135)
- <a id="_run_kernel"></a>`_run_kernel` — [`L104`](../../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/scaled_mm/kernels/blockwise128_scaled_mm_kernel_test.py#L104) — documented in [python-ops](../../../../../../../concepts/python-ops.md)
