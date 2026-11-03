---
title: 'Module: src/vllm_torchtpu/distributed/dcp.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/dcp.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.dcp`/
symbols:
  get_or_create_dcp_mesh: get_or_create_dcp_mesh().
  get_dcp_group: get_dcp_group().
  get_dcp_rank: get_dcp_rank().
  get_dcp_group_layout: get_dcp_group_layout().
  get_dcp_world_size: get_dcp_world_size().
  logger: logger.
  _MESH_CACHE._MESH_CACHE: _MESH_CACHE._MESH_CACHE.
  DCP_AXIS_NAME: DCP_AXIS_NAME.
  DCP_LANE_AXIS_NAME: DCP_LANE_AXIS_NAME.
  _validate_dcp_rank_alignment: _validate_dcp_rank_alignment().
  _single_device_dcp_mesh: _single_device_dcp_mesh().
---
# Module: [`src/vllm_torchtpu/distributed/dcp.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/dcp.py)

## Functions
- <a id="_single_device_dcp_mesh"></a>`_single_device_dcp_mesh(axis_names: tuple[str, str])` — [`L94`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/dcp.py#L94) — The mesh before distributed init: one device, both axes length 1.
- <a id="_validate_dcp_rank_alignment"></a>`_validate_dcp_rank_alignment(group: Any, dcp_size: int)` — [`L70`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/dcp.py#L70) — Check DCP is the fastest-varying factor of the global rank.
- <a id="get_dcp_group"></a>`get_dcp_group()` — [`L45`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/dcp.py#L45) — Return vLLM's DCP GroupCoordinator, or None if not initialized. — documented in [adaptive-fused-moe-kernel](../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="get_dcp_group_layout"></a>`get_dcp_group_layout()` — [`L65`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/dcp.py#L65) — The DCP group's rank order and the TPU device each rank sits on. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="get_dcp_rank"></a>`get_dcp_rank()` — [`L55`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/dcp.py#L55)
- <a id="get_dcp_world_size"></a>`get_dcp_world_size()` — [`L60`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/dcp.py#L60)
- <a id="get_or_create_dcp_mesh"></a>`get_or_create_dcp_mesh(axis_name: str | None = None)` — [`L104`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/dcp.py#L104) — Build the full-world ``(lane, DCP)`` mesh the DCP Pallas ops run on. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)

## Module values
- <a id="DCP_AXIS_NAME"></a>`DCP_AXIS_NAME` — [`L33`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/dcp.py#L33)
- <a id="DCP_LANE_AXIS_NAME"></a>`DCP_LANE_AXIS_NAME` — [`L37`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/dcp.py#L37)
- <a id="_MESH_CACHE._MESH_CACHE"></a>`_MESH_CACHE` — [`L42`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/dcp.py#L42)
- <a id="logger"></a>`logger` — [`L30`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/dcp.py#L30)

