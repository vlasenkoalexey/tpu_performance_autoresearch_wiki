---
title: 'Module: src/torch_tpu/_internal/distributed/_distributed_module.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/distributed/_distributed_module.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.distributed._distributed_module`/
symbols:
  DistributedModuleProperties: DistributedModuleProperties#
  DistributedModuleProperties.window_num_stripes: DistributedModuleProperties#window_num_stripes().
  DistributedModuleProperties.window_stripe_chunk_mb: DistributedModuleProperties#window_stripe_chunk_mb().
  _get_backend_fn: _get_backend_fn().
  topology_aware_mesh: topology_aware_mesh().
---
# Module: [`src/torch_tpu/_internal/distributed/_distributed_module.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/_distributed_module.py)

## Classes
### <a id="DistributedModuleProperties"></a>`DistributedModuleProperties`
- def: [`src/torch_tpu/_internal/distributed/_distributed_module.py:38`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/_distributed_module.py#L38)
- doc: Properties of the `torch.tpu.distributed` module.
- signature: `class DistributedModuleProperties:`
- members:
  - <a id="DistributedModuleProperties.window_num_stripes"></a>`window_num_stripes(self)` — [`L49`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/_distributed_module.py#L49) — Maximum concurrent DMA stripes for WindowTpu peer transfers.
  - <a id="DistributedModuleProperties.window_stripe_chunk_mb"></a>`window_stripe_chunk_mb(self)` — [`L80`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/_distributed_module.py#L80) — Minimum payload size in MB per parallel DMA stripe for WindowTpu.
- uses (calls/refs, reference-scoped): [`_get_backend_fn`](_distributed_module.md#_get_backend_fn)

## Functions
- <a id="_get_backend_fn"></a>`_get_backend_fn(name: str)` — [`L30`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/_distributed_module.py#L30) — Returns the `_device_ops_backend` function `name`.
- <a id="topology_aware_mesh"></a>`topology_aware_mesh(mesh_shape: tuple[int, ...], *, dcn_mesh_shape: tuple[int, ...] | None = None, allow_split_physical_axes: bool = False, contiguous_submeshes: bool = False)` — [`L111`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/_distributed_module.py#L111) — Computes a topology-aware rank layout tensor.

