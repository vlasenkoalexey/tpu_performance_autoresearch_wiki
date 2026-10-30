---
title: 'Module: src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.dynamic.generative_ops_pass`/HandleGenerativeOpsPass#
symbols:
  HandleGenerativeOpsPass._process_bounded_size_op: _process_bounded_size_op().
  HandleGenerativeOpsPass._process_like_op: _process_like_op().
  HandleGenerativeOpsPass._process_arange_op: _process_arange_op().
  HandleGenerativeOpsPass._transform_context: _transform_context.
  HandleGenerativeOpsPass._op_handlers: _op_handlers.
  HandleGenerativeOpsPass._process_arange_dynamic_length: _process_arange_dynamic_length().
  HandleGenerativeOpsPass._process_arange_static_length: _process_arange_static_length().
  HandleGenerativeOpsPass.__init__: __init__().
  HandleGenerativeOpsPass.__call__: __call__().
  HandleGenerativeOpsPass._insert_set_dimension_logical_size: _insert_set_dimension_logical_size().
  HandleGenerativeOpsPass: ''
---
# Module: [`src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.py)

## Classes
### <a id="HandleGenerativeOpsPass"></a>`HandleGenerativeOpsPass`
- def: [`src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.py:23`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.py#L23)
- doc: Generative ops transformation pass.
- signature: `class HandleGenerativeOpsPass:`
- members:
  - <a id="HandleGenerativeOpsPass.__call__"></a>`__call__(self, graph_module: torch.fx.GraphModule)` — [`L172`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.py#L172) — Runs the op insertion pass.
  - <a id="HandleGenerativeOpsPass._insert_set_dimension_logical_size"></a>`_insert_set_dimension_logical_size(self, graph_module: torch.fx.GraphModule, current_node: torch.fx.Node, tensor_size_node: torch.fx.Node, dim: int, original_node: torch.fx.Node)` — [`L403`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.py#L403) — Inserts a set_dimension_logical_size node after the current node.
  - <a id="HandleGenerativeOpsPass._process_arange_dynamic_length"></a>`_process_arange_dynamic_length(self, graph_module: torch.fx.GraphModule, node: torch.fx.Node, length_symint: torch.SymInt, start: Any, end: Any, step: Any, dtype: torch.dtype)` — [`L283`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.py#L283) — Handles arange with dynamic sequence length.
  - <a id="HandleGenerativeOpsPass._process_arange_op"></a>`_process_arange_op(self, graph_module: torch.fx.GraphModule, node: torch.fx.Node)` — [`L180`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.py#L180) — Unified pass to replace dynamic arange with custom op. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="HandleGenerativeOpsPass._process_arange_static_length"></a>`_process_arange_static_length(self, graph_module: torch.fx.GraphModule, node: torch.fx.Node, length: int, start: Any, step: Any, dtype: torch.dtype)` — [`L234`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.py#L234) — Handles arange with dynamic boundaries but constant sequence length.
  - <a id="HandleGenerativeOpsPass._process_bounded_size_op"></a>`_process_bounded_size_op(self, graph_module: torch.fx.GraphModule, node: torch.fx.Node, size_arg_idx: int = 0)` — [`L326`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.py#L326) — Processes generative ops with dynamic sizes (e.g. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="HandleGenerativeOpsPass._process_like_op"></a>`_process_like_op(self, graph_module: torch.fx.GraphModule, node: torch.fx.Node)` — [`L373`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.py#L373) — Processes *_like generative ops with dynamic shapes (e.g. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
- protocol/private: <a id="HandleGenerativeOpsPass.__init__"></a>`__init__`[`L124`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.py#L124), <a id="HandleGenerativeOpsPass._op_handlers"></a>`_op_handlers`[`L126`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.py#L126), <a id="HandleGenerativeOpsPass._transform_context"></a>`_transform_context`[`L125`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/generative_ops_pass.py#L125)
- uses (calls/refs, reference-scoped): [`is_symint`](sym_utils.md#is_symint), [`ensure_tensor`](graph_transform_context.md#GraphTransformContext.ensure_tensor), [`get_upper_bound`](graph_transform_context.md#GraphTransformContext.get_upper_bound), [`GraphTransformContext`](graph_transform_context.md#GraphTransformContext)
- used by: [`HandleGenerativeOpsPass`](graph_transformations.md#HandleGenerativeOpsPass)

