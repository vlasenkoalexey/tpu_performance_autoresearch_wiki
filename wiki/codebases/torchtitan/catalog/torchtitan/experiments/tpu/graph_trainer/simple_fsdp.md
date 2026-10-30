---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.simple_fsdp`/
symbols:
  install_tpu_replicate_computation: install_tpu_replicate_computation().
  TpuReplicateComputation.replicate_compute: TpuReplicateComputation#replicate_compute().
  TpuReplicateComputation: TpuReplicateComputation#
  replicate_sharded_tensor: replicate_sharded_tensor().
  _ShardToReplicate.forward: _ShardToReplicate#forward().
  _ShardToReplicate.backward: _ShardToReplicate#backward().
  _all_gather_on_dim: _all_gather_on_dim().
  _reduce_scatter_on_dim: _reduce_scatter_on_dim().
  _ShardToReplicate: _ShardToReplicate#
  _has_nonleading_shard: _has_nonleading_shard().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py)

## Classes
### <a id="TpuReplicateComputation"></a>`TpuReplicateComputation`  ·  implements/extends ReplicateComputation
- def: [`torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py:114`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py#L114) — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- doc: Use native TPU collectives for even, non-leading SimpleFSDP shards.
- signature: `class TpuReplicateComputation(ReplicateComputation):`
- members:
  - <a id="TpuReplicateComputation.replicate_compute"></a>`replicate_compute(self, x: DTensor)` — [`L117`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py#L117)
- uses (calls/refs, reference-scoped): [`replicate_compute`](../../graph_trainer/simple_fsdp.md#ReplicateComputation.replicate_compute), [`ReplicateComputation`](../../graph_trainer/simple_fsdp.md#ReplicateComputation), [`reduce_dtype`](../../graph_trainer/simple_fsdp.md#ReplicateComputation.reduce_dtype), [`param_dtype`](../../graph_trainer/simple_fsdp.md#ReplicateComputation.param_dtype), [`device_mesh`](../../graph_trainer/simple_fsdp.md#ReplicateComputation.device_mesh), [`replicate_sharded_tensor`](simple_fsdp.md#replicate_sharded_tensor)
- used by: [`replicate_compute`](../../graph_trainer/simple_fsdp.md#ReplicateComputation.replicate_compute), [`install_tpu_replicate_computation`](simple_fsdp.md#install_tpu_replicate_computation), [`ReplicateComputation`](../../graph_trainer/simple_fsdp.md#ReplicateComputation)  (1 test-only)

### <a id="_ShardToReplicate"></a>`_ShardToReplicate`
- def: [`torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py:63`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py#L63)
- signature: `class _ShardToReplicate(torch.autograd.Function):`
- members:
  - <a id="_ShardToReplicate.backward"></a>`backward(ctx: Any, grad: torch.Tensor)` — [`L85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py#L85)
  - <a id="_ShardToReplicate.forward"></a>`forward(ctx: Any, shard: torch.Tensor, group_name: str, param_dtype: torch.dtype | None, reduce_dtype: torch.dtype | None, replicate_group_name: str | None, shard_dim: int)` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py#L66)
- uses (calls/refs, reference-scoped): [`_all_gather_on_dim`](simple_fsdp.md#_all_gather_on_dim), [`_reduce_scatter_on_dim`](simple_fsdp.md#_reduce_scatter_on_dim)
- used by: [`replicate_sharded_tensor`](simple_fsdp.md#replicate_sharded_tensor)

## Functions
- <a id="_all_gather_on_dim"></a>`_all_gather_on_dim(shard: torch.Tensor, dim: int, group_name: str)` — [`L15`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py#L15) — Gather ``dim``, requiring the native dimensional operator on TPU.
- <a id="_has_nonleading_shard"></a>`_has_nonleading_shard(param: torch.Tensor)` — [`L150`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py#L150)
- <a id="_reduce_scatter_on_dim"></a>`_reduce_scatter_on_dim(grad: torch.Tensor, dim: int, group_name: str)` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py#L34) — Reduce-scatter ``dim``, requiring its native TPU operator off dim 0.
- <a id="install_tpu_replicate_computation"></a>`install_tpu_replicate_computation(model: nn.Module)` — [`L157`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py#L157) — Replace SimpleFSDP's parametrization only on the TPU Qwen model.
- <a id="replicate_sharded_tensor"></a>`replicate_sharded_tensor(shard: torch.Tensor, *, group_name: str, shard_dim: int, param_dtype: torch.dtype | None, reduce_dtype: torch.dtype | None, replicate_group_name: str | None = None)` — [`L94`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py#L94) — Return a compute replica whose backward returns the local FSDP shard.

## Module values
- <a id="__all__"></a>`__all__` — [`L206`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py#L206)

