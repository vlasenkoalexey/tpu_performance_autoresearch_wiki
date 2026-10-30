---
title: 'Module: src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.dynamic.view_ops_passes`/
symbols:
  HandleSliceLikeOpsPass._process_slice_op: HandleSliceLikeOpsPass#_process_slice_op().
  HandleSliceLikeOpsPass._process_select_op: HandleSliceLikeOpsPass#_process_select_op().
  HandleSliceLikeOpsPass._process_slice_backward_op: HandleSliceLikeOpsPass#_process_slice_backward_op().
  HandleReshapeLikeOpsPass._process_view_op: HandleReshapeLikeOpsPass#_process_view_op().
  HandleSliceLikeOpsPass._transform_context: HandleSliceLikeOpsPass#_transform_context.
  HandleSliceLikeOpsPass._process_constant_pad_nd_op: HandleSliceLikeOpsPass#_process_constant_pad_nd_op().
  HandleSliceLikeOpsPass._prepare_slice_operand: HandleSliceLikeOpsPass#_prepare_slice_operand().
  _extract_shape_tensors_and_bounds: _extract_shape_tensors_and_bounds().
  _get_node_val: _get_node_val().
  HandleSliceLikeOpsPass._op_handlers: HandleSliceLikeOpsPass#_op_handlers.
  HandleBroadcastLikeOpsPass._process_broadcast_op: HandleBroadcastLikeOpsPass#_process_broadcast_op().
  HandleSliceLikeOpsPass._normalize_index: HandleSliceLikeOpsPass#_normalize_index().
  HandleSliceLikeOpsPass._build_constant_tensor: HandleSliceLikeOpsPass#_build_constant_tensor().
  HandleSliceLikeOpsPass._dynamic_output_dim_sizes: HandleSliceLikeOpsPass#_dynamic_output_dim_sizes().
  ReplaceDynamicOutputBroadcastOpsPreGradPass.__call__: ReplaceDynamicOutputBroadcastOpsPreGradPass#__call__().
  HandleSliceLikeOpsPass._is_negative: HandleSliceLikeOpsPass#_is_negative().
  HandleSliceLikeOpsPass._extract_slice_args: HandleSliceLikeOpsPass#_extract_slice_args().
  HandleSliceLikeOpsPass._replace_node_with_set_logical_sizes: HandleSliceLikeOpsPass#_replace_node_with_set_logical_sizes().
  HandleReshapeLikeOpsPass._op_handlers: HandleReshapeLikeOpsPass#_op_handlers.
  HandleBroadcastLikeOpsPass._op_handlers: HandleBroadcastLikeOpsPass#_op_handlers.
  HandleSliceLikeOpsPass._extract_select_args: HandleSliceLikeOpsPass#_extract_select_args().
  HandleReshapeLikeOpsPass.__init__: HandleReshapeLikeOpsPass#__init__().
  HandleReshapeLikeOpsPass.__call__: HandleReshapeLikeOpsPass#__call__().
  HandleBroadcastLikeOpsPass.__init__: HandleBroadcastLikeOpsPass#__init__().
  HandleBroadcastLikeOpsPass.__call__: HandleBroadcastLikeOpsPass#__call__().
  HandleSliceLikeOpsPass.__init__: HandleSliceLikeOpsPass#__init__().
  HandleSliceLikeOpsPass.__call__: HandleSliceLikeOpsPass#__call__().
  HandleReshapeLikeOpsPass: HandleReshapeLikeOpsPass#
  HandleReshapeLikeOpsPass._transform_context: HandleReshapeLikeOpsPass#_transform_context.
  HandleBroadcastLikeOpsPass: HandleBroadcastLikeOpsPass#
  HandleBroadcastLikeOpsPass._transform_context: HandleBroadcastLikeOpsPass#_transform_context.
  HandleSliceLikeOpsPass: HandleSliceLikeOpsPass#
  _SLICE_LIKE_FUNCTIONS: _SLICE_LIKE_FUNCTIONS.
  _SLICE_LIKE_METHODS: _SLICE_LIKE_METHODS.
  _has_symbolic_index_args: _has_symbolic_index_args().
  ReplaceDynamicOutputBroadcastOpsPreGradPass: ReplaceDynamicOutputBroadcastOpsPreGradPass#
---
# Module: [`src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py)

## Classes
### <a id="HandleBroadcastLikeOpsPass"></a>`HandleBroadcastLikeOpsPass`
- def: [`src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py:139`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L139)
- doc: Broadcast-like ops transformation pass.
- signature: `class HandleBroadcastLikeOpsPass:`
- members:
  - <a id="HandleBroadcastLikeOpsPass.__call__"></a>`__call__(self, graph_module: torch.fx.GraphModule)` — [`L155`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L155) — Runs the broadcast-like ops transformation pass.
  - <a id="HandleBroadcastLikeOpsPass._process_broadcast_op"></a>`_process_broadcast_op(self, graph_module: torch.fx.GraphModule, node: torch.fx.Node)` — [`L163`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L163) — Processes broadcast op node and converts to dynamic_broadcast if dynamic. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
