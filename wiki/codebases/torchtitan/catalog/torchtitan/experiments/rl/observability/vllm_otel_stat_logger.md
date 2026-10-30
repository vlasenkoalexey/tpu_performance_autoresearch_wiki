---
title: 'Module: torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.observability.vllm_otel_stat_logger`/
symbols:
  VllmOtelStatLogger.record: VllmOtelStatLogger#record().
  _extract_step_stats: _extract_step_stats().
  VllmOtelStatLogger._num_waiting_last: VllmOtelStatLogger#_num_waiting_last.
  VllmOtelStatLogger.Config: VllmOtelStatLogger#Config#
  VllmOtelStatLogger: VllmOtelStatLogger#
  VllmOtelStatLogger._build_resource_attributes: VllmOtelStatLogger#_build_resource_attributes().
  _StepStats.finished: _StepStats#finished.
  VllmOtelStatLogger._create_gauges: VllmOtelStatLogger#_create_gauges().
  StatLoggerContext: StatLoggerContext#
  _StepStats.kv_cache_usage: _StepStats#kv_cache_usage.
  _StepStats.prefix_queries: _StepStats#prefix_queries.
  _StepStats.prefix_hits: _StepStats#prefix_hits.
  StatLoggerContext.output_dir: StatLoggerContext#output_dir.
  _StepStats.num_running_reqs: _StepStats#num_running_reqs.
  _StepStats.num_waiting_reqs: _StepStats#num_waiting_reqs.
  VllmOtelStatLogger.__init__: VllmOtelStatLogger#__init__().
  VllmOtelStatLogger._enabled: VllmOtelStatLogger#_enabled.
  VllmOtelStatLogger.log_engine_initialized: VllmOtelStatLogger#log_engine_initialized().
  StatLoggerContext.rank: StatLoggerContext#rank.
  StatLoggerContext.generator_name: StatLoggerContext#generator_name.
  _StepStats.num_generation_tokens: _StepStats#num_generation_tokens.
  _StepStats.ttft_ms: _StepStats#ttft_ms.
  _StepStats.itl_ms: _StepStats#itl_ms.
  logger.logger: logger.logger.
  VllmOtelStatLogger.kv_cb: VllmOtelStatLogger#kv_cb().
  VllmOtelStatLogger.running_cb: VllmOtelStatLogger#running_cb().
  VllmOtelStatLogger.waiting_cb: VllmOtelStatLogger#waiting_cb().
  StatLoggerContext.tp_rank: StatLoggerContext#tp_rank.
  StatLoggerContext.dp_rank: StatLoggerContext#dp_rank.
  _FinishedRequestStats: _FinishedRequestStats#
  _FinishedRequestStats.decode_time_ms: _FinishedRequestStats#decode_time_ms.
  _FinishedRequestStats.queue_time_ms: _FinishedRequestStats#queue_time_ms.
  _FinishedRequestStats.e2e_latency_ms: _FinishedRequestStats#e2e_latency_ms.
  _StepStats.num_prompt_tokens: _StepStats#num_prompt_tokens.
  _StepStats.num_cached_prompt_tokens: _StepStats#num_cached_prompt_tokens.
  _StepStats.num_preempted_reqs: _StepStats#num_preempted_reqs.
  _StepStats: _StepStats#
  VllmOtelStatLogger.Config.extra_resource_attributes: VllmOtelStatLogger#Config#extra_resource_attributes.
  VllmOtelStatLogger._kv_cache_usage_last: VllmOtelStatLogger#_kv_cache_usage_last.
  VllmOtelStatLogger._num_running_last: VllmOtelStatLogger#_num_running_last.
  _compact_json: _compact_json().
  VllmOtelStatLogger._config: VllmOtelStatLogger#_config.
  VllmOtelStatLogger._create_counters: VllmOtelStatLogger#_create_counters().
  VllmOtelStatLogger._c_gen_tokens: VllmOtelStatLogger#_c_gen_tokens.
  VllmOtelStatLogger._c_prompt_tokens: VllmOtelStatLogger#_c_prompt_tokens.
  VllmOtelStatLogger._c_cached_prompt_tokens: VllmOtelStatLogger#_c_cached_prompt_tokens.
  VllmOtelStatLogger._c_preempted: VllmOtelStatLogger#_c_preempted.
  VllmOtelStatLogger._c_finished: VllmOtelStatLogger#_c_finished.
  VllmOtelStatLogger._c_prefix_queries: VllmOtelStatLogger#_c_prefix_queries.
  VllmOtelStatLogger._c_prefix_hits: VllmOtelStatLogger#_c_prefix_hits.
  VllmOtelStatLogger._create_histograms: VllmOtelStatLogger#_create_histograms().
  VllmOtelStatLogger._h_ttft: VllmOtelStatLogger#_h_ttft.
  VllmOtelStatLogger._h_itl: VllmOtelStatLogger#_h_itl.
  VllmOtelStatLogger._h_decode: VllmOtelStatLogger#_h_decode.
  VllmOtelStatLogger._h_queue: VllmOtelStatLogger#_h_queue.
  VllmOtelStatLogger._h_e2e: VllmOtelStatLogger#_h_e2e.
  VllmOtelStatLogger.log: VllmOtelStatLogger#log().
