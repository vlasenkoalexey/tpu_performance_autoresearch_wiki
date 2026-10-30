---
title: 'Module: torchtitan/models/flux/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/models/flux/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.flux.parallelize`/
symbols:
  parallelize_flux: parallelize_flux().
  parallelize_encoders: parallelize_encoders().
  apply_compile: apply_compile().
  apply_ac: apply_ac().
  apply_fsdp: apply_fsdp().
  _checkpoint_block: _checkpoint_block().
  _full_ac_save_splash_policy: _full_ac_save_splash_policy().
  _is_splash_attention_fwd: _is_splash_attention_fwd().
---
# Module: [`torchtitan/models/flux/parallelize.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/parallelize.py)

## Functions
- <a id="_checkpoint_block"></a>`_checkpoint_block(block: nn.Module, ac_config)` — [`L229`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/parallelize.py#L229)
- <a id="_full_ac_save_splash_policy"></a>`_full_ac_save_splash_policy(ctx, func, *args, **kwargs)` — [`L217`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/parallelize.py#L217) — Full activation checkpointing, except the splash-attention forward is saved.
- <a id="_is_splash_attention_fwd"></a>`_is_splash_attention_fwd(func)` — [`L206`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/parallelize.py#L206) — True for the Pallas splash-attention forward ops.
- <a id="apply_ac"></a>`apply_ac(model: nn.Module, ac_config: ActivationCheckpointingConfig)` — [`L237`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/parallelize.py#L237) — Apply full activation checkpointing to the Flux double/single blocks.
- <a id="apply_compile"></a>`apply_compile(model: nn.Module, compile_config: CompileConfig)` — [`L184`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/parallelize.py#L184) — Apply torch.compile to each DoubleStreamBlock and SingleStreamBlock, which
- <a id="apply_fsdp"></a>`apply_fsdp(model: nn.Module, dp_mesh: DeviceMesh, param_dtype: torch.dtype, reduce_dtype: torch.dtype, cpu_offload: bool = False, enable_symm_mem: bool = False, dp_mesh_dims: DataParallelMeshDims | None = None)` — [`L117`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/parallelize.py#L117) — Apply data parallelism (via FSDP2) to the model.
- <a id="parallelize_encoders"></a>`parallelize_encoders(t5_model: FluxEmbedder, clip_model: FluxEmbedder, parallel_dims: ParallelDims, *, training: TrainingConfig, parallelism: ParallelismConfig, enable_symm_mem: bool = False)` — [`L257`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/parallelize.py#L257) — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)
- <a id="parallelize_flux"></a>`parallelize_flux(model: FluxModel, *, parallel_dims: ParallelDims, training: TrainingConfig, parallelism: ParallelismConfig, compile_config: CompileConfig, ac_config: ActivationCheckpointingConfig, dump_folder: str)` — [`L52`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/parallelize.py#L52) — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)

