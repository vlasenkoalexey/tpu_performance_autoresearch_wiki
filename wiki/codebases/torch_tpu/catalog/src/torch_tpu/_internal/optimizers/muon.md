---
title: 'Module: src/torch_tpu/_internal/optimizers/muon.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/optimizers/muon.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.optimizers.muon`/
symbols:
  Muon.step: Muon#step().
  ReferenceMuon._reference_muon_update: ReferenceMuon#_reference_muon_update().
  _MuonBase: _MuonBase#
  _MuonBase.__init__: _MuonBase#__init__().
  ReferenceMuon.step: ReferenceMuon#step().
  Muon.__init__: Muon#__init__().
  _muon_param_group_flatten: _muon_param_group_flatten().
  _muon_param_group_unflatten: _muon_param_group_unflatten().
  _MuonBase.init_param_group: _MuonBase#init_param_group().
  _MuonBase.ParamGroup: _MuonBase#ParamGroup#
  _MuonBase.step: _MuonBase#step().
  _MuonBase.ParamGroup.params: _MuonBase#ParamGroup#params.
  _MuonBase.ParamGroup.opt_state_m: _MuonBase#ParamGroup#opt_state_m.
  _MuonBase.ParamGroup.opt_steps: _MuonBase#ParamGroup#opt_steps.
  ReferenceMuon: ReferenceMuon#
  Muon: Muon#
  _MuonBase._momentum: _MuonBase#_momentum.
  _MuonBase._nesterov: _MuonBase#_nesterov.
  _MuonBase._ns_coefficients: _MuonBase#_ns_coefficients.
  _MuonBase._eps: _MuonBase#_eps.
  _MuonBase._ns_steps: _MuonBase#_ns_steps.
  _MuonBase._adjust_lr_fn: _MuonBase#_adjust_lr_fn.
  DEFAULT_A.DEFAULT_A: DEFAULT_A.DEFAULT_A.
  DEFAULT_B.DEFAULT_B: DEFAULT_B.DEFAULT_B.
  DEFAULT_C.DEFAULT_C: DEFAULT_C.DEFAULT_C.
  DEFAULT_NS_STEPS.DEFAULT_NS_STEPS: DEFAULT_NS_STEPS.DEFAULT_NS_STEPS.
  EPS.EPS: EPS.EPS.
  _zeropower_via_newtonschulz: _zeropower_via_newtonschulz().
  _adjust_lr: _adjust_lr().
  _MuonBase._use_bfloat16_moments: _MuonBase#_use_bfloat16_moments.
  Muon._foreach: Muon#_foreach.
  Muon._has_complex: Muon#_has_complex.
  __all__: __all__.
  _MuonBase._HYPERPARAMETER_NAMES: _MuonBase#_HYPERPARAMETER_NAMES.
  Muon._HYPERPARAMETER_NAMES: Muon#_HYPERPARAMETER_NAMES.
---
# Module: [`src/torch_tpu/_internal/optimizers/muon.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py)

## Classes
### <a id="Muon"></a>`Muon`  ·  implements/extends _MuonBase
- def: [`src/torch_tpu/_internal/optimizers/muon.py:236`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L236)
- doc: Torch Muon implementation calling torch.optim._muon.muon directly.
- signature: `class Muon(_MuonBase):`
- members:
  - <a id="Muon.step"></a>`step(self, param_group: _MuonBase.ParamGroup, grads: dict[str, torch.Tensor])` — [`L288`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L288) — Torch Muon step calling torch.optim._muon.muon directly. — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- protocol/private: <a id="Muon._HYPERPARAMETER_NAMES"></a>`_HYPERPARAMETER_NAMES`[`L239`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L239), <a id="Muon.__init__"></a>`__init__`[`L253`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L253), <a id="Muon._foreach"></a>`_foreach`[`L282`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L282), <a id="Muon._has_complex"></a>`_has_complex`[`L283`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L283)
