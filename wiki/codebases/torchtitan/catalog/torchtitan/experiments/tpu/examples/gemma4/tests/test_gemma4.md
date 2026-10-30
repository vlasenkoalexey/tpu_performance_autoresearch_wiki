---
title: 'Module: torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.examples.gemma4.tests.test_gemma4`/
symbols:
  TestGemma4SdpaSlidingWindow.test_sliding_window_applied_beyond_window: TestGemma4SdpaSlidingWindow#test_sliding_window_applied_beyond_window().
  TestGemma4HFReferenceParity.test_one_step_matches_hf: TestGemma4HFReferenceParity#test_one_step_matches_hf().
  TestGemma4SoftCappedLoss.test_chunked_loss_matches_full_cross_entropy_with_soft_cap: TestGemma4SoftCappedLoss#test_chunked_loss_matches_full_cross_entropy_with_soft_cap().
  TestGemma4HFReferenceParity.test_tied_hf_safetensors_load_into_untied_recipe: TestGemma4HFReferenceParity#test_tied_hf_safetensors_load_into_untied_recipe().
  TestTpuGroupedExpertsActivation.test_gelu_tanh_vs_silu_forward: TestTpuGroupedExpertsActivation#test_gelu_tanh_vs_silu_forward().
  TestTpuGroupedExpertsActivation.test_silu_delegates_to_super_and_gelu_uses_grouped_mm_seam: TestTpuGroupedExpertsActivation#test_silu_delegates_to_super_and_gelu_uses_grouped_mm_seam().
  TestTpuGroupedExpertsActivation.test_config_registry_valid: TestTpuGroupedExpertsActivation#test_config_registry_valid().
  TestTpuGroupedExpertsActivation.test_context_parallel_rejected: TestTpuGroupedExpertsActivation#test_context_parallel_rejected().
  TestTpuGroupedExpertsActivation.test_moe_spmd_safe_applied_when_ep_disabled: TestTpuGroupedExpertsActivation#test_moe_spmd_safe_applied_when_ep_disabled().
  TestTpuGroupedExpertsActivation.test_converter_propagates_gemma4_gelu_tanh: TestTpuGroupedExpertsActivation#test_converter_propagates_gemma4_gelu_tanh().
  TestTpuGroupedExpertsActivation.test_build_flavor_config_weight_tying: TestTpuGroupedExpertsActivation#test_build_flavor_config_weight_tying().
  TestGemma4StateDictAdapter.test_dense_state_dict_roundtrip: TestGemma4StateDictAdapter#test_dense_state_dict_roundtrip().
  TestGemma4StateDictAdapter.test_moe_state_dict_roundtrip_and_vision_skip: TestGemma4StateDictAdapter#test_moe_state_dict_roundtrip_and_vision_skip().
  TestGemma4StateDictAdapter.test_tied_hf_checkpoint_loads_into_untied_recipe: TestGemma4StateDictAdapter#test_tied_hf_checkpoint_loads_into_untied_recipe().
  TestGemma4SoftCappedLoss.test_legacy_loss_kernel_rejects_soft_capped_lm_head: TestGemma4SoftCappedLoss#test_legacy_loss_kernel_rejects_soft_capped_lm_head().
  TestGemma4SdpaSlidingWindow._SEQ_LEN: TestGemma4SdpaSlidingWindow#_SEQ_LEN.
  TestGemma4SdpaSlidingWindow.test_flavor_sliding_layers_use_windowed_sdpa: TestGemma4SdpaSlidingWindow#test_flavor_sliding_layers_use_windowed_sdpa().
  TestGemma4SdpaSlidingWindow._DIM: TestGemma4SdpaSlidingWindow#_DIM.
  TestGemma4StateDictAdapter.test_fused_qkv_rejected: TestGemma4StateDictAdapter#test_fused_qkv_rejected().
  TestGemma4SdpaSlidingWindow._attention_with_mask: TestGemma4SdpaSlidingWindow#_attention_with_mask().
  TestGemma4SdpaSlidingWindow.masked_sdpa: TestGemma4SdpaSlidingWindow#masked_sdpa().
  _LINEAR_INIT: _LINEAR_INIT.
  _EXPERTS_INIT: _EXPERTS_INIT.
  TestGemma4SdpaSlidingWindow._WINDOW: TestGemma4SdpaSlidingWindow#_WINDOW.
  TestTpuGroupedExpertsActivation: TestTpuGroupedExpertsActivation#
  TestGemma4HFReferenceParity: TestGemma4HFReferenceParity#
  TestGemma4HFReferenceParity.setUp: TestGemma4HFReferenceParity#setUp().
  TestGemma4HFReferenceParity._build_hf_reference: TestGemma4HFReferenceParity#_build_hf_reference().
  _NORM_INIT: _NORM_INIT.
  TestGemma4StateDictAdapter: TestGemma4StateDictAdapter#
  TestGemma4SoftCappedLoss: TestGemma4SoftCappedLoss#
  TestGemma4SdpaSlidingWindow: TestGemma4SdpaSlidingWindow#
---
# Module: [`torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py)

