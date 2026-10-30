---
title: 'Module: torchtitan/experiments/tpu/tests/test_workarounds.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/tests/test_workarounds.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.tests.test_workarounds`/
symbols:
  WorkaroundsTest.test_all_gather_cp_config_and_numerical_parity: WorkaroundsTest#test_all_gather_cp_config_and_numerical_parity().
  _Tiny.attn: _Tiny#attn.
  WorkaroundsTest.test_tokamax_patch_forwards_splash_config: WorkaroundsTest#test_tokamax_patch_forwards_splash_config().
  WorkaroundsTest.test_qwen3_ulysses_cp_recipe_and_validation: WorkaroundsTest#test_qwen3_ulysses_cp_recipe_and_validation().
  WorkaroundsTest.test_fused_loss_matches_unfused_cross_entropy: WorkaroundsTest#test_fused_loss_matches_unfused_cross_entropy().
  WorkaroundsTest.test_tpu_selective_ac_recomputes_saved_collectives: WorkaroundsTest#test_tpu_selective_ac_recomputes_saved_collectives().
  WorkaroundsTest.test_cp_with_tp_or_ep_on_fsdp2_needs_spmd_types_fsdp: WorkaroundsTest#test_cp_with_tp_or_ep_on_fsdp2_needs_spmd_types_fsdp().
  WorkaroundsTest.test_wrapper_conversion_positions_to_segment_ids: WorkaroundsTest#test_wrapper_conversion_positions_to_segment_ids().
  _TinyModel.lm_head: _TinyModel#lm_head.
  WorkaroundsTest.test_loss_kernel_patch_keeps_hf_state_dict_adapter_working: WorkaroundsTest#test_loss_kernel_patch_keeps_hf_state_dict_adapter_working().
  WorkaroundsTest.test_tokamax_patch_forwards_segment_ids: WorkaroundsTest#test_tokamax_patch_forwards_segment_ids().
  WorkaroundsTest.test_splash_attention_patch_plugs_into_cp_attention: WorkaroundsTest#test_splash_attention_patch_plugs_into_cp_attention().
  WorkaroundsTest.test_splash_patch_warns_on_cp_block_skipping: WorkaroundsTest#test_splash_patch_warns_on_cp_block_skipping().
  WorkaroundsTest.test_tpu_cp_inner_attention_lookup: WorkaroundsTest#test_tpu_cp_inner_attention_lookup().
  WorkaroundsTest.test_ulysses_cp_repeats_kv_heads: WorkaroundsTest#test_ulysses_cp_repeats_kv_heads().
  WorkaroundsTest.test_all_gather_cp_reference_attention_limits: WorkaroundsTest#test_all_gather_cp_reference_attention_limits().
  WorkaroundsTest.test_tokamax_patch_warns_on_unsupported_block_skipping: WorkaroundsTest#test_tokamax_patch_warns_on_unsupported_block_skipping().
  WorkaroundsTest.test_cp_without_cp_recipe_is_rejected: WorkaroundsTest#test_cp_without_cp_recipe_is_rejected().
  WorkaroundsTest._tokamax_patch_fixture: WorkaroundsTest#_tokamax_patch_fixture().
  WorkaroundsTest.test_all_gather_cp_needs_a_kernel_off_cpu: WorkaroundsTest#test_all_gather_cp_needs_a_kernel_off_cpu().
  WorkaroundsTest.test_tokamax_patch_accepts_a_config_with_no_splash_fields: WorkaroundsTest#test_tokamax_patch_accepts_a_config_with_no_splash_fields().
  WorkaroundsTest.test_splash_attention_auto_block_size_and_fallback: WorkaroundsTest#test_splash_attention_auto_block_size_and_fallback().
  WorkaroundsTest.build: WorkaroundsTest#build().
  WorkaroundsTest.test_pallas_loss_linear_patches_output_and_output_transform: WorkaroundsTest#test_pallas_loss_linear_patches_output_and_output_transform().
  WorkaroundsTest.test_loss_kernel_patch_preserves_weight_initialization: WorkaroundsTest#test_loss_kernel_patch_preserves_weight_initialization().
  WorkaroundsTest.test_tokamax_patch_raises_when_a_splash_config_resolves_nothing._BrokenSplash.sa_block_kv: WorkaroundsTest#test_tokamax_patch_raises_when_a_splash_config_resolves_nothing()._BrokenSplash#sa_block_kv.
  WorkaroundsTest.test_tokamax_patch_drops_kwargs_the_kernel_does_not_accept: WorkaroundsTest#test_tokamax_patch_drops_kwargs_the_kernel_does_not_accept().
  WorkaroundsTest.test_all_gather_cp_requires_headtail_inputs: WorkaroundsTest#test_all_gather_cp_requires_headtail_inputs().
  WorkaroundsTest._tokamax_patch_fixture._Tiny.__init__: WorkaroundsTest#_tokamax_patch_fixture()._Tiny#__init__().
  WorkaroundsTest.test_tokamax_patch_raises_when_a_splash_config_resolves_nothing: WorkaroundsTest#test_tokamax_patch_raises_when_a_splash_config_resolves_nothing().
  WorkaroundsTest.test_wait_helper_waits_async_tensors_once: WorkaroundsTest#test_wait_helper_waits_async_tensors_once().
  WorkaroundsTest.fake_redistribute: WorkaroundsTest#fake_redistribute().
  WorkaroundsTest.mock_splash_sdpa_capture: WorkaroundsTest#mock_splash_sdpa_capture().
  WorkaroundsTest.test_pallas_loss_linear_preserves_state_dict_keys._TinyModel: WorkaroundsTest#test_pallas_loss_linear_preserves_state_dict_keys()._TinyModel#
  WorkaroundsTest.reference_linear_loss: WorkaroundsTest#reference_linear_loss().
  WorkaroundsTest._tokamax_patch_fixture._Tiny: WorkaroundsTest#_tokamax_patch_fixture()._Tiny#
  WorkaroundsTest.test_tokamax_patch_raises_when_a_splash_config_resolves_nothing._BrokenSplash: WorkaroundsTest#test_tokamax_patch_raises_when_a_splash_config_resolves_nothing()._BrokenSplash#
  WorkaroundsTest.test_tokamax_patch_accepts_a_config_with_no_splash_fields._NotASplashConfig: WorkaroundsTest#test_tokamax_patch_accepts_a_config_with_no_splash_fields()._NotASplashConfig#
  WorkaroundsTest.capture: WorkaroundsTest#capture().
  WorkaroundsTest.fallback: WorkaroundsTest#fallback().
  WorkaroundsTest.fake_local_attn: WorkaroundsTest#fake_local_attn().
  WorkaroundsTest: WorkaroundsTest#
  WorkaroundsTest.test_pallas_loss_linear_preserves_state_dict_keys: WorkaroundsTest#test_pallas_loss_linear_preserves_state_dict_keys().
  WorkaroundsTest.test_pallas_loss_linear_preserves_state_dict_keys._TinyModel.__init__: WorkaroundsTest#test_pallas_loss_linear_preserves_state_dict_keys()._TinyModel#__init__().
  ? WorkaroundsTest.test_tokamax_patch_raises_when_a_splash_config_resolves_nothing._BrokenSplash.use_tokamax_splash_attention_kernel
  : WorkaroundsTest#test_tokamax_patch_raises_when_a_splash_config_resolves_nothing()._BrokenSplash#use_tokamax_splash_attention_kernel.
  WorkaroundsTest.test_tokamax_patch_raises_when_a_splash_config_resolves_nothing._BrokenSplash.sa_block_q: WorkaroundsTest#test_tokamax_patch_raises_when_a_splash_config_resolves_nothing()._BrokenSplash#sa_block_q.
