---
title: 'Module: src/vllm_torchtpu/distributed/mesh_utils.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/mesh_utils.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.mesh_utils`/
symbols:
  get_cp_group_layout: get_cp_group_layout().
  CpGroupLayout.world_size: CpGroupLayout#world_size.
  _get_current_global_rank: _get_current_global_rank().
  CpGroupLayout: CpGroupLayout#
  CpGroupLayout.device_ids: CpGroupLayout#device_ids.
  _get_tpu_global_device_id: _get_tpu_global_device_id().
  _collect_rank_to_device_id: _collect_rank_to_device_id().
  CpGroupLayout.ranks: CpGroupLayout#ranks.
  CpGroupLayout.rank_in_group: CpGroupLayout#rank_in_group.
  CpGroupLayout.device_id: CpGroupLayout#device_id().
  CpGroupLayout.prev_rank_in_group: CpGroupLayout#prev_rank_in_group().
  CpGroupLayout.next_rank_in_group: CpGroupLayout#next_rank_in_group().
  _LAYOUT_CACHE._LAYOUT_CACHE: _LAYOUT_CACHE._LAYOUT_CACHE.
  get_pipeline_stage: get_pipeline_stage().
  get_stage_mesh: get_stage_mesh().
---
# Module: [`src/vllm_torchtpu/distributed/mesh_utils.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/mesh_utils.py)

## Classes
### <a id="CpGroupLayout"></a>`CpGroupLayout`
- def: [`src/vllm_torchtpu/distributed/mesh_utils.py:42`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/mesh_utils.py#L42) — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- doc: A CP process group's rank order plus the matching TPU device ids.
- signature: `class CpGroupLayout:`
- members:
  - <a id="CpGroupLayout.device_id"></a>`device_id(self)` — [`L51`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/mesh_utils.py#L51)
  - <a id="CpGroupLayout.next_rank_in_group"></a>`next_rank_in_group(self)` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/mesh_utils.py#L59)
  - <a id="CpGroupLayout.prev_rank_in_group"></a>`prev_rank_in_group(self)` — [`L55`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/mesh_utils.py#L55)
  - <a id="CpGroupLayout.device_ids"></a>`device_ids` — [`L46`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/mesh_utils.py#L46)
  - <a id="CpGroupLayout.rank_in_group"></a>`rank_in_group` — [`L47`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/mesh_utils.py#L47)
  - <a id="CpGroupLayout.ranks"></a>`ranks` — [`L45`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/mesh_utils.py#L45)
  - <a id="CpGroupLayout.world_size"></a>`world_size` — [`L48`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/mesh_utils.py#L48)
- used by: [`get_or_create_pcp_mesh`](pcp.md#get_or_create_pcp_mesh), [`get_cp_group_layout`](mesh_utils.md#get_cp_group_layout), [`stage_chips`](pp_wave.md#stage_chips), [`get_dcp_group_layout`](dcp.md#get_dcp_group_layout), [`_LAYOUT_CACHE`](mesh_utils.md#_LAYOUT_CACHE._LAYOUT_CACHE), [`PcpGroupLayout`](pcp.md#PcpGroupLayout)

## Functions
- <a id="_collect_rank_to_device_id"></a>`_collect_rank_to_device_id(group: Any, global_rank: int, device_id: int)` — [`L92`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/mesh_utils.py#L92) — documented in [adaptive-fused-moe-kernel](../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="_get_current_global_rank"></a>`_get_current_global_rank()` — [`L66`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/mesh_utils.py#L66) — documented in [adaptive-fused-moe-kernel](../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="_get_tpu_global_device_id"></a>`_get_tpu_global_device_id()` — [`L72`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/mesh_utils.py#L72)
- <a id="get_cp_group_layout"></a>`get_cp_group_layout(group: Any | None)` — [`L108`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/mesh_utils.py#L108) — Return `group`'s rank order and the matching TPU device-id order. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="get_pipeline_stage"></a>`get_pipeline_stage()` — [`L155`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/mesh_utils.py#L155) — This worker's pipeline stage and the number of stages.
- <a id="get_stage_mesh"></a>`get_stage_mesh(axis_names: tuple[str, ...], mesh_shape: tuple[int, ...], group: Any, device_ids: tuple[int, ...])` — [`L169`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/mesh_utils.py#L169) — Build a rank-aligned JAX mesh over `group`, one pipeline stage. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)

## Module values
- <a id="_LAYOUT_CACHE._LAYOUT_CACHE"></a>`_LAYOUT_CACHE` — [`L63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/mesh_utils.py#L63)

