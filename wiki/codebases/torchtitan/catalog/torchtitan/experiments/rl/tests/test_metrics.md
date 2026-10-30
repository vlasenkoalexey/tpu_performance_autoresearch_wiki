---
title: 'Module: torchtitan/experiments/rl/tests/test_metrics.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/tests/test_metrics.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.tests.test_metrics`/
symbols:
  TestMetricsProcessorFanOut.test_log_aggregates_and_dispatches: TestMetricsProcessorFanOut#test_log_aggregates_and_dispatches().
  TestMetricsProcessorFanOut.test_log_isolates_failures: TestMetricsProcessorFanOut#test_log_isolates_failures().
  TestIsValidationSwitch.test_backends_get_every_call_regardless_of_console_filter: TestIsValidationSwitch#test_backends_get_every_call_regardless_of_console_filter().
  TestMetricsProcessorFanOut.test_close_isolates_failures: TestMetricsProcessorFanOut#test_close_isolates_failures().
  TestAggregator.test_groups_by_key_and_reduction: TestAggregator#test_groups_by_key_and_reduction().
  TestMetricsProcessorBuild.test_wandb_with_log_dir: TestMetricsProcessorBuild#test_wandb_with_log_dir().
  TestAggregatorWarnOnce.test_warns_once_on_all_empty_max: TestAggregatorWarnOnce#test_warns_once_on_all_empty_max().
  TestAggregator.test_nan_filtered: TestAggregator#test_nan_filtered().
  TestMetricsProcessorBuild.test_default_builds_no_backends: TestMetricsProcessorBuild#test_default_builds_no_backends().
  TestMean.test_from_list_basic: TestMean#test_from_list_basic().
  TestMean.test_empty_list_filtered: TestMean#test_empty_list_filtered().
  TestMaxMin.test_max_from_list: TestMaxMin#test_max_from_list().
  TestMaxMin.test_min_from_list: TestMaxMin#test_min_from_list().
  TestMaxMin.test_max_empty_filtered: TestMaxMin#test_max_empty_filtered().
  TestMaxMin.test_min_empty_filtered: TestMaxMin#test_min_empty_filtered().
  TestMaxMin.test_max_empty_actor_first_does_not_erase: TestMaxMin#test_max_empty_actor_first_does_not_erase().
  TestMaxMin.test_max_empty_actor_last_does_not_erase: TestMaxMin#test_max_empty_actor_last_does_not_erase().
  TestMaxMin.test_max_all_empty_returns_no_key: TestMaxMin#test_max_all_empty_returns_no_key().
  TestMaxMin.test_min_empty_actor_first_does_not_erase: TestMaxMin#test_min_empty_actor_first_does_not_erase().
  TestMaxMin.test_min_empty_actor_last_does_not_erase: TestMaxMin#test_min_empty_actor_last_does_not_erase().
  TestStd.test_from_list_matches_population_std: TestStd#test_from_list_matches_population_std().
  TestStd.test_combine_equals_concatenation: TestStd#test_combine_equals_concatenation().
  TestStd.test_empty_filtered: TestStd#test_empty_filtered().
  TestSummaryStats.test_five_keys_emitted: TestSummaryStats#test_five_keys_emitted().
  TestSummaryStats.test_empty_keeps_sum_zero: TestSummaryStats#test_empty_keeps_sum_zero().
  TestSummaryStats.test_combine_two_records: TestSummaryStats#test_combine_two_records().
  TestSum.test_from_list: TestSum#test_from_list().
  TestSum.test_does_not_collide_with_summary_stats_sum: TestSum#test_does_not_collide_with_summary_stats_sum().
  TestStdPreAggregated.test_pre_aggregated_equals_from_list: TestStdPreAggregated#test_pre_aggregated_equals_from_list().
  TestStdPreAggregated.test_combine_pre_aggregated_with_from_list: TestStdPreAggregated#test_combine_pre_aggregated_with_from_list().
  TestNoReduce.test_from_list_single: TestNoReduce#test_from_list_single().
  TestAggregator.test_mean_and_summary_stats_no_collision: TestAggregator#test_mean_and_summary_stats_no_collision().
  TestMetricsProcessorBuild.test_tensorboard_appends_backend: TestMetricsProcessorBuild#test_tensorboard_appends_backend().
  TestMetricsProcessorBuild.test_wandb_and_tensorboard_create_both: TestMetricsProcessorBuild#test_wandb_and_tensorboard_create_both().
  TestMetricsProcessorBuild.test_console_log_keys_round_trip: TestMetricsProcessorBuild#test_console_log_keys_round_trip().
  TestMetricsProcessorBuild.test_wandb_project_config_overrides_default: TestMetricsProcessorBuild#test_wandb_project_config_overrides_default().
  TestMean.test_weighted_combine: TestMean#test_weighted_combine().
  TestMean.test_single_value: TestMean#test_single_value().
  TestMaxMin.test_max_single: TestMaxMin#test_max_single().
  TestMaxMin.test_max_combine: TestMaxMin#test_max_combine().
  TestStd.test_single_value_zero: TestStd#test_single_value_zero().
  TestSum.test_combine: TestSum#test_combine().
  TestNoReduce.test_pass_through: TestNoReduce#test_pass_through().
  TestNoReduce.test_two_entries_same_key_raises: TestNoReduce#test_two_entries_same_key_raises().
  TestAggregator.test_duplicate_no_reduce_raises: TestAggregator#test_duplicate_no_reduce_raises().
  TestMetricsProcessorBuild.test_wandb_without_log_dir_raises: TestMetricsProcessorBuild#test_wandb_without_log_dir_raises().
  TestMetricsProcessorBuild.test_tensorboard_without_log_dir_raises: TestMetricsProcessorBuild#test_tensorboard_without_log_dir_raises().
  TestMetricsProcessorBuild.test_tensorboard_only_does_not_set_wandb_project_env: TestMetricsProcessorBuild#test_tensorboard_only_does_not_set_wandb_project_env().
  TestMetricsProcessorBuild.test_wandb_project_default_titan_rl: TestMetricsProcessorBuild#test_wandb_project_default_titan_rl().
  TestMetricsProcessorBuild.test_wandb_project_env_var_wins: TestMetricsProcessorBuild#test_wandb_project_env_var_wins().
  TestIsValidationSwitch.test_default_uses_train_allow_list: TestIsValidationSwitch#test_default_uses_train_allow_list().
  TestIsValidationSwitch.test_is_validation_uses_validation_allow_list_and_prefix: TestIsValidationSwitch#test_is_validation_uses_validation_allow_list_and_prefix().
  TestIsValidationSwitch.test_empty_train_list_silences_console: TestIsValidationSwitch#test_empty_train_list_silences_console().
  TestIsValidationSwitch.test_default_none_train_list_prints_all: TestIsValidationSwitch#test_default_none_train_list_prints_all().
  TestIsValidationSwitch._logger: TestIsValidationSwitch#_logger().
  _RecordingBackend.calls: _RecordingBackend#calls.
  TestNoReduce.test_from_list_empty_raises: TestNoReduce#test_from_list_empty_raises().
  TestNoReduce.test_from_list_multiple_raises: TestNoReduce#test_from_list_multiple_raises().
  TestAggregator.test_empty: TestAggregator#test_empty().
  _RecordingBackend: _RecordingBackend#
  _RaisingBackend.log_calls: _RaisingBackend#log_calls.
  TestStdPreAggregated.test_partial_args_raise: TestStdPreAggregated#test_partial_args_raise().
  TestLogToConsole.test_alphabetical_when_no_allow_list: TestLogToConsole#test_alphabetical_when_no_allow_list().
  TestLogToConsole.test_allow_list_none_prints_all: TestLogToConsole#test_allow_list_none_prints_all().
  TestLogToConsole.test_allow_list_empty_prints_nothing: TestLogToConsole#test_allow_list_empty_prints_nothing().
  TestLogToConsole.test_allow_list_regex_search: TestLogToConsole#test_allow_list_regex_search().
  TestLogToConsole.test_pattern_order_preserved: TestLogToConsole#test_pattern_order_preserved().
  TestLogToConsole.test_no_match_no_print: TestLogToConsole#test_no_match_no_print().
  TestLogToConsole.test_console_prefix_renders_before_step: TestLogToConsole#test_console_prefix_renders_before_step().
  test_fmt_metric_value: test_fmt_metric_value().
  test_metric_backend_is_base_logger: test_metric_backend_is_base_logger().
  _RecordingBackend.log: _RecordingBackend#log().
  _RecordingBackend.close: _RecordingBackend#close().
  _RaisingBackend.log: _RaisingBackend#log().
  _RaisingBackend.close: _RaisingBackend#close().
  _RecordingBackend.closed: _RecordingBackend#closed.
  _RaisingBackend: _RaisingBackend#
  _RaisingBackend.close_calls: _RaisingBackend#close_calls.
  TestMean: TestMean#
  TestMaxMin: TestMaxMin#
  TestStd: TestStd#
  TestSummaryStats: TestSummaryStats#
  TestSum: TestSum#
  TestStdPreAggregated: TestStdPreAggregated#
  TestNoReduce: TestNoReduce#
  TestAggregatorWarnOnce: TestAggregatorWarnOnce#
  TestAggregator: TestAggregator#
  TestLogToConsole: TestLogToConsole#
  _RecordingBackend.__init__: _RecordingBackend#__init__().
  _RaisingBackend.__init__: _RaisingBackend#__init__().
  TestMetricsProcessorFanOut: TestMetricsProcessorFanOut#
  TestMetricsProcessorBuild: TestMetricsProcessorBuild#
  TestIsValidationSwitch: TestIsValidationSwitch#
