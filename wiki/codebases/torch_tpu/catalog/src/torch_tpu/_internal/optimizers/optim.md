---
title: 'Module: src/torch_tpu/_internal/optimizers/optim.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/optimizers/optim.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.optimizers.optim`/
symbols:
  Optimizer: Optimizer#
  Optimizer.step: Optimizer#step().
  Optimizer._weight_decay: Optimizer#_weight_decay.
  Optimizer._lr: Optimizer#_lr.
  Optimizer.init_param_group: Optimizer#init_param_group().
  Optimizer.__init__: Optimizer#__init__().
  Optimizer.defaults: Optimizer#defaults().
  Optimizer.__call__: Optimizer#__call__().
  Optimizer._HYPERPARAMETER_NAMES: Optimizer#_HYPERPARAMETER_NAMES.
  __all__: __all__.
  Optimizer.ParamGroup: Optimizer#ParamGroup.
---
# Module: [`src/torch_tpu/_internal/optimizers/optim.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/optim.py)

## Classes
### <a id="Optimizer"></a>`Optimizer`  ·  implements/extends ABC
- def: [`src/torch_tpu/_internal/optimizers/optim.py:33`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/optim.py#L33) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- doc: Abstract base class for stateless functional optimizers operating on nested ParamGroup.
- signature: `class Optimizer(abc.ABC):`
- members:
  - <a id="Optimizer.defaults"></a>`defaults(self)` — [`L55`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/optim.py#L55) — Returns a read-only mapping of the optimizer's hyperparameters.
  - <a id="Optimizer.init_param_group"></a>`init_param_group(self, params: dict[str, torch.Tensor] | torch.nn.Module)` — [`L66`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/optim.py#L66) — Initializes a fresh ParamGroup instance from model parameters or nn.Module.
  - <a id="Optimizer.step"></a>`step(self, param_group: Any, grads: dict[str, torch.Tensor])` — [`L76`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/optim.py#L76) — Performs optimizer step on param_group given grads and returns updated ParamGroup.
  - <a id="Optimizer.ParamGroup"></a>`ParamGroup` — [`L41`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/optim.py#L41)
- protocol/private: <a id="Optimizer._HYPERPARAMETER_NAMES"></a>`_HYPERPARAMETER_NAMES`[`L45`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/optim.py#L45), <a id="Optimizer.__call__"></a>`__call__`[`L80`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/optim.py#L80), <a id="Optimizer.__init__"></a>`__init__`[`L47`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/optim.py#L47), <a id="Optimizer._lr"></a>`_lr`[`L48`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/optim.py#L48), <a id="Optimizer._weight_decay"></a>`_weight_decay`[`L49`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/optim.py#L49)
- uses (calls/refs, reference-scoped): [`_AdamWBase`](adamw.md#_AdamWBase), [`_MuonBase`](muon.md#_MuonBase), [`_SgdBase`](sgd.md#_SgdBase), [`init_param_group`](adamw.md#_AdamWBase.init_param_group), [`init_param_group`](muon.md#_MuonBase.init_param_group), [`init_param_group`](sgd.md#_SgdBase.init_param_group), [`step`](adamw.md#_AdamWBase.step), [`step`](muon.md#_MuonBase.step), [`step`](sgd.md#_SgdBase.step)
- used by: [`step`](adamw.md#AdamW.step), [`step`](sgd.md#Sgd.step), [`step`](muon.md#Muon.step), [`_reference_muon_update`](muon.md#ReferenceMuon._reference_muon_update), [`_AdamWBase`](adamw.md#_AdamWBase), [`_MuonBase`](muon.md#_MuonBase), [`_SgdBase`](sgd.md#_SgdBase), [`__init__`](muon.md#_MuonBase.__init__), [`_reference_adamw_update`](adamw.md#ReferenceAdamW._reference_adamw_update), [`_reference_sgd_update`](sgd.md#ReferenceSgd._reference_sgd_update), [`__init__`](adamw.md#_AdamWBase.__init__), [`__init__`](sgd.md#_SgdBase.__init__), [`Optimizer`](single_trace_trainer.md#Optimizer)

## Module values
- <a id="__all__"></a>`__all__` — [`L25`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/optim.py#L25)

