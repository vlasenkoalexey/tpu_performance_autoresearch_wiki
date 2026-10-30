---
title: 'Module: src/torch_tpu/_internal/optimizers/sgd.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/optimizers/sgd.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.optimizers.sgd`/
symbols:
  Sgd.step: Sgd#step().
  _SgdBase: _SgdBase#
  ReferenceSgd.step: ReferenceSgd#step().
  ReferenceSgd._reference_sgd_update: ReferenceSgd#_reference_sgd_update().
  _sgd_param_group_flatten: _sgd_param_group_flatten().
  _sgd_param_group_unflatten: _sgd_param_group_unflatten().
  _SgdBase.init_param_group: _SgdBase#init_param_group().
  _SgdBase.ParamGroup: _SgdBase#ParamGroup#
  _SgdBase.step: _SgdBase#step().
  _SgdBase.ParamGroup.params: _SgdBase#ParamGroup#params.
  _SgdBase._momentum: _SgdBase#_momentum.
  _SgdBase.ParamGroup.opt_state_m: _SgdBase#ParamGroup#opt_state_m.
  _SgdBase.ParamGroup.opt_steps: _SgdBase#ParamGroup#opt_steps.
  _SgdBase.__init__: _SgdBase#__init__().
  ReferenceSgd: ReferenceSgd#
  Sgd: Sgd#
  Sgd.__init__: Sgd#__init__().
  _SgdBase._dampening: _SgdBase#_dampening.
  _SgdBase._nesterov: _SgdBase#_nesterov.
  Sgd._maximize: Sgd#_maximize.
  Sgd._foreach: Sgd#_foreach.
  Sgd._fused: Sgd#_fused.
  Sgd._grad_scale: Sgd#_grad_scale.
  Sgd._found_inf: Sgd#_found_inf.
  Sgd._has_sparse_grad: Sgd#_has_sparse_grad.
  __all__: __all__.
  _SgdBase._HYPERPARAMETER_NAMES: _SgdBase#_HYPERPARAMETER_NAMES.
  Sgd._HYPERPARAMETER_NAMES: Sgd#_HYPERPARAMETER_NAMES.
---
# Module: [`src/torch_tpu/_internal/optimizers/sgd.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py)

