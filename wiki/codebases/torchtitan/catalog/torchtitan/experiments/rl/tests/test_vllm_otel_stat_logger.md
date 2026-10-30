---
title: 'Module: torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.tests.test_vllm_otel_stat_logger`/
symbols:
  test_extract_step_stats_populated_converts_seconds_to_ms: test_extract_step_stats_populated_converts_seconds_to_ms().
  _context: _context().
  test_extract_step_stats_both_none: test_extract_step_stats_both_none().
  _vllm_config: _vllm_config().
  test_extra_resource_attributes_support_arrays_and_overrides: test_extra_resource_attributes_support_arrays_and_overrides().
  test_record_disables_on_instrument_failure: test_record_disables_on_instrument_failure().
  test_context_populates_resource_attributes: test_context_populates_resource_attributes().
  test_context_reads_distributed_env_tags: test_context_reads_distributed_env_tags().
  test_logger_does_not_gate_on_tp_rank: test_logger_does_not_gate_on_tp_rank().
  test_exporter_none_raises: test_exporter_none_raises().
  test_endpoint_without_exporter_raises: test_endpoint_without_exporter_raises().
  test_sdk_disabled_is_inert: test_sdk_disabled_is_inert().
  test_unsupported_exporter_raises: test_unsupported_exporter_raises().
  test_jsonl_requires_output_dir: test_jsonl_requires_output_dir().
  test_otlp_requires_endpoint: test_otlp_requires_endpoint().
  test_otlp_requires_http_protobuf: test_otlp_requires_http_protobuf().
  test_jsonl_export_is_asynchronous: test_jsonl_export_is_asynchronous().
  test_jsonl_export_writes_recorded_metrics: test_jsonl_export_writes_recorded_metrics().
  test_record_disables_on_extract_failure: test_record_disables_on_extract_failure().
  test_extract_step_stats_prefix_cache_none: test_extract_step_stats_prefix_cache_none().
  meter_providers: meter_providers().
  meter_providers.create_meter_provider: meter_providers().create_meter_provider().
  test_record_disables_on_instrument_failure.FailingCounter: test_record_disables_on_instrument_failure().FailingCounter#
  no_otel_env: no_otel_env().
  test_record_disables_on_instrument_failure.FailingCounter.add: test_record_disables_on_instrument_failure().FailingCounter#add().
---
# Module: [`torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py)

> **Collapsed catalog** (25 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="_context"></a>`_context` — [`L31`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L31)
- <a id="_vllm_config"></a>`_vllm_config` — [`L22`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L22)
- <a id="meter_providers"></a>`meter_providers` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L50)
- <a id="meter_providers.create_meter_provider"></a>`meter_providers.create_meter_provider` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L56)
- <a id="no_otel_env"></a>`no_otel_env` — [`L42`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L42)
- <a id="test_context_populates_resource_attributes"></a>`test_context_populates_resource_attributes` — [`L67`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L67)
- <a id="test_context_reads_distributed_env_tags"></a>`test_context_reads_distributed_env_tags` — [`L91`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L91)
- <a id="test_endpoint_without_exporter_raises"></a>`test_endpoint_without_exporter_raises` — [`L215`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L215)
- <a id="test_exporter_none_raises"></a>`test_exporter_none_raises` — [`L206`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L206)
- <a id="test_extra_resource_attributes_support_arrays_and_overrides"></a>`test_extra_resource_attributes_support_arrays_and_overrides` — [`L108`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L108)
- <a id="test_extract_step_stats_both_none"></a>`test_extract_step_stats_both_none` — [`L127`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L127)
- <a id="test_extract_step_stats_populated_converts_seconds_to_ms"></a>`test_extract_step_stats_populated_converts_seconds_to_ms` — [`L141`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L141)
- <a id="test_extract_step_stats_prefix_cache_none"></a>`test_extract_step_stats_prefix_cache_none` — [`L178`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L178)
- <a id="test_jsonl_export_is_asynchronous"></a>`test_jsonl_export_is_asynchronous` — [`L279`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L279)
- <a id="test_jsonl_export_writes_recorded_metrics"></a>`test_jsonl_export_writes_recorded_metrics` — [`L311`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L311)
- <a id="test_jsonl_requires_output_dir"></a>`test_jsonl_requires_output_dir` — [`L249`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L249)
- <a id="test_logger_does_not_gate_on_tp_rank"></a>`test_logger_does_not_gate_on_tp_rank` — [`L193`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L193)
- <a id="test_otlp_requires_endpoint"></a>`test_otlp_requires_endpoint` — [`L259`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L259)
- <a id="test_otlp_requires_http_protobuf"></a>`test_otlp_requires_http_protobuf` — [`L268`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L268)
- <a id="test_record_disables_on_extract_failure"></a>`test_record_disables_on_extract_failure` — [`L408`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L408)
- <a id="test_record_disables_on_instrument_failure"></a>`test_record_disables_on_instrument_failure` — [`L386`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L386)
- <a id="test_record_disables_on_instrument_failure.FailingCounter"></a>`test_record_disables_on_instrument_failure.FailingCounter` — [`L395`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L395)
- <a id="test_record_disables_on_instrument_failure.FailingCounter.add"></a>`test_record_disables_on_instrument_failure.FailingCounter.add` — [`L396`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L396)
- <a id="test_sdk_disabled_is_inert"></a>`test_sdk_disabled_is_inert` — [`L224`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L224)
- <a id="test_unsupported_exporter_raises"></a>`test_unsupported_exporter_raises` — [`L240`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py#L240)
