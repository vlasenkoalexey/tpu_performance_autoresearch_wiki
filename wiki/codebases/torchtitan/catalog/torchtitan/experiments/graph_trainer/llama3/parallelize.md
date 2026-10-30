---
title: 'Module: torchtitan/experiments/graph_trainer/llama3/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/llama3/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.llama3.parallelize`/
symbols:
  parallelize_llama: parallelize_llama().
  annotate_llama: annotate_llama().
---
# Module: [`torchtitan/experiments/graph_trainer/llama3/parallelize.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/parallelize.py)

## Functions
- <a id="annotate_llama"></a>`annotate_llama(model: GraphTrainerLlama3Model)` — [`L18`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/parallelize.py#L18) — Attach module FQN annotations to FX graph nodes.
- <a id="parallelize_llama"></a>`parallelize_llama(model: GraphTrainerLlama3Model, *, parallel_dims: ParallelDims, training: TrainingConfig, parallelism: ParallelismConfig, compile_config: CompileConfig, ac_config: ActivationCheckpointingConfig, dump_folder: str)` — [`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/parallelize.py#L28) — Apply tensor parallelism, activation checkpointing, torch.compile, and data

