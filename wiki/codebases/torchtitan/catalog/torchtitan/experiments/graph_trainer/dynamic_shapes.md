---
title: 'Module: torchtitan/experiments/graph_trainer/dynamic_shapes.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/dynamic_shapes.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.dynamic_shapes`/
symbols:
  _wrapper_subclass_has_marked_dynamic_dims: _wrapper_subclass_has_marked_dynamic_dims().
  _fakeify_input: _fakeify_input().
  _fakeify_input.copy_tensor_annotations: _fakeify_input().copy_tensor_annotations().
  _tensor_has_mark_unbacked: _tensor_has_mark_unbacked().
  _tensor_has_mark_dynamic: _tensor_has_mark_dynamic().
  _insert_runtime_asserts: _insert_runtime_asserts().
  _DYNAMO_SHAPE_ANNOTATION_NAMES: _DYNAMO_SHAPE_ANNOTATION_NAMES.
  _symbolic_context_for_marked_dims: _symbolic_context_for_marked_dims().
---
# Module: [`torchtitan/experiments/graph_trainer/dynamic_shapes.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/dynamic_shapes.py)

## Functions
- <a id="_fakeify_input"></a>`_fakeify_input(fake_mode: FakeTensorMode, arg: torch.Tensor, *, input_name: str)` — [`L170`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/dynamic_shapes.py#L170) — Fakeify one tracer input while preserving user shape annotations.
- <a id="_insert_runtime_asserts"></a>`_insert_runtime_asserts(gm: torch.fx.GraphModule, fake_mode: FakeTensorMode)` — [`L205`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/dynamic_shapes.py#L205) — Materialize the ShapeEnv's deferred runtime asserts into the graph.
- <a id="_symbolic_context_for_marked_dims"></a>`_symbolic_context_for_marked_dims(tensor: torch.Tensor)` — [`L94`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/dynamic_shapes.py#L94) — Convert Dynamo shape annotations into FakeTensor symbolic context.
- <a id="_tensor_has_mark_dynamic"></a>`_tensor_has_mark_dynamic(tensor: torch.Tensor)` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/dynamic_shapes.py#L62) — Return whether ``tensor`` itself carries mark_dynamic() metadata.
- <a id="_tensor_has_mark_unbacked"></a>`_tensor_has_mark_unbacked(tensor: torch.Tensor)` — [`L54`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/dynamic_shapes.py#L54) — Return whether ``tensor`` itself carries mark_unbacked() metadata.
- <a id="_wrapper_subclass_has_marked_dynamic_dims"></a>`_wrapper_subclass_has_marked_dynamic_dims(tensor: torch.Tensor)` — [`L67`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/dynamic_shapes.py#L67) — Detect marked dims anywhere inside a traceable wrapper subclass.
- <a id="_fakeify_input.copy_tensor_annotations"></a>`copy_tensor_annotations(fake_arg: torch.Tensor)` — [`L182`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/dynamic_shapes.py#L182)

## Module values
- <a id="_DYNAMO_SHAPE_ANNOTATION_NAMES"></a>`_DYNAMO_SHAPE_ANNOTATION_NAMES` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/dynamic_shapes.py#L34)

