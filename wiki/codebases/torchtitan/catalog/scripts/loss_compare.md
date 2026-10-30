---
title: 'Module: scripts/loss_compare.py'
type: catalog
provenance: extracted
module: scripts/loss_compare.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `scripts.loss_compare`/
symbols:
  log_print: log_print().
  main: main().
  LOG_PREFIX: LOG_PREFIX.
  create_seed_checkpoint: create_seed_checkpoint().
  log_and_save: log_and_save().
  run_training: run_training().
  perform_loss_analysis: perform_loss_analysis().
  generate_summary_statistics: generate_summary_statistics().
  assert_metrics_equal: assert_metrics_equal().
  build_training_command: build_training_command().
  extract_metrics_from_tensorboard: extract_metrics_from_tensorboard().
  run_scenario: run_scenario().
  export_metrics_to_file: export_metrics_to_file().
  print_configuration: print_configuration().
  generate_step_comparison: generate_step_comparison().
  assert_losses_equal: assert_losses_equal().
  parse_arguments: parse_arguments().
  run_with_realtime_output: run_with_realtime_output().
  TB_TAGS: TB_TAGS.
  extract_scalar_from_tensorboard: extract_scalar_from_tensorboard().
  validate_arguments: validate_arguments().
  setup_output_directory: setup_output_directory().
  check_git_clean_state: check_git_clean_state().
  checkout_commit: checkout_commit().
  restore_original_commit: restore_original_commit().
  print_completion_summary: print_completion_summary().
  read_metrics_from_file: read_metrics_from_file().
  DEFAULT_METRICS: DEFAULT_METRICS.
  FIXED_OPTIONS: FIXED_OPTIONS.
  get_log_path: get_log_path().
  generate_summary_statistics.calculate_average: generate_summary_statistics().calculate_average().
  SEED_PARALLELISM_OPTIONS: SEED_PARALLELISM_OPTIONS.
  build_base_command: build_base_command().
  get_current_commit: get_current_commit().
  assert_losses_equal.LossEqualityTest: assert_losses_equal().LossEqualityTest#
  assert_losses_equal.LossEqualityTest.test_losses_equal: assert_losses_equal().LossEqualityTest#test_losses_equal().
---
# Module: [`scripts/loss_compare.py`](../../../../../raw/code/torchtitan/scripts/loss_compare.py)

## Classes
### <a id="assert_losses_equal.LossEqualityTest"></a>`assert_losses_equal.LossEqualityTest`  ·  implements/extends TestCase
- def: [`scripts/loss_compare.py:846`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L846)
- signature: `class LossEqualityTest(unittest.TestCase):`
- members:
  - <a id="assert_losses_equal.LossEqualityTest.test_losses_equal"></a>`test_losses_equal(self)` — [`L847`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L847)
