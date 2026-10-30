---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/passes/insert_combine_barriers.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/passes/insert_combine_barriers.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.passes.insert_combine_barriers`/
symbols:
  apply_combine_barrier_pass: apply_combine_barrier_pass().
  _has_tag: _has_tag().
  _TAG_VAL: _TAG_VAL.
  apply_combine_barrier_pass._insert_barrier: apply_combine_barrier_pass()._insert_barrier().
  _TAG_KEY: _TAG_KEY.
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/passes/insert_combine_barriers.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/passes/insert_combine_barriers.py)

## Functions
- <a id="_has_tag"></a>`_has_tag(node: torch.fx.Node)` — [`L72`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/passes/insert_combine_barriers.py#L72)
- <a id="apply_combine_barrier_pass._insert_barrier"></a>`_insert_barrier(node: torch.fx.Node, users_to_redirect: list[torch.fx.Node])` — [`L130`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/passes/insert_combine_barriers.py#L130) — Insert barrier+getitem after ``node`` and rewrite ``users_to_redirect``
- <a id="apply_combine_barrier_pass"></a>`apply_combine_barrier_pass(gm: torch.fx.GraphModule, example_inputs)` — [`L79`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/passes/insert_combine_barriers.py#L79) — Insert optimization_barrier on entries+exits of the padded-combine — documented in [tpu-graph-trainer](../../../../../../concepts/tpu-graph-trainer.md)

## Module values
- <a id="_TAG_KEY"></a>`_TAG_KEY` — [`L68`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/passes/insert_combine_barriers.py#L68)
- <a id="_TAG_VAL"></a>`_TAG_VAL` — [`L69`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/passes/insert_combine_barriers.py#L69)
- <a id="__all__"></a>`__all__` — [`L193`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/passes/insert_combine_barriers.py#L193)

