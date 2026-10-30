---
title: 'Module: torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.tests.test_paired_segment_matmul`/PairedSegmentMatmulTest#
symbols:
  PairedSegmentMatmulTest._paired_vs_unpaired: _paired_vs_unpaired().
  PairedSegmentMatmulTest.test_forward_and_backward_parity: test_forward_and_backward_parity().
  PairedSegmentMatmulTest._bounded_values: _bounded_values().
  PairedSegmentMatmulTest.test_k_tiled_dweight_at_qwen3_235b_like_shape: test_k_tiled_dweight_at_qwen3_235b_like_shape().
  PairedSegmentMatmulTest.test_dinput_rounds_like_two_matmuls_with_random_values: test_dinput_rounds_like_two_matmuls_with_random_values().
  PairedSegmentMatmulTest.bounded_values: bounded_values().
  PairedSegmentMatmulTest.randn: randn().
  PairedSegmentMatmulTest.test_rejects_k_tile_that_does_not_divide_k: test_rejects_k_tile_that_does_not_divide_k().
  PairedSegmentMatmulTest.test_rejects_all_empty_groups: test_rejects_all_empty_groups().
  PairedSegmentMatmulTest: ''
  PairedSegmentMatmulTest.test_k_tiled_dweight_parity: test_k_tiled_dweight_parity().
  PairedSegmentMatmulTest.test_dinput_tiles_shared_by_many_groups: test_dinput_tiles_shared_by_many_groups().
---
# Module: [`torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.py)

> **Collapsed catalog** (12 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="PairedSegmentMatmulTest"></a>`PairedSegmentMatmulTest` — [`L13`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.py#L13)
- <a id="PairedSegmentMatmulTest._bounded_values"></a>`PairedSegmentMatmulTest._bounded_values` — [`L83`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.py#L83)
- <a id="PairedSegmentMatmulTest._paired_vs_unpaired"></a>`PairedSegmentMatmulTest._paired_vs_unpaired` — [`L94`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.py#L94)
- <a id="PairedSegmentMatmulTest.bounded_values"></a>`PairedSegmentMatmulTest.bounded_values` — [`L20`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.py#L20)
- <a id="PairedSegmentMatmulTest.randn"></a>`PairedSegmentMatmulTest.randn` — [`L247`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.py#L247)
- <a id="PairedSegmentMatmulTest.test_dinput_rounds_like_two_matmuls_with_random_values"></a>`PairedSegmentMatmulTest.test_dinput_rounds_like_two_matmuls_with_random_values` — [`L234`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.py#L234)
- <a id="PairedSegmentMatmulTest.test_dinput_tiles_shared_by_many_groups"></a>`PairedSegmentMatmulTest.test_dinput_tiles_shared_by_many_groups` — [`L217`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.py#L217)
- <a id="PairedSegmentMatmulTest.test_forward_and_backward_parity"></a>`PairedSegmentMatmulTest.test_forward_and_backward_parity` — [`L14`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.py#L14)
- <a id="PairedSegmentMatmulTest.test_k_tiled_dweight_at_qwen3_235b_like_shape"></a>`PairedSegmentMatmulTest.test_k_tiled_dweight_at_qwen3_235b_like_shape` — [`L150`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.py#L150)
- <a id="PairedSegmentMatmulTest.test_k_tiled_dweight_parity"></a>`PairedSegmentMatmulTest.test_k_tiled_dweight_parity` — [`L141`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.py#L141)
- <a id="PairedSegmentMatmulTest.test_rejects_all_empty_groups"></a>`PairedSegmentMatmulTest.test_rejects_all_empty_groups` — [`L290`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.py#L290)
- <a id="PairedSegmentMatmulTest.test_rejects_k_tile_that_does_not_divide_k"></a>`PairedSegmentMatmulTest.test_rejects_k_tile_that_does_not_divide_k` — [`L279`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.py#L279)
