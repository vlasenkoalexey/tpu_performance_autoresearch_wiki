---
title: 'Module: torchtitan/distributed/linear.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/linear.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.linear`/
symbols:
  LinearReduceScatter: LinearReduceScatter#
  AllGatherLinear: AllGatherLinear#
  ensure_symm_mem_ops: ensure_symm_mem_ops().
  AllGatherLinear.forward: AllGatherLinear#forward().
  AllGatherLinearMulti.forward: AllGatherLinearMulti#forward().
  LinearReduceScatter.forward: LinearReduceScatter#forward().
  AllGatherLinearMulti: AllGatherLinearMulti#
  AllGatherLinear.spmd_typecheck: AllGatherLinear#spmd_typecheck().
  AllGatherLinear.backward: AllGatherLinear#backward().
  AllGatherLinearMulti.backward: AllGatherLinearMulti#backward().
  AllGatherLinearMulti.spmd_typecheck: AllGatherLinearMulti#spmd_typecheck().
  LinearReduceScatter.spmd_typecheck: LinearReduceScatter#spmd_typecheck().
  LinearReduceScatter.backward: LinearReduceScatter#backward().
---
# Module: [`torchtitan/distributed/linear.py`](../../../../../../raw/code/torchtitan/torchtitan/distributed/linear.py)

## Classes
### <a id="AllGatherLinear"></a>`AllGatherLinear`
- def: [`torchtitan/distributed/linear.py:47`](../../../../../../raw/code/torchtitan/torchtitan/distributed/linear.py#L47)
- doc: All-gather the sequence shard, then apply a column-parallel linear.
- signature: `class AllGatherLinear(torch.autograd.Function):`
- members:
  - <a id="AllGatherLinear.backward"></a>`backward(ctx, grad_y_shard_n: torch.Tensor)` — [`L144`](../../../../../../raw/code/torchtitan/torchtitan/distributed/linear.py#L144)
  - <a id="AllGatherLinear.forward"></a>`forward(ctx, x_shard_m: torch.Tensor, w_shard_n: torch.Tensor, bias_shard_n: torch.Tensor | None, group: dist.ProcessGroup, group_name: str)` — [`L110`](../../../../../../raw/code/torchtitan/torchtitan/distributed/linear.py#L110)
  - <a id="AllGatherLinear.spmd_typecheck"></a>`spmd_typecheck(result: torch.Tensor, *, x_shard_m: torch.Tensor, w_shard_n: torch.Tensor, bias_shard_n: torch.Tensor | None, group_name: str)` — [`L82`](../../../../../../raw/code/torchtitan/torchtitan/distributed/linear.py#L82) — SPMD type: x S(0)@TP, w S(0)@TP -> y S(1)@TP.
- uses (calls/refs, reference-scoped): [`ensure_symm_mem_ops`](linear.md#ensure_symm_mem_ops)
- used by: [`forward`](../models/common/dist_gemm.md#AllGatherFusedQKVLinear.forward), [`forward`](../overrides/fused_swiglu.md#DistGEMMFusedSwiGLU.forward)

### <a id="AllGatherLinearMulti"></a>`AllGatherLinearMulti`
- def: [`torchtitan/distributed/linear.py:185`](../../../../../../raw/code/torchtitan/torchtitan/distributed/linear.py#L185)
- doc: One all-gather feeding a pair of column-parallel linears on the same input.
- signature: `class AllGatherLinearMulti(torch.autograd.Function):`
- members:
  - <a id="AllGatherLinearMulti.backward"></a>`backward(ctx, grad_ya_shard_n: torch.Tensor, grad_yb_shard_n: torch.Tensor)` — [`L243`](../../../../../../raw/code/torchtitan/torchtitan/distributed/linear.py#L243)
  - <a id="AllGatherLinearMulti.forward"></a>`forward(ctx, x_shard_m: torch.Tensor, wa_shard_n: torch.Tensor, wb_shard_n: torch.Tensor, group: dist.ProcessGroup, group_name: str)` — [`L214`](../../../../../../raw/code/torchtitan/torchtitan/distributed/linear.py#L214)
  - <a id="AllGatherLinearMulti.spmd_typecheck"></a>`spmd_typecheck(results: tuple[torch.Tensor, torch.Tensor], *, x_shard_m: torch.Tensor, wa_shard_n: torch.Tensor, wb_shard_n: torch.Tensor, group_name: str)` — [`L283`](../../../../../../raw/code/torchtitan/torchtitan/distributed/linear.py#L283) — SPMD type: x S(0)@TP, both w S(0)@TP -> both y S(1)@TP.
- uses (calls/refs, reference-scoped): [`ensure_symm_mem_ops`](linear.md#ensure_symm_mem_ops)
- used by: [`forward`](../models/common/dist_gemm.md#DistGEMMFeedForward.forward)

### <a id="LinearReduceScatter"></a>`LinearReduceScatter`
- def: [`torchtitan/distributed/linear.py:305`](../../../../../../raw/code/torchtitan/torchtitan/distributed/linear.py#L305)
- doc: Apply a row-parallel linear, then reduce-scatter over the sequence.
- signature: `class LinearReduceScatter(torch.autograd.Function):`
- members:
  - <a id="LinearReduceScatter.backward"></a>`backward(ctx, grad_y_shard_m: torch.Tensor)` — [`L386`](../../../../../../raw/code/torchtitan/torchtitan/distributed/linear.py#L386)
  - <a id="LinearReduceScatter.forward"></a>`forward(ctx, x_shard_k: torch.Tensor, w_shard_k: torch.Tensor, bias: torch.Tensor | None, group: dist.ProcessGroup, group_name: str)` — [`L357`](../../../../../../raw/code/torchtitan/torchtitan/distributed/linear.py#L357)
  - <a id="LinearReduceScatter.spmd_typecheck"></a>`spmd_typecheck(result: torch.Tensor, *, x_shard_k: torch.Tensor, w_shard_k: torch.Tensor, bias: torch.Tensor | None, group_name: str)` — [`L329`](../../../../../../raw/code/torchtitan/torchtitan/distributed/linear.py#L329) — SPMD type: x S(1)@TP, w S(1)@TP, bias R@TP -> y S(0)@TP.
- uses (calls/refs, reference-scoped): [`ensure_symm_mem_ops`](linear.md#ensure_symm_mem_ops)
- used by: [`forward`](../models/common/dist_gemm.md#DistGEMMFeedForward.forward), [`forward`](../overrides/fused_swiglu.md#DistGEMMFusedSwiGLU.forward), [`forward`](../models/common/dist_gemm.md#RowParallelLinear.forward)

## Functions
- <a id="ensure_symm_mem_ops"></a>`ensure_symm_mem_ops()` — [`L35`](../../../../../../raw/code/torchtitan/torchtitan/distributed/linear.py#L35) — Import the symmetric-memory module and return it.

