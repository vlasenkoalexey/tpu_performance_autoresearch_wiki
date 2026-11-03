---
title: 'Module: src/vllm_torchtpu/distributed/pallas_shapes.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/pallas_shapes.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.pallas_shapes`/
symbols:
  install_pallas_shape_conversion: install_pallas_shape_conversion().
  get_global_shape: get_global_shape().
  get_local_shape: get_local_shape().
  _convert_partitioned_shape: _convert_partitioned_shape().
---
# Module: [`src/vllm_torchtpu/distributed/pallas_shapes.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pallas_shapes.py)

## Functions
- <a id="_convert_partitioned_shape"></a>`_convert_partitioned_shape(shape, mesh, partition_spec, *, to_global)` — [`L25`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pallas_shapes.py#L25)
- <a id="get_global_shape"></a>`get_global_shape(local_shape, mesh, partition_spec)` — [`L41`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pallas_shapes.py#L41)
- <a id="get_local_shape"></a>`get_local_shape(global_shape, mesh, partition_spec)` — [`L45`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pallas_shapes.py#L45)
- <a id="install_pallas_shape_conversion"></a>`install_pallas_shape_conversion()` — [`L51`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/pallas_shapes.py#L51) — Apply the shared conversion before custom ops are registered. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)

