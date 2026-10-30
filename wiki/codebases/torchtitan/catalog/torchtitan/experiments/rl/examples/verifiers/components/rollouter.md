---
title: 'Module: torchtitan/experiments/rl/examples/verifiers/components/rollouter.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/verifiers/components/rollouter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.verifiers.components.rollouter`/
symbols:
  VerifiersRollouter._run_single_rollout: VerifiersRollouter#_run_single_rollout().
  VerifiersRollouter.trace_to_rollout_turns: VerifiersRollouter#trace_to_rollout_turns().
  VerifiersRollouter.run_group_rollouts: VerifiersRollouter#run_group_rollouts().
  VerifiersRollouter.setup_async: VerifiersRollouter#setup_async().
  VerifiersRollouter.Config.__post_init__: VerifiersRollouter#Config#__post_init__().
  VerifiersRollouter.rollout_status: VerifiersRollouter#rollout_status().
  VerifiersRollouter.close: VerifiersRollouter#close().
  VerifiersRollouter: VerifiersRollouter#
  VerifiersRollouter._generation_server: VerifiersRollouter#_generation_server.
  RewardFromVerifiers.__call__: RewardFromVerifiers#__call__().
  VerifiersRollouter.Config.verifiers_env_server: VerifiersRollouter#Config#verifiers_env_server.
  VerifiersRollouter._rubric: VerifiersRollouter#_rubric.
  VerifiersRollouter._advantage_estimator: VerifiersRollouter#_advantage_estimator.
  VerifiersRollouter.Config.train_dataset: VerifiersRollouter#Config#train_dataset.
  VerifiersRollouter._verifiers_env_server: VerifiersRollouter#_verifiers_env_server.
  VerifiersRollouter.Config: VerifiersRollouter#Config#
  VerifiersRollouter._verifiers_env_client: VerifiersRollouter#_verifiers_env_client.
  RewardFromVerifiers.Config: RewardFromVerifiers#Config#
  VerifiersRollouter.Config.rubric: VerifiersRollouter#Config#rubric.
  VerifiersRollouter.Config.advantage: VerifiersRollouter#Config#advantage.
  VerifiersRollouter.Config.generation_server: VerifiersRollouter#Config#generation_server.
  RewardFromVerifiers: RewardFromVerifiers#
  VerifiersRollouter.Config.validation_dataset: VerifiersRollouter#Config#validation_dataset.
  VerifiersRollouter.Config.worker: VerifiersRollouter#Config#worker.
  VerifiersRollouter.__init__: VerifiersRollouter#__init__().
  VerifiersRollouter._verifiers_train_client_config: VerifiersRollouter#_verifiers_train_client_config.
  VERIFIERS_REWARD_KEY: VERIFIERS_REWARD_KEY.
  VerifiersRollouter._verifiers_config: VerifiersRollouter#_verifiers_config.
  _trainable_token_spans: _trainable_token_spans().
  VerifiersRollouter.Config.renderer_multiplex: VerifiersRollouter#Config#renderer_multiplex.
  VerifiersRollouter.Config.connection_timeout_sec: VerifiersRollouter#Config#connection_timeout_sec.
  _local_taskset_module: _local_taskset_module().
  VerifiersRollouter.Config.worker_pool_size: VerifiersRollouter#Config#worker_pool_size.
  VerifiersRollouter.Config.num_threads_per_worker: VerifiersRollouter#Config#num_threads_per_worker.
---
# Module: [`torchtitan/experiments/rl/examples/verifiers/components/rollouter.py`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py)

