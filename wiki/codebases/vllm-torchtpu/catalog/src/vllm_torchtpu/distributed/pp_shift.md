---
title: 'Module: src/vllm_torchtpu/distributed/pp_shift.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/pp_shift.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.pp_shift`/
symbols:
  get_or_create_pp_mesh: get_or_create_pp_mesh().
  pp_permute_op: pp_permute_op().
  pp_positions: pp_positions().
  pp_permute_op.shift: pp_permute_op().shift().
  _MESH._MESH: _MESH._MESH.
  AXIS: AXIS.
  _POS_OF_RANK._POS_OF_RANK: _POS_OF_RANK._POS_OF_RANK.
  logger: logger.
  _OPS._OPS: _OPS._OPS.
---
# Module: [`src/vllm_torchtpu/distributed/pp_shift.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_shift.py)

## Functions
- <a id="get_or_create_pp_mesh"></a>`get_or_create_pp_mesh()` — [`L46`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_shift.py#L46) — A JAX mesh over the pipeline group's devices in device-id order. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="pp_permute_op"></a>`pp_permute_op(mesh: Mesh, num_tensors: int = 1)` — [`L82`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_shift.py#L82) — Torch op carrying ``num_tensors`` [tokens, width] tensors one stage — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="pp_positions"></a>`pp_positions()` — [`L76`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_shift.py#L76) — Mesh position of each pipeline rank, in rank order.
- <a id="pp_permute_op.shift"></a>`shift(x: jax.Array)` — [`L105`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_shift.py#L105)

## Module values
- <a id="AXIS"></a>`AXIS` — [`L40`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_shift.py#L40)
- <a id="_MESH._MESH"></a>`_MESH` — [`L41`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_shift.py#L41)
- <a id="_OPS._OPS"></a>`_OPS` — [`L43`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_shift.py#L43)
- <a id="_POS_OF_RANK._POS_OF_RANK"></a>`_POS_OF_RANK` — [`L42`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_shift.py#L42)
- <a id="logger"></a>`logger` — [`L38`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pp_shift.py#L38)