---
# Module: [`torchtitan/experiments/tpu/tests/test_workarounds.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py)

> **Collapsed catalog** (46 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="WorkaroundsTest"></a>`WorkaroundsTest` — [`L9`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L9)
- <a id="WorkaroundsTest._tokamax_patch_fixture"></a>`WorkaroundsTest._tokamax_patch_fixture` — [`L314`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L314)
- <a id="WorkaroundsTest._tokamax_patch_fixture._Tiny"></a>`WorkaroundsTest._tokamax_patch_fixture._Tiny` — [`L319`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L319)
- <a id="WorkaroundsTest._tokamax_patch_fixture._Tiny.__init__"></a>`WorkaroundsTest._tokamax_patch_fixture._Tiny.__init__` — [`L321`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L321)
- <a id="WorkaroundsTest.build"></a>`WorkaroundsTest.build` — [`L295`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L295)
- <a id="WorkaroundsTest.capture"></a>`WorkaroundsTest.capture` — [`L433`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L433)
- <a id="WorkaroundsTest.fake_local_attn"></a>`WorkaroundsTest.fake_local_attn` — [`L743`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L743)
- <a id="WorkaroundsTest.fake_redistribute"></a>`WorkaroundsTest.fake_redistribute` — [`L727`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L727)
- <a id="WorkaroundsTest.fallback"></a>`WorkaroundsTest.fallback` — [`L638`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L638)
- <a id="WorkaroundsTest.mock_splash_sdpa_capture"></a>`WorkaroundsTest.mock_splash_sdpa_capture` — [`L31`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L31)
- <a id="WorkaroundsTest.reference_linear_loss"></a>`WorkaroundsTest.reference_linear_loss` — [`L184`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L184)
- <a id="WorkaroundsTest.test_all_gather_cp_config_and_numerical_parity"></a>`WorkaroundsTest.test_all_gather_cp_config_and_numerical_parity` — [`L770`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L770) — documented in [tpu-context-parallel-attention](../../../../../concepts/tpu-context-parallel-attention.md)
- <a id="WorkaroundsTest.test_all_gather_cp_needs_a_kernel_off_cpu"></a>`WorkaroundsTest.test_all_gather_cp_needs_a_kernel_off_cpu` — [`L956`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L956)
- <a id="WorkaroundsTest.test_all_gather_cp_reference_attention_limits"></a>`WorkaroundsTest.test_all_gather_cp_reference_attention_limits` — [`L984`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L984)
- <a id="WorkaroundsTest.test_all_gather_cp_requires_headtail_inputs"></a>`WorkaroundsTest.test_all_gather_cp_requires_headtail_inputs` — [`L1013`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L1013) — documented in [tpu-context-parallel-attention](../../../../../concepts/tpu-context-parallel-attention.md)
- <a id="WorkaroundsTest.test_cp_with_tp_or_ep_on_fsdp2_needs_spmd_types_fsdp"></a>`WorkaroundsTest.test_cp_with_tp_or_ep_on_fsdp2_needs_spmd_types_fsdp` — [`L1028`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L1028)
- <a id="WorkaroundsTest.test_cp_without_cp_recipe_is_rejected"></a>`WorkaroundsTest.test_cp_without_cp_recipe_is_rejected` — [`L656`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L656)
- <a id="WorkaroundsTest.test_fused_loss_matches_unfused_cross_entropy"></a>`WorkaroundsTest.test_fused_loss_matches_unfused_cross_entropy` — [`L144`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L144)
- <a id="WorkaroundsTest.test_loss_kernel_patch_keeps_hf_state_dict_adapter_working"></a>`WorkaroundsTest.test_loss_kernel_patch_keeps_hf_state_dict_adapter_working` — [`L246`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L246)
- <a id="WorkaroundsTest.test_loss_kernel_patch_preserves_weight_initialization"></a>`WorkaroundsTest.test_loss_kernel_patch_preserves_weight_initialization` — [`L274`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L274)
- <a id="WorkaroundsTest.test_pallas_loss_linear_patches_output_and_output_transform"></a>`WorkaroundsTest.test_pallas_loss_linear_patches_output_and_output_transform` — [`L229`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L229)
- <a id="WorkaroundsTest.test_pallas_loss_linear_preserves_state_dict_keys"></a>`WorkaroundsTest.test_pallas_loss_linear_preserves_state_dict_keys` — [`L103`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L103)
- <a id="WorkaroundsTest.test_pallas_loss_linear_preserves_state_dict_keys._TinyModel"></a>`WorkaroundsTest.test_pallas_loss_linear_preserves_state_dict_keys._TinyModel` — [`L115`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L115)
- <a id="WorkaroundsTest.test_pallas_loss_linear_preserves_state_dict_keys._TinyModel.__init__"></a>`WorkaroundsTest.test_pallas_loss_linear_preserves_state_dict_keys._TinyModel.__init__` — [`L117`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L117)
- <a id="WorkaroundsTest.test_qwen3_ulysses_cp_recipe_and_validation"></a>`WorkaroundsTest.test_qwen3_ulysses_cp_recipe_and_validation` — [`L550`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L550)
- <a id="WorkaroundsTest.test_splash_attention_auto_block_size_and_fallback"></a>`WorkaroundsTest.test_splash_attention_auto_block_size_and_fallback` — [`L623`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L623)
- <a id="WorkaroundsTest.test_splash_attention_patch_plugs_into_cp_attention"></a>`WorkaroundsTest.test_splash_attention_patch_plugs_into_cp_attention` — [`L491`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L491)
- <a id="WorkaroundsTest.test_splash_patch_warns_on_cp_block_skipping"></a>`WorkaroundsTest.test_splash_patch_warns_on_cp_block_skipping` — [`L517`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L517)
- <a id="WorkaroundsTest.test_tokamax_patch_accepts_a_config_with_no_splash_fields"></a>`WorkaroundsTest.test_tokamax_patch_accepts_a_config_with_no_splash_fields` — [`L381`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L381)
- <a id="WorkaroundsTest.test_tokamax_patch_accepts_a_config_with_no_splash_fields._NotASplashConfig"></a>`WorkaroundsTest.test_tokamax_patch_accepts_a_config_with_no_splash_fields._NotASplashConfig` — [`L392`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L392)
- <a id="WorkaroundsTest.test_tokamax_patch_drops_kwargs_the_kernel_does_not_accept"></a>`WorkaroundsTest.test_tokamax_patch_drops_kwargs_the_kernel_does_not_accept` — [`L397`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L397)
- <a id="WorkaroundsTest.test_tokamax_patch_forwards_segment_ids"></a>`WorkaroundsTest.test_tokamax_patch_forwards_segment_ids` — [`L416`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L416)
- <a id="WorkaroundsTest.test_tokamax_patch_forwards_splash_config"></a>`WorkaroundsTest.test_tokamax_patch_forwards_splash_config` — [`L342`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L342) — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)
- <a id="WorkaroundsTest.test_tokamax_patch_raises_when_a_splash_config_resolves_nothing"></a>`WorkaroundsTest.test_tokamax_patch_raises_when_a_splash_config_resolves_nothing` — [`L369`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L369)
- <a id="WorkaroundsTest.test_tokamax_patch_raises_when_a_splash_config_resolves_nothing._BrokenSplash"></a>`WorkaroundsTest.test_tokamax_patch_raises_when_a_splash_config_resolves_nothing._BrokenSplash` — [`L373`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L373)
- <a id="WorkaroundsTest.test_tokamax_patch_raises_when_a_splash_config_resolves_nothing._BrokenSplash.sa_block_kv"></a>`WorkaroundsTest.test_tokamax_patch_raises_when_a_splash_config_resolves_nothing._BrokenSplash.sa_block_kv` — [`L376`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L376)
- <a id="WorkaroundsTest.test_tokamax_patch_raises_when_a_splash_config_resolves_nothing._BrokenSplash.sa_block_q"></a>`WorkaroundsTest.test_tokamax_patch_raises_when_a_splash_config_resolves_nothing._BrokenSplash.sa_block_q` — [`L375`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L375)
- <a id="WorkaroundsTest.test_tokamax_patch_raises_when_a_splash_config_resolves_nothing._BrokenSplash.use_tokamax_splash_attention_kernel"></a>`WorkaroundsTest.test_tokamax_patch_raises_when_a_splash_config_resolves_nothing._BrokenSplash.use_tokamax_splash_attention_kernel` — [`L374`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L374)
- <a id="WorkaroundsTest.test_tokamax_patch_warns_on_unsupported_block_skipping"></a>`WorkaroundsTest.test_tokamax_patch_warns_on_unsupported_block_skipping` — [`L469`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L469)
- <a id="WorkaroundsTest.test_tpu_cp_inner_attention_lookup"></a>`WorkaroundsTest.test_tpu_cp_inner_attention_lookup` — [`L597`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L597)
- <a id="WorkaroundsTest.test_tpu_selective_ac_recomputes_saved_collectives"></a>`WorkaroundsTest.test_tpu_selective_ac_recomputes_saved_collectives` — [`L683`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L683)
- <a id="WorkaroundsTest.test_ulysses_cp_repeats_kv_heads"></a>`WorkaroundsTest.test_ulysses_cp_repeats_kv_heads` — [`L712`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L712)
- <a id="WorkaroundsTest.test_wait_helper_waits_async_tensors_once"></a>`WorkaroundsTest.test_wait_helper_waits_async_tensors_once` — [`L666`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L666)
- <a id="WorkaroundsTest.test_wrapper_conversion_positions_to_segment_ids"></a>`WorkaroundsTest.test_wrapper_conversion_positions_to_segment_ids` — [`L19`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L19)
- <a id="_Tiny.attn"></a>`_Tiny.attn` — [`L325`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L325)
- <a id="_TinyModel.lm_head"></a>`_TinyModel.lm_head` — [`L119`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_workarounds.py#L119)