---
# Module: [`torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py)

## Classes
### <a id="StatLoggerContext"></a>`StatLoggerContext`
- def: [`torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py:47`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L47)
- doc: Per-engine context the generator injects into its stat loggers.
- signature: `class StatLoggerContext:`
- members:
  - <a id="StatLoggerContext.dp_rank"></a>`dp_rank` — [`L52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L52)
  - <a id="StatLoggerContext.generator_name"></a>`generator_name` — [`L53`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L53)
  - <a id="StatLoggerContext.output_dir"></a>`output_dir` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L54)
  - <a id="StatLoggerContext.rank"></a>`rank` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L50)
  - <a id="StatLoggerContext.tp_rank"></a>`tp_rank` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L51)
- used by: [`model_path`](../actors/generator.md#VLLMGenerator.model_path), [`_num_waiting_last`](vllm_otel_stat_logger.md#VllmOtelStatLogger._num_waiting_last), [`_build_resource_attributes`](vllm_otel_stat_logger.md#VllmOtelStatLogger._build_resource_attributes), [`__init__`](vllm_otel_stat_logger.md#VllmOtelStatLogger.__init__)  (1 test-only)

### <a id="VllmOtelStatLogger"></a>`VllmOtelStatLogger`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py:148`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L148)
- doc: Per-engine vLLM stat logger that exports OpenTelemetry metrics.
- signature: `class VllmOtelStatLogger(Configurable, StatLoggerBase):`
- members:
  - <a id="VllmOtelStatLogger._build_resource_attributes"></a>`_build_resource_attributes(self, vllm_config: VllmConfig, context: StatLoggerContext)` — [`L267`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L267) — Build resource attributes.
  - <a id="VllmOtelStatLogger._create_counters"></a>`_create_counters(self, meter: Meter)` — [`L284`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L284) — Monotonic counters; the backend derives throughput/rates via rate().
  - <a id="VllmOtelStatLogger._create_gauges"></a>`_create_gauges(self, meter: Meter, observation_cls: type[Observation])` — [`L311`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L311) — Observable gauges report the last-seen scheduler state at collection.
  - <a id="VllmOtelStatLogger._create_histograms"></a>`_create_histograms(self, meter: Meter)` — [`L303`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L303) — Latency histograms; the backend computes percentiles (p50/p95/p99).
  - <a id="VllmOtelStatLogger.kv_cb"></a>`kv_cb(_options: CallbackOptions)` — [`L314`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L314)
  - <a id="VllmOtelStatLogger.log"></a>`log(self)` — [`L377`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L377) — Leave vLLM's synchronous logging hook empty.
  - <a id="VllmOtelStatLogger.log_engine_initialized"></a>`log_engine_initialized(self)` — [`L385`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L385) — Log the active export cadence after vLLM initializes the engine.
  - <a id="VllmOtelStatLogger.record"></a>`record(self, scheduler_stats: SchedulerStats | None, iteration_stats: IterationStats | None, mm_cache_stats: MultiModalCacheStats | None = None, engine_idx: int = 0)` — [`L331`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L331) — Record one vLLM engine step without propagating telemetry errors.
  - <a id="VllmOtelStatLogger.running_cb"></a>`running_cb(_options: CallbackOptions)` — [`L317`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L317)
  - <a id="VllmOtelStatLogger.waiting_cb"></a>`waiting_cb(_options: CallbackOptions)` — [`L320`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L320)
