---
title: 'Module: src/torch_tpu/_internal/export/export.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/export/export.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.export.export`/
symbols:
  fx_to_mlir: fx_to_mlir().
  _process_fx_outputs: _process_fx_outputs().
  _TensorDedupeKey.from_tensor: _TensorDedupeKey#from_tensor().
  exported_to_mlir: exported_to_mlir().
  _extract_sample_arguments: _extract_sample_arguments().
  ExportedMlir.module: ExportedMlir#module.
  EagerLikeFxInterpreter.run_node: EagerLikeFxInterpreter#run_node().
  EagerLikeFxInterpreter.dispatch_fx_node: EagerLikeFxInterpreter#dispatch_fx_node().
  ExportedMlir: ExportedMlir#
  _TensorDedupeKey.layout: _TensorDedupeKey#layout.
  _TensorLayout: _TensorLayout#
  _TensorDedupeKey: _TensorDedupeKey#
  ExportedMlir.serialize_text: ExportedMlir#serialize_text().
  ExportedMlir.serialize_bytecode: ExportedMlir#serialize_bytecode().
  ExportedMlir.serialize_portable_artifact: ExportedMlir#serialize_portable_artifact().
  ExportedMlir.executable: ExportedMlir#executable.
  ExportedMlir.mlir_result_tensors: ExportedMlir#mlir_result_tensors.
  ExportedMlir.reconstruct_fx_outputs_fn: ExportedMlir#reconstruct_fx_outputs_fn.
  ExportedMlir.updates_default_generator_state: ExportedMlir#updates_default_generator_state.
  ExportedMlir.dynamic_outputs: ExportedMlir#dynamic_outputs.
  ExportedMlir.unique_output_indices: ExportedMlir#unique_output_indices.
  EagerLikeFxInterpreter: EagerLikeFxInterpreter#
  _DedupedTensorOutput: _DedupedTensorOutput#
  _NonTensorPassthrough: _NonTensorPassthrough#
  EagerMode.EagerMode: EagerMode.EagerMode.
  _fx_to_mlir_lock: _fx_to_mlir_lock.
  _extract_states_from_exported_program: _extract_states_from_exported_program().
  _extract_sample_arguments._to_aval: _extract_sample_arguments()._to_aval().
  _extract_sample_arguments._get_inputs: _extract_sample_arguments()._get_inputs().
  ExportedMlir.is_noop: ExportedMlir#is_noop.
  EagerLikeFxInterpreter._set_func_code_to_node_source_locations: EagerLikeFxInterpreter#_set_func_code_to_node_source_locations().
  _TensorLayout.dtype: _TensorLayout#dtype.
  _TensorLayout.shape: _TensorLayout#shape.
  _TensorLayout.stride: _TensorLayout#stride.
  _TensorLayout.storage_offset: _TensorLayout#storage_offset.
  _map_unused_fake_inputs_to_outputs: _map_unused_fake_inputs_to_outputs().
  __all__: __all__.
  EagerLikeFxInterpreter.__init__: EagerLikeFxInterpreter#__init__().
  EagerLikeFxInterpreter.state_dict: EagerLikeFxInterpreter#state_dict.
  EagerLikeFxInterpreter._set_current_node: EagerLikeFxInterpreter#_set_current_node().
  _DedupedTensorOutput.tensor_idx: _DedupedTensorOutput#tensor_idx.
  _NonTensorPassthrough.input_idx: _NonTensorPassthrough#input_idx.
  _TensorDedupeKey.data_ptr: _TensorDedupeKey#data_ptr.
  enable_tracebacks: enable_tracebacks().
---
# Module: [`src/torch_tpu/_internal/export/export.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py)

