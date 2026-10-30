---
title: 'Module: src/torch_tpu/_internal/optimizers/adamw.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/optimizers/adamw.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.optimizers.adamw`/
symbols:
  AdamW.step: AdamW#step().
  ReferenceAdamW.step: ReferenceAdamW#step().
  _AdamWBase: _AdamWBase#
  _adam_param_group_flatten: _adam_param_group_flatten().
  _adam_param_group_unflatten: _adam_param_group_unflatten().
  _AdamWBase.init_param_group: _AdamWBase#init_param_group().
  ReferenceAdamW._reference_adamw_update: ReferenceAdamW#_reference_adamw_update().
  _AdamWBase.ParamGroup: _AdamWBase#ParamGroup#
  _AdamWBase.step: _AdamWBase#step().
  _AdamWBase.ParamGroup.params: _AdamWBase#ParamGroup#params.
  _AdamWBase.ParamGroup.opt_state_m: _AdamWBase#ParamGroup#opt_state_m.
  _AdamWBase.ParamGroup.opt_state_v: _AdamWBase#ParamGroup#opt_state_v.
  _AdamWBase.ParamGroup.opt_steps: _AdamWBase#ParamGroup#opt_steps.
  _AdamWBase._beta1: _AdamWBase#_beta1.
  _AdamWBase._beta2: _AdamWBase#_beta2.
  _AdamWBase.__init__: _AdamWBase#__init__().
  ReferenceAdamW: ReferenceAdamW#
  AdamW: AdamW#
  AdamW.__init__: AdamW#__init__().
  _AdamWBase._eps: _AdamWBase#_eps.
  _AdamWBase._use_bfloat16_moments: _AdamWBase#_use_bfloat16_moments.
  AdamW._amsgrad: AdamW#_amsgrad.
  AdamW._maximize: AdamW#_maximize.
  AdamW._foreach: AdamW#_foreach.
  AdamW._capturable: AdamW#_capturable.
  AdamW._differentiable: AdamW#_differentiable.
  AdamW._fused: AdamW#_fused.
  AdamW._grad_scale: AdamW#_grad_scale.
  AdamW._found_inf: AdamW#_found_inf.
  __all__: __all__.
  _AdamWBase._HYPERPARAMETER_NAMES: _AdamWBase#_HYPERPARAMETER_NAMES.
  AdamW._HYPERPARAMETER_NAMES: AdamW#_HYPERPARAMETER_NAMES.
---
# Module: [`src/torch_tpu/_internal/optimizers/adamw.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py)

## Classes
### <a id="AdamW"></a>`AdamW`  ·  implements/extends _AdamWBase
- def: [`src/torch_tpu/_internal/optimizers/adamw.py:192`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L192)
- doc: Torch AdamW implementation calling torch.optim.adamw.adamw directly.
- signature: `class AdamW(_AdamWBase):`
- members:
  - <a id="AdamW.step"></a>`step(self, param_group: _AdamWBase.ParamGroup, grads: dict[str, torch.Tensor])` — [`L249`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L249) — Torch AdamW step calling torch.optim.adamw.adamw directly. — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- protocol/private: <a id="AdamW._HYPERPARAMETER_NAMES"></a>`_HYPERPARAMETER_NAMES`[`L195`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L195), <a id="AdamW.__init__"></a>`__init__`[`L212`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L212), <a id="AdamW._amsgrad"></a>`_amsgrad`[`L237`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L237), <a id="AdamW._capturable"></a>`_capturable`[`L240`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L240), <a id="AdamW._differentiable"></a>`_differentiable`[`L241`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L241), <a id="AdamW._foreach"></a>`_foreach`[`L239`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L239), <a id="AdamW._found_inf"></a>`_found_inf`[`L244`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L244), <a id="AdamW._fused"></a>`_fused`[`L242`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L242), <a id="AdamW._grad_scale"></a>`_grad_scale`[`L243`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L243), <a id="AdamW._maximize"></a>`_maximize`[`L238`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L238)
