---
title: 'Module: src/torch_tpu/_internal/distributed/device_utils.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/distributed/device_utils.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.distributed.device_utils`/
symbols:
  device_kind_handler_dict.device_kind_handler_dict: device_kind_handler_dict.device_kind_handler_dict.
  _get_physical_tpu_mesh: _get_physical_tpu_mesh().
  create_device_mesh: create_device_mesh().
  _v5e_create_device_mesh: _v5e_create_device_mesh().
  _create_device_mesh_for_nd_torus_splitting_axes: _create_device_mesh_for_nd_torus_splitting_axes().
  _7x_create_device_mesh: _7x_create_device_mesh().
  _tpu_v2_v3_create_device_mesh: _tpu_v2_v3_create_device_mesh().
  _v4i_v8i_create_device_mesh: _v4i_v8i_create_device_mesh().
  _v5p_create_device_mesh: _v5p_create_device_mesh().
  _TRANSPOSE_TRICKS._TRANSPOSE_TRICKS: _TRANSPOSE_TRICKS._TRANSPOSE_TRICKS.
  _create_device_mesh_for_nd_torus: _create_device_mesh_for_nd_torus().
  _enumerate_feasible_logical_axis_assignments: _enumerate_feasible_logical_axis_assignments().
  _transpose_trick: _transpose_trick().
  create_hybrid_device_mesh: create_hybrid_device_mesh().
  _TPU_V2: _TPU_V2.
  _TPU_V3: _TPU_V3.
  _TPU_V5: _TPU_V5.
  _TPU_V5P: _TPU_V5P.
  _TPU_7X: _TPU_7X.
  _TPU_7: _TPU_7.
  _TPU_8I: _TPU_8I.
  _TRAY_RING_ORDER: _TRAY_RING_ORDER.
  _TRAY_2x2_RING_ORDER: _TRAY_2x2_RING_ORDER.
  _get_prime_factors: _get_prime_factors().
  _TPU_V4_LITE: _TPU_V4_LITE.
  _TPU_V5_LITE: _TPU_V5_LITE.
  _TPU_V5E: _TPU_V5E.
  _TPU_V6_LITE: _TPU_V6_LITE.
  _TRAY_4x4_RING_ORDER: _TRAY_4x4_RING_ORDER.
  _V5E_TRAY_RING_ORDER: _V5E_TRAY_RING_ORDER.
  _V5E_TRAY_IOTA_ORDER: _V5E_TRAY_IOTA_ORDER.
  _V5P_2x2x2_ORDER: _V5P_2x2x2_ORDER.
  _7X_TRAY_2x2x2_RING_ORDER: _7X_TRAY_2x2x2_RING_ORDER.
  _prefer_first_logical_axis_assignment: _prefer_first_logical_axis_assignment().
  _generate_logical_mesh: _generate_logical_mesh().
  _canonicalize_axis_sizes: _canonicalize_axis_sizes().
  _TPU_V4: _TPU_V4.
---
# Module: [`src/torch_tpu/_internal/distributed/device_utils.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py)

