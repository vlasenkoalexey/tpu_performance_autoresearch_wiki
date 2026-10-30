---
title: 'Module: torchtitan/experiments/tpu/muse_glimmer/infra/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/muse_glimmer/infra/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.muse_glimmer.infra.parallelize`/
symbols:
  parallelize_muse_glimmer: parallelize_muse_glimmer().
  configure_muse_glimmer_simple_fsdp_shard_dims: configure_muse_glimmer_simple_fsdp_shard_dims().
  _validate_supported: _validate_supported().
  _EMBEDDING_FQN: _EMBEDDING_FQN.
---
# Module: [`torchtitan/experiments/tpu/muse_glimmer/infra/parallelize.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/infra/parallelize.py)

## Functions
- <a id="_validate_supported"></a>`_validate_supported(model: nn.Module, parallel_dims: torchtitan.distributed.ParallelDims)` — [`L98`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/infra/parallelize.py#L98)
- <a id="configure_muse_glimmer_simple_fsdp_shard_dims"></a>`configure_muse_glimmer_simple_fsdp_shard_dims(model: nn.Module, parallel_dims: torchtitan.distributed.ParallelDims)` — [`L35`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/infra/parallelize.py#L35) — Selects SimpleFSDP dim 1 for vocab-sized weights with an uneven dim 0.
- <a id="parallelize_muse_glimmer"></a>`parallelize_muse_glimmer(model: nn.Module, *, parallel_dims: torchtitan.distributed.ParallelDims, training: torchtitan.config.TrainingConfig, parallelism: torchtitan.config.ParallelismConfig, compile_config: torchtitan.config.CompileConfig, ac_config: torchtitan.distributed.activation_checkpoint.ActivationCheckpointingConfig | None, dump_folder: str, skip_dp: bool = False, tpu_compile_mode: str = "layer", **kwargs)` — [`L124`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/infra/parallelize.py#L124) — Parallelizes a text-only Muse Glimmer model for TPU.

## Module values
- <a id="_EMBEDDING_FQN"></a>`_EMBEDDING_FQN` — [`L32`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/infra/parallelize.py#L32)

