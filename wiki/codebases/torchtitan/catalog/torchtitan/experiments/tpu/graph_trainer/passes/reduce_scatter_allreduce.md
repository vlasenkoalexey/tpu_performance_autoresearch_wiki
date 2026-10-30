---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/passes/reduce_scatter_allreduce.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/passes/reduce_scatter_allreduce.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.passes.reduce_scatter_allreduce`/
symbols:
  apply_selected_reduce_scatter_allreduce_pass: apply_selected_reduce_scatter_allreduce_pass().
  _find_reduce_scatter: _find_reduce_scatter().
  _WAIT_TENSOR: _WAIT_TENSOR.
  _ALL_REDUCE: _ALL_REDUCE.
  _REDUCE_SCATTER: _REDUCE_SCATTER.
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/passes/reduce_scatter_allreduce.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/passes/reduce_scatter_allreduce.py)

## Functions
- <a id="_find_reduce_scatter"></a>`_find_reduce_scatter(gradient: torch.fx.Node)` — [`L38`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/passes/reduce_scatter_allreduce.py#L38) — Find the reduce-scatter/wait in a tagged gradient's unary FSDP tail.
- <a id="apply_selected_reduce_scatter_allreduce_pass"></a>`apply_selected_reduce_scatter_allreduce_pass(gm: torch.fx.GraphModule, example_inputs, *, parameter_patterns: tuple[str, ...], max_input_bytes: int)` — [`L61`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/passes/reduce_scatter_allreduce.py#L61) — Rewrite all selected gradients, or raise before changing the graph.

## Module values
- <a id="_ALL_REDUCE"></a>`_ALL_REDUCE` — [`L33`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/passes/reduce_scatter_allreduce.py#L33)
- <a id="_REDUCE_SCATTER"></a>`_REDUCE_SCATTER` — [`L34`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/passes/reduce_scatter_allreduce.py#L34)
- <a id="_WAIT_TENSOR"></a>`_WAIT_TENSOR` — [`L35`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/passes/reduce_scatter_allreduce.py#L35)
- <a id="__all__"></a>`__all__` — [`L221`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/passes/reduce_scatter_allreduce.py#L221)

