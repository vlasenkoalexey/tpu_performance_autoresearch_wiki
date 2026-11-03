---
title: 'Module: src/vllm_torchtpu/distributed/pcp.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/pcp.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.pcp`/
symbols:
  get_or_create_pcp_mesh: get_or_create_pcp_mesh().
  get_pcp_rank: get_pcp_rank().
  get_pcp_world_size: get_pcp_world_size().
  get_pcp_group_layout: get_pcp_group_layout().
  get_pcp_group: get_pcp_group().
  all_reduce_sum: all_reduce_sum().
  all_gather_equal_tokens: all_gather_equal_tokens().
  logger: logger.
  PcpGroupLayout: PcpGroupLayout.
  _MESH_CACHE._MESH_CACHE: _MESH_CACHE._MESH_CACHE.
---
# Module: [`src/vllm_torchtpu/distributed/pcp.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp.py)

## Functions
- <a id="all_gather_equal_tokens"></a>`all_gather_equal_tokens(tensor: torch.Tensor, dim: int = 0)` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp.py#L59) — Gather equal-shaped tensors across the native PCP group. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="all_reduce_sum"></a>`all_reduce_sum(tensor: torch.Tensor)` — [`L72`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp.py#L72) — Sum a tensor across the native PCP group.
- <a id="get_or_create_pcp_mesh"></a>`get_or_create_pcp_mesh(axis_name: str = "pcp", *, tp_axis_name: str | None = None)` — [`L92`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp.py#L92) — Build a rank-aligned PCP x TP mesh over the TorchTPU world. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="get_pcp_group"></a>`get_pcp_group()` — [`L39`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp.py#L39) — Return vLLM's native PCP group, or None before distributed init. — documented in [adaptive-fused-moe-kernel](../../../../concepts/adaptive-fused-moe-kernel.md)
- <a id="get_pcp_group_layout"></a>`get_pcp_group_layout()` — [`L82`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp.py#L82) — Return the current PCP group's rank order and TPU device-id order. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="get_pcp_rank"></a>`get_pcp_rank()` — [`L49`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp.py#L49)
- <a id="get_pcp_world_size"></a>`get_pcp_world_size()` — [`L54`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp.py#L54) — documented in [adaptive-fused-moe-kernel](../../../../concepts/adaptive-fused-moe-kernel.md)

## Module values
- <a id="PcpGroupLayout"></a>`PcpGroupLayout` — [`L31`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp.py#L31)
- <a id="_MESH_CACHE._MESH_CACHE"></a>`_MESH_CACHE` — [`L36`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp.py#L36)
- <a id="logger"></a>`logger` — [`L29`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pcp.py#L29)

