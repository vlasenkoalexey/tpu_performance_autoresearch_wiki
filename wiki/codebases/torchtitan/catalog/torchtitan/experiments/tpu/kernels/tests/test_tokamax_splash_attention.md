---
title: 'Module: torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.tests.test_tokamax_splash_attention`/
symbols:
  SplashAttentionTokamaxTest.test_block_sizes_parity: SplashAttentionTokamaxTest#test_block_sizes_parity().
  SplashAttentionTokamaxTest.test_config_change_retraces_kernel: SplashAttentionTokamaxTest#test_config_change_retraces_kernel().
  SplashAttentionTokamaxTest.test_cp_shard_parity: SplashAttentionTokamaxTest#test_cp_shard_parity().
  SplashAttentionTokamaxTest.test_segment_ids_parity: SplashAttentionTokamaxTest#test_segment_ids_parity().
  SplashAttentionTokamaxTest.check_forward_parity: SplashAttentionTokamaxTest#check_forward_parity().
  HeadTailMaskTest.test_mask_matches_dense_reference: HeadTailMaskTest#test_mask_matches_dense_reference().
  SplashAttentionTokamaxTest.test_mha_parity: SplashAttentionTokamaxTest#test_mha_parity().
  SplashAttentionTokamaxTest.test_mqa_parity: SplashAttentionTokamaxTest#test_mqa_parity().
  SplashAttentionTokamaxTest.test_mqa_parity_one_kv_head: SplashAttentionTokamaxTest#test_mqa_parity_one_kv_head().
  SplashAttentionTokamaxTest.test_custom_scale_backward: SplashAttentionTokamaxTest#test_custom_scale_backward().
  SplashAttentionTokamaxTest.test_mha_backward: SplashAttentionTokamaxTest#test_mha_backward().
  SplashAttentionTokamaxTest.test_mqa_backward: SplashAttentionTokamaxTest#test_mqa_backward().
  _CP_SHARD_CASES: _CP_SHARD_CASES.
  _DOCUMENTS: _DOCUMENTS.
  HeadTailMaskTest.test_mask_equality_follows_q_order: HeadTailMaskTest#test_mask_equality_follows_q_order().
  HeadTailMaskTest.test_non_causal_mask_is_full: HeadTailMaskTest#test_non_causal_mask_is_full().
  SplashAttentionTokamaxTest: SplashAttentionTokamaxTest#
  SplashAttentionTokamaxTest.test_enable_gqa_is_validated: SplashAttentionTokamaxTest#test_enable_gqa_is_validated().
  SplashAttentionTokamaxTest.test_gpu_available: SplashAttentionTokamaxTest#test_gpu_available().
  _packed_segment_ids: _packed_segment_ids().
  SplashAttentionTokamaxTest.record: SplashAttentionTokamaxTest#record().
  HeadTailMaskTest: HeadTailMaskTest#
---
# Module: [`torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py)

> **Collapsed catalog** (22 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="HeadTailMaskTest"></a>`HeadTailMaskTest` — [`L70`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L70)
- <a id="HeadTailMaskTest.test_mask_equality_follows_q_order"></a>`HeadTailMaskTest.test_mask_equality_follows_q_order` — [`L88`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L88)
- <a id="HeadTailMaskTest.test_mask_matches_dense_reference"></a>`HeadTailMaskTest.test_mask_matches_dense_reference` — [`L74`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L74) — documented in [tpu-context-parallel-attention](../../../../../../concepts/tpu-context-parallel-attention.md)
- <a id="HeadTailMaskTest.test_non_causal_mask_is_full"></a>`HeadTailMaskTest.test_non_causal_mask_is_full` — [`L98`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L98)
- <a id="SplashAttentionTokamaxTest"></a>`SplashAttentionTokamaxTest` — [`L103`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L103)
- <a id="SplashAttentionTokamaxTest.check_forward_parity"></a>`SplashAttentionTokamaxTest.check_forward_parity` — [`L105`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L105)
- <a id="SplashAttentionTokamaxTest.record"></a>`SplashAttentionTokamaxTest.record` — [`L551`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L551)
- <a id="SplashAttentionTokamaxTest.test_block_sizes_parity"></a>`SplashAttentionTokamaxTest.test_block_sizes_parity` — [`L187`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L187)
- <a id="SplashAttentionTokamaxTest.test_config_change_retraces_kernel"></a>`SplashAttentionTokamaxTest.test_config_change_retraces_kernel` — [`L529`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L529)
- <a id="SplashAttentionTokamaxTest.test_cp_shard_parity"></a>`SplashAttentionTokamaxTest.test_cp_shard_parity` — [`L566`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L566) — documented in [tpu-context-parallel-attention](../../../../../../concepts/tpu-context-parallel-attention.md)
- <a id="SplashAttentionTokamaxTest.test_custom_scale_backward"></a>`SplashAttentionTokamaxTest.test_custom_scale_backward` — [`L246`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L246)
- <a id="SplashAttentionTokamaxTest.test_enable_gqa_is_validated"></a>`SplashAttentionTokamaxTest.test_enable_gqa_is_validated` — [`L223`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L223)
- <a id="SplashAttentionTokamaxTest.test_gpu_available"></a>`SplashAttentionTokamaxTest.test_gpu_available` — [`L288`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L288)
- <a id="SplashAttentionTokamaxTest.test_mha_backward"></a>`SplashAttentionTokamaxTest.test_mha_backward` — [`L292`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L292)
- <a id="SplashAttentionTokamaxTest.test_mha_parity"></a>`SplashAttentionTokamaxTest.test_mha_parity` — [`L145`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L145)
- <a id="SplashAttentionTokamaxTest.test_mqa_backward"></a>`SplashAttentionTokamaxTest.test_mqa_backward` — [`L363`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L363)
- <a id="SplashAttentionTokamaxTest.test_mqa_parity"></a>`SplashAttentionTokamaxTest.test_mqa_parity` — [`L159`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L159)
- <a id="SplashAttentionTokamaxTest.test_mqa_parity_one_kv_head"></a>`SplashAttentionTokamaxTest.test_mqa_parity_one_kv_head` — [`L173`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L173)
- <a id="SplashAttentionTokamaxTest.test_segment_ids_parity"></a>`SplashAttentionTokamaxTest.test_segment_ids_parity` — [`L439`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L439)
- <a id="_CP_SHARD_CASES"></a>`_CP_SHARD_CASES` — [`L34`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L34)
- <a id="_DOCUMENTS"></a>`_DOCUMENTS` — [`L30`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L30)
- <a id="_packed_segment_ids"></a>`_packed_segment_ids` — [`L18`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py#L18)
