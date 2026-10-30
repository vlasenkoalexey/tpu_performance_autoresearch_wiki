---
title: 'Module: src/torch_tpu/_internal/ops/collectives.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/ops/collectives.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.ops.collectives`/
symbols:
  all_gather_dim: all_gather_dim().
  reduce_scatter_dim: reduce_scatter_dim().
  _resolve_group: _resolve_group().
  __all__: __all__.
---
# Module: [`src/torch_tpu/_internal/ops/collectives.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/collectives.py)

## Functions
- <a id="_resolve_group"></a>`_resolve_group(group: Optional[dist.ProcessGroup])` — [`L36`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/collectives.py#L36)
- <a id="all_gather_dim"></a>`all_gather_dim(input: torch.Tensor, dim: int, group: Optional[dist.ProcessGroup] = None)` — [`L51`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/collectives.py#L51) — All-gathers `input` from every rank and concatenates along `dim`.
- <a id="reduce_scatter_dim"></a>`reduce_scatter_dim(input: torch.Tensor, dim: int, group: Optional[dist.ProcessGroup] = None, reduce_op: str = "sum")` — [`L78`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/collectives.py#L78) — Reduces `input` across ranks and returns this rank's chunk along `dim`.

## Module values
- <a id="__all__"></a>`__all__` — [`L30`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/collectives.py#L30)

