---
title: 'Module: torchtitan/distributed/fsdp.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/fsdp.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.fsdp`/
symbols:
  apply_fsdp_to_decoder: apply_fsdp_to_decoder().
  resolve_fsdp_mesh: resolve_fsdp_mesh().
  resolve_sparse_fsdp_mesh: resolve_sparse_fsdp_mesh().
  apply_fsdp_to_vision_encoder: apply_fsdp_to_vision_encoder().
  get_fsdp_reshard_after_forward_policy: get_fsdp_reshard_after_forward_policy().
  disable_fsdp_gradient_division: disable_fsdp_gradient_division().
  enable_fsdp_symm_mem: enable_fsdp_symm_mem().
  _DENSE_STORAGE_AXES: _DENSE_STORAGE_AXES.
  _SPARSE_STORAGE_AXES: _SPARSE_STORAGE_AXES.
  apply_fsdp_to_decoder._experts_shard_placement_fn: apply_fsdp_to_decoder()._experts_shard_placement_fn().
  apply_fsdp_to_decoder._shard_placement_fn: apply_fsdp_to_decoder()._shard_placement_fn().
---
# Module: [`torchtitan/distributed/fsdp.py`](../../../../../../raw/code/torchtitan/torchtitan/distributed/fsdp.py)

## Functions
- <a id="apply_fsdp_to_decoder._experts_shard_placement_fn"></a>`_experts_shard_placement_fn(param: nn.Parameter, _expert_params: set = expert_params)` — [`L324`](../../../../../../raw/code/torchtitan/torchtitan/distributed/fsdp.py#L324)
- <a id="apply_fsdp_to_decoder._shard_placement_fn"></a>`_shard_placement_fn(param: nn.Parameter, _expert_params: set = expert_params, _expert_placement: Shard = expert_shard_placement, _edp_mesh_info: FSDPMeshInfo = edp_mesh_info, _dp_mesh_info: FSDPMeshInfo = dp_mesh_info)` — [`L360`](../../../../../../raw/code/torchtitan/torchtitan/distributed/fsdp.py#L360)
- <a id="apply_fsdp_to_decoder"></a>`apply_fsdp_to_decoder(model: Decoder, dp_mesh: DeviceMesh, param_dtype: torch.dtype, reduce_dtype: torch.dtype, pp_enabled: bool, cpu_offload: bool = False, reshard_after_forward_policy: str = "default", ep_degree: int = 1, edp_mesh: DeviceMesh | None = None, dp_mesh_dims: DataParallelMeshDims | None = None, edp_mesh_dims: DataParallelMeshDims | None = None, enable_symm_mem: bool = False)` — [`L189`](../../../../../../raw/code/torchtitan/torchtitan/distributed/fsdp.py#L189) — Apply data parallelism (via FSDP2) to a decoder-style transformer model. — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
- <a id="apply_fsdp_to_vision_encoder"></a>`apply_fsdp_to_vision_encoder(vision_encoder: nn.Module, dp_mesh: DeviceMesh, param_dtype: torch.dtype, reduce_dtype: torch.dtype, reshard_after_forward_policy: str = "default", pp_enabled: bool = False, cpu_offload: bool = False, *, dp_mesh_dims: DataParallelMeshDims | None = None)` — [`L150`](../../../../../../raw/code/torchtitan/torchtitan/distributed/fsdp.py#L150) — FSDP a VLM vision encoder as a single unit.
- <a id="disable_fsdp_gradient_division"></a>`disable_fsdp_gradient_division(model: nn.Module)` — [`L85`](../../../../../../raw/code/torchtitan/torchtitan/distributed/fsdp.py#L85) — Disable FSDP's automatic gradient division for all FSDP modules.
- <a id="enable_fsdp_symm_mem"></a>`enable_fsdp_symm_mem(model: nn.Module)` — [`L113`](../../../../../../raw/code/torchtitan/torchtitan/distributed/fsdp.py#L113) — Enable symmetric-memory communication optimizations for all FSDP modules.
- <a id="get_fsdp_reshard_after_forward_policy"></a>`get_fsdp_reshard_after_forward_policy(reshard_after_forward_policy: str, pp_enabled: bool)` — [`L123`](../../../../../../raw/code/torchtitan/torchtitan/distributed/fsdp.py#L123) — Resolve fsdp_reshard_after_forward policy string to a boolean.
- <a id="resolve_fsdp_mesh"></a>`resolve_fsdp_mesh(parallel_dims: ParallelDims)` — [`L32`](../../../../../../raw/code/torchtitan/torchtitan/distributed/fsdp.py#L32) — Select the dense storage mesh and DataParallelMeshDims. — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
- <a id="resolve_sparse_fsdp_mesh"></a>`resolve_sparse_fsdp_mesh(parallel_dims: ParallelDims)` — [`L65`](../../../../../../raw/code/torchtitan/torchtitan/distributed/fsdp.py#L65) — Sparse counterpart of ``resolve_fsdp_mesh`` for routed experts. — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)

## Module values
- <a id="_DENSE_STORAGE_AXES"></a>`_DENSE_STORAGE_AXES` — [`L28`](../../../../../../raw/code/torchtitan/torchtitan/distributed/fsdp.py#L28)
- <a id="_SPARSE_STORAGE_AXES"></a>`_SPARSE_STORAGE_AXES` — [`L29`](../../../../../../raw/code/torchtitan/torchtitan/distributed/fsdp.py#L29)

