---
title: 'Module: torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.tests.test_splash_attention`/
symbols:
  SplashAttentionTest.test_cp_shard_parity: SplashAttentionTest#test_cp_shard_parity().
  SplashMaskInfoTest.test_document_aware_block_skipping_is_optional: SplashMaskInfoTest#test_document_aware_block_skipping_is_optional().
  SplashAttentionTest.check_forward_parity: SplashAttentionTest#check_forward_parity().
  HeadTailMaskTest.test_mask_matches_dense_reference: HeadTailMaskTest#test_mask_matches_dense_reference().
  SplashAttentionTest.test_mha_parity: SplashAttentionTest#test_mha_parity().
  SplashAttentionTest.test_segment_ids_parity: SplashAttentionTest#test_segment_ids_parity().
  SplashAttentionTest.test_segment_ids_backward_parity: SplashAttentionTest#test_segment_ids_backward_parity().
  SplashAttentionTest.test_mqa_parity: SplashAttentionTest#test_mqa_parity().
  SplashAttentionTest.test_mqa_parity_one_kv_head: SplashAttentionTest#test_mqa_parity_one_kv_head().
  SplashAttentionTest.test_block_sizes_parity: SplashAttentionTest#test_block_sizes_parity().
  SplashAttentionTest.test_mha_backward: SplashAttentionTest#test_mha_backward().
  SplashAttentionTest.test_mqa_backward: SplashAttentionTest#test_mqa_backward().
  SplashAttentionTest.make_packed_inputs: SplashAttentionTest#make_packed_inputs().
  _CP_SHARD_CASES: _CP_SHARD_CASES.
  HeadTailMaskTest.test_mask_equality_follows_q_order: HeadTailMaskTest#test_mask_equality_follows_q_order().
  HeadTailMaskTest.test_non_causal_mask_is_full: HeadTailMaskTest#test_non_causal_mask_is_full().
  SplashAttentionTest: SplashAttentionTest#
  _DOCUMENTS: _DOCUMENTS.
  _dense_cp_reference: _dense_cp_reference().
  _packed_segment_ids: _packed_segment_ids().
  HeadTailMaskTest: HeadTailMaskTest#
  SplashMaskInfoTest: SplashMaskInfoTest#
---
# Module: [`torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py)

> **Collapsed catalog** (22 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="HeadTailMaskTest"></a>`HeadTailMaskTest` — [`L108`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L108)
- <a id="HeadTailMaskTest.test_mask_equality_follows_q_order"></a>`HeadTailMaskTest.test_mask_equality_follows_q_order` — [`L124`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L124)
- <a id="HeadTailMaskTest.test_mask_matches_dense_reference"></a>`HeadTailMaskTest.test_mask_matches_dense_reference` — [`L112`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L112) — documented in [tpu-context-parallel-attention](../../../../../../concepts/tpu-context-parallel-attention.md)
- <a id="HeadTailMaskTest.test_non_causal_mask_is_full"></a>`HeadTailMaskTest.test_non_causal_mask_is_full` — [`L135`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L135)
- <a id="SplashAttentionTest"></a>`SplashAttentionTest` — [`L172`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L172)
- <a id="SplashAttentionTest.check_forward_parity"></a>`SplashAttentionTest.check_forward_parity` — [`L181`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L181)
- <a id="SplashAttentionTest.make_packed_inputs"></a>`SplashAttentionTest.make_packed_inputs` — [`L228`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L228)
- <a id="SplashAttentionTest.test_block_sizes_parity"></a>`SplashAttentionTest.test_block_sizes_parity` — [`L368`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L368)
- <a id="SplashAttentionTest.test_cp_shard_parity"></a>`SplashAttentionTest.test_cp_shard_parity` — [`L511`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L511) — documented in [tpu-context-parallel-attention](../../../../../../concepts/tpu-context-parallel-attention.md)
- <a id="SplashAttentionTest.test_mha_backward"></a>`SplashAttentionTest.test_mha_backward` — [`L386`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L386)
- <a id="SplashAttentionTest.test_mha_parity"></a>`SplashAttentionTest.test_mha_parity` — [`L217`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L217)
- <a id="SplashAttentionTest.test_mqa_backward"></a>`SplashAttentionTest.test_mqa_backward` — [`L446`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L446)
- <a id="SplashAttentionTest.test_mqa_parity"></a>`SplashAttentionTest.test_mqa_parity` — [`L346`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L346)
- <a id="SplashAttentionTest.test_mqa_parity_one_kv_head"></a>`SplashAttentionTest.test_mqa_parity_one_kv_head` — [`L357`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L357)
- <a id="SplashAttentionTest.test_segment_ids_backward_parity"></a>`SplashAttentionTest.test_segment_ids_backward_parity` — [`L299`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L299)
- <a id="SplashAttentionTest.test_segment_ids_parity"></a>`SplashAttentionTest.test_segment_ids_parity` — [`L268`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L268)
- <a id="SplashMaskInfoTest"></a>`SplashMaskInfoTest` — [`L140`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L140)
- <a id="SplashMaskInfoTest.test_document_aware_block_skipping_is_optional"></a>`SplashMaskInfoTest.test_document_aware_block_skipping_is_optional` — [`L142`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L142)
- <a id="_CP_SHARD_CASES"></a>`_CP_SHARD_CASES` — [`L72`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L72)
- <a id="_DOCUMENTS"></a>`_DOCUMENTS` — [`L69`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L69)
- <a id="_dense_cp_reference"></a>`_dense_cp_reference` — [`L24`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L24)
- <a id="_packed_segment_ids"></a>`_packed_segment_ids` — [`L57`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py#L57)
