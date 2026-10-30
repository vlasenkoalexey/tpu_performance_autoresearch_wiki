---
title: 'Module: src/torch_tpu/_internal/compile/dynamic/graph_transformations.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/dynamic/graph_transformations.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.dynamic.graph_transformations`/
symbols:
  apply_dynamism_transformations: apply_dynamism_transformations().
  apply_pre_dynamism_transformations: apply_pre_dynamism_transformations().
  HandleSymIntUsagesPass.__call__: HandleSymIntUsagesPass#__call__().
  HandleDynamicInputTensorPass.__call__: HandleDynamicInputTensorPass#__call__().
  ScanInputsCreatePlaceholdersPass.__call__: ScanInputsCreatePlaceholdersPass#__call__().
  GraphTransformObserver: GraphTransformObserver.
  HandleDynamicInputTensorSetDimensionSizePass._process_node: HandleDynamicInputTensorSetDimensionSizePass#_process_node().
  HandleDynamicInputTensorSetDimensionSizePass.__call__: HandleDynamicInputTensorSetDimensionSizePass#__call__().
  HandleDynamicInputTensorPass._process_node: HandleDynamicInputTensorPass#_process_node().
  DetectSymIntUsagesPass.__call__: DetectSymIntUsagesPass#__call__().
  ConvertConstantSymIntsPass: ConvertConstantSymIntsPass.
  HandleGenerativeOpsPass: HandleGenerativeOpsPass.
  _is_assertion_or_check_node: _is_assertion_or_check_node().
  HandleDynamicInputTensorPass.__init__: HandleDynamicInputTensorPass#__init__().
  HandleDynamicInputTensorSetDimensionSizePass.__init__: HandleDynamicInputTensorSetDimensionSizePass#__init__().
  ScanInputsCreatePlaceholdersPass.__init__: ScanInputsCreatePlaceholdersPass#__init__().
  HandleSymIntUsagesPass.__init__: HandleSymIntUsagesPass#__init__().
  HandleDynamicInputTensorPass._transform_context: HandleDynamicInputTensorPass#_transform_context.
  HandleSymIntUsagesPass._transform_context: HandleSymIntUsagesPass#_transform_context.
  HandleDynamicInputTensorPass: HandleDynamicInputTensorPass#
  HandleDynamicInputTensorPass._placeholders: HandleDynamicInputTensorPass#_placeholders.
  HandleDynamicInputTensorSetDimensionSizePass: HandleDynamicInputTensorSetDimensionSizePass#
  HandleDynamicInputTensorSetDimensionSizePass._transform_context: HandleDynamicInputTensorSetDimensionSizePass#_transform_context.
  HandleDynamicInputTensorSetDimensionSizePass._placeholders: HandleDynamicInputTensorSetDimensionSizePass#_placeholders.
  HandleDynamicInputTensorSetDimensionSizePass._insert_set_dimension_logical_size_node: HandleDynamicInputTensorSetDimensionSizePass#_insert_set_dimension_logical_size_node().
  ScanInputsCreatePlaceholdersPass: ScanInputsCreatePlaceholdersPass#
  ScanInputsCreatePlaceholdersPass._transform_context: ScanInputsCreatePlaceholdersPass#_transform_context.
  ScanInputsCreatePlaceholdersPass._placeholders: ScanInputsCreatePlaceholdersPass#_placeholders.
  HandleSymIntUsagesPass: HandleSymIntUsagesPass#
  _PYTHON_COMPARISON_BUILTINS: _PYTHON_COMPARISON_BUILTINS.
  DetectSymIntUsagesPass: DetectSymIntUsagesPass#
---
# Module: [`src/torch_tpu/_internal/compile/dynamic/graph_transformations.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py)

