---
title: 'Module: torchtitan/experiments/rl/tests/test_async_controller.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/tests/test_async_controller.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.tests.test_async_controller`/
symbols:
  test_batcher_filters_training_samples_longer_than_context: test_batcher_filters_training_samples_longer_than_context().
  _training_sample: _training_sample().
  test_untrainable_group_releases_before_training.run: test_untrainable_group_releases_before_training().run().
  test_take_finalized_does_not_release_active_slot.run: test_take_finalized_does_not_release_active_slot().run().
  _trainable_group: _trainable_group().
  test_batcher_carries_metric_only_groups_until_trainable_batch: test_batcher_carries_metric_only_groups_until_trainable_batch().
  _untrainable_group: _untrainable_group().
  _admit: _admit().
  test_windowed_fifo_takes_within_anchored_window.run: test_windowed_fifo_takes_within_anchored_window().run().
  test_compute_perf_ratio_metrics_reads_flushed_means: test_compute_perf_ratio_metrics_reads_flushed_means().
  _finalize: _finalize().
  _build_batcher: _build_batcher().
  test_microbatch_grid_avoids_all_padding_cells_when_possible: test_microbatch_grid_avoids_all_padding_cells_when_possible().
  test_document_limit_applies_to_each_local_microbatch: test_document_limit_applies_to_each_local_microbatch().
  test_document_limit_can_be_smaller_than_rows_per_microbatch: test_document_limit_can_be_smaller_than_rows_per_microbatch().
  test_compute_perf_ratio_metrics_skips_missing_spans: test_compute_perf_ratio_metrics_skips_missing_spans().
  test_rollout_id_to_string_is_callable_and_uses_int_group_id: test_rollout_id_to_string_is_callable_and_uses_int_group_id().
  test_batcher_resets_no_progress_count_on_trainable_group: test_batcher_resets_no_progress_count_on_trainable_group().
  _fifo_buffer: _fifo_buffer().
  test_batcher_counts_trainable_groups_not_rollouts: test_batcher_counts_trainable_groups_not_rollouts().
  test_batcher_warns_after_each_batch_of_untrainable_groups: test_batcher_warns_after_each_batch_of_untrainable_groups().
  test_batcher_raises_at_consecutive_untrainable_group_limit: test_batcher_raises_at_consecutive_untrainable_group_limit().
  test_batcher_requires_whole_rows_per_microbatch: test_batcher_requires_whole_rows_per_microbatch().
  test_metrics_timer_flush_drains: test_metrics_timer_flush_drains().
  test_compute_policy_age_metrics_uses_hard_offpolicy_limit: test_compute_policy_age_metrics_uses_hard_offpolicy_limit().
  test_compute_perf_ratio_metrics_returns_empty_without_total: test_compute_perf_ratio_metrics_returns_empty_without_total().
  test_take_finalized_does_not_release_active_slot: test_take_finalized_does_not_release_active_slot().
  test_untrainable_group_releases_before_training: test_untrainable_group_releases_before_training().
  test_compute_policy_age_metrics_raises_on_consume_time_staleness: test_compute_policy_age_metrics_raises_on_consume_time_staleness().
  test_work_buffer_rejects_window_larger_than_capacity: test_work_buffer_rejects_window_larger_than_capacity().
  test_windowed_fifo_takes_within_anchored_window: test_windowed_fifo_takes_within_anchored_window().
---
# Module: [`torchtitan/experiments/rl/tests/test_async_controller.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py)

