---
title: 'Module: torchtitan/experiments/jax/metrics.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/jax/metrics.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.jax.metrics`/
symbols:
  JaxMetricsProcessor._log_summary: JaxMetricsProcessor#_log_summary().
  JaxMetricsProcessor.color: JaxMetricsProcessor#color.
  JaxMetricsProcessor.num_flops_per_token: JaxMetricsProcessor#num_flops_per_token.
  JaxMetricsProcessor.gpu_peak_flops: JaxMetricsProcessor#gpu_peak_flops.
  JaxMetricsProcessor.should_log: JaxMetricsProcessor#should_log().
  JaxMetricsProcessor.log: JaxMetricsProcessor#log().
  JaxMetricsProcessor.ntokens_since_last_log: JaxMetricsProcessor#ntokens_since_last_log.
  JaxMetricsProcessor.data_loading_times: JaxMetricsProcessor#data_loading_times.
  JaxMetricsProcessor.time_last_log: JaxMetricsProcessor#time_last_log.
  get_peak_flops: get_peak_flops().
  JaxMetricsProcessor: JaxMetricsProcessor#
  JaxMetricsProcessor.log_freq: JaxMetricsProcessor#log_freq.
  JaxMetricsProcessor.num_global_devices: JaxMetricsProcessor#num_global_devices.
  JaxMetricsProcessor.__init__: JaxMetricsProcessor#__init__().
  JaxMetricsProcessor.job_config: JaxMetricsProcessor#job_config.
  JaxMetricsProcessor.parallel_dims: JaxMetricsProcessor#parallel_dims.
  JaxMetricsProcessor.tag: JaxMetricsProcessor#tag.
  JaxMetricsProcessor.optimizers: JaxMetricsProcessor#optimizers.
  JaxMetricsProcessor.lr_schedulers: JaxMetricsProcessor#lr_schedulers.
  JaxMetricsProcessor.model_parts: JaxMetricsProcessor#model_parts.
---
# Module: [`torchtitan/experiments/jax/metrics.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py)

## Classes
### <a id="JaxMetricsProcessor"></a>`JaxMetricsProcessor`
- def: [`torchtitan/experiments/jax/metrics.py:52`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L52) — documented in [jax-lane](../../../../concepts/jax-lane.md)
- doc: Metrics processor for jax/ and torchax/ experiments.
- signature: `class JaxMetricsProcessor:`
- members:
  - <a id="JaxMetricsProcessor._log_summary"></a>`_log_summary(self, step: int, avg_loss: float)` — [`L112`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L112) — Compute TPS/TFLOPs/MFU, emit the colorized log line, reset counters. — documented in [jax-lane](../../../../concepts/jax-lane.md)
  - <a id="JaxMetricsProcessor.log"></a>`log(self, step: int, loss: float, max_loss: float | None = None, grad_norm: float | None = None, extra_metrics: dict[str, Any] | None = None)` — [`L100`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L100)
  - <a id="JaxMetricsProcessor.should_log"></a>`should_log(self, step: int)` — [`L97`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L97)
  - <a id="JaxMetricsProcessor.color"></a>`color` — [`L75`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L75)
  - <a id="JaxMetricsProcessor.data_loading_times"></a>`data_loading_times` — [`L85`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L85)
  - <a id="JaxMetricsProcessor.gpu_peak_flops"></a>`gpu_peak_flops` — [`L80`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L80)
  - <a id="JaxMetricsProcessor.job_config"></a>`job_config` — [`L73`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L73)
  - <a id="JaxMetricsProcessor.log_freq"></a>`log_freq` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L74)
  - <a id="JaxMetricsProcessor.lr_schedulers"></a>`lr_schedulers` — [`L94`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L94)
  - <a id="JaxMetricsProcessor.model_parts"></a>`model_parts` — [`L95`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L95)
  - <a id="JaxMetricsProcessor.ntokens_since_last_log"></a>`ntokens_since_last_log` — [`L84`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L84)
  - <a id="JaxMetricsProcessor.num_flops_per_token"></a>`num_flops_per_token` — [`L87`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L87)
  - <a id="JaxMetricsProcessor.num_global_devices"></a>`num_global_devices` — [`L83`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L83)
  - <a id="JaxMetricsProcessor.optimizers"></a>`optimizers` — [`L93`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L93)
  - <a id="JaxMetricsProcessor.parallel_dims"></a>`parallel_dims` — [`L91`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L91)
  - <a id="JaxMetricsProcessor.tag"></a>`tag` — [`L92`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L92)
  - <a id="JaxMetricsProcessor.time_last_log"></a>`time_last_log` — [`L86`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L86)
- protocol/private: <a id="JaxMetricsProcessor.__init__"></a>`__init__`[`L63`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L63)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`Color`](../../tools/utils.md#Color), [`NoColor`](../../tools/utils.md#NoColor), [`blue`](../../tools/utils.md#NoColor.blue), [`green`](../../tools/utils.md#NoColor.green), [`reset`](../../tools/utils.md#NoColor.reset), [`cyan`](../../tools/utils.md#NoColor.cyan), [`magenta`](../../tools/utils.md#NoColor.magenta), [`orange`](../../tools/utils.md#NoColor.orange), [`red`](../../tools/utils.md#NoColor.red), [`get_peak_flops`](metrics.md#get_peak_flops)
- used by: [`train`](trainer.md#JaxTrainer.train)

## Functions
- <a id="get_peak_flops"></a>`get_peak_flops(accelerator: str, num_devices, tpu_megacore)` — [`L15`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/metrics.py#L15) — Return the system-wide peak theoretical BF16 FLOPS for MFU.

