---
title: 'Module: src/torch_tpu/_internal/compile/dynamic/convert_constant_symints_pass.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/dynamic/convert_constant_symints_pass.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.dynamic.convert_constant_symints_pass`/
symbols:
  ConvertConstantSymIntsPass.__call__: ConvertConstantSymIntsPass#__call__().
  ConvertConstantSymIntsPass._example_inputs: ConvertConstantSymIntsPass#_example_inputs.
  ConvertConstantSymIntsPass.updated_example_inputs: ConvertConstantSymIntsPass#updated_example_inputs().
  _replace_node_with_value: _replace_node_with_value().
  ConvertConstantSymIntsPass: ConvertConstantSymIntsPass#
  ConvertConstantSymIntsPass._placeholders: ConvertConstantSymIntsPass#_placeholders.
  ConvertConstantSymIntsPass.__init__: ConvertConstantSymIntsPass#__init__().
---
# Module: [`src/torch_tpu/_internal/compile/dynamic/convert_constant_symints_pass.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/convert_constant_symints_pass.py)

## Classes
### <a id="ConvertConstantSymIntsPass"></a>`ConvertConstantSymIntsPass`
- def: [`src/torch_tpu/_internal/compile/dynamic/convert_constant_symints_pass.py:36`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/convert_constant_symints_pass.py#L36)
- doc: Converts constant SymInt placeholders and expressions to concrete integers.
- signature: `class ConvertConstantSymIntsPass:`
- members:
  - <a id="ConvertConstantSymIntsPass.updated_example_inputs"></a>`updated_example_inputs(self)` — [`L55`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/convert_constant_symints_pass.py#L55)
- protocol/private: <a id="ConvertConstantSymIntsPass.__call__"></a>`__call__`[`L58`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/convert_constant_symints_pass.py#L58), <a id="ConvertConstantSymIntsPass.__init__"></a>`__init__`[`L46`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/convert_constant_symints_pass.py#L46), <a id="ConvertConstantSymIntsPass._example_inputs"></a>`_example_inputs`[`L52`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/convert_constant_symints_pass.py#L52), <a id="ConvertConstantSymIntsPass._placeholders"></a>`_placeholders`[`L51`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/convert_constant_symints_pass.py#L51)
- uses (calls/refs, reference-scoped): [`get_constant_symint_value`](sym_utils.md#get_constant_symint_value), [`is_constant_symint`](sym_utils.md#is_constant_symint), [`_replace_node_with_value`](convert_constant_symints_pass.md#_replace_node_with_value)
- used by: [`apply_pre_dynamism_transformations`](graph_transformations.md#apply_pre_dynamism_transformations), [`ConvertConstantSymIntsPass`](graph_transformations.md#ConvertConstantSymIntsPass)

## Functions
- <a id="_replace_node_with_value"></a>`_replace_node_with_value(node: torch.fx.Node, value: Any)` — [`L27`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/convert_constant_symints_pass.py#L27) — Replaces uses of an FX node with a scalar constant value.

