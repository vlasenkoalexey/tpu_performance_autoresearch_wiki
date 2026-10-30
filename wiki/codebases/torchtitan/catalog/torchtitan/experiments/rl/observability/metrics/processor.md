---
title: 'Module: torchtitan/experiments/rl/observability/metrics/processor.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/observability/metrics/processor.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.observability.metrics.processor`/
symbols:
  MetricsProcessor: MetricsProcessor#
  MetricsProcessor._aggregate_metrics: MetricsProcessor#_aggregate_metrics().
  MetricsProcessor.Config: MetricsProcessor#Config#
  MetricsProcessor.log: MetricsProcessor#log().
  MetricsProcessor.Config.enable_wandb: MetricsProcessor#Config#enable_wandb.
  MetricsProcessor._backends: MetricsProcessor#_backends.
  MetricsProcessor.close: MetricsProcessor#close().
  MetricsProcessor.Config.enable_tensorboard: MetricsProcessor#Config#enable_tensorboard.
  MetricsProcessor.Config.console_log_keys_train: MetricsProcessor#Config#console_log_keys_train.
  MetricsProcessor.Config.console_log_keys_validation: MetricsProcessor#Config#console_log_keys_validation.
  MetricsProcessor.__init__: MetricsProcessor#__init__().
  MetricsProcessor.Config.wandb_project: MetricsProcessor#Config#wandb_project.
  MetricsProcessor.config: MetricsProcessor#config.
  __all__: __all__.
---
# Module: [`torchtitan/experiments/rl/observability/metrics/processor.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/processor.py)

## Classes
### <a id="MetricsProcessor"></a>`MetricsProcessor`
- def: [`torchtitan/experiments/rl/observability/metrics/processor.py:36`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/processor.py#L36)
- members:
  - <a id="MetricsProcessor._aggregate_metrics"></a>`_aggregate_metrics(cls, metrics: Iterable[Metric])` — [`L121`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/processor.py#L121) — Reduces a list of `Metric` records into a single float per metric key.
  - <a id="MetricsProcessor.close"></a>`close(self)` — [`L219`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/processor.py#L219)
  - <a id="MetricsProcessor.log"></a>`log(self, step: int, metrics: Iterable[Metric], *, is_validation: bool = False)` — [`L165`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/processor.py#L165) — Reduce metrics, prints to console, dispatch to backends.
  - <a id="MetricsProcessor.config"></a>`config` — [`L108`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/processor.py#L108)
- protocol/private: <a id="MetricsProcessor.__init__"></a>`__init__`[`L101`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/processor.py#L101), <a id="MetricsProcessor._backends"></a>`_backends`[`L109`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/processor.py#L109)
- uses (calls/refs, reference-scoped): [`logger`](../../../../tools/logging.md#logger), [`Configurable`](../../../../config/configurable.md#Configurable), [`Metric`](types.md#Metric), [`Config`](processor.md#MetricsProcessor.Config), [`log_to_console`](console.md#log_to_console), [`BaseLogger`](../../../../components/metrics.md#BaseLogger), [`enable_wandb`](processor.md#MetricsProcessor.Config.enable_wandb), [`log`](../../../../components/metrics.md#BaseLogger.log), [`close`](../../../../components/metrics.md#BaseLogger.close), [`MetricValue`](types.md#MetricValue), [`value`](types.md#Metric.value), [`warn_once`](../../../../tools/logging.md#warn_once), [`key`](types.md#Metric.key), [`TensorBoardLogger`](../../../../components/metrics.md#TensorBoardLogger), [`WandBLogger`](../../../../components/metrics.md#WandBLogger), [`enable_tensorboard`](processor.md#MetricsProcessor.Config.enable_tensorboard), [`console_log_keys_train`](processor.md#MetricsProcessor.Config.console_log_keys_train), [`console_log_keys_validation`](processor.md#MetricsProcessor.Config.console_log_keys_validation), [`wandb_project`](processor.md#MetricsProcessor.Config.wandb_project)
- used by: [`_trainer_loop`](../../controller.md#Controller._trainer_loop), [`close`](../../controller.md#Controller.close), [`metrics`](../../controller.md#Controller.Config.metrics), [`metrics_processor`](../../controller.md#Controller.metrics_processor), [`_validate_and_log`](../../controller.md#Controller._validate_and_log)  (77 test-only)

### <a id="MetricsProcessor.Config"></a>`MetricsProcessor.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/observability/metrics/processor.py:51`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/processor.py#L51)
- doc: Metrics processor configuration.
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="MetricsProcessor.Config.console_log_keys_train"></a>`console_log_keys_train` — [`L54`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/processor.py#L54) — ---
  - <a id="MetricsProcessor.Config.console_log_keys_validation"></a>`console_log_keys_validation` — [`L80`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/processor.py#L80) — ---
  - <a id="MetricsProcessor.Config.enable_tensorboard"></a>`enable_tensorboard` — [`L94`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/processor.py#L94) — ---
  - <a id="MetricsProcessor.Config.enable_wandb"></a>`enable_wandb` — [`L91`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/processor.py#L91) — ---
  - <a id="MetricsProcessor.Config.wandb_project"></a>`wandb_project` — [`L97`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/processor.py#L97) — ---
- uses (calls/refs, reference-scoped): [`Configurable`](../../../../config/configurable.md#Configurable), [`Config`](../../../../config/configurable.md#Configurable.Config)
- used by: [`log`](processor.md#MetricsProcessor.log), [`_backends`](processor.md#MetricsProcessor._backends), [`metrics`](../../controller.md#Controller.Config.metrics), [`__init__`](processor.md#MetricsProcessor.__init__)  (35 test-only)

## Module values
- <a id="__all__"></a>`__all__` — [`L30`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/processor.py#L30)

