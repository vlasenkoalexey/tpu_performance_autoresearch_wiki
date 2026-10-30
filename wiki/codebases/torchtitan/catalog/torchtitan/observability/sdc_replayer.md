---
title: 'Module: torchtitan/observability/sdc_replayer.py'
type: catalog
provenance: extracted
module: torchtitan/observability/sdc_replayer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.observability.sdc_replayer`/
symbols:
  _ReplayStateProvider.capture: _ReplayStateProvider#capture().
  _ReplayStateProvider.restore: _ReplayStateProvider#restore().
  SDCReplayer._run_checked: SDCReplayer#_run_checked().
  SDCReplayer._signature: SDCReplayer#_signature().
  SDCReplayer: SDCReplayer#
  SDCReplayer.run_fwd_bwd: SDCReplayer#run_fwd_bwd().
  _ReplaySignature: _ReplaySignature#
  _ReplaySignature.clone: _ReplaySignature#clone().
  _compare_signature: _compare_signature().
  _find_signature_mismatch: _find_signature_mismatch().
  SDCReplayer.Config: SDCReplayer#Config#
  SDCReplayer._raise_if_mismatch: SDCReplayer#_raise_if_mismatch().
  _ReplaySignature.state: _ReplaySignature#state.
  SDCReplayer.add_tensor: SDCReplayer#add_tensor().
  SDCReplayer._state_provider: SDCReplayer#_state_provider.
  _ReplaySignature.schema: _ReplaySignature#schema.
  _ReplaySignature.digests: _ReplaySignature#digests.
  SDCReplayer._execute: SDCReplayer#_execute().
  SDCReplayer._steps_since_reset: SDCReplayer#_steps_since_reset.
  ScalarStateAccessor: ScalarStateAccessor#
  _local_tensor: _local_tensor().
  SDCReplayer.Config.num_steps: SDCReplayer#Config#num_steps.
  _ReplayResult.signature: _ReplayResult#signature.
  _BufferSnapshot.original: _BufferSnapshot#original.
  _GradientSnapshot.original: _GradientSnapshot#original.
  SDCReplayer.Config.num_replays: SDCReplayer#Config#num_replays.
  SDCReplayer.Config.__post_init__: SDCReplayer#Config#__post_init__().
  SDCReplayer.__init__: SDCReplayer#__init__().
  _ReplayStateSnapshot.buffers: _ReplayStateSnapshot#buffers.
  _ReplayStateSnapshot.gradients: _ReplayStateSnapshot#gradients.
  ScalarStateAccessor.get: ScalarStateAccessor#get.
  _BufferSnapshot.module: _BufferSnapshot#module.
  _BufferSnapshot.name: _BufferSnapshot#name.
  _GradientSnapshot.parameter: _GradientSnapshot#parameter.
  _ReplayStateSnapshot.accelerator_rng_states: _ReplayStateSnapshot#accelerator_rng_states.
  _ReplayStateProvider._device: _ReplayStateProvider#_device.
  _hash_tensor: _hash_tensor().
  _clone_tensor: _clone_tensor().
  SDCReplayer.steps_since_reset: SDCReplayer#steps_since_reset().
  SDCReplayer.reset_schedule: SDCReplayer#reset_schedule().
  SDCReplayMismatch: SDCReplayMismatch#
  _BufferSnapshot: _BufferSnapshot#
  _BufferSnapshot.value: _BufferSnapshot#value.
  _ReplayStateSnapshot: _ReplayStateSnapshot#
  SDCReplayer.config: SDCReplayer#config.
  SDCReplayer._modules: SDCReplayer#_modules.
  _ReplayStateProvider.__init__: _ReplayStateProvider#__init__().
  _ReplayResult: _ReplayResult#
  SDCReplayMismatch.signature_mismatch: SDCReplayMismatch#signature_mismatch.
  _accelerator_rng_states: _accelerator_rng_states().
  _GradientSnapshot: _GradientSnapshot#
  _ReplayStateSnapshot.python_rng_state: _ReplayStateSnapshot#python_rng_state.
  _ReplayStateSnapshot.cpu_rng_state: _ReplayStateSnapshot#cpu_rng_state.
  _ReplayStateSnapshot.scalar_values: _ReplayStateSnapshot#scalar_values.
  _ReplayStateProvider._scalar_state: _ReplayStateProvider#_scalar_state.
  SDCReplayer._device: SDCReplayer#_device.
  SDCReplayer._scalar_state: SDCReplayer#_scalar_state.
  _ReplayResult.loss: _ReplayResult#loss.
  SDCReplayMismatch.step: SDCReplayMismatch#step.
  SDCReplayMismatch.local_step: SDCReplayMismatch#local_step.
  SDCReplayMismatch.replay: SDCReplayMismatch#replay.
  SDCReplayMismatch.rank: SDCReplayMismatch#rank.
  _ReplayStateProvider: _ReplayStateProvider#
  _ReplayStateProvider._modules: _ReplayStateProvider#_modules.
  SDCReplayer._validate_hash_support: SDCReplayer#_validate_hash_support().
  SDCReplayMismatch.__init__: SDCReplayMismatch#__init__().
---
# Module: [`torchtitan/observability/sdc_replayer.py`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py)

## Classes
### <a id="SDCReplayMismatch"></a>`SDCReplayMismatch`  ·  implements/extends RuntimeError
- def: [`torchtitan/observability/sdc_replayer.py:86`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L86)
- doc: Raised on every rank when deterministic replay finds a mismatch.
- signature: `class SDCReplayMismatch(RuntimeError):`
- members:
  - <a id="SDCReplayMismatch.local_step"></a>`local_step` — [`L104`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L104)
  - <a id="SDCReplayMismatch.rank"></a>`rank` — [`L106`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L106)
  - <a id="SDCReplayMismatch.replay"></a>`replay` — [`L105`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L105)
  - <a id="SDCReplayMismatch.signature_mismatch"></a>`signature_mismatch` — [`L107`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L107)
  - <a id="SDCReplayMismatch.step"></a>`step` — [`L103`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L103)
- protocol/private: <a id="SDCReplayMismatch.__init__"></a>`__init__`[`L94`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L94)
- used by: [`_raise_if_mismatch`](sdc_replayer.md#SDCReplayer._raise_if_mismatch)  (1 test-only)

### <a id="SDCReplayer"></a>`SDCReplayer`  ·  implements/extends Configurable
- def: [`torchtitan/observability/sdc_replayer.py:318`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L318) — documented in [observability](../../../concepts/observability.md)
- doc: Replay-checks each scheduled optimizer step's first forward/backward.
- signature: `class SDCReplayer(Configurable):`
- members:
  - <a id="SDCReplayer._signature"></a>`_signature(self, loss: torch.Tensor)` — [`L415`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L415) — Capture hashes and scalar state after one forward/backward execution. — documented in [observability](../../../concepts/observability.md)
  - <a id="SDCReplayer.add_tensor"></a>`add_tensor(name: str, tensor: torch.Tensor)` — [`L426`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L426) — documented in [observability](../../../concepts/observability.md)
  - <a id="SDCReplayer.reset_schedule"></a>`reset_schedule(self)` — [`L388`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L388) — Restart the check schedule; call after loading a checkpoint.
  - <a id="SDCReplayer.run_fwd_bwd"></a>`run_fwd_bwd(self, execute: Callable[[], torch.Tensor], *, step: int)` — [`L392`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L392) — Run one optimizer step's first forward/backward, replay-checking it — documented in [observability](../../../concepts/observability.md)
  - <a id="SDCReplayer.steps_since_reset"></a>`steps_since_reset(self)` — [`L384`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L384) — Optimizer steps observed since construction or ``reset_schedule``.
  - <a id="SDCReplayer.config"></a>`config` — [`L360`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L360)
- protocol/private: <a id="SDCReplayer.__init__"></a>`__init__`[`L352`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L352), <a id="SDCReplayer._device"></a>`_device`[`L363`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L363), <a id="SDCReplayer._execute"></a>`_execute`[`L486`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L486), <a id="SDCReplayer._modules"></a>`_modules`[`L361`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L361), <a id="SDCReplayer._raise_if_mismatch"></a>`_raise_if_mismatch`[`L490`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L490), <a id="SDCReplayer._run_checked"></a>`_run_checked`[`L528`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L528), <a id="SDCReplayer._scalar_state"></a>`_scalar_state`[`L364`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L364), <a id="SDCReplayer._state_provider"></a>`_state_provider`[`L365`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L365), <a id="SDCReplayer._steps_since_reset"></a>`_steps_since_reset`[`L370`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L370), <a id="SDCReplayer._validate_hash_support"></a>`_validate_hash_support`[`L374`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L374)
- uses (calls/refs, reference-scoped): [`Configurable`](../config/configurable.md#Configurable), [`capture`](sdc_replayer.md#_ReplayStateProvider.capture), [`restore`](sdc_replayer.md#_ReplayStateProvider.restore), [`Config`](sdc_replayer.md#SDCReplayer.Config), [`_ReplaySignature`](sdc_replayer.md#_ReplaySignature), [`_compare_signature`](sdc_replayer.md#_compare_signature), [`_find_signature_mismatch`](sdc_replayer.md#_find_signature_mismatch), [`clone`](sdc_replayer.md#_ReplaySignature.clone), [`ScalarStateAccessor`](sdc_replayer.md#ScalarStateAccessor), [`_local_tensor`](sdc_replayer.md#_local_tensor), [`num_steps`](sdc_replayer.md#SDCReplayer.Config.num_steps), [`signature`](sdc_replayer.md#_ReplayResult.signature), [`num_replays`](sdc_replayer.md#SDCReplayer.Config.num_replays), [`get`](sdc_replayer.md#ScalarStateAccessor.get), [`_hash_tensor`](sdc_replayer.md#_hash_tensor), [`SDCReplayMismatch`](sdc_replayer.md#SDCReplayMismatch), [`_ReplayResult`](sdc_replayer.md#_ReplayResult), [`_accelerator_rng_states`](sdc_replayer.md#_accelerator_rng_states), [`_ReplayStateProvider`](sdc_replayer.md#_ReplayStateProvider), [`loss`](sdc_replayer.md#_ReplayResult.loss)
- used by: [`Configurable`](../config/configurable.md#Configurable), [`train_step`](../trainer.md#Trainer.train_step), [`train_step`](../experiments/torchft/trainer.md#FaultTolerantTrainer.train_step), [`graph_trainer_llama3_debugmodel_sdc_replay`](../experiments/graph_trainer/llama3/config_registry.md#graph_trainer_llama3_debugmodel_sdc_replay), [`sdc_replayer`](../trainer.md#Trainer.Config.sdc_replayer), [`sdc_replayer`](../trainer.md#Trainer.sdc_replayer), [`load_state_dict`](../trainer.md#Trainer.load_state_dict), [`sdc_replayer`](../experiments/torchft/trainer.md#FaultTolerantTrainer.sdc_replayer)  (4 test-only)

### <a id="SDCReplayer.Config"></a>`SDCReplayer.Config`  ·  implements/extends Config
- def: [`torchtitan/observability/sdc_replayer.py:331`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L331) — documented in [observability](../../../concepts/observability.md)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="SDCReplayer.Config.num_replays"></a>`num_replays` — [`L340`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L340) — --- — documented in [observability](../../../concepts/observability.md)
  - <a id="SDCReplayer.Config.num_steps"></a>`num_steps` — [`L332`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L332) — ---
- protocol/private: <a id="SDCReplayer.Config.__post_init__"></a>`__post_init__`[`L346`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L346)
- uses (calls/refs, reference-scoped): [`Configurable`](../config/configurable.md#Configurable), [`Config`](../config/configurable.md#Configurable.Config)
- used by: [`pp_schedule`](../experiments/torchft/trainer.md#FaultTolerantTrainer.pp_schedule), [`_collect_moe_routing_metrics`](../trainer.md#Trainer._collect_moe_routing_metrics), [`graph_trainer_llama3_debugmodel_sdc_replay`](../experiments/graph_trainer/llama3/config_registry.md#graph_trainer_llama3_debugmodel_sdc_replay), [`_run_checked`](sdc_replayer.md#SDCReplayer._run_checked), [`_validate_sdc_replay`](../trainer.md#Trainer.Config._validate_sdc_replay), [`sdc_replayer`](../trainer.md#Trainer.Config.sdc_replayer), [`run_fwd_bwd`](sdc_replayer.md#SDCReplayer.run_fwd_bwd), [`__init__`](sdc_replayer.md#SDCReplayer.__init__)  (3 test-only)

### <a id="ScalarStateAccessor"></a>`ScalarStateAccessor`
- def: [`torchtitan/observability/sdc_replayer.py:56`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L56)
- doc: Read/write access to one caller-owned scalar mutated by the replayed
- signature: `class ScalarStateAccessor:`
- members:
  - <a id="ScalarStateAccessor.get"></a>`get` — [`L62`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L62)
- used by: [`pp_schedule`](../experiments/torchft/trainer.md#FaultTolerantTrainer.pp_schedule), [`_collect_moe_routing_metrics`](../trainer.md#Trainer._collect_moe_routing_metrics), [`capture`](sdc_replayer.md#_ReplayStateProvider.capture), [`_signature`](sdc_replayer.md#SDCReplayer._signature), [`__init__`](sdc_replayer.md#SDCReplayer.__init__), [`__init__`](sdc_replayer.md#_ReplayStateProvider.__init__)

### <a id="_BufferSnapshot"></a>`_BufferSnapshot`
- def: [`torchtitan/observability/sdc_replayer.py:151`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L151)
- signature: `class _BufferSnapshot:`
- members:
  - <a id="_BufferSnapshot.module"></a>`module` — [`L152`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L152)
  - <a id="_BufferSnapshot.name"></a>`name` — [`L153`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L153)
  - <a id="_BufferSnapshot.original"></a>`original` — [`L154`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L154)
  - <a id="_BufferSnapshot.value"></a>`value` — [`L155`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L155)
- used by: [`capture`](sdc_replayer.md#_ReplayStateProvider.capture), [`restore`](sdc_replayer.md#_ReplayStateProvider.restore), [`buffers`](sdc_replayer.md#_ReplayStateSnapshot.buffers)

### <a id="_GradientSnapshot"></a>`_GradientSnapshot`
- def: [`torchtitan/observability/sdc_replayer.py:159`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L159)
- signature: `class _GradientSnapshot:`
- members:
  - <a id="_GradientSnapshot.original"></a>`original` — [`L161`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L161)
  - <a id="_GradientSnapshot.parameter"></a>`parameter` — [`L160`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L160)
- used by: [`capture`](sdc_replayer.md#_ReplayStateProvider.capture), [`restore`](sdc_replayer.md#_ReplayStateProvider.restore), [`gradients`](sdc_replayer.md#_ReplayStateSnapshot.gradients)

### <a id="_ReplayResult"></a>`_ReplayResult`
- def: [`torchtitan/observability/sdc_replayer.py:81`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L81)
- signature: `class _ReplayResult:`
- members:
  - <a id="_ReplayResult.loss"></a>`loss` — [`L82`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L82)
  - <a id="_ReplayResult.signature"></a>`signature` — [`L83`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L83)
- uses (calls/refs, reference-scoped): [`_ReplaySignature`](sdc_replayer.md#_ReplaySignature)
- used by: [`_run_checked`](sdc_replayer.md#SDCReplayer._run_checked), [`_execute`](sdc_replayer.md#SDCReplayer._execute)

### <a id="_ReplaySignature"></a>`_ReplaySignature`
- def: [`torchtitan/observability/sdc_replayer.py:67`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L67) — documented in [observability](../../../concepts/observability.md)
- signature: `class _ReplaySignature:`
- members:
  - <a id="_ReplaySignature.clone"></a>`clone(self)` — [`L72`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L72) — documented in [observability](../../../concepts/observability.md)
  - <a id="_ReplaySignature.digests"></a>`digests` — [`L69`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L69)
  - <a id="_ReplaySignature.schema"></a>`schema` — [`L68`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L68)
  - <a id="_ReplaySignature.state"></a>`state` — [`L70`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L70) — documented in [observability](../../../concepts/observability.md)
- used by: [`_run_checked`](sdc_replayer.md#SDCReplayer._run_checked), [`_signature`](sdc_replayer.md#SDCReplayer._signature), [`_compare_signature`](sdc_replayer.md#_compare_signature), [`_find_signature_mismatch`](sdc_replayer.md#_find_signature_mismatch), [`_raise_if_mismatch`](sdc_replayer.md#SDCReplayer._raise_if_mismatch), [`signature`](sdc_replayer.md#_ReplayResult.signature)

### <a id="_ReplayStateProvider"></a>`_ReplayStateProvider`
- def: [`torchtitan/observability/sdc_replayer.py:174`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L174)
- doc: Captures and restores the semantic state of one replayed execution.
- signature: `class _ReplayStateProvider:`
- members:
  - <a id="_ReplayStateProvider.capture"></a>`capture(self)` — [`L188`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L188) — documented in [observability](../../../concepts/observability.md)
  - <a id="_ReplayStateProvider.restore"></a>`restore(self, state: _ReplayStateSnapshot)` — [`L236`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L236) — documented in [observability](../../../concepts/observability.md)
- protocol/private: <a id="_ReplayStateProvider.__init__"></a>`__init__`[`L177`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L177), <a id="_ReplayStateProvider._device"></a>`_device`[`L185`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L185), <a id="_ReplayStateProvider._modules"></a>`_modules`[`L183`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L183), <a id="_ReplayStateProvider._scalar_state"></a>`_scalar_state`[`L186`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L186)
- uses (calls/refs, reference-scoped): [`ScalarStateAccessor`](sdc_replayer.md#ScalarStateAccessor), [`_local_tensor`](sdc_replayer.md#_local_tensor), [`original`](sdc_replayer.md#_BufferSnapshot.original), [`original`](sdc_replayer.md#_GradientSnapshot.original), [`buffers`](sdc_replayer.md#_ReplayStateSnapshot.buffers), [`gradients`](sdc_replayer.md#_ReplayStateSnapshot.gradients), [`accelerator_rng_states`](sdc_replayer.md#_ReplayStateSnapshot.accelerator_rng_states), [`get`](sdc_replayer.md#ScalarStateAccessor.get), [`module`](sdc_replayer.md#_BufferSnapshot.module), [`name`](sdc_replayer.md#_BufferSnapshot.name), [`parameter`](sdc_replayer.md#_GradientSnapshot.parameter), [`_clone_tensor`](sdc_replayer.md#_clone_tensor), [`_BufferSnapshot`](sdc_replayer.md#_BufferSnapshot), [`_ReplayStateSnapshot`](sdc_replayer.md#_ReplayStateSnapshot), [`value`](sdc_replayer.md#_BufferSnapshot.value), [`_GradientSnapshot`](sdc_replayer.md#_GradientSnapshot), [`_accelerator_rng_states`](sdc_replayer.md#_accelerator_rng_states), [`cpu_rng_state`](sdc_replayer.md#_ReplayStateSnapshot.cpu_rng_state), [`python_rng_state`](sdc_replayer.md#_ReplayStateSnapshot.python_rng_state), [`scalar_values`](sdc_replayer.md#_ReplayStateSnapshot.scalar_values)
- used by: [`_run_checked`](sdc_replayer.md#SDCReplayer._run_checked), [`_state_provider`](sdc_replayer.md#SDCReplayer._state_provider)

### <a id="_ReplayStateSnapshot"></a>`_ReplayStateSnapshot`
- def: [`torchtitan/observability/sdc_replayer.py:165`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L165)
- signature: `class _ReplayStateSnapshot:`
- members:
  - <a id="_ReplayStateSnapshot.accelerator_rng_states"></a>`accelerator_rng_states` — [`L168`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L168)
  - <a id="_ReplayStateSnapshot.buffers"></a>`buffers` — [`L170`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L170)
  - <a id="_ReplayStateSnapshot.cpu_rng_state"></a>`cpu_rng_state` — [`L167`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L167)
  - <a id="_ReplayStateSnapshot.gradients"></a>`gradients` — [`L171`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L171)
  - <a id="_ReplayStateSnapshot.python_rng_state"></a>`python_rng_state` — [`L166`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L166)
  - <a id="_ReplayStateSnapshot.scalar_values"></a>`scalar_values` — [`L169`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L169)
- uses (calls/refs, reference-scoped): [`_BufferSnapshot`](sdc_replayer.md#_BufferSnapshot), [`_GradientSnapshot`](sdc_replayer.md#_GradientSnapshot)
- used by: [`capture`](sdc_replayer.md#_ReplayStateProvider.capture), [`restore`](sdc_replayer.md#_ReplayStateProvider.restore)

## Functions
- <a id="_accelerator_rng_states"></a>`_accelerator_rng_states(device: torch.device)` — [`L140`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L140)
- <a id="_clone_tensor"></a>`_clone_tensor(tensor: torch.Tensor)` — [`L136`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L136)
- <a id="_compare_signature"></a>`_compare_signature(reference: _ReplaySignature, candidate: _ReplaySignature)` — [`L276`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L276) — documented in [observability](../../../concepts/observability.md)
- <a id="_find_signature_mismatch"></a>`_find_signature_mismatch(reference: _ReplaySignature, candidate: _ReplaySignature)` — [`L296`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L296) — documented in [observability](../../../concepts/observability.md)
- <a id="_hash_tensor"></a>`_hash_tensor(tensor: torch.Tensor)` — [`L119`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L119) — Return a lightweight device-side digest for replay comparison.
- <a id="_local_tensor"></a>`_local_tensor(tensor: torch.Tensor)` — [`L115`](../../../../../../raw/code/torchtitan/torchtitan/observability/sdc_replayer.py#L115)

