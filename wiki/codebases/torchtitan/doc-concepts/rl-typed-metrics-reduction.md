---
title: TitanRL typed metrics and lazy per-step reduction
type: doc-concept
provenance: doc
source: torchtitan/experiments/rl/observability/metrics/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# TitanRL typed metrics and lazy per-step reduction

## Definition
RL actors, the controller and the loss emit **typed records** `Metric(key, value)` where the value type declares how it reduces (`Mean`, `Max`, `Min`, `Sum`, `Std`, `SummaryStats`, `NoReduce`). Nothing is reduced at emit time; the metrics processor reduces all records **once per step** inside `log(step, metrics)` and forwards a flat `dict[str, float]` to every backend, printing only an allow-listed subset to the console.

## In torchtitan (grounded)
- Record and value types: [`Metric`](../catalog/torchtitan/experiments/rl/observability/metrics/types.md#Metric), base [`MetricValue`](../catalog/torchtitan/experiments/rl/observability/metrics/types.md#MetricValue) (each subclass defines `reduce` and an `output_suffix`, plus a `from_list` constructor that makes one record from many observations), [`Mean`](../catalog/torchtitan/experiments/rl/observability/metrics/types.md#Mean), [`Max`](../catalog/torchtitan/experiments/rl/observability/metrics/types.md#Max), [`Min`](../catalog/torchtitan/experiments/rl/observability/metrics/types.md#Min), [`Sum`](../catalog/torchtitan/experiments/rl/observability/metrics/types.md#Sum), [`Std`](../catalog/torchtitan/experiments/rl/observability/metrics/types.md#Std), [`SummaryStats`](../catalog/torchtitan/experiments/rl/observability/metrics/types.md#SummaryStats), [`NoReduce`](../catalog/torchtitan/experiments/rl/observability/metrics/types.md#NoReduce).
- Processor: the RL [`MetricsProcessor`](../catalog/torchtitan/experiments/rl/observability/metrics/processor.md#MetricsProcessor) - [`MetricsProcessor.log`](../catalog/torchtitan/experiments/rl/observability/metrics/processor.md#MetricsProcessor.log) calls [`MetricsProcessor._aggregate_metrics`](../catalog/torchtitan/experiments/rl/observability/metrics/processor.md#MetricsProcessor._aggregate_metrics); console output via [`log_to_console`](../catalog/torchtitan/experiments/rl/observability/metrics/console.md#log_to_console).
- Config: [`console_log_keys_train`](../catalog/torchtitan/experiments/rl/observability/metrics/processor.md#MetricsProcessor.Config.console_log_keys_train), [`console_log_keys_validation`](../catalog/torchtitan/experiments/rl/observability/metrics/processor.md#MetricsProcessor.Config.console_log_keys_validation), [`enable_wandb`](../catalog/torchtitan/experiments/rl/observability/metrics/processor.md#MetricsProcessor.Config.enable_wandb), [`enable_tensorboard`](../catalog/torchtitan/experiments/rl/observability/metrics/processor.md#MetricsProcessor.Config.enable_tensorboard), [`wandb_project`](../catalog/torchtitan/experiments/rl/observability/metrics/processor.md#MetricsProcessor.Config.wandb_project) (default `titan_rl`, used as the `WANDB_PROJECT` default). Both backends require `log_dir` at build time.
- Producers include [`compute_rollout_metrics`](../catalog/torchtitan/experiments/rl/controller_metrics.md#compute_rollout_metrics), [`compute_policy_age_metrics`](../catalog/torchtitan/experiments/rl/controller_metrics.md#compute_policy_age_metrics) and [`compute_perf_ratio_metrics`](../catalog/torchtitan/experiments/rl/controller_metrics.md#compute_perf_ratio_metrics).

## Why it matters / when it applies
- **Naming contract:** a key reduced by `Mean` becomes `key/mean`, by `Max` `key/max`, etc.; several value types may share one key. `SummaryStats` expands to `key/_max`, `key/_mean`, `key/_min`, `key/_std`, `key/_sum` (leading underscore avoids collisions with bare `Mean`/`Max` records under the same key). `NoReduce` passes an already-reduced value through unchanged.
- Prefer `X.from_list(values)` over N separate records when observations are already in a list.
- W&B is on by default in reference recipes (`wandb login` first, or `--metrics.no-enable-wandb`); TensorBoard via `--metrics.enable-tensorboard`.
- This is distinct from the core training [`MetricsProcessor`](../catalog/torchtitan/components/metrics.md#MetricsProcessor) used by `Trainer` and the TPU lane.
- **TPU relevance.** None directly; RL-lane observability.

## Connections
- Code concepts: [observability](../concepts/observability.md), [rl-training](../concepts/rl-training.md), [training-components](../concepts/training-components.md)
- Module catalogs: [rl/observability/metrics/types](../catalog/torchtitan/experiments/rl/observability/metrics/types.md), [rl/observability/metrics/processor](../catalog/torchtitan/experiments/rl/observability/metrics/processor.md), [rl/controller_metrics](../catalog/torchtitan/experiments/rl/controller_metrics.md)
- Related doc-concepts: [vllm-otel-engine-metrics](vllm-otel-engine-metrics.md), [titanrl-architecture](titanrl-architecture.md)

## Source
Extracted from `torchtitan/experiments/rl/observability/metrics/README.md` (kept in place).
