---
title: 'Module: torchtitan/experiments/tpu/examples/mamba2/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/examples/mamba2/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.examples.mamba2.parallelize`/
symbols:
  parallelize_mamba2: parallelize_mamba2().
---
# Module: [`torchtitan/experiments/tpu/examples/mamba2/parallelize.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/parallelize.py)

## Functions
- <a id="parallelize_mamba2"></a>`parallelize_mamba2(model: Mamba2LM, *, parallel_dims: ParallelDims, training: TrainingConfig, parallelism: ParallelismConfig, compile_config: CompileConfig, ac_config: ActivationCheckpointingConfig, dump_folder: str, skip_dp: bool = False)` — [`L21`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/parallelize.py#L21) — Applies FSDP, compilation, and activation checkpointing to Mamba-2.

