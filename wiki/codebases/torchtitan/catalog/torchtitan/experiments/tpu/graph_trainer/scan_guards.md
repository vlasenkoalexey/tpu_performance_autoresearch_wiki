---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/scan_guards.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/scan_guards.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.scan_guards`/
symbols:
  check_scan_parallelism: check_scan_parallelism().
  check_scan_was_applied: check_scan_was_applied().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/scan_guards.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_guards.py)

## Functions
- <a id="check_scan_parallelism"></a>`check_scan_parallelism(parallelism: ParallelismConfig)` — [`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_guards.py#L21) — Scan is 1-D data parallel only.
- <a id="check_scan_was_applied"></a>`check_scan_was_applied(model: nn.Module, *, use_scan_layers: bool)` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_guards.py#L50) — After parallelization: did the flag actually reach anything? — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)

## Module values
- <a id="__all__"></a>`__all__` — [`L15`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_guards.py#L15)

