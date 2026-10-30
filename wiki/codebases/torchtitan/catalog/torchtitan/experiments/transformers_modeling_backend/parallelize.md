---
title: 'Module: torchtitan/experiments/transformers_modeling_backend/parallelize.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/transformers_modeling_backend/parallelize.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.transformers_modeling_backend.parallelize`/
symbols:
  parallelize_hf_transformers: parallelize_hf_transformers().
  apply_fsdp: apply_fsdp().
  _wrap_flex_kernel_cp: _wrap_flex_kernel_cp().
  _wrap_flex_kernel_cp._make_cp_forward: _wrap_flex_kernel_cp()._make_cp_forward().
  _wrap_flex_kernel_cp._make_cp_forward.cp_forward: _wrap_flex_kernel_cp()._make_cp_forward().cp_forward().
  apply_fsdp._shard_placement_fn: apply_fsdp()._shard_placement_fn().
---
# Module: [`torchtitan/experiments/transformers_modeling_backend/parallelize.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/parallelize.py)

## Functions
- <a id="_wrap_flex_kernel_cp._make_cp_forward"></a>`_make_cp_forward(orig_forward)` — [`L68`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/parallelize.py#L68)
- <a id="apply_fsdp._shard_placement_fn"></a>`_shard_placement_fn(param: nn.Parameter, _expert_params: set = expert_params, _expert_placement: Shard = expert_shard_placement, _edp_mesh_info: FSDPMeshInfo = edp_mesh_info, _dp_mesh_info: FSDPMeshInfo = dp_mesh_info)` — [`L339`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/parallelize.py#L339)
- <a id="_wrap_flex_kernel_cp"></a>`_wrap_flex_kernel_cp(model: nn.Module, cp_mesh: DeviceMesh)` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/parallelize.py#L39) — All-gather k/v across the CP axis inside each flex kernel forward.
- <a id="apply_fsdp"></a>`apply_fsdp(model: nn.Module, dp_mesh: DeviceMesh, param_dtype: torch.dtype, reduce_dtype: torch.dtype, pp_enabled: bool, cpu_offload: bool = False, reshard_after_forward_policy: str = "default", ep_degree: int = 1, dp_mod_ep_mesh: DeviceMesh | None = None, dp_mesh_dims: DataParallelMeshDims | None = None, edp_mesh_dims: DataParallelMeshDims | None = None, gradient_divide_factor: int | None = None, enable_symm_mem: bool = False)` — [`L240`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/parallelize.py#L240) — Apply data parallelism (via FSDP2) to the model.
- <a id="_wrap_flex_kernel_cp._make_cp_forward.cp_forward"></a>`cp_forward(query, key, value, **kwargs)` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/parallelize.py#L69)
- <a id="parallelize_hf_transformers"></a>`parallelize_hf_transformers(model: nn.Module, *, parallel_dims: ParallelDims, training: TrainingConfig, parallelism: ParallelismConfig, compile_config: CompileConfig, ac_config: ActivationCheckpointingConfig, dump_folder: str, skip_dp: bool = False)` — [`L87`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/parallelize.py#L87) — Apply parallelism to the HF model using the titan Module protocol.

