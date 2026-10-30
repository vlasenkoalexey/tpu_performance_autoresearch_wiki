---
title: 'Module: torchtitan/experiments/graph_trainer/gradient_accumulation.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/gradient_accumulation.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.gradient_accumulation`/
symbols:
  GraphGradientState.create: GraphGradientState#create().
  GraphGradientState: GraphGradientState#
  GraphGradientState.validate_bindings: GraphGradientState#validate_bindings().
  _storage_keys: _storage_keys().
  GraphGradientState.buffers: GraphGradientState#buffers.
  GraphGradientState.validate_parameters: GraphGradientState#validate_parameters().
  GraphGradientState.parameters: GraphGradientState#parameters.
  GraphGradientState.prepare_for_backward: GraphGradientState#prepare_for_backward().
  GraphGradientState.validate_grad_bindings: GraphGradientState#validate_grad_bindings().
  GraphGradientState.graph_state: GraphGradientState#graph_state.
  GraphGradientState.bind_buffers_to_params_grads: GraphGradientState#bind_buffers_to_params_grads().
  GraphGradientState.parameter_fqns: GraphGradientState#parameter_fqns.
  StorageKey: StorageKey.
  GraphGradientState.validate_optimizers: GraphGradientState#validate_optimizers().
  GraphGradientState.parameter_storage_keys: GraphGradientState#parameter_storage_keys.
  GraphGradientState.buffer_storage_keys: GraphGradientState#buffer_storage_keys.
  GraphGradientState._validate_unique_parameters: GraphGradientState#_validate_unique_parameters().
  GraphGradientState._validate_optimizer_params_membership: GraphGradientState#_validate_optimizer_params_membership().
  GraphGradientState._validate_module_grad_contracts: GraphGradientState#_validate_module_grad_contracts().
---
# Module: [`torchtitan/experiments/graph_trainer/gradient_accumulation.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py)

## Classes
### <a id="GraphGradientState"></a>`GraphGradientState`
- def: [`torchtitan/experiments/graph_trainer/gradient_accumulation.py:41`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L41)
- doc: Own persistent, optimizer-visible gradients for traced execution.
- signature: `class GraphGradientState:`
- members:
  - <a id="GraphGradientState.bind_buffers_to_params_grads"></a>`bind_buffers_to_params_grads(self)` — [`L171`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L171) — Bind newly allocated buffers to ``parameter.grad``.
  - <a id="GraphGradientState.create"></a>`create(cls, model: nn.Module, optimizers: Iterable[torch.optim.Optimizer])` — [`L65`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L65)
  - <a id="GraphGradientState.prepare_for_backward"></a>`prepare_for_backward(self)` — [`L182`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L182) — Clear and rebind retained buffers after ``zero_grad(set_to_none=True)``.
  - <a id="GraphGradientState.validate_bindings"></a>`validate_bindings(self)` — [`L229`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L229) — Validate stable optimizer-visible gradient identities.
  - <a id="GraphGradientState.validate_grad_bindings"></a>`validate_grad_bindings(self)` — [`L253`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L253) — Validate that parameter gradients still use trainer-owned buffers.
  - <a id="GraphGradientState.validate_optimizers"></a>`validate_optimizers(self, optimizers: Iterable[torch.optim.Optimizer])` — [`L222`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L222) — Validate that optimizers still own exactly the bound parameters.
  - <a id="GraphGradientState.validate_parameters"></a>`validate_parameters(self, parameters: Sequence[torch.Tensor])` — [`L199`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L199) — Validate that tracing still uses the parameters bound at creation.
  - <a id="GraphGradientState.buffer_storage_keys"></a>`buffer_storage_keys` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L61)
  - <a id="GraphGradientState.buffers"></a>`buffers` — [`L60`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L60)
  - <a id="GraphGradientState.graph_state"></a>`graph_state` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L62)
  - <a id="GraphGradientState.parameter_fqns"></a>`parameter_fqns` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L57)
  - <a id="GraphGradientState.parameter_storage_keys"></a>`parameter_storage_keys` — [`L59`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L59)
  - <a id="GraphGradientState.parameters"></a>`parameters` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L58)
- protocol/private: <a id="GraphGradientState._validate_module_grad_contracts"></a>`_validate_module_grad_contracts`[`L99`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L99), <a id="GraphGradientState._validate_optimizer_params_membership"></a>`_validate_optimizer_params_membership`[`L150`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L150), <a id="GraphGradientState._validate_unique_parameters"></a>`_validate_unique_parameters`[`L114`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L114)
- uses (calls/refs, reference-scoped): [`_storage_keys`](gradient_accumulation.md#_storage_keys), [`StorageKey`](gradient_accumulation.md#StorageKey)
- used by: [`_make_fx_forward_backward_step`](trainer.md#GraphTrainer._make_fx_forward_backward_step), [`_graph_gradient_state`](trainer.md#GraphTrainer._graph_gradient_state), [`train_step`](trainer.md#GraphTrainer.train_step), [`_ensure_graph_gradient_state`](trainer.md#GraphTrainer._ensure_graph_gradient_state), [`_get_trainable_parameters`](trainer.md#GraphTrainer._get_trainable_parameters)  (11 test-only)

## Functions
- <a id="_storage_keys"></a>`_storage_keys(tensor: torch.Tensor)` — [`L22`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L22)

## Module values
- <a id="StorageKey"></a>`StorageKey` — [`L19`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/gradient_accumulation.py#L19)