## Classes
### <a id="RewardFromVerifiers"></a>`RewardFromVerifiers`  ·  implements/extends RewardFn
- def: [`torchtitan/experiments/rl/examples/verifiers/components/rollouter.py:54`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L54)
- doc: Pass through the reward that Verifiers computed during the rollout.
- signature: `class RewardFromVerifiers(RewardFn):`
- protocol/private: <a id="RewardFromVerifiers.__call__"></a>`__call__`[`L61`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L61)
- uses (calls/refs, reference-scoped): [`Rollout`](../../../rollout/types.md#Rollout), [`turns`](../../../rollout/types.md#Rollout.turns), [`RewardFn`](../../../rubrics/rubric.md#RewardFn), [`env_rewards`](../../../rollout/types.md#RolloutTurn.env_rewards)  (1 test-only)
- used by: [`RewardFn`](../../../rubrics/rubric.md#RewardFn)  (1 test-only)

### <a id="RewardFromVerifiers.Config"></a>`RewardFromVerifiers.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/verifiers/components/rollouter.py:58`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L58)
- signature: `class Config(RewardFn.Config):`
- uses (calls/refs, reference-scoped): [`RewardFn`](../../../rubrics/rubric.md#RewardFn), [`Config`](../../../rubrics/rubric.md#RewardFn.Config)
- used by: (1 test-only callers)

### <a id="VerifiersRollouter"></a>`VerifiersRollouter`  ·  implements/extends Rollouter
- def: [`torchtitan/experiments/rl/examples/verifiers/components/rollouter.py:69`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L69)
- doc: Adapt Verifiers execution to TitanRL's `Rollouter` contract.
- signature: `class VerifiersRollouter(Rollouter):`
- members:
  - <a id="VerifiersRollouter._run_single_rollout"></a>`_run_single_rollout(self, *, sample: object, sampling: SamplingConfig, group_id: int, rollout_id: int)` — [`L268`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L268) — Send one task to Verifiers and convert its trace to a rollout. — documented in [rl-training](../../../../../../../concepts/rl-training.md)
  - <a id="VerifiersRollouter.close"></a>`close(self)` — [`L213`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L213) — Close the Verifiers client, generation server, and environment server.
  - <a id="VerifiersRollouter.rollout_status"></a>`rollout_status(*, verifiers_episode: Any, trace: Any)` — [`L329`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L329)
  - <a id="VerifiersRollouter.run_group_rollouts"></a>`run_group_rollouts(self, *, generate_fn: GenerateFn, sample: object, group_id: int, group_size: int, sampling: SamplingConfig)` — [`L228`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L228) — Run sibling rollouts through Verifiers, then compute advantages.
  - <a id="VerifiersRollouter.setup_async"></a>`setup_async(self, *, tokenizer_config: HuggingFaceTokenizer.Config, renderer_config: RendererConfig, hf_assets_path: str)` — [`L162`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L162) — Start the EnvServer and connect it to TorchTitan generation.
  - <a id="VerifiersRollouter.trace_to_rollout_turns"></a>`trace_to_rollout_turns(*, trace: Any, generation_metadata: VerifiersGenerationMetadata | None, group_id: int, rollout_id: int)` — [`L339`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L339) — Flatten a Verifiers trace into TorchTitan's trainable rollout turns.
- protocol/private: <a id="VerifiersRollouter.__init__"></a>`__init__`[`L152`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L152), <a id="VerifiersRollouter._advantage_estimator"></a>`_advantage_estimator`[`L156`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L156), <a id="VerifiersRollouter._generation_server"></a>`_generation_server`[`L158`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L158), <a id="VerifiersRollouter._rubric"></a>`_rubric`[`L155`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L155), <a id="VerifiersRollouter._verifiers_config"></a>`_verifiers_config`[`L154`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L154), <a id="VerifiersRollouter._verifiers_env_client"></a>`_verifiers_env_client`[`L159`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L159), <a id="VerifiersRollouter._verifiers_env_server"></a>`_verifiers_env_server`[`L157`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L157), <a id="VerifiersRollouter._verifiers_train_client_config"></a>`_verifiers_train_client_config`[`L160`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L160)
- uses (calls/refs, reference-scoped): [`build`](../../../../../config/configurable.md#Configurable.Config.build), [`HuggingFaceTokenizer`](../../../../../components/tokenizer.md#HuggingFaceTokenizer), [`SamplingConfig`](../../../actors/generator.md#SamplingConfig), [`Rollout`](../../../rollout/types.md#Rollout), [`RolloutStatus`](../../../rollout/types.md#RolloutStatus), [`RolloutGroup`](../../../rollout/types.md#RolloutGroup), [`RenderersLibraryConfig`](../../../renderer.md#RenderersLibraryConfig), [`Rollouter`](../../../rollout/rollouter.md#Rollouter), [`turns`](../../../rollout/types.md#Rollout.turns), [`RolloutTurn`](../../../rollout/types.md#RolloutTurn), [`renderers_config`](../../../renderer.md#RenderersLibraryConfig.renderers_config), [`RolloutTurnID`](../../../types.md#RolloutTurnID), [`RendererConfig`](../../../renderer.md#RendererConfig), [`max_tokens`](../../../actors/generator.md#SamplingConfig.max_tokens), [`temperature`](../../../actors/generator.md#SamplingConfig.temperature), [`top_p`](../../../actors/generator.md#SamplingConfig.top_p), [`rollouts`](../../../rollout/types.md#RolloutGroup.rollouts), [`Rubric`](../../../rubrics/rubric.md#Rubric), [`group_id`](../../../rollout/types.md#RolloutGroup.group_id), [`completion_token_ids`](../../../rollout/types.md#RolloutTurn.completion_token_ids), [`Config`](../../../../../components/tokenizer.md#HuggingFaceTokenizer.Config), [`turn_id`](../../../types.md#RolloutTurnID.turn_id), [`group_id`](../../../types.md#RolloutTurnID.group_id), [`rollout_id`](../../../types.md#RolloutTurnID.rollout_id), [`AdvantageEstimator`](../../../rollout/advantage.md#AdvantageEstimator), [`status`](../../../rollout/types.md#Rollout.status), [`completion_message`](../../../rollout/types.md#RolloutTurn.completion_message), [`group_id`](../../../rollout/types.md#Rollout.group_id), [`prompt_token_ids`](../../../rollout/types.md#RolloutTurn.prompt_token_ids), [`rollout_id`](../../../rollout/types.md#Rollout.rollout_id), [`completion_logprobs`](../../../rollout/types.md#RolloutTurn.completion_logprobs), [`rollout_id`](../../../rollout/types.md#RolloutTurn.rollout_id), [`GenerateFn`](../../../rollout/types.md#GenerateFn), [`score_group`](../../../rubrics/rubric.md#Rubric.score_group), [`min_policy_version`](../../../rollout/types.md#RolloutTurn.min_policy_version), [`COMPLETED`](../../../rollout/types.md#RolloutStatus.COMPLETED), [`seed`](../../../actors/generator.md#SamplingConfig.seed), [`max_policy_version`](../../../rollout/types.md#RolloutTurn.max_policy_version), [`advantage`](../../../rollout/types.md#Rollout.advantage), [`metrics`](../../../rollout/types.md#RolloutTurn.metrics)  (+7 more; 21 test-only)
- used by: [`Rollouter`](../../../rollout/rollouter.md#Rollouter), [`setup_async`](../../../rollout/rollouter.md#Rollouter.setup_async), [`run_group_rollouts`](../../../rollout/rollouter.md#Rollouter.run_group_rollouts), [`close`](../../../rollout/rollouter.md#Rollouter.close)  (4 test-only)

### <a id="VerifiersRollouter.Config"></a>`VerifiersRollouter.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/verifiers/components/rollouter.py:84`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L84)
- signature: `class Config(Rollouter.Config):`
- members:
  - <a id="VerifiersRollouter.Config.advantage"></a>`advantage` — [`L106`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L106) — ---
  - <a id="VerifiersRollouter.Config.connection_timeout_sec"></a>`connection_timeout_sec` — [`L123`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L123) — ---
  - <a id="VerifiersRollouter.Config.generation_server"></a>`generation_server` — [`L111`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L111) — ---
  - <a id="VerifiersRollouter.Config.num_threads_per_worker"></a>`num_threads_per_worker` — [`L97`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L97) — ---
  - <a id="VerifiersRollouter.Config.renderer_multiplex"></a>`renderer_multiplex` — [`L116`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L116) — ---
  - <a id="VerifiersRollouter.Config.rubric"></a>`rubric` — [`L103`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L103) — ---
  - <a id="VerifiersRollouter.Config.train_dataset"></a>`train_dataset` — [`L85`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L85) — ---
  - <a id="VerifiersRollouter.Config.validation_dataset"></a>`validation_dataset` — [`L88`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L88) — ---
  - <a id="VerifiersRollouter.Config.verifiers_env_server"></a>`verifiers_env_server` — [`L100`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L100) — ---
  - <a id="VerifiersRollouter.Config.worker"></a>`worker` — [`L91`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L91) — ---
  - <a id="VerifiersRollouter.Config.worker_pool_size"></a>`worker_pool_size` — [`L94`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L94) — ---
- protocol/private: <a id="VerifiersRollouter.Config.__post_init__"></a>`__post_init__`[`L126`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L126)
- uses (calls/refs, reference-scoped): [`Rollouter`](../../../rollout/rollouter.md#Rollouter), [`RolloutWorker`](../../../rollout/rollouter.md#RolloutWorker), [`Rubric`](../../../rubrics/rubric.md#Rubric), [`AdvantageEstimator`](../../../rollout/advantage.md#AdvantageEstimator), [`Config`](../../../rubrics/rubric.md#Rubric.Config), [`Config`](../../../rollout/advantage.md#AdvantageEstimator.Config), [`Config`](../../../rollout/rollouter.md#RolloutWorker.Config), [`Config`](../../../rollout/rollouter.md#Rollouter.Config), [`__post_init__`](../../../rollout/rollouter.md#Rollouter.Config.__post_init__)  (9 test-only)
- used by: (6 test-only callers)

## Functions
- <a id="_local_taskset_module"></a>`_local_taskset_module(taskset: VerifiersTasksetConfig)` — [`L424`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L424) — Return the module backing a locally registered taskset alias.
- <a id="_trainable_token_spans"></a>`_trainable_token_spans(mask: list[bool])` — [`L411`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L411) — Return half-open token spans marked trainable by a Verifiers node mask.

## Module values
- <a id="VERIFIERS_REWARD_KEY"></a>`VERIFIERS_REWARD_KEY` — [`L51`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/rollouter.py#L51)

