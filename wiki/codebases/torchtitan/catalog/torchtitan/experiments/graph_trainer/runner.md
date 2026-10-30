---
title: 'Module: torchtitan/experiments/graph_trainer/runner.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/runner.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.runner`/
symbols:
  GraphRunner.validate_state: GraphRunner#validate_state().
  GraphRunner.__call__: GraphRunner#__call__().
  _flatten_state_inputs: _flatten_state_inputs().
  GraphRunner: GraphRunner#
  _resolve_state_tensors: _resolve_state_tensors().
  GraphRunner._traced_result: GraphRunner#_traced_result.
  GraphRunner._validate_runtime_meshes: GraphRunner#_validate_runtime_meshes().
  GraphRunner._state_signatures: GraphRunner#_state_signatures.
  GraphRunner._flat_state_inputs: GraphRunner#_flat_state_inputs.
  GraphRunner._runtime_meshes: GraphRunner#_runtime_meshes.
  GraphRunner._validate_user_inputs: GraphRunner#_validate_user_inputs.
  GraphRunner.__init__: GraphRunner#__init__().
  _state_input_signature: _state_input_signature().
  GraphRunner._state_tensors: GraphRunner#_state_tensors.
  _flat_input_metadata: _flat_input_metadata().
  GraphRunner._module: GraphRunner#_module.
  GraphRunner._graph_state: GraphRunner#_graph_state.
  __all__: __all__.
---
# Module: [`torchtitan/experiments/graph_trainer/runner.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py)

## Classes
### <a id="GraphRunner"></a>`GraphRunner`
- def: [`torchtitan/experiments/graph_trainer/runner.py:123`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L123) — documented in [graph-trainer](../../../../concepts/graph-trainer.md)
- doc: Run a traced graph using state inputs prepared once at initialization.
- signature: `class GraphRunner:`
- members:
  - <a id="GraphRunner.__call__"></a>`__call__(self, *args: Any, **kwargs: Any)` — [`L248`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L248) — Execute the graph with dynamic inputs and reconstruct its outputs.
  - <a id="GraphRunner._validate_runtime_meshes"></a>`_validate_runtime_meshes(self)` — [`L201`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L201) — Validate runtime meshes against the inputs used to load the graph.
  - <a id="GraphRunner.validate_state"></a>`validate_state(self)` — [`L215`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L215) — Fail if bound state objects, subclass leaves, or storage changed.
- protocol/private: <a id="GraphRunner.__init__"></a>`__init__`[`L162`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L162), <a id="GraphRunner._flat_state_inputs"></a>`_flat_state_inputs`[`L192`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L192), <a id="GraphRunner._graph_state"></a>`_graph_state`[`L176`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L176), <a id="GraphRunner._module"></a>`_module`[`L175`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L175), <a id="GraphRunner._runtime_meshes"></a>`_runtime_meshes`[`L177`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L177), <a id="GraphRunner._state_signatures"></a>`_state_signatures`[`L196`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L196), <a id="GraphRunner._state_tensors"></a>`_state_tensors`[`L187`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L187), <a id="GraphRunner._traced_result"></a>`_traced_result`[`L174`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L174), <a id="GraphRunner._validate_user_inputs"></a>`_validate_user_inputs`[`L178`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L178)
- uses (calls/refs, reference-scoped): [`gm`](make_fx_tracer.md#TracedResult.gm), [`example_inputs`](make_fx_tracer.md#TracedResult.example_inputs), [`TracedResult`](make_fx_tracer.md#TracedResult), [`num_static_inputs`](make_fx_tracer.md#TracedResult.num_static_inputs), [`_flatten_state_inputs`](runner.md#_flatten_state_inputs), [`_wrap_subclasses`](make_fx_tracer.md#_wrap_subclasses), [`_unwrap_subclasses`](make_fx_tracer.md#_unwrap_subclasses), [`_resolve_state_tensors`](runner.md#_resolve_state_tensors), [`output_subclass_layouts`](make_fx_tracer.md#TracedResult.output_subclass_layouts), [`num_flat_outputs`](make_fx_tracer.md#TracedResult.num_flat_outputs), [`output_spec`](make_fx_tracer.md#TracedResult.output_spec), [`user_inputs_spec`](make_fx_tracer.md#TracedResult.user_inputs_spec), [`num_runtime_mesh_inputs`](make_fx_tracer.md#TracedResult.num_runtime_mesh_inputs), [`_state_input_signature`](runner.md#_state_input_signature), [`num_optimizer_state_inputs`](make_fx_tracer.md#TracedResult.num_optimizer_state_inputs)
- used by: [`_make_fx_forward_backward_step`](trainer.md#GraphTrainer._make_fx_forward_backward_step), [`_graph_runner`](trainer.md#GraphTrainer._graph_runner)  (10 test-only)

## Functions
- <a id="_flat_input_metadata"></a>`_flat_input_metadata(value: Any)` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L53) — Describe input properties that must remain stable after binding.
- <a id="_flatten_state_inputs"></a>`_flatten_state_inputs(traced_result: TracedResult, state_tensors: tuple[torch.Tensor, ...])` — [`L83`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L83) — Flatten state tensors and validate compatibility with the traced inputs.
- <a id="_resolve_state_tensors"></a>`_resolve_state_tensors(traced_result: TracedResult, module: nn.Module | None, graph_state: dict[str, torch.Tensor] | None)` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L29) — Resolve persistent state tensors in their trace-time input order.
- <a id="_state_input_signature"></a>`_state_input_signature(value: Any)` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L70) — Combine stable input metadata with its storage identity when available.

## Module values
- <a id="__all__"></a>`__all__` — [`L26`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/runner.py#L26)

