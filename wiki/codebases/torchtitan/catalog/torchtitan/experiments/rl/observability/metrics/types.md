---
title: 'Module: torchtitan/experiments/rl/observability/metrics/types.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/observability/metrics/types.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.observability.metrics.types`/
symbols:
  Metric: Metric#
  NoReduce: NoReduce#
  Mean: Mean#
  Max: Max#
  Max.from_list: Max#from_list().
  SummaryStats.from_list: SummaryStats#from_list().
  Mean.from_list: Mean#from_list().
  Std: Std#
  MetricValue.from_list: MetricValue#from_list().
  MetricValue.reduce: MetricValue#reduce().
  Sum: Sum#
  SummaryStats.reduce: SummaryStats#reduce().
  SummaryStats: SummaryStats#
  Std.reduce: Std#reduce().
  Min: Min#
  Std.from_list: Std#from_list().
  MetricValue: MetricValue#
  Mean.reduce: Mean#reduce().
  Metric.value: Metric#value.
  Min.from_list: Min#from_list().
  Std.sum_squares: Std#sum_squares.
  Metric.key: Metric#key.
  Max.reduce: Max#reduce().
  Min.reduce: Min#reduce().
  Sum.reduce: Sum#reduce().
  NoReduce.reduce: NoReduce#reduce().
  NoReduce.from_list: NoReduce#from_list().
  SummaryStats.count: SummaryStats#count.
  Sum.from_list: Sum#from_list().
  SummaryStats.total: SummaryStats#total.
  SummaryStats.sum_squares: SummaryStats#sum_squares.
  SummaryStats.min_value: SummaryStats#min_value.
  SummaryStats.max_value: SummaryStats#max_value.
  Mean.value: Mean#value.
  Mean.output_suffix: Mean#output_suffix.
  Max.output_suffix: Max#output_suffix.
  Max.value: Max#value.
  Min.output_suffix: Min#output_suffix.
  Min.value: Min#value.
  Std.output_suffix: Std#output_suffix.
  Std.total: Std#total.
  Std.count: Std#count.
  Mean.count: Mean#count.
  Sum.output_suffix: Sum#output_suffix.
  Sum.value: Sum#value.
  NoReduce.output_suffix: NoReduce#output_suffix.
  NoReduce.value: NoReduce#value.
  __all__: __all__.
  MetricValue.output_suffix: MetricValue#output_suffix.
  MetricValue.__repr__: MetricValue#__repr__().
  Mean.__init__: Mean#__init__().
  Max.__init__: Max#__init__().
  Min.__init__: Min#__init__().
  Sum.__init__: Sum#__init__().
  Std.__init__: Std#__init__().
  SummaryStats.output_suffix: SummaryStats#output_suffix.
  SummaryStats.__init__: SummaryStats#__init__().
  NoReduce.__init__: NoReduce#__init__().
---
# Module: [`torchtitan/experiments/rl/observability/metrics/types.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py)

## Classes
### <a id="Max"></a>`Max`
- def: [`torchtitan/experiments/rl/observability/metrics/types.py:155`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L155)
- members:
  - <a id="Max.from_list"></a>`from_list(cls, values: Sequence[Any])` — [`L164`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L164)
  - <a id="Max.reduce"></a>`reduce(cls, metrics: Sequence[Max])` — [`L171`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L171)
  - <a id="Max.output_suffix"></a>`output_suffix` — [`L158`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L158)
  - <a id="Max.value"></a>`value` — [`L161`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L161)
