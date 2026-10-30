---
title: 'Module: torchtitan/experiments/tpu/examples/gemma4/infra/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/examples/gemma4/infra/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.examples.gemma4.infra.parallelize`/
symbols:
  _parallelize_gemma4: _parallelize_gemma4().
  parallelize_gemma4: parallelize_gemma4().
  configure_gemma4_simple_fsdp_shard_dims: configure_gemma4_simple_fsdp_shard_dims().
  _apply_ac_gemma4: _apply_ac_gemma4().
  _apply_compile_gemma4: _apply_compile_gemma4().
---
# Module: [`torchtitan/experiments/tpu/examples/gemma4/infra/parallelize.py`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/infra/parallelize.py)

## Functions
- <a id="_apply_ac_gemma4"></a>`_apply_ac_gemma4(model: nn.Module, ac_config: torchtitan.distributed.activation_checkpoint.ActivationCheckpointing.Config, dump_folder: str)` — [`L29`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/infra/parallelize.py#L29)
- <a id="_apply_compile_gemma4"></a>`_apply_compile_gemma4(model: nn.Module, compile_config: torchtitan.config.CompileConfig)` — [`L41`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/infra/parallelize.py#L41) — Apply torch.compile to each Gemma4TransformerBlock with dynamic=False.
- <a id="_parallelize_gemma4"></a>`_parallelize_gemma4(model: nn.Module, *, parallel_dims: torchtitan.distributed.ParallelDims, training: torchtitan.config.TrainingConfig, parallelism: torchtitan.config.ParallelismConfig, compile_config: torchtitan.config.CompileConfig, ac_config: torchtitan.distributed.activation_checkpoint.ActivationCheckpointing.Config | None, dump_folder: str, skip_dp: bool = False)` — [`L65`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/infra/parallelize.py#L65) — Apply DTensor/SPMD TP, EP, AC, compile, and FSDP to Gemma4.
- <a id="configure_gemma4_simple_fsdp_shard_dims"></a>`configure_gemma4_simple_fsdp_shard_dims(model: nn.Module, parallel_dims: torchtitan.distributed.ParallelDims)` — [`L146`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/infra/parallelize.py#L146) — Use divisible hidden axes for uneven Gemma4 parameters under SimpleFSDP.
- <a id="parallelize_gemma4"></a>`parallelize_gemma4(model: nn.Module, *, parallel_dims: torchtitan.distributed.ParallelDims, training: torchtitan.config.TrainingConfig, parallelism: torchtitan.config.ParallelismConfig, compile_config: torchtitan.config.CompileConfig, ac_config: torchtitan.distributed.activation_checkpoint.ActivationCheckpointing.Config | None, dump_folder: str, skip_dp: bool = False, tpu_compile_mode: str = "layer", **kwargs)` — [`L215`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/infra/parallelize.py#L215) — Parallelizes the Gemma4 model, optionally applying Simple FSDP.

