---
title: 'Module: torchtitan/experiments/tpu/qwen3_5/infra/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/qwen3_5/infra/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.qwen3_5.infra.parallelize`/
symbols:
  parallelize_qwen3_5: parallelize_qwen3_5().
---
# Module: [`torchtitan/experiments/tpu/qwen3_5/infra/parallelize.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/infra/parallelize.py)

## Functions
- <a id="parallelize_qwen3_5"></a>`parallelize_qwen3_5(model: nn.Module, *, parallel_dims: torchtitan.distributed.ParallelDims, training: torchtitan.config.TrainingConfig, parallelism: torchtitan.config.ParallelismConfig, compile_config: torchtitan.config.CompileConfig, ac_config: torchtitan.distributed.activation_checkpoint.ActivationCheckpointingConfig | None, dump_folder: str, skip_dp: bool = False, tpu_compile_mode: str = "layer", **kwargs)` — [`L19`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/infra/parallelize.py#L19) — Parallelizes a text-only Qwen3.5 model on TPU, optionally with SimpleFSDP.

