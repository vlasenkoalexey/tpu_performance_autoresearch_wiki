---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.scan_fsdp`/
symbols:
  plan_stacked_gathers: plan_stacked_gathers().
  gather_slice: gather_slice().
  configure_simple_fsdp_shard_dims: configure_simple_fsdp_shard_dims().
  _movedim_all_gather_tensor: _movedim_all_gather_tensor().
  _movedim_reduce_scatter_tensor: _movedim_reduce_scatter_tensor().
  ScanFSDPSpec: ScanFSDPSpec#
  ScanFSDPSpec.sharded: ScanFSDPSpec#sharded.
  ScanFSDPSpec.param_dtype: ScanFSDPSpec#param_dtype.
  ScanFSDPSpec.gather_dim: ScanFSDPSpec#gather_dim.
  ScanFSDPSpec.group_name: ScanFSDPSpec#group_name.
  ScanFSDPSpec.reduce_dtype: ScanFSDPSpec#reduce_dtype.
  ScanFSDPSpec.replicate_group_name: ScanFSDPSpec#replicate_group_name.
  _AllGatherReduceScatter.forward: _AllGatherReduceScatter#forward().
  _AllGatherReduceScatter.backward: _AllGatherReduceScatter#backward().
  _fold_rows: _fold_rows().
  _gather_on: _gather_on().
  _orig_all_gather_single: _orig_all_gather_single.
  _orig_reduce_scatter_single: _orig_reduce_scatter_single.
  _scatter_on: _scatter_on().
  _AllGatherReduceScatter: _AllGatherReduceScatter#
  _ReduceGradOnly: _ReduceGradOnly#
  __all__: __all__.
  _ReduceGradOnly.forward: _ReduceGradOnly#forward().
  _ReduceGradOnly.backward: _ReduceGradOnly#backward().
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py)

## Classes
### <a id="ScanFSDPSpec"></a>`ScanFSDPSpec`
- def: [`torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py:42`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L42) — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- doc: How the scan body should gather one stacked parameter.
- signature: `class ScanFSDPSpec:`
- members:
  - <a id="ScanFSDPSpec.gather_dim"></a>`gather_dim` — [`L67`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L67)
  - <a id="ScanFSDPSpec.group_name"></a>`group_name` — [`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L62)
  - <a id="ScanFSDPSpec.param_dtype"></a>`param_dtype` — [`L63`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L63)
  - <a id="ScanFSDPSpec.reduce_dtype"></a>`reduce_dtype` — [`L64`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L64)
  - <a id="ScanFSDPSpec.replicate_group_name"></a>`replicate_group_name` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L66)
  - <a id="ScanFSDPSpec.sharded"></a>`sharded` — [`L65`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L65)
- used by: [`plan_stacked_gathers`](scan_fsdp.md#plan_stacked_gathers), [`gather_slice`](scan_fsdp.md#gather_slice), [`fsdp_plan`](layer_stack.md#LayerStack.fsdp_plan)  (4 test-only)

### <a id="_AllGatherReduceScatter"></a>`_AllGatherReduceScatter`
- def: [`torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py:212`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L212)
- doc: Gathers one sharded layer's weight, and reduces its gradient back.
- signature: `class _AllGatherReduceScatter(torch.autograd.Function):`
- members:
  - <a id="_AllGatherReduceScatter.backward"></a>`backward(ctx: Any, grad: torch.Tensor)` — [`L244`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L244)
  - <a id="_AllGatherReduceScatter.forward"></a>`forward(ctx: Any, shard: torch.Tensor, group_name: str, param_dtype: torch.dtype | None, reduce_dtype: torch.dtype | None, replicate_group_name: str | None, gather_dim: int)` — [`L225`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L225)
- uses (calls/refs, reference-scoped): [`_gather_on`](scan_fsdp.md#_gather_on), [`_scatter_on`](scan_fsdp.md#_scatter_on)
- used by: [`gather_slice`](scan_fsdp.md#gather_slice)

### <a id="_ReduceGradOnly"></a>`_ReduceGradOnly`
- def: [`torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py:256`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L256)
- doc: Sums the gradient of a weight SimpleFSDP left replicated.
- signature: `class _ReduceGradOnly(torch.autograd.Function):`
- members:
  - <a id="_ReduceGradOnly.backward"></a>`backward(ctx: Any, grad: torch.Tensor)` — [`L282`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L282)
  - <a id="_ReduceGradOnly.forward"></a>`forward(ctx: Any, replica: torch.Tensor, group_names: tuple[str, ...], param_dtype: torch.dtype | None, reduce_dtype: torch.dtype | None)` — [`L269`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L269)
- used by: [`gather_slice`](scan_fsdp.md#gather_slice)

## Functions
- <a id="_fold_rows"></a>`_fold_rows(t: torch.Tensor, k: int)` — [`L74`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L74) — Views 2-D `t` as `[rows * k, cols // k]`.
- <a id="_gather_on"></a>`_gather_on(x: torch.Tensor, dim: int, group_name: str)` — [`L182`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L182) — All-gather `x` along `dim`, always collecting on dim 0.
- <a id="_movedim_all_gather_tensor"></a>`_movedim_all_gather_tensor(self: torch.Tensor, gather_dim: int, group: Any, tag: str = "")` — [`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L88) — TPU-friendly drop-in replacement for `funcol.all_gather_single` / `all_gather_tensor`.
- <a id="_movedim_reduce_scatter_tensor"></a>`_movedim_reduce_scatter_tensor(self: torch.Tensor, reduceOp: str, scatter_dim: int, group: Any, tag: str = "")` — [`L131`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L131) — TPU-friendly drop-in replacement for `funcol.reduce_scatter_single` / `reduce_scatter_tensor`.
- <a id="_scatter_on"></a>`_scatter_on(x: torch.Tensor, dim: int, group_name: str)` — [`L196`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L196) — Reduce-scatter `x` along `dim`, always scattering on dim 0.
- <a id="configure_simple_fsdp_shard_dims"></a>`configure_simple_fsdp_shard_dims(model: nn.Module, parallel_dims: Any)` — [`L417`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L417) — Picks SimpleFSDP shard axes that divide evenly, for any decoder model.
- <a id="gather_slice"></a>`gather_slice(shard: torch.Tensor, spec: ScanFSDPSpec | None)` — [`L290`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L290) — Turns one layer's local shard into that layer's whole weight.
- <a id="plan_stacked_gathers"></a>`plan_stacked_gathers(holder: nn.Module)` — [`L316`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L316) — Save what the body needs to know about each stack, before ``to_local``.

## Module values
- <a id="__all__"></a>`__all__` — [`L33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L33)
- <a id="_orig_all_gather_single"></a>`_orig_all_gather_single` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L70)
- <a id="_orig_reduce_scatter_single"></a>`_orig_reduce_scatter_single` — [`L71`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py#L71)

