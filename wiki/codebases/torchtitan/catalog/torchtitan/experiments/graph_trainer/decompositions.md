---
title: 'Module: torchtitan/experiments/graph_trainer/decompositions.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/decompositions.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.decompositions`/
symbols:
  apply_decompositions_pass: apply_decompositions_pass().
  _apply_decompositions: _apply_decompositions().
  _copy_attr: _copy_attr().
---
# Module: [`torchtitan/experiments/graph_trainer/decompositions.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/decompositions.py)

## Functions
- <a id="_apply_decompositions"></a>`_apply_decompositions(gm: fx.GraphModule, example_inputs, decomposition_table: dict[torch._ops.OperatorBase, Callable[..., Any]])` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/decompositions.py#L43)
- <a id="_copy_attr"></a>`_copy_attr(src: torch.nn.Module, dst: torch.nn.Module, target: str)` — [`L22`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/decompositions.py#L22)
- <a id="apply_decompositions_pass"></a>`apply_decompositions_pass(gm: fx.GraphModule, example_inputs=None, *, decomposition_table: dict[torch._ops.OperatorBase, Callable[..., Any]], recurse: bool = False, apply_to_root: bool = True)` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/decompositions.py#L70) — Apply decompositions to selected FX graph modules in place.

