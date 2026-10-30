---
title: 'Module: src/torch_tpu/_internal/utils/utils.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/utils/utils.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.utils.utils`/
symbols:
  ActivationTracer._register_hooks_recursive: ActivationTracer#_register_hooks_recursive().
  ActivationTracer._idx: ActivationTracer#_idx.
  ActivationTracer.__init__: ActivationTracer#__init__().
  format_model: format_model().
  ActivationTracer.__enter__: ActivationTracer#__enter__().
  Event.Event: Event.Event.
  get_primary_tensor_output: get_primary_tensor_output().
  _InputArgumentMetadata.__str__: _InputArgumentMetadata#__str__().
  OpTracer.ops_log: OpTracer#ops_log.
  ActivationTracer._hook_handles: ActivationTracer#_hook_handles.
  ActivationTracer._forward_pre_hook: ActivationTracer#_forward_pre_hook().
  ActivationTracer._forward_hook: ActivationTracer#_forward_hook().
  ActivationTracer._backward_pre_hook: ActivationTracer#_backward_pre_hook().
  ActivationTracer._backward_hook: ActivationTracer#_backward_hook().
  ActivationTracer.forward_pre_log: ActivationTracer#forward_pre_log.
  ActivationTracer.forward_log: ActivationTracer#forward_log.
  ActivationTracer.backward_pre_log: ActivationTracer#backward_pre_log.
  ActivationTracer.backward_log: ActivationTracer#backward_log.
  InputMetadata.__init__: InputMetadata#__init__().
  InputMetadata._inputs: InputMetadata#_inputs.
  OpTracer._pformat: OpTracer#_pformat().
  _InputArgumentMetadata._arg: _InputArgumentMetadata#_arg.
  _InputArgumentMetadata.__repr__: _InputArgumentMetadata#__repr__().
  InputMetadata.__str__: InputMetadata#__str__().
  OpTracer.__torch_dispatch__: OpTracer#__torch_dispatch__().
  OpTracer.num_atens: OpTracer#num_atens().
  ActivationTracer.__exit__: ActivationTracer#__exit__().
  libtpu_version: libtpu_version().
  get_torch_version: get_torch_version().
  parse_version: parse_version().
  EagerMode.EagerMode: EagerMode.EagerMode.
  model_memory: model_memory().
  get_tensor_summary: get_tensor_summary().
  _InputArgumentMetadata: _InputArgumentMetadata#
  ActivationTracer._model: ActivationTracer#_model.
  OpTracer: OpTracer#
  open_output: open_output().
  format_tensor: format_tensor().
  _InputArgumentMetadata.__init__: _InputArgumentMetadata#__init__().
  InputMetadata: InputMetadata#
  OpTracer.__enter__: OpTracer#__enter__().
  ActivationTracer: ActivationTracer#
---
# Module: [`src/torch_tpu/_internal/utils/utils.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py)

## Classes
### <a id="ActivationTracer"></a>`ActivationTracer`  ·  implements/extends ContextDecorator
- def: [`src/torch_tpu/_internal/utils/utils.py:400`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L400)
- doc: Traces activations in a model's forward and backward pass.
- signature: `class ActivationTracer(contextlib.ContextDecorator):`
- members:
  - <a id="ActivationTracer._backward_hook"></a>`_backward_hook(self, module: torch.nn.Module, grad_input: tuple[torch.Tensor, ...], grad_output: tuple[torch.Tensor, ...], depth: int)` — [`L521`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L521) — Logs the backward pass of a module. Called after a backward pass. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
  - <a id="ActivationTracer._backward_pre_hook"></a>`_backward_pre_hook(self, module: torch.nn.Module, grad_output: tuple[torch.Tensor, ...], depth: int)` — [`L496`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L496) — Logs the backward pass of a module. Called before a backward pass. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
  - <a id="ActivationTracer._forward_hook"></a>`_forward_hook(self, module: torch.nn.Module, args: tuple[Any, ...], kwargs: dict[str, Any], output: Any, depth: int)` — [`L465`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L465) — Logs the forward pass of a module. Called after a forward pass. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
  - <a id="ActivationTracer._forward_pre_hook"></a>`_forward_pre_hook(self, module: torch.nn.Module, args: tuple[Any, ...], kwargs: dict[str, Any], depth: int)` — [`L437`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L437) — Logs the forward pass of a module. Called before a forward pass. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
  - <a id="ActivationTracer._register_hooks_recursive"></a>`_register_hooks_recursive(self, module: torch.nn.Module, depth: int)` — [`L547`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L547) — Registers hooks on the current module and recursively on its children. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
  - <a id="ActivationTracer.backward_log"></a>`backward_log` — [`L425`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L425) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
  - <a id="ActivationTracer.backward_pre_log"></a>`backward_pre_log` — [`L424`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L424) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
  - <a id="ActivationTracer.forward_log"></a>`forward_log` — [`L423`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L423) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
  - <a id="ActivationTracer.forward_pre_log"></a>`forward_pre_log` — [`L422`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L422) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- protocol/private: <a id="ActivationTracer.__enter__"></a>`__enter__`[`L580`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L580), <a id="ActivationTracer.__exit__"></a>`__exit__`[`L590`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L590), <a id="ActivationTracer.__init__"></a>`__init__`[`L427`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L427), <a id="ActivationTracer._hook_handles"></a>`_hook_handles`[`L429`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L429), <a id="ActivationTracer._idx"></a>`_idx`[`L585`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L585), <a id="ActivationTracer._model"></a>`_model`[`L428`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L428)