> **Collapsed catalog** (31 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="_admit"></a>`_admit` — [`L397`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L397)
- <a id="_build_batcher"></a>`_build_batcher` — [`L61`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L61)
- <a id="_fifo_buffer"></a>`_fifo_buffer` — [`L385`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L385)
- <a id="_finalize"></a>`_finalize` — [`L403`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L403)
- <a id="_trainable_group"></a>`_trainable_group` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L46)
- <a id="_training_sample"></a>`_training_sample` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L34)
- <a id="_untrainable_group"></a>`_untrainable_group` — [`L57`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L57)
- <a id="test_batcher_carries_metric_only_groups_until_trainable_batch"></a>`test_batcher_carries_metric_only_groups_until_trainable_batch` — [`L87`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L87)
- <a id="test_batcher_counts_trainable_groups_not_rollouts"></a>`test_batcher_counts_trainable_groups_not_rollouts` — [`L71`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L71)
- <a id="test_batcher_filters_training_samples_longer_than_context"></a>`test_batcher_filters_training_samples_longer_than_context` — [`L213`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L213)
- <a id="test_batcher_raises_at_consecutive_untrainable_group_limit"></a>`test_batcher_raises_at_consecutive_untrainable_group_limit` — [`L136`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L136)
- <a id="test_batcher_requires_whole_rows_per_microbatch"></a>`test_batcher_requires_whole_rows_per_microbatch` — [`L249`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L249)
- <a id="test_batcher_resets_no_progress_count_on_trainable_group"></a>`test_batcher_resets_no_progress_count_on_trainable_group` — [`L119`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L119)
- <a id="test_batcher_warns_after_each_batch_of_untrainable_groups"></a>`test_batcher_warns_after_each_batch_of_untrainable_groups` — [`L104`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L104)
- <a id="test_compute_perf_ratio_metrics_reads_flushed_means"></a>`test_compute_perf_ratio_metrics_reads_flushed_means` — [`L260`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L260)
- <a id="test_compute_perf_ratio_metrics_returns_empty_without_total"></a>`test_compute_perf_ratio_metrics_returns_empty_without_total` — [`L289`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L289)
- <a id="test_compute_perf_ratio_metrics_skips_missing_spans"></a>`test_compute_perf_ratio_metrics_skips_missing_spans` — [`L277`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L277)
- <a id="test_compute_policy_age_metrics_raises_on_consume_time_staleness"></a>`test_compute_policy_age_metrics_raises_on_consume_time_staleness` — [`L357`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L357)
- <a id="test_compute_policy_age_metrics_uses_hard_offpolicy_limit"></a>`test_compute_policy_age_metrics_uses_hard_offpolicy_limit` — [`L367`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L367)
- <a id="test_document_limit_applies_to_each_local_microbatch"></a>`test_document_limit_applies_to_each_local_microbatch` — [`L169`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L169)
- <a id="test_document_limit_can_be_smaller_than_rows_per_microbatch"></a>`test_document_limit_can_be_smaller_than_rows_per_microbatch` — [`L194`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L194)
- <a id="test_metrics_timer_flush_drains"></a>`test_metrics_timer_flush_drains` — [`L295`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L295)
- <a id="test_microbatch_grid_avoids_all_padding_cells_when_possible"></a>`test_microbatch_grid_avoids_all_padding_cells_when_possible` — [`L146`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L146)
- <a id="test_rollout_id_to_string_is_callable_and_uses_int_group_id"></a>`test_rollout_id_to_string_is_callable_and_uses_int_group_id` — [`L303`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L303)
- <a id="test_take_finalized_does_not_release_active_slot"></a>`test_take_finalized_does_not_release_active_slot` — [`L309`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L309)
- <a id="test_take_finalized_does_not_release_active_slot.run"></a>`test_take_finalized_does_not_release_active_slot.run` — [`L310`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L310)
- <a id="test_untrainable_group_releases_before_training"></a>`test_untrainable_group_releases_before_training` — [`L328`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L328)
- <a id="test_untrainable_group_releases_before_training.run"></a>`test_untrainable_group_releases_before_training.run` — [`L329`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L329)
- <a id="test_windowed_fifo_takes_within_anchored_window"></a>`test_windowed_fifo_takes_within_anchored_window` — [`L407`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L407)
- <a id="test_windowed_fifo_takes_within_anchored_window.run"></a>`test_windowed_fifo_takes_within_anchored_window.run` — [`L408`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L408)
- <a id="test_work_buffer_rejects_window_larger_than_capacity"></a>`test_work_buffer_rejects_window_larger_than_capacity` — [`L392`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_async_controller.py#L392)
