---
title: 'Module: torchtitan/experiments/graph_trainer/qwen3/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/qwen3/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.qwen3.parallelize`/
symbols:
  parallelize_qwen3: parallelize_qwen3().
  annotate_qwen3: annotate_qwen3().
---
# Module: [`torchtitan/experiments/graph_trainer/qwen3/parallelize.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/qwen3/parallelize.py)

## Functions
- <a id="annotate_qwen3"></a>`annotate_qwen3(model: GraphTrainerQwen3Model)` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/qwen3/parallelize.py#L24) — Attach annotations to FX graph nodes with ``torch.fx.traceback.annotate_fn``
- <a id="parallelize_qwen3"></a>`parallelize_qwen3(model: GraphTrainerQwen3Model, *, parallel_dims: ParallelDims, training: TrainingConfig, parallelism: ParallelismConfig, compile_config: GraphTrainerCompileConfig, ac_config: ActivationCheckpointingConfig, dump_folder: str)` — [`L40`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/qwen3/parallelize.py#L40) — Apply annotation, parallelization, activation checkpointing, and full graph — documented in [graph-trainer](../../../../../concepts/graph-trainer.md)