- uses (calls/refs, reference-scoped): [`Event`](utils.md#Event.Event)

### <a id="InputMetadata"></a>`InputMetadata`
- def: [`src/torch_tpu/_internal/utils/utils.py:308`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L308)
- doc: A class to log call inputs without requiring access to their data.
- signature: `class InputMetadata:`
- protocol/private: <a id="InputMetadata.__init__"></a>`__init__`[`L316`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L316), <a id="InputMetadata.__str__"></a>`__str__`[`L323`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L323), <a id="InputMetadata._inputs"></a>`_inputs`[`L317`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L317)
- uses (calls/refs, reference-scoped): [`_InputArgumentMetadata`](utils.md#_InputArgumentMetadata)

### <a id="OpTracer"></a>`OpTracer`
- def: [`src/torch_tpu/_internal/utils/utils.py:327`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L327)
- members:
  - <a id="OpTracer._pformat"></a>`_pformat(self)` — [`L380`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L380) — Pretty-formats the collected data from OpTracer.
  - <a id="OpTracer.num_atens"></a>`num_atens(self)` — [`L375`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L375)
  - <a id="OpTracer.ops_log"></a>`ops_log` — [`L365`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L365) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- protocol/private: <a id="OpTracer.__enter__"></a>`__enter__`[`L363`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L363), <a id="OpTracer.__torch_dispatch__"></a>`__torch_dispatch__`[`L368`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L368)
- used by: [`format_model`](utils.md#format_model)

### <a id="_InputArgumentMetadata"></a>`_InputArgumentMetadata`
- def: [`src/torch_tpu/_internal/utils/utils.py:289`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L289)
- doc: A class to log a single argument's metadata.
- signature: `class _InputArgumentMetadata:`
- protocol/private: <a id="_InputArgumentMetadata.__init__"></a>`__init__`[`L296`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L296), <a id="_InputArgumentMetadata.__repr__"></a>`__repr__`[`L304`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L304), <a id="_InputArgumentMetadata.__str__"></a>`__str__`[`L299`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L299), <a id="_InputArgumentMetadata._arg"></a>`_arg`[`L297`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L297)
- uses (calls/refs, reference-scoped): [`get_tensor_summary`](utils.md#get_tensor_summary)
- used by: [`__init__`](utils.md#InputMetadata.__init__)

## Functions
- <a id="format_model"></a>`format_model(model: torch.nn.Module | Callable[..., Any], *input_tensors: torch.Tensor | tuple[torch.Tensor, ...], params: bool = False, pt: bool = False, aten: bool = False, shlo: bool = False)` — [`L91`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L91) — Formats a model or tensor function in various ways. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="format_tensor"></a>`format_tensor(tensor: torch.Tensor, desc: str = "", data: bool = False)` — [`L171`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L171) — Formats the most common properties of a PyTorch tensor.
- <a id="get_primary_tensor_output"></a>`get_primary_tensor_output(out: Any)` — [`L645`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L645) — Recursively extracts a primary output torch.Tensor from model output objects. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="get_tensor_summary"></a>`get_tensor_summary(tensor: torch.Tensor, data: bool = True)` — [`L219`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L219) — Returns a one-line, compact summary of a PyTorch tensor.
- <a id="get_torch_version"></a>`get_torch_version()` — [`L640`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L640) — Returns the parsed version tuple of torch.
- <a id="libtpu_version"></a>`libtpu_version()` — [`L628`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L628) — Returns the parsed version tuple of libtpu in OSS, or None in google3.
- <a id="model_memory"></a>`model_memory(model: torch.nn.Module, dtype: torch.dtype = torch.float32)` — [`L36`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L36) — Estimate the physical memory requirements for a model.
- <a id="open_output"></a>`open_output(filepath: str | None, mode: str = "w", default: TextIO = sys.stdout)` — [`L68`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L68) — Opens an output file if filepath is provided.
- <a id="parse_version"></a>`parse_version(version: str)` — [`L603`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L603) — Parses the leading numeric components of a version string into a tuple.

## Module values
- <a id="EagerMode.EagerMode"></a>`EagerMode` — [`L33`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L33) — documented in [context-states-and-execution-modes](../../../../../concepts/context-states-and-execution-modes.md)
- <a id="Event.Event"></a>`Event` — [`L397`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/utils.py#L397) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)

