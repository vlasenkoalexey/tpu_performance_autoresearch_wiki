---
title: 'Module: torchtitan/experiments/rl/rollout/rollouter.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/rollout/rollouter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.rollout.rollouter`/
symbols:
  RolloutWorker._run_single_rollout: RolloutWorker#_run_single_rollout().
  RolloutWorker.run_group: RolloutWorker#run_group().
  Rollouter: Rollouter#
  Rollouter.setup_async: Rollouter#setup_async().
  RolloutWorker: RolloutWorker#
  Rollouter.run_group_rollouts: Rollouter#run_group_rollouts().
  RolloutWorker.setup_async: RolloutWorker#setup_async().
  RolloutWorker.make_env_group: RolloutWorker#make_env_group().
  RolloutWorker.score_group: RolloutWorker#score_group().
  RolloutWorker.Config.advantage: RolloutWorker#Config#advantage.
  Rollouter.Config: Rollouter#Config#
  RolloutWorker.Config: RolloutWorker#Config#
  Rollouter._worker_actors: Rollouter#_worker_actors.
  Rollouter.close: Rollouter#close().
  RolloutWorker.rubric: RolloutWorker#rubric.
  RolloutWorker.advantage_estimator: RolloutWorker#advantage_estimator.
  Rollouter.Config.train_dataset: Rollouter#Config#train_dataset.
  Rollouter.Config.validation_dataset: Rollouter#Config#validation_dataset.
  Rollouter.Config.worker: Rollouter#Config#worker.
  Rollouter.Config.__post_init__: Rollouter#Config#__post_init__().
  Rollouter._train_dataset: Rollouter#_train_dataset.
  Rollouter._validation_dataset: Rollouter#_validation_dataset.
  Rollouter._worker_mesh: Rollouter#_worker_mesh.
  Rollouter.sync_log_step: Rollouter#sync_log_step().
  RolloutWorker.Config.rubric: RolloutWorker#Config#rubric.
  RolloutWorker.Config.message_env: RolloutWorker#Config#message_env.
  RolloutWorker.Config.token_env: RolloutWorker#Config#token_env.
  Rollouter.get_training_sample: Rollouter#get_training_sample().
  Rollouter._config: Rollouter#_config.
  Rollouter.__init__: Rollouter#__init__().
  Rollouter.get_validation_sample: Rollouter#get_validation_sample().
  RolloutWorker.__init__: RolloutWorker#__init__().
  RolloutWorker._message_env_config: RolloutWorker#_message_env_config.
  RolloutWorker._token_env_config: RolloutWorker#_token_env_config.
  Rollouter.Config.worker_pool_size: Rollouter#Config#worker_pool_size.
  Rollouter.Config.num_threads_per_worker: Rollouter#Config#num_threads_per_worker.
  RolloutWorker._renderer: RolloutWorker#_renderer.
  logger: logger.
---
# Module: [`torchtitan/experiments/rl/rollout/rollouter.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py)

## Classes
### <a id="RolloutWorker"></a>`RolloutWorker`
- def: [`torchtitan/experiments/rl/rollout/rollouter.py:217`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L217)
- members:
  - <a id="RolloutWorker._run_single_rollout"></a>`_run_single_rollout(self, *, generate_fn: GenerateFn, env: TokenEnv, sampling: SamplingConfig, group_id: int, rollout_id: int)` — [`L370`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L370) — Produce a single rollout, alternating between env and generator calls, — documented in [rl-training](../../../../../concepts/rl-training.md)
  - <a id="RolloutWorker.make_env_group"></a>`make_env_group(self, *, sample: object, group_size: int)` — [`L255`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L255) — Construct `group_size` single-use envs from one dataset sample.
  - <a id="RolloutWorker.run_group"></a>`run_group(self, *, generate_fn: GenerateFn, sample: object, group_id: int, group_size: int, sampling: SamplingConfig)` — [`L298`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L298) — Roll out and score one prompt group.
  - <a id="RolloutWorker.score_group"></a>`score_group(self, rollouts: list[Rollout], env_input: object)` — [`L278`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L278) — Score one group's rollouts; `run_group` applies the rewards.
  - <a id="RolloutWorker.setup_async"></a>`setup_async(self, *, tokenizer_config: HuggingFaceTokenizer.Config, renderer_config: RendererConfig, hf_assets_path: str)` — [`L244`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L244) — Build runtime dependencies after the worker actor is spawned.
  - <a id="RolloutWorker.advantage_estimator"></a>`advantage_estimator` — [`L241`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L241)
  - <a id="RolloutWorker.rubric"></a>`rubric` — [`L238`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L238)
