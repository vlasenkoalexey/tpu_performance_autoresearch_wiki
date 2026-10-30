---
title: Verifiers integration (external rollout environments for TitanRL)
type: doc-concept
provenance: doc
source: torchtitan/experiments/rl/examples/verifiers/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Verifiers integration (external rollout environments for TitanRL)

## Definition
An optional bridge that lets the external Verifiers library (pinned to 0.3.1, `verifiers.v1` API) run the environment, agent/tool loop, runtime and task reward, while TitanRL keeps everything on the training side: sample loading, rollout-group scheduling, generation routing, policy-version tracking, advantages and policy training. An adapter converts samples and traces between the two. Other TitanRL recipes do not import Verifiers.

## In torchtitan (grounded)
- Data: [`VerifiersTaskDataset`](../catalog/torchtitan/experiments/rl/examples/verifiers/components/data.md#VerifiersTaskDataset) loads a Verifiers taskset in the controller and turns typed task data into plain dicts ([`VerifiersTaskSample`](../catalog/torchtitan/experiments/rl/examples/verifiers/components/data.md#VerifiersTaskSample)) for msgpack-over-ZMQ transport.
- Environment server: [`VerifiersEnvServer`](../catalog/torchtitan/experiments/rl/examples/verifiers/components/env_server.md#VerifiersEnvServer) spawns and owns the Verifiers server as a separate local process on the controller host; the agent runtime is independently selectable (subprocess, Docker, or a hosted runtime).
- Generation bridge: [`GenerationServer`](../catalog/torchtitan/experiments/rl/examples/verifiers/components/generation_server.md#GenerationServer) exposes TitanRL's generate function over the HTTP token-generation protocol Verifiers expects, and keeps the policy-version span and metrics that Verifiers traces lack ([`VerifiersGenerationMetadata`](../catalog/torchtitan/experiments/rl/examples/verifiers/components/generation_server.md#VerifiersGenerationMetadata)).
- Rollouter: [`VerifiersRollouter`](../catalog/torchtitan/experiments/rl/examples/verifiers/components/rollouter.md#VerifiersRollouter) overrides [`VerifiersRollouter.run_group_rollouts`](../catalog/torchtitan/experiments/rl/examples/verifiers/components/rollouter.md#VerifiersRollouter.run_group_rollouts), converts the returned trace graph with [`VerifiersRollouter.trace_to_rollout_turns`](../catalog/torchtitan/experiments/rl/examples/verifiers/components/rollouter.md#VerifiersRollouter.trace_to_rollout_turns), and surfaces the task reward via [`RewardFromVerifiers`](../catalog/torchtitan/experiments/rl/examples/verifiers/components/rollouter.md#RewardFromVerifiers); TitanRL's rubric and advantage estimator then run normally.
- DAPO Math example: [`VerifiersMathTaskset`](../catalog/torchtitan/experiments/rl/examples/verifiers/dapo_math/data.md#VerifiersMathTaskset), [`VerifiersMathRollouter`](../catalog/torchtitan/experiments/rl/examples/verifiers/dapo_math/rollouter.md#VerifiersMathRollouter), configs [`rl_dapo_qwen3_4b_verifiers_8k`](../catalog/torchtitan/experiments/rl/examples/verifiers/dapo_math/config_registry.md#rl_dapo_qwen3_4b_verifiers_8k) and [`rl_dapo_qwen3_4b_verifiers_32k`](../catalog/torchtitan/experiments/rl/examples/verifiers/dapo_math/config_registry.md#rl_dapo_qwen3_4b_verifiers_32k) (built by [`_qwen3_4b_verifiers_config`](../catalog/torchtitan/experiments/rl/examples/verifiers/dapo_math/config_registry.md#_qwen3_4b_verifiers_config)).

## Why it matters / when it applies
- **Single source of truth:** the training dataset carries the taskset config and `VerifiersRollouter.Config` copies it into the env-server config; an experiment must not configure the taskset twice.
- Adding a task: one package per task (`data.py` with `Taskset`/`TasksetConfig`, `rollouter.py`, `config_registry.py`, `requirements.txt`), registered in `torchtitan/experiments/__init__.py`, run with `--module verifiers.<task>`.
- The DAPO Math variant keeps the reference recipe unchanged and swaps only the rollout path, using Verifiers' null harness and a local subprocess runtime - no tools or sandbox, so not for untrusted code execution.
- Performance note from the README: for CPU-heavy environments, raise the Verifiers worker-pool size first. Placing the env server in a Monarch actor would need routable ZMQ/generation addresses and actor-owned lifecycle, which the current integration does not provide.
- **TPU relevance.** None; rollout-side plumbing.

## Connections
- Code concepts: [rl-training](../concepts/rl-training.md), [data-loading](../concepts/data-loading.md)
- Module catalogs: [rl/examples/verifiers/components/rollouter](../catalog/torchtitan/experiments/rl/examples/verifiers/components/rollouter.md), [rl/examples/verifiers/components/generation_server](../catalog/torchtitan/experiments/rl/examples/verifiers/components/generation_server.md), [rl/examples/verifiers/components/env_server](../catalog/torchtitan/experiments/rl/examples/verifiers/components/env_server.md), [rl/examples/verifiers/dapo_math/config_registry](../catalog/torchtitan/experiments/rl/examples/verifiers/dapo_math/config_registry.md)
- Related doc-concepts: [rl-dapo-math-recipe](rl-dapo-math-recipe.md), [titanrl-rollouter-api](titanrl-rollouter-api.md), [titanrl-architecture](titanrl-architecture.md)

## Source
Extracted from `torchtitan/experiments/rl/examples/verifiers/README.md` and `torchtitan/experiments/rl/examples/verifiers/dapo_math/README.md` (kept in place).
