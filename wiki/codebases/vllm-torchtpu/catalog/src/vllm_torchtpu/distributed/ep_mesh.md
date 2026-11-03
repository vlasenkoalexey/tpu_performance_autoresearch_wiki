---
title: 'Module: src/vllm_torchtpu/distributed/ep_mesh.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/ep_mesh.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.ep_mesh`/
symbols:
  build_ep_mesh: build_ep_mesh().
  ep_mesh_index: ep_mesh_index().
  ep_token_replica_groups: ep_token_replica_groups().
  ep_device_ids: ep_device_ids().
  EP_AXIS_NAME: EP_AXIS_NAME.
  ep_rank_order: ep_rank_order().
  ep_sorted_gather_group: ep_sorted_gather_group().
  _ep_mesh_order: _ep_mesh_order().
  get_ep_group: get_ep_group().
  logger: logger.
  _MESH_CACHE._MESH_CACHE: _MESH_CACHE._MESH_CACHE.
  _TOKEN_GROUP_CACHE._TOKEN_GROUP_CACHE: _TOKEN_GROUP_CACHE._TOKEN_GROUP_CACHE.
  _SORTED_GATHER_CACHE._SORTED_GATHER_CACHE: _SORTED_GATHER_CACHE._SORTED_GATHER_CACHE.
---
# Module: [`src/vllm_torchtpu/distributed/ep_mesh.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/ep_mesh.py)

## Functions
- <a id="_ep_mesh_order"></a>`_ep_mesh_order(device_ids: tuple[int, ...])` — [`L155`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/ep_mesh.py#L155) — EP rank at each index of the mesh `build_ep_mesh` builds. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="build_ep_mesh"></a>`build_ep_mesh(axis_name: str = EP_AXIS_NAME)` — [`L266`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/ep_mesh.py#L266) — A one-axis JAX mesh over the EP group, or None when EP is off. — documented in [adaptive-fused-moe-kernel](../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="ep_device_ids"></a>`ep_device_ids()` — [`L132`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/ep_mesh.py#L132) — Global TPU device ids of the EP group, in EP-rank order. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="ep_mesh_index"></a>`ep_mesh_index()` — [`L217`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/ep_mesh.py#L217) — This rank's index into the mesh `build_ep_mesh` builds, or None. — documented in [adaptive-fused-moe-kernel](../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="ep_rank_order"></a>`ep_rank_order()` — [`L198`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/ep_mesh.py#L198) — EP rank at each mesh index, or None when EP is off. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="ep_sorted_gather_group"></a>`ep_sorted_gather_group()` — [`L227`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/ep_mesh.py#L227) — A process group over the EP ranks in ascending device-id order. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="ep_token_replica_groups"></a>`ep_token_replica_groups(*, is_sequence_parallel: bool = False)` — [`L63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/ep_mesh.py#L63) — Native token replica groups expressed in the EP mesh's coordinates. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="get_ep_group"></a>`get_ep_group()` — [`L119`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/ep_mesh.py#L119) — vLLM's expert-parallel group, or None when EP is off. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)

## Module values
- <a id="EP_AXIS_NAME"></a>`EP_AXIS_NAME` — [`L56`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/ep_mesh.py#L56) — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="_MESH_CACHE._MESH_CACHE"></a>`_MESH_CACHE` — [`L58`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/ep_mesh.py#L58)
- <a id="_SORTED_GATHER_CACHE._SORTED_GATHER_CACHE"></a>`_SORTED_GATHER_CACHE` — [`L60`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/ep_mesh.py#L60)
- <a id="_TOKEN_GROUP_CACHE._TOKEN_GROUP_CACHE"></a>`_TOKEN_GROUP_CACHE` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/ep_mesh.py#L59)
- <a id="logger"></a>`logger` — [`L49`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/ep_mesh.py#L49)

