---
title: 'Module: torchtitan/models/kimi_k3/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/models/kimi_k3/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.kimi_k3.parallelize`/
symbols:
  parallelize_kimi_k3: parallelize_kimi_k3().
---
# Module: [`torchtitan/models/kimi_k3/parallelize.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/parallelize.py)

## Functions
- <a id="parallelize_kimi_k3"></a>`parallelize_kimi_k3(model: nn.Module, *, parallel_dims: ParallelDims, training: TrainingConfig, parallelism: ParallelismConfig, compile_config: CompileConfig, ac_config: ActivationCheckpointingConfig, dump_folder: str, skip_dp: bool = False)` — [`L27`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/parallelize.py#L27) — Apply FSDP2 to the Kimi K3 decoder and vision encoder. — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)

