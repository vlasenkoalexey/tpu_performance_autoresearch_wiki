---
title: 'Module: torchtitan/experiments/tpu/examples/mamba3/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/examples/mamba3/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.examples.mamba3.parallelize`/
symbols:
  parallelize_mamba3: parallelize_mamba3().
---
# Module: [`torchtitan/experiments/tpu/examples/mamba3/parallelize.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/parallelize.py)

## Functions
- <a id="parallelize_mamba3"></a>`parallelize_mamba3(model: Mamba3LM, *, parallel_dims: ParallelDims, training: TrainingConfig, parallelism: ParallelismConfig, compile_config: CompileConfig, ac_config: ActivationCheckpointingConfig, dump_folder: str, skip_dp: bool = False)` — [`L17`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/parallelize.py#L17) — Applies FSDP, compilation, and activation checkpointing to Mamba-3.

