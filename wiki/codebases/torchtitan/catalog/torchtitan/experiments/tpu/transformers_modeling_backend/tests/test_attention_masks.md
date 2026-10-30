---
title: 'Module: torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.transformers_modeling_backend.tests.test_attention_masks`/
symbols:
  _module: _module().
  _POSITIONS: _POSITIONS.
  FallbackMaskTest.test_document_causal: FallbackMaskTest#test_document_causal().
  FallbackMaskTest.test_document_bidirectional: FallbackMaskTest#test_document_bidirectional().
  FallbackMaskTest.test_windowed_documents: FallbackMaskTest#test_windowed_documents().
  FallbackMaskTest.test_padding: FallbackMaskTest#test_padding().
  _ours: _ours().
  SegmentIdsTest.test_precomputed_segment_ids_win_over_positions: SegmentIdsTest#test_precomputed_segment_ids_win_over_positions().
  SegmentIdsTest.test_padding_gets_segment_zero: SegmentIdsTest#test_padding_gets_segment_zero().
  FallbackMaskTest.test_causal_sliding_window: FallbackMaskTest#test_causal_sliding_window().
  FallbackMaskTest.test_bidirectional_sliding_window: FallbackMaskTest#test_bidirectional_sliding_window().
  _hf_mask: _hf_mask().
  SegmentIdsTest.test_documents_match_hf_packed_sequence_indices: SegmentIdsTest#test_documents_match_hf_packed_sequence_indices().
  SegmentIdsTest.test_missing_positions_raise_under_document_masking: SegmentIdsTest#test_missing_positions_raise_under_document_masking().
  SegmentIdsTest.test_plain_causal_needs_no_positions: SegmentIdsTest#test_plain_causal_needs_no_positions().
  KernelArgumentsTest.test_window_from_kwarg_wins: KernelArgumentsTest#test_window_from_kwarg_wins().
  KernelArgumentsTest.test_bidirectional_window_falls_back: KernelArgumentsTest#test_bidirectional_window_falls_back().
  KernelArgumentsTest.test_pick_block: KernelArgumentsTest#test_pick_block().
  KernelArgumentsTest.test_kernel_kwargs_come_from_module_config: KernelArgumentsTest#test_kernel_kwargs_come_from_module_config().
  SegmentIdsTest: SegmentIdsTest#
  FallbackMaskTest: FallbackMaskTest#
  KernelArgumentsTest: KernelArgumentsTest#
---
# Module: [`torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py)

> **Collapsed catalog** (22 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="FallbackMaskTest"></a>`FallbackMaskTest` — [`L78`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L78)
- <a id="FallbackMaskTest.test_bidirectional_sliding_window"></a>`FallbackMaskTest.test_bidirectional_sliding_window` — [`L102`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L102)
- <a id="FallbackMaskTest.test_causal_sliding_window"></a>`FallbackMaskTest.test_causal_sliding_window` — [`L93`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L93)
- <a id="FallbackMaskTest.test_document_bidirectional"></a>`FallbackMaskTest.test_document_bidirectional` — [`L86`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L86)
- <a id="FallbackMaskTest.test_document_causal"></a>`FallbackMaskTest.test_document_causal` — [`L80`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L80)
- <a id="FallbackMaskTest.test_padding"></a>`FallbackMaskTest.test_padding` — [`L114`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L114)
- <a id="FallbackMaskTest.test_windowed_documents"></a>`FallbackMaskTest.test_windowed_documents` — [`L108`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L108)
- <a id="KernelArgumentsTest"></a>`KernelArgumentsTest` — [`L128`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L128)
- <a id="KernelArgumentsTest.test_bidirectional_window_falls_back"></a>`KernelArgumentsTest.test_bidirectional_window_falls_back` — [`L137`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L137)
- <a id="KernelArgumentsTest.test_kernel_kwargs_come_from_module_config"></a>`KernelArgumentsTest.test_kernel_kwargs_come_from_module_config` — [`L153`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L153)
- <a id="KernelArgumentsTest.test_pick_block"></a>`KernelArgumentsTest.test_pick_block` — [`L150`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L150)
- <a id="KernelArgumentsTest.test_window_from_kwarg_wins"></a>`KernelArgumentsTest.test_window_from_kwarg_wins` — [`L130`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L130)
- <a id="SegmentIdsTest"></a>`SegmentIdsTest` — [`L48`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L48)
- <a id="SegmentIdsTest.test_documents_match_hf_packed_sequence_indices"></a>`SegmentIdsTest.test_documents_match_hf_packed_sequence_indices` — [`L50`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L50)
- <a id="SegmentIdsTest.test_missing_positions_raise_under_document_masking"></a>`SegmentIdsTest.test_missing_positions_raise_under_document_masking` — [`L63`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L63)
- <a id="SegmentIdsTest.test_padding_gets_segment_zero"></a>`SegmentIdsTest.test_padding_gets_segment_zero` — [`L70`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L70)
- <a id="SegmentIdsTest.test_plain_causal_needs_no_positions"></a>`SegmentIdsTest.test_plain_causal_needs_no_positions` — [`L67`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L67)
- <a id="SegmentIdsTest.test_precomputed_segment_ids_win_over_positions"></a>`SegmentIdsTest.test_precomputed_segment_ids_win_over_positions` — [`L57`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L57)
- <a id="_POSITIONS"></a>`_POSITIONS` — [`L45`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L45)
- <a id="_hf_mask"></a>`_hf_mask` — [`L24`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L24)
- <a id="_module"></a>`_module` — [`L19`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L19)
- <a id="_ours"></a>`_ours` — [`L34`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py#L34)
