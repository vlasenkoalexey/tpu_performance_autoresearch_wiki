---
title: 'Module: torchtitan/experiments/rl/actors/rollout_worker.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/actors/rollout_worker.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.actors.rollout_worker`/RolloutWorkerActor#
symbols:
  RolloutWorkerActor.setup_async: setup_async().
  RolloutWorkerActor.run_group: run_group().
  RolloutWorkerActor._worker: _worker.
  RolloutWorkerActor.__init__: __init__().
  RolloutWorkerActor: ''
  RolloutWorkerActor.sync_log_step: sync_log_step().
---
# Module: [`torchtitan/experiments/rl/actors/rollout_worker.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/rollout_worker.py)

## Classes
### <a id="RolloutWorkerActor"></a>`RolloutWorkerActor`
- def: [`torchtitan/experiments/rl/actors/rollout_worker.py:22`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/rollout_worker.py#L22)
- doc: Hosts a rollout worker in one CPU process.
- signature: `class RolloutWorkerActor(Actor):`
- members:
  - <a id="RolloutWorkerActor.run_group"></a>`run_group(self, *, generate_fn: Any, sample: object, group_id: int, group_size: int, sampling: Any)` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/rollout_worker.py#L51)
  - <a id="RolloutWorkerActor.setup_async"></a>`setup_async(self, *, tokenizer_config: HuggingFaceTokenizer.Config, renderer_config: RendererConfig, hf_assets_path: str)` — [`L37`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/rollout_worker.py#L37)
  - <a id="RolloutWorkerActor.sync_log_step"></a>`sync_log_step(self, step: int)` — [`L69`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/rollout_worker.py#L69)
- protocol/private: <a id="RolloutWorkerActor.__init__"></a>`__init__`[`L25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/rollout_worker.py#L25), <a id="RolloutWorkerActor._worker"></a>`_worker`[`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/rollout_worker.py#L34)
- uses (calls/refs, reference-scoped): [`build`](../../../config/configurable.md#Configurable.Config.build), [`HuggingFaceTokenizer`](../../../components/tokenizer.md#HuggingFaceTokenizer), [`RolloutGroup`](../rollout/types.md#RolloutGroup), [`run_group`](../rollout/rollouter.md#RolloutWorker.run_group), [`RolloutWorker`](../rollout/rollouter.md#RolloutWorker), [`RendererConfig`](../renderer.md#RendererConfig), [`set_step`](../../../observability/structured_logger/step_state.md#set_step), [`Config`](../../../components/tokenizer.md#HuggingFaceTokenizer.Config), [`setup_async`](../rollout/rollouter.md#RolloutWorker.setup_async), [`Config`](../rollout/rollouter.md#RolloutWorker.Config)
- used by: [`setup_async`](../rollout/rollouter.md#Rollouter.setup_async), [`run_group_rollouts`](../rollout/rollouter.md#Rollouter.run_group_rollouts), [`_worker_actors`](../rollout/rollouter.md#Rollouter._worker_actors), [`sync_log_step`](../rollout/rollouter.md#Rollouter.sync_log_step)

