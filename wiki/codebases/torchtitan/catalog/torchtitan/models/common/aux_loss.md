---
title: 'Module: torchtitan/models/common/aux_loss.py'
type: catalog
provenance: extracted
module: torchtitan/models/common/aux_loss.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.common.aux_loss`/
symbols:
  AuxLoss: AuxLoss#
  collect_aux_loss_metrics: collect_aux_loss_metrics().
  AuxLoss.reduce_mesh: AuxLoss#reduce_mesh.
  AuxLoss._accumulate_and_inject: AuxLoss#_accumulate_and_inject().
  _zero_aux_losses: _zero_aux_losses().
  register_aux_loss_zero_hook: register_aux_loss_zero_hook().
  AuxLoss.inject: AuxLoss#inject().
  AuxLoss.set_step_denominator: AuxLoss#set_step_denominator().
  AuxLoss.Config: AuxLoss#Config#
  collect_aux_loss_metrics._group_acc_or_zero: collect_aux_loss_metrics()._group_acc_or_zero().
  AuxLoss.Config.coeff: AuxLoss#Config#coeff.
  AuxLoss._group_counts: AuxLoss#_group_counts.
  AuxLoss.instance_acc: AuxLoss#instance_acc.
  AuxLoss.group_acc: AuxLoss#group_acc.
  AuxLoss._init_self_buffers: AuxLoss#_init_self_buffers().
  AuxLoss.coeff: AuxLoss#coeff.
  AuxLoss.__init__: AuxLoss#__init__().
  _AuxLossInjection: _AuxLossInjection#
  AuxLoss._step_denominator: AuxLoss#_step_denominator.
  AuxLoss.metric_name: AuxLoss#metric_name().
  AuxLoss.Config.reduce_mesh: AuxLoss#Config#reduce_mesh.
  __all__: __all__.
  _AuxLossInjection.forward: _AuxLossInjection#forward().
  _AuxLossInjection.spmd_typecheck: _AuxLossInjection#spmd_typecheck().
  _AuxLossInjection.backward: _AuxLossInjection#backward().
---
# Module: [`torchtitan/models/common/aux_loss.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py)

## Classes
### <a id="AuxLoss"></a>`AuxLoss`  ·  implements/extends Module
- def: [`torchtitan/models/common/aux_loss.py:81`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L81) — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- doc: Base class: subclasses call `inject()` each microbatch.  Each
- signature: `class AuxLoss(Module):`
- members:
  - <a id="AuxLoss._accumulate_and_inject"></a>`_accumulate_and_inject(self, raw_sum: torch.Tensor, *, carrier: torch.Tensor)` — [`L199`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L199) — Accumulate this microbatch's metric value and inject the gradient.
  - <a id="AuxLoss.inject"></a>`inject(self, raw_sum: torch.Tensor, *, carrier: torch.Tensor)` — [`L167`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L167) — Inject the aux-loss gradient on ``carrier``; accumulate the scaled metric.
  - <a id="AuxLoss.metric_name"></a>`metric_name(self)` — [`L129`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L129) — Convert the class name from PascalCase to snake_case.
  - <a id="AuxLoss.set_step_denominator"></a>`set_step_denominator(cls, denominator: torch.Tensor)` — [`L158`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L158) — Set the current step's global valid-token count.
  - <a id="AuxLoss.coeff"></a>`coeff` — [`L139`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L139)
  - <a id="AuxLoss.group_acc"></a>`group_acc` — [`L116`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L116)
  - <a id="AuxLoss.instance_acc"></a>`instance_acc` — [`L155`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L155)
  - <a id="AuxLoss.reduce_mesh"></a>`reduce_mesh` — [`L140`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L140)