- used by: [`assert_losses_equal`](loss_compare.md#assert_losses_equal)

## Functions
- <a id="assert_losses_equal"></a>`assert_losses_equal(baseline_losses: dict[int, float], test_losses: dict[int, float] | None = None, imported_losses: dict[int, float] | None = None, metric_name: str = "loss")` — [`L809`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L809) — Assert one metric is equal between baseline and test using unittest.
- <a id="assert_metrics_equal"></a>`assert_metrics_equal(baseline_metrics: dict[str, dict[int, float]], test_metrics: dict[str, dict[int, float]] | None = None, import_result: str | None = None)` — [`L780`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L780) — Assert every metric matches, against the test run and/or a golden file.
- <a id="build_base_command"></a>`build_base_command(module: str, config: str, job_dump_folder: str)` — [`L125`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L125) — Build the base command from module and config.
- <a id="build_training_command"></a>`build_training_command(module: str, config: str, options: str, steps: int, enable_seed_checkpoint: bool, job_dump_folder: str, tb_folder: str = "tb")` — [`L359`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L359) — Build the final training command with all options.
- <a id="generate_summary_statistics.calculate_average"></a>`calculate_average(losses: dict[int, float])` — [`L728`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L728) — Calculate average loss from losses dict.
- <a id="check_git_clean_state"></a>`check_git_clean_state()` — [`L450`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L450) — Check if git working directory is clean before switching commits.
- <a id="checkout_commit"></a>`checkout_commit(commit: str, commit_name: str)` — [`L488`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L488) — Checkout git commit.
- <a id="create_seed_checkpoint"></a>`create_seed_checkpoint(enable_seed_checkpoint: bool, module: str, config: str, output_folder: str | None, job_dump_folder: str)` — [`L535`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L535) — Create seed checkpoint.
- <a id="export_metrics_to_file"></a>`export_metrics_to_file(metrics: dict[str, dict[int, float]], export_path: str, config: str | None = None, ngpus: int | None = None)` — [`L646`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L646) — Write metrics to a golden result file and echo them to stdout.
- <a id="extract_metrics_from_tensorboard"></a>`extract_metrics_from_tensorboard(job_dump_folder: str, tb_folder: str, metric_names: Sequence[str])` — [`L163`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L163) — Extract full-precision values for each metric from TensorBoard events.
- <a id="extract_scalar_from_tensorboard"></a>`extract_scalar_from_tensorboard(job_dump_folder: str, tb_folder: str, scalar_tag: str)` — [`L186`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L186) — Extract one scalar tag from TensorBoard event files.
- <a id="generate_step_comparison"></a>`generate_step_comparison(baseline_losses: dict[int, float], test_losses: dict[int, float], stats_file: str | None)` — [`L688`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L688) — Generate step-by-step comparison.
- <a id="generate_summary_statistics"></a>`generate_summary_statistics(baseline_losses: dict[int, float], test_losses: dict[int, float], stats_file: str | None)` — [`L718`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L718) — Generate summary statistics.
- <a id="get_current_commit"></a>`get_current_commit()` — [`L497`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L497) — Get the current git commit hash or branch name.
- <a id="get_log_path"></a>`get_log_path(scenario: str, output_folder: str | None)` — [`L118`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L118) — Get log file path for a scenario.
- <a id="log_and_save"></a>`log_and_save(message: str, stats_file: str | None)` — [`L233`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L233) — Output message to both stdout and stats file if provided.
- <a id="log_print"></a>`log_print(message: str = "")` — [`L110`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L110) — Print message with LOG_PREFIX.
- <a id="main"></a>`main()` — [`L1189`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L1189) — Main function that orchestrates the entire comparison process.
- <a id="parse_arguments"></a>`parse_arguments()` — [`L977`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L977) — Parse command line arguments.
- <a id="perform_loss_analysis"></a>`perform_loss_analysis(baseline_losses: dict[int, float], test_losses: dict[int, float], stats_file: str | None)` — [`L749`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L749) — Perform loss comparison analysis.
- <a id="print_completion_summary"></a>`print_completion_summary(output_folder: str | None, enable_seed_checkpoint: bool, baseline_only_mode: bool = False)` — [`L933`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L933) — Print completion summary.
- <a id="print_configuration"></a>`print_configuration(baseline_commit: str, test_commit: str, baseline_module: str, baseline_config: str, baseline_options: str, test_module: str, test_config: str, test_options: str, steps: int, enable_seed_checkpoint: bool, job_dump_folder: str, baseline_only_mode: bool = False, baseline_tb_folder: str = "tb_baseline", test_tb_folder: str = "tb_test")` — [`L387`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L387) — Print configuration summary.
- <a id="read_metrics_from_file"></a>`read_metrics_from_file(result_file: str)` — [`L610`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L610) — Read a golden result file into metric name -> {step: value}.
- <a id="restore_original_commit"></a>`restore_original_commit(original_commit: str)` — [`L524`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L524) — Restore the original git commit/branch.
- <a id="run_scenario"></a>`run_scenario(scenario: str, commit: str, module: str, config: str, options: str, steps: int, enable_seed_checkpoint: bool, output_folder: str | None, job_dump_folder: str, ngpus: int, tb_folder: str = "tb")` — [`L1140`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L1140) — Run training for a specific scenario (baseline or test).
- <a id="run_training"></a>`run_training(scenario: str, module: str, config: str, options: str, steps: int, enable_seed_checkpoint: bool, output_folder: str | None, job_dump_folder: str, ngpus: int, tb_folder: str = "tb")` — [`L562`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L562) — Run training for a specific scenario. Returns the log file path.
- <a id="run_with_realtime_output"></a>`run_with_realtime_output(cmd: str, logfile: str, env: dict[str, Any])` — [`L132`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L132) — Run command with real-time output to both console and log file.
- <a id="setup_output_directory"></a>`setup_output_directory(output_folder: str | None)` — [`L337`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L337) — Setup output directory and return stats file path.
- <a id="validate_arguments"></a>`validate_arguments(baseline_commit: str, test_commit: str, baseline_module: str, baseline_config: str, baseline_options: str, test_module: str, test_config: str, test_options: str, steps: int, assert_equal: bool, export_result: str | None, import_result: str | None)` — [`L246`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L246) — Validate command line arguments.

## Module values
- <a id="DEFAULT_METRICS"></a>`DEFAULT_METRICS` — [`L89`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L89)
- <a id="FIXED_OPTIONS"></a>`FIXED_OPTIONS` — [`L92`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L92)
- <a id="LOG_PREFIX"></a>`LOG_PREFIX` — [`L82`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L82)
- <a id="SEED_PARALLELISM_OPTIONS"></a>`SEED_PARALLELISM_OPTIONS` — [`L93`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L93)
- <a id="TB_TAGS"></a>`TB_TAGS` — [`L85`](../../../../../raw/code/torchtitan/scripts/loss_compare.py#L85)