---
# Module: [`torchtitan/experiments/rl/tests/test_metrics.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py)

> **Collapsed catalog** (93 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="TestAggregator"></a>`TestAggregator` — [`L316`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L316)
- <a id="TestAggregator.test_duplicate_no_reduce_raises"></a>`TestAggregator.test_duplicate_no_reduce_raises` — [`L337`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L337)
- <a id="TestAggregator.test_empty"></a>`TestAggregator.test_empty` — [`L346`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L346)
- <a id="TestAggregator.test_groups_by_key_and_reduction"></a>`TestAggregator.test_groups_by_key_and_reduction` — [`L317`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L317)
- <a id="TestAggregator.test_mean_and_summary_stats_no_collision"></a>`TestAggregator.test_mean_and_summary_stats_no_collision` — [`L349`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L349)
- <a id="TestAggregator.test_nan_filtered"></a>`TestAggregator.test_nan_filtered` — [`L328`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L328)
- <a id="TestAggregatorWarnOnce"></a>`TestAggregatorWarnOnce` — [`L295`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L295)
- <a id="TestAggregatorWarnOnce.test_warns_once_on_all_empty_max"></a>`TestAggregatorWarnOnce.test_warns_once_on_all_empty_max` — [`L296`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L296)
- <a id="TestIsValidationSwitch"></a>`TestIsValidationSwitch` — [`L720`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L720)
- <a id="TestIsValidationSwitch._logger"></a>`TestIsValidationSwitch._logger` — [`L721`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L721)
- <a id="TestIsValidationSwitch.test_backends_get_every_call_regardless_of_console_filter"></a>`TestIsValidationSwitch.test_backends_get_every_call_regardless_of_console_filter` — [`L782`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L782)
- <a id="TestIsValidationSwitch.test_default_none_train_list_prints_all"></a>`TestIsValidationSwitch.test_default_none_train_list_prints_all` — [`L764`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L764)
- <a id="TestIsValidationSwitch.test_default_uses_train_allow_list"></a>`TestIsValidationSwitch.test_default_uses_train_allow_list` — [`L724`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L724)
- <a id="TestIsValidationSwitch.test_empty_train_list_silences_console"></a>`TestIsValidationSwitch.test_empty_train_list_silences_console` — [`L756`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L756)
- <a id="TestIsValidationSwitch.test_is_validation_uses_validation_allow_list_and_prefix"></a>`TestIsValidationSwitch.test_is_validation_uses_validation_allow_list_and_prefix` — [`L739`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L739)
- <a id="TestLogToConsole"></a>`TestLogToConsole` — [`L366`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L366)
- <a id="TestLogToConsole.test_allow_list_empty_prints_nothing"></a>`TestLogToConsole.test_allow_list_empty_prints_nothing` — [`L392`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L392)
- <a id="TestLogToConsole.test_allow_list_none_prints_all"></a>`TestLogToConsole.test_allow_list_none_prints_all` — [`L380`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L380)
- <a id="TestLogToConsole.test_allow_list_regex_search"></a>`TestLogToConsole.test_allow_list_regex_search` — [`L399`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L399)
- <a id="TestLogToConsole.test_alphabetical_when_no_allow_list"></a>`TestLogToConsole.test_alphabetical_when_no_allow_list` — [`L367`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L367)
- <a id="TestLogToConsole.test_console_prefix_renders_before_step"></a>`TestLogToConsole.test_console_prefix_renders_before_step` — [`L436`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L436)
- <a id="TestLogToConsole.test_no_match_no_print"></a>`TestLogToConsole.test_no_match_no_print` — [`L426`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L426)
- <a id="TestLogToConsole.test_pattern_order_preserved"></a>`TestLogToConsole.test_pattern_order_preserved` — [`L412`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L412)
- <a id="TestMaxMin"></a>`TestMaxMin` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L56)
- <a id="TestMaxMin.test_max_all_empty_returns_no_key"></a>`TestMaxMin.test_max_all_empty_returns_no_key` — [`L111`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L111)
- <a id="TestMaxMin.test_max_combine"></a>`TestMaxMin.test_max_combine` — [`L85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L85)
- <a id="TestMaxMin.test_max_empty_actor_first_does_not_erase"></a>`TestMaxMin.test_max_empty_actor_first_does_not_erase` — [`L91`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L91)
- <a id="TestMaxMin.test_max_empty_actor_last_does_not_erase"></a>`TestMaxMin.test_max_empty_actor_last_does_not_erase` — [`L102`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L102)
- <a id="TestMaxMin.test_max_empty_filtered"></a>`TestMaxMin.test_max_empty_filtered` — [`L69`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L69)
- <a id="TestMaxMin.test_max_from_list"></a>`TestMaxMin.test_max_from_list` — [`L57`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L57)
- <a id="TestMaxMin.test_max_single"></a>`TestMaxMin.test_max_single` — [`L81`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L81)
- <a id="TestMaxMin.test_min_empty_actor_first_does_not_erase"></a>`TestMaxMin.test_min_empty_actor_first_does_not_erase` — [`L120`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L120)
- <a id="TestMaxMin.test_min_empty_actor_last_does_not_erase"></a>`TestMaxMin.test_min_empty_actor_last_does_not_erase` — [`L129`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L129)
- <a id="TestMaxMin.test_min_empty_filtered"></a>`TestMaxMin.test_min_empty_filtered` — [`L75`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L75)
- <a id="TestMaxMin.test_min_from_list"></a>`TestMaxMin.test_min_from_list` — [`L63`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L63)
- <a id="TestMean"></a>`TestMean` — [`L27`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L27)
- <a id="TestMean.test_empty_list_filtered"></a>`TestMean.test_empty_list_filtered` — [`L45`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L45)
- <a id="TestMean.test_from_list_basic"></a>`TestMean.test_from_list_basic` — [`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L28)
- <a id="TestMean.test_single_value"></a>`TestMean.test_single_value` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L51)
- <a id="TestMean.test_weighted_combine"></a>`TestMean.test_weighted_combine` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L34)
- <a id="TestMetricsProcessorBuild"></a>`TestMetricsProcessorBuild` — [`L558`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L558)
- <a id="TestMetricsProcessorBuild.test_console_log_keys_round_trip"></a>`TestMetricsProcessorBuild.test_console_log_keys_round_trip` — [`L644`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L644)
- <a id="TestMetricsProcessorBuild.test_default_builds_no_backends"></a>`TestMetricsProcessorBuild.test_default_builds_no_backends` — [`L559`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L559)
- <a id="TestMetricsProcessorBuild.test_tensorboard_appends_backend"></a>`TestMetricsProcessorBuild.test_tensorboard_appends_backend` — [`L575`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L575)
- <a id="TestMetricsProcessorBuild.test_tensorboard_only_does_not_set_wandb_project_env"></a>`TestMetricsProcessorBuild.test_tensorboard_only_does_not_set_wandb_project_env` — [`L584`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L584)
- <a id="TestMetricsProcessorBuild.test_tensorboard_without_log_dir_raises"></a>`TestMetricsProcessorBuild.test_tensorboard_without_log_dir_raises` — [`L571`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L571)
- <a id="TestMetricsProcessorBuild.test_wandb_and_tensorboard_create_both"></a>`TestMetricsProcessorBuild.test_wandb_and_tensorboard_create_both` — [`L593`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L593)
- <a id="TestMetricsProcessorBuild.test_wandb_project_config_overrides_default"></a>`TestMetricsProcessorBuild.test_wandb_project_config_overrides_default` — [`L693`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L693)
- <a id="TestMetricsProcessorBuild.test_wandb_project_default_titan_rl"></a>`TestMetricsProcessorBuild.test_wandb_project_default_titan_rl` — [`L659`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L659)
- <a id="TestMetricsProcessorBuild.test_wandb_project_env_var_wins"></a>`TestMetricsProcessorBuild.test_wandb_project_env_var_wins` — [`L676`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L676)
- <a id="TestMetricsProcessorBuild.test_wandb_with_log_dir"></a>`TestMetricsProcessorBuild.test_wandb_with_log_dir` — [`L609`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L609)
- <a id="TestMetricsProcessorBuild.test_wandb_without_log_dir_raises"></a>`TestMetricsProcessorBuild.test_wandb_without_log_dir_raises` — [`L567`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L567)
- <a id="TestMetricsProcessorFanOut"></a>`TestMetricsProcessorFanOut` — [`L517`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L517)
- <a id="TestMetricsProcessorFanOut.test_close_isolates_failures"></a>`TestMetricsProcessorFanOut.test_close_isolates_failures` — [`L547`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L547)
- <a id="TestMetricsProcessorFanOut.test_log_aggregates_and_dispatches"></a>`TestMetricsProcessorFanOut.test_log_aggregates_and_dispatches` — [`L518`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L518)
- <a id="TestMetricsProcessorFanOut.test_log_isolates_failures"></a>`TestMetricsProcessorFanOut.test_log_isolates_failures` — [`L533`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L533)
- <a id="TestNoReduce"></a>`TestNoReduce` — [`L264`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L264)
- <a id="TestNoReduce.test_from_list_empty_raises"></a>`TestNoReduce.test_from_list_empty_raises` — [`L275`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L275)
- <a id="TestNoReduce.test_from_list_multiple_raises"></a>`TestNoReduce.test_from_list_multiple_raises` — [`L279`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L279)
- <a id="TestNoReduce.test_from_list_single"></a>`TestNoReduce.test_from_list_single` — [`L269`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L269)
- <a id="TestNoReduce.test_pass_through"></a>`TestNoReduce.test_pass_through` — [`L265`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L265)
- <a id="TestNoReduce.test_two_entries_same_key_raises"></a>`TestNoReduce.test_two_entries_same_key_raises` — [`L283`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L283)
- <a id="TestStd"></a>`TestStd` — [`L139`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L139)
- <a id="TestStd.test_combine_equals_concatenation"></a>`TestStd.test_combine_equals_concatenation` — [`L153`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L153)
- <a id="TestStd.test_empty_filtered"></a>`TestStd.test_empty_filtered` — [`L166`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L166)
- <a id="TestStd.test_from_list_matches_population_std"></a>`TestStd.test_from_list_matches_population_std` — [`L144`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L144)
- <a id="TestStd.test_single_value_zero"></a>`TestStd.test_single_value_zero` — [`L140`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L140)
- <a id="TestStdPreAggregated"></a>`TestStdPreAggregated` — [`L235`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L235)
- <a id="TestStdPreAggregated.test_combine_pre_aggregated_with_from_list"></a>`TestStdPreAggregated.test_combine_pre_aggregated_with_from_list` — [`L244`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L244)
- <a id="TestStdPreAggregated.test_partial_args_raise"></a>`TestStdPreAggregated.test_partial_args_raise` — [`L257`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L257)
- <a id="TestStdPreAggregated.test_pre_aggregated_equals_from_list"></a>`TestStdPreAggregated.test_pre_aggregated_equals_from_list` — [`L236`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L236)
- <a id="TestSum"></a>`TestSum` — [`L212`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L212)
- <a id="TestSum.test_combine"></a>`TestSum.test_combine` — [`L219`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L219)
- <a id="TestSum.test_does_not_collide_with_summary_stats_sum"></a>`TestSum.test_does_not_collide_with_summary_stats_sum` — [`L225`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L225)
- <a id="TestSum.test_from_list"></a>`TestSum.test_from_list` — [`L213`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L213)
- <a id="TestSummaryStats"></a>`TestSummaryStats` — [`L173`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L173)
- <a id="TestSummaryStats.test_combine_two_records"></a>`TestSummaryStats.test_combine_two_records` — [`L200`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L200)
- <a id="TestSummaryStats.test_empty_keeps_sum_zero"></a>`TestSummaryStats.test_empty_keeps_sum_zero` — [`L191`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L191)
- <a id="TestSummaryStats.test_five_keys_emitted"></a>`TestSummaryStats.test_five_keys_emitted` — [`L174`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L174)
- <a id="_RaisingBackend"></a>`_RaisingBackend` — [`L503`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L503)
- <a id="_RaisingBackend.__init__"></a>`_RaisingBackend.__init__` — [`L504`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L504)
- <a id="_RaisingBackend.close"></a>`_RaisingBackend.close` — [`L512`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L512)
- <a id="_RaisingBackend.close_calls"></a>`_RaisingBackend.close_calls` — [`L506`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L506)
- <a id="_RaisingBackend.log"></a>`_RaisingBackend.log` — [`L508`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L508)
- <a id="_RaisingBackend.log_calls"></a>`_RaisingBackend.log_calls` — [`L505`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L505)
- <a id="_RecordingBackend"></a>`_RecordingBackend` — [`L491`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L491)
- <a id="_RecordingBackend.__init__"></a>`_RecordingBackend.__init__` — [`L492`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L492)
- <a id="_RecordingBackend.calls"></a>`_RecordingBackend.calls` — [`L493`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L493)
- <a id="_RecordingBackend.close"></a>`_RecordingBackend.close` — [`L499`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L499)
- <a id="_RecordingBackend.closed"></a>`_RecordingBackend.closed` — [`L494`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L494)
- <a id="_RecordingBackend.log"></a>`_RecordingBackend.log` — [`L496`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L496)
- <a id="test_fmt_metric_value"></a>`test_fmt_metric_value` — [`L471`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L471)
- <a id="test_metric_backend_is_base_logger"></a>`test_metric_backend_is_base_logger` — [`L482`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_metrics.py#L482)
