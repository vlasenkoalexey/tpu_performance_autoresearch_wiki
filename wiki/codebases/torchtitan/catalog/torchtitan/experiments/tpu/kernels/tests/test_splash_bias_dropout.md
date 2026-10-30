---
title: 'Module: torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.tests.test_splash_bias_dropout`/
symbols:
  SplashBiasDropoutTest._qkv: SplashBiasDropoutTest#_qkv().
  SplashBiasDropoutTest.test_perkey_bias_dbias: SplashBiasDropoutTest#test_perkey_bias_dbias().
  SplashBiasDropoutTest.test_segment_ids_padding_layout_parity: SplashBiasDropoutTest#test_segment_ids_padding_layout_parity().
  SplashBiasDropoutTest.test_document_aware_mask_info_compacts_grid: SplashBiasDropoutTest#test_document_aware_mask_info_compacts_grid().
  SplashBiasDropoutTest.test_segment_ids_block_skipping_parity: SplashBiasDropoutTest#test_segment_ids_block_skipping_parity().
  SplashBiasDropoutTest.run: SplashBiasDropoutTest#run().
  SplashBiasDropoutTest._segment_ids_case: SplashBiasDropoutTest#_segment_ids_case().
  SplashBiasDropoutTest.test_dropout_determinism_and_grads: SplashBiasDropoutTest#test_dropout_determinism_and_grads().
  _sdpa_ref: _sdpa_ref().
  SplashBiasDropoutTest.test_gqa_parity: SplashBiasDropoutTest#test_gqa_parity().
  SplashBiasDropoutTest.test_mqa_parity: SplashBiasDropoutTest#test_mqa_parity().
  SplashBiasDropoutTest.test_segment_ids_with_dropout: SplashBiasDropoutTest#test_segment_ids_with_dropout().
  SplashBiasDropoutTest.test_attn_logits_soft_cap: SplashBiasDropoutTest#test_attn_logits_soft_cap().
  SplashBiasDropoutTest.test_dq_reduction_steps_3_matches_default: SplashBiasDropoutTest#test_dq_reduction_steps_3_matches_default().
  SplashBiasDropoutTest.test_fullrank_bias_forward_and_backward: SplashBiasDropoutTest#test_fullrank_bias_forward_and_backward().
  SplashBiasDropoutTest.test_mha_parity: SplashBiasDropoutTest#test_mha_parity().
  SplashBiasDropoutTest.test_gemma4_shapes: SplashBiasDropoutTest#test_gemma4_shapes().
  SplashBiasDropoutTest.test_block_skipping_with_dropout_is_bit_identical: SplashBiasDropoutTest#test_block_skipping_with_dropout_is_bit_identical().
  SplashBiasDropoutTest.test_document_aware_mask_info_has_no_gather: SplashBiasDropoutTest#test_document_aware_mask_info_has_no_gather().
  SplashBiasDropoutTest.test_noncausal_parity: SplashBiasDropoutTest#test_noncausal_parity().
  SplashBiasDropoutTest.test_sliding_window_parity: SplashBiasDropoutTest#test_sliding_window_parity().
  SplashBiasDropoutTest.test_unflatten_shim_leaves_batch_shared_bias_alone: SplashBiasDropoutTest#test_unflatten_shim_leaves_batch_shared_bias_alone().
  SplashBiasDropoutTest._assert_matches_tokamax: SplashBiasDropoutTest#_assert_matches_tokamax().
  SplashBiasDropoutTest._blocks: SplashBiasDropoutTest#_blocks().
  SplashBiasDropoutTest.test_heads_first_layout_matches_torch_standard: SplashBiasDropoutTest#test_heads_first_layout_matches_torch_standard().
  SplashBiasDropoutTest.test_matches_tokamax: SplashBiasDropoutTest#test_matches_tokamax().
  SplashBiasDropoutTest.reference: SplashBiasDropoutTest#reference().
  SplashBiasDropoutTest.steps: SplashBiasDropoutTest#steps().
  SplashBiasDropoutTest._expand_kv: SplashBiasDropoutTest#_expand_kv().
  SplashBiasDropoutTest.build: SplashBiasDropoutTest#build().
  SplashBiasDropoutTest: SplashBiasDropoutTest#
  SplashBiasDropoutTest.test_segment_ids_mha_causal: SplashBiasDropoutTest#test_segment_ids_mha_causal().
  SplashBiasDropoutTest.test_segment_ids_mha_bidirectional: SplashBiasDropoutTest#test_segment_ids_mha_bidirectional().
  SplashBiasDropoutTest.test_segment_ids_gqa_causal: SplashBiasDropoutTest#test_segment_ids_gqa_causal().
  SplashBiasDropoutTest.test_segment_ids_mqa_causal: SplashBiasDropoutTest#test_segment_ids_mqa_causal().
  SplashBiasDropoutTest.test_segment_ids_window: SplashBiasDropoutTest#test_segment_ids_window().
  _causal_bias_mask: _causal_bias_mask().
---
# Module: [`torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py)

