---
title: 'Module: torchtitan/experiments/graph_trainer/deepseek_v3/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/deepseek_v3/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.deepseek_v3.parallelize`/
symbols:
  parallelize_deepseekv3: parallelize_deepseekv3().
  annotate_deepseekv3: annotate_deepseekv3().
---
# Module: [`torchtitan/experiments/graph_trainer/deepseek_v3/parallelize.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/parallelize.py)

## Functions
- <a id="annotate_deepseekv3"></a>`annotate_deepseekv3(model: GraphTrainerDeepSeekV3Model)` — [`L25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/parallelize.py#L25) — Attach annotations to FX graph nodes with ``torch.fx.traceback.annotate_fn``
- <a id="parallelize_deepseekv3"></a>`parallelize_deepseekv3(model: GraphTrainerDeepSeekV3Model, *, parallel_dims: ParallelDims, training: TrainingConfig, parallelism: ParallelismConfig, compile_config: GraphTrainerCompileConfig, ac_config: ActivationCheckpointingConfig, dump_folder: str)` — [`L38`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/parallelize.py#L38) — documented in [graph-trainer](../../../../../concepts/graph-trainer.md)