- protocol/private: <a id="HandleBroadcastLikeOpsPass.__init__"></a>`__init__`[`L147`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L147), <a id="HandleBroadcastLikeOpsPass._op_handlers"></a>`_op_handlers`[`L149`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L149), <a id="HandleBroadcastLikeOpsPass._transform_context"></a>`_transform_context`[`L148`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L148)
- uses (calls/refs, reference-scoped): [`is_symint`](sym_utils.md#is_symint), [`GraphTransformContext`](graph_transform_context.md#GraphTransformContext), [`_extract_shape_tensors_and_bounds`](view_ops_passes.md#_extract_shape_tensors_and_bounds)
- used by: [`apply_dynamism_transformations`](graph_transformations.md#apply_dynamism_transformations)

### <a id="HandleReshapeLikeOpsPass"></a>`HandleReshapeLikeOpsPass`
- def: [`src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py:73`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L73)
- doc: Reshape-like ops transformation pass.
- signature: `class HandleReshapeLikeOpsPass:`
- members:
  - <a id="HandleReshapeLikeOpsPass.__call__"></a>`__call__(self, graph_module: torch.fx.GraphModule)` — [`L92`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L92) — Runs the reshape-like ops transformation pass.
  - <a id="HandleReshapeLikeOpsPass._process_view_op"></a>`_process_view_op(self, graph_module: torch.fx.GraphModule, node: torch.fx.Node)` — [`L100`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L100) — Processes view/reshape op node and converts to dynamic_reshape if dynamic. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
- protocol/private: <a id="HandleReshapeLikeOpsPass.__init__"></a>`__init__`[`L81`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L81), <a id="HandleReshapeLikeOpsPass._op_handlers"></a>`_op_handlers`[`L83`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L83), <a id="HandleReshapeLikeOpsPass._transform_context"></a>`_transform_context`[`L82`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L82)
- uses (calls/refs, reference-scoped): [`is_symint`](sym_utils.md#is_symint), [`GraphTransformContext`](graph_transform_context.md#GraphTransformContext), [`_extract_shape_tensors_and_bounds`](view_ops_passes.md#_extract_shape_tensors_and_bounds), [`has_dynamic_shape`](sym_utils.md#has_dynamic_shape)
- used by: [`apply_dynamism_transformations`](graph_transformations.md#apply_dynamism_transformations)

### <a id="HandleSliceLikeOpsPass"></a>`HandleSliceLikeOpsPass`
- def: [`src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py:213`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L213)
- doc: Slice-like ops transformation pass.
- signature: `class HandleSliceLikeOpsPass:`
- members:
  - <a id="HandleSliceLikeOpsPass.__call__"></a>`__call__(self, graph_module: torch.fx.GraphModule)` — [`L441`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L441) — Runs the slice-like ops transformation pass.
  - <a id="HandleSliceLikeOpsPass._build_constant_tensor"></a>`_build_constant_tensor(self, graph_module: torch.fx.GraphModule, node: torch.fx.Node, block_shape: Sequence[Any], value: Any, dtype: torch.dtype)` — [`L274`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L274) — Builds a constant tensor of block_shape using _dynamic_broadcast. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="HandleSliceLikeOpsPass._dynamic_output_dim_sizes"></a>`_dynamic_output_dim_sizes(self, graph_module: torch.fx.GraphModule, node: torch.fx.Node)` — [`L360`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L360) — Returns (dim, runtime size tensor) for every dynamic output dim. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="HandleSliceLikeOpsPass._extract_select_args"></a>`_extract_select_args(self, node: torch.fx.Node, offset: int = 0)` — [`L378`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L378) — Extracts (dim, index) from select node args/kwargs.
  - <a id="HandleSliceLikeOpsPass._extract_slice_args"></a>`_extract_slice_args(self, node: torch.fx.Node, offset: int = 0)` — [`L394`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L394) — Extracts (dim, start, end, step) from slice or slice_backward node args/kwargs.
  - <a id="HandleSliceLikeOpsPass._is_negative"></a>`_is_negative(self, index: int | torch.SymInt)` — [`L238`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L238) — Returns whether an int or SymInt index is negative, without guards. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="HandleSliceLikeOpsPass._normalize_index"></a>`_normalize_index(self, index: int | torch.SymInt, dim_size: Any)` — [`L259`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L259) — Normalizes a negative int or SymInt index relative to dim_size. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="HandleSliceLikeOpsPass._prepare_slice_operand"></a>`_prepare_slice_operand(self, graph_module: torch.fx.GraphModule, node: torch.fx.Node, inp: torch.fx.Node, inp_val: Any, dim: int, start: int | torch.SymInt, slice_extent: int)` — [`L295`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L295) — Returns inp prepared as the operand of a bound-sized _dynamic_slice. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="HandleSliceLikeOpsPass._process_constant_pad_nd_op"></a>`_process_constant_pad_nd_op(self, graph_module: torch.fx.GraphModule, node: torch.fx.Node)` — [`L674`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L674) — Lowers constant_pad_nd on dynamic tensors to dynamic_broadcast + cat. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="HandleSliceLikeOpsPass._process_select_op"></a>`_process_select_op(self, graph_module: torch.fx.GraphModule, node: torch.fx.Node)` — [`L616`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L616) — Processes select op node and converts to dynamic_slice + squeeze. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="HandleSliceLikeOpsPass._process_slice_backward_op"></a>`_process_slice_backward_op(self, graph_module: torch.fx.GraphModule, node: torch.fx.Node)` — [`L550`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L550) — Lowers slice_backward with dynamic input sizes / parameters. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="HandleSliceLikeOpsPass._process_slice_op"></a>`_process_slice_op(self, graph_module: torch.fx.GraphModule, node: torch.fx.Node)` — [`L449`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L449) — Lowers a slice on dynamic input / with dynamic parameters. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="HandleSliceLikeOpsPass._replace_node_with_set_logical_sizes"></a>`_replace_node_with_set_logical_sizes(self, graph_module: torch.fx.GraphModule, node: torch.fx.Node, new_op_node: torch.fx.Node, dynamic_dim_sizes: Sequence[tuple[int, torch.fx.Node]])` — [`L420`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L420) — Wraps new_op_node with set_dimension_logical_size for all dynamic dims, replaces all uses, and erases node.
- protocol/private: <a id="HandleSliceLikeOpsPass.__init__"></a>`__init__`[`L225`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L225), <a id="HandleSliceLikeOpsPass._op_handlers"></a>`_op_handlers`[`L227`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L227), <a id="HandleSliceLikeOpsPass._transform_context"></a>`_transform_context`[`L226`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L226)
- uses (calls/refs, reference-scoped): [`is_symint`](sym_utils.md#is_symint), [`ensure_tensor`](graph_transform_context.md#GraphTransformContext.ensure_tensor), [`get_upper_bound`](graph_transform_context.md#GraphTransformContext.get_upper_bound), [`GraphTransformContext`](graph_transform_context.md#GraphTransformContext), [`_extract_shape_tensors_and_bounds`](view_ops_passes.md#_extract_shape_tensors_and_bounds), [`_get_node_val`](view_ops_passes.md#_get_node_val), [`has_dynamic_shape`](sym_utils.md#has_dynamic_shape), [`get_constant_symint_value`](sym_utils.md#get_constant_symint_value), [`get_symint_bounds`](graph_transform_context.md#GraphTransformContext.get_symint_bounds), [`is_statically_equal`](sym_utils.md#is_statically_equal), [`get_symint_hint`](sym_utils.md#get_symint_hint)
- used by: [`apply_dynamism_transformations`](graph_transformations.md#apply_dynamism_transformations)

### <a id="ReplaceDynamicOutputBroadcastOpsPreGradPass"></a>`ReplaceDynamicOutputBroadcastOpsPreGradPass`
- def: [`src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py:791`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L791)
- doc: Pre-grad pass turning returned dynamic views into explicit copies.
- signature: `class ReplaceDynamicOutputBroadcastOpsPreGradPass:`
- members:
  - <a id="ReplaceDynamicOutputBroadcastOpsPreGradPass.__call__"></a>`__call__(self, graph_module: torch.fx.GraphModule)` — [`L811`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L811) — Runs the pre-grad pass to replace returned dynamic broadcast ops. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
- uses (calls/refs, reference-scoped): [`is_symint_node`](sym_utils.md#is_symint_node), [`_SLICE_LIKE_FUNCTIONS`](view_ops_passes.md#_SLICE_LIKE_FUNCTIONS), [`_SLICE_LIKE_METHODS`](view_ops_passes.md#_SLICE_LIKE_METHODS), [`_has_symbolic_index_args`](view_ops_passes.md#_has_symbolic_index_args)
- used by: [`execute_pre_grad_passes`](dynamic_compiler.md#DynamicCompiler.execute_pre_grad_passes)

## Functions
- <a id="_extract_shape_tensors_and_bounds"></a>`_extract_shape_tensors_and_bounds(graph_module: torch.fx.GraphModule, node: torch.fx.Node, target_shape: Sequence[Any], transform_context: GraphTransformContext)` — [`L35`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L35) — Extracts shape tensor nodes, static bounds, and dynamic flags for a target shape.
- <a id="_get_node_val"></a>`_get_node_val(arg: Any)` — [`L28`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L28) — Unwraps an FX Node to its metadata value ('val') if present.
- <a id="_has_symbolic_index_args"></a>`_has_symbolic_index_args(node: torch.fx.Node)` — [`L773`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L773) — Returns whether any slice/select/narrow index argument of node is dynamic.

## Module values
- <a id="_SLICE_LIKE_FUNCTIONS"></a>`_SLICE_LIKE_FUNCTIONS` — [`L759`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L759)
- <a id="_SLICE_LIKE_METHODS"></a>`_SLICE_LIKE_METHODS` — [`L770`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/view_ops_passes.py#L770)

