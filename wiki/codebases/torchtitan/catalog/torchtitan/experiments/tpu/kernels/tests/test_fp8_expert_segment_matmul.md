---
title: 'Module: torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.tests.test_fp8_expert_segment_matmul`/
symbols:
  Fp8GmmTest.test_fwd_matches_dequantized_reference: Fp8GmmTest#test_fwd_matches_dequantized_reference().
  Fp8ExpertSegmentMatmulTest.test_forward_matches_dequantized_reference: Fp8ExpertSegmentMatmulTest#test_forward_matches_dequantized_reference().
  Fp8ExpertSegmentMatmulTest.test_backward_is_close_to_bf16: Fp8ExpertSegmentMatmulTest#test_backward_is_close_to_bf16().
  Fp8ExpertSegmentMatmulTest.test_tiny_gradient_rows_stay_finite: Fp8ExpertSegmentMatmulTest#test_tiny_gradient_rows_stay_finite().
  Fp8ExpertSegmentMatmulTest.test_swiglu_matches_separate_ops: Fp8ExpertSegmentMatmulTest#test_swiglu_matches_separate_ops().
  Fp8GmmTest.test_bwd_is_close_to_f32: Fp8GmmTest#test_bwd_is_close_to_f32().
  _to_torch: _to_torch().
  Fp8SwigluKernelTest.test_swiglu_quantize_matches_xla: Fp8SwigluKernelTest#test_swiglu_quantize_matches_xla().
  Fp8SwigluKernelTest.test_swiglu_grad_matches_autodiff: Fp8SwigluKernelTest#test_swiglu_grad_matches_autodiff().
  _rel_err: _rel_err().
  Fp8ExpertSegmentMatmulTest.test_paired_matches_unpaired: Fp8ExpertSegmentMatmulTest#test_paired_matches_unpaired().
  Fp8ExpertSegmentMatmulTest.test_paired_unsplit_is_concatenation: Fp8ExpertSegmentMatmulTest#test_paired_unsplit_is_concatenation().
  _GROUP_SIZES: _GROUP_SIZES.
  _TILINGS: _TILINGS.
  Fp8ExpertSegmentMatmulTest._to_dev: Fp8ExpertSegmentMatmulTest#_to_dev().
  Fp8ExpertSegmentMatmulTest._operands: Fp8ExpertSegmentMatmulTest#_operands().
  Fp8ExpertSegmentMatmulTest.unpaired: Fp8ExpertSegmentMatmulTest#unpaired().
  Fp8ExpertSegmentMatmulTest.paired: Fp8ExpertSegmentMatmulTest#paired().
  _dequantized: _dequantized().
  _grouped_reference: _grouped_reference().
  Fp8SwigluKernelTest._gate_up: Fp8SwigluKernelTest#_gate_up().
  _TILING: _TILING.
  Fp8GmmTest._operands: Fp8GmmTest#_operands().
  Fp8SwigluKernelTest._ROWS: Fp8SwigluKernelTest#_ROWS.
  Fp8GmmTest: Fp8GmmTest#
  Fp8SwigluKernelTest: Fp8SwigluKernelTest#
  Fp8ExpertSegmentMatmulTest: Fp8ExpertSegmentMatmulTest#
  Fp8SwigluKernelTest._HIDDEN: Fp8SwigluKernelTest#_HIDDEN.
---
# Module: [`torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py)

> **Collapsed catalog** (28 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="Fp8ExpertSegmentMatmulTest"></a>`Fp8ExpertSegmentMatmulTest` — [`L146`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L146)
- <a id="Fp8ExpertSegmentMatmulTest._operands"></a>`Fp8ExpertSegmentMatmulTest._operands` — [`L148`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L148)
- <a id="Fp8ExpertSegmentMatmulTest._to_dev"></a>`Fp8ExpertSegmentMatmulTest._to_dev` — [`L157`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L157)
- <a id="Fp8ExpertSegmentMatmulTest.paired"></a>`Fp8ExpertSegmentMatmulTest.paired` — [`L255`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L255)
- <a id="Fp8ExpertSegmentMatmulTest.test_backward_is_close_to_bf16"></a>`Fp8ExpertSegmentMatmulTest.test_backward_is_close_to_bf16` — [`L180`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L180) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="Fp8ExpertSegmentMatmulTest.test_forward_matches_dequantized_reference"></a>`Fp8ExpertSegmentMatmulTest.test_forward_matches_dequantized_reference` — [`L162`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L162) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="Fp8ExpertSegmentMatmulTest.test_paired_matches_unpaired"></a>`Fp8ExpertSegmentMatmulTest.test_paired_matches_unpaired` — [`L235`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L235)
- <a id="Fp8ExpertSegmentMatmulTest.test_paired_unsplit_is_concatenation"></a>`Fp8ExpertSegmentMatmulTest.test_paired_unsplit_is_concatenation` — [`L277`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L277)
- <a id="Fp8ExpertSegmentMatmulTest.test_swiglu_matches_separate_ops"></a>`Fp8ExpertSegmentMatmulTest.test_swiglu_matches_separate_ops` — [`L293`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L293)
- <a id="Fp8ExpertSegmentMatmulTest.test_tiny_gradient_rows_stay_finite"></a>`Fp8ExpertSegmentMatmulTest.test_tiny_gradient_rows_stay_finite` — [`L209`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L209) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="Fp8ExpertSegmentMatmulTest.unpaired"></a>`Fp8ExpertSegmentMatmulTest.unpaired` — [`L242`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L242)
- <a id="Fp8GmmTest"></a>`Fp8GmmTest` — [`L47`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L47)
- <a id="Fp8GmmTest._operands"></a>`Fp8GmmTest._operands` — [`L50`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L50)
- <a id="Fp8GmmTest.test_bwd_is_close_to_f32"></a>`Fp8GmmTest.test_bwd_is_close_to_f32` — [`L73`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L73) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="Fp8GmmTest.test_fwd_matches_dequantized_reference"></a>`Fp8GmmTest.test_fwd_matches_dequantized_reference` — [`L61`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L61) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="Fp8SwigluKernelTest"></a>`Fp8SwigluKernelTest` — [`L94`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L94)
- <a id="Fp8SwigluKernelTest._HIDDEN"></a>`Fp8SwigluKernelTest._HIDDEN` — [`L98`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L98)
- <a id="Fp8SwigluKernelTest._ROWS"></a>`Fp8SwigluKernelTest._ROWS` — [`L98`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L98)
- <a id="Fp8SwigluKernelTest._gate_up"></a>`Fp8SwigluKernelTest._gate_up` — [`L100`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L100)
- <a id="Fp8SwigluKernelTest.test_swiglu_grad_matches_autodiff"></a>`Fp8SwigluKernelTest.test_swiglu_grad_matches_autodiff` — [`L124`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L124)
- <a id="Fp8SwigluKernelTest.test_swiglu_quantize_matches_xla"></a>`Fp8SwigluKernelTest.test_swiglu_quantize_matches_xla` — [`L106`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L106)
- <a id="_GROUP_SIZES"></a>`_GROUP_SIZES` — [`L15`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L15)
- <a id="_TILING"></a>`_TILING` — [`L13`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L13)
- <a id="_TILINGS"></a>`_TILINGS` — [`L14`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L14)
- <a id="_dequantized"></a>`_dequantized` — [`L18`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L18)
- <a id="_grouped_reference"></a>`_grouped_reference` — [`L29`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L29)
- <a id="_rel_err"></a>`_rel_err` — [`L38`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L38)
- <a id="_to_torch"></a>`_to_torch` — [`L43`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py#L43)
