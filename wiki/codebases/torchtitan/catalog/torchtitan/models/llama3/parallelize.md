---
title: 'Module: torchtitan/models/llama3/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/models/llama3/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.llama3.parallelize`/
symbols:
  parallelize_llama: parallelize_llama().
---
# Module: [`torchtitan/models/llama3/parallelize.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/parallelize.py)

## Functions
- <a id="parallelize_llama"></a>`parallelize_llama(model: Llama3Model, *, parallel_dims: ParallelDims, training: TrainingConfig, parallelism: ParallelismConfig, compile_config: CompileConfig, ac_config: ActivationCheckpointingConfig, dump_folder: str, skip_dp: bool = False)` — [`L23`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/parallelize.py#L23) — Apply tensor parallelism, activation checkpointing, torch.compile, and data — documented in [llama3-model](../../../../concepts/llama3-model.md)