## Classes
### <a id="ReferenceSgd"></a>`ReferenceSgd`  ·  implements/extends _SgdBase
- def: [`src/torch_tpu/_internal/optimizers/sgd.py:122`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L122)
- doc: Reference pure PyTorch implementation of SGD.
- signature: `class ReferenceSgd(_SgdBase):`
- members:
  - <a id="ReferenceSgd._reference_sgd_update"></a>`_reference_sgd_update(self, param: torch.Tensor, grad: torch.Tensor, m: torch.Tensor | None = None, step: float | torch.Tensor = 1)` — [`L129`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L129) — Performs an in-place reference SGD update on param and momentum buffer m. — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
  - <a id="ReferenceSgd.step"></a>`step(self, param_group: _SgdBase.ParamGroup, grads: dict[str, torch.Tensor])` — [`L155`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L155) — Reference pure PyTorch implementation of SGD step. — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- uses (calls/refs, reference-scoped): [`_SgdBase`](sgd.md#_SgdBase), [`ParamGroup`](sgd.md#_SgdBase.ParamGroup), [`_lr`](optim.md#Optimizer._lr), [`_weight_decay`](optim.md#Optimizer._weight_decay), [`params`](sgd.md#_SgdBase.ParamGroup.params), [`_momentum`](sgd.md#_SgdBase._momentum), [`opt_state_m`](sgd.md#_SgdBase.ParamGroup.opt_state_m), [`opt_steps`](sgd.md#_SgdBase.ParamGroup.opt_steps), [`_dampening`](sgd.md#_SgdBase._dampening), [`_nesterov`](sgd.md#_SgdBase._nesterov)
- used by: [`_SgdBase`](sgd.md#_SgdBase), [`step`](sgd.md#_SgdBase.step), [`ReferenceSgd`](single_trace_trainer.md#ReferenceSgd)

### <a id="Sgd"></a>`Sgd`  ·  implements/extends _SgdBase
- def: [`src/torch_tpu/_internal/optimizers/sgd.py:175`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L175)
- doc: Torch SGD implementation calling torch.optim.sgd.sgd directly.
- signature: `class Sgd(_SgdBase):`
- members:
  - <a id="Sgd.step"></a>`step(self, param_group: _SgdBase.ParamGroup, grads: dict[str, torch.Tensor])` — [`L223`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L223) — Torch SGD step calling torch.optim.sgd.sgd directly. — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- protocol/private: <a id="Sgd._HYPERPARAMETER_NAMES"></a>`_HYPERPARAMETER_NAMES`[`L178`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L178), <a id="Sgd.__init__"></a>`__init__`[`L192`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L192), <a id="Sgd._foreach"></a>`_foreach`[`L214`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L214), <a id="Sgd._found_inf"></a>`_found_inf`[`L217`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L217), <a id="Sgd._fused"></a>`_fused`[`L215`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L215), <a id="Sgd._grad_scale"></a>`_grad_scale`[`L216`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L216), <a id="Sgd._has_sparse_grad"></a>`_has_sparse_grad`[`L218`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L218), <a id="Sgd._maximize"></a>`_maximize`[`L213`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L213)
- uses (calls/refs, reference-scoped): [`_SgdBase`](sgd.md#_SgdBase), [`ParamGroup`](sgd.md#_SgdBase.ParamGroup), [`_lr`](optim.md#Optimizer._lr), [`_weight_decay`](optim.md#Optimizer._weight_decay), [`params`](sgd.md#_SgdBase.ParamGroup.params), [`_momentum`](sgd.md#_SgdBase._momentum), [`opt_state_m`](sgd.md#_SgdBase.ParamGroup.opt_state_m), [`opt_steps`](sgd.md#_SgdBase.ParamGroup.opt_steps), [`__init__`](sgd.md#_SgdBase.__init__), [`_dampening`](sgd.md#_SgdBase._dampening), [`_nesterov`](sgd.md#_SgdBase._nesterov)
- used by: [`_SgdBase`](sgd.md#_SgdBase), [`step`](sgd.md#_SgdBase.step), [`Sgd`](single_trace_trainer.md#Sgd)

### <a id="_SgdBase"></a>`_SgdBase`  ·  implements/extends Optimizer
- def: [`src/torch_tpu/_internal/optimizers/sgd.py:33`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L33) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- doc: Internal base class for SGD optimizer variants with nested ParamGroup.
- signature: `class _SgdBase(_optim.Optimizer):`
- members:
  - <a id="_SgdBase.init_param_group"></a>`init_param_group(self, params: dict[str, torch.Tensor] | torch.nn.Module)` — [`L74`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L74) — Initializes SGD optimizer state from model parameters or nn.Module. — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
  - <a id="_SgdBase.step"></a>`step(self, param_group: ParamGroup, grads: dict[str, torch.Tensor])` — [`L115`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L115) — Performs optimizer step on param_group given grads and returns updated ParamGroup.
- protocol/private: <a id="_SgdBase._HYPERPARAMETER_NAMES"></a>`_HYPERPARAMETER_NAMES`[`L49`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L49), <a id="_SgdBase.__init__"></a>`__init__`[`L57`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L57), <a id="_SgdBase._dampening"></a>`_dampening`[`L67`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L67), <a id="_SgdBase._momentum"></a>`_momentum`[`L66`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L66), <a id="_SgdBase._nesterov"></a>`_nesterov`[`L68`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L68)
- uses (calls/refs, reference-scoped): [`step`](sgd.md#Sgd.step), [`step`](sgd.md#ReferenceSgd.step), [`ParamGroup`](sgd.md#_SgdBase.ParamGroup), [`Optimizer`](optim.md#Optimizer), [`params`](sgd.md#_SgdBase.ParamGroup.params), [`opt_state_m`](sgd.md#_SgdBase.ParamGroup.opt_state_m), [`opt_steps`](sgd.md#_SgdBase.ParamGroup.opt_steps), [`ReferenceSgd`](sgd.md#ReferenceSgd), [`Sgd`](sgd.md#Sgd), [`__init__`](optim.md#Optimizer.__init__)
- used by: [`step`](sgd.md#Sgd.step), [`step`](sgd.md#ReferenceSgd.step), [`_reference_sgd_update`](sgd.md#ReferenceSgd._reference_sgd_update), [`_sgd_param_group_flatten`](sgd.md#_sgd_param_group_flatten), [`_sgd_param_group_unflatten`](sgd.md#_sgd_param_group_unflatten), [`Optimizer`](optim.md#Optimizer), [`step`](optim.md#Optimizer.step), [`init_param_group`](optim.md#Optimizer.init_param_group), [`ReferenceSgd`](sgd.md#ReferenceSgd), [`Sgd`](sgd.md#Sgd), [`__init__`](sgd.md#Sgd.__init__)

### <a id="_SgdBase.ParamGroup"></a>`_SgdBase.ParamGroup`
- def: [`src/torch_tpu/_internal/optimizers/sgd.py:40`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L40) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- doc: Holds model parameters and SGD optimizer states (m, steps).
- signature: `class ParamGroup:`
- members:
  - <a id="_SgdBase.ParamGroup.opt_state_m"></a>`opt_state_m` — [`L44`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L44) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
  - <a id="_SgdBase.ParamGroup.opt_steps"></a>`opt_steps` — [`L47`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L47) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
  - <a id="_SgdBase.ParamGroup.params"></a>`params` — [`L43`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L43) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- used by: [`step`](sgd.md#Sgd.step), [`step`](sgd.md#ReferenceSgd.step), [`_sgd_param_group_flatten`](sgd.md#_sgd_param_group_flatten), [`_sgd_param_group_unflatten`](sgd.md#_sgd_param_group_unflatten), [`init_param_group`](sgd.md#_SgdBase.init_param_group), [`step`](sgd.md#_SgdBase.step)

## Functions
- <a id="_sgd_param_group_flatten"></a>`_sgd_param_group_flatten(group: _SgdBase.ParamGroup)` — [`L258`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L258)
- <a id="_sgd_param_group_unflatten"></a>`_sgd_param_group_unflatten(children, _context)` — [`L267`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L267)

## Module values
- <a id="__all__"></a>`__all__` — [`L27`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/sgd.py#L27)

