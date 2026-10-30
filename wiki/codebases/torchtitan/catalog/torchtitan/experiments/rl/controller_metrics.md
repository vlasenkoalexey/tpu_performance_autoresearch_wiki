---
title: 'Module: torchtitan/experiments/rl/controller_metrics.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/controller_metrics.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.controller_metrics`/
symbols:
  compute_rollout_metrics: compute_rollout_metrics().
  compute_perf_ratio_metrics: compute_perf_ratio_metrics().
  compute_policy_age_metrics: compute_policy_age_metrics().
  MetricsTimer.flush: MetricsTimer#flush().
  compute_perf_ratio_metrics._add_metric: compute_perf_ratio_metrics()._add_metric().
  MetricsTimer.record: MetricsTimer#record().
  MetricsTimer: MetricsTimer#
  MetricsTimer.durations: MetricsTimer#durations.
  combine_microbatch_metrics: combine_microbatch_metrics().
  MetricsTimer.__init__: MetricsTimer#__init__().
---
# Module: [`torchtitan/experiments/rl/controller_metrics.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller_metrics.py)

## Classes
### <a id="MetricsTimer"></a>`MetricsTimer`
- def: [`torchtitan/experiments/rl/controller_metrics.py:20`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller_metrics.py#L20)
- doc: Times named code spans; flush() drains them into Mean metrics, then resets.
- signature: `class MetricsTimer:`
- members:
  - <a id="MetricsTimer.flush"></a>`flush(self)` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller_metrics.py#L47) — Return one Mean metric per recorded span, then reset so the timer can be reused.
  - <a id="MetricsTimer.record"></a>`record(self, key: str)` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller_metrics.py#L38)
  - <a id="MetricsTimer.durations"></a>`durations` — [`L35`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller_metrics.py#L35)
- protocol/private: <a id="MetricsTimer.__init__"></a>`__init__`[`L34`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller_metrics.py#L34)
- uses (calls/refs, reference-scoped): [`Metric`](observability/metrics/types.md#Metric), [`Mean`](observability/metrics/types.md#Mean), [`from_list`](observability/metrics/types.md#Mean.from_list)
- used by: [`_trainer_loop`](controller.md#Controller._trainer_loop)  (1 test-only)

## Functions
- <a id="compute_perf_ratio_metrics._add_metric"></a>`_add_metric(key: str, value: float)` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller_metrics.py#L113)
- <a id="combine_microbatch_metrics"></a>`combine_microbatch_metrics(microbatch_metrics: list[dict[str, float]])` — [`L56`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller_metrics.py#L56) — Combine per-microbatch loss metrics over the grad-accumulation: mean/frac keys are pre-normalized
- <a id="compute_perf_ratio_metrics"></a>`compute_perf_ratio_metrics(*, num_global_valid_tokens: int, time_metrics: list[m.Metric])` — [`L82`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller_metrics.py#L82) — Trainer-side timing ratios from the flushed step timers. A ratio is emitted only if every span
- <a id="compute_policy_age_metrics"></a>`compute_policy_age_metrics(*, trainer_policy_version: int, min_policy_versions: list[int], target_offpolicy_steps: int, max_offpolicy_steps: int)` — [`L167`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller_metrics.py#L167) — Age of each packed training sample at the moment the trainer consumes the batch.
- <a id="compute_rollout_metrics"></a>`compute_rollout_metrics(prefix: str, rollouts: list[Rollout])` — [`L216`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/controller_metrics.py#L216) — Build rollout-derived metrics: lengths, truncation, reward breakdown, and each turn's — documented in [rl-training](../../../../concepts/rl-training.md)

