---
title: vLLM engine metrics via OpenTelemetry (VllmOtelStatLogger)
type: doc-concept
provenance: doc
source: torchtitan/experiments/rl/observability/metrics/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# vLLM engine metrics via OpenTelemetry (VllmOtelStatLogger)

## Definition
Generator-side engine health (throughput, latency, KV-cache pressure, prefix-cache hits) is exported through a **separate OpenTelemetry pipeline**, not through the per-step RL metrics processor. A vLLM stat logger records engine stats into OTel instruments and exports them either to local JSONL files or to an OTLP collector.

## In torchtitan (grounded)
- [`VllmOtelStatLogger`](../catalog/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.md#VllmOtelStatLogger) ([`VllmOtelStatLogger.record`](../catalog/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.md#VllmOtelStatLogger.record), [`VllmOtelStatLogger.log`](../catalog/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.md#VllmOtelStatLogger.log)), configured by [`VllmOtelStatLogger.Config`](../catalog/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.md#VllmOtelStatLogger.Config).
- Enabled only when [`VLLMGenerator.Config.vllm_stat_logger`](../catalog/torchtitan/experiments/rl/actors/generator.md#VLLMGenerator.Config.vllm_stat_logger) holds that config; built per engine by [`VLLMGenerator.build_stat_logger`](../catalog/torchtitan/experiments/rl/actors/generator.md#VLLMGenerator.build_stat_logger). Only TP rank 0 in each DP replica creates a logger (all TP ranks see the same engine aggregates).

## Why it matters / when it applies
- **Explicit double gate:** the config must be set **and** `OTEL_METRICS_EXPORTER` must be `jsonl` or `otlp`, so inherited OTel env vars cannot turn it on by accident.
- Instruments: counters `vllm.generation_tokens`, `vllm.prompt_tokens`, `vllm.cached_prompt_tokens`, `vllm.preempted_requests`, `vllm.finished_requests`, `vllm.prefix_cache_queries`, `vllm.prefix_cache_hits` (cumulative - derive rates in the backend); histograms in ms `vllm.time_to_first_token`, `vllm.inter_token_latency`, `vllm.decode_time`, `vllm.queue_time`, `vllm.e2e_latency`; gauges `vllm.kv_cache_usage`, `vllm.num_running_requests`, `vllm.num_waiting_requests`.
- Prefix-cache hit rate = `rate(prefix_cache_hits) / rate(prefix_cache_queries)`; across generators, sum the rates before dividing; return nothing when the query rate is 0.
- Exporters: `jsonl` for local/small runs (`{dump_folder}/vllm_metrics/{generator_name}.rank{rank}.jsonl`, requires an output dir); `otlp` (HTTP/protobuf only; endpoint from `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` or `OTEL_EXPORTER_OTLP_ENDPOINT`) for production aggregation. Cadence: `VLLM_LOG_STATS_INTERVAL` seconds (default 10). Resource attributes include model name, host, rank, local rank, world size, DP/TP rank and generator name.
- These are the generator-side counterparts to the bitwise-parity doc's ITL/decode-time measurements ([rl-batch-invariance-bitwise-parity](rl-batch-invariance-bitwise-parity.md)) and the signal for generator-bound RL steps.
- **TPU relevance.** None at this commit (GPU vLLM only).

## Connections
- Code concepts: [observability](../concepts/observability.md), [rl-training](../concepts/rl-training.md)
- Module catalogs: [rl/observability/vllm_otel_stat_logger](../catalog/torchtitan/experiments/rl/observability/vllm_otel_stat_logger.md), [rl/actors/generator](../catalog/torchtitan/experiments/rl/actors/generator.md)
- Related doc-concepts: [rl-typed-metrics-reduction](rl-typed-metrics-reduction.md), [titanrl-architecture](titanrl-architecture.md)

## Source
Extracted from `torchtitan/experiments/rl/observability/metrics/README.md` (kept in place).