## Classes
### <a id="DetectSymIntUsagesPass"></a>`DetectSymIntUsagesPass`
- def: [`src/torch_tpu/_internal/compile/dynamic/graph_transformations.py:326`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L326)
- doc: Pass to detect any remaining SymInt usages in the graph after transformations.
- signature: `class DetectSymIntUsagesPass:`
- protocol/private: <a id="DetectSymIntUsagesPass.__call__"></a>`__call__`[`L334`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L334)
- uses (calls/refs, reference-scoped): [`is_symint`](sym_utils.md#is_symint), [`_is_assertion_or_check_node`](graph_transformations.md#_is_assertion_or_check_node)
- used by: [`apply_dynamism_transformations`](graph_transformations.md#apply_dynamism_transformations)

### <a id="HandleDynamicInputTensorPass"></a>`HandleDynamicInputTensorPass`
- def: [`src/torch_tpu/_internal/compile/dynamic/graph_transformations.py:42`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L42)
- doc: Dynamic input tensor transformation pass using pad_real_to_static.
- signature: `class HandleDynamicInputTensorPass:`
- members:
  - <a id="HandleDynamicInputTensorPass.__call__"></a>`__call__(self, graph_module: torch.fx.GraphModule)` — [`L57`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L57) — Runs the op insertion pass. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="HandleDynamicInputTensorPass._process_node"></a>`_process_node(self, graph_module: torch.fx.GraphModule, node: torch.fx.Node, bounded_shape: list[int], is_dynamic: list[bool])` — [`L78`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L78) — Processes a single placeholder node and inserts pad_real_to_static.
- protocol/private: <a id="HandleDynamicInputTensorPass.__init__"></a>`__init__`[`L49`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L49), <a id="HandleDynamicInputTensorPass._placeholders"></a>`_placeholders`[`L55`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L55), <a id="HandleDynamicInputTensorPass._transform_context"></a>`_transform_context`[`L54`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L54)
- uses (calls/refs, reference-scoped): [`is_symint`](sym_utils.md#is_symint), [`ensure_tensor`](graph_transform_context.md#GraphTransformContext.ensure_tensor), [`get_upper_bound`](graph_transform_context.md#GraphTransformContext.get_upper_bound), [`GraphTransformContext`](graph_transform_context.md#GraphTransformContext)
- used by: [`apply_dynamism_transformations`](graph_transformations.md#apply_dynamism_transformations)

### <a id="HandleDynamicInputTensorSetDimensionSizePass"></a>`HandleDynamicInputTensorSetDimensionSizePass`
- def: [`src/torch_tpu/_internal/compile/dynamic/graph_transformations.py:110`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L110)
- doc: Dynamic input tensor transformation pass using set_dimension_logical_size.
- signature: `class HandleDynamicInputTensorSetDimensionSizePass:`
- members:
  - <a id="HandleDynamicInputTensorSetDimensionSizePass.__call__"></a>`__call__(self, graph_module: torch.fx.GraphModule)` — [`L126`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L126) — Runs the op insertion pass. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="HandleDynamicInputTensorSetDimensionSizePass._insert_set_dimension_logical_size_node"></a>`_insert_set_dimension_logical_size_node(self, graph_module: torch.fx.GraphModule, current_tensor_node: torch.fx.Node, size_tensor_node: torch.fx.Node, dim: int, meta: dict[str, Any])` — [`L164`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L164) — Inserts a set_dimension_logical_size node after the current tensor node.
  - <a id="HandleDynamicInputTensorSetDimensionSizePass._process_node"></a>`_process_node(self, graph_module: torch.fx.GraphModule, node: torch.fx.Node, dynamic_dims: Sequence[int])` — [`L140`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L140) — Processes a single placeholder node and inserts set_dimension_size chains.
- protocol/private: <a id="HandleDynamicInputTensorSetDimensionSizePass.__init__"></a>`__init__`[`L118`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L118), <a id="HandleDynamicInputTensorSetDimensionSizePass._placeholders"></a>`_placeholders`[`L124`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L124), <a id="HandleDynamicInputTensorSetDimensionSizePass._transform_context"></a>`_transform_context`[`L123`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L123)
- uses (calls/refs, reference-scoped): [`is_symint`](sym_utils.md#is_symint), [`ensure_tensor`](graph_transform_context.md#GraphTransformContext.ensure_tensor), [`GraphTransformContext`](graph_transform_context.md#GraphTransformContext)
- used by: [`apply_dynamism_transformations`](graph_transformations.md#apply_dynamism_transformations)

### <a id="HandleSymIntUsagesPass"></a>`HandleSymIntUsagesPass`
- def: [`src/torch_tpu/_internal/compile/dynamic/graph_transformations.py:228`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L228)
- doc: Usages of SymInt nodes in tensor operations and graph outputs transformation pass.
- signature: `class HandleSymIntUsagesPass:`
- protocol/private: <a id="HandleSymIntUsagesPass.__call__"></a>`__call__`[`L240`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L240), <a id="HandleSymIntUsagesPass.__init__"></a>`__init__`[`L237`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L237), <a id="HandleSymIntUsagesPass._transform_context"></a>`_transform_context`[`L238`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L238)
- uses (calls/refs, reference-scoped): [`is_symint`](sym_utils.md#is_symint), [`ensure_tensor`](graph_transform_context.md#GraphTransformContext.ensure_tensor), [`GraphTransformContext`](graph_transform_context.md#GraphTransformContext), [`is_symint_node`](sym_utils.md#is_symint_node), [`get_target_device`](sym_utils.md#get_target_device), [`is_scalar`](sym_utils.md#is_scalar)
- used by: [`apply_dynamism_transformations`](graph_transformations.md#apply_dynamism_transformations)

### <a id="ScanInputsCreatePlaceholdersPass"></a>`ScanInputsCreatePlaceholdersPass`
- def: [`src/torch_tpu/_internal/compile/dynamic/graph_transformations.py:182`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L182)
- doc: Pass to scan inputs and create placeholders for SymInt inputs.
- signature: `class ScanInputsCreatePlaceholdersPass:`
- members:
  - <a id="ScanInputsCreatePlaceholdersPass.__call__"></a>`__call__(self, graph_module: torch.fx.GraphModule)` — [`L197`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L197) — Runs the create placeholders pass. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
- protocol/private: <a id="ScanInputsCreatePlaceholdersPass.__init__"></a>`__init__`[`L189`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L189), <a id="ScanInputsCreatePlaceholdersPass._placeholders"></a>`_placeholders`[`L195`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L195), <a id="ScanInputsCreatePlaceholdersPass._transform_context"></a>`_transform_context`[`L194`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L194)
- uses (calls/refs, reference-scoped): [`GraphTransformContext`](graph_transform_context.md#GraphTransformContext), [`is_symint_node`](sym_utils.md#is_symint_node), [`register_symint_placeholder`](graph_transform_context.md#GraphTransformContext.register_symint_placeholder), [`get_target_device`](sym_utils.md#get_target_device)
- used by: [`apply_dynamism_transformations`](graph_transformations.md#apply_dynamism_transformations)

## Functions
- <a id="_is_assertion_or_check_node"></a>`_is_assertion_or_check_node(node: torch.fx.Node)` — [`L316`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L316)
- <a id="apply_dynamism_transformations"></a>`apply_dynamism_transformations(graph_module: torch.fx.GraphModule, example_inputs: Sequence[InputType], symbol_bounds: SymbolBounds, use_pad_real_to_static: bool = True)` — [`L395`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L395) — Runs all FX graph transforms for dynamic shapes. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
- <a id="apply_pre_dynamism_transformations"></a>`apply_pre_dynamism_transformations(graph_module: torch.fx.GraphModule, example_inputs: Sequence[InputType])` — [`L349`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L349) — Runs pre-dynamism passes including view transformations and constant SymInt conversions. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)

## Module values
- <a id="ConvertConstantSymIntsPass"></a>`ConvertConstantSymIntsPass` — [`L35`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L35)
- <a id="GraphTransformObserver"></a>`GraphTransformObserver` — [`L38`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L38) — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
- <a id="HandleGenerativeOpsPass"></a>`HandleGenerativeOpsPass` — [`L39`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L39)
- <a id="_PYTHON_COMPARISON_BUILTINS"></a>`_PYTHON_COMPARISON_BUILTINS` — [`L306`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/graph_transformations.py#L306)