- protocol/private: <a id="VllmOtelStatLogger.__init__"></a>`__init__`[`L162`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L162), <a id="VllmOtelStatLogger._c_cached_prompt_tokens"></a>`_c_cached_prompt_tokens`[`L290`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L290), <a id="VllmOtelStatLogger._c_finished"></a>`_c_finished`[`L296`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L296), <a id="VllmOtelStatLogger._c_gen_tokens"></a>`_c_gen_tokens`[`L286`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L286), <a id="VllmOtelStatLogger._c_preempted"></a>`_c_preempted`[`L293`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L293), <a id="VllmOtelStatLogger._c_prefix_hits"></a>`_c_prefix_hits`[`L301`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L301), <a id="VllmOtelStatLogger._c_prefix_queries"></a>`_c_prefix_queries`[`L300`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L300), <a id="VllmOtelStatLogger._c_prompt_tokens"></a>`_c_prompt_tokens`[`L289`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L289), <a id="VllmOtelStatLogger._config"></a>`_config`[`L170`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L170), <a id="VllmOtelStatLogger._enabled"></a>`_enabled`[`L171`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L171), <a id="VllmOtelStatLogger._h_decode"></a>`_h_decode`[`L307`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L307), <a id="VllmOtelStatLogger._h_e2e"></a>`_h_e2e`[`L309`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L309), <a id="VllmOtelStatLogger._h_itl"></a>`_h_itl`[`L306`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L306), <a id="VllmOtelStatLogger._h_queue"></a>`_h_queue`[`L308`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L308), <a id="VllmOtelStatLogger._h_ttft"></a>`_h_ttft`[`L305`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L305), <a id="VllmOtelStatLogger._kv_cache_usage_last"></a>`_kv_cache_usage_last`[`L173`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L173), <a id="VllmOtelStatLogger._num_running_last"></a>`_num_running_last`[`L174`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L174), <a id="VllmOtelStatLogger._num_waiting_last"></a>`_num_waiting_last`[`L175`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L175)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`_extract_step_stats`](vllm_otel_stat_logger.md#_extract_step_stats), [`Config`](vllm_otel_stat_logger.md#VllmOtelStatLogger.Config), [`finished`](vllm_otel_stat_logger.md#_StepStats.finished), [`StatLoggerContext`](vllm_otel_stat_logger.md#StatLoggerContext), [`kv_cache_usage`](vllm_otel_stat_logger.md#_StepStats.kv_cache_usage), [`prefix_hits`](vllm_otel_stat_logger.md#_StepStats.prefix_hits), [`prefix_queries`](vllm_otel_stat_logger.md#_StepStats.prefix_queries), [`num_running_reqs`](vllm_otel_stat_logger.md#_StepStats.num_running_reqs), [`num_waiting_reqs`](vllm_otel_stat_logger.md#_StepStats.num_waiting_reqs), [`output_dir`](vllm_otel_stat_logger.md#StatLoggerContext.output_dir), [`generator_name`](vllm_otel_stat_logger.md#StatLoggerContext.generator_name), [`itl_ms`](vllm_otel_stat_logger.md#_StepStats.itl_ms), [`logger`](vllm_otel_stat_logger.md#logger.logger), [`num_generation_tokens`](vllm_otel_stat_logger.md#_StepStats.num_generation_tokens), [`rank`](vllm_otel_stat_logger.md#StatLoggerContext.rank), [`ttft_ms`](vllm_otel_stat_logger.md#_StepStats.ttft_ms), [`decode_time_ms`](vllm_otel_stat_logger.md#_FinishedRequestStats.decode_time_ms), [`dp_rank`](vllm_otel_stat_logger.md#StatLoggerContext.dp_rank), [`e2e_latency_ms`](vllm_otel_stat_logger.md#_FinishedRequestStats.e2e_latency_ms), [`num_cached_prompt_tokens`](vllm_otel_stat_logger.md#_StepStats.num_cached_prompt_tokens), [`num_preempted_reqs`](vllm_otel_stat_logger.md#_StepStats.num_preempted_reqs), [`num_prompt_tokens`](vllm_otel_stat_logger.md#_StepStats.num_prompt_tokens), [`queue_time_ms`](vllm_otel_stat_logger.md#_FinishedRequestStats.queue_time_ms), [`tp_rank`](vllm_otel_stat_logger.md#StatLoggerContext.tp_rank), [`extra_resource_attributes`](vllm_otel_stat_logger.md#VllmOtelStatLogger.Config.extra_resource_attributes), [`_compact_json`](vllm_otel_stat_logger.md#_compact_json)
- used by: [`Configurable`](../../../config/configurable.md#Configurable), [`vllm_stat_logger`](../actors/generator.md#VLLMGenerator.Config.vllm_stat_logger)  (15 test-only)

### <a id="VllmOtelStatLogger.Config"></a>`VllmOtelStatLogger.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py:155`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L155)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="VllmOtelStatLogger.Config.extra_resource_attributes"></a>`extra_resource_attributes` — [`L156`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L156) — ---
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Config`](../../../config/configurable.md#Configurable.Config)
- used by: [`_build_resource_attributes`](vllm_otel_stat_logger.md#VllmOtelStatLogger._build_resource_attributes), [`vllm_stat_logger`](../actors/generator.md#VLLMGenerator.Config.vllm_stat_logger), [`__init__`](vllm_otel_stat_logger.md#VllmOtelStatLogger.__init__)  (15 test-only)

### <a id="_FinishedRequestStats"></a>`_FinishedRequestStats`
- def: [`torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py:58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L58)
- doc: Per-finished-request latencies for one engine step (milliseconds).
- signature: `class _FinishedRequestStats:`
- members:
  - <a id="_FinishedRequestStats.decode_time_ms"></a>`decode_time_ms` — [`L61`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L61)
  - <a id="_FinishedRequestStats.e2e_latency_ms"></a>`e2e_latency_ms` — [`L63`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L63)
  - <a id="_FinishedRequestStats.queue_time_ms"></a>`queue_time_ms` — [`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L62)
- used by: [`record`](vllm_otel_stat_logger.md#VllmOtelStatLogger.record), [`_extract_step_stats`](vllm_otel_stat_logger.md#_extract_step_stats), [`finished`](vllm_otel_stat_logger.md#_StepStats.finished)  (1 test-only)

### <a id="_StepStats"></a>`_StepStats`
- def: [`torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py:67`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L67)
- doc: Snapshot of one vLLM engine step.
- signature: `class _StepStats:`
- members:
  - <a id="_StepStats.finished"></a>`finished` — [`L81`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L81)
  - <a id="_StepStats.itl_ms"></a>`itl_ms` — [`L80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L80)
  - <a id="_StepStats.kv_cache_usage"></a>`kv_cache_usage` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L70)
  - <a id="_StepStats.num_cached_prompt_tokens"></a>`num_cached_prompt_tokens` — [`L77`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L77)
  - <a id="_StepStats.num_generation_tokens"></a>`num_generation_tokens` — [`L75`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L75)
  - <a id="_StepStats.num_preempted_reqs"></a>`num_preempted_reqs` — [`L78`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L78)
  - <a id="_StepStats.num_prompt_tokens"></a>`num_prompt_tokens` — [`L76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L76)
  - <a id="_StepStats.num_running_reqs"></a>`num_running_reqs` — [`L71`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L71)
  - <a id="_StepStats.num_waiting_reqs"></a>`num_waiting_reqs` — [`L72`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L72)
  - <a id="_StepStats.prefix_hits"></a>`prefix_hits` — [`L74`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L74)
  - <a id="_StepStats.prefix_queries"></a>`prefix_queries` — [`L73`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L73)
  - <a id="_StepStats.ttft_ms"></a>`ttft_ms` — [`L79`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L79)
- uses (calls/refs, reference-scoped): [`_FinishedRequestStats`](vllm_otel_stat_logger.md#_FinishedRequestStats)
- used by: [`record`](vllm_otel_stat_logger.md#VllmOtelStatLogger.record), [`_extract_step_stats`](vllm_otel_stat_logger.md#_extract_step_stats)  (3 test-only)

## Functions
- <a id="_compact_json"></a>`_compact_json(metrics_data)` — [`L142`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L142)
- <a id="_extract_step_stats"></a>`_extract_step_stats(scheduler_stats: SchedulerStats | None, iteration_stats: IterationStats | None)` — [`L84`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L84) — Read one engine step's vLLM stats.

## Module values
- <a id="logger.logger"></a>`logger` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py#L43)

