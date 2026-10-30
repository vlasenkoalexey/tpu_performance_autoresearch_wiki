---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/muse_glimmer.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/muse_glimmer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.muse_glimmer`/
symbols:
  parallelize_muse_glimmer: parallelize_muse_glimmer().
  model_registry: model_registry().
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/muse_glimmer.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/muse_glimmer.py)

## Functions
- <a id="model_registry"></a>`model_registry(flavor: str)` — [`L59`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/muse_glimmer.py#L59) — Returns the GraphTrainer ``ModelSpec`` for a TPU Muse Glimmer flavor.
- <a id="parallelize_muse_glimmer"></a>`parallelize_muse_glimmer(model: GraphTrainerMuseGlimmerModel, *, training: TrainingConfig, parallel_dims: ParallelDims, **kwargs)` — [`L33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/muse_glimmer.py#L33) — Applies the TPU uneven-vocab FSDP policy, then upstream's setup.

