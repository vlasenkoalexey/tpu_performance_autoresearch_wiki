---
title: 'Module: torchtitan/experiments/tpu/qwen3/infra/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/qwen3/infra/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.qwen3.infra.parallelize`/
symbols:
  parallelize_qwen3: parallelize_qwen3().
---
# Module: [`torchtitan/experiments/tpu/qwen3/infra/parallelize.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/infra/parallelize.py)

## Functions
- <a id="parallelize_qwen3"></a>`parallelize_qwen3(model: nn.Module, *, parallel_dims: torchtitan.distributed.ParallelDims, training: torchtitan.config.TrainingConfig, parallelism: torchtitan.config.ParallelismConfig, compile_config: torchtitan.config.CompileConfig, ac_config: torchtitan.distributed.activation_checkpoint.ActivationCheckpointing.Config, dump_folder: str, skip_dp: bool = False, tpu_compile_mode: str = "layer", **kwargs)` — [`L23`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/infra/parallelize.py#L23) — Parallelizes the Qwen3 model, optionally applying Simple FSDP. — documented in [tpu-layer-loop-remat-and-layouts](../../../../../../concepts/tpu-layer-loop-remat-and-layouts.md)

