---
title: 'Module: torchtitan/models/qwen3_5/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/models/qwen3_5/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.qwen3_5.parallelize`/
symbols:
  parallelize_qwen3_5: parallelize_qwen3_5().
---
# Module: [`torchtitan/models/qwen3_5/parallelize.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/parallelize.py)

## Functions
- <a id="parallelize_qwen3_5"></a>`parallelize_qwen3_5(model: nn.Module, *, parallel_dims: ParallelDims, training: TrainingConfig, parallelism: ParallelismConfig, compile_config: CompileConfig, ac_config: ActivationCheckpointingConfig, dump_folder: str, skip_dp: bool = False)` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/parallelize.py#L34) — Apply tensor parallelism, activation checkpointing, torch.compile, and data — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)