> **Collapsed catalog** (32 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="TestGemma4HFReferenceParity"></a>`TestGemma4HFReferenceParity` — [`L577`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L577)
- <a id="TestGemma4HFReferenceParity._build_hf_reference"></a>`TestGemma4HFReferenceParity._build_hf_reference` — [`L588`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L588)
- <a id="TestGemma4HFReferenceParity.setUp"></a>`TestGemma4HFReferenceParity.setUp` — [`L580`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L580)
- <a id="TestGemma4HFReferenceParity.test_one_step_matches_hf"></a>`TestGemma4HFReferenceParity.test_one_step_matches_hf` — [`L649`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L649) — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)
- <a id="TestGemma4HFReferenceParity.test_tied_hf_safetensors_load_into_untied_recipe"></a>`TestGemma4HFReferenceParity.test_tied_hf_safetensors_load_into_untied_recipe` — [`L772`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L772)
- <a id="TestGemma4SdpaSlidingWindow"></a>`TestGemma4SdpaSlidingWindow` — [`L457`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L457)
- <a id="TestGemma4SdpaSlidingWindow._DIM"></a>`TestGemma4SdpaSlidingWindow._DIM` — [`L462`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L462)
- <a id="TestGemma4SdpaSlidingWindow._SEQ_LEN"></a>`TestGemma4SdpaSlidingWindow._SEQ_LEN` — [`L461`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L461)
- <a id="TestGemma4SdpaSlidingWindow._WINDOW"></a>`TestGemma4SdpaSlidingWindow._WINDOW` — [`L460`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L460)
- <a id="TestGemma4SdpaSlidingWindow._attention_with_mask"></a>`TestGemma4SdpaSlidingWindow._attention_with_mask` — [`L464`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L464)
- <a id="TestGemma4SdpaSlidingWindow.masked_sdpa"></a>`TestGemma4SdpaSlidingWindow.masked_sdpa` — [`L468`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L468)
- <a id="TestGemma4SdpaSlidingWindow.test_flavor_sliding_layers_use_windowed_sdpa"></a>`TestGemma4SdpaSlidingWindow.test_flavor_sliding_layers_use_windowed_sdpa` — [`L561`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L561)
- <a id="TestGemma4SdpaSlidingWindow.test_sliding_window_applied_beyond_window"></a>`TestGemma4SdpaSlidingWindow.test_sliding_window_applied_beyond_window` — [`L490`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L490)
- <a id="TestGemma4SoftCappedLoss"></a>`TestGemma4SoftCappedLoss` — [`L403`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L403)
- <a id="TestGemma4SoftCappedLoss.test_chunked_loss_matches_full_cross_entropy_with_soft_cap"></a>`TestGemma4SoftCappedLoss.test_chunked_loss_matches_full_cross_entropy_with_soft_cap` — [`L406`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L406)
- <a id="TestGemma4SoftCappedLoss.test_legacy_loss_kernel_rejects_soft_capped_lm_head"></a>`TestGemma4SoftCappedLoss.test_legacy_loss_kernel_rejects_soft_capped_lm_head` — [`L448`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L448)
- <a id="TestGemma4StateDictAdapter"></a>`TestGemma4StateDictAdapter` — [`L278`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L278)
- <a id="TestGemma4StateDictAdapter.test_dense_state_dict_roundtrip"></a>`TestGemma4StateDictAdapter.test_dense_state_dict_roundtrip` — [`L281`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L281)
- <a id="TestGemma4StateDictAdapter.test_fused_qkv_rejected"></a>`TestGemma4StateDictAdapter.test_fused_qkv_rejected` — [`L366`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L366)
- <a id="TestGemma4StateDictAdapter.test_moe_state_dict_roundtrip_and_vision_skip"></a>`TestGemma4StateDictAdapter.test_moe_state_dict_roundtrip_and_vision_skip` — [`L319`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L319)
- <a id="TestGemma4StateDictAdapter.test_tied_hf_checkpoint_loads_into_untied_recipe"></a>`TestGemma4StateDictAdapter.test_tied_hf_checkpoint_loads_into_untied_recipe` — [`L373`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L373)
- <a id="TestTpuGroupedExpertsActivation"></a>`TestTpuGroupedExpertsActivation` — [`L65`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L65)
- <a id="TestTpuGroupedExpertsActivation.test_build_flavor_config_weight_tying"></a>`TestTpuGroupedExpertsActivation.test_build_flavor_config_weight_tying` — [`L124`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L124)
- <a id="TestTpuGroupedExpertsActivation.test_config_registry_valid"></a>`TestTpuGroupedExpertsActivation.test_config_registry_valid` — [`L111`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L111)
- <a id="TestTpuGroupedExpertsActivation.test_context_parallel_rejected"></a>`TestTpuGroupedExpertsActivation.test_context_parallel_rejected` — [`L205`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L205)
- <a id="TestTpuGroupedExpertsActivation.test_converter_propagates_gemma4_gelu_tanh"></a>`TestTpuGroupedExpertsActivation.test_converter_propagates_gemma4_gelu_tanh` — [`L100`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L100)
- <a id="TestTpuGroupedExpertsActivation.test_gelu_tanh_vs_silu_forward"></a>`TestTpuGroupedExpertsActivation.test_gelu_tanh_vs_silu_forward` — [`L68`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L68)
- <a id="TestTpuGroupedExpertsActivation.test_moe_spmd_safe_applied_when_ep_disabled"></a>`TestTpuGroupedExpertsActivation.test_moe_spmd_safe_applied_when_ep_disabled` — [`L234`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L234)
- <a id="TestTpuGroupedExpertsActivation.test_silu_delegates_to_super_and_gelu_uses_grouped_mm_seam"></a>`TestTpuGroupedExpertsActivation.test_silu_delegates_to_super_and_gelu_uses_grouped_mm_seam` — [`L160`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L160) — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)
- <a id="_EXPERTS_INIT"></a>`_EXPERTS_INIT` — [`L58`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L58)
- <a id="_LINEAR_INIT"></a>`_LINEAR_INIT` — [`L57`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L57)
- <a id="_NORM_INIT"></a>`_NORM_INIT` — [`L56`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py#L56)