- uses (calls/refs, reference-scoped): [`_MuonBase`](muon.md#_MuonBase), [`__init__`](muon.md#_MuonBase.__init__), [`ParamGroup`](muon.md#_MuonBase.ParamGroup), [`_lr`](optim.md#Optimizer._lr), [`_weight_decay`](optim.md#Optimizer._weight_decay), [`params`](muon.md#_MuonBase.ParamGroup.params), [`opt_state_m`](muon.md#_MuonBase.ParamGroup.opt_state_m), [`opt_steps`](muon.md#_MuonBase.ParamGroup.opt_steps), [`_momentum`](muon.md#_MuonBase._momentum), [`DEFAULT_A`](muon.md#DEFAULT_A.DEFAULT_A), [`DEFAULT_B`](muon.md#DEFAULT_B.DEFAULT_B), [`DEFAULT_C`](muon.md#DEFAULT_C.DEFAULT_C), [`DEFAULT_NS_STEPS`](muon.md#DEFAULT_NS_STEPS.DEFAULT_NS_STEPS), [`EPS`](muon.md#EPS.EPS), [`_adjust_lr_fn`](muon.md#_MuonBase._adjust_lr_fn), [`_eps`](muon.md#_MuonBase._eps), [`_nesterov`](muon.md#_MuonBase._nesterov), [`_ns_coefficients`](muon.md#_MuonBase._ns_coefficients), [`_ns_steps`](muon.md#_MuonBase._ns_steps)
- used by: [`_MuonBase`](muon.md#_MuonBase), [`step`](muon.md#_MuonBase.step), [`Muon`](single_trace_trainer.md#Muon)

### <a id="ReferenceMuon"></a>`ReferenceMuon`  ·  implements/extends _MuonBase
- def: [`src/torch_tpu/_internal/optimizers/muon.py:191`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L191)
- doc: Reference pure PyTorch implementation of Muon.
- signature: `class ReferenceMuon(_MuonBase):`
- members:
  - <a id="ReferenceMuon._reference_muon_update"></a>`_reference_muon_update(self, param: torch.Tensor, grad: torch.Tensor, m: torch.Tensor)` — [`L198`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L198) — Performs an in-place reference Muon update on param and momentum buffer m. — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
  - <a id="ReferenceMuon.step"></a>`step(self, param_group: _MuonBase.ParamGroup, grads: dict[str, torch.Tensor])` — [`L219`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L219) — Reference pure PyTorch implementation of Muon step. — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- uses (calls/refs, reference-scoped): [`_MuonBase`](muon.md#_MuonBase), [`ParamGroup`](muon.md#_MuonBase.ParamGroup), [`_lr`](optim.md#Optimizer._lr), [`_weight_decay`](optim.md#Optimizer._weight_decay), [`params`](muon.md#_MuonBase.ParamGroup.params), [`opt_state_m`](muon.md#_MuonBase.ParamGroup.opt_state_m), [`opt_steps`](muon.md#_MuonBase.ParamGroup.opt_steps), [`_momentum`](muon.md#_MuonBase._momentum), [`_adjust_lr_fn`](muon.md#_MuonBase._adjust_lr_fn), [`_eps`](muon.md#_MuonBase._eps), [`_nesterov`](muon.md#_MuonBase._nesterov), [`_ns_coefficients`](muon.md#_MuonBase._ns_coefficients), [`_ns_steps`](muon.md#_MuonBase._ns_steps), [`_adjust_lr`](muon.md#_adjust_lr), [`_zeropower_via_newtonschulz`](muon.md#_zeropower_via_newtonschulz)
- used by: [`_MuonBase`](muon.md#_MuonBase), [`step`](muon.md#_MuonBase.step), [`ReferenceMuon`](single_trace_trainer.md#ReferenceMuon)

### <a id="_MuonBase"></a>`_MuonBase`  ·  implements/extends Optimizer
- def: [`src/torch_tpu/_internal/optimizers/muon.py:88`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L88) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- doc: Internal base class for Muon optimizer variants with nested ParamGroup.
- signature: `class _MuonBase(_optim.Optimizer):`
- members:
  - <a id="_MuonBase.init_param_group"></a>`init_param_group(self, params: dict[str, torch.Tensor] | torch.nn.Module)` — [`L145`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L145) — Initializes Muon optimizer state from model parameters or nn.Module. — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
  - <a id="_MuonBase.step"></a>`step(self, param_group: ParamGroup, grads: dict[str, torch.Tensor])` — [`L184`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L184) — Performs optimizer step on param_group given grads and returns updated ParamGroup.
- protocol/private: <a id="_MuonBase._HYPERPARAMETER_NAMES"></a>`_HYPERPARAMETER_NAMES`[`L104`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L104), <a id="_MuonBase.__init__"></a>`__init__`[`L116`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L116), <a id="_MuonBase._adjust_lr_fn"></a>`_adjust_lr_fn`[`L138`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L138), <a id="_MuonBase._eps"></a>`_eps`[`L136`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L136), <a id="_MuonBase._momentum"></a>`_momentum`[`L133`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L133), <a id="_MuonBase._nesterov"></a>`_nesterov`[`L134`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L134), <a id="_MuonBase._ns_coefficients"></a>`_ns_coefficients`[`L135`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L135), <a id="_MuonBase._ns_steps"></a>`_ns_steps`[`L137`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L137), <a id="_MuonBase._use_bfloat16_moments"></a>`_use_bfloat16_moments`[`L139`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L139)
- uses (calls/refs, reference-scoped): [`step`](muon.md#Muon.step), [`step`](muon.md#ReferenceMuon.step), [`ParamGroup`](muon.md#_MuonBase.ParamGroup), [`Optimizer`](optim.md#Optimizer), [`params`](muon.md#_MuonBase.ParamGroup.params), [`opt_state_m`](muon.md#_MuonBase.ParamGroup.opt_state_m), [`opt_steps`](muon.md#_MuonBase.ParamGroup.opt_steps), [`Muon`](muon.md#Muon), [`ReferenceMuon`](muon.md#ReferenceMuon), [`__init__`](optim.md#Optimizer.__init__), [`DEFAULT_A`](muon.md#DEFAULT_A.DEFAULT_A), [`DEFAULT_B`](muon.md#DEFAULT_B.DEFAULT_B), [`DEFAULT_C`](muon.md#DEFAULT_C.DEFAULT_C), [`DEFAULT_NS_STEPS`](muon.md#DEFAULT_NS_STEPS.DEFAULT_NS_STEPS), [`EPS`](muon.md#EPS.EPS)
- used by: [`step`](muon.md#Muon.step), [`_reference_muon_update`](muon.md#ReferenceMuon._reference_muon_update), [`__init__`](muon.md#Muon.__init__), [`step`](muon.md#ReferenceMuon.step), [`_muon_param_group_flatten`](muon.md#_muon_param_group_flatten), [`_muon_param_group_unflatten`](muon.md#_muon_param_group_unflatten), [`Optimizer`](optim.md#Optimizer), [`step`](optim.md#Optimizer.step), [`init_param_group`](optim.md#Optimizer.init_param_group), [`Muon`](muon.md#Muon), [`ReferenceMuon`](muon.md#ReferenceMuon)

### <a id="_MuonBase.ParamGroup"></a>`_MuonBase.ParamGroup`
- def: [`src/torch_tpu/_internal/optimizers/muon.py:95`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L95) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- doc: Holds model parameters and Muon optimizer states (m, steps).
- signature: `class ParamGroup:`
- members:
  - <a id="_MuonBase.ParamGroup.opt_state_m"></a>`opt_state_m` — [`L99`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L99) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
  - <a id="_MuonBase.ParamGroup.opt_steps"></a>`opt_steps` — [`L102`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L102) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
  - <a id="_MuonBase.ParamGroup.params"></a>`params` — [`L98`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L98) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- used by: [`step`](muon.md#Muon.step), [`step`](muon.md#ReferenceMuon.step), [`_muon_param_group_flatten`](muon.md#_muon_param_group_flatten), [`_muon_param_group_unflatten`](muon.md#_muon_param_group_unflatten), [`init_param_group`](muon.md#_MuonBase.init_param_group), [`step`](muon.md#_MuonBase.step)

## Functions
- <a id="_adjust_lr"></a>`_adjust_lr(lr: float, adjust_lr_fn: str | None, param_shape: torch.Size)` — [`L65`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L65) — Default learning rate adjustment used by Muon.
- <a id="_muon_param_group_flatten"></a>`_muon_param_group_flatten(group: _MuonBase.ParamGroup)` — [`L318`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L318)
- <a id="_muon_param_group_unflatten"></a>`_muon_param_group_unflatten(children, _context)` — [`L327`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L327)
- <a id="_zeropower_via_newtonschulz"></a>`_zeropower_via_newtonschulz(grad: torch.Tensor, ns_coefficients: tuple[float, float, float], ns_steps: int, eps: float)` — [`L34`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L34) — Newton-Schulz iteration to compute zeroth power / orthogonalization of 2D grad.

## Module values
- <a id="DEFAULT_A.DEFAULT_A"></a>`DEFAULT_A` — [`L81`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L81)
- <a id="DEFAULT_B.DEFAULT_B"></a>`DEFAULT_B` — [`L82`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L82)
- <a id="DEFAULT_C.DEFAULT_C"></a>`DEFAULT_C` — [`L83`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L83)
- <a id="DEFAULT_NS_STEPS.DEFAULT_NS_STEPS"></a>`DEFAULT_NS_STEPS` — [`L84`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L84)
- <a id="EPS.EPS"></a>`EPS` — [`L85`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L85)
- <a id="__all__"></a>`__all__` — [`L28`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/muon.py#L28)