- uses (calls/refs, reference-scoped): [`_AdamWBase`](adamw.md#_AdamWBase), [`ParamGroup`](adamw.md#_AdamWBase.ParamGroup), [`_lr`](optim.md#Optimizer._lr), [`_weight_decay`](optim.md#Optimizer._weight_decay), [`params`](adamw.md#_AdamWBase.ParamGroup.params), [`opt_state_m`](adamw.md#_AdamWBase.ParamGroup.opt_state_m), [`opt_state_v`](adamw.md#_AdamWBase.ParamGroup.opt_state_v), [`opt_steps`](adamw.md#_AdamWBase.ParamGroup.opt_steps), [`_beta1`](adamw.md#_AdamWBase._beta1), [`_beta2`](adamw.md#_AdamWBase._beta2), [`__init__`](adamw.md#_AdamWBase.__init__), [`_eps`](adamw.md#_AdamWBase._eps)
- used by: [`_AdamWBase`](adamw.md#_AdamWBase), [`step`](adamw.md#_AdamWBase.step), [`AdamW`](single_trace_trainer.md#AdamW)

### <a id="ReferenceAdamW"></a>`ReferenceAdamW`  ·  implements/extends _AdamWBase
- def: [`src/torch_tpu/_internal/optimizers/adamw.py:136`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L136) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- doc: Reference pure PyTorch implementation of AdamW.
- signature: `class ReferenceAdamW(_AdamWBase):`
- members:
  - <a id="ReferenceAdamW._reference_adamw_update"></a>`_reference_adamw_update(self, param: torch.Tensor, grad: torch.Tensor, m: torch.Tensor, v: torch.Tensor, step: float | torch.Tensor = 1)` — [`L143`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L143) — Performs an in-place reference AdamW update on param, m, and v. — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
  - <a id="ReferenceAdamW.step"></a>`step(self, param_group: _AdamWBase.ParamGroup, grads: dict[str, torch.Tensor])` — [`L172`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L172) — Reference pure PyTorch implementation of AdamW step. — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- uses (calls/refs, reference-scoped): [`_AdamWBase`](adamw.md#_AdamWBase), [`ParamGroup`](adamw.md#_AdamWBase.ParamGroup), [`_lr`](optim.md#Optimizer._lr), [`_weight_decay`](optim.md#Optimizer._weight_decay), [`params`](adamw.md#_AdamWBase.ParamGroup.params), [`opt_state_m`](adamw.md#_AdamWBase.ParamGroup.opt_state_m), [`opt_state_v`](adamw.md#_AdamWBase.ParamGroup.opt_state_v), [`opt_steps`](adamw.md#_AdamWBase.ParamGroup.opt_steps), [`_beta1`](adamw.md#_AdamWBase._beta1), [`_beta2`](adamw.md#_AdamWBase._beta2), [`_eps`](adamw.md#_AdamWBase._eps)
- used by: [`_AdamWBase`](adamw.md#_AdamWBase), [`step`](adamw.md#_AdamWBase.step), [`ReferenceAdamW`](single_trace_trainer.md#ReferenceAdamW)

### <a id="_AdamWBase"></a>`_AdamWBase`  ·  implements/extends Optimizer
- def: [`src/torch_tpu/_internal/optimizers/adamw.py:33`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L33) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- doc: Internal base class for AdamW optimizer variants with nested ParamGroup.
- signature: `class _AdamWBase(_optim.Optimizer):`
- members:
  - <a id="_AdamWBase.init_param_group"></a>`init_param_group(self, params: dict[str, torch.Tensor] | torch.nn.Module)` — [`L80`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L80) — Initializes Adam optimizer state from model parameters or nn.Module. — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
  - <a id="_AdamWBase.step"></a>`step(self, param_group: ParamGroup, grads: dict[str, torch.Tensor])` — [`L129`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L129) — Performs optimizer step on param_group given grads and returns updated ParamGroup.
- protocol/private: <a id="_AdamWBase._HYPERPARAMETER_NAMES"></a>`_HYPERPARAMETER_NAMES`[`L52`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L52), <a id="_AdamWBase.__init__"></a>`__init__`[`L61`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L61), <a id="_AdamWBase._beta1"></a>`_beta1`[`L71`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L71), <a id="_AdamWBase._beta2"></a>`_beta2`[`L72`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L72), <a id="_AdamWBase._eps"></a>`_eps`[`L73`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L73), <a id="_AdamWBase._use_bfloat16_moments"></a>`_use_bfloat16_moments`[`L74`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L74)
- uses (calls/refs, reference-scoped): [`step`](adamw.md#AdamW.step), [`step`](adamw.md#ReferenceAdamW.step), [`ParamGroup`](adamw.md#_AdamWBase.ParamGroup), [`Optimizer`](optim.md#Optimizer), [`params`](adamw.md#_AdamWBase.ParamGroup.params), [`opt_state_m`](adamw.md#_AdamWBase.ParamGroup.opt_state_m), [`opt_state_v`](adamw.md#_AdamWBase.ParamGroup.opt_state_v), [`opt_steps`](adamw.md#_AdamWBase.ParamGroup.opt_steps), [`AdamW`](adamw.md#AdamW), [`ReferenceAdamW`](adamw.md#ReferenceAdamW), [`__init__`](optim.md#Optimizer.__init__)
- used by: [`step`](adamw.md#AdamW.step), [`step`](adamw.md#ReferenceAdamW.step), [`_adam_param_group_flatten`](adamw.md#_adam_param_group_flatten), [`_adam_param_group_unflatten`](adamw.md#_adam_param_group_unflatten), [`_reference_adamw_update`](adamw.md#ReferenceAdamW._reference_adamw_update), [`Optimizer`](optim.md#Optimizer), [`step`](optim.md#Optimizer.step), [`init_param_group`](optim.md#Optimizer.init_param_group), [`AdamW`](adamw.md#AdamW), [`ReferenceAdamW`](adamw.md#ReferenceAdamW), [`__init__`](adamw.md#AdamW.__init__)

### <a id="_AdamWBase.ParamGroup"></a>`_AdamWBase.ParamGroup`
- def: [`src/torch_tpu/_internal/optimizers/adamw.py:40`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L40) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- doc: Holds model parameters and Adam optimizer states (m, v, steps).
- signature: `class ParamGroup:`
- members:
  - <a id="_AdamWBase.ParamGroup.opt_state_m"></a>`opt_state_m` — [`L44`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L44) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
  - <a id="_AdamWBase.ParamGroup.opt_state_v"></a>`opt_state_v` — [`L47`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L47) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
  - <a id="_AdamWBase.ParamGroup.opt_steps"></a>`opt_steps` — [`L50`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L50) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
  - <a id="_AdamWBase.ParamGroup.params"></a>`params` — [`L43`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L43) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- used by: [`step`](adamw.md#AdamW.step), [`step`](adamw.md#ReferenceAdamW.step), [`_adam_param_group_flatten`](adamw.md#_adam_param_group_flatten), [`_adam_param_group_unflatten`](adamw.md#_adam_param_group_unflatten), [`init_param_group`](adamw.md#_AdamWBase.init_param_group), [`step`](adamw.md#_AdamWBase.step)

## Functions
- <a id="_adam_param_group_flatten"></a>`_adam_param_group_flatten(group: _AdamWBase.ParamGroup)` — [`L284`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L284) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- <a id="_adam_param_group_unflatten"></a>`_adam_param_group_unflatten(children, _context)` — [`L294`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L294) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)

## Module values
- <a id="__all__"></a>`__all__` — [`L27`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/adamw.py#L27)