- protocol/private: <a id="RolloutWorker.__init__"></a>`__init__`[`L237`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L237), <a id="RolloutWorker._message_env_config"></a>`_message_env_config`[`L239`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L239), <a id="RolloutWorker._renderer"></a>`_renderer`[`L242`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L242), <a id="RolloutWorker._token_env_config"></a>`_token_env_config`[`L240`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L240)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`build`](../../../config/configurable.md#Configurable.Config.build), [`step`](../environment/token.md#TokenEnv.step), [`HuggingFaceTokenizer`](../../../components/tokenizer.md#HuggingFaceTokenizer), [`SamplingConfig`](../actors/generator.md#SamplingConfig), [`Rollout`](types.md#Rollout), [`RolloutStatus`](types.md#RolloutStatus), [`init`](../environment/token.md#TokenEnv.init), [`RolloutGroup`](types.md#RolloutGroup), [`turns`](types.md#Rollout.turns), [`RolloutTurn`](types.md#RolloutTurn), [`RolloutTurnID`](../types.md#RolloutTurnID), [`RendererConfig`](../renderer.md#RendererConfig), [`rollouts`](types.md#RolloutGroup.rollouts), [`Rubric`](../rubrics/rubric.md#Rubric), [`group_id`](types.md#RolloutGroup.group_id), [`completion_token_ids`](types.md#RolloutTurn.completion_token_ids), [`TokenEnv`](../environment/token.md#TokenEnv), [`Config`](../../../components/tokenizer.md#HuggingFaceTokenizer.Config), [`turn_id`](../types.md#RolloutTurnID.turn_id), [`group_id`](../types.md#RolloutTurnID.group_id), [`rollout_id`](../types.md#RolloutTurnID.rollout_id), [`AdvantageEstimator`](advantage.md#AdvantageEstimator), [`status`](types.md#Rollout.status), [`status`](../environment/token.md#TokenEnvOutput.status), [`completion_message`](types.md#RolloutTurn.completion_message), [`group_id`](types.md#Rollout.group_id), [`prompt_token_ids`](types.md#RolloutTurn.prompt_token_ids), [`advantage`](rollouter.md#RolloutWorker.Config.advantage), [`rollout_id`](types.md#Rollout.rollout_id), [`completion_logprobs`](types.md#RolloutTurn.completion_logprobs), [`next_prompt_token_ids`](../environment/token.md#TokenEnvOutput.next_prompt_token_ids), [`rollout_id`](types.md#RolloutTurn.rollout_id), [`Config`](rollouter.md#RolloutWorker.Config), [`GenerateFn`](types.md#GenerateFn), [`score_group`](../rubrics/rubric.md#Rubric.score_group), [`token_ids`](../types.md#Completion.token_ids), [`to_string`](../types.md#RolloutTurnID.to_string), [`next_prompt_messages`](../environment/token.md#TokenEnvOutput.next_prompt_messages), [`RubricOutput`](../rubrics/rubric.md#RubricOutput)  (+25 more; 6 test-only)
- used by: [`setup_async`](../actors/rollout_worker.md#RolloutWorkerActor.setup_async), [`run_group`](../actors/rollout_worker.md#RolloutWorkerActor.run_group), [`_worker`](../actors/rollout_worker.md#RolloutWorkerActor._worker), [`worker`](rollouter.md#Rollouter.Config.worker), [`__init__`](../actors/rollout_worker.md#RolloutWorkerActor.__init__)  (13 test-only)

### <a id="RolloutWorker.Config"></a>`RolloutWorker.Config`
- def: [`torchtitan/experiments/rl/rollout/rollouter.py:221`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L221)
- members:
  - <a id="RolloutWorker.Config.advantage"></a>`advantage` — [`L231`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L231) — ---
  - <a id="RolloutWorker.Config.message_env"></a>`message_env` — [`L225`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L225) — ---
  - <a id="RolloutWorker.Config.rubric"></a>`rubric` — [`L222`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L222) — ---
  - <a id="RolloutWorker.Config.token_env"></a>`token_env` — [`L228`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L228) — ---
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Config`](../../../config/configurable.md#Configurable.Config), [`MessageEnv`](../environment/message.md#MessageEnv), [`Rubric`](../rubrics/rubric.md#Rubric), [`TokenEnv`](../environment/token.md#TokenEnv), [`AdvantageEstimator`](advantage.md#AdvantageEstimator), [`Config`](../rubrics/rubric.md#Rubric.Config), [`Config`](../environment/token.md#TokenEnv.Config), [`Config`](advantage.md#AdvantageEstimator.Config), [`Config`](../environment/message.md#MessageEnv.Config)
- used by: [`advantage_estimator`](rollouter.md#RolloutWorker.advantage_estimator), [`rubric`](rollouter.md#RolloutWorker.rubric), [`worker`](rollouter.md#Rollouter.Config.worker), [`__init__`](../actors/rollout_worker.md#RolloutWorkerActor.__init__), [`__init__`](rollouter.md#RolloutWorker.__init__), [`_message_env_config`](rollouter.md#RolloutWorker._message_env_config), [`_token_env_config`](rollouter.md#RolloutWorker._token_env_config)  (7 test-only)

### <a id="Rollouter"></a>`Rollouter`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/rollout/rollouter.py:43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L43)
- doc: Turns a problem (train/val datasets, the `MessageEnv` to build per sample, and a
- signature: `class Rollouter(Configurable):`
- members:
  - <a id="Rollouter.close"></a>`close(self)` — [`L165`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L165) — Stop the owned rollout worker proc mesh.
  - <a id="Rollouter.get_training_sample"></a>`get_training_sample(self)` — [`L128`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L128) — Get one training sample (the env input) from the training dataset.
  - <a id="Rollouter.get_validation_sample"></a>`get_validation_sample(self)` — [`L132`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L132) — Get one validation sample (the env input) from the validation dataset.
  - <a id="Rollouter.run_group_rollouts"></a>`run_group_rollouts(self, *, generate_fn: GenerateFn, sample: object, group_id: int, group_size: int, sampling: SamplingConfig)` — [`L178`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L178) — Roll out and score one prompt group.
  - <a id="Rollouter.setup_async"></a>`setup_async(self, *, tokenizer_config: HuggingFaceTokenizer.Config, renderer_config: RendererConfig, hf_assets_path: str)` — [`L136`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L136) — Spawn and initialize the owned worker proc mesh and actor pool.
  - <a id="Rollouter.sync_log_step"></a>`sync_log_step(self, step: int)` — [`L173`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L173) — Propagate the controller log step to every rollout worker.
- protocol/private: <a id="Rollouter.__init__"></a>`__init__`[`L119`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L119), <a id="Rollouter._config"></a>`_config`[`L120`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L120), <a id="Rollouter._train_dataset"></a>`_train_dataset`[`L121`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L121), <a id="Rollouter._validation_dataset"></a>`_validation_dataset`[`L122`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L122), <a id="Rollouter._worker_actors"></a>`_worker_actors`[`L124`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L124), <a id="Rollouter._worker_mesh"></a>`_worker_mesh`[`L125`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L125)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`build`](../../../config/configurable.md#Configurable.Config.build), [`HuggingFaceTokenizer`](../../../components/tokenizer.md#HuggingFaceTokenizer), [`SamplingConfig`](../actors/generator.md#SamplingConfig), [`RolloutGroup`](types.md#RolloutGroup), [`RendererConfig`](../renderer.md#RendererConfig), [`Config`](../../../components/tokenizer.md#HuggingFaceTokenizer.Config), [`Config`](rollouter.md#Rollouter.Config), [`GenerateFn`](types.md#GenerateFn), [`run_group`](../actors/rollout_worker.md#RolloutWorkerActor.run_group), [`train_dataset`](rollouter.md#Rollouter.Config.train_dataset), [`validation_dataset`](rollouter.md#Rollouter.Config.validation_dataset), [`worker`](rollouter.md#Rollouter.Config.worker), [`RolloutWorkerActor`](../actors/rollout_worker.md#RolloutWorkerActor), [`sync_log_step`](../actors/rollout_worker.md#RolloutWorkerActor.sync_log_step), [`num_threads_per_worker`](rollouter.md#Rollouter.Config.num_threads_per_worker), [`worker_pool_size`](rollouter.md#Rollouter.Config.worker_pool_size)  (7 test-only)
- used by: [`Configurable`](../../../config/configurable.md#Configurable), [`_trainer_loop`](../controller.md#Controller._trainer_loop), [`trainer_dp_degree`](../controller.md#Controller.trainer_dp_degree), [`_rollout_loop`](../controller.md#Controller._rollout_loop), [`close`](../controller.md#Controller.close), [`_collect_validation_rollouts`](../controller.md#Controller._collect_validation_rollouts), [`_data_input_loop`](../controller.md#Controller._data_input_loop), [`rollouter`](../controller.md#Controller.Config.rollouter), [`_rollouter`](../controller.md#Controller._rollouter)  (15 test-only)

### <a id="Rollouter.Config"></a>`Rollouter.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/rollout/rollouter.py:89`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L89)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="Rollouter.Config.num_threads_per_worker"></a>`num_threads_per_worker` — [`L103`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L103) — ---
  - <a id="Rollouter.Config.train_dataset"></a>`train_dataset` — [`L90`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L90) — ---
  - <a id="Rollouter.Config.validation_dataset"></a>`validation_dataset` — [`L93`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L93) — ---
  - <a id="Rollouter.Config.worker"></a>`worker` — [`L96`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L96) — ---
  - <a id="Rollouter.Config.worker_pool_size"></a>`worker_pool_size` — [`L100`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L100) — ---
- protocol/private: <a id="Rollouter.Config.__post_init__"></a>`__post_init__`[`L107`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L107)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Config`](../../../config/configurable.md#Configurable.Config), [`RolloutWorker`](rollouter.md#RolloutWorker), [`Config`](rollouter.md#RolloutWorker.Config)
- used by: [`setup_async`](rollouter.md#Rollouter.setup_async), [`rollouter`](../controller.md#Controller.Config.rollouter), [`_train_dataset`](rollouter.md#Rollouter._train_dataset), [`_validation_dataset`](rollouter.md#Rollouter._validation_dataset), [`__init__`](rollouter.md#Rollouter.__init__)  (5 test-only)

## Module values
- <a id="logger"></a>`logger` — [`L40`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/rollouter.py#L40)