## Classes
### <a id="EagerLikeFxInterpreter"></a>`EagerLikeFxInterpreter`
- def: [`src/torch_tpu/_internal/export/export.py:145`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L145)
- doc: Interpreter for TorchTPU.
- signature: `class EagerLikeFxInterpreter(torch.fx.Interpreter):`
- members:
  - <a id="EagerLikeFxInterpreter._set_current_node"></a>`_set_current_node(self, node: torch.fx.Node)` — [`L191`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L191) — No-op override to prevent mutating process-global FX metadata.
  - <a id="EagerLikeFxInterpreter._set_func_code_to_node_source_locations"></a>`_set_func_code_to_node_source_locations(self, func, node)` — [`L160`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L160) — Update the function's code locations to the node's source locations.
  - <a id="EagerLikeFxInterpreter.dispatch_fx_node"></a>`dispatch_fx_node(node)` — [`L203`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L203)
  - <a id="EagerLikeFxInterpreter.run_node"></a>`run_node(self, node)` — [`L200`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L200) — (Override) Run a single node in the FX graph, adding source locations.
  - <a id="EagerLikeFxInterpreter.state_dict"></a>`state_dict` — [`L158`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L158)
- protocol/private: <a id="EagerLikeFxInterpreter.__init__"></a>`__init__`[`L153`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L153)
- used by: [`fx_to_mlir`](export.md#fx_to_mlir)

### <a id="ExportedMlir"></a>`ExportedMlir`
- def: [`src/torch_tpu/_internal/export/export.py:97`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L97)
- doc: The MLIR representation and compiled executable of an FX graph module.
- signature: `class ExportedMlir:`
- members:
  - <a id="ExportedMlir.serialize_bytecode"></a>`serialize_bytecode(self)` — [`L136`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L136) — Returns the MLIR representation of the graph as bytecode.
  - <a id="ExportedMlir.serialize_portable_artifact"></a>`serialize_portable_artifact(self)` — [`L140`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L140) — Returns the MLIR representation of the graph as a versioned portable artifact.
  - <a id="ExportedMlir.serialize_text"></a>`serialize_text(self, enable_debug_info: bool = False)` — [`L130`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L130) — Returns the MLIR representation of the graph as text.
  - <a id="ExportedMlir.dynamic_outputs"></a>`dynamic_outputs` — [`L127`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L127)
  - <a id="ExportedMlir.executable"></a>`executable` — [`L120`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L120)
  - <a id="ExportedMlir.is_noop"></a>`is_noop` — [`L126`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L126)
  - <a id="ExportedMlir.mlir_result_tensors"></a>`mlir_result_tensors` — [`L121`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L121)
  - <a id="ExportedMlir.module"></a>`module` — [`L119`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L119)
  - <a id="ExportedMlir.reconstruct_fx_outputs_fn"></a>`reconstruct_fx_outputs_fn` — [`L122`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L122)
  - <a id="ExportedMlir.unique_output_indices"></a>`unique_output_indices` — [`L128`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L128)
  - <a id="ExportedMlir.updates_default_generator_state"></a>`updates_default_generator_state` — [`L125`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L125)
- used by: [`fx_to_mlir`](export.md#fx_to_mlir), [`exported_to_mlir`](export.md#exported_to_mlir)

### <a id="_DedupedTensorOutput"></a>`_DedupedTensorOutput`
- def: [`src/torch_tpu/_internal/export/export.py:245`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L245)
- signature: `class _DedupedTensorOutput:`
- members:
  - <a id="_DedupedTensorOutput.tensor_idx"></a>`tensor_idx` — [`L246`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L246)
- used by: [`_process_fx_outputs`](export.md#_process_fx_outputs)

### <a id="_NonTensorPassthrough"></a>`_NonTensorPassthrough`
- def: [`src/torch_tpu/_internal/export/export.py:250`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L250)
- signature: `class _NonTensorPassthrough:`
- members:
  - <a id="_NonTensorPassthrough.input_idx"></a>`input_idx` — [`L251`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L251)
- used by: [`_process_fx_outputs`](export.md#_process_fx_outputs)

### <a id="_TensorDedupeKey"></a>`_TensorDedupeKey`
- def: [`src/torch_tpu/_internal/export/export.py:306`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L306)
- doc: A key for deduplicating tensors based on their data and view layout.
- signature: `class _TensorDedupeKey:`
- members:
  - <a id="_TensorDedupeKey.from_tensor"></a>`from_tensor(cls, tensor: torch.Tensor)` — [`L319`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L319)
  - <a id="_TensorDedupeKey.data_ptr"></a>`data_ptr` — [`L315`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L315)
  - <a id="_TensorDedupeKey.layout"></a>`layout` — [`L316`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L316)
- uses (calls/refs, reference-scoped): [`_TensorLayout`](export.md#_TensorLayout), [`dtype`](export.md#_TensorLayout.dtype), [`shape`](export.md#_TensorLayout.shape), [`storage_offset`](export.md#_TensorLayout.storage_offset), [`stride`](export.md#_TensorLayout.stride)
- used by: [`_process_fx_outputs`](export.md#_process_fx_outputs)

### <a id="_TensorLayout"></a>`_TensorLayout`
- def: [`src/torch_tpu/_internal/export/export.py:255`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L255)
- signature: `class _TensorLayout:`
- members:
  - <a id="_TensorLayout.dtype"></a>`dtype` — [`L256`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L256)
  - <a id="_TensorLayout.shape"></a>`shape` — [`L257`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L257)
  - <a id="_TensorLayout.storage_offset"></a>`storage_offset` — [`L259`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L259)
  - <a id="_TensorLayout.stride"></a>`stride` — [`L258`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L258)
- used by: [`_process_fx_outputs`](export.md#_process_fx_outputs), [`from_tensor`](export.md#_TensorDedupeKey.from_tensor), [`layout`](export.md#_TensorDedupeKey.layout)

## Functions
- <a id="_extract_sample_arguments"></a>`_extract_sample_arguments(exported: torch.export.ExportedProgram)` — [`L62`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L62) — Return a list of sample arguments for the given exported program.
- <a id="_extract_states_from_exported_program"></a>`_extract_states_from_exported_program(exported_model)` — [`L43`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L43) — Return a list of parameters that were lifted during export.
- <a id="_extract_sample_arguments._get_inputs"></a>`_get_inputs(exported)` — [`L82`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L82) — Return placeholders with input metadata.
- <a id="_map_unused_fake_inputs_to_outputs"></a>`_map_unused_fake_inputs_to_outputs(gm: torch.fx.GraphModule)` — [`L262`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L262) — Maps indices of fake inputs that are directly passed through to outputs.
- <a id="_process_fx_outputs"></a>`_process_fx_outputs(gm: torch.fx.GraphModule, outputs: Any, dynamic_outputs: Sequence[bool] | None = None)` — [`L331`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L331) — Removes Nones, maps passthrough values, and dedups outputs.
- <a id="_extract_sample_arguments._to_aval"></a>`_to_aval(arg_meta)` — [`L65`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L65) — Convert from torch type to TPU meta buffer for tracing.
- <a id="enable_tracebacks"></a>`enable_tracebacks(value: bool | None = True)` — [`L417`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L417) — A context manager that overrides whether enabling MLIR tracebacks.
- <a id="exported_to_mlir"></a>`exported_to_mlir(exported: torch.export.ExportedProgram)` — [`L210`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L210) — Converts a `torch.export.ExportedProgram` into its MLIR representation.
- <a id="fx_to_mlir"></a>`fx_to_mlir(module: torch.fx.GraphModule, args: list[torch.Tensor | Any], build_mlir_module: bool = True, use_stablehlo_bounds: bool = False, argument_layouts: list[list[int]] | None = None, dynamic_outputs: Sequence[bool] | None = None, donated_inputs: Sequence[int] | None = None, module_name: str | None = None)` — [`L431`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L431) — Converts an FX graph module to MLIR using TorchTPU's FX-tracing mode.

## Module values
- <a id="EagerMode.EagerMode"></a>`EagerMode` — [`L33`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L33) — documented in [context-states-and-execution-modes](../../../../../concepts/context-states-and-execution-modes.md)
- <a id="__all__"></a>`__all__` — [`L36`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L36)
- <a id="_fx_to_mlir_lock"></a>`_fx_to_mlir_lock` — [`L34`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/export/export.py#L34)

