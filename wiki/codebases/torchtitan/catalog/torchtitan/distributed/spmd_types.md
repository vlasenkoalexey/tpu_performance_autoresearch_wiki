---
title: 'Module: torchtitan/distributed/spmd_types.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/spmd_types.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.spmd_types`/
symbols:
  annotate_input_spmd_types: annotate_input_spmd_types().
  current_spmd_mesh: current_spmd_mesh().
  plain_tensor_to_dtensor_state_dict: plain_tensor_to_dtensor_state_dict().
  spmd_mesh_size: spmd_mesh_size().
  spmd_local_context: spmd_local_context().
  maybe_set_sparse_mesh: maybe_set_sparse_mesh().
  set_current_spmd_mesh: set_current_spmd_mesh().
  spmd_axes: spmd_axes().
  annotate_replicated_parameters: annotate_replicated_parameters().
  _per_axis_types: _per_axis_types().
  spmd_mesh_group: spmd_mesh_group().
  spmd_validate_redistributions._validate_redistribute_spmd_pair: spmd_validate_redistributions()._validate_redistribute_spmd_pair().
  _MESH_TLS: _MESH_TLS.
  dtensor_to_plain_tensor_state_dict: dtensor_to_plain_tensor_state_dict().
  spmd_sparse_mesh: spmd_sparse_mesh().
  spmd_redistribute_per_axis: spmd_redistribute_per_axis().
  set_spmd_meshes: set_spmd_meshes().
  spmd_dense_mesh: spmd_dense_mesh().
  _spmd_mesh_stack: _spmd_mesh_stack().
  spmd_validate_redistributions: spmd_validate_redistributions().
  spmd_validate_redistributions._normalize_partition_spec: spmd_validate_redistributions()._normalize_partition_spec().
  spmd_distribute_tensor: spmd_distribute_tensor().
  __all__: __all__.
---
# Module: [`torchtitan/distributed/spmd_types.py`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py)

## Functions
- <a id="spmd_validate_redistributions._normalize_partition_spec"></a>`_normalize_partition_spec(axis_types: Mapping[MeshAxisName, spmd.PerMeshAxisSpmdType], *, ndim: int)` — [`L322`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L322) — Normalize per-axis-types w/ S(dim) -> PartitionSpec-style tuple.
- <a id="_per_axis_types"></a>`_per_axis_types(layout: spmd.SpmdType)` — [`L281`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L281)
- <a id="_spmd_mesh_stack"></a>`_spmd_mesh_stack()` — [`L133`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L133)
- <a id="spmd_validate_redistributions._validate_redistribute_spmd_pair"></a>`_validate_redistribute_spmd_pair(src: spmd.SpmdType, dst: spmd.SpmdType, *, name: str)` — [`L343`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L343) — Validate a SPMD redistribution is expressible with one-axis collective.
- <a id="annotate_input_spmd_types"></a>`annotate_input_spmd_types(parallel_dims: ParallelDims, input_dict: dict[str, Any], input_sharding: dict[str, spmd.SpmdType])` — [`L230`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L230) — Annotate named forward inputs with SPMD types from ``input_sharding``. — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
- <a id="annotate_replicated_parameters"></a>`annotate_replicated_parameters(module: torch.nn.Module, parallel_dims: ParallelDims)` — [`L266`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L266) — Annotate undistributed model parameters as replicated.
- <a id="current_spmd_mesh"></a>`current_spmd_mesh()` — [`L141`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L141) — Return the current runtime mesh, or ``None`` if unset. — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
- <a id="dtensor_to_plain_tensor_state_dict"></a>`dtensor_to_plain_tensor_state_dict(state_dict: dict[str, Any])` — [`L101`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L101) — Replace DTensor state-dict entries with their plain local tensors.
- <a id="maybe_set_sparse_mesh"></a>`maybe_set_sparse_mesh()` — [`L220`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L220) — Activate the registered sparse mesh under spmd_types, otherwise no-op.
- <a id="plain_tensor_to_dtensor_state_dict"></a>`plain_tensor_to_dtensor_state_dict(state_dict: dict[str, Any], *, state_dict_layouts: Mapping[str, spmd.SpmdType], parallel_dims: ParallelDims)` — [`L69`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L69) — Represent plain local state tensors as DTensors for state transfer.
- <a id="set_current_spmd_mesh"></a>`set_current_spmd_mesh(mesh: DeviceMesh | None)` — [`L195`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L195) — Set TorchTitan and spmd_types current mesh state for one runtime region.
- <a id="set_spmd_meshes"></a>`set_spmd_meshes(*, dense_mesh: DeviceMesh, sparse_mesh: DeviceMesh | None)` — [`L111`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L111) — Register the SPMD meshes for dense and sparse runtime regions.
- <a id="spmd_axes"></a>`spmd_axes(layout: spmd.SpmdType)` — [`L57`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L57) — Return and validate the named mesh axes used by an SPMD layout.
- <a id="spmd_dense_mesh"></a>`spmd_dense_mesh()` — [`L121`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L121) — Return the registered dense SPMD mesh.
- <a id="spmd_distribute_tensor"></a>`spmd_distribute_tensor(tensor: torch.Tensor, mesh: DeviceMesh, layout: spmd.SpmdType)` — [`L490`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L490) — Materialize local state shards according to the declared SPMD layout.
- <a id="spmd_local_context"></a>`spmd_local_context(*local_axes: str)` — [`L174`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L174) — Context manager treating the named mesh axes as local axes.
- <a id="spmd_mesh_group"></a>`spmd_mesh_group(axis_name: str)` — [`L162`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L162) — Return a non-singleton process group from the current SPMD mesh.
- <a id="spmd_mesh_size"></a>`spmd_mesh_size(axis_name: str)` — [`L151`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L151) — Return the size of a mesh axis, or 1 if not active.
- <a id="spmd_redistribute_per_axis"></a>`spmd_redistribute_per_axis(x: torch.Tensor, mesh: DeviceMesh | None, src: spmd.SpmdType, dst: spmd.SpmdType)` — [`L448`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L448) — Redistribute a local tensor along axes whose SPMD type changes.
- <a id="spmd_sparse_mesh"></a>`spmd_sparse_mesh()` — [`L128`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L128) — Return the registered sparse SPMD mesh, if EP is enabled.
- <a id="spmd_validate_redistributions"></a>`spmd_validate_redistributions(sharding_config: Any)` — [`L306`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L306) — Validate that SPMD redistributions fit the current runtime helper.

## Module values
- <a id="_MESH_TLS"></a>`_MESH_TLS` — [`L54`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L54)
- <a id="__all__"></a>`__all__` — [`L33`](../../../../../../raw/code/torchtitan/torchtitan/distributed/spmd_types.py#L33)

