---
title: TitanRL experiment API (Rollouter, MessageEnv, Rubric, config registry)
type: doc-concept
provenance: doc
source: torchtitan/experiments/rl/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# TitanRL experiment API (Rollouter, MessageEnv, Rubric, config registry)

## Definition
A TitanRL experiment is defined by four pieces: training/validation **datasets**, a **`MessageEnv`** (interaction, tools, termination), a **rubric** (per-rollout or group reward), and a **`Rollouter`** that composes them. The default path then handles rollout, scoring, batching, training and weight sync; the experiment is wired into a `config_registry` function returning a `Controller.Config` and launched with `python -m torchtitan.experiments.rl.train --module <pkg> --config <fn>`, CLI flags overriding registry fields.

## In torchtitan (grounded)
- [`Rollouter`](../catalog/torchtitan/experiments/rl/rollout/rollouter.md#Rollouter): [`Rollouter.get_training_sample`](../catalog/torchtitan/experiments/rl/rollout/rollouter.md#Rollouter.get_training_sample) and [`Rollouter.run_group_rollouts`](../catalog/torchtitan/experiments/rl/rollout/rollouter.md#Rollouter.run_group_rollouts) are what the controller calls; its config carries `train_dataset`, `validation_dataset` and a `worker` ([`Rollouter.Config.worker`](../catalog/torchtitan/experiments/rl/rollout/rollouter.md#Rollouter.Config.worker), pool size [`Rollouter.Config.worker_pool_size`](../catalog/torchtitan/experiments/rl/rollout/rollouter.md#Rollouter.Config.worker_pool_size)).
- [`RolloutWorker`](../catalog/torchtitan/experiments/rl/rollout/rollouter.md#RolloutWorker) owns the per-rollout pieces: [`RolloutWorker.Config.message_env`](../catalog/torchtitan/experiments/rl/rollout/rollouter.md#RolloutWorker.Config.message_env), [`RolloutWorker.Config.rubric`](../catalog/torchtitan/experiments/rl/rollout/rollouter.md#RolloutWorker.Config.rubric), [`RolloutWorker.Config.token_env`](../catalog/torchtitan/experiments/rl/rollout/rollouter.md#RolloutWorker.Config.token_env), and the hooks [`RolloutWorker.run_group`](../catalog/torchtitan/experiments/rl/rollout/rollouter.md#RolloutWorker.run_group), [`RolloutWorker._run_single_rollout`](../catalog/torchtitan/experiments/rl/rollout/rollouter.md#RolloutWorker._run_single_rollout), [`RolloutWorker.score_group`](../catalog/torchtitan/experiments/rl/rollout/rollouter.md#RolloutWorker.score_group). Workers run as [`RolloutWorkerActor`](../catalog/torchtitan/experiments/rl/actors/rollout_worker.md#RolloutWorkerActor).
- Environments: [`MessageEnv`](../catalog/torchtitan/experiments/rl/environment/message.md#MessageEnv) (messages), wrapped by [`TokenEnv`](../catalog/torchtitan/experiments/rl/environment/token.md#TokenEnv) (message <-> token plumbing, turn and token budgets).
- Rewards: [`Rubric`](../catalog/torchtitan/experiments/rl/rubrics/rubric.md#Rubric) of weighted [`RewardFn`](../catalog/torchtitan/experiments/rl/rubrics/rubric.md#RewardFn)s; losses such as [`GRPOLoss`](../catalog/torchtitan/experiments/rl/losses/grpo.md#GRPOLoss) / [`DAPOLoss`](../catalog/torchtitan/experiments/rl/losses/dapo.md#DAPOLoss).
- Prompt rendering: [`RenderersLibraryConfig`](../catalog/torchtitan/experiments/rl/renderer.md#RenderersLibraryConfig) (e.g. a Qwen3 renderer with `enable_thinking`).
- Registration: the module name must be added to [`_supported_experiments`](../catalog/torchtitan/experiments/__init__.md#_supported_experiments); [`ConfigManager`](../catalog/torchtitan/config/manager.md#ConfigManager) also searches `torchtitan.experiments.rl.examples.<module>.config_registry`.

## Why it matters / when it applies
- Customization levels: replace the sample source (dataset config or `get_training_sample`), replace group orchestration wholesale (override `run_group_rollouts`, as the Verifiers bridge does), or keep the stock orchestration and customize the worker.
- Reference experiments: DAPO Math ([rl-dapo-math-recipe](rl-dapo-math-recipe.md)), Search-R1 multi-turn tool use ([rl-search-r1-multiturn-tool-use](rl-search-r1-multiturn-tool-use.md)), Verifiers-managed rollouts ([rl-verifiers-integration](rl-verifiers-integration.md)); the alphabet_sort example hosts the batch-invariant configs.
- **TPU relevance.** Not TPU-facing; included because the `Controller.Config` composition (model spec + trainer parallelism + generator parallelism) is where RL performance knobs live.

**Doc vs code at this commit:** the README's `MyRollouter` sketch puts `message_env` and `rubric` directly on `Rollouter.Config` and shows `_run_single_rollout` as a `Rollouter` method. In code those fields live on `RolloutWorker.Config` (nested under `Rollouter.Config.worker`) and `_run_single_rollout` is a `RolloutWorker` method; the docstring example on `Rollouter` shows the current shape.

## Connections
- Code concepts: [rl-training](../concepts/rl-training.md), [job-config](../concepts/job-config.md), [config-overrides](../concepts/config-overrides.md), [data-loading](../concepts/data-loading.md)
- Module catalogs: [rl/rollout/rollouter](../catalog/torchtitan/experiments/rl/rollout/rollouter.md), [rl/environment/message](../catalog/torchtitan/experiments/rl/environment/message.md), [rl/environment/token](../catalog/torchtitan/experiments/rl/environment/token.md), [rl/rubrics/rubric](../catalog/torchtitan/experiments/rl/rubrics/rubric.md)
- Related doc-concepts: [titanrl-architecture](titanrl-architecture.md), [rl-dapo-math-recipe](rl-dapo-math-recipe.md), [rl-search-r1-multiturn-tool-use](rl-search-r1-multiturn-tool-use.md), [rl-verifiers-integration](rl-verifiers-integration.md)

## Source
Extracted from `torchtitan/experiments/rl/README.md` (kept in place).
