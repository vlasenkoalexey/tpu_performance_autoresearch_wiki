---
title: 'Module: torchtitan/models/kimi_k2_7/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/models/kimi_k2_7/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.kimi_k2_7.parallelize`/
symbols:
  parallelize_kimi_k2_5: parallelize_kimi_k2_5().
---
# Module: [`torchtitan/models/kimi_k2_7/parallelize.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/parallelize.py)

## Functions
- <a id="parallelize_kimi_k2_5"></a>`parallelize_kimi_k2_5(model: nn.Module, *, parallel_dims: ParallelDims, training: TrainingConfig, parallelism: ParallelismConfig, compile_config: CompileConfig, ac_config: ActivationCheckpointingConfig, dump_folder: str, skip_dp: bool = False)` — [`L36`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/parallelize.py#L36) — Apply TP/EP, activation checkpointing, ``torch.compile``, and FSDP. — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)