- protocol/private: <a id="Max.__init__"></a>`__init__`[`L160`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L160)
- uses (calls/refs, reference-scoped): [`MetricValue`](types.md#MetricValue)
- used by: [`build_from_group`](../../components/training_sample_builder.md#TrainingSampleBuilder.build_from_group), [`compute_rollout_metrics`](../../controller_metrics.md#compute_rollout_metrics), [`_rank0_resolve_futures`](../../actors/generator.md#RequestDispatcher._rank0_resolve_futures), [`_prepare_generation_request_metrics`](../../actors/generator.md#_prepare_generation_request_metrics), [`from_list`](types.md#MetricValue.from_list), [`reduce`](types.md#MetricValue.reduce)  (11 test-only)

### <a id="Mean"></a>`Mean`
- def: [`torchtitan/experiments/rl/observability/metrics/types.py:108`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L108)
- members:
  - <a id="Mean.from_list"></a>`from_list(cls, values: Sequence[Any])` — [`L142`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L142)
  - <a id="Mean.reduce"></a>`reduce(cls, metrics: Sequence[Mean])` — [`L147`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L147)
  - <a id="Mean.count"></a>`count` — [`L139`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L139)
  - <a id="Mean.output_suffix"></a>`output_suffix` — [`L135`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L135)
  - <a id="Mean.value"></a>`value` — [`L138`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L138)
- protocol/private: <a id="Mean.__init__"></a>`__init__`[`L137`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L137)
- uses (calls/refs, reference-scoped): [`MetricValue`](types.md#MetricValue)
- used by: [`build_from_group`](../../components/training_sample_builder.md#TrainingSampleBuilder.build_from_group), [`compute_rollout_metrics`](../../controller_metrics.md#compute_rollout_metrics), [`_rank0_resolve_futures`](../../actors/generator.md#RequestDispatcher._rank0_resolve_futures), [`_prepare_generation_request_metrics`](../../actors/generator.md#_prepare_generation_request_metrics), [`compute_perf_ratio_metrics`](../../controller_metrics.md#compute_perf_ratio_metrics), [`from_list`](types.md#MetricValue.from_list), [`reduce`](types.md#MetricValue.reduce), [`compute_policy_age_metrics`](../../controller_metrics.md#compute_policy_age_metrics), [`flush`](../../controller_metrics.md#MetricsTimer.flush)  (11 test-only)

### <a id="Metric"></a>`Metric`
- def: [`torchtitan/experiments/rl/observability/metrics/types.py:89`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L89)
- members:
  - <a id="Metric.key"></a>`key` — [`L104`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L104)
  - <a id="Metric.value"></a>`value` — [`L105`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L105)
- uses (calls/refs, reference-scoped): [`MetricValue`](types.md#MetricValue)
- used by: [`_trainer_loop`](../../controller.md#Controller._trainer_loop), [`build_from_group`](../../components/training_sample_builder.md#TrainingSampleBuilder.build_from_group), [`_aggregate_metrics`](processor.md#MetricsProcessor._aggregate_metrics), [`_rollout_loop`](../../controller.md#Controller._rollout_loop), [`compute_rollout_metrics`](../../controller_metrics.md#compute_rollout_metrics), [`add_training_samples`](../../components/batcher.md#Batcher.add_training_samples), [`RolloutGroup`](../../rollout/types.md#RolloutGroup), [`_rank0_resolve_futures`](../../actors/generator.md#RequestDispatcher._rank0_resolve_futures), [`_prepare_generation_request_metrics`](../../actors/generator.md#_prepare_generation_request_metrics), [`_pack_one_training_batch`](../../components/batcher.md#Batcher._pack_one_training_batch), [`log`](processor.md#MetricsProcessor.log), [`_collect_validation_rollouts`](../../controller.md#Controller._collect_validation_rollouts), [`metrics`](../../components/work_buffer.md#RolloutGroupWorkBuffer.metrics), [`validate`](../../controller.md#Controller.validate), [`compute_perf_ratio_metrics`](../../controller_metrics.md#compute_perf_ratio_metrics), [`wait_prev_pull`](../../components/weight_sync.md#WeightSyncManager.wait_prev_pull), [`_packing_metrics`](../../components/batcher.md#Batcher._packing_metrics), [`_take_groups`](../../components/batcher.md#Batcher._take_groups), [`compute_policy_age_metrics`](../../controller_metrics.md#compute_policy_age_metrics), [`wait_prev_push`](../../components/weight_sync.md#WeightSyncManager.wait_prev_push), [`metrics`](../../types.md#TrainingSampleGroup.metrics), [`flush`](../../controller_metrics.md#MetricsTimer.flush), [`_add_metric`](../../controller_metrics.md#compute_perf_ratio_metrics._add_metric), [`metrics`](../../rollout/types.md#RolloutTurn.metrics), [`metrics`](../../types.md#Completion.metrics), [`metrics`](../../types.md#TrainingBatch.metrics)  (52 test-only)

### <a id="MetricValue"></a>`MetricValue`  ·  implements/extends Protocol
- def: [`torchtitan/experiments/rl/observability/metrics/types.py:30`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L30)
- doc: Value object that holds a metric partial value and defines how it
- signature: `class MetricValue(Protocol):`
- members:
  - <a id="MetricValue.__repr__"></a>`__repr__(self)` — [`L54`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L54) — Human-readable representation of print(self)
  - <a id="MetricValue.from_list"></a>`from_list(cls, values: Sequence[Any])` — [`L60`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L60) — Build one MetricValue from a list of raw observations.
  - <a id="MetricValue.reduce"></a>`reduce(cls, metrics: Sequence[object])` — [`L75`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L75) — Reduce same-typed MetricValues into output sub-keys.
  - <a id="MetricValue.output_suffix"></a>`output_suffix` — [`L50`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L50) — ---
- uses (calls/refs, reference-scoped): [`from_list`](types.md#Max.from_list), [`from_list`](types.md#SummaryStats.from_list), [`from_list`](types.md#Mean.from_list), [`reduce`](types.md#SummaryStats.reduce), [`reduce`](types.md#Std.reduce), [`from_list`](types.md#Std.from_list), [`reduce`](types.md#Mean.reduce), [`from_list`](types.md#Min.from_list), [`reduce`](types.md#Max.reduce), [`reduce`](types.md#Min.reduce), [`reduce`](types.md#NoReduce.reduce), [`reduce`](types.md#Sum.reduce), [`from_list`](types.md#NoReduce.from_list), [`from_list`](types.md#Sum.from_list)
- used by: [`_aggregate_metrics`](processor.md#MetricsProcessor._aggregate_metrics), [`NoReduce`](types.md#NoReduce), [`Mean`](types.md#Mean), [`Max`](types.md#Max), [`Std`](types.md#Std), [`Sum`](types.md#Sum), [`SummaryStats`](types.md#SummaryStats), [`Min`](types.md#Min), [`value`](types.md#Metric.value)

### <a id="Min"></a>`Min`
- def: [`torchtitan/experiments/rl/observability/metrics/types.py:180`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L180)
- members:
  - <a id="Min.from_list"></a>`from_list(cls, values: Sequence[Any])` — [`L189`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L189)
  - <a id="Min.reduce"></a>`reduce(cls, metrics: Sequence[Min])` — [`L196`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L196)
  - <a id="Min.output_suffix"></a>`output_suffix` — [`L183`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L183)
  - <a id="Min.value"></a>`value` — [`L186`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L186)
- protocol/private: <a id="Min.__init__"></a>`__init__`[`L185`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L185)
- uses (calls/refs, reference-scoped): [`MetricValue`](types.md#MetricValue)
- used by: [`build_from_group`](../../components/training_sample_builder.md#TrainingSampleBuilder.build_from_group), [`from_list`](types.md#MetricValue.from_list), [`reduce`](types.md#MetricValue.reduce)  (4 test-only)

### <a id="NoReduce"></a>`NoReduce`
- def: [`torchtitan/experiments/rl/observability/metrics/types.py:357`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L357)
- members:
  - <a id="NoReduce.from_list"></a>`from_list(cls, values: Sequence[Any])` — [`L373`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L373)
  - <a id="NoReduce.reduce"></a>`reduce(cls, metrics: Sequence[NoReduce])` — [`L381`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L381)
  - <a id="NoReduce.output_suffix"></a>`output_suffix` — [`L367`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L367)
  - <a id="NoReduce.value"></a>`value` — [`L370`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L370)
- protocol/private: <a id="NoReduce.__init__"></a>`__init__`[`L369`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L369)
- uses (calls/refs, reference-scoped): [`MetricValue`](types.md#MetricValue)
- used by: [`_trainer_loop`](../../controller.md#Controller._trainer_loop), [`_pack_one_training_batch`](../../components/batcher.md#Batcher._pack_one_training_batch), [`metrics`](../../components/work_buffer.md#RolloutGroupWorkBuffer.metrics), [`validate`](../../controller.md#Controller.validate), [`from_list`](types.md#MetricValue.from_list), [`reduce`](types.md#MetricValue.reduce), [`wait_prev_pull`](../../components/weight_sync.md#WeightSyncManager.wait_prev_pull), [`_packing_metrics`](../../components/batcher.md#Batcher._packing_metrics), [`compute_policy_age_metrics`](../../controller_metrics.md#compute_policy_age_metrics), [`wait_prev_push`](../../components/weight_sync.md#WeightSyncManager.wait_prev_push), [`_add_metric`](../../controller_metrics.md#compute_perf_ratio_metrics._add_metric)  (14 test-only)

### <a id="Std"></a>`Std`
- def: [`torchtitan/experiments/rl/observability/metrics/types.py:220`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L220)
- members:
  - <a id="Std.from_list"></a>`from_list(cls, values: Sequence[Any])` — [`L261`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L261)
  - <a id="Std.reduce"></a>`reduce(cls, metrics: Sequence[Std])` — [`L270`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L270)
  - <a id="Std.count"></a>`count` — [`L253`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L253)
  - <a id="Std.output_suffix"></a>`output_suffix` — [`L237`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L237)
  - <a id="Std.sum_squares"></a>`sum_squares` — [`L254`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L254)
  - <a id="Std.total"></a>`total` — [`L252`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L252)
- protocol/private: <a id="Std.__init__"></a>`__init__`[`L239`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L239)
- uses (calls/refs, reference-scoped): [`MetricValue`](types.md#MetricValue)
- used by: [`compute_rollout_metrics`](../../controller_metrics.md#compute_rollout_metrics), [`from_list`](types.md#MetricValue.from_list), [`reduce`](types.md#MetricValue.reduce)  (7 test-only)

### <a id="Sum"></a>`Sum`
- def: [`torchtitan/experiments/rl/observability/metrics/types.py:203`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L203)
- members:
  - <a id="Sum.from_list"></a>`from_list(cls, values: Sequence[Any])` — [`L212`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L212)
  - <a id="Sum.reduce"></a>`reduce(cls, metrics: Sequence[Sum])` — [`L216`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L216)
  - <a id="Sum.output_suffix"></a>`output_suffix` — [`L206`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L206)
  - <a id="Sum.value"></a>`value` — [`L209`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L209)
- protocol/private: <a id="Sum.__init__"></a>`__init__`[`L208`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L208)
- uses (calls/refs, reference-scoped): [`MetricValue`](types.md#MetricValue)
- used by: [`build_from_group`](../../components/training_sample_builder.md#TrainingSampleBuilder.build_from_group), [`_rollout_loop`](../../controller.md#Controller._rollout_loop), [`add_training_samples`](../../components/batcher.md#Batcher.add_training_samples), [`_collect_validation_rollouts`](../../controller.md#Controller._collect_validation_rollouts), [`from_list`](types.md#MetricValue.from_list), [`reduce`](types.md#MetricValue.reduce)  (3 test-only)

### <a id="SummaryStats"></a>`SummaryStats`
- def: [`torchtitan/experiments/rl/observability/metrics/types.py:282`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L282)
- members:
  - <a id="SummaryStats.from_list"></a>`from_list(cls, values: Sequence[Any])` — [`L302`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L302)
  - <a id="SummaryStats.reduce"></a>`reduce(cls, metrics: Sequence[SummaryStats])` — [`L322`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L322)
  - <a id="SummaryStats.count"></a>`count` — [`L296`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L296)
  - <a id="SummaryStats.max_value"></a>`max_value` — [`L299`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L299)
  - <a id="SummaryStats.min_value"></a>`min_value` — [`L298`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L298)
  - <a id="SummaryStats.output_suffix"></a>`output_suffix` — [`L291`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L291)
  - <a id="SummaryStats.sum_squares"></a>`sum_squares` — [`L297`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L297)
  - <a id="SummaryStats.total"></a>`total` — [`L295`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L295)
- protocol/private: <a id="SummaryStats.__init__"></a>`__init__`[`L293`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L293)
- uses (calls/refs, reference-scoped): [`MetricValue`](types.md#MetricValue)
- used by: [`build_from_group`](../../components/training_sample_builder.md#TrainingSampleBuilder.build_from_group), [`compute_rollout_metrics`](../../controller_metrics.md#compute_rollout_metrics), [`from_list`](types.md#MetricValue.from_list), [`reduce`](types.md#MetricValue.reduce)  (5 test-only)

## Module values
- <a id="__all__"></a>`__all__` — [`L17`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/types.py#L17)

