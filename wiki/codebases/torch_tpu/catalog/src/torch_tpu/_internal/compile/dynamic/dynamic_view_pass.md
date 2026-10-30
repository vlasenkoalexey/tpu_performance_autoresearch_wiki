---
title: 'Module: src/torch_tpu/_internal/compile/dynamic/dynamic_view_pass.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/dynamic/dynamic_view_pass.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.dynamic.dynamic_view_pass`/InputDynamicViewPass#
symbols:
  InputDynamicViewPass.__call__: __call__().
  InputDynamicViewPass._example_inputs: _example_inputs.
  InputDynamicViewPass.updated_example_inputs: updated_example_inputs().
  InputDynamicViewPass.view_arg_indices: view_arg_indices.
  InputDynamicViewPass: ''
  InputDynamicViewPass._placeholders: _placeholders.
  InputDynamicViewPass.__init__: __init__().
---
# Module: [`src/torch_tpu/_internal/compile/dynamic/dynamic_view_pass.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_view_pass.py)

## Classes
### <a id="InputDynamicViewPass"></a>`InputDynamicViewPass`
- def: [`src/torch_tpu/_internal/compile/dynamic/dynamic_view_pass.py:28`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_view_pass.py#L28)
- doc: Pass to convert non-contiguous view placeholders into contiguous base buffer
- signature: `class InputDynamicViewPass:`
- members:
  - <a id="InputDynamicViewPass.__call__"></a>`__call__(self, graph_module: torch.fx.GraphModule)` — [`L48`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_view_pass.py#L48) — Runs the dynamic view transformation pass on graph_module.
  - <a id="InputDynamicViewPass.updated_example_inputs"></a>`updated_example_inputs(self)` — [`L45`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_view_pass.py#L45)
  - <a id="InputDynamicViewPass.view_arg_indices"></a>`view_arg_indices` — [`L42`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_view_pass.py#L42)
- protocol/private: <a id="InputDynamicViewPass.__init__"></a>`__init__`[`L35`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_view_pass.py#L35), <a id="InputDynamicViewPass._example_inputs"></a>`_example_inputs`[`L41`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_view_pass.py#L41), <a id="InputDynamicViewPass._placeholders"></a>`_placeholders`[`L40`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_view_pass.py#L40)
- uses (calls/refs, reference-scoped): [`decompose_into_view_sequence`](view_decomposition.md#decompose_into_view_sequence)
- used by: [`apply_pre_dynamism_transformations`](graph_transformations.md#apply_pre_dynamism_transformations)

