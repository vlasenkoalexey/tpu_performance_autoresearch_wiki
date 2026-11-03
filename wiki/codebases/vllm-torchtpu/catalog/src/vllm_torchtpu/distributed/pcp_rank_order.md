---
title: 'Module: src/vllm_torchtpu/distributed/pcp_rank_order.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/pcp_rank_order.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.pcp_rank_order`/
symbols:
  logger: logger.
  pcp_topology_order: pcp_topology_order().
  resolve_pcp_topology_order: resolve_pcp_topology_order().
  pcp_topology_order.patched: pcp_topology_order().patched().
  verify_pcp_topology_order: verify_pcp_topology_order().
  pcp_topology_order.new_group_preserving_order: pcp_topology_order().new_group_preserving_order().
---
# Module: [`src/vllm_torchtpu/distributed/pcp_rank_order.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp_rank_order.py)

## Functions
- <a id="pcp_topology_order.new_group_preserving_order"></a>`new_group_preserving_order(*args, **kwargs)` — [`L249`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp_rank_order.py#L249)
- <a id="pcp_topology_order.patched"></a>`patched(group_ranks, local_rank, backend, *args, **kwargs)` — [`L213`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp_rank_order.py#L213)
- <a id="pcp_topology_order"></a>`pcp_topology_order(group_ranks_by_name: dict[str, list[list[int]]] | None, preserve_dcp_order: bool = False)` — [`L177`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp_rank_order.py#L177) — Install the mesh's groups while model-parallel groups are built.
- <a id="resolve_pcp_topology_order"></a>`resolve_pcp_topology_order(vllm_config)` — [`L61`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp_rank_order.py#L61) — Groups to build for each axis, or ``None`` if PCP does not apply. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="verify_pcp_topology_order"></a>`verify_pcp_topology_order(group_ranks_by_name: dict[str, list[list[int]]] | None)` — [`L275`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp_rank_order.py#L275) — Assert vLLM adopted the mesh's order, by reading the built groups back.

## Module values
- <a id="logger"></a>`logger` — [`L58`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp_rank_order.py#L58)

