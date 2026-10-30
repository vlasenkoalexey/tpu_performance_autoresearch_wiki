---
title: 'Module: torchtitan/experiments/tpu/compiled_optimizers/functional.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/compiled_optimizers/functional.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.compiled_optimizers.functional`/
symbols:
  update_model_and_optstate_buffers: update_model_and_optstate_buffers().
  _get_optstate_buffer: _get_optstate_buffer().
  functional_adamw_step: functional_adamw_step().
  _get_param_by_fqn: _get_param_by_fqn().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/compiled_optimizers/functional.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/compiled_optimizers/functional.py)

## Functions
- <a id="_get_optstate_buffer"></a>`_get_optstate_buffer(model: nn.Module, fqn: str, kind: str)` — [`L38`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/compiled_optimizers/functional.py#L38) — Return the live ``_optstate_<leaf>_<kind>`` buffer for a param.
- <a id="_get_param_by_fqn"></a>`_get_param_by_fqn(model: nn.Module, fqn: str)` — [`L20`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/compiled_optimizers/functional.py#L20) — Return the underlying parameter Tensor for ``fqn``.
- <a id="functional_adamw_step"></a>`functional_adamw_step(params: Sequence[torch.Tensor], grads: Sequence[torch.Tensor], exp_avgs: Sequence[torch.Tensor], exp_avg_sqs: Sequence[torch.Tensor], steps: Sequence[torch.Tensor], lr: torch.Tensor, *, beta1: float = 0.9, beta2: float = 0.999, eps: float = 1e-8, weight_decay: float = 0.01, maximize: bool = False, foreach: bool = True, capturable: bool = True)` — [`L68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/compiled_optimizers/functional.py#L68) — Runs AdamW functionally by cloning state tensors before in-place modification.
- <a id="update_model_and_optstate_buffers"></a>`update_model_and_optstate_buffers(model: nn.Module, param_fqns: Sequence[str], new_params: Sequence[torch.Tensor], new_exp_avgs: Sequence[torch.Tensor], new_exp_avg_sqs: Sequence[torch.Tensor])` — [`L49`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/compiled_optimizers/functional.py#L49) — Updates live model parameters and optimizer state buffers in-place from graph outputs.

## Module values
- <a id="__all__"></a>`__all__` — [`L135`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/compiled_optimizers/functional.py#L135)

