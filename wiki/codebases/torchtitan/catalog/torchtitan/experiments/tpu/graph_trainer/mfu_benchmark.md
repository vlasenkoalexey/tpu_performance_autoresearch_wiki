---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/mfu_benchmark.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/mfu_benchmark.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.mfu_benchmark`/MfuBenchmark#
symbols:
  MfuBenchmark.record: record().
  MfuBenchmark.__post_init__: __post_init__().
  MfuBenchmark.start_step: start_step.
  MfuBenchmark.final_step: final_step.
  MfuBenchmark.metrics_processor: metrics_processor.
  MfuBenchmark: ''
  MfuBenchmark._start_time: _start_time.
  MfuBenchmark._start_tokens: _start_tokens.
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/mfu_benchmark.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/mfu_benchmark.py)

## Classes
### <a id="MfuBenchmark"></a>`MfuBenchmark`
- def: [`torchtitan/experiments/tpu/graph_trainer/mfu_benchmark.py:17`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/mfu_benchmark.py#L17) — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- doc: Get a longer-time average without requiring a less frequent `log_freq`
- signature: `class MfuBenchmark:`
- members:
  - <a id="MfuBenchmark.record"></a>`record(self, step: int, ntokens_seen: int)` — [`L38`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/mfu_benchmark.py#L38) — Record a boundary after the normal metrics path has drained the device.
  - <a id="MfuBenchmark.final_step"></a>`final_step` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/mfu_benchmark.py#L24)
  - <a id="MfuBenchmark.metrics_processor"></a>`metrics_processor` — [`L22`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/mfu_benchmark.py#L22)
  - <a id="MfuBenchmark.start_step"></a>`start_step` — [`L23`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/mfu_benchmark.py#L23)
- protocol/private: <a id="MfuBenchmark.__post_init__"></a>`__post_init__`[`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/mfu_benchmark.py#L28), <a id="MfuBenchmark._start_time"></a>`_start_time`[`L25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/mfu_benchmark.py#L25), <a id="MfuBenchmark._start_tokens"></a>`_start_tokens`[`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/mfu_benchmark.py#L26)
- uses (calls/refs, reference-scoped): [`logger`](../../../tools/logging.md#logger)
- used by: [`_mfu_benchmark`](tpu_graph_trainer.md#TpuGraphTrainer._mfu_benchmark), [`train_step`](tpu_graph_trainer.md#TpuGraphTrainer.train_step)  (1 test-only)

