---
title: 'Module: torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.muse_glimmer.tests.test_muse_glimmer_config`/
symbols:
  MuseGlimmerConfigTest.test_fused_ce_recipe_carries_soft_cap_into_loss: MuseGlimmerConfigTest#test_fused_ce_recipe_carries_soft_cap_into_loss().
  MuseGlimmerConfigTest.test_model_registry_uses_tpu_parallelize: MuseGlimmerConfigTest#test_model_registry_uses_tpu_parallelize().
  MuseGlimmerConfigTest.test_tpu_attention_matches_upstream_on_single_document: MuseGlimmerConfigTest#test_tpu_attention_matches_upstream_on_single_document().
  _get_model_config: _get_model_config().
  MuseGlimmerConfigTest.test_logit_transform_check_rejects_untransformed_loss: MuseGlimmerConfigTest#test_logit_transform_check_rejects_untransformed_loss().
  MuseGlimmerConfigTest.test_logit_transform_check_rejects_non_fused_loss: MuseGlimmerConfigTest#test_logit_transform_check_rejects_non_fused_loss().
  MuseGlimmerConfigTest.test_testmodel_layer_pattern: MuseGlimmerConfigTest#test_testmodel_layer_pattern().
  MuseGlimmerConfigTest.test_packed_mask_matches_upstream_flex_document_mask: MuseGlimmerConfigTest#test_packed_mask_matches_upstream_flex_document_mask().
  MuseGlimmerConfigTest.test_loss_kernel_rejects_soft_capped_lm_head: MuseGlimmerConfigTest#test_loss_kernel_rejects_soft_capped_lm_head().
  MuseGlimmerConfigTest.test_30b_recipe_trainer_loss_and_optimizer_selection: MuseGlimmerConfigTest#test_30b_recipe_trainer_loss_and_optimizer_selection().
  MuseGlimmerConfigTest.test_30b_fused_ce_recipe_passes_logit_transform_check: MuseGlimmerConfigTest#test_30b_fused_ce_recipe_passes_logit_transform_check().
  MuseGlimmerConfigTest.test_rejects_invalid_window: MuseGlimmerConfigTest#test_rejects_invalid_window().
  MuseGlimmerConfigTest.test_sliding_window_changes_output: MuseGlimmerConfigTest#test_sliding_window_changes_output().
  MuseGlimmerConfigTest.test_model_registry_uses_tpu_outer_attention: MuseGlimmerConfigTest#test_model_registry_uses_tpu_outer_attention().
  MuseGlimmerConfigTest.test_attention_isolates_packed_documents: MuseGlimmerConfigTest#test_attention_isolates_packed_documents().
  MuseGlimmerConfigTest.test_logit_transform_check_rejects_mismatched_multiplier: MuseGlimmerConfigTest#test_logit_transform_check_rejects_mismatched_multiplier().
  MuseGlimmerConfigTest.test_splash_window_is_one_less_than_muse_window: MuseGlimmerConfigTest#test_splash_window_is_one_less_than_muse_window().
  MuseGlimmerConfigTest._build_fused_ce_model: MuseGlimmerConfigTest#_build_fused_ce_model().
  MuseGlimmerConfigTest.test_fused_ce_recipe_passes_logit_transform_check: MuseGlimmerConfigTest#test_fused_ce_recipe_passes_logit_transform_check().
  MuseGlimmerConfigTest.test_30b_full_logits_readme_memory_overrides: MuseGlimmerConfigTest#test_30b_full_logits_readme_memory_overrides().
  MuseGlimmerConfigTest._build_attention: MuseGlimmerConfigTest#_build_attention().
  MuseGlimmerConfigTest.test_30b_layer_pattern: MuseGlimmerConfigTest#test_30b_layer_pattern().
  MuseGlimmerConfigTest.test_model_registry_rejects_long_testmodel_seq_len: MuseGlimmerConfigTest#test_model_registry_rejects_long_testmodel_seq_len().
  MuseGlimmerConfigTest.test_loss_kernel_still_wraps_plain_linear_lm_head: MuseGlimmerConfigTest#test_loss_kernel_still_wraps_plain_linear_lm_head().
  MuseGlimmerConfigTest.test_sliding_window_mask_semantics: MuseGlimmerConfigTest#test_sliding_window_mask_semantics().
  MuseGlimmerConfigTest.test_window_size_one_attends_only_to_self: MuseGlimmerConfigTest#test_window_size_one_attends_only_to_self().
  MuseGlimmerConfigTest.test_splash_patch_matches_inner_attention_class_name: MuseGlimmerConfigTest#test_splash_patch_matches_inner_attention_class_name().
  MuseGlimmerConfigTest.test_model_registry_rejects_unknown_flavor: MuseGlimmerConfigTest#test_model_registry_rejects_unknown_flavor().
  _FUSED_LOSS_OVERRIDE_PATH: _FUSED_LOSS_OVERRIDE_PATH.
  MuseGlimmerConfigTest: MuseGlimmerConfigTest#
  MuseGlimmerConfigTest.test_30b_recipes_share_upstream_model_and_flags: MuseGlimmerConfigTest#test_30b_recipes_share_upstream_model_and_flags().
  MuseGlimmerConfigTest.test_30b_graph_trainer_recipes_use_zero3_and_remat_policy: MuseGlimmerConfigTest#test_30b_graph_trainer_recipes_use_zero3_and_remat_policy().