> **Collapsed catalog** (37 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="SplashBiasDropoutTest"></a>`SplashBiasDropoutTest` — [`L51`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L51)
- <a id="SplashBiasDropoutTest._assert_matches_tokamax"></a>`SplashBiasDropoutTest._assert_matches_tokamax` — [`L686`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L686)
- <a id="SplashBiasDropoutTest._blocks"></a>`SplashBiasDropoutTest._blocks` — [`L367`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L367)
- <a id="SplashBiasDropoutTest._expand_kv"></a>`SplashBiasDropoutTest._expand_kv` — [`L60`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L60)
- <a id="SplashBiasDropoutTest._qkv"></a>`SplashBiasDropoutTest._qkv` — [`L53`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L53)
- <a id="SplashBiasDropoutTest._segment_ids_case"></a>`SplashBiasDropoutTest._segment_ids_case` — [`L125`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L125)
- <a id="SplashBiasDropoutTest.build"></a>`SplashBiasDropoutTest.build` — [`L527`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L527)
- <a id="SplashBiasDropoutTest.reference"></a>`SplashBiasDropoutTest.reference` — [`L148`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L148)
- <a id="SplashBiasDropoutTest.run"></a>`SplashBiasDropoutTest.run` — [`L343`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L343)
- <a id="SplashBiasDropoutTest.steps"></a>`SplashBiasDropoutTest.steps` — [`L533`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L533)
- <a id="SplashBiasDropoutTest.test_attn_logits_soft_cap"></a>`SplashBiasDropoutTest.test_attn_logits_soft_cap` — [`L234`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L234)
- <a id="SplashBiasDropoutTest.test_block_skipping_with_dropout_is_bit_identical"></a>`SplashBiasDropoutTest.test_block_skipping_with_dropout_is_bit_identical` — [`L373`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L373)
- <a id="SplashBiasDropoutTest.test_document_aware_mask_info_compacts_grid"></a>`SplashBiasDropoutTest.test_document_aware_mask_info_compacts_grid` — [`L517`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L517)
- <a id="SplashBiasDropoutTest.test_document_aware_mask_info_has_no_gather"></a>`SplashBiasDropoutTest.test_document_aware_mask_info_has_no_gather` — [`L565`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L565)
- <a id="SplashBiasDropoutTest.test_dq_reduction_steps_3_matches_default"></a>`SplashBiasDropoutTest.test_dq_reduction_steps_3_matches_default` — [`L422`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L422)
- <a id="SplashBiasDropoutTest.test_dropout_determinism_and_grads"></a>`SplashBiasDropoutTest.test_dropout_determinism_and_grads` — [`L889`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L889)
- <a id="SplashBiasDropoutTest.test_fullrank_bias_forward_and_backward"></a>`SplashBiasDropoutTest.test_fullrank_bias_forward_and_backward` — [`L768`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L768)
- <a id="SplashBiasDropoutTest.test_gemma4_shapes"></a>`SplashBiasDropoutTest.test_gemma4_shapes` — [`L279`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L279)
- <a id="SplashBiasDropoutTest.test_gqa_parity"></a>`SplashBiasDropoutTest.test_gqa_parity` — [`L75`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L75)
- <a id="SplashBiasDropoutTest.test_heads_first_layout_matches_torch_standard"></a>`SplashBiasDropoutTest.test_heads_first_layout_matches_torch_standard` — [`L329`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L329)
- <a id="SplashBiasDropoutTest.test_matches_tokamax"></a>`SplashBiasDropoutTest.test_matches_tokamax` — [`L717`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L717)
- <a id="SplashBiasDropoutTest.test_mha_parity"></a>`SplashBiasDropoutTest.test_mha_parity` — [`L66`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L66)
- <a id="SplashBiasDropoutTest.test_mqa_parity"></a>`SplashBiasDropoutTest.test_mqa_parity` — [`L85`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L85)
- <a id="SplashBiasDropoutTest.test_noncausal_parity"></a>`SplashBiasDropoutTest.test_noncausal_parity` — [`L656`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L656)
- <a id="SplashBiasDropoutTest.test_perkey_bias_dbias"></a>`SplashBiasDropoutTest.test_perkey_bias_dbias` — [`L832`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L832) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="SplashBiasDropoutTest.test_segment_ids_block_skipping_parity"></a>`SplashBiasDropoutTest.test_segment_ids_block_skipping_parity` — [`L588`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L588) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="SplashBiasDropoutTest.test_segment_ids_gqa_causal"></a>`SplashBiasDropoutTest.test_segment_ids_gqa_causal` — [`L188`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L188)
- <a id="SplashBiasDropoutTest.test_segment_ids_mha_bidirectional"></a>`SplashBiasDropoutTest.test_segment_ids_mha_bidirectional` — [`L185`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L185)
- <a id="SplashBiasDropoutTest.test_segment_ids_mha_causal"></a>`SplashBiasDropoutTest.test_segment_ids_mha_causal` — [`L182`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L182)
- <a id="SplashBiasDropoutTest.test_segment_ids_mqa_causal"></a>`SplashBiasDropoutTest.test_segment_ids_mqa_causal` — [`L191`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L191)
- <a id="SplashBiasDropoutTest.test_segment_ids_padding_layout_parity"></a>`SplashBiasDropoutTest.test_segment_ids_padding_layout_parity` — [`L470`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L470) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- <a id="SplashBiasDropoutTest.test_segment_ids_window"></a>`SplashBiasDropoutTest.test_segment_ids_window` — [`L195`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L195)
- <a id="SplashBiasDropoutTest.test_segment_ids_with_dropout"></a>`SplashBiasDropoutTest.test_segment_ids_with_dropout` — [`L198`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L198)
- <a id="SplashBiasDropoutTest.test_sliding_window_parity"></a>`SplashBiasDropoutTest.test_sliding_window_parity` — [`L730`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L730)
- <a id="SplashBiasDropoutTest.test_unflatten_shim_leaves_batch_shared_bias_alone"></a>`SplashBiasDropoutTest.test_unflatten_shim_leaves_batch_shared_bias_alone` — [`L805`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L805)
- <a id="_causal_bias_mask"></a>`_causal_bias_mask` — [`L41`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L41)
- <a id="_sdpa_ref"></a>`_sdpa_ref` — [`L26`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py#L26)
