---
title: 'Module: torchtitan/experiments/tpu/numerical_validation.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/numerical_validation.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.numerical_validation`/
symbols:
  StateValidatorCallback.on_step: StateValidatorCallback#on_step().
  StateRecorderCallback.on_step: StateRecorderCallback#on_step().
  StateRecorderCallback.history: StateRecorderCallback#history.
  capture_local_state: capture_local_state().
  StateRecorderCallback.__init__: StateRecorderCallback#__init__().
  StateValidatorCallback.__init__: StateValidatorCallback#__init__().
  StateValidatorCallback.errors: StateValidatorCallback#errors.
  StateValidatorCallback.__exit__: StateValidatorCallback#__exit__().
  StateRecorderCallback.get_history: StateRecorderCallback#get_history().
  clean_parameter_name: clean_parameter_name().
  StateValidatorCallback.current_label: StateValidatorCallback#current_label.
  StateValidatorCallback.recorded_label: StateValidatorCallback#recorded_label.
  StateValidatorCallback.in_context: StateValidatorCallback#in_context.
  StateValidatorCallback.__enter__: StateValidatorCallback#__enter__().
  CaptureFn: CaptureFn.
  StateRecorderCallback: StateRecorderCallback#
  StateValidatorCallback: StateValidatorCallback#
  StateValidatorCallback.recorded_history: StateValidatorCallback#recorded_history.
  StateRecorderCallback.capture_fn: StateRecorderCallback#capture_fn.
  StateValidatorCallback.capture_fn: StateValidatorCallback#capture_fn.
  StateValidatorCallback.loss_atol: StateValidatorCallback#loss_atol.
  StateValidatorCallback.loss_rtol: StateValidatorCallback#loss_rtol.
  StateValidatorCallback.grad_atol: StateValidatorCallback#grad_atol.
  StateValidatorCallback.grad_rtol: StateValidatorCallback#grad_rtol.
  StateValidatorCallback.param_atol: StateValidatorCallback#param_atol.
  StateValidatorCallback.param_rtol: StateValidatorCallback#param_rtol.
  StateValidatorCallback.init_state: StateValidatorCallback#init_state.
---
# Module: [`torchtitan/experiments/tpu/numerical_validation.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py)

## Classes
### <a id="StateRecorderCallback"></a>`StateRecorderCallback`
- def: [`torchtitan/experiments/tpu/numerical_validation.py:53`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L53)
- doc: Generic callback to record model state history during training.
- signature: `class StateRecorderCallback:`
- members:
  - <a id="StateRecorderCallback.get_history"></a>`get_history(self)` — [`L80`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L80) — Returns the recorded state history.
  - <a id="StateRecorderCallback.on_step"></a>`on_step(self, step: int, model: nn.Module, loss: torch.Tensor, inputs: torch.Tensor = None, labels: torch.Tensor = None, positions: torch.Tensor = None)` — [`L60`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L60) — Records the state at the current step.
  - <a id="StateRecorderCallback.capture_fn"></a>`capture_fn` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L58)
  - <a id="StateRecorderCallback.history"></a>`history` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L57)
- protocol/private: <a id="StateRecorderCallback.__init__"></a>`__init__`[`L56`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L56)
- uses (calls/refs, reference-scoped): [`capture_local_state`](numerical_validation.md#capture_local_state), [`CaptureFn`](numerical_validation.md#CaptureFn)
- used by: [`__call__`](base_distributed_device_test.md#DistributedTrainWithRecorder.__call__), [`_run_trainer_device_parity_test`](base_device_test.md#BaseAcceleratorDeviceTest._run_trainer_device_parity_test)

### <a id="StateValidatorCallback"></a>`StateValidatorCallback`
- def: [`torchtitan/experiments/tpu/numerical_validation.py:85`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L85)
- doc: Generic callback to validate current model state against device history.
- signature: `class StateValidatorCallback:`
- members:
  - <a id="StateValidatorCallback.__enter__"></a>`__enter__(self)` — [`L126`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L126) — Enters the context.
  - <a id="StateValidatorCallback.__exit__"></a>`__exit__(self, exc_type, exc_val, exc_tb)` — [`L131`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L131) — Exits the context and raises any collected errors.
  - <a id="StateValidatorCallback.on_step"></a>`on_step(self, step: int, model: nn.Module, loss: torch.Tensor, inputs: torch.Tensor = None, labels: torch.Tensor = None, positions: torch.Tensor = None)` — [`L137`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L137) — Validates the current state against the reference history.
  - <a id="StateValidatorCallback.capture_fn"></a>`capture_fn` — [`L111`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L111)
  - <a id="StateValidatorCallback.current_label"></a>`current_label` — [`L121`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L121)
  - <a id="StateValidatorCallback.errors"></a>`errors` — [`L123`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L123)
  - <a id="StateValidatorCallback.grad_atol"></a>`grad_atol` — [`L115`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L115)
  - <a id="StateValidatorCallback.grad_rtol"></a>`grad_rtol` — [`L116`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L116)
  - <a id="StateValidatorCallback.in_context"></a>`in_context` — [`L124`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L124)
  - <a id="StateValidatorCallback.init_state"></a>`init_state` — [`L112`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L112)
  - <a id="StateValidatorCallback.loss_atol"></a>`loss_atol` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L113)
  - <a id="StateValidatorCallback.loss_rtol"></a>`loss_rtol` — [`L114`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L114)
  - <a id="StateValidatorCallback.param_atol"></a>`param_atol` — [`L117`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L117)
  - <a id="StateValidatorCallback.param_rtol"></a>`param_rtol` — [`L118`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L118)
  - <a id="StateValidatorCallback.recorded_history"></a>`recorded_history` — [`L110`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L110)
  - <a id="StateValidatorCallback.recorded_label"></a>`recorded_label` — [`L122`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L122)
- protocol/private: <a id="StateValidatorCallback.__init__"></a>`__init__`[`L96`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L96)
- uses (calls/refs, reference-scoped): [`capture_local_state`](numerical_validation.md#capture_local_state), [`clean_parameter_name`](numerical_validation.md#clean_parameter_name), [`CaptureFn`](numerical_validation.md#CaptureFn)  (1 test-only)
- used by: [`_run_cpu_verification`](base_distributed_device_test.md#_run_cpu_verification), [`_run_trainer_device_parity_test`](base_device_test.md#BaseAcceleratorDeviceTest._run_trainer_device_parity_test)

## Functions
- <a id="capture_local_state"></a>`capture_local_state(model: nn.Module, loss: torch.Tensor)` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L29) — Captures local model state (CPU/GPU/TPU single device).
- <a id="clean_parameter_name"></a>`clean_parameter_name(name: str)` — [`L11`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L11) — Removes wrapper prefixes (like activation checkpointing) from parameter names.

## Module values
- <a id="CaptureFn"></a>`CaptureFn` — [`L26`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/numerical_validation.py#L26)