## Functions
- <a id="_7x_create_device_mesh"></a>`_7x_create_device_mesh(mesh_shape: Sequence[int], devices: Sequence[Any], **unused_kwargs)` — [`L193`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L193) — Creates device assignment for small 7x topologies.
- <a id="_canonicalize_axis_sizes"></a>`_canonicalize_axis_sizes(axis_sizes: Sequence[int])` — [`L775`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L775)
- <a id="_create_device_mesh_for_nd_torus"></a>`_create_device_mesh_for_nd_torus(physical_mesh: np.ndarray, mesh_shape: Sequence[int], *, allow_split_physical_axes: bool = False)` — [`L251`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L251) — Assigns logical parallelism axes to physical axes of an N-D torus network.
- <a id="_create_device_mesh_for_nd_torus_splitting_axes"></a>`_create_device_mesh_for_nd_torus_splitting_axes(physical_mesh: np.ndarray, mesh_shape: Sequence[int])` — [`L377`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L377) — Assigns logical parallelism axes to physical axes of an N-D torus network.
- <a id="_enumerate_feasible_logical_axis_assignments"></a>`_enumerate_feasible_logical_axis_assignments(physical_mesh_shape: Sequence[int], assignment: np.ndarray, logical_axis_size: int)` — [`L469`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L469) — Yields feasible assignments for a single logical axis.
- <a id="_generate_logical_mesh"></a>`_generate_logical_mesh(physical_mesh: np.ndarray, logical_mesh_shape: Sequence[int], assignment: np.ndarray)` — [`L610`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L610) — Compute the logical mesh from assignment map.
- <a id="_get_physical_tpu_mesh"></a>`_get_physical_tpu_mesh(jax_devices: Sequence[Any])` — [`L664`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L664) — Rearrange TPU devices in a slice into a physical mesh. — documented in [distributed-launchers-and-spmd](../../../../../concepts/distributed-launchers-and-spmd.md)
- <a id="_get_prime_factors"></a>`_get_prime_factors(x: int)` — [`L454`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L454) — Returns a sorted list of prime factors for the given number.
- <a id="_prefer_first_logical_axis_assignment"></a>`_prefer_first_logical_axis_assignment(x: np.ndarray, y: np.ndarray, *, physical_mesh_shape: Sequence[int], assignment: np.ndarray)` — [`L536`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L536) — Returns True if the first axis assignment is preferred over the second.
- <a id="_tpu_v2_v3_create_device_mesh"></a>`_tpu_v2_v3_create_device_mesh(mesh_shape: Sequence[int], devices: Sequence[Any], **unused_kwargs)` — [`L80`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L80)
- <a id="_transpose_trick"></a>`_transpose_trick(physical_mesh: np.ndarray, mesh_shape: Sequence[int])` — [`L748`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L748)
- <a id="_v4i_v8i_create_device_mesh"></a>`_v4i_v8i_create_device_mesh(mesh_shape: Sequence[int], devices: Sequence[Any], **unused_kwargs)` — [`L104`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L104)
- <a id="_v5e_create_device_mesh"></a>`_v5e_create_device_mesh(mesh_shape: Sequence[int], devices: Sequence[Any], **unused_kwargs)` — [`L115`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L115) — Creates rotated pincer device assignment for selected topologies.
- <a id="_v5p_create_device_mesh"></a>`_v5p_create_device_mesh(mesh_shape: Sequence[int], devices: Sequence[Any], **unused_kwargs)` — [`L164`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L164) — Creates device assignment for selected topologies.
- <a id="create_device_mesh"></a>`create_device_mesh(mesh_shape: Sequence[int], devices: Sequence[Any] | None = None, *, contiguous_submeshes: bool = False, allow_split_physical_axes: bool = False)` — [`L785`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L785) — Creates a performant device mesh for jax.sharding.Mesh.
- <a id="create_hybrid_device_mesh"></a>`create_hybrid_device_mesh(mesh_shape: Sequence[int], dcn_mesh_shape: Sequence[int], devices: Sequence[Any] | None = None, *, process_is_granule: bool = False, should_sort_granules_by_key: bool = True, allow_split_physical_axes: bool = False)` — [`L864`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L864) — Creates a device mesh for hybrid (e.g., ICI and DCN) parallelism.

## Module values
- <a id="_7X_TRAY_2x2x2_RING_ORDER"></a>`_7X_TRAY_2x2x2_RING_ORDER` — [`L77`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L77)
- <a id="_TPU_7"></a>`_TPU_7` — [`L37`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L37)
- <a id="_TPU_7X"></a>`_TPU_7X` — [`L36`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L36)
- <a id="_TPU_8I"></a>`_TPU_8I` — [`L38`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L38)
- <a id="_TPU_V2"></a>`_TPU_V2` — [`L27`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L27)
- <a id="_TPU_V3"></a>`_TPU_V3` — [`L28`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L28)
- <a id="_TPU_V4"></a>`_TPU_V4` — [`L29`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L29)
- <a id="_TPU_V4_LITE"></a>`_TPU_V4_LITE` — [`L30`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L30)
- <a id="_TPU_V5"></a>`_TPU_V5` — [`L32`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L32)
- <a id="_TPU_V5E"></a>`_TPU_V5E` — [`L33`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L33)
- <a id="_TPU_V5P"></a>`_TPU_V5P` — [`L34`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L34)
- <a id="_TPU_V5_LITE"></a>`_TPU_V5_LITE` — [`L31`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L31)
- <a id="_TPU_V6_LITE"></a>`_TPU_V6_LITE` — [`L35`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L35)
- <a id="_TRANSPOSE_TRICKS._TRANSPOSE_TRICKS"></a>`_TRANSPOSE_TRICKS` — [`L45`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L45)
- <a id="_TRAY_2x2_RING_ORDER"></a>`_TRAY_2x2_RING_ORDER` — [`L72`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L72)
- <a id="_TRAY_4x4_RING_ORDER"></a>`_TRAY_4x4_RING_ORDER` — [`L73`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L73)
- <a id="_TRAY_RING_ORDER"></a>`_TRAY_RING_ORDER` — [`L71`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L71)
- <a id="_V5E_TRAY_IOTA_ORDER"></a>`_V5E_TRAY_IOTA_ORDER` — [`L75`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L75)
- <a id="_V5E_TRAY_RING_ORDER"></a>`_V5E_TRAY_RING_ORDER` — [`L74`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L74)
- <a id="_V5P_2x2x2_ORDER"></a>`_V5P_2x2x2_ORDER` — [`L76`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L76)
- <a id="device_kind_handler_dict.device_kind_handler_dict"></a>`device_kind_handler_dict` — [`L233`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/device_utils.py#L233) — documented in [distributed-launchers-and-spmd](../../../../../concepts/distributed-launchers-and-spmd.md)

