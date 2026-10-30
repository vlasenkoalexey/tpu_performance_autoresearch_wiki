---
title: 'Module: torchtitan/experiments/graph_trainer/cudagraph.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/cudagraph.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.cudagraph`/
symbols:
  cudagraph_pass: cudagraph_pass().
  insert_kernel_annotations_pass: insert_kernel_annotations_pass().
  is_cudagraphable: is_cudagraphable().
  is_cudagraph_compatible: is_cudagraph_compatible().
  is_full_cudagraphable: is_full_cudagraphable().
  _iter_tensors: _iter_tensors().
  _has_dynamic_shape: _has_dynamic_shape().
  is_cudagraphable._dyn: is_cudagraphable()._dyn().
  insert_kernel_annotations_pass._exit: insert_kernel_annotations_pass()._exit().
  get_static_input_indices: get_static_input_indices().
  insert_kernel_annotations_pass._enter: insert_kernel_annotations_pass()._enter().
---
# Module: [`torchtitan/experiments/graph_trainer/cudagraph.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cudagraph.py)

## Functions
- <a id="is_cudagraphable._dyn"></a>`_dyn(n: torch.fx.Node)` — [`L95`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cudagraph.py#L95)
- <a id="insert_kernel_annotations_pass._enter"></a>`_enter(annotation: dict)` — [`L208`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cudagraph.py#L208)
- <a id="insert_kernel_annotations_pass._exit"></a>`_exit(ctx: object)` — [`L215`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cudagraph.py#L215)
- <a id="_has_dynamic_shape"></a>`_has_dynamic_shape(val: Any)` — [`L24`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cudagraph.py#L24) — True if ``val`` is (or contains) a tensor with a symbolic (data-dependent)
- <a id="_iter_tensors"></a>`_iter_tensors(val: Any)` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cudagraph.py#L34) — Flatten ``val`` (tensor / list / tuple) to the tensors it contains.
- <a id="cudagraph_pass"></a>`cudagraph_pass(gm: torch.fx.GraphModule, example_inputs: tuple, *, is_forward: bool = True, static_input_indices: list[int] | None = None, tensor_input_indices: list[int] | None = None)` — [`L261`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cudagraph.py#L261) — Apply cudagraph.
- <a id="get_static_input_indices"></a>`get_static_input_indices(gm: torch.fx.GraphModule, is_forward: bool)` — [`L151`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cudagraph.py#L151) — Get indices of gm inputs that are static input tensors whose tensor addresses do not
- <a id="insert_kernel_annotations_pass"></a>`insert_kernel_annotations_pass(gm: torch.fx.GraphModule, example_inputs: tuple | None = None)` — [`L181`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cudagraph.py#L181) — Insert mark_kernels() calls at module boundaries in the FX graph.
- <a id="is_cudagraph_compatible"></a>`is_cudagraph_compatible(gm: torch.fx.GraphModule, *, skip_flex_attention_check: bool = False)` — [`L125`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cudagraph.py#L125) — Whole-graph cudagraph gate: True iff the graph has no cudagraph-unsafe op.
- <a id="is_cudagraphable"></a>`is_cudagraphable(node: torch.fx.Node, dyn_map: dict[torch.fx.Node, bool] | None = None)` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cudagraph.py#L43) — Whether ``node`` can be captured by a CUDA graph.
- <a id="is_full_cudagraphable"></a>`is_full_cudagraphable(gm: torch.fx.GraphModule)` — [`L116`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cudagraph.py#L116) — True if every node is cudagraphable (:func:`is_cudagraphable`), i.e. the

