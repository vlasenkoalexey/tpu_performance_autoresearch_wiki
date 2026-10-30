---
title: 'Module: torchtitan/experiments/tpu/llama3/infra/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/llama3/infra/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.llama3.infra.parallelize`/
symbols:
  parallelize_llama: parallelize_llama().
---
# Module: [`torchtitan/experiments/tpu/llama3/infra/parallelize.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/infra/parallelize.py)

## Functions
- <a id="parallelize_llama"></a>`parallelize_llama(model: nn.Module, *, parallel_dims: torchtitan.distributed.ParallelDims, training: torchtitan.config.TrainingConfig, parallelism: torchtitan.config.ParallelismConfig, compile_config: torchtitan.config.CompileConfig, ac_config: torchtitan.distributed.activation_checkpoint.ActivationCheckpointing.Config, dump_folder: str, skip_dp: bool = False, tpu_compile_mode: str = "layer", **kwargs)` — [`L21`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/infra/parallelize.py#L21) — Parallelizes the Llama model based on the provided configuration and applies TPU-specific workarounds.

