---
title: 'Module: src/torch_tpu/_internal/distributed/distributed.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/distributed/distributed.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.distributed.distributed`/
symbols:
  set_tpu_launch_env: set_tpu_launch_env().
  _query_local_device_coords: _query_local_device_coords().
  _get_slice_host_coordinates: _get_slice_host_coordinates().
  _calculate_topological_node_rank: _calculate_topological_node_rank().
  set_tpu_launch_env.resolve_node_rank: set_tpu_launch_env().resolve_node_rank().
  _print_local_device_coords: _print_local_device_coords().
  set_tpu_launch_env.build_slicebuilder_addresses: set_tpu_launch_env().build_slicebuilder_addresses().
  set_tpu_launch_env.resolve_nnodes: set_tpu_launch_env().resolve_nnodes().
  _print_launch_env: _print_launch_env().
  _LOCAL_DEVICE_COORDS_PREFIX: _LOCAL_DEVICE_COORDS_PREFIX.
  set_tpu_launch_env.require_worker_hostnames: set_tpu_launch_env().require_worker_hostnames().
  _PRINT_LOCAL_DEVICE_COORDS_FLAG: _PRINT_LOCAL_DEVICE_COORDS_FLAG.
  _CHIPS_PER_HOST._CHIPS_PER_HOST: _CHIPS_PER_HOST._CHIPS_PER_HOST.
  _MODULE_NAME: _MODULE_NAME.
  _LOCAL_DEVICE_COORDS_TIMEOUT_SECONDS: _LOCAL_DEVICE_COORDS_TIMEOUT_SECONDS.
  _parse_topology: _parse_topology().
  set_tpu_launch_env.pick_slicebuilder_addresses: set_tpu_launch_env().pick_slicebuilder_addresses().
  set_tpu_launch_env.require_topology: set_tpu_launch_env().require_topology().
---
# Module: [`src/torch_tpu/_internal/distributed/distributed.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py)

## Functions
- <a id="_calculate_topological_node_rank"></a>`_calculate_topological_node_rank(coords: Sequence[int] | None, topology_str: str | None, fallback_index: str | int | None = None, chips_per_host: tuple[int, int, int] = _CHIPS_PER_HOST)` — [`L191`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L191) — Calculates the topologically sorted NODE_RANK from device coordinates.
- <a id="_get_slice_host_coordinates"></a>`_get_slice_host_coordinates(topology_str: str, chips_per_host: tuple[int, int, int] = _CHIPS_PER_HOST)` — [`L143`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L143) — Computes and returns all host coordinates in the slice, topologically sorted.
- <a id="_parse_topology"></a>`_parse_topology(topology_str: str)` — [`L111`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L111) — Parses a topology string into (Mx, My, Mz) mesh bounds.
- <a id="_print_launch_env"></a>`_print_launch_env()` — [`L479`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L479) — Bootstraps TPU launch env and prints shell variable assignments to stdout.
- <a id="_print_local_device_coords"></a>`_print_local_device_coords()` — [`L316`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L316) — Prints the local TPU device coordinates for `_query_local_device_coords`.
- <a id="_query_local_device_coords"></a>`_query_local_device_coords()` — [`L265`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L265) — Returns the physical coordinates of this host's TPU device, if available.
- <a id="set_tpu_launch_env.build_slicebuilder_addresses"></a>`build_slicebuilder_addresses()` — [`L405`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L405) — Returns one address per device across all worker hosts.
- <a id="set_tpu_launch_env.pick_slicebuilder_addresses"></a>`pick_slicebuilder_addresses()` — [`L461`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L461) — Returns addresses for `count` unused ports on this host.
- <a id="set_tpu_launch_env.require_topology"></a>`require_topology()` — [`L467`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L467) — Returns the detected topology, which must not be empty.
- <a id="set_tpu_launch_env.require_worker_hostnames"></a>`require_worker_hostnames()` — [`L387`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L387) — Returns the parsed worker hostnames, which must not be empty.
- <a id="set_tpu_launch_env.resolve_nnodes"></a>`resolve_nnodes()` — [`L425`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L425) — Returns the total number of hosts in the job.
- <a id="set_tpu_launch_env.resolve_node_rank"></a>`resolve_node_rank()` — [`L434`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L434) — Returns this host's rank, by physical coordinates when available.
- <a id="set_tpu_launch_env"></a>`set_tpu_launch_env(*, nnodes: int | None = None, nproc_per_node: int | None = None)` — [`L328`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L328) — Sets the environment variables a TPU job needs, before workers spawn.

## Module values
- <a id="_CHIPS_PER_HOST._CHIPS_PER_HOST"></a>`_CHIPS_PER_HOST` — [`L91`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L91)
- <a id="_LOCAL_DEVICE_COORDS_PREFIX"></a>`_LOCAL_DEVICE_COORDS_PREFIX` — [`L104`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L104)
- <a id="_LOCAL_DEVICE_COORDS_TIMEOUT_SECONDS"></a>`_LOCAL_DEVICE_COORDS_TIMEOUT_SECONDS` — [`L108`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L108)
- <a id="_MODULE_NAME"></a>`_MODULE_NAME` — [`L95`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L95)
- <a id="_PRINT_LOCAL_DEVICE_COORDS_FLAG"></a>`_PRINT_LOCAL_DEVICE_COORDS_FLAG` — [`L99`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed.py#L99)