---
# Module: [`torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py)

> **Collapsed catalog** (32 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="MuseGlimmerConfigTest"></a>`MuseGlimmerConfigTest` — [`L55`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L55)
- <a id="MuseGlimmerConfigTest._build_attention"></a>`MuseGlimmerConfigTest._build_attention` — [`L227`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L227)
- <a id="MuseGlimmerConfigTest._build_fused_ce_model"></a>`MuseGlimmerConfigTest._build_fused_ce_model` — [`L325`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L325)
- <a id="MuseGlimmerConfigTest.test_30b_full_logits_readme_memory_overrides"></a>`MuseGlimmerConfigTest.test_30b_full_logits_readme_memory_overrides` — [`L448`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L448)
- <a id="MuseGlimmerConfigTest.test_30b_fused_ce_recipe_passes_logit_transform_check"></a>`MuseGlimmerConfigTest.test_30b_fused_ce_recipe_passes_logit_transform_check` — [`L465`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L465)
- <a id="MuseGlimmerConfigTest.test_30b_graph_trainer_recipes_use_zero3_and_remat_policy"></a>`MuseGlimmerConfigTest.test_30b_graph_trainer_recipes_use_zero3_and_remat_policy` — [`L415`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L415)
- <a id="MuseGlimmerConfigTest.test_30b_layer_pattern"></a>`MuseGlimmerConfigTest.test_30b_layer_pattern` — [`L142`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L142)
- <a id="MuseGlimmerConfigTest.test_30b_recipe_trainer_loss_and_optimizer_selection"></a>`MuseGlimmerConfigTest.test_30b_recipe_trainer_loss_and_optimizer_selection` — [`L389`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L389)
- <a id="MuseGlimmerConfigTest.test_30b_recipes_share_upstream_model_and_flags"></a>`MuseGlimmerConfigTest.test_30b_recipes_share_upstream_model_and_flags` — [`L365`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L365)
- <a id="MuseGlimmerConfigTest.test_attention_isolates_packed_documents"></a>`MuseGlimmerConfigTest.test_attention_isolates_packed_documents` — [`L232`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L232)
- <a id="MuseGlimmerConfigTest.test_fused_ce_recipe_carries_soft_cap_into_loss"></a>`MuseGlimmerConfigTest.test_fused_ce_recipe_carries_soft_cap_into_loss` — [`L291`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L291)
- <a id="MuseGlimmerConfigTest.test_fused_ce_recipe_passes_logit_transform_check"></a>`MuseGlimmerConfigTest.test_fused_ce_recipe_passes_logit_transform_check` — [`L330`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L330)
- <a id="MuseGlimmerConfigTest.test_logit_transform_check_rejects_mismatched_multiplier"></a>`MuseGlimmerConfigTest.test_logit_transform_check_rejects_mismatched_multiplier` — [`L336`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L336)
- <a id="MuseGlimmerConfigTest.test_logit_transform_check_rejects_non_fused_loss"></a>`MuseGlimmerConfigTest.test_logit_transform_check_rejects_non_fused_loss` — [`L352`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L352)
- <a id="MuseGlimmerConfigTest.test_logit_transform_check_rejects_untransformed_loss"></a>`MuseGlimmerConfigTest.test_logit_transform_check_rejects_untransformed_loss` — [`L344`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L344)
- <a id="MuseGlimmerConfigTest.test_loss_kernel_rejects_soft_capped_lm_head"></a>`MuseGlimmerConfigTest.test_loss_kernel_rejects_soft_capped_lm_head` — [`L276`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L276)
- <a id="MuseGlimmerConfigTest.test_loss_kernel_still_wraps_plain_linear_lm_head"></a>`MuseGlimmerConfigTest.test_loss_kernel_still_wraps_plain_linear_lm_head` — [`L284`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L284)
- <a id="MuseGlimmerConfigTest.test_model_registry_rejects_long_testmodel_seq_len"></a>`MuseGlimmerConfigTest.test_model_registry_rejects_long_testmodel_seq_len` — [`L176`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L176)
- <a id="MuseGlimmerConfigTest.test_model_registry_rejects_unknown_flavor"></a>`MuseGlimmerConfigTest.test_model_registry_rejects_unknown_flavor` — [`L171`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L171)
- <a id="MuseGlimmerConfigTest.test_model_registry_uses_tpu_outer_attention"></a>`MuseGlimmerConfigTest.test_model_registry_uses_tpu_outer_attention` — [`L184`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L184)
- <a id="MuseGlimmerConfigTest.test_model_registry_uses_tpu_parallelize"></a>`MuseGlimmerConfigTest.test_model_registry_uses_tpu_parallelize` — [`L157`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L157)
- <a id="MuseGlimmerConfigTest.test_packed_mask_matches_upstream_flex_document_mask"></a>`MuseGlimmerConfigTest.test_packed_mask_matches_upstream_flex_document_mask` — [`L193`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L193)
- <a id="MuseGlimmerConfigTest.test_rejects_invalid_window"></a>`MuseGlimmerConfigTest.test_rejects_invalid_window` — [`L82`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L82)
- <a id="MuseGlimmerConfigTest.test_sliding_window_changes_output"></a>`MuseGlimmerConfigTest.test_sliding_window_changes_output` — [`L89`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L89)
- <a id="MuseGlimmerConfigTest.test_sliding_window_mask_semantics"></a>`MuseGlimmerConfigTest.test_sliding_window_mask_semantics` — [`L58`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L58)
- <a id="MuseGlimmerConfigTest.test_splash_patch_matches_inner_attention_class_name"></a>`MuseGlimmerConfigTest.test_splash_patch_matches_inner_attention_class_name` — [`L107`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L107)
- <a id="MuseGlimmerConfigTest.test_splash_window_is_one_less_than_muse_window"></a>`MuseGlimmerConfigTest.test_splash_window_is_one_less_than_muse_window` — [`L132`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L132)
- <a id="MuseGlimmerConfigTest.test_testmodel_layer_pattern"></a>`MuseGlimmerConfigTest.test_testmodel_layer_pattern` — [`L115`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L115)
- <a id="MuseGlimmerConfigTest.test_tpu_attention_matches_upstream_on_single_document"></a>`MuseGlimmerConfigTest.test_tpu_attention_matches_upstream_on_single_document` — [`L253`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L253)
- <a id="MuseGlimmerConfigTest.test_window_size_one_attends_only_to_self"></a>`MuseGlimmerConfigTest.test_window_size_one_attends_only_to_self` — [`L75`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L75)
- <a id="_FUSED_LOSS_OVERRIDE_PATH"></a>`_FUSED_LOSS_OVERRIDE_PATH` — [`L33`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L33)
- <a id="_get_model_config"></a>`_get_model_config` — [`L39`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py#L39)