- protocol/private: <a id="AuxLoss.__init__"></a>`__init__`[`L137`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L137), <a id="AuxLoss._group_counts"></a>`_group_counts`[`L103`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L103), <a id="AuxLoss._init_self_buffers"></a>`_init_self_buffers`[`L151`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L151), <a id="AuxLoss._step_denominator"></a>`_step_denominator`[`L109`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L109)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`MoELoadBalanceAuxLoss`](moe.md#MoELoadBalanceAuxLoss), [`remat_region_name`](../../protocols/module.md#Module.remat_region_name), [`Config`](aux_loss.md#AuxLoss.Config), [`coeff`](aux_loss.md#AuxLoss.Config.coeff), [`MicrobatchWiseLoadBalanceLoss`](moe.md#MicrobatchWiseLoadBalanceLoss), [`_AuxLossInjection`](aux_loss.md#_AuxLossInjection), [`reduce_mesh`](aux_loss.md#AuxLoss.Config.reduce_mesh), [`_init_self_buffers`](moe.md#MoELoadBalanceAuxLoss._init_self_buffers)
- used by: [`Module`](../../protocols/module.md#Module), [`train_step`](../../trainer.md#Trainer.train_step), [`train_step`](../../experiments/torchft/trainer.md#FaultTolerantTrainer.train_step), [`_train_step_optimizer_in_graph`](../../experiments/tpu/graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer._train_step_optimizer_in_graph), [`_common_setup`](../../experiments/graph_trainer/precompile_main.md#_common_setup), [`forward`](moe.md#MoELoadBalanceAuxLoss.forward), [`_init_self_buffers`](../../protocols/module.md#Module._init_self_buffers), [`__init__`](moe.md#MoELoadBalanceAuxLoss.__init__), [`MoELoadBalanceAuxLoss`](moe.md#MoELoadBalanceAuxLoss), [`collect_aux_loss_metrics`](aux_loss.md#collect_aux_loss_metrics), [`Config`](moe.md#MoELoadBalanceAuxLoss.Config), [`_zero_aux_losses`](aux_loss.md#_zero_aux_losses), [`aux_loss`](moe.md#TokenChoiceTopKRouter.Config.aux_loss), [`forward`](moe.md#MicrobatchWiseLoadBalanceLoss.forward), [`_group_acc_or_zero`](aux_loss.md#collect_aux_loss_metrics._group_acc_or_zero), [`Config`](moe.md#MicrobatchWiseLoadBalanceLoss.Config), [`MicrobatchWiseLoadBalanceLoss`](moe.md#MicrobatchWiseLoadBalanceLoss)  (3 test-only)

### <a id="AuxLoss.Config"></a>`AuxLoss.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/aux_loss.py:119`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L119)
- signature: `class Config(Module.Config):`
- members:
  - <a id="AuxLoss.Config.coeff"></a>`coeff` — [`L120`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L120) — ---
  - <a id="AuxLoss.Config.reduce_mesh"></a>`reduce_mesh` — [`L122`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L122) — ---
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`make_moe_config`](config_utils.md#make_moe_config), [`__init__`](moe.md#MoELoadBalanceAuxLoss.__init__), [`make_aux_loss_config`](config_utils.md#make_aux_loss_config), [`reduce_mesh`](aux_loss.md#AuxLoss.reduce_mesh), [`Config`](moe.md#MoELoadBalanceAuxLoss.Config), [`aux_loss`](moe.md#TokenChoiceTopKRouter.Config.aux_loss), [`Config`](moe.md#MicrobatchWiseLoadBalanceLoss.Config), [`coeff`](aux_loss.md#AuxLoss.coeff), [`__init__`](aux_loss.md#AuxLoss.__init__)  (3 test-only)

### <a id="_AuxLossInjection"></a>`_AuxLossInjection`
- def: [`torchtitan/models/common/aux_loss.py:55`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L55)
- doc: Identity-forward autograd that injects an aux-loss gradient on backward.
- signature: `class _AuxLossInjection(torch.autograd.Function):`
- members:
  - <a id="_AuxLossInjection.backward"></a>`backward(ctx, grad_carrier)` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L76)
  - <a id="_AuxLossInjection.forward"></a>`forward(ctx, carrier, aux_loss)` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L63)
  - <a id="_AuxLossInjection.spmd_typecheck"></a>`spmd_typecheck(result, *, carrier)` — [`L68`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L68)
- used by: [`_accumulate_and_inject`](aux_loss.md#AuxLoss._accumulate_and_inject), [`_last_local_tokens_per_expert_E`](moe.md#MoELoadBalanceAuxLoss._last_local_tokens_per_expert_E)

## Functions
- <a id="collect_aux_loss_metrics._group_acc_or_zero"></a>`_group_acc_or_zero(key: tuple[str, str])` — [`L254`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L254)
- <a id="_zero_aux_losses"></a>`_zero_aux_losses(model_parts)` — [`L223`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L223) — Roll per-instance ``instance_acc`` values into the ``group_acc``
- <a id="collect_aux_loss_metrics"></a>`collect_aux_loss_metrics(parallel_dims: ParallelDims)` — [`L240`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L240) — Reduce the current step's ``group_acc`` registers for logging.
- <a id="register_aux_loss_zero_hook"></a>`register_aux_loss_zero_hook(optimizers: OptimizersContainer, model_parts: list[nn.Module], parallel_dims: ParallelDims)` — [`L280`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L280) — Register the step pre-hook that rolls per-instance ``instance_acc``

## Module values
- <a id="__all__"></a>`__all__` — [`L48`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/aux_loss.py#L48)

