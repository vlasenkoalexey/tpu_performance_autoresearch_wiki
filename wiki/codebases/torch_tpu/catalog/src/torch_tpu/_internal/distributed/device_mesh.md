---
title: 'Module: src/torch_tpu/_internal/distributed/device_mesh.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/distributed/device_mesh.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.distributed.device_mesh`/
symbols:
  _gather_global_device_info: _gather_global_device_info().
  topology_aware_mesh: topology_aware_mesh().
  _validate_multi_slice: _validate_multi_slice().
  _DeviceStub.id: _DeviceStub#id.
  _DeviceStub: _DeviceStub#
  _DeviceStub.slice_index: _DeviceStub#slice_index.
  _DeviceStub.has_slice_index: _DeviceStub#has_slice_index.
  _DeviceStub.coords: _DeviceStub#coords.
  _DeviceStub.core_on_chip: _DeviceStub#core_on_chip.
  _DeviceStub.device_kind: _DeviceStub#device_kind.
  _DeviceStub.platform: _DeviceStub#platform.
  _DeviceStub.process_index: _DeviceStub#process_index.
  _infer_dcn_mesh_shape: _infer_dcn_mesh_shape().
  __all__: __all__.
  get_device_assignment: get_device_assignment().
---
# Module: [`src/torch_tpu/_internal/distributed/device_mesh.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_mesh.py)

## Classes
### <a id="_DeviceStub"></a>`_DeviceStub`
- def: [`src/torch_tpu/_internal/distributed/device_mesh.py:52`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_mesh.py#L52)
- doc: Duck-types the subset of jax.Device that mesh_utils touches.
- signature: `class _DeviceStub:`
- members:
  - <a id="_DeviceStub.coords"></a>`coords` — [`L56`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_mesh.py#L56)
  - <a id="_DeviceStub.core_on_chip"></a>`core_on_chip` — [`L57`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_mesh.py#L57)
  - <a id="_DeviceStub.device_kind"></a>`device_kind` — [`L58`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_mesh.py#L58)
  - <a id="_DeviceStub.has_slice_index"></a>`has_slice_index` — [`L66`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_mesh.py#L66)
  - <a id="_DeviceStub.id"></a>`id` — [`L55`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_mesh.py#L55)
  - <a id="_DeviceStub.platform"></a>`platform` — [`L59`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_mesh.py#L59)
  - <a id="_DeviceStub.process_index"></a>`process_index` — [`L60`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_mesh.py#L60)
  - <a id="_DeviceStub.slice_index"></a>`slice_index` — [`L61`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_mesh.py#L61)
- used by: [`_gather_global_device_info`](device_mesh.md#_gather_global_device_info), [`topology_aware_mesh`](device_mesh.md#topology_aware_mesh), [`_validate_multi_slice`](device_mesh.md#_validate_multi_slice)

## Functions
- <a id="_gather_global_device_info"></a>`_gather_global_device_info(device_type: str)` — [`L69`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_mesh.py#L69) — Each torch rank reports its PJRT device; returns list indexed by rank. — documented in [distributed-launchers-and-spmd](../../../../../concepts/distributed-launchers-and-spmd.md)
- <a id="_infer_dcn_mesh_shape"></a>`_infer_dcn_mesh_shape(mesh_shape: Tuple[int, ...], num_slices: int)` — [`L91`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_mesh.py#L91) — Picks the logical axis along which to split the mesh across slices.
- <a id="_validate_multi_slice"></a>`_validate_multi_slice(infos: list[_DeviceStub], mesh_shape: Tuple[int, ...], dcn_mesh_shape: Tuple[int, ...])` — [`L151`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_mesh.py#L151) — Validates a multi-slice request against the observed device topology.
- <a id="get_device_assignment"></a>`get_device_assignment(pg: Optional[dist.ProcessGroup] = None)` — [`L369`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_mesh.py#L369) — Returns physical device assignment for the given process group.
- <a id="topology_aware_mesh"></a>`topology_aware_mesh(device_type: str, mesh_shape: Tuple[int, ...], *, dcn_mesh_shape: Optional[Tuple[int, ...]] = None, allow_split_physical_axes: bool = False, contiguous_submeshes: bool = False)` — [`L224`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_mesh.py#L224) — Computes a topology-aware rank layout tensor, without building a mesh. — documented in [distributed-launchers-and-spmd](../../../../../concepts/distributed-launchers-and-spmd.md)

## Module values
- <a id="__all__"></a>`__all__` — [`L221`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_mesh.py#L221)

